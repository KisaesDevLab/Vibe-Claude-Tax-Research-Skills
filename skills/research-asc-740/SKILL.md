---
name: research-asc-740
description: |
  ASC 740 income tax accounting research. Covers UTP recognition
  and measurement (ASC 740-10-25 two-step), valuation allowances,
  DTA/DTL recognition, intraperiod allocation, disclosures.
  Cross-references tax-research-federal for the underlying tax-
  position substantial-authority analysis. Routes any non-740 ASC
  question to research-financial-reporting. Use when the user asks
  "ASC 740", "deferred tax", "DTA", "DTL", "valuation allowance",
  "uncertain tax position", "UTP", "FIN 48", "tax provision",
  "effective tax rate", "intraperiod allocation", "ASC 740
  disclosure", "tax footnote", or "book-tax difference" (when GAAP
  side dominates). Make sure to use this skill whenever the user
  mentions ASC 740, deferred taxes, UTP, valuation allowance, or
  tax provision in a financial-reporting context.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# research-asc-740 — ASC 740 income tax accounting

Sits at the boundary between U.S. GAAP financial reporting and
federal/state income tax. Cross-references `tax-research-federal`
for substantial-authority analysis underlying a UTP recognition
decision.

## Read before output

1. `shared/citation-discipline.md` — authority_domain: gaap (for
   ASC) and tax_position (for IRC referenced from the tax memo).
2. `shared/authority-hierarchy.md` — GAAP authority subsection.
3. `shared/confidence-bands.md` — band assignment.
4. `shared/compliance.md` — GAAP research scaffolding.
5. `references/utp-recognition-measurement.md` — ASC 740-10-25
   two-step recognition and measurement.
6. `references/valuation-allowances.md` — ASC 740-10-30
   recognition and reversal.
7. `references/dta-dtl.md` — DTA and DTL identification,
   measurement, scheduling.
8. `references/intraperiod-allocation.md` — ASC 740-20.
9. `references/disclosures.md` — ASC 740-10-50 + ASU 2023-09.

## Operative authority

- ASC 740 (Income Taxes) — primary.
- Cross-domain references to IRC for the tax position underlying a
  UTP recognition or measurement decision.
- ASU 2023-09 — Income Taxes — Disclosures (rate reconciliation
  + income tax paid). Effective for PBE annual periods after Dec.
  15, 2024; non-PBE Dec. 15, 2025.

## Workflow

### 1. Intake

- `entity_type`: nonissuer (typical) | issuer | governmental
  (route GASB) | nonprofit | pass-through (S-corp / partnership —
  ASC 740 applies at the entity for entity-level taxes;
  pass-through items are not provided unless taxable to the
  entity)
- `framework`: U.S. GAAP | private-company alternatives (PCC has
  no specific 740 elections beyond goodwill / receivables) |
  IFRS (route externally; IAS 12 differs from ASC 740)
- `issue_area`: UTP recognition / measurement | DTA / DTL
  identification | valuation allowance | intraperiod allocation |
  disclosure | tax provision computation | other ASC 740
- `tax_year` / `fiscal_year_end`: integer
- `position_underlying_utp`: brief description of the tax position
  if the question is UTP; route the substantive tax analysis to
  `tax-research-federal`

### 2. Out-of-scope routing

- Governmental entity → GASB Codification (governmental tax
  accounting differs).
- IFRS reporter → IAS 12 + IFRIC 23 (route externally).
- Issuer with significant SEC overlay → ASC 740 still applies but
  SEC SAB Topic 5.J / 11 commentary may add layers; route SEC-
  specific overlay externally.

### 3. Issue-specific routing

- **UTP recognition / measurement** → walk `references/utp-
  recognition-measurement.md`. Cross-reference
  `tax-research-federal` for the underlying tax-position analysis
  (substantial-authority, more-likely-than-not, etc.).
- **DTA / DTL** → walk `references/dta-dtl.md`.
- **Valuation allowance** → walk `references/valuation-
  allowances.md`.
- **Intraperiod allocation** → walk `references/intraperiod-
  allocation.md`.
- **Disclosure** → walk `references/disclosures.md`.

### 4. Recognition / measurement framework

**ASC 740 two-step (ASC 740-10-25)**:
1. **Recognition**: Tax position recognized only if more-likely-
   than-not (MLTN, > 50%) sustained on examination based on
   technical merits, assuming examiner has full knowledge.
2. **Measurement**: Largest amount more than 50% likely of being
   realized upon ultimate settlement (cumulative probability).

**Valuation allowance (ASC 740-10-30-17)**: Reduce DTA to the
amount more likely than not to be realized. Sources of taxable
income evaluated:
- Future reversals of existing taxable temporary differences.
- Future taxable income exclusive of reversing temporary
  differences and carryforwards.
- Tax-planning strategies (TPS).
- Carryback to prior taxable years.

### 5. Conclusion

State the GAAP conclusion: recognition outcome (recognize or do
not recognize), measurement amount, valuation-allowance
conclusion, intraperiod allocation, disclosure requirements.

Confidence band per `shared/confidence-bands.md`. ASC 740
questions typically land HIGH for codified rules but MODERATE
for judgment-heavy areas (UTP measurement when authority is
mixed; valuation allowance with significant scheduling judgment;
intraperiod allocation with complex APIC components).

### 6. JSON sidecar

`authority_domain: gaap` for ASC 740 citations.
`authority_domain: tax_position` for IRC / Treas. Reg. /
Tax-Court citations referenced for UTP underlying analysis.
`verification_checklist_gaap` populated.

## Hard rules

- Never recognize a UTP that is NOT more-likely-than-not under
  ASC 740-10-25.
- Never measure a recognized UTP at less than the largest amount
  more-than-50%-likely under ASC 740-10-25.
- Always evaluate the four sources of taxable income for VA
  determination.
- Always cite IRC for the tax position underlying a UTP — this
  is cross-domain; tag IRC as `authority_domain: tax_position`.
- Never claim Chevron / Skidmore for ASC 740.
- Always disclose UTP unrecognized tax benefit per ASC 740-10-50
  + ASU 2023-09 rate reconciliation requirements.

## Verification checklist (appendix)

End the markdown response with the GAAP research scaffolding
module + tax-position SSTS / Circular 230 module (the latter
applies to the underlying tax positions; route to
`compliance-ssts-circular230` for the tax-position checklist).

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
