# Rolling Prebuild Release-Candidate Rule

## Objective
Prevent front-of-line publication delay by completing release-candidate work for downstream manuals before they become the publication front.

## Required rolling state
At all times, maintain the deepest safe stagger possible:

- Front manual N: publication / release transaction and final reconciliation.
- N+1: QA complete or in final QA with release candidate substantially built.
- N+2: active full build, including controlled English content and localization work.
- N+3: pre-stage/source verification/architecture so it can enter full build immediately.
- N+4 and beyond: source-watch, dependency verification, intake, and architecture preparation.

## Prebuild work that must occur ahead of publication
For N+1 and, where safely possible, N+2, do not wait for front-of-line status to begin:

1. controlled source/content completion;
2. es-419 and pt-BR localization;
3. terminology and cross-language parity preparation;
4. DOCX/PDF publication-candidate generation;
5. rendered accessibility, layout, link, table, heading, and language-metadata QA;
6. SHA-256 checksums, provenance, and release-manifest preparation;
7. exact binary durability/staging preparation;
8. catalog/release-registry reconciliation preparation without false publication claims;
9. authoritative-source re-verification close enough to release to remain current;
10. predecessor-regression, workflow-security, structure, and release-package QA.

## Handoff rule
When a manual advances a stage, immediately promote the next downstream manual one stage in the same work cycle. Do not leave an avoidable idle gap between publication, QA, active build, and pre-stage lanes.

Example:
- If N moves to publication, N+1 must already be in QA/final candidate state.
- If N+1 clears QA, N+2 immediately enters QA and N+3 immediately enters active build.
- N+4 is then pre-staged.

## Fail-closed boundary
Parallelization never permits a downstream manual to publish ahead of its predecessor. No source, technical, integrity, packaging, security, or substantive defect may be bypassed. Required genuine-human review boundaries remain preserved where repository policy requires them; missing duplicate paperwork alone does not create an artificial halt when the repository-wide clean-candidate rule applies.

## Manual 14 corrective application
Manual 14 PCI DSS is the immediate corrective case. Its remaining controlled content completion, localization, publication-candidate generation, rendered QA, checksums/provenance, durable staging, and release-registry preparation must proceed now. Manuals 15 and 16 must perform as much of the same downstream work as safely possible before they become publication-front manuals.
