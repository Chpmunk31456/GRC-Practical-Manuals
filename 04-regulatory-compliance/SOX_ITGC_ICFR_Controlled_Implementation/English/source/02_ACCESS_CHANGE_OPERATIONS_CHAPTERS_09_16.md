# Manual 13 — SOX ITGC / ICFR Controlled Implementation

## Chapter 9 — Logical access governance
Define joiner, mover, leaver, privileged-access, service-account, emergency-access, and periodic-review controls for financially relevant systems. Link each access control to the risk it mitigates. Evidence should show request, approval, implementation, timely removal, reviewer decision, exceptions, and remediation. Generic IAM dashboards are supporting evidence only when they prove the relevant control population and period.

## Chapter 10 — Segregation of duties and privileged access
Identify incompatible duties that could permit unauthorized financial transactions, configuration changes, journal activity, master-data changes, or concealment of errors. Where technical segregation is impractical, document compensating controls and test them. Privileged access should be limited, approved, monitored, periodically reviewed, and tied to named responsibilities.

## Chapter 11 — Program change management
Require authorized requests, impact assessment, testing, approval, migration control, production access restrictions, and post-implementation evidence for financially relevant changes. Distinguish routine, standard, emergency, configuration, code, infrastructure-as-code, SaaS configuration, and vendor-managed changes. Emergency procedures should preserve traceability and retrospective approval.

## Chapter 12 — Development, acquisition, and implementation
For new systems and major implementations, define requirements, control design, data conversion, interface validation, user acceptance testing, access design, segregation, cutover, rollback, and post-go-live monitoring. Evidence should demonstrate that financially relevant requirements were tested and that migration did not compromise completeness or accuracy.

## Chapter 13 — Computer operations
Control scheduled jobs, batch processing, interfaces, backups, recovery, monitoring, failures, reruns, incident escalation, and operational changes. Evidence should demonstrate that exceptions are detected and resolved, not merely that monitoring tools exist. For cloud and SaaS services, identify which operational controls are retained by management and which depend on providers.

## Chapter 14 — Interfaces and data transfers
Inventory financially significant inbound and outbound interfaces. Define control points for completeness, accuracy, authorization, reconciliation, error handling, rejected records, duplicate prevention, and change management. Automated transfer success alone does not prove financial completeness; reconcile source and destination populations where the risk requires it.

## Chapter 15 — Reports and information produced by the entity (IPE)
Identify reports, queries, extracts, spreadsheets, dashboards, and calculations used in controls or financial reporting. Validate source data, parameters, logic, access, change history, and completeness/accuracy at a level appropriate to reliance. If a report is configurable, retain evidence of the exact parameters used for the control period.

## Chapter 16 — Spreadsheets and end-user computing
Classify financially relevant spreadsheets and EUC tools by risk. Apply ownership, access restriction, version/change control, formula protection or review, input validation, reconciliation, backup, and independent review proportionate to risk. Track critical macros, scripts, low-code automations, and linked data sources as technology dependencies when they influence ICFR.
