# Appendix E — High-Risk Classification Worksheet

> **Legal status:** Corrected English master. This file controls over earlier Appendix E language. Classification must be based on the current consolidated EU AI Act, the actor’s actual conduct, the system’s intended purpose, the relevant Annex route, and the applicable application date. Qualified legal review is required for uncertain or materially consequential classifications.

## Purpose

Use this worksheet to determine whether an AI system is high-risk under Article 6 and Annex I or Annex III, whether an Article 6(3) exception is claimed, whether profiling prevents reliance on that exception, and which legal and operational consequences follow.

Complete the assessment before production deployment or market placement and repeat it after material changes, repurposing, new jurisdictions, new affected populations, changed human oversight, supplier changes, or legal developments.

## 1. Assessment record

| Field | Response |
|---|---|
| System name | |
| Inventory ID | |
| Legal entity assessed | |
| Actor role or roles | |
| Business owner | |
| Technical/product owner | |
| Provider/vendor | |
| Product integration | |
| Version, configuration, prompts, tools, and data assessed | |
| Intended purpose | |
| Actual or proposed use | |
| Users and affected persons | |
| Jurisdictions | |
| Assessment owner and date | |
| Legal reviewer | |
| Current consolidated legal source and date | |

## 2. Intended-purpose and decision-context analysis

Document:

- the approved intended purpose;
- actual and reasonably foreseeable use;
- the business or public process supported;
- decisions, recommendations, predictions, classifications, rankings, or actions produced;
- whether the system makes, materially influences, prepares, supports, or merely records a decision;
- users, decision-makers, affected persons, and vulnerable groups;
- consequences of error, bias, delay, misuse, unavailability, or manipulation;
- human-review authority, timing, competence, and ability to override;
- whether the use affects employment, education, credit, insurance, essential services, healthcare, safety, law enforcement, migration, justice, democratic processes, or another material opportunity or right.

## 3. Article 6(1) and Annex I pathway

| Question | Yes/No/Uncertain | Evidence and rationale |
|---|---|---|
| Is the AI system itself a product covered by Annex I legislation? | | |
| Is it a safety component of a product covered by Annex I legislation? | | |
| Is the product required to undergo third-party conformity assessment under the applicable Annex I legislation? | | |
| Which legal entity is the relevant provider or product manufacturer? | | |
| Which product legislation, conformity route, and notified-body requirements apply? | | |
| Does failure of the AI component create a material health or safety risk? | | |
| What application date, legacy-system rule, or transitional provision controls? | | |

**Article 6(1) conclusion:**  
**Applicable Annex I legislation:**  
**Conformity implications:**  

## 4. Article 6(2) and Annex III pathway

For each Annex III category, record the exact point, intended use, affected persons, decision or process influenced, evidence, and conclusion.

| Annex III area | In scope? | Exact point | Intended use and affected persons | Rationale and evidence |
|---|---|---|---|---|
| Biometrics | | | | |
| Critical infrastructure | | | | |
| Education and vocational training | | | | |
| Employment, recruitment, worker management, or access to self-employment | | | | |
| Essential private and public services and benefits | | | | |
| Law enforcement | | | | |
| Migration, asylum, and border control | | | | |
| Administration of justice and democratic processes | | | | |

Do not infer Annex III status from a sector label alone. Match the actual intended use to the exact listed category and point.

## 5. Material-influence and human-review analysis

| Question | Response and evidence |
|---|---|
| Does the system make or materially influence a decision? | |
| Is the output presented as a recommendation but routinely followed? | |
| Is meaningful human review performed before the decision takes effect? | |
| Can the reviewer understand the basis, limitations, and uncertainty of the output? | |
| Can the reviewer challenge, disregard, override, or stop the system without penalty or automation bias? | |
| Is sufficient time, staffing, competence, and information available for review? | |
| Are affected persons exposed to legal, economic, safety, service-access, employment, educational, or fundamental-rights consequences? | |
| Are overrides, appeals, and disagreements logged and monitored? | |

Human participation does not automatically remove high-risk status.

## 6. Article 6(3) exception analysis

An Annex III-listed system is not excluded merely because a human participates or the provider characterizes the function as administrative. Test every statutory condition and document the facts.

| Test | Response | Evidence |
|---|---|---|
| Does the system pose a significant risk of harm to health, safety, or fundamental rights? | | |
| Does it materially influence the outcome of decision-making? | | |
| Is the system limited to a narrow procedural task? | | |
| Does it improve the result of a previously completed human activity without replacing or materially influencing that result? | | |
| Does it detect decision-making patterns or deviations without replacing or influencing the prior human assessment? | | |
| Does it perform a preparatory task that does not materially influence the outcome? | | |
| Does the system perform profiling of natural persons? | | |
| Are all relied-upon facts, safeguards, and limitations stable in production? | | |

**Profiling caveat:** Where the system performs profiling of natural persons within the statutory rule, do not rely on the Article 6(3) exception without qualified legal confirmation.

**Claimed exception basis:**  
**Facts supporting the exception:**  
**Residual risk and safeguards:**  
**Legal conclusion:**  

## 7. Classification conclusion

- [ ] High-risk under Article 6(1)/Annex I
- [ ] High-risk under Article 6(2)/Annex III
- [ ] Annex III system meeting every documented Article 6(3) exception condition
- [ ] Not high-risk on the verified facts
- [ ] Outside current scope
- [ ] Uncertain — additional evidence required
- [ ] Uncertain — qualified legal review required

### Final rationale

Document the exact legal route, facts, intended purpose, actor role, affected persons, application date, assumptions, uncertainties, and evidence supporting the conclusion.

## 8. Consequence mapping

Record applicable duties by actor and date.

| Obligation | Actor | Applies? | Application date | Owner | Evidence/status |
|---|---|---|---|---|---|
| Quality-management system | | | | | |
| Risk-management system | | | | | |
| Data and data governance | | | | | |
| Technical documentation | | | | | |
| Logging and recordkeeping | | | | | |
| Transparency and instructions for use | | | | | |
| Human oversight | | | | | |
| Accuracy, robustness, cybersecurity, and resilience | | | | | |
| Conformity assessment | | | | | |
| Notified-body involvement | | | | | |
| EU declaration of conformity | | | | | |
| CE marking | | | | | |
| Registration | | | | | |
| Deployer monitoring and log retention | | | | | |
| Worker information or consultation | | | | | |
| Fundamental-rights impact assessment | | | | | |
| Data-protection impact assessment | | | | | |
| Post-market monitoring | | | | | |
| Serious-incident reporting | | | | | |
| Corrective action, restriction, recall, or withdrawal | | | | | |
| Authority cooperation and access | | | | | |

## 9. Required follow-up

| Action | Owner | Due date | Status | Closure evidence |
|---|---|---|---|---|
| | | | | |

No internal readiness decision may substitute for a legally required conformity assessment, registration, declaration, CE marking, notified-body process, authority decision, or sector approval.

## 10. Review triggers

Reassess after:

- intended-purpose or actual-use change;
- actor-role, branding, own-name placement, or legal-entity change;
- model, version, data, prompt, tool, workflow, interface, or autonomy change;
- new provider, vendor, subprocessor, or open-source component;
- change in human oversight, staffing, authority, or decision process;
- new affected population, sector, product, or jurisdiction;
- incident, complaint, bias finding, audit issue, or failed acceptance criterion;
- substantial modification or repurposing;
- conformity-route or product-law change;
- legal, regulatory, implementing-act, authority, standard, or code change.

## GlobalWay Travel Services example

GlobalWay assesses an employee-allocation system used to rank workers for assignments. The intended use maps to an Annex III employment category. Although managers approve final assignments, testing shows that the ranking materially influences decisions and is rarely overridden. The supplier also performs profiling. GlobalWay classifies the system as high-risk, blocks release until the applicable provider and deployer duties are mapped, and initiates documentation, testing, oversight, FRIA/DPIA, conformity, monitoring, and supplier-remediation work.

## Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Qualified legal reviewer | | | |
| Compliance/risk | | | |
| Business owner | | | |
| Technical/product owner | | | |
| Product-safety or sector specialist, where applicable | | | |

**Assumptions and uncertainty:**  
**Evidence references:**  
**Conditions or restrictions:**  
**Next review trigger/date:**  
**Assessment version:**  

## Primary legal references

- Regulation (EU) 2024/1689, as amended: Article 6, Annex I, Annex III, relevant definitions, actor duties, high-risk requirements, conformity, registration, monitoring, incident, corrective-action, and enforcement provisions.
- Regulation (EU) 2026/1744 where applicable, including amended timing and transitional treatment.
- Applicable Annex I product legislation and national or sector law.
- Current consolidated EUR-Lex text and official product-law sources control over internal summaries.