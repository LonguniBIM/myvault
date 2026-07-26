"""Minimal, dependency-free logging helpers."""

from __future__ import annotations

import sys
from typing import Any

_VERBOSE = False


def set_verbose(value: bool) -> None:
    global _VERBOSE
    _VERBOSE = value


def info(msg: str, *args: Any) -> None:
    print(msg.format(*args) if args else msg, file=sys.stderr)


def debug(msg: str, *args: Any) -> None:
    if _VERBOSE:
        print("  " + (msg.format(*args) if args else msg), file=sys.stderr)


def warn(msg: str, *args: Any) -> None:
    print("WARN: " + (msg.format(*args) if args else msg), file=sys.stderr)
