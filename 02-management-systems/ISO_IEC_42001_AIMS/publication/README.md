# Manual 02 publication QA candidates

This directory contains controlled **publication QA candidates** for Manual 02. It is not a release directory.

## Control record

- Manual: `02`
- Edition/version: `1.0 publication QA candidate`
- Source branch: `build/iso-iec-42001-manual-02-2026`
- Source commit: `b1ddffa6a33376ec72db570d8437f996cf61b97d`
- Generation date: `2026-08-24`
- English status: controlled-source publication QA candidate
- Spanish and Brazilian Portuguese status: **DRAFT — HUMAN SEMANTIC REVIEW REQUIRED**
- Human semantic-review gate: open
- Release-ready: no

The Spanish and Brazilian Portuguese documents are layout and accessibility candidates generated only from the reviewed localized source files already present on this branch. Document processing did not silently change disputed or substantive translation meaning.

## Candidate artifacts

| Language | Controlled Markdown master | Accessible DOCX | Accessible PDF |
|---|---|---|---|
| English | [`../English/ISO_IEC_42001_2023_Practical_AIMS_Manual_English_v1.0.md`](../English/ISO_IEC_42001_2023_Practical_AIMS_Manual_English_v1.0.md) | [`qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_EN.docx`](qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_EN.docx) | [`qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_EN.pdf`](qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_EN.pdf) |
| Spanish (`es-419`) | [`../translations/es-419/source/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.md`](../translations/es-419/source/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.md) | [`qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.docx`](qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.docx) | [`qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.pdf`](qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_ES-419.pdf) |
| Brazilian Portuguese (`pt-BR`) | [`../translations/pt-BR/source/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.md`](../translations/pt-BR/source/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.md) | [`qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.docx`](qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.docx) | [`qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.pdf`](qa-candidate/Manual_02_ISO_IEC_42001_AI_Management_System_PT-BR.pdf) |

Checksums and page-level QA records are in [`../../../qa/manual02-document-processing`](../../../qa/manual02-document-processing).

## Reproduction and QA

Run from the repository root:

```bash
python3 scripts/generate_iso42001_publication.py \
  --source-commit b1ddffa6a33376ec72db570d8437f996cf61b97d \
  --generation-date 2026-08-24 \
  --force

python3 scripts/qa_iso42001_publication.py \
  --source-commit b1ddffa6a33376ec72db570d8437f996cf61b97d \
  --generation-date 2026-08-24
```

The generator refuses to replace an existing candidate unless `--force` is supplied. It does not overwrite the English controlled Markdown or the four-part localized source files.

## Assurance boundary

These materials are original educational implementation guidance. They do not reproduce ISO standard text beyond material legitimately present in the repository, are not ISO-authorized translations, and do not establish certification, conformity, legal compliance, or audit assurance. The localized editions must not move to a release package until competent human semantic and terminology reviewers close the recorded gate.
