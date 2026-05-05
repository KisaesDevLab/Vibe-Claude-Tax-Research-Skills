---
name: tax-research-state-salesuse
description: |
  State sales-and-use-tax research skill covering nexus (physical
  and Wayfair economic), taxability of goods / services / digital
  / SaaS, sourcing (origin / destination / mixed), marketplace
  facilitator obligations, and exemption certificates for all 51
  jurisdictions (50 states + DC). Implements a state-router protocol:
  when the user mentions a state by name, abbreviation, or
  distinctive feature, the skill loads the corresponding
  references/states/<XX>.md before drafting analysis. Use when the
  user asks "sales tax", "use tax", "Wayfair nexus", "sales-tax
  nexus", "SaaS sales tax", "marketplace facilitator", "sales-tax
  for [state]", "Streamlined Sales Tax", "exemption certificate", or
  "destination sourcing". Make sure to use this skill whenever the
  user mentions sales tax, use tax, Wayfair, marketplace
  facilitator, or sales-tax nexus.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# tax-research-state-salesuse — State sales/use-tax research

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/state-template.md` — promotion ladder.
6. `references/router-protocol.md` — state-detection and routing
   procedure.
7. The relevant `references/states/<XX>.md` per the user's
   jurisdiction(s).

## Supported jurisdictions

All 50 states + DC. State codes (ISO/USPS):

```
AL  AK  AZ  AR  CA  CO  CT  DE  DC  FL
GA  HI  ID  IL  IN  IA  KS  KY  LA  ME
MD  MA  MI  MN  MS  MO  MT  NE  NV  NH
NJ  NM  NY  NC  ND  OH  OK  OR  PA  RI
SC  SD  TN  TX  UT  VT  VA  WA  WV  WI
WY
```

Per `shared/sources.json`:
- **No state sales tax**: AK*, DE, MT, NH, OR.
- *AK has no statewide sales tax but has local sales taxes
  administered by the Alaska Remote Seller Sales Tax Commission
  (ARSSTC).

## State-router protocol

When the user mentions a state — by full name, USPS code,
distinctive feature, or DOR brand — the skill MUST:

1. Identify the jurisdiction code.
2. Load `references/states/<XX>.md`.
3. Read the file's `status` field:
   - `stub`: per-state file is intentionally placeholder. Cap
     state confidence at LOW.
   - `draft`: cap at MODERATE.
   - `reviewed`: cap at HIGH if facts well-aligned.
   - `verified`: HIGH band available.
4. Note `state_code` and `status` in
   `state_files_consulted[]`.

## Workflow

### 1. Intake

- `taxpayer_business_state(s)`: states where seller has
  operations / employees / property.
- `customer_state(s)`: where deliveries / digital downloads occur.
- `transaction_volume_per_state`: dollars and transactions for
  Wayfair economic-nexus thresholds.
- `product_or_service_type`: goods, services, digital, SaaS,
  Software-as-a-Service vs. installed software, custom vs. off-
  the-shelf.
- `marketplace_facilitator_relationship`: selling through Amazon,
  Shopify, Walmart Marketplace, etc.
- `tax_year`.

### 2. Nexus analysis

#### Physical nexus

Pre- and post-Wayfair physical-presence triggers:
- Office / warehouse / retail location.
- Employees / agents / contractors performing services.
- Inventory in third-party fulfillment (Amazon FBA — significant
  litigation).
- Trade-show / event presence (state-specific de-minimis rules).
- Affiliate / click-through nexus statutes (largely subsumed by
  Wayfair).

#### Wayfair economic nexus

South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018) overruled
Quill physical-presence requirement for sales tax.

Most states adopted economic nexus thresholds:
- $100,000 gross receipts OR 200 transactions (the SD Wayfair
  benchmark) — adopted by many states.
- Variations: $250K (some states); $500K (CA, TX, NY); transaction
  count alone (some states).

Per-state file documents the specific threshold.

### 3. Taxability analysis

#### Tangible personal property (TPP)

Generally taxable. Exemptions vary by state:
- Food / groceries (varies; CA exempt; some taxable).
- Clothing (PA exempt; MA $175 cap; others taxable).
- Prescription drugs (most states exempt).
- Medical devices.
- Manufacturing equipment (most states exempt under specific
  conditions).
- Agricultural inputs.

#### Services

- Many states tax SOME services (e.g., commercial cleaning, data
  processing, telecommunications).
- Few states tax MOST services (HI's General Excise Tax taxes
  almost everything).
- Some states tax NO services (CA largely services-exempt).

Per-state file documents service-taxability framework.

#### Digital goods / SaaS

Highly variable. Categories:
- Pre-written / canned software delivered electronically (most
  states tax).
- Custom software (often exempt as a service).
- SaaS / cloud computing (varies widely; NY, TX, MA, WA, PA tax;
  CA / VA / FL generally exempt).
- Streaming media / digital books (varies).
- Information services (NY taxes; CA does not).

#### Marketplace facilitator

Wayfair-era marketplace facilitator laws:
- Marketplace operator (Amazon, Shopify with Shopify Tax, eBay,
  Etsy) collects and remits sales tax on behalf of third-party
  sellers.
- Per-state effective dates and threshold rules.
- Seller's own threshold computation may exclude marketplace
  sales (Streamlined Sales Tax states) or include them (other
  states).

### 4. Sourcing

- **Origin sourcing**: tax determined by seller's location.
  Examples: AZ (intrastate), MO, OH, TX (intrastate).
- **Destination sourcing**: tax determined by purchaser's
  location. Most states for interstate sales.
- **Mixed**: origin for intrastate, destination for interstate
  (most states).

### 5. Streamlined Sales Tax (SST)

24 member states (verify current — list in
`shared/sources.json` `multistate.streamlined_sales_tax`).

Member states harmonize:
- Definitions of products / services.
- Sourcing rules (destination).
- Exemption certificate forms (Streamlined Exemption Certificate).
- Single registration via SST.

### 6. Exemption certificates

For sales to:
- Resellers (resale certificate).
- Manufacturers (manufacturing exemption).
- Tax-exempt organizations (§501(c) certificates).
- Government entities.

State-specific forms; periodic renewal required.

### 7. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`.
Required: `state_files_consulted[]` array.

Confidence band per `shared/confidence-bands.md` with state-stub
decay rule:
- HIGH only if state file is `verified` AND facts unambiguous.
- LOW (cap) if state file is `stub`.

### 8. Tax Foundation / Tax Policy Center

`persuasive_non_authority` only. MUST NOT serve as the closest
cite.

## Hard rules

- ALWAYS load the relevant `references/states/<XX>.md` BEFORE
  drafting analysis when any state is implicated.
- ALWAYS cap state confidence at LOW when state file is
  `status: stub`.
- ALWAYS verify Wayfair economic-nexus threshold per the
  per-state file before stating numbers.
- NEVER let Tax Foundation or Tax Policy Center drive a
  confidence band.
- For local sales-tax overlays (AK, CO, AZ, LA, et al.),
  separately address state vs. local administration.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Add the state-stub residual
practitioner responsibility per `tax-research-state-income`
SKILL.md.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
