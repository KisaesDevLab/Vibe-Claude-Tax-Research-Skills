# Strategy library — canonical list

The Vibe CPA Skills `planning-strategy-library` skill catalogs 30
core CPA-vetted strategies. Each strategy lives at
`skills/planning-strategy-library/references/strategies/<slug>.md`.

In addition to the curated 30, the directory contains an extended
**addendum library** of 87 reference strategies (#8–#94 from a
practitioner-source addendum; #1–#7 were not delivered). The
extended library lives in the same directory but is governed by
the cross-reference matrix at
`skills/planning-strategy-library/references/strategy-cross-reference.md`
(human-readable) and `strategy-relationships.json` (machine-
readable). The extended files are intended as deeper reference
material related to the curated 30; the curated 30 remain the
short-form planning catalog. Where the addendum's slug collided
with a curated slug, the addendum file is suffixed with
`-extended.md` (`cost-segregation-extended.md`,
`real-estate-professional-extended.md`,
`section-1202-qsbs-extended.md`, `backdoor-roth-extended.md`).

Strategies are organized by domain. Each entry below shows:
- Slug (filename without `.md`).
- Strategy name.
- Primary IRC section.
- Brief description.
- State interplay flag (✓ = state-specific eligibility).
- Recent-legislation flag (✓ = post-2024 legislation may have
  modified — see `shared/legislation-tracking.md`).

## Individual / 1040 strategies (10)

| # | Slug | Strategy | IRC § | State | Recent legis. |
|---|---|---|---|---|---|
| 1 | backdoor-roth | Backdoor Roth IRA | §408A | | |
| 2 | mega-backdoor-roth | Mega backdoor Roth (after-tax 401(k)) | §401(k) | | ✓ (SECURE 2.0) |
| 3 | tax-loss-harvesting | Tax-loss harvesting | §1091 | | |
| 4 | charitable-bunching-daf | Charitable bunching with DAF | §170 | | |
| 5 | qcd-from-ira | Qualified Charitable Distribution | §408(d)(8) | | |
| 6 | solo-401k | Solo 401(k) for self-employed | §401(k) | | |
| 7 | cash-balance-plan | Cash-balance defined-benefit plan | §412, §401(a) | | |
| 8 | hsa-as-retirement | HSA as long-term retirement vehicle | §223 | | |
| 9 | roth-conversion-ladder | Roth conversion ladder | §408A | | ✓ (TCJA sunset) |
| 10 | state-residency-shift | State-residency planning | (state) | ✓ | |

## Entity strategies (10)

| # | Slug | Strategy | IRC § | State | Recent legis. |
|---|---|---|---|---|---|
| 11 | ptet-election | Pass-Through Entity Tax election | §164; Notice 2020-75 | ✓ | |
| 12 | s-corp-reasonable-comp | S-corp reasonable-comp optimization | §162, §1366 | | |
| 13 | accountable-plan | Accountable-plan reimbursement | §62(c) | | |
| 14 | cost-segregation | Cost-segregation + bonus depreciation | §168(k), §179 | | ✓ (§168(k) phase-down) |
| 15 | section-179-expensing | §179 expensing | §179 | | |
| 16 | section-1202-qsbs | §1202 QSBS exclusion | §1202 | ✓ (CA/PA non-conformity) | ✓ (OBBBA) |
| 17 | section-1045-rollover | §1045 QSBS rollover | §1045 | | |
| 18 | section-163j-rptb-election | §163(j) real-property-trade-or-business election | §163(j)(7)(B) | | |
| 19 | opportunity-zones | Qualified Opportunity Zones | §1400Z-2 | | ✓ (TCJA / OBBBA) |
| 20 | r-and-d-280c-election | §41 R&D credit + §280C(c) reduced credit | §41, §280C | | ✓ (§174 OBBBA) |

## Real-estate / specialized (5)

| # | Slug | Strategy | IRC § | State | Recent legis. |
|---|---|---|---|---|---|
| 21 | like-kind-exchange-1031 | §1031 like-kind exchange | §1031 | ✓ (CA Form 3840) | |
| 22 | real-estate-professional | Real-estate professional (REPS) | §469(c)(7) | ✓ (state PAL) | |
| 23 | str-loophole | Short-term-rental "loophole" | Treas. Reg. §1.469-1T(e)(3)(ii) | | |
| 24 | installment-sale-453 | §453 installment sale | §453 | | |
| 25 | self-directed-ira-re | Self-directed IRA real estate | §408, §4975 | | |

## Estate / gift (5)

| # | Slug | Strategy | IRC § | State | Recent legis. |
|---|---|---|---|---|---|
| 26 | annual-exclusion-gifting | §2503(b) annual exclusion gifting | §2503(b) | | |
| 27 | spousal-portability-dsue | DSUE / spousal portability | §2010(c)(4) | | ✓ (TCJA sunset) |
| 28 | grat-zeroed-out | "Zeroed-out" GRAT | §2702 | | |
| 29 | ilit | Irrevocable Life Insurance Trust | §2042, §2702 | | |
| 30 | charitable-remainder-trust | Charitable Remainder Trust (CRT/CRAT/CRUT) | §664 | | |

## Excluded strategies (Dirty-Dozen / Listed Transactions)

The following strategies are **NOT** included in the library
because they are flagged by the IRS as Dirty-Dozen / Listed /
Reportable Transactions or carry severe practitioner-liability
risk. Practitioners considering these strategies should first
route to `predict-economic-substance` and `compliance-ssts-
circular230` before any client engagement.

- §831(b) micro-captive insurance (Notice 2016-66).
- Syndicated conservation easements (Notice 2017-10).
- Monetized installment sales.
- Charitable LLC structures.
- Pre-packaged "tax shelters" of any kind.
- Promoter-marketed structures lacking economic substance.

## Extended addendum library (#8–#94)

The 87 addendum strategies share the same `references/strategies/`
directory and follow a similar entry shape (YAML frontmatter,
overview, primary IRC authority, regulations, IRS guidance, court
decisions, eligibility, mechanics, documentation, pitfalls, recent
legislation flags, state conformity, default confidence band,
cross-references, JSON authorities). They are listed in full at
`skills/planning-strategy-library/references/strategy-cross-reference.md`
(matrix and combinations / conflicts / mutually-exclusive paths).
Strategies #1–#7 from the addendum's Part 1 source were not
delivered; the matrix retains those rows for navigability with a
note that no detail file exists.

## Standalone strategy files (added with the addendum)

Two practitioner-targeted reimbursement strategies that do not
duplicate any curated entry:

- `corp-vehicle-personal-name.md` — Accountable-plan reimbursement
  for a vehicle titled in the owner-employee's personal name (PLR
  200930029; Reg. §1.179-1(a)(e); §67(g) suspension forecloses
  Form 2106 alternative).
- `s-corp-home-office-reimbursement.md` — The "only method that
  works" post-TCJA: §62(a)(2)(A) accountable-plan reimbursement
  (Treas. Reg. §1.62-2; §280A(c)(1); *Hamacher* convenience-of-
  employer test). Why renting the home to the corporation fails
  (§280A(c)(6); PMTA 00431_7138). Why Form 2106 fails (§67(g)).

## Companion catalog skills

Two new top-level skills index the strategies by Form line:

- `s-corp-strategy-catalog` — 10 S-corp strategies mapped to
  Form 1120-S lines.
- `schedule-c-strategy-catalog` — 10 Schedule C / SE strategies
  mapped to Schedule C / Form 8829 lines.

A third companion skill, `tax-elections-library`, indexes 24
commonly-needed tax elections with authority, deadline, where-to-
file, mechanics, and sample election language.

## Maintenance

This file is the canonical strategy index. The
`planning-strategy-library` SKILL.md and `references/index.md`
should reference each strategy slug exactly as listed above.

Adding a new strategy:
1. Add a row to this table with a new slug.
2. Create
   `skills/planning-strategy-library/references/strategies/<slug>.md`
   with the standard structure (see `index.md`).
3. Cross-reference in `index.md`.
4. Add an eval case if appropriate.
