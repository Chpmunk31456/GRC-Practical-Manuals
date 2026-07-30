#!/usr/bin/env python3
"""Fail-closed automated QA for the assembled English publication artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

CHAPTER_HEADING = re.compile(r"^## Chapter\s+(\d+)\b", re.MULTILINE)
APPENDIX_HEADING = re.compile(r"^## Appendix\s+([A-Z])\b", re.MULTILINE)
BAD_TOKENS = (
    "turn0search",
    "turn1search",
    "cite",
    "filecite",
    "TODO",
    "TBD",
    "PLACEHOLDER",
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def inspect_docx(path: Path, failures: list[str]) -> None:
    require(path.exists() and path.stat().st_size > 10_000, f"DOCX missing or too small: {path}", failures)
    if not path.exists():
        return
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            require("word/document.xml" in names, "DOCX lacks word/document.xml", failures)
            require("word/styles.xml" in names, "DOCX lacks word/styles.xml", failures)
            require("docProps/core.xml" in names, "DOCX lacks core properties", failures)
            document = archive.read("word/document.xml").decode("utf-8", errors="replace")
            require("EU Artificial Intelligence Act" in document, "DOCX title not found", failures)
            require("Chapter 138" in document, "DOCX Chapter 138 not found", failures)
            require("Appendix Z" in document, "DOCX Appendix Z not found", failures)
    except zipfile.BadZipFile:
        failures.append("DOCX is not a valid ZIP/OOXML package")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--build-dir", default="build/eu-ai-act")
    args = parser.parse_args()

    build_dir = Path(args.build_dir)
    md = build_dir / "EU_AI_Act_GRC_Compliance_Manual_English_Controlled_Master.md"
    manifest_path = build_dir / "CANONICAL_BUILD_MANIFEST.json"
    docx = build_dir / "EU_AI_Act_GRC_Compliance_Manual_English_Controlled_Review.docx"
    pdf = build_dir / "EU_AI_Act_GRC_Compliance_Manual_English_Controlled_Review.pdf"
    failures: list[str] = []

    require(md.exists(), f"Missing integrated Markdown: {md}", failures)
    require(manifest_path.exists(), f"Missing build manifest: {manifest_path}", failures)
    if md.exists():
        text = md.read_text(encoding="utf-8")
        chapters = [int(value) for value in CHAPTER_HEADING.findall(text)]
        appendices = APPENDIX_HEADING.findall(text)
        require(chapters == list(range(1, 139)), "Chapter sequence is not exactly 1-138", failures)
        require(appendices == [chr(code) for code in range(ord("A"), ord("Z") + 1)], "Appendix sequence is not exactly A-Z", failures)
        require(len(text.splitlines()) > 5_000, "Integrated Markdown appears unexpectedly short", failures)
        for token in BAD_TOKENS:
            require(token not in text, f"Forbidden unresolved token found: {token}", failures)

    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        require(manifest.get("chapter_count") == 138, "Manifest chapter count is not 138", failures)
        require(manifest.get("appendix_count") == 26, "Manifest appendix count is not 26", failures)
        require(len(manifest.get("records", [])) == 164, "Manifest does not contain 164 source records", failures)
        if md.exists():
            require(manifest.get("master_sha256") == sha256(md), "Manifest master hash does not match Markdown", failures)

    inspect_docx(docx, failures)
    require(pdf.exists() and pdf.stat().st_size > 10_000, f"PDF missing or too small: {pdf}", failures)
    if pdf.exists():
        require(pdf.read_bytes().startswith(b"%PDF-"), "PDF signature is invalid", failures)

    report = {
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "artifacts": {
            "markdown": str(md),
            "manifest": str(manifest_path),
            "docx": str(docx),
            "pdf": str(pdf),
        },
    }
    (build_dir / "AUTOMATED_QA_REPORT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    if failures:
        for failure in failures:
            print(f"QA ERROR: {failure}", file=sys.stderr)
        return 1
    print("Automated publication QA passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
