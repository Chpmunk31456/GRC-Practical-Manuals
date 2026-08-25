# AG-01 — Human Approval Before Consequential Actions

**Control objective:** Ensure consequential AI-agent actions require a qualified human decision before execution where the risk, legal effect, financial impact, safety impact, rights impact, or irreversibility warrants approval.

**Control owner:** ____________________  
**System / use case:** ____________________  
**Business owner:** ____________________  
**Review frequency:** At least annually and after material change or incident.

## Implementation
- Define consequential-action categories and approval thresholds.
- Identify named reviewer roles with sufficient competence and authority.
- Prevent execution until required approval is recorded.
- Preserve the action parameters presented to the approver.
- Re-approve if material parameters change after approval.

## Required evidence
- approved action-classification matrix;
- reviewer RACI and competency records;
- approval workflow configuration;
- sampled approval records;
- rejected/escalated action records;
- exceptions and corrective actions.

## Audit test
1. Select a sample of consequential agent actions.
2. Verify each action was classified correctly.
3. Verify an authorized reviewer approved before execution.
4. Confirm approved parameters match executed parameters.
5. Confirm exceptions were logged and remediated.

## Exceptions / findings
| Date | Exception or finding | Risk | Owner | Due date | Status |
|---|---|---|---|---|---|
| | | | | | |

## Framework mapping
- EU AI Act: human-oversight, transparency, logging, risk-management implementation support where applicable.
- ISO/IEC 42001: map to applicable governance, operational-control, competence, and monitoring requirements after licensed-source verification.
- NIST AI RMF: Govern / Map / Manage implementation support.
- NIST CSF 2.0: Govern and Protect implementation support.

> Mapping statements are implementation crosswalks, not claims of automatic legal compliance or certification.
