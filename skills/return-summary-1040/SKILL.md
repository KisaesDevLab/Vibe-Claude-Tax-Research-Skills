---
name: return-summary-1040
description: |
  Summarizes an individual federal Form 1040 return for a CPA — line-
  by-line key figures, AGI, taxable income, total tax, refund or
  balance due, effective and marginal rates — and surfaces planning-
  relevant red flags (large Schedule A, capital-loss carryover,
  unused QBI, unfilled HSA, missing estimated payments, AMT exposure,
  net investment income tax exposure, dependency or filing-status
  edge cases). Use when the user pastes a 1040, asks "summarize this
  return", "what should I look at on this 1040", "what planning
  opportunities does this return surface", "find red flags", or asks
  for a quick AGI / TI / total-tax readout. Make sure to use this
  skill whenever the user mentions Form 1040, Schedule A / B / C / D
  / E / SE, AGI, taxable income, marginal rate, NIIT, AMT, or
  estimated payments.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# return-summary-1040 — Individual return summary

Flagship summary skill. Produces a structured readout of Form 1040
key lines, computes effective and marginal rates, and surfaces
planning-relevant red flags. Does NOT produce tax-position advice;
that is the job of `planning-actions-1040` or `tax-research-federal`.

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/line-keys.md` — Form 1040 / Schedule line numbers and
   computed values
6. `references/red-flags.md` — pattern catalog for planning hooks

## Workflow

### 1. Intake

Accept any of the following:

- Full Form 1040 PDF (text-extractable) or pasted text
- A list of line-item amounts the user has typed (line N = $X)
- A summary table (e.g., AGI, taxable income, total tax) with at
  least three of the five core figures

If the input is incomplete, request the missing core figures or
proceed with explicit assumptions noted in the output.

### 2. Extract the core figures

From Form 1040 (2024 + tax year):

- Filing status (line 1) and number of dependents
- Total income (line 9)
- Adjusted gross income (line 11)
- Standard or itemized deduction amount (line 12; if itemized, sum
  Schedule A subtotals)
- QBI deduction (line 13)
- Taxable income (line 15)
- Tax (line 16, before credits)
- Credits and payments
- Total tax (line 24)
- Total payments (line 33)
- Refund or balance due (line 34 / line 37)

For prior years, line numbers shift; use the year-appropriate
version of `references/line-keys.md`.

### 3. Compute derived figures

- **Effective tax rate** = total tax (line 24) / total income (line
  9). Round to 2 decimals.
- **Marginal tax rate** = bracket containing taxable income (line
  15) for the filing status, year-appropriate.
- **Average federal tax burden** = total tax / AGI.
- **Withholding gap** = total tax minus withholding (Form W-2 +
  1099) — flags estimated-payment shortfall.

For 2024 brackets, look up the year-appropriate inflation-adjustment
Rev. Proc. (e.g., the IRS publishes one each fall keyed to the
following year). If the relevant Rev. Proc. cannot be retrieved at
runtime, emit the sentinel pattern documented in
`shared/citation-discipline.md` with the search query
`inflation-adjusted individual brackets <tax year> rev proc`.

The skill must look up the correct Rev. Proc. for the relevant tax
year before stating any bracket as fact.

### 4. Schedule walk

For each Schedule attached, surface:

- **Schedule A**: total itemized; if SALT cap binding (SALT > $10K,
  $5K MFS), flag PTET opportunity for state-passthrough owners.
- **Schedule B**: high taxable interest (> $4K) or foreign accounts
  (Part III) — flag FBAR / Form 8938.
- **Schedule C**: net profit, hobby-loss test trigger (3 of 5
  rule), SE-tax exposure, retirement-plan opportunity (Solo 401(k),
  SEP).
- **Schedule D / Form 8949**: large net capital loss carryover
  ($3K limit per § 1211(b)); wash-sale items (§ 1091).
- **Schedule E**: passive vs. nonpassive; § 469 grouping; real-
  estate-professional possibility (route to `predict-real-estate-pro`);
  K-1 sources.
- **Schedule SE**: SE-tax computation; one-half above-the-line
  deduction.

### 5. Red-flag catalog

Run the input through `references/red-flags.md`. Flag each pattern
with a short note and a suggested next-skill route.

### 6. Conclusion

Single paragraph: filing status, AGI, TI, total tax, effective
rate, marginal rate, refund/balance, top 3 red flags, top 3
planning opportunities. NO tax-position advice.

### 7. JSON sidecar

Emit JSON validating against `shared/output-schema.json`. Required
fields: `skill, version, generated_at, task, conclusion,
confidence_band, authorities, verification_checklist`.

For a return-summary skill, `confidence_band` reflects accuracy of
the extraction — typically HIGH when the user provided a full PDF,
MODERATE when figures were typed, LOW when key figures were
estimated. The confidence band does NOT imply tax-position
confidence (that's outside this skill's scope).

`authorities[]` should cite the IRS Form 1040 instructions for the
relevant year (`Form` / `persuasive_non_authority`) and any Rev.
Proc. or IRC section invoked for derived figures.

## Hard rules

- This skill summarizes; it does NOT advise. Tax-position advice
  is the job of `planning-actions-1040` or `tax-research-federal`.
- Never fabricate a line-item value. If the user did not provide
  it and it cannot be derived, mark "not provided" in the output.
- Never assert a bracket or threshold without retrieving the year-
  appropriate Rev. Proc. (or emit the sentinel pattern documented
  in `shared/citation-discipline.md`).
- Treat the input as confidential client data; do NOT echo SSN,
  taxpayer name, or address verbatim — redact with `[REDACTED]`.
- For state piggyback summaries, route to
  `tax-research-state-income` for the state's specific rules; this
  skill is federal-only.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. For a return summary, the SSTS § 2.3
"use of estimates" item is most often invoked when the user has
typed approximate numbers — flag any imputed values explicitly.
