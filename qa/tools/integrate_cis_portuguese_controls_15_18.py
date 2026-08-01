#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_PTBR_CONTROLS_15_18_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'
start = re.compile(r'^#\s*20\.\s*Controle\s+15\b.*$', re.MULTILINE | re.IGNORECASE)
end = re.compile(r'^#\s*24\.\s*Ferramentas\s+de\s+C[oó]digo\s+Aberto\b.*$', re.MULTILINE | re.IGNORECASE)
starts = list(start.finditer(text)); ends = list(end.finditer(text))
if len(starts) != 1 or len(ends) != 1 or starts[0].start() >= ends[0].start():
    raise SystemExit(f'Invalid bounded section state: start={len(starts)} end={len(ends)}')
new_text = text[:starts[0].start()] + replacement + text[ends[0].start():]
block = replacement
expected_rows = {15: 7, 16: 14, 17: 9, 18: 5}
for control, count in expected_rows.items():
    ids = re.findall(rf'^\|\s*{control}\.\d+\s*\|', block, re.MULTILINE)
    if len(ids) != count:
        raise SystemExit(f'Control {control}: expected {count} safeguard rows; found {len(ids)}')
for section in range(20, 24):
    if len(re.findall(rf'^#\s+{section}\.\s+.+$', block, re.MULTILINE)) != 1:
        raise SystemExit(f'Expected exactly one level-one heading for Section {section}')
for token in ['□', '# # ', '. ** Finalidade', 'Train Workforce', 'Vetted']:
    if token in block:
        raise SystemExit(f'Forbidden corruption token remains: {token}')
if block.count('media/image9.png') != 1:
    raise SystemExit('Expected exactly one Control 17 image reference')
if len(end.findall(new_text)) != 1:
    raise SystemExit('Section 24 boundary was not preserved exactly once')
TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Portuguese Controls 15-18')
