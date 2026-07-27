**PRACTICAL CYBERSECURITY, PRIVACY & COMPLIANCE SERIES**

**GDPR**

**A Practical Manual for Managers and Junior Analysts**

*How privacy work is scoped, operated, evidenced, and improved—explained in clear professional language*

**Alberto (Al) Leiva**

First Edition • July 2026

| **Inside:** Plain-English GDPR articles • Manager playbook • Open-source tools • Evidence examples • Junior analyst labs • Interview preparation |
|--------------------------------------------------------------------------------------------------------------------------------------------------|

# Publication and Use Notice

Author: Alberto (Al) Leiva

Edition: First Edition, July 2026

Purpose: Free, practical education for managers, students, career changers, junior analysts, privacy professionals, and cybersecurity practitioners.

## Educational and legal notice

This manual provides general educational information. It is not legal advice and does not replace advice from qualified counsel or an organization’s data protection officer. GDPR duties depend on facts, Member State law, regulator guidance, contracts, and court decisions. Always verify the current official sources before acting on a real matter.

## Ethical and authorized use

Use tools and exercises only with written authorization and only with fictional, synthetic, or properly sanitized data. Personal data can harm people when it is exposed or misused. Technical skill does not create permission.

# Preface

*A welcoming introduction to practical privacy work.*

GDPR can look like a wall of legal language. In daily work, it becomes a set of practical questions: What personal data do we use? Why do we need it? Who can see it? How long do we keep it? How do we protect it? How can a person exercise a right? How do we prove that our answers are true?

Managers need clear ownership, honest risk decisions, suitable resources, and reliable evidence. Junior analysts need to map processing, review notices and contracts, coordinate rights requests, support DPIAs, organize breach facts, and communicate without hiding uncertainty.

This manual follows a methodology-first approach. Tools can help discover data, control access, find weaknesses, and organize records. They cannot choose a lawful basis, decide whether a person’s rights were respected, or replace legal and professional judgment.

| **Central lesson:** GDPR compliance is not a one-time document project. It is a continuing program for lawful, fair, transparent, secure, and accountable use of personal data. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

*— Alberto (Al) Leiva*

# How to Use This Manual

Managers should begin with Chapters 1 through 8 and use the playbook and templates as working references.

Junior analysts should study the rights, evidence, article guide, tools, fictional laboratory, portfolio projects, and interview chapter.

Technical readers should connect every tool to a defined purpose, risk, control, owner, and review process.

Legal and privacy teams should verify Member State rules and the current EDPB or supervisory authority guidance.

| **Edition note:** The final table of contents includes verified page numbers for this edition. If the manual is edited, confirm the new layout and update the page references. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Table of Contents

[Publication and Use Notice [2](#publication-and-use-notice)](#publication-and-use-notice)

[Educational and legal notice [2](#educational-and-legal-notice)](#educational-and-legal-notice)

[Ethical and authorized use [2](#ethical-and-authorized-use)](#ethical-and-authorized-use)

[Preface [3](#preface)](#preface)

[How to Use This Manual [4](#how-to-use-this-manual)](#how-to-use-this-manual)

[Table of Contents [4](#table-of-contents)](#table-of-contents)

[1. GDPR Foundations [9](#gdpr-foundations)](#gdpr-foundations)

[1.1 What GDPR protects [9](#what-gdpr-protects)](#what-gdpr-protects)

[1.2 Compliance is more than security [9](#compliance-is-more-than-security)](#compliance-is-more-than-security)

[1.3 What GDPR does not mean [9](#what-gdpr-does-not-mean)](#what-gdpr-does-not-mean)

[2. Scope, Roles, and Definitions [10](#scope-roles-and-definitions)](#scope-roles-and-definitions)

[2.1 Scope questions [10](#scope-questions)](#scope-questions)

[2.2 Core roles [10](#core-roles)](#core-roles)

[2.3 Personal, special-category, and criminal data [10](#personal-special-category-and-criminal-data)](#personal-special-category-and-criminal-data)

[3. Principles and Lawful Bases [11](#principles-and-lawful-bases)](#principles-and-lawful-bases)

[3.1 Article 5 principles [11](#article-5-principles)](#article-5-principles)

[3.2 Lawful bases under Article 6 [11](#lawful-bases-under-article-6)](#lawful-bases-under-article-6)

[3.3 Consent and sensitive data [12](#consent-and-sensitive-data)](#consent-and-sensitive-data)

[4. Data Subject Rights [13](#data-subject-rights)](#data-subject-rights)

[4.1 The request clock [13](#the-request-clock)](#the-request-clock)

[4.2 A defensible request file [14](#a-defensible-request-file)](#a-defensible-request-file)

[5. Controller and Processor Governance [15](#controller-and-processor-governance)](#controller-and-processor-governance)

[5.1 Records of processing activities [15](#records-of-processing-activities)](#records-of-processing-activities)

[5.2 Processor due diligence and Article 28 contracts [15](#processor-due-diligence-and-article-28-contracts)](#processor-due-diligence-and-article-28-contracts)

[5.3 Accountability records [15](#accountability-records)](#accountability-records)

[6. Security and Personal Data Breaches [16](#security-and-personal-data-breaches)](#security-and-personal-data-breaches)

[6.1 Article 32 security [16](#article-32-security)](#article-32-security)

[6.2 Breach decisions [16](#breach-decisions)](#breach-decisions)

[7. DPIAs, Privacy by Design, and the DPO [17](#dpias-privacy-by-design-and-the-dpo)](#dpias-privacy-by-design-and-the-dpo)

[7.1 DPIA workflow [17](#dpia-workflow)](#dpia-workflow)

[7.2 Privacy by design and default [17](#privacy-by-design-and-default)](#privacy-by-design-and-default)

[7.3 DPO independence [17](#dpo-independence)](#dpo-independence)

[8. International Data Transfers [18](#international-data-transfers)](#international-data-transfers)

[8.1 Transfer workflow [18](#transfer-workflow)](#transfer-workflow)

[8.2 Common transfer evidence [18](#common-transfer-evidence)](#common-transfer-evidence)

[9. Complete Article-by-Article Guide [19](#complete-article-by-article-guide)](#complete-article-by-article-guide)

[9.1 Chapter I — General provisions [19](#chapter-i-general-provisions)](#chapter-i-general-provisions)

[9.2 Chapter II — Principles [19](#chapter-ii-principles)](#chapter-ii-principles)

[9.3 Chapter III — Rights of the data subject [19](#chapter-iii-rights-of-the-data-subject)](#chapter-iii-rights-of-the-data-subject)

[9.4 Chapter IV — Controller and processor [20](#chapter-iv-controller-and-processor)](#chapter-iv-controller-and-processor)

[9.5 Chapter V — Transfers to third countries or international organizations [21](#chapter-v-transfers-to-third-countries-or-international-organizations)](#chapter-v-transfers-to-third-countries-or-international-organizations)

[9.6 Chapter VI — Independent supervisory authorities [22](#chapter-vi-independent-supervisory-authorities)](#chapter-vi-independent-supervisory-authorities)

[9.7 Chapter VII — Cooperation and consistency [22](#chapter-vii-cooperation-and-consistency)](#chapter-vii-cooperation-and-consistency)

[9.8 Chapter VIII — Remedies, liability and penalties [23](#chapter-viii-remedies-liability-and-penalties)](#chapter-viii-remedies-liability-and-penalties)

[9.9 Chapter IX — Specific processing situations [23](#chapter-ix-specific-processing-situations)](#chapter-ix-specific-processing-situations)

[9.10 Chapter X — Delegated and implementing acts [24](#chapter-x-delegated-and-implementing-acts)](#chapter-x-delegated-and-implementing-acts)

[9.11 Chapter XI — Final provisions [24](#chapter-xi-final-provisions)](#chapter-xi-final-provisions)

[10. Manager’s GDPR Playbook [25](#managers-gdpr-playbook)](#managers-gdpr-playbook)

[10.1 Questions for every processing owner [25](#questions-for-every-processing-owner)](#questions-for-every-processing-owner)

[10.2 Monthly dashboard [25](#monthly-dashboard)](#monthly-dashboard)

[10.3 Common management mistakes [25](#common-management-mistakes)](#common-management-mistakes)

[11. From Beginner to Junior Privacy Analyst [26](#from-beginner-to-junior-privacy-analyst)](#from-beginner-to-junior-privacy-analyst)

[11.1 Job titles [26](#job-titles)](#job-titles)

[11.2 Typical junior work [26](#typical-junior-work)](#typical-junior-work)

[11.3 Skills employers can observe [27](#skills-employers-can-observe)](#skills-employers-can-observe)

[12. Open-Source Tools for GDPR Work [28](#open-source-tools-for-gdpr-work)](#open-source-tools-for-gdpr-work)

[12.1 CISO Assistant [28](#ciso-assistant)](#ciso-assistant)

[Quick start [28](#quick-start)](#quick-start)

[Evidence to retain [28](#evidence-to-retain)](#evidence-to-retain)

[12.2 OpenMetadata [28](#openmetadata)](#openmetadata)

[Quick start [29](#quick-start-1)](#quick-start-1)

[Evidence to retain [29](#evidence-to-retain-1)](#evidence-to-retain-1)

[12.3 Microsoft Presidio [29](#microsoft-presidio)](#microsoft-presidio)

[Quick start [29](#quick-start-2)](#quick-start-2)

[Evidence to retain [29](#evidence-to-retain-2)](#evidence-to-retain-2)

[12.4 ARX [29](#arx)](#arx)

[Quick start [29](#quick-start-3)](#quick-start-3)

[Evidence to retain [29](#evidence-to-retain-3)](#evidence-to-retain-3)

[12.5 Keycloak [29](#keycloak)](#keycloak)

[Quick start [30](#quick-start-4)](#quick-start-4)

[Evidence to retain [30](#evidence-to-retain-4)](#evidence-to-retain-4)

[12.6 Wazuh [30](#wazuh)](#wazuh)

[Quick start [30](#quick-start-5)](#quick-start-5)

[Evidence to retain [30](#evidence-to-retain-5)](#evidence-to-retain-5)

[12.7 OWASP ZAP [30](#owasp-zap)](#owasp-zap)

[Quick start [30](#quick-start-6)](#quick-start-6)

[Evidence to retain [30](#evidence-to-retain-6)](#evidence-to-retain-6)

[12.8 Trivy [30](#trivy)](#trivy)

[Quick start [30](#quick-start-7)](#quick-start-7)

[Evidence to retain [31](#evidence-to-retain-7)](#evidence-to-retain-7)

[12.9 Open Policy Agent [31](#open-policy-agent)](#open-policy-agent)

[Quick start [31](#quick-start-8)](#quick-start-8)

[Evidence to retain [31](#evidence-to-retain-8)](#evidence-to-retain-8)

[12.10 Klaro! [31](#klaro)](#klaro)

[Quick start [31](#quick-start-9)](#quick-start-9)

[Evidence to retain [31](#evidence-to-retain-9)](#evidence-to-retain-9)

[12.11 Greenbone Community Edition [31](#greenbone-community-edition)](#greenbone-community-edition)

[Quick start [31](#quick-start-10)](#quick-start-10)

[Evidence to retain [32](#evidence-to-retain-10)](#evidence-to-retain-10)

[12.12 Tool governance checklist [32](#tool-governance-checklist)](#tool-governance-checklist)

[13. Fictional SaaS Laboratory and Portfolio [33](#fictional-saas-laboratory-and-portfolio)](#fictional-saas-laboratory-and-portfolio)

[Project 1 — Scope and roles [33](#project-1-scope-and-roles)](#project-1-scope-and-roles)

[Project 2 — ROPA [33](#project-2-ropa)](#project-2-ropa)

[Project 3 — Rights [33](#project-3-rights)](#project-3-rights)

[Project 4 — DPIA [33](#project-4-dpia)](#project-4-dpia)

[Project 5 — Breach [33](#project-5-breach)](#project-5-breach)

[Project 6 — Vendor and transfer [33](#project-6-vendor-and-transfer)](#project-6-vendor-and-transfer)

[Project 7 — Tools [33](#project-7-tools)](#project-7-tools)

[13.1 Portfolio ethics [33](#portfolio-ethics)](#portfolio-ethics)

[14. Thirty-Day Learning Plan [34](#thirty-day-learning-plan)](#thirty-day-learning-plan)

[14.1 Daily habit [34](#daily-habit)](#daily-habit)

[15. Interview Preparation [35](#interview-preparation)](#interview-preparation)

[What is personal data? [35](#what-is-personal-data)](#what-is-personal-data)

[Controller versus processor? [35](#controller-versus-processor)](#controller-versus-processor)

[Is consent always needed? [35](#is-consent-always-needed)](#is-consent-always-needed)

[What is a ROPA? [35](#what-is-a-ropa)](#what-is-a-ropa)

[How do you handle a rights request? [35](#how-do-you-handle-a-rights-request)](#how-do-you-handle-a-rights-request)

[When is a DPIA needed? [35](#when-is-a-dpia-needed)](#when-is-a-dpia-needed)

[What is a personal data breach? [35](#what-is-a-personal-data-breach)](#what-is-a-personal-data-breach)

[What happens at 72 hours? [35](#what-happens-at-72-hours)](#what-happens-at-72-hours)

[How do you prove compliance? [35](#how-do-you-prove-compliance)](#how-do-you-prove-compliance)

[15.1 Manager’s 60-second answer [36](#managers-60-second-answer)](#managers-60-second-answer)

[16. Templates and Checklists [37](#templates-and-checklists)](#templates-and-checklists)

[16.1 ROPA fields [37](#ropa-fields)](#ropa-fields)

[16.2 Rights-request register [37](#rights-request-register)](#rights-request-register)

[16.3 DPIA screen [37](#dpia-screen)](#dpia-screen)

[16.4 Breach fact sheet [38](#breach-fact-sheet)](#breach-fact-sheet)

[16.5 Manager pre-launch checklist [38](#manager-pre-launch-checklist)](#manager-pre-launch-checklist)

[17. GDPR, AI, and Analytics [39](#gdpr-ai-and-analytics)](#gdpr-ai-and-analytics)

[17.1 Practical review questions [39](#practical-review-questions)](#practical-review-questions)

[18. Glossary [40](#glossary)](#glossary)

[19. Subject Index [42](#subject-index)](#subject-index)

[20. Official References and Further Study [43](#official-references-and-further-study)](#official-references-and-further-study)

# 1. GDPR Foundations

*What the law protects, what compliance means, and what managers own.*

<img src="media/image1.png" style="width:6.15in;height:3.23744in" alt="Four connected blocks show people, data, purpose, and control." />

Figure 1. GDPR as a practical management program

## 1.1 What GDPR protects

GDPR protects natural persons when their personal data is processed. Personal data is information relating to an identified or identifiable person. It can include names, identifiers, location data, online identifiers, employment records, financial details, images, device data, and many other facts.

## 1.2 Compliance is more than security

Security matters, but GDPR also requires lawful and fair processing, clear information, respect for rights, purpose limits, data minimization, retention control, and accountability.

## 1.3 What GDPR does not mean

- Consent is not the only lawful basis.

- Encryption alone does not create compliance.

- A privacy notice does not fix unlawful processing.

- A processor contract does not remove the controller’s responsibility.

- A tool cannot guarantee that personal data has been fully discovered or deleted.

- A fine is not the only risk; people may suffer material or non-material harm.

# 2. Scope, Roles, and Definitions

*How to decide whether GDPR applies and who is responsible.*

## 2.1 Scope questions

1.  Identify the organization’s EU establishments.

2.  Identify offers of goods or services to people in the EU.

3.  Identify monitoring of behavior in the EU.

4.  Document excluded activities and the reason for exclusion.

5.  Check Member State laws and other sector rules.

## 2.2 Core roles

| **Role**              | **Plain meaning**                                    | **Key responsibility**                                   |
|-----------------------|------------------------------------------------------|----------------------------------------------------------|
| Data subject          | The person the data relates to                       | Exercise rights and receive clear information            |
| Controller            | Decides why and essential means of processing        | Lawfulness, rights, design, vendors, evidence            |
| Joint controllers     | Two or more parties jointly decide purpose and means | Transparent allocation of duties                         |
| Processor             | Processes personal data for a controller             | Follow instructions, protect data, assist controller     |
| Subprocessor          | Processor engaged by another processor               | Meet approved contractual and security duties            |
| DPO                   | Independent adviser and monitor where appointed      | Advise, monitor, support DPIAs, cooperate with authority |
| Supervisory authority | Independent privacy regulator                        | Guidance, investigation, corrective action, enforcement  |

## 2.3 Personal, special-category, and criminal data

Personal data is broader than information that directly names someone. Special-category data includes information about racial or ethnic origin, political opinions, religion or beliefs, trade-union membership, genetics, biometrics used for unique identification, health, sex life, or sexual orientation. Criminal conviction and offense data have separate controls under Article 10.

| **Manager checkpoint:** Require a written scope and role analysis before approving a new product, vendor, tracking technology, AI use case, or international data flow. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 3. Principles and Lawful Bases

*The rules that shape every processing purpose.*

<img src="media/image2.png" style="width:6.15in;height:3.34699in" alt="The lifecycle connects collection, use, sharing, retention, and deletion." />

Figure 2. Personal-data lifecycle

## 3.1 Article 5 principles

| **Principle**                      | **Manager question**                                              | **Useful evidence**                             |
|------------------------------------|-------------------------------------------------------------------|-------------------------------------------------|
| Lawfulness, fairness, transparency | Would the use be legal, honest, and understandable to the person? | Lawful-basis record, notice, fairness review    |
| Purpose limitation                 | Is the purpose specific, stated, and compatible with later use?   | Purpose statement, compatibility review         |
| Data minimization                  | Do we collect only what is needed?                                | Field review, form design decision              |
| Accuracy                           | How do we correct or refresh important data?                      | Validation rules, correction log                |
| Storage limitation                 | When will we delete or anonymize it?                              | Retention schedule, deletion proof              |
| Integrity and confidentiality      | Are security measures suitable for the risk?                      | Risk assessment, control evidence, tests        |
| Accountability                     | Can we prove the above?                                           | ROPA, approvals, reviews, training, audit trail |

## 3.2 Lawful bases under Article 6

| **Basis**            | **Use when**                                                                                       | **Common caution**                   |
|----------------------|----------------------------------------------------------------------------------------------------|--------------------------------------|
| Consent              | The person has a real choice and can withdraw                                                      | Do not bundle or pressure consent    |
| Contract             | Processing is objectively necessary for a contract with the person or requested pre-contract steps | Convenience is not necessity         |
| Legal obligation     | EU or Member State law requires processing                                                         | Record the legal source              |
| Vital interests      | Needed to protect life or another vital interest                                                   | Usually narrow and exceptional       |
| Public task          | Required for a public-interest task or official authority grounded in law                          | Identify the legal basis             |
| Legitimate interests | A real interest is necessary and not overridden by the person’s rights                             | Complete and retain a balancing test |

## 3.3 Consent and sensitive data

Consent must be specific, informed, unambiguous, freely given, and demonstrable. Special-category data usually needs both an Article 6 lawful basis and an Article 9 condition. Withdrawal must be as easy as giving consent.

# 4. Data Subject Rights

*How to receive, assess, complete, and document requests.*

<img src="media/image3.png" style="width:6.15in;height:3.34699in" alt="A five-step workflow covers intake through recorded outcome." />

Figure 3. Data-subject-rights workflow

| **Right**           | **Practical work**                                                   | **Watch for**                                                |
|---------------------|----------------------------------------------------------------------|--------------------------------------------------------------|
| Information         | Give clear, timely notices                                           | Layered notices, children, indirect collection               |
| Access              | Search, review, redact where lawful, and deliver securely            | Other people’s rights, identity, complete systems            |
| Rectification       | Correct inaccurate or incomplete data                                | Downstream recipients and system copies                      |
| Erasure             | Delete where the right applies                                       | Legal holds, claims, public-interest and other exceptions    |
| Restriction         | Limit use while an issue is resolved                                 | Flags must work across systems                               |
| Portability         | Provide qualifying data in a reusable format                         | Only certain automated processing and supplied/observed data |
| Objection           | Assess public-task or legitimate-interest use; stop direct marketing | Compelling grounds and research exceptions                   |
| Automated decisions | Provide safeguards for qualifying solely automated decisions         | Meaningful human involvement and explanation                 |

## 4.1 The request clock

The normal response period is one month after receipt. It may be extended by two further months when necessary due to complexity and the number of requests, but the person must be told within the first month. Identity checks must be proportionate. Fees or refusal are limited to cases that are manifestly unfounded or excessive, especially because of repetition.

## 4.2 A defensible request file

1.  Request and receipt date

2.  Identity-check decision

3.  Systems, vendors, and owners searched

4.  Search terms and date ranges

5.  Legal issues, exemptions, and redactions

6.  Approval and secure delivery

7.  Response date and retained outcome

# 5. Controller and Processor Governance

*The operating records, contracts, roles, and reviews that make accountability real.*

## 5.1 Records of processing activities

A ROPA is more than a spreadsheet of applications. It connects purposes, categories of people and data, recipients, transfers, retention, security, owners, and legal reasoning. Keep controller and processor records separate where needed.

## 5.2 Processor due diligence and Article 28 contracts

Assess expertise, reliability, security, location, subprocessors, and incident history.

Document subject matter, duration, nature, purpose, data types, people, and controller rights.

Require instructions, confidentiality, security, subprocessor controls, rights assistance, breach help, deletion or return, and audit information.

Monitor material changes and retain decisions.

## 5.3 Accountability records

| **Record**         | **Owner**                        | **Review trigger**                           |
|--------------------|----------------------------------|----------------------------------------------|
| ROPA               | Privacy program + business owner | New or changed processing                    |
| Privacy notices    | Legal/privacy + product          | Purpose, source, recipient, or law change    |
| Vendor register    | Procurement/privacy/security     | New vendor, subprocessor, location, incident |
| Retention schedule | Records/legal/privacy            | Legal, system, or business change            |
| Rights log         | Privacy operations               | Request, complaint, overdue item             |
| DPIA register      | Privacy/DPO                      | High-risk feature or material change         |

# 6. Security and Personal Data Breaches

*Risk-based safeguards, incident facts, notification decisions, and proof.*

<img src="media/image4.png" style="width:6.15in;height:3.45654in" alt="Contain, assess, decide, and improve are shown as a linked process." />

Figure 4. Personal-data-breach workflow

## 6.1 Article 32 security

Controllers and processors must use technical and organizational measures appropriate to risk. Consider confidentiality, integrity, availability, resilience, restoration, regular testing, the state of the art, costs, and the nature, scope, context, and purposes of processing.

## 6.2 Breach decisions

| **Question**                                                                                               | **Possible result**                                                           | **Evidence**                              |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------|
| Was there destruction, loss, alteration, unauthorized disclosure, or unauthorized access to personal data? | If yes, it may be a personal data breach                                      | Incident facts, affected systems and data |
| Is risk to people unlikely?                                                                                | Authority notification may not be required, but document the decision         | Risk analysis and approval                |
| Is there risk to people?                                                                                   | Notify the authority without undue delay and, where feasible, within 72 hours | Notification and delay explanation        |
| Is high risk likely?                                                                                       | Communicate clearly to affected people unless an exception applies            | Communication decision and delivery proof |

| **Important:** A processor must notify the controller without undue delay after becoming aware of a personal data breach. The controller remains responsible for the Article 33 decision. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 7. DPIAs, Privacy by Design, and the DPO

*How to find high-risk processing early and build safeguards into decisions.*

## 7.1 DPIA workflow

- Describe the processing, purpose, systems, data, people, recipients, locations, and lifecycle.

- Assess necessity and proportionality.

- Identify risks to rights and freedoms, not only risks to the company.

- Select safeguards and owners.

- Evaluate residual risk.

- Seek the DPO’s advice where applicable.

- Consult the authority before processing if unmitigated high risk remains.

- Review when risk or processing changes.

## 7.2 Privacy by design and default

Minimize fields and access by default.

Separate identifiers where practical.

Make retention and deletion work technically.

Prevent optional sharing until a valid choice is made.

Test notices, rights, exports, deletion, and logs before launch.

Record design decisions and rejected options.

## 7.3 DPO independence

The DPO must be involved in a timely way, receive resources and access, report to the highest management level, and avoid conflicts of interest. Management owns decisions. The DPO advises and monitors, but should not be held responsible for business purposes or the means of processing.

# 8. International Data Transfers

*How to identify transfers and use lawful transfer tools.*

## 8.1 Transfer workflow

1.  Map exporters, importers, remote access, support locations, subprocessors, and onward transfers.

2.  Confirm the roles and countries.

3.  Check for an adequacy decision.

4.  If needed, select appropriate safeguards such as SCCs or approved BCRs.

5.  Assess whether the safeguard works in practice and identify supplementary measures.

6.  Use Article 49 derogations only when their narrow conditions apply.

7.  Monitor legal, vendor, and technical changes.

## 8.2 Common transfer evidence

| **Item**               | **What it should show**                                                                  |
|------------------------|------------------------------------------------------------------------------------------|
| Transfer map           | Data, purpose, systems, countries, recipients, remote access, onward transfers           |
| Transfer mechanism     | Adequacy, SCC module, BCR, approved code/certification, or narrow derogation             |
| Assessment             | Relevant law and practice, requests, safeguards, risks, and conclusion                   |
| Supplementary measures | Encryption, key control, minimization, pseudonymization, policy and challenge procedures |
| Monitoring             | Changes in law, importer, subprocessor, location, service, and access                    |

# 9. Complete Article-by-Article Guide

*A concise working guide to all 99 GDPR articles. Use the official legal text for real legal analysis.*

| **How to read this chapter:** The table explains each article in plain language. The manager action and evidence columns are practical starting points, not a complete legal opinion. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 9.1 Chapter I — General provisions

| **Art.** | **Article topic**             | **Plain meaning**                                                                                                                      | **Manager action**                                                    | **Typical evidence**              |
|----------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------|
| 1        | Subject-matter and objectives | Sets the Regulation’s purpose: protect people and allow lawful movement of personal data.                                              | Confirm applicability, scope, and definitions; document the decision. | Scope memo, service map, data map |
| 2        | Material scope                | Explains which automated and structured manual processing is covered and which activities are excluded.                                | Confirm applicability, scope, and definitions; document the decision. | Scope memo, service map, data map |
| 3        | Territorial scope             | Can apply to EU establishments and to some organizations outside the EU that offer goods or services to, or monitor, people in the EU. | Confirm applicability, scope, and definitions; document the decision. | Scope memo, service map, data map |
| 4        | Definitions                   | Defines personal data, processing, controller, processor, consent, breach, profiling, and other key terms.                             | Confirm applicability, scope, and definitions; document the decision. | Scope memo, service map, data map |

## 9.2 Chapter II — Principles

| **Art.** | **Article topic**                                   | **Plain meaning**                                                                                                                      | **Manager action**                                               | **Typical evidence**                                  |
|----------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------------------|
| 5        | Principles relating to processing                   | Requires lawfulness, fairness, transparency, purpose limitation, minimization, accuracy, storage limits, security, and accountability. | Map each purpose, data type, lawful basis, safeguard, and proof. | ROPA, lawful-basis record, consent or exception proof |
| 6        | Lawfulness of processing                            | Requires at least one valid lawful basis for each processing purpose.                                                                  | Map each purpose, data type, lawful basis, safeguard, and proof. | ROPA, lawful-basis record, consent or exception proof |
| 7        | Conditions for consent                              | Consent must be demonstrable, clear, separate where appropriate, and as easy to withdraw as to give.                                   | Map each purpose, data type, lawful basis, safeguard, and proof. | ROPA, lawful-basis record, consent or exception proof |
| 8        | Children’s consent for information-society services | Sets rules for a child’s consent in certain online services and permits Member States to set the age from 13 to 16.                    | Map each purpose, data type, lawful basis, safeguard, and proof. | ROPA, lawful-basis record, consent or exception proof |
| 9        | Special categories of personal data                 | Generally, prohibits sensitive-data processing unless a listed exception applies.                                                      | Map each purpose, data type, lawful basis, safeguard, and proof. | ROPA, lawful-basis record, consent or exception proof |
| 10       | Criminal-conviction and offense data                | Limits this processing to official authority or processing authorized by law with safeguards.                                          | Map each purpose, data type, lawful basis, safeguard, and proof. | ROPA, lawful-basis record, consent or exception proof |
| 11       | Processing not requiring identification             | Does not require keeping extra identifying data only to comply when identification is not needed.                                      | Map each purpose, data type, lawful basis, safeguard, and proof. | ROPA, lawful-basis record, consent or exception proof |

## 9.3 Chapter III — Rights of the data subject

| **Art.** | **Article topic**                                            | **Plain meaning**                                                                                             | **Manager action**                                                                              | **Typical evidence**                                     |
|----------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 12       | Transparent information, communication and modalities        | Requires clear notices and practical methods for people to exercise rights.                                   | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 13       | Information collected from the data subject                  | Lists notice information to give when personal data comes directly from the person.                           | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 14       | Information not obtained from the data subject               | Lists notice information and timing when data comes from another source.                                      | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 15       | Right of access                                              | Let’s a person confirm processing and obtain information and a copy of personal data, subject to limits.      | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 16       | Right to rectification                                       | Let’s people correct inaccurate data and complete incomplete data.                                            | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 17       | Right to erasure                                             | Requires deletion in listed situations, subject to legal exceptions.                                          | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 18       | Right to restriction of processing                           | Let’s people limit processing while certain issues are checked.                                               | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 19       | Notification regarding rectification, erasure or restriction | Requires telling recipients about changes unless impossible or disproportionate.                              | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 20       | Right to data portability                                    | Provides certain data in a structured, commonly used, machine-readable format when conditions apply.          | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 21       | Right to object                                              | Let’s people object to some public-task, legitimate-interest, research, and direct-marketing processing.      | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 22       | Automated decision-making and profiling                      | Provides safeguards against certain solely automated decisions with legal or similarly significant effects.   | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |
| 23       | Restrictions                                                 | Allows Union or Member State law to restrict listed rights only when legal safeguards and conditions are met. | Build a tracked rights process with identity checks, deadlines, decisions, and secure delivery. | Notice, request log, identity check, search and response |

## 9.4 Chapter IV — Controller and processor

| **Art.** | **Article topic**                                     | **Plain meaning**                                                                                                                       | **Manager action**                                                      | **Typical evidence**                                        |
|----------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|
| 24       | Responsibility of the controller                      | Requires risk-based measures and proof that processing complies.                                                                        | Assign roles, contracts, instructions, records, and accountability.     | Policies, RACI, contracts, instructions, ROPA               |
| 25       | Data protection by design and by default              | Requires privacy safeguards in system design and privacy-protective default settings.                                                   | Assign roles, contracts, instructions, records, and accountability.     | Policies, RACI, contracts, instructions, ROPA               |
| 26       | Joint controllers                                     | Requires joint controllers to define responsibilities transparently and provide the arrangement’s essence to people.                    | Assign roles, contracts, instructions, records, and accountability.     | Policies, RACI, contracts, instructions, ROPA               |
| 27       | Representatives outside the Union                     | Requires some non-EU controllers and processors to name an EU representative, with stated exceptions.                                   | Assign roles, contracts, instructions, records, and accountability.     | Policies, RACI, contracts, instructions, ROPA               |
| 28       | Processor                                             | Requires suitable processors and detailed contracts or other legal acts governing processing.                                           | Assign roles, contracts, instructions, records, and accountability.     | Policies, RACI, contracts, instructions, ROPA               |
| 29       | Processing under authority                            | Limits staff and processors to instructions unless law requires otherwise.                                                              | Assign roles, contracts, instructions, records, and accountability.     | Policies, RACI, contracts, instructions, ROPA               |
| 30       | Records of processing activities                      | Requires controller and processor records, with a limited small-organization exception that often does not apply.                       | Assign roles, contracts, instructions, records, and accountability.     | Policies, RACI, contracts, instructions, ROPA               |
| 31       | Cooperation with the supervisory authority            | Requires cooperation with the regulator when requested.                                                                                 | Assign roles, contracts, instructions, records, and accountability.     | Policies, RACI, contracts, instructions, ROPA               |
| 32       | Security of processing                                | Requires security appropriate to risk, including resilience, restoration, testing, and measures such as encryption where suitable.      | Operate risk-based security and a tested breach-response process.       | Risk assessment, controls, logs, incident and breach record |
| 33       | Notification of a breach to the supervisory authority | Requires controller notification without undue delay and, where feasible, within 72 hours unless the breach is unlikely to create risk. | Operate risk-based security and a tested breach-response process.       | Risk assessment, controls, logs, incident and breach record |
| 34       | Communication of a breach to the data subject         | Requires notice to affected people when a breach is likely to create high risk, subject to exceptions.                                  | Operate risk-based security and a tested breach-response process.       | Risk assessment, controls, logs, incident and breach record |
| 35       | Data protection impact assessment                     | Requires a DPIA before processing likely to create high risk.                                                                           | Screen high-risk work, support the DPO, and consult when required.      | DPIA screen, DPIA, DPO record, consultation file            |
| 36       | Prior consultation                                    | Requires consulting the authority before processing when a DPIA shows unmitigated high risk.                                            | Screen high-risk work, support the DPO, and consult when required.      | DPIA screen, DPIA, DPO record, consultation file            |
| 37       | Designation of the data protection officer            | Lists when a DPO must be appointed and permits voluntary appointment.                                                                   | Screen high-risk work, support the DPO, and consult when required.      | DPIA screen, DPIA, DPO record, consultation file            |
| 38       | Position of the data protection officer               | Protects DPO independence, access, resources, and direct reporting.                                                                     | Screen high-risk work, support the DPO, and consult when required.      | DPIA screen, DPIA, DPO record, consultation file            |
| 39       | Tasks of the data protection officer                  | Lists advice, monitoring, DPIA, cooperation, and regulator-contact duties.                                                              | Screen high-risk work, support the DPO, and consult when required.      | DPIA screen, DPIA, DPO record, consultation file            |
| 40       | Codes of conduct                                      | Allows sector codes to help apply GDPR requirements.                                                                                    | Use codes or certification only with clear scope, oversight, and proof. | Code or certification scope, monitoring and findings        |
| 41       | Monitoring of approved codes                          | Sets requirements for bodies that monitor compliance with approved codes.                                                               | Use codes or certification only with clear scope, oversight, and proof. | Code or certification scope, monitoring and findings        |
| 42       | Certification                                         | Allows voluntary certification mechanisms, seals, and marks without reducing controller or processor responsibility.                    | Use codes or certification only with clear scope, oversight, and proof. | Code or certification scope, monitoring and findings        |
| 43       | Certification bodies                                  | Sets accreditation and operating requirements for certification bodies.                                                                 | Use codes or certification only with clear scope, oversight, and proof. | Code or certification scope, monitoring and findings        |

## 9.5 Chapter V — Transfers to third countries or international organizations

| **Art.** | **Article topic**                                    | **Plain meaning**                                                                                                           | **Manager action**                                                  | **Typical evidence**                                           |
|----------|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------|
| 44       | General principle for transfers                      | Requires Chapter V conditions for transfers while preserving all other GDPR duties.                                         | Map transfers and validate the lawful transfer tool and safeguards. | Transfer map, adequacy/SCC/BCR file, assessment and safeguards |
| 45       | Transfers based on an adequacy decision              | Allows transfers where the Commission recognizes adequate protection.                                                       | Map transfers and validate the lawful transfer tool and safeguards. | Transfer map, adequacy/SCC/BCR file, assessment and safeguards |
| 46       | Transfers subject to appropriate safeguards          | Allows transfers using safeguards such as SCCs or BCRs with enforceable rights and remedies.                                | Map transfers and validate the lawful transfer tool and safeguards. | Transfer map, adequacy/SCC/BCR file, assessment and safeguards |
| 47       | Binding corporate rules                              | Sets approval and content requirements for BCRs within corporate groups.                                                    | Map transfers and validate the lawful transfer tool and safeguards. | Transfer map, adequacy/SCC/BCR file, assessment and safeguards |
| 48       | Transfers or disclosures not authorized by Union law | Foreign court or authority orders alone are not a transfer basis unless supported by an applicable international agreement. | Map transfers and validate the lawful transfer tool and safeguards. | Transfer map, adequacy/SCC/BCR file, assessment and safeguards |
| 49       | Derogations for specific situations                  | Provides narrow transfer exceptions and conditions when adequacy or safeguards are unavailable.                             | Map transfers and validate the lawful transfer tool and safeguards. | Transfer map, adequacy/SCC/BCR file, assessment and safeguards |
| 50       | International cooperation                            | Encourages cooperation with non-EU countries and organizations in privacy enforcement.                                      | Map transfers and validate the lawful transfer tool and safeguards. | Transfer map, adequacy/SCC/BCR file, assessment and safeguards |

## 9.6 Chapter VI — Independent supervisory authorities

| **Art.** | **Article topic**              | **Plain meaning**                                                                                  | **Manager action**                                                                 | **Typical evidence**                                    |
|----------|--------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------|
| 51       | Supervisory authority          | Requires each Member State to provide one or more independent public authorities.                  | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 52       | Independence                   | Requires authorities and their members to act independently and without outside instruction.       | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 53       | General conditions for members | Sets appointment, qualification, and conduct conditions for authority members.                     | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 54       | Rules on establishment         | Requires Member State law to define establishment, powers, terms, and related rules.               | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 55       | Competence                     | Defines the general authority of each supervisory authority within its territory.                  | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 56       | Lead supervisory authority     | Sets the one-stop-shop lead-authority rules for cross-border processing.                           | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 57       | Tasks                          | Lists regulator duties, including monitoring, awareness, complaints, investigations, and guidance. | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 58       | Powers                         | Lists investigative, corrective, authorization, and advisory powers.                               | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 59       | Activity reports               | Requires annual public reports by supervisory authorities.                                         | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |

## 9.7 Chapter VII — Cooperation and consistency

| **Art.** | **Article topic**                                  | **Plain meaning**                                                                   | **Manager action**                                                                 | **Typical evidence**                                    |
|----------|----------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------|
| 60       | Cooperation between lead and concerned authorities | Creates the cooperation process for cross-border cases.                             | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 61       | Mutual assistance                                  | Requires authorities to provide relevant information and assistance to one another. | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 62       | Joint operations                                   | Allows joint investigations and enforcement work.                                   | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 63       | Consistency mechanism                              | Creates a process for consistent GDPR application across the EU.                    | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 64       | Opinion of the Board                               | Lists matters requiring or allowing an EDPB opinion.                                | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 65       | Dispute resolution by the Board                    | Allows binding EDPB decisions in specified authority disputes.                      | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 66       | Urgency procedure                                  | Allows urgent provisional or final measures and urgent EDPB action.                 | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 67       | Exchange of information                            | Allows the Commission to define formats and procedures for authority exchanges.     | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 68       | European Data Protection Board                     | Establishes the EDPB as an EU body with legal personality.                          | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 69       | Independence of the Board                          | Requires independent performance of EDPB duties.                                    | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 70       | Tasks of the Board                                 | Lists EDPB guidance, consistency, dispute, accreditation, and advisory tasks.       | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 71       | Reports                                            | Requires an annual EDPB report on personal-data protection.                         | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 72       | Procedure                                          | Sets EDPB voting rules.                                                             | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 73       | Chair                                              | Requires election of a chair and two deputy chairs.                                 | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 74       | Tasks of the Chair                                 | Lists meeting, notice, and performance duties of the chair.                         | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 75       | Secretariat                                        | Provides an EDPS-supplied secretariat under the chair’s direction.                  | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |
| 76       | Confidentiality                                    | Sets confidentiality rules for Board discussions and document access.               | Know the regulator, cooperation path, and records needed for cross-border matters. | Authority correspondence, case file, cooperation record |

## 9.8 Chapter VIII — Remedies, liability and penalties

| **Art.** | **Article topic**                                 | **Plain meaning**                                                                                                                   | **Manager action**                                                              | **Typical evidence**                                            |
|----------|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------|
| 77       | Right to lodge a complaint                        | Lets a person complain to a supervisory authority, especially where they live, work, or believe a violation occurred.               | Maintain complaint, litigation, liability, and enforcement-response procedures. | Complaint, legal hold, decision, remediation and payment record |
| 78       | Judicial remedy against a supervisory authority   | Provides court remedies against legally binding authority decisions and certain delays.                                             | Maintain complaint, litigation, liability, and enforcement-response procedures. | Complaint, legal hold, decision, remediation and payment record |
| 79       | Judicial remedy against a controller or processor | Provides court remedies when a person believes GDPR rights were violated.                                                           | Maintain complaint, litigation, liability, and enforcement-response procedures. | Complaint, legal hold, decision, remediation and payment record |
| 80       | Representation of data subjects                   | Allows qualified nonprofit bodies to represent people, subject to national rules.                                                   | Maintain complaint, litigation, liability, and enforcement-response procedures. | Complaint, legal hold, decision, remediation and payment record |
| 81       | Suspension of proceedings                         | Helps courts coordinate related GDPR cases in different Member States.                                                              | Maintain complaint, litigation, liability, and enforcement-response procedures. | Complaint, legal hold, decision, remediation and payment record |
| 82       | Compensation and liability                        | Provides compensation for material or non-material damage and allocates controller and processor liability.                         | Maintain complaint, litigation, liability, and enforcement-response procedures. | Complaint, legal hold, decision, remediation and payment record |
| 83       | General conditions for administrative fines       | Requires fines to be effective, proportionate, and dissuasive and lists factors and maximum tiers.                                  | Maintain complaint, litigation, liability, and enforcement-response procedures. | Complaint, legal hold, decision, remediation and payment record |
| 84       | Penalties                                         | Requires Member States to set other effective, proportionate, and dissuasive penalties for infringements not covered by Article 83. | Maintain complaint, litigation, liability, and enforcement-response procedures. | Complaint, legal hold, decision, remediation and payment record |

## 9.9 Chapter IX — Specific processing situations

| **Art.** | **Article topic**                     | **Plain meaning**                                                                                                  | **Manager action**                                                   | **Typical evidence**                       |
|----------|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|--------------------------------------------|
| 85       | Freedom of expression and information | Requires Member States to reconcile data protection with expression and information rights.                        | Check applicable Member State rules and document special safeguards. | National-law review, safeguards, approvals |
| 86       | Public access to official documents   | Allows national rules to reconcile public-document access with data protection.                                    | Check applicable Member State rules and document special safeguards. | National-law review, safeguards, approvals |
| 87       | National identification number        | Allows Member States to set specific conditions and safeguards.                                                    | Check applicable Member State rules and document special safeguards. | National-law review, safeguards, approvals |
| 88       | Employment context                    | Allows more specific national or collective-agreement rules with safeguards for employee data.                     | Check applicable Member State rules and document special safeguards. | National-law review, safeguards, approvals |
| 89       | Archiving, research and statistics    | Requires safeguards and allows certain rights exceptions under stated conditions.                                  | Check applicable Member State rules and document special safeguards. | National-law review, safeguards, approvals |
| 90       | Obligations of secrecy                | Allows rules that balance regulator access with professional secrecy.                                              | Check applicable Member State rules and document special safeguards. | National-law review, safeguards, approvals |
| 91       | Churches and religious associations   | Allows existing comprehensive data-protection rules to continue if aligned with GDPR and independently supervised. | Check applicable Member State rules and document special safeguards. | National-law review, safeguards, approvals |

## 9.10 Chapter X — Delegated and implementing acts

| **Art.** | **Article topic**          | **Plain meaning**                                                               | **Manager action**                                                                         | **Typical evidence**                              |
|----------|----------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------|
| 92       | Exercise of the delegation | Sets how the Commission may exercise delegated powers under specified articles. | Track the legal rule and any Commission or Member State action affecting the organization. | Legal register, review notes, management decision |
| 93       | Committee procedure        | Sets the committee process supporting Commission implementing acts.             | Track the legal rule and any Commission or Member State action affecting the organization. | Legal register, review notes, management decision |

## 9.11 Chapter XI — Final provisions

| **Art.** | **Article topic**                        | **Plain meaning**                                                                                       | **Manager action**                                                                         | **Typical evidence**                              |
|----------|------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------|
| 94       | Repeal of Directive 95/46/EC             | Repeals the former Data Protection Directive and preserves reference continuity.                        | Track the legal rule and any Commission or Member State action affecting the organization. | Legal register, review notes, management decision |
| 95       | Relationship with the ePrivacy Directive | Avoids extra GDPR duties where specific electronic-communications duties already cover the same matter. | Track the legal rule and any Commission or Member State action affecting the organization. | Legal register, review notes, management decision |
| 96       | Previously concluded agreements          | Allows compliant pre-24 May 2016 international agreements to remain until changed or replaced.          | Track the legal rule and any Commission or Member State action affecting the organization. | Legal register, review notes, management decision |
| 97       | Commission reports                       | Requires periodic evaluation reports, especially on transfers and cooperation.                          | Track the legal rule and any Commission or Member State action affecting the organization. | Legal register, review notes, management decision |
| 98       | Review of other Union legal acts         | Requires review and possible amendment of other EU data-protection laws for consistency.                | Track the legal rule and any Commission or Member State action affecting the organization. | Legal register, review notes, management decision |
| 99       | Entry into force and application         | States entry into force and application from 25 May 2018.                                               | Track the legal rule and any Commission or Member State action affecting the organization. | Legal register, review notes, management decision |

# 10. Manager’s GDPR Playbook

*Questions, meetings, metrics, decisions, and warning signs for management.*

## 10.1 Questions for every processing owner

- What is the exact purpose?

- What personal data is used and about whom?

- What is the lawful basis and, if needed, Article 9 condition?

- What notice is given?

- Who receives or accesses the data?

- Where is it stored or remotely accessed?

- How long is it kept and how is deletion proved?

- What rights apply and how will they work?

- What could harm people?

- Which owner reviews evidence and changes?

## 10.2 Monthly dashboard

| **Area**  | **Manager question**                                 | **Status**           |
|-----------|------------------------------------------------------|----------------------|
| ROPA      | Are new and changed activities recorded?             | Green / Yellow / Red |
| Rights    | Are requests complete and on time?                   | Green / Yellow / Red |
| DPIAs     | Are high-risk changes screened before launch?        | Green / Yellow / Red |
| Breaches  | Are decisions timely and supported?                  | Green / Yellow / Red |
| Vendors   | Are contracts, subprocessors, and locations current? | Green / Yellow / Red |
| Transfers | Are mechanisms and assessments current?              | Green / Yellow / Red |
| Retention | Are deletion jobs operating and reviewed?            | Green / Yellow / Red |
| Training  | Are role-based training and follow-up complete?      | Green / Yellow / Red |

## 10.3 Common management mistakes

- Treating consent as the answer to every purpose.

- Keeping data because it may be useful someday.

- Buying a privacy tool before defining the operating process.

- Launching high-risk processing before the DPIA.

- Ignoring employee and business-contact data.

- Signing SCCs without mapping transfers or assessing practical safeguards.

- Making the DPO own business decisions.

- Hiding incidents or delaying escalation while facts are incomplete.

# 11. From Beginner to Junior Privacy Analyst

*A safe and honest path from learning the law to demonstrating entry-level ability.*

<img src="media/image5.png" style="width:6.15in;height:3.34699in" alt="Learning, practice, portfolio, explanation, and application form a career path." />

Figure 5. Junior privacy analyst pathway

## 11.1 Job titles

**Junior Privacy Analyst**

**Data Protection Analyst**

**Privacy Operations Analyst**

**GRC Analyst — Privacy**

**Data Governance Analyst**

**Third-Party Privacy Analyst**

**Privacy and Security Analyst**

**Privacy Program Coordinator**

## 11.2 Typical junior work

- Update ROPA records from owner interviews.

- Check notices against processing facts.

- Log, coordinate, and document rights requests.

- Gather processor, security, and transfer evidence.

- Perform DPIA screening and prepare drafts for review.

- Maintain breach facts and decision timelines.

- Track actions, owners, due dates, and retests.

- Prepare clear reports without making unsupported legal conclusions.

## 11.3 Skills employers can observe

| **Skill**         | **Portfolio proof**                                              |
|-------------------|------------------------------------------------------------------|
| Data mapping      | Fictional ROPA and lifecycle diagram                             |
| Legal reasoning   | Lawful-basis and legitimate-interest examples with assumptions   |
| Rights operations | Request log, identity decision, search checklist, response draft |
| Risk              | DPIA screen and completed fictional DPIA                         |
| Incidents         | Breach fact sheet, risk assessment, notification decision        |
| Communication     | One-page manager summary and interview explanation               |

| **Career honesty:** A laboratory portfolio is not professional work experience. Label it clearly as practice, use fictional data, and explain what you learned and what required expert review. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 12. Open-Source Tools for GDPR Work

*What each tool can support, how to start safely, and what evidence to retain.*

| **Methodology first:** A tool can support discovery, access, security, anonymization, or evidence. It cannot determine legal compliance by itself. |
|----------------------------------------------------------------------------------------------------------------------------------------------------|

| **Tool**                    | **Purpose**                                     | **Typical GDPR support**                                                      |
|-----------------------------|-------------------------------------------------|-------------------------------------------------------------------------------|
| CISO Assistant              | GRC and control records                         | Accountability, security, minimization, rights, or privacy-by-design evidence |
| OpenMetadata                | Data catalog and lineage                        | Accountability, security, minimization, rights, or privacy-by-design evidence |
| Microsoft Presidio          | PII detection and de-identification             | Accountability, security, minimization, rights, or privacy-by-design evidence |
| ARX                         | Data anonymization and risk analysis            | Accountability, security, minimization, rights, or privacy-by-design evidence |
| Keycloak                    | Identity and access management                  | Accountability, security, minimization, rights, or privacy-by-design evidence |
| Wazuh                       | Security monitoring                             | Accountability, security, minimization, rights, or privacy-by-design evidence |
| OWASP ZAP                   | Authorized web testing                          | Accountability, security, minimization, rights, or privacy-by-design evidence |
| Trivy                       | Code, image, secret, and configuration scanning | Accountability, security, minimization, rights, or privacy-by-design evidence |
| Open Policy Agent           | Policy as code                                  | Accountability, security, minimization, rights, or privacy-by-design evidence |
| Klaro!                      | Consent interface support                       | Accountability, security, minimization, rights, or privacy-by-design evidence |
| Greenbone Community Edition | Vulnerability scanning                          | Accountability, security, minimization, rights, or privacy-by-design evidence |

## 12.1 CISO Assistant

GRC and control records.

**Official documentation and setup:** [<u>Open the official CISO Assistant guide</u>](https://intuitem.gitbook.io/ciso-assistant)

### Quick start

Create a fictional organization, map one GDPR requirement to a control, assign an owner, and attach sanitized evidence.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.2 OpenMetadata

Data catalog and lineage.

**Official documentation and setup:** [<u>Open the official OpenMetadata guide</u>](https://docs.open-metadata.org/)

### Quick start

Deploy a lab catalog, register a sample data asset, add an owner, classification, purpose note, and retention tag.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.3 Microsoft Presidio

PII detection and de-identification.

**Official documentation and setup:** [<u>Open the official Microsoft Presidio guide</u>](https://microsoft.github.io/presidio/)

### Quick start

Run sample text containing invented identifiers, review detections, apply masking, and record false positives and misses.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.4 ARX

Data anonymization and risk analysis.

**Official documentation and setup:** [<u>Open the official ARX guide</u>](https://arx.deidentifier.org/anonymization-tool/)

### Quick start

Load a synthetic dataset, mark identifiers and quasi-identifiers, apply a privacy model, and compare utility and risk.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.5 Keycloak

Identity and access management.

**Official documentation and setup:** [<u>Open the official Keycloak guide</u>](https://www.keycloak.org/guides)

### Quick start

Create a lab realm, users, roles, and MFA; test least privilege and export the configuration and review evidence.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.6 Wazuh

Security monitoring.

**Official documentation and setup:** [<u>Open the official Wazuh guide</u>](https://documentation.wazuh.com/current/quickstart.html)

### Quick start

Connect one lab endpoint, create a harmless event, review the alert, and save the event, analyst decision, and follow-up.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.7 OWASP ZAP

Authorized web testing.

**Official documentation and setup:** [<u>Open the official OWASP ZAP guide</u>](https://www.zaproxy.org/getting-started/)

### Quick start

Proxy a local training application, begin with passive findings, validate one result, and export the approved scope and report.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.8 Trivy

Code, image, secret, and configuration scanning.

**Official documentation and setup:** [<u>Open the official Trivy guide</u>](https://trivy.dev/latest/)

### Quick start

Scan a pinned laboratory image or repository, protect reports, validate one finding, fix it, and scan again.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.9 Open Policy Agent

Policy as code.

**Official documentation and setup:** [<u>Open the official Open Policy Agent guide</u>](https://www.openpolicyagent.org/docs)

### Quick start

Write a lab rule that denies a data resource without an owner or retention tag; test allowed and denied inputs.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.10 Klaro!

Consent interface support.

**Official documentation and setup:** [<u>Open the official Klaro! guide</u>](https://klaro.org/docs/)

### Quick start

Configure a lab page so optional services remain off until choice; test accept, reject, change, and withdrawal paths.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.11 Greenbone Community Edition

Vulnerability scanning.

**Official documentation and setup:** [<u>Open the official Greenbone Community Edition guide</u>](https://greenbone.github.io/docs/latest/)

### Quick start

Scan only an approved lab target, validate a finding, correct it, rescan, and record scope, version, result, and reviewer.

### Evidence to retain

Record the approved purpose, owner, scope, data used, tool and content version, configuration, complete result, reviewer, decision, corrective action, and retest. Protect reports that contain personal data, credentials, or vulnerabilities.

## 12.12 Tool governance checklist

- Use fictional or sanitized data in training.

- Approve purpose, owner, scope, access, hosting, and retention before production use.

- Review licenses, software sources, releases, checksums, and dependencies.

- Test detection accuracy and document false positives and false negatives.

- Restrict and log administrative access.

- Define human review, escalation, correction, and deletion processes.

- Do not upload personal data to an external service without an approved legal, security, and transfer review.

# 13. Fictional SaaS Laboratory and Portfolio

*A complete practice company using only synthetic information.*

Blue Lantern Analytics is a fictional EU-facing SaaS provider with 30 employees. It serves business customers, uses cloud hosting and support vendors, monitors application activity, sends product messages, and plans an AI support feature. It has no real customers or real personal data.

## Project 1 — Scope and roles

Define establishments, targeting, services, roles, systems, people, and data.

## Project 2 — ROPA

Create 12 processing activities with purpose, basis, data, recipients, transfers, retention, security, and owners.

## Project 3 — Rights

Complete fictional access, correction, deletion, objection, and portability requests.

## Project 4 — DPIA

Assess monitoring or the AI support feature and define safeguards.

## Project 5 — Breach

Assess a lost support export, build the timeline, decide notifications, and write a manager brief.

## Project 6 — Vendor and transfer

Review a fictional processor, Article 28 terms, location, SCC module, assessment, and safeguards.

## Project 7 — Tools

Use three Chapter 12 tools in an isolated lab and document limitations and evidence.

## 13.1 Portfolio ethics

- Never publish real employee, customer, applicant, patient, or user data.

- Label every file as fictional training work.

- Do not copy a company’s confidential notice, DPIA, contract, or incident report.

- Explain assumptions, uncertainty, and where legal review would be required.

# 14. Thirty-Day Learning Plan

*A realistic month of study, practice, portfolio work, and interview preparation.*

| **Week** | **Focus**                                           | **Required output**                         |
|----------|-----------------------------------------------------|---------------------------------------------|
| Week 1   | Scope, roles, definitions, principles, lawful bases | Scope memo, role map, lawful-basis examples |
| Week 2   | Rights, ROPA, retention, processors                 | ROPA, rights checklist, processor review    |
| Week 3   | Security, breach, DPIA, design, transfers           | Breach file, DPIA, transfer map             |
| Week 4   | Tools, portfolio, interview, application            | Sanitized portfolio and practiced answers   |

## 14.1 Daily habit

1.  Read one official source section.

2.  Explain one concept in your own words.

3.  Create one small fictional record.

4.  Review the record for clarity and evidence.

5.  Add one improvement to the portfolio.

# 15. Interview Preparation

*Questions and short answers for junior analysts and managers.*

## What is personal data?

Information relating to an identified or identifiable natural person. Context matters; indirect identifiers can also make someone identifiable.

## Controller versus processor?

A controller decides the purpose and essential means. A processor acts on behalf of the controller under instructions.

## Is consent always needed?

No. Article 6 provides six lawful bases. Consent is appropriate only when its conditions and genuine choice are met.

## What is a ROPA?

A record of processing activities that helps explain purposes, people, data, recipients, transfers, retention, security, and roles.

## How do you handle a rights request?

Log it, verify identity proportionately, clarify scope if needed, search complete systems and vendors, review legal issues, respond securely, and retain the decision trail.

## When is a DPIA needed?

Before processing likely to result in high risk to people’s rights and freedoms.

## What is a personal data breach?

A security breach causing accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to personal data.

## What happens at 72 hours?

A controller notifies the authority where required without undue delay and, where feasible, within 72 hours after awareness. Delay reasons must be explained.

## How do you prove compliance?

With reliable, dated records that connect the requirement, processing, control, owner, review, decision, action, and outcome.

## 15.1 Manager’s 60-second answer

| **Interview response:** I treat GDPR as an operating program. I define scope and roles, map processing and lawful bases, make rights and deletion work, assess high-risk changes, manage processors and transfers, operate risk-based security and breach response, and require evidence. The DPO and legal team provide independent advice, while management owns business decisions and resources. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 16. Templates and Checklists

*Practical structures to copy into an approved organizational system.*

## 16.1 ROPA fields

- Activity and owner

- Controller/processor role

- Purpose

- People and data categories

- Lawful basis and Article 9/10 condition

- Recipients and processors

- Countries and transfer tool

- Retention and deletion

- Security measures

- Notice and rights process

- DPIA status

- Last review and next review

## 16.2 Rights-request register

- Request ID and receipt date

- Person and right

- Identity decision

- Scope clarification

- Systems, owners, and processors searched

- Legal review and redactions

- Extension or fee decision

- Response and secure delivery

- Completion date and outcome

## 16.3 DPIA screen

- Evaluation or scoring

- Automated decisions with significant effect

- Systematic monitoring

- Sensitive or highly personal data

- Large scale

- Matching datasets

- Vulnerable people

- New technology

- Prevents access to service or right

- Supervisory-authority list trigger

## 16.4 Breach fact sheet

| **Field**       | **Required information**                               |
|-----------------|--------------------------------------------------------|
| Awareness       | When the controller became aware and why               |
| Incident        | What happened and current containment                  |
| Data and people | Categories, approximate numbers, sensitivity, context  |
| Consequences    | Likely effects on people                               |
| Risk            | Likelihood, severity, high-risk analysis               |
| Decision        | Authority and person notification decisions            |
| Action          | Containment, recovery, protection, correction, lessons |
| Approval        | Decision owner, legal/DPO input, dates                 |

## 16.5 Manager pre-launch checklist

- Purpose and owner approved

- Scope and role analysis complete

- Lawful basis and sensitive-data condition recorded

- Notice accurate

- Fields and default settings minimized

- Rights and deletion tested

- Processor and transfer reviews complete

- Security risk assessed

- DPIA complete if needed

- Evidence and review date retained

# 17. GDPR, AI, and Analytics

*Applying established GDPR duties to models, training data, monitoring, and automated decisions.*

AI does not create an exception to GDPR. Start with the same questions: scope, roles, purpose, lawful basis, fairness, transparency, minimization, accuracy, rights, retention, security, transfers, and accountability. Then assess risks specific to the model and use case.

## 17.1 Practical review questions

- What personal data enters training, fine-tuning, retrieval, prompts, logs, evaluation, and output?

- Is the purpose compatible with the source and notice?

- Can people reasonably understand the processing and consequences?

- Could output reveal, infer, or falsely state sensitive facts?

- Is there solely automated decision-making with legal or similar significant effect?

- Can access, correction, objection, deletion, and restriction work in practice?

- What data leaves the organization or crosses borders?

- Does the DPIA cover model error, discrimination, security, misuse, and impacts on vulnerable people?

- What human review is meaningful, trained, authorized, and documented?

| **Do not assume:** Removing direct names may not make data anonymous. Pseudonymous data remains personal data when it can be linked back using additional information. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# 18. Glossary

*Plain-English definitions of important GDPR and privacy terms.*

**Accountability.** The duty to comply and be able to prove compliance.

**Anonymization.** Processing that makes a person no longer identifiable by reasonably likely means. Truly anonymous data falls outside GDPR.

**Binding corporate rules.** Approved internal transfer rules for groups of companies.

**Consent.** A freely given, specific, informed, and unambiguous indication of wishes through a statement or clear affirmative action.

**Controller.** The party deciding why and essential means of processing.

**Data protection impact assessment.** A written assessment of planned high-risk processing, necessity, proportionality, risks, and safeguards.

**Data protection officer.** An independent adviser and monitor required in certain cases or appointed voluntarily.

**Data subject.** The natural person the personal data relates to.

**EDPB.** The European Data Protection Board.

**International transfer.** Making personal data available to a recipient in a third country or international organization under Chapter V.

**Lawful basis.** An Article 6 ground that permits processing for a defined purpose.

**Legitimate interests assessment.** A documented purpose, necessity, and balancing analysis for Article 6(1)(f).

**Personal data.** Information relating to an identified or identifiable natural person.

**Personal data breach.** A security breach causing accidental or unlawful destruction, loss, alteration, unauthorized disclosure, or access.

**Processing.** Almost any operation performed on personal data, including collection, use, storage, disclosure, or deletion.

**Processor.** A party processing personal data for a controller.

**Profiling.** Automated processing used to evaluate certain personal aspects.

**Pseudonymization.** Separating identifying information so data cannot be linked to a person without additional information kept separately.

**ROPA.** Record of processing activities under Article 30.

**SCCs.** European Commission standard contractual clauses used as an appropriate transfer safeguard when their conditions are met.

**Special-category data.** Sensitive categories listed in Article 9.

**Supervisory authority.** An independent public privacy regulator.

**Transfer impact assessment.** A practical assessment of whether a transfer safeguard can work in the destination context and what extra measures are needed.

# 19. Subject Index

*An alphabetical guide to major topics. References point to sections so the index remains useful after editing.*

| **Topic**               | **Sections**   | **Topic**             | **Sections**   |
|-------------------------|----------------|-----------------------|----------------|
| Accountability          | 1, 3, 5, 9, 10 | Open-source tools     | 12             |
| AI and analytics        | 17             | Personal data         | 1, 2, 18       |
| Article 28 contract     | 5.2, 9.4       | Privacy by design     | 7.2, 9.4       |
| Automated decisions     | 4, 9.3, 17     | Processor             | 2.2, 5.2, 9.4  |
| Breach                  | 6, 9.4, 16.4   | Pseudonymization      | 6, 7, 18       |
| Consent                 | 3.2–3.3, 9.2   | Records of processing | 5.1, 9.4, 16.1 |
| Controller              | 2.2, 5, 9.4    | Retention             | 3.1, 5, 16     |
| Data minimization       | 3.1, 7.2       | Security              | 6, 9.4         |
| Data subject rights     | 4, 9.3         | Special-category data | 2.3, 3.3, 9.2  |
| DPIA                    | 7.1, 9.4, 16.3 | Supervisory authority | 6, 9.6–9.7     |
| DPO                     | 7.3, 9.4       | Table of contents     | How to Use     |
| International transfers | 8, 9.5         | Tools                 | 12             |
| Junior analyst          | 11, 13–15      | Transfer safeguards   | 8, 9.5         |
| Lawful bases            | 3.2, 9.2       | Vendor management     | 5.2, 8, 10     |

# 20. Official References and Further Study

*Authoritative law, EU guidance, and official project documentation used for verification and further study.*

[<u>EUR-Lex — Regulation (EU) 2016/679</u>](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)

[<u>EUR-Lex — GDPR summary updated March 2026</u>](https://eur-lex.europa.eu/EN/legal-content/summary/general-data-protection-regulation-gdpr.html)

[<u>European Data Protection Board</u>](https://www.edpb.europa.eu/edpb_en)

[<u>EDPB SME Data Protection Guide</u>](https://www.edpb.europa.eu/sme-data-protection-guide/home_en)

[<u>EDPB breach notification Guidelines 9/2022</u>](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-92022-personal-data-breach-notification-under_en)

[<u>European Commission — Data protection</u>](https://commission.europa.eu/law/law-topic/data-protection_en)

[<u>European Commission — Standard Contractual Clauses</u>](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en)

[<u>European Commission — Adequacy decisions</u>](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en)

[<u>ENISA — Handbook on Security of Personal Data Processing</u>](https://www.enisa.europa.eu/publications/handbook-on-security-of-personal-data-processing)

[<u>CISO Assistant documentation</u>](https://intuitem.gitbook.io/ciso-assistant)

[<u>OpenMetadata documentation</u>](https://docs.open-metadata.org/)

[<u>Microsoft Presidio documentation</u>](https://microsoft.github.io/presidio/)

[<u>ARX documentation</u>](https://arx.deidentifier.org/anonymization-tool/)

[<u>Keycloak documentation</u>](https://www.keycloak.org/guides)

[<u>Wazuh documentation</u>](https://documentation.wazuh.com/current/quickstart.html)

[<u>OWASP ZAP documentation</u>](https://www.zaproxy.org/getting-started/)

[<u>Trivy documentation</u>](https://trivy.dev/latest/)

[<u>Open Policy Agent documentation</u>](https://www.openpolicyagent.org/docs)

[<u>Klaro! documentation</u>](https://klaro.org/docs/)

[<u>Greenbone Community Edition documentation</u>](https://greenbone.github.io/docs/latest/)

| **Final reminder:** Law, guidance, technology, and facts change. Verify the official legal text, current EDPB and supervisory-authority guidance, Member State law, and qualified legal advice before acting on a real matter. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
