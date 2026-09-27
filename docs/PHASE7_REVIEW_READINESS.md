# Phase 7 review readiness

## Improvement 46 — deterministic reviewer-readiness packets

Phase 7 operationalizes the remaining human-review boundaries without converting
automation into approval.

Run:

`python scripts/review_readiness_packets.py --queue review-queue.json --packet-dir review-packets`

The generator produces one deterministic packet for every candidate manual. Each
packet is bound to the exact repository revision and includes only controlled
metadata: manifest path/hash, source file paths and SHA-256 values, publication
artifact paths and SHA-256 values, review-record paths/hashes, readiness status,
and repository-wide blocker categories.

Packets do not contain document prose and do not authorize publication. Candidate
review records remain `REVIEW_REQUIRED` until separately completed human review
evidence is recorded and verified by the Phase 5 controls.

The repository-level queue currently reports fail-closed blockers when approved
source baselines are absent, hash-bound translation reviews are missing,
independent accessibility reviews are absent, the production toolchain is not
verified, or the authorized release-reviewer allowlist is insufficient.

The queue is retained as CI evidence. It is a work-organizing artifact only; the
controlled-release verifier remains authoritative for exact-candidate release
verification.
