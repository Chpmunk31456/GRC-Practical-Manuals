# Manual 03 — Publication Repair Status — 2026-08-29

**State:** RELEASE REPAIR / FAIL-CLOSED UNTIL REMAINING SUBSTANTIVE HUMAN GATES CLOSE

## Purpose

Repair the missing committed publication-package condition recorded for Manual 03 and revalidate the exact release candidate without weakening semantic, accessibility, provenance, security, or changed-scope controls.

## Publication evidence

The controlled Manual 03 workflows generate a complete isolated trilingual publication QA package containing:

- English DOCX and PDF;
- Spanish (`es-419`) DOCX and PDF;
- Brazilian Portuguese (`pt-BR`) DOCX and PDF;
- 15 generated learning graphics per language (45 total);
- rendered-review/contact-sheet evidence;
- publication report, page-QA CSV, and SHA-256 manifest.

The six DOCX/PDF publication artifacts are now durably committed under `01-foundations/NIST_AI_RMF_1.0/publication/` together with compact QA evidence. Exact artifact sizes, page counts, hashes, and source-head identity remain recorded in the generated publication report and manifest rather than duplicated here.

## Visual defect found and remediated

Full-size rendered review identified crowding/overlap in the three fan-out route labels in Manual 03 Figure 1. The controlled English, `es-419`, and `pt-BR` source wording remains unchanged. The shared semantic graph renderer was corrected so each fan-out label is centered in its destination node's horizontal slot, can wrap without truncation, and is drawn on an opaque background.

This renderer-level remediation avoids changing substantive routing criteria merely to fit the graphic and applies consistently to all three language editions. Automated and AI-assisted rendered inspection may support the evidence package but does not substitute for the required human rendered-document review.

## Repository release-pipeline reconciliation

The controlled-build publication QA compatibility repair was merged to `main` through PR #130. Published controlled-build manuals are now validated with explicit English, `es-419`, and `pt-BR` Markdown/DOCX/PDF evidence rather than being rejected solely because of their controlled-build layout. Manual 01 also now has a durable English publication package on `main`.

This status update intentionally retriggers Manual 03 exact-head QA against that repaired base.

## Closed gates

- durable repository placement of the six Manual 03 DOCX/PDF artifacts: **COMPLETE**;
- standing Final Human Release Approval: **PRE-AUTHORIZED** under the repository release procedure and requires no additional owner prompt once all preceding substantive gates are green.

## Remaining fail-closed substantive human gates

- competent semantic/terminology review of `es-419` against English;
- competent semantic/terminology review of `pt-BR` against English;
- human rendered-document accessibility/visual review of the regenerated final candidate;
- human changed-scope review recorded against the exact final candidate;
- exact-final repository/security/provenance reconciliation after those reviews.

Automated QA or AI-assisted inspection does not substitute for the required competent human review evidence. Once these remaining gates are evidenced and exact-final reconciliation is green, the standing automatic-publication rule applies and Manual 03 must be published without another approval request.
