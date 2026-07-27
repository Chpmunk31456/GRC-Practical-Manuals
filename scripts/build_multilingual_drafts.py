#!/usr/bin/env python3
"""Create Spanish and Brazilian Portuguese Markdown drafts from extracted English GRC sources.

The script uses locally installed Argos Translate models. It preserves fenced code blocks,
URLs, inline code, Markdown link targets, and common framework/control identifiers. Generated
files are explicitly labeled as machine-assisted drafts pending human language review.
"""
from __future__ import annotations

import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parents[1]

LANGUAGES = {
    "es": {
        "folder": "Espanol",
        "label": "Español (América Latina)",
        "notice": (
            "> **Estado de revisión:** Borrador de traducción asistida por máquina. Requiere revisión humana de "
            "terminología, significado, enlaces, formato y vigencia técnica antes de marcarse como edición final."
        ),
        "suffix": "Espanol_v1.0",
    },
    "pt": {
        "folder": "Portugues_BR",
        "label": "Português do Brasil",
        "notice": (
            "> **Status da revisão:** Rascunho de tradução assistida por máquina. Requer revisão humana de "
            "terminologia, significado, links, formatação e atualidade técnica antes de ser marcado como edição final."
        ),
        "suffix": "Portugues_BR_v1.0",
    },
}

PROTECTED_PATTERNS = [
    re.compile(r"https?://[^\s)>]+"),
    re.compile(r"`[^`]+`"),
    re.compile(r"\b(?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2}(?:-\d+)?\b"),
    re.compile(r"\b(?:NIST|CSF|RMF|CIS|ISO|IEC|SOC|GDPR|HIPAA|PCI DSS|OWASP|API|RACI|GRC)\b"),
]


def protect(text: str) -> tuple[str, dict[str, str]]:
    mapping: dict[str, str] = {}
    counter = 0
    for pattern in PROTECTED_PATTERNS:
        while True:
            match = pattern.search(text)
            if not match:
                break
            token = f"ZXPROTECTED{counter}XZ"
            mapping[token] = match.group(0)
            text = text[: match.start()] + token + text[match.end() :]
            counter += 1
    return text, mapping


def restore(text: str, mapping: dict[str, str]) -> str:
    for token, value in mapping.items():
        text = text.replace(token, value)
    return text


def translate_fragment(text: str, target: str) -> str:
    if not text.strip():
        return text
    protected, mapping = protect(text)
    translated = argostranslate.translate.translate(protected, "en", target)
    return restore(translated, mapping)


def translate_markdown(source: str, target: str, notice: str) -> str:
    lines = source.splitlines()
    output: list[str] = [notice, ""]
    in_fence = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            output.append(line)
            continue
        if in_fence or not stripped:
            output.append(line)
            continue

        # Preserve Markdown link destinations while translating link labels and surrounding text.
        link_targets: dict[str, str] = {}
        def replace_target(match: re.Match[str]) -> str:
            token = f"ZXLINK{len(link_targets)}XZ"
            link_targets[token] = match.group(1)
            return f"]({token})"
        prepared = re.sub(r"\]\(([^)]+)\)", replace_target, line)

        translated = translate_fragment(prepared, target)
        for token, value in link_targets.items():
            translated = translated.replace(token, value)
        output.append(translated)

    return "\n".join(output).rstrip() + "\n"


def output_name(source: Path, suffix: str) -> str:
    stem = source.stem
    stem = re.sub(r"^English_Source_", "", stem)
    stem = re.sub(r"_v1\.0$", "", stem)
    return f"{stem}_{suffix}.md"


def main() -> int:
    sources = sorted(ROOT.glob("[0-9][0-9]-*/**/English_Source_*.md"))
    if not sources:
        raise SystemExit("No extracted English source Markdown files found.")

    for source in sources:
        original = source.read_text(encoding="utf-8-sig", errors="strict")
        for target, cfg in LANGUAGES.items():
            folder = source.parent / cfg["folder"]
            folder.mkdir(parents=True, exist_ok=True)
            destination = folder / output_name(source, cfg["suffix"])
            translated = translate_markdown(original, target, cfg["notice"])
            destination.write_text(translated, encoding="utf-8")
            print(f"Generated {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
