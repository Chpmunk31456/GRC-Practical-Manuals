# Manual 46 — Global AI Governance: Senior Manager Interview & Operating Model

**Build status:** CONTROLLED DEVELOPMENT  
**Version:** 0.1.0-draft  
**Source verification date:** 31 August 2026  
**Primary language:** English  
**Audience:** AI Governance Program Managers, Senior Managers, GRC leaders, cybersecurity/privacy leaders, model-risk teams, internal audit, legal/compliance partners, product and technology leaders.

## Training objective

Enable a senior practitioner to explain, design, defend, and operationalize an enterprise AI governance program across regulatory, standards, risk, security, privacy, assurance and agentic-AI domains—without treating each framework as an isolated checklist.

## Interview outcome

By completion, the learner should be able to answer executive and panel questions using a repeatable structure:

1. Establish business context and intended AI use.
2. Identify accountable owner and affected stakeholders.
3. Inventory and classify the AI system/use case.
4. Determine applicable legal/regulatory obligations.
5. Assess AI, security, privacy, data, human-rights and third-party risks.
6. Define controls proportionate to risk and autonomy.
7. Establish human oversight and approval authority.
8. Validate before deployment.
9. Record evidence and residual-risk decisions.
10. Monitor performance, drift, incidents and change.
11. Escalate, remediate or suspend when thresholds are exceeded.
12. Audit, report and continuously improve.

## Part I — Executive mental model

### 1. What AI governance is

AI governance is the system of decision rights, policies, controls, evidence, accountability and assurance used to ensure that AI is selected, developed, acquired, deployed, operated, changed and retired consistently with law, organizational risk appetite, security, privacy, human rights, ethical commitments and business objectives.

### 2. The governance spine

**Accountability → Inventory → Classification → Risk/Impact Assessment → Data Governance → Security → Human Oversight → Transparency → Testing/Validation → Documentation → Approval → Deployment → Monitoring → Incident/Change Management → Third-Party Governance → Evidence/Audit → Retirement → Continuous Improvement**

### 3. Risk-based—not paperwork-based—governance

Governance intensity should be driven by factors such as:

- Legal or regulatory classification.
- Degree of autonomy and ability to take consequential action.
- Impact on people, rights, safety or access to essential services.
- Data sensitivity and provenance.
- Cybersecurity exposure and tool/API access.
- Model capability, scale and systemic impact.
- Business criticality and financial impact.
- Reversibility of decisions and availability of human intervention.
- Third-party dependency and concentration risk.
- Geographic deployment and jurisdiction.

## Part II — Framework landscape

### 4. EU AI Act

Interview focus:

- Risk-based regulatory model and prohibited practices.
- AI literacy.
- Provider/deployer and value-chain responsibilities.
- General-purpose AI obligations.
- Transparency duties, including interactive AI and synthetic content.
- High-risk AI controls and later application dates.
- Documentation, logging, human oversight, robustness, cybersecurity and accuracy.
- Post-market monitoring, incident handling and enforcement.

**Current timing note (verified 31 August 2026):** the Act entered into force on 1 August 2024 and became generally applicable on 2 August 2026, subject to phased exceptions. Prohibited practices and AI-literacy provisions applied from 2 February 2025; governance and GPAI obligations applied from 2 August 2025; transparency requirements and Commission/member-state enforcement began 2 August 2026. Current Commission materials state that Annex III high-risk rules apply from 2 December 2027 and regulated-product high-risk rules from 2 August 2028.

Dependency: Manual 01 remains the detailed EU AI Act compliance manual.

### 5. ISO/IEC 42001

Interview focus:

- AI management system (AIMS), organizational context and scope.
- Leadership, policy, objectives and accountability.
- AI risk and impact assessment.
- Lifecycle and data controls.
- Supplier governance.
- Monitoring, internal audit, management review, nonconformity and continual improvement.
- Integration with existing ISO management systems.

Copyright control: operational concepts may be explained, but protected standard text is not reproduced.

Dependency: Manual 02 remains the detailed ISO/IEC 42001 implementation manual.

### 6. NIST AI RMF 1.0

Use the four functions as an operating vocabulary:

- **GOVERN** — culture, accountability, policies, roles, risk tolerance and lifecycle governance.
- **MAP** — context, intended purpose, affected parties, dependencies, impacts and risk framing.
- **MEASURE** — testing, evaluation, verification, validation, metrics and uncertainty.
- **MANAGE** — prioritize, treat, monitor, communicate and respond to risk.

NIST states that AI RMF 1.0 is voluntary, rights-preserving, non-sector-specific and use-case agnostic. As of August 2026, NIST also states that AI RMF 1.0 is being revised.

### 7. NIST AI 600-1 Generative AI Profile

Use the GenAI Profile to extend AI RMF practices for risks specific to or intensified by generative AI. Interview subjects include content integrity, confabulation, information security, privacy, harmful bias, intellectual-property considerations, human-AI configuration, misuse, model/system evaluation and lifecycle risk treatment.

### 8. Singapore AI governance

Singapore provides a practical bridge between governance principles and assurance/testing.

Interview focus:

- Model AI Governance Framework foundations.
- Model AI Governance Framework for Generative AI.
- AI Verify governance testing and process checks.
- Global AI assurance work.
- Model AI Governance Framework for Agentic AI.

The Agentic AI framework was launched on 22 January 2026 and updated in May 2026 with case studies and additional practices. Its four high-level dimensions are especially useful for interviews: bound agent risks and capabilities upfront; make humans meaningfully accountable; implement lifecycle technical controls/processes; and enable end-user responsibility through transparency and education.

### 9. OECD AI Principles

Use OECD principles for international interoperability and policy-level discussion. The principles were updated in 2024 to address developments including general-purpose and generative AI and associated concerns such as privacy, intellectual property, safety and information integrity.

### 10. Human-rights and ethics layer

Legal compliance is a floor, not the entire governance objective. Mature governance considers foreseeable effects on individuals and groups, fairness, dignity, accessibility, contestability, privacy, autonomy and societal impact alongside business value.

## Part III — Enterprise operating model

### 11. AI governance committee

A mature committee should have defined decision rights rather than merely advisory status. Typical representation:

- Executive/business owner.
- AI/data leadership.
- Cybersecurity.
- Privacy/data protection.
- Legal/regulatory compliance.
- Enterprise risk/model risk.
- Product/engineering.
- Procurement/third-party risk.
- Internal audit as an independent assurance function, not first-line owner.

### 12. Three-lines model

- **First line:** business, product, engineering and operational owners own AI use and risks.
- **Second line:** governance, risk, compliance, privacy, security and model-risk functions establish policy, challenge and oversight.
- **Third line:** internal audit independently assesses design and operating effectiveness.

### 13. AI inventory

Minimum useful inventory attributes include:

- System/use-case identifier.
- Business owner and technical owner.
- Purpose and users.
- Model/provider and version.
- Deployment geography.
- Data categories and sources.
- Regulatory classification.
- Risk tier.
- Autonomy/tool access.
- Human-oversight design.
- Validation status.
- Vendor dependencies.
- Monitoring metrics.
- Approval and exception records.
- Incident/change history.
- Retirement status.

### 14. Lifecycle gates

**Intake → Inventory → Classification → Risk/Impact Assessment → Design/Acquisition Controls → Validation → Approval → Deployment → Monitoring → Change/Incident Management → Revalidation → Retirement**

No high-impact use case should reach production solely because a model performs well technically.

## Part IV — GenAI and agentic AI

### 15. Generative AI control areas

- Prompt-injection and indirect prompt-injection resistance.
- Sensitive-data disclosure prevention.
- Retrieval and knowledge-source governance.
- RAG source quality, provenance and authorization.
- Hallucination/confabulation measurement and response.
- Content provenance and labelling when applicable.
- Copyright/IP and training/input/output considerations.
- Red teaming and adversarial testing.
- Guardrails and output validation.
- Human review for consequential outputs.

### 16. Agentic AI control areas

Agent governance must control **actions**, not only outputs.

Key controls include:

- Bounded scope and permitted objectives.
- Agent identity and authentication.
- Least-privilege authorization.
- Tool/API allowlists.
- Credential and secret isolation.
- Transaction and resource limits.
- Human approval checkpoints for consequential actions.
- Separation of duties.
- Memory/data-retention controls.
- Complete action/audit logs.
- Runtime monitoring and anomaly detection.
- Emergency disablement/kill capability.
- Multi-agent delegation and trust controls.
- Revalidation after capability, model, prompt, tool or data changes.

## Part V — Controls and evidence

### 17. Convert requirements into evidence

Use the chain:

**Requirement → Risk → Control Objective → Control Activity → Owner → Frequency/Trigger → Evidence → Test Procedure → Exception → Remediation → Residual-Risk Acceptance**

### 18. Evidence examples

- Inventory record.
- Classification decision.
- AI impact/risk assessment.
- DPIA or privacy assessment where applicable.
- Security threat model.
- Architecture/data-flow diagram.
- Dataset/model provenance record.
- Validation and red-team results.
- Human-oversight procedure.
- Approval record.
- Supplier due diligence.
- Contract/control clauses.
- Monitoring dashboards and KRIs.
- Incident/change records.
- Exception/risk-acceptance record.
- Internal-audit or independent-assurance evidence.

## Part VI — Senior Manager interview method

### 19. Answer architecture

For scenario questions, answer in this order:

**Business objective → Applicable obligations → Risk classification → Stakeholders/ownership → Controls → Evidence → Monitoring → Escalation → Business enablement.**

This keeps the answer executive-level while showing that governance can be operationalized.

### 20. Example executive response pattern

If asked how to govern a new enterprise AI use case:

> I would start with the business purpose and accountable owner, get the use case into the AI inventory, and classify it against regulatory, human-impact, security, privacy, autonomy and business-criticality criteria. The classification determines the depth of assessment and approval. I would then require proportionate controls—data and security review, impact assessment, testing and validation, human oversight, vendor due diligence where relevant, and documented residual-risk acceptance. Deployment is not the end of governance: we establish monitoring thresholds, change triggers, incident escalation and periodic revalidation, with evidence retained so the organization can demonstrate that the controls actually operated.

## Part VII — Rapid review checklist

Before an interview, be able to explain without notes:

- EU AI Act risk model and current 2026 enforcement timeline.
- ISO/IEC 42001 as a management-system approach.
- NIST AI RMF GOVERN/MAP/MEASURE/MANAGE.
- NIST AI 600-1 as the GenAI profile.
- Singapore MGF, AI Verify and Agentic AI governance.
- Difference between model governance, AI-system governance and agent governance.
- AI inventory and risk tiering.
- Impact assessment and human oversight.
- Third-party AI governance.
- GenAI/LLM security and privacy controls.
- Evidence and assurance.
- Monitoring, incident management and change/revalidation.
- How governance enables safe adoption rather than simply blocking AI.

## Publication gates

- [ ] Authoritative-source verification complete.
- [ ] Controlled-English substantive review complete.
- [ ] Legal/regulatory date check refreshed immediately before release.
- [ ] ISO copyright/licensed-source control verified.
- [ ] Cross-framework consistency review complete.
- [ ] Technical AI/security review complete.
- [ ] Interview-scenario QA complete.
- [ ] Accessibility review complete.
- [ ] Links checked.
- [ ] Localization terminology prepared.
- [ ] DOCX/PDF generation and visible-page QA complete if publication artifacts are produced.
- [ ] Release manifest/provenance/checksums prepared.
- [ ] Repository/workflow security QA complete.
- [ ] Required accountable-human release approval recorded.

## Source register

See `SOURCE_REGISTER.md`.
