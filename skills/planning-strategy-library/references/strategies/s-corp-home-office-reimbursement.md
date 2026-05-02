---
name: "S Corporation Home-Office Deduction via Accountable Plan Reimbursement"
slug: s-corp-home-office-reimbursement
type: Reimbursement Strategy
tax_type: Income / SE
complexity: Moderate
irc_sections: ["§280A", "§280A(c)(1)", "§280A(c)(6)", "§62(a)(2)(A)", "§62(c)", "§162(a)", "§1(h)(6)(A)"]
treas_regs: ["Reg. §1.62-2(c)", "Reg. §1.62-2(d)(1)", "Reg. §1.62-2(e)-(g)", "Reg. §1.280A-2(g)", "Prop. Reg. §1.280A-2"]
forms: ["Form 1120-S", "Form 1040 Schedule A", "Form 1040 Schedule E"]
state_specific: true
caution: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

# S Corporation Home-Office Deduction via Accountable Plan Reimbursement

> **Bottom line:** For S corp owner-employees, the **only**
> defensible way to capture the home-office deduction is the
> **accountable-plan reimbursement** method. Renting the office to
> the corporation produces a $0 net benefit (because §280A(c)(6)
> disallows offsetting deductions against the rental income), and
> Form 2106 employee-expense treatment is unavailable for tax
> years 2018-2025 under TCJA §67(g) suspension of miscellaneous
> itemized deductions (and even when available, was hobbled by the
> 2%-of-AGI floor, the AMT add-back, and the requirement to
> itemize).

## Why the alternatives fail

### Why renting to the corporation produces $0 benefit

Under §280A(c)(6), an **employee** who rents a portion of a dwelling
unit to their employer **cannot** claim deductions allocable to the
rental use that exceed the rental income. Effect:

1. Owner-employee receives rental income on **Schedule E**.
2. Schedule E income is offset only to the extent of mortgage
   interest and property tax already deductible elsewhere (and
   those are simply moved from Schedule A to Schedule E — net
   zero).
3. **No deduction allowed** for utilities, insurance, repairs,
   depreciation allocable to the rented portion.
4. The S corp deducts the rent paid; the owner reports income
   that nets to zero after allocable interest/taxes — but
   crucially, the owner-employee **cannot** apply the home-office
   §280A(c)(1) exception because §280A(c)(6) **specifically
   carves out** employee-to-employer rentals from the (c)(1)
   regular-and-exclusive-use deduction.

**Authority:** §280A(c)(6) ("Treatment of rental to employer.
Paragraphs (1) and (3) shall not apply to any item which is
attributable to the rental of the dwelling unit (or any portion
thereof) by the taxpayer to his employer during any period in
which the taxpayer uses the dwelling unit (or portion) in
performing services as an employee of the employer.").

**Cases on rental-to-employer trap:**

- *Leslie A. Roy v. Commissioner*, T.C. Memo. 1998-125 — confirmed
  §280A(c)(6) bar on employee-to-employer rental deductions.
- **PLR 8819009** — IRS internal analysis of §280A(c)(6).
- **CCA 200121070** — IRS Chief Counsel Advice; an accounting-
  firm partner's above-market rental from his firm did not
  create §280A(c)(1) deductibility because of §280A(c)(6).
- Note: At the **S corporation entity level**, §280A(c)(6) does
  NOT disallow the corporation's §162 rent expense (per CCA
  200121070); the disallowance applies only at the
  employee/shareholder level.

### Why Form 2106 fails for 2018-2025

The Tax Cuts and Jobs Act (TCJA) added **§67(g)**, which suspends
**all miscellaneous itemized deductions** (those subject to the
2%-of-AGI floor) for tax years **2018 through 2025**. Form 2106
unreimbursed employee business expenses (including the home-
office portion) are miscellaneous itemized deductions — therefore
**NOT deductible** for years 2018-2025 even if they otherwise
qualify. **Status post-2025:** Without further legislation, §67(g)
sunsets after 2025; OBBBA `[CITATION NEEDED — search: OBBBA §67(g)
miscellaneous itemized deductions Pub. L. 119-21]` should be
verified for any extension or modification.

Even after §67(g) sunsets, three pre-TCJA structural problems
remain:

1. **Itemize-or-lose.** The deduction is available only if the
   employee itemizes — most do not.
2. **2%-of-AGI floor.** Reduces the deduction by 2% of AGI.
3. **AMT add-back.** Miscellaneous itemized deductions are AMT
   preferences — taxpayers in AMT lose them entirely.

## The accountable-plan reimbursement method

### Statutory framework

- **§62(a)(2)(A)** — reimbursements of employee business expenses
  under an accountable plan are **excluded from the employee's
  gross income** (specifically, treated as not "wages" subject
  to wage withholding).
- **§62(c)** — defines "reimbursement or other expense allowance
  arrangement" for purposes of this exclusion.
- **Reg. §1.62-2(c)(1)** — an arrangement is an "accountable
  plan" only if it satisfies: (1) **business connection**, (2)
  **substantiation**, and (3) **return of excess** within
  reasonable time.
- **Reg. §1.62-2(d)(1)** — the corporation gets the full
  deduction for the reimbursed amount on its return as if it had
  incurred the expense directly.
- **Reg. §1.62-2(e)** — substantiation must be within reasonable
  time (60 days/120 days safe harbors under Reg. §1.62-2(g)).

### Why the home office qualifies for reimbursement

Reg. §1.62-2(c)(2) defines reimbursable expenses to include
amounts paid by the employee in connection with the performance
of services and that satisfy the requirements of part VI,
subchapter B, chapter 1 (i.e., §§161 through 199) — which
includes **§162 (trade or business expenses)**, **§167
(depreciation)**, and **§280A(c)(1)** (the home-office exception
for employees).

Critically, **§280A(c)(1)** (the home-office exception) applies
to "an employee" only if **all** of these are satisfied:

1. **Exclusive use** of the home office for trade or business.
2. **Regular use** of the office.
3. The home office is the **principal place of business** OR a
   place where the employee meets clients/customers in the
   normal course of business OR a separate structure used for
   business.
4. The exclusive use is **for the convenience of the employer**
   (and not merely "appropriate and helpful").

Once the §280A(c)(1) requirements are satisfied, the home-office
expenses become **§162 / §167 trade-or-business expenses** that
the employer (S corp) may reimburse under an accountable plan
(Reg. §1.62-2(c)(2)(ii)), excluding them from the employee's
income (§62(a)(2)(A)) and giving the corporation a §162
deduction.

### "Convenience of the employer" — the operational test

The phrase "for the convenience of the employer" (§280A(c)(1)
flush language) is **not** statutorily defined. The Tax Court's
operative tests are drawn from:

- **Hamacher v. Commissioner, 94 T.C. 348 (1990)** — the
  foundational case on convenience-of-employer in the home-office
  context. Hamacher established three alternative tests:
  1. The home office is **maintained as a condition of
     employment**.
  2. The home office is **necessary for the functioning of the
     employer's business**.
  3. The home office is **necessary to allow the employee to
     properly perform** their duties.
- **Sharon v. Commissioner, 66 T.C. 515 (1976), aff'd 591 F.2d
  1273 (9th Cir. 1979)** — established that home office for the
  employee's "personal convenience, comfort, or economy" does
  **NOT** satisfy the test.
- **Cadwallader v. Commissioner, T.C. Memo. 1989-356** — applied
  Hamacher tests to deny a university professor's home-office
  deduction.
- **Soliman v. Commissioner, 506 U.S. 168 (1993)** — Supreme
  Court "principal place of business" test; subsequently
  modified by the **1997 amendment** to §280A(c)(1) which added
  the safe harbor that "principal place of business" includes
  any place used for **administrative or management activities**
  if there is no other fixed location where the taxpayer
  conducts substantial administrative or management activities.

For an S corp owner-employee, satisfying convenience-of-employer
is straightforward — the owner essentially makes the rules of
employment, and a written board / shareholder resolution
formalizing that the home office is required as a condition of
employment establishes the requirement decisively.

### Reimbursable expenses

Under the accountable plan, the corporation reimburses the
**business-use percentage** of:

- **Mortgage interest** (or rent if leased).
- **Real estate taxes** allocable to the home.
- **Utilities** — electric, gas, water, sewer, trash.
- **Homeowner's insurance**.
- **Repairs and maintenance** allocable to the home (or
  specifically to the office if direct).
- **Depreciation** on the structure (39-year straight-line for
  business portion; calculated based on lower of cost or FMV at
  time first used for business; land excluded).
- **HOA dues** allocable to the home.
- **Security system** (allocable portion).
- **Snow removal, lawn care** (if home use is primary basis;
  generally not allocable for home office unless directly
  business-related).
- **Internet and home phone** allocable portion (often 100%
  business if separately metered).

**Business-use percentage** is calculated as:

- **Square-footage method:** Square footage of office ÷ Total
  square footage of home.
- **Number-of-rooms method:** Number of rooms used as office ÷
  Total rooms (rooms must be of approximately equal size for
  this to apply).

### Required substantiation

Reg. §1.62-2(e)(2) requires substantiation under Reg. §1.274-5
standards. For the home office, this means:

1. **Photo or floor plan** showing the office space and
   exclusive use.
2. **Square footage measurement** of office and total home.
3. **Receipts/invoices** for all expenses being reimbursed
   (utility bills, insurance bills, mortgage statement, property
   tax bill).
4. **Calculation worksheet** showing the business-use percentage
   and the allocable amounts.
5. **Annual statement of exclusive and regular use, and
   convenience-of-employer.**

### Critical: the simplified method does NOT apply

The **§280A simplified method** ($5/sq.ft. up to 300 sq.ft. =
$1,500 max) is available **only to taxpayers who are individuals
filing Schedule C, Schedule E, or Schedule F**, per IRS Rev. Proc.
2013-13. **It does NOT apply to S corp accountable plan
reimbursements.** The S corp must use the **actual expense
method**.

## Implementation steps

### Step 1: Adopt a written accountable plan

A board / shareholder resolution adopting the accountable plan,
referencing Reg. §1.62-2 and listing categories of reimbursable
expenses (including home-office expenses). Should be in place at
the **start** of the tax year (or before reimbursements begin).

### Step 2: Create a home-office substantiation packet

Annual packet from the owner-employee to the corporation
including:

1. **Photo and/or floor plan** of the home office.
2. **Square footage measurement** (office and total home).
3. **Statement of exclusive and regular use** signed by owner-
   employee.
4. **Convenience-of-employer statement** referencing one or more
   Hamacher tests:
   - Office maintained as a condition of employment (cite board
     resolution).
   - Office necessary for the corporation's business
     functioning.
   - Office necessary for owner-employee to properly perform
     duties.
5. **Updated annually** (or whenever facts change).

### Step 3: Submit periodic expense reports

Owner-employee submits expense reports (monthly, quarterly, or
annually) listing reimbursable home-office expenses with
supporting documentation. Corporation reimburses on a regular
schedule (not as a year-end lump sum suggesting backdating).

### Step 4: Corporation deducts on Form 1120-S

The reimbursed home-office expenses are deducted on Form 1120-S
**"Other deductions"** (Line 19) with a label such as **"Office
space"** or **"Home office reimbursement"**. The deduction reduces
ordinary business income passed through to the shareholder on
Schedule K-1.

### Step 5: Coordinate Schedule A reporting

Critical coordination: the owner-employee personally claims
mortgage interest and real estate taxes on Schedule A — but
**must reduce** the Schedule A amount by the portion that was
reimbursed by the corporation. Failure to reduce results in
**double-counting** of the deductions.

### Step 6: Track depreciation carefully

The corporation reimburses depreciation as an employee business
expense, but the owner-employee must:

1. Track the depreciation (39-year straight-line, MACRS) in a
   personal home-basis schedule.
2. **Reduce the home's basis** by the depreciation reimbursed,
   for purposes of computing gain on eventual sale.
3. At sale, the depreciation portion is subject to
   **unrecaptured §1250 gain** (taxed at up to **25%** under
   §1(h)(6)(A)) — separate from the §121 home-sale exclusion of
   $250,000 / $500,000 (which excludes only the gain in excess
   of depreciation recapture).

## Sample documents

### Accountable plan resolution

```
[CORPORATION NAME] — ACCOUNTABLE PLAN RESOLUTION

Resolved: [Corporation Name] hereby adopts an accountable plan,
effective [DATE], pursuant to Treas. Reg. § 1.62-2, for the
reimbursement of employee business expenses incurred by employees
in the performance of their duties for the corporation.

Reimbursable categories include, but are not limited to:
  (1) Travel, meals, and lodging while away from home on
      corporation business;
  (2) Local transportation and vehicle expenses (mileage or
      actual);
  (3) Home office expenses qualifying under § 280A(c)(1)
      (regular and exclusive use; principal place of business
      or administrative-or-management home-office under
      § 280A(c)(1)(A); for the convenience of the corporation);
  (4) Communications expenses (cellular, internet);
  (5) Office supplies and equipment;
  (6) Other ordinary and necessary § 162 expenses incurred in
      performance of duties.

Substantiation: Employees must submit expense reports within
60 days after expenses are incurred, accompanied by receipts and
records sufficient to satisfy Reg. § 1.274-5. Expenses must
state amount, time, place, and business purpose.

Return of excess: Any reimbursement in excess of substantiated
expenses must be returned within 120 days.

Authorized by:    _____________________________   Date: ______
Title:           _____________________________
```

### Home-office annual statement

```
HOME OFFICE STATEMENT — TAX YEAR ____

Employee: _________________________________
Employer: _________________________________
Home Address: _____________________________

Office Description: _______________________________________________
Office Square Footage: ________________
Total Home Square Footage: ________________
Business Use Percentage: ________________%

Exclusive Use (initial): I hereby certify that the above-described
office space is used regularly and exclusively for the business
of [Corporation Name]. _______ (Initials)

Convenience-of-Employer (check all applicable):
   ☐ Maintained as a condition of my employment with [Corporation
     Name] (per board resolution dated ________).
   ☐ Necessary for the functioning of [Corporation Name]'s
     business.
   ☐ Necessary to allow me to properly perform my duties as an
     employee of [Corporation Name].

The home office is NOT maintained "purely as a matter of personal
convenience, comfort, or economy."

Hours of business use: ________________ per week.
Type of business activities performed in home office:
___________________________________________________________________
___________________________________________________________________

Photographs / floor plan: ☐ Attached    ☐ On file

Annual reimbursement total: $ ________________

Employee Signature: _________________________  Date: ___________
```

### Expense report worksheet

```
HOME OFFICE EXPENSE REPORT — [PERIOD]

Employee: _________________________________
Tax Year: ____   Period Covered: ____________________

Total Annual Home Expenses (total home, before allocation):

  Mortgage interest:        $ ____________
  Real estate taxes:        $ ____________
  Homeowner insurance:      $ ____________
  Utilities — electric:     $ ____________
  Utilities — gas:          $ ____________
  Utilities — water/sewer:  $ ____________
  HOA dues:                 $ ____________
  Repairs (allocable):      $ ____________
  Depreciation (annual):    $ ____________
  Other: ___________________ $ ____________

Total Home Expenses:        $ ____________
Business Use Percentage:    ____________%
Allocable Business Use:     $ ____________

Expense report submitted with:
   ☐ Utility bills
   ☐ Mortgage statement
   ☐ Property tax bill
   ☐ Insurance declaration page
   ☐ Repair receipts
   ☐ Depreciation schedule

Total Reimbursement Requested: $ ____________

Employee:   _____________________________   Date: ______
Approved:   _____________________________   Date: ______
   (Officer signature)
```

## Common pitfalls

1. **Mid-year accountable-plan adoption.** The accountable plan
   must be in place when reimbursements are made. Retroactive
   adoption raises substance-over-form challenges.
2. **No exclusive use.** The home office must be used **only**
   for business — not as a guest room, kids' homework area, or
   storage for personal items. Any non-business use defeats the
   §280A(c)(1) exception.
3. **Failing to update business-use percentage.** Changes in
   home (additions, finished basement, etc.) or office
   configuration require recomputation.
4. **Double-deducting interest and taxes.** The owner-employee
   personally itemizes on Schedule A — must reduce Schedule A
   by the reimbursed portion to avoid double-deducting. SALT
   $10,000 cap applies.
5. **Not tracking depreciation for basis adjustment.** At sale,
   reimbursed depreciation creates unrecaptured §1250 gain (up
   to 25% federal rate). Maintain schedule.
6. **Year-end lump-sum reimbursement.** Reimbursements made in a
   single year-end lump sum invite scrutiny that the arrangement
   isn't a real accountable plan. Better practice is monthly or
   quarterly.
7. **Conflating with simplified method.** The $5/sq.ft. simplified
   method does NOT apply to S corp reimbursements — must use
   actual expense method.
8. **§121 exclusion confusion.** The home office portion is NOT
   excluded under §121 to the extent of post-5/6/97 depreciation
   reimbursed. Separate calculation of unrecaptured §1250 gain
   required at sale.
9. **State conformity.** California, New York, and other states
   may have separate accountable plan rules or different home-
   office calculations.
10. **Multi-shareholder S corps.** Accountable plan applies to
    each shareholder-employee separately; each must independently
    satisfy §280A(c)(1) and submit own expense reports.

## Tax savings illustration

For a typical S corp owner-employee with home office:

| Annual Home Expenses | Total | × 12% Business Use |
|---|---|---|
| Mortgage interest | $24,000 | $2,880 |
| Real estate taxes | $6,000 | $720 |
| Insurance | $1,500 | $180 |
| Utilities | $4,000 | $480 |
| Repairs | $1,000 | $120 |
| HOA dues | $2,400 | $288 |
| Depreciation (annual) | $5,000 | $600 |
| **Total reimbursable** | | **$5,268** |

Tax savings to owner-employee at 32% federal + 15.3% SE
equivalent through reduced K-1 income (if reasonable comp held
constant): roughly **$1,685 to $2,500** annually depending on
specifics. The owner-employee receives the $5,268 as a non-
taxable expense reimbursement. The corporation deducts the
$5,268 on Form 1120-S, reducing the K-1 income passed to the
shareholder.

The benefit is most powerful when:

- The owner has substantial other home expenses (utilities,
  insurance, HOA) that would otherwise be non-deductible
  personal expenses.
- AGI / SALT phase-outs are reducing Schedule A benefit.
- Combined with the **principal-place-of-business test**, the
  arrangement converts personal commuting miles into deductible
  business travel — see related skill `s-corp-vehicle-personal-
  name`.

## Cross-references to other skills

- `s-corp-vehicle-personal-name` — accountable plan
  reimbursement of vehicle expenses for vehicles titled in
  owner's personal name.
- `accountable-plan-framework` — general framework for
  Reg. §1.62-2 accountable plans.
- `s-corp-strategy-catalog` — Strategy #5 (home office
  reimbursement) within the broader 10-strategy S corp
  catalog.
- `home-office-deduction-schedule-c` — comparable analysis
  for sole proprietors / single-member LLCs (Schedule C).
- `reasonable-comp-corp-owners` — interaction with W-2 wage
  / distribution split.
- `business-vehicle-and-home-office-combo` — using qualifying
  home office to convert commuting miles to deductible
  business miles.

## Authorities (JSON sidecar)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 280A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 280A(c)(1)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute","note":"Home office exception"},
    {"authority_type":"IRC","citation":"I.R.C. § 280A(c)(6)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A","weight":"primary_statute","note":"Bar on employee-to-employer rental deductions"},
    {"authority_type":"IRC","citation":"I.R.C. § 62(a)(2)(A)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section62","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 62(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section62","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 162(a)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1(h)(6)(A)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1","weight":"primary_statute","note":"Unrecaptured § 1250 gain rate cap"},
    {"authority_type":"IRC","citation":"I.R.C. § 67(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section67","weight":"primary_statute","note":"TCJA suspension of misc itemized deductions through 2025"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.62-2(c)","url":"https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFRf6cbb86dec3b4dd/section-1.62-2","weight":"regulation"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.62-2(d)(1)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.62-2(e)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.62-2(g)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation","note":"60/120-day safe harbors"},
    {"authority_type":"TreasReg","citation":"Prop. Reg. § 1.280A-2(g)","url":"https://www.ecfr.gov/current/title-26","weight":"proposed_regulation"},
    {"authority_type":"TaxCt","citation":"Hamacher v. Commissioner, 94 T.C. 348 (1990)","url":"https://www.ustaxcourt.gov","weight":"judicial","note":"Convenience-of-employer 3-test framework"},
    {"authority_type":"TaxCt","citation":"Sharon v. Commissioner, 66 T.C. 515 (1976), aff'd 591 F.2d 1273 (9th Cir. 1979)","url":"https://www.ustaxcourt.gov","weight":"judicial","note":"Personal convenience does not satisfy"},
    {"authority_type":"TaxCt","citation":"Cadwallader v. Commissioner, T.C. Memo. 1989-356","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Leslie A. Roy v. Commissioner, T.C. Memo. 1998-125","url":"https://www.ustaxcourt.gov","weight":"judicial","note":"§ 280A(c)(6) employee-to-employer rental bar"},
    {"authority_type":"SCOTUS","citation":"Commissioner v. Soliman, 506 U.S. 168 (1993)","url":"https://www.supremecourt.gov","weight":"binding_supreme_court","note":"Principal place of business; modified by 1997 § 280A amendment"},
    {"authority_type":"PLR","citation":"PLR 8819009","url":"https://www.irs.gov","weight":"non_precedential_irs","note":"§ 280A(c)(6) analysis"},
    {"authority_type":"CCA","citation":"CCA 200121070","url":"https://www.irs.gov","weight":"non_precedential_irs","note":"§ 280A(c)(6) does not affect S corp's § 162 rent deduction"},
    {"authority_type":"RevProc","citation":"Rev. Proc. 2013-13","url":"https://www.irs.gov","weight":"irs_published","note":"Simplified method for home office (Schedule C/E/F only — not S corp)"}
  ]
}
```
