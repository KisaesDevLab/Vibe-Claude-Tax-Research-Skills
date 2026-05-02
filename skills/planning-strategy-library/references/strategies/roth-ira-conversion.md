---
name: "Roth IRA Conversion"
slug: roth-ira-conversion
type: Retirement
tax_type: EFR
complexity: Medium
irc_sections: ["§408A(d)(3)", "§408(d)(2)"]
forms: ["Form 1099-R", "Form 8606"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Roth IRA conversion converts pre-tax Traditional IRA, SEP-IRA, or
SIMPLE IRA balance into Roth IRA. Mechanics:

1. **Pay ordinary income tax on converted amount** (in year of
   conversion).
2. **No 10% early withdrawal penalty** on conversion itself.
3. **5-year holding period** before each conversion's earnings
   are tax-free (each conversion has its own 5-year clock for
   penalty-free principal access).

There is **no income limit on Roth conversions** (since 2010 when
AGI cap eliminated). High-income taxpayers can convert any amount
in any year.

Strategic timing for conversions:
- **Low-income years** — early retirement before Social Security /
  RMD age.
- **Bear market** — convert when account values are temporarily
  low.
- **Tax-bracket arbitrage** — convert in year of low taxable
  income.
- **Pre-RMD fill-up** — fill lower brackets before RMD age 73
  forces large distributions.
- **Estate planning** — convert before death to remove tax burden
  from heirs (heirs of Traditional IRA pay tax; heirs of Roth do
  not, subject to SECURE Act 10-year rule).

Pro-rata rule under §408(d)(2): If taxpayer has multiple IRAs
(some pre-tax, some after-tax basis), conversion is treated as
pro-rata of combined IRA balance. Cannot select "only after-tax"
for conversion.

TCJA (2017) eliminated Roth conversion recharacterization. Once
converted, cannot be undone. Plan carefully.

## Primary IRC authority

- §408A(d)(3) — Conversions.
- §408(d)(2) — Pro-rata rule.
- §72(t) — 10% early withdrawal penalty (does NOT apply to
  conversion itself).
- §408A(d)(2) — Qualified distributions.

## Treasury regulations

- Reg §1.408A-4 — Conversions.
- Reg §1.408A-6 — Distributions from Roth IRAs.

## Key IRS guidance

- IRS Publication 590-A.
- IRS Publication 590-B.
- Notice 2009-75 — Conversions during 2010 (transitional).

## Key court decisions

- Limited dispute area (well-settled mechanics).

## Eligibility requirements

1. Pre-tax balance in Traditional, SEP, or SIMPLE IRA.
2. SIMPLE IRA: 2-year participation requirement before conversion
   (else 25% penalty).
3. Cash or in-kind transfer to Roth IRA.
4. Conversion election made by year-end of conversion year.

## Mechanics — how it works

1. **Compute pro-rata basis.** All IRAs aggregated; if any
   non-deductible basis, calculate ratio.
2. **Initiate transfer** from Traditional/SEP/SIMPLE to Roth.
3. **Form 1099-R issued** showing distribution.
4. **Form 8606** for basis tracking and conversion reporting.
5. **Pay tax** on converted amount (less basis) in year of
   conversion.
6. **Track 5-year clock** for each conversion separately (for
   pre-59½ access).

## Documentation requirements

- Pre-conversion IRA balances.
- Form 1099-R.
- Form 8606.
- Custodian statements.

## Common pitfalls / audit risks

- **Pro-rata rule.** Mixed pre-tax and after-tax basis triggers
  pro-rata taxation.
- **No recharacterization.** Cannot undo conversion (post-TCJA).
- **5-year rule.** Each conversion has its own 5-year clock for
  penalty-free access to converted principal.
- **NIIT impact.** Roth conversion increases AGI; may trigger
  NIIT on other investment income.
- **Medicare IRMAA.** Conversion year AGI affects Medicare premium
  brackets 2 years later.
- **State tax.** State may have different conversion treatment.
- **Estimated tax.** Large conversion may require additional
  estimated payment to avoid §6654 underpayment penalty.

## Recent legislative changes

- **TCJA (2017)** — Eliminated recharacterization.
- **SECURE Act (2019)** — Inherited Roth 10-year rule.
- **SECURE 2.0 (2022)** — RMD age changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408A
  Pub L 119-21]`. Working assumption: conversions remain
  unlimited for income.

## State conformity considerations

State conformity generally complete. Some states have unique
basis tracking.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `roth-ira-contributions` (#79).
- `traditional-ira-contributions` (#83).
- `backdoor-roth-extended` (#72).
- `401k-pretax` (#75) — in-plan Roth conversion variant.
- `niit-minimization` (#69).
- `qcd` (#78) — alternative AGI management for IRA owners 70½+.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408A(d)(3)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 408(d)(2)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"}
  ]
}
```
