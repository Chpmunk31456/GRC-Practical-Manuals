#!/usr/bin/env python3
"""Fail-closed localization depth/parity gate for Manual 03.

This check cannot substitute for semantic human judgment. It prevents a known
failure mode: localized files that retain chapter numbers while omitting a
material portion of the controlled English implementation detail.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUAL = ROOT / "01-foundations" / "NIST_AI_RMF_1.0"
CHAPTER_RE = re.compile(r"(?m)^#\s+([0-9]{1,2})\.\s+.+?\s*$")
SUBSECTION_RE = re.compile(r"(?m)^##\s+([0-9]{1,2}\.[0-9]+)\s+.+?\s*$")
MERMAID_RE = re.compile(r"(?ms)^```mermaid\s*\n.*?^```\s*$")


def split_chapters(text: str) -> dict[int, str]:
    matches = list(CHAPTER_RE.finditer(text))
    result: dict[int, str] = {}
    for idx, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        result[number] = text[match.start():end]
    return result


def source_files(language: str) -> list[Path]:
    if language == "en":
        return sorted((MANUAL / "English" / "source").glob("*.md"))
    paths: list[Path] = []
    for base in [MANUAL / "translations" / language / "source", MANUAL / language / "source"]:
        if base.is_dir():
            paths.extend(sorted(base.glob("*.md")))
    return paths


def load_chapters(language: str) -> dict[int, str]:
    chapters: dict[int, str] = {}
    for path in source_files(language):
        text = path.read_text(encoding="utf-8")
        for number, chapter in split_chapters(text).items():
            if number in chapters and chapters[number] != chapter:
                raise ValueError(f"duplicate conflicting chapter {number} in {language}: {path}")
            chapters[number] = chapter
    return chapters


def normalize_words(text: str) -> list[str]:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"https?://\S+", " ", text)
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", text)


def main() -> int:
    errors: list[str] = []
    try:
        english = load_chapters("en")
        localized = {lang: load_chapters(lang) for lang in ("es-419", "pt-BR")}
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    expected = set(range(1, 33))
    if set(english) != expected:
        errors.append(f"English chapter set mismatch: {sorted(english)}")

    for language, chapters in localized.items():
        if set(chapters) != expected:
            errors.append(f"{language} chapter set mismatch: {sorted(chapters)}")
            continue
        for number in range(1, 33):
            en = english[number]
            loc = chapters[number]
            en_sub = set(SUBSECTION_RE.findall(en))
            loc_sub = set(SUBSECTION_RE.findall(loc))
            if en_sub != loc_sub:
                missing = sorted(en_sub - loc_sub)
                extra = sorted(loc_sub - en_sub)
                errors.append(
                    f"{language} chapter {number} subsection mismatch; missing={missing}, extra={extra}"
                )

            en_mermaid = len(MERMAID_RE.findall(en))
            loc_mermaid = len(MERMAID_RE.findall(loc))
            if en_mermaid != loc_mermaid:
                errors.append(
                    f"{language} chapter {number} Mermaid count {loc_mermaid} != English {en_mermaid}"
                )

            en_access = en.count("**Accessible explanation:**")
            access_label = "**Explicación accesible:**" if language == "es-419" else "**Explicação acessível:**"
            loc_access = loc.count(access_label)
            if en_access != loc_access:
                errors.append(
                    f"{language} chapter {number} accessible-explanation count {loc_access} != English {en_access}"
                )

            en_words = len(normalize_words(en))
            loc_words = len(normalize_words(loc))
            ratio = loc_words / max(1, en_words)
            if ratio < 0.60 or ratio > 1.65:
                errors.append(
                    f"{language} chapter {number} semantic-depth proxy ratio {ratio:.2f} outside 0.60-1.65 "
                    f"(localized={loc_words}, English={en_words})"
                )

            for controlled in ("GOVERN", "MAP", "MEASURE", "MANAGE"):
                if controlled in en and controlled not in loc:
                    errors.append(f"{language} chapter {number} lost controlled NIST identifier {controlled}")

    for language in ("es-419", "pt-BR"):
        combined = "\n".join(localized[language].values())
        required = [
            "NIST AI 600-1",
            "TEVV",
            "ISO/IEC 42001",
        ]
        for marker in required:
            if marker not in combined:
                errors.append(f"{language} controlled localization missing marker: {marker}")

    if errors:
        print("FAIL: Manual 03 localization depth/parity gate")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: Manual 03 localization depth/parity gate")
    print("- 32 chapters present in English, es-419, and pt-BR")
    print("- numbered subsection parity preserved chapter-by-chapter")
    print("- Mermaid and accessible-explanation parity preserved")
    print("- semantic-depth proxy remains within controlled bounds")
    print("- controlled NIST identifiers and assurance markers preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
