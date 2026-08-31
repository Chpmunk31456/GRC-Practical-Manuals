# Manuals 40–45 — Active Controlled-Build Architecture

Status: downstream build preparation. Publication order remains sequential. This file converts Manuals 40–45 from source-only prestage into an explicit build queue with target repositories, controlled-source architecture, candidate-generation expectations, and predecessor gates.

## Shared build contract
Every manual uses a 32-chapter controlled English master, then exact English freeze, controlled es-419 and pt-BR project localizations, structure/parity QA, reproducible DOCX/PDF candidate generation, nonblank/searchable PDF preflight, rendered/accessibility review, immutable SHA-256/byte provenance, exact-byte staging, staged-head QA, predecessor verification, workflow-security validation, and catalog/release-registry reconciliation. Copyrighted standards are paraphrased/originally operationalized and never presented as authorized translations.

## Manual 40 — CJIS Security Policy
**Target path:** `04-regulatory-compliance/CJIS_Security_Policy_Controlled_Implementation`
**Controlled baseline:** FBI CJIS Security Policy Version 6.1 dated June 25, 2026, subject to release-time re-verification.
**Predecessor:** Manual 39.

32-chapter controlled architecture:
01 purpose/source hierarchy; 02 applicability/CJI boundaries; 03 agency/CSA roles; 04 governance/accountability; 05 system/data inventory; 06 security-policy mapping; 07 personnel screening; 08 security awareness/training; 09 physical protection; 10 identity/account lifecycle; 11 advanced authentication/MFA; 12 privileged access; 13 least privilege/access control; 14 encryption in transit; 15 encryption at rest; 16 cryptographic/key governance; 17 logging/audit records; 18 monitoring/time synchronization; 19 media protection; 20 mobile/remote/wireless access; 21 network/security architecture; 22 vulnerability/patch/configuration management; 23 incident response/reporting; 24 cloud/service-provider governance; 25 outsourcing/security addendum/agreements; 26 backup/resilience/continuity; 27 data retention/disposal; 28 audits/assessments; 29 corrective actions/exceptions; 30 metrics/management review; 31 localization/provenance/release evidence; 32 implementation roadmap/reverification.

## Manual 41 — UK GDPR / Data Protection Act
**Target path:** `04-regulatory-compliance/UK_GDPR_Data_Protection_Act_Controlled_Implementation`
**Controlled baseline:** UK GDPR and Data Protection Act 2018 as amended by Data (Use and Access) Act 2025, with ICO guidance kept distinct from statutory text.
**Predecessor:** Manual 40.

32-chapter controlled architecture:
01 purpose/source hierarchy; 02 applicability/territorial scope; 03 controller/processor roles; 04 accountability/governance; 05 records of processing/data inventory; 06 lawful bases; 07 recognized legitimate interests/legitimate interests; 08 consent; 09 transparency/notices; 10 data minimization/purpose limitation; 11 accuracy; 12 retention/deletion; 13 security; 14 processors/contracts; 15 international transfers; 16 access rights; 17 rectification/erasure/restriction; 18 objection; 19 portability; 20 automated decision-making/profiling; 21 children/data subjects requiring special handling; 22 special-category/criminal-offence data; 23 DPIAs/high-risk processing; 24 breach response/notification; 25 complaints/regulator engagement; 26 PECR/cookies/electronic communications boundary; 27 research/statistics/public-interest overlays; 28 training; 29 assurance/audit; 30 metrics/management review; 31 localization/provenance; 32 release-time legislative re-verification.

## Manual 42 — Canada Privacy
**Target path:** `04-regulatory-compliance/Canada_Privacy_Controlled_Implementation`
**Controlled baseline:** PIPEDA remains the federal private-sector baseline, with provincial substantially-similar/private-sector laws, sector rules, and OPC guidance analyzed separately.
**Predecessor:** Manual 41.

32-chapter controlled architecture:
01 purpose/source hierarchy; 02 federal/provincial applicability; 03 accountability; 04 identifying purposes; 05 consent; 06 limiting collection; 07 limiting use/disclosure/retention; 08 accuracy; 09 safeguards; 10 openness; 11 individual access; 12 challenging compliance; 13 data inventory/flows; 14 processor/vendor governance; 15 cross-border processing; 16 breach risk assessment; 17 breach reporting/notification; 18 breach recordkeeping; 19 employee information; 20 children/youth; 21 biometrics; 22 marketing/analytics; 23 cloud/SaaS; 24 AI/automated processing; 25 rights-request operations; 26 provincial overlays; 27 retention/disposal; 28 training; 29 assurance; 30 metrics/management review; 31 localization/provenance; 32 release-time federal/provincial re-verification.

## Manual 43 — ISO/IEC 27017 & 27018 Cloud Security and Privacy
**Target path:** `06-cloud-and-technology-risk/ISO_IEC_27017_27018_Controlled_Implementation`
**Controlled baseline:** ISO/IEC 27017:2026 Edition 2 and ISO/IEC 27018:2025 Edition 3; only project-authored summaries and implementation guidance may be published.
**Predecessor:** Manual 42.

32-chapter controlled architecture:
01 source/copyright boundary; 02 scopes and standard relationships; 03 cloud service models; 04 customer/provider accountability; 05 shared responsibility; 06 information-security governance; 07 asset/configuration governance; 08 identity/access; 09 privileged cloud administration; 10 virtualized/shared environments; 11 administrative operations; 12 network/cloud architecture; 13 logging/monitoring; 14 cryptography/key management; 15 vulnerability/configuration management; 16 incident management; 17 resilience/availability; 18 portability/interoperability; 19 secure deletion/return; 20 supplier/subprocessor governance; 21 public-cloud PII processor scope; 22 customer instructions/purpose limits; 23 disclosure/transparency; 24 breach support; 25 data location/transfer considerations; 26 contractual controls; 27 evidence/auditability; 28 risk treatment; 29 crosswalks to 27001/27002/27701; 30 metrics/assurance limitations; 31 localization/provenance/copyright control; 32 edition-status reverification/release governance.

## Manual 44 — NIST SSDF / SP 800-218
**Target path:** `06-cloud-and-technology-risk/NIST_SSDF_SP_800-218_Controlled_Implementation`
**Controlled baseline:** NIST SP 800-218 SSDF v1.1 final; SP 800-218A final AI community profile; SP 800-218 Rev.1 / SSDF v1.2 remains draft unless reverified as final at release.
**Predecessor:** Manual 43.

32-chapter controlled architecture:
01 source/version hierarchy; 02 SSDF scope; 03 Prepare the Organization; 04 Protect the Software; 05 Produce Well-Secured Software; 06 Respond to Vulnerabilities; 07 governance/roles; 08 secure design; 09 threat modeling; 10 architecture review; 11 source control; 12 build integrity; 13 dependency governance; 14 SBOM/provenance; 15 secrets; 16 secure coding; 17 code review/static analysis; 18 dynamic/security testing; 19 CI/CD controls; 20 environment separation; 21 release integrity/signing/attestation; 22 vulnerability intake; 23 remediation/prioritization; 24 supplier assurance; 25 software acquisition; 26 incident feedback/lessons learned; 27 AI-development profile controls using 800-218A; 28 federal/acquisition overlay boundaries; 29 evidence/metrics; 30 exceptions/continual improvement; 31 localization/provenance; 32 draft-watch and release-time version re-verification.

## Manual 45 — Enterprise Compliance Training Capstone
**Target path:** `08-templates-and-tools/Enterprise_Compliance_Training_Capstone`
**Controlled baseline:** the exact published-state snapshot of Manuals 01–44 plus explicitly identified organizational policies, role requirements, legal/regulatory overlays, and evidence requirements. This is not an independent normative standard.
**Predecessor:** Manual 44.

32-chapter controlled architecture:
01 capstone purpose/source boundaries; 02 role-based learning paths; 03 applicability analysis; 04 governance decisions; 05 obligation-vs-control-vs-evidence reasoning; 06 risk assessment; 07 policy/control design; 08 evidence-quality scoring; 09 exception/risk acceptance; 10 privacy scenario; 11 AI governance scenario; 12 cybersecurity governance scenario; 13 cloud scenario; 14 OT/ICS scenario; 15 third-party scenario; 16 software supply-chain scenario; 17 incident-response scenario; 18 business-continuity scenario; 19 audit-readiness exercise; 20 regulatory-change exercise; 21 conflicting-framework analysis; 22 crosswalk limitations; 23 executive escalation; 24 regulator/auditor communication; 25 remediation/CAPA exercise; 26 metrics/dashboard exercise; 27 localization/jurisdiction scenario; 28 accessibility/inclusive training; 29 scored competency assessment; 30 answer rationales/remediation paths; 31 provenance/dependency snapshot; 32 integrated final simulation and release governance.

## Conveyor state after this architecture lands
- Manual 38: publication front — exact candidate provenance complete; next exact-candidate inspection/staging/reconciliation.
- Manual 39: active controlled trilingual build/candidate lane.
- Manual 40: next active English build.
- Manual 41: build-ready architecture.
- Manual 42: build-ready architecture.
- Manual 43: build-ready architecture with ISO copyright/source constraints recorded.
- Manual 44: build-ready architecture with final/draft NIST version boundary recorded.
- Manual 45: build-ready capstone architecture; final freeze waits for Manuals 01–44 publication-state snapshot.
