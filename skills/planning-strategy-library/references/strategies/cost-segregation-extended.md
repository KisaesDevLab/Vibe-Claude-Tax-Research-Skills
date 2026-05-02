---
name: "Cost Segregation Study"
slug: cost-segregation
type: Depreciation
tax_type: EFR
complexity: Medium
irc_sections: ["§168", "§263A", "§263(a)"]
forms: ["Form 4562", "Form 3115 (accounting method change)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Cost segregation is an engineering-based methodology that
re-classifies portions of a real estate building from 39-year
nonresidential or 27.5-year residential rental into shorter-lived
MACRS classes (5-year, 7-year, 15-year). Reclassified components
become eligible for §168(k) bonus and §179 expensing — materially
accelerating depreciation in early years of ownership.

Typical reclassifications:
- **5-year property:** Carpeting, decorative lighting, removable
  partitions, certain electrical and plumbing for specific tasks
  (kitchen equipment, dental chair plumbing), specialty HVAC.
- **7-year property:** Office furniture, certain manufacturing
  equipment.
- **15-year property:** Land improvements (parking lots, sidewalks,
  fencing, landscaping, certain site improvements).
- **Qualified Improvement Property (QIP).** 15-year recovery
  (post-CARES); bonus eligible.

Combines particularly well with:
- **REPS (#20)** — turns rental losses into nonpassive deductions.
- **Short-Term Rental (#26)** — STR with material participation
  similarly converts losses.
- **§168(k) bonus depreciation (#12)** — bonus % applied to
  shorter-life components magnifies first-year deduction.

OBBBA reportedly restored 100% bonus, dramatically increasing
cost-seg value for 2025+ acquisitions.

The IRS issued the **Cost Segregation Audit Techniques Guide
(ATG)** providing detailed methodology guidance. Cost-seg studies
are not aggressive when methodology is engineering-based and
documented properly. Audit issue is study quality (engineer
credentials, methodology, documentation).

## Primary IRC authority

- §168 — MACRS.
- §168(k) — Bonus.
- §168(e) — Classification.
- §179 — Expensing.
- §263(a) — Capital expenditures.
- §263A — UNICAP.

## Treasury regulations

- Reg §1.168-1 through §1.168(k)-2.
- Reg §1.263(a)-3 — Tangible property improvement.
- Reg §1.446-1(e) — Accounting method changes.

## Key IRS guidance

- **IRS Cost Segregation Audit Techniques Guide (ATG)** —
  https://www.irs.gov/businesses/cost-segregation-atg
- **Rev. Proc. 2015-13** — §481(a) accounting method changes.
- **Rev. Proc. 2019-08, 2019-13** — §168(k) procedural.
- **Rev. Proc. 2020-25** — QIP CARES Act fix.

## Key court decisions

- **Hospital Corp. of America v. Commissioner, 109 T.C. 21
  (1997)** — Foundational case validating cost-seg methodology;
  established engineering-based reclassification approach.
- **AmeriSouth XXXII, Ltd. v. Commissioner, T.C. Memo. 2012-67** —
  Reclassification rules for residential rental components.
- **Whiteco Industries, Inc. v. Commissioner, 65 T.C. 664
  (1975)** — Six-factor test for tangible vs. structural
  components.

## Eligibility requirements

1. Real estate placed in service.
2. Cost-seg study performed (typically by qualified engineer).
3. Components properly identified and reclassified per Whiteco
   six-factor test.
4. Form 3115 if applying to prior-year acquisitions (§481(a)
   catch-up adjustment).

## Mechanics — how it works

1. **Engage qualified engineer.** Cost-seg specialist with
   construction/engineering background and tax knowledge.
2. **Engineer performs detailed study.** Site visit; detailed cost
   allocation by component; classification per IRS ATG.
3. **Receive cost-seg report** with detailed component schedule.
4. **For prior-year acquisitions:** Form 3115 with §481(a)
   adjustment.
5. **For current-year:** Direct application on Form 4562.
6. **Combine with §168(k) bonus** to maximize first-year deduction.
7. **Track recapture** at sale: shorter-life property triggers
   §1245 recapture (ordinary); long-life real property triggers
   §1250 recapture (typically capped at unrecaptured §1250 gain).

## Documentation requirements

- Cost-seg study with engineer credentials, methodology,
  component-by-component breakdown.
- Construction documents, plans, photos, invoices.
- Form 4562 (current-year) or Form 3115 (catch-up).
- §481(a) adjustment computation.

## Common pitfalls / audit risks

- **Aggressive reclassification.** Studies that reclassify
  structural components (load-bearing walls, building shell, roof
  structure) as shorter-life property are challenged.
- **Inadequate engineering.** Studies done without engineer site
  visit, or done by non-engineers.
- **§1245 recapture surprise.** Faster depreciation now means more
  ordinary recapture later if property is sold.
- **Form 3115 procedural failures.** Catch-up §481(a) per Rev.
  Proc. 2015-13.
- **State decoupling.** States that decouple from §168(k) bonus
  affect state benefit.
- **Personal-use property.** Cost-seg generally not appropriate
  for primary residences.

## Recent legislative changes

- **TCJA (2017)** — §168(k) extended to used property.
- **CARES Act (2020)** — QIP fix (15-year, bonus-eligible).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §168(k)
  100% bonus Pub L 119-21]`. 100% bonus restoration dramatically
  increases cost-seg utility.

## State conformity considerations

States decoupling from §168(k) bonus affect state-level cost-seg
benefit. CA, NY, NJ, MA, MD, MN, PA major decouplers.

## AICPA SSTS / Circular 230 considerations

Cost-seg is not aggressive when properly executed. Verify engineer
credentials and study methodology.

## Default confidence band rationale

**HIGH** for properly-executed engineer-based studies. Drops to
MODERATE for aggressive reclassifications.

## Cross-references

- `bonus-and-section-179-depreciation` (#12) — primary partner.
- `real-estate-professional-extended` (#20) — primary user.
- `short-term-rental` (#26) — alternative user.
- `active-participation-real-estate` (#3).
- `1031-like-kind-exchange` (#1).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 168","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section168","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.168(k)-2","url":"https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1","weight":"regulation"},
    {"authority_type":"RevProc","citation":"Rev. Proc. 2015-13","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"ATG","citation":"IRS Cost Segregation Audit Techniques Guide","url":"https://www.irs.gov/businesses/cost-segregation-atg","weight":"persuasive_non_authority"},
    {"authority_type":"TaxCt","citation":"Hospital Corp. of America v. Commissioner, 109 T.C. 21 (1997)","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
