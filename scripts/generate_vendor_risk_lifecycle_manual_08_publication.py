#!/usr/bin/env python3
"""Safe runner for Manual 08 publication generation.

Prevents inherited adapter recursion, stale upstream labels, and linked-section
footer duplication while preserving fail-closed publication QA controls.
"""
from __future__ import annotations

import generate_vendor_risk_lifecycle_manual_08_publication as manual08
import generate_ai_security_lifecycle_manual_07_publication as manual07
import generate_hipaa_implementation_manual_06_publication as hipaa06


FIGURE_CAPTIONS = {
    "en": "Figure {number}. Implementation memory graphic",
    "es-419": "Figura {number}. Gráfico de memoria de implementación",
    "pt-BR": "Figura {number}. Gráfico de memória de implementação",
}


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


# Manual 06 retains the raw Manual 03 renderer and alt-text helper before any
# Manual 07 relabeling wrapper. Bind Manual 08 to the raw helpers so generated
# image titles cannot inherit an upstream manual number.
manual08._base_render = hipaa06._base_render
manual08._base_alt = hipaa06._base_alt

_base_build_docx = manual08.build_docx


def _rewrite_footer(section, language: str):
    """Give each section one independent Manual 08 footer."""
    section.footer.is_linked_to_previous = False
    p = section.footer.paragraphs[0]
    p.clear()
    p.alignment = manual08.WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f"Manual 08 | {manual08.LANG_META[language]['status']} | ")
    manual08.core.set_run_font(run, language, size=8)
    field = manual08.OxmlElement("w:fldSimple")
    field.set(manual08.qn("w:instr"), "PAGE")
    p._p.append(field)


def build_docx(source, out_path, image_dir, source_head):
    """Generate with Manual 08 controls, then normalize captions and footers."""
    count = _base_build_docx(source, out_path, image_dir, source_head)
    doc = manual08.Document(out_path)
    template = FIGURE_CAPTIONS[source.language]
    changed = False
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if not text.startswith("Figure ") or "Implementation memory graphic" not in text:
            continue
        number = text.split(".", 1)[0].split()[-1]
        paragraph.text = template.format(number=number)
        paragraph.alignment = manual08.WD_ALIGN_PARAGRAPH.CENTER
        manual08.core.set_paragraph_keep(paragraph, keep_next=True)
        for run in paragraph.runs:
            manual08.core.set_run_font(run, source.language)
        changed = True
    for section in doc.sections:
        _rewrite_footer(section, source.language)
        changed = True
    if changed:
        doc.save(out_path)
    return count


# Patch every inherited module-level binding that participates in generation or
# DOCX visibility inspection. This preserves inspection itself while ensuring it
# reads Manual 08's controlled source rather than re-entering the Manual 07 adapter.
manual08.find_localized_chapters = find_localized_chapters
manual08.core.find_localized_chapters = find_localized_chapters
manual08.base.find_localized_chapters = find_localized_chapters
manual07.find_localized_chapters = find_localized_chapters
hipaa06.find_localized_chapters = find_localized_chapters
manual08.build_docx = build_docx
manual08.core.build_docx = build_docx

if __name__ == "__main__":
    raise SystemExit(manual08.core.main())
