#!/usr/bin/env python3
from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

TARGET = Path("01-foundations/NIST_RMF_SP_800-53/English_Source_NIST_RMF_and_SP_800-53_Release_5.2.0_Practical_Manual_v1.0.md")
REPORT = Path("qa/NIST_RMF_SP_800_53_ENGLISH_MASTER_AUDIT.md")

PATTERNS = {
    "conversion box glyph": re.compile(r"□"),
    "broken image marker": re.compile(r"^[■□]img\b", re.MULTILINE | re.IGNORECASE),
    "double heading marker": re.compile(r"^#\s+#\s+", re.MULTILINE),
    "raw separator line": re.compile(r"^-{20,}$", re.MULTILINE),
    "empty markdown link": re.compile(r"\[[^\]]+\]\(\s*\)"),
    "placeholder token": re.compile(r"\b(?:TBD|TODO|FIXME|PLACEHOLDER)\b", re.IGNORECASE),
    "malformed Word contents label": re.compile(r"\*\*True Word contents:\*\*", re.IGNORECASE),
}

REQUIRED_SECTIONS = [re.compile(rf"^#\s+{n}\.\s+", re.MULTILINE) for n in range(1, 31)]
REQUIRED_FACTS = {
    "seven RMF steps": "seven RMF steps",
    "20 control families": "all 20 SP 800-53 control families",
    "SP 800-37 Rev. 2": "SP 800-37 Rev. 2",
    "Release 5.2.0": "Release 5.2.0",
    "SP 800-18 Rev. 2": "SP 800-18 Rev. 2",
    "Prepare": "# 5. Prepare at the Organization Level",
    "Categorize": "# 7. Categorize the System",
    "Select": "# 8. Select Controls",
    "Implement": "# 9. Implement Controls",
    "Assess": "# 10. Assess Controls",
    "Authorize": "# 11. Authorize the System or Common Controls",
    "Monitor": "# 12. Monitor Continuously",
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
        "# NIST RMF and SP 800-53 English Master Audit",
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
        "This automated baseline checks structural integrity, placeholders, section counts, the seven RMF steps, current publication markers, and the stated control-family count. It does not replace detailed technical, editorial, link, visual, accessibility, or standards-currentness review.",
        "",
    ])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {REPORT}: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
