# Engagement letter library — index

Per-engagement-type templates (in `letters/`) and cross-cutting
reference files. Each template includes:
- Required AICPA elements (cited).
- Bracketed fields the firm fills in.
- Engagement-specific risk-allocation language.
- A "practitioner notes" section.

All templates are starting frameworks — firm counsel reviews and
tailors before client use.

## Per-engagement templates

### Attest (independence required)
- `letters/audit.md` — Nonissuer audit (AU-C §210).
- `letters/review.md` — SSARS review (AR-C §90).
- `letters/compilation.md` — SSARS compilation (AR-C §80).
- `letters/preparation.md` — SSARS preparation (AR-C §70).
- `letters/soc1.md` — SOC 1 service organization (AT-C §320).
- `letters/soc2.md` — SOC 2 service organization (AT-C §205 + Trust
  Services Criteria).

### Attestation other
- `letters/aup.md` — Agreed-upon procedures (AT-C §215).

### Tax
- `letters/tax-1040.md` — Individual income tax (1040).
- `letters/tax-business.md` — Business returns (1120, 1120-S,
  1065, 706, 709, 990).
- `letters/tax-advisory.md` — Tax planning / advisory (non-return
  preparation).

### Other / non-attest
- `letters/bookkeeping.md` — Bookkeeping / write-up (note §1.295
  if client is also attest).
- `letters/payroll.md` — Payroll services.
- `letters/consulting.md` — Consulting / advisory.

## Cross-cutting reference files

- `common-clauses.md` — recurring clauses (fee/billing, dispute
  resolution, termination, communication, confidentiality,
  e-signature, governing law).
- `ftc-safeguards-rule.md` — required for tax engagements.
- `indemnification-state-overlay.md` — CA, IL, NJ stricter
  limits + AICPA Ethics Interpretation §1.400.205 attest-
  independence implications.

## Authority structure

Each per-engagement template is anchored to the relevant AICPA
standard. Attest templates cite AU-C / AR-C / AT-C with
`authority_domain: professional_conduct`, `weight: binding_on_member`.
Tax templates cite AICPA Tax Section practice aids with
`weight: practice_aid` plus IRC §7216 and FTC Safeguards Rule for
binding clauses.

## Sentinel-permitted directory

Per `scripts/validate.sh`, the
`engagement-letter-library/references/letters/` directory is
exempted from the verification-flag grep. Per-template files MAY
include the verification-flag sentinel pattern (per
`shared/citation-discipline.md`) where firm counsel must complete
jurisdiction-specific language. This is a deliberate verification
flag, not a fabrication.

## State-board overlay reminder

Engagement letters do not satisfy state-board licensure or firm
registration requirements. Confirm:
- Firm licensed in `engagement_state` for engagements involving an
  attest opinion.
- Mobility provisions for cross-state attest engagements.
- Stricter independence rules per `compliance-aicpa-code` skill's
  state-board overlay.

## Hard rules echo

1. Templates are NOT legal advice. Firm counsel reviews before
   client use.
2. State UPL rules vary.
3. Indemnification provisions on attest engagements may impair
   independence (AICPA Ethics Interpretation §1.400.205).
4. Contingent fees prohibited on attest, return preparation,
   amended returns (AICPA Code §1.510).
5. FTC Safeguards Rule clause required for tax engagements.
