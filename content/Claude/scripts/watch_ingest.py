"""
File watcher for auto-ingest: monitors raw/sources/ for new files and triggers
the wiki ingest pipeline via the configured AI agent.

When a new .md file appears in raw/sources/, this script:
1. Detects the new file (via polling manifest comparison)
2. Creates a trigger file at .llm-wiki/ingest-queue/<timestamp>.json
3. Optionally notifies via system notification

The AI agent (Claude Code, Cursor) can then pick up pending items from
.llm-wiki/ingest-queue/ and run the CLAUDE.md Auto-Ingest Pipeline.

Usage:
  python scripts/watch_ingest.py              # start watching (poll every 5s)
  python scripts/watch_ingest.py --interval 3 # custom poll interval
  python scripts/watch_ingest.py --once       # single check, no loop
  python scripts/watch_ingest.py --status     # show pending ingest items
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# BIM_ISO\scripts is a junction into .shared\scripts; os.path.abspath normalizes
# without following it, keeping us anchored on the real project (Path.resolve
# would rewrite the base to .shared, where raw/ and wiki/ do not exist).
SCRIPTS_DIR = Path(os.path.abspath(__file__)).parent
WORKSPACE = SCRIPTS_DIR.parent
RAW_SOURCES_DIR = WORKSPACE / "raw" / "sources"
QUEUE_DIR = WORKSPACE / ".llm-wiki" / "ingest-queue"
MANIFEST_FILE = SCRIPTS_DIR / ".ingest_manifest.json"

# The bridge that turns a lesson folder into a wiki page, run with the tool venv
# (which has course_extractor + faster-whisper installed).
BRIDGE = SCRIPTS_DIR / "ingest_lesson.py"
TOOL_PY = WORKSPACE / "tools" / "webpage-content-extractor" / ".venv" / "Scripts" / "python.exe"

sys.path.insert(0, str(SCRIPTS_DIR))
from lesson_utils import find_lesson_folders, folder_signature  # noqa: E402


def load_manifest() -> dict:
    if MANIFEST_FILE.exists():
        m = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
        m.setdefault("processed", [])
        m.setdefault("lessons", {})
        m.setdefault("last_check", None)
        return m
    return {"processed": [], "lessons": {}, "last_check": None}


def save_manifest(manifest: dict) -> None:
    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_FILE.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def get_source_files() -> list[Path]:
    if not RAW_SOURCES_DIR.exists():
        return []
    return sorted(RAW_SOURCES_DIR.glob("*.md"))


def detect_new_files(manifest: dict) -> list[Path]:
    all_files = get_source_files()
    processed = set(manifest.get("processed", []))
    return [f for f in all_files if f.name not in processed]


def detect_new_lessons(manifest: dict) -> list[Path]:
    """Lesson folders whose signature changed since last ingest."""
    seen = manifest.get("lessons", {})
    new = []
    for folder in find_lesson_folders(RAW_SOURCES_DIR):
        key = folder.name
        if seen.get(key) != folder_signature(folder):
            new.append(folder)
    return new


def ingest_lesson_folder(folder: Path) -> bool:
    """Run the bridge on one lesson folder. Returns True on success."""
    if not TOOL_PY.exists():
        print(f"  ! tool venv not found ({TOOL_PY}). Run scripts\\setup.ps1 in the tool first.")
        return False
    env = dict(os.environ, PYTHONUTF8="1")
    proc = subprocess.run(
        [str(TOOL_PY), str(BRIDGE), "--input", str(folder)],
        env=env,
    )
    return proc.returncode == 0


def queue_for_ingest(filepath: Path) -> Path:
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    queue_item = {
        "file": str(filepath.relative_to(WORKSPACE)),
        "filename": filepath.name,
        "detected_at": datetime.now().isoformat(),
        "status": "pending",
        "title": derive_title(filepath.stem),
    }
    queue_file = QUEUE_DIR / f"{timestamp}-{filepath.stem[:40]}.json"
    queue_file.write_text(
        json.dumps(queue_item, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return queue_file


def derive_title(stem: str) -> str:
    title = stem.replace("-", " ").replace("_", " ")
    if title.startswith("github "):
        parts = title.split(" ")
        if len(parts) > 2:
            title = " ".join(parts[1:5]) + "..."
    return title.title()


def show_status():
    if not QUEUE_DIR.exists():
        print("No ingest queue directory. Nothing pending.")
        return

    items = sorted(QUEUE_DIR.glob("*.json"))
    if not items:
        print("Ingest queue is empty. All items processed.")
        return

    print(f"\n{'='*60}")
    print(f" Pending Ingest Queue ({len(items)} items)")
    print(f"{'='*60}\n")

    for item_file in items:
        data = json.loads(item_file.read_text(encoding="utf-8"))
        status_icon = {"pending": "⏳", "processing": "🔄", "done": "✅", "error": "❌"}.get(
            data.get("status", "pending"), "?"
        )
        print(f"  {status_icon} {data.get('title', 'Unknown')}")
        print(f"     File: {data.get('file', '?')}")
        print(f"     Detected: {data.get('detected_at', '?')}")
        print()


def watch_loop(interval: int = 5, once: bool = False):
    print(f"👁️  Watching raw/sources/ for new files (poll every {interval}s)")
    print(f"   Directory: {RAW_SOURCES_DIR}")
    print(f"   Queue: {QUEUE_DIR}")
    print(f"   Press Ctrl+C to stop\n")

    manifest = load_manifest()

    while True:
        new_files = detect_new_files(manifest)
        new_lessons = detect_new_lessons(manifest)

        if new_lessons:
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Detected {len(new_lessons)} lesson folder(s):")
            for folder in new_lessons:
                print(f"  → ingesting lesson: {folder.name}")
                if ingest_lesson_folder(folder):
                    manifest["lessons"][folder.name] = folder_signature(folder)
                    save_manifest(manifest)
                    print(f"  ✅ {folder.name}")
                else:
                    print(f"  ❌ failed: {folder.name} (will retry next poll)")

        if new_files:
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Detected {len(new_files)} new file(s):")
            for f in new_files:
                queue_file = queue_for_ingest(f)
                manifest["processed"].append(f.name)
                print(f"  + {f.name} → queued at {queue_file.name}")

            manifest["last_check"] = datetime.now().isoformat()
            save_manifest(manifest)
            print(f"\n  💡 Run agent command to ingest: open Cursor chat and say 'ingest pending'")

        if once:
            if not new_files and not new_lessons:
                print("No new files or lessons detected.")
            break

        time.sleep(interval)


def main():
    parser = argparse.ArgumentParser(description="Watch raw/sources/ for new files to ingest")
    parser.add_argument("--interval", type=int, default=5, help="Poll interval in seconds (default: 5)")
    parser.add_argument("--once", action="store_true", help="Single check, no loop")
    parser.add_argument("--status", action="store_true", help="Show pending ingest items")
    args = parser.parse_args()

    if args.status:
        show_status()
        return

    watch_loop(interval=args.interval, once=args.once)


if __name__ == "__main__":
    main()
