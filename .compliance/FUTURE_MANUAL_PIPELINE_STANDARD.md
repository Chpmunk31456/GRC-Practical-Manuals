# Future Manual Pipeline Standard

**Scope:** all remaining and future manuals in the controlled publication series.

## Operating model

The publication queue must operate as a rolling staggered pipeline. The front manual is always driven toward publication, and every downstream manual must remain exactly one substantive stage behind its immediate predecessor unless a documented fail-closed blocker requires otherwise.

After each downstream advancement, execution returns to the front manual and pushes or repairs its next eligible gate. No manual may remain merely branch-aligned when safe substantive work can advance it.

## Canonical stages

1. authoritative-source verification and source-state record;
2. controlled architecture / chapter and evidence model;
3. controlled English master construction;
4. exact English freeze plus es-419 and pt-BR controlled localization;
5. DOCX/PDF candidate generation for all three locales;
6. rendered, accessibility, visual, content, structural and parity QA;
7. SHA-256 candidate identity, provenance and release evidence;
8. durable publication artifact staging on `main` with README and correct publication-relative checksum paths;
9. exact-head release/security/package QA;
10. catalog and work-product release-registry reconciliation; publication complete only after reconciliation lands on `main`.

## Canonical release authorization equation

**NO ERRORS + NO ISSUES + ALL APPLICABLE OBJECTIVE GATES GREEN + PREDECESSOR PUBLISHED = HUMAN APPROVAL SATISFIED UNDER STANDING AUTHORIZATION = PUBLISH NOW.**

This equation is the controlling release rule for Manual 18 and every current or future manual. When it is satisfied, do not stop at `ready`, `review-ready`, `candidate`, `awaiting approval`, `owner confirmation`, or equivalent states. Publish immediately, reconcile publication state on `main`, and continue to the next manual.

A separate generic human-approval, final-signoff, owner-confirmation, or release-approval prompt must not be created or reintroduced after the equation is satisfied.

## One-stage-behind rule

If Manual N advances from stage X to stage X+1, Manual N+1 must be advanced to stage X as soon as safely executable. Manual N+2 must be at stage X-1, and the stagger continues down the defined series. Work may run in parallel, but publication order remains strictly sequential.

## Front-line automatic advancement

When the current front manual has objective evidence that its applicable gate is green, merge or advance immediately under standing clean-candidate release authorization without waiting for another routine user prompt. A genuine unresolved substantive defect remains fail-closed.

## Artifact-first rule

Before publication-state promotion, each manual must have durable actual EN/es-419/pt-BR DOCX/PDF artifacts, required README, exact checksums using correct publication-relative paths, provenance, and required QA evidence on `main`. Catalog or release-registry promotion must never substitute for missing durable binaries.

## Release-efficiency lessons learned

Every future manual must inherit the following preflight controls before its release workflow is opened:

- pin every third-party GitHub Action to a full immutable commit SHA; mutable tags such as `@v4` are prohibited;
- include every repository script invoked by a workflow in that workflow's `pull_request.paths` dependency set so meta-QA cannot discover missing trigger coverage late in the release cycle;
- establish the candidate-build workflow and dependency map before the manual reaches the front line;
- generate the exact EN/es-419/pt-BR DOCX/PDF six-pack reproducibly from frozen controlled sources, not from ad hoc local files;
- upload or stage the exact candidate bytes, then bind SHA-256 identities and provenance to those bytes before any release-state promotion;
- run workflow-security, trigger-dependency meta-QA, PDF preflight, structural/parity QA and release-package QA on the exact candidate head before durable staging;
- treat any workflow-hygiene defect found on Manual N as a preventive control to be applied immediately to Manual N+1 and all later manuals, rather than rediscovering it when they become front-of-line.

These controls are preparation requirements, not optional cleanup. Downstream manuals should have them satisfied while they are still behind the front manual so publication latency is reduced without weakening any fail-closed gate.

## Approval and substantive-review boundary

There is no separate routine or generic human-approval gate for a clean publication candidate. Standing release authorization applies automatically when all objective technical, source, integrity, localization, accessibility, packaging, provenance, workflow-security, predecessor-order and release-state checks applicable to that manual are green and no unresolved material defect or error is recorded.

A manual must not be held merely for an additional approval prompt, owner confirmation, or reviewer sign-off when the repository contains no distinct substantive-review requirement for that manual.

This rule does not authorize fabrication of human judgment. If a manual's own documented control, authoritative-source boundary, legal/regulatory interpretation, localization-semantic boundary, accessibility/visual inspection requirement, licensing condition, or other specialist control explicitly requires genuine human judgment that cannot be established deterministically, that substantive review remains fail-closed until evidence exists. Such substantive review is not a generic release approval and must be scoped only to the competency actually required.

## Early review-preflight control

For every Manual N beginning with Manual 19 and continuing through the end of the series, identify before candidate generation whether any genuinely non-deterministic substantive review is actually required. Do not create a human-review blocker by default.

- If no distinct substantive-review competency is required after source, legal/regulatory, localization, editorial, accessibility, licensing and specialist-control analysis, record `no separate substantive human review required` and proceed under standing clean-candidate release authorization once objective QA is green.
- If a genuine human-judgment competency is required, define only that competency, the exact evidence needed, and the exact source/artifact identities to which it applies.
- Do not require generic final human approval in addition to the standing release authorization.
- Run deterministic content, structural, parity, link, metadata, checksum, workflow-security, provenance, PDF-preflight and package checks before any necessary substantive review so human reviewers are never asked to inspect a technically defective candidate.
- Keep candidate hashes stable once any necessary substantive review begins. A material source or binary change invalidates only the affected review decision and triggers targeted re-review.
- Any late-discovered unnecessary approval or review requirement is a pipeline defect. Remove it from the shared standard/tooling and cascade the correction to all later manuals.

The intended steady state is: a clean, error-free manual with all applicable objective gates green publishes automatically; human involvement is required only where a specific, documented, non-deterministic substantive judgment is genuinely necessary.

## Anti-halt behavior

A blocker on one manual must not idle the rest of the queue. Continue all safe downstream work, preserve unique branch work, restack when needed, and return repeatedly to the front manual until publication is complete. After publication, the next manual immediately becomes front-of-line and the stagger is re-established.
