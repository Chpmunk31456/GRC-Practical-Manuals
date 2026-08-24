# Compliance Implementation Expansion Roadmap — 2026

## Purpose

This roadmap extends the GRC Practical Manuals collection with implementation-focused
guidance for major NIST publications, HIPAA, artificial intelligence governance and
auditing, ISO/IEC 42001, and vendor risk. The manuals remain free, beginner-friendly,
trilingual educational resources for organizations of any size.

Passing repository QA does not establish legal compliance, certification, or assurance.
Readers must obtain applicable official standards, verify current regulatory requirements,
and use qualified legal, audit, privacy, security, or certification professionals when needed.

## Scale without weakening accountability

Implementation guidance will use three proportional paths. The selected path depends on
AI or compliance risk, complexity, regulated status, data sensitivity, and third-party
dependency—not employee count alone.

1. **Essential:** named owner, scoped inventory, basic risk assessment, minimum policy,
   approval record, vendor review, evidence retention, and periodic monitoring.
2. **Structured:** formal committee, control library, impact assessments, documented
   testing, internal audit, remediation tracking, and executive metrics.
3. **Enhanced:** three-lines governance, continuous monitoring, independent assurance,
   technical validation, model-risk management, regulatory mapping, and certification
   readiness.

Every manual must explain what to implement, who owns it, the evidence to retain, how an
auditor tests it, and how each proportional path changes the implementation.

## Controlled workstreams

### NIST implementation series

- NIST CSF 2.0 and organizational profiles
- SP 800-30 risk assessments
- SP 800-37 RMF
- SP 800-53 and SP 800-53A controls and assessment
- SP 800-61 incident response
- SP 800-63 digital identity
- SP 800-82 operational technology security
- SP 800-115 security testing
- SP 800-137 continuous monitoring
- SP 800-160 secure systems engineering
- SP 800-161 cybersecurity supply-chain risk management
- SP 800-171, 800-171A, and 800-172 CUI protection and assessment
- SP 800-207 Zero Trust Architecture
- SP 800-218 Secure Software Development Framework
- NIST Privacy Framework

### AI governance, management, and auditing

- NIST AI RMF 1.0: Govern, Map, Measure, and Manage
- NIST AI 600-1 Generative AI Profile
- ISO/IEC 42001 AI management system implementation
- ISO/IEC 42005 AI system impact assessment
- ISO/IEC 42006 AIMS audit and certification readiness
- ISO/IEC 23894 AI risk management
- ISO/IEC 5338 AI system lifecycle processes
- ISO/IEC 27090 AI security threats and mitigations
- ISO 19011 management-system audit principles and programme management
- EU AI Act crosswalk and implementation linkage
- AI inventory, intake, approval, human oversight, monitoring, change, and incident response
- AI vendor, foundation-model, agent, RAG, and fourth-party assurance

The AI auditing manual will cover audit-universe development, audit criteria, independence,
competence, planning, sampling, design and operating effectiveness, data and model testing,
privacy, security, robustness, bias, transparency, human oversight, vendor risk, findings,
corrective action, and executive reporting.

### HIPAA implementation and audit series

- Applicability, covered entities, business associates, and subcontractors
- Privacy Rule implementation
- Security Rule administrative, physical, and technical safeguards
- Risk analysis and risk management
- Business associate agreements and vendor oversight
- Breach determination, notification, and incident response
- Cloud, SaaS, telehealth, and tracking-technology considerations
- Minimum necessary, access, de-identification, evidence, and audit readiness
- Clearly separated readiness guidance for proposed rules that are not current law

### Vendor-risk lifecycle series

- Inventory, ownership, criticality, and tiering
- Due diligence, evidence validation, and approval
- Contract, SLA, DPA, BAA, security, audit, and incident clauses
- Continuous monitoring and reassessment
- Fourth-party, concentration, geographic, cloud, SaaS, and AI-provider risk
- Software supply chain, SBOM, and open-source dependencies
- Incident management, exit, transition, data return, and destruction
- Metrics, exceptions, residual-risk acceptance, and board reporting

## Publication sequence

1. Verify authoritative sources and the applicable version.
2. Build the English master with original implementation guidance.
3. Complete technical, legal-status, editorial, accessibility, and evidence QA.
4. Create neutral Latin American Spanish and Brazilian Portuguese editions.
5. Complete terminology, link, artifact, and visual parity QA.
6. Merge through a reviewed pull request to protected `main`.
7. Run the release-package gate against the exact tagged commit.
8. Create the approved GitHub release for Zenodo archival and DOI assignment.

No workflow in this repository may push directly to `main` or publish a release without a
separate human-approved release action.
