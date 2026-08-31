# Manual 23 — Exact Durable Staging Handoff

The exact six publication-candidate binaries from workflow run `33382887620` / artifact `9754443202` were staged without regeneration after fail-closed verification of all six bound SHA-256 identities.

The temporary write-enabled staging workflow removed itself in the same staging commit. This owner-authored handoff commit intentionally changes no publication binary and exists to place ordinary repository QA on an owner-authored exact staging head after GitHub classified bot-triggered follow-on checks as `action_required` without jobs.

Candidate provenance is recorded in `.compliance/MANUAL_23_EXACT_CANDIDATE_PROVENANCE_2026-08-31.md`. Publication remains sequential; once this exact staging head passes the applicable objective gates, Manual 23 proceeds immediately to catalog/release-registry reconciliation under the canonical clean-candidate authorization rule.

Final publication reconciliation has now updated the catalog and work-product release registry on this branch and self-removed its temporary workflow. This owner-authored metadata-only touch intentionally preserves every staged publication binary byte while re-triggering ordinary exact-head QA on the final reconciled candidate.
