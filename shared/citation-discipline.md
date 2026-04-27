# Citation discipline

## Hard rule
Never fabricate a citation. If you cannot ground a proposition in a
primary source you have actually retrieved (or that has been provided
to you), you must:
1. Emit the sentinel `[CITATION NEEDED — search: <specific query>]`
   inline at the point of the proposition.
2. Add an entry to the JSON sidecar's `unresolved_citations` array.
3. Lower the confidence band by at least one step (see
   confidence-bands.md).

A "primary source" is the IRC section, the Treasury Regulation, the
court opinion, the Revenue Ruling/Procedure/Notice, the PLR/TAM, the
Form/Instructions, the state DOR pronouncement, or a comparable
authoritative document — accessed at its canonical URL listed in
live-sources.md.

## Stub vs. published files
State stub files at `references/states/<XX>.md` use `TODO:` markers
(NOT `[CITATION NEEDED]`) because their content is intentionally
placeholder pending practitioner edits. The CI grep for fabricated
citations excludes `references/states/`. When a state stub is
promoted to `status: reviewed` or `verified`, all `TODO:` markers
must be resolved or replaced with `[CITATION NEEDED]` sentinels for
items still requiring research.

## Required fields per citation
Every citation in the `authorities` array of the JSON sidecar MUST
include:
- `authority_type`: one of (extended in v1.1):
  - **Primary federal**: `IRC`, `TreasReg`, `TreasuryDecision`,
    `StatutesAtLarge`
  - **IRS published guidance (IRB)**: `RevRul`, `RevProc`, `Notice`,
    `Announcement`
  - **IRS written determinations**: `PLR`, `TAM`, `CCA`, `GCM`, `AOD`,
    `FSA`, `OfficeMemo`, `InfoLetter`
  - **IRS practice/published**: `IRSPub`, `IRM`, `ATG`, `ISPPaper`,
    `IRSNewsRelease`
  - **Legislative**: `JCT_BlueBook`, `LegHistory`, `Greenbook`,
    `CBOReport`
  - **Federal courts**: `SCOTUS`, `CtAppeals`, `TaxCt`, `DistCt`,
    `CtFedClaims`
  - **State**: `StateStatute`, `StateReg`, `StateAdmin`, `StateCt`
  - **Treaty**: `Treaty`
  - **Forms**: `Form`, `Instructions`
- `citation`: human-readable cite (e.g., "I.R.C. § 199A(a)(1)" or
  "Treas. Reg. § 1.199A-1(b)(14)" or "Watson v. United States, 668
  F.3d 1008 (8th Cir. 2012)")
- `url`: canonical URL from live-sources.md
- `retrieved_date`: ISO 8601 (YYYY-MM-DD)
- `quoted_text`: ≤ 75 words verbatim excerpt that supports the cited
  proposition. Paraphrase is not acceptable for this field.
- `pin_cite`: optional — paragraph, line, or footnote pointer
- `weight`: see authority-hierarchy.md (`primary_statute`,
  `binding_judicial`, `regulation`, `binding_circuit`, `judicial`,
  `irs_published`, `legislative_history`, `written_determinations`,
  `persuasive_non_authority`, `not_authority`)

## Authority-type-to-weight default mapping (v1.1)

| authority_type | default weight |
|---|---|
| `IRC`, `StatutesAtLarge`, `Treaty` | `primary_statute` |
| `SCOTUS` | `binding_judicial` |
| `TreasReg`, `TreasuryDecision` | `regulation` |
| `CtAppeals` | `binding_circuit` (in taxpayer's circuit) or `judicial` (other circuits) |
| `TaxCt`, `DistCt`, `CtFedClaims` | `judicial` |
| `RevRul`, `RevProc`, `Notice`, `Announcement` | `irs_published` |
| `JCT_BlueBook`, `LegHistory`, `Greenbook`, `CBOReport` | `legislative_history` |
| `PLR`, `TAM`, `CCA`, `GCM`, `AOD`, `FSA`, `OfficeMemo`, `InfoLetter` | `written_determinations` |
| `IRSPub`, `IRM`, `ATG`, `ISPPaper`, `IRSNewsRelease`, `Form`, `Instructions` | `persuasive_non_authority` |
| `StateStatute` | `primary_statute` (state-tier) |
| `StateReg` | `regulation` (state-tier) |
| `StateCt` | `judicial` (state-tier) |
| `StateAdmin` | `persuasive_non_authority` to `judicial` depending on body |

The mapping is a default. Skills may override with rationale recorded
in the citation entry's `weight_override_rationale` field.

## Sentinel format
Use exactly: `[CITATION NEEDED — search: <query>]`
Examples:
- `[CITATION NEEDED — search: §199A QBI deduction wage limitation 2024]`
- `[CITATION NEEDED — search: Watson reasonable comp 8th Circuit]`

## Graceful degradation ladder
When a primary source is unreachable mid-task, descend in order:
1. Same authority via mirror URL (e.g., Cornell LII for eCFR).
2. A higher authority that subsumes the proposition (Code section
   that directly states the rule).
3. A clearly-labeled IRS Publication or IRM citation, marked
   `weight: persuasive_non_authority`, with explicit caveat in the
   conclusion.
4. Sentinel + `unresolved_citations` entry + lowered confidence band.
Never silently substitute a treatise, blog, or AI summary.

## Out-of-date detection
If `retrieved_date` is older than 365 days for a proposition tied to
a regulation that may have been amended, emit a `staleness_warning`
in the sidecar with the recommended re-verification date.

## Loper Bright caveat (post-Chevron)
Treasury Regulations no longer command Chevron deference. When
relying on a Treasury Regulation's interpretation of an ambiguous
statute, flag `chevron_replaced: true` and note that a court would
review the regulation under Skidmore (Loper Bright Enterprises v.
Raimondo, 144 S. Ct. 2244 (2024)).

## Negative-treatment-detection limitation (v1.1)

The pack relies on free primary sources only. There is **no free
equivalent** of a commercial citator (KeyCite, Shepards, BCite,
Citator 2nd) capable of detecting implicit overrules with
comprehensive coverage.

Mitigations the skills implement:
- Authority-weight rules drop one band when retrieved_date > 365 days
  in fast-moving areas (state SALT/PTET, R&D §174 capitalization,
  OZ rules) — see confidence-bands.md.
- DAWSON Today's Opinions / Today's Orders feeds are consulted for
  freshness signals on Tax Court authorities.
- The Federal Register IRS feed is consulted for new TDs and proposed
  regs that may supersede current guidance.

Mitigations the skills do NOT implement (residual practitioner
responsibility):
- Comprehensive negative-treatment review of cited cases.
- Detection of implicit overrules outside the freshness window.

Every output's verification checklist appendix must explicitly call
out this residual practitioner responsibility.

## Current-awareness sources are NOT authority

TaxProf Blog, Procedurally Taxing, Tax Appellate Blog, Tax Foundation,
Tax Policy Center, and similar sources are listed in live-sources.md
as current-awareness signals. They are tagged `weight: not_authority`
or at most `persuasive_non_authority`. They MUST NOT drive a
confidence band assignment, and they MUST NOT appear as the closest
authority for any cited proposition.
