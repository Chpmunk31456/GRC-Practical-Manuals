#!/usr/bin/env python3
"""Integrate reviewed NIST CSF 2.0 rewrite blocks into complete target manuals.

This script performs deterministic source integration only. It does not mark the
resulting editions publication-ready and does not modify DOCX or PDF packages.
"""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

EDIT_NOTE_PATTERNS = (
    r"\n---\n\n\*\*Estado editorial:\*\*.*\Z",
    r"\n---\n\n\*\*Status editorial:\*\*.*\Z",
)

STAGING_HEADER_PATTERNS = (
    r"\A# NIST CSF 2\.0[^\n]*\n(?:\n|## (?:Capítulos?|Capitulo|Capítulo)[^\n]*\n|\*\*[^\n]*\*\*\s*\n|\*[^\n]*\*\s*\n)*",
)

JOBS = {
    "es-419": {
        "blocks": [
            "qa/rewrite/NIST_CSF_2_ES_OPENING_CH1_CH3_REVIEWED.md",
            "qa/rewrite/NIST_CSF_2_ES_BLOCK_02_GOVERN_IDENTIFY.md",
            "qa/rewrite/NIST_CSF_2_ES_BLOCK_03_PROTECT_DETECT_RESPOND_RECOVER.md",
            "qa/rewrite/NIST_CSF_2_ES_CH10_15_REVIEWED.md",
            "qa/rewrite/NIST_CSF_2_ES_CH16_24_REVIEWED.md",
        ],
        "target": "01-foundations/NIST_CSF_2/Espanol/NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_Espanol_v1.0.md",
    },
    "pt-BR": {
        "blocks": [
            "qa/rewrite/NIST_CSF_2_PTBR_OPENING_CH1_CH3_REVIEWED.md",
            "qa/rewrite/NIST_CSF_2_PTBR_BLOCK_02_GOVERN_IDENTIFY.md",
            "qa/rewrite/NIST_CSF_2_PTBR_BLOCK_03_PROTEGER_DETECTAR_RESPONDER_RECUPERAR.md",
            "qa/rewrite/NIST_CSF_2_PTBR_CH10_15_REVIEWED.md",
            "qa/rewrite/NIST_CSF_2_PTBR_CH16_24_REVIEWED.md",
        ],
        "target": "01-foundations/NIST_CSF_2/Portugues_BR/NIST_CSF_2_Practical_GRC_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md",
    },
}


def clean_block(text: str, *, first_block: bool) -> str:
    cleaned = text.replace("\r\n", "\n").strip()
    for pattern in EDIT_NOTE_PATTERNS:
        cleaned = re.sub(pattern, "", cleaned, flags=re.DOTALL)

    # Remove internal staging titles from every block except the opening block.
    if not first_block:
        lines = cleaned.splitlines()
        while lines and (
            lines[0].startswith("# NIST CSF 2.0")
            or lines[0].startswith("## Capítulo")
            or lines[0].startswith("## Capitulo")
            or lines[0].startswith("## Capítulos")
            or lines[0].startswith("**Estado:")
            or lines[0].startswith("**Status:")
            or lines[0].startswith("**Idioma:")
            or lines[0].startswith("**Regla editorial:")
            or lines[0].startswith("**Regra editorial:")
            or not lines[0].strip()
        ):
            lines.pop(0)
        cleaned = "\n".join(lines).strip()

    # Normalize reviewed Chapter 10–15 staging headings to final chapter headings.
    cleaned = re.sub(
        r"^##\s+(?:Capítulo|Capitulo)\s+(\d+)\.\s+",
        r"# \1. ",
        cleaned,
        flags=re.MULTILINE,
    )
    return cleaned.strip()


def validate_combined(language: str, text: str) -> None:
    headings = {int(n) for n in re.findall(r"^#\s+(\d+)\.", text, flags=re.MULTILINE)}
    missing = [number for number in range(1, 25) if number not in headings]
    duplicates = sorted(number for number in headings if list(re.findall(rf"^#\s+{number}\.", text, flags=re.MULTILINE)).count(f"# {number}.") > 1)
    if missing:
        raise ValueError(f"{language}: missing chapter headings: {missing}")

    if language == "es-419":
        forbidden = ["Tiros", "Policía (GV.PO)", "Función del PROTECTO", "Silencio"]
    else:
        forbidden = ["COMPLIANÇA", "Função do Governo", "Conteúdo verdadeiro da palavra"]

    found = [term for term in forbidden if term in text]
    if found:
        raise ValueError(f"{language}: known defective terms remain: {found}")

    if len(text) < 20_000:
        raise ValueError(f"{language}: integrated manual is unexpectedly short ({len(text)} chars)")


def main() -> None:
    for language, job in JOBS.items():
        block_paths = [ROOT / item for item in job["blocks"]]
        missing_files = [str(path.relative_to(ROOT)) for path in block_paths if not path.is_file()]
        if missing_files:
            raise FileNotFoundError(f"{language}: missing reviewed blocks: {missing_files}")

        cleaned_blocks = [
            clean_block(path.read_text(encoding="utf-8"), first_block=(index == 0))
            for index, path in enumerate(block_paths)
        ]
        combined = "\n\n".join(cleaned_blocks).rstrip() + "\n"
        validate_combined(language, combined)

        target = ROOT / job["target"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(combined, encoding="utf-8", newline="\n")
        print(f"Integrated {language}: {target.relative_to(ROOT)} ({len(combined)} chars)")


if __name__ == "__main__":
    main()
