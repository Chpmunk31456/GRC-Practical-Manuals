# EU Artificial Intelligence Act GRC Compliance Manual

**Status:** Published and validated in English, Latin American Spanish, and Brazilian Portuguese  
**Languages:** English, `es-419`, and `pt-BR`  
**Default publication branch:** `main`  
**Localized production PR:** #35  
**Main publication PR:** #38

## Purpose

This manual translates the EU Artificial Intelligence Act into a practical governance, risk, compliance, control, evidence, audit, and implementation guide.

It is designed for executives, compliance teams, lawyers, auditors, security teams, procurement, HR, operations, technology teams, and nontechnical business owners.

The manual uses a fictional multinational travel-management company, **GlobalWay Travel Services**, as a recurring case study.

## Published editions

The controlled publication package is complete in:

- English
- Latin American Spanish (`es-419`)
- Brazilian Portuguese (`pt-BR`)

Each language edition includes:

- 138 chapters
- Appendices A–Z
- controlled Markdown master
- DOCX edition
- PDF edition
- build and source manifests
- automated QA report
- PDF metadata
- SHA-256 checksums

The Spanish and Brazilian Portuguese packages are available in [translations](./translations/).

## Publication evidence

The localized editions were validated and merged through pull request #35 from `translation/eu-ai-act-es-ptbr` into `production/multilingual-grc-editions`. The focused EU AI Act v1.3 package was then published to the repository default branch, `main`, through pull request #38.

The approved publication workflow verified structural counts, localized chapter and appendix headings, tables of contents, Figure 12-1, Portuguese Appendix Q, automated QA results, and checksum integrity before publication.

## Writing model

Major sections use this sequence where appropriate:

> **Requirement → Plain-English explanation → GlobalWay travel-agency example → Control activity → Evidence → Audit test**

Legal requirements, recommended practices, organization controls, contractual duties, and optional enhancements are distinguished throughout the manual.

## Controlling legal baseline

The binding legal source baseline is:

1. Regulation (EU) 2024/1689, as amended;
2. Regulation (EU) 2026/1744;
3. the current consolidated EUR-Lex text;
4. official European Commission and EU AI Office guidance, identified as non-binding where applicable.

Key controlled source and quality records include:

- [Corrected Canonical Foundation](./EU_AI_Act_GRC_Manual_Foundation_CORRECTED_MASTER.md)
- [Binding Legal Corrections — Batch 01](./quality/BINDING_LEGAL_CORRECTIONS_BATCH_01.md)
- [Foundation Timeline and Source Register Correction — 30 July 2026](./quality/FOUNDATION_TIMELINE_AND_SOURCE_REGISTER_CORRECTION_2026_07_30.md)
- [Canonical Source Consolidation Register](./quality/CANONICAL_SOURCE_CONSOLIDATION_REGISTER.md)
- [Appendix A–Z Canonical and Legal Audit Index](./quality/APPENDIX_A_Z_CANONICAL_AND_LEGAL_AUDIT_INDEX.md)
- [English Editorial and Internal-Consistency QA Register](./quality/ENGLISH_EDITORIAL_AND_INTERNAL_CONSISTENCY_QA_REGISTER.md)
- [Graphics and Accessibility QA Register](./quality/GRAPHICS_AND_ACCESSIBILITY_QA_REGISTER.md)
- [English Publication Source Map](./quality/ENGLISH_PUBLICATION_SOURCE_MAP.md)
- [Publication Release Checklist](./quality/PUBLICATION_RELEASE_CHECKLIST.md)

## Continuing maintenance

Publication does not freeze the law or official guidance. Future updates should:

1. verify the current consolidated EUR-Lex text;
2. record legal, regulatory, and guidance changes;
3. update the English controlled source first;
4. propagate approved changes to `es-419` and `pt-BR`;
5. rerun structural, linguistic, DOCX, PDF, accessibility, and checksum QA;
6. document the exact production commit and publication evidence.

## Important notice

This manual is educational and operational guidance. It is not legal advice and does not guarantee compliance, certification, audit success, or protection from every AI, privacy, cybersecurity, or operational risk.
