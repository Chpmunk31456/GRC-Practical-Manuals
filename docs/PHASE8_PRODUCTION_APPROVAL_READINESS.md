# Phase 8 — Production approval and release readiness

Phase 8 prepares the repository for real production approval without manufacturing
human decisions.

## Improvement 49 — hosted CI toolchain attestation

The repository records the exact successful hosted-CI toolchain observed during
the Phase 7 closure run:

- Python 3.12.14
- GitHub-hosted Ubuntu 24.04 runner image 20260920.314.1
- poppler-utils 24.02.0-1ubuntu9.9
- pdftotext 24.02.0
- pdfinfo 24.02.0

Run:

`python scripts/toolchain_attestation.py --output toolchain-attestation.json`

The verifier fails on drift from that baseline. This is an attested CI baseline,
not an immutable production environment. The repository therefore retains
`REVIEW_REQUIRED` for production-toolchain status until an immutable build
environment or equivalent production verification is supplied.

No toolchain attestation authorizes publication.
