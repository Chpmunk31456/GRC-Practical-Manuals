# Manual 03 — Publication Repair Status — 2026-08-28

**State:** RELEASE REPAIR / FAIL-CLOSED UNTIL HUMAN GATES CLOSE

## Purpose

Repair the missing committed publication-package condition recorded for Manual 03 and revalidate the exact release candidate without weakening semantic, accessibility, provenance, security, or Final Human Release Approval controls.

## Publication evidence

The controlled Manual 03 workflows generate a complete isolated trilingual publication QA package containing:

- English DOCX and PDF;
- Spanish (`es-419`) DOCX and PDF;
- Brazilian Portuguese (`pt-BR`) DOCX and PDF;
- 15 generated learning graphics per language (45 total);
- rendered-review/contact-sheet evidence;
- publication report, page-QA CSV, and SHA-256 manifest.

Exact artifact sizes, page counts, hashes, and source-head identity are recorded in each generated publication report and manifest rather than duplicated in this status file. This prevents stale evidence after a controlled repair commit.

## Visual defect found and remediated

Full-size rendered review identified crowding/overlap in the three fan-out route labels in Manual 03 Figure 1. The controlled English, `es-419`, and `pt-BR` source wording remains unchanged. The shared semantic graph renderer was corrected so each fan-out label is centered in its destination node's horizontal slot, can wrap without truncation, and is drawn on an opaque background.

This renderer-level remediation avoids changing substantive routing criteria merely to fit the graphic and applies consistently to all three language editions. Automated and AI-assisted rendered inspection may support the evidence package but does not substitute for the required human rendered-document review.

## Durable publication-package gate

The approved six DOCX/PDF publication artifacts must be durably placed under the controlled Manual 03 publication package and reconciled to the exact approved candidate before `release_state` can become `published`.

## Remaining fail-closed human gates

- competent semantic/terminology review of `es-419` against English;
- competent semantic/terminology review of `pt-BR` against English;
- human rendered-document accessibility/visual review of the regenerated final candidate;
- changed-scope review recorded against the exact final candidate;
- explicit Final Human Release Approval for that exact candidate.

Automated QA or AI-assisted inspection does not substitute for these human gates.
