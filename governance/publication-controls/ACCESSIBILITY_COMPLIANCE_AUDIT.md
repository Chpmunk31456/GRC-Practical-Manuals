# Accessibility Compliance Audit

Run this audit as a mandatory pre-release gate for every published language and every distributed DOCX/PDF artifact.

## Scope

Audit the Markdown/source, DOCX, PDF, and educational graphics where applicable. Record evidence by file and page rather than relying on a generic accessibility claim.

## Required checks

### Document structure

- Logical heading hierarchy; no skipped or simulated headings where avoidable.
- Correct document title and language metadata.
- Logical reading order.
- Real lists rather than visual-only bullets.
- Tables used for data, not page layout.
- Table headers identified and repeated where needed.
- Links use meaningful text and remain functional.
- Page numbering, headers, footers, and TOC/navigation are consistent.

### Images and graphics

- Informative images have meaningful alt text.
- Decorative images are identified appropriately where the format permits.
- Every important diagram has an adjacent accessible text explanation.
- Meaning does not depend on color alone.
- Contrast is sufficient for normal use and grayscale remains understandable.
- Visible text remains readable at normal page size.

### DOCX checks

- Semantic Word styles are used for headings.
- Reading order is usable.
- No one-cell layout tables for core content.
- Table header rows are defined where applicable.
- Images have descriptions/alt text.
- Hyperlinks and TOC navigation work.
- Core reading content is not trapped in inaccessible text boxes.

### PDF checks

Where supported by the production path:

- Searchable/selectable text.
- Correct language metadata.
- Bookmarks/outline for major headings.
- Tagged structure and logical reading order.
- Table structure represented correctly.
- Figures have alternative descriptions where supported.
- Links remain usable.
- Fonts render safely and accented characters are intact.

### Page-by-page visual inspection

For every PDF page verify:

- no clipped or overlapping text;
- no missing glyphs or corrupted accents;
- no cut-off tables or URLs;
- no missing, distorted, or unreadably small figures;
- captions match the correct graphic;
- headers/footers do not collide with content;
- no unintended blank pages;
- no broken orientation changes.

## Issue severity

- `LOW`: cosmetic or minor usability issue.
- `MEDIUM`: meaningful accessibility/usability degradation with a practical workaround.
- `HIGH`: important content is difficult to access or interpret.
- `CRITICAL`: important content is inaccessible, missing, or materially misleading.

## Gate outcome

Use exactly one:

- `ACCESSIBILITY QA STATUS: PASS`
- `ACCESSIBILITY QA STATUS: PASS WITH APPROVED EXCEPTIONS`
- `ACCESSIBILITY QA STATUS: CORRECTIONS REQUIRED`

No release may proceed with unresolved HIGH or CRITICAL accessibility findings unless a documented, accountable exception explicitly authorizes the residual risk and provides a correction plan.
