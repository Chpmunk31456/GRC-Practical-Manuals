# Manual 32 — Exact Staging Handoff

The exact six Manual 32 FFIEC publication binaries from workflow run `33415623228` / artifact `9766895211` were durably staged after fail-closed verification of every provenance-bound SHA-256 identity. No publication binary was regenerated or modified.

The temporary write-enabled staging workflow removed itself in the same bot-authored staging commit. This owner-authored metadata-only handoff exists to place normal repository QA on the exact staged head.

Publication remains unchanged until Manual Structure QA, Trilingual Publication Parity, Release Package QA, and final publication-state reconciliation succeed. Candidate provenance is recorded in `.compliance/MANUAL_32_EXACT_CANDIDATE_PROVENANCE_2026-08-31.md`.
