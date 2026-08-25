# Manual 02 — Human Semantic and Terminology Review Checklist

**Applies to:** ISO/IEC 42001 Manual 02 localized draft sources in neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`)

**Gate status:** OPEN — human review required before localized sources may be consolidated or represented as final release editions.

This checklist is a controlled human-in-the-loop gate. Automated QA and AI assistance may identify structural, terminology, accessibility, and parity issues, but **must not mark this gate complete or impersonate a human language/domain reviewer**.

## 1. Reviewer qualifications and independence

Record the reviewer for each language and confirm that the reviewer can evaluate both meaning and professional GRC/AI-management terminology.

| Field | Español (`es-419`) | Português (`pt-BR`) |
|---|---|---|
| Reviewer name | Pending | Pending |
| Review date | Pending | Pending |
| Language competence | Pending | Pending |
| ISO/AI/GRC domain competence | Pending | Pending |
| Relationship/conflict note | Pending | Pending |
| Review result | Pending | Pending |

A reviewer does not need to be an ISO certification auditor, but the review must be performed by a competent human who can identify misleading terminology, changed meaning, false assurance, and unnatural localized language.

## 2. Controlled source set

### Español de América Latina (`es-419`)

- `es-419/source/01_PRELIMINARES_CAPITULOS_01_08.md`
- `es-419/source/02_CAPITULOS_09_16.md`
- `es-419/source/03_CAPITULOS_17_24.md`
- `es-419/source/04_CAPITULOS_25_32.md`

### Português do Brasil (`pt-BR`)

- `pt-BR/source/01_PRELIMINARES_CAPITULOS_01_08.md`
- `pt-BR/source/02_CAPITULOS_09_16.md`
- `pt-BR/source/03_CAPITULOS_17_24.md`
- `pt-BR/source/04_CAPITULOS_25_32.md`

The English 32-chapter Markdown master remains the semantic source of truth during this review.

## 3. Meaning-preservation review

For each chapter, the human reviewer should verify that the localized text preserves the practical meaning of the English master without adding or removing obligations.

- [ ] Chapter titles preserve scope and subject.
- [ ] Clause and Annex references remain correct.
- [ ] Requirements are not strengthened into claims that ISO does not make.
- [ ] Guidance is not weakened so that an important control, risk, impact, evidence, or approval step disappears.
- [ ] Risk assessment and AI system impact assessment remain distinct concepts.
- [ ] Statement/Declaración/Declaração of Applicability concepts remain accurate.
- [ ] Certification language does not imply product certification, guaranteed safety, legal compliance, or guaranteed audit success.
- [ ] Internal-audit independence and management accountability remain clear.
- [ ] Supplier/customer responsibility is not mistranslated as transfer of accountability.
- [ ] Tool outputs are consistently described as evidence inputs rather than proof of conformity.
- [ ] Corrective action remains distinct from correction.
- [ ] Human oversight, affected-person considerations, complaints, redress, and change triggers remain present.

## 4. Controlled terminology review

### Spanish (`es-419`) terms to verify consistently

- `sistema de gestión de inteligencia artificial (SGIA)`
- `Declaración de Aplicabilidad`
- `evaluación de riesgos de IA`
- `evaluación de impacto de sistemas de IA`
- `alta dirección`
- `auditoría interna`
- `revisión por la dirección`
- `no conformidad`
- `corrección`
- `acción correctiva`
- `mejora continua`
- `parte interesada`
- `riesgo residual`
- `propietario del riesgo`
- `proveedor`
- `supervisión humana`

### Brazilian Portuguese (`pt-BR`) terms to verify consistently

- `sistema de gestão de inteligência artificial (SGIA)`
- `Declaração de Aplicabilidade`
- `avaliação de riscos de IA`
- `avaliação de impacto de sistemas de IA`
- `alta direção`
- `auditoria interna`
- `análise crítica pela direção`
- `não conformidade`
- `correção`
- `ação corretiva`
- `melhoria contínua`
- `parte interessada`
- `risco residual`
- `proprietário do risco`
- `fornecedor`
- `supervisão humana`

The reviewer may approve a different professional term when it is more natural or technically correct for the target locale, but the decision should be recorded and applied consistently.

## 5. Tables, templates, and evidence questions

- [ ] Table headings are natural and unambiguous in the target language.
- [ ] Rows preserve the same decision/evidence relationship as the English master.
- [ ] Template fields do not alter authority, accountability, or required evidence.
- [ ] Blank fields remain usable for practitioners.
- [ ] Examples remain examples rather than implied ISO requirements.
- [ ] The 38-control Annex A discussion is not presented as a universal checklist.
- [ ] Certification Stage 1 and Stage 2 descriptions remain appropriately bounded.

## 6. Figures and accessibility

The localized source drafts now reference ten language-specific learning graphics per language. Each figure has an editable SVG controlled source, a 1657×871 PNG derivative, numbered steps, arrows, localized visible labels, alternative text, and an accessible explanation. Their production resolves the English-visible-label dependency, but a competent human must still confirm terminology, meaning, readability, and accessibility before release.

For each figure:

- [ ] Caption meaning is correct.
- [ ] Alternative text is accurate and useful.
- [ ] Accessible explanation communicates the decision/process without requiring the image.
- [ ] Visible labels use accurate and natural terminology for the target locale.
- [ ] Meaning does not depend on color alone.
- [ ] The localized graphic does not introduce a new requirement or remove a decision point.

## 7. Official-source and copyright boundary

- [ ] ISO/IEC 42001, ISO/IEC 42005, ISO/IEC 42006, ISO/IEC 23894, and ISO 19011 references retain the correct standard identifiers and editions.
- [ ] Official-source links are not altered to unofficial substitutes.
- [ ] The localized manual remains original educational guidance and does not reproduce protected ISO clause/control text.
- [ ] The disclaimer clearly states that the localized work is not an ISO-authorized translation.
- [ ] No statement implies OpenAI, ISO, an accreditation body, or a certification body endorses the manual.

## 8. Locale and readability

- [ ] Spanish is neutral and practical for Latin American readers; avoid unexplained Spain-specific legal or professional usage unless required by a source.
- [ ] Portuguese follows natural Brazilian professional usage rather than literal English syntax.
- [ ] Acronyms are introduced before repeated use where needed.
- [ ] Sentences are readable for managers and junior analysts without losing technical precision.
- [ ] Examples, role names, and instructions sound natural to practitioners in the target locale.

## 9. Issue log

Record every material correction made during human review.

| ID | Language | Chapter/section | Issue | Severity | Resolution | Reviewer verification |
|---|---|---|---|---|---|---|
| HR-001 | Pending | Pending | Pending | Pending | Pending | Pending |

Severity guidance:

- **Critical:** changes compliance/certification meaning, authority, safety boundary, or source identity.
- **Major:** materially changes a control, risk, impact, evidence, lifecycle, audit, supplier, or corrective-action concept.
- **Minor:** terminology, readability, punctuation, or style with no material change in meaning.

## 10. Human sign-off gate

This gate may change from OPEN to COMPLETE only after both language reviews are finished, all Critical and Major issues are resolved, and the human reviewer records approval below.

| Language | Human reviewer | Decision | Date | Critical open | Major open |
|---|---|---|---|---:|---:|
| `es-419` | Pending | Pending | Pending | Pending | Pending |
| `pt-BR` | Pending | Pending | Pending | Pending | Pending |

**Controlled release rule:** Until both rows contain a human `APPROVED` decision with zero open Critical and Major issues, the baseline must remain `draft-human-review-required`, localized DOCX/PDF artifacts must not be described as final, and Manual 02 must remain a draft development item.
