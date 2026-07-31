#!/usr/bin/env python3
from pathlib import Path

TARGET = Path('01-foundations/CIS_Controls_v8.1/Espanol/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_ES_SECTIONS_25_TO_28_REVIEWED.md')
START = '# 25.'
END = '# 29.'

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'
start = text.find(START)
end = text.find(END, start)
if start < 0 or end < 0 or end <= start:
    raise SystemExit('Could not locate bounded sections 25 through 28.')

required = ['# 25.', '# 26.', '# 27.', '# 28.', 'media/image10.png']
missing = [item for item in required if item not in replacement]
if missing:
    raise SystemExit(f'Replacement missing required markers: {missing}')

forbidden = ['TEN ', 'tención', 'Silencioso', '■img', '←', '|... |']
present = [item for item in forbidden if item in replacement]
if present:
    raise SystemExit(f'Replacement contains forbidden corruption markers: {present}')

updated = text[:start] + replacement + text[end:]
TARGET.write_text(updated, encoding='utf-8')
print('Integrated reviewed CIS Spanish sections 25 through 28.')
