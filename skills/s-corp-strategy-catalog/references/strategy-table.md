# Form 1120-S strategy map — long-form

Long-form treatment of the ten strategies in `s-corp-strategy-catalog`,
mapped to specific Form 1120-S lines. **2025 / 2026 figures are
post-OBBBA (Pub. L. 119-21, July 4, 2025); verify annual indexing
before relying.**

Source-of-record indexed values:

- Social Security wage base: 2025 = $176,100; 2026 = $184,500.
- §199A QBI thresholds: 2025 MFJ = $394,600; 2025 single = $197,300.
- §179 limit / phase-out: 2025 = $2,500,000 / $4,000,000.
- §179(b)(5) SUV cap: 2025 = $31,300; 2026 = $32,000.
- §168(k) bonus: 100% for property acquired after 1/19/2025
  (post-OBBBA) — verify against Classification Tables.

---

## Strategy #1 — Reduce S corp owner wages (Line 7)

Reduces W-2 wages paid to the shareholder-employee to the lowest
*defensible* amount, shifting the residual to K-1 distributions.
K-1 distributions are not subject to FICA/SE tax. Net SE-tax
savings = (excess wage reduction) × (applicable FICA rate). The
2025 Social Security wage base is $176,100 (above-base wages still
incur the 2.9% Medicare HI plus 0.9% Additional Medicare).

**Critical constraint — reasonable compensation.**

- *Mayson Manufacturing* 9-factor test (1949) and *Elliotts*
  5-factor test (1983) frame the analysis.
- IRS reclassification authority under §7436.
- *Watson v. United States*, 668 F.3d 1008 (8th Cir. 2012);
  *Sean McAlary Ltd., Inc. v. Commissioner*, T.C. Sum. Op. 2013-62.

**§199A interaction.** Above the QBI threshold, the W-2 wage
limitation incentivizes higher wages. Below the threshold, lower
wages and higher K-1 income generally favor the deduction (subject
to specified-service-trade-or-business carve-outs).

**Detail files:** `reasonable-comp-corp-owners.md` and existing
`s-corp-reasonable-comp.md`.

---

## Strategy #2 — Deduct ≥2% shareholder health insurance premiums (Line 7)

S corp pays the premium; premium is added to the shareholder's W-2
Box 1 (income tax) but **excluded from Box 3 / Box 5** (FICA-free
under §3121(a)(2)(B); see Notice 2008-1). On Form 1040 Schedule 1,
the premium is deducted above-the-line under §162(l) as the
self-employed health insurance deduction.

**Net effect:** income-tax neutral; saves 15.3% FICA on the
premium amount.

**Mechanics:**

1. S corp must establish the plan (or premiums paid in the
   corporation's name, or paid personally and reimbursed per
   Notice 2008-1).
2. Box 1 inclusion / Box 3 & 5 exclusion / Box 14 informational.
3. Schedule 1 deduction; cannot exceed earned income from S corp.

**Detail file:** `health-insurance-s-corp.md`.

---

## Strategy #3 — Employ your child (Line 8)

Shifts income from the higher-bracket parent to the lower-bracket
child via legitimate employment. 2025 single standard deduction is
$15,000.

**S corp specific constraint — no FICA exemption.** Unlike
Schedule C / parent-only partnerships (where children under 18 are
exempt from FICA per §3121(b)(3)(A)), wages paid by an S corp to a
child are subject to FICA regardless of age. This significantly
reduces the strategy's S-corp benefit relative to a Schedule C
employer.

**Substance requirements:** *Eller v. Commissioner*, 77 T.C. 934
(1981); *Denman v. Commissioner*, 48 T.C. 439 (1967). Bona fide
work, age-appropriate, reasonable wage, contemporaneous records,
written employment agreement, separate bank account.

**Detail files:** `hiring-kids.md` (SE-corp variant).

---

## Strategy #4 — Sell home to S corp before rental conversion (Line 14)

Before converting a personal residence to rental, the homeowner
sells it to the S corp at FMV. Owner uses §121 to exclude up to
$250K / $500K of gain. S corp's depreciable basis is FMV minus
land allocation — producing larger depreciation deductions than
if the rental conversion happened at original cost basis.

**Critical constraints.**

- §121(d)(11) related-party rules / §1239 ordinary-income
  conversion on the depreciable portion. Allocate between land
  (non-depreciable; §121 gain excluded) and structure
  (depreciable; §1239 risk).
- §121 use-and-ownership tests (2 of 5 preceding years).
- Two-year anti-churning limit on multiple §121 exclusions.
- Substance over form: bona fide arms-length sale (financing,
  escrow, recorded deed, insurance).

**Cases:** *Wendy E. Smith v. Commissioner*, T.C. Memo. 2002-148.

**Detail files:** `primary-home-sale-exclusion.md` (§121) and
`cost-segregation.md` (post-purchase basis treatment).

---

## Strategy #5 — Reimbursement of home office expenses (Line 19)

Owner-employee submits home-office expense reports under an
accountable plan; corporation reimburses business-use percentage of
mortgage interest, property taxes, utilities, insurance, repairs,
depreciation, HOA dues. Reimbursement is non-taxable to the
employee (§62(a)(2)(A); Treas. Reg. §1.62-2) and fully deductible
to the corporation.

**Why the alternatives fail:**

- §280A(c)(6) bars employee-to-employer rentals (no offsetting
  deductions to the employee; PMTA 00431_7138).
- §67(g) suspends miscellaneous itemized deductions (Form 2106)
  through 2025; the deduction is zero on the personal return.

**Authority chain:** §280A(c)(1), §62(a)(2)(A), Treas. Reg.
§1.62-2, *Hamacher v. Commissioner*, 94 T.C. 348 (1990) (3-prong
convenience-of-employer test).

**Detail file:** `s-corp-home-office-reimbursement.md`.

---

## Strategy #6 — Augusta Rule (§280A(g)) home rental (Line 11)

Owner rents the entire home to the S corp for **14 days or fewer**
during the year. Corporation deducts as ordinary §162 business
expense (e.g., board meetings, retreats, training events). Owner
excludes the rental income under §280A(g).

**Absolute constraints.**

- 14-day cliff: a 15th day disqualifies the *entire* exclusion;
  all 15 days become taxable income.
- Rent must be reasonable (§482 / §162). Use comparable hotel
  meeting room or Airbnb/VRBO rates for the locale.
- Documentation: board resolution, written rental agreement,
  comparable-rate evidence, meeting agendas, attendance records.
- 1099-MISC Box 1 reporting from S corp to owner; owner reports
  rental income on Schedule E and claims the §280A(g) exclusion.

**Practitioner trap.** *Sinopoli v. Commissioner*, T.C. Memo.
2023-105 — Tax Court rejected $3,000/day rental for 12 days as
neither a §162 ordinary-and-necessary expense nor reasonable in
amount. Corporation's deduction disallowed; owner still had to
report the rental income.

**Detail file:** `augusta-rule-280a-g.md`.

---

## Strategy #7 — Reimbursement of depreciation (Line 19)

When the owner-employee personally owns business assets (vehicle,
computer, equipment) used for corporate business, the corporation
reimburses the owner for §179, §168(k), and MACRS depreciation
under the accountable plan.

**PLR 200930029 — citable but non-precedential** under §6110(k)(3).
Confirms §179 does not require corporate title; the corporation
must bear the cost (satisfied by reimbursement).

**Detail file:** `corp-vehicle-personal-name.md`.

---

## Strategy #8 — Reimbursement of vehicle expenses (Line 19)

Specific application of #7 to vehicles. Combined with the home
office (#5), the home becomes the principal place of business —
eliminating commuting miles and increasing business-use percentage.

**Heavy SUV + home office combo.** A heavy SUV (>6,000 lbs GVWR)
combined with a qualifying home office produces immediate Year-1
deductions in the $40K–$90K range for typical owner-employees,
respecting the §179(b)(5) SUV cap ($31,300 for 2025; $32,000 for
2026).

**Notice 2018-59** confirms a pickup with a 6+ ft cargo bed is not
subject to the SUV cap.

**Detail file:** `corp-vehicle-personal-name.md`.

---

## Strategy #9 — Reimbursement of travel expenses (Line 19)

Owner-employee submits travel reports under accountable plan;
corporation reimburses transportation, lodging, meals (50% per
§274(n)) tax-free to employee, deductible to corporation.

**Domestic vs. foreign rules:**

- Domestic: if majority of trip days are business, 100% of
  transportation deductible; lodging and 50% meals deductible for
  business days only.
- Foreign < 7 days: 100% transportation deductible regardless of
  mix (§274(c)).
- Foreign ≥ 7 days: allocation between business and personal days.

**OBBBA reversion note:** the COVID-era 100% restaurant-meal
deduction has reverted to 50% for 2023+.

**Detail file:** `reimbursement-business-expenses.md`.

---

## Strategy #10 — Cell-phone working-condition fringe (Line 18)

Corporation provides employee with a smartphone (or reimburses for
personal phone used for business) **primarily for non-compensatory
business reasons**. IRS treats this as a working-condition fringe
under §132(d), excludable from wages.

**Authority:** §132(d); Notice 2011-72; SBSE Memorandum
SBSE-04-0911-083.

**Non-compensatory business reasons test:** need to contact
employee at all times for emergencies; need for availability away
from office; need to speak with clients in different time zones.
The phone may be used for personal purposes; full cost remains
deductible — no allocation required.

---

## Implementation notes

These strategies are typically implemented in combination. The
accountable plan (Treas. Reg. §1.62-2) is the operational backbone
for #5, #7, #8, #9 and supports #10.

**Annual workflow:**

1. **Q1 — Adoption.** Adopt or update accountable plan; establish
   reasonable-comp baseline; verify OBBBA / annual indexing of
   §179, §168(k), QBI thresholds.
2. **Quarterly — Substantiation.** Submit expense reports for home
   office, vehicle, travel, cell phone.
3. **Q4 — Year-end.** Health insurance W-2 inclusion (Box 1
   adjustment by Dec 31); §1377(a)(2) closing-of-books coordination
   if shareholder turnover; §663(b) 65-day rule coordination if
   connected trusts.
4. **Q1 (following year).** Form 1120-S preparation with strategy-
   mapping; verify §199A QBI calculation.

## Cross-references

- `predict-reasonable-comp` — substance check for #1.
- `predict-qbi-eligibility` — §199A interaction for #1, #2.
- `tax-research-state-income` — per-state non-conformity for
  §168(k), §179, §199A.
- `irc-section-lookup` + `shared/legislation-tracking.md` — OBBBA
  Public-Law-to-USC for any post-2024 figure.
- `s-corp-home-office-reimbursement.md`, `corp-vehicle-personal-name.md`,
  `reasonable-comp-corp-owners.md`, `augusta-rule-280a-g.md`,
  `health-insurance-s-corp.md`, `hiring-kids.md`,
  `primary-home-sale-exclusion.md`, `cost-segregation.md`,
  `reimbursement-business-expenses.md` — detail files in
  `skills/planning-strategy-library/references/strategies/`.
