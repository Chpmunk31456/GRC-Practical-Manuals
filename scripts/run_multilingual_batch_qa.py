from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "qa" / "batch"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

TARGETS = sorted(
    p for p in ROOT.rglob("*.md")
    if any(part in {"Espanol", "Portugues_BR"} for part in p.parts)
    and "qa" not in p.parts
)

ENGLISH_MARKERS = {
    "Espanol": [
        "Plain meaning", "Manager or analyst verification", "Example evidence",
        "Quick start", "Evidence and limitation", "Table of Contents",
    ],
    "Portugues_BR": [
        "Plain meaning", "Manager or analyst verification", "Example evidence",
        "Quick start", "Evidence and limitation", "Table of Contents",
    ],
}

KNOWN_DEFECTS = [
    "Función del PROTECTO", "Conteúdo verdadeiro da palavra", "COMPLIANÇA",
    "Tiros", "Gerente ou verificação do analista", "Significado liso",
]

HEADING_RE = re.compile(r"^# (\d+)\.", re.MULTILINE)
IMAGE_RE = re.compile(r"<img\s+[^>]*alt=\"([^\"]*)\"", re.IGNORECASE)

results: list[dict[str, object]] = []
for path in TARGETS:
    text = path.read_text(encoding="utf-8", errors="replace")
    lang = "Espanol" if "Espanol" in path.parts else "Portugues_BR"
    headings = sorted({int(x) for x in HEADING_RE.findall(text)})
    markers = [m for m in ENGLISH_MARKERS[lang] if m in text]
    defects = [d for d in KNOWN_DEFECTS if d in text]
    empty_alt = sum(1 for alt in IMAGE_RE.findall(text) if not alt.strip())
    malformed_tables = sum(
        1 for line in text.splitlines()
        if line.startswith("|") and line.count("|") < 2
    )
    status = "PASS" if not markers and not defects and not empty_alt and not malformed_tables else "REVIEW"
    results.append({
        "file": str(path.relative_to(ROOT)),
        "language": lang,
        "status": status,
        "chapter_headings": headings,
        "english_markers": markers,
        "known_defects": defects,
        "empty_alt_text_count": empty_alt,
        "malformed_table_line_count": malformed_tables,
        "characters": len(text),
        "lines": text.count("\n") + 1,
    })

summary = {
    "files_scanned": len(results),
    "pass": sum(r["status"] == "PASS" for r in results),
    "review": sum(r["status"] == "REVIEW" for r in results),
    "results": results,
}

(REPORT_DIR / "MULTILINGUAL_BATCH_QA.json").write_text(
    json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

lines = [
    "# Multilingual Batch QA Report",
    "",
    f"Files scanned: **{summary['files_scanned']}**",
    f"Automated pass: **{summary['pass']}**",
    f"Requires review: **{summary['review']}**",
    "",
    "| Status | Language | File | English leakage | Known defects | Empty alt text | Malformed table lines |",
    "|---|---|---|---:|---:|---:|---:|",
]
for row in results:
    lines.append(
        f"| {row['status']} | {row['language']} | `{row['file']}` | "
        f"{len(row['english_markers'])} | {len(row['known_defects'])} | "
        f"{row['empty_alt_text_count']} | {row['malformed_table_line_count']} |"
    )
lines += [
    "",
    "> Automated PASS means only that the listed mechanical checks passed. It does not constitute human language review, factual verification, accessibility approval, or publication approval.",
]
(REPORT_DIR / "MULTILINGUAL_BATCH_QA.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

print(json.dumps({k: summary[k] for k in ("files_scanned", "pass", "review")}, indent=2))
