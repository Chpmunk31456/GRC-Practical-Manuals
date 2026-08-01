#!/usr/bin/env python3
"""Restore Markdown table structure in ISO PT-BR sections 13-16.

The source rows are preserved in their existing order. Control identifiers come from
the fixed ISO/IEC 27002:2022 Annex A sequence. The script fails closed if row counts
or repeated column markers do not match expectations.
"""
from pathlib import Path
import re

P = Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
HEAD = re.compile(r'^#\s+(\d+)\.\s+.+$', re.M)
VERIFY = 'Confirmar risco ou obrigação, design, proprietário, implementação, operação, exceções e medição.'
EVIDENCE = 'Procedimento, configuração, registro, registro, ticket, revisão, teste ou observação.'

CONTROLS = {
    13: [f'5.{n}' for n in range(1, 38)],
    14: [f'6.{n}' for n in range(1, 9)],
    15: [f'7.{n}' for n in range(1, 15)],
    16: [f'8.{n}' for n in range(1, 35)],
}


def bounds(text: str, section: int) -> tuple[int, int]:
    matches = list(HEAD.finditer(text))
    start_match = next((m for m in matches if int(m.group(1)) == section), None)
    if not start_match:
        raise SystemExit(f'missing section {section}')
    end = next((m.start() for m in matches if m.start() > start_match.start()), len(text))
    return start_match.start(), end


def clean_meaning(line: str) -> str:
    prefix = line.split(VERIFY, 1)[0]
    prefix = re.sub(r'^[\s□•.!*]+', '', prefix)
    prefix = re.sub(r'^\d+[,.]\d+(?:\.\d+)?\s*', '', prefix)
    prefix = re.sub(r'^[\s□•.!*]+', '', prefix)
    return prefix.strip()


def rebuild(section_text: str, controls: list[str]) -> str:
    lines = section_text.splitlines()
    row_lines = [line.strip() for line in lines if VERIFY in line and EVIDENCE in line]
    if len(row_lines) != len(controls):
        raise SystemExit(f'row-count mismatch: expected {len(controls)}, found {len(row_lines)}')
    meanings = [clean_meaning(line) for line in row_lines]
    if any(not value for value in meanings):
        raise SystemExit('empty practical-meaning cell after parsing')

    intro_end = next((i for i, line in enumerate(lines) if line.strip().startswith('* Resumos originais')), None)
    rule_start = next((i for i, line in enumerate(lines) if 'Regra da seleção:' in line), None)
    if intro_end is None or rule_start is None or rule_start <= intro_end:
        raise SystemExit('unable to locate Annex table boundaries')

    table = [
        '',
        '| **Controle** | **Significado prático** | **Foco de verificação** | **Exemplo de evidência** |',
        '|---|---|---|---|',
    ]
    for control, meaning in zip(controls, meanings):
        meaning = meaning.replace('|', '\\|')
        table.append(f'| {control} | {meaning} | {VERIFY} | {EVIDENCE} |')
    table.append('')

    tail = lines[rule_start:]
    while tail and re.fullmatch(r'-{20,}', tail[-1].strip()):
        tail.pop()
    tail = [line for line in tail if not re.fullmatch(r'-{20,}', line.strip())]
    if tail:
        tail[0] = '**Regra de seleção:** O Anexo A é um conjunto de referência usado para verificar se controles necessários não foram ignorados. A organização pode precisar de outros controles. Toda inclusão ou exclusão deve ser justificada pelo tratamento de riscos e registrada na Declaração de Aplicabilidade.'

    return '\n'.join(lines[:intro_end + 1] + table + tail).rstrip() + '\n'


text = P.read_text(encoding='utf-8')
for section, controls in CONTROLS.items():
    start, end = bounds(text, section)
    text = text[:start] + rebuild(text[start:end], controls) + '\n' + text[end:]

for section, controls in CONTROLS.items():
    start, end = bounds(text, section)
    chunk = text[start:end]
    pipe_rows = sum(1 for line in chunk.splitlines() if line.count('|') >= 2)
    if pipe_rows < len(controls) + 2:
        raise SystemExit(f'section {section} table validation failed: {pipe_rows} pipe rows')

P.write_text(text, encoding='utf-8')
print('Normalized ISO PT-BR Annex tables in sections 13-16')
