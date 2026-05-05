---
name: tax-research-state-income
description: |
  State income-tax research skill covering individual / fiduciary
  / passthrough / corporate income tax for all 51 jurisdictions
  (50 states + DC). Implements a state-router protocol: when the
  user mentions a state by name, abbreviation, or distinctive
  feature ("FTB", "convenience-of-employer rule", "Mass. surtax",
  "WA cap gains", "TX margin"), the skill loads the corresponding
  references/states/<XX>.md before drafting analysis. Use when the
  user asks "state income tax", "state residency", "PTET",
  "state tax for [state]", "FTB", "convenience-of-employer rule",
  "TN Hall tax", "WA capital-gains tax", or "MA millionaire
  surtax". Make sure to use this skill whenever the user mentions
  state income tax, state residency, PTET, or any state DOR by
  name.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# tax-research-state-income — State income-tax research

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/state-template.md` — promotion ladder (stub → draft →
   reviewed → verified) and state-file structure.
6. `shared/legislation-tracking.md` — for federal-conformity
   questions affected by recent Public Laws.
7. `references/router-protocol.md` — state-detection and routing
   procedure.
8. The relevant `references/states/<XX>.md` per the user's
   jurisdiction (see Supported jurisdictions below).

## Supported jurisdictions

All 50 states + DC. State codes (ISO/USPS):

```
AL  AK  AZ  AR  CA  CO  CT  DE  DC  FL
GA  HI  ID  IL  IN  IA  KS  KY  LA  ME
MD  MA  MI  MN  MS  MO  MT  NE  NV  NH
NJ  NM  NY  NC  ND  OH  OK  OR  PA  RI
SC  SD  TN  TX  UT  VT  VA  WA  WV  WI
WY
```

Per `shared/sources.json`:
- **No individual income tax**: AK, FL, NV, SD, TN (Hall repealed),
  TX, WA (capital-gains-only since 2022), WY.
- **NH** repealed I&D tax in 2025; verify per-state file.

## State-router protocol

When the user mentions a state — by full name, USPS code,
distinctive feature, or DOR brand — the skill MUST:

1. Identify the jurisdiction code.
2. Load `references/states/<XX>.md`.
3. Read the file's `status` field:
   - `stub`: per-state file is intentionally placeholder. Use the
     primary agency URL for live retrieval; cap state confidence
     at LOW per `shared/confidence-bands.md` decay rule.
   - `draft`: practitioner has begun edits; cap at MODERATE.
   - `reviewed`: peer-reviewed; cap at HIGH if facts well-aligned.
   - `verified`: verified live citation walk; HIGH band available.
4. Note `state_code` and `status` in the JSON sidecar's
   `state_files_consulted[]` array.

State-detection trigger phrases (non-exhaustive):

| Trigger | Code |
|---|---|
| "California", "CA", "FTB", "AB5", "Dynamex", "Prop 22", "$800 LLC fee" | CA |
| "New York", "NY", "convenience-of-employer rule", "TSB-A", "Article 9-A" | NY |
| "Texas", "TX", "Comptroller", "margin tax" | TX |
| "Florida", "FL" | FL |
| "Massachusetts", "MA", "millionaire surtax" | MA |
| "Washington", "WA", "B&O tax", "WA cap gains" | WA |
| "Pennsylvania", "PA" | PA |
| "Illinois", "IL" | IL |
| "New Jersey", "NJ", "BAIT" | NJ |
| "Tennessee", "TN", "Hall tax", "F&E" | TN |
| ... (full table in references/router-protocol.md) | ... |

## Workflow

### 1. Intake

- `taxpayer_state_residence`: home state.
- `taxpayer_secondary_states`: states where income is sourced or
  property held.
- `tax_year`.
- `issue`: free text.
- `entity_type` for passthrough / corporate questions.
- `prior_year_returns`: filing history, residency claims,
  apportionment.

### 2. State-detection and routing

Run trigger detection. For each state implicated, load the
corresponding `references/states/<XX>.md`. If multiple states are
implicated, load each.

### 3. Conformity analysis

Three primary conformity types:
- **Rolling conformity**: state automatically adopts current IRC.
  States: NY, IL, NJ, MA (varies by section), CA (rolling for
  some / static for others).
- **Static conformity**: state adopts IRC as of a specific date.
  States: VA (12/31/2023 typically), AZ, FL (corp), MN, NH, etc.
- **Selective conformity**: state picks-and-chooses.

Confirm the state's conformity posture per the per-state file
before applying federal authority to a state question.

### 4. Apportionment / sourcing

For multi-state taxpayers:
- Single-sales-factor vs. three-factor (sales / property /
  payroll).
- Market-based sourcing vs. cost-of-performance.
- Throwback / throwout rules.
- §965 / GILTI / FDII state inclusion variations.

Per-state file documents the apportionment formula.

### 5. PTET (Pass-Through Entity Tax)

For pass-through clients in PTET-enacting states:
- Election deadline (varies by state; some require pre-payment
  early in the year).
- Election form (e.g., CA Form 3804, NY ETP, NJ BAIT).
- Computation rules and credit at owner level.
- Notice 2020-75 federal deductibility framework.

### 6. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`.
Required: `state_files_consulted[]` array with `state_code`,
`skill: tax-research-state-income`, `status`, `last_reviewed`.

Confidence band per `shared/confidence-bands.md` with state-stub
decay rule:
- HIGH only if state file is `verified` AND facts unambiguous.
- MODERATE if state file is `reviewed`.
- LOW (cap) if state file is `stub` (most states are stubs at
  v1.0.0-beta).

### 7. Tax Foundation / Tax Policy Center

Tax Foundation Center for State Tax Policy is a useful secondary
SOURCE for state conformity and rate tables but is
`persuasive_non_authority` only. MUST NOT serve as the closest
cite for any conclusion.

URL: https://taxfoundation.org/center/state-tax-policy/

Tax Policy Center (Urban-Brookings) is similarly tagged.

URL: https://www.taxpolicycenter.org

These secondary sources may be cited in practitioner notes for
context only.

## Hard rules

- ALWAYS load the relevant `references/states/<XX>.md` BEFORE
  drafting analysis when any state is implicated.
- ALWAYS cap state confidence at LOW when state file is
  `status: stub`.
- NEVER let Tax Foundation or Tax Policy Center drive a
  confidence band; they are `persuasive_non_authority` at most.
- NEVER cite a state DOR publication as the closest authority
  for a contested position; cap at "describes administrative
  practice".
- ALWAYS verify state conformity posture (rolling / static /
  selective) before applying federal authority.
- ALWAYS include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Add the state-stub residual
practitioner responsibility: "When the per-state file's status is
`stub`, the practitioner must independently verify cited
authority against current state statute, regulation, and DOR
guidance before relying on the conclusion."

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
