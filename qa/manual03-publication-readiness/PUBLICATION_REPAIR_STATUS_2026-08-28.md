# Manual 03 — Publication Repair Status — 2026-08-28

**State:** RELEASE REPAIR / FAIL-CLOSED UNTIL HUMAN GATES CLOSE

## Purpose

Repair the missing committed publication-package condition recorded for Manual 03 and revalidate the exact release candidate without weakening semantic, accessibility, provenance, security, or Final Human Release Approval controls.

## Evidence already obtained

A current controlled Manual 03 workflow run generated a complete isolated publication QA package containing:

- English DOCX and PDF;
- Spanish (`es-419`) DOCX and PDF;
- Brazilian Portuguese (`pt-BR`) DOCX and PDF;
- 15 generated learning graphics per language (45 total);
- page renders and contact sheets for all editions;
- publication report, page-QA CSV, and SHA-256 manifest.

The generated package reported PASS for all six publication artifacts. Independent local verification also confirmed all six recorded SHA-256 values, zero findings from the DOCX accessibility audit for each edition, and openable/non-scanned PDFs with the expected 45/47/47 page counts.

## Visual defect found and remediated in this branch

Full-size rendered review identified crowding/overlap in the three fan-out route labels in Manual 03 Figure 1. The controlled English, `es-419`, and `pt-BR` source wording is preserved unchanged. The shared semantic graph renderer was corrected instead so parallel fan-out edges receive staggered routing lanes and wrapped labels on opaque backgrounds.

This renderer-level remediation avoids changing substantive routing criteria merely to fit the graphic and applies consistently to all three language editions. The publication workflow must regenerate the complete trilingual package at the exact branch head, and rendered review must confirm the overlap is closed.

## Remaining fail-closed human gates

- competent semantic/terminology review of `es-419` against English;
- competent semantic/terminology review of `pt-BR` against English;
- human rendered-document accessibility/visual review of the regenerated final candidate;
- changed-scope review recorded against the exact final candidate;
- explicit Final Human Release Approval for that exact candidate.

Automated QA or AI-assisted inspection does not substitute for these human gates.
