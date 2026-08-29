# Manual 08 — Vendor and Third-Party Risk Lifecycle
## Controlled English Source — Chapters 01–08

> Original third-party-risk implementation guidance. This material operationalizes the controlled source baseline without reproducing standards text and does not certify any supplier or eliminate supplier risk.

## Chapter 01 — TPRM objective and lifecycle

Third-party risk management should govern the full relationship lifecycle: intake, classification, due diligence, risk decision, contracting, onboarding, monitoring, issue/change management, reassessment, and offboarding.

The process should apply proportionally based on what the supplier can access, influence, process, host, operate, or disrupt.

## Chapter 02 — Vendor inventory and ownership

Maintain a controlled inventory of suppliers, service providers, subprocessors, AI/model providers, data providers, APIs, hosting services, and other material external dependencies.

Each record should identify the business owner, service, data handled, system dependencies, contract, criticality, geography where relevant, fourth-party exposure, renewal date, monitoring tier, and exit requirements.

## Chapter 03 — Criticality and inherent risk

Criticality asks what happens if the supplier fails; inherent risk asks what exposure exists before considering controls. These are related but not identical.

Factors may include sensitive-data access, privileged connectivity, production access, operational dependency, concentration, substitutability, financial impact, regulatory exposure, AI autonomy, model or data dependency, and business-continuity consequences.

## Chapter 04 — Due diligence planning

Due diligence should be evidence-based and proportional. The review plan should identify the questions to answer, evidence needed, reviewers, and acceptance thresholds.

Potential evidence includes policies, independent reports, certifications, architecture information, test results, incident history, resilience evidence, privacy documentation, contractual commitments, financial information, and targeted interviews.

A questionnaire alone is not assurance for a material supplier.

## Chapter 05 — Security, privacy, and resilience review

Review should determine whether supplier controls are appropriate to the service and exposure. Security, privacy, and resilience should be assessed as connected disciplines rather than isolated questionnaires.

The review should address identity, access, data protection, logging, vulnerability management, incident response, recovery capability, subcontracting, location, retention, deletion, and service continuity where applicable.

## Chapter 06 — AI suppliers and model/component dependencies

AI supplier review should identify model providers, hosted inference, fine-tuning services, data suppliers, safety services, retrieval sources, agent/tool providers, and other AI components.

Key questions include data use, training or retention behavior, model/version change notification, security boundaries, content and abuse controls, service availability, intellectual-property terms, audit evidence, incident notification, and exit options.

## Chapter 07 — Risk decision and exceptions

Every material due-diligence outcome should produce a decision: approve, conditionally approve, require remediation, restrict scope, defer, or reject.

Exceptions should record the unmet requirement, business justification, compensating control, owner, residual risk, approver, expiration date, and monitoring requirement. Permanent exceptions without periodic review should be avoided.

## Chapter 08 — Fail-closed onboarding gate

Onboarding should fail closed when required due diligence is incomplete, critical evidence is missing, high-risk findings lack approved treatment, required contract terms are unresolved, or mandatory human approval is absent.

A supplier may not be represented as “approved” merely because procurement is complete. Material change after approval—such as a new subprocessor, service model, data use, AI component, hosting location, or security architecture—can reopen the affected review gate.