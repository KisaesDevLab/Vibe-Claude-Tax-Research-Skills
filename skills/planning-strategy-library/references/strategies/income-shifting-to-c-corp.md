---
name: "Income Shifting to C Corporation"
slug: income-shifting-to-c-corp
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§11", "§531-537", "§541-547", "§482"]
forms: ["Form 1120"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

> **Caution:** Income shifting to a C corporation is a planning
> strategy that became more attractive after TCJA reduced the C
> corp rate to 21%. Common structures include forming a C corp
> service entity or holding company. Risks include §531
> accumulated earnings tax, §541 PHC tax, §482 transfer pricing
> scrutiny, reasonable compensation issues, and constructive
> dividend exposure. Practitioners should evaluate whether
> substance supports the structure beyond tax benefit.

## Overview

After TCJA reduced the C corp rate to 21% (vs. top individual rate
of 37%), income shifting from individual / pass-through to C corp
became economically attractive in some scenarios. Common structures:

1. **C corp service entity.** Owner forms separate C corp that
   provides management services to operating LLC/S corp at
   arm's-length fee. Some income shifted to C corp at 21% rather
   than passing through at 37% individual rate.

2. **C corp IP holding company.** IP held in C corp; licensed to
   operating entity at arm's-length royalty.

3. **Conversion to C corp.** S corp to C corp conversion (§1362(d)
   revocation).

4. **Choice-of-entity at formation.** Formation as C corp rather
   than S corp / LLC for new business.

The math: at 21% C corp rate plus subsequent dividend at 23.8%
(20% qualified dividend + 3.8% NIIT), effective combined rate is
approximately 39.8% — slightly above the 37% top individual rate.
Strategy works only if (a) earnings can be retained in corporation
rather than distributed, (b) eventual stock sale qualifies for
§1202 QSBS exclusion (#43), or (c) shareholder dies and basis
steps up under §1014.

The strategy is constrained by:
- **§531 accumulated earnings tax** — 20% penalty on unreasonable
  accumulation beyond ~$250K small business exemption.
- **§541 PHC tax** — 20% penalty on personal holding company
  failing to distribute earnings.
- **§482 transfer pricing** — intercompany pricing must be
  arm's-length.
- **Reasonable compensation** — both directions (#21).
- **Constructive dividends** — personal expenses run through
  C corp recharacterized as dividends.
- **§199A loss** — pass-through QBI deduction (20%) not available
  for C corps.

## Primary IRC authority

- §11 — C corp tax (21% rate).
- §531-537 — Accumulated earnings tax.
- §541-547 — PHC tax.
- §482 — Transfer pricing.
- §269 — Acquisition to avoid tax.
- §269A — Personal service corporation tax avoidance.
- §1361-1378 — S corp rules (S corp election / revocation).
- §199A — QBI (only for pass-through; flag for analysis).
- §1202 — QSBS (companion strategy).

## Treasury regulations

- Reg §1.482-1 through §1.482-9 — Transfer pricing.
- Reg §1.531-1 through §1.537-3 — Accumulated earnings.
- Reg §1.541-1 through §1.547-7 — PHC.

## Key IRS guidance

- IRS Publication 542 — Corporations.

## Key court decisions

- **Bardahl Manufacturing Corp. v. Commissioner, 24 T.C.M. 1030
  (1965)** — Bardahl formula for reasonable working capital
  needs.
- **Atlas Tool Co. v. Commissioner, 70 T.C. 86 (1978), aff'd, 614
  F.2d 860 (3d Cir. 1980)** — Constructive dividend.
- **Roubik v. Commissioner, 53 T.C. 365 (1969)** — Multiple-corp
  structures and §269A.

## Eligibility requirements

Vary by structure. Key considerations:
1. C corp legitimate business purpose.
2. §482 arm's-length pricing.
3. §269A personal service corporation.
4. §531/§541 accumulation justification.

## Mechanics — how it works

For C corp service entity:
1. **Form C corp** with reasonable business purpose (not solely
   tax-motivated).
2. **Service agreement with operating entity** at arm's-length
   pricing. §482 transfer pricing analysis required.
3. **C corp performs services** (separate office, employees, or
   identifiable function).
4. **Reasonable compensation to owner-employee** of C corp.
5. **Retain excess earnings in C corp** — invest in qualifying
   property; build §1202 QSBS basis if applicable.
6. **Annual §531 reasonable accumulation analysis** documenting
   business purpose.

For S to C conversion:
1. **Revoke S election** under §1362(d).
2. **5-year wait** before re-electing S status.
3. **Consider §1202 QSBS eligibility** for new C corp stock.

## Documentation requirements

- Business purpose memo for structure.
- Service agreements.
- §482 transfer pricing study.
- §531 accumulation analysis (Bardahl formula or similar).
- Board resolutions.
- Reasonable compensation analysis.

## Common pitfalls / audit risks

- **§269A personal service corporation.** Service corporations
  formed primarily for tax avoidance subject to penalty rates.
- **§482 transfer pricing.** Aggressive intercompany pricing
  challenged.
- **Constructive dividends.** Personal expenses run through C corp.
- **§531 accumulated earnings tax.** Excess accumulation beyond
  business needs.
- **§541 PHC tax.** Closely-held holding company with passive
  income.
- **Reasonable compensation.** Both excessive (treated as
  dividend) and insufficient (recharacterized as wages).
- **§199A loss.** Switching from pass-through forfeits §199A 20%
  deduction.
- **§1202 timing.** QSBS requires 5-year hold for full exclusion.
- **State conformity.** State may not follow federal C corp rate;
  state PTET-equivalent may not apply.

## Recent legislative changes

- **TCJA (2017)** — 21% C corp rate; created strategy attractiveness.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §11 §199A
  Pub L 119-21]`. If §199A made permanent and C corp rate
  unchanged, strategy economics reaffirmed; possible §1202
  expansion increases attractiveness.

## State conformity considerations

State C corp tax rates vary significantly. State conformity to
§482 transfer pricing varies. State combined-reporting rules may
collapse intercompany shifts.

## AICPA SSTS / Circular 230 considerations

Aggressive structure requiring substance documentation. Practitioner
should: verify business purpose; confirm §482 arm's-length pricing;
recommend Form 8275 disclosure for borderline positions; address
constructive dividend and reasonable compensation throughout
operating period.

## Default confidence band rationale

**MODERATE** — well-established structure but execution-sensitive.
HIGH for properly-documented separate-business C corps with clear
business purpose. LOW for aggressive shell structures lacking
substance.

## Cross-references

- `c-corp-dividends` (#31).
- `c-corp-misc-deductions` (#42).
- `c-corp-state-tax-savings` (#35).
- `section-1202-qsbs-extended` (#43).
- `reasonable-comp-corp-owners` (#21).
- `choice-of-entity-se-tax` (#86).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 11","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section11","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 482","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section482","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 531","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section531","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 269A","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section269A","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Bardahl Manufacturing Corp. v. Commissioner, 24 T.C.M. 1030 (1965)","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
