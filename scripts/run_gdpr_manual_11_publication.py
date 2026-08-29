#!/usr/bin/env python3
"""Safe runner for Manual 11 GDPR publication generation.

Prevents inherited Manual 10/09/07/06 publication bindings from reading or
relabeling the wrong manual while preserving legal/privacy, semantic,
accessibility, provenance, security, and human-review gates.
"""
from __future__ import annotations

import generate_gdpr_manual_11_publication as manual11
import generate_nist_rmf_800_53_manual_10_publication as manual10
import generate_nist_csf_2_manual_09_publication as manual09
import generate_ai_security_lifecycle_manual_07_publication as manual07
import generate_hipaa_implementation_manual_06_publication as hipaa06


def find_localized_chapters(language: str):
    chapters: dict[int, str] = {}
    used: list[str] = []
    for path in sorted(manual11.source_dir(language).glob("*.md")):
        if path.name in {"RUTAS_DE_IMPLEMENTACION_MANUAL_11.md", "CAMINHOS_DE_IMPLEMENTACAO_MANUAL_11.md"}:
            continue
        found = manual11.core.split_chapters(path.read_text(encoding="utf-8"))
        if not found:
            continue
        for number, body in found.items():
            if number in chapters and chapters[number] != body:
                raise ValueError(f"conflicting chapter {number} for {language}: {path}")
            chapters[number] = body
        used.append(str(path.relative_to(manual11.ROOT)))
    expected = set(range(1, 33))
    if set(chapters) != expected:
        raise ValueError(f"{language} chapter inventory invalid: {sorted(chapters)}")
    return "\n".join(chapters[n].rstrip() for n in range(1, 33)) + "\n", used


# Bind Manual 11 to the raw renderer/alt-text helper retained before
# manual-specific relabeling wrappers are applied.
manual11._base_render = hipaa06._base_render
manual11._base_alt = hipaa06._base_alt

manual11.find_localized_chapters = find_localized_chapters
manual11.core.find_localized_chapters = find_localized_chapters
manual11.base.find_localized_chapters = find_localized_chapters
manual10.find_localized_chapters = find_localized_chapters
manual09.find_localized_chapters = find_localized_chapters
manual07.find_localized_chapters = find_localized_chapters
hipaa06.find_localized_chapters = find_localized_chapters

if __name__ == "__main__":
    raise SystemExit(manual11.core.main())
