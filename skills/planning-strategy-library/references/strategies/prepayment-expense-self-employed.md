---
name: "Prepayment of Expense — Self-Employed (12-Month Rule)"
slug: prepayment-expense-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§461", "§263(a)"]
forms: ["Schedule C"]
state_specific: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Self-employed application of the 12-month rule prepayment strategy
(see #18 for full coverage). Reg §1.263(a)-4(f) allows cash-basis
taxpayers to deduct prepaid expenses if the right or benefit does
not extend beyond the earlier of (a) 12 months after the first
date on which the right or benefit begins or (b) the end of the
following tax year.

For Schedule C taxpayers, this is a primary year-end planning
lever. December prepayments of:
- Insurance (next year's annual premium).
- Rent on business space (12 months in advance).
- Subscriptions and software annual renewals.
- Service contracts.
- Professional dues and memberships.
- Continuing education registration fees.

create current-year deductions reducing both income tax base AND
SE tax base.

§448 cash method threshold: TCJA increased small-business cash-
method threshold to $25M average annual gross receipts (now
indexed to ~$30M for 2024). Most Schedule C filers use cash method.

## Primary IRC authority

- §461 — General timing rule.
- §263(a) — Capital expenditures.
- §446 — Methods of accounting.
- §448 — Cash method limitations.
- §461(g) — Prepaid interest (not deductible in advance).

## Treasury regulations

- Reg §1.263(a)-4(f) — 12-month rule.
- Reg §1.461-1 — Timing.

## Key IRS guidance

- IRS Publication 538 — Accounting Periods and Methods.

## Eligibility requirements

For cash-basis self-employed:
1. Right or benefit does not extend beyond earlier of 12 months
   after benefit begins or end of following tax year.
2. Payment is for non-tax-shelter expenditure.
3. Item is not specifically capitalized under another rule.

## Mechanics — how it works

1. **Year-end planning review** — identify upcoming prepayable
   expenses.
2. **Prepay before December 31.**
3. **Deduct full amount on Schedule C.**
4. **Reduces income tax AND SE tax base.**

## Documentation requirements

- Vendor invoices showing service period.
- Payment records dated current year.

## Common pitfalls / audit risks

- **Benefit extends beyond 12 months.** Two-year service contract
  in advance does not qualify.
- **Prepaid interest under §461(g).** Must spread over loan period.
- **Tax shelter taxpayer.** §461(i) imposes accrual.

## Recent legislative changes

- **TCJA (2017)** — Increased small-business cash-method threshold.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §461 §448
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — clear regulatory safe harbor.

## Cross-references

- `prepayment-of-expense` (#18) — corporate context.
- `maximize-business-deductions` (#13).
- `accountable-plan-self-employed` (#84).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 461","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section461","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.263(a)-4(f)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"}
  ]
}
```
