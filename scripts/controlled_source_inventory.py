#!/usr/bin/env python3
"""Reusable controlled-source inventory helpers.

Classify Markdown by what it contains instead of assuming every .md file in a
source directory is a chapter block. This prevents valid implementation,
appendix, QA, or evidence files from corrupting chapter-count gates.

The helper is intentionally semantic-light: it identifies deterministic source
roles and chapter-number coverage. Human semantic review remains separate.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

CHAPTER_PATTERNS = (
    re.compile(r"(?mi)^##\s+Chapter\s+(\d{1,2})\b"),
    re.compile(r"(?mi)^##\s+Cap[ií]tulo\s+(\d{1,2})\b"),
    re.compile(r"(?mi)^##\s+Cap[ií]tulo\s+(\d{1,2})\b"),
    re.compile(r"(?mi)^#\s+(\d{1,2})\.\s+"),
)


@dataclass(frozen=True)
class SourceInventory:
    chapter_files: tuple[Path, ...]
    support_files: tuple[Path, ...]
    chapter_numbers: frozenset[int]


def chapter_numbers(text: str) -> set[int]:
    found: set[int] = set()
    for pattern in CHAPTER_PATTERNS:
        found.update(int(value) for value in pattern.findall(text))
    return found


def inventory_markdown(directory: Path) -> SourceInventory:
    chapter_files: list[Path] = []
    support_files: list[Path] = []
    numbers: set[int] = set()

    if not directory.is_dir():
        return SourceInventory((), (), frozenset())

    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        found = chapter_numbers(text)
        if found:
            chapter_files.append(path)
            numbers.update(found)
        else:
            support_files.append(path)

    return SourceInventory(tuple(chapter_files), tuple(support_files), frozenset(numbers))


def self_test() -> list[str]:
    """Regression fixtures for the source-role classifier."""
    errors: list[str] = []
    fixtures = {
        "english": ("## Chapter 01 — Scope\nBody", {1}),
        "spanish": ("## Capítulo 09 — Riesgo\nCuerpo", {9}),
        "portuguese": ("## Capítulo 17 — Risco\nCorpo", {17}),
        "numbered": ("# 32. Closure\nBody", {32}),
        "support": ("# Implementation paths\nNo numbered chapter heading here.", set()),
    }
    for name, (text, expected) in fixtures.items():
        actual = chapter_numbers(text)
        if actual != expected:
            errors.append(f"source-role regression {name}: expected {sorted(expected)}, got {sorted(actual)}")
    return errors
