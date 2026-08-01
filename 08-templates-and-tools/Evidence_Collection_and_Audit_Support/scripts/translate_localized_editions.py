#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "English/Evidence_Collection_and_Audit_Support_Practical_Manual_English_v1.0.md"

LOCALES = {
    "es": {
        "folder": "translations/es-419",
        "file": "Manual_Practico_de_Recoleccion_de_Evidencia_y_Apoyo_de_Auditoria_es-419_v1.0.md",
        "notice": "**Estado de traducción:** candidato de publicación asistido por máquina; no se presenta como revisión lingüística nativa.",
    },
    "pt": {
        "folder": "translations/pt-BR",
        "file": "Manual_Pratico_de_Coleta_de_Evidencias_e_Suporte_de_Auditoria_pt-BR_v1.0.md",
        "notice": "**Status da tradução:** candidato de publicação assistido por máquina; não é apresentado como revisão linguística nativa.",
    },
}

PROTECTED = re.compile(
    r"(`[^`]+`|https?://\S+|NIST|SP 800-53A|SP 800-53|ISO 19011:2026|GAO-25-107721|Global Internal Audit Standards|CC BY-NC-SA 4\.0|es-419|pt-BR)"
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
    if not stripped or stripped == "---":
        return line
    prefix = line[: len(line) - len(line.lstrip())]
    body = line.lstrip()
    marker = ""
    match = re.match(r"(#{1,6}\s+|[-*+]\s+|\d+\.\s+|>\s+)", body)
    if match:
        marker = match.group(1)
        body = body[len(marker) :]
    safe, values = protect(body)
    translated = argostranslate.translate.translate(safe, "en", target)
    return prefix + marker + restore(translated, values)


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    for target, locale in LOCALES.items():
        translated = [translate_line(line, target) for line in source.splitlines()]
        if translated and translated[0].startswith("# "):
            translated.insert(1, "")
            translated.insert(2, locale["notice"])
        out_dir = ROOT / locale["folder"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out = out_dir / locale["file"]
        out.write_text("\n".join(translated).strip() + "\n", encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
