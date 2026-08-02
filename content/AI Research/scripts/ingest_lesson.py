"""
Ingest a "Webpage, Complete" lesson (HTML + _files + separate audio) into the
wiki, reusing the existing wiki-integration layer from ``extract_content.py``.

This is the bridge between the ``course_extractor`` tool
(tools/webpage-content-extractor) and the workspace's existing ingest
workflow. Where ``extract_content.py`` transcribes each media file in
isolation, this routes a *lesson folder* through ``course_extractor`` so the
audio transcripts land inside the lesson's own audio placeholders, images are
embedded, and one coherent source page is produced — then it reuses
``update_wiki_index`` / ``update_wiki_log`` / ``slugify`` so the page is
registered exactly like every other source.

Run it with the tool's venv (which has ``course_extractor`` + faster-whisper):

  tools\\webpage-content-extractor\\.venv\\Scripts\\python.exe scripts\\ingest_lesson.py --all
  ...                                                          scripts\\ingest_lesson.py --input "raw\\sources\\Lesson 1 - ..."
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

# NOTE: BIM_ISO\scripts is a junction into .shared\scripts, so Path.resolve()
# would rewrite our base to .shared (where raw/ and wiki/ do not exist). Use
# os.path.abspath, which normalizes without following the junction, so we stay
# anchored on the real project root.
SCRIPTS_DIR = Path(os.path.abspath(__file__)).parent
WORKSPACE = SCRIPTS_DIR.parent
RAW_SOURCES_DIR = WORKSPACE / "raw" / "sources"
WIKI_DIR = WORKSPACE / "wiki"
WIKI_SOURCES_DIR = WIKI_DIR / "sources"
MANIFEST_PATH = SCRIPTS_DIR / ".lesson_manifest.json"
TOOL_DIR = WORKSPACE / "tools" / "webpage-content-extractor"

# Reuse the existing wiki-integration helpers instead of reinventing them.
sys.path.insert(0, str(SCRIPTS_DIR))
import extract_content as _ec  # noqa: E402
from extract_content import slugify, update_wiki_index, update_wiki_log  # noqa: E402
from lesson_utils import find_lesson_folders as _find, folder_signature, is_lesson_folder  # noqa: E402

# The imported helpers derive their wiki paths from extract_content's own
# __file__.resolve() (which lands in .shared). Repoint them at the real project
# so index.md / log.md are updated in this workspace.
_ec.WORKSPACE = WORKSPACE
_ec.WIKI_DIR = WIKI_DIR
_ec.WIKI_SOURCES_DIR = WIKI_SOURCES_DIR
_ec.WIKI_INDEX = WIKI_DIR / "index.md"
_ec.WIKI_LOG = WIKI_DIR / "log.md"

# Make course_extractor importable even without an editable install on this python.
_TOOL_SRC = TOOL_DIR / "src"
if _TOOL_SRC.exists():
    sys.path.insert(0, str(_TOOL_SRC))


def _require_course_extractor():
    try:
        from course_extractor.config import Config  # noqa: F401
        from course_extractor.pipeline import run_extract  # noqa: F401
    except Exception as exc:  # noqa: BLE001
        print(
            "ERROR: could not import course_extractor. Run this with the tool venv:\n"
            r"  tools\webpage-content-extractor\.venv\Scripts\python.exe scripts\ingest_lesson.py --all"
            f"\n(import error: {exc})"
        )
        sys.exit(2)


def find_lesson_folders() -> list[Path]:
    return _find(RAW_SOURCES_DIR)


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {"processed": {}}


def save_manifest(manifest: dict) -> None:
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def ingest_folder(folder: Path, *, transcribe: bool, whisper_model: str, language: str | None) -> str:
    """Extract one lesson folder and publish it as a flat wiki source page."""
    from course_extractor.config import Config
    from course_extractor.pipeline import run_extract

    config = Config(
        formats=["md", "docx", "json"],
        transcribe=transcribe,
        whisper_model=whisper_model,
        whisper_language=language,
    )
    staging = TOOL_DIR / "output"
    result = run_extract(folder, staging, config)
    lesson_dir = result.output_dir
    slug = lesson_dir.name
    title = result.document.source.title

    # Preserve Unit info from folder name if not already in title
    folder_name = folder.name
    if folder_name.startswith("Unit ") and "Unit " not in title:
        # Extract unit prefix (e.g., "Unit 2 - " from "Unit 2 - Lesson 4 - ...")
        unit_prefix = folder_name.split(" - ")[0] + " - "
        title = unit_prefix + title
        # Update slug to include unit for uniqueness
        unit_part = unit_prefix.lower().replace(" - ", "-").replace(" ", "-")
        slug = unit_part + slug

    # Publish as wiki/sources/<slug>.md with assets under wiki/sources/<slug>/assets/
    page_path = WIKI_SOURCES_DIR / f"{slug}.md"
    asset_root = WIKI_SOURCES_DIR / slug
    WIKI_SOURCES_DIR.mkdir(parents=True, exist_ok=True)

    src_assets = lesson_dir / "assets"
    if src_assets.exists():
        dst_assets = asset_root / "assets"
        if dst_assets.exists():
            shutil.rmtree(dst_assets)
        dst_assets.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src_assets, dst_assets)

    # Rewrite relative asset links from "assets/" to "<slug>/assets/".
    md = (lesson_dir / "index.md").read_text(encoding="utf-8")
    md = md.replace("](assets/", f"]({slug}/assets/")
    page_path.write_text(md, encoding="utf-8")

    # Keep the report + docx alongside the assets for reference.
    shutil.copy2(lesson_dir / "extraction-report.md", asset_root / "extraction-report.md")
    docx = next(lesson_dir.glob("*.docx"), None)
    if docx:
        shutil.copy2(docx, asset_root / docx.name)

    # Reuse the existing wiki registration helpers.
    update_wiki_index(title, slug, "lesson")
    update_wiki_log(title, folder, "lesson")

    print(f"  Published: wiki/sources/{slug}.md")
    return slug


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest Webpage-Complete lesson folders into the wiki")
    parser.add_argument("--input", type=str, help="A specific lesson folder (default: scan raw/sources)")
    parser.add_argument("--all", action="store_true", help="Process every new/changed lesson folder")
    parser.add_argument("--no-transcribe", action="store_true", help="Skip audio transcription")
    parser.add_argument("--model", default="small", help="Whisper model (default: small)")
    parser.add_argument("--language", default="en", help="Transcription language (default: en)")
    parser.add_argument("--force", action="store_true", help="Reprocess even if unchanged")
    parser.add_argument("--dry-run", action="store_true", help="List what would be processed")
    args = parser.parse_args()

    _require_course_extractor()

    if args.input:
        folders = [Path(args.input).resolve()]
    else:
        folders = find_lesson_folders()

    if not folders:
        print("No Webpage-Complete lesson folders found in raw/sources/.")
        return

    manifest = load_manifest()
    processed = 0
    for folder in folders:
        if not is_lesson_folder(folder):
            print(f"  Skip (not a lesson folder): {folder.name}")
            continue
        key = str(folder.relative_to(WORKSPACE)) if str(folder).startswith(str(WORKSPACE)) else str(folder)
        sig = folder_signature(folder)
        if not args.force and manifest["processed"].get(key, {}).get("signature") == sig:
            print(f"  Unchanged, skip: {folder.name}")
            continue
        print(f"\n--- Ingesting lesson: {folder.name} ---")
        if args.dry_run:
            processed += 1
            continue
        slug = ingest_folder(
            folder,
            transcribe=not args.no_transcribe,
            whisper_model=args.model,
            language=args.language,
        )
        manifest["processed"][key] = {
            "signature": sig,
            "slug": slug,
            "ingested_at": datetime.now().isoformat(),
        }
        save_manifest(manifest)
        processed += 1

    print(f"\n=== Done. {processed} lesson(s) {'to process' if args.dry_run else 'ingested'}. ===")


if __name__ == "__main__":
    main()
