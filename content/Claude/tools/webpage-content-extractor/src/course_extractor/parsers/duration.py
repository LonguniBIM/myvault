"""Parse audio durations from Rise audio-player DOM."""

from __future__ import annotations

import re

from bs4 import Tag

_TIMER = re.compile(r"(\d+):(\d{2})")


def parse_valuemax(container: Tag) -> float | None:
    handle = container.select_one(".audio-player__tracker-handle[aria-valuemax]")
    if handle is None:
        handle = container.select_one("[aria-valuemax]")
    if handle is None:
        return None
    try:
        return float(handle["aria-valuemax"])
    except (KeyError, TypeError, ValueError):
        return None


def parse_timer_label(container: Tag) -> str | None:
    timer = container.select_one(".audio-player__timer")
    if timer is None:
        return None
    text = timer.get_text(strip=True)
    return text or None


def timer_to_seconds(label: str | None) -> float | None:
    if not label:
        return None
    m = _TIMER.search(label)
    if not m:
        return None
    return int(m.group(1)) * 60 + int(m.group(2))
