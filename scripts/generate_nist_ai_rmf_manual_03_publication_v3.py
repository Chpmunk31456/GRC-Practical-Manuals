#!/usr/bin/env python3
"""Manual 03 publication generator, revision 3.

Keeps the semantic graph renderer from v2 and makes footer generation
idempotent across linked Word sections so the page footer is not duplicated.
"""
from __future__ import annotations

import generate_nist_ai_rmf_manual_03_publication as base
import generate_nist_ai_rmf_manual_03_publication_v2  # noqa: F401  (installs semantic graph renderer)

_original_add_footer = base.add_footer


def add_footer_once(section, language: str):
    """Add the controlled footer once even when Word sections share a footer part."""
    footer = section.footer
    existing = "\n".join(p.text for p in footer.paragraphs)
    if "Manual 03 | Controlled publication QA candidate" in existing:
        return
    _original_add_footer(section, language)


base.add_footer = add_footer_once

if __name__ == "__main__":
    raise SystemExit(base.main())
