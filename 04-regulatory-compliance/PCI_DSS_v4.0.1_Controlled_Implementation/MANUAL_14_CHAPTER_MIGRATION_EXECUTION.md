# Manual 14 — Controlled Chapter Migration Execution

## Purpose

Convert the mapped legacy PCI DSS v4.0.1 practical source into the controlled 32-chapter Manual 14 lineage without copying protected PCI SSC standard text, changing the verified source baseline, or reusing legacy binaries as publication artifacts.

## Execution sequence

1. Build controlled English chapters from the approved migration map using original implementation guidance and only necessary criterion/requirement identifiers.
2. For every chapter, preserve: applicability, control intent, owner, operating frequency, implementation procedure, evidence artifact, evidence location, test method, exception/remediation path, and reassessment trigger.
3. Separate standard interpretation from SAQ/ROC/AOC validation mechanics, contractual/acquirer obligations, and jurisdiction-specific law.
4. Reconcile cross-cutting topics across the 32-chapter architecture: CDE scoping, connected-to/security-impacting systems, data flows, retention, cryptography/key management, secure configuration, vulnerability management, identity/access, MFA, logging/monitoring, testing, incident response, service providers, change control, customized approach, compensating controls, continuous compliance, and reassessment.
5. Run English structural/content QA before localization.
6. Produce es-419 and pt-BR controlled drafts from the exact English candidate; use official PCI SSC terminology only as a reference and retain English as controlling interpretation.
7. Run terminology and cross-language parity checks tied to the exact candidate commit.
8. Generate DOCX/PDF publication candidates only after source/localization QA passes.
9. Run rendered PDF accessibility, links, headings, tables, language metadata, layout, page-break, figure-caption, and visual QA.
10. Generate SHA-256 checksums, provenance, release manifest, and exact-candidate evidence.
11. Stage the exact validated binaries without resaving or regenerating them.
12. Reconcile manual catalog, work-product release registry, lifecycle state, and predecessor order.

## Fail-closed conditions

Do not move to publication if any of the following remains unresolved: current-standard uncertainty, incomplete controlled chapter coverage, translation/parity defect, copyright-boundary defect, rendered-document defect, stale or mismatched checksum/provenance, binary identity drift, missing release-manifest evidence, or a substantive implementation defect.

## Current status

- PCI DSS v4.0.1 source state freshly verified on 2026-08-30.
- Legacy-to-controlled architecture migration map merged.
- Controlled chapter migration is now the active front-line execution task.
