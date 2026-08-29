#!/usr/bin/env python3
"""Manual 03 publication generator, revision 3.

Keeps the semantic graph renderer from v2, makes footer generation idempotent,
and localizes generator-owned publication boilerplate/captions for each edition.
Controlled Markdown source meaning is unchanged; human semantic review remains
mandatory for localized editions.
"""
from __future__ import annotations

import generate_nist_ai_rmf_manual_03_publication as base
import generate_nist_ai_rmf_manual_03_publication_v2  # noqa: F401  (installs semantic graph renderer)

_original_add_footer = base.add_footer
_original_build_docx = base.build_docx

LOCALIZED = {
    "en": {
        "title": "Manual 03 - NIST AI Risk Management Framework Implementation",
        "status": "CONTROLLED PUBLICATION QA CANDIDATE",
        "control": "Controlled source revision: {head} | Language: en | NIST AI RMF 1.0 / NIST AI 100-1 baseline; version-aware and subject to source-watch controls.",
        "boundary": "Assurance boundary: This practical implementation manual does not certify an AI system, establish legal compliance, prove trustworthy-AI achievement, or provide an audit opinion.",
        "implementation_heading": "Implementation paths and operating model",
        "chapter_heading": "Controlled 32-chapter manual",
        "implementation_caption": "Figure {number}. Implementation memory graphic",
        "chapter_caption": "Figure {number}. Chapter memory graphic",
        "footer": "Manual 03 | Controlled publication QA candidate | ",
        "subject": "Manual 03 controlled publication-QA artifact; language en; source head {head}",
        "comments": "Generation and QA do not establish certification, legal compliance, trustworthy-AI achievement, or an audit opinion.",
    },
    "es-419": {
        "title": "Manual 03 - Implementación del Marco de Gestión de Riesgos de IA del NIST",
        "status": "CANDIDATO CONTROLADO PARA QA DE PUBLICACIÓN",
        "control": "Revisión de fuente controlada: {head} | Idioma: es-419 | Línea base NIST AI RMF 1.0 / NIST AI 100-1; control de versiones y vigilancia de fuentes requeridos.",
        "boundary": "Límite de aseguramiento: Este manual práctico de implementación no certifica un sistema de IA, no establece cumplimiento legal, no demuestra el logro de una IA confiable ni proporciona una opinión de auditoría.",
        "implementation_heading": "Rutas de implementación y modelo operativo",
        "chapter_heading": "Manual controlado de 32 capítulos",
        "implementation_caption": "Figura {number}. Gráfico de memoria de implementación",
        "chapter_caption": "Figura {number}. Gráfico de memoria del capítulo",
        "footer": "Manual 03 | Candidato controlado para QA de publicación | ",
        "subject": "Artefacto controlado de QA de publicación del Manual 03; idioma es-419; revisión de fuente {head}",
        "comments": "La generación y el QA no establecen certificación, cumplimiento legal, logro de IA confiable ni una opinión de auditoría.",
    },
    "pt-BR": {
        "title": "Manual 03 - Implementação do Marco de Gestão de Riscos de IA do NIST",
        "status": "CANDIDATO CONTROLADO PARA QA DE PUBLICAÇÃO",
        "control": "Revisão da fonte controlada: {head} | Idioma: pt-BR | Linha de base NIST AI RMF 1.0 / NIST AI 100-1; controle de versão e vigilância de fontes obrigatórios.",
        "boundary": "Limite de asseguração: Este manual prático de implementação não certifica um sistema de IA, não estabelece conformidade legal, não comprova o alcance de IA confiável nem fornece uma opinião de auditoria.",
        "implementation_heading": "Caminhos de implementação e modelo operacional",
        "chapter_heading": "Manual controlado de 32 capítulos",
        "implementation_caption": "Figura {number}. Gráfico de memória de implementação",
        "chapter_caption": "Figura {number}. Gráfico de memória do capítulo",
        "footer": "Manual 03 | Candidato controlado para QA de publicação | ",
        "subject": "Artefato controlado de QA de publicação do Manual 03; idioma pt-BR; revisão da fonte {head}",
        "comments": "A geração e o QA não estabelecem certificação, conformidade legal, alcance de IA confiável nem opinião de auditoria.",
    },
}


def add_footer_once(section, language: str):
    """Add the controlled footer once even when Word sections share a footer part."""
    footer = section.footer
    existing = "\n".join(p.text for p in footer.paragraphs)
    if "Manual 03 |" in existing:
        return
    _original_add_footer(section, language)


def _replace_paragraph(paragraph, text: str, language: str, *, keep_next: bool = False):
    paragraph.text = text
    for run in paragraph.runs:
        base.set_run_font(run, language)
    base.set_paragraph_keep(paragraph, keep_next=keep_next)


def _localize_generated_docx(path, language: str, source_head: str):
    """Localize only generator-owned boilerplate and captions after controlled build."""
    doc = base.Document(path)
    meta = LOCALIZED[language]

    # Core properties are generator-owned metadata, not controlled source prose.
    doc.core_properties.title = meta["title"]
    doc.core_properties.subject = meta["subject"].format(head=source_head)
    doc.core_properties.comments = meta["comments"]

    title_done = status_done = control_done = boundary_done = False
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        style_name = paragraph.style.name if paragraph.style else ""

        if not title_done and style_name == "Title":
            _replace_paragraph(paragraph, meta["title"], language)
            paragraph.alignment = base.WD_ALIGN_PARAGRAPH.CENTER
            title_done = True
            continue
        if not status_done and text == base.LANG_META[language]["status"]:
            _replace_paragraph(paragraph, meta["status"], language)
            paragraph.alignment = base.WD_ALIGN_PARAGRAPH.CENTER
            status_done = True
            continue
        if text.startswith("Controlled source revision:"):
            _replace_paragraph(paragraph, meta["control"].format(head=source_head), language)
            paragraph.alignment = base.WD_ALIGN_PARAGRAPH.CENTER
            control_done = True
            continue
        if text.startswith("Assurance boundary:"):
            _replace_paragraph(paragraph, meta["boundary"], language)
            boundary_done = True
            continue
        if text == "Implementation paths and operating model":
            _replace_paragraph(paragraph, meta["implementation_heading"], language, keep_next=True)
            continue
        if text == "Controlled 32-chapter manual":
            _replace_paragraph(paragraph, meta["chapter_heading"], language, keep_next=True)
            continue
        if text.startswith("Figure ") and "memory graphic" in text:
            number = text.split(".", 1)[0].split()[-1]
            template = meta["implementation_caption"] if "Implementation" in text else meta["chapter_caption"]
            _replace_paragraph(paragraph, template.format(number=number), language, keep_next=True)
            paragraph.alignment = base.WD_ALIGN_PARAGRAPH.CENTER

    if not all((title_done, status_done, control_done, boundary_done)):
        raise ValueError(
            f"{language} generated boilerplate localization incomplete: "
            f"title={title_done}, status={status_done}, control={control_done}, boundary={boundary_done}"
        )

    # Sections can share footer parts; rewrite each unique footer paragraph safely.
    seen = set()
    for section in doc.sections:
        footer = section.footer
        key = id(footer._element)
        if key in seen:
            continue
        seen.add(key)
        for paragraph in footer.paragraphs:
            if "Manual 03 |" not in paragraph.text:
                continue
            # Preserve the PAGE field by rebuilding text + field.
            paragraph.clear()
            paragraph.alignment = base.WD_ALIGN_PARAGRAPH.CENTER
            run = paragraph.add_run(meta["footer"])
            base.set_run_font(run, language, size=8)
            field = base.OxmlElement("w:fldSimple")
            field.set(base.qn("w:instr"), "PAGE")
            paragraph._p.append(field)

    doc.save(path)


def build_docx_localized(source, out_path, image_dir, source_head):
    count = _original_build_docx(source, out_path, image_dir, source_head)
    _localize_generated_docx(out_path, source.language, source_head)
    return count


base.add_footer = add_footer_once
base.build_docx = build_docx_localized

if __name__ == "__main__":
    raise SystemExit(base.main())
