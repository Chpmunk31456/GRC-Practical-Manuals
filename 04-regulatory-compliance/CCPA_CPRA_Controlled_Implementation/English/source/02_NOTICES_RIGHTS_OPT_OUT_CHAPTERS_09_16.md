# Manual 12 — CCPA / CPRA California Privacy Controlled Implementation
## Controlled English Source — Chapters 09–16

> Original training and implementation guidance for disclosures, consumer rights, opt-out, sensitive PI, minors, and financial incentives. Context-specific legal judgment remains required.

## Chapter 09 — Notice at collection

Provide required information at or before collection in a format appropriate to the interaction. Connect notices to actual categories collected, purposes, sensitive PI, retention, sale/sharing, and relevant rights.

Notice design should account for websites, mobile apps, offline collection, connected devices, forms, call centers, employees/applicants where covered, and other collection channels.

## Chapter 10 — Privacy policy and disclosure governance

Maintain a privacy policy that accurately describes current practices and applicable consumer rights. Establish ownership, versioning, legal review, accessibility, update triggers, evidence, and synchronization with data inventories and downstream relationships.

Material changes in purposes, sale/sharing, sensitive PI, ADMT, vendors, or rights operations should trigger policy-impact review.

## Chapter 11 — Consumer request intake and verification

Provide required methods for consumers to submit applicable requests and implement identity/authority verification proportionate to the request and data involved.

Maintain controls for authorized agents, household requests where applicable, minors, account and non-account contexts, suspicious requests, verification failure, and secure response delivery.

## Chapter 12 — Rights to know/access and data portability

Implement search, data aggregation, category/specific-information analysis, source/purpose/recipient identification, exception review, formatting, security, approval, timing, and delivery for applicable access/know requests.

Evidence should show which systems and downstream parties were searched, limitations applied, decisions made, and when the response was delivered.

## Chapter 13 — Deletion and correction

Route deletion and correction requests across relevant systems and service providers/contractors, apply documented exceptions where appropriate, validate downstream completion, and preserve evidence without unnecessarily retaining the data that should be deleted.

Correction workflows should address source-of-truth decisions, conflicting records, derived data, and re-propagation to dependent systems where required.

## Chapter 14 — Sale, sharing, and opt-out preference signals

Determine whether disclosures constitute sale or sharing under the applicable California definitions and operate opt-out mechanisms accordingly. Implement recognized opt-out preference signals in a manner consistent with current regulations and the organization’s processing model.

Testing should cover websites, apps, consent/choice platforms, advertising tags, SDKs, server-side flows, identity resolution, downstream parties, and post-opt-out behavior.

## Chapter 15 — Sensitive PI, minors, and special choice controls

Where applicable, implement the right to limit certain uses/disclosures of sensitive personal information and required notices or mechanisms. For minors, implement age-aware opt-in and consent processes consistent with applicable requirements.

Do not use dark patterns or interface designs that materially impair consumer choice.

## Chapter 16 — Financial incentives and rights fail-closed gate

Where financial incentives or price/service differences depend on personal information, maintain required notices, valuation or justification records, opt-in/withdrawal processes, and consistency with current legal requirements.

Do not pass the gate when notices materially diverge from practice, requests cannot be fulfilled end-to-end, opt-out preference signals are ignored, sensitive-PI controls are missing, or consumer choices are undermined by interface behavior.
