#!/usr/bin/env python3
"""Fail-closed regression QA for localized controlled publication packages.

Catches generator/presentation defects that structural QA can miss:
- English generator-owned boilerplate left in es-419 / pt-BR editions;
- English figure captions left in localized editions;
- DOCX image alt text referring to the wrong numbered manual;
- duplicate page-footer text caused by linked Word section footers.

Supporting machine QA only. This does not replace competent human semantic,
terminology, accessibility, rendered visual, legal, or changed-scope review.
"""
from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path

import fitz
from docx import Document

FORBIDDEN_LOCALIZED_TEXT = (
    "Controlled source revision:",
    "Assurance boundary:",
    "Implementation paths and operating model",
    "Controlled 32-chapter manual",
    "Controlled publication QA candidate",
    "controlled assurance baseline",
    "source watch retained",
)
ENGLISH_CAPTION_RE = re.compile(r"\bFigure\s+\d+\.", re.IGNORECASE)
MANUAL_ALT_RE = re.compile(r"Manual\s+(\d{1,2})\s+memory graphic", re.IGNORECASE)


def extract_pdf_text(path: Path) -> str:
    with fitz.open(path) as pdf:
        return "\n".join(page.get_text("text") for page in pdf)


def extract_docx_text_and_alt(path: Path) -> tuple[str, str]:
    doc = Document(path)
    text = "\n".join(p.text for p in doc.paragraphs)
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml").decode("utf-8", errors="replace")
    alt = "\n".join(re.findall(r'\bdescr="([^"]+)"', xml))
    return text, alt


def classify(path: Path) -> str | None:
    name = path.name.upper().replace("_", "-")
    if "ES-419" in name:
        return "es-419"
    if "PT-BR" in name:
        return "pt-BR"
    return None


def validate_text(text: str, label: str) -> list[str]:
    errors: list[str] = []
    for phrase in FORBIDDEN_LOCALIZED_TEXT:
        if phrase in text:
            errors.append(f"{label}: stale English generator boilerplate: {phrase!r}")
    if ENGLISH_CAPTION_RE.search(text):
        errors.append(f"{label}: English 'Figure N.' caption detected in localized edition")
    if "memory graphic" in text.lower():
        errors.append(f"{label}: English 'memory graphic' wording detected in localized edition")
    return errors


def validate_alt(alt: str, label: str, manual_number: int) -> list[str]:
    errors: list[str] = []
    for match in MANUAL_ALT_RE.finditer(alt):
        found = int(match.group(1))
        if found != manual_number:
            errors.append(
                f"{label}: inherited alt-text manual number {found:02d}; expected {manual_number:02d}"
            )
    return errors


def validate_footer_duplication(text: str, label: str, manual_number: int) -> list[str]:
    token = f"Manual {manual_number:02d} |"
    errors: list[str] = []
    for index, line in enumerate(text.splitlines(), start=1):
        if line.count(token) > 1:
            errors.append(f"{label}: duplicate footer text detected on extracted line {index}: {token}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("publication_dir", type=Path)
    parser.add_argument("--manual-number", type=int, required=True)
    args = parser.parse_args()

    root = args.publication_dir
    if not root.is_dir():
        print(f"ERROR: publication directory not found: {root}")
        return 2

    localized_seen = {"es-419": {"pdf": 0, "docx": 0}, "pt-BR": {"pdf": 0, "docx": 0}}
    errors: list[str] = []

    for path in sorted(root.iterdir()):
        suffix = path.suffix.lower()
        if suffix == ".pdf":
            pdf_text = extract_pdf_text(path)
            errors.extend(validate_footer_duplication(pdf_text, path.name, args.manual_number))
        else:
            pdf_text = ""

        language = classify(path)
        if language is None:
            continue
        label = f"{language}:{path.name}"
        if suffix == ".pdf":
            localized_seen[language]["pdf"] += 1
            errors.extend(validate_text(pdf_text, label))
            if "Figura " not in pdf_text and "FIGURA " not in pdf_text.upper():
                errors.append(f"{label}: no localized 'Figura' caption marker found")
        elif suffix == ".docx":
            localized_seen[language]["docx"] += 1
            text, alt = extract_docx_text_and_alt(path)
            errors.extend(validate_text(text, label))
            errors.extend(validate_alt(alt, label, args.manual_number))

    for language, counts in localized_seen.items():
        for kind in ("docx", "pdf"):
            if counts[kind] != 1:
                errors.append(
                    f"{language}: expected exactly one localized {kind.upper()} candidate, found {counts[kind]}"
                )

    if errors:
        print("Localized publication regression QA: FAIL")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Localized publication regression QA: PASS")
    print(f"  manual: {args.manual_number:02d}")
    print("  localized editions: es-419, pt-BR")
    print("  stale English generator boilerplate/captions: none detected")
    print("  inherited wrong-manual alt-text labels: none detected")
    print("  duplicate footer text: none detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
