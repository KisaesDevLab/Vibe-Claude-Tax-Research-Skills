---
name: predict-qbi-eligibility
description: |
  Predicts whether a taxpayer's income qualifies for the IRC §199A
  Qualified Business Income deduction, including the Specified
  Service Trade or Business (SSTB) limitation, the W-2 wage and
  unadjusted-basis-in-qualified-property (UBIA) limitations, the
  rental-real-estate safe harbor under Rev. Proc. 2019-38, and
  aggregation under Treas. Reg. §1.199A-4. Use when the user asks
  "do I qualify for QBI", "199A deduction", "SSTB", "specified
  service trade", "W-2 wage limitation", "UBIA limitation", "QBI
  threshold", "real estate enterprise safe harbor", or "aggregation
  for §199A". Make sure to use this skill whenever the user mentions
  QBI, §199A, SSTB, qualified business income, or pass-through
  deduction.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-qbi-eligibility — §199A Qualified Business Income deduction

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — TCJA (Pub. L. 115-97) created
   §199A; verify any post-2024 amendments via Classification Tables
   before stating "current law".
6. `references/sstb-tests.md` — SSTB list and reputation/skill
   facts-and-circumstances guidance.

## Operative authority

- IRC §199A — added by TCJA, Pub. L. 115-97 §11011 (2017).
- Treas. Reg. §1.199A-1 through §1.199A-6 (2019).
- Treas. Reg. §1.199A-4 — aggregation rules.
- Treas. Reg. §1.199A-5 — SSTB definition (rebuttable de-minimis
  rule: < 10% gross receipts from SSTB activity if total < $25M;
  < 5% if total ≥ $25M).
- Rev. Proc. 2019-38 — rental-real-estate safe harbor (250 hours).
- Notice 2019-07 — superseded by Rev. Proc. 2019-38 but still in
  citation chains.

## Workflow

### 1. Intake

- `tax_year`
- `filing_status`
- `taxable_income_before_QBI`: needed for threshold testing
- `business_or_businesses`: list with type, gross receipts, W-2
  wages paid, UBIA of qualified property
- `is_sstb`: yes/no/uncertain (the practitioner's facts-driven
  call)
- `aggregation_election_filed`: yes/no
- `rental_safe_harbor_qualifying`: yes/no/n/a (250-hour test;
  separate books and records)

### 2. Threshold gate

For tax year 2024, thresholds (verify year-appropriate Rev. Proc.
or §199A(e) inflation-adjusted figures):

- Single / HoH / MFS: phase-in begins at $191,950; complete at
  $241,950.
- MFJ: phase-in begins at $383,900; complete at $483,900.

Below the lower threshold: SSTB / W-2 / UBIA limits do NOT apply.
Within phase-in: pro-rated. Above the upper threshold: full SSTB
disqualification (if SSTB) AND W-2 / UBIA cap on non-SSTB.

If the taxable-income figure is missing, request it; the threshold
gate is dispositive.

### 3. SSTB analysis (if relevant)

§199A(d)(2)(A) lists health, law, accounting, actuarial science,
performing arts, consulting, athletics, financial services,
brokerage services, investment management, dealing in securities/
partnership interests/commodities — and any trade or business where
the principal asset is the reputation or skill of one or more
employees or owners.

Treas. Reg. §1.199A-5(b)(2)(xiv) narrows "reputation or skill" to
three specific situations: endorsement income, licensing of
likeness, and appearance fees. Service businesses outside the
enumerated list are NOT SSTBs merely because they involve
professional skill.

The de-minimis rule (§1.199A-5(c)(1)):
- Total gross receipts < $25M: ≥ 10% from an SSTB activity makes
  the entire trade or business an SSTB.
- Total gross receipts ≥ $25M: ≥ 5% threshold.

### 4. W-2 wages / UBIA cap (above-threshold non-SSTB)

§199A(b)(2)(B): the deduction is limited to the GREATER of:
- 50% of W-2 wages paid by the trade or business; OR
- 25% of W-2 wages PLUS 2.5% of UBIA of qualified property.

Verify the W-2 wage figure with Form W-3 / Box 1 of W-2. UBIA is
the unadjusted basis immediately after acquisition (not net of
depreciation) of "qualified property" (depreciable tangible
property held at year-end, used in the qualified trade or
business, and within its depreciable period).

### 5. Aggregation (§1.199A-4)

Aggregation may help when one trade-or-business has wages but
little QBI and another has QBI but no wages. Five tests
(§1.199A-4(b)(1)):

1. Each trade or business is itself a qualified trade or business.
2. Same person or group owns ≥ 50% of each.
3. Same tax year (not for partial-year changes).
4. None is an SSTB.
5. Two of three: same products/services; same shared facilities
   or shared business elements; or operated in coordination.

Aggregation election filed annually with the return; binding once
made.

### 6. Rental safe harbor (Rev. Proc. 2019-38)

Real-estate rental activity is a §199A-qualifying trade or business
if all conditions met:
- Separate books and records for each rental enterprise.
- ≥ 250 hours of rental services per year (for the enterprise as a
  whole — taxpayer + employees + agents + contractors).
- Contemporaneous records (effective for tax years beginning after
  2019).
- Statement attached to the return.

Triple-net leases EXCLUDED from the safe harbor. Real estate used
as residence by the taxpayer for any part of the year EXCLUDED.

### 7. Conclusion

Confidence band per `shared/confidence-bands.md`:

- HIGH: under threshold OR clearly non-SSTB and W-2/UBIA cap not
  binding OR safe-harbor met cleanly.
- MODERATE: within phase-in OR SSTB analysis is fact-driven.
- LOW: above threshold + SSTB call disputed OR rental safe-harbor
  partial.
- SPECULATIVE: clearly an SSTB above the upper threshold.

### 8. Authorities + sidecar

Cite §199A, relevant Treas. Regs., Rev. Proc. 2019-38, and any
case law (limited as of 2026; the regulatory framework dominates).
JSON sidecar validates against `shared/output-schema.json`.

For Public-Law-touching questions (TCJA permanence, OBBBA
modifications), populate `public_laws_consulted[]` per
`shared/legislation-tracking.md`.

## Hard rules

- Never apply the SSTB bar without first checking the threshold
  gate.
- Never claim the rental safe harbor without the 250-hour log AND
  separate books AND statement attached.
- Never claim Chevron deference for Treas. Reg. §1.199A-5;
  reputation-or-skill narrowing is a Loper-Bright-vulnerable
  interpretation. Note the §1.6662 substantial-authority posture.
- Drop one band when relying solely on Treas. Reg. §1.199A-5 for
  a non-enumerated trade-or-business outside the three reputation
  prongs.
- Verify any year-specific threshold via the year-appropriate
  inflation-adjustment Rev. Proc. before stating numbers.

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. For high-stakes positions (large QBI
deduction, contested SSTB classification), include the
negative-treatment-review residual practitioner responsibility.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
