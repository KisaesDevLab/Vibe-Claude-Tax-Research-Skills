---
name: "Unreimbursed Partnership Expenses (UPE)"
slug: unreimbursed-partnership-expenses
type: Passthrough
tax_type: EFR
complexity: Low
irc_sections: ["§162", "§702", "§707"]
forms: ["Schedule E (Page 2 with K-1)"]
state_specific: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

## Overview

Partners often incur expenses personally that are connected to
partnership activities — vehicle expenses, home office, professional
development, supplies, etc. Whether these expenses are deductible
by the partner depends on:

1. **Partnership agreement provision.** If the partnership agreement
   requires the partner to pay these expenses without reimbursement
   (or expressly prohibits reimbursement), the partner may deduct
   them as Unreimbursed Partnership Expenses (UPE) on Schedule E
   (page 2, with K-1).

2. **Reimbursable expenses paid personally.** If the partnership
   would have reimbursed but the partner chose not to seek
   reimbursement, those expenses are NOT deductible — under §162,
   the partner cannot deduct expenses for which reimbursement was
   available but not sought (Klaassen v. Commissioner; Lucas v.
   Earl analysis).

3. **§67(g) post-TCJA suspension** — Through 2025 (and likely
   permanent under OBBBA), §67(g) suspended miscellaneous itemized
   deductions for individuals. UPE is NOT subject to §67(g)
   suspension because it's an above-the-line deduction reducing
   K-1 income, not a §212 / Schedule A miscellaneous itemized
   deduction. This makes UPE one of the few remaining mechanisms
   for partners to deduct personal expenses.

The strategy is particularly valuable for:
- Service partnerships (law firms, accounting, medical practices)
  where partners commonly pay travel, meals, vehicle, and home
  office expenses personally.
- Professional partnerships with no expense reimbursement policy.
- Real estate partnerships where individual partners manage their
  share of properties.

## Primary IRC authority

- §162(a) — Trade or business expenses.
- §702 — Income and credits of partner.
- §702(a)(4), (7), (8) — Specific items of partnership income/loss.
- §707 — Transactions between partner and partnership.
- §67(g) — Miscellaneous itemized deduction suspension (does NOT
  apply to UPE).

## Treasury regulations

- Reg §1.162-1.
- Reg §1.702-1 — Income and credits of partner.

## Key IRS guidance

- IRS Publication 541 — Partnerships.
- IRS Form 1040 instructions.
- Schedule E instructions (Part II).

## Key court decisions

- **Klaassen v. Commissioner, T.C. Memo. 1998-241** — Partner not
  entitled to deduct expenses for which partnership would have
  reimbursed but partner did not seek reimbursement.
- **Cropland Chemical Co. v. Commissioner, 75 T.C. 288 (1980)** —
  Partner deductibility of partnership-related expenses.
- **McLaulin v. Commissioner, T.C. Memo. 2017-204** — Partnership
  agreement provision requiring partner to bear expenses upheld.

## Eligibility requirements

1. **Partnership agreement requires** the partner to pay the
   expense without reimbursement (express or implied policy).
2. **Expense is ordinary and necessary** under §162.
3. **Expense is connected to partnership business.**
4. **Partner did not seek reimbursement** — must be required, not
   merely declined.
5. **Substantiation per §6001 (and §274(d) for vehicle/travel/
   M&E).**

## Mechanics — how it works

1. **Document partnership agreement provision.** Operating agreement
   should specifically address which categories of expenses are
   partner-borne.
2. **Track expenses** by category (vehicle, home office,
   professional development, etc.).
3. **Substantiate per category** (§274(d) for applicable
   categories).
4. **Report on Schedule E (Part II).** Net K-1 income reduced by
   UPE for each partnership; reported as separate line item.
5. **State coordination.** State return follows federal.

## Documentation requirements

- Partnership agreement provision documenting expense
  responsibility.
- §274(d) substantiation for vehicle, travel, M&E.
- Receipts and supporting records.
- Schedule E (Part II) UPE attachment.

## Common pitfalls / audit risks

- **No partnership agreement provision.** Without express
  requirement, IRS may argue reimbursement was available; deduction
  denied per Klaassen.
- **Reimbursable expenses claimed.** Even if reimbursement was
  available but not sought.
- **§274(d) substantiation failures.** Vehicle, travel, M&E.
- **Personal expenses claimed.** UPE applies only to genuine
  partnership-business expenses.
- **Self-employment tax interaction.** UPE reduces K-1 income;
  may reduce SE tax base for general partner allocations.

## Recent legislative changes

- **TCJA (2017)** — §67(g) suspension does NOT apply to UPE
  (because UPE is above-the-line on Schedule E, not §212
  miscellaneous itemized deduction).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §67(g) UPE
  Pub L 119-21]`. Working assumption: UPE preserved as above-the-
  line deduction.

## State conformity considerations

State conformity to UPE generally complete. State partnership
return adjustments follow federal.

## AICPA SSTS / Circular 230 considerations

Standard diligence; verify partnership agreement provision and
expense substantiation.

## Default confidence band rationale

**MODERATE** — fact-intensive depending on partnership agreement
provision strength. HIGH for partnerships with explicit expense
responsibility provisions; LOW for ad hoc claims without
underlying agreement.

## Cross-references

- `accountable-plan-home-office` (#2) — corporate alternative.
- `business-vehicle-usage` (#4).
- `cell-phone-expenses` (#5).
- `maximize-business-deductions` (#13).
- `family-limited-partnership` (#55).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 702","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section702","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Klaassen v. Commissioner, T.C. Memo. 1998-241","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"McLaulin v. Commissioner, T.C. Memo. 2017-204","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
