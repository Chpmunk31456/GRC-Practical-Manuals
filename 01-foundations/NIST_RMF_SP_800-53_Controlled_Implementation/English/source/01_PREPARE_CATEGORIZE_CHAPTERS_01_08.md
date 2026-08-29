# Manual 10 — NIST RMF and SP 800-53 Controlled Implementation
## Controlled English Source — Chapters 01–08

> Original implementation guidance aligned to the NIST RMF and SP 800-53 ecosystem. This material does not reproduce NIST control text and does not authorize any system or certify compliance.

## Chapter 01 — RMF purpose and decision architecture

Use RMF as a risk-management operating cycle that connects mission objectives, system context, security and privacy risk, control implementation, assessment evidence, authorization decisions, and continuous monitoring. Avoid treating the framework as a one-time documentation exercise.

Define accountable roles, system boundaries, decision authorities, escalation routes, evidence expectations, and how organization-level and system-level risk decisions interact.

## Chapter 02 — PREPARE at the organization level

Establish organization-wide risk assumptions, governance, risk tolerance, common-control strategy, supply-chain expectations, enterprise architecture, shared services, assessment strategy, and monitoring strategy before individual systems are evaluated.

Evidence should show ownership, approved risk criteria, dependency assumptions, common-control providers, reusable evidence, and unresolved enterprise-level risks.

## Chapter 03 — PREPARE at the system level

Define the system mission, business owner, system owner, authorization boundary, operating environment, users, data, interfaces, dependencies, suppliers, inherited services, and expected lifecycle.

Document assumptions and unknowns explicitly. Boundary uncertainty, unclear ownership, or missing dependency information must remain visible as risk rather than being normalized away.

## Chapter 04 — Stakeholder and role accountability

Identify the authorizing official, risk executive function, system owner, information owner, control providers, assessors, security/privacy officers, architects, engineers, operations teams, legal/privacy participants, supply-chain stakeholders, and business representatives needed for the system.

Segregate implementation, assessment, and authorization responsibilities sufficiently to preserve credible challenge and decision accountability.

## Chapter 05 — Information and system characterization

Characterize information types, processing purpose, users, technologies, locations, interfaces, data flows, external connections, cloud or shared-service dependencies, operational technology where relevant, and supply-chain relationships.

The characterization should support both security and privacy analysis and be maintained as the system changes.

## Chapter 06 — CATEGORIZE security impact

Categorize the system using applicable impact-analysis methods and organizational policy. Record the rationale for confidentiality, integrity, and availability impact determinations, including mission consequences and dependencies.

The category is a decision input, not a substitute for threat, privacy, or business-risk analysis. Tailoring and risk decisions must remain traceable to context.

## Chapter 07 — Privacy and additional impact considerations

Integrate privacy risk, legal obligations, data sensitivity, mission harms, safety considerations, contractual requirements, supply-chain exposure, and other context that may require controls or protections beyond the initial security category.

Document where separate privacy analysis, risk assessment, or specialist review affects the control baseline or authorization package.

## Chapter 08 — PREPARE/CATEGORIZE fail-closed gate

Do not proceed as if the system is ready for control selection when the authorization boundary is unresolved, accountable ownership is missing, impact determinations are unsupported, critical dependencies are unknown, or organization-level assumptions conflict with system reality.

Automated checks may verify required records and relationships, but competent human judgment is required for categorization, scope, and accountability decisions.
