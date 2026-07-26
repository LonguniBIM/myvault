"""Resolve a user input into a root directory + candidate HTML files.

Accepts a ``.zip`` (safe-extracted to temp), a single ``.html``/``.htm``
file, or a directory (recursively scored for lesson HTML candidates).
"""

from __future__ import annotations

import tempfile
from dataclasses import dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup

from .security import safe_extract_zip
from .util import logging as log

_MAX_DEPTH = 6


@dataclass
class ResolvedInput:
    root_dir: Path
    html_candidates: list[Path]
    temp_dir: Path | None = None
    scores: dict[Path, int] = field(default_factory=dict)

    @property
    def best(self) -> Path | None:
        return self.html_candidates[0] if self.html_candidates else None


def _iter_html(root: Path):
    for path in root.rglob("*"):
        if path.suffix.lower() in (".html", ".htm"):
            try:
                depth = len(path.relative_to(root).parts)
            except ValueError:
                depth = 0
            if depth <= _MAX_DEPTH:
                yield path


def score_html(path: Path) -> int:
    """Heuristic score for how likely a file is the lesson page (PLAN M1.3)."""
    score = 0
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return -1000
    if 'data-lesson="true"' in text:
        score += 100
    if "blocks-lesson" in text:
        score += 80
    if 'data-ba="lessonEdit.block"' in text:
        score += 60
    soup = BeautifulSoup(text, "lxml")
    if soup.title and soup.title.get_text(strip=True):
        score += 10
    body_len = len(soup.get_text(" ", strip=True))
    score += min(20, body_len // 2000)
    if "_files" in path.parent.name:
        score -= 100
    lower = path.name.lower()
    if "index" in lower or "lesson" in lower:
        score += 5
    return score


def resolve_input(input_path: Path, *, max_unpacked_bytes: int) -> ResolvedInput:
    input_path = input_path.expanduser()
    temp_dir: Path | None = None

    if input_path.is_file() and input_path.suffix.lower() == ".zip":
        temp_dir = Path(tempfile.mkdtemp(prefix="wce_"))
        log.debug("extracting zip -> {}", temp_dir)
        root = safe_extract_zip(input_path, temp_dir, max_unpacked_bytes)
    elif input_path.is_file() and input_path.suffix.lower() in (".html", ".htm"):
        return ResolvedInput(
            root_dir=input_path.parent,
            html_candidates=[input_path],
            scores={input_path: score_html(input_path)},
        )
    elif input_path.is_dir():
        root = input_path
    else:
        raise FileNotFoundError(f"input not found or unsupported: {input_path}")

    candidates = list(_iter_html(root))
    scores = {p: score_html(p) for p in candidates}
    ranked = sorted(candidates, key=lambda p: (-scores[p], len(p.parts)))
    return ResolvedInput(
        root_dir=root, html_candidates=ranked, temp_dir=temp_dir, scores=scores
    )
