# Vibe CPA Skills — Strategy Library Addendum (94 Strategies)

**Part 2 of 10** — Strategies #8 through #17.

**Part navigation:**
- Part 1: Exec summary, master index, PART A build-plan addendum, strategies #1–#7
- **Part 2: Strategies #8–#17** ← this file
- Part 3: Strategies #18–#27
- Part 4: Strategies #28–#37
- Part 5: Strategies #38–#47
- Part 6: Strategies #48–#57
- Part 7: Strategies #58–#67
- Part 8: Strategies #68–#77
- Part 9: Strategies #78–#86
- Part 10: Strategies #87–#94 + cross-reference matrix

---

## Strategy #8: Group Health Insurance

**File:** `references/strategies/group-health-insurance.md`

```markdown
---
name: "Group Health Insurance for Employees"
slug: group-health-insurance
type: Business - Other
tax_type: EFR
complexity: Low
irc_sections: ["§106", "§125", "§4980H", "§5000A"]
forms: ["Form 1094-C / 1095-C (ALEs)", "Form 8941 (Small Business Health Care Tax Credit)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Employer-provided group health insurance is excludable from
employees' gross income under §106(a) and is deductible by the
employer under §162. When combined with a §125 cafeteria plan, the
employee's share of premiums can also be paid pre-tax, generating
combined federal income tax and FICA savings on both employer and
employee sides. This is the most foundational employee benefit
planning strategy and the baseline against which alternative
arrangements (HRAs, ICHRAs, QSEHRAs) are evaluated.

For Applicable Large Employers (ALEs — generally employers with 50
or more full-time-equivalent employees), §4980H imposes the
employer shared responsibility provision (the "employer mandate"):
ALEs must offer affordable, minimum-value coverage to substantially
all full-time employees or face penalties. Small employers (under
50 FTE) face no mandate but may qualify for the Small Business
Health Care Tax Credit under §45R if they purchase coverage through
the SHOP marketplace.

For S corporation 2%+ shareholders, the special rule under §1372
applies: premiums paid by the corporation are includible in the
shareholder-employee's W-2 income (Box 1, but not Box 3 or Box 5),
then deducted above-the-line under §162(l) on Form 1040. See
companion strategy `health-insurance-s-corp` (#10) for S-corp-
specific mechanics.

## Primary IRC authority

- **§106(a)** — Employer-provided coverage under accident or health
  plan is excludable from employee gross income.
  https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section106
- **§105(b)** — Reimbursement of employee medical expenses
  excludable.
- **§162(a)** — Employer deduction for compensation including
  health insurance premiums.
- **§125** — Cafeteria plans; permits pre-tax election by employees.
- **§4980H** — Employer shared responsibility (ACA employer
  mandate; ALEs only).
- **§45R** — Small Business Health Care Tax Credit (employers
  under 25 FTE with average wages under threshold; SHOP marketplace
  required).
- **§1372** — Treatment of S corporation 2%+ shareholders for
  fringe benefit purposes.

## Treasury regulations

- **Reg §1.106-1** — Contributions by employer to accident and
  health plans.
- **Reg §1.105-2** — Reimbursement of medical care.
- **Reg §1.125-1 through 1.125-7** — Cafeteria plan rules.
- **Reg §54.4980H-1 through §54.4980H-5** — Employer shared
  responsibility regulations.
- **Reg §1.45R-1 through 1.45R-5** — Small Business Health Care
  Tax Credit.

## Key IRS guidance

- **Notice 2013-54** — Restricted employer payment plans and
  standalone HRAs.
- **Notice 2015-87** — ACA implementation guidance.
- **Notice 2018-88** — ICHRA and QSEHRA guidance.
- **Rev. Rul. 61-146** — Employer reimbursement of individually
  purchased insurance treated as compensation absent §105 plan.
- **IRS Publication 535** — Business Expenses (employer side).
- **IRS Publication 502** — Medical and Dental Expenses (deductible
  medical care definition).

## Key court decisions

- Limited dispute area for traditional group plans; most case law
  focuses on edge cases (executive-only plans, self-employed
  exclusions, S corp shareholder-employees).

## Eligibility requirements

For employer deduction under §162:
1. Coverage is bona fide health insurance (compliant with state
   insurance law, ACA, ERISA where applicable).
2. Plan does not discriminate in favor of highly compensated
   employees in self-insured arrangements (§105(h)).

For employee exclusion under §106:
1. Coverage provided under an "accident or health plan" within
   meaning of Reg §1.106-1.
2. Coverage provided to employee, spouse, dependents, or §152(f)(2)
   children under age 27.

For §125 cafeteria plan:
1. Written plan document.
2. Eligibility limited to employees (not partners or 2%+ S corp
   shareholders).
3. Annual elections made before plan year begins (with limited
   change-in-status exceptions).
4. Nondiscrimination testing (key employee concentration; eligibility;
   contributions/benefits).

## Mechanics — how it works

1. **Plan procurement.** Engage broker or use SHOP marketplace
   (small employer). Compare PPO, HMO, HDHP options.
2. **§125 cafeteria plan adoption.** Written plan document; SPD;
   employee election forms.
3. **Premium structure.** Employer pays full premium (most generous);
   or shared with employee paying the difference; or employee pays
   full premium pre-tax (still saves FICA at minimum).
4. **§4980H compliance for ALEs.** Track FTE counts monthly. Offer
   coverage to ≥95% of full-time employees and dependents.
   "Affordability" = required employee contribution ≤9.5% (indexed)
   of household income; safe harbors based on W-2 box 1, rate of
   pay, or federal poverty line.
5. **§45R credit for small employers.** If <25 FTE, average wages
   below threshold (~$58,000 for 2024), and coverage purchased
   through SHOP, claim credit on Form 8941 for 2 consecutive years.
6. **Reporting (ALEs).** Forms 1094-C and 1095-C filed annually.
   Forms 1095-B for self-insured non-ALEs.

## Documentation requirements

- Insurance policy and plan booklet (SPD).
- §125 plan document.
- Employee election forms.
- Payroll records reflecting pre-tax deductions (§125 reduces W-2
  Box 1, 3, 5 consistently).
- §4980H tracking workpapers (ALEs).
- Form 8941 (small business credit).

## Common pitfalls / audit risks

- **§125 cafeteria plan failure to satisfy nondiscrimination
  testing.** Highly compensated employees lose pre-tax treatment.
- **Standalone employer payment plan / employer reimbursement of
  individual health insurance.** Notice 2013-54 prohibits standalone
  arrangements that pay or reimburse individual premiums (except
  ICHRA/QSEHRA which are specifically permitted post-Notice 2018-88).
  Penalties under §4980D ($100/day per affected employee).
- **§105(h) self-insured discrimination failures** — HCEs lose
  exclusion to extent of discriminatory amount.
- **2% S corp shareholder-employees treated as employees for §125** —
  they cannot, per §1372. Common error.
- **Mid-year election change errors** — §125 elections are
  irrevocable absent change-in-status events listed in Reg §1.125-4.

## Recent legislative changes

- **ACA (2010)** — Created §4980H, §5000A, §45R, §6055-6056
  reporting.
- **TCJA (2017)** — Reduced §5000A individual mandate penalty to $0
  effective 2019 (statute remains but penalty zeroed).
- **CARES Act (2020)** — Expanded §125 mid-year election change
  flexibility temporarily; some made permanent in subsequent
  guidance.
- **Inflation Reduction Act (2022)** — Extended ACA marketplace
  premium tax credit subsidies through 2025.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §125 §4980H
  changes Pub L 119-21 classification table]`. Working assumption:
  no material §125 or §4980H changes; ACA premium tax credit
  treatment may have been adjusted.

## State conformity considerations

State conformity is generally complete for §106 exclusion. State
mandates may layer on top of federal requirements (e.g., California
SB 1255, Massachusetts mandate). Some states (CA, NJ, RI, VT, DC)
have residual individual mandates with state-level penalties.

## AICPA SSTS / Circular 230 considerations

Standard practitioner diligence; group health is not an aggressive
position. Disclosure considerations apply only to highly unusual
discriminatory plans.

## Default confidence band rationale

**HIGH** — bedrock employee benefit treatment with universal
acceptance. Drops to MODERATE only for unusual structures (executive
medical plans, post-Notice 2013-54 standalone arrangements that
attempt to operate outside ICHRA/QSEHRA framework).

## Cross-references

- **`health-insurance-s-corp`** (#10) — S corp 2% shareholder
  variant.
- **`hra-merp`** (#11) — alternative reimbursement structure.
- **`flexible-spending-account`** (#62) — companion §125 component.
- **`employer-benefit-package-review`** (#71) — broader fringe
  optimization.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 106(a)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section106",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 125",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section125",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 4980H",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section4980H",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.106-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2013-54",
      "url": "https://www.irs.gov/irb/2013-40_IRB",
      "weight": "irs_published"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2018-88",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
```

---

## Strategy #9: Grouping of Activities

**File:** `references/strategies/grouping-of-activities.md`

```markdown
---
name: "Grouping of Activities Election (§469 Aggregation)"
slug: grouping-of-activities
type: Business - Other
tax_type: EFR
complexity: High
irc_sections: ["§469"]
forms: ["Disclosure statement attached to Form 1040 / 1120-S / 1065 (per Rev. Proc. 2010-13)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: MODERATE
last_obbba_review: "N/A"
cross_reference_skills: ["predict-material-participation", "predict-real-estate-pro"]
---

## Overview

The §469 grouping election under Reg §1.469-4 allows a taxpayer to
combine two or more separate activities into a single activity for
purposes of the passive activity loss (PAL) rules. The strategic
value is significant in three contexts:

1. **Material participation.** Activities can be aggregated to meet
   the 500-hour material-participation test (Temp. Reg §1.469-5T(a)(1))
   when no single activity by itself crosses 500 hours, but the
   aggregate does.
2. **Real estate professional (REPS) elections.** A real estate
   professional under §469(c)(7) can elect under §469(c)(7)(A) to
   treat all rental real estate interests as a single activity,
   easing the material-participation requirement that otherwise
   applies separately to each property.
3. **Disposition triggering loss release.** When a passive activity
   is disposed of in a fully taxable transaction, suspended losses
   are released under §469(g). Grouping can affect what constitutes
   a "complete disposition" — selling one activity that was grouped
   with others does not release the suspended losses.

The grouping decision is durable: once made, it generally cannot be
regrouped except to correct a clearly inappropriate prior grouping
or upon material change in facts and circumstances. Rev. Proc.
2010-13 imposes annual disclosure requirements; failure to disclose
new groupings, additions, or dispositions may invalidate the
election.

## Primary IRC authority

- **§469** — Passive activity loss limitations.
- **§469(c)(7)** — Real estate professional rules.
- **§469(c)(7)(A)** — Election to treat all interests in rental real
  estate as one activity.
- **§469(g)** — Treatment of dispositions.

## Treasury regulations

- **Reg §1.469-4** — Definition of activity. The cornerstone
  regulation. Establishes the "appropriate economic unit" standard
  for grouping.
- **Reg §1.469-4(c)** — Five-factor test for what constitutes an
  "appropriate economic unit": (1) similarities and differences in
  types of trade or business, (2) extent of common control, (3)
  extent of common ownership, (4) geographic location, (5)
  interdependencies.
- **Reg §1.469-4(d)** — Limitations on grouping (e.g., rental
  activities may not generally be grouped with non-rental activities;
  trading activities have separate rules).
- **Reg §1.469-9** — Specific real estate professional grouping
  rules.

## Key IRS guidance

- **Rev. Proc. 2010-13** — Disclosure requirements for grouping
  determinations. Requires written statement attached to original
  return for the year of grouping, addition, or regrouping.
- **Rev. Proc. 2011-34** — Late grouping election procedure for
  REPS who failed to make timely §469(c)(7)(A) election.

## Key court decisions

- **Gregg v. United States, 186 F. Supp. 2d 1123 (D. Or. 2000)** —
  Two LLCs operating different real estate activities could be
  grouped under "appropriate economic unit" framework.
- **Schumann v. Commissioner, T.C. Memo. 2014-138** — Failure to
  make timely §469(c)(7)(A) election was fatal; taxpayer treated
  each rental as separate, defeating REPS material participation.
- **Trzeciak v. Commissioner, T.C. Memo. 2012-83** — Improperly
  grouped activities; IRS regrouped, defeating loss claim.

## Eligibility requirements

For general grouping under Reg §1.469-4:
1. Activities constitute an "appropriate economic unit" considering
   the five-factor test under Reg §1.469-4(c).
2. Disclosure statement filed per Rev. Proc. 2010-13 with original
   return for year of grouping.
3. Subsequent additions or material changes also disclosed.

For REPS §469(c)(7)(A) election:
1. Taxpayer is a real estate professional under §469(c)(7)(B).
2. Election is made by attaching a statement to the return for the
   year of election.
3. Election is binding for all future years until revoked.

## Mechanics — how it works

1. **Identify activities.** List each rental property, each operating
   business, each S-corp/partnership/LLC interest.
2. **Apply five-factor test.** Determine which activities form an
   "appropriate economic unit."
3. **Determine strategic grouping.** Common patterns:
   - Group multiple commercial properties under common management
     into one activity.
   - Group an operating business with the real estate it occupies
     when commonly owned (subject to self-rental rule, §469
     recharacterization).
   - REPS election: treat all rental real estate as one activity.
4. **File Rev. Proc. 2010-13 disclosure** with original return for
   year of initial grouping.
5. **Track grouping for all subsequent years.** Annual disclosure
   required for additions, dispositions, regroupings.
6. **Material participation analysis** applied at the grouped-
   activity level.

## Documentation requirements

- Grouping rationale memo applying the five-factor test.
- Rev. Proc. 2010-13 disclosure statement filed with return.
- For REPS: §469(c)(7)(A) election statement.
- Hours logs supporting material participation at the grouped-
   activity level.

## Common pitfalls / audit risks

- **Failure to disclose grouping** under Rev. Proc. 2010-13. IRS
  may treat activities as separate, defeating material
  participation. Late disclosure relief may be available.
- **Grouping rentals with non-rental businesses** — generally
  prohibited under Reg §1.469-4(d) unless one activity is
  insubstantial relative to the other.
- **Self-rental rule** under Reg §1.469-2(f)(6). Net rental income
  from property leased to a business in which the taxpayer
  materially participates is recharacterized as nonpassive (preventing
  use of rental losses against the income, but the income itself
  is nonpassive). Grouping does not defeat this.
- **Regrouping without facts-and-circumstances change.** Once made,
  grouping is durable. IRS may challenge unsupported regroupings.
- **Failure to make §469(c)(7)(A) election** — leading to defeat of
  REPS treatment because each rental is tested separately for
  material participation.

## Recent legislative changes

- **TCJA (2017)** — No direct §469 changes affecting grouping.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §469
  changes Pub L 119-21]`. Working assumption: no material §469
  changes.

## State conformity considerations

State conformity to §469 is generally complete; grouping elections
flow through. **California** has unique passive activity rules
(R&TC §17561 and following) — verify CA stub.

## AICPA SSTS / Circular 230 considerations

Grouping is a documented election; failure to file the Rev. Proc.
2010-13 disclosure is a recurring compliance issue. Practitioner
should explicitly memorialize the grouping rationale and disclosure
filing.

## Default confidence band rationale

**MODERATE** — fact-intensive determination; the "appropriate
economic unit" standard is inherently flexible. Drops to LOW for
aggressive groupings (rentals with non-rentals, geographically
dispersed properties with no common management). Rises to HIGH for
straightforward groupings of commonly-controlled, commonly-managed
properties in similar locations.

## Cross-references

- **`real-estate-professional`** (#20) — REPS election companion.
- **`active-participation-real-estate`** (#3) — alternative for
  non-REPS taxpayers.
- **`predict-material-participation`** (predict skill).
- **`predict-real-estate-pro`** (predict skill).
- **`passive-income-pigs`** (#16) — alternative to grouping for
  releasing passive losses.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 469",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 469(c)(7)(A)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.469-4",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.469-9",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2010-13",
      "url": "https://www.irs.gov/irb/2010-04_IRB",
      "weight": "irs_published"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2011-34",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
```

---

## Strategy #10: Health Insurance - S Corporation

**File:** `references/strategies/health-insurance-s-corp.md`

```markdown
---
name: "Health Insurance for S Corporation 2%+ Shareholders"
slug: health-insurance-s-corp
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§162(l)", "§1372", "§3121(a)(2)(B)"]
forms: ["Form W-2 (Box 1 inclusion)", "Form 1040 above-the-line §162(l) deduction"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

The S corporation 2%+ shareholder health insurance treatment is one
of the most frequently mishandled compliance items in small-business
tax preparation. The rules are statutory and the IRS guidance is
clear, but the treatment differs from W-2 employee health insurance
in counterintuitive ways:

1. The S corporation pays the premium (or reimburses the
   shareholder under Notice 2008-1 procedures).
2. The premium is included in the 2%+ shareholder-employee's W-2
   Box 1 (federal wages) but **excluded** from Box 3 (Social
   Security wages) and Box 5 (Medicare wages).
3. The shareholder-employee then deducts the premium above-the-line
   on Form 1040 under §162(l), eliminating the federal income tax
   impact.
4. The S corporation deducts the premium as compensation under §162.

Net result: federal income tax is zero (W-2 inclusion offset by
§162(l) deduction); FICA is saved on both employer and employee
sides because the premium is excluded from Box 3 and Box 5; state
income tax treatment varies by state.

The strategy works because §1372 treats 2%+ S corporation
shareholder-employees as partners for fringe benefit purposes,
denying them §106 exclusion. But §162(l) gives self-employed
individuals (including 2%+ S corp shareholders per §1372) an
above-the-line deduction for health insurance.

## Primary IRC authority

- **§1372** — 2%+ S corp shareholders treated as partners for fringe
  benefit purposes.
  https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1372
- **§162(l)** — Self-employed health insurance deduction
  (above-the-line on Schedule 1 of Form 1040).
- **§3121(a)(2)(B)** — Exclusion of payments under §106 from
  Social Security wages (and corresponding exclusion under
  §3306(b)(2) for FUTA and §3401(a) for income tax withholding —
  but income tax inclusion under §162 compensation treatment for
  shareholder-employees).
- **§106** — Employer-provided health coverage exclusion (does NOT
  apply to 2%+ S corp shareholders due to §1372).

## Treasury regulations

- **Reg §1.162(l)-1** — Self-employed health insurance deduction
  rules.
- **Reg §31.3121(a)(2)-1** — Social Security wage exclusion for
  payments under §106.

## Key IRS guidance

- **Notice 2008-1** — Specific S corporation health insurance
  rules. Provides the procedural framework and confirms the W-2
  inclusion / §162(l) deduction structure.
  https://www.irs.gov/irb/2008-02_IRB
- **Rev. Rul. 91-26** — Treatment of S corporation shareholder
  health insurance as compensation.
- **Announcement 92-16** — Additional S corp shareholder health
  insurance guidance.
- **Chief Counsel Advice 200912059** — Detailed application of
  Notice 2008-1.

## Key court decisions

- **Swope v. Commissioner, T.C. Memo. 1985-516** — S corp
  shareholder denied §106 exclusion.
- **Gulley v. Commissioner, T.C. Memo. 1995-122** — Failure to
  include premium in W-2 defeated §162(l) deduction (statutory
  conditioning).

## Eligibility requirements

1. **Shareholder owns more than 2% of S corporation stock** at any
   time during the taxable year. §1372(b).
2. **Premium paid by S corporation** OR **paid by shareholder and
   reimbursed by S corporation** under a plan established by the
   corporation. Notice 2008-1.
3. **Premium included in W-2 Box 1** of the shareholder-employee
   for the year. Without W-2 inclusion, no §162(l) deduction is
   available. Notice 2008-1.
4. **Plan established by the S corporation.** Notice 2008-1
   originally required premiums paid in name of corporation;
   subsequent guidance allows premiums in name of shareholder if
   corporation reimburses.
5. **§162(l) limits.** Deduction limited to earned income from the
   S corporation (the shareholder's W-2 compensation from that
   corporation). Cannot exceed corporation-derived earned income.

## Mechanics — how it works

1. **Adopt the plan.** Corporate resolution confirming health
   insurance plan covering 2%+ shareholders.
2. **Pay or reimburse premiums during the year.** Either
   corporation pays carrier directly or shareholder pays and
   submits for reimbursement.
3. **Year-end W-2 preparation.** Add total annual premium to Box 1.
   Do NOT add to Box 3 (Social Security wages) or Box 5 (Medicare
   wages). Box 14 commonly used to disclose the amount.
4. **Form 1040 preparation.** Shareholder claims §162(l) deduction
   on Schedule 1 line 17 (above-the-line). Deduction limited to
   earned income from corporation.
5. **State considerations.** Most states follow federal treatment;
   some (Pennsylvania historically) had unique rules.

## Documentation requirements

- Corporate resolution adopting plan.
- Insurance policy or carrier statements.
- If reimbursement structure: receipts and reimbursement records.
- W-2 prepared with proper Box 1 inclusion and Box 3/5 exclusion.
- Schedule 1 supporting §162(l) calculation.

## Common pitfalls / audit risks

- **Failure to include premium in W-2 Box 1.** Without inclusion,
  §162(l) deduction is denied per Notice 2008-1. Common error.
- **Inclusion in Box 3 and Box 5.** Costs FICA unnecessarily.
- **Coverage for shareholder-employee less than 2%.** Such
  shareholders are W-2 employees and §106 exclusion applies; do
  NOT include in Box 1.
- **Ineligibility for spouse coverage.** §162(l) covers the
  shareholder, spouse, and dependents.
- **Family attribution.** §1372 attributes ownership: a 2%+
  shareholder's spouse, children, parents, and grandparents are
  also treated as 2%+ shareholders if any family member is.
- **§162(l) earned income limit.** Deduction cannot exceed earned
  income from the corporation. Insufficient W-2 wages means
  some premium is non-deductible.
- **Coordination with §125 cafeteria plan.** 2%+ shareholders are
  ineligible for §125 plans (statutory). Common error to allow
  pre-tax election.

## Recent legislative changes

- No material recent changes; the framework has been stable since
  Notice 2008-1.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1372 §162(l)
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §162(l) is generally complete. **California**
has historically followed §162(l). **Pennsylvania** has unique S
corporation income treatment but generally conforms to §162(l).
Verify state stub for SALT details.

## AICPA SSTS / Circular 230 considerations

Standard practitioner diligence. The most common error — omitting
W-2 inclusion — creates a real compliance exposure. Practitioner
should review every 2%+ S corp shareholder's W-2 for proper
inclusion at year-end.

## Default confidence band rationale

**HIGH** — explicit statutory framework (§1372, §162(l)) and clear
IRS guidance (Notice 2008-1). Drops to MODERATE only when
shareholder ownership is borderline 2% (family attribution issues)
or earned income limitation creates partial deduction situations.

## Cross-references

- **`group-health-insurance`** (#8) — non-2%+-shareholder
  treatment.
- **`hra-merp`** (#11) — alternative reimbursement structure.
- **`health-insurance-self-employed`** (#87) — sole proprietor /
  partner variant.
- **`reasonable-comp-corp-owners`** (#21) — interaction with
  reasonable compensation analysis.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1372",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1372",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 162(l)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162",
      "weight": "primary_statute"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2008-1",
      "url": "https://www.irs.gov/irb/2008-02_IRB",
      "weight": "irs_published"
    },
    {
      "authority_type": "RevRul",
      "citation": "Rev. Rul. 91-26",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
```

---

## Strategy #11: HRA / MERP

**File:** `references/strategies/hra-merp.md`

```markdown
---
name: "Health Reimbursement Arrangement (HRA) and Medical Expense Reimbursement Plan (MERP)"
slug: hra-merp
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§105(b)", "§105(h)", "§106"]
forms: ["Plan document (no IRS form filing for §105 plan adoption)"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

A Health Reimbursement Arrangement (HRA) — also called a Medical
Expense Reimbursement Plan (MERP) when self-insured by a small
employer — is an employer-funded plan that reimburses employees for
qualified medical expenses on a tax-free basis under §105(b). Unlike
a §125 FSA, HRAs are funded solely by the employer (no employee
salary reduction). Unused balances may roll over year to year (per
plan design). HRAs predate the ACA but were significantly restricted
by Notice 2013-54 (effectively prohibiting standalone HRAs that pay
for individual health insurance premiums) and then partially
restored through specific permitted arrangements:

1. **Qualified Small Employer HRA (QSEHRA)** — created by the 21st
   Century Cures Act of 2016. Available to employers under 50 FTE
   that do not offer group health coverage. Employees use the HRA
   to pay individual market premiums and out-of-pocket medical
   costs. Annual limits indexed.
2. **Individual Coverage HRA (ICHRA)** — created by 2019 Treasury
   regulations. Available to employers of any size; employees use
   the ICHRA to purchase individual market or Medicare coverage.
   Must be offered uniformly to defined classes of employees.
3. **Excepted Benefit HRA (EBHRA)** — limited use HRA for excepted
   benefits like dental and vision; employees must also be eligible
   for group health coverage offered by employer.
4. **Group Coverage HRA** — traditional HRA paired with group
   health insurance. Most common structure pre-Notice 2013-54 and
   still permitted.

For closely-held businesses where the owner is a W-2 employee (C
corp; W-2 employee of S corp other than 2%+ shareholder), an HRA
can be powerful: employer reimburses the family's full out-of-
pocket medical costs (deductibles, copays, dental, vision, etc.) on
a deductible/excludable basis. The §105(h) nondiscrimination test
limits this in practice — for a self-insured plan, the plan cannot
discriminate in favor of highly compensated employees as to
eligibility or benefits, or HCEs lose exclusion to extent of
discriminatory excess.

The classic "spouse-employed-by-business" structure paired with a
§105 HRA: a sole proprietor employs his/her spouse, the business
adopts a §105 HRA covering all employees (including the spouse and
the spouse's family — the proprietor and children), and the
business reimburses the family's full medical costs. This is the
"Section 105 HRA" structure popularized in the 1990s and validated
by case law.

## Primary IRC authority

- **§105(b)** — Amounts received under an accident or health plan
  for personal injuries or sickness; excludable from gross income.
- **§105(h)** — Self-insured medical reimbursement plans
  nondiscrimination requirements.
- **§106** — Contributions by employer to accident or health plans;
  excludable from gross income.

## Treasury regulations

- **Reg §1.105-2** — Reimbursements for medical care.
- **Reg §1.105-11** — Self-insured medical reimbursement plans;
  nondiscrimination rules under §105(h).
- **Reg §1.106-1** — Contributions by employer to accident or
  health plans.
- **Reg §54.9802-1** — HIPAA nondiscrimination (group health).
- **Reg §54.9831-1(c)(3)** — Excepted benefits.
- **Reg §54.9802-4** (2019) — ICHRA regulations.

## Key IRS guidance

- **Rev. Rul. 71-588** — Spouse-employed-by-sole-proprietor §105
  HRA structure validated.
- **Notice 2002-45** — HRA general guidance.
- **Notice 2013-54** — Restricted standalone HRAs and employer
  payment plans.
- **Notice 2017-67** — QSEHRA detailed guidance.
- **Notice 2018-88** — ICHRA / QSEHRA combined guidance.

## Key court decisions

- **Speltz v. Commissioner, T.C. Memo. 2006-25** — §105 HRA with
  spouse employee upheld; documentation crucial.
- **Shellito v. Commissioner, 437 F.3d 1255 (10th Cir. 2006)** —
  §105 HRA with spouse employee disallowed where the spouse was not
  a bona fide employee (no real services, no independent role).
- **Albers v. Commissioner, T.C. Memo. 2007-144** — Bona fide
  employment of spouse upheld; deductions allowed.

## Eligibility requirements

For traditional HRA paired with group health:
1. Plan funded only by employer (no salary reduction).
2. Reimbursements limited to qualified medical expenses under §213(d).
3. §105(h) nondiscrimination if self-insured.
4. Coordinated with group health coverage (per Notice 2013-54).

For QSEHRA:
1. Employer has fewer than 50 FTE.
2. Employer does NOT offer group health coverage.
3. Available to all eligible employees on uniform basis (with
   limited permitted distinctions).
4. Annual contribution limits (e.g., 2024: $6,150 self-only /
   $12,450 family — verify current).
5. Employee must have minimum essential coverage to receive tax-
   free reimbursement.
6. Employer notice required 90 days before plan year.

For ICHRA:
1. Employer (any size) offers ICHRA in lieu of (or alongside, with
   class restrictions) traditional group health.
2. Employees must enroll in individual market coverage or Medicare.
3. Class-based design with permitted classes (full-time vs. part-
   time, salaried vs. hourly, geographic, etc.) under Reg
   §54.9802-4.
4. Annual notice to participants.

For "spouse-employed-by-sole-prop" §105 HRA:
1. Spouse is bona fide employee (real services, paid wages,
   reasonable compensation, employment records).
2. Plan adopted by the business covering all employees.
3. Plan reimburses spouse for family medical costs (the
   proprietor benefits as the spouse's family member).
4. §105(h) nondiscrimination if self-insured (typically a
   non-issue if all employees are covered).

## Mechanics — how it works

1. **Adopt written plan document.** §105 self-insured plan; or
   QSEHRA / ICHRA plan document.
2. **Establish reimbursement procedures.** Employee submits medical
   expense receipts; employer reimburses tax-free.
3. **Annual administration.** Track reimbursements; comply with
   plan limits.
4. **§105(h) nondiscrimination testing** for self-insured plans
   (annual).
5. **For QSEHRA / ICHRA:** Annual employee notice (Notice 2017-67
   for QSEHRA).

For the spouse-employee variant:
1. Hire spouse as W-2 employee with documented job duties.
2. Pay reasonable wages.
3. Adopt §105 HRA covering all employees.
4. Reimburse spouse for family's medical expenses.
5. Sole proprietor benefits as spouse's family member; cost is
   §162 ordinary business expense.

## Documentation requirements

- Written §105 plan document.
- §105(h) nondiscrimination test annual workpapers.
- Reimbursement records and receipts (§213(d) qualified medical
  expenses).
- For spouse-employee structure: employment agreement, time
  records, payroll records.
- For QSEHRA: annual notice to employees; minimum essential
  coverage attestation.
- For ICHRA: annual notice; class-based design documentation;
  affordability testing.

## Common pitfalls / audit risks

- **Notice 2013-54 violations.** Standalone HRAs that pay individual
  market premiums (other than QSEHRA / ICHRA / EBHRA) trigger
  §4980D penalty ($100/day per affected employee).
- **§105(h) discrimination failures.** Self-insured plans favoring
  HCEs cause loss of exclusion to extent of discriminatory excess.
- **Spouse-employee not bona fide.** Shellito-style failure.
  Without real services, real wages, real records, IRS will
  recharacterize the entire arrangement.
- **QSEHRA without minimum essential coverage** by employee — tax-
  free reimbursement denied.
- **ICHRA class design issues.** Improperly drawn classes risk
  recharacterization.
- **Coverage of non-§213(d) expenses.** Reimbursements for non-
  qualified expenses are taxable wages.

## Recent legislative changes

- **Affordable Care Act (2010)** — Created the post-Notice 2013-54
  restrictions.
- **21st Century Cures Act (2016)** — Created QSEHRA effective
  2017.
- **2019 Treasury Regulations** — Created ICHRA, EBHRA effective
  2020.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA HRA QSEHRA
  ICHRA Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §105 / §106 is generally complete. State-
mandated insurance benefits may layer additional requirements.

## AICPA SSTS / Circular 230 considerations

The spouse-employee HRA structure is well-supported by case law
(Speltz, Albers) but requires bona fide employment. Practitioner
should document substance carefully. No Form 8275 disclosure
required for properly-implemented HRAs.

## Default confidence band rationale

**HIGH** — clear statutory and regulatory framework; long-standing
IRS guidance. Drops to MODERATE for spouse-employee structures with
weak documentation, or for ICHRA class designs near edges of Reg
§54.9802-4.

## Cross-references

- **`group-health-insurance`** (#8) — companion strategy.
- **`flexible-spending-account`** (#62) — alternative §125 path.
- **`employer-benefit-package-review`** (#71) — broader optimization.
- **`hiring-kids`** (#49) — child-employee structures (not HRA-
  qualified for own family because §3121(b)(3) family exemption
  conflicts).
- **`wages-spouse-parents`** (#50) — companion family-employment
  strategy.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 105(b)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section105",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 105(h)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section105",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.105-11",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "RevRul",
      "citation": "Rev. Rul. 71-588",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2013-54",
      "url": "https://www.irs.gov/irb/2013-40_IRB",
      "weight": "irs_published"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2017-67",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    },
    {
      "authority_type": "CtAppeals",
      "citation": "Shellito v. Commissioner, 437 F.3d 1255 (10th Cir. 2006)",
      "url": "https://www.courtlistener.com",
      "weight": "binding_circuit"
    }
  ]
}
```
```

---

## Strategy #12: Bonus & §179 Depreciation

**File:** `references/strategies/bonus-and-section-179-depreciation.md`

```markdown
---
name: "Maximize Bonus Depreciation (§168(k)) and §179 Expensing"
slug: bonus-and-section-179-depreciation
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§168", "§168(k)", "§179", "§280F"]
forms: ["Form 4562"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§168(k) bonus depreciation and §179 expensing are the two primary
mechanisms for accelerating depreciation deductions. They are
distinct but complementary:

**§179 expensing** allows a taxpayer to elect to expense up to
$1,160,000 (2024) of qualified property in the year placed in
service, with a $2,890,000 (2024) phase-out threshold (above which
§179 dollar-for-dollar phases out). §179 is limited by taxable
income — cannot create or increase a loss. Available for new and
used property. Election made on Form 4562.

**§168(k) bonus depreciation** allows additional first-year
depreciation. Pre-OBBBA scheduled phase-down: 80% (2023), 60%
(2024), 40% (2025), 20% (2026), 0% (2027). Available for new and
used property (post-TCJA expansion). No taxable-income limitation
— can create or increase a loss (and thus an NOL or §461(l) excess
business loss).

**OBBBA restoration of 100% bonus depreciation:** The One Big
Beautiful Bill Act of 2025 reportedly restored 100% bonus
depreciation effective for property placed in service after a
specified date. Verify exact provision via Classification Tables.
This is one of the most consequential OBBBA changes for capital-
intensive businesses.

The strategic combination most often deployed:
1. Apply §179 first to short-lived assets up to taxable income
   limit.
2. Apply §168(k) bonus to remaining property and to property that
   would create a loss (allowed under §168(k) but not §179).
3. Evaluate §263A UNICAP capitalization rules for inventory-related
   property.

## Primary IRC authority

- **§168(k)** — Special allowance for certain property (bonus
  depreciation).
- **§179** — Election to expense certain depreciable assets.
- **§280F** — Luxury auto and listed property limitations.
- **§263(a)** — General capitalization requirement.
- **§263A** — Uniform capitalization (UNICAP); interplay with
  inventory production.
- **§461(l)** — Excess business losses (limits net business losses
  to thresholds; created TCJA, extended OBBBA).

## Treasury regulations

- **Reg §1.168(k)-2** — Bonus depreciation post-TCJA.
- **Reg §1.179-1 through §1.179-6** — §179 expensing rules.
- **Reg §1.263(a)-1, -2, -3** — Tangible property regulations
  ("repair regs").
- **Reg §1.263(a)-1(f)** — De minimis safe harbor (companion
  strategy #28).

## Key IRS guidance

- **Rev. Proc. 2019-08** — §179 election procedures.
- **Rev. Proc. 2019-13** — §168(k) safe harbor for passenger
  automobiles.
- **Rev. Proc. 2020-25** — §168(k) procedural guidance for
  qualified improvement property (QIP) — the TCJA "drafting error"
  fix from CARES Act.
- **IRS Tangible Property Audit Technique Guide** — Detailed audit
  approach to §263A and §168.

## Key court decisions

Most disputes are factual (whether property qualifies; whether
placed in service). No major recent SCOTUS or circuit-level
decisions on bonus / §179 mechanics.

## Eligibility requirements

For §168(k) bonus depreciation:
1. Tangible property with class life of 20 years or less under
   MACRS.
2. Computer software, water utility property, qualified
   improvement property (QIP).
3. Used property eligible (post-TCJA), with restrictions on related-
   party acquisition.
4. Acquired and placed in service after applicable date.
5. NOT acquired from a related party (§267 or §707(b)) or in a
   §351, §721, §731 transaction (with some exceptions).

For §179:
1. Tangible §1245 property (including off-the-shelf software).
2. Limited categories of §1250 (real property): roofs, HVAC, fire
   protection, alarm systems, security systems on nonresidential
   real property (post-TCJA).
3. Acquired by purchase from unrelated party for use in active
   trade or business.
4. Election made on Form 4562 in year placed in service.
5. Subject to §179(b)(3) taxable income limitation — cannot create
   or increase a loss; carryover available.
6. SUV >6,000 lbs GVWR: separate $30,500 (2024) limit.

## Mechanics — how it works

1. **Identify capital expenditures for the year.** Group by class
   life, type, and §179 eligibility.
2. **Apply §263A UNICAP** if property is for production.
3. **Apply tangible property regulations** — capitalize vs. expense
   determination; de minimis safe harbor election.
4. **Optimize §179 election.** Use §179 first for property closest
   to taxable income limit.
5. **Apply §168(k) bonus to remainder.** Special election available
   to elect out of §168(k) on a class-by-class basis if disadvantageous.
6. **Coordinate with state add-backs.** Many states (CA, NY, NJ,
   MD, MA, PA, MN) decouple from §168(k) bonus, requiring add-back
   and separate state depreciation tracking.
7. **Form 4562** — primary depreciation reporting.
8. **§280F luxury auto cap** applied to vehicles ≤6,000 lbs GVWR.
9. **§461(l) excess business loss** — net business loss limited to
   threshold ($305,000 single / $610,000 MFJ for 2024); excess
   becomes NOL carryforward.

## Documentation requirements

- Asset acquisition records (invoices, contracts).
- Placed-in-service dates with supporting evidence.
- Form 4562 with §179 election and bonus calculations.
- §168(k) election out (if made).
- For QIP: documentation of qualifying improvements.
- For SUVs: GVWR documentation.

## Common pitfalls / audit risks

- **§179 taxable income limitation.** Election in excess of
  taxable income carries forward but is not deductible currently.
  Must coordinate with §168(k) (no income limit).
- **State decoupling errors.** Many states require add-back of bonus.
  Failure to track creates state audit risk.
- **§280F coordination on vehicles.** Heavy SUV vs. light vehicle
  distinction is technical.
- **Related-party acquisition fail.** §168(k)(2)(E) requires used
  property acquired from unrelated party.
- **Placed in service before year end.** Property must be ready and
  available for use, not merely acquired.
- **§461(l) trap.** Even when §179 / §168(k) generate a loss, the
  loss may be deferred under §461(l).

## Recent legislative changes

- **TCJA (2017)** — Increased §179 limit; allowed used property for
  bonus; expanded §179 to include certain real property
  improvements.
- **CARES Act (2020)** — Fixed QIP "drafting error" by making QIP
  15-year property and bonus-eligible retroactively.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §168(k) 100%
  bonus depreciation Pub L 119-21 classification table]`. Reports
  indicate restoration of 100% bonus effective for property placed
  in service after a specified 2025 date. Verify via Classification
  Tables. This is a major planning shift.

## State conformity considerations

**Major decoupling states (require add-back):** California, New
York, New Jersey, Maryland, Massachusetts, Pennsylvania, Minnesota,
Wisconsin, North Carolina (partial). State-specific schedules
(e.g., CA Form 3885A) recapture the deferred federal acceleration.
**Conforming states:** most others, with variation on §179 limits.

## AICPA SSTS / Circular 230 considerations

Standard diligence; depreciation elections are well-established. For
aggressive component-segregation (cost-segregation interactions)
practitioner should document the engineering study supporting
component lives.

## Default confidence band rationale

**HIGH** — clear statutory and regulatory framework. Drops to
MODERATE for QIP characterization issues, related-party acquisition
edge cases, or aggressive bonus on used property where business
purpose may be questioned.

## Cross-references

- **`cost-segregation`** (#41) — engineering study to maximize
  bonus / §179 on real property components.
- **`de-minimis-safe-harbor`** (#28) — alternative for small assets.
- **`business-vehicle-usage`** (#4) — vehicle-specific application.
- **`startup-cost-optimization`** (#27) — §195 vs. depreciation.
- **`bonus-179-depreciation-self-employed`** (#89) — Schedule C
  variant.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 168(k)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section168",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 179",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section179",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.168(k)-2",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.179-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2020-25",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
```

---

## Strategy #13: Maximize Business Deductions

**File:** `references/strategies/maximize-business-deductions.md`

```markdown
---
name: "Maximize Business Deductions (§162 Ordinary and Necessary)"
slug: maximize-business-deductions
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§162", "§263", "§263A", "§274"]
forms: ["Schedule C / Form 1120-S / Form 1120 / Form 1065"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

This strategy is the umbrella concept covering the systematic
identification and substantiation of all available §162 business
deductions. Rather than a single technique, it represents the
practitioner discipline of running a business expense audit
periodically to identify deductions the client has not been claiming
or has been miscategorizing.

The §162 standard is "ordinary and necessary" — well-developed
through decades of judicial interpretation. "Ordinary" means the
expense is normal, customary, or usual in the type of business at
issue (Welch v. Helvering, 290 U.S. 111 (1933)). "Necessary" means
appropriate and helpful for development of the taxpayer's business
(Commissioner v. Tellier, 383 U.S. 687 (1966)). These standards are
broad and forgiving; the practical limit is usually substantiation
under §6001 and, for certain categories, the strict §274(d)
substantiation rules.

Common deduction categories that taxpayers under-claim:
- Subscriptions, periodicals, professional dues
- Continuing education and conference attendance (with strict
  §162(a)(2) travel rules)
- Professional library and reference materials
- Software subscriptions and SaaS tools
- Industry-specific supplies and equipment
- Bank and merchant account fees
- Marketing, advertising, and sponsorship
- Networking events (with §274 50% disallowance for entertainment-
  characterized activities post-TCJA)
- Postage, shipping, and freight
- Office supplies and small equipment
- Repair and maintenance (vs. capitalizable improvement)

## Primary IRC authority

- **§162(a)** — Ordinary and necessary trade or business expenses.
- **§162(a)(1)** — Reasonable allowance for salaries.
- **§162(a)(2)** — Travel expenses while away from home.
- **§162(a)(3)** — Rentals or other payments required to be made.
- **§162(c)** — Illegal payments not deductible.
- **§162(e)** — Lobbying and political expenses not deductible.
- **§162(f)** — Fines and penalties paid to government generally
  not deductible.
- **§162(g)** — Treble damages under antitrust laws.
- **§162(m)** — Limitation on excessive employee remuneration ($1M
  cap for public companies).
- **§263** — Capital expenditures.
- **§263A** — UNICAP.
- **§274** — Disallowance of certain entertainment expenses;
  substantiation requirements.

## Treasury regulations

- **Reg §1.162-1 through 1.162-29** — §162 implementing regulations.
- **Reg §1.263(a)-1, -2, -3** — Tangible property regulations.
- **Reg §1.274-1 through §1.274-12** — §274 limitations and
  substantiation.

## Key IRS guidance

- **IRS Publication 535** — Business Expenses.
- **IRS Publication 463** — Travel, Gift, and Car Expenses.
- **IRS Audit Technique Guides** — Industry-specific (real estate,
  cash-intensive businesses, professional services, attorneys, etc.).

## Key court decisions

- **Welch v. Helvering, 290 U.S. 111 (1933)** — Foundational
  "ordinary and necessary" interpretation.
- **Commissioner v. Tellier, 383 U.S. 687 (1966)** — "Necessary"
  defined as appropriate and helpful.
- **Cohan v. Commissioner, 39 F.2d 540 (2d Cir. 1930)** —
  Approximation rule for inadequate substantiation (now limited by
  §274(d) for specific categories).
- **INDOPCO, Inc. v. Commissioner, 503 U.S. 79 (1992)** —
  Capitalization framework for expenses producing future benefits
  (later codified in §263 regulations).

## Eligibility requirements

1. Expense paid or incurred during the taxable year.
2. Expense paid or incurred in carrying on a trade or business
   (§162) or for production of income (§212; not deductible by
   individuals through 2025 under TCJA suspension).
3. Expense is "ordinary and necessary" — fact-specific.
4. Substantiation under §6001 records requirement; §274(d) strict
   substantiation for specific categories (vehicle, travel, M&E,
   listed property).
5. Not a capital expenditure (§263) — i.e., does not produce a
   significant future benefit beyond the current year.

## Mechanics — how it works

1. **Conduct annual business expense audit.** Review:
   - Bank and credit card statements
   - QuickBooks / accounting software categorizations
   - Personal expenses that may have business character (dual-use
     items, mixed-personal use)
2. **Identify miscategorized expenses.** Personal items charged to
   business (problematic — recategorize); business items charged
   personally (deductible if substantiated; reimburse via
   accountable plan if entity-structured).
3. **Map to deduction categories.** Schedule C lines / corporate
   chart of accounts.
4. **Apply category-specific rules.**
   - Meals & Entertainment: 50% (or 100% certain categories).
   - Travel: §162(a)(2) "away from home" requirement.
   - Vehicle: §274(d) substantiation; standard mileage vs. actual.
   - Education: §162 if maintains/improves skills required in
     current job; not §162 if qualifies for new trade.
5. **Capitalization vs. expense determination** under tangible
   property regulations.
6. **Documentation.** Receipts, business purpose, contemporaneous
   records.

## Documentation requirements

- Receipts and invoices.
- Business purpose notation (especially for ambiguous categories).
- §274(d) substantiation for specific categories.
- Capital vs. expense memo for borderline items.

## Common pitfalls / audit risks

- **Personal-use creep.** Personal expenses in business categories
  draw scrutiny.
- **Inadequate substantiation.** §274(d) categories are unforgiving.
- **Capitalizable items expensed.** Tangible property regulations
  draw lines that are often missed.
- **§274 50% meals limitation** — many practitioners forget post-
  TCJA disallowance of entertainment.
- **§162(a)(2) travel "away from home" definition** — if the
  taxpayer has no fixed work location, may not have a "tax home."
- **§162 vs. §263 capitalization** — major audit area.

## Recent legislative changes

- **TCJA (2017)** — Eliminated §274 entertainment deduction;
  reduced meals to 50% (with limited 100% exceptions); suspended
  §67(g) miscellaneous itemized deductions.
- **CAA 2021** — Temporarily restored 100% meals (2021-2022) for
  restaurant meals.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §162 §274
  Pub L 119-21]`. Working assumption: no material §162 changes.

## State conformity considerations

State conformity to §162 is essentially universal. State decoupling
on specific items (§168(k), §163(j), §174 amortization) flow through
this strategy area.

## AICPA SSTS / Circular 230 considerations

Standard diligence; SSTS §1.4 reasonable inquiry into client
representations regarding business character of expenses.

## Default confidence band rationale

**HIGH** for ordinary expenses with proper documentation. Drops to
MODERATE for unusual items (e.g., heavy travel, large education,
high entertainment characterization), and LOW for personal-use
items recharacterized as business.

## Cross-references

- **`accountable-plan-home-office`** (#2)
- **`meals-and-entertainment`** (#14)
- **`business-vehicle-usage`** (#4)
- **`bonus-and-section-179-depreciation`** (#12)
- **`de-minimis-safe-harbor`** (#28)
- **`startup-cost-optimization`** (#27)

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 162(a)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162",
      "weight": "primary_statute"
    },
    {
      "authority_type": "SCOTUS",
      "citation": "Welch v. Helvering, 290 U.S. 111 (1933)",
      "url": "https://www.supremecourt.gov",
      "weight": "binding_judicial"
    },
    {
      "authority_type": "SCOTUS",
      "citation": "Commissioner v. Tellier, 383 U.S. 687 (1966)",
      "url": "https://www.supremecourt.gov",
      "weight": "binding_judicial"
    },
    {
      "authority_type": "SCOTUS",
      "citation": "INDOPCO, Inc. v. Commissioner, 503 U.S. 79 (1992)",
      "url": "https://www.supremecourt.gov",
      "weight": "binding_judicial"
    }
  ]
}
```
```

---

## Strategy #14: Meals & Entertainment Deduction

**File:** `references/strategies/meals-and-entertainment.md`

```markdown
---
name: "Meals & Entertainment Deduction (§274)"
slug: meals-and-entertainment
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§162", "§274"]
forms: ["Schedule C / Form 1120-S / Form 1120 / Form 1065 (deduction lines)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

§274 imposes substantial limitations on otherwise-deductible §162
business expenses for meals and entertainment. The TCJA (2017)
made the most significant change in decades: **entertainment
expenses are entirely non-deductible** (§274(a)(1)) starting in
2018. Meals remain 50%-deductible (with specific 100% exceptions).

The current rule structure (post-TCJA, post-CAA-2021):

| Category | Deduction |
|---|---|
| Entertainment (sports tickets, concerts, golf, fishing trips, club dues) | **0%** |
| Business meals with clients/customers (restaurant or similar) | **50%** |
| Employee meals at office (in-house cafeteria; convenience-of-employer) | 50% (was 100% pre-TCJA; phases to 0% by 2026 — verify current year) |
| Office snacks / break room food | 50% |
| Employee meal at all-employee meeting/event | 100% |
| Meals provided to employees at company picnics/holiday parties | 100% |
| Restaurant meals provided to employees as compensation (W-2 inclusion) | 100% to employer |
| Travel-while-away-from-home meals | 50% |
| Per-diem meal allowance | 50% |
| Marketing meals open to general public | 100% |
| Food/beverage in qualified employer-operated eating facility | 50% (phases to 0% by 2026) |

The TCJA also clarified that food/beverage with entertainment is
deductible 50% if separately stated on the bill (Notice 2018-76).
Food/beverage purchased at an entertainment event without
separately-stated charge is non-deductible.

## Primary IRC authority

- **§162(a)** — Ordinary and necessary business expenses.
- **§274(a)** — Disallowance of entertainment, amusement, or
  recreation activities.
- **§274(d)** — Substantiation requirements (amount, time, place,
  business purpose, business relationship).
- **§274(e)** — Specific exceptions to entertainment disallowance
  (food at picnics, employee compensation, etc.).
- **§274(k)** — Meals must not be "lavish or extravagant."
- **§274(n)** — 50% limitation on meals; 100% limitations on
  certain categories.
- **§274(o)** — 0% limitation phase-in for employer-operated eating
  facilities through 2025; eliminated by 2026 (verify current).

## Treasury regulations

- **Reg §1.274-1 through §1.274-12** — Implementing regulations.
- **Reg §1.274-11** (2020 final) — Entertainment disallowance after
  TCJA.
- **Reg §1.274-12** (2020 final) — 50% meals limitation rules.

## Key IRS guidance

- **Notice 2018-76** — Transitional guidance on TCJA M&E changes;
  food/beverage with entertainment 50%-deductible if separately
  stated.
- **Rev. Proc. 2019-48** — Per diem methodology.
- **Rev. Proc. updates annually** — High-low and standard per diem
  rates.
- **IRS Publication 463** — Travel, Gift, and Car Expenses.

## Key court decisions

- **Sutter v. Commissioner, 21 T.C. 170 (1953)** — Meals must have
  substantial business benefit beyond personal sustenance for
  deductibility.
- **Commissioner v. Sullivan, 356 U.S. 27 (1958)** — Defined
  business purpose substantiation.
- **Moss v. Commissioner, 758 F.2d 211 (7th Cir. 1985)** — Daily
  lunch meetings of law firm partners disallowed for lack of
  substantial business benefit.

## Eligibility requirements

For 50% meals deduction:
1. Meal not "lavish or extravagant" under §274(k).
2. Taxpayer (or employee) is present.
3. Provided to current or potential business contact.
4. Substantiated under §274(d): amount, time, place, business
   purpose, business relationship.

For 100% meals exceptions (§274(e)):
- Picnics, holiday parties, all-employee meetings.
- Meals reimbursed under accountable plan.
- Meals included in employee compensation (W-2).
- Restaurant operations (food held for sale).

## Mechanics — how it works

1. **Categorize each expense.**
2. **Apply the 50% / 100% / 0% classification.**
3. **Substantiate under §274(d).** Receipts plus contemporaneous
   notes (date, location, attendees, business purpose).
4. **For per diem reimbursement:** track high-low rates by location;
   employee receives tax-free per diem if substantiated; employer
   subject to 50% meals limitation.
5. **Track on books separately** — 50% meals account; 100% meals
   account; non-deductible entertainment account.

## Documentation requirements

- Receipts (or other documentary evidence; for amounts under $75
  except lodging, oral substantiation is allowable per Reg §1.274-
  5T(c)(2)(iii)).
- Date, location, attendees, business purpose, business relationship.
- For employee compensation meals: W-2 inclusion.

## Common pitfalls / audit risks

- **Entertainment characterized as meals.** Sports tickets, golf
  outings, concerts — entirely non-deductible since 2018.
- **Insufficient substantiation.** §274(d) is unforgiving.
- **All meals categorized at 50%** — missing 100% exceptions.
- **Restaurant requirement under §274(n)(2)(D).** Pre-CAA 2021
  100% restaurant meals (2021-2022) required actual restaurant
  setting; takeout from grocery deli did not qualify.
- **Per diem inflation.** Using rates above federal CONUS rates
  triggers W-2 inclusion of excess.

## Recent legislative changes

- **TCJA (2017)** — Eliminated entertainment deduction; reduced
  meals to 50%; phased in 0% on employer-operated eating facilities.
- **CAA 2021** — Temporarily 100% restaurant meals 2021-2022.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §274 meals
  entertainment Pub L 119-21]`. Working assumption: no major §274
  changes; some reports indicate full meal deductibility for certain
  categories restored. Verify.

## State conformity considerations

Most states conform. **California** has historically had unique
M&E rules. **Pennsylvania** has separate corporate income tax
treatment. Verify state stub.

## AICPA SSTS / Circular 230 considerations

Substantiation discipline is the practitioner's primary concern.
SSTS §1.4 reasonable inquiry into business purpose.

## Default confidence band rationale

**HIGH** for properly-substantiated 50% meals. **MODERATE** for
100% characterizations. **LOW** for entertainment characterized as
meals.

## Cross-references

- **`maximize-business-deductions`** (#13) — broader framework.
- **`accountable-plan-home-office`** (#2) — reimbursement structure.
- **`augusta-rule-280a-g`** (#24) — meal-rental edge case.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 274(a)(1)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section274",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 274(n)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section274",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.274-11",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.274-12",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2018-76",
      "url": "https://www.irs.gov/irb/2018-42_IRB",
      "weight": "irs_published"
    },
    {
      "authority_type": "CtAppeals",
      "citation": "Moss v. Commissioner, 758 F.2d 211 (7th Cir. 1985)",
      "url": "https://www.courtlistener.com",
      "weight": "binding_circuit"
    }
  ]
}
```
```

---

## Strategy #15: NOL Carryback / Carryforward

**File:** `references/strategies/nol-carryback-carryforward.md`

```markdown
---
name: "Net Operating Loss (NOL) Carryback and Carryforward"
slug: nol-carryback-carryforward
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§172", "§461(l)"]
forms: ["Form 1045 (quick refund)", "Form 1040X / 1120X (amended)", "Form 1139 (corp quick refund)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

A Net Operating Loss (NOL) is the excess of allowable deductions
over gross income for the tax year. NOLs can offset taxable income
in other years through carryback and carryforward mechanisms,
producing tax refunds (for carrybacks) or tax savings in future
years (for carryforwards).

The §172 rules have changed substantially:

**Pre-TCJA (NOLs arising before 2018):** 2-year carryback,
20-year carryforward, unlimited offset of taxable income.

**TCJA (NOLs arising 2018-2020):** No carryback; indefinite
carryforward; 80% of taxable income offset limit.

**CARES Act (NOLs arising 2018-2020 only, retroactive):**
Restored 5-year carryback for those years; suspended 80% limitation
for those years; ability to elect out of carryback.

**Post-CARES (NOLs arising 2021+):** No carryback; indefinite
carryforward; 80% of taxable income offset limit (back to TCJA
rule).

This change creates intricate timing analysis: NOLs from different
years follow different rules, and the practitioner must track each
NOL year's vintage separately.

§461(l) Excess Business Loss: Created by TCJA, originally suspended
through 2020 by CARES, now permanent through 2028 (via 2022 IRA
extension; OBBBA may have extended further). Limits net business
losses to a threshold ($305,000 single / $610,000 MFJ for 2024;
indexed). Excess becomes NOL carryforward subject to §172 rules.

## Primary IRC authority

- **§172(a)** — NOL deduction.
- **§172(b)** — Carryback and carryforward periods.
- **§172(b)(2)** — 80% taxable income limitation.
- **§172(d)** — NOL definition; modifications.
- **§461(l)** — Excess business losses; created by TCJA.

## Treasury regulations

- **Reg §1.172-1 through §1.172-13** — NOL implementing regulations.
- **Reg §1.461-1** — General timing rules.

## Key IRS guidance

- **Rev. Proc. 2020-24** — CARES Act NOL implementation.
- **Notice 2020-26** — CARES Act NOL guidance.
- **Rev. Proc. 2020-50** — §168 / §172 procedural guidance.
- **IRS Publication 536** — NOLs for Individuals, Estates, and
  Trusts.

## Key court decisions

- Limited recent dispute area; rules are largely mechanical.

## Eligibility requirements

For NOL generation:
1. Deductions exceed gross income.
2. NOL determined per §172(d) modifications (no NOL deduction in
   computing NOL; limited capital loss; no §199A QBI; no §250
   FDII/GILTI; no §1202 exclusion; etc.).

For carryback (CARES Act years 2018-2020 only):
1. NOL arises in 2018, 2019, or 2020.
2. Form 1045 (individual) or Form 1139 (corporation) for quick
   refund within 12 months of year-end.
3. OR Form 1040X / 1120X amended return.
4. Election to forgo carryback under §172(b)(3).

For carryforward (post-2020):
1. Indefinite carryforward.
2. 80% of taxable income offset limit per year.

## Mechanics — how it works

1. **Determine NOL.** Compute on Schedule A of Form 1045 (individual)
   or per §172(d) for corporations.
2. **Determine vintage.** Apply rules applicable to NOL year.
3. **Coordinate with §461(l).** Determine excess business loss; convert
   to NOL.
4. **Carryback (if applicable).** File Form 1045 (individual) or
   Form 1139 (corporation) for quick refund within 12 months of
   year-end. Otherwise file Form 1040X / 1120X.
5. **Carryforward.** Track each NOL year's vintage and remaining
   balance. Apply 80% taxable income limitation per year.
6. **State NOL tracking.** Many states have separate NOL rules
   (different carryback/carryforward periods, different limits).

## Documentation requirements

- NOL computation workpapers with §172(d) modifications.
- Form 1045 / 1139 / 1040X / 1120X.
- Multi-year NOL schedule by vintage.
- §461(l) computation if applicable.
- State NOL schedules.

## Common pitfalls / audit risks

- **Failure to elect out of CARES Act carryback** — §172(b)(3)
  election if carryback would generate refund of low-tax-rate years
  while taxpayer is in higher tax bracket on carryforward.
- **Incorrect NOL modifications.** §172(d) excludes various items
  (capital losses, §199A, §250) that affect NOL determination.
- **§461(l) trap.** Net business loss limited to threshold; excess
  becomes NOL.
- **State decoupling.** Many states do not follow federal CARES Act
  carryback or 80% limit; track separately.
- **Form 1045 12-month deadline.** After the deadline, must use
  Form 1040X / 1120X (amended returns).
- **AMT NOL.** AMT NOL is a separate computation; track in parallel
  for years with AMT exposure.

## Recent legislative changes

- **TCJA (2017)** — Eliminated 2-year carryback; 80% limit;
  indefinite carryforward.
- **CARES Act (2020)** — 5-year carryback for 2018-2020 NOLs;
  suspended 80% limit for those years.
- **TCDTRA 2020 / CAA 2021** — Various technical corrections.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §172 §461(l)
  Pub L 119-21]`. Reports indicate §461(l) extended; §172 generally
  unchanged.

## State conformity considerations

State NOL rules vary widely. Major decoupling states for NOLs:
California (separate NOL system), New York, New Jersey,
Pennsylvania, Massachusetts. Track state NOLs separately.

## AICPA SSTS / Circular 230 considerations

Standard diligence; NOL utilization decisions can affect multiple
years and require careful documentation.

## Default confidence band rationale

**HIGH** for properly-computed NOLs and carryforward applications.
Drops to MODERATE for §172(d) modifications that are complex (e.g.,
NOLs interacting with §199A or §250).

## Cross-references

- **`worthless-stock-ordinary-loss`** (#30) — generates NOL.
- **`maximize-business-deductions`** (#13) — generates current-
  year deductions.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 172",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section172",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 461(l)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section461",
      "weight": "primary_statute"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2020-24",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
```

---

## Strategy #16: Passive Income & PIGs

**File:** `references/strategies/passive-income-pigs.md`

```markdown
---
name: "Passive Income Generators (PIGs) and Passive Loss Absorption"
slug: passive-income-pigs
type: Business - Other
tax_type: EFR
complexity: High
irc_sections: ["§469"]
forms: ["Form 8582"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

## Overview

A "Passive Income Generator" (PIG) is an investment that produces
§469 passive income, used strategically to absorb suspended passive
losses from other passive activities. The §469 rules require that
passive losses be deductible only against passive income; losses in
excess of passive income suspend and carry forward (with eventual
release upon complete disposition under §469(g)). PIGs invert this
problem by intentionally generating passive income that the
taxpayer can offset with otherwise-suspended losses.

Common PIG structures:
- **Limited partnership interests in income-producing businesses.**
- **Working interests in oil and gas** (NOT a passive activity under
   §469(c)(3) — but if structured to fail working-interest exception,
   becomes passive).
- **Net leased real estate** — by statute and regulation a passive
  activity (no material participation possible).
- **Carried-interest shells** structured around passive treatment.

The classic PIG structure was the subject of significant abuse in
the 1980s and 1990s (sham passive income generators); the IRS has
brought numerous challenges. Modern PIG planning requires economic
substance — the income-producing activity must be real, not merely
a tax conduit.

## Primary IRC authority

- **§469(a)** — General PAL disallowance.
- **§469(c)** — Definitions of passive activity.
- **§469(c)(2)** — Per-se passive treatment of rentals.
- **§469(c)(3)** — Working interest exception (oil & gas).
- **§469(d)(1)** — Passive activity loss definition.
- **§469(g)** — Disposition of activity.
- **§469(h)** — Material participation tests.

## Treasury regulations

- **Reg §1.469-1 through §1.469-11** — Implementing regulations.
- **Reg §1.469-2(f)(6)** — Self-rental recharacterization rule.
- **Reg §1.469-2T(f)** — Recharacterization of passive income to
  nonpassive in certain situations (the "trap" — net rental income
  from property leased to a related taxpayer's nonpassive business
  is recharacterized as nonpassive, defeating PIG strategy if not
  carefully structured).

## Key IRS guidance

- **IRS Publication 925** — Passive Activity and At-Risk Rules.

## Key court decisions

- **Schwalbach v. Commissioner, 111 T.C. 215 (1998)** — Self-rental
  rule analysis.
- **Krukowski v. Commissioner, 114 T.C. 366 (2000)** — Self-rental
  applied; net rental income recharacterized as nonpassive.
- **Beecher v. Commissioner, 481 F.3d 717 (9th Cir. 2007)** —
  Affirmed self-rental recharacterization.

## Eligibility requirements

For an investment to be a valid PIG:
1. Activity must be a passive activity under §469(c).
2. Income must be passive income, not subject to recharacterization
   under Reg §1.469-2T(f).
3. Income must have economic substance (real income from real
   activity).
4. Taxpayer must not materially participate.

## Mechanics — how it works

1. **Identify suspended passive losses.** Typically from rental real
   estate or LP interests.
2. **Source PIG investment.** Common: LP interest in income-
   producing real estate; LP interest in operating business; net
   lease commercial property.
3. **Verify passive characterization.** Apply §469 tests; verify no
   recharacterization risk under Reg §1.469-2T(f).
4. **Hold long enough to generate income.** Match passive income
   to passive losses on Form 8582.
5. **Avoid self-rental trap.** Property rented to taxpayer's own
   business (or commonly-owned business) is recharacterized as
   nonpassive net income — destroying PIG utility.

## Documentation requirements

- Investment documents (LP agreement, etc.).
- Schedule K-1s.
- Form 8582 with passive activity tracking.
- Self-rental analysis if applicable.

## Common pitfalls / audit risks

- **Self-rental recharacterization.** If passive income comes from
  property rented to a business in which taxpayer materially
  participates, Reg §1.469-2T(f)(6) recharacterizes the income as
  nonpassive — defeating the PIG strategy.
- **Sham PIG.** Investments without economic substance are
  challenged.
- **Working interest oil & gas.** §469(c)(3) excludes working
  interests from passive — careful structuring required if the goal
  is passive income.
- **Material participation in PIG.** Inadvertent material
  participation defeats passive treatment.
- **Loss release on disposition.** Disposing of the PIG itself
  triggers release of THAT activity's losses, not the underlying
  losses the PIG was meant to absorb.

## Recent legislative changes

- **TCJA (2017)** — No direct §469 changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §469 PIG
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §469 is generally complete; PIG strategy flows
through.

## AICPA SSTS / Circular 230 considerations

PIG strategies attract IRS scrutiny. Practitioner must verify
economic substance and absence of recharacterization.

## Default confidence band rationale

**MODERATE** — depends on absence of self-rental recharacterization
and economic substance. **LOW** for aggressive structures or
investments with thin operating substance.

## Cross-references

- **`active-participation-real-estate`** (#3) — alternative for
  $25K offset.
- **`grouping-of-activities`** (#9) — alternative loss absorption
  through grouping.
- **`real-estate-professional`** (#20) — REPS releases all rentals
  from passive treatment.
- **`predict-material-participation`** (predict skill).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 469",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.469-2(f)(6)",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TaxCt",
      "citation": "Krukowski v. Commissioner, 114 T.C. 366 (2000)",
      "url": "https://www.ustaxcourt.gov",
      "weight": "judicial"
    }
  ]
}
```
```

---

## Strategy #17: PTET (Pass-Through Entity SALT Workaround)

**File:** `references/strategies/ptet-salt-workaround.md`

```markdown
---
name: "Pass-Through Entity Tax (PTET) — SALT Cap Workaround"
slug: ptet-salt-workaround
type: Business - Other
tax_type: EFR
complexity: High
irc_sections: ["§164(b)(6)", "§164"]
forms: ["State PTE election forms (varies by state)", "K-1s adjusted for PTET credit"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

The Pass-Through Entity Tax (PTET) is the most consequential state
tax planning strategy of the 2020s. It is a state-level workaround
to TCJA's $10,000 cap on state and local tax (SALT) deductions
under §164(b)(6). The mechanism: a partnership or S corporation
elects to pay state income tax at the entity level (entity-level
state tax is fully deductible federally as a §162 business
expense), with the entity's owners receiving a state tax credit
for their share of the PTET paid. The result: the entity's owners
effectively get full federal deduction for state income tax that
otherwise would have been capped at $10,000.

The IRS validated the structure in **Notice 2020-75** (issued
November 9, 2020): "specified income tax payments" made by a
partnership or S corporation to a state are deductible by the
entity in computing its non-separately stated taxable income.
This Notice essentially blessed the workaround that approximately
36 states (and counting) have now enacted.

State variation is enormous:
- **Mandatory vs. elective:** Most are elective; CA's was elective
  through 2025; NY's is annual elective; Minnesota's was originally
  mandatory then elective.
- **Election timing:** Some require election by entity due date;
  others by extended due date; some allow late election.
- **Calculation methodology:** Some apply state's top individual
  rate; others apply graduated rates; others use unique formulas.
- **Credit mechanism:** Some give 100% credit at owner level;
  some give partial.
- **Resident vs. nonresident:** Some apply only to resident owners;
  some both.
- **Coordination with composite/withholding:** State-by-state.

For practitioners, the PTET decision is one of the most consequential
year-end planning decisions for pass-through entities. The state
stub files in `tax-research-state-income/references/states/<XX>.md`
should track each state's PTET regime in detail.

## Primary IRC authority

- **§164(b)(6)** — $10,000 SALT cap (TCJA-created; OBBBA may have
  modified — verify).
- **§164** — Taxes generally deductible.
- **§162** — Business expense deduction.

## State authority

PTET is fundamentally state law. Each state's PTET statute and
regulations govern. Reference state-specific stubs for citations.

## Treasury regulations

No federal Treasury Regulation specifically addresses PTET (the
issue is a state-tax characterization).

## Key IRS guidance

- **Notice 2020-75** — Specified income tax payments by partnerships
  and S corporations are deductible at the entity level.
  https://www.irs.gov/irb/2020-49_IRB
- The Notice validated the structure but stopped short of issuing
  full regulations.

## Key court decisions

- No major federal case law specifically addressing PTET (because
  Notice 2020-75 effectively settled federal treatment).

## Eligibility requirements

Vary by state. Common requirements:
1. Entity is a partnership or S corporation.
2. Owners include at least some individuals (some states bar
   non-PTE owners or require all-individual ownership).
3. Election made within state-specific deadline.
4. Entity pays the PTET in the year claimed.

## Mechanics — how it works

1. **Identify state PTET regimes** for each state where the
   pass-through entity operates or has resident owners.
2. **Run cost-benefit analysis.**
   - Federal benefit: PTET amount × owner's marginal federal rate
     × percentage of owner's SALT cap that PTET avoids.
   - State cost: any difference between PTET rate and what the
     owner would have paid as resident.
   - Coordination cost: AMT, NIIT, basis tracking.
3. **Make the election by deadline** (varies by state).
4. **Pay the PTET.** Entity makes payment to state.
5. **Adjust K-1s.** Reduce ordinary income by PTET; increase basis
   adjustment.
6. **Owner claims credit at state level.** Effectively eliminates
   owner's individual state tax on the related income.
7. **Federal Schedule K reporting.** PTET deduction reduces income
   passed through to owners. Owner's federal AGI is reduced
   accordingly.

## Documentation requirements

- State PTET election forms.
- Entity-level PTET payment records.
- Adjusted K-1s reflecting PTET deduction.
- State return reflecting PTET payment.
- Owner state return claiming PTET credit.

## Common pitfalls / audit risks

- **Election deadline missed.** State-specific deadlines are strict.
- **Wrong year payment.** Cash basis entities must actually pay in
  the deduction year.
- **Federal/state coordination.** Owner basis adjustments,
  estimated payment recalculation, AMT, NIIT all interact.
- **Resident vs. nonresident issues.** Some states' PTET applies
  only to resident owners' shares; need careful entity allocation.
- **Multiple-state owner.** PTET benefit calculation across states
  is complex.
- **Composite return interaction.** PTET typically replaces
  composite/nonresident withholding regimes.

## Recent legislative changes

- **TCJA (2017)** — Created $10,000 SALT cap effective 2018.
- **Notice 2020-75 (November 2020)** — Federal validation of PTET
  structure.
- **Wave of state PTET enactments 2018-2024** — Now ~36 states
  plus DC.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA SALT cap
  §164(b)(6) Pub L 119-21]`. Reports indicate OBBBA modified the
  SALT cap. Possible scenarios: (a) increased to $40,000; (b)
  eliminated; (c) made permanent. PTET utility depends on the
  specific OBBBA SALT cap treatment. Verify via Classification
  Tables.

## State conformity considerations

PTET is fundamentally state-by-state. Track in per-state stub
files. Major variations:
- **CA SB 113 / AB 150** — California PTET; up to 9.3% rate;
  elective.
- **NY S2509 / Tax Law §860** — New York PTET; graduated rates.
- **NJ BAIT** — New Jersey Business Alternative Income Tax.
- **MA Chapter 269 of 2021 Acts** — Massachusetts 4% PTE excise.

## AICPA SSTS / Circular 230 considerations

PTET decisions are major year-end planning events. Practitioner
should run formal cost-benefit analysis and document.

## Default confidence band rationale

**HIGH** — Notice 2020-75 explicitly validated the structure;
state legislation provides clear statutory basis. Drops to
MODERATE only for unusual structures or election timing edge cases.

## Cross-references

- **`state-tax-savings`** (#40) — broader state planning.
- **`c-corp-state-tax-savings`** (#35) — C corp variant.
- All state stub files at
  `skills/tax-research-state-income/references/states/<XX>.md`.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 164(b)(6)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section164",
      "weight": "primary_statute"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2020-75",
      "url": "https://www.irs.gov/irb/2020-49_IRB",
      "weight": "irs_published"
    }
  ]
}
```
```

---

**End of Part 2 of 10.** Strategies #8 through #17 delivered.

**Continue to Part 3 of 10** for strategies #18 through #27 (Prepayment of Expense, QBI Deduction, Real Estate Professional, Reasonable Comp - Corp Owners, Reimbursement of Business Expenses, Reimbursement of Depreciation - S Corp Vehicle, Augusta Rule, Rental Strategies, Short-Term Rental, Startup Cost Optimization).
