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

## Human-review boundary

Automation may prepare evidence, deterministic QA, review packets and release records, but must never invent reviewer identity, semantic judgment, findings or approval. Existing standing final release authorization applies only when all required technical, source, integrity, packaging and genuine-human evidence gates are satisfied and no unresolved substantive defect remains.

## Human-review early-preflight control — Manual 18 lesson learned

No future manual may reach front-of-line with an undiscovered or unprepared genuine-human review requirement. Human-review requirements must be identified and operationalized before candidate generation, not at final publication reconciliation.

For every Manual N beginning with Manual 19 and continuing through the end of the series:

- during controlled architecture, enumerate every substantive review competency required by the manual's own release controls, including legal/regulatory meaning, localization semantics, editorial usability, accessibility/visual inspection, and any domain-specific specialist review;
- create the review-evidence schema and reviewer packet template before the English source is frozen, including required reviewer identity, review date, PASS/FAIL decision, findings, remediation, re-review, exact source identities, and exact artifact identities;
- before candidate generation, verify that the repository contains no additional release boundary, localization gate, accessibility gate, legal/regulatory gate, or specialist-review requirement that is absent from the planned review packet;
- immediately after the exact six candidate binaries and their SHA-256 identities are frozen, populate the review packet with those exact identities and start all genuinely human substantive review lanes at once rather than waiting for durable staging or catalog reconciliation;
- run deterministic content, structural, parity, link, metadata, checksum, workflow-security, provenance, PDF-preflight and package checks before sending the exact candidate for human review so reviewers are not asked to inspect a technically defective candidate;
- keep candidate hashes stable once substantive review begins. A material source or binary change invalidates only the affected review decisions and must trigger targeted re-review rather than silent carry-forward;
- durable staging may proceed in parallel with human review when safe, but publication reconciliation must not begin until every genuinely required substantive review decision is recorded against the exact current hashes;
- a manual is not considered "review-ready" merely because a review packet exists. It is review-ready only when exact candidate hashes, required competencies, evidence fields, and reviewer-facing artifacts are all complete and stable;
- any late-discovered human-review requirement on Manual N is a pipeline defect. Fix the shared standard immediately and cascade the new preflight requirement to Manual N+1 and all later manuals before they reach the same stage.

The intended steady state is: when a manual becomes front-of-line, its substantive human reviews are already complete or actively tied to a stable exact candidate, so the front publication path cannot be surprised by a newly discovered evidence requirement.

## Anti-halt behavior

A blocker on one manual must not idle the rest of the queue. Continue all safe downstream work, preserve unique branch work, restack when needed, and return repeatedly to the front manual until publication is complete. After publication, the next manual immediately becomes front-of-line and the stagger is re-established.
