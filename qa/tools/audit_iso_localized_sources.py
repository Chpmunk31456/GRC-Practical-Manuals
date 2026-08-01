#!/usr/bin/env python3
"""Fail-closed structural and localization audit for ISO/IEC 27001/27002 ES and PT-BR sources."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import re

ROOT = Path("02-management-systems/ISO_IEC_27001_27002")
SOURCES = {
    "es-419": ROOT / "Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md",
    "pt-BR": ROOT / "Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md",
}
REPORT_MD = Path("qa/ISO_IEC_27001_27002_LOCALIZED_SOURCE_AUDIT.md")
REPORT_JSON = Path("qa/ISO_IEC_27001_27002_LOCALIZED_SOURCE_AUDIT.json")

EXPECTED_MAJOR_SECTIONS = list(range(1, 29))
EXPECTED_IMAGES = list(range(1, 10))

COMMON_PATTERNS = {
    "malformed_html_or_image_markup": [
        r"لimg\b",
        r"\bEl estilo [\"']?png",
        r"<img\b[^>]*(?<!/)>$",
    ],
    "placeholder_or_injected_text": [
        r"La vida eterna",
        r"\bSilencioso\b",
        r"\|\. \|",
    ],
    "malformed_markdown_links": [
        r"\]\s+\(#",
        r"\[[^\]]+\]\s*\(#.*\)\]\(#",
    ],
    "malformed_emphasis": [
        r"^\*\*\s+[^*]+$",
        r"^\*[^*]+\*\*$",
    ],
}

LANGUAGE_PATTERNS = {
    "es-419": {
        "untranslated_english_headings": [
            r"^#?\s*Publication and Use Notice$",
            r"^#?\s*Management Review and Corrective Action$",
            r"^#?\s*ISMS Scope and Interested Parties$",
            r"^#?\s*ISO/IEC 27001 y 27002 Foundations$",
        ],
        "known_mistranslations": [
            r"Lectura de certificación",
            r"Laboratorio de Ficción y Cartera",
            r"Valor de los empleadores de habilidades",
            r"Uso electrónico y autorizado",
            r"Contenido de la palabra",
            r"SIV\b",
            r"37 orgánicos",
        ],
    },
    "pt-BR": {
        "untranslated_english_text": [
            r"\bThe SoA\b",
            r"^#?\s*ISO/IEC 27001 e 27002 Fundações$",
        ],
        "non_brazilian_or_mixed_locale_forms": [
            r"\bcontrolos\b",
            r"\bselecção\b",
            r"\bobjectivo\b",
            r"\bactivo\b",
            r"\bregisto\b",
            r"\bplaneamento\b",
            r"\butilização\b",
        ],
        "known_mistranslations": [
            r"mudadores de carreira",
            r"Alterações da ação climática",
            r"portas do produto",
            r"Papel de ensaio de controlo",
            r"Quadro de conteúdos",
        ],
    },
}


def line_hits(text: str, patterns: list[str]) -> list[dict[str, object]]:
    hits: list[dict[str, object]] = []
    lines = text.splitlines()
    for pattern in patterns:
        rx = re.compile(pattern, re.IGNORECASE)
        for number, line in enumerate(lines, 1):
            if rx.search(line):
                hits.append({"line": number, "pattern": pattern, "text": line[:240]})
    return hits


def section_counts(text: str) -> dict[int, int]:
    counts: Counter[int] = Counter()
    for line in text.splitlines():
        match = re.match(r"^#\s+(\d+)\.\s+", line)
        if match:
            counts[int(match.group(1))] += 1
    return {n: counts[n] for n in EXPECTED_MAJOR_SECTIONS}


def image_counts(text: str) -> dict[int, int]:
    counts: dict[int, int] = {}
    for n in EXPECTED_IMAGES:
        counts[n] = len(re.findall(rf"media/image{n}\.png", text, flags=re.IGNORECASE))
    return counts


def table_signal(text: str) -> dict[str, int]:
    lines = text.splitlines()
    pipe_rows = sum(1 for line in lines if line.count("|") >= 2)
    separator_rows = sum(1 for line in lines if re.match(r"^\s*\|?\s*:?-{3,}", line))
    collapsed_rule_rows = sum(1 for line in lines if re.match(r"^-{20,}$", line))
    return {
        "pipe_rows": pipe_rows,
        "separator_rows": separator_rows,
        "collapsed_rule_rows": collapsed_rule_rows,
    }


def audit_language(language: str, path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    findings: dict[str, list[dict[str, object]]] = {}
    for category, patterns in COMMON_PATTERNS.items():
        hits = line_hits(text, patterns)
        if hits:
            findings[category] = hits
    for category, patterns in LANGUAGE_PATTERNS[language].items():
        hits = line_hits(text, patterns)
        if hits:
            findings[category] = hits

    sections = section_counts(text)
    missing_sections = [n for n, count in sections.items() if count == 0]
    duplicate_sections = [n for n, count in sections.items() if count > 1]
    images = image_counts(text)
    missing_images = [n for n, count in images.items() if count == 0]

    return {
        "language": language,
        "source": str(path),
        "status": "FAIL" if findings or missing_sections or duplicate_sections or missing_images else "PASS",
        "findings": findings,
        "major_section_counts": sections,
        "missing_major_sections": missing_sections,
        "duplicate_major_sections": duplicate_sections,
        "image_reference_counts": images,
        "missing_image_references": missing_images,
        "table_signals": table_signal(text),
    }


def render_markdown(results: list[dict[str, object]]) -> str:
    lines = [
        "# ISO/IEC 27001 and 27002 Localized Source Audit",
        "",
        "## Result",
        "",
        "**FAIL-CLOSED**" if any(r["status"] == "FAIL" for r in results) else "**PASS**",
        "",
        "This deterministic audit identifies structural and known localization defects. It does not replace native-language, standards, legal, accessibility, or page-level review.",
        "",
    ]
    for result in results:
        lines.extend([
            f"## {result['language']}",
            "",
            f"- Source: `{result['source']}`",
            f"- Status: **{result['status']}**",
            f"- Missing major sections: {result['missing_major_sections'] or 'none'}",
            f"- Duplicate major sections: {result['duplicate_major_sections'] or 'none'}",
            f"- Missing image references: {result['missing_image_references'] or 'none'}",
            f"- Table signals: `{result['table_signals']}`",
            "",
            "### Findings",
            "",
        ])
        findings = result["findings"]
        if not findings:
            lines.append("No configured findings.")
        else:
            for category, hits in findings.items():
                lines.append(f"#### {category}")
                for hit in hits:
                    lines.append(f"- Line {hit['line']}: `{hit['text']}`")
                lines.append("")
    lines.extend([
        "## Release implication",
        "",
        "Any FAIL blocks localized DOCX/PDF rebuild and publication-readiness claims until the source defects are repaired and this audit passes at the exact candidate SHA.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    results = [audit_language(language, path) for language, path in SOURCES.items()]
    REPORT_JSON.write_text(json.dumps({"results": results}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT_MD.write_text(render_markdown(results), encoding="utf-8")
    failed = any(result["status"] == "FAIL" for result in results)
    print(f"ISO localized source audit: {'FAIL' if failed else 'PASS'}")
    for result in results:
        finding_count = sum(len(v) for v in result["findings"].values())
        print(f"{result['language']}: {result['status']} ({finding_count} configured findings)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
