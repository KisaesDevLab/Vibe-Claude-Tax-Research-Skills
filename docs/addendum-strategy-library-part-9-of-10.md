# Vibe CPA Skills — Strategy Library Addendum (94 Strategies)

**Part 9 of 10** — Strategies #78 through #86.

**Part navigation:**
- Part 1: Exec summary, master index, PART A build-plan addendum, strategies #1–#7
- Part 2: Strategies #8–#17
- Part 3: Strategies #18–#27
- Part 4: Strategies #28–#37
- Part 5: Strategies #38–#47
- Part 6: Strategies #48–#57
- Part 7: Strategies #58–#67
- Part 8: Strategies #68–#77
- **Part 9: Strategies #78–#86** ← this file
- Part 10: Strategies #87–#94 + cross-reference matrix

---

## Strategy #78: Qualified Charitable Distribution (QCD)

**File:** `references/strategies/qcd.md`

```markdown
---
name: "Qualified Charitable Distribution (QCD) from IRA"
slug: qcd
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§408(d)(8)", "§170"]
forms: ["Form 1099-R", "Form 1040"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§408(d)(8) Qualified Charitable Distribution (QCD) is a powerful
charitable giving vehicle for IRA owners age 70½ or older. The
mechanism:

1. **Direct transfer from IRA to qualified charity.**
2. **Up to $105,000 (2024; indexed by SECURE 2.0)** per year per
   IRA owner.
3. **Excluded from gross income** (does NOT appear in AGI).
4. **Counts toward Required Minimum Distribution (RMD)** for the
   year.
5. **No charitable deduction** (because not in income).

The exclusion-from-AGI feature is the key benefit — it produces
multiple downstream advantages:

- **§121 §22 §86 phaseouts** based on AGI / MAGI not affected.
- **Medicare IRMAA** brackets not triggered.
- **Social Security taxation** (up to 85% at high AGI) not
  affected.
- **§213 medical deduction threshold** (7.5% of AGI) not raised.
- **§170 charitable deduction AGI limits** not consumed.
- **Effective for non-itemizers** (post-TCJA standard deduction
  era).

QCD is generally superior to taking RMD and donating proceeds
because:
- Donating proceeds requires itemizing for §170 deduction.
- Itemized deduction may not fully offset RMD income.
- AGI-driven phaseouts hit harder at higher income.

SECURE 2.0 added one-time election to fund Charitable Gift
Annuity (CGA) or Charitable Remainder Trust (CRT) up to $53,000
(2024) from QCD; verify implementation.

## Primary IRC authority

- §408(d)(8) — Qualified charitable distributions.
- §408(d)(8)(B) — $105,000 limit (post-SECURE 2.0; was $100,000
  pre-SECURE 2.0).
- §408(d)(8)(F) — One-time CGA/CRT (SECURE 2.0).
- §170(c) — Qualified charitable organizations.
- §401(a)(9) — RMD requirements.

## Treasury regulations

- Reg §1.408-8 — RMD rules.
- Reg §1.408-1 — Individual retirement accounts general.

## Key IRS guidance

- IRS Publication 590-B — Distributions from IRAs.
- Notice 2007-7 — QCD initial guidance.

## Eligibility requirements

1. **IRA owner age 70½+** (NOT age 73 RMD threshold —
   §408(d)(8)(B)(ii)).
2. **Distribution from Traditional or Roth IRA** (NOT from
   employer-sponsored plan; rollover to IRA first).
3. **Direct transfer to charity** — IRA custodian sends directly
   to charity (or makes check payable to charity but delivered to
   account holder for delivery).
4. **Recipient is qualified §170(c) charity** — NOT donor advised
   fund, NOT private foundation (with limited exceptions for
   certain public charities), NOT supporting organization.
5. **Up to $105,000 (2024) per IRA owner.**

## Mechanics — how it works

1. **Verify charity §170(c) status** — most public charities
   qualify; DAFs and private foundations do NOT.
2. **Contact IRA custodian** — request QCD distribution.
3. **Custodian sends check directly to charity** OR makes payable
   to charity for delivery by IRA owner.
4. **Form 1099-R issued** by IRA custodian — typically Box 1
   shows total distribution including QCD amount; Box 2a (taxable
   amount) often shows full amount because custodian doesn't know
   QCD treatment.
5. **Taxpayer reports on Form 1040** Line 4a (gross IRA
   distribution); Line 4b (taxable amount) is the gross
   distribution MINUS the QCD amount.
6. **Write "QCD" next to Line 4b.**
7. **Counts toward RMD** for the year.

## Documentation requirements

- Form 1099-R from IRA custodian.
- Charity acknowledgment letter (substantiation per §170(f)(8)).
- Custodian distribution records showing direct transfer.

## Common pitfalls / audit risks

- **Age requirement (70½, not 73).** Common error post-SECURE Act
  RMD age change.
- **Indirect distribution.** If IRA owner takes distribution to
  personal account first and then donates, NOT a QCD.
- **DAF / private foundation as recipient.** Disqualifies QCD.
- **SEP-IRA / SIMPLE IRA QCD.** Restrictions on "ongoing"
  SEP/SIMPLE — consult guidance.
- **§408(b) annuity contracts.** May or may not qualify.
- **Form 1099-R Box 2a inflated.** Need to manually adjust on
  Form 1040.
- **Roth IRA QCD.** Permitted but typically wasteful (Roth
  distributions already tax-free).
- **Coordination with §401(a)(9) RMD.** QCD counts toward RMD;
  ensure full RMD satisfied.
- **State tax treatment.** Some states do not conform; QCD may be
  state-taxable.

## Recent legislative changes

- **PATH Act (2015)** — Made QCD permanent.
- **SECURE Act (2019)** — Increased RMD age to 72.
- **SECURE 2.0 (2022)** — Increased $100K to $105K (indexed);
  RMD age to 73; one-time CGA/CRT $50K (indexed to $53K for 2024).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408(d)(8)
  Pub L 119-21]`. Working assumption: SECURE 2.0 framework
  preserved.

## State conformity considerations

State conformity to QCD varies. **California** does not conform
fully; QCD may be taxable at state level.

## Default confidence band rationale

**HIGH** — clear statutory framework; well-established practice.

## Cross-references

- `charitable-donation-appreciated` (#51).
- `donor-advised-fund` (#54).
- `charitable-planning` (#53).
- `traditional-ira-contributions` (#83).
- `niit-minimization` (#69) — AGI reduction benefit.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408(d)(8)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 170(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section170","weight":"primary_statute"},
    {"authority_type":"Notice","citation":"Notice 2007-7","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
```

---

## Strategy #79: Roth IRA Contributions

**File:** `references/strategies/roth-ira-contributions.md`

```markdown
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
- `backdoor-roth` (#72) — high-income variant.
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
```

---

## Strategy #80: Roth IRA Conversion

**File:** `references/strategies/roth-ira-conversion.md`

```markdown
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
- `backdoor-roth` (#72).
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
```

---

## Strategy #81: SEP-IRA — Self-Employed

**File:** `references/strategies/sep-ira-self-employed.md`

```markdown
---
name: "SEP-IRA — Self-Employed Owner Maximization"
slug: sep-ira-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§408(k)", "§415(c)", "§401(a)(17)", "§164(f)"]
forms: ["Schedule SE", "Schedule 1 (deduction)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

SEP-IRA strategy for sole proprietors, single-member LLCs, and
partners. Distinct considerations vs. employee-side SEP (#76):

1. **Deduction is above-the-line on Schedule 1.**
2. **Self-employed effective rate:** 25% of compensation = 20% of
   net earnings from self-employment (NESE).
3. **Compensation calculation:**
   - Net earnings from SE = Schedule C net profit × 92.35%.
   - Less ½ SE tax deduction.
   - Less SEP contribution (circular calculation).
4. **Maximum deductible contribution** = NESE × 20% (after ½ SE tax
   deduction), subject to §415(c) $69,000 (2024) and §401(a)(17)
   $345,000 compensation cap.

For partnerships and multi-member LLCs:
- SEP contribution is from partnership; pre-K-1 calculation.
- Each partner's contribution determined by partnership agreement.

Key planning advantage: SEP-IRA is the simplest plan for solo
business owners with no employees. Setup, ongoing administration,
and IRS reporting are minimal compared to 401(k) or DB plans.

For solo business with desire for higher contributions, consider:
- **Solo 401(k) (#82)** — adds $23,000 employee deferral capacity
  ($30,500 with catch-up over 50) on top of employer profit
  sharing.
- **Defined benefit / cash balance (#73)** — much higher
  contributions for older owners.

## Primary IRC authority

- §408(k) — Simplified employee pension.
- §415(c) — Annual additions limit.
- §401(a)(17) — Compensation limit.
- §164(f) — ½ SE tax deduction.
- §401(c)(2) — Net earnings from self-employment.

## Treasury regulations

- Reg §1.408-7.
- Reg §1.401(c)(2)-1.

## Key IRS guidance

- IRS Publication 560 — Retirement Plans for Small Business.
- IRS Publication 334 — Tax Guide for Small Business.
- Form 5305-SEP / 5305A-SEP.

## Eligibility requirements

For self-employed:
1. Net earnings from self-employment.
2. Plan adopted by tax filing deadline.
3. SEP-IRA established at custodian.

## Mechanics — how it works

1. **Compute Schedule C net profit** (or partnership earnings).
2. **Compute SE tax** on Schedule SE (15.3% on first $168,600
  Social Security wage base 2024; 2.9% Medicare on remainder; 0.9%
  Additional Medicare).
3. **Net earnings from SE** = SE income × 92.35%.
4. **Deductible ½ SE tax** = ½ × SE tax.
5. **Compensation for SEP purposes** = NESE - ½ SE tax.
6. **Maximum SEP contribution** = Compensation × (0.25 / 1.25) =
   Compensation × 20%.
7. **Contribute to SEP-IRA** by tax filing deadline (with
   extensions).
8. **Deduct on Schedule 1** as adjustment to income.

## Documentation requirements

- Schedule C / Schedule SE / Schedule K-1.
- SEP plan adoption (Form 5305-SEP or custom).
- Annual contribution computation worksheet.
- IRA custodian statements.

## Common pitfalls / audit risks

- **20% vs. 25% confusion.** 25% applies to W-2 employees; 20%
  applies to NESE.
- **§415(c) limit.** $69,000 (2024) total annual additions.
- **§401(a)(17) compensation cap.** $345,000 (2024).
- **Circular calculation.** Deducted SEP reduces NESE basis.
- **Multiple businesses.** §415(c) aggregated across all
  controlled businesses.
- **Pro-rata rule trap.** SEP balance counted in Backdoor Roth
  pro-rata calculation.

## Recent legislative changes

- **SECURE Act (2019)** — Plan adoption deadline.
- **SECURE 2.0 (2022)** — SEP Roth permitted (verify
  implementation).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408(k)
  Pub L 119-21]`. Working assumption: standard rules preserved.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — straightforward statutory framework.

## Cross-references

- `sep-ira` (#76) — employee-side detail.
- `solo-401k-employer-contributions` (#82) — preferred if
  deferral capacity desired.
- `defined-benefit-cash-balance` (#73) — higher contribution
  alternative.
- `backdoor-roth` (#72) — pro-rata rule trap.
- `minimize-self-employment-tax` (#90).
- `traditional-ira-contributions` (#83).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 401(a)(17)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section401","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #82: Solo 401(k) — Employer Contributions

**File:** `references/strategies/solo-401k-employer-contributions.md`

```markdown
---
name: "Solo 401(k) Employer Contributions"
slug: solo-401k-employer-contributions
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§401(k)", "§401(c)", "§415(c)", "§401(a)(17)", "§164(f)"]
forms: ["Form 5500-EZ (if assets >$250K)", "Schedule SE"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Solo 401(k) (also "Individual 401(k)" or "Self-Employed 401(k)")
is a 401(k) plan covering only the business owner (and possibly
spouse). The plan combines:

1. **Employee deferral** under §402(g): up to $23,000 ($30,500
   catch-up over 50) for 2024.
2. **Employer profit sharing** under §401(c): up to 25% of comp
   (20% of NESE for self-employed).
3. **Combined cap** under §415(c): $69,000 ($76,500 with catch-up)
   for 2024.

For solo business owners, this is generally the most powerful
retirement plan structure — combining employee deferral with
employer profit sharing maximizes total contributions while
remaining administratively simple.

Roth 401(k) component:
- Employee deferral can be Roth (or pre-tax, or split).
- Employer profit sharing must be pre-tax (until SECURE 2.0
  permitted Roth match — verify implementation).

Mega Backdoor Roth via Solo 401(k):
- Some Solo 401(k) plans permit after-tax (NOT Roth) contributions
  beyond §402(g) limit.
- After-tax can be converted to Roth via in-plan or distribution.
- Effectively allows additional $46,000+ Roth annually.

Form 5500-EZ filing required if plan assets exceed $250,000 at
year-end (or if final plan year).

Key advantage over SEP-IRA: Solo 401(k) allows owner to defer
$23,000+ on top of employer contribution; SEP-IRA only allows
employer contribution.

Key disadvantage: more administrative complexity than SEP-IRA;
plan adoption deadline traditionally December 31 of plan year
(SECURE Act extended to tax filing deadline for some elements
but employee deferral requires plan in place during year).

## Primary IRC authority

- §401(k) — Cash or deferred arrangements.
- §401(c) — Self-employed individuals.
- §402(g) — Elective deferral limit.
- §414(v) — Catch-up.
- §415(c) — Annual additions.
- §401(a)(17) — Compensation cap.
- §401(m) — Matching.
- §402A — Designated Roth.

## Treasury regulations

- Reg §1.401(k)-1 through §1.401(k)-6.
- Reg §1.401(c)(2)-1.
- Reg §1.402(g)-1.

## Key IRS guidance

- IRS Publication 560.
- Form 5500-EZ instructions.

## Eligibility requirements

For Solo 401(k):
1. Self-employed business owner.
2. No employees other than spouse (and limited part-time exclusions).
3. Plan adopted by deadline (employee deferral requires plan
   adoption by year-end of plan year; employer profit sharing by
   tax filing deadline).
4. Plan document (prototype/volume submitter typically used).

## Mechanics — how it works

1. **Adopt Solo 401(k) plan** by year-end (for deferral) and tax
   filing deadline (for profit sharing).
2. **Compute NESE** per Schedule SE.
3. **Employee deferral** up to §402(g) limit.
4. **Employer profit sharing** up to 20% of NESE.
5. **Combined ≤ §415(c) limit.**
6. **Form 5500-EZ if assets >$250K.**
7. **Roth deferral component** if elected.

## Documentation requirements

- Plan document.
- Plan adoption resolution.
- Annual contribution worksheet.
- Form 5500-EZ if applicable.
- Custodian statements.

## Common pitfalls / audit risks

- **Plan not adopted by year-end** for current-year employee
  deferral.
- **Hire of employee** triggers nondiscrimination testing and
  potential conversion to traditional 401(k).
- **§415(c) limit.** Combined employee + employer + after-tax.
- **§401(a)(17) compensation cap.**
- **Form 5500-EZ filing.** Required when assets >$250K.
- **Excess deferral.** §402(g) corrective distribution by April 15.
- **Spouse-employee.** Spouse can also defer if employed by
  business.
- **Pro-rata rule trap (Backdoor Roth).** Solo 401(k) balance NOT
  counted in IRA pro-rata (because it's not an IRA).

## Recent legislative changes

- **SECURE Act (2019)** — Plan adoption deadline extended for
  employer contributions.
- **SECURE 2.0 (2022)** — Various enhancements; Roth match
  permitted; SIMPLE Roth.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §401(k)
  Pub L 119-21]`. Working assumption: standard rules preserved.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `401k-pretax` (#75) — employee-side detail.
- `sep-ira-self-employed` (#81) — simpler alternative.
- `defined-benefit-cash-balance` (#73) — higher contribution
  alternative.
- `backdoor-roth` (#72) — Mega Backdoor variant.
- `minimize-self-employment-tax` (#90).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 401(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 401(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 402(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section402","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 415(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section415","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #83: Traditional IRA Contributions

**File:** `references/strategies/traditional-ira-contributions.md`

```markdown
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
- `backdoor-roth` (#72) — non-deductible variant.
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
```

---

## Strategy #84: Accountable Plan — Self-Employed

**File:** `references/strategies/accountable-plan-self-employed.md`

```markdown
---
name: "Accountable Plan Equivalent for Self-Employed"
slug: accountable-plan-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§162", "§280A", "§274"]
forms: ["Schedule C / Schedule SE"]
state_specific: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Sole proprietors do NOT have an "accountable plan" structure
because there is no separate entity to reimburse the proprietor.
Schedule C reflects the proprietor's business, so business
expenses are simply Schedule C deductions — no reimbursement
mechanism needed or available.

The Schedule C equivalent of an accountable plan is direct
deduction of all eligible business expenses on Schedule C,
including:
- Home office (using §280A simplified method or actual expenses).
- Business vehicle (#88).
- Business cell phone (#5).
- Office supplies, software, subscriptions.
- Travel, meals (50%).
- Professional development.
- Insurance (business).

The strategic point of this file: many sole proprietors
inadvertently miss home office, vehicle, and other expenses that
would be reimbursed through accountable plan if they were S-corp
owners. Schedule C deduction captures equivalent benefit; just
use different mechanism (direct deduction, not reimbursement).

Single-member LLC (default disregarded entity) follows Schedule C.
Single-member LLC electing C corp or S corp treatment uses
accountable plan structure (#2, #22, #23).

For partners (multi-member LLC, partnership): Unreimbursed
Partnership Expenses (UPE — #56) plays the accountable plan role
with specific partnership-agreement requirement.

## Primary IRC authority

- §162 — Trade or business expenses.
- §280A — Business use of home.
- §280A(c)(5) — Home office gross income limit.
- §274 — Substantiation requirements.

## Treasury regulations

- Reg §1.162-1 through §1.162-29.
- Reg §1.280A-2.
- Reg §1.274-5T.

## Key IRS guidance

- IRS Publication 535 — Business Expenses.
- IRS Publication 587 — Business Use of Your Home.
- IRS Publication 463 — Travel, Gift, and Car Expenses.

## Eligibility requirements

For Schedule C deduction:
1. Self-employed individual or single-member LLC (disregarded).
2. Expense is ordinary and necessary §162.
3. Substantiation per §6001 / §274.

For §280A home office:
1. Regular and exclusive use for business.
2. Principal place of business OR meet customers/clients OR
   separate structure.

## Mechanics — how it works

1. **Direct deduction on Schedule C.** No reimbursement structure;
   expenses paid directly by business or by proprietor (no
   distinction).
2. **Home office:** Form 8829 actual expenses or simplified $5/sf
   method (max 300 sf = $1,500).
3. **Vehicle:** Standard mileage or actual expenses (#88).
4. **Substantiate per category.**
5. **Reduce Schedule C net profit accordingly.**
6. **Reduces SE tax base** as well as income tax.

## Documentation requirements

- Receipts and substantiation.
- Mileage log (vehicle).
- Home office allocation worksheet.
- Form 8829 (if home office actual expense method).

## Common pitfalls / audit risks

- **Personal use creep.** Personal expenses on business return.
- **Inadequate substantiation.** §274(d) for vehicle, travel, M&E.
- **Home office regular and exclusive use.** Strict.
- **§280A(c)(5) limit.** Home office deduction can't create or
  increase Schedule C loss.
- **Self-employed health insurance §162(l).** Above-the-line on
  Schedule 1, not on Schedule C.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §162 §280A
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — straightforward Schedule C mechanics.

## Cross-references

- `accountable-plan-home-office` (#2) — corporate variant.
- `home-office-deduction-self-employed` (#88).
- `business-vehicle-self-employed` (#88).
- `cell-phone-expenses` (#5).
- `unreimbursed-partnership-expenses` (#56) — partnership variant.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 280A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #85: Business Vehicle — Self-Employed

**File:** `references/strategies/business-vehicle-self-employed.md`

```markdown
---
name: "Business Vehicle Usage — Self-Employed"
slug: business-vehicle-self-employed
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§162", "§168", "§179", "§280F", "§274(d)"]
forms: ["Schedule C", "Form 4562"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Self-employed business vehicle deduction parallels #4 (corporate
context) but with Schedule C mechanics. Two methods:

**Standard Mileage Rate Method (2024: 67¢/mile business):**
- Apply rate × business miles.
- Includes implicit depreciation; cannot also depreciate vehicle.
- Year-1 election locks in for vehicle's life (with limited
  exceptions).
- Simpler; no vehicle expense tracking.

**Actual Expense Method:**
- Track all vehicle expenses (gas, oil, maintenance, insurance,
  registration).
- Apply business-use percentage.
- Depreciation per §168 / §179 / §168(k).
- §280F luxury auto cap if light passenger auto ≤6,000 lbs GVWR.
- Heavy SUV (>6,000 lbs) escapes §280F cap; full §179 / §168(k)
  bonus available.

Strategic considerations:
- **Heavy SUV strategy** — vehicles >6,000 lbs GVWR escape §280F;
  immediate §179 expensing up to $30,500 (2024 SUV limit) plus
  remaining basis at §168(k) bonus rate.
- **OBBBA 100% bonus restoration** — if confirmed, full
  first-year deduction on heavy SUV.
- **Standard mileage simplicity** — for low-cost vehicles or low
  business mileage.
- **Year-1 method election** — affects vehicle's deductibility
  for life.

§274(d) substantiation:
- **Mileage log:** date, destination, business purpose, miles.
- **Contemporaneous** preferred; reconstructed records routinely
  rejected.
- **Apps:** MileIQ, Everlance acceptable if used contemporaneously.

## Primary IRC authority

- §162 — Trade or business expenses.
- §168 — MACRS.
- §168(k) — Bonus depreciation.
- §179 — Expensing.
- §280F — Luxury auto cap.
- §274(d) — Substantiation.

## Treasury regulations

- Reg §1.162-2.
- Reg §1.168-1 through §1.168(k)-2.
- Reg §1.280F-1T through §1.280F-7.
- Reg §1.274-5T.

## Key IRS guidance

- Rev. Proc. 2019-46 — Standard mileage.
- Annual Rev. Proc. on §280F luxury auto caps.
- IRS Publication 463 — Travel, Gift, and Car Expenses.

## Eligibility requirements

For deduction:
1. Vehicle used in business activity.
2. §274(d) substantiation.
3. Method election (standard mileage or actual).

## Mechanics — how it works

1. **Track business use percentage.**
2. **Choose method:**
   - Standard Mileage: 67¢/mile (2024) × business miles.
   - Actual Expense: total expenses × business use %.
3. **Year-1 election** is significant — affects future years.
4. **Form 4562** for depreciation (actual method).
5. **§280F cap** for light passenger auto.
6. **Heavy SUV §179.**
7. **Schedule C deduction.**

## Documentation requirements

- Mileage log (contemporaneous).
- Vehicle records (purchase, financing, repairs, insurance).
- Form 4562 (actual method).
- Title and registration.

## Common pitfalls / audit risks

- **Inadequate mileage logs.** §274(d) is unforgiving.
- **Personal use creep.** Reduces business %.
- **Standard vs. actual lock-in.** Year-1 election affects vehicle's
  life.
- **§280F luxury auto cap miscalculation.**
- **Heavy SUV vs. light vehicle.** GVWR distinction critical.
- **State decoupling on §168(k) bonus.** Track state separately.
- **§179 carryforward.** Section 179 cannot create loss; carries
  forward.

## Recent legislative changes

- **TCJA (2017)** — Used vehicles eligible for §168(k); QIP fix
  later.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §168(k)
  100% bonus Pub L 119-21]`. 100% bonus restoration significantly
  affects this strategy.

## State conformity considerations

State decoupling on §168(k) bonus widely. State auto deduction
rules vary.

## Default confidence band rationale

**HIGH** for properly-documented vehicles. Drops to MODERATE for
borderline business-use percentages or §274(d) substantiation
issues.

## Cross-references

- `business-vehicle-usage` (#4) — corporate context.
- `bonus-and-section-179-depreciation` (#12).
- `bonus-179-depreciation-self-employed` (#89).
- `accountable-plan-self-employed` (#84).
- `reimbursement-depreciation-s-corp-vehicle` (#23).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 280F","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280F","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 179","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section179","weight":"primary_statute"},
    {"authority_type":"RevProc","citation":"Rev. Proc. 2019-46","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
```

---

## Strategy #86: Choice of Entity — SE Tax Analysis

**File:** `references/strategies/choice-of-entity-se-tax.md`

```markdown
---
name: "Choice of Entity — Self-Employment Tax Analysis"
slug: choice-of-entity-se-tax
type: SE Tax
tax_type: 2SH
complexity: High
irc_sections: ["§1401", "§1402", "§3101", "§3121", "§1361-1378", "§199A"]
forms: ["Form 1040 / 1120-S / 1120 / 1065"]
state_specific: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

## Overview

Choice of entity for self-employed individuals is one of the most
consequential planning decisions, with the SE tax implications
often dominating the analysis. Comparison framework:

**Sole Proprietor / Single-Member LLC (disregarded):**
- All net profit subject to SE tax (15.3% on first $168,600 SS
  wage base 2024; 2.9% Medicare on remainder; 0.9% Additional
  Medicare on wages >$200K single / $250K MFJ).
- Schedule C reporting.
- Subject to §199A 20% QBI deduction (with limits).

**Partnership / Multi-Member LLC (default):**
- General partner share of trade-or-business income subject to SE
  tax.
- Limited partner share subject to SE tax debate (case law
  uncertain — Renkemeyer; Castigliola; Thompson).
- LLC member treatment unclear post-Renkemeyer.

**S Corporation:**
- Wages to shareholder-employees subject to FICA (employer + employee
  7.65% × 2 = 15.3% on wages up to SS base).
- Distributions to shareholders NOT subject to SE tax / FICA.
- Reasonable compensation requirement (#21) — IRS may
  recharacterize distributions as wages if comp inadequate.
- Subject to §199A QBI (with W-2 limit at higher incomes).

**C Corporation:**
- 21% federal corporate rate.
- Wages subject to FICA (deductible by corp, taxable to employee).
- Dividends not subject to FICA but subject to qualified dividend
  rate (vs. corporate rate creating double-tax).
- Not eligible for §199A.
- §1202 QSBS potential for stock sale exclusion.

The classic SE tax savings analysis: S corp vs. sole proprietor.
Example: Sole prop with $200K net profit pays SE tax on full
$200K. S corp with $80K reasonable wages + $120K distribution pays
FICA on $80K only — saving FICA on $120K.

Trade-offs:
- S corp administrative cost (separate return, payroll, K-1).
- §199A interaction — S corp wages reduce K-1 QBI.
- State franchise tax (CA 1.5% S corp tax; NY annual fees).
- Reasonable compensation audit risk.

The break-even analysis varies but generally S corp election
becomes worthwhile around $80K-$100K net profit.

## Primary IRC authority

- §1401 — Self-employment tax rate.
- §1402 — Definitions of self-employment.
- §1402(a) — Net earnings from self-employment.
- §3101 — FICA tax on employee.
- §3111 — FICA tax on employer.
- §3121 — Definitions of FICA wages.
- §1361-1378 — S corporation rules.
- §199A — QBI deduction.
- §11 — C corporation rate.

## Treasury regulations

- Reg §1.1401 / 1.1402.
- Reg §1.3121 / 1.3111.
- Reg §1.1361 / 1.1378.
- Reg §1.199A-1 through 1.199A-6.

## Key IRS guidance

- IRS Publication 533 — Self-Employment Tax.
- IRS Publication 535.
- IRS Fact Sheet 2008-25 — S corp reasonable comp.

## Key court decisions

- **Renkemeyer, Campbell & Weaver, LLP v. Commissioner, 136 T.C.
  137 (2011)** — Limited liability partnership members; LLP
  members in active law practice subject to SE tax (limited
  partner exception narrow).
- **Castigliola v. Commissioner, T.C. Memo. 2017-62** — LLC members
  in active law practice subject to SE tax.
- **Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)** —
  S corp reasonable compensation.
- **Hardy v. Commissioner, T.C. Memo. 2017-16** — Limited partner
  SE tax (anesthesiologist).

## Eligibility requirements

For S corporation election:
1. Domestic corporation.
2. ≤100 eligible shareholders (US individuals, certain trusts).
3. One class of stock.
4. No nonresident alien shareholders.
5. Form 2553 election by ≤2 months 15 days into tax year.

For QBI deduction:
- See §199A (#19) and predict-qbi-eligibility.

## Mechanics — how it works

Comparative analysis:
1. **Calculate net business income.**
2. **Project SE tax / FICA under each entity.**
3. **Project §199A under each entity.**
4. **Subtract entity overhead** (S corp annual costs, payroll
   processing, separate return).
5. **Consider state franchise tax** (CA 1.5%; NY fees; etc.).
6. **Choose entity** based on net after-tax income.

For S corp election:
1. **Form Inc / Form LLC.**
2. **Form 2553** to elect S status.
3. **Establish payroll** for owner-employee.
4. **Set reasonable compensation** (annual analysis).
5. **Annual S corp Form 1120-S.**

## Documentation requirements

- Entity formation documents.
- Form 2553 (S corp election).
- Reasonable compensation analysis (annual).
- Payroll records.
- Form 1120-S / Form 1065.

## Common pitfalls / audit risks

- **Reasonable compensation challenge.** S corp owner taking $0
  wages with substantial distributions.
- **§199A W-2 limit.** S corp wages reduce QBI (with W-2 limit
  benefit at higher incomes).
- **§199A SSTB limit.** Specified Service Trade or Business
  excluded above threshold.
- **State franchise tax.** CA, NY, TX, MA — added cost.
- **Qualified subchapter S subsidiary (QSub).** Tracking complications.
- **S corp election deadline missed.** Late election available
  under Rev. Proc. 2013-30.
- **Limited partner SE tax.** Renkemeyer narrowed exception;
  active partners cannot rely on limited partner status alone.
- **Payroll late filing.** Form 941 / 944 / W-2 deadlines strict.

## Recent legislative changes

- **TCJA (2017)** — Created §199A; reduced C corp rate to 21%.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §199A §1
  Pub L 119-21]`. §199A permanence and possible §1402 changes.

## State conformity considerations

State entity-tax rules vary widely. **California** has 1.5% S corp
franchise tax. **New York** has annual filing fees. **Tennessee**
has F&E tax on LLCs. **Texas** has franchise tax based on margin.

## AICPA SSTS / Circular 230 considerations

Choice of entity is foundational decision; practitioner should
run formal comparative analysis annually for high-margin
self-employed clients.

## Default confidence band rationale

**MODERATE** — depends on multiple variables; HIGH for clean S corp
elections with proper reasonable comp; LOW for partnerships with
limited partner SE tax uncertainty post-Renkemeyer.

## Cross-references

- `reasonable-comp-corp-owners` (#21).
- `qbi-deduction` (#19).
- `minimize-self-employment-tax` (#90).
- `income-shifting-to-c-corp` (#47).
- `section-1202-qsbs` (#43) — C corp QSBS potential.
- `c-corp-state-tax-savings` (#35).
- `predict-qbi-eligibility` (predict skill).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 1401","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1402(a)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1402","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1361","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1361","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 199A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section199A","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Renkemeyer, Campbell & Weaver, LLP v. Commissioner, 136 T.C. 137 (2011)","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Castigliola v. Commissioner, T.C. Memo. 2017-62","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"CtAppeals","citation":"Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)","url":"https://www.courtlistener.com","weight":"binding_circuit"}
  ]
}
```
```

---

**End of Part 9 of 10.** Strategies #78 through #86 delivered.

**Continue to Part 10 of 10** for strategies #87 through #94 (Health Insurance SE, Home Office Deduction SE, Bonus/179 Depreciation SE, Minimize SE Tax, Prepayment Expense SE, Split Entity Operations vs RE, De Minimis Safe Harbor SE, Hiring Kids SE) PLUS the comprehensive cross-reference matrix showing strategy combinations, conflicts, and mutual exclusions.
