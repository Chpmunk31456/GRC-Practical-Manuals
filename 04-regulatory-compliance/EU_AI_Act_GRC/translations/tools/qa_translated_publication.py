#!/usr/bin/env python3
"""Fail-closed structural and artifact QA for translated EU AI Act editions."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

LANG_RULES = {
    "es-419": {
        "chapter": re.compile(r"^##\s+(?:Capítulo|Chapter)\s+(\d+)\b", re.MULTILINE),
        "appendix": re.compile(r"^##\s+(?:Apéndice|Appendix)\s+([A-Z])\b", re.MULTILINE),
        "required": ["sistema de IA", "supervisión humana", "evidencia", "prueba de auditoría"],
        "forbidden_phrases": ["Plain-English explanation", "Control activity", "Audit test", "How to use this manual"],
    },
    "pt-BR": {
        "chapter": re.compile(r"^##\s+(?:Capítulo|Chapter)\s+(\d+)\b", re.MULTILINE),
        "appendix": re.compile(r"^##\s+(?:Apêndice|Appendix)\s+([A-Z])\b", re.MULTILINE),
        "required": ["sistema de IA", "supervisão humana", "evidência", "teste de auditoria"],
        "forbidden_phrases": ["Plain-English explanation", "Control activity", "Audit test", "How to use this manual"],
    },
}
BAD_TOKENS = ["TODO", "TBD", "PLACEHOLDER", "cite", "filecite", "turn0search"]


def require(ok: bool, message: str, failures: list[str]) -> None:
    if not ok:
        failures.append(message)


def inspect_docx(path: Path, title_fragment: str, failures: list[str]) -> None:
    require(path.exists() and path.stat().st_size > 10000, f"DOCX missing or too small: {path}", failures)
    if not path.exists():
        return
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            require("word/document.xml" in names, "DOCX lacks document.xml", failures)
            require("word/styles.xml" in names, "DOCX lacks styles.xml", failures)
            xml = archive.read("word/document.xml").decode("utf-8", errors="replace")
            require(title_fragment in xml, "Localized DOCX title not found", failures)
    except zipfile.BadZipFile:
        failures.append("DOCX is not a valid OOXML ZIP package")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", choices=sorted(LANG_RULES), required=True)
    parser.add_argument("--build-dir", required=True)
    args = parser.parse_args()

    language = args.language
    rules = LANG_RULES[language]
    build = Path(args.build_dir)
    stem = f"EU_AI_Act_GRC_Compliance_Manual_{language}_Controlled_Master"
    md = build / f"{stem}.md"
    manifest = build / f"CANONICAL_BUILD_MANIFEST_{language}.json"
    docx = build / f"EU_AI_Act_GRC_Compliance_Manual_{language}_Controlled_Review.docx"
    pdf = build / f"EU_AI_Act_GRC_Compliance_Manual_{language}_Controlled_Review.pdf"
    failures: list[str] = []

    require(md.exists(), f"Missing integrated Markdown: {md}", failures)
    require(manifest.exists(), f"Missing manifest: {manifest}", failures)
    if md.exists():
        text = md.read_text(encoding="utf-8")
        chapters = [int(v) for v in rules["chapter"].findall(text)]
        appendices = rules["appendix"].findall(text)
        require(chapters == list(range(1, 139)), "Chapter sequence is not exactly 1-138", failures)
        require(appendices == [chr(c) for c in range(ord("A"), ord("Z") + 1)], "Appendix sequence is not exactly A-Z", failures)
        require(len(text.splitlines()) > 4000, "Translated master appears unexpectedly short", failures)
        for token in BAD_TOKENS:
            require(token not in text, f"Forbidden unresolved token: {token}", failures)
        for phrase in rules["forbidden_phrases"]:
            require(phrase not in text, f"Untranslated English heading or phrase: {phrase}", failures)
        for required in rules["required"]:
            require(required in text, f"Controlled localized term not found: {required}", failures)

    if manifest.exists():
        data = json.loads(manifest.read_text(encoding="utf-8"))
        require(data.get("chapter_count") == 138, "Manifest chapter count mismatch", failures)
        require(data.get("appendix_count") == 26, "Manifest appendix count mismatch", failures)
        require(data.get("record_count") == 164, "Manifest record count mismatch", failures)

    title = "Manual de Cumplimiento" if language == "es-419" else "Manual de Conformidade"
    inspect_docx(docx, title, failures)
    require(pdf.exists() and pdf.stat().st_size > 10000, f"PDF missing or too small: {pdf}", failures)
    if pdf.exists():
        require(pdf.read_bytes().startswith(b"%PDF-"), "Invalid PDF signature", failures)

    report = {"language": language, "status": "PASS" if not failures else "FAIL", "failures": failures}
    (build / f"AUTOMATED_QA_REPORT_{language}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if failures:
        for failure in failures:
            print(f"QA ERROR: {failure}", file=sys.stderr)
        return 1
    print(f"Automated QA passed for {language}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
