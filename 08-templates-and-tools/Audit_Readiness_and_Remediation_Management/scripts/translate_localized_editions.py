#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "English/Audit_Readiness_and_Remediation_Management_Practical_Manual_English_v1.0.md"
LOCALES = {
    "es": {
        "folder": "translations/es-419",
        "file": "Preparacion_para_Auditorias_y_Gestion_de_Remediacion_Manual_Practico_es-419_v1.0.md",
        "lang": "es-419",
        "title": "Manual Práctico de Preparación para Auditorías y Gestión de Remediación",
        "status": "Candidato de publicación asistido por máquina; no se presenta como revisión lingüística nativa.",
    },
    "pt": {
        "folder": "translations/pt-BR",
        "file": "Preparacao_para_Auditorias_e_Gestao_de_Remediacao_Manual_Pratico_pt-BR_v1.0.md",
        "lang": "pt-BR",
        "title": "Manual Prático de Preparação para Auditorias e Gestão de Remediação",
        "status": "Candidato de publicação assistido por máquina; não é apresentado como revisão linguística nativa.",
    },
}
PROTECTED = re.compile(r"(`[^`]+`|https?://\S+|NIST|ISO 19011:2026|ISO/IEC|SP 800-53A|SP 800-53|CSF 2\.0|GAO|IIA|CC BY-NC-SA 4\.0)")


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
    body = line.lstrip()
    marker = ""
    match = re.match(r"(#{1,6}\s+|[-*+]\s+|\d+\.\s+|>\s+)", body)
    if match:
        marker = match.group(1)
        body = body[len(marker):]
    safe, values = protect(body)
    translated = argostranslate.translate.translate(safe, "en", target)
    return prefix + marker + restore(translated, values)


def replace_frontmatter(text: str, locale: dict[str, str]) -> str:
    if not text.startswith("---\n"):
        raise RuntimeError("Expected YAML front matter")
    end = text.find("\n---\n", 4)
    body = text[end + 5:]
    header = f'''---
title: "{locale['title']}"
author: "Alberto Al Leiva"
date: "1 de agosto de 2026"
lang: {locale['lang']}
subject: "GRC, preparación para auditorías, hallazgos, remediación y validación de cierre"
rights: "CC BY-NC-SA 4.0 salvo que un archivo indique lo contrario"
status: "{locale['status']}"
---
'''
    return header + body


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    for target, locale in LOCALES.items():
        localized = replace_frontmatter(source, locale)
        translated = [translate_line(line, target) for line in localized.splitlines()]
        out_dir = ROOT / locale["folder"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / locale["file"]
        out.write_text("\n".join(translated).strip() + "\n", encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
