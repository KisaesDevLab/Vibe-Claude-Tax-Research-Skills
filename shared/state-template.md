---
state_code: <XX>
state_name: <Full name>
status: stub                    # stub → draft → reviewed → verified
last_reviewed: 1970-01-01
last_reviewed_by: <handle>
applies_to:                     # which research skills consume this file
  - tax-research-state-income
  - tax-research-state-salesuse
---

# <Full state name> (<XX>)

> **Status: STUB.** This file contains the canonical agency entry point
> and a structural skeleton. Substantive content has not been verified
> by a practitioner. Treat as a starting pointer for live retrieval, not
> as authority. Promote to `draft` after first practitioner edit;
> `reviewed` after a second-pair review; `verified` after live
> citation-walk against current statute and regulation.

## Administrative bodies

- **Primary agency:** <name> — <URL from shared/sources.json>
- **Income tax administration:** <agency, URL>           <!-- TODO: confirm -->
- **Sales/use tax administration:** <agency, URL>        <!-- TODO: confirm -->
- **Employment tax administration:** <agency, URL>       <!-- TODO: confirm -->
- **Property/local tax administration:** <agency, URL>   <!-- TODO: confirm -->
- **Tax appeals body:** <agency, URL>                    <!-- TODO: confirm -->

## Statute and regulation citation pattern

- **Statute citation form:** <e.g., "Cal. Rev. & Tax. Code § 17041">  <!-- TODO -->
- **Regulation citation form:** <e.g., "Cal. Code Regs. tit. 18, § 17041"> <!-- TODO -->
- **Legislative website:** <URL>                                 <!-- TODO -->
- **Regulation hub:** <URL>                                      <!-- TODO -->

## Income tax overview

- **Has individual income tax?** <yes|no|limited>                <!-- TODO -->
- **Filing status / rate structure:** <flat | graduated | brackets>  <!-- TODO -->
- **Conformity to federal IRC:** <rolling | static | selective>  <!-- TODO -->
- **Conformity date (if static):** <YYYY-MM-DD>                  <!-- TODO -->
- **Standard deduction:** <amount or "follows federal">          <!-- TODO -->
- **Itemized deduction conformity:** <notes>                     <!-- TODO -->
- **Notable departures from federal:** <list>                    <!-- TODO -->
- **Resident definition / domicile rule citation:**              <!-- TODO -->
- **Convenience-of-employer rule applicable?** <yes|no>          <!-- TODO -->

## Sales and use tax overview

- **Has state sales tax?** <yes|no>                              <!-- TODO -->
- **State rate:** <%>                                            <!-- TODO -->
- **Local rates allowed?** <yes|no, range>                       <!-- TODO -->
- **Streamlined Sales Tax member?** <full | associate | no>      <!-- TODO -->
- **Wayfair economic nexus thresholds:** <$ + transaction count> <!-- TODO -->
- **Marketplace facilitator law citation:**                       <!-- TODO -->
- **Notable taxability quirks:** <SaaS, digital goods, services> <!-- TODO -->
- **Sourcing rule (origin / destination / mixed):**              <!-- TODO -->
- **Local jurisdiction count and complexity notes:**             <!-- TODO -->

## Pass-through entity tax (PTET) / SALT cap workaround

- **PTET available?** <yes|no>                                   <!-- TODO -->
- **Election entity types:** <PTE types eligible>                <!-- TODO -->
- **Election deadline / mechanics:**                              <!-- TODO -->
- **Statute citation:**                                          <!-- TODO -->
- **Practitioner notes:** <annual? irrevocable? credit at owner level?> <!-- TODO -->

## Letter ruling / advisory opinion repository

- **Repository URL:** <URL>                                      <!-- TODO -->
- **Citation form for rulings:** <e.g., "TSB-A-22(5)I (NY)">     <!-- TODO -->
- **Search interface notes:**                                    <!-- TODO -->

## Tax court / administrative appeals

- **Appeals tribunal name:** <agency>                            <!-- TODO -->
- **Decisions repository URL:**                                  <!-- TODO -->
- **Statute of limitations on assessment:** <years>              <!-- TODO -->
- **Statute of limitations on refund claim:** <years>            <!-- TODO -->

## Practitioner notes

- <Free-form bullets: special elections, unusual rules, traps,
  e.g., CA AB5, NY convenience rule, MA millionaire surtax, WA
  capital gains tax, OR statewide transit tax.>                  <!-- TODO -->

## Recent developments (last 24 months)

<!-- TODO: bullet major legislative or regulatory changes -->

## Secondary policy data (optional, NON-AUTHORITY) — v1.1

When promoting this stub to `draft` or higher, the practitioner may
consult independent policy data sources for context on conformity,
rates, and recent legislative tracking. These sources are
`persuasive_non_authority` at most and MUST NOT serve as the closest
cite for any conclusion:

- **Tax Foundation Center for State Tax Policy** —
  https://taxfoundation.org/center/state-tax-policy/
  (state conformity tables, rate tables, PTET tracker; pro-low-tax
  editorial viewpoint)
- **Tax Policy Center (Urban-Brookings)** —
  https://www.taxpolicycenter.org
  (state tax fact-sheets; centrist/progressive editorial viewpoint)

When citing either, tag as `weight: persuasive_non_authority` and
record the citation in the practitioner notes section, NOT in the
authoritative analysis.

## Sources consulted

<!-- TODO: list URL + retrieved_date for any source consulted while
     populating this file. Required before promoting status above stub. -->
