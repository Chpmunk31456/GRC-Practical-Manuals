#!/usr/bin/env python3
"""Safe runner for Manual 08 publication generation.

Prevents inherited adapter recursion while preserving the existing publication,
semantic, accessibility, provenance, security, and human approval gates.
"""
from __future__ import annotations

import generate_vendor_risk_lifecycle_manual_08_publication as manual08
import generate_ai_security_lifecycle_manual_07_publication as manual07
import generate_hipaa_implementation_manual_06_publication as hipaa06


def find_localized_chapters(language: str):
    chapters: dict[int, str] = {}
    used: list[str] = []
    for path in sorted(manual08.source_dir(language).glob("*.md")):
        found = manual08.core.split_chapters(path.read_text(encoding="utf-8"))
        if not found:
            continue
        for number, body in found.items():
            if number in chapters and chapters[number] != body:
                raise ValueError(f"conflicting chapter {number} for {language}: {path}")
            chapters[number] = body
        used.append(str(path.relative_to(manual08.ROOT)))
    expected = set(range(1, 33))
    if set(chapters) != expected:
        raise ValueError(f"{language} chapter inventory invalid: {sorted(chapters)}")
    return "\n".join(chapters[n].rstrip() for n in range(1, 33)) + "\n", used


# Patch every inherited module-level binding that participates in generation or
# DOCX visibility inspection. This preserves inspection itself while ensuring it
# reads Manual 08's controlled source rather than re-entering the Manual 07 adapter.
manual08.find_localized_chapters = find_localized_chapters
manual08.core.find_localized_chapters = find_localized_chapters
manual08.base.find_localized_chapters = find_localized_chapters
manual07.find_localized_chapters = find_localized_chapters
hipaa06.find_localized_chapters = find_localized_chapters

if __name__ == "__main__":
    raise SystemExit(manual08.core.main())
