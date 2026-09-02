# Manual 55 — Source and Control Architecture

**Controlled stage:** 1 — source qualification, lifecycle control mapping, evidence architecture, and scenario design  
**Date:** 2 September 2026

## Purpose
Establish a practical governance framework for AI third parties, vendors, foundation-model providers, hosted-model services, agents, plugins, tool providers, data suppliers, and other supply-chain dependencies. This manual distinguishes legal obligations, contractual commitments, supervisory expectations, voluntary frameworks, and community guidance rather than treating them as interchangeable.

## Control domains

### TP-01 — Provider inventory and materiality
Maintain a complete inventory of AI providers, services, models, APIs, agents, plugins, data sources, hosting dependencies, and fourth parties. Classify by business criticality, autonomy, data sensitivity, decision consequence, concentration risk, substitutability, and regulatory exposure.

### TP-02 — Pre-contract due diligence
Assess provider ownership, financial viability, security posture, privacy practices, AI governance, incident history, model/system documentation, hosting architecture, subcontractors, continuity, and evidence availability before approval.

### TP-03 — Security and technical assurance
Evaluate access control, tenant isolation, encryption, vulnerability management, secure development, model/API abuse controls, logging, monitoring, incident response, and independent assurance evidence proportionate to risk.

### TP-04 — Privacy and data-use restrictions
Document permitted data uses, training/fine-tuning use, retention, deletion, secondary use, cross-border processing, sensitive data restrictions, subprocessors, and evidence of deletion or return at exit.

### TP-05 — Model, version, and change transparency
Require identification of material model/service versions, significant architecture changes, deprecations, behavior changes, safety-control changes, and change-notification mechanisms sufficient to trigger internal revalidation.

### TP-06 — Subprocessors and fourth parties
Identify material fourth parties and dependencies supporting the AI service. Establish risk-based visibility, approval, notification, flow-down obligations, and exit/continuity controls.

### TP-07 — Hosting, residency, and transfer architecture
Map hosting regions, data locations, control planes, backups, failover, and transfer mechanisms. Validate stated residency commitments against technical and contractual evidence.

### TP-08 — Identity, authorization, and delegated action
For agents, plugins, connectors, MCP servers, and tool providers, validate identity, authorization scope, least privilege, delegated authority, transaction limits, revocation, and attributable action logging.

### TP-09 — AI supply-chain integrity
Assess model provenance, package/dependency integrity, artifacts, images, containers, libraries, model files, adapters, datasets, prompts, plugins, and update channels. Require controls against substitution, tampering, poisoning, and unauthorized changes.

### TP-10 — Contractual control and evidence rights
Establish clauses for security, privacy, AI-use restrictions, audit/evidence access, incident notification, material change, subcontractors, continuity, termination, data return/deletion, cooperation, and regulatory support where applicable.

### TP-11 — Performance and safety claims
Challenge material provider claims regarding accuracy, robustness, safety, fairness, privacy, security, certifications, and benchmark performance. Distinguish independently verified evidence from supplier assertions.

### TP-12 — Change and revalidation
Define events requiring reassessment: model/version change, new subprocessor, hosting change, control failure, security incident, data-use change, ownership change, financial distress, major benchmark regression, or new regulatory requirement.

### TP-13 — Incident and breach coordination
Define provider notification windows, evidence-sharing expectations, containment roles, customer communications, forensic cooperation, regulatory support, and post-incident corrective actions.

### TP-14 — Concentration and systemic dependency risk
Assess single-provider concentration, common cloud/foundation-model dependencies, shared libraries, common data providers, regional concentration, and correlated failure scenarios.

### TP-15 — Continuity, portability, and exit
Validate backup/restore, service continuity, alternate providers, data/model portability, export formats, migration procedures, credential revocation, data deletion, and residual dependency removal.

### TP-16 — Ongoing monitoring
Monitor provider risk signals, service changes, security advisories, regulatory actions, model/version changes, SLA degradation, incidents, evidence expirations, and unresolved findings.

### TP-17 — Exceptions and residual risk
Record approved deviations, rationale, compensating controls, accountable risk owner, expiration, review triggers, and closure evidence.

### TP-18 — Post-exit assurance
Confirm access removal, credential revocation, data return/deletion, model or adapter disposal where applicable, subprocessor termination effects, retention exceptions, and evidence preservation.

## Evidence catalogue
- EV-01 provider inventory and materiality record
- EV-02 due-diligence assessment
- EV-03 security/privacy evidence package
- EV-04 architecture and data-flow map
- EV-05 subprocessor/fourth-party register
- EV-06 model/version/change register
- EV-07 contract/control clause matrix
- EV-08 provider claims challenge record
- EV-09 incident/notification playbook
- EV-10 continuity and exit test
- EV-11 concentration-risk assessment
- EV-12 monitoring dashboard and review log
- EV-13 exception/residual-risk record
- EV-14 termination and deletion evidence

## Required scenarios
1. Hosted model provider silently changes model behavior.
2. A subprocessor begins processing data in a new region.
3. Provider terms begin permitting customer data for model improvement.
4. A plugin or agent tool gains broader permissions after an update.
5. A common dependency is compromised across several AI vendors.
6. A provider cannot substantiate a material safety or security claim.
7. A critical provider has a prolonged outage with no tested migration path.
8. A security incident requires coordinated containment and evidence preservation.
9. Exit is initiated but deletion evidence is incomplete.
10. Multiple critical AI services depend on the same foundation-model or cloud provider.

## Stage-1 completion criterion
Stage 1 is complete when each lifecycle control has qualified source relationships, evidence expectations, scenario coverage, ownership, escalation, change triggers, and exit requirements sufficient to build release-depth training architecture and localization.