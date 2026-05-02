# Vibe CPA Skills — Strategy Library Addendum (94 Strategies)

**Part 10 of 10** — Strategies #87 through #94, plus comprehensive cross-reference matrix.

**Part navigation:**
- Part 1: Exec summary, master index, PART A build-plan addendum, strategies #1–#7
- Part 2: Strategies #8–#17
- Part 3: Strategies #18–#27
- Part 4: Strategies #28–#37
- Part 5: Strategies #38–#47
- Part 6: Strategies #48–#57
- Part 7: Strategies #58–#67
- Part 8: Strategies #68–#77
- Part 9: Strategies #78–#86
- **Part 10: Strategies #87–#94 + cross-reference matrix** ← this file

---

## Strategy #87: Health Insurance — Self-Employed

**File:** `references/strategies/health-insurance-self-employed.md`

```markdown
---
name: "Self-Employed Health Insurance Deduction (§162(l))"
slug: health-insurance-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§162(l)"]
forms: ["Schedule 1 (above-the-line deduction)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

§162(l) provides an above-the-line deduction for health insurance
premiums paid by self-employed individuals. The deduction is
"above-the-line" on Schedule 1 of Form 1040, reducing AGI (not
just taxable income), and is available without itemizing.

The deduction covers:
- Medical, dental, and qualified long-term care insurance.
- For taxpayer, spouse, dependents, and §152(f)(2) children
  under age 27.

Key features:
1. **Above-the-line** — reduces AGI; benefits non-itemizers.
2. **Earned income limit** — deduction cannot exceed earned income
   from the trade or business that established the plan.
3. **Plan establishment** — plan must be in name of business OR
   in name of self-employed individual.
4. **NOT subject to SE tax reduction** — the deduction reduces
   income tax base but does NOT reduce SE tax base under
   §1402(a)(12). Common practitioner error.
5. **Coordination with §125 cafeteria plan** — sole proprietor
   cannot participate in §125 plan (must use §162(l) instead).
6. **Coordination with marketplace premium tax credit** —
   deduction reduces MAGI for §36B premium tax credit phaseout
   computation.
7. **§1402(a)(12) reduction** — no longer available; pre-2010
   special rule allowed deduction in computing SE tax was
   eliminated.

For S corp 2%+ shareholders: §162(l) applies via §1372 special
rule — see `health-insurance-s-corp` (#10).

For partners: §162(l) applies if partnership pays premium and
includes in K-1 guaranteed payment.

## Primary IRC authority

- §162(l) — Special rules for health insurance costs of self-
  employed individuals.
- §162(l)(1)(A) — Deduction equal to amount paid.
- §162(l)(2) — Earned income limitation.
- §162(l)(5) — Coordination with other rules.
- §1372 — S corp 2%+ shareholders treated as partners (interaction).
- §1402(a)(12) — Treatment for SE tax (deduction NOT allowed in
  computing SE tax post-2010).

## Treasury regulations

- Reg §1.162(l)-1 — Self-employed health insurance deduction.

## Key IRS guidance

- IRS Publication 535 — Business Expenses.
- IRS Publication 502 — Medical and Dental Expenses (for §213
  comparison).

## Eligibility requirements

1. **Self-employed individual** with net earnings from
   self-employment, OR partner in partnership, OR 2%+ S corp
   shareholder.
2. **Insurance plan established in name of business** OR in name
   of self-employed individual (post-Notice 2008-1 expansion).
3. **Eligible for employer-subsidized coverage NOT available** —
   if taxpayer or spouse eligible for subsidized coverage from
   another job, deduction unavailable for that month.
4. **Earned income from the business** establishing the plan ≥
   premium amount.

## Mechanics — how it works

1. **Verify plan establishment.** Sole proprietor: in name of
   individual is acceptable post-Notice 2008-1.
2. **Pay premium.** Direct payment by individual or by business.
3. **Compute earned income limit.** Self-employed: NESE less ½ SE
   tax less retirement plan contributions.
4. **Deduct on Schedule 1 line 17** — above-the-line.
5. **Coordinate with marketplace premium tax credit** — circular
   calculation under §36B because deduction reduces MAGI which
   affects credit which affects deduction.

## Documentation requirements

- Insurance policy and premium statements.
- Earned income computation worksheet.
- For S corp 2%+ shareholders: W-2 with proper Box 1 inclusion
  (#10).
- For partners: K-1 with guaranteed payment for premium.

## Common pitfalls / audit risks

- **Earned income limit.** Deduction cannot exceed business
  earnings from plan-establishing entity.
- **Multiple businesses.** Plan established by Business A;
  deduction limited to Business A earned income, not aggregate.
- **Eligibility for subsidized coverage.** Disqualifies for any
  month either spouse eligible for employer subsidy.
- **§125 coordination error.** Sole prop cannot use §125 cafeteria
  plan; must use §162(l).
- **§1402(a)(12) pre-2010 method.** Old practice of deducting in
  SE tax base was eliminated; some practitioners still incorrectly
  apply.
- **§213 itemized deduction.** Same premiums cannot be both
  §162(l) and §213.
- **Marketplace premium tax credit interaction.** Circular
  calculation requires care.

## Recent legislative changes

- **No material recent changes.**
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §162(l)
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §162(l) generally complete.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `health-insurance-s-corp` (#10) — S corp variant.
- `group-health-insurance` (#8).
- `hra-merp` (#11).
- `hsa-optimization` (#63).
- `accountable-plan-self-employed` (#84).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162(l)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.162(l)-1","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"}
  ]
}
```
```

---

## Strategy #88: Home Office Deduction — Self-Employed

**File:** `references/strategies/home-office-deduction-self-employed.md`

```markdown
---
name: "Home Office Deduction — Self-Employed (§280A)"
slug: home-office-deduction-self-employed
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§280A", "§280A(c)(1)", "§280A(c)(5)"]
forms: ["Form 8829 (actual expense method)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

§280A allows a self-employed individual to deduct expenses for the
business use of a home, subject to strict eligibility requirements
and limitations. Two methods:

**Simplified Method:**
- $5/square foot × business-use square footage.
- **Maximum 300 square feet** = $1,500 maximum deduction.
- No depreciation; no recapture on sale.
- Annual election (can switch year-to-year).
- Itemized deduction items (mortgage interest, property tax) still
  fully deductible on Schedule A.

**Actual Expense Method (Form 8829):**
- Compute total home expenses: mortgage interest, property tax,
  insurance, utilities, repairs, depreciation.
- Multiply by business-use percentage (typically square footage
  ratio).
- Direct expenses (improvements to home office only): 100%
  deductible.
- Indirect expenses (whole-home utilities, etc.): business %.
- Depreciation portion creates §1250 recapture exposure on sale.
- Itemized deduction items reduced by home-office portion.

§280A(c)(1) eligibility tests (must satisfy ALL):
1. **Regular use** — home office used regularly (not occasionally).
2. **Exclusive use** — area used SOLELY for business; any
   personal use defeats deduction.
3. **One of these:**
   - **Principal place of business** (under §280A(c)(1)(A)) —
     either where most income-producing activity occurs OR where
     administrative/management activities occur AND no other fixed
     location used substantially for those activities.
   - **Meeting customers/clients** (under §280A(c)(1)(B)) —
     regular meeting place.
   - **Separate structure** (under §280A(c)(1)(C)) — separate
     building (detached garage, shed, ADU) used for business.

§280A(c)(5) gross income limit:
- Home office deduction cannot create or increase Schedule C loss.
- Excess carries forward to future years.

§121 interaction:
- Home office depreciation taken since May 6, 1997 must be
  recaptured at sale (max 25% rate) regardless of §121 exclusion.
- Simplified method does NOT create depreciation recapture.

## Primary IRC authority

- §280A — Disallowance of certain expenses in connection with
  business use of home, rental of vacation homes, etc.
- §280A(c)(1) — Exception for business use.
- §280A(c)(5) — Gross income limitation.
- §280A(g) — Augusta Rule (separate strategy #24).
- §121(d)(6) — §121 exclusion does not apply to depreciation
  recapture portion.

## Treasury regulations

- Reg §1.280A-1 through §1.280A-3.

## Key IRS guidance

- Rev. Proc. 2013-13 — Simplified method.
- IRS Publication 587 — Business Use of Your Home.
- Form 8829 instructions.

## Key court decisions

- **Commissioner v. Soliman, 506 U.S. 168 (1993)** — Principal
  place of business analysis pre-1999 amendments.
- **Hamacher v. Commissioner, 94 T.C. 348 (1990)** — Strict
  exclusive-use requirement.

## Eligibility requirements

§280A(c)(1) requirements all must be met:
1. Regular use.
2. Exclusive use.
3. One of: principal place of business, meet customers/clients, or
   separate structure.

## Mechanics — how it works

For Simplified Method:
1. **Measure business-use square footage** (max 300).
2. **Multiply by $5.**
3. **Schedule C direct deduction.**

For Actual Expense Method:
1. **Compute home expenses by category.**
2. **Apply business-use percentage** (square footage typically).
3. **Form 8829 computation.**
4. **§280A(c)(5) gross income limit.**
5. **Carryforward of excess.**
6. **Track depreciation** for §1250 recapture.

## Documentation requirements

- Home office floor plan / square footage.
- Photos showing exclusive-use nature.
- Home expense records (mortgage statements, utility bills, etc.).
- Form 8829 (actual method).
- Depreciation schedule (actual method).

## Common pitfalls / audit risks

- **Exclusive use violation.** Personal use of office area defeats
  entire deduction.
- **"Convenience of employer" test for employees.** Pre-TCJA test
  for employees no longer relevant (no employee home office
  deduction post-§67(g) suspension).
- **Home office in non-deductible business activity.** §280A
  presupposes §162 trade or business.
- **§280A(c)(5) gross income limit.** Cannot create loss; carries
  forward.
- **Depreciation recapture surprise** at sale.
- **Method election.** Annual; can switch.
- **Day-care exception.** §280A(c)(4) special rule for family
  day care.

## Recent legislative changes

- **TCJA (2017)** — Eliminated §67(g) employee home office
  deduction.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §280A
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** for properly-documented home offices with clear exclusive
use. Drops to MODERATE for borderline exclusive-use arrangements.

## Cross-references

- `accountable-plan-home-office` (#2) — corporate variant.
- `accountable-plan-self-employed` (#84).
- `augusta-rule-280a-g` (#24) — separate §280A(g) strategy.
- `primary-home-sale-exclusion` (#67) — depreciation recapture
  interaction.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 280A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 280A(c)(5)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute"},
    {"authority_type":"RevProc","citation":"Rev. Proc. 2013-13","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"SCOTUS","citation":"Commissioner v. Soliman, 506 U.S. 168 (1993)","url":"https://www.supremecourt.gov","weight":"binding_judicial"}
  ]
}
```
```

---

## Strategy #89: Bonus / §179 Depreciation — Self-Employed

**File:** `references/strategies/bonus-179-depreciation-self-employed.md`

```markdown
---
name: "Bonus / §179 Depreciation — Self-Employed Maximization"
slug: bonus-179-depreciation-self-employed
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§168", "§168(k)", "§179", "§280F"]
forms: ["Form 4562", "Schedule C"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Self-employed application of bonus depreciation and §179 expensing
parallels corporate context (#12) but with Schedule C mechanics
and unique self-employment considerations:

1. **§179 election limited to net business income.** Cannot create
   or increase Schedule C loss.
2. **§168(k) bonus has NO income limit** — can create loss.
3. **§461(l) excess business loss** — limits net business loss
   to threshold ($305K single / $610K MFJ for 2024); excess becomes
   NOL.
4. **SE tax interaction** — depreciation reduces Schedule C net
   profit, reducing both income tax base AND SE tax base.

OBBBA reportedly restored 100% bonus depreciation. Verify via
Classification Tables.

Self-employed strategic considerations:
- **Heavy SUV strategy** — vehicles >6,000 lbs GVWR escape §280F;
  $30,500 §179 (2024 SUV limit) plus remaining basis at §168(k)
  bonus.
- **Equipment purchases** — §179 first up to net income; §168(k)
  bonus on remainder.
- **§263A UNICAP** for inventory production.
- **De minimis safe harbor (#28)** for items under threshold.

## Primary IRC authority

- §168 — MACRS.
- §168(k) — Bonus depreciation.
- §179 — Expensing election.
- §179(b)(3) — Income limitation.
- §280F — Luxury auto cap.
- §461(l) — Excess business losses.
- §263A — UNICAP.

## Treasury regulations

- Reg §1.168(k)-2 — Bonus depreciation.
- Reg §1.179-1 through §1.179-6.
- Reg §1.263(a)-1, -2, -3 — Tangible property regs.
- Reg §1.461-1 — Timing.

## Key IRS guidance

- Rev. Proc. 2019-08, 2019-13 — §168(k) procedural.
- Rev. Proc. 2020-25 — QIP CARES Act fix.
- IRS Publication 946 — How to Depreciate Property.

## Eligibility requirements

For §168(k) bonus:
1. Tangible property class life ≤20 years.
2. Acquired and placed in service after applicable date.
3. NOT acquired from related party.

For §179:
1. Tangible §1245 property (including off-the-shelf software).
2. Limited categories of §1250 (real property).
3. Acquired by purchase from unrelated party.
4. Election made on Form 4562.
5. Subject to §179(b)(3) taxable income limit.

## Mechanics — how it works

1. **Identify capital expenditures.**
2. **Apply tangible property regulations** (capitalize vs.
   expense).
3. **De minimis safe harbor** for items under threshold.
4. **§179 first** up to net business income limit.
5. **§168(k) bonus** on remainder.
6. **§280F limit** for light passenger autos.
7. **§461(l) excess business loss** — net loss limited to threshold.
8. **State decoupling** — track separately for major decoupling
   states.
9. **Form 4562.**

## Documentation requirements

- Asset acquisition records.
- Placed-in-service dates.
- Form 4562.
- For SUVs: GVWR documentation.

## Common pitfalls / audit risks

- **§179 income limit.** Cannot create loss; carryforward.
- **§168(k) bonus + §461(l).** Bonus can create loss but
  §461(l) limits net business loss.
- **Related-party acquisition.** §168(k) excluded.
- **Placed in service before year end.** Must be ready and
  available for use.
- **State decoupling.** CA, NY, NJ, MA, MD, MN, PA require
  add-back.
- **§280F luxury auto.** Light passenger autos capped.

## Recent legislative changes

- **TCJA (2017)** — Used property eligible; §179 expansion.
- **CARES Act (2020)** — QIP fix.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §168(k)
  100% bonus Pub L 119-21]`. Restoration significantly increases
  benefit.

## State conformity considerations

Major decoupling states require state add-back tracking.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `bonus-and-section-179-depreciation` (#12) — corporate context.
- `business-vehicle-self-employed` (#85).
- `de-minimis-safe-harbor` (#28).
- `de-minimis-safe-harbor-self-employed` (#93).
- `cost-segregation` (#41).
- `nol-carryback-carryforward` (#15).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 168(k)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section168","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 179","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section179","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 461(l)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section461","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #90: Minimize Self-Employment Tax

**File:** `references/strategies/minimize-self-employment-tax.md`

```markdown
---
name: "Minimize Self-Employment Tax"
slug: minimize-self-employment-tax
type: SE Tax
tax_type: 2SH
complexity: High
irc_sections: ["§1401", "§1402", "§1402(a)(13)", "§3121", "§1361-1378"]
forms: ["Schedule SE", "Form 1040", "Form 1120-S"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

> **Caution:** SE tax minimization strategies — especially S corp
> election, limited partner classification, and family employment
> structures — are heavily IRS-audited. Each strategy requires
> substance and documentation. Aggressive implementations face
> reasonable compensation challenges (#21), Renkemeyer-style
> limited partner SE tax inclusion, and family employment substance
> challenges.

## Overview

Comprehensive umbrella for SE tax minimization, integrating
multiple strategies covered elsewhere:

**SE Tax Mechanics:**
- 12.4% Social Security on first $168,600 (2024 wage base; verify
  2025).
- 2.9% Medicare on all earnings.
- 0.9% Additional Medicare on earnings >$200K single / $250K MFJ.
- ½ SE tax deductible above-the-line under §164(f).

**Primary minimization strategies:**

1. **S corp election (#86).** Wages-vs-distribution split. The
   most powerful tool; saves 15.3% on distribution portion.
   Requires reasonable compensation (#21).

2. **Limited partner classification (#86).** §1402(a)(13) excludes
   limited partner share of partnership earnings. Renkemeyer
   narrowed exception; active participants in service partnerships
   subject to SE tax even if structured as LP.

3. **Hiring spouse / kids (#49, #50).** Family wages reduce
   Schedule C net profit; FICA exemption for children under 18 in
   sole prop.

4. **Reasonable compensation analysis (#21).** S corp owner-
   employee comp must be defensible.

5. **§125 cafeteria plan participation.** S corp 2%+ shareholders
   ineligible (cannot reduce wages pre-tax). Sole proprietors also
   ineligible.

6. **Retirement plan contributions.** §401(k) employee deferrals
   reduce W-2 Box 1 (income tax) but NOT Box 3, 5 (FICA). SEP-IRA
   employer contributions reduce Schedule C net profit (reducing
   both income tax and SE tax).

7. **Health insurance.** §162(l) above-the-line deduction; does
   NOT reduce SE tax base post-2010.

8. **HSA contributions.** Above-the-line deduction; reduces income
   tax but NOT SE tax.

9. **§179 / §168(k) depreciation.** Reduces Schedule C net profit
   (reducing both income tax and SE tax).

10. **Active vs. passive activity classification.** Material
    participation in §469 trade or business → Schedule C with SE
    tax. Investor in passive activity → Schedule E without SE tax.

## Primary IRC authority

- §1401 — Self-employment tax rate.
- §1402(a) — Net earnings from self-employment.
- §1402(a)(12) — Health insurance treatment (no longer reduces SE
  tax).
- §1402(a)(13) — Limited partner exclusion.
- §1402(a)(2) — Real estate rental exclusion.
- §3101 — FICA on employees.
- §3121 — FICA wages.
- §1361-1378 — S corporation rules.
- §164(f) — ½ SE tax deduction.
- §469 — Passive activity (interaction).

## Treasury regulations

- Reg §1.1401, 1.1402.
- Reg §1.3121.
- Reg §1.1361 et seq.

## Key IRS guidance

- IRS Publication 533.
- IRS Publication 535.
- IRS Fact Sheet 2008-25 (S corp comp).

## Key court decisions

- **Renkemeyer, Campbell & Weaver, LLP v. Commissioner, 136 T.C.
  137 (2011)** — Limited partners in active law practice subject
  to SE tax.
- **Castigliola v. Commissioner, T.C. Memo. 2017-62** — LLC active
  members subject to SE tax.
- **Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)** — S
  corp reasonable compensation.
- **Soroban Capital Partners LP v. Commissioner, 161 T.C. No. 12
  (2023)** — State law limited partner status alone insufficient
  for §1402(a)(13) exclusion; functional analysis required.

## Mechanics — how it works

Strategic decision framework:
1. **Determine entity** — sole prop, partnership, S corp, C corp.
2. **Run break-even analysis** — S corp election typically
   beneficial above $80K-$100K net profit.
3. **Set reasonable compensation** with documentation.
4. **Implement family employment** if appropriate.
5. **Maximize retirement contributions** (deductible at Schedule
   C reduces SE tax; SEP-IRA / Solo 401(k) employer portion
   reduces SE base).
6. **Annual review** — SE tax minimization is ongoing.

## Documentation requirements

- Reasonable compensation analysis (S corp).
- Family employment documentation (#49, #50).
- Limited partner functional analysis (post-Soroban).
- Entity formation and election documents.
- Retirement plan documents.

## Common pitfalls / audit risks

- **S corp reasonable comp challenge.** Watson, Spicer, JD &
  Associates.
- **Limited partner trap.** Renkemeyer, Castigliola, Soroban —
  active partners cannot rely on LP status alone.
- **Family employment substance.** Eller, Denman.
- **Self-rental recharacterization (#16).**
- **§1402(a)(2) real estate rental exclusion misuse.** Real estate
  rental from §469 generally not SE income, but service-laden
  rental (hotels, B&Bs) is SE.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1401
  §1402 Pub L 119-21]`. Working assumption: standard rules
  preserved.

## State conformity considerations

State franchise / entity taxes vary widely.

## Default confidence band rationale

**MODERATE** — multi-strategy umbrella with fact-intensive
substance requirements per strategy.

## Cross-references

- `choice-of-entity-se-tax` (#86) — primary entity decision.
- `reasonable-comp-corp-owners` (#21).
- `hiring-kids` (#49) and `wages-spouse-parents` (#50).
- `solo-401k-employer-contributions` (#82).
- `sep-ira-self-employed` (#81).
- `health-insurance-self-employed` (#87).
- `qbi-deduction` (#19).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 1401","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1402(a)(13)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1402","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Renkemeyer, Campbell & Weaver, LLP v. Commissioner, 136 T.C. 137 (2011)","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Soroban Capital Partners LP v. Commissioner, 161 T.C. No. 12 (2023)","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
```

---

## Strategy #91: Prepayment of Expense — Self-Employed

**File:** `references/strategies/prepayment-expense-self-employed.md`

```markdown
---
name: "Prepayment of Expense — Self-Employed (12-Month Rule)"
slug: prepayment-expense-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§461", "§263(a)"]
forms: ["Schedule C"]
state_specific: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Self-employed application of the 12-month rule prepayment strategy
(see #18 for full coverage). Reg §1.263(a)-4(f) allows cash-basis
taxpayers to deduct prepaid expenses if the right or benefit does
not extend beyond the earlier of (a) 12 months after the first
date on which the right or benefit begins or (b) the end of the
following tax year.

For Schedule C taxpayers, this is a primary year-end planning
lever. December prepayments of:
- Insurance (next year's annual premium).
- Rent on business space (12 months in advance).
- Subscriptions and software annual renewals.
- Service contracts.
- Professional dues and memberships.
- Continuing education registration fees.

create current-year deductions reducing both income tax base AND
SE tax base.

§448 cash method threshold: TCJA increased small-business cash-
method threshold to $25M average annual gross receipts (now
indexed to ~$30M for 2024). Most Schedule C filers use cash method.

## Primary IRC authority

- §461 — General timing rule.
- §263(a) — Capital expenditures.
- §446 — Methods of accounting.
- §448 — Cash method limitations.
- §461(g) — Prepaid interest (not deductible in advance).

## Treasury regulations

- Reg §1.263(a)-4(f) — 12-month rule.
- Reg §1.461-1 — Timing.

## Key IRS guidance

- IRS Publication 538 — Accounting Periods and Methods.

## Eligibility requirements

For cash-basis self-employed:
1. Right or benefit does not extend beyond earlier of 12 months
   after benefit begins or end of following tax year.
2. Payment is for non-tax-shelter expenditure.
3. Item is not specifically capitalized under another rule.

## Mechanics — how it works

1. **Year-end planning review** — identify upcoming prepayable
   expenses.
2. **Prepay before December 31.**
3. **Deduct full amount on Schedule C.**
4. **Reduces income tax AND SE tax base.**

## Documentation requirements

- Vendor invoices showing service period.
- Payment records dated current year.

## Common pitfalls / audit risks

- **Benefit extends beyond 12 months.** Two-year service contract
  in advance does not qualify.
- **Prepaid interest under §461(g).** Must spread over loan period.
- **Tax shelter taxpayer.** §461(i) imposes accrual.

## Recent legislative changes

- **TCJA (2017)** — Increased small-business cash-method threshold.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §461 §448
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — clear regulatory safe harbor.

## Cross-references

- `prepayment-of-expense` (#18) — corporate context.
- `maximize-business-deductions` (#13).
- `accountable-plan-self-employed` (#84).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 461","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section461","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.263(a)-4(f)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"}
  ]
}
```
```

---

## Strategy #92: Split Entity Operations vs Real Estate

**File:** `references/strategies/split-entity-operations-vs-re.md`

```permission
---
name: "Split Operating Entity from Real Estate Holding Entity"
slug: split-entity-operations-vs-re
type: SE Tax
tax_type: EFR
complexity: High
irc_sections: ["§469", "§1031", "§1411", "§199A", "§267"]
forms: ["Form 1065 / 1120-S / 1040"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Splitting an operating business from the real estate it occupies
into separate entities is a foundational planning structure for
operating businesses that own their real estate. Common structure:

- **Operating Entity (S corp or LLC):** Conducts the trade or
  business; pays rent to RE entity.
- **Real Estate Entity (LLC):** Holds the real estate; receives
  rent.

Strategic benefits:

1. **Asset protection.** RE not exposed to operating business
   liability.

2. **§469 self-rental rule (#16).** Rent paid by operating
   business to commonly-controlled RE entity is recharacterized as
   nonpassive net rental INCOME (under Reg §1.469-2(f)(6)) — but
   the RECHARACTERIZATION is one-way: income recharacterized as
   nonpassive cannot be offset by passive losses; but losses
   remain passive. Practical effect: rent income is nonpassive
   (offsettable by other nonpassive income or no other income),
   but if RE entity has losses, they remain passive.

3. **§1031 like-kind exchange flexibility.** RE entity can do
   §1031; operating business assets generally cannot.

4. **Estate planning.** RE can be gifted/inherited separately
   from business.

5. **Future sale flexibility.** Sell business without selling RE
   (or vice versa).

6. **Cost-segregation maximization** on RE entity.

7. **§199A QBI optimization** — rent income may be QBI under
   Notice 2019-07 safe harbor (250 hours of rental services) if
   RE constitutes a trade or business; otherwise not QBI.

8. **NIIT planning (#69)** — net rental income may or may not be
   NIIT depending on §469 trade or business classification under
   §1411.

Limitations:
- **§267 related-party rules.** Rent must be at arm's-length;
  excess rent recharacterized.
- **§469(j)(8) self-rental fix-up.** Self-rental rule limits
  passive loss strategies but does not eliminate the need for
  arm's-length rent.
- **Operating expense allocation.** Mortgage interest, property
  tax, insurance must be properly allocated between entities.

## Primary IRC authority

- §469 — Passive activity.
- §469(c)(2) — Per-se passive treatment of rentals.
- §1031 — Like-kind exchange.
- §1411 — NIIT.
- §199A — QBI.
- §267 — Related-party rules.
- §482 — Transfer pricing (intercompany).

## Treasury regulations

- Reg §1.469-2(f)(6) — Self-rental recharacterization.
- Reg §1.469-4 — Definition of activity (grouping interaction).
- Reg §1.1411-4 — NIIT trade or business analysis.
- Reg §1.199A-1 through 1.199A-6.

## Key IRS guidance

- Notice 2019-07 — Rental real estate enterprise §199A safe harbor
  (250 hours of rental services).
- IRS Publication 925.

## Key court decisions

- **Krukowski v. Commissioner, 114 T.C. 366 (2000)** — Self-rental
  rule applied.
- **Beecher v. Commissioner, 481 F.3d 717 (9th Cir. 2007)** —
  Self-rental upheld.
- **Schwalbach v. Commissioner, 111 T.C. 215 (1998)** — Self-
  rental analysis.

## Eligibility requirements

For valid split structure:
1. Bona fide separate entities.
2. Arm's-length rent.
3. Properly documented lease agreement.
4. Each entity properly capitalized.
5. Each entity respects formalities.

## Mechanics — how it works

1. **Form RE entity** (typically LLC) and transfer real estate
   into it (or purchase RE in entity initially).
2. **Form / maintain operating entity** (S corp or LLC).
3. **Establish lease** at fair market rent supported by
   comparables or appraisal.
4. **Operating entity pays rent** to RE entity.
5. **RE entity pays mortgage, property tax, insurance, repairs,
   improvements.**
6. **Operating entity deducts rent** as §162.
7. **RE entity reports rent income.** Subject to §469 and §1411
   analysis.
8. **§469 grouping consideration (#9)** — may affect both passive
   activity classification and §199A aggregation.

## Documentation requirements

- Entity formation documents.
- Lease agreement.
- Rent comparables / appraisal (arm's-length support).
- Annual rent payment records.
- Maintenance cost allocation between entities.

## Common pitfalls / audit risks

- **Rent not at arm's-length.** Below-market rent may be
  recharacterized as gift or capital contribution; above-market
  rent may be recharacterized as dividend.
- **§267 related-party loss disallowance.**
- **Self-rental recharacterization** of rent income as nonpassive
  (limits offsetting by passive losses).
- **§199A QBI uncertainty.** Whether rental constitutes §162 trade
  or business affects QBI eligibility.
- **§1411 NIIT applicability.** Self-rental income still NII unless
  rises to §162 trade or business level under §469.
- **State entity tax overhead** — separate entity adds franchise
  tax, return filing, state-level fees.

## Recent legislative changes

- **TCJA (2017)** — Created §199A; QBI analysis now relevant for
  rental activities.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §199A
  §469 Pub L 119-21]`. Working assumption: framework preserved.

## State conformity considerations

State entity-tax overhead and reporting requirements vary. **CA,
NY, TX** have meaningful state-level entity taxes.

## Default confidence band rationale

**HIGH** for properly-structured arm's-length splits. Drops to
MODERATE for rent valuation issues or §199A trade-or-business
classification.

## Cross-references

- `passive-income-pigs` (#16) — self-rental rule detail.
- `grouping-of-activities` (#9).
- `1031-like-kind-exchange` (#1).
- `cost-segregation` (#41).
- `qbi-deduction` (#19).
- `niit-minimization` (#69).
- `rental-strategies` (#25).
- `c-corp-state-tax-savings` (#35).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 469","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.469-2(f)(6)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TaxCt","citation":"Krukowski v. Commissioner, 114 T.C. 366 (2000)","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"Notice","citation":"Notice 2019-07","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
```

---

## Strategy #93: De Minimis Safe Harbor — Self-Employed

**File:** `references/strategies/de-minimis-safe-harbor-self-employed.md`

```markdown
---
name: "De Minimis Safe Harbor — Self-Employed"
slug: de-minimis-safe-harbor-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§263(a)"]
forms: ["No specific form; election annually on timely return"]
state_specific: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Self-employed application of de minimis safe harbor (see #28 for
corporate context). Reg §1.263(a)-1(f) allows election to deduct
tangible property under threshold:

- **$2,500 per item** for non-AFS taxpayers (most self-employed).
- **$5,000 per item** for AFS taxpayers (rare for self-employed).

Annual election required by attached statement.

For sole proprietors, the de minimis safe harbor is the simplest
mechanism for routine small-asset purchases (computers, peripherals,
small office equipment, tools, etc.). Avoids depreciation tracking
on items individually under threshold.

## Primary IRC authority

- §263(a) — Capital expenditures.
- §162(a) — Trade or business expenses.

## Treasury regulations

- Reg §1.263(a)-1(f) — De minimis safe harbor.

## Key IRS guidance

- Notice 2015-82 — Threshold increase.
- Rev. Proc. 2015-20 — Small business tangible property
  procedures.

## Eligibility requirements

For non-AFS:
1. Item cost ≤$2,500 per item (per invoice or substantiated per
   item).
2. Annual election attached to timely-filed return.
3. Property is not inventory.

## Mechanics — how it works

1. **Annual election** via attached statement.
2. **Apply threshold per item.**
3. **Deduct items under threshold** as Schedule C ordinary expense.
4. **Items over threshold** continue under §168 / §179 / §168(k).

## Documentation requirements

- Election statement attached to return.
- Invoices substantiating per-item cost.

## Common pitfalls / audit risks

- **Annual election forgotten.** Must be made each year.
- **Per-invoice vs. per-item.** Threshold per item; one invoice
  for multiple items qualifies if each item is under threshold.
- **Inventory disqualified.**

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §263 de
  minimis Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — explicit regulatory safe harbor.

## Cross-references

- `de-minimis-safe-harbor` (#28).
- `bonus-and-section-179-depreciation` (#12).
- `bonus-179-depreciation-self-employed` (#89).
- `accountable-plan-self-employed` (#84).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 263(a)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section263","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.263(a)-1(f)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"Notice","citation":"Notice 2015-82","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
```

---

## Strategy #94: Hiring Kids — Self-Employed

**File:** `references/strategies/hiring-kids-self-employed.md`

```markdown
---
name: "Hiring Kids — Self-Employed (Sole Prop / Partnership) Variant"
slug: hiring-kids-self-employed
type: SE Tax
tax_type: EFR
complexity: Medium
irc_sections: ["§3121(b)(3)(A)", "§162", "§3306(c)(5)", "§3401(a)(4)"]
forms: ["W-2", "Schedule C / 1065"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

> **Caution:** This strategy is subject to the same fact-intensive
> substance requirements as #49 (corporate context). Wages must be
> for bona fide work performed at reasonable compensation, with
> contemporaneous documentation. Eller and Denman cases established
> the standard. Family employment lacking substance is denied.

## Overview

Self-employed variant of hiring kids strategy (#49), with the
critical advantage of §3121(b)(3) FICA exemption applying to
children under 18 employed by parent's:

1. **Sole proprietorship** (Schedule C), OR
2. **Partnership where ALL partners are parents** (single set of
   parents).

The FICA exemption produces these benefits stacked together:

1. **Child receives W-2 wages** taxed at child's bracket (typically
   0% up to standard deduction $14,600 for 2024).
2. **No FICA** on those wages (15.3% savings vs. corporate or
   non-qualifying structure).
3. **No FUTA** on wages to children under 21 (§3306(c)(5)).
4. **Sole prop / partnership deducts wages** on Schedule C / Form
   1065 — reducing both income tax base AND SE tax base.
5. **Child can fund Roth IRA** up to lesser of earned income or
   $7,000 (2024).

Combined effect: parent shifts $14,600 to child at 0% bracket;
parent saves SE tax (15.3%) on full $14,600 (because Schedule C
profit reduced); $14,600 funds Roth IRA for child.

§3121(b)(3) FICA exemption does NOT apply to:
- Children employed by parent-owned C corporation.
- Children employed by parent-owned S corporation.
- Children employed by partnership where any partner is not the
  child's parent.
- Children of a single member LLC taxed as a corporation.

For LLC: default partnership treatment (multi-member) or
disregarded entity (single-member with parent as sole owner) — both
qualify for §3121(b)(3) FICA exemption when child is employed by
parent.

## Primary IRC authority

- §3121(b)(3)(A) — FICA exemption for child under 18 employed by
  parent in unincorporated business.
- §3306(c)(5) — FUTA exemption (under 21).
- §3401(a)(4) — Income tax withholding exemption (limited).
- §162 — Trade or business expense.
- §1402 — SE tax (interaction).
- §1(g) — Kiddie tax (does NOT apply to earned income).

## Treasury regulations

- Reg §31.3121(b)(3)-1 — FICA family employment.
- Reg §31.3306(c)(5)-1 — FUTA family employment.
- Reg §1.162-7 — Reasonable compensation.

## Key IRS guidance

- IRS Publication 15 — Employer's Tax Guide.
- IRS Publication 51 — Agricultural Employer's Tax Guide.
- IRS Publication 334 — Tax Guide for Small Business.

## Key court decisions

- **Eller v. Commissioner, 77 T.C. 934 (1981)** — Wages to child
  must be reasonable.
- **Denman v. Commissioner, 48 T.C. 439 (1967)** — Family employment
  must reflect actual services.

## Eligibility requirements

For §162 deduction:
1. Bona fide work performed.
2. Reasonable compensation.
3. Compliance with child labor laws.
4. Documentation.

For §3121(b)(3) FICA exemption:
1. Child under age 18.
2. Employed by parent's sole proprietorship OR partnership where
   ALL partners are parents.
3. Does NOT apply to corporation (C or S) or LLC taxed as
   corporation.

## Mechanics — how it works

1. **Identify legitimate work** appropriate for child's age.
2. **Establish work agreement.** Job description, hourly rate, pay
   schedule.
3. **Track hours and tasks** contemporaneously.
4. **Pay wages on regular schedule.** Direct deposit or check.
5. **§3121(b)(3) FICA exemption** applies to sole prop / parent-only
   partnership.
6. **W-2 issued at year-end.** With FICA boxes (Box 3, 5)
   appropriately blank or zero for FICA-exempt wages.
7. **Child files own return** if required.
8. **Roth IRA contribution** funded by child or parent up to earned
   income / annual limit.

## Documentation requirements

- Job description and work agreement.
- Time records (contemporaneous).
- Pay records (direct deposit confirmations, canceled checks).
- W-2 issued with proper Box 3, 5 treatment for FICA-exempt wages.
- Records establishing reasonableness.
- State child labor law compliance.

## Common pitfalls / audit risks

- **No actual work** (Eller/Denman pattern).
- **Unreasonable compensation.**
- **Reconstructed time records.**
- **Corporation employment.** §3121(b)(3) FICA exemption does NOT
  apply; common error.
- **LLC taxed as corporation.** Same — FICA exemption lost.
- **Multi-member partnership with non-parent partner.** FICA
  exemption lost.
- **State child labor law violation.**
- **Withholding errors.** Federal income tax may be required.
- **W-2 vs. 1099.** Children should be W-2 employees; FICA
  exemption applies to W-2 only.
- **Spouse-as-non-parent partnership.** If business structured as
  partnership with spouse, all partners are parents and exemption
  preserved.

## Recent legislative changes

- No material recent changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §3121
  family employment Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §3121 family employment exemption varies.
State child labor laws layer additional restrictions.

## AICPA SSTS / Circular 230 considerations

Family employment is fact-intensive. Practitioner should: verify
work substance; document reasonableness; advise on child labor law
compliance; recommend Form W-2 (not 1099) for clarity.

## Default confidence band rationale

**MODERATE** — fact-intensive. HIGH for properly-documented,
reasonable, substantive employment. LOW for token employment of
young children with high pay and minimal documented work.

## Cross-references

- `hiring-kids` (#49) — corporate context.
- `wages-spouse-parents` (#50).
- `roth-ira-contributions` (#79).
- `income-shifting-family-member` (#48).
- `reasonable-comp-corp-owners` (#21).
- `hra-merp` (#11) — interaction with family HRA structures.
- `minimize-self-employment-tax` (#90).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 3121(b)(3)(A)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section3121","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 162(a)(1)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 31.3121(b)(3)-1","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TaxCt","citation":"Eller v. Commissioner, 77 T.C. 934 (1981)","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Denman v. Commissioner, 48 T.C. 439 (1967)","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
```

---

# CROSS-REFERENCE MATRIX

This matrix documents how the 94 strategies interact: which combine well, which conflict, and which are mutually exclusive. The Vibe TB skills platform should surface relevant interactions when a user combines strategies, flagging conflicts and suggesting complementary additions.

## Format

For each strategy ID, three categories of relationship:
- **Combines with:** Strategies that complement and stack benefits.
- **Conflicts with:** Strategies that cannot be used simultaneously, or where one significantly reduces the benefit of the other.
- **Mutually exclusive with:** Strategies that are alternative paths to the same goal — choosing one means not choosing the other.

## Cross-reference table

| ID | Strategy | Combines with | Conflicts with | Mutually exclusive with |
|---|---|---|---|---|
| 1 | 1031 Like-Kind Exchange | #25, #41, #92 | #29 (DST), #30 (loss recognition) | #33 (installment), #34 (QOZ), #67 (§121) |
| 2 | Accountable Plan / Home Office | #4, #5, #22, #23 | None | #84 (Schedule C direct deduction) |
| 3 | Active Participation in RE | #25, #41 | None directly | #20 (REPS — superior path) |
| 4 | Business Vehicle Usage | #2, #12, #22, #23 | None | #85 (SE variant) |
| 5 | Cell Phone | #2, #22 | None | None |
| 6 | Day Trader / §475(f) | None | §1411 NIIT (§475 income still NII for non-trade) | None |
| 7 | ESOP | #21 reasonable comp | §409A interaction | None |
| 8 | Group Health Insurance | #62, #71 | #11 standalone HRA (Notice 2013-54) | #10 (S corp variant) |
| 9 | Grouping of Activities | #20 REPS, #19 §199A aggregation | Self-rental (#16) | None |
| 10 | Health Insurance — S Corp | #21, #71 | None | #87 (SE variant), #8 (group plan) |
| 11 | HRA / MERP | #50 (spouse employee) | #8 standalone (Notice 2013-54), #62 HCFSA | None directly |
| 12 | Bonus & §179 Depreciation | #28, #41, #85, #89 | #461(l) excess business loss | None |
| 13 | Maximize Business Deductions | All deduction-related | None | None |
| 14 | Meals & Entertainment | #2, #13 | None | None |
| 15 | NOL Carryback / Carryforward | #30, #44 (W-2 wage history) | None | None |
| 16 | Passive Income & PIGs | #3, #9 | Self-rental rule | #20 REPS (different path), #17 PTET |
| 17 | PTET | #19 (interacts with state income), #25 | None | None directly |
| 18 | Prepayment of Expense | #13 | None | #91 (SE variant) |
| 19 | QBI Deduction | #9 (aggregation), #20, #25, #57, predict-qbi-eligibility | C corp election (#47) | #47 (C corp shifts income out of QBI) |
| 20 | Real Estate Professional | #9, #20, #25, #41, predict-real-estate-pro | #69 (NIIT may not apply if §162 trade) | #3 (under-threshold alternative), #26 (STR alternative) |
| 21 | Reasonable Comp Corp Owners | #19, #22, #50, #82, predict-reasonable-comp | None | #86 (SE alternative analysis) |
| 22 | Reimbursement of Business Expenses | #2, #4, #5 | None | #84 (SE variant) |
| 23 | Reimbursement Depreciation S-Corp Vehicle | #4, #12 | Standard mileage with #4 (lock-in) | #4 (alternative method) |
| 24 | Augusta Rule | #2, #14 | Total annual rentals >14 days | None |
| 25 | Rental Strategies | #1, #3, #9, #16, #17, #20, #25, #26, #41, #67 | None | None |
| 26 | Short-Term Rental | #41, #69, predict-material-participation | None | #20 REPS (alternative path), #25 long-term rental |
| 27 | Startup Cost Optimization | #12, #18 | None | None |
| 28 | De Minimis Safe Harbor | #12, #13 | None | #93 (SE variant) |
| 29 | Deferred Sales Trust [AGGRESSIVE] | None | Notice 2023-34 listed transaction | #1, #33, #34 (compliant alternatives) |
| 30 | Worthless Stock Ordinary Loss | #15 NOL | None | None |
| 31 | C Corp Dividends | #21, #42, #47 | §531 / §541 penalty taxes | None |
| 32 | Capital Gain Offsets | #46, #51, #54, #69 | §1091 wash sale | None |
| 33 | Installment Sale | #25, #92 | §453(g) related party trap | #1, #34 (alternative deferrals) |
| 34 | QOZ Reinvestment | #43 (potential combo for double exclusion) | Dec 31 2026 mandatory recognition | #1, #33 (alternative deferrals) |
| 35 | C Corp State Tax Savings | #17 PTET equiv, #47 | None | None |
| 36 | EV Credits | #4, #12 | None | None |
| 37 | Late Penalties / Interest | #66 broader penalty abatement | None | None |
| 38 | Misc Tax Credits | #39, #58, #61 | §38(c) tax liability limit | None |
| 39 | R&D Credit | #38, predict-r-and-d-credit | §174 capitalization (TCJA) | None |
| 40 | State Tax Savings | #17 PTET, #67 §121, residency planning | None | None |
| 41 | Cost Segregation | #12, #20, #25, #26 | §1245 recapture at sale (later) | None |
| 42 | C Corp Misc Deductions | #31, #35, #43, #47 | §163(j) limit | None |
| 43 | §1202 QSBS | #47 (C corp formation), #34 | S corp / LLC stock not eligible | None |
| 44 | Corporate-Owned VUL [AGGRESSIVE] | None | §101(j) compliance, §409A, §7702A MEC | #74 (similar individual strategy), #75-#83 (compliant retirement alternatives) |
| 45 | §127 Education Assistance | #71 | None | #61 education credits (different funding source) |
| 46 | Gifting Stock | #51, #54, #56, #57 | §1015 carryover basis (vs. §1014 step-up) | #51 charity-only (different recipient) |
| 47 | Income Shifting to C Corp [Caution] | #43 (QSBS interaction), #47 | §269A PSC, §531/§541, §482 transfer pricing | #19 §199A (forfeit pass-through QBI) |
| 48 | Income Shifting to Family Member | #46, #49, #50, #55, #57 | §1(g) kiddie tax (under 24 dependents) | None |
| 49 | Hiring Kids | #11 (HRA family), #50, #79 Roth IRA | §3121(b)(3) limited to non-corporate | #94 (SE variant) |
| 50 | Wages: Spouse / Non-Dependents / Parents | #11 (HRA spouse), #21, #75-#83 | None | None |
| 51 | Charitable Donation Appreciated | #32, #46, #54 | Short-term property limited to basis | #54 DAF, #78 QCD (alternative paths) |
| 52 | Charitable LLC [AGGRESSIVE] | None | IRS Dirty Dozen / private benefit / §501(c)(3) | #51, #54 (compliant alternatives) |
| 53 | Charitable Planning | All charitable strategies (umbrella) | None | None |
| 54 | Donor Advised Fund | #46, #51, #32 (bunching strategy) | §4966/§4967 distributions | #78 QCD (alternative) |
| 55 | Family Limited Partnership [AGGRESSIVE] | #46, #48, #56 | §2036, §2704, §2503 | None |
| 56 | Unreimbursed Partnership Expenses | #2, #4, #5 (substance-equivalent) | Klaassen if reimbursable | #2 (corporate accountable plan) |
| 57 | 529 Savings Plan | #46, #48, #60, #61, #80 (Roth rollover) | §529 vs. §25A double-dipping | None |
| 58 | Adoption Incentives | #71 §137 | None | None |
| 59 | Amend for Missed Deductions | All missed-item strategies | §6511 statute | Form 3115 (alternative for method changes) |
| 60 | College Student Strategies | #45, #49, #57, #61, #79, #80 | None | None |
| 61 | Education Credits | #57, #60, #80, #45 | §529 double-dipping prohibition | AOTC vs. LLC (per student per year) |
| 62 | Flexible Spending Account | #8 | #63 HSA (HCFSA disqualifies; LPFSA OK) | None |
| 63 | HSA Optimization | #8 HDHP, #62 LPFSA, #71, #79 | #11 traditional HRA, #62 standard HCFSA | None |
| 64 | Individual Planning Ideas | All individual strategies (umbrella) | None | None |
| 65 | Married Filing Separate | #61 disqualification, #79 phase-out, #69 | None | None (filing status decision) |
| 66 | Penalty Abatement | #37, #59 (amend for FTA), predict-reasonable-cause | §6707A limited reasonable cause | None |
| 67 | Primary Home Sale Exclusion | #25, #40 (domicile), #88 (recapture) | Non-qualified use post-2008 | #1 (rental conversion path) |
| 68 | Employee Stock Options | #43, #69, #32, #80 (NQSO income management) | §409A, §1091 wash sale | None |
| 69 | NIIT Minimization | #20, #26, #9, #80, #63, #75-#83, #67 | None | None |
| 70 | Series I Bond | #61 §135 education, #57 (alternative) | None | None |
| 71 | Employer Benefit Package Review | All employer benefits (umbrella) | None | None |
| 72 | Backdoor Roth | #75 (Mega Backdoor via after-tax 401(k)), #79, #80 | Pre-tax IRA balance (pro-rata trap) | #79 (direct Roth — preferred if eligible) |
| 73 | Defined Benefit / Cash Balance | #75, #82, #21 | §415(b) limit | None |
| 74 | LIRP [AGGRESSIVE] | None | §7702A MEC, §409A | #75-#83 (compliant alternatives), #79, #72 |
| 75 | 401(k) Pre-Tax | #72 Mega Backdoor, #79 Roth, #82 Solo | §402(g) cross-plan limit | None |
| 76 | SEP-IRA | #79 if income within | §408(d)(2) pro-rata trap (#72) | #77 (small business alternative), #82 (deferral capacity), #73 |
| 77 | SIMPLE IRA | #79 if income within | 2-year rule §72(t)(6) | #76, #82, #73, #75 (alternative plans) |
| 78 | QCD | #51, #54 (alternatives), #69 AGI minimization, #83 | DAF / private foundation as recipient | None |
| 79 | Roth IRA Contributions | #72, #80, #75 | MAGI phase-out (Backdoor as workaround) | #83 (deductible Traditional) |
| 80 | Roth IRA Conversion | #79, #72, #69 | TCJA recharacterization elimination | None |
| 81 | SEP-IRA Self-Employed | #82 (preferred when desired deferral), #79 | §408(d)(2) pro-rata trap | #82, #73 |
| 82 | Solo 401(k) | #72 Mega Backdoor, #79, #73 | None | #81, #76, #77 (alternative plans) |
| 83 | Traditional IRA Contributions | #72 non-deductible variant, #80 conversion | §219(g) phase-out | #79 (Roth alternative) |
| 84 | Accountable Plan Self-Employed | #84-#94 (all SE strategies) | None | #2 (corporate equivalent) |
| 85 | Business Vehicle SE | #4, #12, #36 | Standard mileage Year-1 lock-in | #4 (corporate equivalent) |
| 86 | Choice of Entity SE Tax | #19, #21, #43, #47, #90 | §269A PSC | None (foundational decision) |
| 87 | Health Insurance SE | #10, #11, #84 | §125 (SE ineligible) | #10 (S corp variant), #8 (group plan if employee) |
| 88 | Home Office Deduction SE | #2 (corp equivalent), #84, #67 (recapture) | Exclusive use violation | #2 (corporate accountable plan) |
| 89 | Bonus / §179 Depreciation SE | #12, #28, #41, #85, #89, #93 | §179 income limit | None |
| 90 | Minimize Self-Employment Tax | #21, #49, #50, #82, #86 | Renkemeyer LP trap | None (umbrella) |
| 91 | Prepayment Expense SE | #18, #13, #84 | None | None |
| 92 | Split Entity Operations vs RE | #1, #9, #16, #17, #19, #25, #41, #69 | Self-rental recharacterization | None |
| 93 | De Minimis Safe Harbor SE | #28, #84, #89 | None | None |
| 94 | Hiring Kids SE | #11, #50, #79, #84 | §3121 limited to sole prop / parent-only partnership | #49 (corporate variant) |

---

## Common strategy combinations (positive)

These combinations represent foundational planning structures where strategies stack effectively:

**Real Estate Professional Power Stack:**
- #20 REPS + #41 cost segregation + #12 §168(k) bonus + #9 grouping aggregation + #19 §199A QBI safe harbor (Notice 2019-07)
- Result: Large first-year depreciation deductions offsetting W-2 income.

**S Corp Owner Standard Package:**
- #86 S corp election + #21 reasonable comp + #10 health insurance + #2 accountable plan + #82 Solo 401(k) + #75 401(k) deferral + #19 §199A QBI
- Result: Optimized SE tax savings with full benefit package.

**Charitable Bunching:**
- #54 DAF (year of bunch) + #51 appreciated stock contribution + #32 capital gain offset + standard deduction (off-years)
- Result: Itemize benefit captured in bunch year; standard deduction in off-years.

**High-Net-Worth Estate Plan:**
- #46 gifting stock (annual + lifetime exclusion) + #55 FLP (with bona fide substance) + #54 DAF charitable component + #57 529 grandparent funding
- Result: Wealth transfer with valuation discounts and charitable / education goals.

**Self-Employed Retirement Maximization:**
- #82 Solo 401(k) (employee deferral $23K + profit sharing 20%) + #72 Mega Backdoor Roth (after-tax) + #79 Roth IRA + #73 Defined Benefit (older owners)
- Result: Maximum tax-advantaged contribution capacity ($69K+ standard; $200K+ with DB).

**Short-Term Rental Strategy:**
- #26 STR + material participation + #41 cost segregation + #69 NIIT exclusion + #19 §199A
- Result: Real estate losses against W-2 income without REPS qualification.

**Family Employment Stack:**
- #94 Hiring kids SE (or #49 corporate) + #79 Roth IRA child + #11 HRA family medical + #50 Spouse employment
- Result: Income shifting + Roth funding + medical reimbursement + retirement contribution capacity.

---

## Red-flag combinations (conflicts)

**Notice 2013-54 violations:**
- #11 standalone HRA + individual health insurance reimbursement (without QSEHRA / ICHRA / EBHRA structure) → §4980D $100/day per employee penalty.

**Wash sale combinations:**
- #32 tax loss harvesting + replacement security purchase within 30 days → §1091 disallowance.
- RSU vesting + same-day employer stock purchase via ESPP → potential §1091.

**Self-rental trap:**
- #16 PIG + property leased to taxpayer's own active business → Reg §1.469-2(f)(6) recharacterizes income as nonpassive, defeating PIG purpose.

**§408(d)(2) pro-rata trap:**
- #72 Backdoor Roth + existing Traditional IRA / SEP / SIMPLE balance → pro-rata taxation of conversion.

**§101(j) failure:**
- #44 Corporate-Owned VUL without notice and consent → Death benefit ordinary income.

**§6707A reportable transaction:**
- #29 Deferred Sales Trust without Form 8886 → $10K-$100K penalty.
- #52 Charitable LLC variants matching reportable transaction → same.

**§469(c)(7)(A) election forgotten:**
- #20 REPS + multiple rentals without aggregation election → each rental tested separately for material participation; typically fails.

**§1244 documentation missed:**
- #30 Worthless stock ordinary loss claim without §1244 designation at issuance → capital loss only.

---

## Mutually exclusive paths to same goal

**Capital gain deferral:**
- #1 §1031 (real estate only)
- #33 §453 installment sale
- #34 §1400Z-2 QOZ
- #29 DST [AGGRESSIVE — avoid]
- Choose ONE per gain transaction.

**Charitable giving:**
- #51 direct appreciated stock
- #54 DAF
- #78 QCD (IRA owners 70½+)
- Various trust structures (#53 umbrella)
- #52 Charitable LLC [AGGRESSIVE — avoid]
- Different vehicles for different gifts; can use multiple but each gift uses one path.

**Retirement plan choice (no employees):**
- #76 SEP-IRA (simple)
- #82 Solo 401(k) (deferral capacity)
- #73 Defined Benefit / Cash Balance (highest contributions for older owners)
- Generally choose ONE primary plan; can layer (e.g., Solo 401(k) + DB).

**Roth contribution paths (high income):**
- #79 direct Roth IRA (if MAGI permits)
- #72 Backdoor Roth (if pro-rata permits)
- #80 Roth conversion
- #75 Roth 401(k) deferral
- Mega Backdoor via #72 / #82
- Multiple paths can be combined; pro-rata rule limits Backdoor.

**Real estate passive loss path:**
- #20 REPS (full nonpassive treatment)
- #3 Active participation $25K offset (under-threshold)
- #26 STR with material participation (alternative to REPS)
- #16 PIG (loss absorption via passive income generation)
- #9 grouping (loss release through aggregated material participation)

**S corp election timing:**
- #86 election by 2 months 15 days into target year (Form 2553)
- Late election under Rev. Proc. 2013-30
- Choose effective year carefully — can affect entire year of operations.

---

## Strategy selection decision support

The Vibe TB platform should expose this matrix programmatically. When a user selects a primary strategy:

1. **Surface "Combines with"** as recommended additions.
2. **Surface "Conflicts with"** as warnings before the user can select the conflicting strategy.
3. **Surface "Mutually exclusive with"** when user attempts to add an alternative path.

The skills directory `references/strategies/` contains all 94 strategy detail files. The `references/strategy-list.md` provides the master index. The `references/strategy-relationships.json` (to be generated from this matrix) provides programmatic access to the relationships.

---

## Final implementation checklist

This addendum (Parts 1-10) provides:

✅ **Master index** — All 94 strategies listed (Part 1).
✅ **Build-plan PART A addendum** — Phase 4 task list, dispatcher routing, shared/strategy-list.md spec, CI workflow patch, revised time-token budget.
✅ **All 94 strategy detail files** — Full template depth across Parts 1-10:
  - YAML frontmatter
  - Overview / Primary IRC authority / Treasury regulations / Key IRS guidance / Key court decisions
  - Eligibility requirements / Mechanics / Documentation requirements
  - Common pitfalls / Recent legislative changes (with OBBBA `[CITATION NEEDED]` flags)
  - State conformity considerations / SSTS Circular 230 considerations
  - Default confidence band rationale / Cross-references / JSON authority sidecar
✅ **Aggressive-strategy banners** on Strategies #29, #44, #52, #55, #74 (with #47 Caution, #21 Caution, #16 Caution, etc.)
✅ **Specific case law citations** including Watson, Renkemeyer, Castigliola, Soroban, Sinopoli, Bongard, Strangi, Powell, Hospital Corp of America, Whiteco, Hassanipour, Frank Aragona Trust, Lucas v. Earl, Helvering v. Horst, Crummey, Eller, Denman, Boyle, Brockamp, Boehm, Cohan, Welch, Tellier, INDOPCO, Wynne, Wayfair, Suder, Geosyntec, Trinity, Union Carbide, Populous Holdings, Speltz, Sutardja, Klaassen, McLaulin, Owen, Krukowski, Beecher, Schwalbach, Albers, Shellito, Soliman, Hamacher, Estate of Givens, Ohio Furnace, Helvering v. Bashford, Stranahan, U.S. Freightways, Encyclopedia Britannica, Holman, Bigelow, Korby, Speltz Tax Court (ISO), Atlas Tool, Bardahl, Menard, Exacto Spring, Spicer, Joseph M. Grey, JD & Associates, Hailstock, Gates, Reesink, Generes, Fairbairn, Smith, Hewitt, Pankratz, Estate of Halby, and others.
✅ **OBBBA verification flags** throughout — `[CITATION NEEDED — search: <query>]` sentinels for unverified provisions.
✅ **Cross-reference matrix** — comprehensive combinations / conflicts / mutual exclusions for all 94 strategies.

The output is ready for ingestion into the Vibe CPA Skills Pack `planning-strategy-library` skill at `references/strategies/<slug>.md` per file. The build-plan addendum (PART A in Part 1) covers integration with BUILD_PLAN.md Phase 4, dispatcher routing, JSON authority sidecar validation against shared/output-schema.json, and revised time / token budget (30-45 hours / 13M-22M tokens).

---

**End of Part 10 of 10. Strategy library addendum complete.** All 94 strategies delivered with full law-library depth, citation discipline, OBBBA verification flags, and cross-reference matrix.
