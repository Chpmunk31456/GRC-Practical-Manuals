from __future__ import annotations

import re
from pathlib import Path

import argostranslate.translate

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "English/GRC_Metrics_and_Executive_Reporting_Toolkit_English_v1.0.md"

TARGETS = {
    "es-419": {
        "code": "es",
        "title": "Kit de Métricas GRC e Informes Ejecutivos",
        "filename": "Kit_Metricas_GRC_e_Informes_Ejecutivos_es-419_v1.0.md",
        "status": "candidato de publicación con traducción asistida por máquina",
    },
    "pt-BR": {
        "code": "pt",
        "title": "Kit de Métricas de GRC e Relatórios Executivos",
        "filename": "Kit_Metricas_GRC_e_Relatorios_Executivos_pt-BR_v1.0.md",
        "status": "candidato a publicação com tradução assistida por máquina",
    },
}

PROTECTED = re.compile(
    r"`[^`]+`|https?://\S+|\b(?:NIST|ISO|GRC|KPI|KRI|KCI|CSV|DOCX|PDF|SHA-256|H1|H2)\b|\b\d+(?:[.,]\d+)*%?\b"
)


def protect(text: str) -> tuple[str, dict[str, str]]:
    mapping: dict[str, str] = {}

    def repl(match: re.Match[str]) -> str:
        key = f"ZXQ{len(mapping):04d}QXZ"
        mapping[key] = match.group(0)
        return key

    return PROTECTED.sub(repl, text), mapping


def restore(text: str, mapping: dict[str, str]) -> str:
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text


def translate_text(text: str, target: str) -> str:
    if not text.strip():
        return text
    protected, mapping = protect(text)
    translated = argostranslate.translate.translate(protected, "en", target)
    return restore(translated, mapping)


def translate_body(body: str, target: str) -> str:
    output: list[str] = []
    in_code = False
    for line in body.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            output.append(line)
            continue
        if in_code or not line.strip():
            output.append(line)
            continue
        match = re.match(r"^(#{1,6}\s+|>\s+|-\s+|\d+\.\s+)(.*)$", line)
        if match:
            output.append(match.group(1) + translate_text(match.group(2), target))
        else:
            output.append(translate_text(line, target))
    return "\n".join(output).rstrip() + "\n"


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    if not source.startswith("---\n"):
        raise SystemExit("English master does not begin with YAML metadata")
    _, _, remainder = source.partition("---\n")
    _, sep, body = remainder.partition("\n---\n")
    if not sep:
        raise SystemExit("English YAML metadata boundary not found")

    for locale, cfg in TARGETS.items():
        out_dir = ROOT / "translations" / locale
        out_dir.mkdir(parents=True, exist_ok=True)
        translated_body = translate_body(body.lstrip("\n"), cfg["code"])
        metadata = "\n".join(
            [
                "---",
                f'title: "{cfg["title"]}"',
                'author: "Alberto Al Leiva"',
                f'language: "{locale}"',
                'version: "1.0"',
                'date: "2026-08-01"',
                f'status: "{cfg["status"]}"',
                'source_language: "en"',
                'translation_method: "machine-assisted; human editorial approval pending"',
                "---",
                "",
            ]
        )
        output = metadata + translated_body
        if re.search(r"ZXQ\d{4}QXZ", output):
            raise SystemExit(f"Unrestored protected token in {locale}")
        path = out_dir / cfg["filename"]
        path.write_text(output, encoding="utf-8")
        print(path)


if __name__ == "__main__":
    main()
