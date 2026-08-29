# Manual 11 — GDPR Privacy and Data Protection Controlled Implementation
## Controlled English Source — Chapters 09–16

> Original implementation and training guidance for lawfulness, transparency, rights, and privacy-by-design. Context-specific legal judgment remains required.

## Chapter 09 — Lawful bases

Map each material processing purpose to a documented lawful basis and the facts supporting that choice. Record purpose, data categories, data subjects, decision owner, supporting evidence, alternatives considered, dependencies, and review triggers.

Do not treat lawful-basis selection as a dropdown choice. Contract necessity, legal obligation, vital interests, public task, legitimate interests, and consent each have distinct conditions and limitations.

## Chapter 10 — Consent and withdrawal

Where consent is used, design collection, evidence, granularity, transparency, voluntariness, withdrawal, and downstream system behavior so that consent can be demonstrated and revoked in practice.

Consent should not be relied upon where imbalance, bundling, ambiguity, or inability to withdraw would undermine validity.

## Chapter 11 — Legitimate interests and balancing

Where legitimate interests are considered, document the interest pursued, necessity, impact on individuals, reasonable expectations, safeguards, alternatives, objections, and residual risk. Reassess when purpose, technology, data, affected populations, or safeguards change.

Automated balancing templates may support consistency but do not replace legal/privacy judgment.

## Chapter 12 — Special-category and criminal-offence data

Identify processing involving special-category data or criminal-conviction/offence data and document the applicable additional legal condition, purpose, safeguards, access restrictions, retention, sharing rules, and specialist review.

High-sensitivity processing should be visible in the ROPA, DPIA screening, supplier review, security design, and incident response processes.

## Chapter 13 — Transparency and privacy notices

Provide clear, accessible, accurate information about identity, purposes, lawful bases, recipients, retention, rights, transfers, automated decision-making, and other required information according to context.

Notices should match actual processing. Material product, data-use, supplier, AI, or transfer changes should trigger notice-impact analysis.

## Chapter 14 — Data-subject rights operations

Implement controlled intake, identity/authority validation, right classification, search, processor coordination, exception review, response approval, timing, delivery, logging, and closure for applicable rights.

Maintain evidence of what systems and parties were searched, decisions made, limitations applied, deadlines, communications, and completion.

## Chapter 15 — Automated decision-making and profiling

Identify profiling and automated decision processes, determine whether legal restrictions or enhanced transparency apply, and document human involvement, decision significance, logic explanations where required, contestability, safeguards, bias/quality risks, and review.

AI-enabled decision support must not be labeled “human reviewed” merely because a person can theoretically intervene.

## Chapter 16 — Privacy by design/default and rights fail-closed gate

Embed privacy requirements into requirements, architecture, defaults, data collection, retention, access, testing, deployment, change management, and decommissioning. Defaults should support minimisation and purpose alignment rather than maximize collection or exposure.

Do not pass the gate when lawful basis is unsupported, notices materially diverge from actual processing, rights cannot be executed end-to-end, or high-impact automated decisions lack accountable review and safeguards.
