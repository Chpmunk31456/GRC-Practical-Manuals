#!/usr/bin/env python3
"""Track translation dependencies; never infer approval from generated text."""
from __future__ import annotations
import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
from repository_publication_qa import ROOT, discover, contained, read_json
from controlled_publication_qa import collect, sha256


def inventory(root, patterns):
    paths = collect(root, patterns)
    if not paths:
        raise ValueError('controlled source inventory is empty')
    return {p.relative_to(root).as_posix(): sha256(p) for p in paths}


def assess(source, target, previous, review, terminology_digest, missing_terms, evidence_root=ROOT):
    reasons = []
    if previous is None:
        reasons.append('dependency_baseline_required')
    else:
        if previous.get('source') != source:
            reasons.append('english_source_changed')
        if previous.get('translation') != target:
            reasons.append('translation_changed')
    if missing_terms:
        reasons.append('controlled_terminology_missing')
    if not review:
        reasons.append('human_review_required')
    else:
        try:
            evidence = contained(evidence_root, review['evidence_path'])
            valid = (review['decision'] == 'APPROVED' and bool(review['reviewer'].strip())
                     and date.fromisoformat(review['date']) <= date.today()
                     and review['source'] == source and review['translation'] == target
                     and review['terminology_sha256'] == terminology_digest
                     and evidence.is_file() and sha256(evidence) == review['evidence_sha256'])
        except (KeyError, ValueError, OSError, TypeError):
            valid = False
        if not valid:
            reasons.append('review_evidence_missing_or_stale')
    return {'status': 'REVIEW_REQUIRED' if reasons else 'REVIEW_EVIDENCE_CURRENT',
            'reasons': reasons, 'missing_terms': missing_terms,
            'changed_source_files': sorted(set(source) ^ set((previous or {}).get('source', {})) |
                {p for p, h in source.items() if (previous or {}).get('source', {}).get(p) != h}),
            'source': source, 'translation': target, 'terminology_sha256': terminology_digest}


def run():
    records = read_json(ROOT / 'config/translation_lifecycle.json')
    policy_hash = sha256(ROOT / 'config/writing_semantic_policy.json')
    manifests, _ = discover()
    results = []
    for _, manifest in manifests:
        root = contained(ROOT, manifest['manual_root'])
        source = inventory(root, manifest['languages']['en']['source_globs'])
        for locale in ('es-419', 'pt-BR'):
            cfg = manifest['languages'][locale]
            target = inventory(root, cfg['source_globs'])
            text = '\n'.join((root / p).read_text(encoding='utf-8') for p in target)
            missing = [term for term in cfg['required_terms'] if term.casefold() not in text.casefold()]
            digest = hashlib.sha256(json.dumps([policy_hash,cfg['required_terms']],sort_keys=True).encode()).hexdigest()
            key = manifest['manual_id'] + ':' + locale
            result = assess(source, target, records['dependencies'].get(key), records['reviews'].get(key), digest, missing)
            result.update(manual_id=manifest['manual_id'],locale=locale,
                          affected_chapters=list(range(1,manifest['expected_chapters']+1)))
            results.append(result)
    expected = {r['manual_id']+':'+r['locale'] for r in results}
    if (set(records['dependencies']) | set(records['reviews'])) - expected:
        raise ValueError('unregistered translation lifecycle record')
    return {'schema_version':1,'status':'REVIEW_REQUIRED' if any(r['status']!='REVIEW_EVIDENCE_CURRENT' for r in results) else 'CURRENT',
            'results':results,'human_publication_approval':'NOT_EVALUATED'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=run()
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Translation lifecycle: '+result['status'])
    return 0

if __name__=='__main__':raise SystemExit(main())
