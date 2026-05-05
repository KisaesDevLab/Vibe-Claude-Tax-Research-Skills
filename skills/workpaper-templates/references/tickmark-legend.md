# Tickmark legend

Tickmarks are workpaper shorthand for the procedure performed.
Each tickmark used must appear on a tickmark legend included in
the workpaper file (typically on every workpaper, or referenced
to a master legend in the current file). A tickmark without a
legend on or referenced from the workpaper is a documentation
deficiency under AU-C §230.08 / AR-C §60.A26.

## Conventions

- Use a single legend per engagement. Mixing tickmarks across
  engagements creates ambiguity.
- Tickmarks are colored per firm convention (commonly red ink in
  paper files; specific font color in electronic files like
  ProSystem fx Engagement, Caseware).
- A tickmark identifies WHAT was done, not the result. The
  conclusion is stated separately.
- The tickmark scheme should be capable of expressing both
  procedure-performed and any exception found.

## Standard tickmark legend (audit / review baseline)

| Mark | Meaning | Example use |
|---|---|---|
| `✓` (or "TB") | Agreed to trial balance | AR aging total `✓` to TB AR account 1200. |
| `CF` | Cross-foot (column total verified) | Aging columns added vertically — `CF`. |
| `F` | Foot (column total verified — synonym; use one consistently) | — |
| `XF` | Cross-cast (rows added laterally) | — |
| `R` | Recalculated | Depreciation expense `R` per useful-life and method. |
| `E` | Examined supporting document | Invoice `E` for $42,000 capex addition. |
| `C` | Confirmed (positive confirmation reply received) | AR balance `C` per customer reply. |
| `Cn` | Confirmed (negative confirmation — no reply, deemed agreed under AU-C §505.15) | — |
| `BS` | Traced to bank statement | Cash balance `BS` per Wells Fargo 12/31 statement. |
| `SP` | Traced to subsequent payment | AP balance `SP` per 1/15 disbursement. |
| `SR` | Traced to subsequent receipt / collection | AR balance `SR` per 1/22 customer payment. |
| `I` | Examined invoice | — |
| `CO` | Examined contract | Lease term `CO` per signed lease 4/1/2024. |
| `MIN` | Examined minutes | Dividend declaration `MIN` per 12/15 board meeting. |
| `V` | Verbal inquiry — name and date documented separately | "Tested via inquiry of CFO Jane Doe 11/15 — `V`." |
| `O` | Observed | Inventory count `O` 12/30 at warehouse 1. |
| `RP` | Reperformed | Bank rec `RP` from underlying detail. |
| `A` | Analytical procedure applied (AR-C §90 review only) | — |
| `NE` | No exception noted | Test of details `NE`. |
| `EX` | Exception noted — see exception memo at WP [ref] | `EX` — see WP A-3.1 exception memo. |
| `N/A` | Not applicable | — |
| `NT` | Not tested (with rationale) | Population < $X; immaterial. `NT` — see scoping memo. |
| `?` | Open item — to follow up | (Cleared before partner sign-off; replaced with the operative tickmark.) |

## Tickmark sufficiency rule

Per AU-C §230.08 and AR-C §60.A26, a workpaper must enable an
experienced practitioner without prior connection to the engagement
to understand the procedure performed. Tickmarks alone are
insufficient if the legend is unclear or the scope of the procedure
is undocumented. Pair every tickmark with:

- A **scope statement** at the top of the workpaper (e.g., "Tested
  100% of items > $10,000; sampled 25 items below threshold per
  random selection from population of 412.")
- A **conclusion** at the bottom (e.g., "Test results: no
  exceptions noted on selected sample. Population characteristics
  consistent with auditor expectation; population accepted.")
- The **preparer / reviewer / partner** sign-off block (per AU-C
  §220.18 / AR-C §60.31).

## Engagement-quality flags

- "Tested — no exceptions" without scope description is a
  documentation deficiency, not a procedure.
- A workpaper using any tickmark not appearing on the engagement's
  tickmark legend is a documentation deficiency.
- Tickmark inconsistency across the file (e.g., `✓` meaning
  "agreed to TB" on one workpaper and "footed" on another) is a
  documentation deficiency.
- Open `?` tickmarks at file lock-down (60 days post-report-release
  per AU-C §230.16) must be either cleared or memorialized as
  a withdrawal / scope limitation.

## Firm-software notes

- **CCH ProSystem fx Engagement:** tickmarks via the "Tickmark"
  ribbon; legend lives in the current-file root document.
- **Caseware Working Papers:** tickmark library with engagement-
  level legend; supports custom legends.
- **Karbon / spreadsheet-only firms:** maintain a single tickmark-
  legend tab in the master engagement workbook; reference from
  every working paper tab.

The tickmark legend itself receives a current-file index (often
`A-0` or as part of the planning section) and is signed off as
prepared / reviewed.
