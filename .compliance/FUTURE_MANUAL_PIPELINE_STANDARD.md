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

## Human-review boundary

Automation may prepare evidence, deterministic QA, review packets and release records, but must never invent reviewer identity, semantic judgment, findings or approval. Existing standing final release authorization applies only when all required technical, source, integrity, packaging and genuine-human evidence gates are satisfied and no unresolved substantive defect remains.

## Anti-halt behavior

A blocker on one manual must not idle the rest of the queue. Continue all safe downstream work, preserve unique branch work, restack when needed, and return repeatedly to the front manual until publication is complete. After publication, the next manual immediately becomes front-of-line and the stagger is re-established.