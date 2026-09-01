# Manual 47 — EU AI Act Controlled Training Modules

**Controlled language:** English  
**Canonical stage:** 3 — controlled English master construction  
**Release boundary:** Training and operationalization; existing Manual 01 remains the detailed legal/compliance reference.

## Module 1 — Regulatory architecture and applicability

### Objective
Determine whether an AI use case falls within the material and territorial scope of Regulation (EU) 2024/1689 and identify the organization's relevant role or roles.

### Training points
- Start with intended purpose, system functionality, users, affected persons and deployment geography.
- Distinguish the regulated AI system from broader business processes and from underlying general-purpose models.
- Identify whether the organization acts as provider, deployer, importer, distributor, product manufacturer or another value-chain participant.
- Document multiple-role situations and material modifications that may change role allocation.
- Record exclusions, special regimes or other applicability limitations with primary-source support.

### Evidence outcome
A dated applicability and role determination tied to the inventory record and the specific system/model version.

## Module 2 — Prohibited-practice screening

### Objective
Prevent prohibited AI practices from entering procurement, development, approval or production.

### Training points
- Perform screening before risk-tier approval.
- Treat prohibited-practice analysis as a fail-closed gate.
- Capture business context, intended and reasonably foreseeable use, affected persons and operational design.
- Escalate ambiguity rather than converting legal uncertainty into an assumed approval.
- Re-screen when purpose, data, user population, functionality or deployment context materially changes.

### Evidence outcome
Completed prohibited-practice screen, disposition, rationale and escalation record where needed.

## Module 3 — AI literacy

### Objective
Operationalize role-appropriate AI literacy obligations rather than treating literacy as one generic awareness course.

### Training points
- Map competence expectations to governance, business, engineering, procurement, legal/compliance, security/privacy, oversight and operational roles.
- Address system limitations, foreseeable misuse, escalation, human oversight and relevant organizational policies.
- Use onboarding, role changes, material system changes and periodic refresh as training triggers.
- Retain audience mapping, curriculum version, completion and exception evidence.

### Evidence outcome
Role-based AI-literacy matrix and training record traceable to personnel responsibilities.

## Module 4 — Risk classification

### Objective
Classify systems accurately and connect classification to the correct legal and enterprise control path.

### Training points
- Distinguish prohibited uses, high-risk systems, transparency-triggering systems, GPAI obligations and lower-risk uses.
- Separate legal classification from the organization's own risk tier; both may apply simultaneously.
- Document the intended-purpose reasoning that supports the conclusion.
- Identify applicable Annex I or Annex III pathways when assessing high-risk status.
- Establish reclassification triggers for material changes.

### Evidence outcome
Classification worksheet, evidence references, reviewer/challenge record and reclassification triggers.

## Module 5 — High-risk AI risk management

### Objective
Integrate applicable high-risk risk-management duties into the organization's lifecycle governance.

### Training points
- Identify known and reasonably foreseeable risks across intended use and reasonably foreseeable misuse.
- Connect risk analysis to design controls, testing, human oversight, instructions, monitoring and incident processes.
- Evaluate residual risk after controls.
- Preserve evidence of iterative reassessment through the lifecycle.
- Do not treat a one-time project risk assessment as sufficient lifecycle risk management.

### Evidence outcome
Version-controlled risk file linking risks, controls, testing, residual-risk decisions and change triggers.

## Module 6 — Data and data governance

### Objective
Operationalize applicable data-governance requirements for high-risk AI and integrate them with enterprise data controls.

### Training points
- Establish provenance, collection/preparation practices, relevance, quality and documented limitations.
- Address representativeness and bias-related considerations where applicable to the use context.
- Maintain lineage from source through transformation and use.
- Protect access and integrity and define retention/correction processes.
- Separate AI Act obligations from additional privacy or sectoral data requirements while integrating execution where practical.

### Evidence outcome
Controlled data-governance record linked to system version and validation evidence.

## Module 7 — Technical documentation and traceability

### Objective
Make the regulated system reconstructable from controlled records.

### Training points
- Maintain current system description, architecture and component dependencies.
- Connect technical documentation to model/provider versions, data, testing, human oversight and monitoring.
- Preserve change history and configuration state.
- Keep documentation synchronized with production rather than only with pre-deployment design.

### Evidence outcome
Technical-documentation index with version linkage and controlled references.

## Module 8 — Logging and recordkeeping

### Objective
Provide traceability sufficient for monitoring, investigation, accountability and applicable legal duties.

### Training points
- Define events that must be logged and retained.
- Protect log integrity and access.
- Synchronize timestamps and identities where consequential actions require reconstruction.
- Ensure third-party systems provide the logs needed by the organization's role.
- Test whether a material event can actually be reconstructed.

### Evidence outcome
Logging specification, retention rule, sample reconstruction test and access-control record.

## Module 9 — Transparency and instructions for use

### Objective
Provide required information to downstream actors, users and affected persons in a manner that works in production.

### Training points
- Distinguish provider instructions from deployer-facing or end-user transparency duties.
- Treat Article 50 applicability as a separate determination.
- Test disclosures in the actual user experience.
- Where machine-readable marking or content labeling is applicable, verify technical operation and retention of evidence.
- Keep notices synchronized with system changes.

### Evidence outcome
Applicability determination, approved notice/instructions, production evidence and test record.

## Module 10 — Meaningful human oversight

### Objective
Design human oversight as an operational control rather than a nominal role assignment.

### Training points
- Define who is authorized and competent to intervene.
- Give reviewers the information and time needed to understand system outputs and limitations.
- Provide override, stop, escalation and safe-state mechanisms where applicable.
- Address automation bias and inappropriate reliance.
- Record significant interventions and overrides.

### Evidence outcome
Oversight procedure, authority matrix, competence record, functional intervention test and logs.

## Module 11 — Accuracy, robustness and cybersecurity

### Objective
Integrate applicable AI Act performance and resilience requirements with enterprise validation and cybersecurity.

### Training points
- Define measurable acceptance criteria appropriate to intended purpose.
- Evaluate robustness under expected variation and foreseeable misuse.
- Threat-model the full system including model endpoints, data, prompts, retrieval, tools, APIs and supply chain.
- Track vulnerabilities and unresolved findings to risk decisions.
- Revalidate after material security, model or environment change.

### Evidence outcome
Validation report, threat model, security test evidence, findings register and acceptance decision.

## Module 12 — Quality-management and conformity-related controls

### Objective
Understand where provider-side quality and conformity obligations become operational governance requirements.

### Training points
- Map policies, responsibilities, development controls, testing, documentation, supplier controls, corrective actions and records into a quality-management system where applicable.
- Determine the conformity-assessment path relevant to the system and role.
- Prevent enterprise governance labels from being represented as formal conformity evidence unless the required process was actually completed.
- Preserve the exact system identity to which assessments and declarations apply.

### Evidence outcome
Quality-system control map and conformity evidence register where applicable.

## Module 13 — Provider and deployer obligations

### Objective
Avoid role confusion across the AI value chain.

### Training points
- Build separate obligation matrices for provider and deployer responsibilities.
- Identify duties that depend on control over design versus operational use.
- Ensure procurement contracts provide documentation, logs, instructions, incident/change notification and cooperation required for the deployer's obligations.
- Reassess role allocation after material modifications, rebranding or changes to intended purpose.

### Evidence outcome
Role-specific responsibility matrix and contract/evidence map.

## Module 14 — General-purpose AI governance

### Objective
Operationalize obligations and dependencies associated with GPAI models without confusing model-level and system-level governance.

### Training points
- Identify whether the organization is a GPAI provider, downstream provider/developer or deployer/user of a system that incorporates GPAI.
- Maintain provider information and downstream documentation dependencies.
- Address applicable transparency and copyright-related requirements.
- Identify additional systemic-risk duties where applicable.
- Continue system-level risk, security, privacy and oversight governance even when the underlying model is third-party.

### Evidence outcome
GPAI role determination, documentation register, provider dependency record and system-level control map.

## Module 15 — Fundamental-rights impact assessment

### Objective
Complete a legally required FRIA where the trigger applies and integrate it with broader enterprise impact assessment.

### Training points
- Determine whether the FRIA obligation applies to the deployer/use context.
- Identify affected persons/groups and relevant rights impacts.
- Document safeguards, human oversight, complaint/contestability mechanisms and residual impact.
- Keep the FRIA aligned with intended use and material changes.
- Distinguish FRIA from privacy DPIA and enterprise AI risk assessment while coordinating evidence where appropriate.

### Evidence outcome
FRIA trigger analysis and completed assessment where required.

## Module 16 — Post-market monitoring

### Objective
Operate continuous monitoring that can detect changed risk, performance or compliance conditions after deployment.

### Training points
- Define performance and risk indicators, thresholds and escalation paths.
- Monitor misuse, drift, model/provider change, incidents, complaints and changing deployment context.
- Link monitoring to corrective action and revalidation.
- Ensure provider and deployer monitoring responsibilities are coordinated where applicable.

### Evidence outcome
Monitoring plan, dashboard/KRIs, threshold history, corrective actions and revalidation records.

## Module 17 — Serious incidents and regulatory escalation

### Objective
Detect, assess and escalate incidents consistently with applicable AI Act obligations and enterprise incident management.

### Training points
- Define intake criteria and severity assessment.
- Preserve logs, versions and decision evidence.
- Determine legal notification requirements and responsible party.
- Coordinate provider/deployer/vendor actions.
- Track remediation and safe return-to-service criteria.

### Evidence outcome
Incident record, legal/role assessment, notifications where required, remediation and revalidation evidence.

## Module 18 — Third-party and supply-chain governance

### Objective
Preserve accountable governance when AI capability or components are externally supplied.

### Training points
- Perform role-aware due diligence.
- Require documentation/instructions, security/privacy commitments, change notification, incident cooperation, evidence access and exit support.
- Evaluate subcontractor and model dependency chains.
- Track provider/model version changes that could affect classification or obligations.

### Evidence outcome
Due-diligence file, responsibility allocation, contract controls and ongoing-monitoring record.

## Module 19 — Governance evidence and assurance

### Objective
Make legal obligations testable through an evidence chain.

### Training pattern
**Legal requirement → organizational interpretation → control objective → control activity → owner → trigger/frequency → evidence → test method → exception → remediation → residual-risk decision**

### Evidence outcome
A control/evidence register capable of supporting management challenge, internal assurance and regulatory response.

## Module 20 — Implementation roadmap

### Objective
Translate the Act into a sequenced enterprise program rather than a one-time checklist.

### Recommended workstreams
1. inventory and applicability;
2. role mapping and classification;
3. prohibited-practice and AI-literacy controls;
4. high-risk/GPAI/transparency obligation mapping;
5. lifecycle control integration;
6. vendor/value-chain controls;
7. evidence and documentation architecture;
8. monitoring/incident/change management;
9. assurance and readiness testing;
10. regulatory-change management.

## Completion standard

A learner should be able to take an AI use case from inventory through EU AI Act scope/role determination, prohibited-practice screening, legal classification, obligation mapping, control/evidence design, approval, monitoring, incident/change management and revalidation while preserving the distinction between legal requirements and voluntary-framework alignment.
