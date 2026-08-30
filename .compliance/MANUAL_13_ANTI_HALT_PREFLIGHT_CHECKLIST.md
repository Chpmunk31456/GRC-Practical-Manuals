# Manual 13 — SOX ITGC / ICFR Anti-Halt Preflight Checklist

Status: PREPUBLICATION / FAIL-CLOSED

This checklist converts the Manual 13 preflight baseline into an executable release-preparation sequence. It does not authorize publication and does not substitute automation for required human judgment.

## Candidate identity

Before human review begins, record and freeze:
- exact candidate commit SHA;
- SHA-256 for each controlled English, es-419, and pt-BR source artifact;
- SHA-256 for each rendered DOCX/PDF publication artifact;
- source-registry and baseline-record hashes;
- generator/tooling version or commit used for rendering.

Any material content or rendering change after review begins reopens only the affected review gates and requires updated hashes.

## Authoritative-source gate

Verify at candidate time against official sources:
- Sarbanes-Oxley Act statutory text relevant to Sections 302 and 404;
- SEC Section 404 implementation and management ICFR guidance;
- PCAOB AS 2201 text currently effective on the candidate date;
- separately identify amendments approved but not yet effective;
- do not present COSO, COBIT, NIST, ISO, CIS, or other frameworks as statutory requirements unless an authoritative source makes that relationship explicit.

Record source URL, title, publisher, effective/version date, verification date, reviewer, and disposition.

## Scope and control-model gate

Fail closed unless the manual clearly distinguishes:
- ICFR-relevant IT general controls from generic cybersecurity controls;
- management's ICFR assessment from external-auditor attestation;
- entity-level controls, automated/application controls, interfaces, reports/IPE, and ITGC dependencies;
- design effectiveness from operating effectiveness;
- deficiencies, significant deficiencies, and material weaknesses without inventing legal conclusions;
- evidence examples from mandatory evidence requirements.

## Human substantive reviews

Each review must identify reviewer, date, exact candidate/artifact hashes, decision, evidence examined, findings, remediation, and re-review disposition where applicable.

Required reviews:
1. SOX / ICFR legal-audit-editorial review.
2. ITGC and control-mapping technical review.
3. es-419 semantic and terminology review against controlled English.
4. pt-BR semantic and terminology review against controlled English.
5. rendered accessibility and visual/page-level review.
6. changed-scope review after the final material change.

Standing Final Human Release Approval is a separate already-authorized release control and is not a substitute for these substantive reviews.

## Localization gate

For es-419 and pt-BR:
- preserve legal/audit meaning and defined terminology;
- retain source citations and control identifiers;
- prohibit claims of official/authorized translation unless demonstrably true;
- reconcile headings, tables, figures, captions, footers, cross-references, links, and evidence examples;
- document intentional locale-specific adaptations.

## Rendered accessibility / visual gate

Human page-level review must cover at minimum:
- heading hierarchy and reading order;
- table structure and repeated headers;
- figure/caption placement and alternative text;
- contrast and non-color-only meaning;
- link text and destination behavior;
- page breaks, clipping, overflow, orphaned headings, and blank pages;
- locale/language metadata and visible locale consistency;
- headers, footers, page numbering, and document title/version consistency.

## Automated exact-head preflight

At the final candidate head require green evidence for:
- manual structure/schema validation;
- authoritative-source registry validation;
- controlled-language and prohibited-claim checks;
- link/reference checks;
- trilingual structural/parity checks;
- generated-document/package integrity checks;
- checksum/manifest validation;
- workflow security and dependency/pinning checks;
- release-pipeline/meta QA;
- predecessor/publication-order validation.

Automation may detect defects but cannot satisfy the human substantive-review gates above.

## Durable release evidence

Before publication require committed or durably linked evidence for:
- exact-head candidate identity;
- human review decisions and reviewed hashes;
- automated QA results;
- authoritative-source verification date and source versions;
- final artifact checksums;
- release manifest and provenance;
- publication package inventory;
- catalog/release-registry mutation prepared for the same release transaction.

## Publication transaction

Publish only after Manual 12 is published and all Manual 13 gates are green. In the release transaction:
1. re-read live main and predecessor state;
2. verify exact candidate head has not moved;
3. verify all required human evidence binds to that candidate/artifacts;
4. verify required checks are green;
5. merge/publish in repository-approved order;
6. reconcile catalog and release registry;
7. verify durable artifacts, checksums, provenance, tag/release metadata where applicable;
8. re-read main and report publication only if repository evidence confirms it.

## Anti-halt continuation

If Manual 13 is blocked on human review, keep its reviewed candidate stable and continue safe work on Manual 14 and later manuals: source/version verification, architecture, localization terminology, graphics, generator hardening, accessibility preflight, package/provenance design, and reusable regression checks. A Manual 13 blocker must not halt downstream preparation.
