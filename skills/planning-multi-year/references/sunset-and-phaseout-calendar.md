# Sunset / phase-out / phase-in calendar

Verify each row against current law via the Public-Law-to-USC
workflow in `shared/legislation-tracking.md` before relying on it
for client advice. Many provisions modified by OBBBA (Pub. L.
119-XX, 2025); this calendar is a starting reference, not
authority.

## Major TCJA individual sunsets (12/31/2025)

| Provision | TCJA-era | Post-sunset (absent extension) |
|---|---|---|
| §1(j) brackets | 10/12/22/24/32/35/37 | Reverts to pre-TCJA: 10/15/25/28/33/35/39.6 |
| §63 standard deduction | $14,600 single (2024) / $29,200 MFJ | Reverts to pre-TCJA × inflation |
| §164(b)(6) SALT cap | $10,000 | Repealed |
| §163(h)(3) HELOC interest | Limited to acquisition indebtedness | Pre-TCJA broader scope returns |
| §199A QBI | 20% deduction | Repealed (PTET workarounds become less valuable) |
| §11 corporate rate | 21% flat | (TCJA permanently changed; not a sunset) |
| §2010 estate / gift exclusion | Doubled to ~$13.99M (2025) | Reverts to ~$7M inflation-adjusted |
| AMT exemption | $85,700 single / $133,300 MFJ (2024) | Reverts to lower pre-TCJA exemption |
| Misc. itemized deduction (§67(g)) | Suspended | Reinstated |
| §132(g) moving-expense deduction | Suspended (except military) | Reinstated |
| §165(h) personal casualty deduction | Suspended (except disaster) | Reinstated |
| §219(b) IRA deduction | (Already extended) | n/a |

OBBBA enacted in 2025 may have made many of these permanent or
modified the schedule — verify per Classification Tables.

## TCJA business provisions

| Provision | Schedule |
|---|---|
| §168(k) bonus depreciation | 100% (2017–2022); 80% (2023); 60% (2024); 40% (2025); 20% (2026); 0% (2027) — verify OBBBA modifications |
| §174 R&E expensing | 5-year domestic / 15-year foreign amortization for years beginning after 12/31/2021 — verify OBBBA reversion |
| §163(j) ATI | EBITDA basis (2018–2021); EBIT basis (2022+) — verify OBBBA modifications |
| §250 FDII deduction | 37.5% (2018–2025); 21.875% (2026+) — verify OBBBA |
| §250 GILTI deduction | 50% (2018–2025); 37.5% (2026+) — verify OBBBA |
| §59A BEAT rate | 10% (2018–2025); 12.5% (2026+) — verify OBBBA |

## SECURE Act / SECURE 2.0 RMD age

| Birth year | RMD age |
|---|---|
| Pre-1951 | 70½ (legacy) |
| 1951–1959 | 73 |
| 1960+ | 75 |

§401(a)(9)(C) — verify SECURE 2.0 provisions (Pub. L. 117-328
div. T) for specifics.

## SECURE 2.0 catch-up indexing (§414(v))

- 2024: regular catch-up $7,500; SIMPLE $3,500.
- 2025+: enhanced catch-up at ages 60-63 = $11,250 (or 150% of
  regular limit).
- 2026: Roth catch-up MANDATORY for high earners (Notice 2023-62
  delayed from 2024).

## IRA 2022 (Pub. L. 117-169) credits

| Credit | Schedule |
|---|---|
| §30D EV (consumer) | $7,500 ($3,750 each component) for vehicles placed in service 2023+; manufacturing-source phase-in |
| §45W commercial EV | $7,500 / $40,000 (large) |
| §25C residential energy | 30%, $1,200 cap (annual); $2,000 heat-pump |
| §25D solar | 30%, no cap (residential) |
| §45 PTC (production) | Various phase-out periods |
| §48 ITC (investment) | Various (50% bonus + adders) |
| §48D advanced manufacturing | (CHIPS Act, Pub. L. 117-167) |
| §45X production credit | New for 2023+ |
| §40A clean fuel credit | 2025+ |

OBBBA may have modified specific credit amounts, eligibility, and
phase-outs — verify per shared/legislation-tracking.md.

## §55 corporate AMT (IRA 2022)

- Effective for tax years beginning after 12/31/2022.
- "Applicable corporation" = 3-year average AFSI > $1B.
- 15% minimum on AFSI; AMT FTC and AMT NOL adjustments.
- Form 4626.

## §4501 stock-buyback excise (IRA 2022)

- Effective for tax years beginning after 12/31/2022.
- 1% of net buybacks by publicly-traded U.S. corporations.
- Form 7208.

## IRMAA Medicare premium tiers (annual indexing)

§1839(i) — Medicare Part B/D premium tiers indexed annually;
verify current-year thresholds.

| 2024 single | 2024 MFJ |
|---|---|
| ≤ $103,000 | ≤ $206,000 |
| $103,001 – $129,000 | $206,001 – $258,000 |
| $129,001 – $161,000 | $258,001 – $322,000 |
| $161,001 – $193,000 | $322,001 – $386,000 |
| $193,001 – $499,999 | $386,001 – $749,999 |
| ≥ $500,000 | ≥ $750,000 |

Tier breaks: each level adds substantial Part B/D surcharges.

## §401(a)(17) / §415 compensation caps (annual indexing)

- 2024 §401(a)(17): $345,000.
- 2024 §415(c) defined-contribution limit: $69,000.
- 2024 §415(b) defined-benefit limit: $275,000.

## Estate / gift / GST exclusions (annual indexing)

§2010 / §2503 exclusions — annual inflation adjustments under
§2010(c)(3).

| Year | Annual exclusion (§2503(b)) | Lifetime exclusion (§2010) |
|---|---|---|
| 2023 | $17,000 | $12.92M |
| 2024 | $18,000 | $13.61M |
| 2025 | $19,000 | $13.99M |
| 2026+ | (verify) | Reverts to ~$7M absent extension; OBBBA may have modified |

## Section-by-section practitioner reference

When a multi-year projection touches any of these provisions, use
`shared/legislation-tracking.md` to:
1. Confirm the Public Law(s) governing the provision.
2. Pull the Classification Table for the relevant Public Law.
3. Verify the current text of the affected USC section.
4. Identify legislative-history artifacts (JCT Bluebook,
   committee reports, Greenbook, CBO score) for interpretive
   support.
5. Document Public Laws in `public_laws_consulted[]` of the JSON
   sidecar.

## Projection modeling template

For each year in the planning horizon:

1. **Statutory rates**: identify rate in effect; apply phase-down
   if applicable.
2. **Itemized vs. standard**: compute under year-specific
   standard deduction.
3. **Capital-gains brackets**: 0% / 15% / 20% with NIIT 3.8%.
4. **AMT**: compute exemption phase-out for the year.
5. **§199A QBI**: identify whether deduction available.
6. **§168(k) bonus**: identify percentage available.
7. **§174 R&E**: identify amortization period or expensing.
8. **§163(j)**: identify ATI basis.
9. **State conformity**: per-state file.
10. **Documentation**: Public Laws material to year-N projection
    in `public_laws_consulted[]`.

## Disclosure flags

Multi-year planning often involves recommendations whose tax
benefit depends on legislative continuity. SSTS §1.1 (realistic
possibility) and §2.3 (estimates) require:
- Disclosure to client of legislative-uncertainty assumptions.
- Annual review when new legislation enacted.
- Conservative interpretation when relying on continuity of
  expiring provisions.
