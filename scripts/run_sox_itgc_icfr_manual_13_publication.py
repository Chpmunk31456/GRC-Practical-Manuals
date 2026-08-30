#!/usr/bin/env python3
"""Safe runner for Manual 13 SOX ITGC / ICFR publication generation."""
from __future__ import annotations

import generate_sox_itgc_icfr_manual_13_publication as manual13
import generate_ccpa_cpra_manual_12_publication as manual12
import generate_gdpr_manual_11_publication as manual11
import generate_nist_rmf_800_53_manual_10_publication as manual10
import generate_nist_csf_2_manual_09_publication as manual09
import generate_ai_security_lifecycle_manual_07_publication as manual07
import generate_hipaa_implementation_manual_06_publication as hipaa06


def find_localized_chapters(language: str):
    return manual13.find_localized_chapters(language)


# Bind directly to the earliest retained generic renderer/alt-text helper so
# inherited manual-specific wrappers cannot relabel Manual 13 artifacts.
manual13.core.render_mermaid_memory_graphic = hipaa06._base_render
manual13.core.set_image_alt_text = hipaa06._base_alt
manual13.core.find_localized_chapters = find_localized_chapters
manual13.core.find_implementation = manual13.find_implementation
manual12.find_localized_chapters = find_localized_chapters
manual11.find_localized_chapters = find_localized_chapters
manual10.find_localized_chapters = find_localized_chapters
manual09.find_localized_chapters = find_localized_chapters
manual07.find_localized_chapters = find_localized_chapters
hipaa06.find_localized_chapters = find_localized_chapters

if __name__ == "__main__":
    raise SystemExit(manual13.core.main())
