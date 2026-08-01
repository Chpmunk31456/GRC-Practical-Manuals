# ISO/IEC 27001 and 27002 Localization — Fail-Closed Audit

Date: 2026-08-01

Repository: `Chpmunk31456/GRC-Practical-Manuals`

Branch: `production/multilingual-grc-editions`

Pull request: `#3` — remains draft and unmerged

## Result

**FAIL — FULL LOCALIZED SOURCE REVIEW AND REPAIR REQUIRED**

The Latin American Spanish and Brazilian Portuguese Markdown sources are not suitable for publication rebuild. The defects are not confined to front matter or the generated table of contents; they continue into substantive chapters.

## Control source

Approved English master:

`02-management-systems/ISO_IEC_27001_27002/English_Source_ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md`

English source blob SHA reviewed: `77568a9e61d6769d6eb3dbbed6b131a58d60e1f1`

The English technical/editorial source gate is recorded as PASS in:

`qa/release/ISO_IEC_27001_27002_ENGLISH_TECHNICAL_EDITORIAL_REVIEW_2026-07-31.md`

## Spanish findings

Source:

`02-management-systems/ISO_IEC_27001_27002/Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md`

Verified defects include:

- untranslated English labels and headings;
- malformed title and emphasis markup;
- malformed Markdown tables and table-of-contents links;
- an incorrect machine translation of the Word table-of-contents instruction;
- corrupted image markup, including a non-Latin character replacing the opening angle bracket in an image element;
- missing heading markers for numbered sections;
- injected or nonsensical text in tables;
- technically material mistranslations involving Annex A controls, certification, climate-change amendment language, scope, risk, evidence, and management review;
- inconsistent use of `ISMS` and `SGSI`;
- untranslated alt text and captions;
- broken prose and sentence structure that cannot be corrected safely by isolated search-and-replace rules.

Representative verified examples include malformed Chapter 1 and Chapter 2 tables, corrupted Figure 1 and Figure 2 markup, `Management Review and Corrective Action` left untranslated, `Lectura de certificación` used for certification readiness, and nonsensical inserted phrases such as `La vida eterna` and `Silencioso`.

## Brazilian Portuguese findings

Source:

`02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md`

Verified defects include:

- malformed title, emphasis, and front-matter structure;
- collapsed tables represented as unstructured text;
- missing heading markers for numbered sections;
- mixed Brazilian and European Portuguese forms, including `controlo`, `selecção`, `objectivo`, `activo`, `registo`, and `planeamento`;
- distorted technical wording, including climate-change amendment language, scope, risk, evidence, and certification concepts;
- untranslated English alt text;
- malformed numbering such as `28,4`;
- wording that does not meet a controlled Brazilian Portuguese terminology standard.

## Superseded repair assumption

The earlier working assumption that the repair could be limited to the opening and table-of-contents region is rejected. Chapter 1 onward is not clean and must not be preserved as an approved localized body.

No localized source replacement or package rebuild should proceed under an opening-only scope.

## Required recovery method

1. Treat the approved English master as the canonical semantic and structural control.
2. Divide each localized manual into bounded sections using the English numbered-section structure.
3. Review and repair Spanish and Brazilian Portuguese separately.
4. Preserve framework names, product names, anchors, image paths, and intended technical meaning.
5. Reconstruct Markdown headings, tables, lists, image syntax, captions, and links deterministically.
6. Apply a controlled terminology glossary for ISO/IEC 27001, ISO/IEC 27002, ISMS/SGSI, Statement of Applicability, risk treatment, internal audit, management review, nonconformity, corrective action, certification, accreditation, Annex A themes, and evidence.
7. Run structural comparison against the English master and language-specific prohibited-marker checks.
8. Rebuild DOCX and PDF only after the complete localized Markdown source passes.
9. Validate DOCX archive integrity, embedded media, searchable PDF text, headings, tables, links, page count, metadata, and visual layout.
10. Record exact source/package hashes and the final candidate production SHA.

## Release implication

Both localized ISO editions are blocked. Existing Spanish and Brazilian Portuguese DOCX/PDF files must not be represented as reviewed or publication-ready.

This failure does not invalidate the approved English Markdown master. It does prevent the ISO manual family from passing the multilingual release gate.

## Human-review boundary

Machine-assisted repair can restore structure and produce controlled draft translations, but final Spanish and Brazilian Portuguese terminology, naturalness, accessibility, and technical-language approval remain human review requirements.
