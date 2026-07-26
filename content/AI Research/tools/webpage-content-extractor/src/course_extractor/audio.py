"""Duration-based matching of local audio files to audio placeholders,
plus optional local transcription via faster-whisper.

The saved "Webpage, Complete" page references transcoded audio under
``assets/`` that the browser usually does NOT download. The real audio is
supplied as separate files whose names do not line up with the placeholders,
so we link them by *duration* instead (the only reliable signal available
offline).
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .asset_resolver import attach_local_file
from .config import Config
from .models import AssetIR, AssetKind, DocumentIR
from .util import logging as log

AUDIO_EXTS = {".mp3", ".m4a", ".wav", ".ogg", ".oga", ".aac", ".flac", ".opus"}


@dataclass
class LocalAudio:
    path: Path
    duration: float


def probe_duration(path: Path, ffprobe: str | None) -> float | None:
    if not ffprobe:
        return None
    try:
        out = subprocess.run(
            [
                ffprobe, "-v", "error", "-show_entries", "format=duration",
                "-of", "json", str(path),
            ],
            capture_output=True, text=True, timeout=60, check=True,
        )
        data = json.loads(out.stdout)
        return float(data["format"]["duration"])
    except Exception as exc:  # noqa: BLE001
        log.debug("ffprobe failed for {}: {}", path.name, exc)
        return None


def discover_local_audio(search_dirs: list[Path], ffprobe: str | None) -> list[LocalAudio]:
    found: dict[Path, LocalAudio] = {}
    for d in search_dirs:
        if not d.exists():
            continue
        for path in sorted(d.rglob("*")):
            if path.suffix.lower() in AUDIO_EXTS and path.is_file():
                resolved = path.resolve()
                if resolved in found:
                    continue
                dur = probe_duration(path, ffprobe)
                if dur is not None:
                    found[resolved] = LocalAudio(path=path, duration=dur)
    return list(found.values())


def match_audio_by_duration(doc: DocumentIR, pool: list[LocalAudio], tolerance: float) -> None:
    """Greedy nearest-duration matching; each file is used at most once."""
    audios = list(doc.iter_audio())
    remaining = list(pool)
    # Build all (delta, audio_idx, file_idx) candidates, sort by closeness.
    candidates = []
    for ai, a in enumerate(audios):
        if a.duration_seconds is None:
            continue
        for fi, f in enumerate(remaining):
            delta = abs(f.duration - a.duration_seconds)
            if delta <= tolerance:
                candidates.append((delta, ai, fi))
    candidates.sort(key=lambda t: t[0])

    taken_audio: set[int] = set()
    taken_file: set[int] = set()
    for delta, ai, fi in candidates:
        if ai in taken_audio or fi in taken_file:
            continue
        taken_audio.add(ai)
        taken_file.add(fi)
        a = audios[ai]
        f = remaining[fi]
        asset = AssetIR(kind=AssetKind.AUDIO)
        attach_local_file(asset, f.path)
        asset.matched_by = f"duration(|{delta:.3f}s|)"
        a.asset = asset
        log.debug(
            "matched audio #{} ({:.2f}s) -> {} ({:.2f}s)",
            a.placeholder_index, a.duration_seconds or 0, f.path.name, f.duration,
        )

    matched = len(taken_audio)
    log.info("Audio: {}/{} placeholders matched to local files", matched, len(audios))
    for a in audios:
        if a.asset is None:
            doc.add_warning(
                "audio_missing",
                f"no local audio within {tolerance}s of placeholder #{a.placeholder_index} "
                f"({a.duration_label or a.duration_seconds}s)",
            )


# --------------------------------------------------------------------------- #
# Transcription
# --------------------------------------------------------------------------- #
class Transcriber:
    def __init__(self, model_name: str, language: str | None):
        self.model_name = model_name
        self.language = language
        self._model = None
        self._ok = None

    def _ensure(self) -> bool:
        if self._ok is not None:
            return self._ok
        try:
            from faster_whisper import WhisperModel

            log.info("Loading transcription model '{}' (first run may download)...", self.model_name)
            self._model = WhisperModel(self.model_name, device="cpu", compute_type="int8")
            self._ok = True
        except Exception as exc:  # noqa: BLE001
            log.warn("transcription unavailable ({}); leaving placeholders", exc)
            self._ok = False
        return self._ok

    def transcribe(self, path: Path) -> str | None:
        if not self._ensure():
            return None
        try:
            segments, _info = self._model.transcribe(
                str(path), language=self.language, vad_filter=True, beam_size=5
            )
            text = " ".join(seg.text.strip() for seg in segments).strip()
            return text or None
        except Exception as exc:  # noqa: BLE001
            log.warn("transcription failed for {}: {}", path.name, exc)
            return None


def transcribe_matched_audio(doc: DocumentIR, config: Config) -> None:
    to_do = [a for a in doc.iter_audio() if a.asset and a.asset.source_path]
    if not to_do:
        return
    transcriber = Transcriber(config.whisper_model, config.whisper_language)
    for a in to_do:
        log.info("Transcribing placeholder #{} ({})...", a.placeholder_index, a.asset.source_path.name)
        text = transcriber.transcribe(a.asset.source_path)
        if text:
            a.transcript = text
            a.transcript_source = f"faster-whisper:{config.whisper_model}"
        else:
            doc.add_warning(
                "transcribe_failed",
                f"could not transcribe audio placeholder #{a.placeholder_index}",
            )
