---
name: predict-hobby-loss
description: |
  Predicts whether an activity rises to a trade or business under
  IRC §183 (the "hobby-loss" rule) by applying the nine factors in
  Treas. Reg. §1.183-2(b) and the §183(d) presumption. Returns a
  confidence band, expected IRS posture, and disclosure
  recommendation. Use when the user asks "is this a hobby or a
  business", "Schedule C losses three of five years", "we have an
  audit notice questioning the activity's profit motive", "horse-
  breeding / boat-charter / writer / artist / day-trader profit
  motive", or "§183 nine factors". Make sure to use this skill
  whenever the user mentions hobby loss, profit motive, §183,
  Schedule C losses, or "not a real business".
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-hobby-loss — §183 profit-motive prediction

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/factors-9.md` — Treas. Reg. §1.183-2(b) nine factors
   with case-law touchstones

## Workflow

### 1. Intake

- `activity`: e.g., horse breeding, boat charter, photography, art
- `years_with_loss / years_with_gain`: for §183(d) presumption
- `gross_receipts_history`: trend
- `taxpayer_other_income`: large other income lowers profit-motive
  weight
- `business_records_quality`: books, separate bank account
- `expert_consultation`: did the taxpayer consult professionals
- `taxpayer_time_devoted`: hours per week
- `prior_business_history`: similar successful ventures
- `personal_pleasure_factors`: recreational / aesthetic enjoyment
- `appreciation_expectation`: assets that may appreciate (horses,
  art) can shift weight

### 2. §183(d) presumption

If the activity has gross income exceeding deductions in 3 of the
last 5 consecutive years (2 of 7 for horse activities under
§183(d)), §183 presumption shifts the burden to the IRS. If the
presumption applies, the band can reach HIGH; otherwise the
analysis is fact-driven.

### 3. Nine-factor analysis

Apply Treas. Reg. §1.183-2(b)(1)–(9):
1. Manner in which activity is carried on (businesslike).
2. Expertise of the taxpayer or advisors.
3. Time and effort expended.
4. Expectation that assets used in the activity may appreciate.
5. Success in similar or dissimilar activities.
6. History of income or losses with respect to the activity.
7. Amount of occasional profits.
8. Financial status of taxpayer.
9. Elements of personal pleasure or recreation.

No single factor controls; courts weigh totality of circumstances.

### 4. Conclusion

- HIGH "for-profit": presumption met OR strong factor majority
  with documented business records.
- MODERATE: factor analysis tilts for-profit but contrary
  authority exists.
- LOW: factor analysis tilts hobby; recommend Form 5213 election
  to defer §183 determination if available.
- SPECULATIVE: recreational activity + losses + no records.

### 5. JSON sidecar

Validates against `shared/output-schema.json`. Populate
`authorities[]` with §183, Treas. Reg. §1.183-2, and any cited
cases.

## Hard rules

- Never use a "rule of thumb" (e.g., "3 of 5 always wins") without
  applying the §183(d) presumption check.
- Never claim Chevron deference for Treas. Reg. §1.183-2.
- Drop one band when relying on a single Tax Court Memorandum
  opinion as the closest authority.
- For activities involving substantial personal pleasure (horse
  breeding, boat charter, vineyards), document factor 9 carefully.

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. Note negative-treatment-review residual
responsibility for high-stakes positions (large multi-year losses,
recently audited).
