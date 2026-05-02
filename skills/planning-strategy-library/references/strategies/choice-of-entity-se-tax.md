---
name: "Choice of Entity — Self-Employment Tax Analysis"
slug: choice-of-entity-se-tax
type: SE Tax
tax_type: 2SH
complexity: High
irc_sections: ["§1401", "§1402", "§3101", "§3121", "§1361-1378", "§199A"]
forms: ["Form 1040 / 1120-S / 1120 / 1065"]
state_specific: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

## Overview

Choice of entity for self-employed individuals is one of the most
consequential planning decisions, with the SE tax implications
often dominating the analysis. Comparison framework:

**Sole Proprietor / Single-Member LLC (disregarded):**
- All net profit subject to SE tax (15.3% on first $168,600 SS
  wage base 2024; 2.9% Medicare on remainder; 0.9% Additional
  Medicare on wages >$200K single / $250K MFJ).
- Schedule C reporting.
- Subject to §199A 20% QBI deduction (with limits).

**Partnership / Multi-Member LLC (default):**
- General partner share of trade-or-business income subject to SE
  tax.
- Limited partner share subject to SE tax debate (case law
  uncertain — Renkemeyer; Castigliola; Thompson).
- LLC member treatment unclear post-Renkemeyer.

**S Corporation:**
- Wages to shareholder-employees subject to FICA (employer + employee
  7.65% × 2 = 15.3% on wages up to SS base).
- Distributions to shareholders NOT subject to SE tax / FICA.
- Reasonable compensation requirement (#21) — IRS may
  recharacterize distributions as wages if comp inadequate.
- Subject to §199A QBI (with W-2 limit at higher incomes).

**C Corporation:**
- 21% federal corporate rate.
- Wages subject to FICA (deductible by corp, taxable to employee).
- Dividends not subject to FICA but subject to qualified dividend
  rate (vs. corporate rate creating double-tax).
- Not eligible for §199A.
- §1202 QSBS potential for stock sale exclusion.

The classic SE tax savings analysis: S corp vs. sole proprietor.
Example: Sole prop with $200K net profit pays SE tax on full
$200K. S corp with $80K reasonable wages + $120K distribution pays
FICA on $80K only — saving FICA on $120K.

Trade-offs:
- S corp administrative cost (separate return, payroll, K-1).
- §199A interaction — S corp wages reduce K-1 QBI.
- State franchise tax (CA 1.5% S corp tax; NY annual fees).
- Reasonable compensation audit risk.

The break-even analysis varies but generally S corp election
becomes worthwhile around $80K-$100K net profit.

## Primary IRC authority

- §1401 — Self-employment tax rate.
- §1402 — Definitions of self-employment.
- §1402(a) — Net earnings from self-employment.
- §3101 — FICA tax on employee.
- §3111 — FICA tax on employer.
- §3121 — Definitions of FICA wages.
- §1361-1378 — S corporation rules.
- §199A — QBI deduction.
- §11 — C corporation rate.

## Treasury regulations

- Reg §1.1401 / 1.1402.
- Reg §1.3121 / 1.3111.
- Reg §1.1361 / 1.1378.
- Reg §1.199A-1 through 1.199A-6.

## Key IRS guidance

- IRS Publication 533 — Self-Employment Tax.
- IRS Publication 535.
- IRS Fact Sheet 2008-25 — S corp reasonable comp.

## Key court decisions

- **Renkemeyer, Campbell & Weaver, LLP v. Commissioner, 136 T.C.
  137 (2011)** — Limited liability partnership members; LLP
  members in active law practice subject to SE tax (limited
  partner exception narrow).
- **Castigliola v. Commissioner, T.C. Memo. 2017-62** — LLC members
  in active law practice subject to SE tax.
- **Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)** —
  S corp reasonable compensation.
- **Hardy v. Commissioner, T.C. Memo. 2017-16** — Limited partner
  SE tax (anesthesiologist).

## Eligibility requirements

For S corporation election:
1. Domestic corporation.
2. ≤100 eligible shareholders (US individuals, certain trusts).
3. One class of stock.
4. No nonresident alien shareholders.
5. Form 2553 election by ≤2 months 15 days into tax year.

For QBI deduction:
- See §199A (#19) and predict-qbi-eligibility.

## Mechanics — how it works

Comparative analysis:
1. **Calculate net business income.**
2. **Project SE tax / FICA under each entity.**
3. **Project §199A under each entity.**
4. **Subtract entity overhead** (S corp annual costs, payroll
   processing, separate return).
5. **Consider state franchise tax** (CA 1.5%; NY fees; etc.).
6. **Choose entity** based on net after-tax income.

For S corp election:
1. **Form Inc / Form LLC.**
2. **Form 2553** to elect S status.
3. **Establish payroll** for owner-employee.
4. **Set reasonable compensation** (annual analysis).
5. **Annual S corp Form 1120-S.**

## Documentation requirements

- Entity formation documents.
- Form 2553 (S corp election).
- Reasonable compensation analysis (annual).
- Payroll records.
- Form 1120-S / Form 1065.

## Common pitfalls / audit risks

- **Reasonable compensation challenge.** S corp owner taking $0
  wages with substantial distributions.
- **§199A W-2 limit.** S corp wages reduce QBI (with W-2 limit
  benefit at higher incomes).
- **§199A SSTB limit.** Specified Service Trade or Business
  excluded above threshold.
- **State franchise tax.** CA, NY, TX, MA — added cost.
- **Qualified subchapter S subsidiary (QSub).** Tracking complications.
- **S corp election deadline missed.** Late election available
  under Rev. Proc. 2013-30.
- **Limited partner SE tax.** Renkemeyer narrowed exception;
  active partners cannot rely on limited partner status alone.
- **Payroll late filing.** Form 941 / 944 / W-2 deadlines strict.

## Recent legislative changes

- **TCJA (2017)** — Created §199A; reduced C corp rate to 21%.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §199A §1
  Pub L 119-21]`. §199A permanence and possible §1402 changes.

## State conformity considerations

State entity-tax rules vary widely. **California** has 1.5% S corp
franchise tax. **New York** has annual filing fees. **Tennessee**
has F&E tax on LLCs. **Texas** has franchise tax based on margin.

## AICPA SSTS / Circular 230 considerations

Choice of entity is foundational decision; practitioner should
run formal comparative analysis annually for high-margin
self-employed clients.

## Default confidence band rationale

**MODERATE** — depends on multiple variables; HIGH for clean S corp
elections with proper reasonable comp; LOW for partnerships with
limited partner SE tax uncertainty post-Renkemeyer.

## Cross-references

- `reasonable-comp-corp-owners` (#21).
- `qbi-deduction` (#19).
- `minimize-self-employment-tax` (#90).
- `income-shifting-to-c-corp` (#47).
- `section-1202-qsbs-extended` (#43) — C corp QSBS potential.
- `c-corp-state-tax-savings` (#35).
- `predict-qbi-eligibility` (predict skill).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 1401","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1401","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1402(a)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1402","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1361","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1361","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 199A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section199A","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Renkemeyer, Campbell & Weaver, LLP v. Commissioner, 136 T.C. 137 (2011)","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"TaxCt","citation":"Castigliola v. Commissioner, T.C. Memo. 2017-62","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"CtAppeals","citation":"Watson v. United States, 668 F.3d 1008 (8th Cir. 2012)","url":"https://www.courtlistener.com","weight":"binding_circuit"}
  ]
}
```
