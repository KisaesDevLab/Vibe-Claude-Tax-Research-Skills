# Schedule C / SE strategy map — long-form

Long-form treatment of the ten strategies in
`schedule-c-strategy-catalog`, mapped to specific Schedule C and
Form 8829 lines. **2025 / 2026 figures are post-OBBBA; verify
annual indexing before relying.**

Source-of-record indexed values (2025 → 2026 where known):

- Standard deduction (single): $15,750 → $16,100.
- §179 deduction limit: $2,500,000 (verify 2026 Rev. Proc.).
- §179 phase-out: $4,000,000.
- §179(b)(5) SUV cap: $31,300 → $32,000.
- §280F luxury auto cap (Year 1 with bonus): $20,200 (verify Rev.
  Proc. annually).
- Standard mileage rate: 70¢/mile (2025; verify 2026 Notice).
- Social Security wage base: $176,100 → $184,500.
- QSEHRA single: $6,150; family: $12,450 (verify 2026 Rev. Proc.).
- §168(k) bonus: 100% for property acquired after 1/19/2025 per
  OBBBA — verify against Classification Tables.

---

## D1. §105 HRA spouse-employee health plan (Line 14)

Sole prop hires spouse as bona fide employee; spouse becomes
employee covered by §105 self-insured medical-reimbursement plan
that reimburses family medical expenses (employee + spouse +
dependents = the proprietor and family). Premiums and direct
medical expenses are deductible to the sole prop and excluded from
the spouse-employee's income.

**Authority:** §105(b), §162(a), Rev. Rul. 71-588, PLR 9409006,
Notice 2013-54 (ACA standalone-HRA prohibition for 2+ employees),
Notice 2015-17 (single-employee HRA permanent transition relief).

**Single-employee rule.** Notice 2015-17 preserves §105 HRAs only
for one-employee employers. Hiring a second employee triggers the
ACA market reforms and the §4980D excise tax ($100/day per
employee). For multi-employee plans, structure as ICHRA, QSEHRA,
or EBHRA.

**Mechanics:**

1. Written §105 plan document, board / sole-prop resolution.
2. Spouse hired as bona fide employee with W-2 wages, time
   records, real work, reasonable wage.
3. Family enrolled in marketplace or other compliant coverage in
   spouse's name.
4. Sole prop reimburses §213(d) medical expenses to spouse with
   substantiation.
5. Deduct on Schedule C Line 14; exclude from spouse's income
   under §105(b).
6. PCORI fee (~$3.47/covered life) due annually via Form 720.

**Detail file:** `hra-merp.md`.

---

## D2. Employ your child (Line 26 wages + Line 23 taxes)

Sole prop / SMLLC default / parent-only partnership employs child to
perform legitimate, age-appropriate work. The child's earned income
is taxed at the child's bracket (often $0 within the standard
deduction). The §3121(b)(3)(A) FICA exemption applies for children
under 18; the §3306(c)(5) FUTA exemption applies for children
under 21.

**Entity-by-entity FICA / FUTA matrix:**

| Employer | FICA < 18 | FUTA < 21 |
|---|---|---|
| Sole proprietorship | EXEMPT | EXEMPT |
| Single-member LLC (default) | EXEMPT | EXEMPT |
| Partnership where ALL partners are parent | EXEMPT | EXEMPT |
| Partnership with non-parent partner | NOT exempt | NOT exempt |
| S corporation | NOT exempt | NOT exempt |
| C corporation | NOT exempt | NOT exempt |
| LLC taxed as S/C corp | NOT exempt | NOT exempt |

**Substance.** *Eller v. Commissioner*, 77 T.C. 934 (1981);
*Denman v. Commissioner*, 48 T.C. 439 (1967). Bona fide work,
age-appropriate, reasonable wage. $5–15/hour for clerical work is
defensible; $50/hour to stuff envelopes is not.

**Stack:** child's wages within the $15,750 (2025) standard
deduction → $0 federal income tax; child can fund a Roth IRA up
to the lesser of earned income or the §408A annual limit; parent's
Schedule C net earnings reduced by the same amount, reducing both
income tax and SE tax bases.

**Pitfalls.** 1099 misclassification eliminates the FICA exemption
and triggers SE tax on the child. Document W-4, I-9, time records,
payroll register, W-2; pay into the child's own bank account.
Coordinate state child labor laws.

**Detail file:** `hiring-kids-self-employed.md`.

---

## D3. Employ your spouse (Lines 26 + 14)

Sole prop employs spouse to provide legitimate services. Two
parallel benefits: (1) §105 HRA family medical (D1), and (2)
reasonable W-2 wages deductible on Schedule C.

**FICA tradeoff.** Unlike children under 18, **spouse wages ARE
subject to FICA**. Schedule C net earnings would be subject to
15.3% SE tax anyway (with ½ deduction), so the FICA cost is
roughly a wash. The optimization is to pay the **minimum
reasonable wage** to qualify the spouse as a bona fide employee
(typically $5,000–$15,000/year) and maximize the §105 HRA medical
reimbursements (no FICA on medical reimbursements).

**Pitfalls.** Bona fide employment required (substance over form);
joint vs. separate accounts (commingled cash flows make
substantiation difficult); spouse becomes wage employee for
program-eligibility / SS earnings purposes.

**Detail files:** `wages-spouse-parents.md`, `hra-merp.md`.

---

## D4. Rent from your spouse — Schedule E SE tax avoidance (Line 20a/20b)

Sole prop rents office space, equipment, vehicles, or real property
**from spouse** at FMV. Rental income reported on **Schedule E**
by the spouse (real property) or as personal-property rental income
(Form 1040 Schedule 1) — Schedule E real-property rental income is
NOT subject to SE tax under §1402(a)(1). The proprietor deducts the
rent on Schedule C (reducing SE tax base).

**Critical: *Bobo v. Commissioner*, T.C. Memo. 1989-329** and
**CCA 202151005**. If "services usually or customarily provided"
(housekeeping, daily linens, meals, on-call concierge) accompany
the rental, the income is recharacterized as Schedule C trade or
business → SE-taxable.

| Service Level | Schedule | SE Tax |
|---|---|---|
| Pure rental (utilities, repairs only) | E | No |
| Substantial services (hotel-like) | C | Yes |

**§469 self-rental rules.** Treas. Reg. §1.469-2(f)(6)
recharacterizes net rental income from self-rented property to
non-passive when leased to a trade or business in which the
taxpayer materially participates. Spouse-to-spouse rental — each
spouse is a separate taxpayer for §469 per Reg. §1.469-1T(j) — so
self-rental rules can apply, and the §1402 SE analysis operates
independently.

**Personal property only.** Non-real-estate rentals are SE-taxable
under §1402(a)(1) UNLESS leased *with* real estate. Equipment-only
rentals to a spouse may be SE-taxable to the spouse.

**Mechanics:**

1. Spouse owns the asset in own name.
2. Written lease at FMV (3 comparable rate quotes).
3. Sole prop pays rent — separate transaction, business → spouse's
   personal / rental account.
4. Spouse reports rent on Schedule E (real property) or Form 1040
   Schedule 1 Line 24b (personal-property rental).
5. Sole prop deducts on Schedule C Line 20a (vehicles/equipment)
   or 20b (other business property).

**Detail file:** `split-entity-operations-vs-re.md` (operating-vs-RE
split logic; spouse-rental is the family-version).

---

## D5. Home office — Schedule C (Line 30 via Form 8829)

Sole prop deducts home office expenses **directly** on Form 8829
(actual-expense method) or via the simplified method on Schedule C
Line 30. No accountable plan needed — there is no employer-employee
distinction.

**Two methods:**

| Feature | Actual Expense (Form 8829) | Simplified Method |
|---|---|---|
| Calculation | % × actual expenses | $5 × sq ft (max 300 sq ft = $1,500) |
| Form | Form 8829 | Schedule C Line 30 only |
| Depreciation | 39-year straight-line | None |
| Carryover (excess) | Yes | None |
| §1250 unrecaptured gain on sale | Yes (max 25% per §1(h)(6)(A)) | No |
| Maximum deduction | Unlimited (subject to §280A net income limit) | $1,500/year |

**Critical post-1999 rule.** Having an outside office does NOT
disqualify the home office, provided (1) home office used
exclusively/regularly for **administrative or management**
activities AND (2) no other fixed location used for substantial
administrative work. (Taxpayer Relief Act of 1997 §932 effectively
overrode *Commissioner v. Soliman*, 506 U.S. 168 (1993), for tax
years beginning after Dec. 31, 1998.)

**Synergy with vehicle deduction (D7).** When the home office
qualifies as principal place of business, trips from home to
customer/client locations become business miles rather than
non-deductible commuting.

**Pitfalls.** Exclusive use violation; regular use violation;
§121 home-sale interaction (depreciation recaptured as
unrecaptured §1250 gain at sale); §280A(c)(5) net income
limitation; state non-conformity (NY, NJ, CA particularly).

**Detail file:** `home-office-deduction-self-employed.md`.

---

## D6. §132(e) de minimis fringe benefits (Line 14)

Occasional, low-value, administratively impracticable-to-account-for
items provided to employees: holiday gifts (non-cash), occasional
meals, occasional coffee/snacks, occasional event tickets (theatre /
sporting events), occasional birthday/holiday parties.

**Authority:** §132(e); Reg. §1.132-6.

**Excluded from §132(e):** cash and cash equivalents (always wages,
no matter how small); regular meal allowances; season tickets;
items exceeding the de minimis threshold.

For a sole prop's own benefits, the §132(e) framework does not
apply (the sole prop is not an "employee" of itself); items go on
the line appropriate to their category (meals — Line 24b at 50%;
office supplies — Line 22).

---

## D7. Heavy vehicle + home office combo (Line 9)

Heavy vehicle (>6,000 lbs GVWR) qualifies for §179 expensing up to
the §179(b)(5) SUV cap ($31,300 in 2025; $32,000 in 2026) plus
§168(k) bonus depreciation (100% post-1/19/2025 acquisitions per
OBBBA). When combined with a qualifying home office under
post-1999 §280A(c)(1), the home becomes the principal place of
business — eliminating commuting miles and pushing business-use
percentage to ~95%+ in many cases.

**Standard mileage vs. actual expense.** The standard mileage
method (70¢/mile for 2025) precludes §179 / bonus on the same
vehicle in the year placed in service; actual-expense method is
required for the heavy-vehicle combo. Year-1 lock-in: choosing
actual-expense in Year 1 forecloses standard mileage in later
years for that vehicle.

**§280F luxury auto cap.** Vehicles ≤ 6,000 lbs GVWR are subject
to §280F; the heavy-vehicle threshold is the basis for the carve-
out. Pickup with 6+ ft cargo bed not subject to SUV cap (Notice
2018-59).

**Detail file:** `business-vehicle-self-employed.md`.

---

## D8. Domestic travel — majority-of-days rule (Line 24a)

Reg. §1.162-2(b): if **more than half** of the trip days are
business, **100% of transportation** (airfare, train, etc.) is
deductible. Lodging and 50% of meals deductible for **business
days only**. Personal-day expenses (lodging, meals) on personal
days are not deductible. Standby / transit days count as business
days.

**Substantiation.** §274(d) requires time, place, business
purpose, and amount.

**Detail file:** `accountable-plan-self-employed.md`.

---

## D9. Foreign travel — §274(c) 7-day / 25% rule (Line 24a)

§274(c) and Reg. §1.274-4 add tighter foreign-travel rules:

- **Foreign trip < 7 days outside the U.S.** (count travel-day to
  travel-day excluding the day of departure): 100% of
  transportation deductible without allocation, even with mixed
  business / personal days.
- **Foreign trip ≥ 7 days** AND personal time ≥ 25% of total
  days: allocation required between business and personal days
  for transportation.
- **Foreign trip ≥ 7 days** AND personal time < 25%: no
  allocation; 100% transportation deductible.

**Detail file:** `accountable-plan-self-employed.md`.

---

## D10. Cell phone — non-compensatory business reasons (Line 25 / Line 18)

Sole prop deducts business-use percentage of cell-phone expense.
For employee-provided phones (e.g., spouse-employee under D3),
**Notice 2011-72** treats employer-provided phones as a §132(d)
working-condition fringe with no allocation required when provided
primarily for non-compensatory business reasons (need to contact
employee at all times; need for availability away from office;
client time-zone differences). The phone may be used personally;
full cost remains deductible.

---

## Annual workflow triggers

For each Schedule C engagement, prompt practitioner with:

1. **D1 / D3 — Spouse strategies.** Married? Spouse covered by
   another employer plan? Anticipated family medical?
2. **D2 — Child employment.** Children of working age? Legitimate
   work? Sole-prop / SMLLC default / parent-only-partnership entity?
3. **D4 — Spouse rental.** Spouse owns business-used real estate /
   equipment / vehicles?
4. **D5 — Home office.** Use home for business? Other office?
5. **D7 — Heavy vehicle + home office combo.** Vehicle GVWR > 6,000
   lbs? Home office qualifies as principal place of business?
6. **D8 / D9 — Travel.** Domestic or foreign? Days breakdown?

## State conformity review

States with material non-conformity:

- **California** — no §168(k) bonus; ADS depreciation; §105 HRA
  conforms but ACA reform interaction varies; AB5 ABC test for
  worker classification.
- **New York** — IT-225 modifications for federal bonus
  depreciation; convenience-of-employer rule for non-resident
  remote workers.
- **Massachusetts** — no bonus depreciation conformity; 4% surtax
  over $1M.
- **Hawaii, Minnesota** — partial conformity to bonus.
- **AK / FL / NV / SD / TN / TX / WA / WY** — no individual income
  tax (income-tax non-conformity moot; sales/use and franchise /
  B&O still apply).

## Cross-references

- `predict-qbi-eligibility` — §199A interaction across most
  Schedule C income.
- `predict-real-estate-pro` — D4 spouse-rental can interact with
  §469.
- `tax-research-state-income` — per-state non-conformity.
- `irc-section-lookup` + `shared/legislation-tracking.md` — OBBBA
  Public-Law-to-USC verification.
