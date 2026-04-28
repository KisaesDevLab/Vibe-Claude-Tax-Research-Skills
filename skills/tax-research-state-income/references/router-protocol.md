# State-router protocol

## Trigger detection

Match any of the following user-input patterns to the
corresponding state code, then load
`references/states/<XX>.md`:

### Direct identifiers

| Pattern | Code |
|---|---|
| "Alabama" / "AL" / "Ala." | AL |
| "Alaska" / "AK" | AK |
| "Arizona" / "AZ" / "Ariz." | AZ |
| "Arkansas" / "AR" / "Ark." | AR |
| "California" / "CA" / "Cal." / "Calif." | CA |
| "Colorado" / "CO" / "Colo." | CO |
| "Connecticut" / "CT" / "Conn." | CT |
| "Delaware" / "DE" / "Del." | DE |
| "District of Columbia" / "DC" / "D.C." / "Washington DC" | DC |
| "Florida" / "FL" / "Fla." | FL |
| "Georgia" / "GA" / "Ga." | GA |
| "Hawaii" / "HI" / "Hawai'i" | HI |
| "Idaho" / "ID" | ID |
| "Illinois" / "IL" / "Ill." | IL |
| "Indiana" / "IN" / "Ind." | IN |
| "Iowa" / "IA" | IA |
| "Kansas" / "KS" / "Kan." | KS |
| "Kentucky" / "KY" / "Ky." | KY |
| "Louisiana" / "LA" / "La." | LA |
| "Maine" / "ME" | ME |
| "Maryland" / "MD" / "Md." | MD |
| "Massachusetts" / "MA" / "Mass." | MA |
| "Michigan" / "MI" / "Mich." | MI |
| "Minnesota" / "MN" / "Minn." | MN |
| "Mississippi" / "MS" / "Miss." | MS |
| "Missouri" / "MO" / "Mo." | MO |
| "Montana" / "MT" / "Mont." | MT |
| "Nebraska" / "NE" / "Neb." | NE |
| "Nevada" / "NV" / "Nev." | NV |
| "New Hampshire" / "NH" / "N.H." | NH |
| "New Jersey" / "NJ" / "N.J." | NJ |
| "New Mexico" / "NM" / "N.M." | NM |
| "New York" / "NY" / "N.Y." / "NYS" | NY |
| "North Carolina" / "NC" / "N.C." | NC |
| "North Dakota" / "ND" / "N.D." | ND |
| "Ohio" / "OH" | OH |
| "Oklahoma" / "OK" / "Okla." | OK |
| "Oregon" / "OR" / "Ore." | OR |
| "Pennsylvania" / "PA" / "Pa." / "Penn." | PA |
| "Rhode Island" / "RI" / "R.I." | RI |
| "South Carolina" / "SC" / "S.C." | SC |
| "South Dakota" / "SD" / "S.D." | SD |
| "Tennessee" / "TN" / "Tenn." | TN |
| "Texas" / "TX" / "Tex." | TX |
| "Utah" / "UT" | UT |
| "Vermont" / "VT" / "Vt." | VT |
| "Virginia" / "VA" / "Va." | VA |
| "Washington" / "WA" / "Wash." | WA |
| "West Virginia" / "WV" / "W.Va." | WV |
| "Wisconsin" / "WI" / "Wis." | WI |
| "Wyoming" / "WY" / "Wyo." | WY |

### Distinctive features → state

| Pattern | Code | Note |
|---|---|---|
| "FTB" / "Franchise Tax Board" | CA | |
| "CDTFA" | CA | sales tax (route to salesuse skill) |
| "EDD" | CA | employment / payroll |
| "AB5" / "Dynamex" / "Prop 22" | CA | worker-classification |
| "$800 LLC fee" / "$800 minimum" | CA | |
| "Comptroller" (Texas) / "margin tax" | TX | |
| "Comptroller" (Maryland) | MD | |
| "Comptroller" (NY) | NY | (less common) |
| "convenience of employer" / "convenience rule" | NY | also DE, NE, PA, AR have variations |
| "TSB-A" | NY | NY advisory opinion citation form |
| "Article 9-A" | NY | NY corporate franchise |
| "Article 22" | NY | NY personal income tax |
| "millionaire surtax" / "Mass. 4% surtax" | MA | |
| "BAIT" | NJ | Business Alternative Income Tax (PTET) |
| "Hall tax" | TN | repealed |
| "F&E" / "franchise and excise" | TN | |
| "B&O" | WA | also OR, WV (different rates) |
| "WA cap gains" / "Washington capital gains" | WA | |
| "Oregon transit" / "TriMet" | OR | |
| "PTE Tax" | CT | (PTET) |
| "PTET" | (any) | route based on state context |
| "PA local EIT" / "local-services tax" | PA | local-tax overlay |
| "DRS" | CT | Department of Revenue Services |
| "DOTAX" | HI | Hawaii DOR |
| "DOR" (with state context) | varies | match by state name |

### Deduction-cap / nexus / specialty triggers

| Pattern | Codes | Note |
|---|---|---|
| "remote-work nexus" / "telecommuter nexus" | varies | route by state of residence + state of employer |
| "P.L. 86-272" | varies | federal protection from net-income tax for solicitation-only |
| "Wayfair" | varies | sales-tax economic nexus (route to salesuse skill) |
| "throwback" / "throwout" | varies | apportionment |
| "single-sales-factor" | varies | apportionment formula |
| "market-based sourcing" / "cost-of-performance" | varies | sourcing |
| "MTC" / "Multistate Tax Commission" | (multi-state) | route to all relevant states |
| "Streamlined Sales Tax" | (member states) | sales tax (route to salesuse skill) |

## Multi-state issues

When user input implicates more than one state:
1. Identify all states.
2. Load each state's per-file.
3. Address residency / domicile / physical-presence first.
4. Address sourcing / apportionment second.
5. Address state-specific quirks third.
6. Document each state file consulted in the JSON sidecar's
   `state_files_consulted[]` array.

Common multi-state patterns:
- Remote worker — resident state + employer state.
- Snowbird / part-year resident — both states.
- Pass-through entity with multi-state operations — apportionment.
- Estate with property in multiple states — situs analysis.

## Residency vs. domicile

- **Residency**: typically physical presence + intent to remain.
  Each state has its own statute / case law.
- **Domicile**: legal home; presumption of continuity.

Some states have "statutory residency" tests (e.g., NY 183-day +
substantial / permanent place of abode) layered on top of common-
law domicile.

Document the controlling state's residency / domicile rule in
the per-state file.

## P.L. 86-272 (federal protection)

15 U.S.C. § 381–384. Limits state's ability to impose net-income
tax on out-of-state seller whose only in-state activity is
solicitation of sales of tangible personal property fulfilled
from outside the state.

MTC's Statement of Information (revised 2021, "MTC Statement") —
post-Wayfair guidance narrowing P.L. 86-272 protections; many
states adopted MTC Statement.

P.L. 86-272 does NOT cover:
- Service businesses.
- Sales of intangibles.
- Internet-based transactions per the MTC Statement.
- Sales-tax obligations (Wayfair physical-presence nexus
  abandoned).

## Documentation in JSON sidecar

For every state implicated:

```json
{
  "state_files_consulted": [
    {
      "state_code": "CA",
      "skill": "tax-research-state-income",
      "status": "stub",
      "last_reviewed": "2026-04-27"
    },
    {
      "state_code": "NY",
      "skill": "tax-research-state-income",
      "status": "stub",
      "last_reviewed": "2026-04-27"
    }
  ]
}
```

When `status: stub`, the confidence-band-decay rule from
`shared/confidence-bands.md` caps the conclusion at LOW.
