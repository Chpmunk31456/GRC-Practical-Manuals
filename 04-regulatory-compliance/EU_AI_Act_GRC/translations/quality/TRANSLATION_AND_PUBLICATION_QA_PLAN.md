# Spanish and Brazilian Portuguese Translation and Publication QA Plan

## Scope

This plan governs the `es-419` and `pt-BR` editions of the EU Artificial Intelligence Act GRC Compliance Manual.

## Source freeze

The source baseline is the English production edition merged through PR #31 and subsequent production catalog/workflow commits. Every translation record must identify the exact English source path and source commit.

## Required source coverage

Each language edition must contain:

- complete front matter;
- Chapters 1–138 in exact order;
- Appendices A–Z in exact order;
- all tables, checklists, worksheets, control statements, evidence lists, and audit tests;
- translated captions, alt text, and figure labels;
- legal-version and source statements;
- document-control and revision history.

## Per-file translation record

| Field | Required value |
|---|---|
| English source path | Canonical production path |
| English source commit | Exact commit SHA |
| Target language | `es-419` or `pt-BR` |
| Target path | Controlled translation path |
| Translator status | Draft / reviewed / approved |
| Terminology review | Pass / fail |
| Legal-reference parity | Pass / fail |
| English-fragment scan | Pass / fail |
| Table and heading parity | Pass / fail |
| Reviewer | Name or accountable role |
| Approval commit | Exact commit SHA |

## Linguistic QA

For each translated file:

1. preserve meaning rather than English word order;
2. use natural professional language appropriate to the target locale;
3. preserve legal modality and actor-role distinctions;
4. use the controlled glossary consistently;
5. preserve defined terms and acronyms at first use;
6. remove unintended English fragments;
7. preserve list, table, heading, and form-field structure;
8. verify punctuation, capitalization, accents, hyphenation, and number/date formatting;
9. keep GlobalWay Travel Services facts consistent;
10. retain disclaimers and current-law control statements.

## Legal-reference parity

Automated and manual checks must confirm parity for:

- Regulation numbers;
- article, annex, recital, and chapter references;
- effective dates and transitional deadlines;
- actor roles;
- penalties and retention periods;
- mandatory, recommended, and optional language;
- official-source URLs.

No translation may independently reinterpret the law. A substantive source issue must be corrected in English first and then propagated to both translations.

## Graphics and accessibility

Every included figure must be recreated for each language with:

- translated labels;
- unchanged visual logic and numbering;
- translated caption and alt text;
- accessible contrast;
- no reliance on colour alone;
- readable text at normal zoom;
- target-language written explanation.

English-language graphics must not be reused in the non-English editions.

## Build QA

Each language build must generate:

- integrated Markdown;
- canonical source manifest;
- DOCX;
- PDF;
- checksum file;
- automated QA report;
- PDF metadata report;
- rendered page images.

The build must fail closed for:

- missing or misordered chapters or appendices;
- unresolved placeholders;
- English-source citation markers;
- missing DOCX or PDF;
- invalid package signatures;
- untranslated headings or known English boilerplate;
- manifest/hash mismatches.

## Page-by-page inspection

Inspect every rendered page for:

- clipped or overlapping text;
- broken tables;
- orphaned headings;
- blank or duplicated pages;
- incorrect language fragments;
- missing captions or alt-text records;
- inconsistent headers, footers, and page numbering;
- unreadable figures;
- broken internal references.

## Publication gate

A language edition may be merged into `production/multilingual-grc-editions` only when:

- all 164 source units are translated and approved;
- terminology and legal-reference parity pass;
- all graphics are localized and approved;
- DOCX/PDF automated QA passes;
- page-by-page inspection is closed;
- the production PR documents source commit, test results, known limitations, and release files.

## Current status

Translation governance and terminology controls are established. Full source translation and artifact production remain open.