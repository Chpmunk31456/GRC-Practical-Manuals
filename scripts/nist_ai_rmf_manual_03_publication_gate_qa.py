#!/usr/bin/env python3
"""Fail-closed publication-source gate for Manual 03 localized editions."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUAL = ROOT / "01-foundations" / "NIST_AI_RMF_1.0"
MERMAID = re.compile(r"(?ms)^```mermaid\s*\n.*?^```\s*$")

FILES = {
    "en": MANUAL / "MANUAL_03_IMPLEMENTATION_PATHS.md",
    "es-419": MANUAL / "translations/es-419/source/RUTAS_DE_IMPLEMENTACION_MANUAL_03.md",
    "pt-BR": MANUAL / "translations/pt-BR/source/CAMINHOS_DE_IMPLEMENTACAO_MANUAL_03.md",
}
MARKERS = {
    "en": ["Essential", "Structured", "Enhanced", "**Accessible explanation:**"],
    "es-419": ["Esencial", "Estructurada", "Mejorada", "**Explicación accesible:**"],
    "pt-BR": ["Essencial", "Estruturado", "Aprimorado", "**Explicação acessível:**"],
}


def main() -> int:
    errors: list[str] = []
    texts: dict[str, str] = {}
    for lang, path in FILES.items():
        if not path.is_file():
            errors.append(f"missing implementation entry: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        texts[lang] = text
        if len(text) < 8000:
            errors.append(f"{lang} implementation entry unexpectedly small: {len(text)} chars")
        graphics = len(MERMAID.findall(text))
        if graphics != 3:
            errors.append(f"{lang} implementation entry must contain exactly 3 Mermaid graphics; found {graphics}")
        for marker in MARKERS[lang]:
            if marker not in text:
                errors.append(f"{lang} implementation entry missing marker: {marker}")
        for controlled in ["GOVERN", "MAP", "MEASURE", "MANAGE", "TEVV", "NIST AI 600-1", "ISO/IEC 42001"]:
            if controlled not in text:
                errors.append(f"{lang} implementation entry missing controlled term: {controlled}")

    if all(lang in texts for lang in FILES):
        en_words = len(re.findall(r"\w+", texts["en"], flags=re.UNICODE))
        for lang in ("es-419", "pt-BR"):
            words = len(re.findall(r"\w+", texts[lang], flags=re.UNICODE))
            ratio = words / max(1, en_words)
            if ratio < 0.65 or ratio > 1.55:
                errors.append(f"{lang} implementation semantic-depth ratio {ratio:.2f} outside 0.65-1.55")

    review = MANUAL / "translations/CONTROLLED_TRANSLATION_REVIEW_01.md"
    if not review.is_file():
        errors.append("controlled localization review record is missing")
    else:
        review_text = review.read_text(encoding="utf-8")
        for required in [
            "L10N-03-001",
            "PASS AFTER REMEDIATION",
            "Remediation status:** CLOSED",
            "Final release remains fail-closed",
        ]:
            if required not in review_text:
                errors.append(f"localization review record missing required evidence: {required}")

    if errors:
        print("FAIL: Manual 03 localized publication-source gate")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: Manual 03 localized publication-source gate")
    print("- implementation-path depth, three-graphic parity, accessibility labels and controlled terms verified")
    print("- localization remediation evidence is present")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
