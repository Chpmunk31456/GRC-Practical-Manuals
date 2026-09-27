#!/usr/bin/env python3
"""Verify exact release candidates and independently recorded GitHub approvals."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
from repository_publication_qa import ROOT, contained, read_json, discover
from controlled_publication_qa import sha256

REPOSITORY = 'Chpmunk31456/GRC-Practical-Manuals'
SEMVER = re.compile(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*))?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?')
REQUIRED_CHECKS = {'controlled-publication-quality','document-writing-quality','validate-workflow-security','meta-qa','release-readiness'}


def fingerprint(candidate):
    return hashlib.sha256(json.dumps(candidate,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def verify_builds(candidate, manifest, first, second):
    if first.resolve() == second.resolve():
        raise ValueError('two independent build directories required')
    expected = {manifest['manual_root']+'/'+cfg['artifacts'][kind]
                for cfg in manifest['languages'].values() for kind in ('docx','pdf')}
    if set(candidate['artifacts']) != expected:
        raise ValueError('release must include every locale and artifact')
    receipts=[]
    for root in (first,second):
        receipt=read_json(root/'build-receipt.json')
        if receipt['source_revision'] != candidate['source_revision'] or receipt['toolchain_sha256'] != candidate['toolchain_sha256']:
            raise ValueError('build provenance mismatch')
        if not receipt.get('build_id'):
            raise ValueError('build identity missing')
        receipts.append(receipt)
        for relative,digest in candidate['artifacts'].items():
            if not re.fullmatch('[0-9a-f]{64}',digest) or sha256(contained(root,relative)) != digest:
                raise ValueError('artifact hash mismatch or non-reproducible build')
    if receipts[0]['build_id'] == receipts[1]['build_id']:
        raise ValueError('independent build identities required')


def verify_approvals(candidate, pull, reviews, checks, policy):
    if pull['head']['sha'] != candidate['source_revision']:
        raise ValueError('pull request head differs from candidate')
    if not REQUIRED_CHECKS <= set(policy['required_checks']):
        raise ValueError('mandatory checks removed from policy')
    latest_checks={}
    for check in sorted(checks,key=lambda item:item['id']):
        if check.get('head_sha') == candidate['source_revision'] and check.get('app',{}).get('slug') == 'github-actions':
            latest_checks[check['name']]=check
    if any(latest_checks.get(name,{}).get('conclusion') != 'success' for name in policy['required_checks']):
        raise ValueError('mandatory exact-revision checks are incomplete')
    latest={}
    for review in sorted(reviews,key=lambda item:item['id']):
        latest[review['user']['login']]=review
    marker='Publication approval: SHA256='+fingerprint(candidate)
    eligible={name for name,review in latest.items()
              if name in policy['reviewers'] and name != pull['user']['login']
              and review['user'].get('type') == 'User' and review['state'] == 'APPROVED'
              and review['commit_id'] == candidate['source_revision']
              and marker in (review.get('body') or '')}
    if len(eligible) < max(2,policy['minimum_independent_reviewers']):
        raise ValueError('independent exact-candidate human approvals missing')
    return sorted(eligible)


def gh(endpoint):
    return json.loads(subprocess.check_output(['gh','api',endpoint],text=True,cwd=ROOT))


def pages(endpoint):
    rows=[]
    for page in range(1,101):
        batch=gh(endpoint+('?' if '?' not in endpoint else '&')+f'per_page=100&page={page}')
        rows.extend(batch)
        if len(batch)<100:return rows
    raise ValueError('approval pagination limit exceeded')


def verify(candidate, first, second):
    revision=candidate['source_revision']
    if not re.fullmatch('[0-9a-f]{40}',revision) or not SEMVER.fullmatch(candidate['version']):
        raise ValueError('invalid source revision or semantic version')
    if subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()!=revision:
        raise ValueError('checkout is not the exact source revision')
    if subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],cwd=ROOT,text=True).strip():
        raise ValueError('tracked checkout changes invalidate release')
    manifests,_=discover()
    manifest=next(m for _,m in manifests if m['manual_id']==candidate['manual_id'])
    if manifest['rollout_lane']!='active':
        raise ValueError('candidate manual is not eligible for publication')
    verify_builds(candidate,manifest,first,second)
    for relative,digest in candidate['artifacts'].items():
        if sha256(contained(ROOT,relative))!=digest:
            raise ValueError('reviewed repository artifact differs from built artifact')
    if not candidate['source_provenance'] or not candidate['translation_evidence'] or not candidate['accessibility_evidence'] or not candidate['visual_evidence']:
        raise ValueError('mandatory provenance/review evidence missing')
    for field in ('source_provenance','translation_evidence','accessibility_evidence','visual_evidence'):
        for relative,digest in candidate[field].items():
            if sha256(contained(ROOT,relative))!=digest:
                raise ValueError('reviewed evidence hash mismatch')
    toolchain=read_json(ROOT/'config/production_toolchain.json')
    if toolchain.get('status')!='VERIFIED' or not all(toolchain.get('pdf_toolchain',{}).values()) or not all(toolchain.get('build_environment',{}).values()):
        raise ValueError('production toolchain has not been verified')
    if not re.fullmatch('[0-9a-f]{64}',candidate['toolchain_sha256']) or sha256(ROOT/'config/production_toolchain.json')!=candidate['toolchain_sha256']:
        raise ValueError('pinned toolchain evidence missing or changed')
    import translation_lifecycle
    import source_monitoring
    if translation_lifecycle.run()['status']!='CURRENT' or source_monitoring.run(True)['status']!='CURRENT':
        raise ValueError('source or translation review remains unresolved')
    import accessibility_validation
    if accessibility_validation.run()['status']!='PASS':
        raise ValueError('accessibility defects or independent reviews unresolved')
    import repository_publication_qa
    if repository_publication_qa.run()['status']!='PASS':
        raise ValueError('mandatory publication validation failed')
    # Read approver policy from the default branch, never from the candidate.
    import base64
    policy_file=gh(f'repos/{REPOSITORY}/contents/config/release_policy.json?ref=main')
    policy=json.loads(base64.b64decode(policy_file['content']))
    number=candidate['pull_request']
    if type(number) is not int or number < 1:raise ValueError('invalid pull request')
    pull=gh(f'repos/{REPOSITORY}/pulls/{number}')
    reviews=pages(f'repos/{REPOSITORY}/pulls/{number}/reviews')
    checks=[]
    for page in range(1,101):
        batch=gh(f'repos/{REPOSITORY}/commits/{revision}/check-runs?per_page=100&page={page}')['check_runs']
        checks.extend(batch)
        if len(batch)<100:break
    else:raise ValueError('check pagination limit exceeded')
    reviewers=verify_approvals(candidate,pull,reviews,checks,policy)
    return {'status':'VERIFIED','candidate_sha256':fingerprint(candidate),'source_revision':revision,
            'reviewers':reviewers,'publication_performed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate',type=Path)
    parser.add_argument('--first-build',type=Path,required=True)
    parser.add_argument('--second-build',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    try:result=verify(read_json(args.candidate),args.first_build,args.second_build)
    except (OSError,ValueError,KeyError,TypeError,StopIteration,subprocess.CalledProcessError) as exc:
        result={'status':'BLOCKED','error_type':type(exc).__name__,'publication_performed':False}
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Controlled release: '+result['status'])
    return 0 if result['status']=='VERIFIED' else 1

if __name__=='__main__':raise SystemExit(main())
