# Manual 47 — EU AI Act Control and Evidence Workbook

**Purpose:** Convert applicable EU AI Act obligations into owned, testable enterprise controls without implying that a voluntary framework mapping proves legal compliance.

## Control pattern

**Legal requirement → organizational interpretation → risk → control objective → control activity → owner → trigger/frequency → evidence → test method → exception/escalation → remediation → residual-risk decision**

## Core workbook domains

### EUA-SCP-01 Scope and role determination
- Objective: document territorial/material scope and value-chain role(s).
- Evidence: applicability memo, entity/role map, intended-purpose record, legal interpretation references.
- Test: sample AI inventory entries and confirm role/scope conclusions are current and supported.

### EUA-PRH-01 Prohibited-practice screening
- Objective: prevent approval/deployment of prohibited AI practices.
- Evidence: screening record, escalation decision, prohibited-use controls, vendor representations.
- Test: verify every in-scope use case completed the screen before approval.

### EUA-LIT-01 AI literacy
- Objective: provide role-appropriate AI literacy for personnel dealing with AI systems.
- Evidence: curriculum, audience mapping, completion records, refresher triggers.
- Test: sample personnel by role and verify required training evidence.

### EUA-CLS-01 High-risk classification
- Objective: document whether a system is high-risk and why.
- Evidence: classification worksheet, Annex analysis, intended purpose, regulated-product linkage where relevant.
- Test: independently challenge selected classifications and verify change triggers.

### EUA-RSK-01 Risk management
- Objective: operate a lifecycle risk-management process for applicable high-risk AI.
- Evidence: risk register, foreseeable misuse analysis, controls, residual-risk decisions, revalidation records.
- Test: trace material risks to controls and evidence.

### EUA-DAT-01 Data and data governance
- Objective: govern datasets and data processes required by applicable obligations.
- Evidence: provenance, quality criteria, preparation records, representativeness analysis where relevant, lineage, access controls.
- Test: sample critical data elements and trace provenance and control operation.

### EUA-DOC-01 Technical documentation
- Objective: maintain required technical documentation and references to controlled source records.
- Evidence: documentation index, version history, architecture, model/system description, testing references.
- Test: confirm documentation corresponds to the deployed version.

### EUA-LOG-01 Recordkeeping and logging
- Objective: preserve required logs and traceability.
- Evidence: logging specification, retention settings, sample logs, access-control records.
- Test: reconstruct a sampled consequential event from logs.

### EUA-TRN-01 Transparency and instructions
- Objective: provide required information, instructions and disclosures.
- Evidence: instructions for use, Article 50 notices where applicable, UI captures, production tests, content marking evidence.
- Test: verify disclosures operate in production and match applicability determination.

### EUA-HUM-01 Human oversight
- Objective: ensure meaningful human oversight for applicable systems.
- Evidence: oversight procedure, role mapping, training, override/stop mechanisms, intervention logs.
- Test: demonstrate that an authorized human can understand, intervene and stop/escalate where required.

### EUA-ROB-01 Accuracy, robustness and cybersecurity
- Objective: maintain proportionate performance, robustness and security controls.
- Evidence: validation results, security testing, threat model, vulnerability findings, remediation, resilience tests.
- Test: verify acceptance thresholds and unresolved findings are governed.

### EUA-GPAI-01 GPAI governance
- Objective: identify and operate controls for applicable GPAI obligations and downstream dependencies.
- Evidence: provider documentation, model information, copyright-related policy evidence, systemic-risk analysis where applicable, downstream instructions.
- Test: verify obligations match the organization's role and current model/provider state.

### EUA-FRIA-01 Fundamental-rights impact assessment
- Objective: complete and retain an FRIA where legally required.
- Evidence: affected persons, impact analysis, safeguards, oversight, complaints/contestability, residual-risk decision.
- Test: confirm trigger analysis and completeness of required elements.

### EUA-PMM-01 Post-market monitoring
- Objective: monitor deployed AI for performance, misuse, incidents, changed context and regulatory change.
- Evidence: monitoring plan, KRIs, thresholds, alerts, review records, trend reports.
- Test: sample threshold breaches and trace response.

### EUA-INC-01 Serious incidents and regulatory escalation
- Objective: detect, assess, preserve evidence, escalate and notify as legally required.
- Evidence: incident taxonomy, response records, legal assessment, notifications, remediation, revalidation.
- Test: tabletop and sample incidents for timeliness and evidence completeness.

### EUA-TPR-01 Third-party/value-chain governance
- Objective: preserve role-appropriate accountability across providers, deployers, importers, distributors and subcontracted services.
- Evidence: due diligence, contracts, role mapping, change/incident notification clauses, assurance evidence, exit plan.
- Test: sample critical vendors and verify evidence access and responsibility allocation.

## Release boundary

This workbook operationalizes legal obligations for training and control design. Final publication must use current primary-law/Commission sources and must distinguish binding legal requirements from explanatory guidance and voluntary framework alignment.
