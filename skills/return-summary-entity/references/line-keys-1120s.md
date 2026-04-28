# Form 1120-S (S-corporation) line keys

For tax year 2024 — verify against year-specific Form 1120-S
instructions before quoting line numbers.

## Page 1 — Income and deductions

| Line | Item |
|---|---|
| 1a | Gross receipts or sales |
| 1b | Returns and allowances |
| 1c | Net |
| 2 | Cost of goods sold (Form 1125-A) |
| 3 | Gross profit |
| 4 | Net gain/(loss) — Form 4797 |
| 5 | Other income |
| 6 | TOTAL INCOME |
| 7 | Compensation of officers (Form 1125-E if receipts ≥ $500K) |
| 8 | Salaries and wages |
| 9 | Repairs |
| 10 | Bad debts |
| 11 | Rents |
| 12 | Taxes and licenses |
| 13 | Interest |
| 14 | Depreciation |
| 15 | Depletion |
| 16 | Advertising |
| 17 | Pension, profit-sharing |
| 18 | Employee benefits |
| 19 | Other deductions |
| 20 | TOTAL DEDUCTIONS |
| 21 | Ordinary business income (Line 6 − 20) |
| 22a | Excess net passive-investment income tax (§1375) |
| 22b | LIFO recapture tax |
| 22c | §1374 built-in gains tax |
| 23 | Tax payments / credits |
| 24 | Total tax |
| 25 | Refund / balance due |

## Schedule K — Shareholders' Pro Rata Share Items

Aggregated items that flow to K-1s.

| Item | Code on K-1 |
|---|---|
| Ordinary business income (loss) | Box 1 |
| Net rental real estate income | Box 2 |
| Other net rental income (loss) | Box 3 |
| Interest income | Box 4 |
| Ordinary dividends | Box 5a |
| Qualified dividends | Box 5b |
| Royalties | Box 6 |
| Net short-term capital gain | Box 7 |
| Net long-term capital gain (loss) | Box 8a |
| Collectibles 28% gain | Box 8b |
| Unrecaptured §1250 gain | Box 8c |
| Net §1231 gain (loss) | Box 9 |
| Other income | Box 10 |
| §179 deduction | Box 11 |
| Other deductions | Box 12 |
| Credits | Box 13 |
| Schedule K-1 supplemental information | Box 17 (multi-codes) |

## Schedule M-2 — Accumulated Adjustments Account

Tracks AAA, OAA (Other Adjustments Account), and PTI (Previously
Taxed Income — for pre-1983 carryover items, rare).

| Column | Account |
|---|---|
| (a) | AAA |
| (b) | OAA |
| (c) | PTI |
| (d) | Earnings and profits (only if S-corp has C-corp E&P from
       prior periods) |

AAA computation per §1368(e):
- Beginning AAA.
- + Items of income (other than tax-exempt income).
- + §1366(b) separately stated items.
- − Distributions to extent of AAA.
- − Non-deductible expenses (other than disqualified items).
- = Ending AAA.

§1368(c) ordering when C-corp E&P present:
1. Distributions tax-free to extent of AAA.
2. Distributions = dividend to extent of C-corp E&P.
3. Distributions tax-free to extent of remaining basis.
4. Distributions = capital gain in excess of basis.

## Schedule L — Balance Sheet

Required if total receipts ≥ $250K and total assets ≥ $250K.

Equity section reconciles to M-2 + retained earnings + capital
stock + APIC.

## Schedule B — Other Information

Includes yes/no questions on:
- Cash vs. accrual.
- Foreign owners (Form 5472 trigger).
- Entity-level audit elections (BBA opt-out NOT applicable to
  S-corps).
- §1374 BIG-tax recognition-period status.

## Schedule K-1 (Form 1120-S)

Per-shareholder K-1 has:
- Part I: shareholder identification.
- Part II: shareholder share (% and acquisition / disposition
  dates).
- Part III: pro-rata items mirroring Schedule K boxes.

§199A QBI items reported separately on K-1 lines (Box 17, codes
V/W/X/Y).

## Forms and schedules referenced

- Form 1125-A (COGS).
- Form 1125-E (compensation of officers).
- Form 2553 (S election; relevant for first-year returns).
- Form 4797 (sales of business property).
- Form 8990 (§163(j) limitation if applicable).

## Computed metrics

- **Per-share-per-day allocation** under §1377(a).
- **Reasonable-comp ratio**: officer W-2 (Form 1125-E Line 1) /
  ordinary business income before officer comp.
- **AAA ending balance** vs. distributions: distributions in
  excess trigger E&P-step-2 (if C-corp E&P) or basis-step-3 / capital-
  gain-step-4 (if no E&P).
- **§1374 BIG recognition period**: 5 years post-2009; expiration
  date to be tracked.
- **§1375 excess net passive-investment income tax**: applies
  only when E&P present and passive-income > 25% of gross receipts
  for 3 consecutive years.
- **§1361(b) eligibility checks**:
  - 100-shareholder limit.
  - Allowable shareholder types.
  - One class of stock.
  - Domestic corporation.

## Common practitioner pull-through items

- Reasonable-comp analysis (Watson pattern → route to
  `predict-reasonable-comp`).
- Stock / loan basis tracking for §1366(d) loss limitation.
- AAA / OAA / PTI maintenance.
- §1374 BIG tax exposure tracking.
- One-class-of-stock issues from disproportionate distributions.
- §362(e)(2) loss-importation if S-corp received §351
  contributions.
