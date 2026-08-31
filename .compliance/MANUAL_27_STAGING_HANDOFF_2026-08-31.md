# Manual 27 — Exact Durable Staging Handoff

The exact six publication-candidate binaries from workflow run `33395518151` / artifact `9759165368` were staged without regeneration after fail-closed verification of all six bound SHA-256 identities.

The temporary write-enabled staging workflow removed itself in the same staging commit. This owner-authored handoff commit intentionally changes no publication binary and exists to place ordinary repository QA on an owner-authored exact staging head after the staging transaction.

Candidate provenance is recorded in `.compliance/MANUAL_27_EXACT_CANDIDATE_PROVENANCE_2026-08-31.md`. Publication remains sequential behind published Manual 26; once this exact staging head passes the applicable objective gates, Manual 27 proceeds immediately to catalog/release-registry reconciliation under the canonical clean-candidate authorization rule.