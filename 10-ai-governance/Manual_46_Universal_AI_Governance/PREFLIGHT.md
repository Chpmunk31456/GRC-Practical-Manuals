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
- [ ] Controlled-English full editorial review.
- [ ] Cross-framework consistency review.
- [ ] Security/privacy/model-risk technical challenge.
- [ ] Examples, exercises and implementation templates added.

## Artifact readiness

- [ ] Final controlled Markdown source frozen.
- [ ] es-419 terminology review/localization.
- [ ] pt-BR terminology review/localization.
- [ ] DOCX candidate generated.
- [ ] PDF candidate generated.
- [ ] Visible text/page validation completed for every PDF.
- [ ] Accessibility review.
- [ ] Checksums/provenance/release manifest.
- [ ] Required accountable-human final release approval.

## Preflight disposition

**Proceed with controlled drafting and parallel downstream pre-stage. Do not promote to publication candidate yet.**
