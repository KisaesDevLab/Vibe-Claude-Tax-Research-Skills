# Strategy cross-reference matrix (extended addendum library, #8–#94)

Documents how the extended-library strategies interact: which
combine well, which conflict, and which are mutually exclusive.
Strategies #1–#7 from the addendum's Part 1 were not delivered;
their rows below are retained for navigability but the underlying
detail files do not exist. The dispatcher and the
`planning-strategy-library` skill rely on this matrix to surface
combinations and conflicts when a user combines strategies.

## Format

For each strategy ID:

- **Combines with:** strategies that complement and stack benefits.
- **Conflicts with:** strategies that cannot be used simultaneously,
  or where one significantly reduces the benefit of the other.
- **Mutually exclusive with:** alternative paths to the same goal
  — choosing one means not choosing the other.

## Note on slug renumbering

For the four collisions where the addendum's slug matches an
existing curated strategy file, the addendum versions live at
`<slug>-extended.md`:

- `cost-segregation-extended.md` (addendum #41)
- `real-estate-professional-extended.md` (addendum #20)
- `section-1202-qsbs-extended.md` (addendum #43)
- `backdoor-roth-extended.md` (addendum #72)

The addendum's internal cross-references in those four cases have
been rewritten to point at the `-extended` variant. The existing
curated entries at the bare slug remain authoritative for the
short-form planning catalog.

## Cross-reference table

| ID | Strategy | Combines with | Conflicts with | Mutually exclusive with |
|---|---|---|---|---|
| 1 | 1031 Like-Kind Exchange *(addendum Part 1 not delivered)* | #25, #41, #92 | #29 (DST), #30 (loss recognition) | #33 (installment), #34 (QOZ), #67 (§121) |
| 2 | Accountable Plan / Home Office *(addendum Part 1 not delivered)* | #4, #5, #22, #23 | None | #84 (Schedule C direct deduction) |
| 3 | Active Participation in RE *(addendum Part 1 not delivered)* | #25, #41 | None directly | #20 (REPS — superior path) |
| 4 | Business Vehicle Usage *(addendum Part 1 not delivered)* | #2, #12, #22, #23 | None | #85 (SE variant) |
| 5 | Cell Phone *(addendum Part 1 not delivered)* | #2, #22 | None | None |
| 6 | Day Trader / §475(f) *(addendum Part 1 not delivered)* | None | §1411 NIIT (§475 income still NII for non-trade) | None |
| 7 | ESOP *(addendum Part 1 not delivered)* | #21 reasonable comp | §409A interaction | None |
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

## Common strategy combinations (positive)

**Real Estate Professional power stack.** #20 REPS + #41 cost
segregation + #12 §168(k) bonus + #9 grouping aggregation + #19
§199A QBI safe harbor (Notice 2019-07). Result: large first-year
depreciation deductions offsetting W-2 income.

**S corp owner standard package.** #86 S corp election + #21
reasonable comp + #10 health insurance + #2 accountable plan +
#82 Solo 401(k) + #75 401(k) deferral + #19 §199A QBI. Result:
optimized SE-tax savings with full benefit package.

**Charitable bunching.** #54 DAF (year of bunch) + #51 appreciated
stock + #32 capital gain offset + standard deduction (off-years).
Result: itemize benefit in bunch year; standard deduction in
off-years.

**High-net-worth estate plan.** #46 gifting stock (annual + lifetime
exclusion) + #55 FLP (with bona fide substance) + #54 DAF
charitable component + #57 529 grandparent funding. Result: wealth
transfer with valuation discounts and charitable / education goals.

**Self-employed retirement maximization.** #82 Solo 401(k)
(employee deferral + profit sharing 20%) + #72 Mega Backdoor Roth
(after-tax) + #79 Roth IRA + #73 Defined Benefit (older owners).

**Short-term rental strategy.** #26 STR + material participation +
#41 cost segregation + #69 NIIT exclusion + #19 §199A. Result:
real estate losses against W-2 income without REPS qualification.

**Family employment stack.** #94 Hiring kids SE (or #49 corporate)
+ #79 Roth IRA child + #11 HRA family medical + #50 Spouse
employment.

## Red-flag combinations (conflicts)

- **Notice 2013-54 violations.** #11 standalone HRA + individual
  health insurance reimbursement (without QSEHRA / ICHRA / EBHRA)
  → §4980D $100/day per employee penalty.
- **Wash-sale combinations.** #32 tax-loss harvesting + replacement
  security purchase within 30 days → §1091 disallowance. RSU vest +
  same-day employer-stock ESPP purchase → potential §1091.
- **Self-rental trap.** #16 PIG + property leased to taxpayer's
  own active business → Reg. §1.469-2(f)(6) recharacterizes income
  as nonpassive, defeating PIG purpose.
- **§408(d)(2) pro-rata trap.** #72 Backdoor Roth + existing
  Traditional / SEP / SIMPLE IRA balance → pro-rata taxation of
  conversion.
- **§101(j) failure.** #44 Corporate-Owned VUL without notice and
  consent → death benefit ordinary income.
- **§6707A reportable transaction.** #29 Deferred Sales Trust
  without Form 8886 → $10K–$100K penalty. #52 Charitable LLC
  variants matching reportable transaction → same.
- **§469(c)(7)(A) election forgotten.** #20 REPS + multiple rentals
  without aggregation election → each rental tested separately for
  material participation; typically fails.
- **§1244 documentation missed.** #30 Worthless stock ordinary loss
  claim without §1244 designation at issuance → capital loss only.

## Mutually exclusive paths to same goal

**Capital-gain deferral.** #1 §1031 (real estate only); #33 §453
installment sale; #34 §1400Z-2 QOZ; #29 DST [AGGRESSIVE — avoid].
Choose ONE per gain transaction.

**Charitable giving.** #51 direct appreciated stock; #54 DAF;
#78 QCD (IRA owners 70½+); various trust structures (#53 umbrella);
#52 Charitable LLC [AGGRESSIVE — avoid]. Different vehicles for
different gifts; multiple may be used but each gift uses one path.

**Retirement plan choice (no employees).** #76 SEP-IRA (simple);
#82 Solo 401(k) (deferral capacity); #73 Defined Benefit / Cash
Balance (highest contributions for older owners). Generally choose
ONE primary plan; layering is permitted (Solo 401(k) + DB).

**Roth contribution paths (high income).** #79 direct Roth IRA (if
MAGI permits); #72 Backdoor Roth (if pro-rata permits); #80 Roth
conversion; #75 Roth 401(k) deferral; Mega Backdoor via #72 / #82.
Multiple paths can be combined; pro-rata rule limits Backdoor.

**Real estate passive-loss path.** #20 REPS (full nonpassive
treatment); #3 active participation $25K offset (under-threshold);
#26 STR with material participation (alternative to REPS); #16 PIG
(loss absorption via passive income generation); #9 grouping (loss
release through aggregated material participation).

**S corp election timing.** #86 election by 2 mo 15 days into
target year (Form 2553); late election under Rev. Proc. 2013-30.
Choose effective year carefully — affects entire year of operations.

## Strategy selection decision support

When a user selects a primary strategy:

1. **Surface "Combines with"** as recommended additions.
2. **Surface "Conflicts with"** as warnings before the user can
   select the conflicting strategy.
3. **Surface "Mutually exclusive with"** when the user attempts to
   add an alternative path.

The strategy detail files at
`skills/planning-strategy-library/references/strategies/<slug>.md`
contain the full mechanics, authority chain, citations, and
documentation requirements for each entry. The accompanying
`strategy-relationships.json` provides the matrix in machine-
readable form.
