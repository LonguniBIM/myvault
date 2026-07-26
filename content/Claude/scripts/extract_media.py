"""
Extract transcripts from video/audio files in raw/ and ingest into the wiki.

Pipeline:
  1. Scan raw/ for new video/audio files (not yet transcribed)
  2. Transcribe each via faster-whisper (local, no cloud)
  3. Save transcript to raw/transcripts/<slug>.md
  4. Create wiki source page at wiki/sources/<slug>.md
  5. Update wiki/index.md and wiki/log.md

Usage:
  python scripts/extract_media.py                    # scan raw/ with default settings
  python scripts/extract_media.py --model medium      # better accuracy for technical content
  python scripts/extract_media.py --url <youtube-url> # download + transcribe YouTube video
  python scripts/extract_media.py --dry-run           # preview what would be processed
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

# ── Constants ──────────────────────────────────────────────────────────────────

DEBUG_ENABLED = False

WORKSPACE = Path(__file__).resolve().parent.parent
RAW_DIR = WORKSPACE / "raw"
RAW_VIDEO_DIR = RAW_DIR / "video"
TRANSCRIPTS_DIR = RAW_DIR / "transcripts"
WIKI_DIR = WORKSPACE / "wiki"
WIKI_SOURCES_DIR = WIKI_DIR / "sources"
WIKI_INDEX = WIKI_DIR / "index.md"
WIKI_LOG = WIKI_DIR / "log.md"
MANIFEST_PATH = WORKSPACE / "scripts" / ".media_manifest.json"

VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}
AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".ogg", ".flac"}
ALL_MEDIA_EXTENSIONS = VIDEO_EXTENSIONS | AUDIO_EXTENSIONS

DEFAULT_WHISPER_MODEL = "base"
DEFAULT_LANGUAGE = None  # auto-detect


def slugify(text: str) -> str:
    """Convert text to kebab-case slug safe for filenames."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:120]


def file_sha256(filepath: Path) -> str:
    """Compute SHA256 hash of a file for change detection."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest() -> dict:
    """Load processed files manifest (tracks what's already transcribed)."""
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"processed": {}}


def save_manifest(manifest: dict) -> None:
    """Save manifest to disk."""
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


def scan_media_files(base_dir: Path) -> list[Path]:
    """Recursively find all video/audio files under base_dir.

    Audio that belongs to a saved "Webpage, Complete" lesson is skipped — it is
    transcribed in-place by ``ingest_lesson.py`` (matched to the lesson's audio
    placeholders by duration), not as a standalone media page.
    """
    from lesson_utils import in_lesson_scope

    results = []
    for root, _dirs, files in os.walk(base_dir):
        for fname in sorted(files):
            fpath = Path(root) / fname
            if fpath.suffix.lower() in ALL_MEDIA_EXTENSIONS and not in_lesson_scope(fpath):
                results.append(fpath)
    return results


def get_new_files(media_files: list[Path], manifest: dict) -> list[Path]:
    """Filter to only files not yet processed (or changed since last run)."""
    new_files = []
    for fpath in media_files:
        key = str(fpath.relative_to(WORKSPACE))
        sha = file_sha256(fpath)
        if key not in manifest["processed"] or manifest["processed"][key]["sha256"] != sha:
            new_files.append(fpath)
    return new_files


def transcribe_file(
    filepath: Path,
    model_name: str = DEFAULT_WHISPER_MODEL,
    language: Optional[str] = DEFAULT_LANGUAGE,
) -> str:
    """Transcribe a video/audio file using faster-whisper. Returns transcript text."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("ERROR: faster-whisper not installed. Run: pip install 'graphifyy[video]'")
        sys.exit(1)

    print(f"  Loading Whisper model '{model_name}'...")
    model = WhisperModel(model_name, device="cpu", compute_type="int8")

    print(f"  Transcribing: {filepath.name}")
    segments, info = model.transcribe(
        str(filepath),
        language=language,
        beam_size=5,
        vad_filter=True,
    )

    detected_lang = info.language
    lang_prob = info.language_probability
    print(f"  Detected language: {detected_lang} (confidence: {lang_prob:.1%})")

    transcript_lines = []
    for segment in segments:
        start_m, start_s = divmod(int(segment.start), 60)
        end_m, end_s = divmod(int(segment.end), 60)
        timestamp = f"[{start_m:02d}:{start_s:02d}-{end_m:02d}:{end_s:02d}]"
        transcript_lines.append(f"{timestamp} {segment.text.strip()}")

    return "\n".join(transcript_lines)


def download_youtube_audio(url: str) -> Path:
    """Download audio from YouTube URL using yt-dlp. Returns path to audio file."""
    RAW_VIDEO_DIR.mkdir(parents=True, exist_ok=True)

    print(f"  Downloading audio from: {url}")
    output_template = str(RAW_VIDEO_DIR / "%(title)s-%(id)s.%(ext)s")

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--extract-audio",
        "--audio-format", "m4a",
        "--audio-quality", "0",
        "--output", output_template,
        "--no-playlist",
        "--print", "after_move:filepath",
        url,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        stderr = result.stderr.strip() if result.stderr else "unknown error"
        print(f"  ERROR from yt-dlp:\n{stderr}")
        raise RuntimeError(f"yt-dlp failed (exit {result.returncode}): {stderr}")

    downloaded_path = result.stdout.strip().split("\n")[-1]
    if not downloaded_path or not Path(downloaded_path).exists():
        all_lines = result.stdout.strip().split("\n")
        for line in reversed(all_lines):
            candidate = line.strip()
            if candidate and Path(candidate).exists():
                downloaded_path = candidate
                break
        else:
            webm_files = sorted(RAW_VIDEO_DIR.glob("*.webm"), key=lambda p: p.stat().st_mtime, reverse=True)
            m4a_files = sorted(RAW_VIDEO_DIR.glob("*.m4a"), key=lambda p: p.stat().st_mtime, reverse=True)
            recent = (m4a_files or webm_files)
            if recent:
                downloaded_path = str(recent[0])
            else:
                raise RuntimeError("yt-dlp completed but output file not found")

    return Path(downloaded_path)


def derive_title_from_filename(filepath: Path) -> str:
    """Extract a human-readable title from the filename."""
    stem = filepath.stem
    for ext in ALL_MEDIA_EXTENSIONS:
        if stem.endswith(ext.lstrip(".")):
            stem = stem[: -len(ext.lstrip("."))].rstrip(".")

    stem = re.sub(r"-\d{14}$", "", stem)  # remove timestamp suffix like -20260429231327
    stem = re.sub(r"-[a-zA-Z0-9_-]{11}$", "", stem)  # remove YouTube ID
    title = stem.replace("_", " ").replace("-", " ")
    title = re.sub(r"\s+", " ", title).strip()
    return title.title() if title else filepath.stem


def save_transcript(filepath: Path, transcript: str, title: str) -> Path:
    """Save transcript as markdown in raw/transcripts/."""
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    slug = slugify(title)
    transcript_path = TRANSCRIPTS_DIR / f"{slug}.md"

    today = datetime.now().strftime("%Y-%m-%d")
    content = f"""---
type: source
title: "{title}"
tags: [transcript, media]
related: []
created: {today}
updated: {today}
media_file: "{filepath.name}"
---

# {title}

**Source**: `{filepath.relative_to(WORKSPACE)}`
**Transcribed**: {today}

---

## Transcript

{transcript}
"""
    transcript_path.write_text(content, encoding="utf-8")
    print(f"  Saved transcript: {transcript_path.relative_to(WORKSPACE)}")
    return transcript_path


def create_wiki_source_page(filepath: Path, transcript: str, title: str) -> Path:
    """Create a wiki source page for the transcribed media."""
    WIKI_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    slug = slugify(title)
    today = datetime.now().strftime("%Y-%m-%d")

    summary_lines = transcript.split("\n")[:10]
    summary_preview = "\n".join(summary_lines)
    if len(transcript.split("\n")) > 10:
        summary_preview += "\n\n*(... full transcript in raw/transcripts/)*"

    wiki_slug = f"media-{slug}"
    wiki_path = WIKI_SOURCES_DIR / f"{wiki_slug}.md"

    content = f"""---
type: source
title: "{title}"
tags: [transcript, media, video]
related: []
created: {today}
updated: {today}
authors: []
year: {datetime.now().year}
url: ""
venue: ""
---

# {title}

**Summary**: Transcript extracted from media file `{filepath.name}`.

**Sources**: `{filepath.relative_to(WORKSPACE)}`

**Last updated**: {today}

---

## Key Points

*(To be filled after reviewing the transcript)*

## Transcript Preview

{summary_preview}

## Related pages

*(Cross-references to be added as concepts are identified)*
"""
    wiki_path.write_text(content, encoding="utf-8")
    print(f"  Created wiki page: {wiki_path.relative_to(WORKSPACE)}")
    return wiki_path


def update_wiki_index(title: str, wiki_slug: str) -> None:
    """Add new source entry to wiki/index.md."""
    if not WIKI_INDEX.exists():
        return

    index_content = WIKI_INDEX.read_text(encoding="utf-8")
    entry = f"- [[{wiki_slug}]] — Transcript: {title}"

    if wiki_slug in index_content:
        print("  Index already contains this entry, skipping.")
        return

    marker = "## Sources"
    if marker in index_content:
        lines = index_content.split("\n")
        insert_idx = None
        for i, line in enumerate(lines):
            if line.strip() == marker:
                insert_idx = i + 1
                break

        if insert_idx is not None:
            while insert_idx < len(lines) and lines[insert_idx].startswith("- "):
                insert_idx += 1
            lines.insert(insert_idx, entry)
            WIKI_INDEX.write_text("\n".join(lines), encoding="utf-8")
            print(f"  Updated wiki/index.md")
    else:
        with open(WIKI_INDEX, "a", encoding="utf-8") as f:
            f.write(f"\n{entry}\n")
        print(f"  Appended to wiki/index.md")


def update_wiki_log(title: str, filepath: Path) -> None:
    """Append entry to wiki/log.md."""
    if not WIKI_LOG.exists():
        return

    today = datetime.now().strftime("%Y-%m-%d")
    log_content = WIKI_LOG.read_text(encoding="utf-8")

    entry = f"- Transcribed and ingested media: **{title}** (from `{filepath.name}`)"
    date_header = f"## {today}"

    if date_header in log_content:
        log_content = log_content.replace(date_header, f"{date_header}\n{entry}", 1)
    else:
        lines = log_content.split("\n")
        insert_after = 0
        for i, line in enumerate(lines):
            if line.startswith("# "):
                insert_after = i + 1
                break

        lines.insert(insert_after, f"\n{date_header}\n{entry}\n")
        log_content = "\n".join(lines)

    WIKI_LOG.write_text(log_content, encoding="utf-8")
    print(f"  Updated wiki/log.md")


def format_duration(seconds: float) -> str:
    """Format seconds into XmYs format."""
    m, s = divmod(int(seconds), 60)
    return f"{m}m{s:02d}s"


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract media transcripts and ingest into wiki")
    parser.add_argument("--model", default=DEFAULT_WHISPER_MODEL,
                        help=f"Whisper model size (default: {DEFAULT_WHISPER_MODEL}). Options: tiny, base, small, medium, large-v3")
    parser.add_argument("--language", default=DEFAULT_LANGUAGE,
                        help="Force language (e.g., 'en', 'vi'). Default: auto-detect")
    parser.add_argument("--url", type=str, default=None,
                        help="YouTube/video URL to download and transcribe")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview files to be processed without transcribing")
    parser.add_argument("--scan-dir", type=str, default=str(RAW_DIR),
                        help=f"Directory to scan for media files (default: {RAW_DIR})")
    args = parser.parse_args()

    start_time = time.time()
    manifest = load_manifest()
    processed_count = 0

    # ── YouTube download mode ──────────────────────────────────────────────
    if args.url:
        print(f"\n=== YouTube Download Mode ===")
        audio_path = download_youtube_audio(args.url)
        title = derive_title_from_filename(audio_path)
        print(f"  Title: {title}")

        transcript = transcribe_file(audio_path, model_name=args.model, language=args.language)
        save_transcript(audio_path, transcript, title)

        wiki_slug = f"media-{slugify(title)}"
        create_wiki_source_page(audio_path, transcript, title)
        update_wiki_index(title, wiki_slug)
        update_wiki_log(title, audio_path)

        key = str(audio_path.relative_to(WORKSPACE))
        manifest["processed"][key] = {
            "sha256": file_sha256(audio_path),
            "transcribed_at": datetime.now().isoformat(),
            "title": title,
        }
        save_manifest(manifest)
        processed_count = 1

    # ── Local scan mode ────────────────────────────────────────────────────
    else:
        scan_dir = Path(args.scan_dir)
        print(f"\n=== Scanning {scan_dir} for media files ===")

        media_files = scan_media_files(scan_dir)
        print(f"  Found {len(media_files)} media file(s) total")

        new_files = get_new_files(media_files, manifest)
        print(f"  New/changed: {len(new_files)} file(s)")

        if not new_files:
            print("\n  Nothing new to process.")
        elif args.dry_run:
            print("\n  [DRY RUN] Would process:")
            for f in new_files:
                print(f"    - {f.relative_to(WORKSPACE)}")
        else:
            for i, fpath in enumerate(new_files, 1):
                print(f"\n--- [{i}/{len(new_files)}] {fpath.name} ---")
                title = derive_title_from_filename(fpath)
                print(f"  Title: {title}")

                transcript = transcribe_file(fpath, model_name=args.model, language=args.language)
                save_transcript(fpath, transcript, title)

                wiki_slug = f"media-{slugify(title)}"
                create_wiki_source_page(fpath, transcript, title)
                update_wiki_index(title, wiki_slug)
                update_wiki_log(title, fpath)

                key = str(fpath.relative_to(WORKSPACE))
                manifest["processed"][key] = {
                    "sha256": file_sha256(fpath),
                    "transcribed_at": datetime.now().isoformat(),
                    "title": title,
                }
                save_manifest(manifest)
                processed_count += 1

    elapsed = time.time() - start_time
    print(f"\n=== Done! Processed {processed_count} file(s) in {format_duration(elapsed)} ===")


if __name__ == "__main__":
    main()
