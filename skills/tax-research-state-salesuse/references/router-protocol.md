# State-router protocol — sales/use tax

Mirror of `tax-research-state-income/references/router-protocol.md`
with sales-tax-specific trigger phrases.

## Trigger detection

### Direct identifiers

Same state-name / USPS-code / abbreviation table as the income-tax
router. (See income-tax router-protocol.md for full table.)

### Sales-tax-specific feature triggers

| Pattern | Code | Note |
|---|---|---|
| "CDTFA" | CA | California Department of Tax and Fee Administration |
| "NY Department of Taxation and Finance" | NY | |
| "FL Dept of Revenue" | FL | |
| "TX Comptroller" / "TX sales tax" | TX | |
| "AK local sales tax" / "ARSSTC" | AK | Alaska Remote Seller Sales Tax Commission |
| "Streamlined Sales Tax" / "SST" / "SSUTA" | (multi) | route to all member states |
| "Wayfair" / "Wayfair nexus" / "economic nexus" | (any state) | route by state |
| "marketplace facilitator" | (any state) | route by state |
| "P.L. 86-272" | n/a | NOT applicable to sales tax — federal protection is limited to net-income tax |
| "destination sourcing" / "origin sourcing" | (any state) | route by state |

### Product-type triggers

| Pattern | Notes |
|---|---|
| "SaaS" / "software as a service" / "cloud computing" | NY/TX/MA/WA/PA tax most SaaS; CA / VA / FL exempt; verify per-state file |
| "digital goods" / "ebooks" / "downloaded software" | most states tax pre-written software; varies for digital goods |
| "streaming" | varies; some states tax (FL communications service tax) |
| "data processing" | TX taxable at reduced rate (3.94%); IL, OH, NM tax data processing |
| "information services" | NY taxes; CA exempt |
| "advertising services" | most states exempt; some (e.g., DC, FL) tax certain advertising |
| "telecommunications" | most states tax; FL imposes Communications Services Tax |
| "groceries" / "food for home consumption" | varies — most exempt, some tax |
| "prepared food" | most states tax |
| "clothing" | PA full exempt; MA $175 cap; NY <$110 exempt; NJ exempt; verify per state |
| "prescription drugs" | most states exempt |
| "medical devices" | many states exempt with conditions |
| "manufacturing equipment" | most states exempt under specific conditions |
| "agricultural inputs" / "feed" / "fertilizer" | most states exempt |

## Multi-state nexus analysis workflow

1. Identify all states where the seller has potential nexus.
2. For each state, check:
   - Physical-presence nexus (employees / property / inventory in
     state).
   - Wayfair economic-nexus thresholds ($100K / 200 transactions
     baseline; verify per-state file for variations).
   - Marketplace facilitator status (does Amazon / Shopify / etc.
     collect on the seller's behalf).
3. Determine collection / remittance obligation per state.
4. Identify exemption-certificate requirements for tax-exempt
   sales.

## Sourcing analysis

### Origin sourcing

Tax determined by seller's location. States: AZ (intrastate), MO,
OH (intrastate), TX (intrastate).

### Destination sourcing

Tax determined by purchaser's location. Most states for interstate
sales.

### Mixed (origin for intrastate, destination for interstate)

Most states fall here. Per-state file documents specifics.

## Local-tax overlay

States with significant local sales tax administration:
- **AK**: no statewide; ARSSTC manages remote sellers; local
  sales taxes vary widely.
- **CO**: home-rule cities self-administer; ~ 70 home-rule
  jurisdictions.
- **AL**: Self-Administered Local Tax Jurisdictions (SALT-J).
- **AZ**: Transaction Privilege Tax (TPT) with city-level rates.
- **LA**: Parish-level tax administration.

For these states, address state and local separately. Per-state
file documents local-jurisdiction count and complexity.

## Documentation in JSON sidecar

Same format as the income-tax router protocol:

```json
{
  "state_files_consulted": [
    {
      "state_code": "TX",
      "skill": "tax-research-state-salesuse",
      "status": "stub",
      "last_reviewed": "2026-04-27"
    }
  ]
}
```

When `status: stub`, the confidence-band-decay rule from
`shared/confidence-bands.md` caps the conclusion at LOW.
