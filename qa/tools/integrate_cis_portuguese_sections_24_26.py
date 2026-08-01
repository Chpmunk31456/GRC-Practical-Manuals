#!/usr/bin/env python3
from pathlib import Path
import re

TARGET = Path('01-foundations/CIS_Controls_v8.1/Portugues_BR/CIS_Critical_Security_Controls_v8.1_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
REPLACEMENT = Path('qa/rewrite/CIS_CONTROLS_V8_1_PTBR_SECTIONS_24_26_REVIEWED.md')

text = TARGET.read_text(encoding='utf-8')
replacement = REPLACEMENT.read_text(encoding='utf-8').rstrip() + '\n\n'
start = re.compile(r'^#\s*24\.\s*Ferramentas\s+de\s+c[oó]digo\s+aberto\b.*$', re.MULTILINE | re.IGNORECASE)
end = re.compile(r'^#\s*27\.\s*Laborat[oó]rio\b.*$', re.MULTILINE | re.IGNORECASE)
starts = list(start.finditer(text)); ends = list(end.finditer(text))
if len(starts) != 1 or len(ends) != 1 or starts[0].start() >= ends[0].start():
    raise SystemExit(f'Invalid bounded section state: start={len(starts)} end={len(ends)}')
new_text = text[:starts[0].start()] + replacement + text[ends[0].start():]
block = replacement
for section in (24, 25, 26):
    if len(re.findall(rf'^#\s+{section}\.\s+.+$', block, re.MULTILINE)) != 1:
        raise SystemExit(f'Expected exactly one level-one heading for Section {section}')
for subsection in range(1, 17):
    if len(re.findall(rf'^##\s+24\.{subsection}\s+.+$', block, re.MULTILINE)) != 1:
        raise SystemExit(f'Expected exactly one tool subsection 24.{subsection}')
for token in ['□', '# # ', 'O que é que se passa?', '(--------------------------------', '• **Ferramenta']:
    if token in block:
        raise SystemExit(f'Forbidden corruption token remains: {token}')
if block.count('media/image10.png') != 1:
    raise SystemExit('Expected exactly one Section 26 image reference')
if len(end.findall(new_text)) != 1:
    raise SystemExit('Section 27 boundary was not preserved exactly once')
TARGET.write_text(new_text, encoding='utf-8')
print('Integrated reviewed CIS Portuguese Sections 24-26')
