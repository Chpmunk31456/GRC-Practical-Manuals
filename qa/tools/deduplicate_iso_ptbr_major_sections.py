#!/usr/bin/env python3
from pathlib import Path
import re

p = Path('02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md')
text = p.read_text(encoding='utf-8')
head = re.compile(r'^#\s+(\d+)\.\s+.+$', re.M)
matches = list(head.finditer(text))
if not matches:
    raise SystemExit('No major section headings found')

preamble = text[:matches[0].start()]
sections = {}
for i, m in enumerate(matches):
    number = int(m.group(1))
    end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
    sections.setdefault(number, []).append(text[m.start():end].rstrip() + '\n')

missing = [n for n in range(1, 29) if n not in sections]
if missing:
    raise SystemExit(f'Missing major sections before deduplication: {missing}')

# Keep the last occurrence because regeneration workflows operate on the body copy,
# while earlier duplicates are conversion artifacts near the front of the document.
chosen = [sections[n][-1].rstrip() for n in range(1, 29)]
new_text = preamble.rstrip() + '\n\n' + '\n\n'.join(chosen) + '\n'

counts = {n: len(re.findall(rf'^#\s+{n}\.\s+', new_text, flags=re.M)) for n in range(1, 29)}
bad = {n: c for n, c in counts.items() if c != 1}
if bad:
    raise SystemExit(f'Unexpected post-deduplication heading counts: {bad}')

p.write_text(new_text, encoding='utf-8')
print('Deduplicated ISO PT-BR major sections; retained one ordered occurrence of sections 1-28')
