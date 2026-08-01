#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    ROOT / "chapters/01_Governance_Source_Authority_and_Obligation_Inventory.md",
    ROOT / "chapters/02_Applicability_Decomposition_and_Interpretation.md",
    ROOT / "chapters/03_Ownership_Implementation_Controls_and_Evidence.md",
    ROOT / "chapters/04_Regulatory_Horizon_Scanning_and_Change_Intake.md",
    ROOT / "chapters/05_Impact_Assessment_Implementation_and_Escalation.md",
    ROOT / "chapters/06_Review_Supersession_Retirement_and_Assurance_Boundaries.md",
    ROOT / "SOURCES.md",
]
TOOLS = {
    "Compliance_Obligations_Register.csv": 48,
    "Regulatory_Change_Intake_and_Assessment_Log.csv": 42,
    "Regulatory_Change_Implementation_Plan.csv": 38,
    "Applicability_Review_Record.csv": 36,
}
OUT = ROOT / "English"
MASTER = OUT / "Compliance_Obligations_and_Regulatory_Change_Toolkit_English_v1.0.md"
HEADER = '''---
title: "Compliance Obligations Register and Regulatory Change Management Toolkit"
author: "Alberto Al Leiva"
date: "1 August 2026"
lang: en-US
subject: "Compliance obligations, regulatory change, GRC, governance and evidence"
rights: "CC BY-NC-SA 4.0 unless a file states otherwise"
status: "Controlled English publication candidate"
---

# Compliance Obligations Register and Regulatory Change Management Toolkit

> **Educational and governance-use notice:** This toolkit does not provide legal advice, determine applicability, certify compliance, prove control effectiveness, or replace official legal texts and qualified professional review.

> **Source-control notice:** Verify every obligation and change against an authoritative current source. Record jurisdiction, scope, dates, version, interpretation owner, implementation status, evidence, and review history.
'''


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_tools() -> dict[str, int]:
    counts = {}
    for name, expected in TOOLS.items():
        p = ROOT / "tools" / name
        if not p.is_file():
            raise SystemExit(f"Missing tool: {p}")
        with p.open(encoding="utf-8-sig", newline="") as f:
            rows = list(csv.reader(f))
        if len(rows) != 1:
            raise SystemExit(f"{name}: expected one header row")
        fields = rows[0]
        if len(fields) != expected:
            raise SystemExit(f"{name}: expected {expected} fields, found {len(fields)}")
        if len(fields) != len(set(fields)):
            raise SystemExit(f"{name}: duplicate fields")
        counts[name] = len(fields)
    return counts


def main() -> None:
    for p in CHAPTERS:
        if not p.is_file():
            raise SystemExit(f"Missing source: {p}")
    counts = validate_tools()
    parts = [HEADER.strip()]
    records = []
    for p in CHAPTERS:
        text = p.read_text(encoding="utf-8").strip()
        if not text.startswith("# "):
            raise SystemExit(f"Source lacks H1: {p}")
        parts.extend(["\\newpage", text])
        records.append({"path": str(p.relative_to(ROOT)), "sha256": sha(p), "words": len(text.split()), "lines": len(text.splitlines())})
    assembled = "\n\n".join(parts).strip() + "\n"
    required = [
        "does not provide legal advice",
        "authoritative current source",
        "qualified professional review",
        "applicability",
        "effective date",
        "evidence",
    ]
    lower = assembled.lower()
    missing = [term for term in required if term not in lower]
    if missing:
        raise SystemExit(f"Missing required safeguards: {missing}")
    if "[insert" in lower or "tbd" in lower:
        raise SystemExit("Unresolved placeholder detected")
    OUT.mkdir(parents=True, exist_ok=True)
    MASTER.write_text(assembled, encoding="utf-8")
    report = {
        "status": "PASS",
        "output": str(MASTER.relative_to(ROOT)),
        "sources": records,
        "tool_field_counts": counts,
        "assembled_sha256": sha(MASTER),
        "assembled_words": len(assembled.split()),
        "assembled_lines": len(assembled.splitlines()),
        "human_review_limitations": [
            "No legal or regulatory opinion or applicability determination is represented.",
            "No compliance certification, audit opinion or control-effectiveness conclusion is represented.",
            "No native-language editorial, assistive-technology or page-by-page visual approval is represented.",
        ],
    }
    (OUT / "ENGLISH_ASSEMBLY_REPORT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    lines = ["# English Assembly Report", "", "- Status: **PASS**", f"- Controlled sources: {len(records)}", f"- Assembled words: {report['assembled_words']}", f"- SHA-256: `{report['assembled_sha256']}`", "", "## Tool schemas", ""]
    lines += [f"- {n}: {c} fields" for n, c in counts.items()]
    lines += ["", "## Human-review limitations", "", "- Qualified legal, regulatory, privacy, labor, tax, sector and jurisdictional review remains required.", "- Automated validation does not determine applicability or establish compliance.", "- Native-language, assistive-technology and page-by-page visual approval are not represented as completed.", ""]
    (OUT / "ENGLISH_ASSEMBLY_REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print(MASTER)


if __name__ == "__main__":
    main()
