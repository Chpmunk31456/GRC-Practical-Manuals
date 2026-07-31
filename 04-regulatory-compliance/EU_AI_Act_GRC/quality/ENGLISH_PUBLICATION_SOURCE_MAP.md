# EU AI Act GRC Manual — English Publication Source Map

**Branch:** `manual/eu-ai-act-grc-compliance`  
**Status:** Controlled assembly map; publication not authorized

## Purpose

This file defines which repository sources may feed the integrated English master. It prevents original drafts, alternate titles, obsolete audits, and unapproved graphics from entering the DOCX or PDF.

## Controlling legal and editorial sources

1. Regulation (EU) 2024/1689, as amended.
2. Regulation (EU) 2026/1744.
3. Current consolidated EUR-Lex text at the time of final legal verification.
4. Official European Commission and EU AI Office materials, identified as non-binding unless incorporated through a binding instrument.
5. `EU_AI_Act_GRC_Manual_Foundation.md`, subject to the controlling 30 July 2026 correction until direct integration is complete.
6. `quality/FOUNDATION_TIMELINE_AND_SOURCE_REGISTER_CORRECTION_2026_07_30.md`.
7. `quality/CANONICAL_SOURCE_CONSOLIDATION_REGISTER.md`.
8. `quality/APPENDIX_A_Z_CANONICAL_AND_LEGAL_AUDIT_INDEX.md`.
9. `quality/ENGLISH_EDITORIAL_AND_INTERNAL_CONSISTENCY_QA_REGISTER.md`.
10. `quality/GRAPHICS_AND_ACCESSIBILITY_QA_REGISTER.md`.

## Chapter-source rule

For every numbered chapter:

- use the verified corrected master where one exists;
- use the canonical decision in the consolidation register for Chapters 71–79;
- do not assemble from an original long-form draft merely because it contains more text;
- migrate nonduplicative useful material into the canonical source before assembly;
- exclude zero-content, incomplete, alternate-title, and superseded files;
- retain source provenance and commit SHA in the assembly record.

## Appendix-source rule

Use the corrected English master for each Appendix A–Z recorded by the appendix audit index. Specifically:

- Appendix C: `appendices/Appendix_C_Applicability_Assessment_CORRECTED_MASTER.md`
- Appendix F: `appendices/Appendix_F_Role_Assessment_Worksheet_CORRECTED_MASTER.md`
- Appendices A–B, D–E, and G–Z: corresponding corrected-master sources created during appendix legal closure

Original appendix files remain provenance sources only and must not be included automatically.

## Assembly order

### Front matter

1. Cover
2. Copyright and licence
3. Educational and legal disclaimer
4. Acknowledgements
5. How to use the manual
6. Audience guide
7. Acronyms and abbreviations
8. Executive summary
9. Table of contents
10. List of figures
11. List of tables
12. Version and source statement

### Main text

- Chapters 1–138 in canonical numerical order

### Back matter

- Appendices A–Z in canonical alphabetical order
- Source and legal-version statement
- Document-control and revision history

## Front-matter control requirements

The front matter must state:

- the manual is educational and operational guidance, not legal advice;
- legal applicability depends on facts, role, classification, jurisdiction, sector, and current law;
- current consolidated EUR-Lex text controls over the manual if a conflict arises;
- organisation-imposed controls and recommended practices are not automatically statutory duties;
- GlobalWay Travel Services is fictional;
- publication date, version, branch or source commit, and legal verification date;
- licence terms and attribution requirements;
- translations are derivative editions of the frozen English source and require separate legal and linguistic review.

## Figure inclusion rule

A figure may enter the integrated master only when its row in `quality/GRAPHICS_AND_ACCESSIBILITY_QA_REGISTER.md` records:

- approved asset path;
- canonical chapter;
- caption;
- alt text;
- legal review complete;
- accessibility review complete;
- DOCX placement verified;
- PDF rendering verified;
- approval commit SHA.

Known Chapter 83 graphics and the generic Chapters 80–91 poster are excluded until corrected and approved.

## Table inclusion rule

Tables must:

- have a unique number and caption;
- repeat header rows where appropriate;
- avoid split rows where readability would be impaired;
- fit within page margins;
- remain understandable without colour;
- include source or legal-status notes where required;
- use consistent terminology and units;
- have accessible reading order in DOCX.

## Hyperlink and bookmark rule

Before publication:

- validate every external URL;
- prefer official EU sources for legal references;
- validate every internal chapter, appendix, figure, table, and control reference;
- generate bookmarks from the heading hierarchy;
- confirm the TOC, list of figures, and list of tables link to the correct locations;
- remove repository-only links that are not meaningful in the publication artifact.

## Build inputs prohibited from automatic inclusion

- original chapter drafts superseded by corrected masters;
- alternate-title chapter files;
- overlapping legal-audit reports;
- correction packages that have already been incorporated into canonical prose;
- archive candidates;
- unapproved graphics;
- Spanish or Portuguese source files;
- generated DOCX or PDF artifacts from unrelated manuals;
- placeholders, zero-content files, and abandoned figure notes.

## Assembly evidence register

| Sequence | Publication section | Canonical path | Source commit | Legal review | Editorial review | Included in master | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Build gate

The integrated English master must not be represented as final until:

- all canonical paths are populated in the assembly evidence register;
- foundation correction is directly integrated or mechanically applied during build with verification;
- duplicate-content migration is complete;
- legal and editorial findings are closed;
- figure and table inventories are approved;
- source links and internal references pass validation;
- owner approval is recorded.

## Current status

The publication source map is established. The English master remains blocked by direct foundation integration, detailed duplicate-content migration, cross-reference closure, editorial correction of canonical files, approved graphics, and final build validation.