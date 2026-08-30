# Manual 14 — Source State and Release Gates

## Source state

Current controlled baseline for build purposes: **PCI DSS v4.0.1**.

Repository preflight evidence records PCI DSS v4.0.1 as published by PCI Security Standards Council on 2024-06-11, with the future-dated v4 requirements effective date of 2025-03-31 unchanged by v4.0.1. A 2026 RFC exists and must be treated only as future-change intelligence unless and until PCI SSC publishes a successor standard.

Release-time source verification must confirm:

1. whether PCI DSS v4.0.1 is still the current published standard;
2. whether any successor revision has been published;
3. whether validation/reporting documents have changed;
4. whether official FAQ/program guidance changes materially affect implementation advice;
5. whether translated PCI SSC materials have changed terminology relevant to es-419 or pt-BR.

## Copyright and authority boundary

This manual must explain and operationalize PCI DSS without reproducing protected PCI SSC standard text beyond what is legally and repository-policy permissible. It must not claim PCI SSC endorsement, authorization, certification, or official translation status.

## Exact release gates

Before publication the exact candidate must have:

- authoritative-source/version verification;
- controlled English 32-chapter completion;
- es-419 and pt-BR localized controlled drafts;
- source/copyright boundary QA;
- structural and predecessor regression QA;
- terminology and cross-language parity QA;
- DOCX/PDF publication-candidate generation;
- rendered PDF content, accessibility, link, table, heading, language-metadata and visual QA;
- SHA-256 checksums and provenance;
- exact durable binary staging with no resave/regeneration after validation;
- catalog, work-product release registry, manifest and lifecycle reconciliation;
- no unresolved technical, source, integrity, packaging, or substantive defect;
- correct sequential predecessor state.

Under the canonical clean-candidate rule, missing duplicate approval paperwork alone does not halt release when all applicable evidence is green and no substantive defect remains.