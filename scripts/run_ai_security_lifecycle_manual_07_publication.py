#!/usr/bin/env python3
"""Safe runner for Manual 07 publication generation.

Repairs the chapter-loader binding in the Manual 07 adapter without weakening any
publication, semantic, accessibility, provenance, security, or human approval gate.
"""
from __future__ import annotations

import generate_ai_security_lifecycle_manual_07_publication as manual07


def find_localized_chapters(language: str):
    chapters: dict[int, str] = {}
    used: list[str] = []
    for path in sorted(manual07.source_dir(language).glob("*.md")):
        found = manual07.base.split_chapters(path.read_text(encoding="utf-8"))
        if not found:
            continue
        for number, body in found.items():
            if number in chapters and chapters[number] != body:
                raise ValueError(f"conflicting chapter {number} for {language}: {path}")
            chapters[number] = body
        used.append(str(path.relative_to(manual07.ROOT)))
    expected = set(range(1, 33))
    if set(chapters) != expected:
        raise ValueError(f"{language} chapter inventory invalid: {sorted(chapters)}")
    return "\n".join(chapters[n].rstrip() for n in range(1, 33)) + "\n", used


manual07.base.find_localized_chapters = find_localized_chapters
manual07.core.find_localized_chapters = find_localized_chapters

if __name__ == "__main__":
    raise SystemExit(manual07.core.main())
