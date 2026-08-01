# ISO/IEC 27001 and 27002 Localized Opening Repair Findings

Date: 2026-08-01

Repository: `Chpmunk31456/GRC-Practical-Manuals`

Branch: `production/multilingual-grc-editions`

Pull request: `#3` — draft and unmerged

## Status

**RELEASE-BLOCKING LOCALIZATION DEFECT CONFIRMED**

## Controlled comparison

The Spanish and Brazilian Portuguese localized Markdown openings were compared with the approved English master:

- `02-management-systems/ISO_IEC_27001_27002/English_Source_ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_v1.0.md`
- `02-management-systems/ISO_IEC_27001_27002/Espanol/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Espanol_v1.0.md`
- `02-management-systems/ISO_IEC_27001_27002/Portugues_BR/ISO_IEC_27001_27002_Practical_Manager_and_Junior_Analyst_Manual_Portugues_BR_v1.0.md`

The defect boundary begins at the first line and continues through the generated table of contents. Chapter 1 begins after this bounded opening region and is not authorized for modification by this repair.

## Spanish findings

Verified defects include:

- untranslated English series, contents, and publication-notice labels;
- malformed title punctuation and spacing;
- malformed one-cell Markdown table syntax (`|. |`);
- mistranslation of “Word table of contents” as `Contenido de la palabra`;
- broken or duplicated Markdown link syntax in the generated table of contents;
- inconsistent English and Spanish visible chapter titles;
- mistranslated phrases affecting professional meaning, including `cambiadores de carrera`, `Uso electrónico y autorizado`, and `ISO/IEC 27001 y 27002 Foundations`;
- grammatical defects in the Amendment 1:2024 and management-system descriptions.

## Brazilian Portuguese findings

Verified defects include:

- broken emphasis markers and heading syntax;
- inconsistent capitalization and encoding in the series title;
- mixed Portuguese variants (`controlos`, `planeamento`) in a Brazilian Portuguese edition;
- missing Markdown heading markers for the preface, manual-use section, and table of contents;
- malformed Word table-of-contents callout;
- untranslated or awkward visible table-of-contents labels;
- grammatical defects in the Amendment 1:2024 and management-system descriptions.

## Authorized repair scope

The bounded repair may:

1. replace each localized opening from the first line through the final generated table-of-contents entry immediately before Chapter 1;
2. preserve the English master’s factual meaning, section order, page references, and anchor targets;
3. correct visible Spanish and Brazilian Portuguese terminology, grammar, capitalization, punctuation, and Markdown structure;
4. preserve the machine-assisted-draft review notice until full human language approval is separately documented; and
5. rebuild only the affected ISO localized DOCX/PDF packages after source validation.

The repair must not:

- change the approved English source;
- alter Chapter 1 or later substantive localized body content;
- claim full human language approval;
- claim ISO conformity, certification, or legal review; or
- mark PR `#3` ready or merge it.

## Required validation

Before this gate can pass, the repair workflow must verify:

- exactly one Chapter 1 boundary remains in each localized source;
- the body from Chapter 1 onward is byte-for-byte unchanged;
- no malformed opening tokens remain;
- all table-of-contents anchors and page references remain present;
- DOCX ZIP integrity passes;
- PDF text is searchable;
- localized title, publication notice, Word table-of-contents instruction, and Chapter 1 marker appear in PDF text; and
- visual-review artifacts are generated for page-level inspection.

## Current release implication

The ISO Spanish and Brazilian Portuguese packages remain draft localization candidates and are not publication-ready until this bounded repair, rebuild, and generated-document review are completed.
