# Vibe CPA Skills — Strategy Library Addendum (94 Strategies)

**Part 3 of 10** — Strategies #18 through #27.

**Part navigation:**
- Part 1: Exec summary, master index, PART A build-plan addendum, strategies #1–#7
- Part 2: Strategies #8–#17
- **Part 3: Strategies #18–#27** ← this file
- Part 4: Strategies #28–#37
- Part 5: Strategies #38–#47
- Part 6: Strategies #48–#57
- Part 7: Strategies #58–#67
- Part 8: Strategies #68–#77
- Part 9: Strategies #78–#86
- Part 10: Strategies #87–#94 + cross-reference matrix

---

## Strategy #18: Prepayment of Expense

**File:** `references/strategies/prepayment-of-expense.md`

```markdown
---
name: "Prepayment of Expense (12-Month Rule)"
slug: prepayment-of-expense
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§461", "§263(a)"]
forms: ["Schedule C / Form 1120-S / Form 1120 / Form 1065"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

The "12-month rule" under Reg §1.263(a)-4(f) allows a cash-basis
taxpayer to deduct certain prepaid expenses in the year of payment
(rather than capitalize and amortize) if the right or benefit does
not extend beyond the earlier of (a) 12 months after the first date
on which the right or benefit begins or (b) the end of the
following tax year.

This is a year-end planning lever: cash-basis businesses can
accelerate deductions by prepaying expenses for the next 12 months
in December. The deduction is allowed in the current year, even
though the benefit is consumed over the following year.

Common applications:
- Insurance (12 months of premiums paid in December for next
  year's coverage).
- Rent (one year's rent paid in advance — but watch §467 deferred
  rent issues for unreasonably front-loaded leases).
- Subscriptions and memberships (annual renewal paid in advance).
- Service contracts (12-month term).

For accrual-basis taxpayers, the analysis is different: economic
performance under §461(h) generally must occur before the deduction
is allowed, regardless of payment. The recurring-item exception
under §461(h)(3) may permit deduction in the year payment is made
even if economic performance occurs in the following year, provided
the item is recurring, the all-events test is met, and the deduction
matches reasonably with income.

## Primary IRC authority

- **§461** — General rule for taxable year of deduction.
- **§263(a)** — Capital expenditures.
- **§446** — Methods of accounting (cash vs. accrual).
- **§448** — Limitations on use of cash method.
- **§461(g)** — Prepaid interest (NOT deductible in advance —
  spread over period to which it applies).
- **§467** — Deferred rent and certain rents.
- **§163(d)** — Investment interest limitations.

## Treasury regulations

- **Reg §1.263(a)-4(f)** — 12-month rule for prepaid expenses.
- **Reg §1.461-1** — General timing rules.
- **Reg §1.461-4** — Economic performance.
- **Reg §1.461-5** — Recurring item exception.

## Key IRS guidance

- **Rev. Proc. 2002-65** — Trade discounts.
- IRS Publication 538 — Accounting Periods and Methods.

## Key court decisions

- **Encyclopedia Britannica, Inc. v. Commissioner, 685 F.2d 212 (7th
  Cir. 1982)** — Capitalization of expenditures with future benefit.
- **U.S. Freightways Corp. v. Commissioner, 270 F.3d 1137 (7th Cir.
  2001)** — Trucking permits with 12-month terms; deductible under
  recurring-item exception.

## Eligibility requirements

Cash-basis taxpayer:
1. Right or benefit does not extend beyond the earlier of:
   - 12 months after the first date on which the right or benefit
     begins, OR
   - The end of the tax year following the year of payment.
2. Payment is for a non-tax-shelter expenditure.
3. Item is not specifically capitalized under another rule (e.g.,
   §263A, §195 startup costs).

Accrual-basis taxpayer:
1. Same all-events test under Reg §1.461-1(a)(2)(i).
2. Economic performance under §461(h) and Reg §1.461-4.
3. Recurring item exception under §461(h)(3) may allow recurring
   items to be deducted before economic performance.

## Mechanics — how it works

1. **Year-end planning review.** Identify prepaid expenses with
   12-month-rule eligibility.
2. **Prepay before year end.** Pay vendor/insurer/landlord by Dec.
   31.
3. **Deduct full amount on current-year return** as ordinary
   business expense.
4. **Coordinate with §263A** if applicable.
5. **For accrual taxpayers:** apply economic performance rules;
   recurring item exception may allow similar acceleration.

## Documentation requirements

- Vendor invoices showing service period.
- Payment records (canceled check, ACH confirmation, credit card
  statement) dated current year.
- For insurance: policy declarations showing coverage period.
- For rent: lease showing rental period.

## Common pitfalls / audit risks

- **Benefit extends beyond 12 months.** Two-year service contract
  paid in advance does not qualify.
- **Prepaid interest under §461(g).** Must be spread over loan
  period regardless of cash payment.
- **Tax shelter taxpayer disqualification.** §461(i) imposes accrual
  method on tax shelters.
- **§267 related-party transactions.** Different rules apply.
- **Economic performance for accrual taxpayers.** Without economic
  performance (e.g., services not yet rendered), accrual taxpayer
  cannot deduct.

## Recent legislative changes

- **TCJA (2017)** — Increased small-business cash-method threshold
  to $25M average annual gross receipts (now indexed; ~$30M for
  2024). More businesses qualify for cash method.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §448 §461
  Pub L 119-21]`. Working assumption: no material changes.

## State conformity considerations

State conformity to federal cash/accrual treatment is generally
complete.

## AICPA SSTS / Circular 230 considerations

Standard practitioner diligence; routine year-end planning lever.

## Default confidence band rationale

**HIGH** — clear regulation (Reg §1.263(a)-4(f)) and well-
established practice. Drops to MODERATE for benefits at the 12-
month boundary.

## Cross-references

- **`maximize-business-deductions`** (#13) — broader framework.
- **`startup-cost-optimization`** (#27) — coordinate with §195.
- **`prepayment-expense-self-employed`** (#91) — Schedule C variant.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 461",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section461",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.263(a)-4(f)",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.461-5",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "CtAppeals",
      "citation": "U.S. Freightways Corp. v. Commissioner, 270 F.3d 1137 (7th Cir. 2001)",
      "url": "https://www.courtlistener.com",
      "weight": "binding_circuit"
    }
  ]
}
```
```

---

## Strategy #19: QBI Deduction

**File:** `references/strategies/qbi-deduction.md`

```markdown
---
name: "Qualified Business Income (QBI) Deduction"
slug: qbi-deduction
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§199A"]
forms: ["Form 8995 / 8995-A"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
cross_reference_skills: ["predict-qbi-eligibility"]
---

> **Cross-reference:** This strategy file complements
> `predict-qbi-eligibility`. The predict skill performs the
> eligibility analysis (whether a specific business qualifies);
> this strategy file describes the planning use case.

## Overview

§199A allows a 20% deduction on Qualified Business Income (QBI) for
non-corporate owners of pass-through entities (sole proprietors,
partnerships, S corporations, LLCs, certain trusts, certain rental
real estate). The deduction is below-the-line but does not require
itemizing.

The 20% rate is subject to:
1. **Wage / UBIA limit** (above income thresholds).
2. **Specified Service Trade or Business (SSTB) phase-out** (above
   income thresholds).
3. **20% taxable income overall cap.**

The thresholds for 2024:
- **Below $383,900 MFJ / $191,950 single:** Full 20% deduction;
  no wage limit; no SSTB exclusion.
- **Phase-in zone:** $383,900–$483,900 MFJ; $191,950–$241,950
  single.
- **Above phase-in:** Wage / UBIA limit applies (greater of 50% of
  W-2 wages or 25% of W-2 wages plus 2.5% of UBIA of qualified
  property); SSTB completely excluded.

OBBBA permanence: §199A was scheduled to sunset after 2025 under
TCJA. OBBBA reportedly made §199A permanent. Verify exact
provisions.

## Primary IRC authority

- **§199A** — QBI deduction. Statute and structure.
- **§199A(b)(2)** — Combined QBI amount calculation.
- **§199A(b)(3)** — Phase-in for SSTBs and W-2/UBIA limit.
- **§199A(c)** — QBI definition.
- **§199A(d)** — SSTB definition.
- **§199A(e)** — Other definitions (W-2 wages, UBIA).

## Treasury regulations

- **Reg §1.199A-1 through 1.199A-6** — Comprehensive implementing
  regulations.
- **Reg §1.199A-3** — QBI definition and computation.
- **Reg §1.199A-4** — Aggregation of trades or businesses.
- **Reg §1.199A-5** — SSTB definition.
- **Reg §1.199A-6** — Trust and estate rules.

`chevron_replaced: true` flagged on Reg §1.199A-5 SSTB definition
(post-Loper Bright). The regulation interprets the ambiguous
statutory term "specified service trade or business" with detailed
examples and de minimis rules. Practitioners relying on the
regulation's specific examples should note Skidmore review now
applies.

## Key IRS guidance

- **Notice 2019-07** — Safe harbor for rental real estate
  enterprise as §199A trade or business (250 hours of rental
  services).
- **Rev. Proc. 2019-38** — Updated rental real estate safe harbor.

## Key court decisions

- Limited recent dispute area; statute and regulations relatively
  recent.

## Eligibility requirements

See `predict-qbi-eligibility` for detailed eligibility analysis. Key:
1. QBI from qualified trade or business (not SSTB above threshold;
   not C corp).
2. Below-threshold taxpayers: no further limits.
3. Above-threshold: W-2/UBIA limit and SSTB exclusion apply.

SSTB categories under §199A(d)(2):
- Health
- Law
- Accounting
- Actuarial science
- Performing arts
- Consulting
- Athletics
- Financial services
- Brokerage services
- Any trade or business where the principal asset is the reputation
  or skill of one or more of its employees or owners

Engineering and architecture are explicitly excluded from SSTB
treatment under §199A(d)(2)(A).

## Mechanics — how it works

1. **Identify each trade or business** for §199A purposes.
2. **Compute QBI per business.**
3. **Apply SSTB analysis if above threshold.**
4. **Apply W-2/UBIA limit if above threshold.**
5. **Aggregation election.** Reg §1.199A-4 allows aggregation under
   conditions: same person directly or by attribution owns 50%+ of
   each business; aggregation reported and tracked annually; same
   tax year; not SSTB; meet two of three tests (similar products/
   services, sharing facilities/personnel, operationally interdependent).
6. **Form 8995 (simplified) or 8995-A (full).**

## Documentation requirements

See predict skill.

## Common pitfalls / audit risks

See predict skill.

## Recent legislative changes

- **TCJA (2017)** — Created §199A.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §199A
  permanence Pub L 119-21]`. Reports indicate §199A made permanent.

## State conformity considerations

State decoupling on QBI varies. Major decoupling states:
California, New York, New Jersey, Pennsylvania (no QBI for state).

## AICPA SSTS / Circular 230 considerations

See predict skill.

## Default confidence band rationale

**HIGH** for clear-fact patterns. See predict skill for fact-
specific analysis.

## Cross-references

- **`predict-qbi-eligibility`** (predict skill) — primary
  qualification analysis.
- **`reasonable-comp-corp-owners`** (#21) — interaction with §199A
  W-2 wage limit (S corp owner wages count toward W-2 limit).
- **`real-estate-professional`** (#20) — REPS rental qualifying
  as §199A trade or business.
- **`grouping-of-activities`** (#9) — interacts with §199A
  aggregation.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 199A",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section199A",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.199A-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.199A-5",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation",
      "chevron_replaced": true
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2019-07",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
```

---

## Strategy #20: Real Estate Professional

**File:** `references/strategies/real-estate-professional.md`

```markdown
---
name: "Real Estate Professional Status (REPS) — §469(c)(7)"
slug: real-estate-professional
type: Business - Other
tax_type: EFR
complexity: High
irc_sections: ["§469(c)(7)", "§469(c)(2)"]
forms: ["No specific form; election under §469(c)(7)(A) by attached statement"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: MODERATE
last_obbba_review: "N/A"
cross_reference_skills: ["predict-real-estate-pro"]
---

> **Cross-reference:** This strategy file complements
> `predict-real-estate-pro`. The predict skill performs the
> qualification analysis. This strategy file focuses on planning
> implementation.

## Overview

§469(c)(7) Real Estate Professional Status (REPS) removes a
taxpayer's rental real estate activities from the per-se passive
characterization of §469(c)(2). REPS taxpayers can deduct rental
losses against other (non-passive) income without the $25,000
active-participation cap or the $100K-$150K phaseout.

REPS is the most-litigated area of §469 because the qualification
test is fact-intensive. The taxpayer (or spouse) must satisfy two
tests:
1. **More than half** of personal services performed in trades or
   businesses during the year are performed in real property trades
   or businesses in which the taxpayer materially participates;
   AND
2. **More than 750 hours** of services during the year in real
   property trades or businesses in which the taxpayer materially
   participates.

After REPS qualification, each separate rental still must satisfy
material participation under §469(h) — UNLESS the §469(c)(7)(A)
election is made to treat all rental real estate as one activity.

The combination of REPS + cost-segregation studies has become the
backbone of high-net-worth real estate tax planning, allowing
taxpayers with substantial real estate holdings to use depreciation
losses against W-2 and other non-passive income. The strategy
collapses if REPS qualification fails — and it fails frequently in
audit, because the IRS routinely challenges contemporaneous-records
adequacy.

## Primary IRC authority

- **§469(c)(7)** — Real estate professional rules.
- **§469(c)(7)(B)** — REPS qualification tests.
- **§469(c)(7)(C)** — Real property trade or business definition.
- **§469(c)(7)(A)** — Election to aggregate rentals.

## Treasury regulations

- **Reg §1.469-9** — Comprehensive REPS rules.
- **Reg §1.469-9(b)** — Real property trade or business definition.
- **Reg §1.469-9(g)** — Aggregation election.

## Key IRS guidance

- **Rev. Proc. 2011-34** — Late §469(c)(7)(A) election relief.

## Key court decisions

- **Bailey v. Commissioner, T.C. Memo. 2001-296** — REPS hours not
  established without contemporaneous records.
- **Hassanipour v. Commissioner, T.C. Memo. 2013-88** — REPS denied;
  contemporaneous logs unconvincing.
- **Lewis v. Commissioner, T.C. Memo. 2015-235** — REPS denied;
  attorney with active legal practice could not satisfy "more than
  half" test.
- **Pohoski v. Commissioner, T.C. Memo. 1998-17** — REPS context.
- **Hailstock v. Commissioner, T.C. Summ. Op. 2016-11** — REPS
  granted for taxpayer who could document hours and substantial
  involvement.
- **Frank Aragona Trust v. Commissioner, 142 T.C. 165 (2014)** —
  Trusts can qualify as real estate professionals (predicate to
  trustee material participation).

## Eligibility requirements

See `predict-real-estate-pro` for detailed analysis. Key:
1. >750 hours in real property trades/businesses with material
   participation.
2. >50% of personal services in trades/businesses in real property
   trades/businesses with material participation.
3. For each rental: separate material participation under §469(h),
   OR §469(c)(7)(A) aggregation election.

## Mechanics — how it works

1. **Document hours throughout the year.** Contemporaneous logs.
2. **Compute material participation for each rental** OR make
   §469(c)(7)(A) election to aggregate.
3. **File §469(c)(7)(A) election** by attached statement to return.
4. **Treat rentals as nonpassive** for §469 purposes.
5. **Coordinate with §1411 NIIT.** REPS rentals can be excluded
   from §1411 NIIT if they constitute a trade or business under
   §162.

## Documentation requirements

- Contemporaneous time logs (calendar entries, billing records).
- Property records establishing hours.
- §469(c)(7)(A) election statement.
- Spouse-aggregation analysis (joint filers can aggregate spouses'
  hours for material participation but not for the >50% / >750-hour
  tests, which are individual).

## Common pitfalls / audit risks

- **Contemporaneous record requirement.** Reconstructed logs are
  routinely rejected.
- **Concurrent W-2 employment.** Other employment generally defeats
  >50% test (need to spend more time in real estate than at the
  primary job).
- **>750 hours not satisfied.** Smaller real estate portfolios
  often fail.
- **Spouse split.** Each spouse must individually meet both tests
  for REPS (joint testing not allowed for >50% / >750).
- **§469(c)(7)(A) election not filed.** Taxpayer must aggregate
  rentals to test material participation; failure to elect means
  each rental tested separately.
- **Property manager handling daily operations.** Outsourced
  management may defeat material participation per rental even with
  REPS qualification at the entity level.

## Recent legislative changes

- No material recent changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §469(c)(7)
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §469 is generally complete; REPS treatment
flows.

## AICPA SSTS / Circular 230 considerations

REPS is fact-intensive and IRS audit-targeted. Practitioner should
maintain rigorous documentation discipline. Form 8275 disclosure
appropriate for borderline cases.

## Default confidence band rationale

**MODERATE** — judicial doctrine with strict tests; outcome heavily
fact-dependent. Drops to LOW for taxpayers with concurrent W-2
employment or thin documentation.

## Cross-references

- **`predict-real-estate-pro`** (predict skill).
- **`predict-material-participation`** (predict skill).
- **`active-participation-real-estate`** (#3) — non-REPS path.
- **`grouping-of-activities`** (#9) — §469(c)(7)(A) aggregation.
- **`short-term-rental`** (#26) — alternative path (STR is not
  rental activity, so REPS not required).
- **`niit-minimization`** (#69) — REPS interaction with §1411.
- **`cost-segregation`** (#41) — primary partner strategy.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 469(c)(7)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.469-9",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2011-34",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    },
    {
      "authority_type": "TaxCt",
      "citation": "Hassanipour v. Commissioner, T.C. Memo. 2013-88",
      "url": "https://www.ustaxcourt.gov",
      "weight": "judicial"
    },
    {
      "authority_type": "TaxCt",
      "citation": "Frank Aragona Trust v. Commissioner, 142 T.C. 165 (2014)",
      "url": "https://www.ustaxcourt.gov",
      "weight": "judicial"
    }
  ]
}
```
```

---

## Strategy #21: Reasonable Compensation for Corporate Owners

**File:** `references/strategies/reasonable-comp-corp-owners.md`

```markdown
---
name: "Reasonable Compensation for S Corporation and C Corporation Owners"
slug: reasonable-comp-corp-owners
type: Business - Other
tax_type: 2SH
complexity: Medium
irc_sections: ["§162(a)(1)", "§3121", "§3306", "§3401", "§174"]
forms: ["Form W-2", "Form 1120-S Schedule K-1", "Form 1120 Schedule M-1"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

> **Caution:** Reasonable compensation is the single most-audited
> issue for S corporations. The IRS treats unreasonably low S corp
> shareholder-employee compensation as a primary enforcement target.
> S corp owners taking $0 wages while drawing six-figure
> distributions face high audit risk and potential reclassification.
> Conversely, C corp closely-held businesses face the opposite
> issue: unreasonably HIGH compensation may be reclassified as
> dividends (non-deductible).

## Overview

Reasonable compensation analysis applies in two opposing contexts:

**S corporation context:** Owner-employees who provide services
must be paid reasonable compensation as W-2 wages, subject to
employment taxes (FICA at 7.65% employer + 7.65% employee on first
$168,600 of wages for 2024 [verify 2025 SS wage base]; 1.45% +
1.45% on remaining wages; 0.9% Additional Medicare Tax above
$200,000 single / $250,000 MFJ). Distributions in excess of
reasonable compensation are not subject to employment tax. The IRS
challenges S corps that pay artificially low wages relative to
distributions, recharacterizing distributions as wages and
imposing FICA, employer match, and penalties.

**C corporation context (closely-held):** Owner-employees with
high compensation may be challenged as receiving disguised
dividends. C corp pays compensation as deductible §162 expense;
recharacterization as dividend disallows deduction at the corp
level (and remains taxable at owner level). The "reasonable" test
is bilateral.

The IRS does not provide bright-line tests. Reasonable comp
analysis applies multiple factors:
- Industry comparables (BLS, RCReports, industry surveys).
- Owner's role, qualifications, hours worked.
- Performance of similar employees.
- Comparison to similarly-sized companies.
- Owner's prior compensation history.
- Value of services rendered.

## Primary IRC authority

- **§162(a)(1)** — Reasonable allowance for salaries or other
  compensation for personal services.
- **§3121** — FICA wage base and rates.
- **§3306** — FUTA.
- **§3401** — Income tax withholding.
- **§199A** — QBI deduction (S corp wages count toward W-2 wages
  limit).
- **§280G** — Golden parachute payments (extreme cases).

## Treasury regulations

- **Reg §1.162-7** — Compensation for personal services.
- **Reg §1.162-8** — Treatment of excessive compensation.
- **Reg §31.3121** — FICA implementing regulations.

## Key IRS guidance

- **Fact Sheet 2008-25** — Reasonable Compensation for S
  Corporation Officers. The most-cited IRS guidance on the topic.
  https://www.irs.gov/businesses/small-businesses-self-employed/wage-compensation-for-s-corporation-officers
- **IRS Job Aid: Reasonable Compensation for S Corporation
  Officers** — internal IRS examination guide.
- **IRS Pub 535** — Business Expenses.

## Key court decisions

For S corporations:
- **Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)** — The
  leading S corp case. Watson, a CPA owner of S corp, paid himself
  $24K W-2 wage and took $200K+ distributions. The court upheld the
  IRS's recharacterization of distributions as wages, applying $91K
  reasonable comp. Cited extensively in subsequent cases.
- **Spicer Accounting, Inc. v. United States, 918 F.2d 90 (9th Cir.
  1990)** — S corp officer received $0 wages.
  Distributions recharacterized.
- **Joseph M. Grey Public Accountant, P.C. v. Commissioner, 119
  T.C. 121 (2002)** — Officer compensation analysis.
- **JD & Associates, Ltd. v. United States, 2006 WL 1037015 (D.N.D.
  2006)** — IRS prevailed on S corp reclassification.

For C corporations:
- **Menard, Inc. v. Commissioner, 560 F.3d 620 (7th Cir. 2009)** —
  Reasonable comp upheld at $20M+ for high-performing CEO of large
  hardware chain. Multi-factor analysis.
- **Exacto Spring Corp. v. Commissioner, 196 F.3d 833 (7th Cir.
  1999)** — "Independent investor test" — would a hypothetical
  outside investor be satisfied with the rate of return after
  paying the compensation?

## Eligibility requirements

There is no bright-line; the analysis is multi-factor:

**S corp underpayment risk factors:**
1. Officer/owner provides material services.
2. W-2 wages are low relative to distributions.
3. W-2 wages are low relative to industry comparables.
4. No reasonable basis for low wage (e.g., no documented PTO,
   limited services, etc.).

**C corp overpayment risk factors:**
1. Compensation greatly exceeds industry comparables.
2. Compensation increases dramatically without corresponding
   business growth.
3. Insufficient corporate dividends paid.
4. Compensation correlates suspiciously with company profits.
5. Independent investor test fails (returns insufficient).

## Mechanics — how it works

1. **Determine reasonable comp range.**
   - **RCReports** — commercial tool; widely accepted.
   - **BLS data** — Bureau of Labor Statistics OEWS by occupation
     and geography.
   - **Industry surveys.**
   - **Comparable employee data.**
2. **Document the analysis.**
3. **Set reasonable comp** — at least the floor of the supported
   range; ideally with a margin.
4. **Coordinate with §199A.** Higher S corp wages reduce QBI
   deduction (W-2 wages reduce QBI passed through). At higher
   incomes, the §199A W-2 wage limit may make higher wages
   beneficial.
5. **Annual review.** Update analysis annually; document changes.

## Documentation requirements

- Reasonable compensation analysis report (RCReports output, BLS
  data printout, industry survey).
- Job description with hours, duties, qualifications.
- Board resolution setting compensation.
- Comparison to industry comparables.

## Common pitfalls / audit risks

- **Zero or near-zero W-2 wages with significant distributions.**
  Highest-risk pattern. IRS recharacterization is highly likely.
- **No documentation of the analysis.** Inability to support
  reasoning at audit.
- **Reasonable comp set after year-end as a tax adjustment.**
  Historical comp pattern matters more than year-end "true-ups."
- **Failure to consider §199A interaction.** S corp wages reduce
  passed-through QBI, which may reduce the 20% deduction. At higher
  incomes the W-2 wage limit may favor higher wages.
- **Multiple-officer scenarios.** Each officer's comp analyzed
  separately.
- **Family-employed.** Family members on payroll without bona fide
  services trigger separate scrutiny.

## Recent legislative changes

- **TCJA (2017)** — Created §199A and the W-2 wage limit, which
  increased the planning complexity around comp setting.
- **CARES Act (2020)** — ERC interaction with comp.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §162 §199A
  reasonable comp Pub L 119-21]`. Working assumption: no direct
  changes.

## State conformity considerations

States generally accept federal comp characterization for S corps,
but unique state rules apply. **California** has significant
state-level S corp tax (1.5% S corp franchise tax) that interacts
with comp planning. Verify state stub.

## AICPA SSTS / Circular 230 considerations

Reasonable compensation is a primary IRS enforcement target. SSTS
§1.4 reasonable inquiry into the basis for the comp position.
Practitioner should obtain or run reasonable comp analysis annually
for each S corp client and document conclusion.

## Default confidence band rationale

**MODERATE** — fact-intensive multi-factor analysis. Drops to LOW
for unreasonably low S corp wages, or unreasonably high C corp
wages. Rises to HIGH for well-documented analyses supported by
RCReports or comparable industry data.

## Cross-references

- **`reimbursement-business-expenses`** (#22) — accountable plan
  alternative.
- **`reimbursement-depreciation-s-corp-vehicle`** (#23).
- **`qbi-deduction`** (#19) — interaction with W-2 limit.
- **`hiring-kids`** (#49) — family-employment companion analysis.
- **`wages-spouse-parents`** (#50) — family-employment companion.
- **`choice-of-entity-se-tax`** (#86) — S corp election analysis
  whose primary value is reasonable comp / SE tax savings.
- **`minimize-self-employment-tax`** (#90) — companion analysis.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 162(a)(1)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.162-7",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "CtAppeals",
      "citation": "Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)",
      "url": "https://www.courtlistener.com",
      "weight": "binding_circuit"
    },
    {
      "authority_type": "CtAppeals",
      "citation": "Menard, Inc. v. Commissioner, 560 F.3d 620 (7th Cir. 2009)",
      "url": "https://www.courtlistener.com",
      "weight": "binding_circuit"
    },
    {
      "authority_type": "CtAppeals",
      "citation": "Exacto Spring Corp. v. Commissioner, 196 F.3d 833 (7th Cir. 1999)",
      "url": "https://www.courtlistener.com",
      "weight": "binding_circuit"
    },
    {
      "authority_type": "IRSPub",
      "citation": "IRS Fact Sheet 2008-25, Wage Compensation for S Corporation Officers",
      "url": "https://www.irs.gov/businesses/small-businesses-self-employed/wage-compensation-for-s-corporation-officers",
      "weight": "persuasive_non_authority"
    }
  ]
}
```
```

---

## Strategy #22: Reimbursement of Deductible Business Expenses

**File:** `references/strategies/reimbursement-business-expenses.md`

```markdown
---
name: "Reimbursement of Deductible Business Expenses Under Accountable Plan"
slug: reimbursement-business-expenses
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§62(a)(2)(A)", "§62(c)", "§162"]
forms: ["No specific form; payroll system handles non-W-2 reimbursement"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

This strategy covers the broader application of accountable plan
reimbursement under Reg §1.62-2 — beyond home office (#2) and
vehicle (#4 / #23). Common reimbursable categories that should run
through an accountable plan rather than be paid personally and
left as nondeductible (post-TCJA §67(g) suspension):

- **Cell phone and internet** — see strategy #5.
- **Travel** — airfare, lodging, meals, ground transportation,
  conference attendance.
- **Professional development** — continuing education, books,
  subscriptions.
- **Office supplies and small equipment** purchased personally.
- **Software subscriptions** charged to personal credit cards.
- **Networking events and dues** — chambers, professional
  associations.
- **Home office expenses** — the primary application; see #2.
- **Vehicle expenses** — see #4 and #23.

The structural point: any owner-employee of a corporation who
incurs business expenses personally should be reimbursed through
the accountable plan rather than absorb the expense personally.
TCJA's §67(g) suspension eliminated the prior fallback (Schedule A
2% deduction), making the accountable plan the only path.

## Primary IRC authority

- **§62(a)(2)(A)** — Reimbursement under accountable plan
  excluded from gross income.
- **§62(c)** — Reimbursement arrangements.
- **§162** — Underlying business expense.
- **§67(g)** — Suspension of miscellaneous itemized deductions
  through 2025 (made permanent by OBBBA per working assumption).
- **§274(d)** — Strict substantiation for vehicle, travel, M&E.

## Treasury regulations

- **Reg §1.62-2** — Accountable plan rules. The cornerstone.
- **Reg §1.274-5T** — §274(d) substantiation.

## Key IRS guidance

- **Rev. Proc. 2019-46** — Standard mileage rate.
- **Rev. Proc. updates annually** — High-low per diem.
- **IRS Publication 463** — Travel, Gift, and Car Expenses.

## Key court decisions

- See accountable plan and §274(d) cases under #2 and #4.

## Eligibility requirements

Same as #2 — Reg §1.62-2(c) three elements:
1. Business connection.
2. Substantiation.
3. Return of excess.

Plus category-specific §274(d) substantiation for vehicle, travel,
M&E.

## Mechanics — how it works

1. **Adopt written accountable plan** by board resolution.
2. **Establish reimbursement procedure.** Monthly or quarterly
   expense reports with receipts.
3. **Substantiate per category.** §274(d) categories require strict
   substantiation; other categories require ordinary records under
   §6001.
4. **Reimburse.** Not included in W-2; deductible by corporation
   under §162.
5. **Annual review.** Catch missed reimbursable items.

## Documentation requirements

- Written accountable plan.
- Expense reports with receipts.
- §274(d) substantiation for applicable categories.

## Common pitfalls / audit risks

- **Failure to reimburse personal payments.** Owner pays personally
  and never gets reimbursed; deduction is lost.
- **Inadequate substantiation.** §274(d) failures.
- **Reimbursing personal items.** Personal items reimbursed
  through accountable plan may be challenged; recharacterized as
  wages.
- **Untimely substantiation.** 60-day fixed-date safe harbor under
  Reg §1.62-2(g)(2).

## Recent legislative changes

- **TCJA (2017)** — Made accountable plan critical via §67(g)
  suspension.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §67(g)
  permanent Pub L 119-21]`. Working assumption: §67(g) made
  permanent.

## State conformity considerations

State conformity to §62 / §67 is generally complete. Some states
(CA) do not conform to §67(g) suspension and still allow Schedule A
miscellaneous deduction at state level.

## AICPA SSTS / Circular 230 considerations

Standard diligence. The accountable plan is well-established and
practitioner role is to ensure it is implemented and used.

## Default confidence band rationale

**HIGH** — settled regulation, decades of practice. Drops to
MODERATE only for substantiation failures.

## Cross-references

- **`accountable-plan-home-office`** (#2) — primary application.
- **`business-vehicle-usage`** (#4) — vehicle application.
- **`cell-phone-expenses`** (#5) — cell phone application.
- **`reimbursement-depreciation-s-corp-vehicle`** (#23).
- **`accountable-plan-self-employed`** (#84) — sole-prop variant
  (different framework).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 62(a)(2)(A)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section62",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.62-2",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    }
  ]
}
```
```

---

## Strategy #23: Reimbursement of Depreciation on S Corp Owner's Vehicle

**File:** `references/strategies/reimbursement-depreciation-s-corp-vehicle.md`

```markdown
---
name: "Reimbursement of Depreciation Expenses — S Corp Owner Vehicle"
slug: reimbursement-depreciation-s-corp-vehicle
type: Business - Other
tax_type: EFR
complexity: High
irc_sections: ["§62(a)(2)(A)", "§168", "§280F", "§274(d)"]
forms: ["Form 4562 (corporate level if corp owns vehicle)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

## Overview

This strategy addresses an intricate question: how should an S
corporation owner-employee handle vehicle ownership and
depreciation? Three structures are common:

1. **Owner owns vehicle; corporation reimburses standard mileage
   rate.** Simplest. Owner reports nothing; corporation deducts.
   Owner cannot also claim depreciation personally because IRS
   standard mileage rate includes a depreciation component.
2. **Owner owns vehicle; corporation reimburses actual expenses
   (including depreciation share).** Complex. Owner must compute
   depreciation; corporation reimburses business-use share. Owner's
   personal depreciation tracking required.
3. **Corporation owns vehicle.** Corporation depreciates fully
   subject to §280F luxury auto caps. Owner-employee personal use
   creates W-2 inclusion (compensation income) for personal
   commuting and personal use — measured under Reg §1.61-21
   (annual lease value or vehicle cents-per-mile rule).

The strategy file's name implies structure #2, which is the most
complex variant. The strategic question: can the corporation's
accountable plan reimburse the owner-employee for depreciation on
the owner's personally-owned vehicle? Generally yes, under Reg
§1.62-2, with §274(d) substantiation. The mechanics require:

1. Owner determines the vehicle's depreciable basis.
2. Annual depreciation computed (subject to §280F luxury auto
   limits if light passenger auto).
3. Business-use percentage applied.
4. Corporation reimburses owner the business-use depreciation
   share.
5. Owner does not also claim depreciation directly (no double-
   dipping).

The §280F luxury auto caps at the owner level limit the
depreciation that can be reimbursed. Heavy SUV (>6,000 lbs GVWR)
and heavy truck planning escapes §280F caps.

The structure is uncommon in practice. Most practitioners prefer
either standard mileage rate reimbursement (simplest) or
corporation ownership (cleanest). The actual-expense-with-
depreciation reimbursement structure has multiple compliance
failure points.

## Primary IRC authority

- **§62(a)(2)(A)** — Accountable plan.
- **§168** — MACRS.
- **§280F** — Luxury auto caps.
- **§274(d)** — Substantiation.

## Treasury regulations

- **Reg §1.62-2** — Accountable plan.
- **Reg §1.280F-1T through §1.280F-7** — Luxury auto.
- **Reg §1.274-5T** — Substantiation.
- **Reg §1.61-21** — Personal use of corporate-owned vehicle (for
  structure #3).

## Key IRS guidance

- **Rev. Proc. 2019-46** — Standard mileage rate.
- **Annual Rev. Proc. on §280F luxury auto caps.**

## Key court decisions

- See cases under #4.

## Eligibility requirements

For the depreciation-reimbursement structure:
1. Owner personally owns the vehicle.
2. Vehicle used in S corp business activity.
3. Accountable plan adopted by S corp.
4. §274(d) substantiation maintained.
5. Owner depreciation tracked personally; reimbursed amount
   not separately claimed by owner.
6. §280F luxury auto caps applied at owner level.

## Mechanics — how it works

1. **Document vehicle ownership.**
2. **Establish depreciation method.** Generally MACRS 5-year for
   passenger autos. §168(k) bonus and §179 considerations.
3. **Apply §280F caps if light passenger auto.**
4. **Compute annual depreciation × business-use percentage.**
5. **Submit reimbursement request to corporation.**
6. **Corporation reimburses; owner does not separately deduct
   depreciation.**
7. **Track basis for eventual sale.** Reimbursed depreciation
   reduces basis (effectively), creating gain on sale.

## Documentation requirements

- Vehicle title.
- Depreciation schedule (cost basis, prior depreciation).
- §274(d) mileage logs.
- Reimbursement records.
- Accountable plan documents.

## Common pitfalls / audit risks

- **Double-dipping.** Owner cannot claim depreciation personally
  AND receive depreciation reimbursement.
- **§280F coordination.** Limits must be applied.
- **Standard mileage rate vs. actual expense locked in.** Standard
  mileage rate in year 1 prevents actual-expense method later. The
  reimbursement method should be consistent.
- **Personal use creep.** Business-use percentage must be tracked
  and documented.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §168(k)
  100% bonus depreciation Pub L 119-21]`. If 100% bonus restored,
  significant impact on first-year reimbursement.

## State conformity considerations

State decoupling on §168(k) bonus requires state-level
adjustment.

## AICPA SSTS / Circular 230 considerations

Multi-step compliance with several failure points. Practitioner
should evaluate whether structure #1 (standard mileage rate) or #3
(corporation ownership) is simpler and produces similar economic
result.

## Default confidence band rationale

**MODERATE** — multiple compliance points; substance is sound but
execution is error-prone. Drops to LOW if §280F or substantiation
issues arise.

## Cross-references

- **`accountable-plan-home-office`** (#2).
- **`business-vehicle-usage`** (#4) — primary vehicle strategy.
- **`bonus-and-section-179-depreciation`** (#12).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 280F",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280F",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 168",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section168",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.62-2",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    }
  ]
}
```
```

---

## Strategy #24: Augusta Rule (§280A(g))

**File:** `references/strategies/augusta-rule-280a-g.md`

```markdown
---
name: "Augusta Rule — §280A(g) Home Rental for ≤14 Days"
slug: augusta-rule-280a-g
type: Business - Other
tax_type: EFR
complexity: Low
irc_sections: ["§280A(g)", "§162"]
forms: ["No specific form (rental income excluded; deduction at corp level)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

> **Caution:** The Augusta Rule has attracted IRS scrutiny in recent
> years. The Tax Court decision in **Sinopoli v. Commissioner, T.C.
> Memo. 2023-105** disallowed Augusta Rule deductions where the
> corporate "rental" of the owner's home was not at fair-rental-value
> and lacked contemporaneous documentation. The strategy is valid
> but requires (a) genuine business use (not pretextual), (b) fair
> rental value supported by comparable rental data, and (c)
> contemporaneous documentation. Practitioners should treat the
> Augusta Rule as audit-targeted.

## Overview

§280A(g) provides that if a taxpayer rents a personal residence
for fewer than 15 days during the year, the rental income is
excluded from gross income and no rental deductions are allowed.
This is a specific carve-out from the general §280A vacation-home
rules.

The Augusta Rule strategy: an owner-employee of a corporation rents
his/her home to the corporation for legitimate business meetings
(board meetings, strategy retreats, client events) for up to 14
days per year. The corporation deducts the rental as §162 business
expense. The owner-employee excludes the rental income under
§280A(g). Net result: a deductible expense at the corporation
without a corresponding income inclusion at the owner.

The rule is named "Augusta" after the Masters Tournament; Augusta,
Georgia residents historically rented their homes for the
tournament week and excluded the income under this provision.

For the strategy to work, three substantive requirements must be
satisfied:
1. **Bona fide business purpose.** The corporate "rental" must be
   for legitimate business activity — board meetings, strategy
   sessions, employee training, client events. Pretextual rentals
   for personal/family events fail.
2. **Fair rental value.** The rental amount must reflect what an
   independent third party would pay for comparable space. Inflated
   "rentals" (e.g., $10,000/day for an unremarkable home) fail.
3. **Contemporaneous documentation.** Meeting minutes, attendee
   lists, agenda, comparable rental data.

## Primary IRC authority

- **§280A(g)** — Special rules for less-than-15-day rentals.
  https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A
- **§162(a)** — Ordinary and necessary business expense
  (corporation side).
- **§280A(a)** — General §280A disallowance (the framework
  §280A(g) carves out from).

## Treasury regulations

- **Reg §1.280A-1 through §1.280A-3** — General §280A regulations.
- No specific regulation extensively interprets §280A(g) — the
  statute is largely self-executing.

## Key IRS guidance

- Limited specific Augusta Rule guidance from IRS.
- IRS Publication 527 — Residential Rental Property.
- IRS Publication 535 — Business Expenses (corporate side).

## Key court decisions

- **Sinopoli v. Commissioner, T.C. Memo. 2023-105** — The leading
  recent case. The court disallowed the Augusta Rule deduction
  where (a) the rental was not at fair rental value (the home was
  rented at $1,500/day; comparable hotel meeting space was
  $50–$150/day), (b) the corporate purpose for the meetings was
  inadequately documented, and (c) the meetings were attended only
  by the owner and family members. Sinopoli is a significant
  warning case; practitioners should structure Augusta Rule
  arrangements to avoid the Sinopoli pattern.
- Other cases: limited prior litigation; the rule was historically
  uncontroversial.

## Eligibility requirements

1. **Property is taxpayer's residence.** Including primary or
   secondary home.
2. **Rented fewer than 15 days during the year.** Including
   non-Augusta-Rule rentals — total annual rental days must be
   under 15.
3. **Bona fide rental.** Rental at fair market value to an unrelated
   party (or, for the Augusta Rule strategy, to the owner's
   corporation under terms an unrelated party would accept).
4. **Business purpose at corporate level.** §162 ordinary and
   necessary.
5. **Substantiation under §6001.** Records of dates, fair rental
   value support, business purpose.

## Mechanics — how it works

1. **Schedule corporate meetings.** Board meetings, strategy
   sessions, employee training, etc. Document agenda, attendees,
   purpose.
2. **Set fair rental value.** Comparable hotel meeting space; local
   event rental rates; coworking space day rates. Document with
   actual quotes from third-party providers.
3. **Execute formal rental agreement** between corporation and
   owner-as-individual.
4. **Hold meetings on the rental days.** Take minutes; sign-in
   sheet; agendas.
5. **Corporation pays rental.** Issue invoice from owner-as-
   individual; corporation pays via check/ACH.
6. **Track total rental days for the year.** Stay under 15.
7. **Tax reporting:** Corporation deducts under §162 (rent
   expense). Owner excludes from gross income under §280A(g) —
   no Schedule E entry required (income is excluded, not just
   non-deductible expenses).

## Documentation requirements

- Meeting minutes with attendee lists, agenda, business purpose.
- Comparable rental quotes (hotel banquet rooms, conference
  centers, coworking spaces).
- Rental agreement between corporation and owner.
- Calendar showing meeting days and confirming under-15-day total.
- Payment records (corporation to owner).
- Photos / floor plan documenting home space used for meetings.

## Common pitfalls / audit risks

- **Inflated rental rates (Sinopoli failure).** Set fair rental
  value with documented support.
- **Pretextual meetings.** Family gatherings recharacterized as
  "board meetings" do not qualify.
- **Solo "meetings."** Owner alone in their home is not a meeting.
  Multiple bona fide attendees expected.
- **No contemporaneous documentation.** Reconstructed records are
  routinely rejected at audit.
- **Total annual rentals exceeding 14 days.** The exclusion is
  cliff-style; 15+ days disqualifies the entire year.
- **Combination with personal-use vacation home.** §280A application
  is intricate; vacation-home treatment may apply.
- **State income tax inclusion.** Some states do not conform to
  §280A(g) and tax the rental income at state level.

## Recent legislative changes

- No statutory changes in recent years.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §280A
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity is generally complete but verify state-specific
treatment. **California** generally conforms.

## AICPA SSTS / Circular 230 considerations

The Sinopoli decision elevated the Augusta Rule to audit-target
status. Practitioner should treat client requests for Augusta Rule
deductions as warranting careful diligence: verify fair rental
value, confirm business substance, and recommend Form 8275
disclosure for borderline cases.

## Default confidence band rationale

**MODERATE** — statute is clear but factual application is
audit-targeted. Drops to LOW for arrangements with thin business
substance, inflated rates, or weak documentation. Rises to HIGH
for properly-documented arrangements with comparable-rental
support and bona fide business purpose.

## Cross-references

- **`accountable-plan-home-office`** (#2) — alternative for
  recurring home-office reimbursement.
- **`meals-and-entertainment`** (#14) — interaction at events.
- **`maximize-business-deductions`** (#13).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 280A(g)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section280A",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TaxCt",
      "citation": "Sinopoli v. Commissioner, T.C. Memo. 2023-105",
      "url": "https://www.ustaxcourt.gov",
      "weight": "judicial"
    }
  ]
}
```
```

---

## Strategy #25: Rental Strategies (Umbrella)

**File:** `references/strategies/rental-strategies.md`

```markdown
---
name: "Rental Real Estate Strategies (Umbrella)"
slug: rental-strategies
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§469", "§280A", "§168", "§121", "§1031", "§199A", "§1411"]
forms: ["Schedule E", "Form 8582"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

This strategy file is the umbrella reference for rental real estate
planning, cross-referencing the more specific rental strategies in
the library. Rental real estate is unusually rich in tax planning
opportunities because it sits at the intersection of:

1. **§469 Passive Activity Loss rules** — including the per-se
   passive characterization (§469(c)(2)), the active-participation
   $25K offset (§469(i)), the real-estate-professional exception
   (§469(c)(7)), grouping (Reg §1.469-4), and self-rental
   recharacterization (Reg §1.469-2(f)(6)).
2. **§280A vacation home rules** — limiting deductions when
   personal use is significant.
3. **§168 / §168(k) / §179 / Cost Segregation** — accelerated
   depreciation on improvements and components.
4. **§1031 Like-Kind Exchange** — deferral on disposition.
5. **§121 Primary Residence Exclusion** — interaction with rental
   conversion.
6. **§199A Qualified Business Income** — Notice 2019-07 safe
   harbor for rental real estate enterprise.
7. **§1411 NIIT** — application to net rental income.

This file consolidates the cross-references and identifies which
specific strategy file to consult for each rental scenario.

## Primary IRC authority

See umbrella-referenced files.

## Strategic decision tree

**Q1: Is the property short-term rental (avg customer use ≤7 days)?**
- Yes → see `short-term-rental` (#26). STR is not a rental activity
  under Temp. Reg §1.469-1T(e)(3); material participation analysis
  determines passive characterization.
- No → continue.

**Q2: Is taxpayer a real estate professional?**
- Yes → see `real-estate-professional` (#20) and
  `predict-real-estate-pro`. Make §469(c)(7)(A) election; rentals
  treated as nonpassive if material participation per rental (or
  aggregated under election).
- No → continue.

**Q3: Below $150K MAGI?**
- Yes → see `active-participation-real-estate` (#3). $25K offset
  available with active participation (lower bar than material
  participation).
- No → continue.

**Q4: Suspended passive losses to absorb?**
- Yes → see `passive-income-pigs` (#16). Or wait for §469(g)
  release on disposition. Or see `grouping-of-activities` (#9).

**Q5: Considering disposition?**
- Yes → see `1031-like-kind-exchange` (#1) for deferral; or
  `installment-sale` (#33); or §121 exclusion if converted to
  primary residence (`primary-home-sale-exclusion` #67).

**Q6: New purchase?**
- See `cost-segregation` (#41) for engineering study to maximize
  bonus / §179.

**Q7: §199A planning?**
- See `qbi-deduction` (#19) and Notice 2019-07 rental real estate
  safe harbor (250 hours of rental services).

## Mechanics — how it works (general)

1. **Maintain separate books per property.** Track income, expenses,
   capital improvements, depreciation, repairs vs. improvements
   under tangible property regs.
2. **Annual passive activity tracking.** Form 8582; track suspended
   losses by activity.
3. **Year-end planning.**
   - Bonus / §179 on improvements.
   - Cost-seg study for new acquisitions.
   - PTET if entity-structured.
   - §1031 planning if disposing.
4. **State PTET election** if entity-structured (interaction with
   #17).

## Cross-references

- **`active-participation-real-estate`** (#3)
- **`real-estate-professional`** (#20)
- **`grouping-of-activities`** (#9)
- **`passive-income-pigs`** (#16)
- **`short-term-rental`** (#26)
- **`1031-like-kind-exchange`** (#1)
- **`cost-segregation`** (#41)
- **`installment-sale`** (#33)
- **`qbi-deduction`** (#19)
- **`primary-home-sale-exclusion`** (#67)
- **`niit-minimization`** (#69)
- **`ptet-salt-workaround`** (#17)

## Authorities (JSON sidecar fragment)

This file is a router; specific authorities live in the cross-
referenced files.

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 469",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469",
      "weight": "primary_statute"
    }
  ]
}
```
```

---

## Strategy #26: Short-Term Rental

**File:** `references/strategies/short-term-rental.md`

```markdown
---
name: "Short-Term Rental Real Estate (Airbnb / VRBO Strategy)"
slug: short-term-rental
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§469", "§280A", "§168"]
forms: ["Schedule C (if material participation hotel-like) or Schedule E (if not)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: MODERATE
last_obbba_review: "N/A"
cross_reference_skills: ["predict-material-participation"]
---

## Overview

Short-Term Rental (STR) real estate — Airbnb, VRBO, and similar
hospitality platforms — receives unique §469 treatment. Under
**Temp. Reg §1.469-1T(e)(3)(ii)(A)**, an activity is NOT a "rental
activity" for §469 purposes if the average period of customer use
is 7 days or less. Because §469(c)(2) imposes per-se passive
characterization on "rental activities," and because STR is not a
"rental activity" by definition, STR is NOT per-se passive.

The consequence: STR can be characterized as nonpassive if the
taxpayer materially participates under §469(h) and Temp. Reg
§1.469-5T (the seven material-participation tests). Material
participation requires:

- **500 hours** in the activity during the year, OR
- The taxpayer's participation **constitutes substantially all** of
  the participation by all individuals (including non-owner
  employees), OR
- The taxpayer participates **more than 100 hours and more than any
  other individual**, OR
- The taxpayer participates **more than 100 hours** in this and
  similar significant participation activities aggregating to >500
  hours, OR
- **Material participation in any 5 of the prior 10 years**, OR
- Personal service activity material participation in any 3 prior
  years (limited application), OR
- **Facts and circumstances** test (regular, continuous, substantial
  basis).

This is the "STR loophole" frequently marketed: an investor without
real-estate-professional status can convert their STR into
nonpassive via material participation, deducting STR losses
(typically created by cost-segregation-driven bonus depreciation)
against W-2 wages and other nonpassive income — without REPS
qualification.

The strategy hinges on:
1. Average period of customer use ≤7 days (verified property by
   property).
2. Material participation (typically the 100-hours-and-more-than-
   anyone-else test, or the 500-hours test).
3. Cost-seg study generating large first-year depreciation.

## Primary IRC authority

- **§469(a)** — General PAL disallowance.
- **§469(c)(1)** — "Passive activity" definition: any activity in
  which taxpayer does not materially participate.
- **§469(c)(2)** — Per-se passive treatment of "rental activities"
  (excludes STR by definition).
- **§469(h)** — Material participation.
- **§469(c)(7)** — REPS exception (alternative path).

## Treasury regulations

- **Temp. Reg §1.469-1T(e)(3)** — Definition of "rental activity"
  with average-period-of-customer-use exclusions.
- **Temp. Reg §1.469-1T(e)(3)(ii)(A)** — 7-day or less average
  period of customer use exclusion.
- **Temp. Reg §1.469-5T** — Material participation tests.
- **Reg §1.469-9** — REPS rules (alternative).

## Key IRS guidance

- **CCA 201427016** — Confirms STR not a rental activity if
  average customer use ≤7 days.
- **PLR 9505011** — Earlier confirmation.

## Key court decisions

- **Akers v. Commissioner, T.C. Memo. 2010-85** — STR/rental
  characterization.
- **Frank Aragona Trust v. Commissioner, 142 T.C. 165 (2014)** —
  Trust material participation analysis.
- **Bailey v. Commissioner, T.C. Memo. 2001-296** — Material
  participation hours documentation.

## Eligibility requirements

1. **Average period of customer use ≤7 days** during the year.
   Verified by examining each rental period.
2. **Material participation** under one of the seven §469(h) tests.
   The "100-hours-and-more-than-anyone-else" test is most commonly
   cited for STR.
3. **Schedule characterization.** Sch C if "substantial services"
   provided (hotel-like — daily housekeeping, breakfast, etc.).
   Otherwise Sch E. Sch C carries SE tax exposure; Sch E does not.
   Most STR is Sch E because typical Airbnb operations do not
   provide hotel-level services.
4. **No §469(c)(7) REPS required.** STR is not a rental activity,
   so REPS is not the path; material participation is.

## Mechanics — how it works

1. **Verify STR characterization.** Calculate average period of
   customer use. (Total days rented) / (number of rental periods).
2. **Cost-segregation study.** Generates substantial first-year
   bonus / §179 depreciation; creates significant losses.
3. **Document material participation.** Contemporaneous logs of
   hours: cleaning, maintenance, guest communication, listing
   management, repairs, etc.
4. **Schedule classification.** Sch E without SE tax (most common);
   Sch C with SE tax if substantial services.
5. **Annual analysis.** Material participation tested annually; STR
   characterization tested annually.

## Documentation requirements

- Rental booking records showing average customer use.
- Contemporaneous time logs.
- Property records.
- Cost-segregation study (if applicable).
- Form 8582 with material participation.

## Common pitfalls / audit risks

- **Average customer use exceeds 7 days.** Reverts to standard
  rental activity (per-se passive); REPS required for nonpassive
  treatment.
- **Insufficient material participation hours.** No bright-line; but
  property managers handling most operations defeats material
  participation in the property.
- **W-2 employment substantial.** Same issue as REPS — concurrent
  W-2 work undermines facts-and-circumstances test.
- **Sch C vs. Sch E mischaracterization.** Substantial services
  trigger SE tax.
- **§280A vacation-home interaction.** If owner uses property
  personally, §280A limits deductions.

## Recent legislative changes

- **TCJA (2017)** — Bonus depreciation and §179 expansion increased
  STR + cost-seg combination value.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §168(k)
  100% bonus]`. Restoration of 100% bonus would significantly
  increase STR strategy economics.

## State conformity considerations

State conformity to §469 is generally complete; STR characterization
flows. State SALT taxation of nonresident STR income varies.

## AICPA SSTS / Circular 230 considerations

STR is increasingly audit-targeted by IRS. Practitioner should
maintain rigorous time-log documentation and confirm 7-day
average annually.

## Default confidence band rationale

**MODERATE** — depends on factual support. HIGH for clearly-
documented under-7-day average and 500+ hours of material
participation. LOW for borderline customer-use averages or weak
participation documentation.

## Cross-references

- **`real-estate-professional`** (#20) — alternative path for
  long-term rentals.
- **`active-participation-real-estate`** (#3).
- **`cost-segregation`** (#41) — primary partner strategy.
- **`predict-material-participation`** (predict skill).
- **`rental-strategies`** (#25) — umbrella router.
- **`niit-minimization`** (#69) — STR with material participation
  may escape §1411 NIIT.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 469(c)(1)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Temp. Treas. Reg. § 1.469-1T(e)(3)(ii)(A)",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Temp. Treas. Reg. § 1.469-5T",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "CCA",
      "citation": "CCA 201427016",
      "url": "https://www.irs.gov/written-determinations",
      "weight": "written_determinations"
    }
  ]
}
```
```

---

## Strategy #27: Startup Cost Optimization

**File:** `references/strategies/startup-cost-optimization.md`

```markdown
---
name: "Startup Cost Optimization (§195 / §248 / §709)"
slug: startup-cost-optimization
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§195", "§248", "§709"]
forms: ["No specific form; election attached to first return"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

§195, §248, and §709 govern the treatment of pre-opening expenses:

- **§195** — "Start-up expenditures" of any active trade or
  business: investigation costs (whether to acquire or create) and
  pre-opening operating costs.
- **§248** — "Organizational expenditures" of a corporation:
  costs of incorporation, drafting bylaws, etc.
- **§709** — "Organization and syndication fees" of a partnership.

Under each provision, a taxpayer may:
1. **Deduct up to $5,000** of qualifying expenses in the year the
   business begins.
2. **Phase-out:** the $5,000 deduction reduces dollar-for-dollar
   above $50,000 of qualifying expenses; fully phased out at
   $55,000.
3. **Amortize the remainder** ratably over 180 months (15 years)
   beginning with the month the business begins.

The election is automatic — made by deducting up to $5,000 on the
first return; an explicit statement is no longer required (Reg
§1.195-1(b)).

Qualifying expenses must be:
1. Paid or incurred before the active trade or business begins.
2. Of a type that would be deductible under §162 if paid or
   incurred in connection with the operation of an existing active
   trade or business.

Common §195 startup expenses:
- Market research, feasibility studies.
- Travel and investigation costs.
- Pre-opening rent on facility.
- Pre-opening salaries (employees not yet generating revenue).
- Pre-opening utility deposits.
- Pre-opening advertising.
- Professional fees (legal, accounting) for investigation.

Notably NOT §195 — must be capitalized or expensed under other
rules:
- Property acquisition costs (capitalized to asset basis).
- Equipment purchases (depreciated under §168).
- Inventory.
- Costs to acquire intangibles (capitalized; §197 amortization).

## Primary IRC authority

- **§195** — Start-up expenditures.
- **§248** — Organizational expenditures (corporations).
- **§709** — Organization and syndication fees (partnerships).
- **§263** — General capitalization.
- **§197** — Intangible amortization.

## Treasury regulations

- **Reg §1.195-1** — Election rules; automatic election.
- **Reg §1.248-1** — Corporate organizational expenses.
- **Reg §1.709-1 and §1.709-2** — Partnership organization /
  syndication.

## Key IRS guidance

- IRS Publication 535 — Business Expenses.

## Key court decisions

- **Richmond Television Corp. v. United States, 354 F.2d 410 (4th
  Cir. 1965)** — Pre-opening expenses are capital items absent
  §195.

## Eligibility requirements

For §195:
1. Expenditure paid or incurred before active trade or business
   begins.
2. Expenditure of a type that would be deductible under §162.
3. Investigation, creation, or acquisition of an active trade or
   business.

## Mechanics — how it works

1. **Identify all pre-opening expenditures.**
2. **Categorize:** §195 startup, §248 organizational, §709
   partnership organization, capitalize to asset basis (real
   property, equipment, inventory), §197 intangible.
3. **Compute $5,000 deduction.** Apply phaseout.
4. **Amortize remainder over 180 months.**
5. **Track partial first-year amortization.** Begin in month
   business begins.
6. **State conformity check.**

## Documentation requirements

- Categorized list of pre-opening expenses.
- Documentation of "business begins" date.
- Amortization schedule.

## Common pitfalls / audit risks

- **Capital items expensed as §195.** Property acquisitions are
  basis, not §195.
- **Mischaracterization of §263A inventory costs.**
- **"Business begins" determination.** Critical for amortization
  start. For investigation that doesn't result in business, §195
  doesn't apply (capital loss instead).
- **Multi-year pre-opening period.** Each year tracked
  separately; amortization starts only when business begins.

## Recent legislative changes

- **American Jobs Creation Act of 2004** — Created the $5,000
  immediate deduction (replacing earlier 60-month amortization
  alone).
- **TCJA (2017)** — No direct §195 changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §195
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §195 / §248 / §709 is generally complete.

## AICPA SSTS / Circular 230 considerations

Standard diligence; routine planning area.

## Default confidence band rationale

**HIGH** — clear statutory framework, automatic election, settled
practice.

## Cross-references

- **`maximize-business-deductions`** (#13).
- **`bonus-and-section-179-depreciation`** (#12) — for capitalized
  equipment.
- **`prepayment-of-expense`** (#18) — coordination with timing.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 195",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section195",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 248",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section248",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 709",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section709",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.195-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    }
  ]
}
```
```

---

**End of Part 3 of 10.** Strategies #18 through #27 delivered.

**Continue to Part 4 of 10** for strategies #28 through #37 (De Minimis Safe Harbor, Deferred Sales Trust, Worthless Stock Ordinary Loss, C Corp Dividends, Capital Gain Offsets, Installment Sale, QOZ, C Corp State Tax Savings, EV Credits, Late Penalties/Interest).
