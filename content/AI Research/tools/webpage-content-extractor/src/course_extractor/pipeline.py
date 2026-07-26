"""End-to-end extraction pipeline (IR-first)."""

from __future__ import annotations

import shutil
import tempfile
import uuid
from dataclasses import dataclass, field
from pathlib import Path

from .adapters.base import ParseContext
from .adapters.detector import detect_adapter
from .audio import discover_local_audio, match_audio_by_duration, transcribe_matched_audio
from .config import Config
from .html_loader import load_html
from .input_resolver import resolve_input
from .models import DocumentIR
from .renderers.docx_renderer import DocxRenderer
from .renderers.manifest_renderer import write_manifest
from .renderers.markdown_renderer import MarkdownRenderer
from .renderers.report_renderer import write_report
from .util import logging as log
from .util.paths import slugify


@dataclass
class ExtractResult:
    document: DocumentIR
    output_dir: Path
    outputs: dict[str, Path] = field(default_factory=dict)


def parse_document(input_path: Path, config: Config) -> tuple[DocumentIR, Path, Path, object]:
    resolved = resolve_input(input_path, max_unpacked_bytes=config.max_unpacked_bytes)
    if not resolved.html_candidates:
        raise RuntimeError(f"no HTML lesson file found under {input_path}")
    html_path = resolved.best
    log.info("Lesson HTML: {}", html_path.name)
    if len(resolved.html_candidates) > 1:
        log.debug("{} HTML candidates; picked highest score", len(resolved.html_candidates))

    soup = load_html(html_path)
    adapter, conf = detect_adapter(soup)
    log.info("Adapter: {} (confidence {:.2f})", adapter.name, conf)

    doc = DocumentIR()
    ctx = ParseContext(
        html_path=html_path, root_dir=resolved.root_dir, config=config, document=doc
    )
    adapter.parse(soup, ctx)
    return doc, html_path, resolved.root_dir, resolved


def run_extract(input_path: Path, output_root: Path, config: Config) -> ExtractResult:
    config.resolve_tools()
    doc, html_path, root_dir, resolved = parse_document(input_path, config)

    # ---- audio: match by duration, then transcribe ----
    audios = list(doc.iter_audio())
    if audios:
        search_dirs = _dedup_dirs([root_dir, html_path.parent, input_path if input_path.is_dir() else input_path.parent])
        if not config.ffprobe_path:
            log.warn("ffprobe not found; cannot match audio by duration")
        pool = discover_local_audio(search_dirs, config.ffprobe_path)
        log.info("Found {} local audio file(s) to match against {} placeholder(s)", len(pool), len(audios))
        match_audio_by_duration(doc, pool, config.duration_tolerance)
        if config.transcribe:
            transcribe_matched_audio(doc, config)

    # ---- render into staging, then atomic move ----
    slug = slugify(doc.source.title)
    final_dir = output_root / slug
    staging = Path(tempfile.mkdtemp(prefix="wce_stage_"))
    run_dir = staging / slug
    run_dir.mkdir(parents=True, exist_ok=True)

    outputs: dict[str, Path] = {}
    try:
        if "md" in config.formats:
            outputs["md"] = MarkdownRenderer(doc, run_dir, config.mode).render()
        if "docx" in config.formats:
            renderer = DocxRenderer(doc, run_dir / f"{slug}.docx", config.mode)
            outputs["docx"] = renderer.render()
        # manifest + report always help
        outputs["manifest"] = write_manifest(doc, run_dir / "extraction-manifest.json")
        outputs["report"] = write_report(doc, run_dir / "extraction-report.md")

        if final_dir.exists():
            shutil.rmtree(final_dir)
        final_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(run_dir), str(final_dir))
    finally:
        shutil.rmtree(staging, ignore_errors=True)
        if resolved.temp_dir:
            shutil.rmtree(resolved.temp_dir, ignore_errors=True)

    final_outputs = {k: final_dir / Path(v).relative_to(run_dir) for k, v in outputs.items()}
    return ExtractResult(document=doc, output_dir=final_dir, outputs=final_outputs)


def _dedup_dirs(dirs: list[Path]) -> list[Path]:
    seen: set[Path] = set()
    out: list[Path] = []
    for d in dirs:
        if d and d.exists() and d.is_dir():
            r = d.resolve()
            if r not in seen:
                seen.add(r)
                out.append(d)
    return out
