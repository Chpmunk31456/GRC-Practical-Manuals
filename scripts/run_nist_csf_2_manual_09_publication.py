#!/usr/bin/env python3
"""Safe runner for Manual 09 NIST CSF 2.0 publication generation.

Prevents inherited publication-adapter bindings from reading or relabeling an
upstream manual while preserving semantic, accessibility, provenance, security,
and human-review gates.
"""
from __future__ import annotations

import generate_nist_csf_2_manual_09_publication as manual09
import generate_ai_security_lifecycle_manual_07_publication as manual07
import generate_hipaa_implementation_manual_06_publication as hipaa06


def find_localized_chapters(language: str):
    chapters: dict[int, str] = {}
    used: list[str] = []
    for path in sorted(manual09.source_dir(language).glob("*.md")):
        if path.name in {"RUTAS_DE_IMPLEMENTACION_MANUAL_09.md", "CAMINHOS_DE_IMPLEMENTACAO_MANUAL_09.md"}:
            continue
        found = manual09.core.split_chapters(path.read_text(encoding="utf-8"))
        if not found:
            continue
        for number, body in found.items():
            if number in chapters and chapters[number] != body:
                raise ValueError(f"conflicting chapter {number} for {language}: {path}")
            chapters[number] = body
        used.append(str(path.relative_to(manual09.ROOT)))
    expected = set(range(1, 33))
    if set(chapters) != expected:
        raise ValueError(f"{language} chapter inventory invalid: {sorted(chapters)}")
    return "\n".join(chapters[n].rstrip() for n in range(1, 33)) + "\n", used


# Manual 07 inherits its renderer through Manual 06. Manual 06 retains the raw
# Manual 03 renderer before any manual-specific relabeling wrapper. Bind Manual
# 09 directly to that raw helper so the image title and alt-text cannot inherit a
# Manual 06/07 label.
manual09._base_render = hipaa06._base_render
manual09._base_alt = hipaa06._base_alt

manual09.find_localized_chapters = find_localized_chapters
manual09.core.find_localized_chapters = find_localized_chapters
manual09.base.find_localized_chapters = find_localized_chapters
manual07.find_localized_chapters = find_localized_chapters
hipaa06.find_localized_chapters = find_localized_chapters

if __name__ == "__main__":
    raise SystemExit(manual09.core.main())
