# Withholding and FICA mechanics

## FICA components

### OASDI (Old Age, Survivors, Disability Insurance)

§3101(a) — employee share 6.2% on wages up to the OASDI wage base.
§3111(a) — employer share 6.2% on same.

The OASDI wage base is announced annually by the Social Security
Administration. Verify the specific year:
https://www.ssa.gov/cola/

Self-employment OASDI: §1401(a) — 12.4% (combined employer +
employee) on net SE earnings up to wage base.

### Medicare HI (Hospital Insurance)

§3101(b) — employee share 1.45% on ALL wages (no wage cap).
§3111(b) — employer share 1.45% on same.

Self-employment Medicare: §1401(b) — 2.9% on all SE earnings.

### Additional Medicare Tax

§3101(b)(2) — additional 0.9% on employee wages > $200,000
regardless of filing status.

§1401(b)(2) — additional 0.9% on combined wages + SE income
above:
- $200,000 single, head of household, qualifying surviving spouse;
- $250,000 MFJ;
- $125,000 MFS.

Employer withholding of additional Medicare per §3102(f):
- Employer withholds 0.9% on any wages paid to an employee in
  excess of $200,000 in a calendar year, regardless of marital
  status.
- Employee reconciles on Form 8959.

### Net Investment Income Tax (NIIT) — 3.8%

§1411 — 3.8% on net investment income above threshold ($200K
single, $250K MFJ). NIIT is NOT a payroll tax but is often grouped
with the additional-Medicare framework. Reported on Form 8960.

## FUTA

§3301 — 6% gross rate on first $7,000 of wages per employee per
year. §3302 credits up to 5.4% for state UI taxes paid timely,
yielding net 0.6%.

§3306(c)(7) — domestic-service exception: applies only when an
employer pays cash wages of less than $1,000 in any quarter to all
household employees combined (note: lower threshold than FICA's
per-employee threshold).

## Federal income-tax withholding (§3402)

§3402 — withholding from wages paid to employees. Form W-4 (post-
TCJA redesigned 2020) used to determine withholding.

§3401(a) — wages excluded from withholding:
- Employer-provided dependent-care assistance.
- Qualified educational-assistance ($5,250 cap, §127).
- Qualified retirement-plan contributions.
- §125 cafeteria-plan elective contributions.

Pub. 15 (Circular E) tables convert Form W-4 inputs + wage period
into withholding amounts.

## Special wage situations

### Severance pay

Generally subject to FICA / FIT withholding as wages. United States
v. Quality Stores, 572 U.S. 141 (2014) — Supreme Court held SUB
(supplemental unemployment-benefit) payments are wages for FICA.

### Bonuses / supplemental wages

§3402(g) and Treas. Reg. §31.3402(g)-1: two methods —
- Aggregate method: combine with regular wages and use W-4 tables.
- Optional flat rate: 22% (for amounts ≤ $1M annually), 37% for
  amounts > $1M.

### Stock-based compensation

§3402(j) — withholding on disqualifying-disposition ISO, NSO
exercise, RSU vesting, ESPP §423(c) qualifying / disqualifying
dispositions.

§409A — non-qualified deferred-compensation rules with severe
penalties for failures (20% additional tax + premium-interest).

§83(b) elections — capture income on grant rather than vesting;
filed within 30 days; treated for FICA on the income recognized.

### Tipped employees (§3121(q))

Tip income reported by the employee on Form 4070 (or W-2 with
tip reporting) is wages for FICA. Employer share computed on
reported tips. §45B FICA-tip credit available to certain food /
beverage employers.

### Reimbursements under accountable plans (§62(c))

Reimbursements under an accountable plan are NOT wages and not
subject to FICA / withholding. Plan must:
- Have a business connection.
- Require substantiation within reasonable time.
- Require return of excess within reasonable time.

Failed accountable plans become non-accountable; entire payment
is wages.

### Health-insurance and §125 cafeteria

§125 elective contributions to cafeteria plans are pre-FICA / pre-
FIT. Health-insurance premiums paid through §125 are similarly
pre-FICA / pre-FIT.

S-corp shareholder-employee health-insurance: §1372 / Notice 2008-
1 — 2%+ shareholders include health-insurance premiums in W-2
Box 1 (FIT-taxable) but NOT in Box 3 (FICA) or Box 5 (Medicare).

### IRC §3134 ERC (Employee Retention Credit) — historical

Pandemic-era credit retired by Infrastructure Investment and Jobs
Act for most employers after Q3 2021. Recovery startup businesses
extended through Q4 2021.

ERC mills generated significant fraudulent / over-aggressive
claims. Practitioners should be alert to client requests to
revisit ERC claims; route to specialized review and consider
voluntary withdrawal under IRS Withdrawal Process (announced
October 2023) for unprocessed claims.

## State payroll-tax interaction

States impose:
- State income-tax withholding (variable rules; some states have
  no income tax — AK, FL, NV, SD, TN [post-Hall repeal], TX, WA
  [capital-gains-only], WY).
- State unemployment insurance (SUI / SUTA) — every state.
- State disability insurance (CA, HI, NJ, NY, RI).
- Local income taxes (NYC, San Francisco, Philadelphia, etc.).

Per-state rates and bases live in
`skills/tax-research-state-income/references/states/<XX>.md`.
Route state-specific questions there.

## Practitioner audit-defense file

- [ ] Form 941 / 940 quarterly filings reconciled to W-3 summary.
- [ ] Schedule of FICA wage bases and additional-Medicare
  withholding triggers.
- [ ] §125 cafeteria-plan / health-insurance pre-tax computation.
- [ ] Bonus / supplemental-wage withholding method documented.
- [ ] Equity-compensation withholding traced through W-2 Box 12
  codes.
- [ ] §62(c) accountable-plan documentation.
- [ ] §3508 statutory non-employee contracts and remuneration
  structure if applicable.
