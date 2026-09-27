# Phase 9 operational handoff

## Improvement 56 — controlled-release drill and artifact fingerprints

The Phase 9 drill consumes the already verified runtime/PDF toolchain, the
one-candidate-at-a-time release queue, exact reviewer-readiness packets, and the
isolated recovery result.

Run after the recovery exercise:

`python scripts/phase9_release_drill.py --recovery /tmp/production-recovery.json --output /tmp/phase9-release-drill.json`

The drill records a stable SHA-256 fingerprint over the six controlled
publication artifacts for each candidate: DOCX and PDF for English, Spanish, and
Brazilian Portuguese.

A successful technical drill reports:

`TECHNICAL_READY_HUMAN_APPROVALS_REQUIRED`

That status means the technical production path is ready while the candidate
remains blocked by real human evidence requirements. It does not authorize
publication.

## Operational cadence

The repository records the following maintenance schedule:

- source and toolchain drift review — weekly;
- isolated recovery exercise — monthly;
- controlled-release dry run — before each candidate release;
- human-evidence freshness validation — before each candidate release;
- exact artifact-hash reconciliation — before each candidate release.

Bulk release remains prohibited. Rollout changes and publication remain outside
the drill.
