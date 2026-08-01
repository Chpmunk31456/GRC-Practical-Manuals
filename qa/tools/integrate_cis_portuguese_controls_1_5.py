#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_PTBR_CONTROLS_1_5_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'
start = re.compile(r'^#\s*6\.\s*Controle\s+1\b.*$', re.MULTILINE | re.IGNORECASE)
end = re.compile(r'^#\s*11\.\s*Controle\s+6\b.*$', re.MULTILINE | re.IGNORECASE)
starts = list(start.finditer(text))
ends = list(end.finditer(text))
if len(starts) != 1 or len(ends) != 1 or starts[0].start() >= ends[0].start():
    raise SystemExit(f'Invalid bounded region: starts={len(starts)}, ends={len(ends)}')

new_text = text[:starts[0].start()] + replacement + text[ends[0].start():]
block = new_text[starts[0].start():new_text.index(text[ends[0].start():])]

for marker in ['# 6.', '# 7.', '# 8.', '# 9.', '# 10.']:
    if block.count(marker) != 1:
        raise SystemExit(f'Expected exactly one section marker: {marker}')

expected = {
    1: range(1, 6),
    2: range(1, 8),
    3: range(1, 15),
    4: range(1, 13),
    5: range(1, 7),
}
for control, safeguards in expected.items():
    for safeguard in safeguards:
        token = f'| {control}.{safeguard} |'
        if block.count(token) != 1:
            raise SystemExit(f'Expected exactly one safeguard row: {control}.{safeguard}')

for token in ['□', '■img', '# # ', '--------------------']:
    if token in block:
        raise SystemExit(f'Forbidden corruption token remains in replacement block: {token}')

if new_text.count('# 11. Controle 6') != 1:
    raise SystemExit('Control 6 boundary was not preserved exactly once')

TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Portuguese Controls 1-5')
