#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

TARGET = Path("04-regulatory-compliance/PCI_DSS_v4.0.1/English_Source_PCI_DSS_v4.0.1_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md")
REPORT = Path("qa/PCI_DSS_V4_0_1_ENGLISH_MASTER_AUDIT.md")

PATTERNS = {
    "conversion box glyph": re.compile(r"□"),
    "broken image marker": re.compile(r"^[■□]img\b", re.MULTILINE | re.IGNORECASE),
    "double heading marker": re.compile(r"^#\s+#\s+", re.MULTILINE),
    "raw separator line": re.compile(r"^-{20,}$", re.MULTILINE),
    "empty markdown link": re.compile(r"\[[^\]]+\]\(\s*\)"),
    "placeholder token": re.compile(r"\b(?:TBD|TODO|FIXME|PLACEHOLDER)\b", re.IGNORECASE),
    "malformed Word contents label": re.compile(r"\*\*True Word contents:\*\*", re.IGNORECASE),
}

REQUIRED_SECTIONS = [re.compile(rf"^#\s+{n}\.\s+", re.MULTILINE) for n in range(1, 26)]
REQUIRED_FACTS = {
    "PCI DSS v4.0.1": "PCI DSS v4.0.1",
    "12 requirements": "all 12 requirements",
    "June 2024": "June 2024",
    "v4.0 retirement date": "December 31, 2024",
    "future-dated effective date": "March 31, 2025",
    "Requirement 1": "# 6. Requirement 1",
    "Requirement 2": "# 7. Requirement 2",
    "Requirement 3": "# 8. Requirement 3",
    "Requirement 4": "# 9. Requirement 4",
    "Requirement 5": "# 10. Requirement 5",
    "Requirement 6": "# 11. Requirement 6",
    "Requirement 7": "# 12. Requirement 7",
    "Requirement 8": "# 13. Requirement 8",
    "Requirement 9": "# 14. Requirement 9",
    "Requirement 10": "# 15. Requirement 10",
    "Requirement 11": "# 16. Requirement 11",
    "Requirement 12": "# 17. Requirement 12",
}


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


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
        "# PCI DSS v4.0.1 English Master Audit",
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
            report.append(f"| {label} | {line} | `{excerpt.replace('|', '\\|')}` |")
    else:
        report.append("No configured findings.")

    if missing_sections:
        report.extend(["", "### Missing sections", "", ", ".join(missing_sections)])
    if duplicate_sections:
        report.extend(["", "### Sections not appearing exactly once", "", ", ".join(duplicate_sections)])
    if missing_facts:
        report.extend(["", "### Missing required framework facts", "", "\n".join(f"- {item}" for item in missing_facts)])

    report.extend([
        "",
        "## Review boundary",
        "",
        "This automated baseline checks structural integrity, placeholders, section counts, all 12 requirement headings, version status, retirement date, and the future-dated-requirement effective date. It does not replace detailed technical, editorial, copyright, link, visual, accessibility, assessor, or standards-currentness review.",
        "",
    ])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
