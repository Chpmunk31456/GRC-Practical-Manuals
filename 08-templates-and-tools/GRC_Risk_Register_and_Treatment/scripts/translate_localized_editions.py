#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "English/GRC_Risk_Register_and_Risk_Treatment_Practical_Manual_English_v1.0.md"

LOCALES = {
    "es": {
        "folder": "translations/es-419",
        "file": "GRC_Registro_de_Riesgos_y_Tratamiento_de_Riesgos_Manual_Practico_es-419_v1.0.md",
        "lang": "es-419",
        "title": "Manual Práctico de Registro y Tratamiento de Riesgos GRC",
        "status": "Borrador asistido por máquina; no se presenta como revisión lingüística nativa.",
    },
    "pt": {
        "folder": "translations/pt-BR",
        "file": "GRC_Registro_e_Tratamento_de_Riscos_Manual_Pratico_pt-BR_v1.0.md",
        "lang": "pt-BR",
        "title": "Manual Prático de Registro e Tratamento de Riscos GRC",
        "status": "Rascunho assistido por máquina; não é apresentado como revisão linguística nativa.",
    },
}

PROTECTED = re.compile(r"(`[^`]+`|https?://\S+|\{\{[^}]+\}\}|NIST|ISO/IEC|ISO 31000|CIS RAM|CSF 2\.0|SP 800-30|IR 8286[A-C]?(?: Rev\. 1)?)")


def protect(text: str) -> tuple[str, dict[str, str]]:
    values: dict[str, str] = {}
    def repl(match: re.Match[str]) -> str:
        key = f"ZXQ{len(values):04d}QXZ"
        values[key] = match.group(0)
        return key
    return PROTECTED.sub(repl, text), values


def restore(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace(key, value)
    return text


def translate_line(line: str, target: str) -> str:
    stripped = line.strip()
    if not stripped or stripped == "---" or stripped.startswith("\\newpage"):
        return line
    prefix = line[: len(line) - len(line.lstrip())]
    marker = ""
    body = line.lstrip()
    match = re.match(r"(#{1,6}\s+|[-*+]\s+|\d+\.\s+|>\s+)", body)
    if match:
        marker = match.group(1)
        body = body[len(marker):]
    safe, values = protect(body)
    translated = argostranslate.translate.translate(safe, "en", target)
    return prefix + marker + restore(translated, values)


def frontmatter(text: str, locale: dict[str, str]) -> str:
    if not text.startswith("---\n"):
        raise RuntimeError("Expected YAML front matter")
    end = text.find("\n---\n", 4)
    body = text[end + 5:]
    header = f'''---
title: "{locale['title']}"
author: "Alberto Al Leiva"
date: "1 de agosto de 2026"
lang: {locale['lang']}
subject: "Gobernanza, gestión de riesgos, GRC, registro y tratamiento de riesgos"
rights: "CC BY-NC-SA 4.0 salvo que un archivo indique lo contrario"
status: "{locale['status']}"
---
'''
    return header + body


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    for target, locale in LOCALES.items():
        localized_source = frontmatter(source, locale)
        lines = localized_source.splitlines()
        translated = [translate_line(line, target) for line in lines]
        out_dir = ROOT / locale["folder"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / locale["file"]
        out.write_text("\n".join(translated).strip() + "\n", encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
