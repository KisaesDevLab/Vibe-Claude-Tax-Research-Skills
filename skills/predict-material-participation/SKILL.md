---
name: predict-material-participation
description: |
  Predicts whether a taxpayer materially participates in a §469
  activity under one of the seven Treas. Reg. §1.469-5T(a) tests,
  treating the activity as nonpassive so that losses are not subject
  to the §469 passive-activity loss limitation. Applies to all §469
  activities — operating businesses owned through pass-throughs,
  short-term rentals, and (when paired with predict-real-estate-pro)
  rental real estate. Use when the user asks "do I materially
  participate", "the seven tests", "100-hour test", "500-hour test",
  "significant participation", "5-of-10 historical test", "facts and
  circumstances test", "passive vs nonpassive", or "limited partner
  material participation". Make sure to use this skill whenever the
  user mentions material participation, §1.469-5T, or the seven
  tests.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-material-participation — §1.469-5T seven-test analysis

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/seven-tests.md` — Treas. Reg. §1.469-5T(a) tests with
   case-law and audit-defense documentation expectations.

## Operative authority

- IRC §469(h) — material-participation definition: "regular,
  continuous, and substantial".
- Treas. Reg. §1.469-5T(a)(1)–(7) — seven safe-harbor tests.
- Treas. Reg. §1.469-5(f) — substantiation by "any reasonable
  means".
- Treas. Reg. §1.469-5T(e) — limited-partner participation rules
  (only tests 1, 5, 6 available unless general partner).
- Garnett v. Commissioner, 132 T.C. 368 (2009) — LLC member
  treated as general partner for §469 material-participation.
- Thompson v. United States, 87 Fed. Cl. 728 (2009) — same.

## Workflow

### 1. Intake

- `activity_type`: pass-through operating business, STR, single-
  member LLC operating activity, partnership/LLC interest, etc.
- `tax_year`
- `taxpayer_role`: GP, LP, LLC member-manager, LLC non-managing
  member, S-corp shareholder
- `taxpayer_hours_in_activity`: contemporaneous log if available
- `other_individuals_hours`: other significant participants
- `historical_participation_years`: prior years materially
  participated
- `personal_service_activity`: medical, legal, accounting,
  consulting, performing arts, etc. (relevant to test 6)

### 2. Limited-partner gatekeeping

If the taxpayer holds a limited-partner interest, ONLY tests 1, 5,
and 6 are available (§1.469-5T(e)(2)). LLC member-managers and
non-managers have been treated as general partners under Garnett /
Thompson / Newell v. Commissioner, T.C. Memo. 2010-23, but the IRS
has not formally conceded outside the litigation context. Cap the
band when relying on this LLC-as-GP position; consider the
practical implications for a multi-member LLC where one member is
the manager.

### 3. Seven-test cascade

Walk in this order — first satisfied test wins.

1. **Test 1 — > 500 hours**: simplest, hardest factual bar.
2. **Test 2 — substantially all participation by taxpayer**: works
   for sole-proprietor-like setups with no other workers.
3. **Test 3 — > 100 hours AND ≥ any other individual's
   participation**: useful for solo-managed activities even if
   total is modest.
4. **Test 4 — significant participation activity (SPA)**: > 100
   hours in this activity, and aggregate of all SPAs > 500 hours.
   Requires aggregating multiple distinct activities; document the
   list.
5. **Test 5 — 5 of last 10 years**: useful for established
   operators currently scaling back hours.
6. **Test 6 — personal-service activity, 3 prior years**:
   medicine, law, accounting, etc.; once a material participant
   in any 3 prior years, locked in.
7. **Test 7 — facts and circumstances**: > 100 hours and
   "regular, continuous, and substantial" participation. Excluded
   when investor-type activities (per §1.469-5T(b)(2)(ii)).

### 4. Documentation

§1.469-5(f): participation may be established by "any reasonable
means" — but Tax Court demands contemporaneous logs in practice
(Bailey, Hakkak, Pohoski). Reconstructed estimates are routinely
disallowed. Recommend:

- Daily log entries with date, hours, and activity description.
- Calendar / appointment records cross-referenced to log entries.
- Communications (emails, texts, vendor calls) date-stamped.
- For test 3, vendor / property-manager hour estimates to satisfy
  the "≥ any other individual" prong.

### 5. Conclusion

Confidence band per `shared/confidence-bands.md`:

- HIGH: contemporaneous log + clearly satisfies test 1 OR
  unambiguously satisfies test 5/6.
- MODERATE: log present but tests 3, 4, or 7 are factually close.
- LOW: log reconstructed; tests 4 or 7 require fact-pattern
  judgment; LLC-as-GP position relied upon.
- SPECULATIVE: no log; only investor activities.

Recommend Form 8275 disclosure when band is LOW (reasonable-basis
path on a §469 nonpassive position).

### 6. Authorities + sidecar

Cite §469(h), Treas. Reg. §1.469-5T(a)(1)–(7), §1.469-5(f), and
relevant case law. JSON sidecar validates against
`shared/output-schema.json`.

## Hard rules

- Never assert material participation without identifying which
  test is satisfied and the supporting fact pattern.
- Never assert test 7 facts-and-circumstances satisfaction for an
  activity that meets the §1.469-5T(b)(2)(ii) investor-activity
  exclusion.
- Drop one band when the log is reconstructive.
- Drop one band when relying on Garnett / Thompson / Newell to
  treat an LLC interest as general-partner-equivalent.
- Never claim Chevron deference for Treas. Reg. §1.469-5T.

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. For high-stakes positions (multi-year
nonpassive treatment, large suspended losses), include the
negative-treatment-review residual practitioner responsibility.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
