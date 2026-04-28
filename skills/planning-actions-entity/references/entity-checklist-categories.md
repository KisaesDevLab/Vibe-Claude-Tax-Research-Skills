# Entity planning checklist categories

For tax year 2024+ — verify year-specific thresholds via the
applicable Rev. Proc. before quoting figures.

## 1. Entity-level retirement plans

### Defined-contribution

- **401(k) with profit-sharing**: $69,000 limit per participant
  2024 (incl. $23K elective + employer profit-sharing).
- **SIMPLE IRA** (§408(p)): smaller employers; lower limits but
  simple administration.
- **SEP-IRA** (§408(k)): 25% of net SE earnings; max $69,000
  2024.
- **Solo 401(k)**: combined employee + employer for owner-only
  business; up to $69,000 + catch-up.

### Defined-benefit

- **§412 / §401(a) defined-benefit plan**: actuarially-determined
  contribution; can be very large for high-income owner-employees
  approaching retirement.
- **Cash-balance plan**: hybrid; defined-benefit format with
  defined-contribution presentation. Useful for combining with
  401(k) profit-sharing for substantial deferral.

### Deadline

- 401(k) employer contributions: by return due date incl.
  extensions.
- DB / cash-balance contributions: 8.5 months after plan year end
  (PBGC-covered) or earlier.
- New plan establishment: SECURE Act allows post-year-end
  establishment by return due date for SEP, SIMPLE, profit-sharing
  (not 401(k) elective).

## 2. Reasonable compensation (S-corp)

Route to `predict-reasonable-comp` for substantive analysis.
Planning checklist items:
- Annual reasonable-comp study at year-end.
- Document board minutes / compensation-committee deliberations.
- Adjust mid-year W-2 to align with industry comparables.
- Multi-shareholder reasonable-comp coordination.

## 3. §199A planning

Route to `predict-qbi-eligibility` for substantive analysis.
Planning checklist items:
- Threshold-band positioning (manage taxable income near phase-in).
- SSTB classification (e.g., crack-and-pack restructuring).
- Aggregation election under §1.199A-4.
- W-2 wage / UBIA optimization for above-threshold non-SSTBs.
- Rental safe-harbor compliance under Rev. Proc. 2019-38.

## 4. §163(j) management

- §163(j)(3) small-taxpayer exception: 3-year average gross
  receipts < $30M (2024). Exempts from §163(j).
- §163(j)(7)(B) real-property trade or business election:
  irrevocable; gives up §168(k) bonus on real property in
  exchange for §163(j) exemption.
- §163(j)(7)(C) farming election: similar.
- ATI computation: post-2022 EBIT-basis (not EBITDA).
- EBIE allocation at partnership level; carry-forward at partner
  level.
- Form 8990 filing required.

## 5. Depreciation acceleration

### §179 expensing

- 2024 limit: $1.16M expensing (verify year-specific Rev. Proc.);
  $2.89M phaseout.
- Available for tangible personal property and §1245 property
  used > 50% in trade or business.
- Cannot create or increase NOL.

### §168(k) bonus depreciation

- 100% for property placed in service after 9/27/2017 and before
  1/1/2023.
- 80% for 2023 / 60% for 2024 / 40% for 2025 / 20% for 2026 / 0%
  for 2027 (TCJA phase-out).
- OBBBA may have modified — verify per
  shared/legislation-tracking.md.
- Available for new and used property (§168(k)(2)(E) post-TCJA).

### Cost segregation

- Reclassify components of building purchase / construction into
  shorter-life §1245 categories (5, 7, 15-year).
- Coordinate with §168(k) bonus and §179.
- Form 3115 / §481(a) catch-up adjustment if cost-seg performed
  after the property placed in service.

### §263A UNICAP

- Inventory and self-constructed asset capitalization.
- §263A(b)(2) small-taxpayer exception: 3-year average gross
  receipts < $30M (2024).

## 6. State PTET elections

Route to `tax-research-state-income` per-state file. Common
attributes:
- Election operates at the entity level.
- Federal §164 deduction at the entity level (Notice 2020-75).
- Owner-level credit on state return.
- Election deadlines vary widely; some states require pre-payment
  by an early-year deadline.

States with PTET (representative — verify per-state file):
NY, CA, NJ, IL, CT, MA, MD, GA, MN, NC, OK, OR, RI, AL, AR, AZ,
CO, ID, IA, KS, KY, LA, MI, MS, MO, NE, OH, SC, UT, VA, WI, and
others.

## 7. §1202 QSBS

- §1202(a) — exclusion of up to 100% of gain on sale of QSBS
  held > 5 years (acquired after 9/27/2010).
- $10M / 10x basis cap on excluded gain (per issuer).
- §1202(c)(2) — domestic C-corp; aggregate gross assets ≤ $50M at
  issuance.
- §1202(e) active-business test.
- §1202(c)(2)(B) gross-asset limit measured at issuance and
  immediately after issuance.
- §1202(d) excluded businesses: SSTB-like list (health, law,
  consulting, etc.); banking, insurance, financing, hotels,
  restaurants, oil-and-gas extraction.
- §1045 rollover: defer §1202 gain by reinvesting in replacement
  QSBS within 60 days.

OBBBA modifications to §1202 thresholds — verify current.

## 8. Accountable plan (§62(c))

Three conditions:
1. Business connection (expenses must arise during the
   performance of services).
2. Substantiation within reasonable time (under §1.62-2(g)).
3. Return of excess within reasonable time.

Failure of any condition makes the entire plan non-accountable;
all reimbursements become wages.

Template documents to maintain:
- Written accountable-plan policy.
- Expense-report forms.
- Substantiation requirements (receipts, business purpose).
- Return-of-excess procedure.

## 9. Deferred compensation (§409A)

§409A applies to non-qualified deferred-compensation arrangements.
Failure penalty: ordinary income inclusion + 20% additional tax +
premium-interest.

Compliant arrangements satisfy:
- Written-plan requirement.
- Initial-deferral-election timing (typically by Dec 31 of prior
  year).
- Permitted distribution events (separation from service, death,
  disability, change in control, hardship, fixed time).
- 6-month delay for "specified employees" of public companies on
  separation.
- §409A(b)(3) anti-tying-to-employer-financial-condition.

## 10. M&A planning

- §351 / §368 / §332 / §338 reorganization analysis.
- §382 NOL limitation post-acquisition.
- §1202 QSBS preservation in stock-for-stock acquisitions.
- §263 capitalization of acquisition costs.
- §453 installment-sale treatment.

Route to `tax-research-entity` for substantive M&A analysis.

## 11. §174 R&E capitalization

Post-TCJA: 5-year domestic / 15-year foreign amortization. OBBBA
may have modified — verify.

§280C(c)(2) election to take reduced §41 R&D credit and avoid
§174 deduction reduction. For 21% C-corp rate, reduced credit =
credit × 0.79.

Route to `predict-r-and-d-credit` for substantive §41 analysis.

## 12. §163(l) and other interest limitations

- §163(l) — disallowed interest on debt issued for stock
  acquisition (anti-inversion, applicable corporations).
- §279 — original-issue-discount on certain corporate
  acquisition debt.
- §385 — debt-vs-equity (route to `predict-debt-vs-equity`).

## 13. State franchise / margin / gross-receipts tax

Route to `tax-research-state-income` per-state file. Examples:
- TX margin tax (gross-receipts based).
- WA B&O tax (gross-receipts based).
- DE franchise tax (capital-stock based).
- CA $800 minimum LLC fee.
- TN F&E tax.

## 14. International planning

Route to `tax-research-international` for substantive analysis:
- §245A DRD eligibility.
- §951A GILTI inclusion management.
- §250 FDII deduction.
- §59A BEAT exposure.
- §367 outbound reorganizations.
- Treaty optimization.
- Pillar 2 / GloBE rules implementation in foreign jurisdictions.

## 15. Form 8975 country-by-country reporting

Required for U.S. parent of MNE group with annual revenue ≥ $850M.

## 16. Worker classification

Route to `predict-worker-classification` for substantive analysis.
Planning checklist:
- Annual review of contractor classification.
- §530 safe-harbor preservation (consistent treatment, 1099
  filing, reasonable basis).
- VCSP eligibility.
- ABC-test state exposure (CA, MA, NJ, IL, CT).

## Disclosure flags (per SSTS / Circular 230)

For any aggressive strategy, the practitioner must:
- Document the substantive position.
- Determine if Form 8275 / 8275-R / 8886 disclosure is required.
- Note SSTS §1.1 realistic-possibility and §2.3 use-of-estimates.
- Note Circular 230 §10.37 written-advice standards.

## Dirty-Dozen / Listed Transaction warning

The following strategies are flagged by the IRS and must NOT
appear without an explicit warning banner and Form 8886
disclosure analysis:

- §831(b) micro-captives (Notice 2016-66).
- Syndicated conservation easements (Notice 2017-10).
- Monetized installment sales.
- Charitable LLC structures.
- Pre-packaged "tax shelters" of any kind.

Route to `predict-economic-substance` for any §7701(o) analysis
required.
