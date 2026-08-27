# Manual 04 — NIST AI 600-1 Generative AI Profile Implementation
## Controlled English Source — Chapters 17–24

> Original implementation guidance. The chapter set supports evidence-based GAI governance and does not reproduce NIST publication text.

## Chapter 17 — Evaluation strategy

Evaluation begins with a documented question: what must the system be able to do, what must it avoid doing, under what conditions, and with what confidence? The evaluation strategy should define objectives, scenarios, datasets, evaluators, methods, thresholds, sampling, limitations, and decision rules.

Evaluation should include representative normal use and plausible misuse. High-impact systems should use independent challenge or separation between builders and final release decision-makers.

## Chapter 18 — Test data and scenario governance

Test data should be traceable to purpose. Teams should record origin, coverage, sensitivity, transformation, representativeness, known limitations, and whether the data may be retained or shared.

Synthetic test data can improve coverage but should not be assumed to represent real-world populations or adversarial behavior. Where synthetic data is used, the evaluation record should state why it is appropriate and what blind spots remain.

## Chapter 19 — Acceptance thresholds and decision criteria

Thresholds should be set before final release testing where practical. They should reflect consequences, not convenience. A low-impact drafting assistant may tolerate different failure rates than a system influencing security, finance, health, employment, or safety decisions.

A release decision should record whether each threshold passed, failed, was conditionally accepted, or was waived. Waivers require rationale, owner, compensating control, expiration or review date, and residual-risk approval.

## Chapter 20 — Red teaming and adversarial evaluation

Adversarial evaluation should test whether controls remain effective when users or external content intentionally attempt to bypass them. Test cases should address direct prompt manipulation, indirect instructions, retrieval poisoning, tool abuse, identity or permission boundary failures, data extraction, system prompt disclosure, and unsafe action chaining when applicable.

Red-team results should be treated as evidence, not theater. Repeated tests with no remediation ownership or retesting should not be represented as assurance.

## Chapter 21 — Content provenance controls

Provenance should support practical questions: what model and configuration produced this output, what data or sources materially influenced it, what transformations occurred, and who or what approved subsequent use?

The organization should select provenance mechanisms proportional to risk. These may include source links, artifact hashes, model/version identifiers, prompt or policy versions, transformation logs, human approval records, or signed metadata.

Provenance improves traceability but does not prove factual accuracy or lawful origin by itself.

## Chapter 22 — Pre-deployment testing package

A pre-deployment evidence package should assemble the material needed for an accountable release decision. At minimum it should include:
- system/use-case inventory record;
- risk and impact register;
- evaluation plan and results;
- security/adversarial test results;
- privacy/data review where applicable;
- supplier/component evidence;
- unresolved findings and exceptions;
- monitoring thresholds;
- rollback/stop plan;
- approval record.

The package should be versioned and linked to the exact release candidate.

## Chapter 23 — Incident disclosure and escalation readiness

Before deployment, the organization should define what events qualify as a GAI incident, who must be informed, what evidence must be preserved, and when external notification or disclosure may be required.

Incident categories can include harmful output, data exposure, unauthorized action, control bypass, supplier failure, material misinformation, unexpected autonomy, regulatory or contractual breach, or repeated threshold violation.

Escalation criteria should be explicit enough that operators are not forced to invent severity rules during an event.

## Chapter 24 — Evidence sufficiency and review quality

Evidence should demonstrate that a control operated for the relevant system and period. Policies, screenshots, vendor claims, or questionnaires may support evidence but should not automatically be treated as proof of effectiveness.

Reviewers should consider relevance, reliability, completeness, timeliness, and independence of evidence. When evidence is weak or unavailable, the record should state that limitation and the resulting effect on residual risk or release confidence.