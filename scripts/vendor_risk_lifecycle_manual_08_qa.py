#!/usr/bin/env python3
"""Fail-closed controlled intake QA for Manual 08 — Vendor and Third-Party Risk Lifecycle."""

import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.compliance' / 'vendor-risk-lifecycle-manual-08-baseline.json'
REG = ROOT / '.compliance' / 'authoritative-sources.json'
CAT = ROOT / '.compliance' / 'manual-catalog.json'
MAN = ROOT / '07-third-party-risk' / 'Vendor_Risk_Lifecycle'
WF = ROOT / '.github' / 'workflows' / '16-vendor-risk-lifecycle-manual-08-qa.yml'

LANGUAGE_FILES = {
    'en': [
        MAN/'English/source/01_FOUNDATIONS_CHAPTERS_01_08.md',
        MAN/'English/source/02_DUE_DILIGENCE_CHAPTERS_09_16.md',
        MAN/'English/source/03_MONITORING_CHAPTERS_17_24.md',
        MAN/'English/source/04_EXIT_AND_ASSURANCE_CHAPTERS_25_32.md',
    ],
    'es-419': [
        MAN/'Spanish_es-419/source/01_FUNDAMENTOS_CAPITULOS_01_08.md',
        MAN/'Spanish_es-419/source/02_DEBIDA_DILIGENCIA_CAPITULOS_09_16.md',
        MAN/'Spanish_es-419/source/03_MONITOREO_CAPITULOS_17_24.md',
        MAN/'Spanish_es-419/source/04_SALIDA_Y_ASEGURAMIENTO_CAPITULOS_25_32.md',
    ],
    'pt-BR': [
        MAN/'Portuguese_pt-BR/source/01_FUNDAMENTOS_CAPITULOS_01_08.md',
        MAN/'Portuguese_pt-BR/source/02_DUE_DILIGENCE_CAPITULOS_09_16.md',
        MAN/'Portuguese_pt-BR/source/03_MONITORAMENTO_CAPITULOS_17_24.md',
        MAN/'Portuguese_pt-BR/source/04_SAIDA_E_ASSEGURACAO_CAPITULOS_25_32.md',
    ],
}

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def roots(text):
    words=re.findall(r'[a-z0-9]+', text.casefold())
    return {w[:-1] if len(w)>4 and w.endswith('s') else w for w in words}
def concept_present(concept, document_roots):
    needed=roots(str(concept)); return bool(needed) and needed.issubset(document_roots)

def chapter_numbers(text):
    return [int(x) for x in re.findall(r'(?mi)^##\s+(?:Chapter|Capítulo)\s+(\d+)\s+—', text)]

def main():
    errors=[]
    try:
        base, reg, cat = load(BASE), load(REG), load(CAT)
    except Exception as exc:
        print(f'FAIL: {exc}'); return 1
    if base.get('manual_id') != 'vendor-risk-lifecycle-manual-08': errors.append('unexpected manual id')
    if base.get('planned_publication_languages') != ['en','es-419','pt-BR']: errors.append('language plan changed')
    ids={x.get('id'):x for x in reg.get('sources',[]) if isinstance(x,dict)}
    for sid in base.get('required_source_ids',[]):
        if sid not in ids: errors.append(f'missing source: {sid}')

    readme=(MAN/'README.md').read_text(encoding='utf-8') if (MAN/'README.md').is_file() else ''
    entry=(MAN/'MANUAL_08_IMPLEMENTATION_PATHS.md').read_text(encoding='utf-8') if (MAN/'MANUAL_08_IMPLEMENTATION_PATHS.md').is_file() else ''
    combined=readme+'\n'+entry; combined_roots=roots(combined)
    for topic in base.get('required_topics',[]):
        if not concept_present(topic, combined_roots): errors.append(f'missing concept: {topic}')
    for boundary in base.get('required_boundaries',[]):
        if not concept_present(boundary, combined_roots): errors.append(f'missing boundary: {boundary}')

    for lang, files in LANGUAGE_FILES.items():
        missing=[str(p.relative_to(ROOT)) for p in files if not p.is_file()]
        if missing:
            errors.extend(f'missing {lang} source: {p}' for p in missing)
            continue
        text='\n'.join(p.read_text(encoding='utf-8') for p in files)
        chapters=chapter_numbers(text)
        if chapters != list(range(1,33)):
            errors.append(f'{lang} chapter sequence invalid: {chapters}')
        if lang != 'en' and not re.search(r'(?i)(revisi[oó]n sem[aâ]ntica humana|revisão semântica humana)', text):
            errors.append(f'{lang} localization must retain explicit human semantic review boundary')

    if len(re.findall(r'(?ms)^```mermaid\s*\n.*?^```\s*$', entry)) != 3: errors.append('expected exactly three Mermaid graphics')
    if entry.count('**Accessible explanation:**') != 3: errors.append('each graphic needs accessible explanation')
    matches=[x for x in cat.get('manuals',[]) if x.get('id')=='vendor-risk-lifecycle']
    if len(matches)!=1 or matches[0].get('status')!='development' or matches[0].get('series_order')!=8: errors.append('catalog entry invalid')
    if not WF.is_file(): errors.append('workflow missing')
    else:
        text=WF.read_text(encoding='utf-8')
        if 'permissions:\n  contents: read' not in text: errors.append('workflow not read-only')
        if re.search(r'(?m)^\s*push:\s*$', text): errors.append('workflow must not push')

    print('Manual 08 Vendor Risk Lifecycle QA')
    for e in errors: print('  ERROR:',e)
    if errors: print('FAIL'); return 1
    print('PASS'); return 0

if __name__=='__main__': sys.exit(main())
