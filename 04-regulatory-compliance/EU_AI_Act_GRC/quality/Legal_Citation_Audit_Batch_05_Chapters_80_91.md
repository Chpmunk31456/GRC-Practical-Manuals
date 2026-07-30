# Legal and Citation Audit — Batch 05 (Chapters 80–91)

## Scope

This audit covers privacy, security, resilience, and technical-governance chapters 80–91 of the English master.

## Controlling source hierarchy

1. Regulation (EU) 2024/1689, as amended.
2. Current consolidated EUR-Lex text.
3. GDPR, NIS2, the Cyber Resilience Act, applicable product-safety and sector legislation.
4. Official European Commission, EDPB, ENISA, and EU AI Office guidance, identified as non-binding unless legally binding.
5. Recognised standards and technical frameworks, clearly distinguished from statutory requirements.

## Required corrections by chapter

### Chapter 80 — GDPR Integration

- State that AI Act compliance does not replace GDPR compliance.
- Require separate lawful-basis, transparency, purpose-limitation, minimisation, rights, security, DPIA, controller/processor, transfer, and retention analysis.
- Avoid treating AI Act role labels as equivalent to GDPR controller or processor roles.

### Chapter 81 — Privacy by Design and Data Minimisation

- Distinguish statutory GDPR requirements from recommended engineering patterns.
- Require necessity and proportionality, feature and field minimisation, retention limits, access controls, privacy-preserving testing, and change reassessment.

### Chapter 82 — Special-Category Data

- Require identification of Article 9 and Article 10 GDPR data and any applicable exception or legal basis.
- Distinguish legally permitted bias detection or correction processing under the AI Act from a general permission to process sensitive data.
- Require strict access, purpose, security, deletion, and documentation controls.

### Chapter 83 — Automated Decision-Making

- Separate GDPR Article 22 analysis from AI Act high-risk, transparency, and human-oversight duties.
- Do not imply that nominal human review defeats Article 22; require meaningful authority, competence, time, information, and ability to change the outcome.
- Correct graphics that misstate Article 10 data governance as Article 17 or imply a universal ten-year retention rule.

### Chapter 84 — Secure AI Development Lifecycle

- Distinguish Article 15 cybersecurity requirements for high-risk AI from broader recommended secure-development practices.
- Link security controls to intended purpose, threat model, system architecture, data and model supply chain, deployment environment, monitoring, and corrective action.

### Chapter 85 — Threat Modelling

- Treat threat modelling as a control method supporting legal requirements, not as a standalone statutory article requirement.
- Include misuse, adversarial manipulation, data poisoning, prompt injection, model extraction, privacy attacks, supply-chain compromise, dependency failure, and human-oversight bypass.

### Chapter 86 — Prompt Injection and Model Manipulation

- Avoid claiming that one technical mitigation eliminates the risk.
- Require layered controls for instruction hierarchy, input and output handling, retrieval boundaries, tool permissions, authentication, monitoring, testing, and incident response.

### Chapter 87 — Data Poisoning and Training-Data Risk

- Link provenance, integrity, quality, representativeness, contamination, malicious contribution, and update controls to Articles 9, 10, 15, technical documentation, and post-market monitoring where applicable.

### Chapter 88 — Model Extraction and Theft

- Distinguish confidentiality, intellectual-property, privacy, security, and systemic-risk concerns.
- Require access, rate, anomaly, credential, interface, watermarking or detection where appropriate, and incident controls without presenting any single technique as mandatory.

### Chapter 89 — Logging, Monitoring, and Vulnerability Management

- Reconcile Article 12 logging and deployer retention duties with GDPR minimisation, security, sector rules, and documented retention analysis.
- Do not state a universal retention period where the Act does not provide one for the specific record.
- Require vulnerability intake, triage, remediation, disclosure, version linkage, and corrective-action evidence.

### Chapter 90 — Business Continuity and Disaster Recovery

- Treat continuity and recovery as risk-proportionate controls supporting robustness, resilience, safety, deployer obligations, and sector law.
- Require fallback, safe-state, human alternatives, dependency failure, data and model restoration, recovery validation, communications, and evidence preservation.

### Chapter 91 — Red-Team and Penetration-Testing Governance

- Distinguish legally required testing for particular high-risk or systemic-risk contexts from recommended assurance activity.
- Require authorization, scope, safety, privacy, evidence handling, independence, remediation, retesting, and production-impact controls.

## Cross-chapter correction requirements

1. Clearly label legal requirements, recommended controls, and optional enhancements.
2. Do not collapse AI Act, GDPR, NIS2, CRA, product-safety, employment, and consumer-protection duties into a single compliance conclusion.
3. Maintain traceability from threat or legal requirement to control, owner, test, evidence, finding, and corrective action.
4. Use version-specific evidence for systems, models, datasets, prompts, retrieval sources, tools, and dependencies.
5. Reassess after material changes, incidents, vulnerabilities, supplier changes, new jurisdictions, or changed processing purposes.

## Graphics corrections

- Figure 83.13: Data Governance must reference Article 10, not Article 17.
- Figure 83.14: remove or qualify any universal ten-year retention statement.
- Figure 83.15: remove duplicate human-oversight treatment and correct language consistency.
- Reject the generic Chapters 80–91 composite poster from publication unless it is fully redrawn and legally revalidated.

## Closure criteria

Batch 05 closes only after Chapters 80–91, related appendices, and every associated figure pass legal-source, terminology, accessibility, and version-consistency review.