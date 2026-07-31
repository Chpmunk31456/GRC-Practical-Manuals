#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_PTBR_CONTROLS_11_14_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'
start = re.compile(r'^#\s*16\.\s*Controle\s+11\b.*$', re.MULTILINE | re.IGNORECASE)
end = re.compile(r'^#\s*20\.\s*Controle\s+15\b.*$', re.MULTILINE | re.IGNORECASE)
starts = list(start.finditer(text))
ends = list(end.finditer(text))
if len(starts) != 1 or len(ends) != 1 or ends[0].start() <= starts[0].start():
    raise SystemExit(f'Invalid boundaries: starts={len(starts)} ends={len(ends)}')
new_text = text[:starts[0].start()] + replacement + text[ends[0].start():]

expected = {11: 5, 12: 8, 13: 11, 14: 9}
for control, count in expected.items():
    ids = re.findall(rf'^\|\s*{control}\.(\d+)\s*\|', replacement, re.MULTILINE)
    wanted = [str(n) for n in range(1, count + 1)]
    if ids != wanted:
        raise SystemExit(f'Control {control} safeguard IDs invalid: {ids}')

for section, control in [(16,11),(17,12),(18,13),(19,14)]:
    pattern = re.compile(rf'^#\s+{section}\.\s+Controle\s+{control}\b.*$', re.MULTILINE | re.IGNORECASE)
    if len(pattern.findall(replacement)) != 1:
        raise SystemExit(f'Expected one heading for Section {section}/Control {control}')

if replacement.count('media/image8.png') != 1:
    raise SystemExit('Expected exactly one image8 reference')
for token in ['□', '■img', '# # ', '| . . .', 'O que é que se passa?']:
    if token in replacement:
        raise SystemExit(f'Forbidden corruption token remains: {token}')
if len(end.findall(new_text)) != 1:
    raise SystemExit('Control 15 boundary was not preserved exactly once')

TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Portuguese Controls 11-14')
