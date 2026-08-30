# Manual 14 — Source State and Release Gates

## Source state

Current controlled baseline for build purposes: **PCI DSS v4.0.1**.

### Live authoritative verification — 2026-08-30

A live PCI Security Standards Council verification on 2026-08-30 confirmed that PCI SSC continues to present **PCI DSS v4.0.1** as the current limited revision in its standards/update surfaces and points users to the PCI DSS v4.x document set. No successor PCI DSS revision was identified in the Council's current standards updates or August 2026 industry-bulletin index during this verification pass.

Authoritative evidence checked:

- PCI Security Standards Council home/standards updates: https://www.pcisecuritystandards.org/
- PCI SSC industry bulletins (including August 2026 current notices): https://www.pcisecuritystandards.org/newsroom_overview/industry_bulletin/
- PCI SSC request-for-comments page, treated only as future-change intelligence and not as a published successor standard: https://www.pcisecuritystandards.org/get_involved/request_for_comments/

Repository preflight evidence records PCI DSS v4.0.1 as published by PCI Security Standards Council on 2024-06-11, with the future-dated v4 requirements effective date of 2025-03-31 unchanged by v4.0.1. Any RFC or future roadmap item must remain future-change intelligence unless and until PCI SSC publishes a successor standard.

Release-time source verification must still confirm immediately before final publication:

1. whether PCI DSS v4.0.1 is still the current published standard;
2. whether any successor revision has been published;
3. whether validation/reporting documents have changed;
4. whether official FAQ/program guidance changes materially affect implementation advice;
5. whether translated PCI SSC materials have changed terminology relevant to es-419 or pt-BR.

This 2026-08-30 verification advances the source-state gate but does not by itself satisfy the final exact-candidate release-time verification if the candidate changes materially or publication occurs after new PCI SSC guidance is issued.

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
