# Manual 46 — Universal AI Governance Foundation

**Status:** CONTROLLED DEVELOPMENT  
**Version:** 0.1.0-draft  
**Controlled language:** English  
**Purpose:** Universal, jurisdiction-aware AI-governance training and operating model.

## 1. Purpose and scope

Manual 46 is the universal foundation for the AI-governance training series. It is intentionally independent of any single employer, jurisdiction, regulator, standard, industry, model family, cloud platform, or AI architecture.

It teaches the common governance system that an organization can use to govern predictive AI, machine learning, generative AI, foundation models, RAG systems, embedded AI, and agentic AI across the complete lifecycle.

Later manuals specialize this foundation. Manual 47 is the first specialist training and covers the EU AI Act.

## 2. Universal governance objective

AI governance is the system of decision rights, accountability, policies, processes, controls, evidence, oversight and assurance used to ensure that AI is selected, designed, acquired, developed, deployed, operated, changed and retired consistently with organizational objectives, risk appetite, law, security, privacy, data governance, human rights and stakeholder expectations.

The purpose is not to stop AI. The purpose is to make AI adoption demonstrably safe, lawful, controlled, useful and accountable.

## 3. Universal governance spine

**Accountability → Inventory → Classification → Risk/Impact Assessment → Data Governance → Security → Privacy → Human Oversight → Transparency → Testing/Validation → Documentation → Approval → Deployment → Monitoring → Incident/Change Management → Third-Party Governance → Evidence/Audit → Retirement → Continuous Improvement**

This spine is the common operating model for the entire series.

## 4. Core governance principles

1. **Accountability is explicit.** Every AI use case has an accountable business owner and identified technical ownership.
2. **Governance is risk-based.** Governance intensity increases with impact, autonomy, criticality, data sensitivity, scale, legal exposure and difficulty of reversal.
3. **Govern the system, not only the model.** Data, prompts, retrieval sources, tools, APIs, agents, humans, vendors, infrastructure and downstream actions are part of the governed system.
4. **Lifecycle governance begins before production.** Intake, classification and assessment precede approval.
5. **Human oversight must be meaningful.** A human reviewer needs competence, information, authority, time and a practical ability to intervene.
6. **Security and privacy are native AI-governance concerns.** They are not optional downstream reviews.
7. **Evidence is required.** An organization should be able to demonstrate what it decided, why, who approved it, what controls operated and how exceptions were handled.
8. **Third-party AI does not outsource accountability.** Providers may perform controls, but the adopting organization retains governance obligations appropriate to its role.
9. **Monitoring is continuous.** Drift, misuse, incidents, vendor changes, model changes, new tools, new data and regulatory changes can all trigger reassessment.
10. **Governance should enable responsible innovation.** Low-risk uses should not be burdened with controls designed for high-impact systems.

## 5. Roles and decision rights

A mature operating model distinguishes ownership, challenge and assurance.

### First line
Business, product, engineering and operational teams own the AI use case, business outcome and day-to-day risk.

### Second line
AI governance, enterprise risk, compliance, privacy, cybersecurity, data governance and model-risk functions establish policy, define control expectations, challenge decisions and monitor risk.

### Third line
Internal audit or another independent assurance function assesses governance design and operating effectiveness without owning first- or second-line controls.

### AI governance committee
The committee should have defined decision authority, escalation thresholds, quorum, conflict-of-interest handling and recorded decisions. Typical participation includes business leadership, AI/data, cybersecurity, privacy, legal/compliance, risk, product/engineering, procurement/third-party risk and, where appropriate, independent assurance observers.

## 6. AI inventory

An AI inventory is the control plane for governance. Minimum useful attributes include:

- unique system/use-case identifier;
- business and technical owners;
- intended purpose and users;
- model/provider/version;
- deployment geography and affected populations;
- model/system architecture;
- data categories and provenance;
- third-party dependencies;
- regulatory applicability;
- organizational risk tier;
- autonomy and tool/API access;
- human-oversight design;
- validation status;
- approval and exception records;
- monitoring metrics and thresholds;
- incident/change history;
- retirement status.

## 7. Classification and risk tiering

A universal classification process should consider at least:

- effect on health, safety, rights or access to essential opportunities/services;
- business criticality and financial exposure;
- autonomy and capacity to take consequential action;
- reversibility and availability of human intervention;
- personal, confidential, regulated or sensitive data;
- cybersecurity privilege and access to tools/systems;
- scale and number of affected users;
- external versus internal use;
- model/provider concentration risk;
- jurisdiction and regulatory classification;
- explainability and contestability requirements.

The classification result should determine assessment depth, required reviewers, validation rigor, approval authority and monitoring intensity.

## 8. Universal AI risk taxonomy

A practical enterprise taxonomy should cover:

- strategic and business risk;
- legal/regulatory risk;
- human-rights and societal impact;
- safety risk;
- model/performance risk;
- data quality and provenance risk;
- privacy risk;
- cybersecurity risk;
- misuse and abuse risk;
- bias/fairness risk;
- transparency/explainability risk;
- intellectual-property risk;
- third-party and supply-chain risk;
- operational resilience risk;
- agentic/autonomy risk;
- financial and fraud risk;
- reputational risk.

## 9. Lifecycle governance gates

**Intake → Inventory → Classification → Risk/Impact Assessment → Design/Acquisition Controls → Testing/Validation → Approval → Deployment → Monitoring → Change/Incident Management → Revalidation → Retirement**

A technical performance result alone is never sufficient approval evidence for a consequential AI system.

## 10. Data governance

AI governance should establish data lineage, lawful/authorized use, quality criteria, provenance, retention, minimization, access control, sensitive-data handling, training/evaluation separation where needed, RAG-source authorization and procedures for data correction or withdrawal.

## 11. Security governance

Security review should consider the full AI attack surface: model access, identity, APIs, secrets, training and inference pipelines, prompts, retrieval, plugins/tools, agent permissions, data exfiltration, model extraction, poisoning, prompt injection, indirect prompt injection, insecure output handling, supply-chain dependencies and monitoring.

## 12. Privacy governance

Privacy controls should address purpose, lawful basis or other applicable authorization, data minimization, sensitive data, retention, data-subject impacts, automated decision-making where relevant, cross-border flows, vendor processing and privacy impact assessment triggers.

## 13. Human oversight

Human oversight design should define:

- which decisions/actions require human review;
- who may approve or override;
- what information the reviewer receives;
- response-time requirements;
- escalation thresholds;
- mechanisms to stop or suspend the AI system;
- how override and intervention decisions are logged.

## 14. Testing, evaluation, verification and validation

Testing should be proportionate to risk and should address intended performance, foreseeable misuse, robustness, security, privacy, bias/fairness where relevant, explainability, data quality, edge cases, human factors, failure modes and residual risk.

Validation should be sufficiently independent from the development team for the risk level involved.

## 15. Generative-AI extensions

Generative AI adds control needs including:

- hallucination/confabulation evaluation;
- prompt and indirect-prompt injection controls;
- retrieval-source quality and authorization;
- sensitive-data leakage controls;
- output validation;
- content provenance/labeling where applicable;
- intellectual-property considerations;
- red teaming;
- guardrails and safe fallback behavior.

## 16. Agentic-AI extensions

Agent governance must control actions, not merely generated content. Key controls include:

- agent identity;
- bounded objectives;
- least-privilege authorization;
- tool/API allowlists;
- credential isolation;
- transaction/resource limits;
- human approval checkpoints;
- separation of duties;
- complete action logs;
- runtime anomaly detection;
- emergency disablement;
- multi-agent delegation controls;
- revalidation after changes to models, prompts, tools, permissions or data.

## 17. Third-party AI governance

Due diligence should evaluate provider governance, security, privacy, data-use terms, model limitations, subcontractors, change notification, incident notification, audit/assurance evidence, service continuity, exit strategy and contractual allocation of responsibilities.

## 18. Monitoring and continuous assurance

Monitoring should combine performance and risk indicators. Examples include drift, error rates, override rates, harmful-output rates, security events, policy exceptions, vendor changes, privacy events, unauthorized tool use, model/version changes, unresolved findings and overdue revalidation.

Threshold breaches should have predetermined escalation and response paths.

## 19. Incident and change management

An AI incident process should support detection, containment, evidence preservation, impact assessment, notification/escalation, remediation, lessons learned and revalidation.

Material changes to model, data, prompts, retrieval, tools, system purpose, user population, geography or autonomy should trigger formal change assessment.

## 20. Controls and evidence

Use the universal evidence chain:

**Requirement or Risk → Control Objective → Control Activity → Owner → Trigger/Frequency → Evidence → Test Procedure → Exception → Remediation → Residual-Risk Decision**

Useful evidence includes inventory records, classification decisions, impact assessments, threat models, data-flow diagrams, validation results, red-team reports, human-oversight procedures, approval records, vendor due diligence, contract clauses, monitoring dashboards, incident records, exception decisions and independent-assurance results.

## 21. Framework interoperability

Manual 46 is framework-neutral but compatible with major governance systems, including:

- EU AI Act;
- ISO/IEC 42001;
- NIST AI RMF and NIST AI 600-1;
- Singapore Model AI Governance Framework and AI Verify;
- OECD AI Principles;
- sector and jurisdiction-specific requirements.

Alignment to a voluntary framework does not, by itself, prove legal compliance or certification.

## 22. Training outcome

A learner completing Manual 46 should be able to:

1. establish an AI governance operating model;
2. design an AI inventory;
3. classify risk and autonomy;
4. run lifecycle risk and impact assessments;
5. establish control gates and approval authority;
6. govern GenAI and agentic AI extensions;
7. manage vendors and supply-chain risks;
8. design evidence and assurance;
9. monitor AI risk continuously; and
10. map the universal model to specialist legal and framework requirements.

## 23. Controlled series sequence

1. **Manual 46 — Universal AI Governance Foundation**
2. **Manual 47 — EU AI Act Training & Operationalization**
3. **Manual 48 — Singapore AI Governance**
4. **Manual 49 — NIST AI RMF + NIST AI 600-1**
5. **Manual 50 — Global AI Governance Crosswalk**
6. **Manual 51 — Agentic AI Governance, Security, Identity & Human Accountability**
7. Subsequent specialist manuals: GenAI/LLM risk, AI cybersecurity, privacy/data governance, model risk, third-party AI, operating model/RACI, lifecycle governance, classification, impact assessment, controls/evidence, monitoring, incidents, audit/assurance, OECD, UNESCO, executive scenarios and interview capstone.

## 24. Publication gates

- [ ] Authoritative-source verification complete.
- [ ] Controlled-English substantive review complete.
- [ ] Cross-framework consistency review complete.
- [ ] AI/security/privacy technical review complete.
- [ ] Copyright/licensed-source controls complete.
- [ ] Accessibility review complete.
- [ ] Localization terminology prepared.
- [ ] DOCX/PDF generation complete if publication artifacts are produced.
- [ ] Visible-page and text validation complete for every PDF.
- [ ] Release manifest/provenance/checksums complete.
- [ ] Repository/workflow security QA complete.
- [ ] Required accountable-human release approval recorded.

**Fail-closed rule:** Manual 46 remains controlled development until every applicable release gate is satisfied.