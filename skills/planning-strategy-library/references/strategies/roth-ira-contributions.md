---
name: "Roth IRA Contributions"
slug: roth-ira-contributions
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§408A", "§219"]
forms: ["Form 5498 (custodian)", "Form 8606 (basis)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Roth IRA contributions are made with after-tax dollars; growth and
qualified distributions are tax-free. Key features:

2024 limits:
- **Annual contribution:** $7,000 ($8,000 with §219(b)(5) catch-up
  over 50).
- **Phase-out:** $146K-$161K single / $230K-$240K MFJ.
- **MFS:** $0-$10K (effectively no Roth contribution at typical
  MFS income).

Eligibility:
- **Earned income** (wages, self-employment).
- **Below MAGI phase-out.**
- **Spousal IRA** if spouse has earned income (MFJ).

Tax treatment:
- **Contributions:** Always withdrawable tax-free and penalty-free
  (basis recovery first).
- **Earnings:** Tax-free if §408A(d)(2) qualified distribution:
  - Account ≥5 years old, AND
  - Owner age 59½+, or first home purchase ($10K lifetime), or
    death, or disability.
- **Non-qualified earnings distribution:** Ordinary income +
  10% penalty (with exceptions).
- **No RMD** during owner's lifetime (post-SECURE Act, surviving
  spouse can also defer).

The strategy aligns with various financial planning frameworks:
- **Tax diversification** — pre-tax + Roth + taxable.
- **Hedging future tax bracket uncertainty.**
- **Estate planning** — Roth IRAs pass to heirs tax-free (subject
  to 10-year rule under SECURE Act for non-spouse beneficiaries).

For high-income taxpayers above phase-out:
- **Backdoor Roth (#72)** — non-deductible Traditional IRA →
  conversion.
- **Mega Backdoor Roth (#72)** — after-tax 401(k) → conversion.
- **Roth conversion (#80)** — convert existing Traditional IRA
  balance.

## Primary IRC authority

- §408A — Roth IRAs.
- §408A(c) — Limits.
- §408A(d) — Distributions.
- §408A(d)(2) — Qualified distributions.
- §219 — Retirement savings.
- §219(b)(5) — Catch-up contributions.

## Treasury regulations

- Reg §1.408A-1 through §1.408A-10.

## Key IRS guidance

- IRS Publication 590-A — Contributions.
- IRS Publication 590-B — Distributions.

## Eligibility requirements

For contribution:
1. **Earned income** (own or spouse).
2. **MAGI below phase-out.**
3. **Within annual limit** ($7,000 / $8,000 catch-up 2024).
4. **Joint contribution** — combined contributions ≤ joint earned
   income.

## Mechanics — how it works

1. **Verify earned income and MAGI.**
2. **Open Roth IRA** at any custodian.
3. **Contribute** by tax filing deadline (April 15 + extensions
   for some).
4. **Investment selection.**
5. **Track contributions** through Form 5498 (custodian).
6. **Form 8606 not required** for direct Roth contributions
   (only for non-deductible Traditional IRA basis).

## Documentation requirements

- Earned income records.
- MAGI calculation.
- Form 5498 from custodian.

## Common pitfalls / audit risks

- **Excess contributions.** §4973 6% excise tax per year until
  withdrawn or recharacterized.
- **Phase-out calculation.** MAGI includes most income with
  limited addbacks; differs from AGI.
- **MFS limit.** $0-$10K phase-out essentially eliminates Roth
  for MFS at any meaningful income.
- **Spousal IRA earnings limit.** Combined contributions limited
  to combined earned income.
- **Roth IRA + Backdoor Roth.** Must aggregate IRA balances for
  pro-rata rule analysis.
- **Recharacterization.** TCJA eliminated ability to
  recharacterize Roth conversion (but not direct contribution).

## Recent legislative changes

- **TCJA (2017)** — Eliminated Roth conversion recharacterization.
- **SECURE Act (2019)** — 10-year rule for non-spouse Roth
  beneficiaries.
- **SECURE 2.0 (2022)** — 529 to Roth IRA rollover; SIMPLE IRA Roth
  permitted.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408A
  Pub L 119-21]`. Working assumption: standard limits and rules
  preserved.

## State conformity considerations

State conformity to Roth IRA generally complete.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `roth-ira-conversion` (#80).
- `traditional-ira-contributions` (#83).
- `backdoor-roth-extended` (#72) — high-income variant.
- `401k-pretax` (#75) — Roth 401(k) variant.
- `qcd` (#78).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 219","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section219","weight":"primary_statute"}
  ]
}
```
