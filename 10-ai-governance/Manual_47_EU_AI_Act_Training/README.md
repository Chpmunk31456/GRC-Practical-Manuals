# Manual 47 — EU AI Act Training & Operationalization

**Status:** CONTROLLED DEVELOPMENT  
**Version:** 0.1.0-draft  
**Role in series:** First specialist training after Manual 46 Universal AI Governance Foundation  
**Source verification date:** 31 August 2026

## 1. Training objective

Teach practitioners how to translate the EU AI Act into an enterprise governance process that identifies scope, determines value-chain roles, classifies AI systems, applies the correct obligations, establishes controls and evidence, and monitors compliance through the lifecycle.

This manual is training-focused. The repository's existing Manual 01 remains the detailed EU AI Act GRC compliance reference.

## 2. Current application timeline

The AI Act entered into force on 1 August 2024 and became generally applicable on 2 August 2026, subject to phased exceptions and later amendments.

Current Commission materials state:

- prohibited-practice and AI-literacy provisions applied from 2 February 2025;
- governance rules and obligations for general-purpose AI models applied from 2 August 2025;
- Article 50 transparency obligations apply from 2 August 2026;
- Annex III high-risk-system rules apply from 2 December 2027;
- high-risk AI embedded in regulated products under Annex I applies from 2 August 2028.

Time-sensitive dates must be reverified immediately before publication.

## 3. Learning sequence

### Module 1 — Scope and applicability

Learners should be able to determine:

- whether an AI system or model falls within territorial and material scope;
- which organizational entity is acting as provider, deployer, importer, distributor, authorized representative or other relevant value-chain actor;
- whether exclusions or special regimes may apply;
- whether multiple roles can apply to one organization.

### Module 2 — Risk classification

Train the learner to distinguish:

- prohibited practices;
- high-risk AI;
- transparency-risk systems subject to Article 50 duties;
- GPAI model obligations;
- minimal/no-risk uses with no dedicated AI Act obligation beyond otherwise applicable law.

Classification should be documented and independently challengeable.

### Module 3 — Prohibited practices

Operational training should cover a formal prohibited-use screening gate before approval. The organization should maintain:

- prohibited-use criteria;
- escalation to legal/compliance;
- documented disposition;
- controls preventing circumvention through vendors or downstream configuration.

### Module 4 — AI literacy

Training should address competence appropriate to organizational roles. AI literacy should be embedded into onboarding, role-based training, policy awareness and governance communications rather than treated as a one-time awareness course.

### Module 5 — High-risk AI requirements

For high-risk AI, training should operationalize requirements around:

- risk management;
- data and data governance;
- technical documentation;
- recordkeeping/logging;
- transparency and instructions for use;
- human oversight;
- accuracy, robustness and cybersecurity;
- quality-management and conformity-related obligations where applicable;
- post-market monitoring and incident processes.

### Module 6 — Provider versus deployer controls

Learners should build separate control matrices for provider and deployer obligations. A procurement decision does not remove deployer accountability, and a provider cannot assume every downstream use will remain within intended conditions.

### Module 7 — General-purpose AI

Training should cover governance of GPAI models, including documentation and transparency duties, downstream information, copyright-related obligations and additional safety/security responsibilities for models subject to systemic-risk provisions.

### Module 8 — Transparency obligations

Article 50 training should address, where applicable:

- informing individuals when they are interacting with AI;
- machine-readable marking/detection of AI-generated or manipulated content;
- labeling deepfakes and certain AI-generated public-interest content;
- documented applicability decisions and evidence that required disclosures operate in production.

### Module 9 — Fundamental rights and impact assessment

Where a fundamental-rights impact assessment or other impact assessment is required, it should be integrated with the enterprise risk process rather than treated as a detached legal form.

Training should connect affected persons, foreseeable impacts, safeguards, human oversight, complaint/contestability mechanisms, residual risk and evidence.

### Module 10 — Human oversight

Human oversight should specify:

- accountable roles;
- information available to the overseer;
- ability to understand system limitations;
- authority to override, stop or escalate;
- safeguards against automation bias;
- recordkeeping for consequential interventions.

### Module 11 — Cybersecurity, robustness and accuracy

AI Act compliance should be connected to existing secure-development, vulnerability-management, identity, logging, change-management and incident-response capabilities.

Testing should be proportionate to intended purpose and reasonably foreseeable misuse.

### Module 12 — Documentation and evidence

Evidence should include, as applicable:

- scope and role determination;
- classification decision;
- risk-management records;
- data-governance evidence;
- technical documentation references;
- testing/validation evidence;
- human-oversight design;
- transparency notices;
- approvals and exceptions;
- provider/deployer instructions;
- monitoring and incident records;
- change and revalidation decisions.

### Module 13 — Third-party and value-chain governance

Procurement should capture:

- provider identity and role;
- model/system documentation;
- intended purpose and limitations;
- data-use terms;
- security/privacy commitments;
- logging and evidence availability;
- material-change notification;
- incident notification;
- cooperation with compliance and regulatory requests;
- exit/transition provisions.

### Module 14 — Post-market monitoring

Governance continues after deployment. Monitoring should evaluate performance, misuse, incidents, changed context, changed models/providers, new jurisdictions and emerging regulatory guidance.

### Module 15 — Enforcement and escalation

The enterprise operating model should define who owns regulatory interaction, internal escalation, incident notification, evidence preservation and remediation.

## 4. Operational decision flow

**Identify AI use → determine territorial/material scope → identify value-chain role → screen prohibited uses → classify risk/GPAI/transparency status → determine obligations → assess impacts and controls → validate → approve → deploy → monitor → manage incidents/changes → revalidate → retire**

## 5. Control design pattern

For each applicable obligation use:

**Legal requirement → organizational interpretation → risk → control objective → control activity → accountable owner → evidence → test method → exception/escalation → remediation**

## 6. Training scenarios

The completed manual will include exercises for:

1. employment-related AI;
2. customer-service chatbot;
3. generative-AI content platform;
4. internally developed GPAI-enabled application;
5. third-party high-risk AI procurement;
6. AI embedded in regulated products;
7. agentic AI with consequential tool access;
8. material model/provider change after production approval.

## 7. Relationship to Manual 46

Manual 46 supplies the universal operating model. Manual 47 overlays EU legal obligations onto that model without replacing the universal governance spine.

## 8. Publication gates

- [ ] Primary-law verification complete.
- [ ] Commission implementation timeline refreshed.
- [ ] Current AI Omnibus amendments and effective dates reconciled.
- [ ] Provider/deployer/GPAI role treatment legally reviewed.
- [ ] High-risk classification examples reviewed.
- [ ] Article 50 transparency treatment verified.
- [ ] Fundamental-rights impact assessment treatment verified.
- [ ] Controlled-English review complete.
- [ ] Accessibility/localization preparation complete.
- [ ] DOCX/PDF visible-page validation complete if artifacts are generated.
- [ ] Provenance/checksums/security QA complete.
- [ ] Required accountable-human release approval recorded.

**Fail-closed:** no publication claim until all applicable gates are green.