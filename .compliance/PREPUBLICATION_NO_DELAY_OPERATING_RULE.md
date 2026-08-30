# Pre-Publication No-Delay Operating Rule

Status: canonical production control for Manuals 14 onward and applicable successor manuals.

## Objective

Eliminate avoidable release delay by advancing every downstream manual as far as safely possible before it becomes front-of-line, while preserving sequential publication, source integrity, security, provenance, accessibility, localization quality, and any genuinely non-waivable substantive review requirement.

## Standing production model

1. The current front manual remains the publication-priority lane. Any true technical, source, packaging, provenance, security, or publication-state defect is corrected as soon as it is identified.
2. The next manual advances to complete pre-publication readiness in parallel.
3. The manual after next advances as far toward the same pre-publication boundary as capacity permits.
4. Additional manuals continue authoritative-source verification, controlled architecture, localization preparation, graphics/accessibility preparation, QA/tooling, provenance preparation, and publication-package preparation in parallel.
5. No downstream manual is published out of sequence.

## Definition of pre-publication ready

A downstream manual should reach the point where, subject only to predecessor publication and any newly discovered true issue, the publication transaction can begin immediately. Where applicable this includes:

- authoritative-source and version/effective-date verification;
- controlled English source complete;
- es-419 and pt-BR controlled localization candidates complete;
- Essential / Structured / Enhanced implementation paths complete;
- accessible graphics, captions, text equivalents, tables, links, metadata, language tags, and reading-order preparation complete;
- automated structure, source-boundary, localization/parity, workflow-security, package, PDF-content, and release-pipeline QA prepared and passing on the exact candidate;
- deterministic DOCX/PDF generation complete;
- durable-artifact path confirmed before front-of-line publication;
- SHA-256 checksums and provenance generated;
- release manifest prepared;
- catalog and work-product release-registry entries pre-staged but not falsely marked published;
- exact-head publication checklist complete except predecessor/publication transaction fields;
- no known substantive defect left unresolved.

## Lessons incorporated from Manual 13

Manual 13 demonstrated that a candidate can be content-complete and QA-green yet still incur release delay if binary durability is addressed only at the final publication transaction. Therefore, for every future manual:

1. Binary durability is a pre-publication requirement, not a post-QA afterthought. The repository-authorized mechanism for committing or durably publishing DOCX/PDF artifacts must be proven before the manual reaches the front of the queue.
2. Final candidate binary artifacts should be generated early enough to verify byte integrity, checksums, page/content QA, and repository/publication transport before predecessor clearance.
3. Catalog and release-registry records must be prepared in advance with publication-state fields left unasserted until the actual release occurs.
4. Publication workflows must not depend on insecure self-pushing GitHub Actions or weakened workflow-security controls.
5. If a tooling constraint affects one manual, isolate that constraint and continue all safe downstream work rather than idling the pipeline.
6. Stale branch ancestry must be restacked promptly onto current main to avoid last-minute mergeability delay.
7. Superseded PRs and stale control wording should be reconciled promptly so later automation reads one current state.

## Forward-motion decision rule

Automation defaults to forward motion. Stop only the affected step for a true issue: substantive defect, failed QA, source/legal conflict, invalid provenance/package, security failure, binary durability failure, or other non-waivable material constraint. Paperwork friction, redundant approval requests, stale branch ancestry that can be repaired, or other automatable process issues are corrected rather than treated as reasons to idle the project.

## Publication boundary

When a manual becomes front-of-line and all applicable pre-publication conditions are green, predecessor order is satisfied, and no true issue remains, proceed automatically through publication, durable artifact verification, checksum/provenance reconciliation, catalog/release-registry promotion, exact-head validation, and post-release verification under the standing owner authorization.

This control does not fabricate human review, weaken security, or authorize out-of-order publication.
