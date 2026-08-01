#!/usr/bin/env python3
from __future__ import annotations

# Controlled localization generator for the validated English policy toolkit.
import json
import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "English/GRC_Policy_Template_Toolkit_English_v1.0.md"

LOCALES = {
    "es": {
        "folder": "translations/es-419",
        "file": "Kit_de_Plantillas_de_Politicas_GRC_es-419_v1.0.md",
        "lang": "es-419",
        "title": "Kit de Plantillas de Políticas GRC",
        "date": "1 de agosto de 2026",
        "subject": "GRC, gobernanza de políticas, seguridad de la información, privacidad y resiliencia",
        "rights": "CC BY-NC-SA 4.0 salvo que un archivo indique lo contrario",
        "status": "Candidato de publicación asistido por máquina; no se presenta como revisión lingüística nativa ni asesoría legal.",
    },
    "pt": {
        "folder": "translations/pt-BR",
        "file": "Kit_de_Modelos_de_Politicas_GRC_pt-BR_v1.0.md",
        "lang": "pt-BR",
        "title": "Kit de Modelos de Políticas GRC",
        "date": "1 de agosto de 2026",
        "subject": "GRC, governança de políticas, segurança da informação, privacidade e resiliência",
        "rights": "CC BY-NC-SA 4.0, salvo indicação em contrário no arquivo",
        "status": "Candidato de publicação assistido por máquina; não é apresentado como revisão linguística nativa nem assessoria jurídica.",
    },
}

PROTECTED = re.compile(
    r"(`[^`]+`|https?://\S+|\[[A-Z0-9 ,/&()._-]+\]|NIST|ISO/IEC|CSF 2\.0|SP 800-53(?:A)?(?: Rev\. 5)?|CC BY-NC-SA 4\.0)"
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
    return "\n".join(
        [
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
        ]
    )


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Missing controlled English master: {SOURCE}")
    body = source_body(SOURCE.read_text(encoding="utf-8"))
    for target, locale in LOCALES.items():
        translated_body = [translate_line(line, target) for line in body.splitlines()]
        out_dir = ROOT / locale["folder"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / locale["file"]
        content = localized_header(locale) + "\n".join(translated_body).strip() + "\n"
        out.write_text(content, encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
