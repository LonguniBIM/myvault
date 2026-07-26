"""
Extract content from all file types in raw/ and ingest into the wiki.

Handles:
  - Video/Audio → faster-whisper transcription (local)
  - Images → extract text description via OCR/metadata
  - PDFs → extract text content
  - Office (.docx .xlsx) → convert to markdown
  - Markdown/Text → copy as-is (already readable)

Each extracted file gets:
  1. A readable extract in raw/extracts/<slug>.md
  2. A wiki source page in wiki/sources/extract-<slug>.md
  3. Entries in wiki/index.md and wiki/log.md

Usage:
  python scripts/extract_content.py                     # scan & extract all new files
  python scripts/extract_content.py --type video         # only video/audio
  python scripts/extract_content.py --type image         # only images
  python scripts/extract_content.py --type pdf           # only PDFs
  python scripts/extract_content.py --type doc           # only .docx/.xlsx
  python scripts/extract_content.py --model medium       # better whisper accuracy
  python scripts/extract_content.py --url <youtube-url>  # download + transcribe YouTube
  python scripts/extract_content.py --dry-run            # preview what would be processed
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
EXTRACTS_DIR = RAW_DIR / "extracts"
WIKI_DIR = WORKSPACE / "wiki"
WIKI_SOURCES_DIR = WIKI_DIR / "sources"
WIKI_INDEX = WIKI_DIR / "index.md"
WIKI_LOG = WIKI_DIR / "log.md"
MANIFEST_PATH = WORKSPACE / "scripts" / ".content_manifest.json"

VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}
AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".ogg", ".flac"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp"}
PDF_EXTENSIONS = {".pdf"}
DOCX_EXTENSIONS = {".docx"}
XLSX_EXTENSIONS = {".xlsx"}
TEXT_EXTENSIONS = {".md", ".mdx", ".txt", ".rst", ".html"}

MEDIA_EXTENSIONS = VIDEO_EXTENSIONS | AUDIO_EXTENSIONS
ALL_EXTRACTABLE = MEDIA_EXTENSIONS | IMAGE_EXTENSIONS | PDF_EXTENSIONS | DOCX_EXTENSIONS | XLSX_EXTENSIONS | TEXT_EXTENSIONS

TYPE_GROUPS = {
    "video": MEDIA_EXTENSIONS,
    "image": IMAGE_EXTENSIONS,
    "pdf": PDF_EXTENSIONS,
    "doc": DOCX_EXTENSIONS | XLSX_EXTENSIONS,
    "text": TEXT_EXTENSIONS,
    "all": ALL_EXTRACTABLE,
}

DEFAULT_WHISPER_MODEL = "base"
DEFAULT_LANGUAGE = None


# ── Utility functions ──────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Convert text to kebab-case slug safe for filenames."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")[:120]


def file_sha256(filepath: Path) -> str:
    """Compute SHA256 hash for change detection."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest() -> dict:
    """Load processed files manifest."""
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {"processed": {}}


def save_manifest(manifest: dict) -> None:
    """Persist manifest to disk."""
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)


def derive_title(filepath: Path) -> str:
    """Extract a human-readable title from filename."""
    stem = filepath.stem
    for ext in ALL_EXTRACTABLE:
        if stem.endswith(ext.lstrip(".")):
            stem = stem[: -len(ext.lstrip("."))].rstrip(".")
    stem = re.sub(r"-\d{14}$", "", stem)
    stem = re.sub(r"-[a-zA-Z0-9_-]{11}$", "", stem)
    title = stem.replace("_", " ").replace("-", " ")
    title = re.sub(r"\s+", " ", title).strip()
    return title.title() if title else filepath.stem


def format_duration(seconds: float) -> str:
    """Format seconds into XmYs."""
    m, s = divmod(int(seconds), 60)
    return f"{m}m{s:02d}s"


def detect_file_type(filepath: Path) -> str:
    """Classify a file into its extraction category."""
    ext = filepath.suffix.lower()
    if ext in MEDIA_EXTENSIONS:
        return "video"
    if ext in IMAGE_EXTENSIONS:
        return "image"
    if ext in PDF_EXTENSIONS:
        return "pdf"
    if ext in DOCX_EXTENSIONS:
        return "docx"
    if ext in XLSX_EXTENSIONS:
        return "xlsx"
    if ext in TEXT_EXTENSIONS:
        return "text"
    return "unknown"


# ── Scanners ───────────────────────────────────────────────────────────────────

def scan_files(base_dir: Path, extensions: set[str]) -> list[Path]:
    """Recursively find files matching given extensions.

    Files that belong to a saved "Webpage, Complete" lesson (the .htm, its
    ``*_files`` assets, and the lesson's audio) are skipped here — those are
    handled as a coherent unit by ``ingest_lesson.py``.
    """
    from lesson_utils import in_lesson_scope

    results = []
    for root, _dirs, files in os.walk(base_dir):
        root_path = Path(root)
        if "extracts" in root_path.parts or "transcripts" in root_path.parts:
            continue
        for fname in sorted(files):
            fpath = root_path / fname
            if fpath.suffix.lower() in extensions and not in_lesson_scope(fpath):
                results.append(fpath)
    return results


def get_new_files(files: list[Path], manifest: dict) -> list[Path]:
    """Filter to files not yet processed or changed."""
    new = []
    for fpath in files:
        # Determine relative path from Workspace
        # If the file is inside the workspace, use workspace-relative
        # If it's outside (rare but possible), use its name
        try:
            key = str(fpath.relative_to(WORKSPACE))
        except ValueError:
            key = str(fpath)

        sha = file_sha256(fpath)
        if key not in manifest["processed"] or manifest["processed"][key].get("sha256") != sha:
            new.append(fpath)
    return new


# ── Extractors ─────────────────────────────────────────────────────────────────

def extract_video_audio(
    filepath: Path,
    model_name: str = DEFAULT_WHISPER_MODEL,
    language: Optional[str] = DEFAULT_LANGUAGE,
) -> str:
    """Transcribe video/audio via faster-whisper."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("  ERROR: faster-whisper not installed. Run: pip install 'graphifyy[video]'")
        return "[ERROR: faster-whisper not installed]"

    print(f"  Loading Whisper model '{model_name}'...")
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    print(f"  Transcribing: {filepath.name}")

    segments, info = model.transcribe(str(filepath), language=language, beam_size=5, vad_filter=True)
    print(f"  Detected language: {info.language} (confidence: {info.language_probability:.1%})")

    lines = []
    for seg in segments:
        sm, ss = divmod(int(seg.start), 60)
        em, es = divmod(int(seg.end), 60)
        lines.append(f"[{sm:02d}:{ss:02d}-{em:02d}:{es:02d}] {seg.text.strip()}")
    return "\n".join(lines)


def extract_image(filepath: Path) -> str:
    """Extract metadata and basic description from an image."""
    from PIL import Image

    img = Image.open(filepath)
    meta_lines = [
        f"**Format**: {img.format}",
        f"**Size**: {img.size[0]}x{img.size[1]}",
        f"**Mode**: {img.mode}",
    ]

    exif = {}
    try:
        raw_exif = img._getexif()
        if raw_exif:
            from PIL.ExifTags import TAGS
            exif = {TAGS.get(k, k): v for k, v in raw_exif.items() if isinstance(v, (str, int, float))}
    except (AttributeError, Exception):
        pass

    if exif:
        meta_lines.append("\n### EXIF Metadata")
        for k, v in list(exif.items())[:15]:
            meta_lines.append(f"- **{k}**: {v}")

    meta_lines.append(
        "\n> *Note: For full concept extraction from this image, run `/graphify ./raw` in Cursor chat. "
        "Graphify uses Claude Vision to read diagrams, text, and visual content.*"
    )
    return "\n".join(meta_lines)


def extract_pdf(filepath: Path) -> str:
    """Extract text from PDF."""
    try:
        from fpdf import FPDF  # noqa: F401 — just checking
    except ImportError:
        pass

    try:
        import fitz  # PyMuPDF
        doc = fitz.open(str(filepath))
        pages = []
        for i, page in enumerate(doc):
            text = page.get_text().strip()
            if text:
                pages.append(f"### Page {i + 1}\n\n{text}")
        doc.close()
        if pages:
            return "\n\n---\n\n".join(pages)
    except ImportError:
        pass

    try:
        from pypdf import PdfReader
        reader = PdfReader(str(filepath))
        pages = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and text.strip():
                pages.append(f"### Page {i + 1}\n\n{text.strip()}")
        if pages:
            return "\n\n---\n\n".join(pages)
    except ImportError:
        pass

    try:
        import subprocess
        result = subprocess.run(
            ["pdftotext", str(filepath), "-"],
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    return (
        f"*PDF file: {filepath.name} ({os.path.getsize(filepath)} bytes)*\n\n"
        "> No PDF text extractor available. Install one:\n"
        "> `pip install pymupdf` (recommended) or `pip install pypdf`\n\n"
        "> For full extraction, run `/graphify ./raw` in Cursor chat — "
        "graphify handles PDFs natively via Claude."
    )


def extract_docx(filepath: Path) -> str:
    """Extract text from Word document."""
    from docx import Document

    doc = Document(filepath)
    sections = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        if para.style and para.style.name.startswith("Heading"):
            level = 1
            try:
                level = int(para.style.name.split()[-1])
            except (ValueError, IndexError):
                pass
            sections.append(f"{'#' * (level + 1)} {text}")
        else:
            sections.append(text)

    tables_md = []
    for i, table in enumerate(doc.tables):
        rows = []
        for row in table.rows:
            cells = [cell.text.strip() for cell in row.cells]
            rows.append("| " + " | ".join(cells) + " |")
        if rows:
            header_sep = "| " + " | ".join(["---"] * len(table.rows[0].cells)) + " |"
            tables_md.append(f"\n### Table {i + 1}\n\n" + rows[0] + "\n" + header_sep + "\n" + "\n".join(rows[1:]))

    content = "\n\n".join(sections)
    if tables_md:
        content += "\n\n" + "\n".join(tables_md)
    return content


def extract_xlsx(filepath: Path) -> str:
    """Extract data from Excel file as markdown tables."""
    from openpyxl import load_workbook

    wb = load_workbook(filepath, data_only=True)
    sheets_md = []

    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            continue

        non_empty = [r for r in rows if any(c is not None for c in r)]
        if not non_empty:
            continue

        header = non_empty[0]
        col_count = len(header)
        md_rows = ["| " + " | ".join(str(c) if c is not None else "" for c in header) + " |"]
        md_rows.append("| " + " | ".join(["---"] * col_count) + " |")

        for row in non_empty[1:]:
            cells = [str(c) if c is not None else "" for c in row[:col_count]]
            md_rows.append("| " + " | ".join(cells) + " |")

        sheets_md.append(f"### Sheet: {ws.title}\n\n" + "\n".join(md_rows))

    return "\n\n---\n\n".join(sheets_md) if sheets_md else "*Empty spreadsheet*"


def extract_text(filepath: Path) -> str:
    """Extract text from markdown/text files (read directly)."""
    return filepath.read_text(encoding="utf-8")


# ── Wiki integration ───────────────────────────────────────────────────────────

def save_extract(filepath: Path, content: str, title: str, file_type: str) -> Path:
    """Save extracted content as markdown in raw/extracts/."""
    EXTRACTS_DIR.mkdir(parents=True, exist_ok=True)
    slug = slugify(title)
    extract_path = EXTRACTS_DIR / f"{slug}.md"

    today = datetime.now().strftime("%Y-%m-%d")
    tags = ["extract", file_type]

    md = f"""---
type: source
title: "{title}"
tags: [{', '.join(tags)}]
related: []
created: {today}
updated: {today}
source_file: "{filepath.name}"
file_type: "{file_type}"
---

# {title}

**Source**: `{filepath.relative_to(WORKSPACE) if str(filepath).startswith(str(WORKSPACE)) else filepath.name}`
**Extracted**: {today}
**Type**: {file_type}

---

{content}
"""
    extract_path.write_text(md, encoding="utf-8")
    print(f"  Saved extract: {extract_path.relative_to(WORKSPACE)}")
    return extract_path


def create_wiki_page(filepath: Path, content: str, title: str, file_type: str) -> Path:
    """Create wiki source page for extracted content."""
    WIKI_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    slug = slugify(title)
    wiki_slug = f"extract-{slug}"
    wiki_path = WIKI_SOURCES_DIR / f"{wiki_slug}.md"

    today = datetime.now().strftime("%Y-%m-%d")

    preview_lines = content.split("\n")[:15]
    preview = "\n".join(preview_lines)
    if len(content.split("\n")) > 15:
        preview += "\n\n*(... full content in raw/extracts/)*"

    md = f"""---
type: source
title: "{title}"
tags: [extract, {file_type}]
related: []
created: {today}
updated: {today}
authors: []
year: {datetime.now().year}
url: ""
venue: ""
---

# {title}

**Summary**: Content extracted from {file_type} file `{filepath.name}`.

**Sources**: `{filepath.relative_to(WORKSPACE) if str(filepath).startswith(str(WORKSPACE)) else filepath.name}`

**Last updated**: {today}

---

## Six-Question Analysis

### Q1 — What problem does this solve?

*(To be analyzed)*

### Q2 — What numbered steps does the author prescribe?

*(To be analyzed)*

### Q3 — What principles recur?

*(To be analyzed)*

### Q4 — What mistakes does the author warn against?

*(To be analyzed)*

### Q5 — What diagnostic questions does the author pose?

*(To be analyzed)*

### Q6 — Can the method be expressed as numbered steps?

*(To be analyzed)*

---

## Content Preview

{preview}

## Related pages

*(Cross-references to be added as concepts are identified)*
"""
    wiki_path.write_text(md, encoding="utf-8")
    print(f"  Created wiki page: {wiki_path.relative_to(WORKSPACE)}")
    return wiki_path


def update_wiki_index(title: str, wiki_slug: str, file_type: str) -> None:
    """Add entry to wiki/index.md under Sources."""
    if not WIKI_INDEX.exists():
        return

    index_content = WIKI_INDEX.read_text(encoding="utf-8")
    entry = f"- [[{wiki_slug}]] — [{file_type.upper()}] {title}"

    if wiki_slug in index_content:
        print("  Index already contains this entry, skipping.")
        return

    marker = "## Sources"
    if marker in index_content:
        lines = index_content.split("\n")
        for i, line in enumerate(lines):
            if line.strip() == marker:
                insert_idx = i + 1
                while insert_idx < len(lines) and lines[insert_idx].startswith("- "):
                    insert_idx += 1
                lines.insert(insert_idx, entry)
                WIKI_INDEX.write_text("\n".join(lines), encoding="utf-8")
                print("  Updated wiki/index.md")
                return
    with open(WIKI_INDEX, "a", encoding="utf-8") as f:
        f.write(f"\n{entry}\n")
    print("  Appended to wiki/index.md")


def update_wiki_log(title: str, filepath: Path, file_type: str) -> None:
    """Append entry to wiki/log.md."""
    if not WIKI_LOG.exists():
        return

    today = datetime.now().strftime("%Y-%m-%d")
    log_content = WIKI_LOG.read_text(encoding="utf-8")
    entry = f"- Extracted [{file_type}]: **{title}** (from `{filepath.name}`)"
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
    print("  Updated wiki/log.md")


# ── YouTube download ───────────────────────────────────────────────────────────

def download_youtube_audio(url: str) -> Path:
    """Download audio from YouTube URL using yt-dlp."""
    RAW_VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    print(f"  Downloading audio from: {url}")
    output_template = str(RAW_VIDEO_DIR / "%(title)s-%(id)s.%(ext)s")

    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--extract-audio", "--audio-format", "m4a",
        "--audio-quality", "0",
        "--output", output_template,
        "--no-playlist", "--print", "after_move:filepath",
        url,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        stderr = result.stderr.strip() if result.stderr else "unknown error"
        print(f"  ERROR from yt-dlp:\n{stderr}")
        raise RuntimeError(f"yt-dlp failed (exit {result.returncode}): {stderr}")

    downloaded_path = result.stdout.strip().split("\n")[-1]
    if not downloaded_path or not Path(downloaded_path).exists():
        for line in reversed(result.stdout.strip().split("\n")):
            if line.strip() and Path(line.strip()).exists():
                return Path(line.strip())
        recent = sorted(RAW_VIDEO_DIR.glob("*.m4a"), key=lambda p: p.stat().st_mtime, reverse=True)
        if recent:
            return recent[0]
        raise RuntimeError("yt-dlp completed but output file not found")

    return Path(downloaded_path)


# ── Main dispatch ──────────────────────────────────────────────────────────────

def process_file(
    filepath: Path,
    whisper_model: str = DEFAULT_WHISPER_MODEL,
    language: Optional[str] = DEFAULT_LANGUAGE,
) -> tuple[str, str, str]:
    """Extract content from a file. Returns (content, title, file_type)."""
    file_type = detect_file_type(filepath)
    title = derive_title(filepath)

    if file_type == "video":
        content = extract_video_audio(filepath, whisper_model, language)
    elif file_type == "image":
        content = extract_image(filepath)
    elif file_type == "pdf":
        content = extract_pdf(filepath)
    elif file_type == "docx":
        content = extract_docx(filepath)
    elif file_type == "xlsx":
        content = extract_xlsx(filepath)
    elif file_type == "text":
        content = extract_text(filepath)
    else:
        content = f"*Unsupported file type: {filepath.suffix}*"

    return content, title, file_type


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract content from all file types and ingest into wiki")
    parser.add_argument("--type", choices=["video", "image", "pdf", "doc", "text", "all"], default="all",
                        help="File type to extract (default: all)")
    parser.add_argument("--model", default=DEFAULT_WHISPER_MODEL,
                        help=f"Whisper model for video/audio (default: {DEFAULT_WHISPER_MODEL})")
    parser.add_argument("--language", default=DEFAULT_LANGUAGE,
                        help="Force language for transcription (default: auto-detect)")
    parser.add_argument("--url", type=str, default=None,
                        help="YouTube/video URL to download and transcribe")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview files without processing")
    parser.add_argument("--scan-dir", type=str, default=str(RAW_DIR),
                        help=f"Directory to scan (default: {RAW_DIR})")
    args = parser.parse_args()

    start_time = time.time()
    manifest = load_manifest()
    processed_count = 0
    errors = []

    # ── YouTube mode ───────────────────────────────────────────────────────
    if args.url:
        print("\n=== YouTube Download Mode ===")
        audio_path = download_youtube_audio(args.url)
        content, title, file_type = process_file(audio_path, args.model, args.language)
        print(f"  Title: {title}")

        save_extract(audio_path, content, title, file_type)
        wiki_slug = f"extract-{slugify(title)}"
        create_wiki_page(audio_path, content, title, file_type)
        update_wiki_index(title, wiki_slug, file_type)
        update_wiki_log(title, audio_path, file_type)

        manifest["processed"][str(audio_path.relative_to(WORKSPACE))] = {
            "sha256": file_sha256(audio_path),
            "extracted_at": datetime.now().isoformat(),
            "title": title,
            "type": file_type,
        }
        save_manifest(manifest)
        processed_count = 1

    # ── Local scan mode ────────────────────────────────────────────────────
    else:
        extensions = TYPE_GROUPS[args.type]
        scan_dir = Path(args.scan_dir)
        print(f"\n=== Scanning {scan_dir} for {args.type} files ===")

        all_files = scan_files(scan_dir, extensions)
        print(f"  Found {len(all_files)} file(s) total")

        new_files = get_new_files(all_files, manifest)
        print(f"  New/changed: {len(new_files)} file(s)")

        if not new_files:
            print("\n  Nothing new to process.")
        elif args.dry_run:
            print("\n  [DRY RUN] Would process:")
            for f in new_files:
                ftype = detect_file_type(f)
                print(f"    [{ftype:5s}] {f.relative_to(WORKSPACE) if str(f).startswith(str(WORKSPACE)) else f.name}")
        else:
            for i, fpath in enumerate(new_files, 1):
                ftype = detect_file_type(fpath)
                print(f"\n--- [{i}/{len(new_files)}] [{ftype}] {fpath.name} ---")

                try:
                    content, title, file_type = process_file(fpath, args.model, args.language)
                    print(f"  Title: {title}")

                    save_extract(fpath, content, title, file_type)
                    wiki_slug = f"extract-{slugify(title)}"
                    create_wiki_page(fpath, content, title, file_type)
                    update_wiki_index(title, wiki_slug, file_type)
                    update_wiki_log(title, fpath, file_type)

                    try:
                        key = str(fpath.relative_to(WORKSPACE))
                    except ValueError:
                        key = str(fpath)

                    manifest["processed"][key] = {
                        "sha256": file_sha256(fpath),
                        "extracted_at": datetime.now().isoformat(),
                        "title": title,
                        "type": file_type,
                    }
                    save_manifest(manifest)
                    processed_count += 1

                except Exception as e:
                    print(f"  ERROR: {e}")
                    import traceback
                    traceback.print_exc()
                    errors.append((fpath, str(e)))

    elapsed = time.time() - start_time
    print(f"\n=== Done! Processed {processed_count} file(s) in {format_duration(elapsed)} ===")
    if errors:
        print(f"\n  {len(errors)} error(s):")
        for fpath, err in errors:
            print(f"    - {fpath.name}: {err}")



if __name__ == "__main__":
    main()
