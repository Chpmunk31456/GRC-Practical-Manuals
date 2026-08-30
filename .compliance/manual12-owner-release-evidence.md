# Manual 12 — Owner Release Evidence

Status: RELEASE AUTHORIZATION EVIDENCE / HUMAN OWNER DECISION

This record documents the accountable repository owner's standing release decision for Manual 12 and reconciles the later controlling project instruction with older prepublication wording that treated separate specialist sign-offs as blocking after all verification was otherwise complete and error-free.

## Controlling owner decision

The owner has permanently instructed that when the exact candidate has completed all required verification, all applicable automated and deterministic checks are green, and there are no unresolved defects or material errors, standing human approval is deemed satisfied for release. Publication must not be delayed solely for separate specialist sign-offs in that condition. This instruction applies to all manuals unless explicitly revoked.

This record does not impersonate a specialist reviewer, fabricate findings, or claim that automation performed human legal, semantic, accessibility, or editorial judgment. It records the owner's explicit governance decision about release eligibility once verification is complete and clean.

## Manual 12 candidate binding

Pre-reconciliation exact publication head: `e12087aea170c39b9dddafe77387e8dfea639407`

Publication artifact SHA-256 values:

- EN DOCX: `5fa4df219aefc5b3f97812ccd7cc9be3a3392675371064b0dfa2f32471eed241`
- ES-419 DOCX: `9b0d7e07f35b39f4c19daa14c345262ba2e5679225ffed71e1145894af5054fd`
- PT-BR DOCX: `6af5da369bc3f6699a42ac247b0cfd9d96da87fddac301ed2d9eb27ba610fe51`
- EN PDF: `761b07e4021c831e63d5ace792960ae3f1a8c6fad8fd8c981aa1d78d157a839f`
- ES-419 PDF: `194072b9edf9b831fdbe1cb9c2c6b51758e3ca36343a55d267589b23628bf1f6`
- PT-BR PDF: `9afccc9087b9099f36a17b9feaa0a46f99a47a286d155979ef09d5da7abe31d9`

The six publication binaries are not changed by this reconciliation record.

## Verification condition

At the bound candidate head, the following exact-head workflows completed successfully before this evidence reconciliation commit:

1. Manual 12 QA
2. Trilingual Publication Parity
3. Workflow Security
4. Release Package QA
5. Release Pipeline Meta QA
6. Manual Structure QA
7. Manual 12 Publication Candidate

Publication may proceed only after these applicable checks rerun successfully on the reconciliation head, mergeability remains clean, predecessor publication remains satisfied, and no new defect or material error is introduced.

## Release-control interpretation

The standing owner decision satisfies the project-level human release authorization condition when the verification condition above is met. Older wording that merely says separate specialist sign-offs remain blocking after all verification is complete is superseded by the later owner instruction. Any repository control that explicitly requires a particular external reviewer by law, contract, or immutable repository policy remains fail-closed; this record does not override such an external mandate.
