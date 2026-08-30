# Manual 13 Practitioner Evidence and Testing Appendix

## A. Control-to-risk worksheet
For every financially relevant technology control, record the financial-reporting risk, relevant process/account/disclosure, affected assertion or objective, system or data dependency, control owner, performer, frequency, evidence source, evidence retention location, control dependencies, exception path, and reassessment trigger. The worksheet should make it possible for a reviewer who did not design the control to understand why the control is in ICFR scope and how its failure could affect financial reporting.

A complete record should answer: What risk is being addressed? What event starts the control? What population is subject to the control? Who performs and reviews it? What evidence proves operation? How precise is the review? What happens when an exception is found? Which upstream or downstream controls depend on it? What change would require the control to be redesigned or retested?

## B. Access-control evidence pattern
For user access, retain request and approval evidence, role or entitlement granted, implementation timestamp, identity of the administrator, source-system record, periodic review decision, and any remediation. For privileged access, include business justification, time or scope limits where applicable, monitoring evidence, and recertification. For terminated users, demonstrate the population source and timeliness of removal rather than presenting a few screenshots without proof of completeness.

A reviewer should be able to reconcile the tested population to a reliable employee/contractor source, identify excluded identities and service accounts, and explain whether access inherited through groups, roles, federation, or application-specific permissions is included. Exceptions should be classified by cause and potential financial-reporting impact before remediation is closed.

## C. Change-management evidence pattern
For financially relevant changes, retain the approved request, risk/impact assessment, requirements or change description, test evidence, segregation between developer and production migration where required, approval to migrate, deployment record, rollback plan where relevant, and post-implementation validation. Emergency changes require a documented emergency basis and retrospective review within the organization’s defined timeframe.

For SaaS and low-code platforms, configuration changes may be as significant as source-code releases. Preserve audit trails, configuration snapshots, approval records, and evidence that changes to workflows, formulas, permissions, integrations, or reporting logic were evaluated for ICFR impact.

## D. Computer-operations evidence pattern
For scheduled processing, identify the expected job population, monitoring method, failure criteria, notification route, restart/rerun authority, reconciliation steps, and evidence of resolution. A successful scheduler status may be insufficient when financial completeness depends on record counts, control totals, interface acknowledgements, or downstream reconciliation.

Backup evidence should be evaluated in the context of the financial-reporting dependency. Demonstrating that backups run is different from demonstrating that critical financial data can be restored within needed recovery objectives. Where recovery controls support ICFR, retain test results, exceptions, remediation, and management review.

## E. Interface and reconciliation evidence pattern
For each material interface, document source and destination, frequency, record or value population, transfer mechanism, automated checks, rejected-record handling, duplicate prevention, reconciliation logic, thresholds, and ownership. Evidence should show both transmission and integrity where the financial-reporting risk requires it.

When a reconciliation is manual, define reviewer precision and escalation thresholds. When it is automated, identify the code/configuration, change controls, input completeness, error handling, and monitoring. If the interface is provider-managed, identify which control evidence is available from the provider and which controls remain the organization’s responsibility.

## F. IPE and report-reliance evidence pattern
When a control relies on a system-generated report or query, preserve evidence that the report is complete and accurate for the intended purpose. Record report name, system, owner, parameters, period, filters, data source, logic, and access restrictions. If report logic can change, identify the applicable change-control evidence.

For ad hoc queries or scripts, retain the exact query/script used and evidence of review. For dashboards, preserve the filters and date ranges used by the control performer. For spreadsheets, identify source data, formulas/macros, version, access, review, and reconciliation. A report title and screenshot are not sufficient when the underlying population cannot be reproduced.

## G. Service-organization reliance worksheet
For each service organization affecting ICFR, document the service, financially relevant processes/systems, report or assurance evidence reviewed, period covered, complementary user-entity controls, subservice organizations, exceptions, bridge-period considerations, incidents, and management conclusion. Do not equate receipt of a SOC report with automatic reliance.

Management should evaluate whether the report’s scope, system description, control objectives/criteria, period, auditor opinion, exceptions, and subservice treatment address the organization’s actual dependency. Unaddressed gaps require additional controls, alternative evidence, or risk acceptance/escalation by competent management.

## H. Testing workpaper minimums
A management testing workpaper should identify control ID, objective, risk, control description, owner, frequency, population source, period, test method, sample rationale where applicable, items tested, evidence examined, exceptions, conclusion, reviewer, review date, and follow-up. Separate design assessment from operating-effectiveness testing so a failure in one dimension is visible.

Testing should be reproducible. Another competent reviewer should be able to understand how the population was obtained, why selected items were tested, what evidence supported each attribute, and why the conclusion follows from the evidence. Unsupported statements such as “control operating effectively” are not sufficient workpaper evidence.

## I. Deficiency and remediation worksheet
Record the factual condition, control objective, affected process/system, duration, population potentially affected, compensating controls, root cause, immediate containment, corrective action, owner, due date, evidence required for closure, and retest plan. Keep factual observations separate from the ultimate significant-deficiency/material-weakness classification.

When multiple control failures share a common cause, evaluate them collectively. When a deficiency spans periods or systems, document how the affected population was bounded. Remediation closure should include evidence of implemented design and evidence of operation for a period appropriate to control frequency and risk.

## J. Change-triggered reassessment checklist
Reassess scope and control design after significant system implementation, ERP migration, acquisition/divestiture, cloud migration, major identity-platform change, outsourcing, finance-process redesign, new interface, material incident, repeated control exception, introduction of financially relevant AI/automation, or a change in authoritative requirements.

The reassessment record should identify the triggering event, affected accounts/processes/systems, changed risks, controls added/removed/modified, evidence impacts, testing required, and whether prior review evidence remains applicable. Material changes after publication-review freeze reopen only affected gates, but the affected scope must be bounded confidently.

## K. Practitioner scenario — privileged-access exception
A finance administrator receives elevated access to resolve a production issue and retains the role beyond the approved emergency window. The organization should identify the affected financial systems and capabilities, determine whether conflicting activities occurred, inspect logs and transactions as needed, remove or correct the access, assess related monitoring controls, record the exception, and determine whether broader population testing is required. Classification of the control issue remains a competent management/audit judgment.

## L. Practitioner scenario — report parameter error
A monthly reconciliation control uses a report generated with an incorrect date filter for two periods. The response should identify the affected reconciliations, reproduce the correct populations, assess whether errors could have been missed, determine whether other controls detected the issue, correct the report procedure or configuration, retest the control, and evaluate the deficiency using current authoritative criteria and organization-specific facts.

## M. Practitioner scenario — SaaS configuration change
A vendor changes a configurable financial workflow after a platform update. The organization should determine whether the change affected approval routing, access, calculation logic, interfaces, or evidence. It should obtain available provider information, compare tenant configuration, test the financially relevant workflow, update change/control documentation, and reassess any related service-organization reliance.

## N. Practitioner scenario — AI-assisted financial process
An AI-enabled tool proposes account classifications used in a financial close process. Controls should address approved use, input provenance, output review, model/tool changes, access, fallback, monitoring, exception handling, and evidence. Management should not assume that model confidence scores prove financial accuracy. The control design must specify how human reviewers validate results and how material anomalies are escalated.

## O. Release evidence checklist
A publication-ready Manual 13 package should contain exact controlled-source identity, authoritative-source verification evidence, trilingual source identity, generated DOCX/PDF artifacts, page-level QA results, accessibility/visual review evidence, artifact checksums, release manifest, workflow-security results, changed-scope reconciliation, and the applicable review decisions tied to the exact candidate and artifact hashes. Standing final release authorization is already established separately; no additional owner approval should be requested once all other required gates are genuinely green.
