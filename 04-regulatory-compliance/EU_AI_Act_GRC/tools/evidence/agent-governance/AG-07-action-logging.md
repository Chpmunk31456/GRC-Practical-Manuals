# AG-07 — Agent Action Logging

**Control objective:** Maintain reliable records of material AI-agent actions sufficient to reconstruct what happened, who or what authorized it, what resources were affected, and the outcome.

**Control owner:** ____________________  
**System / use case:** ____________________  
**Review frequency:** Continuous collection; periodic review based on risk.

## Implementation
- Log material tool calls, approvals, denials, execution results, errors, and escalations.
- Record actor/agent identity, timestamp, target resource, action type, authorization basis, and outcome.
- Protect logs against unauthorized alteration and inappropriate access.
- Define retention based on legal, contractual, operational, and risk requirements.
- Monitor logging failures as control failures.

## Required evidence
- logging specification and event schema;
- representative log extracts;
- retention configuration;
- access-control records for logs;
- integrity-monitoring results;
- logging-failure alerts and remediation.

## Audit test
1. Sample material agent actions and trace them end to end.
2. Verify required event fields are captured.
3. Confirm logs link actions to authorization and outcome.
4. Test access restrictions and retention controls.
5. Review logging gaps and corrective actions.

## Exceptions / findings
| Date | Exception or finding | Risk | Owner | Due date | Status |
|---|---|---|---|---|---|
| | | | | | |

## Framework mapping
- EU AI Act: record-keeping/logging and oversight implementation support where applicable.
- ISO/IEC 42001: map after licensed-source verification.
- NIST AI RMF: Measure / Manage.
- NIST CSF 2.0: Detect / Govern.
