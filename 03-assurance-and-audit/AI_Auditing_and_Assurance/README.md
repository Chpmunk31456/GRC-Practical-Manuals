# Manual 05 — AI Auditing and Assurance

**Status:** Controlled full-build lane. This manual is staged behind Manual 04 and must remain draft until the upstream release sequence and all Manual 05 release gates are complete.

**Controlled source language:** English (`en`)

**Planned publication languages:** English, neutral Latin American Spanish (`es-419`), Brazilian Portuguese (`pt-BR`)

**Author and accountable human creator:** Alberto “Al” Leiva

## Purpose

Manual 05 provides a practical, evidence-centered method for auditing AI governance, AI management systems, AI risk controls, Generative AI controls, model/system lifecycle practices, data controls, supplier dependencies, human oversight, and remediation. It is designed for internal audit, second-line assurance, security/GRC assurance, readiness reviews, supplier assurance, and management-system audit preparation without representing repository QA as a formal audit opinion.

## Controlled source baseline

The build is anchored to controlled repository source identifiers and requires source-state impact analysis before baseline changes:

- `iso-19011-2026` — management-system audit guidance;
- `iso-iec-42006-2025` — requirements for bodies providing audit and certification of AIMS;
- `iso-iec-42001-2023` — AI management-system requirements;
- `nist-ai-rmf-1-0` — AI RMF baseline, currently source-watched for revision;
- `nist-ai-600-1` — Generative AI Profile;
- `nist-sp-800-53a-r5` — security/privacy control assessment methods;
- `isaca-aaia` — ISACA Advanced in AI Audit professional-practice reference.

The AAIA reference is used to ensure Manual 05 explicitly covers the current ISACA domains of **AI Governance and Risk**, **AI Operations**, and **AI Auditing Tools and Techniques**. AAIA is treated as a professional certification/job-practice reference, not as law, regulation, an ISO standard, organizational certification, or a formal audit opinion.

This repository does not reproduce copyrighted ISO or proprietary ISACA study/exam material. Authorized standards and licensed publications must be obtained separately where required.

## Practical operating model

The manual organizes audit work into seven controlled stages:

1. **Mandate and scope** — define objective, authority, boundaries, stakeholders, independence constraints, and applicable criteria.
2. **Criteria and evidence plan** — identify authoritative requirements/guidance, internal controls, expected evidence, sampling approach, and test procedures.
3. **Fieldwork and testing** — inspect design, implementation, operation, technical evidence, human oversight, model/system behavior, data controls, and third-party dependencies.
4. **Findings and severity** — distinguish facts, observations, control gaps, risk implications, severity, and evidence limitations.
5. **Management response** — obtain accountable-owner response, target action, risk acceptance/escalation, and due dates.
6. **Remediation validation** — test whether corrective action addresses root cause and whether residual risk is understood.
7. **Closure and follow-up** — retain evidence, track open issues, identify recurring failure patterns, and trigger reassessment after material change.

## AAIA-aligned practice coverage

Manual 05 cross-checks its practical chapter structure against the three public ISACA AAIA domains:

- **AI Governance and Risk** — strategy alignment, responsible-AI governance, risk, data governance, privacy, security, accountability, and compliance-oriented assurance;
- **AI Operations** — lifecycle, data/model/system operations, change, monitoring, resilience, human oversight, suppliers, incidents, and operational evidence;
- **AI Auditing Tools and Techniques** — audit planning, evidence collection, testing, sampling, analytics, technical challenge, findings, reporting, remediation validation, and follow-up.

The manual uses original implementation guidance and public domain names only; it does not copy proprietary AAIA review-manual or exam content.

## Proportional implementation paths

Manual 05 uses the same **Essential / Structured / Enhanced** model as the other controlled manuals. The path changes the depth, independence, evidence volume, sampling, technical testing, and governance rigor; it does not lower the requirement to be truthful about what was and was not tested.

See [Manual 05 implementation paths](./MANUAL_05_IMPLEMENTATION_PATHS.md).

## Evidence principles

Audit conclusions must be traceable to evidence. The controlled chapter master requires, at minimum:

- objective and scope;
- audit criteria and source version;
- systems, models, use cases, vendors, and lifecycle stages in scope;
- evidence requested and received;
- sampling rationale;
- tests performed and limitations;
- finding statement separated from risk interpretation;
- accountable owner;
- management response;
- remediation evidence;
- residual risk and escalation;
- reviewer and approval record.

## Human and assurance boundaries

Automated QA may validate structure, links, parity, known source state, and publication controls. It does **not** establish auditor independence, professional competence, sufficient appropriate evidence, legal compliance, certification, conformity, or a formal audit opinion.

Human judgment remains mandatory for material audit conclusions, semantic/terminology approval of localized editions, exceptions, unresolved evidence conflicts, and final publication approval.

## Current controlled build state

- [x] Controlled intake branch created.
- [x] Machine-readable baseline created.
- [x] Scalable implementation paths created.
- [x] ISACA AAIA controlled professional-practice reference added.
- [x] Controlled English chapter master present as four 8-chapter source blocks covering Chapters 01–32.
- [x] Dedicated Manual 05 QA workflow established and previously passing; exact-head QA must be re-run after material or control changes.
- [ ] Complete authoritative-source verification at publication candidate head.
- [ ] Complete technical and editorial review.
- [ ] Complete `es-419` and `pt-BR` localization and human semantic review.
- [ ] Complete educational graphics and accessible explanations.
- [ ] Complete DOCX/PDF generation and page-by-page QA.
- [ ] Complete repository/security release audit.
- [ ] Complete release manifest, checksums, and provenance.
- [ ] Record/apply final human release approval only after every mandatory gate is green at the exact final candidate.
- [ ] Merge only through the reviewed stacked PR sequence after Manual 04.

## Parallel-throughput rule

While Manual 04 is in release/QC waits, Manual 05 remains the substantive full-build lane. Independent source review, editorial/technical QA preparation, evidence/workpaper refinement, graphics/accessibility work, localization preparation, document-generation preparation, and provenance/release-control work should continue without bypassing Manual 04.

## Important notice

This manual is educational implementation guidance. It is not legal advice, certification, a conformity assessment, or an audit opinion. Any formal assurance engagement must establish its own mandate, independence, competence, criteria, evidence standard, quality controls, and reporting authority.