#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_PTBR_SECTIONS_11_15_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'

start_re = re.compile(r'^#\s*11\.\s*Controle\s+6\b.*$', re.MULTILINE | re.IGNORECASE)
end_re = re.compile(r'^#\s*16\.\s*Controle\s+11\b.*$', re.MULTILINE | re.IGNORECASE)
starts = list(start_re.finditer(text))
ends = list(end_re.finditer(text))
if len(starts) != 1 or len(ends) != 1 or starts[0].start() >= ends[0].start():
    raise SystemExit(f'Expected one ordered Control 6/Control 11 boundary; found starts={len(starts)} ends={len(ends)}')

expected = {
    11: [f'6.{i}' for i in range(1, 9)],
    12: [f'7.{i}' for i in range(1, 8)],
    13: [f'8.{i}' for i in range(1, 13)],
    14: [f'9.{i}' for i in range(1, 8)],
    15: [f'10.{i}' for i in range(1, 8)],
}
for section, ids in expected.items():
    if len(re.findall(rf'^#\s+{section}\.\s+.+$', replacement, re.MULTILINE)) != 1:
        raise SystemExit(f'Expected exactly one Section {section} heading')
    for safeguard in ids:
        count = len(re.findall(rf'^\|\s*{re.escape(safeguard)}\s*\|', replacement, re.MULTILINE))
        if count != 1:
            raise SystemExit(f'Expected exactly one row for safeguard {safeguard}; found {count}')

rows = re.findall(r'^\|\s*(?:6|7|8|9|10)\.\d+\s*\|', replacement, re.MULTILINE)
if len(rows) != 41:
    raise SystemExit(f'Expected 41 safeguard rows; found {len(rows)}')

for marker in ['media/image6.png', 'media/image7.png']:
    if replacement.count(marker) != 1:
        raise SystemExit(f'Expected exactly one image reference: {marker}')

for token in ['□', '■img', '# # ', '|... |']:
    if token in replacement:
        raise SystemExit(f'Forbidden corruption token remains: {token}')

new_text = text[:starts[0].start()] + replacement + text[ends[0].start():]
if len(end_re.findall(new_text)) != 1:
    raise SystemExit('Control 11 boundary was not preserved exactly once')

TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Portuguese Controls 6-10')
