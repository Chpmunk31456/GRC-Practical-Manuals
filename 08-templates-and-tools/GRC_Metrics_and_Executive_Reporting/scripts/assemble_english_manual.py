from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "chapters"
TOOLS = ROOT / "tools"
OUT = ROOT / "English"
OUT.mkdir(parents=True, exist_ok=True)

ORDER = [
    "01_Metric_Governance_and_Decision_Purpose.md",
    "02_Definitions_Formulas_Scope_and_Normalization.md",
    "03_Data_Lineage_Quality_and_Validation.md",
    "04_Baselines_Targets_Thresholds_Trends_and_Benchmarks.md",
    "05_Executive_and_Board_Reporting.md",
    "06_Lifecycle_Review_Actions_and_Assurance_Boundaries.md",
]
EXPECTED_TOOLS = {
    "Metric_Definition_Register.csv": 40,
    "KPI_KRI_Review_Worksheet.csv": 36,
    "Executive_GRC_Scorecard.csv": 34,
    "Metrics_Action_and_Decision_Tracker.csv": 28,
}

for name in ORDER:
    if not (CHAPTERS / name).is_file():
        raise SystemExit(f"Missing chapter: {name}")

counts: dict[str, int] = {}
for name, wanted in EXPECTED_TOOLS.items():
    path = TOOLS / name
    if not path.is_file():
        raise SystemExit(f"Missing tool: {name}")
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle))
    if len(rows) != 1:
        raise SystemExit(f"{name}: expected header-only template, found {len(rows)} rows")
    got = len(rows[0])
    if got != wanted:
        raise SystemExit(f"{name}: expected {wanted} fields, found {got}")
    counts[name] = got

parts = [
    "---",
    'title: "GRC Metrics and Executive Reporting Toolkit"',
    'author: "Alberto Al Leiva"',
    'language: "en"',
    'version: "1.0"',
    'date: "2026-08-01"',
    'status: "controlled English master"',
    "---",
    "",
    "# GRC Metrics and Executive Reporting Toolkit",
    "",
    "> Educational and operational guidance only. A metric, score, trend, benchmark, threshold, dashboard, maturity rating, or management report does not prove compliance, security, control effectiveness, audit assurance, or business performance.",
    "",
    "## How to use this toolkit",
    "",
    "Use the chapters to design and govern a measurement program. Use the editable CSV tools to retain definitions, review decisions, executive reporting context, and resulting actions. Adapt all content to the organization's objectives, risk profile, obligations, data, governance authorities, and reporting needs.",
    "",
    "## Editable tools",
    "",
]
for name, count in EXPECTED_TOOLS.items():
    parts.append(f"- `{name}` — {count} controlled fields")
parts.extend(["", "## Human-review limitations", "", "Automated checks validate structure, field counts, package integrity, and selected safeguards. They do not perform legal, regulatory, standards, audit, data-quality, accessibility, native-language, statistical, or page-by-page human review.", ""])

for name in ORDER:
    text = (CHAPTERS / name).read_text(encoding="utf-8").strip()
    parts.extend([text, ""])

manual = "\n".join(parts).rstrip() + "\n"
if "does not prove compliance" not in manual.lower():
    raise SystemExit("Required assurance limitation missing")
if re.search(r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b", manual, re.I):
    raise SystemExit("Unresolved placeholder detected")

stem = "GRC_Metrics_and_Executive_Reporting_Toolkit_English_v1.0"
md = OUT / f"{stem}.md"
md.write_text(manual, encoding="utf-8")

report = {
    "status": "PASS",
    "chapters": ORDER,
    "chapter_count": len(ORDER),
    "tool_field_counts": counts,
    "h1_count": len(re.findall(r"^# ", manual, re.M)),
    "h2_count": len(re.findall(r"^## ", manual, re.M)),
    "sha256": hashlib.sha256(manual.encode()).hexdigest(),
    "limitations": [
        "Automated validation does not establish compliance, security, control effectiveness, audit assurance, or business performance.",
        "Qualified legal, regulatory, statistical, data-governance, accessibility, and professional review remains required.",
    ],
}
(OUT / "ENGLISH_ASSEMBLY_REPORT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
lines = ["# English Assembly Report", "", "- Status: **PASS**", f"- Chapters: {len(ORDER)}", f"- H1 headings: {report['h1_count']}", f"- H2 headings: {report['h2_count']}", "", "## Tool schemas", ""]
lines.extend(f"- {name}: {count} fields" for name, count in counts.items())
lines.extend(["", "## Limitations", "", "- Automated validation does not establish compliance, security, control effectiveness, audit assurance, or business performance.", "- Qualified human review remains required.", ""])
(OUT / "ENGLISH_ASSEMBLY_REPORT.md").write_text("\n".join(lines), encoding="utf-8")
print(md)
