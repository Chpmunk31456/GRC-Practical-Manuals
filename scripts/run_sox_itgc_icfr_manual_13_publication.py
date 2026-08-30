#!/usr/bin/env python3
"""Safe runner for Manual 13 SOX ITGC / ICFR publication generation."""
from __future__ import annotations

from docx import Document
from docx.enum.section import WD_SECTION

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

_base_build_docx = manual13.build_docx


def build_docx_with_practitioner_appendix(source, out_path, image_dir, source_head):
    graphic_count = _base_build_docx(source, out_path, image_dir, source_head)
    language = source.language
    if language == "en":
        appendix = manual13.MANUAL / "English" / "source" / "MANUAL_13_PRACTITIONER_APPENDIX.md"
        heading = "Practitioner evidence and testing appendix"
    elif language == "es-419":
        appendix = manual13.MANUAL / "Spanish_es-419" / "source" / "APENDICE_EVIDENCIA_PRACTICANTE_MANUAL_13.md"
        heading = "Apéndice de evidencia y pruebas para practicantes"
    else:
        appendix = manual13.MANUAL / "Portuguese_pt-BR" / "source" / "APENDICE_EVIDENCIA_PRATICANTE_MANUAL_13.md"
        heading = "Apêndice de evidência e testes para praticantes"
    if not appendix.is_file():
        raise ValueError(f"missing practitioner appendix for {language}: {appendix}")
    doc = Document(out_path)
    doc.add_section(WD_SECTION.NEW_PAGE)
    manual13.add_footer(doc.sections[-1], language)
    h = doc.add_paragraph(heading, style="Heading 1")
    manual13.core.set_paragraph_keep(h, keep_next=True)
    counter = [graphic_count]
    manual13.core.add_markdown(doc, appendix.read_text(encoding="utf-8"), language, image_dir, counter, "Appendix")
    if counter[0] != graphic_count:
        raise ValueError(f"unexpected appendix graphic count change for {language}")
    for p in doc.paragraphs:
        for r in p.runs:
            manual13.core.set_run_font(r, language)
    doc.save(out_path)
    return graphic_count


manual13.core.build_docx = build_docx_with_practitioner_appendix

if __name__ == "__main__":
    raise SystemExit(manual13.core.main())
