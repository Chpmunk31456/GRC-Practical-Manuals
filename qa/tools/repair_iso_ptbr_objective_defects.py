#!/usr/bin/env python3
"""Repair objective ISO PT-BR source defects and inventory collapsed table contexts.

This script deliberately does not infer or fabricate table columns. It fixes only
unambiguous text/Markdown defects and emits evidence for controlled table repair.
"""
from pathlib import Path
import re

SOURCE = Path("02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md")
REPORT = Path("qa/ISO_IEC_27001_27002_PTBR_COLLAPSED_TABLE_CONTEXTS.md")

text = SOURCE.read_text(encoding="utf-8")
replacements = {
    "** SÉRIES PRÁTICAS DE CIBERSegurança, PRIVACIDADE E CONFORMIDADE": "**SÉRIE PRÁTICA DE CIBERSEGURANÇA, PRIVACIDADE E CONFORMIDADE**",
    "* Um manual de trabalho para gerentes, analistas júnior, estudantes, mudadores de carreira, auditores internos e equipes de segurança*": "*Um manual de trabalho para gerentes, analistas juniores, estudantes, profissionais em transição de carreira, auditores internos e equipes de segurança*",
    ". **Ferramenta** . **Purpose** . **Possível suporte** .": ". **Ferramenta** . **Finalidade** . **Possível suporte** .",
}

for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one occurrence before replacement: {old!r}; found {count}")
    text = text.replace(old, new)

SOURCE.write_text(text, encoding="utf-8")

lines = text.splitlines()
rule_rx = re.compile(r"^-{20,}$")
contexts = []
for index, line in enumerate(lines):
    if not rule_rx.fullmatch(line):
        continue
    start = max(0, index - 4)
    end = min(len(lines), index + 6)
    contexts.append((index + 1, start + 1, end, lines[start:end]))

out = [
    "# ISO/IEC 27001/27002 PT-BR Collapsed Table Contexts",
    "",
    "This diagnostic inventories long rule rows that indicate collapsed table conversions.",
    "It is evidence for manual or section-specific reconstruction and does not alter table structure.",
    "",
    f"- Source: `{SOURCE}`",
    f"- Collapsed rule rows: **{len(contexts)}**",
    "",
]
for ordinal, (line_number, start, end, snippet) in enumerate(contexts, 1):
    out.extend([
        f"## Context {ordinal} — source line {line_number}",
        "",
        f"Lines {start}–{end}:",
        "",
        "```text",
    ])
    for n, value in enumerate(snippet, start):
        out.append(f"{n:>5}: {value}")
    out.extend(["```", ""])

REPORT.write_text("\n".join(out), encoding="utf-8")
print(f"Repaired 3 objective defects; inventoried {len(contexts)} collapsed table rows")
