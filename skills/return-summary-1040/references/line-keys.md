# Form 1040 line keys

Key line numbers and computed values the skill extracts. Form 1040
lines have shifted between TY 2018, TY 2019, TY 2020, and TY 2024.
For prior years, the skill must verify against the year-appropriate
Form 1040 instructions:
https://www.irs.gov/forms-instructions

## Form 1040 (TY 2024)

| Line | Field | Notes |
|---|---|---|
| 1a–1z | Wages, salaries, tips | Add 1a through 1z; pull from Form W-2 box 1. |
| 2a | Tax-exempt interest | Schedule B Part I if > $1,500. |
| 2b | Taxable interest | Schedule B Part I if > $1,500. |
| 3a | Qualified dividends | Schedule B Part II. |
| 3b | Ordinary dividends | Schedule B Part II. |
| 4a / 4b | IRA distributions / taxable amount | RMD from §401(a)(9); SECURE 2.0 raised RMD age. |
| 5a / 5b | Pensions and annuities / taxable amount | |
| 6a / 6b | Social security benefits / taxable amount | Up to 85% taxable per § 86. |
| 6c | Lump-sum election | If § 86(e) election made. |
| 7 | Capital gain or (loss) | From Schedule D; § 1211(b) $3K limit. |
| 8 | Additional income | From Schedule 1, line 10. |
| 9 | Total income | Sum of 1z–8. |
| 10 | Adjustments | From Schedule 1, line 26. |
| 11 | Adjusted gross income (AGI) | Line 9 − line 10. |
| 12 | Standard deduction OR itemized | Either standard (year-appropriate) or Schedule A line 17. |
| 13 | QBI deduction | From Form 8995 / 8995-A. |
| 14 | Sum of 12 + 13 | |
| 15 | Taxable income | Line 11 − line 14. Cannot go below 0. |
| 16 | Tax | Tax-table or computation; from year-appropriate Rev. Proc. brackets. |
| 17 | Amount from Schedule 2, line 3 | AMT (Form 6251) + excess APTC. |
| 18 | Add 16 + 17 | |
| 19 | Child tax credit and credit for other dependents | § 24. |
| 20 | Amount from Schedule 3, line 8 | Other nonrefundable credits. |
| 21 | Add 19 + 20 | |
| 22 | Line 18 − line 21 | Cannot go below 0. |
| 23 | Other taxes | From Schedule 2, line 21 — SE tax, NIIT (§ 1411), additional Medicare (§ 3101(b)(2)), § 72(t) early-withdrawal, etc. |
| 24 | Total tax | Line 22 + line 23. |
| 25a–25c | Federal income tax withheld | From W-2 box 2 + 1099 box 4 + others. |
| 26 | 2024 estimated tax payments + prior-year refund applied | |
| 27 | Earned income credit (EIC) | § 32. |
| 28 | Additional child tax credit | Refundable portion of CTC. |
| 29 | American opportunity credit (refundable portion) | § 25A. |
| 31 | Amount from Schedule 3, line 15 | |
| 32 | Add 27–29 + 31 | |
| 33 | Total payments | Line 25 + 26 + 32. |
| 34 | Overpayment | Line 33 − line 24 if positive. |
| 35a | Amount of line 34 to be refunded to you | |
| 36 | Amount applied to 2025 estimated tax | |
| 37 | Amount you owe | Line 24 − line 33 if positive. |
| 38 | Estimated tax penalty | § 6654; Form 2210. |

## Schedule line keys (selected)

### Schedule A — Itemized deductions
- Line 5e: SALT cap binding at $10K ($5K MFS) per § 164(b)(6) (TCJA;
  set to expire / be modified — verify current statute).
- Line 8e: Home-mortgage interest cap on acquisition indebtedness;
  $750K post-TCJA, $1M for pre-12/15/2017 grandfathered debt.
- Line 14: Charitable contributions; § 170 percentage limits.
- Line 16: Casualty / theft losses limited to federally-declared
  disasters under § 165(h)(5) post-TCJA.

### Schedule B — Interest and dividends
- Part III: Foreign accounts and FBAR (FinCEN Form 114) trigger.

### Schedule C — Profit or loss from business
- Line 31: Net profit or (loss).
- Line 32: At-risk limitation (§ 465).

### Schedule D — Capital gains and losses
- Line 16: Net long-term + short-term.
- Line 21: Limit to $3,000 ($1,500 MFS) per § 1211(b); excess
  carries forward indefinitely per § 1212(b).

### Schedule E — Supplemental income and loss
- Part I: Rental real estate; passive vs. nonpassive (§ 469);
  real-estate-professional exception (§ 469(c)(7)).
- Part II: Pass-throughs (K-1s).
- Part III: Estates and trusts (K-1).

### Schedule SE — Self-employment tax
- Line 4: Net SE earnings × 92.35% (§ 1402(a)).
- Line 12: SE tax.
- Line 13: Half-SE deduction (§ 164(f)).

## Year-specific differences

For TY 2018–2019, lines 1a/1b versus 1z aggregation differ. For TY
2020 and 2021, "Recovery Rebate Credit" appeared on line 30 (now
removed). For TY 2018–2019, "above-the-line educator expenses"
appeared on different schedule line numbers. The skill must use the
year-appropriate line keys.

## Computed values

- **Effective rate** = total tax (line 24) / total income (line 9).
- **Marginal rate** = bracket of taxable income (line 15) for the
  filing status, year-appropriate. Brackets come from the inflation-
  adjustment Rev. Proc. for the year (issued each fall).
- **Withholding gap** = total tax − federal withholding − estimated
  payments. Positive = balance due risk; > $1,000 with no safe
  harbor triggers § 6654 penalty.
- **Safe harbor**: smaller of 90% current-year tax or 100% prior-
  year (110% if AGI > $150K).
- **Marginal capital-gains rate**: 0% / 15% / 20% per filing-status
  thresholds in § 1(h); year-appropriate.
- **NIIT**: 3.8% on net investment income above § 1411 thresholds
  ($200K single, $250K MFJ).
