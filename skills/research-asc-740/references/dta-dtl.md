# ASC 740 — DTA / DTL Identification, Measurement, Scheduling

Deferred tax assets (DTAs) and deferred tax liabilities (DTLs)
arise from temporary differences between book and tax basis of
assets and liabilities, plus tax loss / credit carryforwards.

## What creates a temporary difference (ASC 740-10-25-20)

A temporary difference is a difference between:
- The reported amount of an asset / liability in F/S; AND
- The tax basis of that asset / liability.

Examples:
- Accrued expenses deductible when paid (book accrued, tax not
  yet deducted) → DTA.
- Accelerated tax depreciation vs. straight-line book → DTL
  (book carries higher value than tax basis).
- Unrealized gain on AFS securities (book recognized through
  OCI, tax recognized at sale) → DTL.
- Warranty reserves (book accrued, tax deducted on payment) → DTA.
- Goodwill — depends on whether tax-basis goodwill exists and
  how it amortizes vs. book impairment.
- Stock compensation expense recognized over vesting (book) vs.
  deduction on exercise (tax) → DTA initially, DTL upon
  measurement of windfall / shortfall.

## Permanent differences

Differences that will NEVER reverse — NO DTA / DTL.
Examples:
- Tax-exempt interest (book income, no tax).
- §263A capitalization differences if permanent.
- §168(k) bonus depreciation — if it is just a timing difference
  between accelerated tax and straight-line book, it's
  TEMPORARY (DTL); but transition rules and AMT can create
  permanent components.
- §162(m) excess executive compensation (book deducted, tax not).
- Penalties and fines (book deducted, tax not).
- Domestic Production Activities Deduction §199 (legacy).
- Tax credits used currently (book and tax difference, but
  classification of credit usage is permanent).

## Carryforwards

Tax loss and credit carryforwards create DTAs:
- Net operating loss (NOL) carryforwards (post-TCJA: indefinite,
  80% limit).
- Capital loss carryforwards (corporations: 5-year carryforward;
  individuals via flow-through: 5-year/lifetime depending).
- Foreign tax credit (FTC) carryforwards (1-year carryback,
  10-year carryforward).
- Charitable contribution carryforwards (5 years for corporations
  under §170(d)).
- §174 R&E capitalization residual creates timing differences.

DTAs from carryforwards subject to valuation allowance.

## Measurement (ASC 740-10-30-2)

DTA / DTL = Temporary difference × Enacted tax rate(s) for the
period(s) of reversal.

- Use ENACTED rates, not proposed or expected rates.
- Substantively-enacted rates not used; only fully enacted
  legislation triggers a remeasurement.
- Rate change recognized in the period of enactment as a
  discrete item.

For multi-jurisdictional DTLs / DTAs:
- Federal rate (currently 21% for C-corps; check periodically).
- State rate (apportioned; net-of-federal-benefit when state tax
  is deductible federally).
- Foreign rate (applicable to foreign subsidiary's pre-tax book
  vs. tax basis differences).

## Scheduling (ASC 740-10-30-9)

DTLs and DTAs reverse over time. Scheduling matters when:
- Different tax rates apply in different periods (e.g., recent
  TCJA changes; pending legislative changes scheduled to expire).
- Valuation allowance evaluation requires matching DTL reversals
  to DTA reversals.
- Rate changes are enacted but not yet effective.

Scheduling is a judgment area. ASC 740 does NOT require detailed
scheduling unless the conclusion turns on it; many entities use
simplified approaches when conclusions are not rate-sensitive.

## Classification (ASC 740-10-45)

Per ASU 2015-17 (effective for PBE 2017, non-PBE 2018):
- ALL DTAs and DTLs classified as NONCURRENT on the balance sheet,
  regardless of the timing of reversal.
- Exception removed: prior rule classified as current/noncurrent
  based on timing of reversal of underlying asset/liability.

## Naked credit / "naked" DTL

A "naked credit" / DTL is a DTL that does not have a finite
reversal date because the underlying asset is indefinite-lived
(e.g., indefinite-lived intangible, goodwill in an asset
acquisition that wasn't a business combination).

- Cannot serve as a source of taxable income for VA on DTAs that
  reverse in finite periods (mismatch in scheduling).
- Indefinite-lived DTLs scheduling is unsettled in older
  guidance; ASU 2015-17 simplifies presentation but does NOT
  resolve VA-source matching.

## Cross-domain — IRC source for the tax basis

The tax basis of an asset / liability is determined under IRC and
Treas. Reg. — federal income tax law. For a UTP, the tax basis
itself may be uncertain. Cross-reference `tax-research-federal`
for the substantive tax-basis analysis.

## Disclosure (ASC 740-10-50-2)

- Significant components of DTAs and DTLs.
- Total VA at year-end.
- Approximate carryforward amounts and expiration dates.
- Significant rate-rec items.

## Cross-references

- VA evaluation: `valuation-allowances.md`.
- UTP: `utp-recognition-measurement.md`.
- Disclosures: `disclosures.md`.
- IRC sections affecting tax basis: `tax-research-federal`.

## Authority

Cite ASC 740-10-25 / -30 / -45 paragraphs as
`authority_type: FASB_ASC`, `authority_domain: gaap`,
`weight: gaap_codified`. Pin-cite to specific paragraph.
