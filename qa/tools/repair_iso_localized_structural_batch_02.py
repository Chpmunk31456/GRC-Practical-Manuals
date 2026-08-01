#!/usr/bin/env python3
"""Normalize ISO localized TOC links and missing major heading markers.

This batch changes only Markdown structure. It does not rewrite prose, tables,
terminology, image content, or publication binaries.
"""
from pathlib import Path
import re

ROOT = Path("02-management-systems/ISO_IEC_27001_27002")
SOURCES = [
    ROOT / "Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md",
    ROOT / "Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md",
]

TOC_RE = re.compile(
    r"^\[(?P<label>.+?)\s+\[(?P<page>\d+)\]\s*\(\s*#(?P<inner>[-a-z0-9]+)\s*\)\]\s*\(\s*#(?P<outer>[-a-z0-9]+)\s*\)\s*$",
    re.IGNORECASE,
)
PLAIN_HEADING_RE = re.compile(r"^(?P<num>(?:[1-9]|1\d|2[0-8]))\.\s+(?P<title>\S.*)$")


def normalize(text: str, path: Path) -> tuple[str, int, int]:
    lines = text.splitlines()
    toc_changes = 0
    heading_changes = 0
    seen_toc = False
    in_body = False
    output: list[str] = []

    for line in lines:
        match = TOC_RE.match(line)
        if match:
            if match.group("inner") != match.group("outer"):
                raise SystemExit(f"{path}: mismatched TOC anchors: {line}")
            line = f"[{match.group('label')} [{match.group('page')}]](#{match.group('outer')})"
            toc_changes += 1
            seen_toc = True

        if line.startswith("# 1. "):
            in_body = True

        heading = PLAIN_HEADING_RE.match(line)
        if in_body and heading:
            line = f"# {heading.group('num')}. {heading.group('title')}"
            heading_changes += 1

        output.append(line)

    if not seen_toc or toc_changes == 0:
        raise SystemExit(f"{path}: expected malformed nested TOC links to normalize")
    if heading_changes == 0:
        # PT-BR may have only one missing major heading; still require a change in each source.
        raise SystemExit(f"{path}: expected at least one missing major heading marker")

    return "\n".join(output) + "\n", toc_changes, heading_changes


def main() -> None:
    totals = []
    for path in SOURCES:
        before = path.read_text(encoding="utf-8")
        after, toc_count, heading_count = normalize(before, path)
        if after == before:
            raise SystemExit(f"{path}: no changes produced")
        path.write_text(after, encoding="utf-8")
        totals.append((path, toc_count, heading_count))
    for path, toc_count, heading_count in totals:
        print(f"{path}: normalized {toc_count} TOC links and {heading_count} major headings")


if __name__ == "__main__":
    main()
