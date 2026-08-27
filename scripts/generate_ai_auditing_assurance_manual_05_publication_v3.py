#!/usr/bin/env python3
"""Manual 05 publication generator v3.

Preserves v2 source-relative completeness validation and makes footer creation
idempotent across Word sections. DOCX sections inherit footers by default; adding
an identical footer to a linked second section duplicated the page footer in the
rendered PDF. This wrapper prevents that presentation defect without changing
content or release-control semantics.
"""
from __future__ import annotations

import generate_ai_auditing_assurance_manual_05_publication as v1
import generate_ai_auditing_assurance_manual_05_publication_v2 as v2  # noqa: F401

_original_add_footer = v1.add_footer


def add_footer(section, language: str):
    existing = " ".join(p.text.strip() for p in section.footer.paragraphs if p.text.strip())
    if "Manual 05" in existing:
        return
    _original_add_footer(section, language)


v1.add_footer = add_footer
v1.core.add_footer = add_footer

if __name__ == "__main__":
    raise SystemExit(v1.core.main())
