---
name: predict-real-estate-pro
description: |
  Predicts whether a taxpayer qualifies as a real-estate professional
  under IRC §469(c)(7) so that rental activities may escape the §469
  passive-activity loss limitation. Applies the two-pronged 750-hour
  / more-than-half-of-personal-services test, the material-
  participation overlay, and the elective grouping under Reg.
  §1.469-9(g). Use when the user asks "do I qualify as a real-estate
  professional", "REPS election", "rental losses against W-2 income",
  "750-hour test", "material participation in rentals", "Hardy",
  "aggregation election", "short-term rental loophole", or "STR
  loophole". Make sure to use this skill whenever the user mentions
  real-estate professional, REPS, §469(c)(7), passive losses, rental
  losses against ordinary income, or aggregation election.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-real-estate-pro — §469(c)(7) qualification

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/quantitative-tests.md` — 750-hour, ½-personal-services,
   material-participation tests with audit-defense documentation.

## Operative authority

- IRC §469(c)(7) — real-estate-professional carve-out from passive
  classification of rental activities.
- IRC §469(h) and Treas. Reg. §1.469-5T — material-participation
  seven tests.
- Treas. Reg. §1.469-9 — definitions, grouping election (§1.469-9(g)).
- Bailey v. Commissioner, T.C. Memo. 2001-296 — contemporaneous log
  expectations.
- Hakkak v. Commissioner, T.C. Memo. 2020-46 — daily-log discipline.
- Hardy v. Commissioner, T.C. Memo. 2017-16 — aggregation
  consequences.

## Workflow

### 1. Intake

- `tax_year`: integer
- `filing_status`: MFJ / S / HoH / MFS
- `w2_employment`: hours per year and nature of W-2 work (the
  more-than-half-of-personal-services prong frequently fails for
  taxpayers with > 1,000 hour W-2 jobs)
- `rental_properties`: list with hours / activities for each
- `aggregation_election_filed`: yes/no/year
- `material_participation_per_property`: hours and tests met
- `short_term_rental_question`: average rental period ≤ 7 days
  (different rule — see §1.469-1T(e)(3)(ii); these are NOT rental
  activities for §469 purposes and do NOT require REPS)

### 2. Two-prong qualifying test

Both must be met for the year (per spouse — the "spouse-by-spouse"
rule of §469(c)(7)(B), confirmed by Hakkak):

1. **More than half of personal services** in real-property trades
   or businesses (§469(c)(7)(C)) in which the taxpayer materially
   participates.
2. **More than 750 hours** of services during the taxable year in
   real-property trades or businesses in which the taxpayer
   materially participates.

The W-2 job is the most common failing point for prong 1. A
taxpayer working 2,000 hours in a non-real-estate W-2 cannot pass
prong 1 unless they spend > 2,000 hours in real-estate.

### 3. Material-participation overlay

Even if a taxpayer is a real-estate professional, EACH rental
activity must independently satisfy material participation under
§469(h) / §1.469-5T (seven tests). The §1.469-9(g) aggregation
election treats all rental real-estate interests as a single
activity for material-participation purposes only.

### 4. Aggregation election (§1.469-9(g))

- Filed once and binding for all future years until revoked.
- Strongly recommended for taxpayers with multiple rentals where
  the per-property hour count is below 500 / 100.
- Hardy v. Commissioner — failure to file the election is fatal
  for material participation in any individual property below the
  thresholds.

### 5. Short-term rental clarification

Per Reg. §1.469-1T(e)(3)(ii), an activity is NOT a rental activity
if average customer use is ≤ 7 days. Short-term rentals (STRs) are
trade-or-business activities subject to material-participation
testing without needing REPS qualification. The popular "STR
loophole" relies on this provision combined with §1.469-5T material
participation. A taxpayer with active management of a single STR
who passes test 1 (> 500 hours) or test 4 (significant participation
> 100 hours) can deduct losses without REPS.

### 6. Conclusion

Confidence band per `shared/confidence-bands.md`:

- HIGH: clear contemporaneous log + W-2 < 1,000 hrs (or no W-2) +
  > 750 RE hours + materially participates in each property OR
  aggregation election filed.
- MODERATE: log present but reconstructive; close on the prong-1
  half-of-personal-services test.
- LOW: substantial W-2 employment; reconstructed log; aggregation
  not elected.
- SPECULATIVE: no log; W-2 work clearly dominates personal services.

Recommend Form 8275 disclosure when band is LOW (reasonable-basis
path for §469 position). Note: aggregation election is filed by
attaching a statement to the return; not a separate form.

### 7. Authorities + sidecar

Cite §469(c)(7), §469(h), Treas. Reg. §1.469-5T, §1.469-9, and
relevant case law. JSON sidecar validates against
`shared/output-schema.json`.

## Hard rules

- Never recommend REPS qualification without a contemporaneous log
  walk-through.
- Never assert the aggregation election was filed if the taxpayer
  cannot produce the election statement.
- Never apply REPS to short-term rentals without first explaining
  the §1.469-1T(e)(3)(ii) carve-out.
- Drop one band when the log is reconstructive; drop another when
  the W-2 hour count exceeds the RE hour count.
- Never claim Chevron deference for Treas. Reg. §1.469-5T.

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. For high-stakes positions (multi-year REPS
strategy), include the negative-treatment-review residual
practitioner responsibility.
