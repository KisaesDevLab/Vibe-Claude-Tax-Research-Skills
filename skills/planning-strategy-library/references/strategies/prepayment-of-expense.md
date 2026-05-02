---
name: "Prepayment of Expense (12-Month Rule)"
slug: prepayment-of-expense
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§461", "§263(a)"]
forms: ["Schedule C / Form 1120-S / Form 1120 / Form 1065"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

The "12-month rule" under Reg §1.263(a)-4(f) allows a cash-basis
taxpayer to deduct certain prepaid expenses in the year of payment
(rather than capitalize and amortize) if the right or benefit does
not extend beyond the earlier of (a) 12 months after the first date
on which the right or benefit begins or (b) the end of the
following tax year.

This is a year-end planning lever: cash-basis businesses can
accelerate deductions by prepaying expenses for the next 12 months
in December. The deduction is allowed in the current year, even
though the benefit is consumed over the following year.

Common applications:
- Insurance (12 months of premiums paid in December for next
  year's coverage).
- Rent (one year's rent paid in advance — but watch §467 deferred
  rent issues for unreasonably front-loaded leases).
- Subscriptions and memberships (annual renewal paid in advance).
- Service contracts (12-month term).

For accrual-basis taxpayers, the analysis is different: economic
performance under §461(h) generally must occur before the deduction
is allowed, regardless of payment. The recurring-item exception
under §461(h)(3) may permit deduction in the year payment is made
even if economic performance occurs in the following year, provided
the item is recurring, the all-events test is met, and the deduction
matches reasonably with income.

## Primary IRC authority

- **§461** — General rule for taxable year of deduction.
- **§263(a)** — Capital expenditures.
- **§446** — Methods of accounting (cash vs. accrual).
- **§448** — Limitations on use of cash method.
- **§461(g)** — Prepaid interest (NOT deductible in advance —
  spread over period to which it applies).
- **§467** — Deferred rent and certain rents.
- **§163(d)** — Investment interest limitations.

## Treasury regulations

- **Reg §1.263(a)-4(f)** — 12-month rule for prepaid expenses.
- **Reg §1.461-1** — General timing rules.
- **Reg §1.461-4** — Economic performance.
- **Reg §1.461-5** — Recurring item exception.

## Key IRS guidance

- **Rev. Proc. 2002-65** — Trade discounts.
- IRS Publication 538 — Accounting Periods and Methods.

## Key court decisions

- **Encyclopedia Britannica, Inc. v. Commissioner, 685 F.2d 212 (7th
  Cir. 1982)** — Capitalization of expenditures with future benefit.
- **U.S. Freightways Corp. v. Commissioner, 270 F.3d 1137 (7th Cir.
  2001)** — Trucking permits with 12-month terms; deductible under
  recurring-item exception.

## Eligibility requirements

Cash-basis taxpayer:
1. Right or benefit does not extend beyond the earlier of:
   - 12 months after the first date on which the right or benefit
     begins, OR
   - The end of the tax year following the year of payment.
2. Payment is for a non-tax-shelter expenditure.
3. Item is not specifically capitalized under another rule (e.g.,
   §263A, §195 startup costs).

Accrual-basis taxpayer:
1. Same all-events test under Reg §1.461-1(a)(2)(i).
2. Economic performance under §461(h) and Reg §1.461-4.
3. Recurring item exception under §461(h)(3) may allow recurring
   items to be deducted before economic performance.

## Mechanics — how it works

1. **Year-end planning review.** Identify prepaid expenses with
   12-month-rule eligibility.
2. **Prepay before year end.** Pay vendor/insurer/landlord by Dec.
   31.
3. **Deduct full amount on current-year return** as ordinary
   business expense.
4. **Coordinate with §263A** if applicable.
5. **For accrual taxpayers:** apply economic performance rules;
   recurring item exception may allow similar acceleration.

## Documentation requirements

- Vendor invoices showing service period.
- Payment records (canceled check, ACH confirmation, credit card
  statement) dated current year.
- For insurance: policy declarations showing coverage period.
- For rent: lease showing rental period.

## Common pitfalls / audit risks

- **Benefit extends beyond 12 months.** Two-year service contract
  paid in advance does not qualify.
- **Prepaid interest under §461(g).** Must be spread over loan
  period regardless of cash payment.
- **Tax shelter taxpayer disqualification.** §461(i) imposes accrual
  method on tax shelters.
- **§267 related-party transactions.** Different rules apply.
- **Economic performance for accrual taxpayers.** Without economic
  performance (e.g., services not yet rendered), accrual taxpayer
  cannot deduct.

## Recent legislative changes

- **TCJA (2017)** — Increased small-business cash-method threshold
  to $25M average annual gross receipts (now indexed; ~$30M for
  2024). More businesses qualify for cash method.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §448 §461
  Pub L 119-21]`. Working assumption: no material changes.

## State conformity considerations

State conformity to federal cash/accrual treatment is generally
complete.

## AICPA SSTS / Circular 230 considerations

Standard practitioner diligence; routine year-end planning lever.

## Default confidence band rationale

**HIGH** — clear regulation (Reg §1.263(a)-4(f)) and well-
established practice. Drops to MODERATE for benefits at the 12-
month boundary.

## Cross-references

- **`maximize-business-deductions`** (#13) — broader framework.
- **`startup-cost-optimization`** (#27) — coordinate with §195.
- **`prepayment-expense-self-employed`** (#91) — Schedule C variant.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 461",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section461",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.263(a)-4(f)",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.461-5",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "CtAppeals",
      "citation": "U.S. Freightways Corp. v. Commissioner, 270 F.3d 1137 (7th Cir. 2001)",
      "url": "https://www.courtlistener.com",
      "weight": "binding_circuit"
    }
  ]
}
```
