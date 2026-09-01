# Manual 50 — Practical Crosswalk Scenarios

**Canonical stage:** 4 — release-depth mapping and training construction  
**Currentness baseline:** 1 September 2026

These scenarios train practitioners to use a common-control architecture without collapsing distinct legal, standards, assurance, and governance regimes into false equivalence. Each scenario requires an evidence-based disposition, explicit source-specific limitations, and a reusable control/evidence strategy.

## Scenario 1 — Enterprise GenAI assistant deployed in the EU and Singapore

A multinational enterprise deploys a third-party GenAI assistant for internal knowledge search and drafting. The service uses retrieval-augmented generation over internal documents and is available to employees in the EU and Singapore.

### Required analysis

1. Identify the enterprise role, provider dependencies, intended purpose, affected data, and user population.
2. Apply GC-02 inventory, GC-03 role/value-chain responsibility, GC-05 risk/impact assessment, GC-06 data governance, GC-08 transparency, GC-11 documentation, GC-13 third-party governance, GC-14 monitoring, and GC-16 change management.
3. Map each common control separately to EU AI Act applicability, ISO/IEC 42001 management-system support, NIST AI RMF/AI 600-1 risk practices, Singapore governance guidance, and OECD principles.
4. Record where a shared enterprise artifact can be reused and where additional source-specific evidence is required.

### Expected evidence

AI inventory record; use-case owner; provider/model inventory; data-flow and RAG-source register; access-control design; risk assessment; prompt/output testing; user disclosure/training; vendor assessment; monitoring metrics; incident and change procedures.

### Anti-false-equivalence lesson

A single risk assessment can support several regimes, but it does not automatically satisfy actor-specific EU obligations, ISO certification requirements, NIST profile outcomes, or Singapore assurance expectations.

## Scenario 2 — High-impact hiring model with human review

An organization uses an AI model to rank job candidates. Human recruiters review the ranking before a final decision.

### Required analysis

- Determine applicable legal and internal risk classification rather than assuming that human review removes regulatory significance.
- Apply GC-04 risk classification, GC-05 impact assessment, GC-06 data governance, GC-08 transparency, GC-09 human oversight, GC-10 testing/validation, GC-12 approval gates, GC-14 monitoring, and GC-17 independent assurance.
- Define measurable evidence for fairness, performance, data quality, override effectiveness, automation-bias risk, and escalation.

### Decision questions

- What evidence proves that human oversight is meaningful rather than nominal?
- Which logs demonstrate overrides, disagreements, and escalation?
- Which jurisdiction-specific notices, rights, or legal assessments remain outside the generic crosswalk?

## Scenario 3 — Agentic finance assistant with tool access

A finance operations team pilots an agent that can read invoices, query ERP records, draft payment instructions, and invoke approved workflow tools.

### Required analysis

Apply GC-07 security/robustness, GC-09 human oversight, GC-13 third-party governance, GC-15 incident management, GC-16 change management, and GC-20 agent identity/autonomy/permissions/action provenance.

### Required controls

- unique workload/agent identity;
- least-privilege tool permissions;
- transaction-value and action-type approval thresholds;
- separation of read, draft, and execute privileges;
- tool-call allowlists and policy denials;
- complete action provenance;
- rollback/containment path;
- provider/model/version monitoring;
- periodic adversarial testing.

### Crosswalk lesson

Singapore agentic governance may provide a direct operating relationship for autonomy and accountability controls; NIST/AI 600-1 may provide strong risk-management support; EU and ISO relationships depend on applicable role, system context, and management-system scope. None of these relationships should be labeled equivalent without source-specific analysis.

## Scenario 4 — AI service provider changes the underlying model

A SaaS provider silently changes the foundation model used by a customer-facing AI feature. Performance improves, but safety behavior, latency, output style, and data-processing location may change.

### Required analysis

Use GC-03, GC-13, GC-14, GC-16, and GC-19 to determine whether the provider change is material and what revalidation is required.

### Evidence to collect

Provider change notice or release record; old/new model identity; benchmark deltas; security/safety regression tests; privacy/data-location assessment; revised risk assessment; approval decision; customer disclosure if applicable; updated inventory and documentation.

### Training objective

Practitioners must distinguish reusable change-management evidence from source-specific legal or assurance consequences.

## Scenario 5 — One audit package for multiple regimes

A company wants to create one annual AI assurance package for executives, auditors, customers, and regulators.

### Required analysis

Create an evidence bundle organized by GC-01 through GC-20, then classify every item as:

- reusable as-is;
- reusable with scope qualification;
- supporting only;
- insufficient without source-specific evidence;
- not applicable.

### Expected outcome

The package may contain a common inventory, governance charter, risk register, testing evidence, incident records, training records, vendor assessments, and monitoring reports. Separate source-specific annexes must preserve legal actor/scope analysis, certification/conformity evidence, jurisdiction-specific notices or filings, and assurance-method requirements.

## Scenario 6 — Board asks for a single “compliance percentage”

The board asks for one percentage showing how compliant the enterprise is across EU AI Act, ISO/IEC 42001, NIST AI RMF, Singapore governance, and OECD principles.

### Required response

Do not calculate a misleading universal percentage. Instead provide:

1. common-control implementation coverage;
2. evidence sufficiency by source;
3. source-specific obligation or objective gaps;
4. assurance/certification status where relevant;
5. unresolved legal-interpretation items;
6. material changes since last assessment.

### Training objective

A crosswalk is a decision-support system, not a mathematical proof of equivalence or compliance.

## Scenario disposition template

For every exercise, record:

- system/use case;
- owner and enterprise role;
- common controls triggered;
- source relationships and relationship type;
- shared evidence;
- source-specific additional evidence;
- gaps and risk;
- accountable decision;
- remediation owner/date;
- revalidation trigger.
