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
