# Legal and Citation Audit — Batch 02

**Scope:** Chapters 36–52 — high-risk AI-system requirements, conformity, registration, fundamental-rights impact assessment, monitoring, incidents, corrective action, and substantial modification.

**Review status:** Initial authoritative-source review completed. Direct chapter consolidation and second-pass closure remain required.

## Authoritative source baseline

1. Regulation (EU) 2024/1689, as amended.
2. Regulation (EU) 2026/1744, Digital Omnibus on AI.
3. Current consolidated EUR-Lex text.
4. European Commission high-risk classification guidance, labelled draft and non-binding until final adoption.
5. Future Commission guidance on high-risk obligations, serious incidents, fundamental-rights impact assessments, post-market monitoring, value-chain responsibilities, and substantial modification.

## Controlling application-date rule

Regulation (EU) 2026/1744 amended Article 113. Chapter III, Sections 1, 2 and 3, except Article 6(5), apply:

- from **2 December 2027** for systems classified as high-risk under Article 6(2) and Annex III;
- from **2 August 2028** for systems classified as high-risk under Article 6(1) and Annex I.

These dates must not be generalized to every AI Act obligation. Chapters 36–52 must distinguish the delayed provisions from independently applicable governance, transparency, enforcement, transitional, and sector-specific requirements.

## Chapter-level findings and required corrections

### Chapter 36 — High-risk quality-management system

- Map the provider quality-management system to Article 17.
- Distinguish mandatory system elements from optional implementation methods.
- Include governance, regulatory strategy, design controls, testing, data governance, technical documentation, recordkeeping, risk management, post-market monitoring, incident reporting, corrective action, and accountability.
- Avoid implying that ISO/IEC 42001 certification automatically proves AI Act conformity.

### Chapter 37 — Continuous risk management

- Cite Article 9.
- Preserve the continuous, iterative, lifecycle requirement.
- Cover intended use, reasonably foreseeable misuse, post-market information, residual risk, testing, children where relevant, and risk-control verification.
- Distinguish provider risk management from the deployer’s operational-risk duties.

### Chapter 38 — Data and data governance

- Cite Article 10.
- Limit legal claims to training, validation, and testing data requirements applicable to the relevant system.
- Cover relevance, representativeness, completeness, error assessment, statistical properties, geographical/contextual suitability, bias examination, data provenance, and governance practices.
- Do not treat Article 10 as a general authorization to process personal or special-category data; GDPR analysis remains separate.

### Chapter 39 — Technical documentation

- Cite Article 11 and Annex IV.
- Require documentation before market placement or putting into service and continuous updating.
- Separate statutory Annex IV content from recommended artifacts such as model cards or system cards.
- Require version traceability and change history.

### Chapter 40 — Logs and recordkeeping

- Cite Articles 12, 19 and applicable deployer recordkeeping duties.
- Distinguish system capability to generate logs from operator retention duties.
- Avoid a universal ten-year retention claim. Retention depends on the applicable provision, actor, system, sector, evidence purpose, and other law.

### Chapter 41 — Transparency and instructions for use

- Cite Article 13.
- Require concise, complete, correct, clear, relevant, accessible, and comprehensible instructions.
- Cover intended purpose, performance characteristics, limitations, foreseeable misuse, human oversight, input specifications, logging, maintenance, and cybersecurity where applicable.

### Chapter 42 — Human oversight

- Cite Article 14.
- Preserve the objectives of preventing or minimizing risks to health, safety, and fundamental rights.
- Require competent, trained, authorized overseers with sufficient authority, information, time, tools, and escalation routes.
- Distinguish meaningful oversight from nominal human presence or rubber-stamping.

### Chapter 43 — Accuracy, robustness, cybersecurity, and resilience

- Cite Article 15.
- Require appropriate levels throughout the lifecycle.
- Address error tolerance, feedback loops, model or data poisoning, adversarial manipulation, confidentiality/integrity/availability, and resilience to faults or inconsistencies.
- Avoid claiming that a single penetration test establishes compliance.

### Chapter 44 — Conformity assessment

- Cite Article 43 and applicable annexes.
- Distinguish internal-control assessment from notified-body involvement.
- Reassess after substantial modification where required.
- Treat harmonised standards and common specifications as conformity-support mechanisms, not automatic substitutes for the statutory assessment.
- Account for sector-specific conformity pathways and the amended treatment of certain Annex I products.

### Chapter 45 — EU declaration of conformity and CE marking

- Cite Articles 47 and 48 and the relevant annex.
- Require an EU declaration of conformity for the applicable high-risk AI system and retention/update controls.
- Explain that CE marking indicates conformity with applicable Union harmonisation requirements; it is not a general endorsement of quality or ethical superiority.

### Chapter 46 — Registration

- Cite Article 49 and the EU database provisions.
- Distinguish provider and deployer registration duties and applicable exceptions or restricted-access entries.
- Require reconciliation between the AI inventory, legal classification, conformity package, and database record.

### Chapter 47 — Fundamental-rights impact assessment

- Cite Article 27.
- Identify the deployers and circumstances to which the statutory FRIA applies.
- Distinguish the mandatory Article 27 assessment from a broader voluntary good-practice assessment.
- Cover processes, period/frequency, affected persons and groups, risks, human oversight, mitigation, governance, and notification requirements.
- Coordinate but do not conflate the FRIA with a GDPR DPIA.

### Chapter 48 — DPIA coordination

- Cite GDPR Article 35 and relevant AI Act coordination language.
- Explain that the AI Act does not replace GDPR legal-basis, transparency, rights, security, international-transfer, or automated-decision requirements.
- Permit a coordinated workflow while retaining separately traceable conclusions and approvals.

### Chapter 49 — Post-market monitoring

- Cite Article 72.
- Require a documented, proportionate, lifecycle post-market monitoring system and plan.
- Include active and systematic collection, documentation, and analysis of performance and compliance data.
- Link monitoring to risk management, incidents, corrective action, technical-documentation updates, and change assessment.

### Chapter 50 — Serious-incident reporting

- Cite Article 73 and current definitions.
- Distinguish serious incidents from ordinary defects, complaints, security events, and near misses.
- Avoid universal reporting deadlines without checking the precise event, actor, knowledge point, and applicable provision.
- Future Commission incident guidance must be labelled non-binding unless formally adopted.

### Chapter 51 — Corrective action, withdrawal, and recall

- Cite the applicable provider/operator obligations, including Articles 20 and 21 where relevant.
- Require evaluation, containment, correction, withdrawal, disablement, recall, downstream communication, authority cooperation, and effectiveness verification.
- Preserve legal hold and evidence before destructive remediation where appropriate.

### Chapter 52 — Change management and substantial modification

- Cite Article 25 and the definition of substantial modification.
- Require assessment of changes to intended purpose, architecture, model, data, thresholds, integrations, geography, affected population, or performance.
- Identify when another actor becomes the provider.
- Distinguish ordinary maintenance from changes that affect compliance or intended purpose.
- Future Commission guidance must be labelled non-binding until adopted.

## Cross-cutting corrections

1. Every chapter must state whether its central legal duty belongs to a provider, deployer, importer, distributor, authorised representative, product manufacturer, or another actor.
2. Every chapter must separate legal requirements from recommended controls.
3. Every chapter must identify evidence and a practical audit test.
4. Effective-date language must identify the relevant classification pathway and transitional rule.
5. ISO/IEC, CEN/CENELEC, NIST, OWASP, and other standards may support compliance but must not be described as binding EU law unless incorporated through an applicable legal mechanism.
6. Draft Commission guidance must be labelled **draft and non-binding**.

## Related appendices requiring alignment

- Appendix E — High-Risk Classification Worksheet
- Appendix G — Fundamental-Rights Impact Assessment
- Appendix I — Data-Governance Assessment
- Appendix J — Human-Oversight Plan
- Appendix K — Technical-Documentation Index
- Appendix L — Conformity-Readiness Checklist
- Appendix M — Post-Market Monitoring Plan
- Appendix N — Serious-Incident Report
- Appendix S — Model-Change Assessment
- Appendix T — Substantial-Modification Assessment

## Publication gate

Chapters 36–52 are not legally cleared until:

1. all chapter-specific corrections are consolidated into the authoritative chapter files;
2. article and annex references are checked against the amended text;
3. the 2027/2028 application dates are consistently stated;
4. all affected appendices and graphics are aligned;
5. draft guidance is clearly identified as non-binding;
6. a second-pass review records closure evidence.