# Manual 55 — AI Third-Party Evidence and Assessment Workbook

**Controlled stage:** Stage 1 supporting work product  
**Date:** 2 September 2026

## Assessment record
For every material AI third party, record:
- provider/service/legal entity;
- business owner and technical owner;
- service purpose and affected processes;
- model/service/version identifiers where available;
- data categories and sensitivity;
- autonomy and delegated-action level;
- criticality/materiality tier;
- hosting/data regions;
- subprocessors/fourth parties;
- contractual renewal/termination dates;
- current residual-risk rating;
- last review and next review date.

## Evidence sufficiency scale
### E0 — assertion only
Supplier statement with no corroborating evidence.

### E1 — documented supplier evidence
Policies, architecture statements, model cards, security white papers, or questionnaires supplied by the provider.

### E2 — contractual or independently attested evidence
Contractual commitments, third-party assurance reports, certifications within their actual scope, test reports, or external assessments.

### E3 — customer-verifiable technical evidence
Logs, configuration evidence, reproducible tests, API behavior, control-plane settings, deletion confirmation, change telemetry, or other directly testable evidence.

No evidence level alone proves adequacy. Sufficiency depends on materiality, scope, currency, independence, and relevance.

## Provider assessment dimensions

### A. Governance and ownership
- accountable provider contacts;
- AI governance roles;
- policy and risk-management structure;
- escalation and incident contacts;
- evidence ownership and retention.

### B. Security
- identity/access control;
- tenant isolation;
- encryption and key-management responsibilities;
- vulnerability/patch management;
- secure development and dependency controls;
- logging/monitoring;
- incident detection/response;
- penetration/adversarial testing evidence where relevant.

### C. Privacy and data governance
- controller/processor or equivalent role allocation where applicable;
- permitted uses of prompts, inputs, outputs and uploaded data;
- training/fine-tuning/model-improvement use;
- retention and deletion;
- sensitive-data restrictions;
- cross-border processing and hosting;
- subprocessor transparency;
- rights/request support where applicable.

### D. Model and AI-system transparency
- model/service identity;
- versioning and change notice;
- intended use and limitations;
- performance/safety claims;
- evaluation evidence;
- human-oversight assumptions;
- agent/tool capabilities and boundaries.

### E. Agentic and delegated-action controls
- agent identity;
- tool/API permissions;
- least privilege;
- delegated authority;
- transaction/resource limits;
- approval thresholds;
- revocation and kill/containment capability;
- attributable logs.

### F. Supply-chain integrity
- software/model/data provenance;
- dependency management;
- model/package signing or integrity evidence where available;
- update channels;
- poisoning/tampering defenses;
- plugin/tool provenance;
- fourth-party dependencies.

### G. Continuity and concentration
- SLA/service dependency;
- backup/failover;
- portability;
- alternate-provider feasibility;
- shared infrastructure dependencies;
- regional or provider concentration;
- recovery objectives where relevant.

### H. Contract and evidence rights
- security/privacy/AI-use clauses;
- audit or assurance access;
- material-change notice;
- incident notice;
- subprocessor controls;
- cooperation obligations;
- termination/data-return/deletion;
- transition assistance;
- evidence preservation.

## Decision states
- APPROVE — evidence is sufficient for current materiality and residual risk.
- APPROVE WITH CONDITIONS — time-bound compensating controls or remediation are required.
- HOLD — material evidence gap or unresolved risk prevents approval.
- REJECT — risk cannot be reduced to accepted tolerance or required conditions are unavailable.
- REVALIDATE — material change or event requires renewed assessment.

## Mandatory change triggers
Reassess when there is a material model/version change, new subprocessor, hosting-region change, data-use change, incident, major control failure, ownership/financial change, new autonomous capability, expanded permissions, significant service degradation, critical vulnerability, regulatory action, or material contractual change.

## Exit checklist
- revoke credentials/tokens/keys;
- remove delegated permissions and integrations;
- export required records and data;
- verify return/deletion obligations;
- confirm subprocessor treatment;
- preserve required evidence and audit records;
- test replacement or continuity path;
- update inventory and concentration-risk records;
- document residual retention exceptions;
- complete post-exit assurance review.

## Stage-1 workbook criterion
This workbook is complete for Stage 1 when each material provider can be assessed using repeatable evidence levels, decision states, change triggers, and exit controls tied to TP-01 through TP-18.