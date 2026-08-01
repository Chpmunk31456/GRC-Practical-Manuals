#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
OUT = ROOT / "English"
STEM = "Audit_Readiness_and_Remediation_Management_Practical_Manual_English_v1.0"
ORDER = [
    "01_Readiness_Governance_and_Assessment_Strategy.md",
    "02_Control_Mapping_and_Readiness_Assessment.md",
    "03_Findings_Root_Cause_and_Risk_Prioritization.md",
    "04_Remediation_Planning_and_Governance.md",
    "05_Closure_Validation_and_Sustainability.md",
    "06_Reporting_Operating_Procedure_and_Worked_Example.md",
]

FRONT = '''---
title: "Audit Readiness and Remediation Management Practical Manual"
author: "Alberto Al Leiva"
date: "1 August 2026"
lang: en
subject: "GRC, audit readiness, findings, remediation, closure validation"
rights: "CC BY-NC-SA 4.0 unless a file states otherwise"
status: "Controlled English publication candidate"
---

# Audit Readiness and Remediation Management Practical Manual

This manual provides educational and operational guidance. It does not constitute legal, regulatory, certification, accounting, or formal audit advice.

'''


def main() -> None:
    missing = [name for name in ORDER if not (CHAPTERS / name).is_file()]
    if missing:
        raise SystemExit(f"Missing controlled chapter(s): {missing}")
    parts = [FRONT]
    sources = []
    for name in ORDER:
        path = CHAPTERS / name
        text = path.read_text(encoding="utf-8").strip()
        if "TODO" in text or "TBD" in text:
            raise SystemExit(f"Unresolved marker in {name}")
        if not text.startswith("# "):
            raise SystemExit(f"Missing level-one heading in {name}")
        parts.append(text + "\n")
        sources.append({
            "path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "words": len(text.split()),
        })
    OUT.mkdir(parents=True, exist_ok=True)
    master = OUT / f"{STEM}.md"
    master.write_text("\n\\newpage\n\n".join(parts).strip() + "\n", encoding="utf-8")
    report = {
        "status": "PASS",
        "source_count": len(sources),
        "sources": sources,
        "master": str(master.relative_to(ROOT)),
        "master_sha256": hashlib.sha256(master.read_bytes()).hexdigest(),
        "master_words": len(master.read_text(encoding="utf-8").split()),
    }
    (OUT / "ENGLISH_ASSEMBLY_REPORT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (OUT / "ENGLISH_ASSEMBLY_REPORT.md").write_text(
        "# English Assembly Report\n\n"
        f"- Status: **PASS**\n- Controlled sources: {report['source_count']}\n"
        f"- Master words: {report['master_words']}\n- Master SHA-256: `{report['master_sha256']}`\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
