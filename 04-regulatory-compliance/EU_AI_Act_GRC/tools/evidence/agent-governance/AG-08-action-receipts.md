# AG-08 — Post-Action Receipts and Traceability

**Control objective:** Provide a clear post-action record for consequential agent activity showing what occurred, when, under what authority, and what recovery or escalation options exist.

**Control owner:** ____________________  
**System / use case:** ____________________  
**Review frequency:** At least annually and after workflow changes.

## Implementation
- Generate a receipt for consequential actions.
- Include action, target, timestamp, authorization basis, result, and responsible owner where appropriate.
- Link the receipt to supporting logs and approval evidence.
- Provide accurate undo/recovery information only where technically valid.
- Retain receipts according to the applicable evidence-retention rule.

## Required evidence
- receipt specification;
- sampled receipts;
- linkage to approval/log records;
- retention configuration;
- recovery or escalation records.

## Audit test
1. Sample consequential actions.
2. Verify a complete receipt exists.
3. Reconcile receipt fields to underlying logs and approvals.
4. Confirm recovery claims are accurate.
5. Verify retention and access controls.

## Exceptions / findings
| Date | Exception or finding | Risk | Owner | Due date | Status |
|---|---|---|---|---|---|
| | | | | | |

## Framework mapping
- EU AI Act: transparency, logging, accountability, and human-oversight implementation support where applicable.
- ISO/IEC 42001: map after licensed-source verification.
- NIST AI RMF: Govern / Measure / Manage.
- NIST CSF 2.0: Govern / Detect / Respond.
