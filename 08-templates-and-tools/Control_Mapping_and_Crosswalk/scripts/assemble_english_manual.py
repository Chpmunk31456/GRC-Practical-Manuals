#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    ROOT / "chapters/01_Mapping_Governance_and_Intended_Use.md",
    ROOT / "chapters/02_Requirement_Decomposition_and_Normalization.md",
    ROOT / "chapters/03_Relationship_Analysis_and_Coverage_Decisions.md",
    ROOT / "chapters/04_Implementation_Evidence_and_Common_Control_Linkage.md",
    ROOT / "chapters/05_Gap_Overlap_Conflict_and_Prioritization.md",
    ROOT / "chapters/06_Review_Change_Control_and_Retirement.md",
    ROOT / "SOURCES.md",
]
TOOLS = {
    "Control_Mapping_Register.csv": 40,
    "Requirement_Decomposition_Worksheet.csv": 30,
    "Mapping_Review_Checklist.csv": 38,
    "Gap_Overlap_and_Conflict_Register.csv": 32,
}
OUT_DIR = ROOT / "English"
OUT_MD = OUT_DIR / "Control_Mapping_and_Crosswalk_Practical_Manual_English_v1.0.md"

HEADER = '''---
title: "Control Mapping and Crosswalk Practical Manual"
author: "Alberto Al Leiva"
date: "1 August 2026"
lang: en-US
subject: "GRC, control mapping, crosswalks, cybersecurity, privacy, audit and compliance"
rights: "CC BY-NC-SA 4.0 unless a file states otherwise"
status: "Controlled English publication candidate"
---

# Control Mapping and Crosswalk Practical Manual

> **Educational and analytical-use notice:** A mapping is not proof of compliance, certification, legal sufficiency, control effectiveness, or audit assurance. Verify authoritative sources, licensing, scope, implementation, evidence, and applicable law.

> **Copyright and licensing notice:** Do not reproduce proprietary standards text without authorization. Use licensed source identifiers and organization-authored analytical summaries where appropriate.
'''


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_tools() -> dict[str, int]:
    counts: dict[str, int] = {}
    for name, expected in TOOLS.items():
        path = ROOT / "tools" / name
        if not path.is_file():
            raise SystemExit(f"Missing tool: {path}")
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        if len(rows) != 1:
            raise SystemExit(f"{name}: expected header-only controlled template")
        actual = len(rows[0])
        if actual != expected:
            raise SystemExit(f"{name}: expected {expected} fields, found {actual}")
        if len(rows[0]) != len(set(rows[0])):
            raise SystemExit(f"{name}: duplicate field names")
        counts[name] = actual
    return counts


def main() -> None:
    for path in CHAPTERS:
        if not path.is_file():
            raise SystemExit(f"Missing controlled source: {path}")
    tool_counts = validate_tools()
    parts = [HEADER.strip()]
    source_records = []
    for path in CHAPTERS:
        text = path.read_text(encoding="utf-8").strip()
        if not text.startswith("# "):
            raise SystemExit(f"Source lacks H1: {path}")
        parts.extend(["\\newpage", text])
        source_records.append({
            "path": str(path.relative_to(ROOT)),
            "sha256": file_sha(path),
            "words": len(text.split()),
            "lines": len(text.splitlines()),
        })
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    assembled = "\n\n".join(parts).strip() + "\n"
    prohibited = [
        "automatically establishes compliance",
        "proves compliance",
        "guarantees certification",
    ]
    lowered = assembled.lower()
    for phrase in prohibited:
        if phrase in lowered:
            raise SystemExit(f"Prohibited claim detected: {phrase}")
    OUT_MD.write_text(assembled, encoding="utf-8")
    report = {
        "status": "PASS",
        "output": str(OUT_MD.relative_to(ROOT)),
        "sources": source_records,
        "tool_field_counts": tool_counts,
        "assembled_sha256": file_sha(OUT_MD),
        "assembled_words": len(assembled.split()),
        "assembled_lines": len(assembled.splitlines()),
        "human_review_limitations": [
            "No legal, regulatory, licensing, certification or audit opinion is represented.",
            "No native-language editorial approval is represented.",
            "No assistive-technology or full page-by-page visual approval is represented.",
        ],
    }
    (OUT_DIR / "ENGLISH_ASSEMBLY_REPORT.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    md_lines = [
        "# English Assembly Report",
        "",
        "- Status: **PASS**",
        f"- Controlled sources: {len(source_records)}",
        f"- Assembled words: {report['assembled_words']}",
        f"- Assembled lines: {report['assembled_lines']}",
        f"- SHA-256: `{report['assembled_sha256']}`",
        "",
        "## Tool schemas",
        "",
    ]
    md_lines.extend(f"- {name}: {count} fields" for name, count in tool_counts.items())
    md_lines += [
        "",
        "## Human-review limitations",
        "",
        "- Legal, regulatory, licensing, certification and audit conclusions require qualified humans.",
        "- Native-language, assistive-technology and page-by-page visual review are not represented as completed.",
        "",
    ]
    (OUT_DIR / "ENGLISH_ASSEMBLY_REPORT.md").write_text("\n".join(md_lines), encoding="utf-8")
    print(OUT_MD)


if __name__ == "__main__":
    main()
