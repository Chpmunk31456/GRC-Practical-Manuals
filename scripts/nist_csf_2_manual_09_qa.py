#!/usr/bin/env python3
"""Fail-closed controlled-build QA for Manual 09 — NIST CSF 2.0."""

import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.compliance' / 'nist-csf-2-manual-09-baseline.json'
REG = ROOT / '.compliance' / 'authoritative-sources.json'
CAT = ROOT / '.compliance' / 'manual-catalog.json'
MAN = ROOT / '01-foundations' / 'NIST_CSF_2_Controlled_Implementation'
WF = ROOT / '.github' / 'workflows' / '21-nist-csf-2-manual-09-qa.yml'

LANGUAGE_FILES = {
    'en': [
        MAN/'English/source/01_GOVERN_CHAPTERS_01_08.md',
        MAN/'English/source/02_IDENTIFY_PROTECT_CHAPTERS_09_16.md',
        MAN/'English/source/03_DETECT_RESPOND_CHAPTERS_17_24.md',
        MAN/'English/source/04_RECOVER_PROFILES_ASSURANCE_CHAPTERS_25_32.md',
    ],
    'es-419': [
        MAN/'Spanish_es-419/source/01_GOBERNAR_CAPITULOS_01_08.md',
        MAN/'Spanish_es-419/source/02_IDENTIFICAR_PROTEGER_CAPITULOS_09_16.md',
        MAN/'Spanish_es-419/source/03_DETECTAR_RESPONDER_CAPITULOS_17_24.md',
        MAN/'Spanish_es-419/source/04_RECUPERAR_PERFILES_ASEGURAMIENTO_CAPITULOS_25_32.md',
    ],
    'pt-BR': [
        MAN/'Portuguese_pt-BR/source/01_GOVERNAR_CAPITULOS_01_08.md',
        MAN/'Portuguese_pt-BR/source/02_IDENTIFICAR_PROTEGER_CAPITULOS_09_16.md',
        MAN/'Portuguese_pt-BR/source/03_DETECTAR_RESPONDER_CAPITULOS_17_24.md',
        MAN/'Portuguese_pt-BR/source/04_RECUPERAR_PERFIS_ASSEGURACAO_CAPITULOS_25_32.md',
    ],
}


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def roots(text):
    words = re.findall(r'[a-z0-9]+', text.casefold())
    return {w[:-1] if len(w) > 4 and w.endswith('s') else w for w in words}


def concept_present(concept, document_roots):
    needed = roots(str(concept))
    return bool(needed) and needed.issubset(document_roots)


def chapter_numbers(text):
    return [int(x) for x in re.findall(r'(?mi)^##\s+(?:Chapter|Capítulo)\s+(\d+)\s+—', text)]


def main():
    errors = []
    try:
        base, reg, cat = load(BASE), load(REG), load(CAT)
    except Exception as exc:
        print(f'FAIL: {exc}')
        return 1

    if base.get('manual_id') != 'nist-csf-2-manual-09':
        errors.append('unexpected manual id')
    if base.get('planned_publication_languages') != ['en', 'es-419', 'pt-BR']:
        errors.append('language plan changed')

    source_ids = {x.get('id') for x in reg.get('sources', []) if isinstance(x, dict)}
    for sid in base.get('required_source_ids', []):
        if sid not in source_ids:
            errors.append(f'missing authoritative source id: {sid}')

    readme = (MAN / 'README.md').read_text(encoding='utf-8') if (MAN / 'README.md').is_file() else ''
    paths = (MAN / 'MANUAL_09_IMPLEMENTATION_PATHS.md').read_text(encoding='utf-8') if (MAN / 'MANUAL_09_IMPLEMENTATION_PATHS.md').is_file() else ''
    combined_roots = roots(readme + '\n' + paths)

    for function in ['GOVERN', 'IDENTIFY', 'PROTECT', 'DETECT', 'RESPOND', 'RECOVER']:
        if function.casefold() not in (readme + '\n' + paths).casefold():
            errors.append(f'missing CSF function: {function}')
    for boundary in base.get('required_boundaries', []):
        if not concept_present(boundary, combined_roots):
            errors.append(f'missing boundary: {boundary}')

    for lang, files in LANGUAGE_FILES.items():
        missing = [str(p.relative_to(ROOT)) for p in files if not p.is_file()]
        if missing:
            errors.extend(f'missing {lang} source: {p}' for p in missing)
            continue
        text = '\n'.join(p.read_text(encoding='utf-8') for p in files)
        chapters = chapter_numbers(text)
        if chapters != list(range(1, 33)):
            errors.append(f'{lang} chapter inventory must be exactly 01-32, found {chapters}')
        if lang == 'es-419' and 'revisión semántica humana' not in text.casefold():
            errors.append('es-419 localization must retain explicit human semantic review boundary')
        if lang == 'pt-BR' and 'revisão semântica humana' not in text.casefold():
            errors.append('pt-BR localization must retain explicit human semantic review boundary')

    matches = [x for x in cat.get('manuals', []) if x.get('id') == 'nist-csf-2-controlled']
    if len(matches) != 1 or matches[0].get('status') != 'development' or matches[0].get('series_order') != 9:
        errors.append('catalog entry invalid')

    for gate in [
        MAN/'qa/SOURCE_VERIFICATION_2026-08-27.md',
        MAN/'qa/LOCALIZATION_SEMANTIC_REVIEW_GATE.md',
        MAN/'qa/DOCUMENT_ACCESSIBILITY_PUBLICATION_QA_GATE.md',
    ]:
        if not gate.is_file():
            errors.append(f'missing release-control evidence file: {gate.relative_to(ROOT)}')

    if not WF.is_file():
        errors.append('workflow missing')
    else:
        workflow = WF.read_text(encoding='utf-8')
        if 'permissions:\n  contents: read' not in workflow:
            errors.append('workflow not read-only')
        if re.search(r'(?m)^\s*push:\s*$', workflow):
            errors.append('workflow must not push')

    print('Manual 09 NIST CSF 2.0 controlled-build QA')
    for error in errors:
        print('  ERROR:', error)
    if errors:
        print('FAIL')
        return 1
    print('PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
