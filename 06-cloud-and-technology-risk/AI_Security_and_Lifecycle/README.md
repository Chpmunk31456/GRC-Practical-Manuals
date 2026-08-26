# Manual 07 — AI Security and Lifecycle Controls

**Status:** Controlled implementation intake, stacked behind Manual 06.

**Controlled source language:** English (`en`)

**Planned publication languages:** English, neutral Latin American Spanish (`es-419`), Brazilian Portuguese (`pt-BR`)

**Author and accountable human creator:** Alberto “Al” Leiva

## Purpose

Manual 07 will provide practical security engineering and governance controls across the complete AI system lifecycle: concept, data/model acquisition, development, evaluation, deployment, operation, incident/change management, and retirement. It will cover conventional ML, Generative AI, RAG, tool-using systems, and agentic AI. Repository QA is not a guarantee of security and must not be presented as one.

## Controlled source baseline

The intake is anchored to controlled source IDs including:

- `iso-iec-27090` — AI security threats and mitigations; **source-state watch only while ISO lists the first edition as under publication (stage 60.00), not a published final standard**;
- `iso-iec-5338-2023` — AI system lifecycle processes;
- `iso-iec-42001-2023` — AI management-system governance;
- `nist-ai-rmf-1-0` and `nist-ai-600-1` — AI/GenAI risk practices;
- `nist-sp-800-218` — secure software development practices;
- `nist-sp-800-207` — Zero Trust architecture principles.

See [Manual 07 authoritative-source verification](./qa/SOURCE_VERIFICATION_2026-08-26.md).

## Security model

Manual 07 will use defense in depth, least privilege, Zero Trust, strong identity, explicit authorization, human oversight, secure defaults, fail-closed behavior, provenance, monitoring, and recoverability as recurring design principles.

The controlled master addresses:

- AI asset/use-case inventory and ownership;
- threat modeling across data, model, application, orchestration, tool, identity, infrastructure, and supplier layers;
- secure development and change control;
- training/evaluation data provenance and integrity;
- model and component provenance;
- prompt injection and indirect prompt injection;
- retrieval and vector-store security;
- tool and agent authorization boundaries;
- secrets and credential handling;
- data exfiltration and privacy leakage;
- model/system evaluation, adversarial testing, and red teaming;
- guardrails and policy enforcement;
- monitoring, detection, incident response, containment, rollback, and kill/stop mechanisms;
- supplier/component and supply chain risk;
- decommissioning, credential revocation, data retention, and evidence preservation.

See [Manual 07 implementation paths](./MANUAL_07_IMPLEMENTATION_PATHS.md).

## Assurance boundary

Passing Manual 07 QA can show that required controlled topics and release evidence exist. It cannot prove that an AI system is secure, safe, compliant, unbiased, or resistant to every attack.

## Pre-staged release gates

- [x] Controlled intake branch and baseline.
- [x] Lifecycle/security implementation entry.
- [x] Complete controlled English chapter master (32 chapters across four controlled source blocks).
- [x] Authoritative-source verification record completed for the current pre-stage head; ISO/IEC 27090 publication-state correction retained as an explicit release watch item.
- [ ] Reconcile the shared authoritative-source registry entry for ISO/IEC 27090 before release.
- [ ] Re-run dedicated exact-head QA after source-state documentation changes.
- [ ] Complete security architecture and technical review.
- [ ] Complete `es-419` and `pt-BR` localization and human semantic review.
- [ ] Complete educational graphics/accessibility review.
- [ ] Generate and QA DOCX/PDF artifacts.
- [ ] Complete repository/security release audit and provenance.
- [ ] Record final human release approval.

## Important notice

This manual is educational security implementation guidance. System-specific threat modeling, testing, legal/regulatory analysis, and professional security judgment remain necessary.
