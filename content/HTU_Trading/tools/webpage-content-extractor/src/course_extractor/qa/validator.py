"""Structural validation of extraction outputs."""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path

_IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def validate_output_dir(out_dir: Path) -> list[str]:
    """Return a list of problems (empty = ok)."""
    problems: list[str] = []
    manifest_path = out_dir / "extraction-manifest.json"
    if not manifest_path.exists():
        return [f"manifest missing: {manifest_path}"]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    # markdown image links exist
    md = out_dir / "index.md"
    if md.exists():
        for rel in _IMG_RE.findall(md.read_text(encoding="utf-8")):
            if rel.startswith(("http://", "https://")):
                continue
            if not (out_dir / rel).exists():
                problems.append(f"markdown references missing asset: {rel}")

    # docx package integrity + image relationships
    docx = next(out_dir.glob("*.docx"), None)
    if docx is not None:
        if not zipfile.is_zipfile(docx):
            problems.append(f"docx is not a valid zip package: {docx.name}")
        else:
            with zipfile.ZipFile(docx) as zf:
                media = [n for n in zf.namelist() if n.startswith("word/media/")]
                imgs_found = manifest.get("counts", {}).get("images_found", 0)
                if imgs_found and not media:
                    problems.append("docx has no embedded media despite images_found > 0")
    return problems
