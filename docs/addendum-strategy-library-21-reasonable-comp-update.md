# Vibe CPA Skills — Strategy Library Supplement
# Strategy #21 — Reasonable Compensation (Updated and Expanded)

This supplement **replaces in full** the Strategy #21 file delivered in
Part 3 of the strategy library addendum. The existing Strategy #21 stub
(`references/strategies/reasonable-comp-corp-owners.md`) should be
overwritten with the content below. A new reference data file
(`references/strategies/data/cpe-wage-distribution-ratios.xlsx`) is
also delivered.

This update integrates:

1. **CPE-derived industry wage:distribution ratio table** — uploaded
   spreadsheet from a CPE event labeled "2025 IRS ATG Illustrative."
   See Provenance Disclaimer below; the table is included as a
   **practitioner heuristic**, not as IRS authority.
2. **Mayson Manufacturing 9-factor test** — the foundational
   multi-factor framework (1949).
3. **Elliotts 5-factor test** — the modern distilled framework (1983).
4. **Three valuation approaches** — Market, Income (independent investor
   test), and Cost — per the 2014 IRS Reasonable Compensation Job Aid.
5. **Recent court decisions** — Clary Hood (2022/2023), Sean McAlary
   (2013), Brewer Quality Homes, Veterinary Surgical Consultants,
   Radtke, Multi-Pak, Eberl's Claim Service, Paula Construction Co.,
   plus the Watson and Menard cases already in v1.
6. **IRC §7436 reclassification authority.**
7. **Treas. Reg. §1.162-7(a) and (b)(1)** — compensatory intent /
   disguised dividend doctrine.
8. **2014 IRS Reasonable Compensation Job Aid for IRS Valuation
   Professionals** — FOIA-released internal-use document. Includes
   explicit disclaimer prohibiting use as authority but provides
   significant insight into IRS examiner methodology.
9. **2005 IRS Compliance Study** — basis for current IRS audit focus.
10. **2025/2026 Social Security wage base correction** —
    $176,100 / $184,500 (the v1 file incorrectly cited 2024's
    $168,600).
11. **Practitioner data sources** — BLS Occupational Employment and
    Wage Statistics (OEWS), RCReports, AICPA *The Tax Adviser*
    October 2024 article.

---

## ⚠️ PROVENANCE DISCLAIMER — CPE Wage:Distribution Ratio Spreadsheet

The accompanying spreadsheet
(`references/strategies/data/cpe-wage-distribution-ratios.xlsx`)
was provided to a CPA practitioner during a Continuing Professional
Education (CPE) event. Its column headers reference a **"2025 IRS
ATG Illustrative" wage:distribution ratio by industry**.

**Important findings on document provenance:**

1. **There is no IRS-published 2025 Audit Techniques Guide that
   contains industry-specific wage:distribution ratio ranges** of the
   type shown in the spreadsheet. The IRS publishes a library of ATGs
   on irs.gov, none of which is a "2025 Reasonable Compensation ATG"
   with such tables.

2. **The actual official IRS internal reference** for IRS examiner
   methodology on reasonable compensation is the **"Reasonable
   Compensation Job Aid for IRS Valuation Professionals"** dated
   **October 29, 2014**, released to the public via Freedom of
   Information Act request. The Job Aid itself contains an explicit
   disclaimer:

   > "This Job Aid is not Official IRS position and was prepared for
   > reference purposes only; it may not be used or cited as authority
   > for setting any legal position."

3. **The 2014 Job Aid does not contain the industry-by-industry
   wage:distribution ratios shown in the CPE spreadsheet.** It
   contains only a general observation that "smaller firms and
   privately-held firms tend to pay a higher percentage of income as
   officers' compensation than do larger" firms.

4. **The "60/40 rule" — and similar fixed wage:distribution
   percentages — are explicitly identified as MYTHS** by AICPA, NATP,
   IRS-aligned commentators, and practitioner literature. Multiple
   AICPA practitioner articles and IRS-affiliated commentators
   (including Michael Gregory, the original IRS champion of the 2014
   Job Aid) confirm there is no IRS-approved wage:distribution
   percentage safe harbor.

**How to use the CPE spreadsheet:**

- ✅ As a **practitioner heuristic** for industry-typical patterns
  observed in audit and litigation outcomes.
- ✅ As a **starting point for risk-band assessment** (the spreadsheet's
  "Risk Level if Below Range" column reflects practitioner experience).
- ✅ As a **conversation tool with clients** to anchor expectations
  about typical defensible ranges.
- ❌ **NOT** as a substitute for the Mayson 9-factor / Elliotts
  5-factor analysis required by case law.
- ❌ **NOT** as IRS-published authority — the "2025 IRS ATG"
  attribution does not match any actual IRS document.
- ❌ **NOT** as a safe harbor — no fixed percentage protects against
  reclassification.

**Recommended replacement caption** for the spreadsheet when used in
client deliverables: "Practitioner-Synthesized Wage:Distribution
Heuristic by Industry (CPE-derived; not IRS authority). Derived from
case law patterns and practitioner experience."

If presenting to a client or examiner, **do not** caption the
spreadsheet as IRS-published. Caption it accurately as a practitioner
heuristic. Misrepresenting source authority risks SSTS §1.4
violations and Circular 230 §10.22 / §10.51 exposure.

---

## File: `references/strategies/reasonable-comp-corp-owners.md`

```markdown
---
name: "Reasonable Compensation for S Corp / C Corp Owner-Employees"
slug: reasonable-comp-corp-owners
type: Wage Plan
tax_type: 2SH
complexity: High
irc_sections: ["§162(a)(1)", "§3121", "§3121(d)", "§7436", "§531", "§541", "§409A"]
forms: ["W-2", "Form 1120-S", "Form 1120", "Form 941", "Form 944"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
ss_wage_base_2025: 176100
ss_wage_base_2026: 184500
references:
  - "data/cpe-wage-distribution-ratios.xlsx (CPE-derived practitioner heuristic; not IRS authority)"
  - "https://www.irs.gov/pub/irs-lbi/Reasonable%20Compensation%20Job%20Aid%20for%20IRS%20Valuation%20Professionals.pdf"
  - "https://www.thetaxadviser.com/issues/2024/oct/advising-s-corporation-clients-on-reasonable-compensation/"
---

> **Caution:** Reasonable compensation is one of the most heavily-
> audited issues for S corporations and closely-held C corporations.
> The IRS uses AI-driven case selection and has consolidated S corp
> compensation enforcement into a specialized team within the
> Employment Tax Program. The "60/40 rule" and similar fixed-percentage
> safe harbors are myths — there is no IRS-published industry-specific
> wage:distribution ratio table. Each determination requires a
> documented Mayson 9-factor or Elliotts 5-factor analysis, supported
> by Market, Income, or Cost approach valuation per the 2014 IRS Job
> Aid methodology.

## Overview

Reasonable compensation analysis arises in two distinct but related
contexts:

1. **S corporation shareholder-employee underpayment.** §162(a)(1)
   permits deduction of "a reasonable allowance for salaries or
   other compensation for personal services actually rendered."
   §3121(d)(1) classifies an officer of a corporation as an employee
   for FICA purposes. When an S corp shareholder-employee receives
   distributions in lieu of (or in addition to) inadequate W-2 wages,
   the IRS may use its §7436 authority to reclassify the
   distributions as wages, triggering employer + employee FICA
   (15.3% combined), Additional Medicare Tax, FUTA, plus penalties
   and interest. The seminal cases are **Watson v. United States,
   668 F.3d 1008 (8th Cir. 2012)** and **Sean McAlary Ltd., Inc.
   v. Commissioner, T.C. Sum. Op. 2013-62**.

2. **C corporation shareholder-employee overpayment.** Closely-held
   C corps have the opposite incentive: pay the owner more salary
   (deductible to corp; ordinary income to owner) and less dividend
   (non-deductible at corp; double-taxed). The IRS challenges
   excessive compensation under Treas. Reg. §1.162-7(b)(1)
   (excessive comp may be disguised dividend). The seminal cases
   include **Mayson Manufacturing Co. v. Commissioner, 178 F.2d 115
   (6th Cir. 1949)**, **Elliotts, Inc. v. Commissioner, 716 F.2d
   1241 (9th Cir. 1983)**, **Exacto Spring Corp. v. Commissioner,
   196 F.3d 833 (7th Cir. 1999)**, and most recently **Clary Hood,
   Inc. v. Commissioner, T.C. Memo. 2022-15, aff'd in part, 69 F.4th
   168 (4th Cir. 2023)**.

The same multi-factor framework applies in both directions. A salary
that is "reasonable" should fall within the same defensible range
whether the IRS is arguing for more (S corp) or less (C corp).

For S corp owners, the planning lever is the **wages-vs-distribution
split**. Setting wages too low triggers §7436 reclassification; setting
them too high forfeits the SE tax savings that drove the S corp
election. The optimal point is the lowest defensible wage that:

- Reflects fair market compensation for services actually performed.
- Is supported by Mayson 9-factor / Elliotts 5-factor analysis.
- Is documented contemporaneously with one of the three valuation
  approaches.
- Compares favorably to BLS OEWS data, RCReports output, or
  comparable industry surveys.

The **Social Security wage base for 2025 is $176,100**; for **2026
is $184,500**. Wages up to the wage base bear 12.4% OASDI; wages
above bear only 2.9% Medicare (plus 0.9% Additional Medicare on
wages above $200,000 single / $250,000 MFJ).

## Primary IRC authority

- **§162(a)(1)** — Reasonable allowance for salaries or other
  compensation. Provides corporate deduction.
- **§3121(a)** — Definition of FICA wages: "all remuneration for
  employment, including the cash value of all remuneration."
- **§3121(d)(1)** — Officer of a corporation is an employee.
- **§3121(d)(2)** — Common-law employee.
- **§3306(a)** — FUTA wages.
- **§7436** — IRS authority to determine worker classification and
  to reclassify distributions / payments as wages. Tax Court
  jurisdiction over §7436 determinations.
- **§3402** — Income tax withholding on wages.
- **§531** — Accumulated earnings tax (C corp context; interaction
  with reasonable comp).
- **§541** — Personal holding company tax (C corp context).
- **§269A** — Personal service corporation reallocation (C corp
  context).
- **§409A** — Deferred compensation (interaction).
- **§199A** — QBI deduction (interaction; W-2 wage limit at
  higher incomes).

## Treasury regulations

- **Treas. Reg. §1.162-7(a)** — General rule: deductibility of
  compensation requires that the payment be (i) reasonable in amount
  and (ii) actually for services rendered. **Compensatory intent
  doctrine.**
- **Treas. Reg. §1.162-7(b)(1)** — Excessive comp may be disguised
  dividend: "An ostensible salary paid by a corporation may be a
  distribution of a dividend on stock. This is likely to occur in
  the case of a corporation having few shareholders, practically
  all of whom draw salaries."
- **Treas. Reg. §1.162-7(b)(3)** — "Reasonable" defined: "Such
  amount as would ordinarily be paid for like services by like
  enterprises under like circumstances." This is the **anchor
  definition** of reasonable compensation.
- **Treas. Reg. §31.3121(d)-1(b)** — Officer as employee; even minor
  services for remuneration trigger employee status.
- **Treas. Reg. §31.3121(d)-2** — Common law employee tests.

## Key IRS guidance

- **Reasonable Compensation Job Aid for IRS Valuation Professionals**
  (October 29, 2014; FOIA-released) — Internal IRS reference
  document. **Explicit disclaimer that it is NOT IRS authority.**
  Covers the three valuation approaches (Market, Income, Cost),
  factor analysis, suggested data sources, and case examples.
  Companion to the Job Aid is a 54-page Appendix with example
  applications. URL:
  `https://www.irs.gov/pub/irs-lbi/Reasonable%20Compensation%20Job%20Aid%20for%20IRS%20Valuation%20Professionals.pdf`

- **IRS Fact Sheet 2008-25** — "Wage Compensation for S Corporation
  Officers." Establishes that S corp officers performing more than
  minor services must receive reasonable compensation.

- **IRS Form 1120-S Instructions** — "Distributions and other
  payments by an S corporation to a corporate officer must be
  treated as wages to the extent the amounts are reasonable
  compensation for services rendered to the corporation."

- **2005 IRS S Corporation Reporting Compliance Study** — IRS
  internal study that triggered the modern shift in audit focus
  from all-or-nothing reclassification to **proportional
  reclassification** based on reasonableness of comp relative to
  services.

- **Technical Advice Memorandum 9326001** — Incorporates Mayson
  factors into IRS examiner guidance for C corp executive
  compensation.

- **Rev. Proc. 80-21** — Compensation in C corp context (older but
  still cited).

- **IRS S Corp Officer Compensation Webpage** — IRS.gov page
  "S Corporation Compensation and Medical Insurance Issues" lists
  factors and cites Watson, Veterinary Surgical Consultants, Joly,
  Spicer, and others.

- **IRS Treasury / SBA Statistics** — Approximately **5.9 million
  S corporation returns** filed for FY2023, of which roughly **73%
  of S corp audits focus on reasonable compensation** (per
  practitioner reports of IRS audit-frequency statistics). S corps
  are audited at approximately **2× the rate of sole
  proprietorships** for compensation-related issues.

## Three valuation approaches (per 2014 Job Aid)

The 2014 Reasonable Compensation Job Aid identifies three valuation
approaches an IRS examiner (or practitioner) should consider:

### 1. Market Approach (preferred by IRS)

Compares the subject employee's compensation to compensation paid
to similarly-situated employees performing similar duties at
similar companies. The Job Aid favors this approach when reliable
comparable data is available.

**Data sources:**
- Bureau of Labor Statistics **Occupational Employment and Wage
  Statistics (OEWS)** — most authoritative free source; covers
  ~800 occupations × every U.S. metro / non-metro area; updated
  annually.
- Industry trade association salary surveys (AMA, ACG, AICPA, AMA
  Manufacturing Compensation Survey, etc.).
- **RCReports** — proprietary practitioner subscription using a
  modified Cost Approach with 800+ occupations × every U.S. county.
- Public company proxy statements / annual reports (for larger
  companies; less useful for typical small business).
- Risk Management Association (RMA) Annual Statement Studies.
- Dun & Bradstreet compensation data.
- Salary.com, Glassdoor, BLS OEWS — for hourly / cost approach
  inputs.

**Limitations:**
- Comparable data is sparse for small / closely-held firms.
- The Job Aid notes that **reconciliation in the case of Reasonable
  Compensation will generally rest heavily on the market approach**.
- However, **Sean McAlary Ltd., Inc. v. Commissioner, T.C. Sum. Op.
  2013-62** rejected the market approach where the IRS expert's
  comparable data inappropriately mixed gross-receipts-based and
  net-sales-based ratios.

### 2. Income Approach (Independent Investor Test)

Originated in **Exacto Spring Corp. v. Commissioner, 196 F.3d 833
(7th Cir. 1999)**. Asks whether a hypothetical independent investor
would be satisfied with the company's return on investment after
the compensation in question.

**Mechanics:**
- Determine business value (using DCF, market multiples, or other
  valuation methods).
- Determine the rate of return on equity that would satisfy a
  hypothetical investor.
- If actual ROE materially exceeds that threshold, compensation is
  presumed reasonable (rebuttable presumption).
- If actual ROE is below threshold, compensation may be excessive
  (suggesting disguised dividend in C corp) or insufficient
  (suggesting reasonable wages have been mischaracterized as
  distributions in S corp).

**Limitations:**
- Requires business valuation (potentially $3,000-$10,000 in
  professional fees).
- Time-intensive and subjective.
- **Multi-Pak v. Commissioner, T.C. Memo. 2010-139** held that the
  independent investor test alone does not control; it is one of
  several factors. Tax Court ruled against taxpayer where ROE was
  only 2.9% (2002) / -15.8% (2003).
- **Owensby & Kritikos, Inc. v. Commissioner, 819 F.2d 1315 (5th
  Cir. 1987)** — "The so-called independent investor test is simply
  one of the factors a court should consider, and in certain cases
  it may be a substantial factor."

### 3. Cost Approach (Replacement Cost / Task-Based)

Decomposes the owner's role into discrete tasks (administration,
sales, accounting, marketing, operations, etc.), assigns a market
hourly or salary rate to each task, multiplies by hours, and sums.

**Mechanics:**
- Identify all tasks performed by the owner.
- Allocate the owner's annual hours across tasks.
- Determine market rate for each task (BLS OEWS, salary surveys).
- Multiply (hours × rate) for each task and sum.
- Result is the cost to **replace** the owner's services with
  comparable employees.

**Strengths:**
- Practical for small businesses where comparable Market data is
  unavailable.
- Used and accepted in **Sean McAlary Ltd., Inc.** after the
  Market Approach was rejected.
- **RCReports** uses this methodology.

**Limitations:**
- Reliant on owner self-reporting of hours (subject to bias).
- Time-intensive.
- May understate value of integrated owner-managers (who may be
  worth more as a unit than the sum of replacement employees).

### Reconciliation

Per the Job Aid: "Although standard appraisal practice requires
the consideration of all three approaches, the reconciliation in
the case of Reasonable Compensation will generally rest heavily on
the market approach (comparison to compensation paid to executives
in comparable positions at comparable companies)."

In practice, practitioners often perform Market and Cost in
parallel, with Income reserved for higher-stakes engagements.

## Key court decisions — multi-factor framework

### The Mayson 9-Factor Test (1949)

**Mayson Manufacturing Co. v. Commissioner, 178 F.2d 115 (6th Cir.
1949)** — The seminal case establishing the multi-factor framework.
The Sixth Circuit identified the following nine factors:

1. **The employee's qualifications.** Education, training,
   experience, certifications.
2. **The nature, extent, and scope of the employee's work.** Hours
   worked; specific duties; supervision exercised; revenue
   generated.
3. **The size and complexity of the business.** Revenue; employee
   headcount; geographic scope; regulatory complexity.
4. **A comparison of salaries paid with gross income and net
   income.** Wage as percentage of revenue and profit.
5. **Prevailing general economic conditions.** Industry cycles;
   inflation; pay trends.
6. **A comparison of salaries with distributions to stockholders.**
   The dividend / distribution history relative to comp.
7. **Prevailing rates of compensation for comparable positions in
   comparable concerns.** Market data.
8. **The employer's salary policy as to all employees.** Internal
   pay equity; whether the comp follows a structured policy.
9. **The amount of compensation paid to the employee in previous
   years** (for small corporations with a limited number of
   officers). Year-over-year consistency or sudden spikes.

The court explicitly held: **"the situation must be considered as a
whole with no single factor decisive."**

### The Elliotts 5-Factor Distillation (1983)

**Elliotts, Inc. v. Commissioner, 716 F.2d 1241 (9th Cir. 1983)** —
The Ninth Circuit consolidated the Mayson factors into five:

1. **The employee's role in the company.** Position, hours, duties,
   importance to operations.
2. **External comparison.** Compensation compared to similar
   companies for similar services.
3. **The character and condition of the company.** Size, complexity,
   profitability.
4. **Conflict of interest / Independent investor test.** Whether a
   relationship between company and employee permits disguising
   nondeductible distributions as deductible compensation.
5. **Internal consistency of compensation.** Whether the
   compensation was paid pursuant to a structured, formal, and
   consistently applied program.

The Elliotts framework has become the dominant analytical structure
in modern reasonable-compensation litigation.

### Other Multi-Factor Variants

- **Eberl's Claim Service, Inc. v. Commissioner (10th Cir.)** —
  Twelve-factor analysis affirmed; held compensation included
  non-deductible disguised dividends.
- **Foos v. Commissioner** — Twenty-one factor test (an outlier;
  not commonly followed).

In all variants, **no single factor is decisive**.

## Key court decisions — specific cases

### S Corporation Underpayment Cases (IRS Wins)

- **Watson v. United States, 668 F.3d 1008 (8th Cir. 2012), cert.
  denied, 568 U.S. 888 (2012)** — CPA paid himself $24,000 salary
  on ~$200,000+ in distributions. IRS expert determined reasonable
  compensation of $91,044. Eighth Circuit held: intent to limit
  wages is not controlling; the test is whether the payments
  received were truly remuneration for services performed. **The
  most-cited modern case.**

- **Sean McAlary Ltd., Inc. v. Commissioner, T.C. Sum. Op. 2013-62**
  — Real estate agency owner paid himself $24,000 on substantial
  S corp profit. Tax Court rejected the IRS's Market Approach
  (because the IRS expert mixed gross-receipts and net-sales
  ratios incorrectly) but accepted the Cost Approach, ultimately
  determining reasonable compensation of approximately $83,200 for
  the year. **Important precedent for the Cost Approach.**

- **Joseph M. Grey Public Accountant, P.C. v. Commissioner, 119
  T.C. 121 (2002), aff'd 93 Fed. Appx. 473 (3d Cir. 2004)** —
  CPA firm paid sole shareholder no wages, only "dividend"
  distributions. Tax Court reclassified entire distribution as
  wages.

- **Spicer Accounting, Inc. v. United States, 918 F.2d 90 (9th
  Cir. 1990)** — Sole accountant paid himself dividends only,
  claiming services were "donated." Court reclassified.

- **Radtke v. United States, 712 F. Supp. 143 (E.D. Wis. 1989),
  aff'd, 895 F.2d 1196 (7th Cir. 1990)** — Attorney sole
  shareholder of S corp law practice paid $0 salary; received
  "dividends" instead. Court held all "dividends" were wages
  subject to FICA and FUTA.

- **Veterinary Surgical Consultants, P.C. v. Commissioner, 117
  T.C. 141 (2001)** — Sole shareholder veterinary surgeon paid
  no salary; took distributions. Court held distributions were
  wages; rejected attempt to characterize as non-wage dividends.

- **Joly v. Commissioner, T.C. Memo. 1998-361, aff'd by unpub.
  op., 211 F.3d 1269 (6th Cir. 2000)** — Shareholder-employee
  used company bank account for personal use; payments classified
  as wages.

- **Glass Blocks Unlimited v. Commissioner, T.C. Memo. 2013-180**
  — Sole shareholder reclassified distributions as wages.

- **JD & Associates, Ltd. v. United States, No. 3:04-CV-59 (D.N.D.
  2006)** — North Dakota district court reclassified distributions
  as wages; substantial penalties imposed.

- **Roob v. Commissioner** — Underscored IRS authority to
  reclassify under §7436.

- **Gale W. Greenlee, Inc. v. United States, 661 F. Supp. 642 (D.
  Colo. 1985)** — "Loans" from S corp to sole shareholder
  reclassified as wages.

### C Corporation Overpayment Cases

- **Mayson Manufacturing Co. v. Commissioner, 178 F.2d 115 (6th
  Cir. 1949)** — Foundational 9-factor case (above).

- **Elliotts, Inc. v. Commissioner, 716 F.2d 1241 (9th Cir.
  1983)** — 5-factor distillation (above).

- **Exacto Spring Corp. v. Commissioner, 196 F.3d 833 (7th Cir.
  1999)** — Independent investor test originator; held that
  multi-factor tests are "redundant, incomplete, and unclear" and
  that the independent investor test should be primary. Posner
  opinion.

- **Owensby & Kritikos, Inc. v. Commissioner, 819 F.2d 1315 (5th
  Cir. 1987)** — Compensation found unreasonable; independent
  investor test as one factor among many.

- **Brewer Quality Homes, Inc. v. Commissioner, T.C. Memo.
  2003-200** — Mobile home retailer; Tax Court determined
  reasonable compensation at 90th percentile of officer
  compensation per Risk Management Association data. Combined
  Mayson and Owensby factor analysis.

- **Menard, Inc. v. Commissioner, 560 F.3d 620 (7th Cir. 2009)**
  — Home improvement retailer; Seventh Circuit reversed Tax Court
  finding of unreasonable compensation; applied Exacto independent
  investor test favorably to Menard.

- **Multi-Pak Corp. v. Commissioner, T.C. Memo. 2010-139** —
  Independent investor test applied; ruled against taxpayer where
  ROE was only 2.9% (2002) and -15.8% (2003).

- **Clary Hood, Inc. v. Commissioner, T.C. Memo. 2022-15, aff'd in
  part, 69 F.4th 168 (4th Cir. 2023)** — **Most significant recent
  decision.** South Carolina excavating company; founder paid
  himself $5M and $7M in two years. Tax Court applied Elliotts
  5-factor test; held portion of compensation excessive; Fourth
  Circuit affirmed in part. **Key practitioner takeaway:** modern
  C corp comp challenges still alive; courts apply Elliotts/Mayson
  rigorously even for highly profitable family businesses.

- **Paula Construction Co. v. Commissioner, 58 T.C. 1055 (1972)**
  — **Compensatory intent doctrine.** Payments initially recorded
  as distributions cannot later be reclassified as compensation
  due to lack of contemporaneous compensatory intent. **Critical
  case for documentation discipline.**

- **Pediatric Surgical Associates, P.C. v. Commissioner, T.C.
  Memo. 2001-81** — Group medical practice; "services rendered"
  test applied.

- **Rapco Inc. v. Commissioner, 85 F.3d 950 (2d Cir. 1996)** —
  Multi-factor analysis; deductibility of compensation.

- **Nor-Cal Adjusters v. Commissioner, 503 F.2d 359 (9th Cir.
  1974)** — Mayson factors applied.

- **Mulcahy, Pauritsch, Salvador & Co., Ltd. v. Commissioner,
  T.C. Memo. 2011-74** — Accounting firm; Tax Court found
  compensation excessive.

- **Guy Schoenecker, Inc. v. Commissioner, T.C. Memo. 1995-539**
  — Independent investor analysis modified given facts.

## Eligibility requirements / Trigger conditions

For S corp shareholder-employees:

1. **Shareholder performs more than minor services.** Treas. Reg.
   §31.3121(d)-1(b) — even minor services trigger employee status.
2. **Cash or property received from the corporation** (whether
   labeled wages, distributions, loans, or other).
3. **No W-2 wages** OR **W-2 wages disproportionately low**
   relative to services and profitability.

For C corp shareholder-employees (overpayment context):

1. **Shareholder controls or significantly influences own
   compensation.**
2. **Compensation materially exceeds market comparables.**
3. **Distributions / dividends are minimal** despite profitability
   (suggesting disguised dividend in compensation).

## Mechanics — how to set defensible compensation

### Annual Process

1. **Document the shareholder-employee's role.** Job description;
   duties; hours worked; revenue generated directly; supervisory
   responsibilities.

2. **Apply the Mayson 9-factor or Elliotts 5-factor analysis.**
   Document each factor in a memo or workbook.

3. **Run at least one of the three valuation approaches:**
   - **Market Approach (preferred):** Pull BLS OEWS data for the
     applicable SOC code in the applicable metro area. Pull
     industry trade association salary surveys. Compare.
   - **Cost Approach:** Decompose owner's tasks; assign hours;
     apply market rates per task; sum. (RCReports automates this.)
   - **Income Approach:** For higher-stakes engagements; requires
     business valuation and ROE benchmarking.

4. **Cross-check against industry pattern heuristics.** The CPE
   wage:distribution ratio table (in `data/cpe-wage-distribution-
   ratios.xlsx`) provides directional benchmarks. **Use as
   sanity-check, not as authority.** If the proposed wage:
   distribution split materially deviates from the practitioner
   pattern, document the basis for the deviation.

5. **Document compensatory intent at time of payment.** Per Paula
   Construction Co.: Cannot retroactively recharacterize
   distributions as wages. Pay W-2 wages on a regular schedule
   (monthly, semi-monthly, or per pay-period); issue Form W-2;
   file Form 941 / 944; remit FICA timely.

6. **Adopt formal corporate action.** Board of directors resolution
   (or sole-shareholder consent) approving annual compensation.
   Board minutes documenting the analysis.

7. **Coordinate with §199A QBI planning.** At higher incomes
   (above $191,950 single / $383,900 MFJ for 2025), the QBI W-2
   wage limitation applies. Higher S corp wages may increase the
   QBI limit even as they increase FICA.

8. **Annual review.** Compensation should be revisited each year
   based on revenue growth, role changes, and updated market data.

### Year-end pitfalls to avoid

- Setting compensation **below the prior employee** doing the same
  job.
- **Zero salary** (Radtke / Veterinary Surgical / Joseph M. Grey
  pattern).
- **Distributions exceeding salary by more than ~5×** without
  substantial non-shareholder labor explanation.
- Calling regular owner draws "**loans**" (Greenlee pattern).
- **Inconsistent compensation** across years without documented
  basis (sudden drops in profit-down years can also be flagged).
- **Compensation set without contemporaneous documentation**
  (Paula Construction Co. compensatory intent doctrine).

## Documentation requirements

A defensible reasonable compensation file should contain, at
minimum:

1. **Annual reasonable compensation analysis memo.**
   - Job description and duties.
   - Hours allocation by task (for Cost Approach).
   - Market data references (BLS OEWS query outputs; salary
     survey citations).
   - Mayson 9-factor or Elliotts 5-factor analysis.
   - Conclusion with stated wage range and recommended point
     within range.

2. **Board / shareholder approval.** Resolution authorizing
   compensation; minutes if multiple owners.

3. **Payroll records.** Form 941 / 944; W-2; pay stubs; FICA
   deposit records.

4. **Comparison to non-shareholder employees** (where applicable).
   Demonstrates internal salary-policy consistency.

5. **Time records or task allocation worksheet** (especially for
   Cost Approach).

6. **Updated annually.** Each year's analysis should reflect
   current revenue, role, and market data.

For practitioner deliverables, the **CPE wage:distribution ratio
table** can serve as an exhibit labeled clearly as a practitioner
heuristic — never as IRS authority.

## Common pitfalls / audit risks

- **Ratio-based shortcuts.** Setting comp at "60/40" or any other
  fixed percentage. **The 60/40 rule is a myth** (per AICPA, NATP,
  and Michael Gregory, the original IRS Job Aid champion). No IRS
  safe harbor.

- **Form 1099 to oneself.** Some owners issue Form 1099 instead
  of Form W-2 to attempt to avoid FICA. The IRS will challenge:
  shareholder-employee per §3121(d)(1) is a W-2 employee.

- **Loans to shareholder.** Repeated, undocumented "loans" with
  no repayment terms or interest will be reclassified as
  constructive dividends or wages (see Greenlee, Shor cases).

- **Health insurance coordination errors.** Health insurance for
  2%+ shareholders must be added to W-2 Box 1 (per §1372 / Notice
  2008-1) but is not subject to FICA — see Strategy #10.

- **State conformity differences.** California has distinct rules
  on S corp officer compensation; some states treat S corps as C
  corps for state tax (Tennessee F&E tax; New Hampshire BPT).

- **Pre-OBBBA §199A interaction.** W-2 wage limitation at
  higher incomes may push optimal wage higher than pure SE-tax
  optimization would suggest.

- **Reasonable comp set in a profitable year, then unchanged.**
  Sudden profit increases without comp adjustment may signal
  underpayment.

- **Compensatory intent.** Paula Construction Co. — cannot
  retroactively recharacterize distributions as wages. Set comp
  in advance; pay through payroll on a schedule; document
  contemporaneously.

- **Multi-shareholder S corps.** Each shareholder-employee needs
  individual reasonable comp analysis. Cannot use ownership
  percentage as proxy.

- **Family employment.** Wages to spouses / children must
  separately satisfy reasonable comp standards (Eller; Denman) —
  see Strategies #49, #50, #94.

- **Late filing of payroll returns.** Form 941 / W-2 deadlines are
  strict; failure to file adds penalty exposure on top of
  reclassification.

## Recent legislative changes

- **TCJA (2017)** — Created §199A QBI deduction, which added a
  new dimension to the optimal wage analysis. Higher wages reduce
  K-1 QBI but may increase the W-2 wage limitation at higher
  incomes.

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §199A QBI
  permanence Pub L 119-21]`. Reports indicate OBBBA made §199A
  permanent and may have adjusted W-2 wage limitation thresholds.
  Verify before relying.

- **2025 Social Security wage base: $176,100.** Up from $168,600
  in 2024. Maximum employer + employee combined OASDI: $21,836.40.

- **2026 Social Security wage base: $184,500.** Up 4.77% from 2025.

## State conformity considerations

State conformity to federal reasonable compensation framework is
generally complete for income tax purposes. However:

- **California** — 1.5% S corp franchise tax applies regardless of
  comp structure. CA EDD has its own reasonable comp focus for
  state SDI / UI purposes.

- **New York** — S corp election must be made separately for state
  purposes.

- **Tennessee** — Excise and franchise tax on S corp net earnings;
  no federal-state distinction on reasonable comp.

- **New Hampshire** — Business Profits Tax (BPT) on S corp;
  reasonable comp deduction permitted but limited.

- **Texas** — Franchise tax based on margin; reasonable comp
  factors into total margin.

- **Massachusetts** — S corp net income above threshold subject to
  MA corporate excise; comp structure matters.

- **State payroll tax bases.** SUI / SDI wage bases vary by state
  and may differ materially from federal SS base.

- **State minimum wage / labor law.** State-level requirements may
  set a floor below which W-2 wages cannot reasonably be
  characterized as legitimate full-time compensation.

## AICPA SSTS / Circular 230 considerations

Reasonable compensation is one of the **highest-stakes practitioner
risk areas** in pass-through entity practice:

- **SSTS §1.4 Use of Estimates.** Practitioner must have a
  reasonable basis for the comp number; pure guesswork or
  percentage-of-profit shortcuts may not satisfy.
- **SSTS §1.6 Knowledge of Error.** If practitioner becomes aware
  that prior-year comp was unreasonable, must advise client and
  document.
- **Circular 230 §10.22 (Diligence as to Accuracy).** Applies to
  comp positions on Form 1120-S.
- **Circular 230 §10.34 (Standards for Tax Returns).** Realistic
  possibility of success / substantial authority requirement.
- **§6694 Preparer Penalty.** Unreasonable position on comp can
  trigger preparer penalty (typically $1,000 or 50% of fee per
  return for unreasonable position; $5,000+ for willful conduct).
- **Form 8275 disclosure.** Consider for borderline positions.

**Practitioner best practice:**
- Annual written engagement letter component covering reasonable
  comp.
- Annual analysis memo retained in workpapers.
- Use of recognized methodology (Market, Cost, or Income).
- Explicit avoidance of "60/40" or other percentage shortcut
  language in workpapers.
- Client signoff on the analysis and conclusion.

## Default confidence band rationale

**MODERATE** — fact-intensive issue with substantial litigation
exposure. Confidence rises to **HIGH** when:
- Mayson 9-factor or Elliotts 5-factor analysis is documented.
- Recognized valuation approach (Market / Cost / Income) is applied.
- Compensation is paid through W-2 payroll on a regular schedule.
- Annual board / shareholder approval is documented.
- Compensation is at or above industry median per BLS OEWS or
  comparable surveys.

Confidence falls to **LOW** when:
- Zero or minimal salary with substantial distributions.
- No contemporaneous documentation.
- Owner-worker performing substantial services with no W-2 wages.
- Compensation set below prior non-owner employee in same role.
- Retroactive recharacterization of distributions as wages
  attempted (Paula Construction Co. trap).

## Cross-references

- `health-insurance-s-corp` (#10) — 2%+ shareholder health insurance
  W-2 reporting interaction.
- `qbi-deduction` (#19) — W-2 wage limitation at high incomes.
- `accountable-plan-home-office` (#2) — separate-from-comp expense
  reimbursement.
- `business-vehicle-usage` (#4) — separate-from-comp vehicle
  expense reimbursement.
- `reimbursement-of-business-expenses` (#22) — accountable plan
  framework.
- `c-corp-dividends` (#31) — disguised dividend doctrine.
- `c-corp-misc-deductions` (#42) — C corp comp interaction.
- `choice-of-entity-se-tax` (#86) — entity-level analysis.
- `minimize-self-employment-tax` (#90) — broader SE tax
  minimization.
- `hiring-kids` (#49) — family wages substance.
- `wages-spouse-parents` (#50) — family wages substance.
- `defined-benefit-cash-balance` (#73) — high comp + DB stack.
- `solo-401k-employer-contributions` (#82) — comp drives plan
  contribution capacity.
- `predict-reasonable-comp` (predict skill) — programmatic
  application.

## References (data files and external links)

- `data/cpe-wage-distribution-ratios.xlsx` — CPE-derived practitioner
  heuristic. **Not IRS authority. See Provenance Disclaimer.**
- IRS Reasonable Compensation Job Aid (October 29, 2014):
  https://www.irs.gov/pub/irs-lbi/Reasonable%20Compensation%20Job%20Aid%20for%20IRS%20Valuation%20Professionals.pdf
- IRS Fact Sheet 2008-25: https://www.irs.gov/pub/irs-news/fs-08-25.pdf
- IRS S Corporation Officer Compensation page:
  https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-employees-shareholders-and-corporate-officers
- The Tax Adviser, October 2024, "Advising S corporation clients
  on reasonable compensation":
  https://www.thetaxadviser.com/issues/2024/oct/advising-s-corporation-clients-on-reasonable-compensation/
- BLS Occupational Employment and Wage Statistics:
  https://www.bls.gov/oes/
- RCReports (commercial; subscription):
  https://rcreports.com/

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 162(a)(1)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section162","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 3121(a)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section3121","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 3121(d)(1)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section3121","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 7436","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7436","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 199A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section199A","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.162-7(a)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.162-7(b)(1)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.162-7(b)(3)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 31.3121(d)-1(b)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"FactSheet","citation":"IRS Fact Sheet 2008-25","url":"https://www.irs.gov/pub/irs-news/fs-08-25.pdf","weight":"irs_published"},
    {"authority_type":"JobAid","citation":"Reasonable Compensation Job Aid for IRS Valuation Professionals (Oct. 29, 2014)","url":"https://www.irs.gov/pub/irs-lbi/Reasonable%20Compensation%20Job%20Aid%20for%20IRS%20Valuation%20Professionals.pdf","weight":"irs_internal_non_authority","disclaimer":"Job Aid is not Official IRS position; may not be cited as authority."},
    {"authority_type":"TAM","citation":"Technical Advice Memorandum 9326001","url":"https://www.irs.gov","weight":"irs_internal"},
    {"authority_type":"CtAppeals","citation":"Mayson Manufacturing Co. v. Commissioner, 178 F.2d 115 (6th Cir. 1949)","url":"https://www.courtlistener.com","weight":"binding_circuit","note":"Foundational 9-factor test"},
    {"authority_type":"CtAppeals","citation":"Elliotts, Inc. v. Commissioner, 716 F.2d 1241 (9th Cir. 1983)","url":"https://www.courtlistener.com","weight":"binding_circuit","note":"5-factor distillation"},
    {"authority_type":"CtAppeals","citation":"Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)","url":"https://www.courtlistener.com","weight":"binding_circuit","note":"S corp underpayment leading case"},
    {"authority_type":"CtAppeals","citation":"Exacto Spring Corp. v. Commissioner, 196 F.3d 833 (7th Cir. 1999)","url":"https://www.courtlistener.com","weight":"binding_circuit","note":"Independent investor test originator"},
    {"authority_type":"CtAppeals","citation":"Owensby & Kritikos, Inc. v. Commissioner, 819 F.2d 1315 (5th Cir. 1987)","url":"https://www.courtlistener.com","weight":"binding_circuit"},
    {"authority_type":"CtAppeals","citation":"Menard, Inc. v. Commissioner, 560 F.3d 620 (7th Cir. 2009)","url":"https://www.courtlistener.com","weight":"binding_circuit"},
    {"authority_type":"CtAppeals","citation":"Spicer Accounting, Inc. v. United States, 918 F.2d 90 (9th Cir. 1990)","url":"https://www.courtlistener.com","weight":"binding_circuit"},
    {"authority_type":"CtAppeals","citation":"Radtke v. United States, 895 F.2d 1196 (7th Cir. 1990)","url":"https://www.courtlistener.com","weight":"binding_circuit"},
    {"authority_type":"CtAppeals","citation":"Clary Hood, Inc. v. Commissioner, 69 F.4th 168 (4th Cir. 2023)","url":"https://www.courtlistener.com","weight":"binding_circuit","note":"Recent significant C corp comp case"},
    {"authority_type":"CtAppeals","citation":"Rapco Inc. v. Commissioner, 85 F.3d 950 (2d Cir. 1996)","url":"https://www.courtlistener.com","weight":"binding_circuit"},
    {"authority_type":"CtAppeals","citation":"Nor-Cal Adjusters v. Commissioner, 503 F.2d 359 (9th Cir. 1974)","url":"https://www.courtlistener.com","weight":"binding_circuit"},
    {"authority_type":"DistCt","citation":"Radtke v. United States, 712 F. Supp. 143 (E.D. Wis. 1989)","url":"https://www.courtlistener.com","weight":"district_court"},
    {"authority_type":"DistCt","citation":"Gale W. Greenlee, Inc. v. United States, 661 F. Supp. 642 (D. Colo. 1985)","url":"https://www.courtlistener.com","weight":"district_court"},
    {"authority_type":"TaxCt","citation":"Sean McAlary Ltd., Inc. v. Commissioner, T.C. Sum. Op. 2013-62","url":"https://www.ustaxcourt.gov","weight":"judicial","note":"Cost approach precedent"},
    {"authority_type":"TaxCt","citation":"Veterinary Surgical Consultants, P.C. v. Commissioner, 117 T.C. 141 (2001)","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Joseph M. Grey Public Accountant, P.C. v. Commissioner, 119 T.C. 121 (2002)","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Brewer Quality Homes, Inc. v. Commissioner, T.C. Memo. 2003-200","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Multi-Pak Corp. v. Commissioner, T.C. Memo. 2010-139","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Clary Hood, Inc. v. Commissioner, T.C. Memo. 2022-15","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Glass Blocks Unlimited v. Commissioner, T.C. Memo. 2013-180","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Pediatric Surgical Associates, P.C. v. Commissioner, T.C. Memo. 2001-81","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Mulcahy, Pauritsch, Salvador & Co., Ltd. v. Commissioner, T.C. Memo. 2011-74","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Paula Construction Co. v. Commissioner, 58 T.C. 1055 (1972)","url":"https://www.ustaxcourt.gov","weight":"judicial","note":"Compensatory intent doctrine"},
    {"authority_type":"TaxCt","citation":"Joly v. Commissioner, T.C. Memo. 1998-361","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Guy Schoenecker, Inc. v. Commissioner, T.C. Memo. 1995-539","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"IRSStudy","citation":"2005 IRS S Corporation Reporting Compliance Study","url":"https://www.irs.gov","weight":"irs_published"},
    {"authority_type":"DataSource","citation":"BLS Occupational Employment and Wage Statistics (OEWS)","url":"https://www.bls.gov/oes/","weight":"government_data"},
    {"authority_type":"PractitionerData","citation":"RCReports — proprietary cost-approach data","url":"https://rcreports.com/","weight":"commercial_practitioner_resource"},
    {"authority_type":"PractitionerArticle","citation":"The Tax Adviser, 'Advising S corporation clients on reasonable compensation,' Oct. 2024","url":"https://www.thetaxadviser.com/issues/2024/oct/advising-s-corporation-clients-on-reasonable-compensation/","weight":"practitioner_secondary"},
    {"authority_type":"PractitionerHeuristic","citation":"CPE Wage:Distribution Ratio Table (cpe-wage-distribution-ratios.xlsx)","url":"data/cpe-wage-distribution-ratios.xlsx","weight":"practitioner_heuristic","disclaimer":"CPE-derived; not IRS-published. Use as directional benchmark only."}
  ]
}
```
```

---

## Implementation notes for Vibe TB ingestion

When this updated Strategy #21 file is ingested into the
`planning-strategy-library` skill:

1. **Replace the existing v1 Strategy #21 file** at
   `references/strategies/reasonable-comp-corp-owners.md`. The v1
   file (delivered in Part 3 of the strategy library addendum)
   should be archived but is now superseded.

2. **Create the data subdirectory** at
   `references/strategies/data/` if it does not yet exist. The
   build plan's Phase 4 task list (PART A in Part 1 of the strategy
   library addendum) should be updated to reference this new
   subdirectory pattern; future strategies may also have data
   companion files.

3. **Place the spreadsheet** at
   `references/strategies/data/cpe-wage-distribution-ratios.xlsx`.

4. **Update the master `references/strategy-list.md`** to note
   that Strategy #21 has a companion data file.

5. **Update the `references/strategy-relationships.json`**
   cross-reference matrix. Strategy #21's relationships are
   unchanged from the matrix in Part 10 of the strategy library
   addendum.

6. **Validate the JSON authority sidecar** against
   `shared/output-schema.json`. Note the new `disclaimer` field on
   the Job Aid and CPE heuristic entries — `output-schema.json`
   may need to be updated to permit this optional field on
   `authorities[].disclaimer`.

7. **Add a `predict-reasonable-comp` skill workflow** that:
   - Loads the CPE wage:distribution table.
   - Pulls BLS OEWS data for the applicable SOC code and metro.
   - Applies Mayson 9-factor / Elliotts 5-factor framework.
   - Outputs a wage range with confidence band, citing
     authorities from the JSON sidecar.
   - **Always discloses the CPE table as practitioner heuristic
     (not IRS authority)** in the output.

8. **CI workflow patch.** The validate.yml workflow should add a
   check for the existence of `data/cpe-wage-distribution-ratios.
   xlsx` and verify the YAML frontmatter `references:` field
   correctly points to it.

---

## Summary of changes vs. Strategy #21 v1 (delivered in Part 3)

| Element | v1 (Part 3) | v1.1 (this update) |
|---|---|---|
| 2025 SS wage base | $168,600 (incorrect; was 2024) | **$176,100** (corrected) |
| 2026 SS wage base | Not stated | **$184,500** (added) |
| Mayson 9-factor framework | Not detailed | **Full framework added** |
| Elliotts 5-factor framework | Not detailed | **Full framework added** |
| Three valuation approaches | Not separated | **Market / Income / Cost detailed** |
| 2014 IRS Job Aid | Not cited | **Cited with explicit non-authority disclaimer** |
| 2005 IRS Compliance Study | Not cited | **Cited** |
| Clary Hood (2022/2023) | Not cited | **Added** |
| Sean McAlary (2013) | Not cited | **Added (Cost Approach precedent)** |
| Brewer Quality Homes | Not cited | **Added** |
| Veterinary Surgical Consultants | Not cited | **Added** |
| Radtke | Not cited | **Added (district + 7th Cir.)** |
| Multi-Pak | Not cited | **Added** |
| Eberl's Claim Service | Not cited | **Added (12-factor variant)** |
| Paula Construction Co. | Not cited | **Added (compensatory intent)** |
| Owensby & Kritikos | Cited briefly | **Expanded** |
| IRC §7436 | Not cited | **Added** |
| Treas. Reg. §1.162-7(a) | Not cited | **Added (compensatory intent)** |
| Treas. Reg. §1.162-7(b)(1) | Not cited | **Added (disguised dividend)** |
| Treas. Reg. §1.162-7(b)(3) | Not cited | **Added (reasonable definition)** |
| TAM 9326001 | Not cited | **Added** |
| BLS OEWS | Not cited | **Added as primary data source** |
| RCReports | Not cited | **Added as practitioner tool** |
| The Tax Adviser Oct 2024 | Not cited | **Added** |
| CPE wage:distribution table | Not present | **Added with provenance disclaimer** |
| §199A QBI W-2 wage interaction | Brief | **Expanded** |
| Mulcahy, Pauritsch, Salvador | Not cited | **Added** |
| Glass Blocks Unlimited | Not cited | **Added** |
| Pediatric Surgical Associates | Not cited | **Added** |
| Greenlee | Not cited | **Added (loan reclassification)** |
| Joly | Cited briefly | **Confirmed** |
| Joseph M. Grey | Cited | **Confirmed** |
| Watson | Cited | **Confirmed** |
| Spicer Accounting | Cited | **Confirmed** |
| Menard | Cited | **Confirmed** |
| Exacto Spring | Cited | **Confirmed** |
| JD & Associates | Cited | **Confirmed** |

---

**End of Strategy #21 update.** The file should be ingested as a
full replacement of the v1 Strategy #21, and the companion
spreadsheet should be placed at the documented data path.
