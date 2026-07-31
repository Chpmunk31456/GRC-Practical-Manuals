# EU AI Act GRC Manual — Canonical Cross-Reference Validation Plan

**Branch:** `manual/eu-ai-act-grc-compliance`  
**Status:** Active publication-closure control  
**Scope:** Corrected canonical foundation, Chapters 1–138, Appendices A–Z, quality records, figures, tables, and final publication outputs

## Objective

Verify that every internal reference resolves to the correct canonical source and that no publication artifact relies on a superseded, incomplete, zero-content, alternate-title, or legally outdated file.

## Validation population

1. chapter-to-chapter references;
2. chapter-to-appendix references;
3. appendix-to-chapter references;
4. references to articles, annexes, dates, actor roles, figures, tables, controls, and evidence;
5. README and foundation links;
6. quality-record links;
7. image, caption, and alt-text references;
8. DOCX and PDF bookmarks, Table of Contents entries, figure lists, table lists, and hyperlinks.

## Canonical resolution rules

- A verified `_CORRECTED_MASTER.md` file controls over a conflicting earlier draft.
- The corrected canonical foundation controls over the earlier research foundation for legal-source, timeline, modality, and publication-status statements.
- Appendix C and Appendix F corrected masters control over their earlier drafts.
- Chapters 71–79 follow the verified canonical chapter map and consolidation register.
- Chapters 115–138 use the corresponding corrected masters.
- Appendices A–Z use the corrected masters created during Appendix audit closure.
- No reference may resolve to a file identified as zero-content, incomplete, or pending migration.

## Test procedure

For each reference:

1. identify the source file and exact reference text;
2. resolve the target path or numbered item;
3. confirm the target exists on the workstream branch;
4. confirm the target is canonical;
5. confirm title, number, terminology, legal role, and date agree with the target;
6. record broken, ambiguous, stale, or circular references;
7. correct the canonical source rather than masking the defect in the final build;
8. retest after correction;
9. record the validating commit SHA.

## High-priority tests

- Chapters 71–79 and Appendices O/P/U/V supplier-governance references;
- Chapters 36–52 and Appendices E/G/I/J/K/L/M/N/T high-risk references;
- Chapters 53–63 GPAI role and systemic-risk references;
- Chapters 64–70 and Appendix R transparency references;
- Chapters 92–121 risk, control, evidence, assurance, and audit references;
- Chapters 129–138 and Appendix Z roadmap references;
- all references to Regulation (EU) 2026/1744 and the revised application dates;
- all references to Article 5, Article 6, Article 27, Article 43, Article 50, Articles 53 and 55, Articles 72 and 73, and Annexes I, III, and IV.

## Finding register

| Finding ID | Source | Reference | Expected target | Actual result | Severity | Action | Owner | Status | Validation commit |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## Severity criteria

- **Critical:** points to legally incorrect, prohibited, or materially misleading content.
- **High:** points to a superseded, missing, incomplete, or wrong-numbered canonical source.
- **Moderate:** terminology, title, numbering, or contextual inconsistency that may confuse readers.
- **Low:** formatting, capitalization, or non-material link-label defect.

## Closure criteria

Cross-reference validation is complete only when:

- every canonical chapter and appendix has been tested;
- all critical and high findings are closed;
- remaining moderate or low findings are documented and approved;
- final DOCX and PDF navigation is tested independently;
- the validated branch commit is recorded in the publication release checklist.
