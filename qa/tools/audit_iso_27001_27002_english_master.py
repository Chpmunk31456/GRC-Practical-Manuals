#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

TARGET = Path("02-management-systems/ISO_IEC_27001_27002/English_Source_ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md")
REPORT = Path("qa/ISO_IEC_27001_27002_ENGLISH_MASTER_AUDIT.md")

PATTERNS = {
    "conversion box glyph": re.compile(r"□"),
    "broken image marker": re.compile(r"^[■□]img\\b", re.MULTILINE | re.IGNORECASE),
    "double heading marker": re.compile(r"^#\\s+#\\s+", re.MULTILINE),
    "raw separator line": re.compile(r"^-{20,}$", re.MULTILINE),
    "empty markdown link": re.compile(r"\\[[^\\]]+\\]\\(\\s*\\)"),
    "placeholder token": re.compile(r"\\b(?:TBD|TODO|FIXME|PLACEHOLDER)\\b", re.IGNORECASE),
    "malformed Word contents label": re.compile(r"\\*\\*True Word contents:\\*\\*", re.IGNORECASE),
}

REQUIRED_SECTIONS = [re.compile(rf"^#\\s+{n}\\.\\s+", re.MULTILINE) for n in range(1, 29)]
REQUIRED_FACTS = {
    "ISO/IEC 27001:2022": "ISO/IEC 27001:2022",
    "ISO/IEC 27002:2022": "ISO/IEC 27002:2022",
    "Amendment 1:2024": "Amendment 1:2024",
    "Clauses 4–10": "Clauses 4–10",
    "93 Annex A controls": "all 93 Annex A controls",
    "37 organizational controls": "37 organizational",
    "8 people controls": "8 people",
    "14 physical controls": "14 physical",
    "34 technological controls": "34 technological",
    "Clause 4": "# 6. Clause 4",
    "Clause 5": "# 7. Clause 5",
    "Clause 6": "# 8. Clause 6",
    "Clause 7": "# 9. Clause 7",
    "Clause 8": "# 10. Clause 8",
    "Clause 9": "# 11. Clause 9",
    "Clause 10": "# 12. Clause 10",
}


def line_number(text: str, offset: int) -> int:
    return text.count("\\n", 0, offset) + 1


def main() -> int:
    text = TARGET.read_text(encoding="utf-8")
    findings: list[tuple[str, int, str]] = []
    counts: Counter[str] = Counter()

    for label, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            line = line_number(text, match.start())
            excerpt = text.splitlines()[line - 1].strip()[:220]
            findings.append((label, line, excerpt))
            counts[label] += 1

    missing_sections = [str(i) for i, pattern in enumerate(REQUIRED_SECTIONS, start=1) if not pattern.search(text)]
    duplicate_sections = [str(i) for i, pattern in enumerate(REQUIRED_SECTIONS, start=1) if len(pattern.findall(text)) != 1]
    missing_facts = [label for label, marker in REQUIRED_FACTS.items() if marker not in text]

    status = "PASS" if not findings and not missing_sections and not duplicate_sections and not missing_facts else "REVIEW REQUIRED"
    report = [
        "# ISO/IEC 27001 and 27002 English Master Audit",
        "",
        f"Target: `{TARGET}`",
        "",
        "## Result",
        "",
        f"**{status}**",
        "",
        "## Summary",
        "",
    ]
    if counts:
        for label, count in sorted(counts.items()):
            report.append(f"- {label}: **{count}**")
    else:
        report.append("- No configured structural or placeholder markers found.")
    report.append(f"- Missing expected numbered sections: **{len(missing_sections)}**")
    report.append(f"- Sections not appearing exactly once: **{len(duplicate_sections)}**")
    report.append(f"- Missing required framework facts: **{len(missing_facts)}**")

    report.extend(["", "## Findings", ""])
    if findings:
        report.extend(["| Category | Line | Excerpt |", "|---|---:|---|"])
        for label, line, excerpt in sorted(findings, key=lambda item: (item[1], item[0])):
            report.append(f"| {label} | {line} | `{excerpt.replace('|', '\\\\|')}` |")
    else:
        report.append("No configured findings.")

    if missing_sections:
        report.extend(["", "### Missing sections", "", ", ".join(missing_sections)])
    if duplicate_sections:
        report.extend(["", "### Sections not appearing exactly once", "", ", ".join(duplicate_sections)])
    if missing_facts:
        report.extend(["", "### Missing required framework facts", "", "\\n".join(f"- {item}" for item in missing_facts)])

    report.extend([
        "",
        "## Review boundary",
        "",
        "This automated baseline checks structural integrity, placeholders, section counts, clauses 4–10, the 93-control total, Annex A theme counts, and current edition markers. It does not replace detailed technical, editorial, copyright, link, visual, accessibility, or standards-currentness review.",
        "",
    ])
    REPORT.write_text("\\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
