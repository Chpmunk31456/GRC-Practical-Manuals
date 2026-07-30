# EU AI Act GRC Manual — Graphics and Accessibility QA Register

**Branch:** `manual/eu-ai-act-grc-compliance`  
**Status:** Active; no figure approved for publication solely by inclusion in a draft

## Scope

This register controls every existing, proposed, generated, embedded, or referenced figure in the English manual and its future DOCX and PDF editions.

## Approval requirements

Every approved figure must include:

- a unique figure number;
- a descriptive caption;
- meaningful alt text conveying purpose and material relationships;
- a written explanation in the body text;
- readable labels at normal page zoom;
- accessible contrast;
- no reliance on colour alone;
- terminology matching the canonical chapter;
- current legal references where legal duties or dates are shown;
- source and version traceability;
- a verified placement in the publication source.

## Automatic rejection criteria

Reject or correct a figure containing:

- incorrect article, annex, actor, deadline, retention, notification, or transition information;
- unsupported legal conclusions;
- governance recommendations presented as statutory obligations;
- mixed-language labels;
- duplicated or contradictory concepts;
- unreadable text or excessive density;
- colour-only status distinctions;
- missing caption, alt text, or written explanation;
- content inconsistent with the final chapter text;
- generic poster content that does not materially support the chapter.

## Known findings

| ID | Figure or area | Finding | Required action | Status |
|---|---|---|---|---|
| FIG-001 | Chapter 83 graphics | Known legal and content issues require correction | Rebuild only after Article 22 and human-review wording is verified against the canonical chapter and applicable GDPR sources | Open |
| FIG-002 | Generic Chapters 80–91 poster | Generic multi-chapter poster is not sufficiently chapter-specific and may duplicate concepts | Reject from publication or replace with targeted figures that support defined chapters | Open |
| FIG-003 | Foundation graphics register | Sixteen proposed figures exist as concepts, not approved publication assets | Assign canonical chapter, legal owner, caption, alt text, and validation status before production | Open |
| FIG-004 | Effective dates | Any graphic using a single 2 August 2026 high-risk date is inaccurate after Regulation (EU) 2026/1744 | Use separate 2 December 2027 Annex III and 2 August 2028 Annex I dates, plus other applicable milestones | Open |
| FIG-005 | Article 5 additions | New intimate-content and child-sexual-abuse-material prohibitions require separate treatment and 2 December 2026 application date | Verify wording and avoid combining distinct statutory categories | Open |
| FIG-006 | Article 50 transition | Pre-2 August 2026 synthetic-content systems have a specific 2 December 2026 compliance rule for Article 50(2) | Include only where directly relevant and accurately scoped | Open |
| FIG-007 | Accessibility | Existing images may not have repository-level alt-text records | Build an image inventory linking each asset to caption and alt text | Open |
| FIG-008 | Language | Future Spanish and Portuguese figures must not be generated from unfrozen English wording | Keep localized graphics blocked until English figure approval | Open |

## Proposed figure disposition

| Proposed figure | Intended chapter or section | Legal-risk level | Publication disposition |
|---|---|---|---|
| EU AI Act applicability decision tree | Chapters 2–6 and Appendix C | High | Create only after legal applicability and timeline closure |
| Regulatory role map | Chapters 5 and 18; Appendix F | High | Create after actor-role terminology is frozen |
| AI risk-classification flow | Chapters 19–24; Appendices D/E | High | Create after prohibited, high-risk, transparency, and GPAI logic is verified |
| AI governance operating model | Chapters 8–15 | Moderate | Permitted as organisational model with explicit non-statutory label |
| Three-lines model | Chapter 10 | Moderate | Permitted as assurance model, not a statutory requirement |
| AI inventory workflow | Chapters 16–17; Appendices A/B | Low to moderate | Create after canonical workflow is frozen |
| High-risk AI lifecycle | Chapters 36–52 | High | Create after all actor-specific duties and dates are closed |
| Fundamental-rights impact assessment | Chapters 47 and 93; Appendix G | High | Distinguish Article 27 duty from broader voluntary review |
| Human-oversight model | Chapters 42 and 99; Appendix J | High | Verify actor, system classification, and actual oversight authority |
| GPAI supply chain | Chapters 53–63 | High | Distinguish GPAI model provider from downstream system provider and deployer |
| Incident-reporting workflow | Chapters 50, 59, 73, 127; Appendix N | High | Do not show one universal notification deadline |
| Conformity-assessment pathway | Chapters 44–46 and 118; Appendix L | High | Distinguish Annex I product routes and Annex III routes |
| Control-to-evidence traceability | Chapters 104–108; Appendices U/V | Low | Permitted after control IDs and evidence fields are frozen |
| Third-party AI risk lifecycle | Chapters 71–79; Appendices O/P | Moderate | Create after supplier-governance duplicate consolidation |
| GlobalWay AI ecosystem | Case-study front matter | Moderate | Create after GlobalWay fact sheet is frozen |
| Twelve-month implementation roadmap | Chapters 129–138; Appendix Z | Moderate | Mark clearly as recommended programme sequencing, not statutory deadlines |

## Accessibility test protocol

For every figure:

1. inspect at 100% PDF zoom and normal DOCX view;
2. confirm body text remains readable without enlargement;
3. check contrast using a recognized WCAG-oriented method;
4. confirm meaning remains understandable in greyscale;
5. verify reading order and anchor placement in DOCX;
6. confirm alt text is present and meaningful;
7. verify the caption remains with the figure;
8. confirm no text is clipped after PDF conversion;
9. validate hyperlinks or referenced source notes;
10. record approval and commit SHA.

## Figure inventory and closure evidence

| Figure ID | Asset path | Chapter | Caption | Alt text | Legal review | Accessibility review | DOCX check | PDF check | Status | Commit SHA |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

## Translation control

No localized figure may be approved until:

- the English source figure is frozen;
- legal wording and dates are final;
- source editable files are retained;
- translated labels receive linguistic review;
- no English fragments remain;
- localized alt text and captions are reviewed;
- the localized DOCX and PDF pass visual QA.

## Current decision

No known Chapter 83 graphic or generic Chapters 80–91 poster is approved for publication. Figure production remains subordinate to legal and editorial closure of the relevant canonical text.