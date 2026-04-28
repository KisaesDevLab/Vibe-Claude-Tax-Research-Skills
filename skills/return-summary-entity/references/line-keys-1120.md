# Form 1120 (C-corporation) line keys

For tax year 2024 — verify year-specific Form 1120 instructions
before quoting line numbers; renumbering does occur.

## Page 1 — Income and tax computation

| Line | Item |
|---|---|
| 1a | Gross receipts or sales |
| 1b | Returns and allowances |
| 1c | Net (1a − 1b) |
| 2 | Cost of goods sold (Form 1125-A) |
| 3 | Gross profit |
| 4 | Dividends (Schedule C) |
| 5 | Interest |
| 6 | Gross rents |
| 7 | Gross royalties |
| 8 | Capital gains (Schedule D) |
| 9 | Net gain/(loss) — Form 4797 |
| 10 | Other income |
| 11 | TOTAL INCOME |
| 12 | Compensation of officers (Form 1125-E if receipts ≥ $500K) |
| 13 | Salaries and wages (less employment-tax credits) |
| 14 | Repairs and maintenance |
| 15 | Bad debts |
| 16 | Rents |
| 17 | Taxes and licenses |
| 18 | Interest |
| 19 | Charitable contributions |
| 20 | Depreciation |
| 21 | Depletion |
| 22 | Advertising |
| 23 | Pension, profit-sharing |
| 24 | Employee benefits |
| 25 | Reserved |
| 26 | Other deductions |
| 27 | TOTAL DEDUCTIONS |
| 28 | TI before NOL / special deductions (Line 11 − 27) |
| 29a | NOL deduction |
| 29b | Special deductions (Schedule C) |
| 30 | TAXABLE INCOME (Line 28 − 29c) |
| 31 | Total tax (Schedule J) |
| 32 | Reserved |
| 33 | Total payments and credits (Schedule J) |
| 34 | Estimated tax penalty (Form 2220) |
| 35 | Amount owed |
| 36 | Overpayment |
| 37 | Amount of overpayment refunded / applied to next year |

## Schedules

### Schedule C — Dividends, Inclusions, Special Deductions

DRD computation per §243 / §245A. GILTI inclusion under §951A
flows here.

### Schedule J — Tax Computation

- Tax under §11 (currently 21% flat post-TCJA — verify year).
- Personal Holding Company tax (§541 / Schedule PH).
- Excess net passive-investment income tax (rare for C-corps).
- §55 corporate AMT (post-IRA 2022 for applicable corporations
  with > $1B average AFSI for prior 3 years).
- §59A BEAT for large multinationals.

### Schedule K — Other Information

Includes:
- Type of entity (cooperative, etc.).
- Personal Service Corporation status (Q3) — flat 35% pre-TCJA;
  21% post-TCJA.
- §269A association-of-persons questions.
- §382 ownership change indicators.

### Schedule L — Balance Sheet

- Beginning and ending balance sheet.
- Reconciles to M-1 / M-2 / M-3.
- Schedule L not required for C-corps with assets < $250K and
  receipts < $250K (test under instructions).

### Schedule M-1 — Reconciliation of Income (Loss) per Books

- Net income per books → Taxable income per Schedule K Line 30.
- Adjustments for tax-exempt income, non-deductible expenses,
  depreciation differences, etc.

### Schedule M-3 — Detailed Reconciliation (assets ≥ $10M)

Partitioned reconciliation:
- Part I: financial-statement reconciliation.
- Part II: income items.
- Part III: deduction items.

### Schedule G — Information on Persons Owning ≥ 25%

Form 5472 trigger when 25% foreign-owned.

## Computed metrics

- **Effective tax rate** = Line 31 / Line 11.
- **Effective rate on book income** = Line 31 / book income (M-1
  Line 1).
- **§163(j) excess interest expense** — separately tracked if
  business-interest > 30% × ATI + interest income + floor-plan.
- **§382 limitation** — annual limit if ownership change occurred.
- **NOL utilization** — pre-TCJA 80% taxable-income limit applies
  to NOLs arising in tax years beginning after 12/31/2017.

## Forms and schedules referenced

- Form 1125-A (COGS).
- Form 1125-E (compensation of officers).
- Form 4626 (Alternative Minimum Tax — corporations, post-IRA).
- Form 4797 (sales of business property).
- Form 5472 (foreign-owned U.S. corporation).
- Form 8990 (§163(j) limitation).
- Form 8991 (§59A BEAT).
- Form 8975 (country-by-country reporting).

## Common practitioner pull-through items

- Officer compensation reasonableness (route to
  `predict-reasonable-comp`).
- §163(j) carryover tracking.
- §382 limitation tracking after ownership changes.
- §1059(e) extraordinary-dividend reductions for §245A.
- §245A DRD eligibility checks.
- §59A BEAT modified-taxable-income computation.
