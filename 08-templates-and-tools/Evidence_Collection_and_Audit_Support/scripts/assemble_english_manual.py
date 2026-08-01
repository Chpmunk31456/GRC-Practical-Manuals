from __future__ import annotations

import hashlib
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = sorted((ROOT / "chapters").glob("*.md"))
OUTPUT_DIR = ROOT / "English"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT = OUTPUT_DIR / "Evidence_Collection_and_Audit_Support_Practical_Manual_English_v1.0.md"

TITLE = "# Evidence Collection and Audit Support Practical Manual\n\n"
FRONT = f"""**Author:** Alberto “Al” Leiva  
**Edition:** English v1.0  
**Controlled build date:** {date.today().isoformat()}  

ChatGPT assisted under the author's direction. The author remains responsible for editorial and release decisions.

> **Educational notice:** This manual provides general professional guidance. It does not constitute legal, regulatory, accounting, certification, or formal audit advice. Adapt it to applicable criteria, contracts, systems, data, risks, and retention obligations.

---

"""

if len(CHAPTERS) != 6:
    raise SystemExit(f"Expected 6 controlled chapters, found {len(CHAPTERS)}")

parts = [TITLE, FRONT]
for chapter in CHAPTERS:
    text = chapter.read_text(encoding="utf-8").strip()
    if not text.startswith("# "):
        raise SystemExit(f"Missing level-one heading: {chapter}")
    parts.append(text + "\n\n---\n\n")

parts.append("# Appendix A — Operational Templates\n\n")
parts.append("The publication package includes the following editable CSV tools:\n\n")
for template in sorted((ROOT / "templates").glob("*.csv")):
    header = template.read_text(encoding="utf-8").splitlines()[0]
    field_count = len(header.split(","))
    parts.append(f"- **{template.name}** — {field_count} fields.\n")
parts.append("\n")
parts.append((ROOT / "SOURCES.md").read_text(encoding="utf-8").strip() + "\n")

content = "".join(parts)
if "TODO" in content or "TBD" in content:
    raise SystemExit("Unresolved drafting marker found")
OUTPUT.write_text(content, encoding="utf-8")

report = {
    "status": "PASS",
    "chapters": len(CHAPTERS),
    "templates": len(list((ROOT / "templates").glob("*.csv"))),
    "words": len(content.split()),
    "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
    "output": str(OUTPUT.relative_to(ROOT)),
}
(OUTPUT_DIR / "ENGLISH_ASSEMBLY_REPORT.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
(OUTPUT_DIR / "ENGLISH_ASSEMBLY_REPORT.md").write_text(
    "# English Assembly Report\n\n"
    f"- Status: **{report['status']}**\n"
    f"- Controlled chapters: {report['chapters']}\n"
    f"- Editable CSV tools: {report['templates']}\n"
    f"- Approximate words: {report['words']}\n"
    f"- Markdown SHA-256: `{report['sha256']}`\n",
    encoding="utf-8",
)
print(OUTPUT)
