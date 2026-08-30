# Manual 14 — PCI DSS Implementation Paths

## Essential path
For smaller or lower-complexity environments that still require disciplined PCI DSS scoping and evidence. Minimum outputs: CDE scope statement, data-flow diagram, asset inventory, responsibility matrix, core configuration standards, access/MFA evidence, vulnerability evidence, logging evidence, incident-response evidence, third-party attestations, and remediation register.

## Structured path
For organizations with multiple applications, service providers, business units, or formal compliance operations. Adds control ownership, evidence calendars, change-driven reassessment, service-provider dependency mapping, secure-development evidence, penetration-test governance, exception/compensating-control records, and management reporting.

## Enhanced path
For complex enterprises, high transaction volumes, hybrid/multi-cloud environments, extensive third-party dependencies, or environments requiring continuous assurance. Adds automated evidence collection where appropriate, continuous control monitoring, risk-based sampling, dependency graphing, control-health metrics, integrated GRC workflows, and formal management assurance.

## Evidence object schema
Every control implementation should record:

- requirement/control objective
- applicability and scope
- accountable owner
- responsible operator
- implementation procedure
- operating frequency
- evidence artifact
- evidence repository/location
- retention expectation
- reviewer/test procedure
- result/status
- exception or compensating-control reference
- remediation owner/date
- reassessment trigger

## Decision controls
The controlled manual must explicitly separate:

- defined approach vs customized approach where applicable;
- underlying security requirements vs SAQ/ROC/AOC validation instruments;
- PCI DSS requirements vs adjacent PCI standards;
- PCI DSS obligations vs contractual/acquirer/payment-brand requirements;
- PCI DSS requirements vs jurisdiction-specific law;
- technical remediation vs formal exception/compensating-control governance.

## Publication rule
Implementation-path maturity must never be represented as certification status. Publication requires exact-candidate QA, durable artifacts, provenance, release-registry reconciliation, and sequential predecessor clearance.