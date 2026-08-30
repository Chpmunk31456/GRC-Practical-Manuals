# Manual 15 — Localization and Artifact Handoff

**State:** controlled pre-publication preparation; not publication authorization  
**Series order:** 15  
**Controlling English source blob:** `92bd8eb8b51dbd1367e4968eaf3fad1b399af5d9`  
**Controlling source:** `English/source/CONTROLLED_CHAPTERS_01_32.md`

## Objective

Move Manual 15 from completed controlled English source into exact-source localization and publication-candidate preparation without changing the authoritative interpretation boundary or fabricating human semantic review.

## Exact-source rule

All es-419 and pt-BR localized drafts must derive from the English source blob identified above. If the English source changes materially, localization parity and all downstream artifact hashes are invalidated and must be regenerated from the new exact source.

English remains the controlling interpretation. Localized editions are implementation translations and must not be described as AICPA-authorized or official translations.

## Mandatory terminology boundaries

Preserve these distinctions in both localized editions:

- SOC 2 is an independent CPA attestation examination/reporting engagement, not a certification.
- Trust Services Criteria and Description Criteria are separate controlled concepts.
- Management owns the system description, assertion, controls, evidence and remediation; the independent practitioner owns examination procedures, professional judgment, opinion and report issuance.
- Type 1 and Type 2 readiness must remain distinct.
- Security, availability, processing integrity, confidentiality and privacy must remain separate categories where applicable.
- Complementary user-entity controls and subservice-organization responsibilities must not be collapsed into service-organization controls.
- Readiness assistance must never be represented as replacing independent CPA judgment.

## es-419 controlled-draft requirements

Use professional Latin American Spanish suitable for GRC, audit, privacy, security and executive readers. Retain `SOC 2`, `Trust Services Criteria`, `Description Criteria`, `Type 1`, `Type 2` and other formal identifiers where translation could imply a different official term. Use consistent controlled equivalents for system description, assertion, service organization, subservice organization, complementary user-entity controls, evidence population, operating effectiveness, exception, remediation and reassessment.

The es-419 draft may be machine-assisted, but substantive semantic acceptance must be recorded separately if repository policy requires genuine human judgment.

## pt-BR controlled-draft requirements

Use professional Brazilian Portuguese suitable for GRC, auditoria, privacidade, segurança and executive readers. Retain formal SOC identifiers where translating them could imply an official AICPA translation. Use consistent controlled equivalents for system description, assertion, service organization, subservice organization, complementary user-entity controls, evidence population, operating effectiveness, exception, remediation and reassessment.

The pt-BR draft may be machine-assisted, but substantive semantic acceptance must be recorded separately if repository policy requires genuine human judgment.

## Parity QA

Before artifact generation, fail closed unless all three editions satisfy:

1. exactly 32 chapters in identical order;
2. equivalent chapter purpose and control/evidence intent;
3. no dropped management/practitioner independence boundary;
4. no new certification, endorsement or legal-compliance claim introduced by translation;
5. no omission of owners, frequencies/triggers, populations, evidence, exceptions/remediation or reassessment concepts where present in English;
6. no stale source lineage;
7. no protected AICPA criteria text reproduced beyond permissible use.

## Publication-candidate generation

After trilingual source/parity QA, generate six candidate binaries from the exact controlled sources:

- EN DOCX and PDF;
- es-419 DOCX and PDF;
- pt-BR DOCX and PDF.

The generator must create reproducible metadata, language tags, headings, page numbering, controlled-use notice and source/provenance references. PDFs must undergo text-content preflight and rendered accessibility/visual review. DOCX/PDF files must not be resaved after SHA-256 binding.

## Provenance and durability

For each candidate record:

- source path and source blob/commit;
- artifact path;
- SHA-256;
- generation workflow/run identifier;
- page/content QA result;
- accessibility/visual result;
- terminology/parity result;
- review evidence required by repository policy;
- predecessor publication state.

Validated binaries must then be durably staged to the repository without regeneration. Catalog and work-product release-registry changes occur only after all publication gates are satisfied.

## Current blocker boundary

Manual 14 is published, so predecessor order is satisfied. Manual 15 is not publication-eligible until controlled es-419 and pt-BR editions, exact candidate artifacts, rendered/accessibility QA, checksum/provenance, durable artifact staging, and any explicitly required genuine-human substantive reviews are complete. Standing Final Human Release Approval remains separate and does not substitute for genuine-human review where repository policy explicitly requires it.
