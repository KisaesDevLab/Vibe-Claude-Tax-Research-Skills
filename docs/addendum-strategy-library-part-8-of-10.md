# Vibe CPA Skills — Strategy Library Addendum (94 Strategies)

**Part 8 of 10** — Strategies #68 through #77.

**Part navigation:**
- Part 1: Exec summary, master index, PART A build-plan addendum, strategies #1–#7
- Part 2: Strategies #8–#17
- Part 3: Strategies #18–#27
- Part 4: Strategies #28–#37
- Part 5: Strategies #38–#47
- Part 6: Strategies #48–#57
- Part 7: Strategies #58–#67
- **Part 8: Strategies #68–#77** ← this file
- Parts 9–10: remaining strategies + cross-reference matrix

---

## Strategy #68: Employee Stock Options

**File:** `references/strategies/employee-stock-options.md`

```markdown
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

- `section-1202-qsbs` (#43) — interaction.
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
```

---

## Strategy #69: NIIT Minimization

**File:** `references/strategies/niit-minimization.md`

```markdown
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

- `real-estate-professional` (#20).
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
```

---

## Strategy #70: Series I Bond

**File:** `references/strategies/series-i-bond.md`

```markdown
---
name: "Series I Savings Bonds"
slug: series-i-bond
type: Personal - Other
tax_type: EFR
complexity: Low
irc_sections: ["§135", "§454"]
forms: ["Form 8815 (education exclusion)", "Form 1099-INT (at redemption)"]
state_specific: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Series I Savings Bonds (issued by U.S. Treasury) offer:

1. **Inflation-adjusted return** — fixed rate + semiannual
   inflation rate.
2. **Federal tax deferral** — interest accrues but not taxed until
   redemption (or election to report annually under §454).
3. **State and local tax exemption** — interest exempt from state/
   local income tax.
4. **§135 education exclusion** — bond proceeds used for qualified
   education expenses excludable from gross income (with phaseouts
   and conditions).

Purchase limits:
- **$10,000/year electronic** per Social Security number through
  TreasuryDirect.
- **$5,000/year paper** purchased with federal tax refund (Form
  8888).
- Total: $15,000/year per individual.

Redemption:
- Cannot redeem within 1 year of purchase.
- 3-month interest penalty if redeemed within 5 years.
- Tax-deferred interest recognized at redemption (or annually if
  §454 election).

The strategy is most attractive in high-inflation periods (2022
peaks of 9.62% inflation-component made I bonds extraordinarily
attractive) and as part of a diversified fixed-income allocation.

## Primary IRC authority

- §135 — Income from United States savings bonds used to pay
  higher education tuition and fees.
- §454 — Obligations issued at discount.
- §454(c) — Election to report income from non-interest-bearing
  obligations.

## Treasury regulations

- Reg §1.135-1 — §135 education exclusion.
- Reg §1.454-1 — Discount obligations.

## Key IRS guidance

- IRS Publication 550 — Investment Income and Expenses.
- IRS Publication 970 — Tax Benefits for Education.

## Eligibility requirements

For §135 education exclusion:
1. Bond purchased after 1989.
2. Owner age 24+ at purchase.
3. Used to pay qualified higher education expenses for taxpayer,
   spouse, or dependent.
4. Below MAGI phaseout ($96,800-$111,800 single / $145,200-
   $175,200 MFJ for 2024; verify current).
5. Form 8815 with return.

For §454 election:
- Annual election to report accrued interest.
- Once made, applies to all current and future bonds; revocation
  requires IRS consent.

## Mechanics — how it works

1. **Purchase via TreasuryDirect** (electronic) or with tax refund
   (paper).
2. **Hold ≥1 year minimum.**
3. **Track interest accrual** (typically deferred until
   redemption).
4. **Redemption.** 1099-INT issued for accrued interest. Pay
   federal tax; no state/local tax.
5. **§135 exclusion if education expenses match.** Form 8815
   computation.

## Documentation requirements

- Bond purchase records (TreasuryDirect or paper bond).
- Form 1099-INT at redemption.
- For §135: education expense receipts.

## Common pitfalls / audit risks

- **Annual purchase limit** strict.
- **§135 phaseout** applies to MAGI in year of redemption, not
  year of purchase.
- **§135 owner-age requirement** — must be 24+ at purchase.
- **Annual interest election (§454).** Once made, irrevocable
  without IRS consent.
- **Redemption timing.** Optimal redemption when 5-year penalty
  ended and inflation-adjusted rate has declined.
- **Estate inclusion.** Bonds at owner's death are estate-includible.

## Recent legislative changes

- No material recent changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §135
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State and local tax exemption is universal for U.S. Treasury
obligations.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `education-credits` (#61).
- `529-savings-plan` (#57).
- `individual-planning-ideas` (#64).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 135","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section135","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 454","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section454","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #71: Employer Benefit Package Review

**File:** `references/strategies/employer-benefit-package-review.md`

```markdown
---
name: "Employer Benefit Package Review (Umbrella)"
slug: employer-benefit-package-review
type: Personal - Other
tax_type: EFR
complexity: Low
irc_sections: ["multiple"]
forms: ["various"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Umbrella reference for systematic annual review of employer-
provided benefits — both employee-side optimization and
employer-side planning for closely-held businesses. Major
benefit categories with cross-references:

**Health & Welfare:**
- Group health insurance (#8) — including HDHP for HSA
  compatibility.
- HSA contributions (#63) — triple tax advantage.
- FSA elections (#62) — HCFSA, DCFSA, LPFSA.
- HRA / MERP (#11) — including QSEHRA, ICHRA, EBHRA.
- Disability insurance — short-term and long-term.
- Life insurance (basic up to $50K excludable; supplemental
  taxable).
- Vision and dental insurance.
- §125 cafeteria plan election review.

**Retirement:**
- 401(k) contributions (#75) — pre-tax and Roth.
- 401(k) employer match — fully take advantage.
- Profit sharing contributions.
- Defined benefit / cash balance (#73).
- SEP-IRA (#76, #81).
- SIMPLE IRA (#77).
- Solo 401(k) (#82).
- §457(b) governmental and tax-exempt employer plans.
- §403(b) educational and nonprofit employer plans.

**Education:**
- §127 employer education assistance (#45) — $5,250.
- Tuition reduction at educational institutions (§117(d)).

**Family:**
- §129 dependent care assistance — $5,000.
- §137 adoption assistance (#58) — $16,810.
- Paid family leave.

**Transportation:**
- §132(f) qualified transportation fringe — parking, transit
  (post-TCJA limited).
- Bicycle commuting (post-TCJA limited).

**Other Fringe:**
- §132 working condition fringes.
- §132(d) de minimis fringes.
- §119 meals/lodging for convenience of employer.
- §132(j)(4) on-premises athletic facility.
- Group-term life insurance up to $50K (excludable; over $50K
  uses Table I imputed income).
- Employee discounts up to §132(c) limits.

**Equity Compensation (#68):**
- ISO, NQSO, RSU, ESPP.

**Severance / Separation:**
- §83 timing on severance comp.
- §409A NQDC timing.
- §72(t)(2)(A)(v) age-55 separation exception.

## Strategic decision tree (annual review)

1. **Maximize tax-advantaged contributions** — HSA, 401(k), FSA.
2. **Match employer contributions** to the maximum extent.
3. **Coordinate FSA/HSA** — choose LPFSA if HSA-eligible.
4. **DCFSA vs. §21 credit** — analyze for each child.
5. **HDHP vs. PPO** — total cost analysis including HSA tax savings.
6. **§125 election review** — premium-only plan vs. flex spending.
7. **Stock comp planning** — §83(b) elections, AMT planning.

## Cross-references

- `group-health-insurance` (#8).
- `hra-merp` (#11).
- `flexible-spending-account` (#62).
- `hsa-optimization` (#63).
- `section-127-education-assistance` (#45).
- `adoption-incentives` (#58).
- `401k-pretax` (#75).
- `defined-benefit-cash-balance` (#73).
- `sep-ira` (#76).
- `simple-ira` (#77).
- `solo-401k-employer-contributions` (#82).
- `employee-stock-options` (#68).

## Authorities (JSON sidecar fragment)

This file is a router; specific authorities live in cross-
referenced files.

```json
{
  "authorities": []
}
```
```

---

## Strategy #72: Backdoor Roth IRA

**File:** `references/strategies/backdoor-roth.md`

```markdown
---
name: "Backdoor Roth IRA Conversion"
slug: backdoor-roth
type: Retirement
tax_type: EFR
complexity: Medium
irc_sections: ["§408", "§408A", "§408A(d)(3)"]
forms: ["Form 8606", "Form 1099-R"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

The "Backdoor Roth IRA" strategy exploits a structural feature of
the Roth conversion rules: while direct Roth IRA contributions
phase out at high income levels ($146K-$161K single / $230K-$240K
MFJ for 2024), Roth conversions have NO income limit (since 2010
when AGI cap was eliminated).

The mechanism:
1. **Make non-deductible Traditional IRA contribution** ($7,000 +
   $1,000 catch-up over 50, for 2024).
2. **Immediately convert to Roth IRA.**
3. **No tax on conversion** (because basis = contribution; no
   pre-tax dollars).
4. **Result: high-income taxpayer effectively contributes to
   Roth.**

The strategy works ONLY if the taxpayer has no other pre-tax IRA
balance (Traditional IRA, SEP-IRA, SIMPLE IRA) — because §408(d)(2)
applies the "pro-rata rule" treating all IRAs as one. Pre-tax
balance triggers proportional taxation of any conversion.

The "Mega Backdoor Roth" extension uses 401(k) after-tax
contributions:
- Some 401(k) plans allow after-tax (NOT Roth) contributions up to
  the §415(c) limit ($69,000 for 2024 / $76,500 with catch-up).
- Subtract employer + pre-tax employee contributions to find
  remaining capacity.
- After-tax contributions can be converted to Roth via in-plan
  Roth conversion or in-service distribution to Roth IRA.
- Effectively allows $30K+ additional Roth contributions per year.

The strategy has been actively discussed in legislative proposals
to eliminate (Build Back Better, etc.) but has not been
restricted. OBBBA may have addressed; verify.

## Primary IRC authority

- §408 — Individual retirement accounts.
- §408(d)(2) — Pro-rata rule for distributions.
- §408A — Roth IRAs.
- §408A(d)(3) — Conversions.
- §415(c) — Defined contribution plan limit ($69,000 / $76,500
  catch-up for 2024).
- §401(k) — Cash or deferred arrangements.
- §401(m) — Matching contributions.

## Treasury regulations

- Reg §1.408-4 — Treatment of distributions.
- Reg §1.408A-1 through §1.408A-9.
- Reg §1.401(k)-1 through §1.401(k)-6.

## Key IRS guidance

- Notice 2014-54 — In-plan Roth conversion of after-tax
  contributions.
- IRS Publication 590-A — Contributions to IRAs.
- IRS Publication 590-B — Distributions from IRAs.

## Key court decisions

- Limited dispute area (strategy is statutorily valid).

## Eligibility requirements

For Backdoor Roth:
1. Must have earned income (or qualifying spouse income).
2. Under §408(d)(2) pro-rata rule: ideally zero pre-tax IRA
   balance.
3. Form 8606 each year for non-deductible Traditional IRA basis
   tracking.

For Mega Backdoor Roth:
1. 401(k) plan permits after-tax contributions.
2. Plan permits in-plan Roth conversion or in-service distribution.
3. Below §415(c) annual additions limit.

## Mechanics — how it works

Backdoor Roth:
1. **Open Traditional IRA** (if not already).
2. **Contribute non-deductible** up to annual limit.
3. **Convert immediately to Roth** — same day or shortly after.
4. **Form 8606** for non-deductible contribution AND conversion.
5. **No tax on conversion** (basis = full contribution; no
   pre-tax dollars).
6. **Track basis** through Form 8606 history.

Mega Backdoor Roth:
1. **Verify 401(k) plan** permits after-tax contributions and
   in-plan Roth or in-service distribution.
2. **Calculate available capacity:** $69,000 (2024) - employee
   pre-tax/Roth - employer match/profit sharing.
3. **Make after-tax contribution.**
4. **Convert immediately** via in-plan Roth or distribute to Roth
   IRA.
5. **Track basis;** confirm employer reports correctly on Form
   1099-R.

## Documentation requirements

- Form 8606 each year (Backdoor Roth basis tracking).
- 401(k) plan summary plan description (Mega Backdoor capability
  verification).
- Form 1099-R for conversions.
- IRA custodian statements.

## Common pitfalls / audit risks

- **Pro-rata rule trap.** Existing pre-tax IRA balance triggers
  partial taxation. Fix: roll pre-tax IRA into 401(k) before
  Backdoor Roth.
- **Step-transaction doctrine.** IRS could theoretically challenge
  rapid contribution + conversion as constructive direct Roth
  contribution. To date, IRS has NOT challenged; multiple IRS
  representatives have indicated acceptance.
- **Form 8606 missed.** Without basis tracking, IRS treats entire
  conversion as taxable.
- **Mega Backdoor Roth basis confusion.** After-tax 401(k)
  contributions vs. Roth 401(k) vs. pre-tax 401(k) — track
  separately.
- **Year-end timing.** Late-year Roth conversion creates Form 8606
  reporting in following year.
- **MFS Roth contribution.** Roth phaseout much lower for MFS.

## Recent legislative changes

- **2010** — AGI cap on Roth conversions eliminated, enabling
  Backdoor Roth.
- **TCJA (2017)** — Eliminated Roth recharacterization (cannot
  undo Roth conversion).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA Backdoor
  Roth §408A Pub L 119-21]`. Some legislative proposals have
  targeted Backdoor Roth; verify if OBBBA implemented restrictions.

## State conformity considerations

State conformity to Roth IRA generally complete.

## AICPA SSTS / Circular 230 considerations

Backdoor Roth is not aggressive — it's a specifically permitted
mechanism. Practitioner should ensure pro-rata rule analysis is
performed and Form 8606 is filed.

## Default confidence band rationale

**HIGH** — well-established strategy with no IRS challenge
history.

## Cross-references

- `roth-ira-contributions` (#79).
- `roth-ira-conversion` (#80).
- `traditional-ira-contributions` (#83).
- `401k-pretax` (#75).
- `solo-401k-employer-contributions` (#82).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408(d)(2)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 408A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"},
    {"authority_type":"Notice","citation":"Notice 2014-54","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
```

---

## Strategy #73: Defined Benefit / Cash Balance Plan

**File:** `references/strategies/defined-benefit-cash-balance.md`

```markdown
---
name: "Defined Benefit and Cash Balance Plans"
slug: defined-benefit-cash-balance
type: Retirement
tax_type: EFR
complexity: High
irc_sections: ["§401(a)", "§412", "§415(b)", "§430", "§4972"]
forms: ["Form 5500", "Schedule SB"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Defined Benefit (DB) plans and Cash Balance plans (a hybrid form of
DB) are qualified retirement plans that promise a specific benefit
at retirement, with employer contribution amount determined by
actuarial calculation.

For closely-held high-income business owners, DB and cash balance
plans allow vastly larger contributions than defined contribution
plans. The §415(b) annual benefit limit ($275,000 for 2024) at
retirement age 62 translates to large current-year contributions —
often $200,000-$300,000+ for owners in their 50s or 60s.

The strategy combines particularly well with:
- **Solo or 401(k) plan (#75, #82)** — DB plan + 401(k) maximizes
  contributions.
- **Profit sharing component** — 401(k) profit sharing piece can
  be added.
- **Roth 401(k) component** — for diversification.

Cash Balance variant:
- DB plan structured as hypothetical individual account.
- Each participant has "cash balance account" credited with annual
  contribution + interest.
- More predictable to participants than traditional DB.
- Frequently used as "DB plan with DC plan look."

DB / Cash Balance plans require:
- **Annual actuarial certification** (additional cost: $2K-$10K
  annually).
- **§412 minimum funding** — funding contributions are mandatory,
  not optional.
- **PBGC premium** for plans with 25+ participants.
- **§415(b) annual benefit limit.**
- **§401(a)(26) minimum participation** — 50 employees or 40% of
  workforce, whichever lesser.
- **§401(a)(4) nondiscrimination** — testing required.

The strategy is most useful for:
- Solo or small-firm professional practices (medical, legal,
  consulting).
- Older owners with high-income lifecycle.
- Businesses with stable, profitable cash flow.
- Few or no employees (or owner-vs-employee comp differential
  significant).

## Primary IRC authority

- §401(a) — Qualified plan requirements.
- §401(a)(26) — Minimum participation.
- §401(a)(4) — Nondiscrimination.
- §412 — Minimum funding.
- §415(b) — Annual benefit limit ($275,000 for 2024).
- §430 — Minimum funding standards.
- §4972 — Excise tax on nondeductible contributions.
- ERISA Title I and II.

## Treasury regulations

- Reg §1.401(a)-1 through §1.401(a)-50.
- Reg §1.412(b)-1 through §1.412(c)-2.
- Reg §1.415(b)-1.
- Reg §1.430(d)-1 — Funding.

## Key IRS guidance

- Rev. Proc. 2024-XX (annual COLA) — Plan limits.
- IRS Publication 560 — Retirement Plans for Small Business.

## Eligibility requirements

For establishing DB / Cash Balance plan:
1. Trade or business with earned income.
2. Plan adopted by deadline (12/31 generally; SECURE Act allows
   adoption by tax filing date for some plans).
3. Written plan document with IRS qualification.
4. Actuarial certification at adoption and annually.
5. §401(a)(26) and §401(a)(4) testing.

## Mechanics — how it works

1. **Engage qualified actuary.** Plan design, funding calculation,
   annual maintenance.
2. **Adopt plan** by qualified deadline.
3. **Determine annual contribution.** Based on actuarial
   calculation considering: participant ages, compensation,
   projected benefits, plan investment returns.
4. **Contribute annually.** Mandatory minimum funding under §412;
   maximum tax-deductible contribution.
5. **Annual administration.** Form 5500, Schedule SB, actuarial
   certification, nondiscrimination testing.
6. **At retirement / termination,** distribute benefits per plan
   terms.

## Documentation requirements

- Plan document (qualified by IRS or via prototype/volume submitter
  letter).
- Annual actuarial valuation.
- Form 5500 / Schedule SB annually.
- Nondiscrimination testing.
- Investment statements.

## Common pitfalls / audit risks

- **Funding obligations are MANDATORY.** Cannot skip in lean year
  without ERISA penalty.
- **§401(a)(26) minimum participation.** Must satisfy or plan
  disqualified.
- **§401(a)(4) nondiscrimination.** Testing failure causes plan
  disqualification.
- **§415(b) annual benefit limit.** Excess contributions trigger
  §4972 excise tax (10% on nondeductible).
- **PBGC premium.** Plans with 25+ participants generally subject
  ($120/participant 2024 + variable rate premium).
- **Plan termination.** Excess assets revert to employer subject
  to 50% excise tax under §4980.
- **Actuarial method changes.** IRS notification required.

## Recent legislative changes

- **SECURE Act (2019)** — Plan adoption deadline extended to tax
  filing date.
- **SECURE 2.0 (2022)** — Various technical changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §401 §415
  Pub L 119-21]`. Working assumption: standard limits preserved.

## State conformity considerations

State conformity to qualified plan rules generally complete.
State tax of distributions varies by state of residence.

## AICPA SSTS / Circular 230 considerations

DB / Cash Balance plans require ongoing actuarial and ERISA
expertise. Practitioner generally coordinates with actuary and
ERISA counsel.

## Default confidence band rationale

**HIGH** — well-established qualified plan structure.

## Cross-references

- `401k-pretax` (#75).
- `solo-401k-employer-contributions` (#82).
- `sep-ira` (#76).
- `simple-ira` (#77).
- `roth-ira-contributions` (#79).
- `reasonable-comp-corp-owners` (#21).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 401(a)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(b)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 412","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section412","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #74: LIRP (Life Insurance Retirement Plan)

**File:** `references/strategies/life-insurance-retirement-plan.md`

```markdown
---
name: "Life Insurance Retirement Plan (LIRP)"
slug: life-insurance-retirement-plan
type: Retirement
tax_type: EFR
complexity: High
irc_sections: ["§7702", "§101(a)", "§72(e)", "§7702A"]
forms: ["Form 1099-R (if distribution becomes taxable)"]
state_specific: true
aggressive: true
caution: true
confidence_default_band: LOW
last_obbba_review: "N/A"
---

> **AGGRESSIVE STRATEGY WARNING:** "Life Insurance Retirement Plan"
> (LIRP) — sometimes marketed as "401(k) Alternative," "Tax-Free
> Retirement Account," "Indexed Universal Life retirement strategy,"
> or "Roth Replacement" — uses an over-funded permanent life
> insurance policy (typically Indexed Universal Life or Whole Life)
> as a retirement accumulation vehicle. The strategy is heavily
> promoted by life insurance agents, often with materially misleading
> claims about returns and tax benefits. Specific risks: (a)
> high insurance costs (mortality, administration, surrender
> charges) significantly reduce actual returns vs. illustrated; (b)
> §7702A Modified Endowment Contract (MEC) classification can
> retroactively eliminate the loan-tax-free benefit; (c) policy
> lapse after substantial loans triggers ordinary income on
> "phantom" gain; (d) lack of regulatory protections and
> transparency relative to qualified plans. Practitioners should
> evaluate LIRPs critically and prefer compliant alternatives
> (Roth IRA, Roth 401(k), Mega Backdoor Roth, defined benefit /
> cash balance) wherever possible.

## Overview

The LIRP structure: an individual purchases a permanent life
insurance policy (typically Indexed Universal Life — IUL — or Whole
Life) and significantly over-funds it relative to the death
benefit. The cash value grows on a tax-deferred basis. At
retirement, the individual takes "tax-free" loans against the
cash value.

Marketed benefits:
1. Tax-deferred growth.
2. Tax-free policy loans (assuming non-MEC).
3. Tax-free death benefit (§101).
4. No income limits or contribution caps (unlike Roth IRA).
5. No required distributions (unlike Traditional IRA).

Reality:
- **High costs.** Mortality charges, administrative fees, surrender
  charges typically consume 10-30% of contributions in early years.
  Net return materially below illustrated.
- **§7702A MEC trap.** Funding too aggressively (more than 7-pay
  test allows) makes contract a MEC; loans become taxable.
- **Lapse risk.** If policy lapses with outstanding loans
  (substantial loans + market downturn + insurance cost increases),
  the entire loan-tax-free framework collapses; ordinary income
  recognized on phantom gain.
- **Surrender charges.** Early termination penalties can eliminate
  20-50% of cash value in first 10-15 years.
- **Investment limitations.** IUL caps and floors limit upside
  participation.
- **Lack of fiduciary protection.** Insurance agent commissions
  often 50%+ of first-year premium.

When LIRPs may be appropriate:
- High-income taxpayers maxed out on qualified plans.
- Need for permanent life insurance.
- Long-term horizon (20+ years).
- Estate planning beneficiary needs.

When LIRPs are inappropriate:
- Substitute for qualified plan / Roth contribution.
- "Free retirement" claims.
- Short investment horizon.
- Low-income taxpayer not maxing out other tax-advantaged accounts.

## Primary IRC authority

- §7702 — Definition of life insurance contract.
- §7702A — Modified endowment contracts.
- §101(a) — Death benefit excluded.
- §72(e) — Annuity / life insurance contract distributions.

## Treasury regulations

- Reg §1.7702-0 through §1.7702-2.
- Reg §1.101-1 through §1.101-7.

## Key IRS guidance

- Notice 2007-78 — §101(j) (when employer-owned).
- IRS Publication 525 — Taxable and Nontaxable Income.

## Key court decisions

- Limited direct case law on the LIRP structure specifically.
- §7702A litigation generally focused on MEC classification.

## Eligibility requirements

For §7702 life insurance treatment:
1. Policy satisfies §7702 cash value accumulation test or
   guideline premium / cash value corridor test.
2. Not a §7702A MEC.

For §72(e) loan tax-free:
1. Non-MEC contract.
2. Loan from cash value (not partial surrender).

## Mechanics — how it works (as marketed)

1. **Purchase permanent life insurance** (IUL, Whole Life, etc.).
2. **Over-fund within §7702 limits.** Pay maximum premium without
   triggering MEC.
3. **Cash value accumulates** through insurance investment options
   (fixed account, indexed account, separate account).
4. **At retirement, take policy loans** against cash value. Not
   currently taxable (assuming non-MEC).
5. **Continue policy through life.** Loans repaid at death from
   death benefit.
6. **Death benefit pays** to beneficiaries tax-free under §101.

## Documentation requirements

- Insurance policy.
- §7702 / §7702A test compliance from carrier.
- Annual policy statements.
- Loan records.

## Common pitfalls / audit risks

- **MEC classification.** §7702A 7-pay test failure makes
  contract a MEC; loans become taxable.
- **Policy lapse.** Outstanding loans + decreasing cash value +
  insurance costs eat the policy alive; lapse triggers ordinary
  income on phantom gain.
- **§409A.** If structured as employer benefit.
- **Insurance cost erosion.** Real returns far below illustrated.
- **Surrender charges.** Early termination expensive.
- **Comparison to alternatives.** Qualified plans, Roth IRA, Mega
  Backdoor Roth all preferable in nearly all cases.

## Recent legislative changes

- No major statutory changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §7702
  §7702A Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State insurance regulations and tax treatment vary significantly.

## AICPA SSTS / Circular 230 considerations

Aggressive strategy. Practitioner should:
- Evaluate critically; compare against qualified alternatives.
- Verify §7702 / §7702A status with carrier.
- Document client's understanding of costs and risks.
- Decline to recommend if client has alternative tax-advantaged
  capacity available.

## Default confidence band rationale

**LOW** — Marketing claims often outpace tax substance and economic
reality. Multiple risk vectors. Compliant alternatives generally
preferable.

## Cross-references

- `corporate-owned-vul` (#44) — corporate variant.
- `roth-ira-contributions` (#79) — preferred alternative.
- `roth-ira-conversion` (#80) — preferred alternative.
- `backdoor-roth` (#72) — preferred alternative.
- `defined-benefit-cash-balance` (#73) — preferred alternative.
- `401k-pretax` (#75) — preferred alternative.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 7702","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7702","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 7702A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7702A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 72(e)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section72","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #75: 401(k) Pre-Tax

**File:** `references/strategies/401k-pretax.md`

```markdown
---
name: "401(k) Pre-Tax (and Roth) Employee Deferral"
slug: 401k-pretax
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§401(k)", "§402(g)", "§414(v)"]
forms: ["W-2 Box 12 Code D (pre-tax) or AA (Roth)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§401(k) cash or deferred arrangement allows employees to elect
salary reduction (pre-tax) or designated Roth (after-tax)
contributions to 401(k) plan, with employer match and profit
sharing additions allocated by formula.

2024 limits:
- **§402(g) employee deferral:** $23,000 ($30,500 with §414(v)
  catch-up over 50).
- **§415(c) total annual additions:** $69,000 ($76,500 with
  catch-up; includes employee + employer + profit sharing).
- **Compensation limit §401(a)(17):** $345,000.

SECURE 2.0 (2022) created additional catch-up provisions:
- **Age 60-63 enhanced catch-up:** $11,250 (2024 — verify; replaces
  standard $7,500 catch-up for that age band).
- **Mandatory Roth catch-up for high earners** (>$145K prior-year
  comp; effective 2026 per SECURE 2.0 originally; delayed by IRS).

Coordination:
- **§402(g) limit applies across all 401(k)/403(b)/457(b) plans.**
- Employee with multiple employers must coordinate.
- §401(k) excludable from Box 1; FICA still applies (Box 3, 5).

Key planning levers:
1. **Max deferral** to §402(g) limit.
2. **Roth vs. pre-tax** based on current vs. expected retirement
   bracket.
3. **Employer match capture** — at minimum contribute enough to
   capture full match.
4. **Mega Backdoor Roth (#72)** — if plan permits after-tax
   contributions.
5. **Coordinate with HSA, FSA** for total tax-advantaged dollars.

## Primary IRC authority

- §401(k) — Cash or deferred arrangements.
- §401(m) — Matching contributions.
- §402(g) — Limitation on elective deferrals.
- §414(v) — Catch-up contributions.
- §415(c) — Annual additions limit.
- §401(a)(17) — Compensation limit.
- §402A — Designated Roth contributions.

## Treasury regulations

- Reg §1.401(k)-1 through §1.401(k)-6.
- Reg §1.401(m)-1.
- Reg §1.402(g)-1.
- Reg §1.414(v)-1.
- Reg §1.402A-1 through §1.402A-2.

## Key IRS guidance

- Rev. Proc. 2024-XX (annual COLA) — limits.
- Notice 2014-54 — In-plan Roth conversions.
- IRS Publication 560 — Retirement Plans for Small Business.

## Eligibility requirements

For employee deferrals:
1. Eligible employee under plan terms.
2. Within §402(g) annual limit (across all plans).
3. Compensation up to §401(a)(17) limit.

## Mechanics — how it works

1. **Plan election** — designate deferral percentage and
   pre-tax/Roth allocation.
2. **Pre-tax deferral reduces W-2 Box 1.**
3. **Roth deferral does NOT reduce Box 1.**
4. **FICA still applies** (Box 3, 5) regardless.
5. **Employer match per plan formula.**
6. **Year-end W-2** reports deferrals in Box 12.
7. **Form 1099-R at distribution.**

## Documentation requirements

- Plan summary.
- Deferral election form.
- W-2 Box 12 codes.
- 1099-R at distribution.

## Common pitfalls / audit risks

- **§402(g) excess deferrals.** Multi-employer scenarios; correct
  by April 15 of following year via §402(g)(2)(A) corrective
  distribution.
- **§415(c) annual additions limit exceeded.** Excess corrected
  per Rev. Proc.
- **§401(k) ADP / ACP testing.** Highly compensated employees
  (HCEs) limited if plan fails testing.
- **Safe harbor 401(k)** avoids ADP/ACP testing but requires
  specific employer contributions.
- **Roth in-plan conversion** — once converted, cannot be undone
  (post-TCJA).
- **§72(t) early distribution penalty** for distributions before
  age 59½ (with exceptions).

## Recent legislative changes

- **SECURE Act (2019)** — Various provisions.
- **SECURE 2.0 (2022)** — Enhanced catch-ups; mandatory Roth
  catch-up for high earners; emergency distributions; etc.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §401(k)
  §402(g) Pub L 119-21]`. Working assumption: standard limits
  preserved.

## State conformity considerations

State conformity to §401(k) generally complete; state tax of
distributions varies.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `solo-401k-employer-contributions` (#82).
- `backdoor-roth` (#72) — Mega Backdoor variant.
- `roth-ira-contributions` (#79).
- `defined-benefit-cash-balance` (#73).
- `sep-ira` (#76).
- `simple-ira` (#77).
- `employer-benefit-package-review` (#71).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 401(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 402(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section402","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 414(v)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section414","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #76: SEP-IRA

**File:** `references/strategies/sep-ira.md`

```markdown
---
name: "SEP-IRA (Simplified Employee Pension)"
slug: sep-ira
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§408(k)", "§415(c)"]
forms: ["Form 5305-SEP (model document)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Simplified Employee Pension (SEP-IRA) is a retirement plan
permitting employer contributions to traditional IRAs of eligible
employees. Strengths:

1. **Easy setup** — Form 5305-SEP model document; no Form 5500
   filing.
2. **Employer-only contributions** (no employee deferrals).
3. **Up to 25% of compensation** (effectively 20% for self-
   employed due to SE tax interaction).
4. **§415(c) limit** — $69,000 (2024).
5. **§401(a)(17) compensation limit** — $345,000 (2024).
6. **No nondiscrimination testing** if uniform percentage
   contributed.
7. **Plan adoption flexibility** — by tax filing deadline of
   employer.

Eligibility (default):
- Age 21+.
- Worked at least 3 of last 5 years.
- Earned at least $750 (2024).

Constraint: SEP-IRA is funded entirely from employer; if the
business has employees, the same percentage must be contributed
for all eligible employees. This makes SEP-IRA economically
unattractive for businesses with substantial employee headcount
relative to owner.

For solo / no-employee businesses, SEP-IRA is straightforward and
cost-effective. For businesses with employees, Solo 401(k)
alternative often better (allows owner to defer separately
without parallel employee contribution requirement).

SEP-IRA cannot offer Roth treatment (until SECURE 2.0 — verify if
implemented; SIMPLE-IRA Roth was added by SECURE 2.0).

## Primary IRC authority

- §408(k) — Simplified employee pension.
- §408(k)(2) — Eligibility requirements.
- §408(k)(3) — Contribution limits.
- §415(c) — Annual additions limit.
- §401(a)(17) — Compensation limit.

## Treasury regulations

- Reg §1.408-7 through §1.408-8.

## Key IRS guidance

- IRS Publication 560 — Retirement Plans for Small Business.
- Form 5305-SEP / Form 5305A-SEP (instructions).

## Eligibility requirements

For employer:
1. Trade or business with earned income.
2. Plan adopted by tax filing deadline.
3. Form 5305-SEP or custom plan document.

For employee (default; can be more generous):
1. Age 21+.
2. Worked at least 3 of last 5 years.
3. Earned at least $750 (2024).

## Mechanics — how it works

1. **Adopt SEP plan.** Form 5305-SEP for prototype; adoption by
   tax filing deadline.
2. **Establish SEP-IRA** at any IRA custodian for each eligible
   employee.
3. **Contribute employer portion.** Up to 25% of compensation per
   employee (uniform percentage for all eligible).
4. **For self-employed:** effective rate is 20% of net earnings
   from self-employment after deduction for ½ SE tax.
5. **Tax deduction** to employer in year of contribution.
6. **No employee deferrals** under SEP-IRA.

## Documentation requirements

- Plan adoption (Form 5305-SEP or custom).
- Annual contribution allocation worksheet.
- Form W-2 (Box 12 not required for SEP-IRA; Box 13 "Retirement
  Plan" checked).
- IRA custodian statements.

## Common pitfalls / audit risks

- **Eligibility confusion.** Default is age 21 + 3 of 5 years;
  employer can be more generous (less restrictive eligibility) but
  not more restrictive.
- **Uniform percentage.** Same % for all eligible.
- **§401(a)(17) compensation cap.** Comp above $345K (2024) not
  considered.
- **Dual-coverage trap.** Employee in SEP-IRA + 401(k) — combined
  §415(c) limit applies.
- **Self-employed effective rate.** 25% of comp = 20% of net SE
  earnings (after ½ SE tax deduction).
- **Plan termination.** Not as flexible as 401(k); SEP balance
  is in IRA.

## Recent legislative changes

- **SECURE Act (2019)** — Plan adoption deadline extended.
- **SECURE 2.0 (2022)** — Various technical changes; SEP Roth
  added (verify implementation).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408(k)
  Pub L 119-21]`. Working assumption: standard rules preserved.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — straightforward statutory framework.

## Cross-references

- `solo-401k-employer-contributions` (#82) — preferred for
  no-employee businesses with deferral capability.
- `simple-ira` (#77) — alternative for small businesses.
- `401k-pretax` (#75).
- `defined-benefit-cash-balance` (#73).
- `sep-ira-self-employed` (#81).
- `traditional-ira-contributions` (#83).
- `backdoor-roth` (#72) — pro-rata interaction.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #77: SIMPLE IRA

**File:** `references/strategies/simple-ira.md`

```markdown
---
name: "SIMPLE IRA (Savings Incentive Match Plan for Employees)"
slug: simple-ira
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§408(p)", "§402(g)"]
forms: ["Form 5304-SIMPLE or Form 5305-SIMPLE"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

SIMPLE IRA is a retirement plan designed for small employers (≤100
employees who received ≥$5,000 compensation in prior year). Key
features:

2024 limits:
- **Employee deferral:** $16,000 ($19,500 with catch-up over 50).
- **Employer contribution:** Either:
  - 3% of compensation matching contribution (for participating
    employees), OR
  - 2% of compensation nonelective contribution (for ALL eligible
    employees).
- **§401(a)(17) compensation limit** — $345,000.

The 3% match has a temporary reduction option (down to 1%) in 2 of
any 5 years.

SECURE 2.0 added:
- **Roth contributions** to SIMPLE IRA permitted (effective 2024).
- **Higher catch-up** for ages 60-63: 50% additional ($24,000
  total elective + $7,500 enhanced catch-up = up to $24,000;
  verify exact 2025/2026 implementation).
- **Higher employer match** option for some plans.

Eligibility (default):
- Compensation ≥$5,000 in any 2 prior years.
- Expected to earn ≥$5,000 current year.

Compared to SEP-IRA:
- SIMPLE allows employee deferrals (SEP does not).
- SIMPLE has lower contribution limits than SEP at higher comp.
- SIMPLE simpler than 401(k); no nondiscrimination testing.

Compared to 401(k):
- SIMPLE simpler administration but lower limits.
- SIMPLE early-withdrawal penalty 25% in first 2 years (vs. 10%).

## Primary IRC authority

- §408(p) — SIMPLE retirement accounts.
- §408(p)(2) — Contribution limits.
- §402(g) — Elective deferral limits.
- §72(t)(6) — 25% early withdrawal in first 2 years.

## Treasury regulations

- Reg §1.408-7.

## Key IRS guidance

- IRS Publication 560.
- Form 5304-SIMPLE / Form 5305-SIMPLE.

## Eligibility requirements

For employer:
1. Trade or business with ≤100 employees who received ≥$5,000
   prior year compensation.
2. No other qualified retirement plan (with limited exceptions).
3. Plan adopted by October 1 (or for new business, as soon as
   practicable).

For employee (default):
1. ≥$5,000 in compensation in any 2 prior years.
2. Expected to earn ≥$5,000 current year.

## Mechanics — how it works

1. **Adopt plan** by October 1 (Form 5304-SIMPLE or 5305-SIMPLE).
2. **Notify employees** of plan terms and election period.
3. **Annual employee election** (60-day window before plan year).
4. **Employee deferrals** via salary reduction.
5. **Employer contributes match (3%)** for participating employees
   OR **nonelective (2%)** for all eligible.
6. **Form 5305-SIMPLE plan document** kept on file (no annual IRS
   filing).
7. **Form W-2 Box 12 Code S** for employee SIMPLE deferrals.

## Documentation requirements

- Form 5304-SIMPLE or 5305-SIMPLE.
- Annual employee notice.
- Employee elections.
- W-2 Box 12 Code S.

## Common pitfalls / audit risks

- **2-year rule.** First 2 years of SIMPLE participation: rollover
  to non-SIMPLE IRA triggers 25% early withdrawal penalty (§72(t)(6))
  + ordinary income. Wait 2 years before any rollover.
- **§402(g) limit** lower than 401(k). Plan participants comparing.
- **Employer cannot have other plan** (with limited exceptions).
- **100-employee limit.** Growth past limit triggers transition
  period.
- **Match formula commitment.** 3% match committed for full year.

## Recent legislative changes

- **SECURE Act (2019)** — Various modifications.
- **SECURE 2.0 (2022)** — Roth contributions; higher employer
  match option; enhanced catch-ups.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408(p)
  Pub L 119-21]`. Working assumption: standard rules preserved.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — straightforward statutory framework.

## Cross-references

- `sep-ira` (#76) — alternative for small business.
- `401k-pretax` (#75) — alternative for higher contribution
  capacity.
- `solo-401k-employer-contributions` (#82) — alternative for
  no-employee businesses.
- `roth-ira-contributions` (#79).
- `traditional-ira-contributions` (#83).
- `backdoor-roth` (#72) — pro-rata interaction.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408(p)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 402(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section402","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 72(t)(6)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section72","weight":"primary_statute"}
  ]
}
```
```

---

**End of Part 8 of 10.** Strategies #68 through #77 delivered.

**Continue to Part 9 of 10** for strategies #78 through #86 (Qualified Charitable Distribution, Roth IRA Contributions, Roth IRA Conversion, SEP-IRA Self-Employed, Solo 401(k) Employer Contributions, Traditional IRA Contributions, Accountable Plan Self-Employed, Business Vehicle Self-Employed, Choice of Entity SE Tax).
