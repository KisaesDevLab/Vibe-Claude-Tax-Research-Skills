---
name: "Net Investment Income Tax (NIIT) Minimization"
slug: niit-minimization
type: Personal - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§1411"]
forms: ["Form 8960"]
state_specific: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

§1411 imposes an additional 3.8% Net Investment Income Tax (NIIT)
on the lesser of:
- Net investment income, OR
- MAGI above threshold ($200,000 single / $250,000 MFJ / $125,000
  MFS).

NIIT thresholds are NOT indexed for inflation, so the affected
population grows annually.

Net investment income includes:
- Interest, dividends, annuities, royalties, rents.
- Capital gains (including §1411 portion of K-1 distributions).
- Net rental income (unless §469 nonpassive trade or business).
- Net royalty income.
- Investment partnership/S corp income.

Excluded from NIIT:
- Wages and self-employment income (subject instead to
  Additional Medicare Tax under §3101(b)(2)).
- Active business income from §162 trade or business in which
  taxpayer materially participates (unless trading in financial
  instruments or commodities).
- §469 nonpassive trade or business income.
- §401(a) qualified retirement plan distributions.
- §72 IRA distributions.
- §3401(a) wages.
- Tax-exempt interest under §103.
- Social Security benefits.

NIIT minimization strategies:

1. **Material participation** — converting passive rental or
   investment to active business income.
2. **REPS (#20)** — converts rental real estate to nonpassive.
3. **Short-term rental with material participation (#26).**
4. **§469 grouping (#9)** for material participation aggregation.
5. **Roth conversion timing (#80)** — Roth distributions in
   retirement not subject to NIIT.
6. **HSA / retirement plan contributions (#63, #75-#83)** — reduce
   MAGI.
7. **Tax-exempt municipal bonds** — §103 interest excluded.
8. **Capital loss harvesting (#32)** — reduce net investment
   income.
9. **§1031 / §1033 deferral (#1)** — defer capital gain.
10. **§121 primary residence exclusion (#67)** — sale of home not
    subject to NIIT (excluded under §1411(d)(1)(B)).
11. **Charitable contributions of appreciated assets (#51)** —
    reduce capital gain inclusion.
12. **Installment sale (#33)** — spread gain across years to
    minimize bracket exposure.
13. **QOZ deferral (#34).**

## Primary IRC authority

- §1411 — Net investment income tax.
- §1411(a) — 3.8% rate.
- §1411(b) — Threshold amounts.
- §1411(c) — Net investment income definition.
- §1411(d)(1)(B) — §121 exclusion.
- §469 — Passive activity (interaction).
- §3101(b)(2) — Additional Medicare Tax on wages.

## Treasury regulations

- Reg §1.1411-1 through §1.1411-10.

## Key IRS guidance

- IRS Publication 550 — Investment Income and Expenses.
- Form 8960 instructions.

## Key court decisions

- **Aaron Brothers, Inc. v. Commissioner, 119 T.C. 91 (2002)** —
  Material participation analysis (pre-NIIT but relevant).

## Eligibility requirements

NIIT applies to individuals, estates, and trusts above thresholds.
Nonresident aliens not subject. C corporations not subject (own
21% rate).

## Mechanics — how it works

1. **Compute MAGI.** AGI + foreign earned income exclusion +
   excluded U.S. possession income.
2. **Compute net investment income.** Form 8960.
3. **Apply 3.8% to lesser** of (a) NII or (b) MAGI excess over
   threshold.
4. **Form 8960** with return.

## Documentation requirements

- Form 8960.
- Investment income records.
- Material participation logs (if claiming nonpassive treatment).
- §469 grouping documentation (if applicable).

## Common pitfalls / audit risks

- **Self-rental recharacterization.** Rental to own business
  recharacterized as nonpassive but still investment income unless
  §469 qualified.
- **Royalty income treated as investment.** Active mineral / IP
  royalties may be nonpassive trade or business; passive royalty
  income is NIIT.
- **K-1 NII line item.** Often misstated by partnerships/S corps
  in NII allocation.
- **Capital gain distribution from mutual fund.** Subject to NIIT
  even if reinvested.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1411
  Pub L 119-21]`. Working assumption: no changes; thresholds remain
  unindexed.

## State conformity considerations

NIIT is purely federal; no state equivalent (some states have
state-level investment income additional taxes — e.g., CA mental
health surcharge).

## Default confidence band rationale

**HIGH** — clear statutory framework. Drops to MODERATE for
material participation classifications determining inclusion.

## Cross-references

- `real-estate-professional-extended` (#20).
- `short-term-rental` (#26).
- `grouping-of-activities` (#9).
- `roth-ira-conversion` (#80).
- `capital-gain-offsets` (#32).
- `installment-sale` (#33).
- `qoz-reinvestment` (#34).
- `primary-home-sale-exclusion` (#67).
- `charitable-donation-appreciated` (#51).
- `predict-material-participation` (predict skill).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 1411","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1411","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.1411-1","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.1411-4","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"}
  ]
}
```
