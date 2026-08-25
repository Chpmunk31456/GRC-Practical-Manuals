# Manual 02 — Controlled Visual-Learning QA Review 01

**Repository:** `Chpmunk31456/GRC-Practical-Manuals`

**Pull request:** `#89` (draft)

**Branch:** `build/iso-iec-42001-manual-02-2026`

**Starting HEAD:** `2a171be625367ace7c2b605638ea1cb7dae6f636`

**Review date:** 2026-08-24

**Scope:** Ten English source graphics, ten neutral Latin American Spanish (`es-419`) graphics, ten Brazilian Portuguese (`pt-BR`) graphics, twenty localized SVG controlled sources, Markdown placements, captions, alternative text, and accessible explanations.

**Boundary:** This visual QA checks structure, hierarchy, sequence, contrast, memory value, language-source parity, and repository accessibility controls. It does not close the human semantic-review gate or replace page-by-page DOCX/PDF rendering, competent locale review, licensed-source review, assistive-technology testing, or accountable human accessibility approval.

## Executive result

- **30/30 controlled PNG graphics** are present, nonblank, 1657×871 pixels, and placed in the intended chapter sequence.
- **20/20 localized editable SVG sources** include `role="img"`, a title, a description, numbered steps, text labels, and directional arrows.
- All six card colors exceed a 4.5:1 contrast ratio against white text.
- Meaning is not communicated by color alone: cards use ordered position, labels, and arrows; localized variants also use visible step numbers.
- Each localized source set references only its own ten PNGs and provides a localized caption, alternative text, and accessible explanation.
- No clipping, overlap, blank output, misplaced arrow, or missing step was observed in the 30-PNG contact-sheet and focused full-resolution review.

The set is suitable for continued draft review. Final release still requires placed-size readability review, human terminology approval, and page-by-page rendering in every publication format.

## A. Inventory and structural checks

| Control | English | `es-419` | `pt-BR` | Result |
|---|---:|---:|---:|---|
| PNG graphics | 10 | 10 | 10 | PASS |
| Controlled canvas | 1657×871 | 1657×871 | 1657×871 | PASS |
| Editable SVG sources | 0 | 10 | 10 | Conditional; English raster decision remains open |
| Visible ordered steps | Position/arrows | Numbers, position, arrows | Numbers, position, arrows | PASS for sequence; cross-language style differs |
| Alternative text in Markdown | 10 | 10 | 10 | PASS |
| Accessible explanation | English source descriptions | 10 | 10 | PASS at source level |
| Language-specific assets | English only | `es-419` only | `pt-BR` only | PASS |

The English graphics are preserved raster sources from the controlled English DOCX. They are coherent and readable at full resolution, but they do not provide the same editable, numbered, footer-labeled SVG source treatment as the localized sets. This difference is not a content defect, but it remains a release-governance and maintainability decision.

## B. Contrast and non-color meaning

White-text contrast ratios calculated for the controlled card palette:

| Color | Ratio | WCAG normal-text threshold |
|---|---:|---|
| `#17324d` | 13.13:1 | PASS |
| `#2f75b5` | 4.85:1 | PASS |
| `#11777d` | 5.30:1 | PASS |
| `#5b3f91` | 8.19:1 | PASS |
| `#9e5700` | 5.50:1 | PASS |
| `#27815f` | 4.78:1 | PASS |

Color distinguishes stages but does not carry the only meaning. Every stage has a text heading and subtitle; each relationship has spatial order and an arrow; localized figures add step numbers.

## C. Figure-by-figure learning review

| Figure | Learning purpose | Memory/hierarchy result | Open human item |
|---:|---|---|---|
| 1 | PDCA cycle | Clear four-stage sequence and strong “living system” takeaway | Confirm localized wording and placed-size subtitle readability |
| 2 | AIMS scope chain | Effective boundary-building progression from organization to scope | Confirm `función/papel de IA` terminology for locale audience |
| 3 | Risk assessment | Clear method-to-review sequence; supports repeatability | Confirm “probabilidad + impacto” remains appropriate for the manual's broader risk method |
| 4 | Impact assessment | Strong people/effect/control/decision chain | Confirm “accept/escalate” cannot imply unqualified acceptance of harm |
| 5 | Audit chain | Criteria, sampling, evidence, testing, finding, and follow-up are memorable | Confirm Portuguese `constatação` and Spanish audit terminology |
| 6 | Responsible lifecycle | Clear need-to-operation release path | Confirm “release evidence” terminology in both locales |
| 7 | Data lifecycle | Strong provenance and quality sequence | Confirm `conservar/preservar` paired with deletion does not read as a contradiction |
| 8 | Interested parties | Clearly distinguishes audience-specific information duties | Confirm affected-person notice/redress wording and role labels |
| 9 | Third-party lifecycle | Selection-to-exit chain supports supplier risk memory | Confirm exit terminology and customer-context wording |
| 10 | Junior analyst pathway | Strong practical competence story from learning to portfolio | Confirm junior-role noun agreement and retest terminology in both locales |

## D. Placed-size and publication risks

The graphics are readable at native resolution. Their intended document width is approximately 6.15 inches. At that placed size, the smallest card subtitles and localized footer text may render near or below comfortable print-reading size, depending on export scaling, raster resampling, display zoom, and printer resolution.

Required downstream tests:

1. Render every English, Spanish, and Portuguese DOCX/PDF page at 100% and inspect headings, subtitles, arrows, step numbers, statements, and footers.
2. Print or emulate print at target page size and verify that the smallest meaningful text remains readable without magnification.
3. Confirm that each figure stays with its caption and does not split, crop, blur, or exceed page margins.
4. Confirm screen-reader reading order and descriptions in generated DOCX/PDF artifacts.
5. If small text fails, increase type size or simplify the card subtitles before release; do not rely only on higher raster resolution.

## E. Safe decisions from this gate

- No source graphic was regenerated or cosmetically redesigned because no verified content, clipping, or contrast defect justified changing controlled artwork.
- The existing localized SVGs remain the editable sources; the PNGs remain compatibility derivatives for Markdown, Word, and PDF.
- English raster graphics are conditionally accepted for continued draft review only. Final release requires an accountable decision either to approve them as controlled legacy artwork or replace them with editable equivalents that preserve meaning.
- Figures 4, 7, and 10 remain priority human-review items in both localized sets; Portuguese Figure 5 terminology also remains explicitly open.

## F. Release boundary and next action

The accountable human reviewer should approve localized visible labels, captions, alternative text, and accessible explanations. After approved text is stable, generate all three DOCX/PDF editions and complete page-by-page visual, print-size, and assistive-technology QA. Any accepted editorial wording changes that affect graphics must be propagated through the SVG controlled sources and regenerated PNG derivatives before artifact QA.

VISUAL QA STATUS: CONDITIONAL PASS — HUMAN ACCESSIBILITY AND TERMINOLOGY REVIEW OPEN
