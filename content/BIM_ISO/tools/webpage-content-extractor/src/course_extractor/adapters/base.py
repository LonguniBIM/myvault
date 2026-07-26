"""Adapter contract shared by all content-platform parsers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

from bs4 import BeautifulSoup

from ..config import Config
from ..models import DocumentIR


@dataclass
class ParseContext:
    html_path: Path
    root_dir: Path
    config: Config
    document: DocumentIR


class ContentAdapter(Protocol):
    name: str

    def confidence(self, soup: BeautifulSoup) -> float: ...

    def parse(self, soup: BeautifulSoup, ctx: ParseContext) -> DocumentIR: ...
