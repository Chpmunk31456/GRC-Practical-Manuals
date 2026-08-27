# Manual 05 — AI Auditing and Assurance
## Controlled English Source — Chapters 01–08

> Original audit implementation guidance. This material uses the controlled standards and AAIA professional-practice baseline without reproducing proprietary standard, training, or exam content. It does not itself constitute an audit opinion or certification.

## Chapter 01 — Audit mandate and objective

Every AI audit begins with a documented mandate. The mandate identifies who requested the work, why the audit is being performed, what decision the results will support, the authority of the audit team, and any restrictions on access or reporting.

The audit objective should be written as a testable statement. “Review AI governance” is too broad; “determine whether production AI systems above the organization’s high-risk threshold have approved owners, current risk assessments, release evidence, monitoring, and documented residual-risk acceptance” is auditable.

## Chapter 02 — Criteria and assurance boundary

Audit criteria must be identified before fieldwork. Criteria may come from law, regulation, contract, internal policy, approved standards, management commitments, control frameworks, or defined operating requirements.

The audit record must distinguish mandatory criteria from guidance and professional-practice references. ISACA AAIA is used here as a professional-practice reference for capability and audit-domain coverage; it is not law, regulation, an ISO standard, organizational certification, or an audit opinion.

## Chapter 03 — Scope and system boundary

The scope should identify the AI systems, business processes, legal entities, locations, environments, time period, suppliers, datasets, models, interfaces, and lifecycle stages included. Exclusions require rationale.

AI audits should decompose systems into relevant components: data, model, prompts, retrieval, tools, identities, infrastructure, monitoring, human review, suppliers, and change processes. A model-only scope may miss material risk in orchestration or downstream actions.

## Chapter 04 — Independence, competence, and conflicts

The audit lead should assess whether the team has sufficient independence and competence for the objective. High-impact technical testing may require security, privacy, data science, model-risk, legal, accessibility, safety, or domain specialists.

Conflicts should be disclosed when auditors designed, implemented, approved, or materially operated the control being evaluated. Where full organizational independence is impossible, the limitation and compensating review should be documented.

## Chapter 05 — Audit planning and risk prioritization

Planning should prioritize areas where control failure could create material harm or where evidence quality is uncertain. Inputs may include prior findings, incidents, risk registers, regulatory obligations, model criticality, data sensitivity, autonomy, supplier dependence, and recent changes.

The audit plan should state procedures, evidence sources, sampling approach, technical tests, interviews, responsible auditors, timing, and expected deliverables.

## Chapter 06 — Evidence strategy and sufficiency

Evidence must be relevant to the audit criterion and reliable enough to support the conclusion. Policies demonstrate design intent; they do not prove operation. Screenshots show a point in time; they may not prove sustained operation. Vendor assertions may support a conclusion but should be corroborated when supplier risk is material.

Evidence should be evaluated for relevance, reliability, completeness, timeliness, reproducibility where appropriate, and independence from the control owner.

## Chapter 07 — Sampling and population definition

Sampling starts by defining the population. Examples include all production AI systems, all high-risk use cases, all model releases in a period, all critical suppliers, or all incidents meeting a severity threshold.

The sampling method should reflect the audit objective and risk. Judgmental sampling may target high-risk items; statistical techniques may be appropriate for homogeneous populations. Sample limitations and untested portions of the population must be disclosed.

## Chapter 08 — Audit lifecycle and fail-closed quality gates

The controlled audit lifecycle is:
1. mandate and scope;
2. criteria and evidence plan;
3. fieldwork and testing;
4. findings and severity;
5. management response;
6. remediation validation;
7. closure and follow-up.

Quality gates fail closed when required evidence is unavailable, independence concerns are unresolved, testing is incomplete, reviewer comments remain open, material scope changes invalidate procedures, or a required human approval is missing.

Automated repository QA supports consistency of the manual package; it does not replace auditor judgment or human release approval.