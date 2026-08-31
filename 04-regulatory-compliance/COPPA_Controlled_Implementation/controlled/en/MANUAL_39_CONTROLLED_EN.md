# Manual 39 — COPPA Controlled Implementation

**Controlled baseline:** Children's Online Privacy Protection Act, 15 U.S.C. §§ 6501–6506, and current 16 CFR Part 312, including the FTC's 2025 final rule amendments.  
**Boundary:** FTC guidance, policy statements, safe-harbor materials, state child/privacy law, education-sector obligations, contracts, and organization practices remain separate source layers.  
**Release rule:** reverify current 16 CFR Part 312, FTC rule/amendment status, and effective-date requirements at candidate freeze.

## Chapter 01 — Purpose, scope, and controlled-source hierarchy
Define COPPA scope, source hierarchy, ownership, and change control. Maintain an applicability register, source register, owner matrix, evidence index, and release-time change watch.

## Chapter 02 — Operator and service applicability
Determine whether the organization is an operator or otherwise within COPPA's scope. Document website/app ownership, service relationships, data collection paths, and jurisdictional assumptions.

## Chapter 03 — Child-directed service analysis
Use documented factors to assess whether a site, app, feature, or audience is child-directed. Preserve evidence supporting audience, content, design, marketing, analytics, and intended-use conclusions.

## Chapter 04 — Actual knowledge and mixed-audience decisions
Define how actual knowledge of users under 13 is identified, escalated, and handled. For mixed-audience services, document age-screening logic, consequences, and anti-circumvention controls.

## Chapter 05 — Personal-information inventory
Inventory identifiers, contact data, persistent identifiers, media, geolocation, behavioral data, device data, user-generated content, and other COPPA-relevant information. Map collection, use, disclosure, storage, and deletion flows.

## Chapter 06 — Governance and accountability
Assign accountable legal/privacy, product, security, engineering, marketing, data, procurement, support, and executive roles. Maintain RACI, approvals, exceptions, and management-review evidence.

## Chapter 07 — Direct notice to parents
Define when and how direct notice is provided before collection or material changes where required. Maintain notice versions, delivery evidence, timing, content approval, and accessibility records.

## Chapter 08 — Online privacy notice
Maintain a clear, complete, current privacy notice describing covered operators, information practices, parental rights, disclosures, retention, and contact methods as applicable.

## Chapter 09 — Verifiable parental consent framework
Establish a controlled process for selecting and operating verifiable parental consent methods appropriate to the data use and risk. Maintain consent evidence, method rationale, identity/authority validation, and revocation handling.

## Chapter 10 — Consent exceptions
Require documented analysis before relying on any collection or use that may proceed without prior parental consent. Record source basis, scope, purpose, data elements, duration, and controls preventing expansion beyond the exception.

## Chapter 11 — Data minimization
Limit collection to information reasonably necessary for the child's participation in the activity or service, consistent with applicable rule requirements. Maintain necessity assessments and product-design evidence.

## Chapter 12 — Purpose limitation and secondary use
Define permitted uses for child data and prevent incompatible secondary uses, profiling, advertising, or reuse without the required legal basis and consent analysis.

## Chapter 13 — Advertising and commercial-use controls
Govern targeted advertising, behavioral advertising, contextual advertising, measurement, attribution, and monetization involving child data. Separate regulatory requirements from internal risk policy.

## Chapter 14 — Persistent identifiers, cookies, and SDKs
Inventory cookies, pixels, SDKs, device identifiers, analytics, ad-tech, and embedded third-party code. Document purpose, provider, data flows, configuration, consent implications, and disablement/removal controls.

## Chapter 15 — Third-party disclosure governance
Control disclosures to service providers, platforms, ad-tech, analytics, processors, and other recipients. Maintain recipient inventory, purpose, necessity, contract terms, downstream restrictions, and monitoring.

## Chapter 16 — Vendor and service-provider lifecycle
Apply child-data due diligence before onboarding vendors. Assess collection, use, disclosure, security, retention, subcontractors, incident support, deletion, audit rights, and termination controls.

## Chapter 17 — School and EdTech use cases
Assess school-authorized and educational uses without assuming a universal COPPA exception. Document operator role, school authority, parental communications, data use, commercial restrictions, and applicable FERPA/state-law overlays separately.

## Chapter 18 — Parental access, review, deletion, and refusal
Provide controlled workflows for applicable parental rights to review information, request deletion, and refuse further collection or use. Maintain identity/authority validation, timing, search, response, and closure evidence.

## Chapter 19 — Age-screening and neutral design
Design age screens and audience controls to avoid steering users toward a particular response. Maintain test evidence, bypass monitoring, exception handling, and product-change reviews.

## Chapter 20 — Security safeguards
Implement reasonable administrative, technical, and physical safeguards for child personal information. Maintain access controls, encryption decisions, secure configuration, logging, vulnerability management, monitoring, and corrective actions.

## Chapter 21 — Data retention and deletion
Retain child personal information only as long as reasonably necessary for the purpose collected and securely delete it when no longer required, subject to documented legal or operational exceptions.

## Chapter 22 — Incident response and breach analysis
Integrate child-data incidents into incident response, legal/privacy review, evidence preservation, contractual obligations, state-law analysis, and FTC/order obligations where applicable.

## Chapter 23 — Product development and privacy engineering
Embed COPPA review into requirements, design, architecture, testing, release, experimentation, and change management. Require privacy review for new data elements, features, integrations, and monetization changes.

## Chapter 24 — AI, personalization, and automated features
Assess AI assistants, recommendations, moderation, profiling, inference, biometrics, and generative features for child-data collection, secondary use, model training, disclosure, retention, and transparency risks.

## Chapter 25 — Safe-harbor program governance
Where relying on an FTC-approved COPPA safe harbor, document program membership, applicable requirements, monitoring, assessments, corrective actions, and the boundary between safe-harbor obligations and the underlying rule.

## Chapter 26 — State child-privacy and sector overlays
Maintain separate applicability analysis for state child/teen privacy laws, consumer privacy laws, education laws, biometrics, health, gaming, and other overlays. Do not relabel overlay duties as COPPA requirements.

## Chapter 27 — Records and evidence management
Maintain notices, consent records, age-screening decisions, vendor records, data inventories, disclosures, rights requests, retention/deletion evidence, incidents, training, testing, and approvals under controlled retention rules.

## Chapter 28 — Training and role competence
Provide role-based training for product, engineering, design, marketing, data, privacy, legal, security, procurement, support, and leadership. Track completion, competency checks, remediation, and refresh triggers.

## Chapter 29 — Assurance and testing
Test notices, consent flows, age screens, SDK inventories, vendor controls, rights handling, retention/deletion, security controls, and child-directed feature decisions. Maintain samples, findings, remediation, and retest evidence.

## Chapter 30 — Metrics and management review
Track meaningful indicators such as consent failures, bypass rates, unauthorized SDKs, unresolved vendor findings, rights-request timeliness, retention exceptions, incidents, training completion, and remediation aging.

## Chapter 31 — Exact-hash localization, provenance, and release evidence
Freeze controlled EN/es-419/pt-BR candidates before substantive release review. Bind DOCX/PDF identities to SHA-256 hashes and preserve localization, accessibility, rendered-page, workflow-security, and release-QA evidence.

## Chapter 32 — Implementation roadmap and release-time reverification
Implement in phases: applicability; data inventory; notices/consent; product and vendor controls; rights; security; retention; assurance; metrics; continual improvement. Immediately before publication, reverify current FTC rule text, amendments, effective dates, and expressly claimed overlays. Publication remains sequential after Manual 38.
