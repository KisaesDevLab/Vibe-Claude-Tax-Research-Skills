---
name: "10 Tax Strategies for S Corporations: What, How, Where on Form 1120-S"
slug: s-corp-strategy-catalog
type: Strategy Catalog
tax_type: Income / SE
complexity: Moderate
applies_to: ["S corporation owner-employees", "Form 1120-S preparers"]
forms: ["Form 1120-S", "Form W-2", "Form 1040 Schedule E", "Form 4562"]
state_specific: true
caution: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
ss_wage_base_2025: 176100
ss_wage_base_2026: 184500
qbi_threshold_2025_mfj: 394600
qbi_threshold_2025_single: 197300
---

# 10 Tax Strategies for S Corporations — Form 1120-S Map

This catalog organizes the ten most-impactful S corporation tax
strategies and maps each to its line position on **Form 1120-S**.
Each entry is a brief summary; full mechanics, authorities, and
samples are in the linked skills. **2025 / 2026 figures are
current** (post-OBBBA, July 4, 2025).

## Form 1120-S map (where each strategy lands)

| Form 1120-S Line | Strategy(ies) |
|---|---|
| Line 7 — Compensation of officers | #1 (Reduce Owner Wages); #2 (Health Insurance) |
| Line 8 — Salaries and wages | #3 (Employ Your Child) |
| Line 11 — Rents | #6 (Augusta Rule — Rent Home to S Corp) |
| Line 14 — Depreciation | #4 (Sale of Home to S Corp Before Rental Conversion) |
| Line 18 — Employee benefit programs | #10 (Cell Phone / Smartphone) |
| Line 19 — Other deductions | #5 (Home Office Reimbursement); #7 (Depreciation Reimbursement); #8 (Vehicle Reimbursement); #9 (Travel Reimbursement) |

---

## Strategy #1 — Reduce S Corporation Owner Wages

**What it does.** Reduces the W-2 wages paid to the
shareholder-employee to the lowest defensible amount, shifting
the residual to K-1 distributions. K-1 distributions are
**not** subject to FICA / SE tax (15.3% combined OASDI/HI on
wages up to the SS wage base; 2.9% HI plus 0.9% Additional
Medicare on wages above).

**How it works.** Net SE tax savings = (excess wage reduction) ×
(applicable FICA rate). 2025 SS wage base = **$176,100**; 2026
= **$184,500**.

**Where on Form 1120-S.** Line 7 (Compensation of officers).

**Critical constraint.** "Reasonable compensation" requirement —
**Mayson Manufacturing 9-factor test** (1949) and **Elliotts
5-factor test** (1983) determine the floor. Setting wages
unreasonably low triggers IRS reclassification of distributions
under **§7436** authority. See *Watson v. United States*, 668
F.3d 1008 (8th Cir. 2012) and *Sean McAlary Ltd., Inc. v.
Commissioner*, T.C. Sum. Op. 2013-62. Cross-reference:
`reasonable-comp-corp-owners` strategy and CPE wage:distribution
ratio table heuristic.

**§199A interaction.** Wages above the QBI threshold ($394,600
MFJ / $197,300 single for 2025) are subject to the W-2 wage
limitation. Below the threshold, the QBI deduction (post-OBBBA
permanent) generally favors lower wages and higher K-1 income.

**Linked skill:** `reasonable-comp-corp-owners`

---

## Strategy #2 — Deduct S Corporation Owner Health Insurance Premiums

**What it does.** S corp pays the health insurance premium for a
≥2% shareholder; premium is added to the shareholder's W-2 Box 1
wages (income tax) but **excluded from Box 3 / Box 5** (FICA-free
under §3121(a)(2)(B)). On the shareholder's personal Form 1040,
the premium is deducted **above the line** as the
self-employed health insurance deduction (§162(l)).

**Net effect:** Income-tax neutral but **saves 15.3% FICA** on
the premium amount; ultimately a deduction equal to the
premium without FICA cost.

**How it works.**
1. S corp must establish the health insurance plan (or
   premiums are paid in the corporation's name); per Notice
   2008-1, premiums paid by the shareholder personally and
   reimbursed by the corporation also qualify.
2. Premium is included in Box 1 (wages subject to income tax)
   but excluded from Box 3 (Social Security wages) and Box 5
   (Medicare wages) per Notice 2008-1.
3. Box 14 reports the premium for the shareholder's tracking.
4. On Form 1040 Schedule 1, the premium is deducted as
   self-employed health insurance.

**Where on Form 1120-S.** Premium paid increases Line 7
(Compensation of officers) — the same line as the underlying
W-2 wages. NOT deducted separately as employee benefits (Line
18) for the ≥2% shareholder; deducted there only for non-
shareholder employees.

**Constraints.**
- Eligibility limited to family/group coverage; HSA
  contributions follow same treatment.
- Must satisfy the Affordable Care Act reporting requirements
  (Form 1095-B/C if applicable).
- Cannot exceed earned income from the S corp.

**Linked skill:** `s-corp-health-insurance-2pct-shareholder`

---

## Strategy #3 — Employ Your Child

**What it does.** Shifts income from the higher-bracket parent
to the lower-bracket (often zero-bracket) child via legitimate
employment.

**How it works.**
- Each child can earn up to the **standard deduction** (2025:
  **$15,000** single) without owing federal income tax.
- The corporation deducts wages paid (Line 8 — Salaries and
  Wages).
- Child reports the wages on their own Form 1040; tax may be
  zero if under the standard deduction.
- Child's earned income can fund a Roth IRA (up to $7,000 for
  2025).

**Where on Form 1120-S.** Line 8 (Salaries and wages — for
non-officer wages).

**Constraints (S corp specific).**
- **FICA applies.** Unlike sole proprietorships and Schedule C
  / single-member LLCs (where children under 18 are exempt
  from FICA per §3121(b)(3)(A)), wages paid by an S
  corporation to a child are **subject to FICA** regardless of
  the child's age. This significantly reduces the strategy's
  S corp benefit relative to Schedule C.
- **Bona fide work required.** The child must perform actual
  work appropriate to their age and capacity. *Eller v.
  Commissioner*, 77 T.C. 934 (1981); *Denman v. Commissioner*,
  48 T.C. 439 (1967).
- **Reasonable wage required.** Wages must be commensurate
  with work performed.
- **Documentation:** time records, written employment
  agreement, separate bank account for child's wages.

**Linked skill:** `hiring-children-s-corp` (also see
`hiring-children-schedule-c` for the more-favorable sole
proprietorship variant).

---

## Strategy #4 — Sell Home to S Corporation Before Rental Conversion

**What it does.** Before converting a personal residence to
rental property, the homeowner sells it to their S corp at
**fair market value**. The owner uses the **§121 home-sale
exclusion** ($250,000 single / $500,000 MFJ) to exclude the
gain. The S corp then operates the property as a rental with
a **stepped-up basis** equal to the FMV purchase price —
producing larger depreciation deductions than if the rental
conversion happened at the original cost basis.

**How it works.**
1. Owner sells home to S corp at FMV.
2. Owner reports gain on Form 8949 / Schedule D; excludes up
   to §121 limit.
3. S corp's depreciable basis = FMV (less land allocation).
4. S corp depreciates 27.5-year residential rental.

**Where on Form 1120-S.** Line 14 (Depreciation — for the
stepped-up basis depreciation).

**Critical constraints.**
- **§121(d)(11) related-party rules.** Sale to a related party
  (§267(b)) is permitted for §121 purposes, but the buyer's
  depreciation deductions are limited under §1239 (gain on sale
  of depreciable property to related party = ordinary income to
  seller, eliminating §121 benefit on depreciable portion).
  **Critical analysis:** Allocate sale price between land
  (non-depreciable; §121 gain excluded) and structure
  (depreciable; §1239 gain may be ordinary).
- **§121 use-and-ownership tests.** Owner must have owned and
  used the home as principal residence for **2 of the 5
  preceding years**.
- **Anti-churning rules.** Cannot do multiple §121 exclusions
  within 2-year window.
- **Substance over form.** Must be a **bona fide sale** with
  arms-length terms — financing, escrow, recorded deed,
  appropriate insurance, etc.

**Cases of note:**
- *Wendy E. Smith v. Commissioner*, T.C. Memo. 2002-148 —
  related-party sale to family corporation; §121 / §1239
  interaction.
- *Bradford Tax Institute* practitioner literature — extensive
  practitioner discussion of this strategy.

**Linked skill:** `selling-home-to-s-corp-before-rental` and
`section-1239-related-party-depreciation`

---

## Strategy #5 — Reimbursement of Home Office Expenses

**What it does.** Owner-employee submits home-office expense
reports under accountable plan; corporation reimburses business-
use percentage of mortgage interest, property taxes, utilities,
insurance, repairs, depreciation, HOA dues. Reimbursement is
**non-taxable** to the employee (§62(a)(2)(A)) and **fully
deductible** to the corporation.

**Where on Form 1120-S.** Line 19 (Other deductions), labeled
"Office space" or "Home office reimbursement."

**Authority chain.**
- §280A(c)(1) permits the home-office deduction at the
  individual level if regular-and-exclusive-use, principal-
  place-of-business, and convenience-of-employer tests
  satisfied.
- §62(a)(2)(A) and Reg. §1.62-2 allow the corporation to
  reimburse the employee's §280A(c)(1)-qualified expenses
  under an accountable plan.
- *Hamacher v. Commissioner*, 94 T.C. 348 (1990) — convenience-
  of-employer 3-test framework.

**Critical constraint.** §280A(c)(6) **bars** the alternative
"rent the office to the corporation" approach — employee-to-
employer rentals have no offsetting deductions. See full skill
for analysis.

**Linked skill:** `s-corp-home-office-reimbursement`

---

## Strategy #6 — Rent Home to S Corporation (Augusta Rule)

**What it does.** Owner rents their **entire home** to the S
corporation for **14 days or fewer** during the year. The
corporation deducts the rent as an ordinary §162 business
expense (e.g., for board meetings, retreats, training events,
client entertainment). The owner excludes the rental income
from gross income under **§280A(g)** ("Augusta Rule") because
the home is used as a personal residence and rented for
fewer than 15 days.

**Where on Form 1120-S.** Line 11 (Rents).

**Authority.** §280A(g) (formerly known as "Masters Rule" or
"Augusta Rule" — refers to homeowners renting to broadcasters
during the Masters golf tournament).

**Critical constraints.**
- **14-day limit is absolute.** A 15th day disqualifies the
  exclusion entirely; all 15 days of rent become taxable
  income.
- **Rent must be reasonable.** §482 / §162 reasonableness
  applies. Use comparable Airbnb / VRBO / hotel meeting room
  rates for the locale.
- **Documentation required.**
  - Board resolution authorizing the rental and the business
    purpose.
  - Written rental agreement.
  - Comparable rate evidence (screenshots of Airbnb/VRBO
    listings, banquet hall quotes).
  - Meeting agendas and attendance records.
- **Form 1099-MISC.** Corporation issues Form 1099-MISC
  (Box 1) to the owner for rent paid. Owner reports on
  Schedule E, then claims the §280A(g) exclusion on the same
  schedule.
- **Practitioner trap.** *Sinopoli v. Commissioner*, T.C. Memo.
  2023-105 — Tax Court rejected an S corp owner's $3,000/day
  rental of a home for 12 days as not a true §162 ordinary-
  and-necessary business expense and not reasonable in amount.
  The corporation's rent deduction was **disallowed** while
  the owner still had to report rental income (worst of both
  worlds). **Lesson:** Rental rate and business purpose must
  withstand scrutiny.

**Linked skill:** `augusta-rule-280a-g`

---

## Strategy #7 — Reimbursement of Depreciation Expenses

**What it does.** When the owner-employee personally owns
business assets (vehicle, computer, equipment) and uses them
for corporate business, the corporation reimburses the owner
for §179 expensing, §168(k) bonus depreciation, and MACRS
depreciation under the accountable plan. **Per PLR 200930029**,
§179 does not require corporate title — only that the
corporation bear the cost (satisfied by reimbursement).

**Where on Form 1120-S.** Line 19 (Other deductions), labeled
"Reimbursement for employee business expenses" or similar.

**Authority chain.**
- §179, §168(k), §168 (depreciation deductions).
- Reg. §1.179-1(a) and (e) — corporation need not hold title.
- §62(a)(2)(A) and Reg. §1.62-2 — accountable plan exclusion.
- PLR 200930029 — explicit confirmation of reimbursement
  approach.

**2025 / 2026 figures (post-OBBBA):**
- §179 limit: $2,500,000 (2025); $2,560,000 (2026).
- §179(b)(5) SUV cap: $31,300 (2025); $32,000 (2026).
- §168(k) bonus: 100% for property acquired after 1/19/2025,
  permanent.

**Linked skill:** `corp-vehicle-personal-name` (and
`section-179-qualifiers` for non-vehicle property).

---

## Strategy #8 — Reimbursement of Vehicle Expenses

**What it does.** Specific application of Strategy #7 to
vehicles. Combined with home-office strategy (Strategy #5), the
home becomes the principal place of business — eliminating
commuting miles and increasing business-use percentage to ~95%+
in many cases.

**Where on Form 1120-S.** Line 19 (Other deductions), labeled
"Vehicle expenses" or "Employee reimbursed expenses."

**Heavy SUV + home office = "major tax savings combo."** A
heavy SUV (>6,000 lbs GVWR) combined with a qualifying home
office produces immediate Year-1 deductions in the $40K-$90K
range for typical owner-employees.

**Linked skill:** `corp-vehicle-personal-name`

---

## Strategy #9 — Reimbursement of Travel Expenses

**What it does.** Owner-employee submits travel expense reports
under accountable plan for business travel; corporation
reimburses (transportation, lodging, meals at 50%) tax-free to
employee, deductible to corporation.

**Where on Form 1120-S.** Line 19 (Other deductions), labeled
"Travel" or "Employee reimbursed expenses."

**Authority chain.**
- §162(a)(2) — travel away from home in pursuit of trade or
  business.
- §274(d) — substantiation requirements (time, place, business
  purpose, amount).
- §274(n) — 50% meal limitation.
- Reg. §1.62-2 — accountable plan.

**Domestic vs. foreign travel rules:**
- **Domestic travel:** If majority of trip days are business,
  100% of transportation is deductible. Lodging and 50% of
  meals deductible for business days only.
- **Foreign travel < 7 days:** 100% of transportation
  deductible regardless of mix (per §274(c)).
- **Foreign travel ≥ 7 days:** Allocation between business and
  personal days.

**Critical:** OBBBA temporary 100% meal deduction (under §274(n)
relief during COVID for restaurant meals 2021-2022) has
**reverted to 50%** for tax years 2023+.

**Linked skill:** `business-travel-reimbursement` and
`travel-rules-7-day-foreign`.

---

## Strategy #10 — Cell Phone / Smartphone Expenses

**What it does.** Corporation provides employee with a
smartphone (or reimburses for personal phone used for business)
**primarily for non-compensatory business reasons**. The IRS
treats this as a **working-condition fringe benefit** under
§132(d), excludable from the employee's wages.

**Where on Form 1120-S.** Line 18 (Employee benefit programs)
or Line 19 (Other deductions) depending on whether the cell
phone provision is part of a broader employee benefit plan or a
specific reimbursement.

**Authority.**
- §132(d) — working-condition fringe benefit.
- **Notice 2011-72** — IRS guidance: cell phones provided for
  non-compensatory business reasons are working-condition
  fringes under §132(d); **no allocation required between
  business and personal use**.
- **Memorandum SBSE-04-0911-083** — examination guidance
  consistent with Notice 2011-72.

**Critical:** The **non-compensatory business reasons** test
requires:
- Need to contact employee at all times for work-related
  emergencies.
- Need for employee to be available when away from office.
- Need to speak with clients in different time zones.

**The phone may be used for personal purposes; full cost is
still deductible** as the working-condition fringe — no
allocation required.

**Linked skill:** `cell-phone-fringe-benefit-notice-2011-72`

---

## Implementation notes

These ten strategies are typically implemented in combination —
the full package can produce $20,000-$60,000 in annual tax
savings for a typical S corp owner-employee. The accountable
plan (Reg. §1.62-2) is the **operational backbone** for
strategies #5, #7, #8, #9 (and supports #10).

**Annual workflow:**

1. **Q1 — Adoption.** Adopt or update accountable plan;
   establish reasonable comp baseline; check OBBBA / annual
   indexing of §179, §168(k), QBI thresholds.
2. **Quarterly — Substantiation.** Submit expense reports for
   home office, vehicle, travel, cell phone.
3. **Q4 — Year-end.** Health insurance W-2 inclusion (W-2 Box 1
   adjustment by Dec 31); §1377(a)(2) closing-of-books
   coordination if shareholder turnover; §663(b) 65-day rule
   coordination if connected trusts.
4. **Q1 of following year.** Form 1120-S preparation with
   strategy-mapping; verification of §199A QBI calculation.

## State conformity considerations

- **California** — does not conform to §168(k) bonus; §179
  capped at $25,000 (CA §17250).
- **New York** — selective conformity; QBI deduction does not
  apply for state income tax.
- **Texas** — franchise tax: §179 in COGS allowed; bonus not
  allowed in COGS.
- **Pennsylvania** — does not conform to §168(k) bonus.
- **Tennessee** — Excise and franchise tax on S corp net
  earnings; no federal-state distinction on most strategies.
- **Massachusetts** — S corp net income above threshold subject
  to MA corporate excise.

## Cross-references to other skills

- `reasonable-comp-corp-owners` — Strategy #1 deep dive.
- `s-corp-health-insurance-2pct-shareholder` — Strategy #2
  deep dive.
- `hiring-children-s-corp` — Strategy #3 deep dive.
- `selling-home-to-s-corp-before-rental` — Strategy #4 deep
  dive.
- `s-corp-home-office-reimbursement` — Strategy #5 deep dive.
- `augusta-rule-280a-g` — Strategy #6 deep dive.
- `corp-vehicle-personal-name` — Strategies #7 and #8 deep
  dive.
- `business-travel-reimbursement` — Strategy #9 deep dive.
- `cell-phone-fringe-benefit-notice-2011-72` — Strategy #10
  deep dive.

## Authorities (consolidated JSON sidecar)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 132(d)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section132","weight":"primary_statute","note":"Working-condition fringe"},
    {"authority_type":"IRC","citation":"I.R.C. § 280A(c)(1)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 280A(c)(6)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 280A(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute","note":"Augusta Rule"},
    {"authority_type":"IRC","citation":"I.R.C. § 121","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section121","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1239","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1239","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 162(l)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute","note":"SE health insurance"},
    {"authority_type":"IRC","citation":"I.R.C. § 199A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section199A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 7436","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7436","weight":"primary_statute","note":"IRS reclassification authority"},
    {"authority_type":"IRC","citation":"I.R.C. § 274(d)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section274","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 274(n)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section274","weight":"primary_statute","note":"50% meal limitation"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.62-2","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"Notice","citation":"Notice 2008-1","url":"https://www.irs.gov","weight":"irs_published","note":"S corp 2%-shareholder health insurance W-2 reporting"},
    {"authority_type":"Notice","citation":"Notice 2011-72","url":"https://www.irs.gov","weight":"irs_published","note":"Cell phone working-condition fringe"},
    {"authority_type":"Notice","citation":"IRS Notice 2018-59","url":"https://www.irs.gov","weight":"irs_published","note":"Pickup with 6+ ft cargo bed not subject to SUV cap"},
    {"authority_type":"PLR","citation":"PLR 200930029","url":"https://www.irs.gov","weight":"non_precedential_irs","note":"§ 179 reimbursement to employee"},
    {"authority_type":"PublicLaw","citation":"Pub. L. 119-21 (OBBBA, July 4, 2025)","url":"https://www.congress.gov","weight":"primary_statute"},
    {"authority_type":"CtAppeals","citation":"Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)","url":"https://www.courtlistener.com","weight":"binding_circuit","note":"Reasonable compensation S corp"},
    {"authority_type":"CtAppeals","citation":"Mayson Manufacturing Co. v. Commissioner, 178 F.2d 115 (6th Cir. 1949)","url":"https://www.courtlistener.com","weight":"binding_circuit","note":"9-factor test"},
    {"authority_type":"CtAppeals","citation":"Elliotts, Inc. v. Commissioner, 716 F.2d 1241 (9th Cir. 1983)","url":"https://www.courtlistener.com","weight":"binding_circuit","note":"5-factor test"},
    {"authority_type":"TaxCt","citation":"Hamacher v. Commissioner, 94 T.C. 348 (1990)","url":"https://www.ustaxcourt.gov","weight":"judicial","note":"Convenience-of-employer 3-test"},
    {"authority_type":"TaxCt","citation":"Sinopoli v. Commissioner, T.C. Memo. 2023-105","url":"https://www.ustaxcourt.gov","weight":"judicial","note":"Augusta Rule rate-and-purpose challenge"},
    {"authority_type":"TaxCt","citation":"Sean McAlary Ltd., Inc. v. Commissioner, T.C. Sum. Op. 2013-62","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Eller v. Commissioner, 77 T.C. 934 (1981)","url":"https://www.ustaxcourt.gov","weight":"judicial","note":"Family employment substance"}
  ]
}
```
