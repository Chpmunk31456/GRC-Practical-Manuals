#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "English/Control_Mapping_and_Crosswalk_Practical_Manual_English_v1.0.md"

LOCALES = {
    "es": {
        "folder": "translations/es-419",
        "file": "Manual_Practico_de_Mapeo_de_Controles_y_Cruces_es-419_v1.0.md",
        "lang": "es-419",
        "title": "Manual Práctico de Mapeo de Controles y Cruces",
        "date": "1 de agosto de 2026",
        "subject": "GRC, mapeo de controles, cruces, ciberseguridad, privacidad, auditoría y cumplimiento",
        "rights": "CC BY-NC-SA 4.0 salvo que un archivo indique lo contrario",
        "status": "Candidato de publicación asistido por máquina; no se presenta como revisión lingüística nativa, equivalencia legal ni asesoría de auditoría.",
    },
    "pt": {
        "folder": "translations/pt-BR",
        "file": "Manual_Pratico_de_Mapeamento_de_Controles_e_Crosswalks_pt-BR_v1.0.md",
        "lang": "pt-BR",
        "title": "Manual Prático de Mapeamento de Controles e Crosswalks",
        "date": "1 de agosto de 2026",
        "subject": "GRC, mapeamento de controles, crosswalks, segurança cibernética, privacidade, auditoria e conformidade",
        "rights": "CC BY-NC-SA 4.0, salvo indicação em contrário no arquivo",
        "status": "Candidato de publicação assistido por máquina; não é apresentado como revisão linguística nativa, equivalência jurídica nem assessoria de auditoria.",
    },
}

PROTECTED = re.compile(
    r"(`[^`]+`|https?://\S+|NIST|ISO/IEC|CIS|PCI DSS|HIPAA|GDPR|CSF 2\.0|SP 800-53|CC BY-NC-SA 4\.0)"
)


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
    if not stripped or stripped.startswith("\\newpage"):
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


def source_body(text: str) -> str:
    if not text.startswith("---\n"):
        raise RuntimeError("Expected YAML front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise RuntimeError("Unterminated YAML front matter")
    return text[end + 5 :]


def yaml_value(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def localized_header(locale: dict[str, str]) -> str:
    return "\n".join([
        "---",
        f"title: {yaml_value(locale['title'])}",
        f"author: {yaml_value('Alberto Al Leiva')}",
        f"date: {yaml_value(locale['date'])}",
        f"lang: {locale['lang']}",
        f"subject: {yaml_value(locale['subject'])}",
        f"rights: {yaml_value(locale['rights'])}",
        f"status: {yaml_value(locale['status'])}",
        "---",
        "",
    ])


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Missing controlled English master: {SOURCE}")
    body = source_body(SOURCE.read_text(encoding="utf-8"))
    for target, locale in LOCALES.items():
        translated_body = [translate_line(line, target) for line in body.splitlines()]
        out_dir = ROOT / locale["folder"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / locale["file"]
        out.write_text(localized_header(locale) + "\n".join(translated_body).strip() + "\n", encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
