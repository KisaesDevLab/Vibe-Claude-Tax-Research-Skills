"""Generate 102 state-stub files (51 income + 51 sales/use) for Phase 3e/f."""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

data = json.load(open(REPO / "shared/sources.json"))
state_dors = data["state_dors"]
state_names = data["state_names"]
state_agency_names = data["state_agency_names"]
no_income = set(data["no_individual_income_tax"])
no_sales = set(data["no_state_sales_tax"])

INCOME_NOTES = {
    "AK": "No individual income tax. Skill applies only to fiduciary, corporate, or specialty contexts.",
    "FL": "No individual income tax. Skill applies only to fiduciary or specialty contexts (no individual filing).",
    "NV": "No individual income tax.",
    "SD": "No individual income tax.",
    "TN": "Hall income tax (interest and dividends) repealed effective tax year 2021. No individual income tax now.",
    "TX": "No individual income tax. State margin tax applies to entities (separate from individual income).",
    "WA": "No general individual income tax. WA capital gains tax (Wash. Rev. Code Sec. 82.87) imposes 7% on long-term gains > $262K standard deduction (2024 - verify year-specific). Quinn v. State, 1 Wn.3d 222 (2023) upheld constitutionality.",
    "WY": "No individual income tax.",
    "NH": "I&D (Interest and Dividends) tax repealed effective tax year 2025. No general individual income tax thereafter.",
    "CA": "CA FTB administers individual / fiduciary / corporate; CDTFA handles sales / use; EDD handles employment. Note: CA AB5 codified Dynamex three-prong ABC test for worker classification. CA Form 3804 PTET election.",
    "NY": "NYS Department of Taxation and Finance. Convenience-of-employer rule (TSB-M-06(5)I) applies to non-resident wages. NYS Article 22 personal income tax; Article 9-A corporate franchise tax. Multiple PTET elections (NY ETP).",
    "MA": "MA imposes a 4% surtax on income > $1M (effective 2023; Question 1 / 2022 ballot). Massachusetts Department of Revenue (DOR).",
    "OR": "OR statewide transit tax (0.1% wages); separate Multnomah / Portland additional taxes for high earners.",
    "PA": "PA local Earned Income Tax (EIT) overlay; PA itself has flat 3.07% state rate. PA did NOT conform to Sec. 1031 for individuals pre-2023.",
    "NJ": "NJ BAIT (Business Alternative Income Tax) PTET. NJ residents may have NY convenience-rule issues.",
    "IL": "IL flat individual rate; Illinois Department of Revenue (IDOR).",
}

SALES_NOTES = {
    "AK": "No statewide sales tax. Local sales taxes administered by Alaska Remote Seller Sales Tax Commission (ARSSTC) for participating municipalities. Wayfair-style threshold under ARSSTC: $100K gross statewide remote sales OR 200 transactions. Non-participating municipalities (e.g., Wasilla, Fairbanks) administer their own local taxes.",
    "DE": "No state sales tax. State imposes a Gross Receipts Tax on certain businesses; not a sales tax in the traditional sense.",
    "MT": "No state sales tax.",
    "NH": "No state sales tax. New Hampshire imposes a Meals and Rooms (Rentals) Tax that functions analogously for specific transactions.",
    "OR": "No state sales tax. Oregon imposes a state lodging tax for tourism-related transactions.",
    "CA": "CDTFA administers. CA Wayfair threshold: $500K (no transaction count). SaaS NOT taxable; pre-written software tangibly delivered IS.",
    "TX": "TX Comptroller administers. Origin sourcing for intrastate; destination for interstate. Data processing / SaaS taxable at 80%-reduced rate (effectively 1.58%). Wayfair threshold: $500K.",
    "NY": "NYS DTF administers. SaaS treated as TPP via 'pre-written software' classification - TAXABLE. Wayfair threshold: > $500K AND > 100 transactions.",
    "FL": "FL DOR administers. SaaS NOT taxable. Wayfair threshold: > $100K (no transaction count).",
    "WA": "WA DOR administers. SaaS taxable. Includes B&O tax overlay (Business and Occupation tax - gross-receipts based).",
    "CO": "CO state and home-rule cities administer separately; ~ 70 home-rule jurisdictions.",
    "AL": "AL state and Self-Administered Local Tax Jurisdictions (SALT-J).",
    "AZ": "Transaction Privilege Tax (TPT) with city-level rates.",
    "LA": "LA state and parish-level tax administration.",
    "TN": "TN imposes both state and local sales tax with combined rates often above 9%.",
    "NV": "NV has no individual income tax but does have state sales tax.",
    "SD": "SD has no individual income tax but does have state sales tax. Originator of South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018).",
    "WY": "WY has no individual income tax but does have state sales tax.",
    "IL": "IL state and Chicago-area local sales tax overlay.",
}


def build_stub(code, skill):
    name = state_names[code]
    agency = state_agency_names[code]
    url = state_dors[code]

    fm = (
        "---\n"
        f"state_code: {code}\n"
        f"state_name: {name}\n"
        "status: stub\n"
        "last_reviewed: 2026-04-27\n"
        "last_reviewed_by: bootstrap\n"
        "applies_to:\n"
        f"  - {skill}\n"
        "---\n\n"
    )

    header = f"# {name} ({code})\n\n"
    intro = (
        "> **Status: STUB.** This file contains the canonical agency entry\n"
        "> point and a structural skeleton. Substantive content has not been\n"
        "> verified by a practitioner. Treat as a starting pointer for live\n"
        "> retrieval, not as authority. Promote to `draft` after first\n"
        "> practitioner edit; `reviewed` after a second-pair review;\n"
        "> `verified` after live citation-walk against current statute and\n"
        "> regulation.\n\n"
    )

    admin = (
        "## Administrative bodies\n\n"
        f"- **Primary agency:** {agency} - {url}\n"
        "- **Income tax administration:** <agency, URL>           <!-- TODO: confirm -->\n"
        "- **Sales/use tax administration:** <agency, URL>        <!-- TODO: confirm -->\n"
        "- **Employment tax administration:** <agency, URL>       <!-- TODO: confirm -->\n"
        "- **Property/local tax administration:** <agency, URL>   <!-- TODO: confirm -->\n"
        "- **Tax appeals body:** <agency, URL>                    <!-- TODO: confirm -->\n\n"
    )

    note_set = INCOME_NOTES if skill == "tax-research-state-income" else SALES_NOTES
    notes_block = ""
    if code in note_set and note_set[code]:
        notes_block = f"## Practitioner notes (auto-populated)\n\n{note_set[code]}\n\n"

    if skill == "tax-research-state-income" and code in no_income:
        notes_block += "> **Note:** This jurisdiction has no general individual income tax. Per-state file applies primarily to fiduciary / corporate / specialty contexts.\n\n"
    if skill == "tax-research-state-salesuse" and code in no_sales:
        notes_block += "> **Note:** This jurisdiction has no statewide sales tax. Some jurisdictions impose local sales tax or alternative tax structures (see notes above).\n\n"

    citation_pattern = (
        "## Statute and regulation citation pattern\n\n"
        '- **Statute citation form:** <e.g., "Cal. Rev. & Tax. Code Sec. 17041">  <!-- TODO -->\n'
        '- **Regulation citation form:** <e.g., "Cal. Code Regs. tit. 18, Sec. 17041"> <!-- TODO -->\n'
        "- **Legislative website:** <URL>                                 <!-- TODO -->\n"
        "- **Regulation hub:** <URL>                                      <!-- TODO -->\n\n"
    )

    if skill == "tax-research-state-income":
        overview = (
            "## Income tax overview\n\n"
            "- **Has individual income tax?** <yes|no|limited>                <!-- TODO -->\n"
            "- **Filing status / rate structure:** <flat | graduated | brackets>  <!-- TODO -->\n"
            "- **Conformity to federal IRC:** <rolling | static | selective>  <!-- TODO -->\n"
            "- **Conformity date (if static):** <YYYY-MM-DD>                  <!-- TODO -->\n"
            '- **Standard deduction:** <amount or "follows federal">          <!-- TODO -->\n'
            "- **Itemized deduction conformity:** <notes>                     <!-- TODO -->\n"
            "- **Notable departures from federal:** <list>                    <!-- TODO -->\n"
            "- **Resident definition / domicile rule citation:**              <!-- TODO -->\n"
            "- **Convenience-of-employer rule applicable?** <yes|no>          <!-- TODO -->\n\n"
            "## Pass-through entity tax (PTET) / SALT cap workaround\n\n"
            "- **PTET available?** <yes|no>                                   <!-- TODO -->\n"
            "- **Election entity types:** <PTE types eligible>                <!-- TODO -->\n"
            "- **Election deadline / mechanics:**                              <!-- TODO -->\n"
            "- **Statute citation:**                                          <!-- TODO -->\n"
            "- **Practitioner notes:** <annual? irrevocable? credit at owner level?> <!-- TODO -->\n\n"
        )
    else:
        overview = (
            "## Sales and use tax overview\n\n"
            "- **Has state sales tax?** <yes|no>                              <!-- TODO -->\n"
            "- **State rate:** <%>                                            <!-- TODO -->\n"
            "- **Local rates allowed?** <yes|no, range>                       <!-- TODO -->\n"
            "- **Streamlined Sales Tax member?** <full | associate | no>      <!-- TODO -->\n"
            "- **Wayfair economic nexus thresholds:** <$ + transaction count> <!-- TODO -->\n"
            "- **Marketplace facilitator law citation:**                       <!-- TODO -->\n"
            "- **Notable taxability quirks:** <SaaS, digital goods, services> <!-- TODO -->\n"
            "- **Sourcing rule (origin / destination / mixed):**              <!-- TODO -->\n"
            "- **Local jurisdiction count and complexity notes:**             <!-- TODO -->\n\n"
        )

    appeals = (
        "## Letter ruling / advisory opinion repository\n\n"
        "- **Repository URL:** <URL>                                      <!-- TODO -->\n"
        '- **Citation form for rulings:** <e.g., "TSB-A-22(5)I (NY)">     <!-- TODO -->\n'
        "- **Search interface notes:**                                    <!-- TODO -->\n\n"
        "## Tax court / administrative appeals\n\n"
        "- **Appeals tribunal name:** <agency>                            <!-- TODO -->\n"
        "- **Decisions repository URL:**                                  <!-- TODO -->\n"
        "- **Statute of limitations on assessment:** <years>              <!-- TODO -->\n"
        "- **Statute of limitations on refund claim:** <years>            <!-- TODO -->\n\n"
        "## Recent developments (last 24 months)\n\n"
        "<!-- TODO: practitioner-populated -->\n\n"
        "## Sources consulted\n\n"
        f"1. {agency} - {url}\n"
    )

    return fm + header + intro + admin + notes_block + citation_pattern + overview + appeals


def main():
    skills = ["tax-research-state-income", "tax-research-state-salesuse"]
    codes = sorted(state_dors.keys())
    print(f"Generating stubs for {len(codes)} states across {len(skills)} skills...")
    count = 0
    for code in codes:
        for skill in skills:
            target = REPO / "skills" / skill / "references" / "states" / f"{code}.md"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(build_stub(code, skill), encoding="utf-8")
            count += 1
    print(f"Wrote {count} stubs.")


if __name__ == "__main__":
    main()
