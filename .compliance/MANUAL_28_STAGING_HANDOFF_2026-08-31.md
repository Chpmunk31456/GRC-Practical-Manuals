# Manual 28 — Exact Durable Staging Handoff

The exact six publication-candidate binaries from workflow run `33398466434` / artifact `9760280725` were staged without regeneration after fail-closed verification of all six bound SHA-256 identities.

The temporary write-enabled staging workflow removed itself in the same staging commit. This owner-authored handoff commit intentionally changes no publication binary and exists to place ordinary repository QA on an owner-authored exact staging head after the staging transaction.

Candidate provenance is recorded in `.compliance/MANUAL_28_EXACT_CANDIDATE_PROVENANCE_2026-08-31.md`. Predecessor Manual 27 is published; once this exact staging head passes the applicable structure, trilingual-parity, and release-package gates, Manual 28 proceeds immediately to catalog/release-registry reconciliation under the canonical clean-candidate authorization rule.