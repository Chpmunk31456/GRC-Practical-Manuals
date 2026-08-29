#!/usr/bin/env python3
"""Fail-closed controlled-build QA for Manual 12 — CCPA / CPRA."""

import json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'.compliance/ccpa-cpra-manual-12-baseline.json'
SOURCES = ROOT/'.compliance/ccpa-cpra-manual-12-sources.json'
CAT = ROOT/'.compliance/manual-catalog.json'
MAN = ROOT/'04-regulatory-compliance/CCPA_CPRA_Controlled_Implementation'
WF = ROOT/'.github/workflows/31-ccpa-cpra-manual-12-qa.yml'
ENGLISH = [
    MAN/'English/source/01_FOUNDATIONS_CHAPTERS_01_08.md',
    MAN/'English/source/02_NOTICES_RIGHTS_OPT_OUT_CHAPTERS_09_16.md',
    MAN/'English/source/03_RISK_SECURITY_ADMT_THIRD_PARTIES_CHAPTERS_17_24.md',
    MAN/'English/source/04_RETENTION_DATA_BROKERS_ENFORCEMENT_CHAPTERS_25_32.md',
]
GATES = [
    MAN/'qa/SOURCE_VERIFICATION_2026-08-27.md',
    MAN/'qa/LOCALIZATION_SEMANTIC_REVIEW_GATE.md',
    MAN/'qa/DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md',
    MAN/'qa/RELEASE_READINESS_PRESTAGE.md',
]

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def chapters(text): return [int(x) for x in re.findall(r'(?mi)^##\s+Chapter\s+(\d+)\s+—', text)]

def main():
    errors=[]
    try:
        base,sources,cat=load(BASE),load(SOURCES),load(CAT)
    except Exception as exc:
        print(f'FAIL: {exc}'); return 1
    if base.get('manual_id')!='ccpa-cpra-controlled-manual-12': errors.append('unexpected manual id')
    if base.get('series_order')!=12: errors.append('series order must be 12')
    if base.get('planned_publication_languages')!=['en','es-419','pt-BR']: errors.append('language plan changed')
    if not base.get('training_grade'): errors.append('training-grade requirement missing')
    if sources.get('manual_id')!='ccpa-cpra-controlled-manual-12': errors.append('unexpected source supplement id')
    rows=[x for x in sources.get('sources',[]) if isinstance(x,dict)]
    ids={x.get('id') for x in rows}
    for sid in base.get('required_source_ids',[]):
        if sid not in ids: errors.append(f'missing source id: {sid}')
    current=[x for x in rows if x.get('id')=='cppa-ccpa-regulations-2026']
    if len(current)!=1 or current[0].get('status')!='final-effective' or current[0].get('source_type')!='binding-regulation':
        errors.append('current 2026 CPPA regulation classification invalid')
    dates=sources.get('controlled_2026_dates',{})
    if dates.get('updated_regulations_effective')!='2026-01-01': errors.append('2026 regulation effective date changed')
    if dates.get('admt_requirements_begin')!='2027-01-01': errors.append('ADMT phased date changed')
    missing=[str(p.relative_to(ROOT)) for p in ENGLISH if not p.is_file()]
    if missing: errors.extend(f'missing English source: {p}' for p in missing)
    else:
        text='\n'.join(p.read_text(encoding='utf-8') for p in ENGLISH)
        nums=chapters(text)
        if nums!=list(range(1,33)): errors.append(f'chapter inventory must be exactly 01-32, found {nums}')
        for phrase in ['opt-out preference signals','risk-assessment','cybersecurity-audit','ADMT','DROP','Final Human Release Approval']:
            if phrase.casefold() not in text.casefold(): errors.append(f'English master missing topic/boundary: {phrase}')
    for p in GATES:
        if not p.is_file(): errors.append(f'missing release-control file: {p.relative_to(ROOT)}')
    readme=(MAN/'README.md').read_text(encoding='utf-8') if (MAN/'README.md').is_file() else ''
    paths=(MAN/'MANUAL_12_IMPLEMENTATION_PATHS.md').read_text(encoding='utf-8') if (MAN/'MANUAL_12_IMPLEMENTATION_PATHS.md').is_file() else ''
    narrative=readme+'\n'+paths+json.dumps(base)+json.dumps(sources)
    for phrase in ['effective requirement versus phased future compliance date','no automatic applicability determination','human legal and privacy judgment retained']:
        if phrase.casefold() not in narrative.casefold(): errors.append(f'missing legal/timing boundary: {phrase}')
    if paths.count('```mermaid')!=3: errors.append('expected exactly three Mermaid learning graphics')
    if paths.count('**Accessible explanation:**')!=3: errors.append('each graphic requires accessible explanation')

    entries=[x for x in cat.get('manuals',[]) if x.get('id')=='ccpa-cpra-controlled']
    release_stage=os.environ.get('MANUAL12_RELEASE_STAGE','repository').strip().lower()
    if release_stage=='candidate':
        if len(entries)>1:
            errors.append('catalog entry duplicated')
        elif len(entries)==1:
            row=entries[0]
            if row.get('status')!='development' or row.get('layout')!='controlled-build' or row.get('series_order')!=12:
                errors.append('candidate catalog entry invalid')
    else:
        if len(entries)!=1:
            errors.append('catalog entry missing or duplicated')
        elif entries[0].get('status')!='development' or entries[0].get('layout')!='controlled-build' or entries[0].get('series_order')!=12:
            errors.append('catalog entry invalid')

    if not WF.is_file(): errors.append('workflow missing')
    else:
        w=WF.read_text(encoding='utf-8')
        if 'permissions:\n  contents: read' not in w: errors.append('workflow not read-only')
        if re.search(r'(?m)^\s*push:\s*$',w): errors.append('workflow must not push')
        if 'pull_request_target' in w: errors.append('workflow must not use pull_request_target')
        if 'MANUAL12_RELEASE_STAGE: candidate' not in w: errors.append('workflow must declare candidate release stage')
    print('Manual 12 CCPA / CPRA controlled-build QA')
    for e in errors: print('  ERROR:',e)
    if errors: print('FAIL'); return 1
    print('PASS'); return 0

if __name__=='__main__': sys.exit(main())
