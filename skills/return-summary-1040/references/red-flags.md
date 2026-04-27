# Red-flag catalog — individual return (Form 1040)

Patterns the skill flags during summary, with suggested next-skill
routes. NOT tax-position advice; the routes lead to skills that
provide rigorous research / prediction.

## High-priority planning hooks

### SALT cap binding
Pattern: Schedule A line 5e capped at $10K ($5K MFS) and the user
shows state-passthrough income on Schedule E.
Flag: PTET opportunity. Route to `tax-research-state-income`
(state-specific PTET rules) and `planning-strategy-library`
(strategy: "PTET election").

### Large Schedule A charitable
Pattern: Schedule A line 14 ≥ 60% of AGI, OR > $50K cash to public
charity, OR appreciated stock contribution.
Flag: Bunching strategy + DAF. Route to `planning-strategy-library`
(strategy: "Donor-advised fund / charitable bunching").

### Capital-loss carryover
Pattern: Schedule D shows large LTCL or STCL carryover; § 1211(b)
$3K cap binding.
Flag: Loss-harvesting strategy + Roth conversion offset.
Route to `planning-actions-1040`.

### Unused HSA capacity
Pattern: Box 12 W (employer HSA contribution) shows < limit (year-
appropriate per Rev. Proc.) AND user has HSA-eligible HDHP.
Flag: HSA top-up. Route to `planning-strategy-library` (strategy:
"HSA maximization").

### Roth-eligible / backdoor opportunity
Pattern: AGI puts user above Roth direct-contribution phase-out
(§ 408A) AND user has no traditional IRA balance.
Flag: Backdoor Roth. Route to `planning-strategy-library`.

### Mega-backdoor opportunity
Pattern: Schedule SE or W-2 indicates self-employment / high W-2
income, and the user has a 401(k) plan with after-tax contribution
allowance.
Flag: Mega-backdoor Roth. Route to `planning-strategy-library`.

### Real-estate-professional possibility
Pattern: Schedule E Part I rental losses suspended; user mentions
real-estate activity hours.
Flag: Run `predict-real-estate-pro` to test § 469(c)(7).

### Material-participation issue
Pattern: Schedule E Part II non-passive treatment of K-1 losses
without obvious indicia of material participation.
Flag: Run `predict-material-participation` to test the seven tests.

### QBI eligibility
Pattern: Schedule C / Schedule E nonpassive K-1 income > 0 AND no
QBI deduction on line 13 (or QBI deduction less than expected).
Flag: Run `predict-qbi-eligibility` to test § 199A.

### Hobby-loss exposure
Pattern: Schedule C activity with losses 3+ of last 5 years
(§ 183(d) presumption).
Flag: Run `predict-hobby-loss` to test § 183 nine-factor analysis.

### Reasonable-comp issue (S-corp)
Pattern: K-1 line 1 ordinary business income > $50K with no Schedule
SE or W-2 from the same entity.
Flag: Run `predict-reasonable-comp` to test § 162(a)(1).

## Compliance / penalty risk

### Estimated-tax penalty (§ 6654)
Pattern: Withholding gap > $1,000 AND user did not meet safe harbor
(90% current / 100% prior, 110% if AGI > $150K).
Flag: Form 2210 required. Route to `penalty-interest-calc`.

### Underpayment penalty (§ 6662)
Pattern: Audit-trigger return characteristics (high Schedule C,
home-office, large meals, vehicle-only basis for large deduction).
Flag: Substantial-authority review for any contested position.
Route to `tax-research-federal` to test the position.

### NIIT exposure (§ 1411)
Pattern: AGI > $200K single / $250K MFJ AND meaningful net
investment income (interest, dividends, capital gains, rental,
passthrough non-active income).
Flag: 3.8% NIIT computation; check Schedule 2 line 12.

### Additional Medicare (§ 3101(b)(2))
Pattern: Wages or SE earnings > $200K single / $250K MFJ.
Flag: 0.9% additional Medicare; Form 8959.

### AMT exposure (§ 55)
Pattern: Schedule 2 line 1 > 0 OR ISO exercise on W-2 / 1099 / 3921.
Flag: Form 6251 review; ISO bargain-element timing.

### Foreign accounts (FBAR / Form 8938)
Pattern: Schedule B Part III "yes" OR foreign-bank-account interest /
dividends.
Flag: FBAR (FinCEN 114) and Form 8938 thresholds (§ 6038D).

### Foreign tax credit
Pattern: Schedule B foreign source income OR Form 1116 attached.
Flag: § 901 / § 904 limitation computation; election to take credit
vs. deduction.

### Crypto / digital assets
Pattern: Form 1040 page 1 question "yes" OR Form 8949 codes for
digital-asset dispositions.
Flag: § 6045 broker reporting (post-IIJA) and ordinary-vs.-capital
character analysis.

### Self-employment retirement plan opportunity
Pattern: Schedule C net profit > $50K with no SEP / Solo 401(k) on
Schedule 1.
Flag: SEP-IRA, SIMPLE-IRA, Solo 401(k) deferral. Route to
`planning-strategy-library`.

## Filing-status / dependency edge cases

### Head of household qualification
Pattern: Single filing status with dependents in household.
Flag: Test § 2(b) HoH eligibility — could lower bracket and unlock
EIC.

### Married-filing-separately
Pattern: MFS filing with high income.
Flag: § 1(d) bracket compression; loss of EIC, IRA deduction, AOC,
student-loan-interest deduction. Recommend MFJ vs. MFS comparison.

### Qualifying relative (§ 152(d))
Pattern: User claims qualifying-relative dependent with high earned
or unearned income.
Flag: Gross-income test; $5,050 (2024) limit (year-appropriate).

### EIC vs. other credits
Pattern: Low AGI + qualifying child.
Flag: EIC + ACTC + AOC interactions; verify dependency tests.

## State piggyback flags (federal-summary skill scope)

The skill notes but does NOT analyze:
- State conformity to QBI / SALT / itemized deductions
- State PTET availability
- State residency / domicile / convenience-of-employer

Routes user to `tax-research-state-income` for any state-specific
follow-up.

## Out-of-scope items (explicitly NOT flagged)

- Estate / gift exposure (route to `tax-research-estate-gift`)
- Audit response (route to `notice-response`)
- Multi-year scenario planning (route to `planning-multi-year`)
