---
name: return-summary-entity
description: |
  Produces a structured readout of an entity tax return — Form 1120
  (C-corp), Form 1120-S (S-corp), or Form 1065 (partnership) — with
  computed effective and marginal rates, balance-sheet sanity
  checks, K-1 distribution traces, and red flags routed to other
  skills. Companion to return-summary-1040 for entity-level work;
  does NOT produce tax-position advice. Use when the user asks
  "summarize this 1120 / 1120-S / 1065", "entity return summary",
  "K-1 trace", "1120 review", or "what's on this entity return".
  Make sure to use this skill whenever the user mentions Form 1120,
  Form 1120-S, Form 1065, K-1 trace, or entity return summary.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# return-summary-entity — 1120 / 1120-S / 1065 summary

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/line-keys-1120.md` — Form 1120 line numbers and
   schedules.
6. `references/line-keys-1120s.md` — Form 1120-S, K-1 (1120-S)
   line numbers.
7. `references/line-keys-1065.md` — Form 1065, K-1 (1065) line
   numbers.
8. `references/red-flags-entity.md` — entity-specific pattern
   catalog.

## Workflow

### 1. Intake

Accept any of:
- Full Form 1120 / 1120-S / 1065 PDF (text-extractable) or pasted
  text.
- A list of line-item amounts.
- A summary table with at least the core figures (gross income,
  taxable income, total tax, distributions / K-1 totals).

### 2. Form-type identification

Distinguish:
- 1120 (C-corp): standalone tax computation.
- 1120-S (S-corp): pass-through; ordinary income/loss flows through
  K-1 to shareholders.
- 1065 (partnership / multi-member LLC default): pass-through; K-1
  to partners.

### 3. Core figures by form

#### Form 1120 (C-corp)

- Gross receipts (Line 1a–c).
- Total income (Line 11).
- Total deductions (Line 27).
- Taxable income (Line 30).
- Total tax (Line 31).
- Tax payments / credits (Line 33–34).
- Refund or balance due (Line 36 / 37).

Schedule J: tax computation; alternative minimum tax (post-IRA
2022 §55 corporate AMT for applicable corporations).

Schedule M-1 / M-3: book-tax reconciliation. M-3 required for
corporations with assets ≥ $10M.

Schedule L: balance sheet at beginning and end of year.

Schedule G: information on persons owning ≥ 25% of stock.

Form 1125-A: cost of goods sold.
Form 1125-E: compensation of officers (required if receipts ≥ $500K).

#### Form 1120-S (S-corp)

- Gross receipts (Line 1a).
- Ordinary business income (Line 21).
- Total tax (Line 22a; rare — usually only built-in gains tax
  under §1374).
- Schedule K: shareholder pro-rata items.
- Schedule M-2: AAA, OAA, PTI.
- Schedule L: balance sheet.

Schedule K-1 (Form 1120-S): per-shareholder allocation of items.
Boxes:
- 1: ordinary business income.
- 2: net rental real estate income.
- 3: other net rental income.
- 4: interest income.
- 5a/5b: ordinary / qualified dividends.
- 8a/8b/8c: capital gains.
- 16: separately stated items (incl. §179, charity, foreign tax,
  etc.).
- 17: AMT items.

#### Form 1065 (partnership)

- Gross receipts (Line 1a).
- Ordinary business income (Line 22).
- Schedule K: partner pro-rata items.
- Schedule M-1 / M-2 / M-3.
- Schedule L: balance sheet.
- Schedule B: questions including §469 / §704(b) / §754
  declarations.

Schedule K-1 (Form 1065): per-partner allocation.

### 4. Compute derived figures

#### C-corp (1120)

- Effective tax rate = Total tax (Line 31) / Total income (Line
  11).
- Marginal tax rate = 21% federal (post-TCJA flat) — verify
  current-year posture.
- Book-tax difference per Schedule M-1 / M-3.
- §163(j) limitation analysis if applicable (excess interest
  expense).
- §382 NOL limitation if ownership-change events.

#### S-corp (1120-S)

- Per-shareholder ordinary-income allocation × shares = K-1 Box 1.
- AAA / OAA / PTI ending balances (Schedule M-2).
- Distributions in excess of stock basis: capital gain to
  shareholder under §1368(b).
- Built-in gains tax exposure (§1374): for converted C-corps in
  recognition period.
- Reasonable-comp ratio (W-2 wages / distributions) — flag if
  W-2 < 30% of distributions for owner-employee.

#### Partnership (1065)

- Per-partner ordinary-income allocation × interest = K-1 Box 1.
- Capital-account analysis (Schedule K-1 Part II).
- §704(c) built-in-gain/loss tracking.
- §752 liability allocation (recourse vs nonrecourse).
- §163(j) at partnership level.
- §163(j) excess-business-interest-expense (EBIE) tracking.
- BBA partnership-audit regime under §6221.

### 5. Schedule L balance-sheet sanity checks

- Beginning and ending equity reconcile to M-2 capital-account
  changes (1065) or AAA + retained-earnings + capital-stock
  (1120-S) or retained-earnings (1120).
- Asset / liability totals match prior-year ending.
- Material book-tax differences flagged.

### 6. Red-flag catalog

Run input through `references/red-flags-entity.md`. Common patterns:

#### C-corp (1120)
- Compensation of officers very high relative to receipts (route
  to `predict-reasonable-comp`).
- Constructive dividends (excessive shareholder loans without
  documentation).
- §382 ownership-change events.
- §163(j) interest deduction shortfall.
- §59A BEAT exposure for large multinationals.

#### S-corp (1120-S)
- Shareholder W-2 too low relative to distributions (Watson
  pattern → route to `predict-reasonable-comp`).
- Distributions in excess of stock basis (capital gain).
- Built-in gains tax exposure (§1374 recognition period).
- Two classes of stock concerns (proportionate distribution
  failures).
- Late S-election or invalid S-election (route to
  `tax-research-entity`).

#### Partnership (1065)
- §704(b) substantial-economic-effect test issues.
- §704(c) tracking gaps.
- §752 liability mis-allocation between recourse and nonrecourse.
- §754 election not made when basis differential exists.
- BBA opt-out election eligibility.

### 7. Conclusion

Single paragraph: form type, fiscal year, gross income, taxable
income, total tax (or pass-through allocation), top 3 red flags,
top 3 routing recommendations. NO tax-position advice.

### 8. JSON sidecar

Validates against `shared/output-schema.json`. Required: skill,
version, generated_at, task, conclusion, confidence_band,
authorities (Form / Instructions / IRC sections cited),
verification_checklist.

`confidence_band` reflects extraction accuracy (HIGH if full PDF;
MODERATE if typed; LOW if estimated). NOT tax-position confidence.

## Hard rules

- Summarize; do NOT advise. Tax-position advice is the job of
  `tax-research-entity` or planning skills.
- Never fabricate line-item values. If user did not provide and it
  cannot be derived, mark "not provided".
- Treat input as confidential client data; redact entity name /
  EIN / tax-id / SSN with `[REDACTED]`.
- Never assert 21% federal corporate rate without verifying year-
  appropriate Rev. Proc. or §11 amendment status (post-TCJA flat;
  IRA / OBBBA modifications to be verified).
- For state piggyback summaries, route to `tax-research-state-income`.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. SSTS §2.3 use-of-estimates is most
relevant when extracting from incomplete inputs.
