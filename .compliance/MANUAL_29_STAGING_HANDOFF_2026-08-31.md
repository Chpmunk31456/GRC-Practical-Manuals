# Manual 29 — Exact Durable Staging Handoff

The exact six publication-candidate binaries from workflow run `33403413629` / artifact `9762169998` were staged without regeneration after fail-closed verification of all six bound SHA-256 identities.

The temporary write-enabled staging workflow removed itself in the same staging commit. This owner-authored handoff changes no publication binary and exists to place ordinary repository QA on a clean owner-authored exact staging head.

Candidate provenance is recorded in `.compliance/MANUAL_29_EXACT_CANDIDATE_PROVENANCE_2026-08-31.md`. Publication remains sequential behind published Manual 28; once this exact staging head passes the applicable objective gates, Manual 29 proceeds immediately to catalog/release-registry reconciliation under the canonical clean-candidate authorization rule.