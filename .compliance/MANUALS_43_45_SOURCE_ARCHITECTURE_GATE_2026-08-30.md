# Manuals 43–45 — Authoritative Source and Architecture Gate

Status: downstream controlled preparation only. Publication state is unchanged. Manuals 43–45 remain sequentially behind Manual 42, and all existing source, localization, accessibility, provenance, workflow-security, artifact, substantive-review, predecessor, and final reconciliation gates remain fail-closed.

## Manual 43 — ISO/IEC 27017 & ISO/IEC 27018 Cloud Security and Privacy

### Current authoritative baseline

- ISO/IEC 27017:2026, Edition 2, published July 2026, is the current ISO cloud-security control guidance baseline. ISO identifies ISO/IEC 27017:2015 as withdrawn.
- ISO/IEC 27018:2025, Edition 3, published August 2025, is the current ISO public-cloud PII processor privacy baseline. ISO identifies ISO/IEC 27018:2019 as withdrawn.
- Both standards build on ISO/IEC 27002. Manual 43 must distinguish ISO/IEC 27017 customer/provider cloud-security responsibility guidance from ISO/IEC 27018 public-cloud PII-processor privacy guidance.

### Source and copyright boundary

- ISO catalogue/public metadata may establish edition, date, lifecycle state, scope, and relationship metadata.
- The manual must not reproduce protected ISO normative text beyond lawful quotation limits or imply that project-localized text is an ISO-authorized translation.
- Exact clause/control mappings require access to lawfully obtained source material and must remain evidence-linked rather than reconstructed from secondary summaries.
- Certification, contractual, regulator, provider, and customer requirements must be labeled separately from ISO implementation guidance.

### Controlled architecture

The controlled English master must cover: scope and applicability; cloud service models; cloud customer/provider accountability; shared-responsibility mapping; asset and configuration governance; identity and privileged access; virtualized and shared environments; administrative operations; cloud monitoring/logging; incident management; portability/deletion; supplier and subprocessor governance; public-cloud PII processor scope; customer instructions; disclosure and transparency; data-return/deletion; breach support; location/transfer considerations; evidence and auditability; risk treatment; contractual controls; crosswalks to ISO/IEC 27001/27002/27701; implementation examples; control ownership; metrics; assurance limitations; localization notes; accessibility; provenance; change management; and release governance.

### Next gate

Build the controlled 32-chapter English master only after exact ISO source identities and any required licensed-source evidence are recorded. Freeze English before es-419 and pt-BR project localization.

## Manual 44 — NIST SSDF / SP 800-218

### Current authoritative baseline

- NIST SP 800-218, Secure Software Development Framework (SSDF) Version 1.1, published February 2022, remains the current final SSDF baseline.
- NIST SP 800-218 Rev. 1, SSDF Version 1.2, released December 17, 2025, is an Initial Public Draft; its public comment period closed January 30, 2026. It must not be treated as final unless NIST publishes a final revision.
- NIST SP 800-218A, published July 2024, is a final SSDF Community Profile for generative AI and dual-use foundation models and augments SSDF 1.1 rather than replacing it.

### Source boundary

Manual 44 must distinguish final NIST publications from draft revisions, federal acquisition/contractual overlays, CISA/OMB requirements, organization-specific SDLC policy, and third-party secure-development frameworks. Draft SSDF 1.2 content may be tracked as change-watch material but must not silently replace Version 1.1 controls.

### Controlled architecture

The controlled English master must cover: Prepare the Organization; Protect the Software; Produce Well-Secured Software; Respond to Vulnerabilities; governance; secure design; threat modeling; architecture review; source/code control; build integrity; dependency governance; SBOM/provenance; secrets; testing; vulnerability intake; remediation; release integrity; signing/attestation; supplier assurance; software acquisition; CI/CD controls; environment separation; metrics; evidence; exception governance; AI-development considerations using SP 800-218A where applicable; federal-overlay boundaries; incident feedback; continuous improvement; crosswalks; localization; accessibility; provenance; change monitoring; and release governance.

### Next gate

Build against SP 800-218 Version 1.1 as the final baseline, with SP 800-218 Rev. 1 Version 1.2 held in explicit draft/change-watch status until NIST finalizes it.

## Manual 45 — Enterprise Compliance Training Capstone

### Controlled source model

Manual 45 is an integration and competency manual, not an independent legal or certification authority. Its source universe is the verified source/provenance set of Manuals 01–44 plus current project controls. It must never assert that a crosswalk proves legal equivalence, certification equivalence, audit sufficiency, or regulator acceptance.

### Controlled architecture

The 32-chapter capstone must integrate role-based scenarios; governance decisions; applicability analysis; control/evidence selection; risk acceptance; third-party governance; AI governance; privacy; security engineering; incident response; OT/ICS; cloud; software supply chain; audit preparation; evidence-quality scoring; conflicting-framework analysis; crosswalk limitations; escalation; exceptions; executive reporting; regulator/auditor communication; localization scenarios; accessibility; provenance; change monitoring; practical exercises; scored competency assessments; answer rationales; remediation paths; and final integrated simulations.

### Assessment boundary

- Training scores demonstrate project-defined competency only.
- Completion must not be represented as ISO, ISACA, CSA, NIST, regulator, or other third-party certification.
- Scenario answers must preserve jurisdiction, scope, source-date, and framework-boundary context.
- Any legal conclusion requiring licensed counsel or regulator interpretation must be framed as an escalation exercise, not as definitive legal advice.

## Shared downstream controls

For Manuals 43–45: authoritative-source re-verification at English freeze; human-review competency preflight before candidate generation; exact English identity; controlled es-419 and pt-BR localization; structure/parity QA; reproducible DOCX/PDF candidates; rendered/accessibility inspection; provenance/checksums; workflow-security checks; durable staging; predecessor publication; exact-hash substantive review where repository controls require it; and final catalog/release-registry reconciliation remain mandatory.