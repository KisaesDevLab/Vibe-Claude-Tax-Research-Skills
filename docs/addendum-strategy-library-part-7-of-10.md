# Vibe CPA Skills — Strategy Library Addendum (94 Strategies)

**Part 7 of 10** — Strategies #58 through #67.

**Part navigation:**
- Part 1: Exec summary, master index, PART A build-plan addendum, strategies #1–#7
- Part 2: Strategies #8–#17
- Part 3: Strategies #18–#27
- Part 4: Strategies #28–#37
- Part 5: Strategies #38–#47
- Part 6: Strategies #48–#57
- **Part 7: Strategies #58–#67** ← this file
- Parts 8–10: remaining strategies + cross-reference matrix

---

## Strategy #58: Adoption Incentives

**File:** `references/strategies/adoption-incentives.md`

```markdown
---
name: "Adoption Tax Credit and Employer Adoption Assistance"
slug: adoption-incentives
type: Personal - Other
tax_type: CREDIT
complexity: Medium
irc_sections: ["§23", "§137"]
forms: ["Form 8839"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Two distinct adoption tax benefits exist:

1. **§23 Adoption Tax Credit.** Nonrefundable tax credit up to
   $16,810 per eligible child (2024; indexed). Credit phases out
   between $252,150 and $292,150 MAGI (2024). For special-needs
   adoptions, the maximum credit is allowed regardless of actual
   expenses.

2. **§137 Employer-Provided Adoption Assistance.** Employer can
   provide up to $16,810 (2024) per eligible child as tax-free
   benefit (excluded from W-2 Box 1; subject to FICA/Medicare).
   Same phaseout as §23.

The two benefits are coordinated — the §137 exclusion reduces
qualified expenses available for the §23 credit. A taxpayer can
use both, but cannot double-count the same expenses.

For special-needs adoptions:
- Maximum credit/exclusion regardless of actual expenses paid.
- "Special needs" determined by state determination of factors
  preventing adoption without assistance.
- This is a major benefit for foster-to-adopt situations.

## Primary IRC authority

- §23 — Adoption credit.
- §23(b)(1) — Limitation on dollar amount.
- §23(b)(2) — Phase-out.
- §23(d) — Definitions (eligible child, qualified adoption
  expenses, special needs).
- §137 — Adoption assistance programs.

## Treasury regulations

- Reg §1.23-1 through §1.23-4 — Adoption credit.
- Reg §1.137-1 — Employer adoption assistance.

## Key IRS guidance

- IRS Publication 968 — Tax Benefits for Adoption.
- Form 8839 instructions.
- Notice 2010-66 — Adoption credit refundability (during ARRA
  period; now nonrefundable).

## Eligibility requirements

For §23 credit:
1. Eligible child: under 18, or physically/mentally incapable.
2. Qualified adoption expenses: adoption fees, court costs,
   attorney fees, travel costs.
3. Below MAGI phaseout.
4. Adoption is final OR child is special needs.

For §137 exclusion:
1. Written employer plan.
2. Nondiscrimination requirements.
3. Qualified adoption expenses paid by employer.

## Mechanics — how it works

1. **Track qualified adoption expenses** by year.
2. **Credit timing:** Domestic adoptions — claim in year expenses
   paid OR in year adoption is final, whichever later. Foreign
   adoptions — claim in year adoption is final.
3. **Form 8839** filed with return.
4. **Credit carryforward** — unused §23 credit carries forward 5
   years.
5. **§137 employer plan** — employer payments excluded from W-2
   Box 1; Form W-2 Box 14 documentation common.

## Documentation requirements

- Adoption agency / attorney records.
- Court orders.
- Travel and out-of-pocket expense receipts.
- §137 employer plan documents.
- Special-needs determination (if applicable).

## Common pitfalls / audit risks

- **MAGI phaseout calculation.** Includes foreign earned income
  exclusion and other addbacks.
- **Coordination of §23 and §137.** Cannot double-count same
  expenses.
- **Timing of foreign adoptions.** Must be final.
- **Special-needs documentation.** State determination required.
- **Carryforward tracking.** 5-year limit.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §23 §137
  Pub L 119-21]`. Reports indicate possible refundability of §23
  credit. Verify.

## State conformity considerations

Many states offer parallel state adoption credits.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `misc-tax-credits` (#38).
- `employer-benefit-package-review` (#71).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 23","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section23","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 137","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section137","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #59: Amend for Missed Deductions

**File:** `references/strategies/amend-missed-deductions.md`

```markdown
---
name: "Amend Prior Returns for Missed Deductions"
slug: amend-missed-deductions
type: Personal - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§6511", "§6402"]
forms: ["Form 1040-X", "Form 1120-X", "Form 1065-X (limited)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Taxpayers commonly miss deductions, credits, or planning
opportunities on returns. Amendment can recover the benefit, but
strict statute of limitations applies:

- **§6511(a) refund claim period** — 3 years from filing date OR 2
  years from payment date, whichever later.
- **§6511(b)(2)(A) refund cap** — limited to tax paid within 3 years
  prior to amendment claim.
- **§6511(d) special rules** — bad debts and worthless securities
  (7 years), foreign tax credit (10 years), etc.

Common amendable items:
1. **Forgotten §1244 ordinary loss** on small business stock.
2. **Missed depreciation methods** (cost-seg catch-up via Form 3115
   accounting method change is preferred for prior years).
3. **Missed credits** — R&D credit, WOTC, energy credits.
4. **Filing status changes** (limited; cannot amend MFJ to MFS
   after due date).
5. **Missed §199A QBI deduction.**
6. **Missed PTET refund** (if state allows retroactive PTET
   claim).
7. **Charitable contributions inadvertently omitted.**
8. **NOL carryback claims** (where allowed; CARES years 2018-2020
   only post-CARES Act).
9. **§831(b) captive insurance recharacterizations.**
10. **Missed §1031 exchange treatment.**

## Primary IRC authority

- §6511 — Limitations on credit or refund.
- §6511(a) — Period of limitation on filing claim.
- §6511(b) — Limitation on allowance of credits and refunds.
- §6511(d) — Special rules.
- §6402 — Authority to make credits or refunds.
- §6532 — Periods of limitation on suits.

## Treasury regulations

- Reg §301.6511-1 through §301.6511-7.
- Reg §301.6402-1 through §301.6402-4.

## Key IRS guidance

- IRS Publication 17 — Your Federal Income Tax.
- Form 1040-X instructions.
- Form 1120-X instructions.

## Key court decisions

- **United States v. Brockamp, 519 U.S. 347 (1997)** — §6511
  statute of limitations strictly enforced.
- **Boyle v. United States, 469 U.S. 241 (1985)** — Filing
  obligation nondelegable.

## Eligibility requirements

For amendment:
1. Within §6511 statute of limitations.
2. Specific item(s) to be corrected identifiable.
3. Tax law support for position (refunds for changes in law
   generally unavailable absent specific provision).

## Mechanics — how it works

1. **Identify amendable items** in prior years (review prior
   returns; client interview about life changes; check for missed
   items).
2. **Verify statute of limitations.**
3. **Form 1040-X / 1120-X** with explanation in Part III.
4. **Attach supporting forms** (Schedule, etc.) reflecting changes.
5. **State amendment** for state-only changes (separate state
   procedure).
6. **NOL carryback (if applicable):** Form 1045 (12-month quick
   refund) or Form 1040-X.
7. **Track refund processing** — typically 16+ weeks for paper-
   filed amendments.

## Documentation requirements

- Original return.
- Supporting documentation for new position (receipts, statements,
  etc.).
- Form 1040-X / 1120-X with detailed explanation.
- Statute of limitations verification.

## Common pitfalls / audit risks

- **Statute of limitations missed.** §6511 strict.
- **Tax paid more than 3 years before amendment.** §6511(b)(2)(A)
  caps refund at tax paid within 3-year window.
- **Original return errors discovered during amendment.** May
  obligate disclosure of additional liability.
- **Filing status change.** MFJ to MFS not allowed after due date
  (with limited exceptions).
- **Estimated tax credit allocation.** Can be complicated for
  joint amendments.
- **State follow-up.** State amendments separate.
- **Form 3115 accounting method change** is the preferred
  mechanism for depreciation and method-change items rather than
  Form 1040-X (no statute of limitations on §481(a) catch-up
  adjustment).

## Recent legislative changes

- **CARES Act (2020)** — Retroactive NOL carryback for 2018-2020
  generated wave of Form 1040-X filings.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §6511
  Pub L 119-21]`. Working assumption: no changes to amendment
  framework.

## State conformity considerations

States generally have parallel amendment procedures with state-
specific forms and statutes of limitations.

## Default confidence band rationale

**HIGH** for clear amendable items within statute. Drops to
MODERATE when statute is near-expired or when interpretive
positions are at issue.

## Cross-references

- `nol-carryback-carryforward` (#15).
- `worthless-stock-ordinary-loss` (#30).
- `qbi-deduction` (#19).
- `cost-segregation` (#41) — Form 3115 alternative.
- `late-penalties-interest` (#37).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 6511","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6511","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 6402","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6402","weight":"primary_statute"},
    {"authority_type":"SCOTUS","citation":"United States v. Brockamp, 519 U.S. 347 (1997)","url":"https://www.supremecourt.gov","weight":"binding_judicial"}
  ]
}
```
```

---

## Strategy #60: College Student Strategies

**File:** `references/strategies/college-student-strategies.md`

```markdown
---
name: "College Student Tax Strategies (Umbrella)"
slug: college-student-strategies
type: Personal - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§25A", "§221", "§152", "§129", "§127", "§529"]
forms: ["Form 8863", "Form 1098-T", "Form 1098-E"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Umbrella reference for tax planning involving college students
and their families. Major strategy categories:

1. **§25A Education Credits (#61).** American Opportunity Credit
   (AOTC) up to $2,500 for first 4 years; Lifetime Learning Credit
   (LLC) up to $2,000.

2. **§221 Student Loan Interest Deduction.** Above-the-line
   deduction up to $2,500/year for student loan interest. MAGI
   phaseout.

3. **§529 Plans (#57).** Tax-free growth and distributions for
   qualified education expenses.

4. **§127 Employer Education Assistance (#45).** $5,250/year tax-
   free; through 2025 (likely permanent under OBBBA), includes
   student loan repayment.

5. **§152 Dependency.** Determines who claims credits and
   exclusions.

6. **Filing strategy.** Whether student files own return; whether
   parent claims as dependent.

7. **Coordination of education benefits** — cannot double-dip same
   expenses.

8. **Roth IRA for college student.** Earned income from summer
   jobs / part-time work funds Roth IRA; tax-free growth; basis
   withdrawable penalty-free anytime.

9. **§529 Roth rollover (SECURE 2.0).** Up to $35,000 lifetime
   from 529 to Roth IRA after 15 years.

10. **Hiring student in family business (#49).** Earned income
    enables Roth contribution; income shifting; possible health
    benefits.

## Strategic decision tree

**Q1: Is student claimed as dependent?**
- Yes → Parent generally claims §25A education credits.
- No → Student claims credits if eligible.

**Q2: Are total qualified education expenses below $4,000?**
- AOTC fully captures with $4,000 of expenses (100% of first
  $2,000 + 25% of next $2,000).
- Above $4,000 → consider 529 distribution for excess.

**Q3: Is parent's MAGI above AOTC phaseout ($90K single / $180K
MFJ for 2024)?**
- Yes → Consider strategies to qualify student to claim credit
  (e.g., not claim as dependent).

**Q4: Has student earned income?**
- Yes → Roth IRA contribution opportunity.

**Q5: Multiple children in college?**
- Each child eligible for separate §25A credit (AOTC for first 4
  years).

## Primary IRC authority

- §25A — Hope and Lifetime Learning credits.
- §25A(i) — American Opportunity Credit (refundable up to 40%).
- §25B — Saver's Credit (interaction).
- §117 — Qualified scholarships.
- §127 — Employer education assistance.
- §129 — Dependent care assistance.
- §152 — Dependents.
- §221 — Student loan interest.
- §529 — Qualified tuition programs.
- §530 — Coverdell ESA.

## Treasury regulations

- Reg §1.25A-1 through §1.25A-5 — Education credits.
- Reg §1.221-1 — Student loan interest.

## Key IRS guidance

- IRS Publication 970 — Tax Benefits for Education.
- Form 1098-T (issued by educational institutions).
- Form 1098-E (student loan interest).
- IRS Publication 501 — Dependents.

## Cross-references

- `education-credits` (#61) — primary detailed reference.
- `529-savings-plan` (#57).
- `section-127-education-assistance` (#45).
- `roth-ira-contributions` (#79).
- `hiring-kids` (#49).
- `married-filing-separate` (#65).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 25A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section25A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 221","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section221","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 152","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section152","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #61: Education Credits

**File:** `references/strategies/education-credits.md`

```markdown
---
name: "American Opportunity Credit and Lifetime Learning Credit (§25A)"
slug: education-credits
type: Personal - Other
tax_type: CREDIT
complexity: Medium
irc_sections: ["§25A"]
forms: ["Form 8863", "Form 1098-T"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§25A provides two education tax credits:

**American Opportunity Credit (AOTC) — §25A(i):**
- Up to $2,500 per eligible student per year.
- 100% of first $2,000 of qualified expenses + 25% of next $2,000.
- Available for first 4 years of post-secondary education.
- Student must be at least half-time and pursuing degree/credential.
- 40% of credit is refundable (up to $1,000 if no tax liability).
- Phaseout: $80K-$90K single / $160K-$180K MFJ (2024).
- Cannot have a felony drug conviction.

**Lifetime Learning Credit (LLC) — §25A(b):**
- Up to $2,000 per return (not per student).
- 20% of first $10,000 of qualified expenses.
- Available for unlimited years (graduate, continuing education,
  professional development).
- No degree/half-time requirement.
- Nonrefundable.
- Phaseout: $80K-$90K single / $160K-$180K MFJ (2024).

Cannot claim both AOTC and LLC for same student in same year.
Cannot claim either if expenses paid from §529 tax-free distribution
(double-dipping prohibition).

Qualified expenses (AOTC): tuition, fees, course materials.
Qualified expenses (LLC): tuition and fees only.

## Primary IRC authority

- §25A — Hope and Lifetime Learning credits.
- §25A(b) — Lifetime Learning Credit.
- §25A(c) — Hope/AOTC.
- §25A(f) — Definitions.
- §25A(g)(2) — Coordination with §529 and §530.
- §25A(i) — American Opportunity Credit.

## Treasury regulations

- Reg §1.25A-1 through §1.25A-5.

## Key IRS guidance

- IRS Publication 970 — Tax Benefits for Education.
- Form 8863 instructions.
- Form 1098-T (issued by educational institutions).

## Eligibility requirements

For AOTC:
1. Student is taxpayer, spouse, or dependent.
2. Student is in first 4 years of post-secondary education.
3. At least half-time enrollment for at least one term.
4. Pursuing degree or credential.
5. No felony drug conviction.
6. Below MAGI phaseout.
7. Educational institution is eligible (Title IV).

For LLC:
1. Student is taxpayer, spouse, or dependent.
2. Below MAGI phaseout.
3. Educational institution is eligible.

## Mechanics — how it works

1. **Receive Form 1098-T** from educational institution.
2. **Determine qualified expenses.**
3. **Choose credit per student.** AOTC if eligible (typically more
   valuable; refundable component); LLC otherwise.
4. **Coordinate with §529 distributions.** Different expenses must
   be used for credit vs. tax-free 529 distribution.
5. **Form 8863** with return.

## Documentation requirements

- Form 1098-T.
- Receipts for qualified expenses (tuition, fees, books).
- Enrollment status verification.
- Educational institution Title IV status.

## Common pitfalls / audit risks

- **Form 1098-T errors.** Box 1 (payments received) may not match
  taxpayer's actual qualified expenses.
- **Double-dipping with §529.** Same expenses cannot be used
  for §529 tax-free distribution AND §25A credit.
- **MAGI phaseout calculation.** Includes foreign earned income
  exclusion addback.
- **Dependency error.** AOTC claimed by both parent and student.
- **AOTC felony drug conviction.** Disqualifies for life.
- **AOTC 4-year limit.** Counted as full academic years; "Junior
  status" or higher disqualifies.
- **Refundable credit identity verification.** AOTC required PTIN
  and Form 8867 due diligence by preparer.

## Recent legislative changes

- **PATH Act (2015)** — Made AOTC permanent.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §25A
  Pub L 119-21]`. Working assumption: no major changes.

## State conformity considerations

Some states have parallel state education credits.

## Default confidence band rationale

**HIGH** — clear statutory framework. Drops to MODERATE for
borderline 4-year-status determinations or coordination issues
with §529 distributions.

## Cross-references

- `college-student-strategies` (#60).
- `529-savings-plan` (#57).
- `section-127-education-assistance` (#45).
- `married-filing-separate` (#65).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 25A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section25A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 25A(i)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section25A","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.25A-3","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"}
  ]
}
```
```

---

## Strategy #62: Flexible Spending Account (FSA)

**File:** `references/strategies/flexible-spending-account.md`

```markdown
---
name: "Flexible Spending Account (Health and Dependent Care)"
slug: flexible-spending-account
type: Personal - Other
tax_type: EFR
complexity: Low
irc_sections: ["§125", "§129", "§105"]
forms: ["W-2 (Box 10 dependent care; pre-tax §125 reduction)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Flexible Spending Accounts (FSAs) are §125 cafeteria plan components
allowing employees to elect pre-tax salary reduction for specific
expense reimbursement:

**Health Care FSA (HCFSA):**
- Up to $3,200 (2024) salary reduction.
- Pre-tax: reduces Box 1, Box 3 (Social Security wages), Box 5
  (Medicare wages).
- Reimburses §213(d) qualified medical expenses.
- "Use it or lose it" with limited rollover (up to $640 in 2024)
  or 2.5-month grace period (employer choice; not both).

**Dependent Care FSA (DCFSA):**
- Up to $5,000 (single or MFJ; $2,500 if MFS).
- Pre-tax: reduces Box 1, Box 3, Box 5.
- Reimburses qualified dependent care expenses for children under
  13 or incapacitated dependents.
- Coordinates with §21 child and dependent care credit (each dollar
  through DCFSA reduces credit-eligible expenses).
- Box 10 of W-2 reports DCFSA contributions.

**Limited-Purpose FSA (LPFSA):**
- Reimburses dental and vision only.
- Compatible with HSA (#63) — allows individual to participate in
  HDHP+HSA AND have an LPFSA simultaneously.

The FSA election is locked at the start of the year (limited
change-in-status events permit mid-year changes per Reg §1.125-4).

## Primary IRC authority

- §125 — Cafeteria plans.
- §129 — Dependent care assistance.
- §105 — Health plan reimbursement.
- §213(d) — Medical care definition.
- §21 — Child and dependent care credit.

## Treasury regulations

- Reg §1.125-1 through §1.125-7.
- Reg §1.129-1.

## Key IRS guidance

- IRS Publication 502 — Medical and Dental Expenses.
- IRS Publication 503 — Child and Dependent Care Expenses.
- IRS Publication 969 — HSAs, MSAs, FSAs, HRAs.
- Notice 2013-71 — FSA carryover rules.
- Rev. Proc. 2024-XX (annual COLA) — FSA limits.

## Eligibility requirements

1. Employer offers §125 cafeteria plan with FSA component.
2. Annual election made before plan year.
3. For DCFSA: care necessary for taxpayer (and spouse if MFJ) to
   be employed or actively seeking employment.

## Mechanics — how it works

1. **Annual open enrollment.** Employee elects FSA contribution.
2. **Pre-tax salary reduction** throughout year.
3. **Reimbursement requests** with receipts for qualified expenses.
4. **Year-end deadline** — claims must be incurred by year end (or
   grace period); claims must be filed by run-out deadline (typically
   90 days after year end).
5. **DCFSA-§21 credit coordination** — same expenses cannot be both
   reimbursed by DCFSA and claimed for credit.

## Documentation requirements

- §125 plan document.
- Annual election form.
- Receipts for reimbursed expenses.
- Form W-2 with proper box reporting.

## Common pitfalls / audit risks

- **Use-it-or-lose-it forfeiture.** Unused balance generally
  forfeits at year end (subject to limited carryover or grace
  period).
- **Mid-year election change.** Limited to qualifying events.
- **HSA + HCFSA conflict.** Standard HCFSA disqualifies HSA
  contribution; LPFSA permits HSA participation.
- **DCFSA over-funding.** Cannot exceed lesser of $5,000, earned
  income, or spouse's earned income.
- **DCFSA-§21 credit double-counting.**
- **Owner-employee 2%+ S corp shareholder.** Cannot participate in
  §125 plans.

## Recent legislative changes

- **CAA 2021 / ARPA 2021** — Temporary FSA flexibility (extended
  rollovers, mid-year changes). Most temporary provisions expired.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §125 §129
  Pub L 119-21]`. Working assumption: standard limits preserved.

## State conformity considerations

State conformity to §125 generally complete.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `hsa-optimization` (#63).
- `hra-merp` (#11).
- `group-health-insurance` (#8).
- `health-insurance-s-corp` (#10).
- `employer-benefit-package-review` (#71).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 125","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section125","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 129","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section129","weight":"primary_statute"},
    {"authority_type":"Notice","citation":"Notice 2013-71","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
```

---

## Strategy #63: HSA Optimization

**File:** `references/strategies/hsa-optimization.md`

```markdown
---
name: "Health Savings Account (HSA) Optimization"
slug: hsa-optimization
type: Personal - Other
tax_type: EFR
complexity: Low
irc_sections: ["§223", "§220", "§106(d)"]
forms: ["Form 8889", "Form 5498-SA", "Form 1099-SA"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

The Health Savings Account (HSA) is the most tax-advantaged account
in the Code — the only account offering "triple tax advantage":

1. **Tax-deductible contributions** (above-the-line under §223 or
   pre-tax via cafeteria plan).
2. **Tax-free growth** of investments.
3. **Tax-free distributions** for qualified medical expenses.

Plus, after age 65, distributions for non-medical purposes are
taxed as ordinary income (no penalty) — effectively making the HSA
function as a backup traditional IRA for non-medical use.

2024 contribution limits:
- **Self-only HDHP:** $4,150.
- **Family HDHP:** $8,300.
- **Catch-up (age 55+):** additional $1,000.

HDHP requirements (2024):
- Minimum deductible: $1,600 self / $3,200 family.
- Maximum out-of-pocket: $8,050 self / $16,100 family.

The optimization strategy:
1. **Maximum HSA contribution annually.**
2. **Pay current medical expenses out-of-pocket** rather than from
   HSA. Save receipts for future tax-free reimbursement.
3. **Invest HSA balance for long-term growth** (not in cash sweep).
4. **In retirement,** withdraw tax-free for qualified medical
   expenses (including Medicare premiums) using stockpiled receipts.
5. **After age 65,** withdraw remainder for non-medical purposes
   (taxable but no penalty).

This effectively converts the HSA into a tax-free investment vehicle
exceeding Roth IRA in tax efficiency (Roth has tax-free in/tax-free
out; HSA has tax-deductible-in/tax-free-out for medical, tax-free-
out for medical at any age).

## Primary IRC authority

- §223 — Health savings accounts.
- §223(c) — High deductible health plan.
- §223(d) — HSA definition.
- §223(f) — Distributions.
- §106(d) — Employer HSA contributions excluded from income.
- §220 — Archer MSA (predecessor; limited current use).

## Treasury regulations

- Reg §1.223-1 through §1.223-7 (proposed in part).

## Key IRS guidance

- Notice 2004-2 — Initial HSA guidance.
- Notice 2008-59 — HSA permitted insurance.
- Notice 2013-57 — Preventive care.
- IRS Publication 969 — HSAs, MSAs, FSAs, HRAs.
- Rev. Proc. 2023-34 — 2024 contribution and HDHP limits.

## Eligibility requirements

For HSA contribution:
1. **Covered by HDHP** as of first day of month.
2. **Not enrolled in Medicare.** (Medicare Part A enrollment
   automatically disqualifies.)
3. **Not claimed as dependent on another's return.**
4. **No other disqualifying coverage:** standard HCFSA, traditional
   HRA, general-purpose health insurance, Tricare, VA medical
   benefits within last 3 months.

## Mechanics — how it works

1. **Verify HDHP enrollment.**
2. **Contribute to HSA.** Direct contributions (deductible above-
   the-line) or through employer cafeteria plan (pre-tax).
3. **Invest HSA.** Most HSA custodians allow investment in mutual
   funds, ETFs above a threshold balance.
4. **Pay medical expenses.** Either from HSA or out-of-pocket
   (saving receipts for future reimbursement).
5. **Form 8889** annually with return.
6. **At age 65:** Medicare enrollment ends HSA contributions;
   existing balance remains tax-free for medical or taxable for
   non-medical use.

## Documentation requirements

- Form 5498-SA (contributions; from custodian).
- Form 1099-SA (distributions; from custodian).
- Form 8889 with return.
- Receipts for qualified medical expenses (no time limit; can be
  reimbursed years later as long as expense was incurred after HSA
  opened).

## Common pitfalls / audit risks

- **HDHP disqualifying coverage.** Standard HCFSA, HRA, or
  Medicare disqualifies.
- **Contribution limit exceeded.** 6% excise tax under §4973.
- **Last-month rule misuse.** If HDHP coverage only at year-end,
  full-year contribution allowed but 12-month testing period
  required.
- **Spousal coordination.** Family HDHP limit shared between
  spouses.
- **Medicare enrollment retroactive 6 months.** Common trap for
  taxpayers turning 65 who delay Medicare.
- **Distribution for non-qualified expense.** Before 65: 20%
  penalty + ordinary income tax. After 65: ordinary income tax
  only.

## Recent legislative changes

- **CARES Act (2020)** — Permanently allowed OTC drugs and
  menstrual products as qualified medical expenses.
- **Inflation Reduction Act (2022)** — Various preventive care
  changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §223
  HSA Pub L 119-21]`. Possible expansion of HSA eligibility.
  Verify.

## State conformity considerations

State conformity to §223 generally complete except **California**
and **New Jersey** (do not conform; no state deduction).

## Default confidence band rationale

**HIGH** — clear statutory framework; well-established planning.

## Cross-references

- `flexible-spending-account` (#62) — LPFSA compatible.
- `group-health-insurance` (#8).
- `hra-merp` (#11) — disqualifying interaction.
- `roth-ira-contributions` (#79) — comparable triple-advantage.
- `qcd` (#78).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 223","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section223","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 106(d)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section106","weight":"primary_statute"},
    {"authority_type":"Notice","citation":"Notice 2004-2","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
```

---

## Strategy #64: Individual Planning Ideas

**File:** `references/strategies/individual-planning-ideas.md`

```markdown
---
name: "Individual Planning Ideas (Umbrella)"
slug: individual-planning-ideas
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

Umbrella reference for individual tax planning ideas not given
separate strategy files. Quick-reference checklist for annual
client review:

1. **Itemize vs. standard deduction.** Compare carefully; consider
   bunching strategy (#54 DAF) if near threshold.

2. **Charitable bunching.** Concentrate multiple years' giving in
   one year for itemizing benefit; DAF facilitates timing.

3. **Roth conversion ladder.** Annual partial conversions in lower-
   income years (#80).

4. **NIIT minimization (#69).** Coordinate AGI under $250K MFJ /
   $200K single.

5. **AMT planning.** Track ISO exercises, large state tax,
   miscellaneous itemized deductions.

6. **Estimated tax safe harbor.** §6654 requires estimated payments
   to avoid underpayment penalty: 100% of prior year (110% if AGI
   >$150K) or 90% of current year, whichever lower.

7. **Tax loss harvesting (#32).** Year-end review for capital loss
   opportunities.

8. **Retirement contribution maxing (#75-#83).**

9. **HSA contribution maxing (#63).**

10. **Education tax planning (#60-#61).**

11. **FSA election (#62).**

12. **Filing status optimization.** MFJ vs. MFS analysis (#65) for
    specific circumstances.

13. **Dependency claims.** Children, parents, qualifying relatives.

14. **State tax planning (#40).**

15. **Estate / gift planning.** Annual exclusion gifts (#46);
    lifetime exclusion use.

16. **Health insurance — employer coverage vs. marketplace
    subsidies.**

17. **SSDI / Social Security taxation planning.** Up to 85% of SS
    can be taxable; managing other income may reduce.

18. **Required Minimum Distributions (RMDs).** Age 73 (post-SECURE
    2.0); QCD coordination (#78).

19. **Medicare IRMAA planning.** Income brackets affect Part B and
    Part D premiums; manage AGI to avoid bracket increases.

20. **Quarterly estimated tax review.**

21. **Wage withholding optimization.** Form W-4 update for life
    changes.

22. **Refund / balance-due planning.** Avoid large refund (interest-
    free loan to government).

23. **Document retention.** 3-7 years (statute of limitations).

24. **Identity protection PIN (IP PIN) enrollment.** IRS-issued PIN
    for taxpayers with prior identity theft or proactively
    requested.

## Cross-references

- `state-tax-savings` (#40).
- `niit-minimization` (#69).
- `roth-ira-conversion` (#80).
- `qcd` (#78).
- `hsa-optimization` (#63).
- `flexible-spending-account` (#62).
- `married-filing-separate` (#65).
- `penalty-abatement` (#66).
- `late-penalties-interest` (#37).
- `capital-gain-offsets` (#32).

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

## Strategy #65: Married Filing Separate

**File:** `references/strategies/married-filing-separate.md`

```markdown
---
name: "Married Filing Separate (MFS) Analysis"
slug: married-filing-separate
type: Personal - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§1(d)", "§6013"]
forms: ["Form 1040 with MFS filing status"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Married Filing Separately (MFS) is generally less tax-favorable
than Married Filing Jointly (MFJ), but specific situations make
MFS preferable:

1. **Income-based student loan repayment.** IBR / PAYE / SAVE plans
   base monthly payment on AGI; MFS lowers each spouse's reported
   AGI.

2. **Large medical expenses for one spouse.** §213 itemized
   deduction threshold (7.5% of AGI) is per-return; MFS lower AGI
   may allow larger medical deduction.

3. **Large miscellaneous itemized deductions** (currently
   suspended under §67(g) but possibly restored — verify post-
   OBBBA).

4. **Liability protection from spouse's tax issues.** MFS doesn't
   create joint liability; protects from spouse's underreporting,
   tax shelter exposure, etc.

5. **Spouse owes back taxes / child support.** MFS protects
   refund from offset.

6. **Significantly different state tax treatment** for separate
   filing.

7. **One spouse died and surviving spouse remarried** (timing
   issue).

MFS disadvantages:
- Cannot claim Earned Income Credit (with limited exceptions).
- Cannot claim education credits.
- Cannot claim student loan interest deduction.
- Cannot deduct IRA contribution if either spouse covered by
  workplace plan above $10,000 income.
- Capital loss limit reduced to $1,500 (vs. $3,000 MFJ).
- Standard deduction is half MFJ.
- Both spouses must use same itemizing status (both itemize or
  both take standard).
- Various phaseouts hit harder.

The decision requires careful comparison: file mock-up MFS and
MFJ returns side-by-side; choose the lower-aggregate-tax option.

## Primary IRC authority

- §1(d) — Tax rates for unmarried (MFS uses unmarried rates with
  modifications).
- §6013 — Joint returns of income tax.
- §6013(a) — Election to file joint return.
- §6013(b) — Joint return after filing separate.
- §6013(d)(3) — Joint and several liability.

## Treasury regulations

- Reg §1.6013-1 through §1.6013-7.

## Key IRS guidance

- IRS Publication 501 — Dependents, Standard Deduction, and Filing
  Information.
- IRS Publication 504 — Divorced or Separated Individuals.

## Eligibility requirements

For MFS:
1. Married as of last day of tax year.
2. Election made on return.
3. Both spouses generally use same itemizing method.

For converting MFS to MFJ:
- Permitted by §6013(b) by filing amended return within 3 years.

For converting MFJ to MFS:
- NOT permitted after due date of return (with very limited
  exceptions for innocent spouse situations).

## Mechanics — how it works

1. **Run MFJ vs. MFS comparison.** Calculate total federal +
   state tax under both scenarios.
2. **Consider non-tax factors:** liability protection, student
   loan implications.
3. **File MFS if lower aggregate tax** OR if non-tax benefits
   outweigh tax cost.
4. **Coordinate state filing.** Most states require state filing
   to match federal status; some allow disconnect.

## Documentation requirements

- Comparison workpaper showing MFS vs. MFJ tax.
- Documented basis for non-tax MFS election.

## Common pitfalls / audit risks

- **Cannot reverse MFS to MFJ after due date.** Election is
  irrevocable.
- **Itemize-or-not consistency.** Both spouses must itemize OR
  both take standard.
- **Community property states.** MFS in CA, AZ, NM, NV, TX, ID,
  LA, WI, WA requires community property income/deduction
  allocation per state law.
- **Dependent claiming.** Each child claimed by only one spouse.
- **Phaseouts.** IRA deduction, Roth contribution, AMT exemption
  all hit MFS harder.

## Recent legislative changes

- **TCJA (2017)** — Various phaseouts adjusted.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA filing
  status Pub L 119-21]`. Working assumption: standard MFS rules
  preserved.

## State conformity considerations

States require state filing status to match federal; some
exceptions. **California, Arizona, Idaho, Louisiana, Nevada,
New Mexico, Texas, Washington, Wisconsin** are community property
states with allocation rules.

## Default confidence band rationale

**HIGH** — straightforward statutory framework. Decision is
analytical, not interpretive.

## Cross-references

- `individual-planning-ideas` (#64).
- `state-tax-savings` (#40).
- `education-credits` (#61) — MFS disqualification.
- `roth-ira-contributions` (#79).
- `niit-minimization` (#69).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 6013","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6013","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1(d)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #66: Penalty Abatement

**File:** `references/strategies/penalty-abatement.md`

```markdown
---
name: "Penalty Abatement (Comprehensive)"
slug: penalty-abatement
type: Personal - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§6651", "§6662", "§6664(c)", "§6707A", "§6699", "§6698"]
forms: ["Form 843", "Form 8857 (innocent spouse)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Comprehensive penalty abatement reference, expanding on #37 (FTA
and reasonable cause for §6651). This file addresses additional
penalty types and abatement mechanisms:

**§6662 Accuracy-Related Penalty (20%; 40% gross valuation):**
- Negligence or disregard of rules/regulations.
- Substantial understatement of income tax.
- Substantial valuation misstatement.
- Substantial overstatement of pension liabilities.
- Substantial estate/gift tax valuation understatement.
- Disallowance of treaty position without disclosure.
- Reasonable cause defense under §6664(c).

**§6707A Reportable Transaction Penalty:**
- Failure to disclose listed or reportable transaction on Form
  8886.
- $10,000 minimum / $50,000 maximum / $100,000 listed transactions.
- Limited reasonable cause defense.

**§6698 Failure to File Partnership Return:**
- $235 per partner per month (2024); maximum 12 months.
- Rev. Proc. 84-35 small partnership reasonable cause exception.

**§6699 Failure to File S Corp Return:**
- $235 per shareholder per month; max 12 months.
- Reasonable cause exception.

**§6694 Preparer Penalty:**
- Understatement due to unreasonable position.
- Reasonable cause defense and reasonable belief standard.

**§6701 Aiding and Abetting Penalty:**
- $1,000 / $10,000 (corp) per document.
- Limited abatement.

**Innocent Spouse Relief (§6015):**
- Three categories: §6015(b) traditional; §6015(c) separation of
  liability; §6015(f) equitable relief.
- Form 8857.

## Primary IRC authority

- §6651 — Failure to file/pay (see #37).
- §6662 — Accuracy-related penalty.
- §6662A — Listed transaction penalty.
- §6664(c) — Reasonable cause defense.
- §6694 — Preparer penalty.
- §6698 — Failure to file partnership return.
- §6699 — Failure to file S corp return.
- §6707A — Reportable transaction penalty.
- §6015 — Innocent spouse relief.
- §6404(e) — Interest abatement (see #37).

## Treasury regulations

- Reg §1.6662-1 through §1.6662-7.
- Reg §1.6664-1 through §1.6664-4.
- Reg §1.6707A-1.
- Reg §1.6015-1 through §1.6015-9.

## Key IRS guidance

- IRM 20.1 — Penalty Handbook (comprehensive).
- IRM 20.1.1.3.6.1 — First-Time Abate.
- Rev. Proc. 84-35 — Small partnership reasonable cause.

## Key court decisions

- **United States v. Boyle, 469 U.S. 241 (1985)** — Reliance on
  agent for filing not reasonable cause.
- **Klein v. Commissioner, 149 T.C. 341 (2017)** — Reasonable
  cause analysis.

## Mechanics — how it works

For §6662 penalty abatement:
1. **Identify category** of accuracy-related penalty.
2. **Reasonable cause and good faith** defense under §6664(c).
3. **Adequate disclosure** via Form 8275 / 8275-R may eliminate
   substantial understatement penalty even without reasonable
   cause.
4. **Form 843** with detailed statement.

For §6698 / §6699 partnership/S corp late filing:
1. **First-time abate** if eligible.
2. **Rev. Proc. 84-35 small partnership** — partnerships with ≤10
   partners; all partners filed timely; allocation per partnership
   agreement.
3. **Form 843** with reasonable cause explanation.

For innocent spouse:
1. **Form 8857.**
2. **Three categories** under §6015.
3. **2-year filing deadline** (generally) from first IRS collection
   activity.

## Documentation requirements

- Form 843 (most penalties) or Form 8857 (innocent spouse).
- Detailed reasonable cause statement.
- Supporting documentation.
- Compliance history (FTA eligibility).

## Common pitfalls / audit risks

- **§6662 reliance defense.** Reliance on tax advice from competent
  preparer can be reasonable cause IF preparer was given full
  facts.
- **§6707A no reasonable cause.** Listed transaction penalty has
  very limited reasonable cause defense; disclosure is the safe
  harbor.
- **Innocent spouse 2-year deadline.** Generally strict.
- **Adequate disclosure standard.** §6662(d)(2)(B) requires
  reasonable basis AND disclosure for substantial understatement
  protection.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA penalties
  Pub L 119-21]`. Working assumption: no major changes.

## State conformity considerations

States have parallel penalty regimes; abatement procedures vary.

## Default confidence band rationale

**HIGH** for FTA-eligible cases. **MODERATE** for reasonable cause
based on documentation.

## Cross-references

- `late-penalties-interest` (#37).
- `predict-reasonable-cause` (predict skill).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 6662","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6662","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 6664(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6664","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 6015","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6015","weight":"primary_statute"},
    {"authority_type":"RevProc","citation":"Rev. Proc. 84-35","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"SCOTUS","citation":"United States v. Boyle, 469 U.S. 241 (1985)","url":"https://www.supremecourt.gov","weight":"binding_judicial"}
  ]
}
```
```

---

## Strategy #67: Primary Home Sale Exclusion (§121)

**File:** `references/strategies/primary-home-sale-exclusion.md`

```markdown
---
name: "Primary Home Sale Exclusion (§121)"
slug: primary-home-sale-exclusion
type: Personal - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§121", "§1031(h)"]
forms: ["Form 8949", "Schedule D"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§121 allows a taxpayer to exclude up to:
- **$250,000 (single)** of gain from sale of principal residence.
- **$500,000 (married filing jointly)** of gain from sale of
  principal residence.

The exclusion is available once every 2 years and requires
satisfaction of two tests:

1. **Ownership test:** Taxpayer owned the property for at least 2
   of the last 5 years before sale.
2. **Use test:** Taxpayer used the property as principal residence
   for at least 2 of the last 5 years before sale.

The 2-year periods need not be continuous and need not coincide.

For MFJ $500K exclusion:
- Either spouse meets ownership test.
- Both spouses meet use test.
- Neither spouse used §121 exclusion in last 2 years.

Partial exclusion under §121(c) for sales due to:
- Change in employment (50+ miles).
- Health.
- Unforeseen circumstances (death, divorce, multiple births,
  involuntary conversion, etc.).

Pro rata exclusion based on time of qualifying use ÷ 2 years.

Recapture exception under §121(d)(11): non-qualified use after
2008 reduces exclusion proportionally if property was rented or
used for business.

§121(d)(10): For property converted from §1031 like-kind exchange
replacement to primary residence — must hold ≥5 years post-
exchange before §121 applies.

## Primary IRC authority

- §121 — Sale of principal residence.
- §121(a) — Exclusion.
- §121(b) — Limitations.
- §121(c) — Partial exclusion.
- §121(d) — Special rules (depreciation recapture, §1031, non-
  qualified use, etc.).
- §1031(h) — Coordination with like-kind exchange.

## Treasury regulations

- Reg §1.121-1 through §1.121-4.

## Key IRS guidance

- IRS Publication 523 — Selling Your Home.

## Key court decisions

- **Gates v. Commissioner, 135 T.C. 1 (2010)** — Property partially
  destroyed by fire; "principal residence" analysis.
- **Reesink v. Commissioner, T.C. Memo. 2012-118** — Principal
  residence test.

## Eligibility requirements

1. **Ownership ≥2 of last 5 years.**
2. **Use as principal residence ≥2 of last 5 years.**
3. **Not used §121 in last 2 years.**
4. **MFJ extra requirements** for $500K limit.

## Mechanics — how it works

1. **Determine basis** — original purchase + improvements -
   prior depreciation.
2. **Compute gain** — sale price - selling costs - basis.
3. **Apply §121 exclusion.** Up to $250K / $500K.
4. **Non-qualified use** — pro rata reduction post-2008.
5. **Depreciation recapture** — depreciation taken since May 6,
   1997 must be recaptured (taxed as unrecaptured §1250 gain;
   max 25%).
6. **Form 8949 / Schedule D** for any taxable gain.

## Documentation requirements

- Closing statements (purchase and sale).
- Improvements records (basis additions).
- Use and ownership timeline.
- Depreciation records (if business/rental use).

## Common pitfalls / audit risks

- **Property converted to rental and back.** Non-qualified use
  reduces exclusion.
- **Multiple residences.** Only "principal" residence qualifies.
- **2-year cap on exclusion.** Cannot use again within 2 years.
- **§1031 replacement converted to residence.** 5-year hold
  required under §121(d)(10).
- **Spouse §121 use during last 2 years.** Disqualifies $500K MFJ.
- **Inheritance basis.** Inherited property has step-up under
  §1014; §121 may not apply.
- **Depreciation recapture.** Taxed even if §121 excludes
  remaining gain.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §121
  Pub L 119-21]`. Some reports indicate proposals to increase
  $250K / $500K limits (which haven't been adjusted since 1997).
  Verify final OBBBA provision.

## State conformity considerations

State conformity to §121 generally complete. **Massachusetts,
Pennsylvania** have unique residence-sale treatment.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `1031-like-kind-exchange` (#1) — interaction.
- `installment-sale` (#33).
- `capital-gain-offsets` (#32).
- `state-tax-savings` (#40) — domicile change interaction.
- `rental-strategies` (#25) — converted-rental interaction.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 121","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section121","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.121-1","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TaxCt","citation":"Gates v. Commissioner, 135 T.C. 1 (2010)","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
```

---

**End of Part 7 of 10.** Strategies #58 through #67 delivered.

**Continue to Part 8 of 10** for strategies #68 through #77 (Employee Stock Options, NIIT Minimization, Series I Bond, Employer Benefit Package Review, Backdoor Roth, Defined Benefit / Cash Balance, LIRP [AGGRESSIVE], 401(k) Pre-Tax, SEP-IRA, SIMPLE IRA).
