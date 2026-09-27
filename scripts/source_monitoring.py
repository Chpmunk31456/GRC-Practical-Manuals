#!/usr/bin/env python3
"""Observe authoritative sources without replacing approved baselines."""
from __future__ import annotations
import argparse
from datetime import date, datetime, timezone
import hashlib
import json
import re
import urllib.request
from urllib.parse import urlparse
from pathlib import Path
from compliance_qa import ALLOWED_SOURCE_DOMAINS
from repository_publication_qa import ROOT, read_json, discover

MAX_BYTES = 16 * 1024 * 1024


def validate_url(url):
    value = urlparse(url)
    if value.scheme != 'https' or value.hostname not in ALLOWED_SOURCE_DOMAINS or value.username or value.password or value.port not in (None, 443):
        raise ValueError('source URL outside approved authoritative domains')


class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url):
    validate_url(url)
    request = urllib.request.Request(url, headers={'User-Agent': 'GRC-source-watch/1.0'})
    with urllib.request.build_opener(SafeRedirect()).open(request, timeout=20) as response:
        validate_url(response.url)
        body = response.read(MAX_BYTES + 1)
        if len(body) > MAX_BYTES:
            raise ValueError('source exceeds observation size limit')
        return {'sha256': hashlib.sha256(body).hexdigest(),
                'etag': response.headers.get('ETag'),
                'last_modified': response.headers.get('Last-Modified')}


def assess(source, baseline, observed, affected, today):
    reasons = []
    verified = date.fromisoformat(source['last_verified'])
    if verified > today or (today - verified).days > source['review_interval_days']:
        reasons.append('review_date_due_or_invalid')
    if not affected:
        reasons.append('chapter_mapping_required')
    if baseline is None:
        reasons.append('baseline_human_review_required')
    else:
        if not re.fullmatch('[0-9a-f]{64}', baseline.get('sha256', '')):
            raise ValueError('invalid approved baseline digest')
        if not baseline.get('publication_date') or not baseline.get('revision') or not baseline.get('approval_evidence'):
            reasons.append('baseline_provenance_incomplete')
        else:
            date.fromisoformat(baseline['publication_date'])
        if baseline.get('revision') != source['version']:
            reasons.append('registry_revision_changed')
    if observed is None:
        reasons.append('observation_unavailable')
    elif baseline and observed['sha256'] != baseline['sha256']:
        reasons.append('content_changed')
    identity = json.dumps([source['id'], baseline, observed, reasons], sort_keys=True)
    return {'source_id': source['id'], 'registry_revision': source['version'],
            'publication_date': baseline.get('publication_date') if baseline else None,
            'approved_sha256': baseline.get('sha256') if baseline else None,
            'observed': observed, 'affected_chapters': affected,
            'status': 'REVIEW_REQUIRED' if reasons else 'CURRENT', 'reasons': reasons,
            'review_id': hashlib.sha256(identity.encode()).hexdigest(),
            'human_approval_required': bool(reasons)}


def run(network=False, today=None):
    today = today or date.today()
    sources = read_json(ROOT / '.compliance/authoritative-sources.json')['sources']
    policy = read_json(ROOT / 'config/source_monitoring.json')
    known = {s['id'] for s in sources}
    if len(known) != len(sources) or set(policy['baselines']) - known or set(policy['chapter_mappings']) - known:
        raise ValueError('source identifier mismatch')
    manifests, _ = discover()
    manuals = {m['manual_id']: m for _, m in manifests}
    for mappings in policy['chapter_mappings'].values():
        for mapping in mappings:
            manual = manuals[mapping['manual_id']]
            if not mapping['chapters'] or any(type(n) is not int or n < 1 or n > manual['expected_chapters'] for n in mapping['chapters']):
                raise ValueError('invalid affected chapter mapping')
    results = []
    for source in sources:
        validate_url(source['url'])
        observed = None
        if network:
            try:
                observed = fetch(source['url'])
            except (OSError, ValueError):
                pass  # No response bodies or network error strings enter public logs.
        results.append(assess(source, policy['baselines'].get(source['id']), observed,
                              policy['chapter_mappings'].get(source['id'], []), today))
    return {'schema_version': 1, 'observed_at': datetime.now(timezone.utc).isoformat(),
            'status': 'REVIEW_REQUIRED' if any(r['status'] != 'CURRENT' for r in results) else 'CURRENT',
            'results': results, 'baseline_updates': 0}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--network', action='store_true')
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    result = run(a.network)
    a.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print('Authoritative source monitoring: ' + result['status'])
    print('Review items: ' + str(sum(r['status'] != 'CURRENT' for r in result['results'])))
    return 0  # Observations are review requests, never publication approvals.


if __name__ == '__main__':
    raise SystemExit(main())
