---
name: "Traditional IRA Contributions"
slug: traditional-ira-contributions
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§408", "§219"]
forms: ["Form 8606 (basis tracking)", "Schedule 1 (deduction)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Traditional IRA contributions provide tax-deferred growth, with
deductibility depending on:

1. **Active participation** in workplace retirement plan.
2. **MAGI level.**

2024 contribution limits:
- **Annual:** $7,000 ($8,000 with §219(b)(5) catch-up over 50).
- **Joint contribution** ≤ joint earned income.

Deductibility phase-out for taxpayer covered by workplace plan
(2024):
- **Single covered:** $77K-$87K.
- **MFJ both covered:** $123K-$143K.
- **MFJ one covered (deductible spouse):** $123K-$143K.
- **MFJ one covered (non-deductible spouse):** $230K-$240K.
- **MFS covered:** $0-$10K.

If above phase-out, contribution is non-deductible (basis tracked
on Form 8606); growth still tax-deferred.

Traditional IRA distributions:
- **Pre-59½:** 10% penalty (with exceptions: first home $10K, higher
  education, disability, death, §72(t)(2)(A)(iv) substantially
  equal periodic payments, etc.).
- **Post-59½:** No penalty; ordinary income tax.
- **RMDs at age 73** (post-SECURE 2.0; was 72 post-SECURE Act, 70½
  pre-SECURE).

Key planning levers:
- **Deductible Traditional IRA** for moderate-income covered
  workers in current high-bracket.
- **Non-deductible Traditional IRA** as on-ramp for Backdoor Roth
  (#72).
- **Roth conversion (#80)** of existing Traditional balance.
- **QCD (#78)** for IRA owners 70½+.

Spousal IRA: Each spouse can contribute even if only one has
earned income (using joint earned income limit).

## Primary IRC authority

- §408 — Individual retirement accounts.
- §219 — Retirement savings.
- §219(g) — Phase-out for active participation.
- §72(t) — 10% early withdrawal penalty.
- §401(a)(9) — RMDs.

## Treasury regulations

- Reg §1.408-1 through §1.408-12.
- Reg §1.219-1 through §1.219-3.

## Key IRS guidance

- IRS Publication 590-A — Contributions.
- IRS Publication 590-B — Distributions.

## Eligibility requirements

For contribution:
1. Earned income (own or spouse).
2. Within annual limit.
3. Joint contribution ≤ joint earned income.

For deduction:
1. Below MAGI phase-out (varies by filing status and active
   participation).

## Mechanics — how it works

1. **Verify earned income.**
2. **Determine deductibility** based on active participation and
   MAGI.
3. **Open Traditional IRA.**
4. **Contribute** by tax filing deadline (April 15 + extensions
   for some).
5. **Track basis** if non-deductible portion (Form 8606).
6. **Deduct on Schedule 1** if deductible.
7. **Form 5498 from custodian** documents contribution.

## Documentation requirements

- Earned income records.
- MAGI calculation.
- Form 5498 from custodian.
- Form 8606 if non-deductible portion.

## Common pitfalls / audit risks

- **Excess contributions.** §4973 6% excise tax until withdrawn
  or recharacterized (recharacterization to Roth still allowed for
  contributions; not for conversions post-TCJA).
- **Phase-out calculation.** Active participation broadly defined;
  even minimal employer plan participation triggers.
- **Form 8606 basis tracking.** Critical for non-deductible
  contributions; without it, IRS treats entire distribution as
  taxable.
- **Pro-rata rule.** Mixed pre-tax and after-tax basis aggregated
  for any distribution / conversion.
- **MFS phase-out.** $0-$10K essentially eliminates Traditional
  IRA deductibility for MFS at any meaningful income.

## Recent legislative changes

- **SECURE Act (2019)** — Eliminated 70½ contribution age cap;
  RMD age to 72.
- **SECURE 2.0 (2022)** — RMD age to 73; various technical changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408 §219
  Pub L 119-21]`. Working assumption: standard limits preserved.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `roth-ira-contributions` (#79).
- `roth-ira-conversion` (#80).
- `backdoor-roth-extended` (#72) — non-deductible variant.
- `qcd` (#78).
- `sep-ira` (#76).
- `simple-ira` (#77).
- `401k-pretax` (#75).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 219","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section219","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 219(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section219","weight":"primary_statute"}
  ]
}
```
