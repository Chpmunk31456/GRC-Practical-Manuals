# Appendix D — Prohibited-Practice Checklist

## Purpose

Use this checklist before approval, procurement, development, deployment, or material modification to identify AI practices that may be prohibited. Escalate every Yes or Uncertain answer for legal review. This checklist is an operational aid, not a substitute for the regulation or legal advice.

## Assessment information

- System or use case:
- Inventory ID:
- Business owner:
- Provider/vendor:
- Legal entities and jurisdictions:
- Intended purpose:
- Affected persons:
- Assessor and date:

## Screening questions

Answer Yes, No, or Uncertain and cite supporting evidence.

### Manipulation and exploitation

- Does the system use subliminal, purposefully manipulative, or deceptive techniques?
- Could those techniques materially distort behavior or impair informed decision-making?
- Could the system exploit vulnerabilities related to age, disability, or social or economic circumstances?
- Could use cause or be reasonably likely to cause significant harm?

### Social scoring and adverse treatment

- Does the system evaluate or classify people based on social behavior or personal characteristics?
- Could resulting treatment be unrelated to the context in which data was generated?
- Could treatment be unjustified or disproportionate?

### Predictive policing and criminal-risk assessment

- Does the system predict an individual’s risk of committing an offense based solely or primarily on profiling, personality, or personal characteristics?
- Is any assessment supported by objective, verifiable facts directly linked to criminal activity?

### Facial-image databases and biometric practices

- Does the system create or expand facial-recognition databases through untargeted scraping of images?
- Does it categorize people biometrically to infer sensitive characteristics?
- Does it perform real-time remote biometric identification in publicly accessible spaces for law-enforcement purposes?
- If an exception is claimed, are necessity, proportionality, authorization, scope, and safeguards documented?

### Emotion recognition

- Does the system infer emotions in workplaces or educational institutions?
- If used for medical or safety purposes, is that purpose genuine, necessary, and documented?

### Other high-concern practices

- Does the design indirectly achieve a prohibited outcome through proxies, combined features, or downstream use?
- Could configuration, repurposing, or user instructions enable a prohibited practice?
- Has the supplier contractually restricted prohibited uses and provided sufficient technical controls?

## Evidence reviewed

- Intended-purpose statement
- System design and model documentation
- Data sources and feature list
- User instructions and prompts
- Vendor documentation and contract
- Testing and demonstrations
- Deployment context and affected populations
- Legal analysis
- Monitoring and misuse controls

## Decision

Select one:

- No prohibited practice identified
- Additional evidence required
- Legal review required
- Use must be redesigned or restricted
- Deployment prohibited
- Existing deployment suspended or withdrawn

## Required controls

- Record the decision and legal basis.
- Apply technical and contractual use restrictions.
- Prevent unauthorized repurposing.
- Train users and approvers.
- Monitor for misuse, workarounds, and material changes.
- Reassess after changes to purpose, data, features, geography, provider, or affected population.

## Approval

**Legal reviewer:**  
**Compliance reviewer:**  
**Business owner:**  
**Decision:**  
**Conditions:**  
**Next review or trigger:**  
