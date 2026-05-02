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
- **`cost-segregation-extended`** (#41) — primary partner strategy.

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
