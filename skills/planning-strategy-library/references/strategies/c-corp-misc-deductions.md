---
name: "C Corporation Specific Deductions and Planning"
slug: c-corp-misc-deductions
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§162", "§243", "§245A", "§163(j)", "§78"]
forms: ["Form 1120", "Form 1118"]
state_specific: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

## Overview

This file addresses C-corp-specific deductions and planning levers
that distinguish C corp tax from pass-through tax:

1. **§243 Dividends-Received Deduction (DRD).** C corp receiving
   dividends from another C corp deducts:
   - 50% of dividends if owns <20% of payer.
   - 65% if owns 20-79%.
   - 100% if owns 80%+ (consolidated returns).

2. **§245A Foreign Source DRD.** 100% DRD for dividends from 10%+
   owned foreign corporations.

3. **§163(j) interest deduction limit.** C corp limited to 30% of
   ATI. Excess interest carries forward. Small business exception:
   average gross receipts <$30M (indexed) exempt.

4. **§199A NOT available to C corps.**

5. **§170(b)(2) charitable contribution limit.** 10% of taxable
   income; excess carries forward 5 years.

6. **§267 related-party rules.** Loss disallowance and matching.

7. **§531 / §541 penalty taxes.** See #31.

8. **§78 gross-up.** Foreign tax credit users.

9. **Bad debt deduction (§166).** C corps use specific charge-off
   method; partial worthlessness allowed.

10. **§481(a) adjustments** for accounting method changes.

## Primary IRC authority

- §162 — Trade or business expenses.
- §163(j) — Interest deduction limit.
- §166 — Bad debts.
- §170(b)(2) — Corporate charitable contribution limit.
- §243 — DRD.
- §245A — Foreign DRD.
- §267 — Related-party loss disallowance.
- §481 — Accounting method change.
- §531, §541 — Penalty taxes.

## Treasury regulations

- Reg §1.162-1 through §1.162-29.
- Reg §1.163(j)-1 through §1.163(j)-11 — Interest limit.
- Reg §1.243-1 through §1.243-3 — DRD.
- Reg §1.245A-1 through §1.245A-12 — Foreign DRD.

## Key IRS guidance

- Notice 2018-28 — §163(j) initial guidance.
- Rev. Proc. 2020-22 — §163(j) accounting method changes.
- IRS Publication 542.

## Key court decisions

- **United States v. Generes, 405 U.S. 93 (1972)** — Bad debt
  business vs. nonbusiness analysis.

## Mechanics — how it works

1. **Annual planning review.** Survey available C corp deductions.
2. **§163(j) computation** — track ATI, interest deduction limit,
   carryforward.
3. **DRD planning** — coordinate inter-corporate distributions.
4. **Charitable contribution management** — track 10% limit,
   carryforward.
5. **§481(a) accounting method changes** — Form 3115.
6. **§78 gross-up** if FTC applicable.

## Common pitfalls / audit risks

- **§163(j) ATI computation errors.** Formula complex; small
  business exception eligibility (gross receipts test) must be
  verified.
- **DRD holding period.** §246(c) requires 45-day (or 90-day for
  preferred) holding period.
- **§267 related-party traps.** Loss disallowance until property
  is later sold.
- **§531 / §541 penalty taxes.**

## Recent legislative changes

- **TCJA (2017)** — Created §163(j) limit; changed DRD; 21% rate.
- **CARES Act (2020)** — Temporarily raised §163(j) ATI to 50%
  for 2019, 2020.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §163(j)
  §243 Pub L 119-21]`. Reports indicate possible §163(j) ATI
  formula reversion to EBITDA basis (pre-2022).

## State conformity considerations

State conformity to §163(j), §243, §245A varies. Many states
decouple from §163(j) ATI changes.

## Default confidence band rationale

**MODERATE** for §163(j) computations and DRD claims. HIGH for
routine items.

## Cross-references

- `c-corp-dividends` (#31).
- `c-corp-state-tax-savings` (#35).
- `section-1202-qsbs-extended` (#43).
- `income-shifting-to-c-corp` (#47).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 163(j)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section163","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 243","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section243","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 245A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section245A","weight":"primary_statute"}
  ]
}
```
