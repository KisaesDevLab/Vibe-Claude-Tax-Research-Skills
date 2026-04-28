# DAWSON Today's Opinions / Today's Orders — freshness signals

## Source

DAWSON (Tax Court e-filing system):
- Today's Opinions: https://dawson.ustaxcourt.gov/todays-opinions
- Today's Orders: https://dawson.ustaxcourt.gov/todays-orders

## Purpose

Free-source citation discipline of this skills pack cannot detect
implicit overrules with the same coverage as a commercial citator
(KeyCite, Shepard's, BCite). DAWSON's daily feeds are one of the
mitigations the pack relies on for FRESHNESS signals on Tax Court
authority.

The other mitigation is the Federal Register IRS feed for new TDs
and proposed regs — see `shared/sources.json` and
`shared/legislation-tracking.md`.

## Workflow

When citing a Tax Court opinion (Regular, Memorandum, or Summary)
from beyond the past 90 days:

### 1. Search DAWSON

Open DAWSON Today's Opinions and Today's Orders for the past 30
days. Look for:
- New opinions citing the case at issue.
- New orders modifying or vacating the case.
- New decisions on motions for reconsideration.

### 2. Check the case docket

For high-stakes citations, look up the case docket directly on
DAWSON. The docket reveals:
- Pending motions.
- Withdrawal of motions.
- Stipulated decisions.
- Appeals status.

### 3. Cross-check Court of Appeals

Tax Court decisions are appealable to the Court of Appeals under
§7482. A reversal or modification on appeal cancels the Tax Court
holding. Use:
- DOJ Tax Division "Tax Appellate Blog" for appeals tracking
  (persuasive_non_authority for trend; not authority).
- Court of Appeals websites for each circuit.
- CourtListener (https://www.courtlistener.com) for full-text
  free access.

### 4. Document the freshness check

In the JSON sidecar, note:
- `retrieved_date` (when the case text was retrieved).
- `dawson_check_date` (when the freshness feeds were consulted).
- `negative_treatment_review_required: true` for high-stakes
  positions.

For PRACTITIONER files, document the date the freshness check was
performed.

## Limitations

DAWSON's freshness feeds DO NOT cover:
- Implicit overrules by Court of Appeals decisions in unrelated
  cases.
- District Court / Court of Federal Claims decisions inconsistent
  with Tax Court.
- IRS Action on Decision (AOD) issuances disagreeing with Tax
  Court.
- Treasury Decisions (TDs) superseding the Tax Court's
  interpretive framework.

For comprehensive negative-treatment review, the practitioner must
manually:
- Read the case in light of subsequent IRS guidance.
- Cross-check against Federal Register IRS issuances.
- Consider whether legislative changes superseded the holding.
- Engage a commercial citator for high-stakes positions.

## Federal Register IRS feed (companion)

URL: https://www.federalregister.gov/agencies/internal-revenue-service

Use:
- New Treasury Decisions (TDs) and proposed regulations.
- Notices of public hearing.
- Withdrawal of proposed regulations.

The feed publishes daily. Subscribe via the Federal Register's
notification service for real-time updates.

## Non-authority blog feeds (informational only)

These are `weight: not_authority` or `persuasive_non_authority` at
most:
- TaxProf Blog: https://taxprof.typepad.com/
- Procedurally Taxing: https://procedurallytaxing.com/
- Tax Appellate Blog (Robert S. Horwitz): https://www.taxlitigator.com/

Useful for trend signals but MUST NOT drive a confidence band or
serve as the closest authority.

## Practitioner freshness checklist

For each Tax Court citation older than 90 days:

- [ ] Cross-checked DAWSON Today's Opinions (last 30 days).
- [ ] Cross-checked DAWSON Today's Orders (last 30 days).
- [ ] Checked case docket for pending motions / appeals.
- [ ] Searched Court of Appeals for the binding circuit.
- [ ] Searched CourtListener for cross-circuit treatment.
- [ ] Searched Federal Register IRS feed for relevant TDs / regs.
- [ ] Noted any AOD or IRS guidance disagreeing.
- [ ] For high-stakes: engaged commercial citator.
- [ ] Documented freshness-check date in audit-defense file.
- [ ] Flagged `negative_treatment_review_required: true` in
  sidecar.
