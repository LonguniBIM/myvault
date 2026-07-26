"""Load saved HTML into a BeautifulSoup tree without running any JavaScript."""

from __future__ import annotations

import re
from pathlib import Path

from bs4 import BeautifulSoup

_SAVED_FROM = re.compile(r"saved from url=\(\d+\)(\S+)")


def load_html(path: Path) -> BeautifulSoup:
    text = path.read_text(encoding="utf-8", errors="replace")
    return BeautifulSoup(text, "lxml")


def extract_source_url(path: Path) -> str | None:
    """Read the ``<!-- saved from url=(NNNN)... -->`` comment if present."""
    head = path.read_text(encoding="utf-8", errors="replace")[:4000]
    m = _SAVED_FROM.search(head)
    return m.group(1) if m else None
