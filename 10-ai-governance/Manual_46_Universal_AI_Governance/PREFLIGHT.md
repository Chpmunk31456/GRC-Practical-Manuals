# Manual 46 — Preflight

**State:** ACTIVE / FAIL-CLOSED  
**Started:** 31 August 2026

## Repository and workflow controls

- [x] Clean build branch created from current `main`.
- [x] Draft PR opened; no direct write to protected `main`.
- [x] No new write-enabled GitHub Actions workflow introduced by this manual.
- [x] Existing repository QA reviewed; workflow-security policy requires top-level `contents: read`, pinned actions, no `git push`, no `contents: write` in QA workflows.
- [ ] Execute/observe repository QA on a release-capable candidate before promotion.
- [ ] Add Manual 46 to the authoritative manual catalog when the branch reaches controlled-build readiness.

## Source controls

- [x] Primary/official source register established.
- [x] Legal, standards and voluntary-framework status separated conceptually.
- [x] ISO copyright control stated; protected standard text is not reproduced.
- [ ] Refresh every time-sensitive source before release.
- [ ] Expand the central authoritative-domain allowlist only through reviewed repository-security change if later manuals require IMDA/OECD/OWASP/MITRE/UNESCO domains.

## Substantive controls

- [x] Universal scope established; not employer/interview specific.
- [x] Universal governance spine established.
- [x] Inventory, classification, risk, lifecycle, data, security, privacy, human oversight, GenAI, agentic AI, third party, monitoring, incidents and evidence included.
- [x] Examples, exercises and implementation templates added.
- [ ] Controlled-English full editorial review.
- [ ] Cross-framework consistency review.
- [ ] Security/privacy/model-risk technical challenge.

## Early substantive-review determination

Canonical release rule applies:

**NO ERRORS + NO ISSUES + ALL APPLICABLE OBJECTIVE GATES GREEN + PREDECESSOR PUBLISHED = HUMAN APPROVAL SATISFIED UNDER STANDING AUTHORIZATION = PUBLISH NOW.**

- [x] No separate generic final human approval gate is permitted.
- [x] Predecessor Manual 45 is published.
- [ ] Determine after deterministic source/editorial/technical/localization/accessibility checks whether any specific non-deterministic specialist judgment remains.
- [ ] If none remains, record `no separate substantive human review required` and continue automatically under standing authorization.
- [ ] If a genuine specialist judgment remains, scope it narrowly to the exact issue and exact candidate identity; do not create a generic sign-off gate.

## Artifact readiness

- [ ] Final controlled Markdown source frozen.
- [ ] es-419 controlled localization and semantic QA.
- [ ] pt-BR controlled localization and semantic QA.
- [ ] EN/es-419/pt-BR DOCX candidates generated.
- [ ] EN/es-419/pt-BR PDF candidates generated.
- [ ] Visible text/page validation completed for every PDF.
- [ ] Accessibility/rendered review completed.
- [ ] Checksums/provenance/release manifest complete.
- [ ] Exact-head release/security/package QA green.
- [ ] Catalog and work-product release-registry reconciliation complete on `main`.

## Preflight disposition

**Continue driving Manual 46 toward publication. Publish immediately when the canonical release equation is satisfied; do not stop for a separate routine approval prompt.**
