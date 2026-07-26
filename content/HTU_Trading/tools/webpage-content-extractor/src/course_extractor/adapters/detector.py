"""Select the best adapter for a given soup."""

from __future__ import annotations

from bs4 import BeautifulSoup

from .rise_adapter import RiseAdapter

_ADAPTERS = [RiseAdapter()]


def detect_adapter(soup: BeautifulSoup):
    best = max(_ADAPTERS, key=lambda a: a.confidence(soup))
    return best, best.confidence(soup)
