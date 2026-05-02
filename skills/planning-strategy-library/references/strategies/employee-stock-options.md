---
name: "Employee Stock Options (ISO, NQSO, RSU, ESPP)"
slug: employee-stock-options
type: Personal - Other
tax_type: EFR
complexity: High
irc_sections: ["§83", "§421", "§422", "§423", "§409A", "§3121(v)"]
forms: ["Form 3921 (ISO)", "Form 3922 (ESPP)", "Schedule D", "Form 6251 (AMT)"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

> **Caution:** Stock-based compensation has multiple tax landmines:
> AMT exposure on ISO exercise; §83(b) election timing for
> restricted stock; §409A discount-stock-option penalties; and
> wash sale rules on RSU sales coordinated with same-day exercises.
> Errors are common and expensive.

## Overview

Four primary equity compensation forms with distinct tax treatment:

**1. Incentive Stock Options (ISOs) — §422:**
- Grant: no income.
- Exercise: no regular income; AMT preference for spread (FMV at
  exercise minus exercise price).
- Sale: capital gain (long-term if held 2 years from grant + 1 year
  from exercise = "qualifying disposition"; otherwise
  "disqualifying disposition" with ordinary income).
- $100K limit on ISO portion vesting in any year.
- Holding-period AMT trap: many taxpayers exercise and hold,
  facing AMT on phantom income, then watch stock decline before
  selling.

**2. Non-Qualified Stock Options (NQSOs) — §83:**
- Grant: no income (assuming no readily-ascertainable FMV).
- Exercise: ordinary income for spread; W-2 reporting; FICA
  applies; tax withholding generally required.
- Sale: capital gain/loss on subsequent appreciation/depreciation
  from exercise FMV.

**3. Restricted Stock Units (RSUs):**
- Grant: no income.
- Vesting: ordinary income for FMV at vest; W-2 reporting; FICA;
  tax withheld via share withholding (default).
- Sale: capital gain/loss on subsequent appreciation.

**4. Restricted Stock (actual stock with restrictions) — §83:**
- §83(b) election within 30 days of grant: report current FMV
  as ordinary income; subsequent appreciation = capital gain.
- Without §83(b): vest = ordinary income for FMV at vest.

**5. Employee Stock Purchase Plans (ESPPs) — §423:**
- Qualifying ESPP: discount up to 15% of stock; no current income
  on purchase; sale treated as ordinary (lesser of discount or
  actual gain) + capital gain for excess.
- Holding period: 2 years from grant + 1 year from purchase.

Key planning levers:
- **§83(b) election** for restricted stock — accelerate ordinary
  income at low FMV; future appreciation taxed as capital.
- **ISO AMT planning** — exercise in low-AMT years; consider
  qualifying vs. disqualifying disposition trade-off.
- **Year-end exercise of NQSOs** — accelerate ordinary income to
  current year; defer capital appreciation.
- **Tender offer / acquisition planning** — ISOs becoming NQSOs
  on accelerated vesting.
- **§1202 QSBS interaction (#43).** ISOs exercised into QSBS-
  eligible C corp may qualify.

## Primary IRC authority

- §83 — Property transferred in connection with services.
- §83(b) — Election to include in current year.
- §421 — Statutory stock options general rule.
- §422 — Incentive stock options.
- §423 — Employee stock purchase plans.
- §409A — Deferred compensation (NQSO discount stock options
  subject).
- §3121(v) — FICA on deferred compensation.
- §55-59 — AMT.
- §1202 — QSBS (interaction).

## Treasury regulations

- Reg §1.83-1 through §1.83-8.
- Reg §1.421-1, §1.422-1 through §1.422-5.
- Reg §1.423-1, §1.423-2.
- Reg §1.409A-1 through §1.409A-6.

## Key IRS guidance

- Notice 2003-79 — ISO/ESPP information reporting.
- Notice 2002-47 — Employer ISO/ESPP reporting.
- IRS Publication 525 — Taxable and Nontaxable Income.
- IRS Publication 550 — Investment Income and Expenses.

## Key court decisions

- **Speltz v. Commissioner, 124 T.C. 165 (2005)** — ISO AMT
  consequences upheld even when stock declined.
- **Sutardja v. United States, 109 Fed. Cl. 358 (2013)** —
  §409A applied to discount stock options.

## Eligibility requirements

ISO §422:
1. Granted under written plan approved by shareholders.
2. Exercise price ≥ FMV at grant.
3. 10-year max term.
4. Granted to employee.
5. $100K vesting limit.
6. 10-year exercise from grant.
7. 3-month exercise after termination.

§83(b) election:
1. Made within 30 days of property transfer.
2. Filed with IRS service center (NOT with return).
3. Copy attached to return for year of transfer.
4. Election irrevocable.

§423 ESPP:
1. All employees eligible (with limited exclusions).
2. Discount ≤15%.
3. Limit of $25,000 worth of stock per year.
4. 5-year max offering period.

## Mechanics — how it works

1. **Receive grant.** Determine option type (ISO/NQSO/RSU/ESPP).
2. **Track grant date, vesting schedule, exercise prices, FMV.**
3. **For restricted stock:** evaluate §83(b) election within 30
   days.
4. **At vesting (RSU):** ordinary income on Form W-2.
5. **At exercise:**
   - ISO: track AMT preference; consider AMT credit recovery in
     subsequent years.
   - NQSO: ordinary income on W-2; tax withholding via share
     withholding or cash.
6. **At sale:** report on Form 8949 / Schedule D; basis includes
   any prior ordinary income recognition.
7. **AMT planning:** Form 6251 in years of ISO exercise.

## Documentation requirements

- Grant notices and stock option agreements.
- Form 3921 (ISO exercises, from employer).
- Form 3922 (ESPP, from employer).
- Form W-2 (ordinary income components).
- Brokerage 1099-B.
- §83(b) election filing receipt.

## Common pitfalls / audit risks

- **§83(b) deadline missed.** 30-day window strict; election void.
- **ISO AMT trap.** Exercise-and-hold creates AMT on phantom
  income; later decline doesn't recover AMT in same year.
- **Same-day exercise-and-sell of ISO.** Disqualifying
  disposition; ordinary income.
- **Wash sale on RSU vesting + sale.** Selling shares within 30
  days of separate purchases triggers §1091.
- **Cost basis errors on Form 1099-B.** Brokers report exercise-
  price basis; W-2 ordinary income component must be added.
- **§409A discount option penalty.** 20% additional tax + interest.
- **State double taxation.** Multistate residents with ISO/RSU
  vesting in different states.
- **AMT credit recovery.** Form 8801 in later years; commonly
  forgotten.

## Recent legislative changes

- **TCJA (2017)** — §83(i) qualified equity grants election (5-year
  deferral for private-company employees; limited use).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §83 §422
  Pub L 119-21]`. Working assumption: no major changes.

## State conformity considerations

State treatment varies. **California** unique sourcing rules for
multistate stock comp. **Pennsylvania** does not allow §83(b)
election deduction.

## AICPA SSTS / Circular 230 considerations

Stock-based comp requires careful tracking and AMT analysis.
Practitioner should obtain Forms 3921/3922 each year and
reconcile basis.

## Default confidence band rationale

**MODERATE** — multiple compliance points; high error rate in
practice. HIGH for clean ISO qualifying dispositions or simple RSU
vesting with proper basis tracking. LOW for AMT-affected
exercise-and-hold strategies.

## Cross-references

- `section-1202-qsbs-extended` (#43) — interaction.
- `niit-minimization` (#69).
- `capital-gain-offsets` (#32).
- `state-tax-savings` (#40) — multistate sourcing.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 83","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section83","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 422","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section422","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 423","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section423","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 409A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section409A","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Speltz v. Commissioner, 124 T.C. 165 (2005)","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
