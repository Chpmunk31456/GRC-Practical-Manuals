#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_ES_SECTIONS_1_5_REVIEWED.md')
START = '# 1.'
END = '# 6.'

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'
start = text.find(START)
end = text.find(END, start + len(START))
if start < 0 or end < 0 or end <= start:
    raise SystemExit('Unable to locate unique Sections 1-5 boundaries')
new_text = text[:start] + replacement + text[end:]
for marker in [f'# {n}.' for n in range(1, 6)]:
    if new_text.count(marker) != 1:
        raise SystemExit(f'Expected exactly one marker: {marker}')
for token in ['■img', '|... |', '← Salvaguardia', 'Silencioso Propietario']:
    block = new_text[new_text.find('# 1.'):new_text.find('# 6.')]
    if token in block:
        raise SystemExit(f'Forbidden corruption token remains in replacement block: {token}')
TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Spanish Sections 1-5')
