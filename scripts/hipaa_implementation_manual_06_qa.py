#!/usr/bin/env python3
"""Fail-closed controlled intake QA for Manual 06 — HIPAA Implementation and Audit."""

import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.compliance' / 'hipaa-implementation-manual-06-baseline.json'
REG = ROOT / '.compliance' / 'authoritative-sources.json'
CAT = ROOT / '.compliance' / 'manual-catalog.json'
MAN = ROOT / '04-regulatory-compliance' / 'HIPAA_Implementation_Series'
WF = ROOT / '.github' / 'workflows' / '14-hipaa-implementation-manual-06-qa.yml'

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def roots(text):
    words=re.findall(r'[a-z0-9]+', text.casefold())
    return {w[:-1] if len(w)>4 and w.endswith('s') else w for w in words}
def concept_present(concept, document_roots):
    needed=roots(str(concept)); return bool(needed) and needed.issubset(document_roots)

def main():
    errors=[]
    try:
        base, reg, cat = load(BASE), load(REG), load(CAT)
    except Exception as exc:
        print(f'FAIL: {exc}'); return 1
    if base.get('manual_id') != 'hipaa-implementation-manual-06': errors.append('unexpected manual id')
    if base.get('planned_publication_languages') != ['en','es-419','pt-BR']: errors.append('language plan changed')
    ids={x.get('id'):x for x in reg.get('sources',[]) if isinstance(x,dict)}
    for sid in base.get('required_source_ids',[]):
        if sid not in ids: errors.append(f'missing source: {sid}')
    for sid in base.get('current_law_source_ids',[]):
        if ids.get(sid,{}).get('status') != 'final': errors.append(f'current-law source status mismatch: {sid}')
    for sid in base.get('proposed_only_source_ids',[]):
        if ids.get(sid,{}).get('status') != 'proposed-not-current-law': errors.append(f'proposed-rule status mismatch: {sid}')
    readme=(MAN/'README.md').read_text(encoding='utf-8') if (MAN/'README.md').is_file() else ''
    entry=(MAN/'MANUAL_06_IMPLEMENTATION_PATHS.md').read_text(encoding='utf-8') if (MAN/'MANUAL_06_IMPLEMENTATION_PATHS.md').is_file() else ''
    combined=readme+'\n'+entry; combined_roots=roots(combined)
    for topic in base.get('required_topics',[]):
        if not concept_present(topic, combined_roots): errors.append(f'missing concept: {topic}')
    if not concept_present('proposed rule', combined_roots) or not concept_present('current law', combined_roots): errors.append('current/proposed legal boundary missing')
    if len(re.findall(r'(?ms)^```mermaid\s*\n.*?^```\s*$', entry)) != 3: errors.append('expected exactly three Mermaid graphics')
    if entry.count('**Accessible explanation:**') != 3: errors.append('each graphic needs accessible explanation')
    matches=[x for x in cat.get('manuals',[]) if x.get('id')=='hipaa-implementation-series']
    if len(matches)!=1 or matches[0].get('status')!='development' or matches[0].get('series_order')!=6: errors.append('catalog entry invalid')
    if not WF.is_file(): errors.append('workflow missing')
    else:
        text=WF.read_text(encoding='utf-8')
        if 'permissions:\n  contents: read' not in text: errors.append('workflow not read-only')
        if re.search(r'(?m)^\s*push:\s*$', text): errors.append('workflow must not push')
    print('Manual 06 HIPAA controlled intake QA')
    for e in errors: print('  ERROR:',e)
    if errors: print('FAIL'); return 1
    print('PASS'); return 0

if __name__=='__main__': sys.exit(main())
