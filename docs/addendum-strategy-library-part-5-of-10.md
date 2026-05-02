# Vibe CPA Skills — Strategy Library Addendum (94 Strategies)

**Part 5 of 10** — Strategies #38 through #47.

**Part navigation:**
- Part 1: Exec summary, master index, PART A build-plan addendum, strategies #1–#7
- Part 2: Strategies #8–#17
- Part 3: Strategies #18–#27
- Part 4: Strategies #28–#37
- **Part 5: Strategies #38–#47** ← this file
- Parts 6–10: remaining strategies + cross-reference matrix

---

## Strategy #38: Miscellaneous Tax Credits

**File:** `references/strategies/misc-tax-credits.md`

```markdown
---
name: "Miscellaneous Tax Credits (Umbrella Reference)"
slug: misc-tax-credits
type: Credit/Payment
tax_type: EFR
complexity: Medium
irc_sections: ["§38", "§44", "§45A", "§45F", "§45R", "§45S", "§51", "§129"]
forms: ["Form 3800 (General Business Credit)", "credit-specific forms"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

This file is the umbrella reference for federal tax credits beyond
the major credits given separate strategy files (R&D #39, EV #36,
§1202 QSBS #43, Education Credits #61, Adoption #58). The General
Business Credit under §38 aggregates many.

Credits commonly missed by practitioners and small businesses:

1. **§51 Work Opportunity Tax Credit (WOTC).** Up to $2,400 per
   eligible new hire (more for veterans, long-term unemployed,
   etc.). 9 target groups including SNAP recipients, ex-felons,
   designated community residents, qualified veterans. Requires
   IRS Form 8850 within 28 days of hire.

2. **§45F Employer-Provided Child Care Credit.** 25% of qualified
   child care facility expenditures + 10% of qualified resource
   and referral expenditures, up to $150,000 annual cap.

3. **§45R Small Business Health Care Tax Credit.** Up to 50% of
   premiums for small employers using SHOP. See #8.

4. **§45S Paid Family and Medical Leave Credit.** 12.5% to 25% of
   wages paid to qualifying employees on FMLA leave.

5. **§44 Disabled Access Credit.** 50% of eligible access
   expenditures between $250 and $10,250, max $5,000.

6. **§47 Rehabilitation Credit (Historic).** 20% of qualified
   rehabilitation expenditures on certified historic structures.

7. **§129 Dependent Care Assistance Programs.** Up to $5,000 of
   pre-tax employer-provided child care benefits.

8. **§45A Indian Employment Credit.** Targeted credit for hiring
   enrolled members of Indian tribes.

9. **State and local credits.** R&D, jobs, investment, film,
   enterprise zone — vary substantially by state.

## Primary IRC authority

- §38 — General business credit.
- §39 — Carryback and carryforward of unused credits.
- §44 — Disabled access credit.
- §45A — Indian employment credit.
- §45F — Employer-provided child care credit.
- §45R — Small employer health insurance credit.
- §45S — Paid family and medical leave credit.
- §47 — Rehabilitation credit.
- §51 — WOTC.
- §52 — Special rules for §51.
- §129 — Dependent care assistance.

## Treasury regulations

- Reg §1.38-1 through §1.39-2 — General business credit.
- Reg §1.51-1 — WOTC.
- Reg §1.45F-1 (proposed) — Child care.
- Reg §1.129-1 — Dependent care.

## Key IRS guidance

- IRS Publication 334 — Tax Guide for Small Business.
- Form 5884 instructions — WOTC.
- Form 8881 — Pension Plan Startup Costs Credit.
- Form 8882 — Employer-Provided Child Care Facilities Credit.
- Form 8826 — Disabled Access Credit.

## Eligibility requirements

Vary by credit. See specific credit forms.

## Mechanics — how it works

1. **Annual credit inventory.** Review available credits each year.
2. **Pre-screen for WOTC** at hiring (Form 8850 within 28 days).
3. **Compute each credit** on respective form.
4. **Aggregate on Form 3800** (General Business Credit).
5. **Apply tax liability limits** (§38(c)).
6. **Carryback / carryforward** unused credits per §39 (1-year
   carryback, 20-year carryforward, generally).

## Documentation requirements

Vary. Generally requires Form 8850 (WOTC), plan documents (child
care, dependent care), employee certifications, payment records.

## Common pitfalls / audit risks

- **WOTC pre-screening missed.** 28-day window from hire date.
- **General business credit limit.** §38(c) limits credit to tax
  liability less tentative minimum tax.
- **§45R complex computation** — small business health credit
  intricate phase-outs.

## Recent legislative changes

- **TCJA (2017)** — Created §45S paid leave credit.
- **CARES / CAA 2021 / IRA 2022** — Various extensions and
  modifications.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA tax credits
  Pub L 119-21]`. Numerous credit modifications likely.

## State conformity considerations

State credits are independent.

## Default confidence band rationale

**HIGH** for properly-documented credits.

## Cross-references

- `r-and-d-credit-strategy` (#39).
- `ev-credits` (#36).
- `adoption-incentives` (#58).
- `group-health-insurance` (#8) — §45R.
- `hiring-kids` (#49).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 38","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section38","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 51","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section51","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 45F","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section45F","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 45S","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section45S","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #39: R&D Credit (Strategic)

**File:** `references/strategies/r-and-d-credit-strategy.md`

```markdown
---
name: "R&D Credit (§41) and §174 R&E Capitalization"
slug: r-and-d-credit-strategy
type: Credit/Payment
tax_type: CREDIT
complexity: High
irc_sections: ["§41", "§174", "§280C(c)"]
forms: ["Form 6765", "Form 8974 (payroll offset)"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
cross_reference_skills: ["predict-r-and-d-credit"]
---

> **Caution:** §41 R&D Credit is a high-IRS-scrutiny area. The LB&I
> R&D Audit Roadmap systematically challenges documentation. Many
> small businesses claim the credit based on aggressive promoter
> calculations without substantiating the §41(d) four-part test.
> Improperly-claimed credits trigger §6662 accuracy penalties.
> Practitioners must require contemporaneous nexus documentation.

## Overview

§41 incentivizes business expenditures on qualified research. The
credit (20% of QREs above base, or simplified 14% / 6% under
Alternative Simplified Credit) offsets income tax. For qualifying
small businesses, §41(h) allows the credit to offset payroll taxes
(up to $500,000) for businesses with gross receipts under $5M and
within their first 5 years.

§174 capitalization (post-TCJA): TCJA effective 2022 eliminated
current deduction of R&E. Domestic R&E capitalized over 5 years;
foreign R&E over 15 years; software development treated as R&E.

OBBBA reportedly restored current expensing of domestic R&E.
Verify via Classification Tables — consequential restoration if
confirmed.

## Primary IRC authority

- §41 — Credit for increasing research activities.
- §41(b) — QREs: wages, supplies, contract research (65%).
- §41(c) — Base amount.
- §41(c)(5) — Alternative Simplified Credit.
- §41(d) — Qualified research definition (four-part test).
- §41(h) — Payroll tax election (qualified small business).
- §174 — R&E expenditures (post-TCJA capitalization).
- §280C(c) — Reduction of §174 deduction by amount of credit.

## Treasury regulations

- Reg §1.41-1 through §1.41-9.
- Reg §1.41-4 — Qualified research definition.
- Reg §1.41-2 — Qualified research expenses.

## Key IRS guidance

- Notice 2023-63 — §174 post-TCJA procedural guidance.
- Rev. Proc. 2023-11 — §174 accounting method change.
- Rev. Proc. 2023-8 — §174 software development.
- LB&I R&D Audit Roadmap — IRS audit approach.
- CCM 20214101F — R&D refund claim documentation.

## Key court decisions

- **Suder v. Commissioner, T.C. Memo. 2014-201** — Section 41
  documentation; nexus between wages and qualified research.
- **Trinity Industries, Inc. v. United States, 691 F. Supp. 2d 688
  (N.D. Tex. 2010)** — Qualified research project definition.
- **Geosyntec Consultants, Inc. v. United States, 776 F.3d 1330
  (11th Cir. 2015)** — Funded research exclusion.
- **Union Carbide Corp. v. Commissioner, T.C. Memo. 2009-50** —
  Process of experimentation.
- **Populous Holdings, Inc. v. Commissioner, T.C. Memo. 2019-118** —
  Architects qualifying for §41.

## Eligibility requirements

§41(d) four-part test for qualified research:
1. **Permitted purpose** — new or improved business component.
2. **Technological in nature** — physical/biological/engineering/CS.
3. **Process of experimentation** — systematic trial and error.
4. **Elimination of uncertainty** — capability/methodology/design.

Excluded under §41(d)(4): post-commercial-production research,
adaptation, duplication, surveys, internal-use software (limited),
funded research.

§41(h) payroll offset: gross receipts <$5M; no gross receipts >5
years before; election on Form 6765.

## Mechanics — how it works

1. **Identify qualified projects** satisfying four-part test.
2. **Identify QREs:** wages, supplies, 65% contract research,
   cloud/computer rental.
3. **Compute credit** — Regular (20%) or ASC (14%/6%).
4. **§280C(c) election.**
5. **Form 6765** with return.
6. **§41(h) payroll offset election** (Form 8974 quarterly).
7. **§174 capitalization** (5-year domestic / 15-year foreign).

## Documentation requirements

- Project documentation linking activities to four-part test.
- Time tracking by qualified project (contemporaneous).
- Wage allocation by project.
- Supply consumption records.
- Contract research agreements (risk allocation).
- Process of experimentation documentation.

## Common pitfalls / audit risks

- **Insufficient nexus documentation.** Most common audit failure.
- **Routine vs. qualified.** Established product development.
- **Internal-use software trap.** §41(d)(4)(E).
- **Funded research exclusion.** Risk-shifted contracts.
- **§41(h) eligibility.** Strict gross receipts/age limits.
- **§174 capitalization** mistakes post-TCJA.
- **R&D refund claim documentation** per CCM 20214101F.

## Recent legislative changes

- **TCJA (2017)** — §174 capitalization effective 2022.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §174 §41
  research expensing Pub L 119-21]`. Reports indicate restoration
  of current expensing for domestic R&E effective 2025+.

## State conformity considerations

State R&D credits independent. CA, PA, TX, NY, MA. State conformity
to §174 varies.

## AICPA SSTS / Circular 230 considerations

Heavily audit-targeted. Verify documentation; avoid promoter
estimates; recommend Form 8275 disclosure for borderline positions.

## Default confidence band rationale

**MODERATE** — well-established but heavily fact-driven. HIGH only
with rigorous contemporaneous documentation.

## Cross-references

- `predict-r-and-d-credit` (predict skill).
- `misc-tax-credits` (#38).
- `income-shifting-to-c-corp` (#47).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 41","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section41","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 174","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section174","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.41-4","url":"https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1","weight":"regulation"},
    {"authority_type":"Notice","citation":"Notice 2023-63","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"TaxCt","citation":"Suder v. Commissioner, T.C. Memo. 2014-201","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"CtAppeals","citation":"Geosyntec Consultants, Inc. v. United States, 776 F.3d 1330 (11th Cir. 2015)","url":"https://www.courtlistener.com","weight":"binding_circuit"}
  ]
}
```
```

---

## Strategy #40: State Tax Savings (Individual)

**File:** `references/strategies/state-tax-savings.md`

```markdown
---
name: "State Tax Savings (Individual Planning)"
slug: state-tax-savings
type: Credit/Payment
tax_type: CREDIT
complexity: Medium
irc_sections: ["§164"]
forms: ["State income tax returns"]
state_specific: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

## Overview

State tax planning for individuals encompasses several strategies:

1. **Domicile / residency planning.** Establishing domicile in a
   no-income-tax state (FL, TX, NV, WA, WY, SD, AK, TN). Requires
   substantial change in life circumstances; states aggressively
   audit residency claims (NY notorious for "convenience-of-
   employer" rule and 183-day tests).

2. **Convenience-of-employer rule mitigation.** NY, PA (modified),
   DE, NE tax wages sourced to employer's state of in-office
   operation, even if employee works remotely from another state.

3. **PTET pass-through (#17).** SALT cap workaround for
   pass-through income.

4. **State PTE-like alternatives** — composite returns,
   withholding, pass-through entity-level tax elections.

5. **State-specific credits.** Residential energy, child care,
   education, dependent care, EITC supplements.

6. **Charitable contribution credits / deductions.** Many states
   offer credits for state-targeted charitable giving (HI renewable
   energy fund, AZ school choice credits, GA qualified school).

7. **Multi-state allocation.** Careful allocation can minimize
   overall state tax burden.

## Primary IRC authority

- §164 — State and local taxes.
- §164(b)(6) — $10,000 SALT cap (TCJA; possibly modified by OBBBA).

## Key federal authority

- **Comptroller of Treasury v. Wynne, 575 U.S. 542 (2015)** —
  Dormant Commerce Clause; states must offer credit for taxes paid
  to other states.
- **Edward A. Zelinsky v. Tax Appeals Tribunal, 1 N.Y.3d 85
  (2003)** — NY convenience-of-employer rule narrowing.

## Mechanics — domicile change

1. **Document substantive life changes.** Move primary residence,
   change driver's license, register to vote, change bank accounts,
   doctors, dentists, schools, club memberships.
2. **Track day count.** 183-day test for statutory residency.
3. **Sever ties to old state.** Sell or rent former primary
   residence; transfer professional licenses; disengage from
   old-state organizations.
4. **Avoid trips to old state.** Especially for high-income
   taxpayers facing residency audit.
5. **Address "abode" test.** Some states (NY) have permanent abode
   test even for non-domiciliaries.

## Mechanics — convenience-of-employer mitigation

1. **Establish bona fide office in employee's state.** Documented
   business need.
2. **Employer cooperation.** Employer must require (not merely
   accommodate) home-state work.
3. **Time tracking.** Document specific days worked in each state.

## Documentation requirements

- For domicile: lease/deed, utility bills, voter registration,
  driver's license, healthcare records, school enrollment, vehicle
  registration, tax filings showing change.
- For multi-state allocation: time and location tracking; income
  source documentation.

## Common pitfalls / audit risks

- **Incomplete domicile change.** NY and CA routinely challenge
  claimed domicile changes. The "5 primary factors" (home, time,
  items near and dear, active business involvement, family) are
  scrutinized.
- **Day-counting failures.** 183-day rules.
- **Statutory residency abode trap.** Even non-domiciliaries can
  be "statutory residents" if permanent abode + >183 days.
- **NY convenience-of-employer.** Telecommuters from NJ, CT, PA
  may still be NY-source-taxed.
- **Aggressive multistate allocation.** State combined-reporting
  rules may collapse aggressive shifts.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA SALT cap
  §164(b)(6) Pub L 119-21]`. SALT cap modifications would
  significantly affect this strategy area.

## State conformity considerations

This entire strategy is state-by-state.

## Default confidence band rationale

**MODERATE** — fact and state-specific. HIGH for substantive
domicile changes with strong documentation; LOW for quasi-domicile
moves intended to dodge tax without genuine life changes.

## Cross-references

- `ptet-salt-workaround` (#17).
- `c-corp-state-tax-savings` (#35).
- `primary-home-sale-exclusion` (#67).
- All state stub files.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 164","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section164","weight":"primary_statute"},
    {"authority_type":"SCOTUS","citation":"Comptroller of Treasury v. Wynne, 575 U.S. 542 (2015)","url":"https://www.supremecourt.gov","weight":"binding_judicial"}
  ]
}
```
```

---

## Strategy #41: Cost Segregation

**File:** `references/strategies/cost-segregation.md`

```markdown
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
- `real-estate-professional` (#20) — primary user.
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
```

---

## Strategy #42: C Corp Misc Deductions

**File:** `references/strategies/c-corp-misc-deductions.md`

```markdown
---
name: "C Corporation Specific Deductions and Planning"
slug: c-corp-misc-deductions
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§162", "§243", "§245A", "§163(j)", "§78"]
forms: ["Form 1120", "Form 1118"]
state_specific: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

## Overview

This file addresses C-corp-specific deductions and planning levers
that distinguish C corp tax from pass-through tax:

1. **§243 Dividends-Received Deduction (DRD).** C corp receiving
   dividends from another C corp deducts:
   - 50% of dividends if owns <20% of payer.
   - 65% if owns 20-79%.
   - 100% if owns 80%+ (consolidated returns).

2. **§245A Foreign Source DRD.** 100% DRD for dividends from 10%+
   owned foreign corporations.

3. **§163(j) interest deduction limit.** C corp limited to 30% of
   ATI. Excess interest carries forward. Small business exception:
   average gross receipts <$30M (indexed) exempt.

4. **§199A NOT available to C corps.**

5. **§170(b)(2) charitable contribution limit.** 10% of taxable
   income; excess carries forward 5 years.

6. **§267 related-party rules.** Loss disallowance and matching.

7. **§531 / §541 penalty taxes.** See #31.

8. **§78 gross-up.** Foreign tax credit users.

9. **Bad debt deduction (§166).** C corps use specific charge-off
   method; partial worthlessness allowed.

10. **§481(a) adjustments** for accounting method changes.

## Primary IRC authority

- §162 — Trade or business expenses.
- §163(j) — Interest deduction limit.
- §166 — Bad debts.
- §170(b)(2) — Corporate charitable contribution limit.
- §243 — DRD.
- §245A — Foreign DRD.
- §267 — Related-party loss disallowance.
- §481 — Accounting method change.
- §531, §541 — Penalty taxes.

## Treasury regulations

- Reg §1.162-1 through §1.162-29.
- Reg §1.163(j)-1 through §1.163(j)-11 — Interest limit.
- Reg §1.243-1 through §1.243-3 — DRD.
- Reg §1.245A-1 through §1.245A-12 — Foreign DRD.

## Key IRS guidance

- Notice 2018-28 — §163(j) initial guidance.
- Rev. Proc. 2020-22 — §163(j) accounting method changes.
- IRS Publication 542.

## Key court decisions

- **United States v. Generes, 405 U.S. 93 (1972)** — Bad debt
  business vs. nonbusiness analysis.

## Mechanics — how it works

1. **Annual planning review.** Survey available C corp deductions.
2. **§163(j) computation** — track ATI, interest deduction limit,
   carryforward.
3. **DRD planning** — coordinate inter-corporate distributions.
4. **Charitable contribution management** — track 10% limit,
   carryforward.
5. **§481(a) accounting method changes** — Form 3115.
6. **§78 gross-up** if FTC applicable.

## Common pitfalls / audit risks

- **§163(j) ATI computation errors.** Formula complex; small
  business exception eligibility (gross receipts test) must be
  verified.
- **DRD holding period.** §246(c) requires 45-day (or 90-day for
  preferred) holding period.
- **§267 related-party traps.** Loss disallowance until property
  is later sold.
- **§531 / §541 penalty taxes.**

## Recent legislative changes

- **TCJA (2017)** — Created §163(j) limit; changed DRD; 21% rate.
- **CARES Act (2020)** — Temporarily raised §163(j) ATI to 50%
  for 2019, 2020.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §163(j)
  §243 Pub L 119-21]`. Reports indicate possible §163(j) ATI
  formula reversion to EBITDA basis (pre-2022).

## State conformity considerations

State conformity to §163(j), §243, §245A varies. Many states
decouple from §163(j) ATI changes.

## Default confidence band rationale

**MODERATE** for §163(j) computations and DRD claims. HIGH for
routine items.

## Cross-references

- `c-corp-dividends` (#31).
- `c-corp-state-tax-savings` (#35).
- `section-1202-qsbs` (#43).
- `income-shifting-to-c-corp` (#47).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 163(j)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section163","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 243","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section243","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 245A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section245A","weight":"primary_statute"}
  ]
}
```
```

---

## Strategy #43: §1202 QSBS Exclusion

**File:** `references/strategies/section-1202-qsbs.md`

```markdown
---
name: "§1202 Qualified Small Business Stock (QSBS) Exclusion"
slug: section-1202-qsbs
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§1202", "§1045", "§1244"]
forms: ["Form 8949 with §1202 exclusion code", "Schedule D"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§1202 is one of the most valuable but underutilized provisions in
the Code. Excludes (under current rules) up to **100% of capital
gain** on sale of "Qualified Small Business Stock" (QSBS), with a
per-issuer limit of the **greater of $10 million or 10× basis**.
Held five years or more.

Exclusion percentage by acquisition date:
- After September 27, 2010: **100% exclusion**.
- August 11, 1993 to February 17, 2009: 50%.
- February 18, 2009 to September 27, 2010: 75%.

For 100% exclusion stock, the gain is also exempt from §1411 NIIT.

§1045 rollover: gains from QSBS held >6 months can be rolled into
new QSBS within 60 days, deferring (not excluding) gain. §1045
restarts the §1202 holding period.

OBBBA reportedly modified §1202 — possibly increasing the exclusion
cap or holding period rules. Verify via Classification Tables.

## Primary IRC authority

- §1202 — 50%/75%/100% exclusion of gain from QSBS sale.
- §1202(a) — Exclusion percentages.
- §1202(b) — Per-issuer limit ($10M or 10× basis).
- §1202(c) — QSBS definition.
- §1202(d) — Qualified small business definition.
- §1202(e) — Active business requirement.
- §1202(h) — Tacked holding period for gifts and inheritance.
- §1045 — Rollover.

## Treasury regulations

- Reg §1.1202-2 (proposed; not finalized) — limited regulatory
  guidance. Most §1202 interpretation via case law and IRS
  pronouncements.

## Key IRS guidance

- PLR 201717010 — QSBS active business eligibility.
- PLR 202144026 — Recent QSBS PLR.
- CCA 201610006 — Corporate redemptions and §1202.

## Key court decisions

- **Owen v. Commissioner, T.C. Memo. 2012-21** — QSBS analysis;
  active business requirement.

## Eligibility requirements

QSBS:
1. **Domestic C corporation** (NOT S corp; NOT LLC taxed as
   partnership).
2. **Qualified small business** at issuance: aggregate gross
   assets ≤$50 million immediately before and after issuance.
3. **Original-issue acquisition** from corporation; not secondary
   market. Cash, property, or services rendered.
4. **Hold ≥5 years.**
5. **Active business requirement** — at least 80% of corporation's
   assets used in active conduct of qualified trade or business.
6. **Not a disqualified business** under §1202(e)(3): professional
   services, banking, insurance, financing, leasing, investing,
   farming, mining/oil & gas, hotels, restaurants.

§1045 rollover:
1. Original QSBS held >6 months.
2. New QSBS purchased within 60 days of sale.
3. Election made on timely return.

## Mechanics — how it works

1. **Verify QSBS status at issuance.** Critical — moment-of-
   issuance test.
2. **Document original issuance.** Stock certificate, board
   resolution, valuation, gross assets.
3. **Track 5-year holding period.**
4. **Verify active business throughout holding.**
5. **Sale or exchange.** Recognize gain.
6. **Exclude under §1202.** Form 8949 with code "Q"; Schedule D
   adjustment.
7. **Per-issuer limit.** $10M or 10× basis, lifetime per issuer.

## Documentation requirements

- Stock certificate.
- Corporate gross assets at issuance.
- Active business activity records.
- Annual confirmation of qualified business activity.
- Form 8949 with §1202 exclusion code.

## Common pitfalls / audit risks

- **S corp / LLC stock not eligible.** Common error: founders
  incorporate as LLC or S corp and lose §1202 entirely.
- **Active business test failure.** Holding company structures
  must satisfy 80% active business test.
- **Disqualified business creep.** Manufacturing pivoting to
  consulting may lose qualified status.
- **Original-issue requirement.** Secondary market acquisitions
  not QSBS.
- **Per-issuer limit.** $10M lifetime per issuer; spousal
  allocation possible.
- **Gift / inheritance.** Holding period and basis tack to donee.

## Recent legislative changes

- §1202(a)(4) 100% exclusion (2010 amendment, made permanent 2015).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1202
  Pub L 119-21]`. Reports indicate possible increase in $50M gross
  assets cap and/or per-issuer exclusion limit.

## State conformity considerations

State conformity varies significantly. **California** does NOT
conform; full state tax on QSBS gain. **Pennsylvania** does not
conform.

## AICPA SSTS / Circular 230 considerations

Verify qualification at multiple time points: issuance, throughout
hold, and sale. Documentation for original issuance often deficient.

## Default confidence band rationale

**HIGH** for clearly-qualifying QSBS with proper documentation.
Drops to MODERATE for aggressive interpretations or holding-company
structures.

## Cross-references

- `worthless-stock-ordinary-loss` (#30) — companion §1244.
- `installment-sale` (#33) — alternative if §1202 unavailable.
- `qoz-reinvestment` (#34) — alternative deferral.
- `gifting-stock` (#46) — gifting QSBS implications.
- `employee-stock-options` (#68).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 1202","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1202","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1045","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1045","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Owen v. Commissioner, T.C. Memo. 2012-21","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
```

---

## Strategy #44: Corporate-Owned Variable Universal Life (VUL)

**File:** `references/strategies/corporate-owned-vul.md`

```markdown
---
name: "Corporate-Owned VUL ('No-Limits Roth IRA')"
slug: corporate-owned-vul
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§7702", "§101(a)", "§101(j)", "§72(e)"]
forms: ["Form 8925 (Employer-Owned Life Insurance Reporting)"]
state_specific: true
aggressive: true
caution: true
confidence_default_band: LOW
last_obbba_review: "N/A"
---

> **AGGRESSIVE STRATEGY WARNING:** "Corporate-Owned VUL" — sometimes
> marketed as "No-Limits Roth IRA" or "401(h) Plan" — uses an
> over-funded permanent life insurance policy owned by an employer
> to provide tax-deferred wealth accumulation. Specific risks:
> (a) §101(j) Employer-Owned Life Insurance rules require notice
> and consent before issuance or death benefit becomes ordinary
> income; (b) IRS attention to over-funded life insurance vehicles
> as deferred compensation under §409A; (c) potential constructive
> dividend treatment; (d) reasonable compensation issues if
> excessive premiums substitute for compensation; (e) state
> insurance regulations. Marketers oversell the "No-Limits Roth"
> framing — the structure is fundamentally life insurance with
> substantial costs and regulatory complexity, not a Roth substitute.

## Overview

Structure: closely-held corporation purchases VUL on executive's
life. Corporation pays substantial premiums, "over-funded" relative
to death benefit, building cash value tax-deferred. At retirement,
executive takes loans against cash value (loans not taxable). At
death, death benefit pays to corporation tax-free (§101); through
complex structuring, value flows to family.

Marketing claims:
1. Tax-deferred growth (similar to 401(k)).
2. Tax-free policy loans (similar to Roth).
3. Tax-free death benefit (§101).
4. No income limits or contribution limits.

Reality:
- Insurance costs (mortality, administration, surrender charges)
  significantly reduce returns.
- §101(j) Employer-Owned Life Insurance rules subject death benefit
  to ordinary income unless specific notice and consent followed.
- §7702A modified endowment contract (MEC) rules can change loan
  tax treatment.
- §409A may apply if structured as deferred compensation.
- Reasonable compensation issues if excessive premiums.
- IRS scrutiny of over-funded life insurance schemes.

## Primary IRC authority

- §7702 — Definition of life insurance contract.
- §101(a) — Death benefit excluded from income.
- §101(j) — Employer-owned life insurance; notice and consent
  required for §101(a) exclusion.
- §72(e) — Annuity / life insurance contract distribution.
- §7702A — Modified endowment contract.
- §409A — Deferred compensation.

## Treasury regulations

- Reg §1.7702-0 through §1.7702-2 — Life insurance definition.
- Reg §1.101-1 through §1.101-7 — §101 implementation.

## Key IRS guidance

- Notice 2007-78 — §101(j) employer-owned life insurance.
- Notice 2009-48 — §101(j) further guidance.

## Eligibility requirements

§101(j) preservation of §101(a):
1. **Notice and consent** before issuance: employee notified in
   writing of insurance, amount, employer beneficiary; written
   consent obtained. Form 8925 required.
2. **Insured is highly compensated employee** at time of issuance,
   OR §101(j)(2)(B) exception applies.

§7702 life insurance treatment:
1. Policy satisfies §7702 cash value accumulation test or
   guideline premium / cash value corridor test.
2. Not a §7702A MEC.

## Mechanics — how it works (as marketed)

1. **Corporation purchases VUL** on executive's life. Substantial
   premium.
2. **§101(j) notice and consent** obtained; Form 8925 filed.
3. **Premium payments continue** for years; cash value grows
   tax-deferred.
4. **At retirement, executive borrows against cash value** —
   policy loans not currently taxable (assuming non-MEC).
5. **Death benefit at executive's death** — tax-free to
   corporation under §101 (assuming §101(j) compliance).
6. **Family receives wealth via supplemental structure** — split-
   dollar arrangement, executive bonus plan, or other vehicle.

## Documentation requirements

- Insurance policy.
- §101(j) notice and consent.
- Form 8925 annual reporting.
- Board resolutions.
- §7702 testing documentation.

## Common pitfalls / audit risks

- **§101(j) compliance failure.** Death benefit becomes ordinary
  income to corporation.
- **MEC classification.** Loans become taxable.
- **Reasonable compensation.** Excessive premiums in lieu of wages
  recharacterized.
- **Constructive dividend.** Personal benefit recharacterized.
- **§409A.** If structured as deferred compensation.
- **State insurable interest rules.** Some states require
  documented insurable interest.
- **Promoter overstatement.** Marketed returns and tax benefits
  often overstate after-cost economics.

## Recent legislative changes

- No major statutory changes recent.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §101 §7702
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State insurance regulations and tax treatment vary significantly.

## AICPA SSTS / Circular 230 considerations

Aggressive strategy. Insist on §101(j) notice and consent and
Form 8925; verify §7702 / §7702A status with carrier; document
business purpose for corporate ownership; recommend Form 8275
disclosure; caution client against promoter oversimplifications.

## Default confidence band rationale

**LOW** — Marketing claims often outpace tax substance; multiple
audit risk vectors; no clear safe harbor for "No-Limits Roth"
structure.

## Cross-references

- `life-insurance-retirement-plan` (#74) — closely-related
  individual variant.
- `reasonable-comp-corp-owners` (#21).
- `401k-pretax` (#75) — compliant alternative.
- `solo-401k-employer-contributions` (#82) — compliant alternative.
- `defined-benefit-cash-balance` (#73) — compliant alternative.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 101(j)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section101","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 7702","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section7702","weight":"primary_statute"},
    {"authority_type":"Notice","citation":"Notice 2007-78","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"Notice","citation":"Notice 2009-48","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
```

---

## Strategy #45: §127 Education Assistance Program

**File:** `references/strategies/section-127-education-assistance.md`

```markdown
---
name: "Section 127 Education Assistance Program"
slug: section-127-education-assistance
type: Income Shifting
tax_type: EFR
complexity: Medium
irc_sections: ["§127"]
forms: ["No specific form; W-2 reporting"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§127 allows an employer to provide up to **$5,250 per year** of
"qualified educational assistance" to employees on a tax-free
basis. Employee excludes assistance from gross income; employer
deducts as §162 business expense.

CARES Act (2020) temporarily expanded §127 to include employer
payments toward employee student loan principal and interest
through 2025; CAA 2021 extended through December 31, 2025. OBBBA
may have made this permanent — verify.

For closely-held businesses, §127 is useful for:
1. Owner-employees pursuing additional education.
2. Family members employed in business pursuing education.
3. Compensation alternative for valued employees.

§127(b) requirements:
- Written plan document.
- Available to all employees on nondiscriminatory basis (cannot
  exceed 5% to owners or HCEs).
- Employer paid (not salary-reduced).
- Employees must not have option to elect cash.

§127(c)(1) "qualified educational assistance":
- Tuition, fees, books, supplies, equipment.
- Through 2025: student loan principal and interest.
- Excludes courses involving sports, games, hobbies (unless related
  to employer's business).

## Primary IRC authority

- §127 — Educational assistance programs.
- §127(a) — $5,250 exclusion.
- §127(b) — Qualified plan requirements.
- §127(c) — Definition of qualified educational assistance.

## Treasury regulations

- Reg §1.127-1 through §1.127-2.

## Key IRS guidance

- IRS Publication 970 — Tax Benefits for Education.
- IRS Publication 535 — Business Expenses.

## Eligibility requirements

1. Written plan document.
2. Plan does not discriminate in favor of HCEs.
3. ≤5% of benefits to >5% owners or family members.
4. Cash election not available.
5. Educational assistance qualifies under §127(c).

## Mechanics — how it works

1. **Adopt written §127 plan.**
2. **Establish reimbursement procedure.** Employee submits invoices;
   employer reimburses.
3. **§127(b) nondiscrimination testing** annual.
4. **Pay or reimburse up to $5,250** per employee per year.
5. **Tax reporting:**
   - Excluded amount NOT in W-2 Box 1.
   - Employer deducts as §162.

## Documentation requirements

- Written plan document.
- Employee educational expense receipts.
- Reimbursement records.
- §127(b) nondiscrimination test annual.

## Common pitfalls / audit risks

- **No written plan.** §127 requires written plan.
- **Discrimination.** >5% owners receiving disproportionate
  benefits.
- **Cash election.** If employee can choose cash, exclusion lost.
- **Exceeds $5,250.** Excess in W-2 Box 1.
- **Non-qualified education.** Recreational courses don't qualify.

## Recent legislative changes

- **TCJA (2017)** — Allowed graduate-level education.
- **CARES Act (2020)** — Added student loan repayment through 2025.
- **CAA 2021** — Extended student loan provision.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §127
  student loan permanent Pub L 119-21]`. Reports indicate possible
  permanent extension.

## State conformity considerations

State conformity to §127 generally complete.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `employer-benefit-package-review` (#71).
- `college-student-strategies` (#60).
- `education-credits` (#61).
- `hra-merp` (#11).
- `hiring-kids` (#49).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 127","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section127","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.127-1","url":"https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1","weight":"regulation"}
  ]
}
```
```

---

## Strategy #46: Gifting Stock

**File:** `references/strategies/gifting-stock.md`

```markdown
---
name: "Gifting Appreciated Stock (and Other Securities)"
slug: gifting-stock
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§1015", "§170", "§2503", "§2511", "§2522"]
forms: ["Form 709", "Form 8283"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Gifting appreciated stock has multiple distinct planning uses:

1. **Charitable gifts of appreciated stock.** Donor deducts FMV
   under §170; avoids capital gain on sale; charity receives full
   FMV. Works only for long-term appreciated property.

2. **Family income shifting.** Gifting income-producing stock to
   lower-bracket family members (subject to kiddie tax §1(g)).

3. **Estate freeze.** Lifetime gifts use donor's lifetime gift tax
   exclusion ($13.61M per person 2024; possibly modified by
   OBBBA), removing future appreciation from estate.

4. **§1015 carryover basis.** Donee takes donor's basis (with
   special loss-property rules); gain on later sale may be
   significant.

5. **§2503(b) annual exclusion.** $18,000 per donor per donee
   (2024); not counted toward lifetime exclusion.

6. **Crummey trust gifts.** Gifts to trust qualify for §2503(b)
   if beneficiaries have demand right.

7. **§2522 charitable gift tax exclusion.**

## Primary IRC authority

- §170 — Charitable contributions deduction.
- §1014 — Basis at death (step-up).
- §1015 — Basis of property acquired by gift.
- §1411 — NIIT on net investment income.
- §2501 — Gift tax imposed.
- §2503(b) — Annual exclusion.
- §2510 — Lifetime gift exclusion.
- §2522 — Gift to charity exclusion.

## Treasury regulations

- Reg §1.170A-1 through §1.170A-17 — Charitable contributions.
- Reg §1.1014-1, §1.1015-1 — Basis.
- Reg §25.2503-1 through §25.2503-6 — Gift annual exclusion.
- Reg §25.2522(a)-1 — Charitable gift exclusion.

## Key IRS guidance

- Rev. Rul. 71-447 — Charity must have control over donated
  property.
- IRS Publication 526 — Charitable Contributions.
- IRS Publication 561 — Determining Value of Donated Property.

## Key court decisions

- **Crummey v. Commissioner, 397 F.2d 82 (9th Cir. 1968)** —
  Demand-right power makes gift "present interest" qualifying for
  annual exclusion.
- **Smith v. Commissioner, 78 T.C. 350 (1982), aff'd, 730 F.2d
  1356 (10th Cir. 1984)** — Charitable contribution valuation.

## Eligibility requirements

Charitable stock gift:
1. Long-term appreciated property (held >1 year).
2. Donee is qualified §170(c) charity.
3. Form 8283 if FMV >$500; appraisal if >$5,000 (with publicly-
   traded exception).
4. AGI limits: 30% for appreciated long-term capital gain property
   to public charities; excess carries forward 5 years.

Family gift:
1. Annual exclusion gifts: ≤$18,000/donor/donee/year (2024).
2. Lifetime exclusion gifts: ≤$13.61M lifetime per donor (2024;
   verify post-OBBBA).
3. Form 709 filed for split gifts or gifts >$18,000.

## Mechanics — how it works

Charitable gift:
1. **Identify long-term appreciated stock.**
2. **Transfer to charity** via brokerage transfer.
3. **Donor deducts FMV** (subject to AGI limits).
4. **Form 8283;** appraisal if >$5,000 (publicly-traded exception).

Family gift:
1. **Determine donor's basis.**
2. **Transfer stock** by brokerage transfer.
3. **Donee takes carryover basis** (no step-up).
4. **Form 709** if exceeds annual exclusion.

## Documentation requirements

- Brokerage transfer records.
- Charity acknowledgment letter; Form 8283.
- Form 709 (if applicable).
- Donor basis records.

## Common pitfalls / audit risks

- **Short-term gain property to charity.** Deduction limited to
  basis.
- **Loss property gifts.** Donee uses lesser of donor basis or
  FMV at gift for loss computation.
- **§170 substantiation.** Contemporaneous written acknowledgment
  required; appraisal for noncash >$5,000.
- **AGI limit miscalculation.** 30% / 50% / 60% limits depend on
  property type and donee.
- **Kiddie tax.** §1(g) imposes parent's bracket on dependent
  children's unearned income.

## Recent legislative changes

- **TCJA (2017)** — Doubled lifetime gift / estate exclusion;
  scheduled to sunset end of 2025.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §2010
  §2503 Pub L 119-21]`. Reports indicate lifetime exclusion made
  permanent at $15M+ inflation-adjusted level.

## State conformity considerations

**Connecticut** has state gift tax. Most states don't. State
conformity to charitable contribution deduction varies.

## Default confidence band rationale

**HIGH** for clearly-qualified gifts. Drops to MODERATE for
appraisal valuation issues.

## Cross-references

- `charitable-donation-appreciated` (#51).
- `donor-advised-fund` (#54).
- `charitable-planning` (#53).
- `income-shifting-family-member` (#48).
- `section-1202-qsbs` (#43).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 170","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section170","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1015","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1015","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 2503(b)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section2503","weight":"primary_statute"},
    {"authority_type":"CtAppeals","citation":"Crummey v. Commissioner, 397 F.2d 82 (9th Cir. 1968)","url":"https://www.courtlistener.com","weight":"binding_circuit"}
  ]
}
```
```

---

## Strategy #47: Income Shifting to C Corp

**File:** `references/strategies/income-shifting-to-c-corp.md`

```markdown
---
name: "Income Shifting to C Corporation"
slug: income-shifting-to-c-corp
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§11", "§531-537", "§541-547", "§482"]
forms: ["Form 1120"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

> **Caution:** Income shifting to a C corporation is a planning
> strategy that became more attractive after TCJA reduced the C
> corp rate to 21%. Common structures include forming a C corp
> service entity or holding company. Risks include §531
> accumulated earnings tax, §541 PHC tax, §482 transfer pricing
> scrutiny, reasonable compensation issues, and constructive
> dividend exposure. Practitioners should evaluate whether
> substance supports the structure beyond tax benefit.

## Overview

After TCJA reduced the C corp rate to 21% (vs. top individual rate
of 37%), income shifting from individual / pass-through to C corp
became economically attractive in some scenarios. Common structures:

1. **C corp service entity.** Owner forms separate C corp that
   provides management services to operating LLC/S corp at
   arm's-length fee. Some income shifted to C corp at 21% rather
   than passing through at 37% individual rate.

2. **C corp IP holding company.** IP held in C corp; licensed to
   operating entity at arm's-length royalty.

3. **Conversion to C corp.** S corp to C corp conversion (§1362(d)
   revocation).

4. **Choice-of-entity at formation.** Formation as C corp rather
   than S corp / LLC for new business.

The math: at 21% C corp rate plus subsequent dividend at 23.8%
(20% qualified dividend + 3.8% NIIT), effective combined rate is
approximately 39.8% — slightly above the 37% top individual rate.
Strategy works only if (a) earnings can be retained in corporation
rather than distributed, (b) eventual stock sale qualifies for
§1202 QSBS exclusion (#43), or (c) shareholder dies and basis
steps up under §1014.

The strategy is constrained by:
- **§531 accumulated earnings tax** — 20% penalty on unreasonable
  accumulation beyond ~$250K small business exemption.
- **§541 PHC tax** — 20% penalty on personal holding company
  failing to distribute earnings.
- **§482 transfer pricing** — intercompany pricing must be
  arm's-length.
- **Reasonable compensation** — both directions (#21).
- **Constructive dividends** — personal expenses run through
  C corp recharacterized as dividends.
- **§199A loss** — pass-through QBI deduction (20%) not available
  for C corps.

## Primary IRC authority

- §11 — C corp tax (21% rate).
- §531-537 — Accumulated earnings tax.
- §541-547 — PHC tax.
- §482 — Transfer pricing.
- §269 — Acquisition to avoid tax.
- §269A — Personal service corporation tax avoidance.
- §1361-1378 — S corp rules (S corp election / revocation).
- §199A — QBI (only for pass-through; flag for analysis).
- §1202 — QSBS (companion strategy).

## Treasury regulations

- Reg §1.482-1 through §1.482-9 — Transfer pricing.
- Reg §1.531-1 through §1.537-3 — Accumulated earnings.
- Reg §1.541-1 through §1.547-7 — PHC.

## Key IRS guidance

- IRS Publication 542 — Corporations.

## Key court decisions

- **Bardahl Manufacturing Corp. v. Commissioner, 24 T.C.M. 1030
  (1965)** — Bardahl formula for reasonable working capital
  needs.
- **Atlas Tool Co. v. Commissioner, 70 T.C. 86 (1978), aff'd, 614
  F.2d 860 (3d Cir. 1980)** — Constructive dividend.
- **Roubik v. Commissioner, 53 T.C. 365 (1969)** — Multiple-corp
  structures and §269A.

## Eligibility requirements

Vary by structure. Key considerations:
1. C corp legitimate business purpose.
2. §482 arm's-length pricing.
3. §269A personal service corporation.
4. §531/§541 accumulation justification.

## Mechanics — how it works

For C corp service entity:
1. **Form C corp** with reasonable business purpose (not solely
   tax-motivated).
2. **Service agreement with operating entity** at arm's-length
   pricing. §482 transfer pricing analysis required.
3. **C corp performs services** (separate office, employees, or
   identifiable function).
4. **Reasonable compensation to owner-employee** of C corp.
5. **Retain excess earnings in C corp** — invest in qualifying
   property; build §1202 QSBS basis if applicable.
6. **Annual §531 reasonable accumulation analysis** documenting
   business purpose.

For S to C conversion:
1. **Revoke S election** under §1362(d).
2. **5-year wait** before re-electing S status.
3. **Consider §1202 QSBS eligibility** for new C corp stock.

## Documentation requirements

- Business purpose memo for structure.
- Service agreements.
- §482 transfer pricing study.
- §531 accumulation analysis (Bardahl formula or similar).
- Board resolutions.
- Reasonable compensation analysis.

## Common pitfalls / audit risks

- **§269A personal service corporation.** Service corporations
  formed primarily for tax avoidance subject to penalty rates.
- **§482 transfer pricing.** Aggressive intercompany pricing
  challenged.
- **Constructive dividends.** Personal expenses run through C corp.
- **§531 accumulated earnings tax.** Excess accumulation beyond
  business needs.
- **§541 PHC tax.** Closely-held holding company with passive
  income.
- **Reasonable compensation.** Both excessive (treated as
  dividend) and insufficient (recharacterized as wages).
- **§199A loss.** Switching from pass-through forfeits §199A 20%
  deduction.
- **§1202 timing.** QSBS requires 5-year hold for full exclusion.
- **State conformity.** State may not follow federal C corp rate;
  state PTET-equivalent may not apply.

## Recent legislative changes

- **TCJA (2017)** — 21% C corp rate; created strategy attractiveness.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §11 §199A
  Pub L 119-21]`. If §199A made permanent and C corp rate
  unchanged, strategy economics reaffirmed; possible §1202
  expansion increases attractiveness.

## State conformity considerations

State C corp tax rates vary significantly. State conformity to
§482 transfer pricing varies. State combined-reporting rules may
collapse intercompany shifts.

## AICPA SSTS / Circular 230 considerations

Aggressive structure requiring substance documentation. Practitioner
should: verify business purpose; confirm §482 arm's-length pricing;
recommend Form 8275 disclosure for borderline positions; address
constructive dividend and reasonable compensation throughout
operating period.

## Default confidence band rationale

**MODERATE** — well-established structure but execution-sensitive.
HIGH for properly-documented separate-business C corps with clear
business purpose. LOW for aggressive shell structures lacking
substance.

## Cross-references

- `c-corp-dividends` (#31).
- `c-corp-misc-deductions` (#42).
- `c-corp-state-tax-savings` (#35).
- `section-1202-qsbs` (#43).
- `reasonable-comp-corp-owners` (#21).
- `choice-of-entity-se-tax` (#86).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 11","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section11","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 482","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section482","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 531","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section531","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 269A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section269A","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Bardahl Manufacturing Corp. v. Commissioner, 24 T.C.M. 1030 (1965)","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
```

---

**End of Part 5 of 10.** Strategies #38 through #47 delivered.

**Continue to Part 6 of 10** for strategies #48 through #57 (Income Shifting to Family Member, Hiring Kids, Wages: Spouse/Parents, Charitable Donation of Appreciated Assets, Charitable LLC, Charitable Planning, Donor Advised Fund, Family Limited Partnership, Unreimbursed Partnership Expenses, 529 Savings Plan).
