# Manual 46 — Universal AI Governance Foundation
## Practical Scenarios and Tabletop Exercises

**Status:** CONTROLLED DEVELOPMENT

These scenarios test whether the learner can apply the universal governance model without depending on one law, one standard or one vendor.

## Scenario 1 — Internal GenAI assistant
An enterprise introduces a generative-AI assistant for employees. It can summarize documents, draft responses and answer questions using internal knowledge.

Required analysis: inventory and ownership; data classification; prompt and retrieval controls; privacy/confidentiality risk; output validation; access control; monitoring; vendor/provider obligations; acceptable-use controls; incident escalation.

Minimum evidence: approved use-case record; data-flow diagram; security/privacy assessment; RAG source approval; acceptable-use policy; validation results; monitoring design; approval record.

## Scenario 2 — Customer-facing AI decision support
A customer-facing AI system recommends products or services that materially affect customer outcomes.

Required analysis: consequential impact; explainability and contestability; bias/fairness where relevant; human oversight; model validation; customer transparency; complaint handling; change/revalidation triggers.

Governance decision: determine whether the system can operate autonomously, requires human review, or should remain advisory only.

## Scenario 3 — HR screening tool
A third-party AI service ranks applicants for employment decisions.

Required analysis: affected population; vendor governance; data provenance; discrimination/fairness risk; human oversight; transparency; legal applicability screening; validation independence; evidence retained for decisions and challenges.

Key lesson: a vendor assurance statement does not replace the deploying organization’s own risk assessment and governance obligations.

## Scenario 4 — RAG over sensitive enterprise records
A RAG application retrieves information from internal legal, financial, HR and customer repositories.

Required analysis: repository authorization; least-privilege retrieval; row/document-level permissions; embeddings/vector-store controls; source freshness; data leakage; prompt injection; logging; source attribution; retention; incident containment.

## Scenario 5 — Autonomous service agent
An AI agent may read customer records, create tickets, modify account attributes and initiate limited financial adjustments.

Required analysis: agent identity; authentication; authorization; bounded purpose; tool allowlists; transaction limits; human approval checkpoints; separation of duties; action provenance; runtime anomaly detection; emergency stop; incident forensics; revalidation after permission/tool changes.

Critical question: what can the agent do that a human would normally need explicit authority to do?

## Scenario 6 — AI coding assistant
Developers use an AI coding assistant with repository context and code-generation capability.

Required analysis: source-code confidentiality; dependency risk; insecure code generation; secrets exposure; license/IP issues; code review; security testing; generated-code provenance; privileged repository access; model/provider data use.

## Scenario 7 — High-volume low-impact automation
An AI classifier routes routine internal support tickets.

Required analysis: risk proportionality; operational resilience; false routing; monitoring; change controls; data sensitivity.

Key lesson: universal governance should not impose high-impact controls on low-impact use cases without justification.

## Scenario 8 — Material vendor model change
A cloud AI provider changes the underlying model version used by a production application.

Required analysis: contractual notification; change materiality; regression testing; risk reassessment; validation scope; user impact; rollback; approval; evidence.

## Scenario 9 — AI incident
A production assistant discloses confidential information and logs show repeated indirect prompt-injection attempts.

Tabletop response: detect; contain; preserve evidence; determine affected data/users; disable risky integrations if needed; assess legal/regulatory notification requirements; remediate; test; revalidate; document lessons learned; update threat model and controls.

## Scenario 10 — Board challenge
The board asks: “Where are we taking the most AI risk, and how do we know controls are working?”

A strong response must synthesize inventory, risk tier, exceptions, validation status, incidents, vendor concentration, KRIs, overdue remediation and residual-risk decisions rather than reporting model counts alone.

## Scoring rubric
For each scenario, score 0–2 on each dimension:
1. accountable ownership;
2. inventory/system boundary;
3. classification;
4. risk/impact assessment;
5. security/privacy/data controls;
6. human oversight;
7. testing/validation;
8. approval/evidence;
9. monitoring/change;
10. incident/escalation.

Maximum score: 20. A score below 14 indicates material gaps in operational governance reasoning.