#!/usr/bin/env python3
"""Build a fail-closed quality summary from revision-bound evidence."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import subprocess
from repository_publication_qa import ROOT, read_json

CATEGORIES = ('sources','translations','writing','regression','docx','pdf','accessibility','visual_review','release_approval')
GOOD = {'PASS','CURRENT','APPROVED'}


def summarize(evidence, revision, now=None):
    now = now or datetime.now(timezone.utc)
    records = evidence.get('categories', {})
    statuses, blockers = {}, []
    for category in CATEGORIES:
        record = records.get(category)
        status = 'MISSING'
        if isinstance(record, dict):
            status = record.get('status', 'MISSING')
            if record.get('source_revision') != revision:
                status = 'STALE_REVISION'
            else:
                try:
                    observed = datetime.fromisoformat(record['observed_at'])
                    if observed.tzinfo is None or observed > now or now - observed > timedelta(hours=24):
                        status = 'STALE_OBSERVATION'
                except (KeyError, TypeError, ValueError):
                    status = 'INVALID_OBSERVATION'
            if record.get('unresolved_defects'):
                status = 'UNRESOLVED_DEFECTS'
            if record.get('status') not in GOOD and status in GOOD:
                status = 'INVALID_STATUS'
        statuses[category] = status
        if status not in GOOD:
            blockers.append(category)
    return {'schema_version':1,'source_revision':revision,'generated_at':now.isoformat(),
            'status':'READY_FOR_INDEPENDENT_RELEASE_CHECK' if not blockers else 'BLOCKED',
            'categories':statuses,'blocking_categories':blockers,
            'approval_history':evidence.get('approval_history',[]),
            'publication_authorized':False,
            'boundary':'Dashboard evidence does not authorize publication or establish full accessibility.'}


def render(report):
    lines=['# Publication quality summary','', 'Revision: '+report['source_revision'], '',
           'Readiness: '+report['status'], '', '| Control | Status |','| --- | --- |']
    lines += ['| '+key+' | '+value+' |' for key,value in report['categories'].items()]
    lines += ['', 'Blocking categories: '+(', '.join(report['blocking_categories']) or 'None'),'',report['boundary'],'']
    return '\n'.join(lines)


def collect():
    import repository_publication_qa
    import source_monitoring
    import translation_lifecycle
    revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    now=datetime.now(timezone.utc).isoformat()
    publication=repository_publication_qa.run()
    categories={}
    def put(name,status):
        categories[name]={'status':status,'source_revision':revision,'observed_at':now,'unresolved_defects':[]}
    put('sources',source_monitoring.run(False)['status'])
    put('translations',translation_lifecycle.run()['status'])
    put('docx',publication['status'])
    put('pdf',publication['status'])
    put('accessibility','INDEPENDENT_REVIEW_REQUIRED')
    return {'categories':categories,'approval_history':[]},revision


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence',type=Path)
    parser.add_argument('--revision')
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--summary',type=Path,required=True)
    args=parser.parse_args()
    if args.evidence:
        if not args.revision:parser.error('--revision is required with supplied evidence')
        evidence,revision=read_json(args.evidence),args.revision
    else:
        evidence,revision=collect()
    report=summarize(evidence,revision)
    args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    args.summary.write_text(render(report),encoding='utf-8')
    print('Publication quality: '+report['status'])
    return 0  # This is reporting; the release gate is authoritative.

if __name__=='__main__':raise SystemExit(main())
