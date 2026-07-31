# EU AI Act GRC Compliance Manual — Research and Architecture Foundation

**Version:** Foundation draft 0.1  
**Date:** 29 July 2026  
**Status:** Research architecture for owner review; not yet a publication-ready manual

## 1. Editorial objective

The finished manual must be accurate, practical, easy to read, human-sounding, and professionally presented. It must explain legal and technical concepts in plain English before using specialist terminology.

Each major requirement should answer six practical questions:

1. What does the rule require?
2. Why does it matter?
3. What does it mean for a real organization?
4. What control should be implemented?
5. What evidence should be retained?
6. How should an auditor test it?

## 2. Authoritative source hierarchy

The manual will use the following source order:

1. **Binding EU legislation and official consolidated text**
2. **European Commission and EU AI Office guidance**
3. **AI Board adequacy assessments and approved codes of practice**
4. **Official harmonised standards and recognized technical standards when available**
5. **Secondary commentary only when clearly identified and never as the sole authority for a legal claim**

### Initial official source register

| Source | Purpose | Status |
|---|---|---|
| Regulation (EU) 2024/1689, Artificial Intelligence Act | Primary legal text | Binding source |
| EUR-Lex consolidated/current text | Article and annex verification | Binding source repository |
| European Commission AI Act policy page | Current implementation timeline and official implementation updates | Official guidance |
| European AI Office guidance for GPAI providers | Interpretation and compliance preparation for GPAI obligations | Official, nonbinding guidance |
| General-Purpose AI Code of Practice | Voluntary compliance pathway for Articles 53 and 55 | Officially assessed voluntary instrument |
| Transparency Code of Practice for AI-generated content | Voluntary compliance support for relevant Article 50 obligations | Officially assessed voluntary instrument |
| Future Commission guidelines on high-risk classification and Article 50 | Implementation interpretation | Track for publication and updates |

### Official source links

- Regulation (EU) 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Current AI Act implementation overview: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- GPAI Code of Practice: https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
- GPAI provider guidelines: https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers
- Transparency Code adequacy opinion: https://digital-strategy.ec.europa.eu/en/library/commission-opinion-assessment-code-practice-transparency-ai-generated-content

## 3. Verified implementation timeline baseline

The timeline below is the working legal baseline and must be reverified immediately before publication.

| Date | Requirement or milestone |
|---|---|
| 1 August 2024 | AI Act entered into force |
| 2 February 2025 | Prohibited AI practices and AI-literacy obligations began applying |
| 2 August 2025 | Governance provisions and obligations for providers of GPAI models began applying |
| 2 August 2026 | Most remaining AI Act provisions apply; Commission enforcement powers for GPAI obligations begin |
| 2 December 2027 | Amended application date for specified Annex III high-risk use cases, including certain employment, education, biometrics, critical-infrastructure, migration, asylum, and border-control uses |
| 2 August 2027 | Existing GPAI models placed on the market before 2 August 2025 must comply, subject to the applicable transitional rules |
| 2 August 2028 | Amended application date for high-risk AI systems embedded in regulated products under Annex I |

**Publication control:** Dates must never be copied from an older summary without checking the current official European Commission implementation page and binding amending text.

## 4. Detailed proposed Table of Contents

### Front matter

- Cover
- Copyright and license notice
- Educational and legal disclaimer
- How to use this manual
- Audience guide
- Table of Contents
- List of Figures
- List of Tables
- Acronyms and abbreviations
- Executive summary

### Part I — Understanding the EU AI Act

1. Why the EU AI Act matters
2. Scope, purpose, and regulatory approach
3. Territorial and extraterritorial applicability
4. Key definitions in plain English
5. Regulatory roles and accountability
6. Application timeline and transitional rules
7. Relationship with GDPR, NIS2, CRA, DSA, product safety, employment law, and consumer protection

### Part II — Building AI governance

8. Board and executive accountability
9. AI governance committee
10. Three-lines model for AI oversight
11. AI policies, standards, and procedures
12. AI literacy and role-based training
13. Decision rights, escalation, and risk acceptance
14. Regulatory change management
15. Management reporting and board dashboards

### Part III — Inventory, intake, and classification

16. Enterprise AI inventory
17. AI use-case intake and approval
18. Provider, deployer, importer, distributor, authorised representative, and product-manufacturer analysis
19. Prohibited-practice screening
20. High-risk classification
21. Annex I and Annex III analysis
22. Transparency-risk classification
23. GPAI and systemic-risk classification
24. Exclusions and out-of-scope determinations
25. Reassessment and substantial-modification triggers

### Part IV — Prohibited practices

26. Manipulative and deceptive techniques
27. Exploitation of vulnerabilities
28. Social scoring
29. Predictive criminal-risk restrictions
30. Untargeted facial-image scraping
31. Emotion-recognition restrictions
32. Biometric categorisation restrictions
33. Remote biometric identification restrictions
34. Newly prohibited intimate-content and child-abuse-material uses
35. Suspension, escalation, and decommissioning

### Part V — High-risk AI systems

36. High-risk quality-management system
37. Continuous risk management
38. Data and data governance
39. Technical documentation
40. Logs and recordkeeping
41. Transparency and instructions for use
42. Human oversight
43. Accuracy, robustness, cybersecurity, and resilience
44. Conformity assessment
45. EU declaration of conformity and CE marking
46. Registration
47. Fundamental-rights impact assessment
48. DPIA coordination
49. Post-market monitoring
50. Serious-incident reporting
51. Corrective action, withdrawal, and recall
52. Change management and substantial modification

### Part VI — GPAI and generative AI

53. Understanding GPAI roles
54. GPAI documentation and downstream information
55. Copyright policy and training-content summary
56. GPAI models with systemic risk
57. Model evaluations and adversarial testing
58. Systemic-risk assessment and mitigation
59. Cybersecurity and incident reporting
60. Energy and resource reporting
61. Open-source considerations
62. GPAI Code of Practice
63. Transparency Code for AI-generated content

### Part VII — Transparency and human communication

64. Chatbot and human-interaction disclosure
65. AI-generated and manipulated content marking
66. Deepfake disclosure
67. AI-generated text disclosures
68. Emotion-recognition and biometric-categorisation disclosure
69. Accessibility and understandable notices
70. Testing and monitoring disclosures

### Part VIII — Third-party and supply-chain risk

71. AI vendor due diligence
72. Contract clauses
73. Provider documentation review
74. Model cards, system cards, and limitations
75. Audit rights and incident notification
76. Cloud, API, and model dependency risk
77. Open-source and component governance
78. Ongoing vendor monitoring
79. Exit, portability, and continuity planning

### Part IX — Privacy, security, and resilience

80. GDPR integration
81. Privacy by design and data minimisation
82. Special-category data
83. Automated decision-making
84. Secure AI development lifecycle
85. Threat modelling
86. Prompt injection and model manipulation
87. Data poisoning and training-data risk
88. Model extraction and theft
89. Logging, monitoring, and vulnerability management
90. Business continuity and disaster recovery
91. Red-team and penetration-testing governance

### Part X — Risk methodology

92. Inherent-risk assessment
93. Fundamental-rights risk
94. Safety risk
95. Bias and discrimination risk
96. Privacy and data-protection risk
97. Cybersecurity risk
98. Explainability and transparency risk
99. Human-autonomy risk
100. Operational and resilience risk
101. Third-party risk
102. Legal, financial, and reputational risk
103. Residual risk, acceptance, and exceptions

### Part XI — Control framework and evidence

104. Control-library design
105. Article-to-control mapping
106. Control ownership and frequency
107. Evidence standards
108. Control testing
109. Deficiency classification
110. Corrective-action management
111. Continuous compliance monitoring

### Part XII — Assurance and audit

112. Audit planning
113. Design-effectiveness testing
114. Operating-effectiveness testing
115. Sampling and evidence evaluation
116. Technical validation
117. Bias, oversight, and transparency testing
118. Conformity-readiness reviews
119. Internal audit
120. Regulatory-examination readiness
121. Findings, remediation, and closure

### Part XIII — Enforcement and response

122. AI Office and national authorities
123. Market-surveillance authorities
124. Investigations and information requests
125. Administrative fines and exposure
126. Executive escalation
127. Regulatory notification
128. Evidence preservation and legal hold

### Part XIV — Implementation roadmap

129. First 30 days
130. Days 31–90
131. Months 4–6
132. Months 7–12
133. High-risk readiness roadmap
134. GPAI readiness roadmap
135. Transparency readiness roadmap
136. Multijurisdictional deployment
137. Maturity model
138. Continuous improvement

### Appendices

A. AI inventory template  
B. AI intake form  
C. Applicability assessment  
D. Prohibited-practice checklist  
E. High-risk classification worksheet  
F. Role-assessment worksheet  
G. Fundamental-rights impact assessment  
H. AI risk assessment  
I. Data-governance assessment  
J. Human-oversight plan  
K. Technical-documentation index  
L. Conformity-readiness checklist  
M. Post-market monitoring plan  
N. Serious-incident report  
O. AI vendor questionnaire  
P. Contract-clause checklist  
Q. AI-literacy matrix  
R. Transparency notice  
S. Model-change assessment  
T. Substantial-modification assessment  
U. Control register  
V. Evidence register  
W. Internal-audit programme  
X. Corrective-action plan  
Y. Board dashboard  
Z. Implementation roadmap

## 5. Recurring case study: GlobalWay Travel Services

GlobalWay Travel Services is a fictional multinational travel-management company serving corporate travelers and enterprise clients in the European Union and other regions.

### AI use cases

- chatbot for booking, baggage, refund, and itinerary questions
- flight and hotel recommendation engine
- automated itinerary planning
- travel-risk alerts
- fraud detection
- customer-service analytics
- personalized travel offers
- dynamic pricing recommendations
- recruitment screening
- employee performance analytics
- supplier and hotel risk scoring
- generative-AI assistance for travel consultants

### Example AI inventory record

| Field | Example |
|---|---|
| System | GlobalWay Traveler Assistant |
| Business purpose | Answer traveler questions and recommend itinerary options |
| Business owner | VP, Traveler Experience |
| Technical owner | Director, Digital Platforms |
| External provider | Third-party cloud and GPAI provider |
| GlobalWay role | Primarily deployer; role must be reassessed for substantial modification or own-brand placement |
| Data | Traveler identity, itinerary, preferences, loyalty information, support history |
| People affected | Travelers, client travel managers, travel consultants |
| Human oversight | Escalation to a travel consultant for exceptions, refunds, safety matters, or low-confidence answers |
| Transparency | Clear notice that the traveler is interacting with AI |
| Evidence | Intake approval, classification, privacy review, security review, vendor assessment, test results, monitoring logs |

## 6. Sample chapter pattern

### Example: customer-service chatbot transparency

#### Requirement

Organizations must determine whether an AI system directly interacts with people and whether a transparency notice is required under the AI Act.

#### Plain-English explanation

A traveler should not have to guess whether a response came from a person or an AI system. The notice should appear early enough to be useful and should be understandable to the intended audience.

#### GlobalWay example

When a traveler opens GlobalWay’s support chatbot, the first screen states that the traveler is interacting with an AI assistant and provides a clearly visible option to request a human travel consultant.

#### Control activity

The product owner must implement and test an approved AI-interaction notice before production deployment. The notice must remain visible or readily accessible during the interaction.

#### Evidence

- approved notice text
- user-interface screenshots
- accessibility test results
- release approval
- periodic monitoring results
- records of human-escalation testing

#### Audit test

Select a sample of customer-facing AI systems. Confirm that each applicable system displays an approved notice, that the notice appears at the correct point in the interaction, and that the organization retains evidence of testing and approval.

## 7. Initial article-to-control framework

| Control ID | Topic | Primary AI Act area | Control objective | Example evidence |
|---|---|---|---|---|
| EUAI-GOV-01 | AI governance | Governance and accountability | Establish accountable oversight and decision rights | Committee charter, RACI, minutes |
| EUAI-LIT-01 | AI literacy | Article 4 | Ensure personnel have appropriate AI knowledge and skills | Training matrix, attendance, assessment results |
| EUAI-INV-01 | AI inventory | Lifecycle governance | Identify and maintain all AI systems and models | Inventory, ownership records, review history |
| EUAI-CLS-01 | Classification | Articles 5–7 and annexes | Classify prohibited, high-risk, transparency, GPAI, and other uses | Classification worksheet, legal review |
| EUAI-TRN-01 | Human interaction | Article 50 | Provide required AI-interaction disclosures | Notice, screenshots, testing evidence |
| EUAI-HR-01 | High-risk risk management | High-risk obligations | Operate continuous documented risk management | Risk register, assessments, approvals |
| EUAI-DATA-01 | Data governance | High-risk obligations | Manage data quality, relevance, representativeness, and governance | Dataset records, quality tests, lineage |
| EUAI-HO-01 | Human oversight | High-risk obligations | Enable effective human supervision and intervention | Oversight plan, training, override logs |
| EUAI-CYB-01 | Robustness and cybersecurity | High-risk obligations | Protect accuracy, robustness, and security | Threat model, tests, monitoring, incidents |
| EUAI-PMM-01 | Post-market monitoring | Provider obligations | Monitor deployed systems and act on emerging risk | Monitoring plan, metrics, corrective actions |
| EUAI-TPRM-01 | Third-party AI | Supply-chain governance | Assess and monitor AI suppliers and dependencies | Due diligence, contract, attestations |
| EUAI-GPAI-01 | GPAI governance | Articles 53 and 55 | Meet applicable GPAI documentation, copyright, safety, and security duties | Model documentation, policies, evaluations |

## 8. Graphics register

All graphics must be original, accessible, colorful, professional, and consistent with the approved corporate visual direction.

| Figure | Working title | Purpose |
|---|---|---|
| 1 | EU AI Act applicability decision tree | Determine whether the Act may apply |
| 2 | Regulatory role map | Distinguish provider, deployer, importer, distributor, authorised representative, and manufacturer |
| 3 | AI risk-classification flow | Screen prohibited, high-risk, transparency, GPAI, and other uses |
| 4 | AI governance operating model | Show board, management, control functions, and business ownership |
| 5 | Three-lines model | Explain ownership, oversight, and independent assurance |
| 6 | AI inventory workflow | Show intake, classification, approval, monitoring, and retirement |
| 7 | High-risk AI lifecycle | Connect design, assessment, deployment, monitoring, incident response, and change |
| 8 | Fundamental-rights impact assessment | Show affected-person and mitigation analysis |
| 9 | Human-oversight model | Show monitor, challenge, intervene, override, and escalate |
| 10 | GPAI supply chain | Explain model provider, system provider, deployer, and affected person |
| 11 | Incident-reporting workflow | Show detection, triage, escalation, notification, correction, and evidence |
| 12 | Conformity-assessment pathway | Explain readiness and decision points |
| 13 | Control-to-evidence traceability | Connect article, risk, control, evidence, and audit test |
| 14 | Third-party AI risk lifecycle | Show due diligence, contracting, monitoring, incident response, and exit |
| 15 | GlobalWay AI ecosystem | Map travel use cases, personal data, suppliers, controls, and human oversight |
| 16 | Twelve-month implementation roadmap | Present phased compliance delivery |

### Figure accessibility standard

Every figure must include:

- figure number and descriptive caption
- meaningful alt text
- plain-language labels
- accessible contrast
- no reliance on color alone
- readable text at normal page zoom
- written explanation immediately below or adjacent to the figure
- consistent terminology with the surrounding section

## 9. Professional layout standard

Professional presentation is a release criterion.

The DOCX and PDF editions must include:

- polished cover page
- automatic clickable Table of Contents
- List of Figures and List of Tables
- consistent heading hierarchy
- balanced margins and paragraph spacing
- professional headers and footers
- consistent page numbering
- controlled table widths and row breaks
- captions kept with their figures or tables
- no orphaned headings
- no clipped content
- no unnecessary blank pages
- no artificial page-count padding
- no oversized headings or excessive white space
- consistent callout, example, control, evidence, and audit-test styles

Both DOCX and PDF must receive a page-by-page visual review.

## 10. Language and style standard

- Use natural, professional English.
- Prefer direct sentences and familiar words.
- Define legal and technical terms before relying on them.
- Avoid repetitive warnings and generic filler.
- Do not imply that a recommended practice is legally mandatory.
- Use consistent role names and capitalization.
- Explain abbreviations at first use.
- Use travel-agency examples to make requirements concrete without oversimplifying them.
- Verify spelling, grammar, punctuation, cross-references, figure numbering, table numbering, citations, and terminology before approval.

## 11. Initial drafting sequence

1. Executive summary and how-to-use section
2. Scope, roles, definitions, and timeline
3. AI inventory, intake, and classification
4. Prohibited practices
5. High-risk lifecycle controls
6. Transparency and GPAI
7. Third-party, privacy, security, and resilience
8. Control library and audit procedures
9. Templates and worksheets
10. Implementation roadmap
11. Graphics production
12. DOCX/PDF build and professional QA

## 12. Current gate

This foundation is ready for owner review. It does not authorize a merge, release, or publication claim.
