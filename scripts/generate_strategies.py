"""Generate the 30 strategy reference files for planning-strategy-library."""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "skills" / "planning-strategy-library" / "references" / "strategies"
OUT.mkdir(parents=True, exist_ok=True)

# Each tuple: (slug, title, irc, summary, eligibility, mechanics, citations, state_notes, legislation_notes, warnings)
STRATEGIES = [
    # ---------- Individual / 1040 (10) ----------
    (
        "backdoor-roth",
        "Backdoor Roth IRA",
        "IRC Sec. 408A",
        "High-income taxpayer makes a non-deductible Traditional IRA contribution and immediately converts to Roth IRA, sidestepping the direct-contribution phase-out at higher AGI levels.",
        [
            "Taxpayer's MAGI exceeds direct Roth contribution phase-out (single $146K-$161K 2024; MFJ $230K-$240K 2024 - verify year-specific Rev. Proc.).",
            "Taxpayer has earned income at or above the contribution limit ($7,000 / $8,000 50+ for 2024).",
            "Pro-rata rule (Sec. 408(d)(2)) requires aggregation of all Traditional IRA balances at year-end; existing pre-tax balances cause partial taxability of the conversion.",
        ],
        [
            "Open or use a Traditional IRA; make non-deductible contribution; track basis on Form 8606.",
            "Convert to Roth IRA; report on Form 8606 Lines 4-13 (pro-rata calculation if other IRA balances).",
            "Roth IRA receives the converted amount; subsequent withdrawals subject to Sec. 408A 5-year ordering rules.",
        ],
        [
            "IRC Sec. 408A (Roth IRA).",
            "IRC Sec. 408(d)(2) (pro-rata rule).",
            "IRC Sec. 408(o) (non-deductible contributions).",
            "Form 8606 (basis tracking).",
        ],
        "No state-specific eligibility issues for federal Roth conversion. State conformity to federal Roth treatment is generally rolling.",
        "TCJA repealed recharacterization (Sec. 408A(d)(6)(B)(iii)); conversions are irrevocable.",
        [],
    ),
    (
        "mega-backdoor-roth",
        "Mega Backdoor Roth (after-tax 401(k))",
        "IRC Sec. 401(k) + Sec. 408A",
        "Taxpayer makes after-tax (non-Roth, non-pre-tax) contributions to 401(k) and converts via in-plan Roth conversion or in-service distribution to Roth IRA, capturing the full Sec. 415(c) limit minus elective deferrals.",
        [
            "Plan must permit after-tax contributions AND in-plan Roth conversions OR in-service distributions.",
            "Taxpayer has not maxed Sec. 415(c) limit ($69,000 2024) via elective deferrals + employer match.",
            "After-tax contributions limited by Sec. 415(c) less elective deferrals less employer match.",
        ],
        [
            "Confirm plan-document permits after-tax contributions and either in-plan Roth conversion or in-service distribution.",
            "Make after-tax contributions during the plan year up to the Sec. 415(c) headroom.",
            "Convert to Roth (in-plan or distributed to Roth IRA).",
            "Report on Form 1099-R (taxable portion = earnings since contribution).",
        ],
        [
            "IRC Sec. 401(k).",
            "IRC Sec. 415(c) (annual limit $69K 2024; verify year-specific).",
            "IRC Sec. 408A(d)(3) (Roth conversion).",
        ],
        "No state-specific eligibility issues.",
        "SECURE 2.0 (Pub. L. 117-328 div. T) modified Sec. 414(v) catch-up indexing; Roth catch-up for high earners delayed to 2026 per Notice 2023-62.",
        [],
    ),
    (
        "tax-loss-harvesting",
        "Tax-Loss Harvesting",
        "IRC Sec. 1091",
        "Taxpayer realizes losses on taxable-account positions and uses them against current-year capital gains, with up to $3K against ordinary income (Sec. 1211(b)) and indefinite carryforward.",
        [
            "Position held in a taxable account (not IRA / 401(k)).",
            "Realized loss available.",
            "Sec. 1091 wash-sale rule: cannot purchase substantially-identical security within 30 days before or after the sale.",
        ],
        [
            "Identify positions with unrealized losses.",
            "Sell the position; recognize loss.",
            "Avoid substantially-identical purchases within 61-day window.",
            "Apply against current capital gains; up to $3K ordinary offset; carryforward.",
        ],
        [
            "IRC Sec. 1091 (wash sales).",
            "IRC Sec. 1211(b) ($3K ordinary loss limit).",
            "IRC Sec. 1212 (capital-loss carryover).",
        ],
        "No state-specific issues for federal harvesting; state conformity varies for capital-loss treatment.",
        "",
        [],
    ),
    (
        "charitable-bunching-daf",
        "Charitable Bunching with Donor-Advised Fund",
        "IRC Sec. 170",
        "Taxpayer aggregates multiple years of charitable contributions into a single year via a Donor-Advised Fund to clear the standard deduction floor; subsequent grants from DAF are non-tax events.",
        [
            "Itemizing in the contribution year exceeds standard deduction ($14,600 single / $29,200 MFJ 2024).",
            "Sufficient cash or appreciated securities available for bunched contribution.",
            "DAF sponsor accepts contribution.",
        ],
        [
            "Open DAF at sponsor (Fidelity Charitable, Schwab Charitable, Vanguard Charitable, community foundation).",
            "Contribute cash or appreciated securities; capture immediate Sec. 170 deduction (cash 60% AGI / appreciated 30% AGI).",
            "Make grants from DAF over multi-year periods to qualifying charities; grants are not tax events.",
            "Substantiate per Sec. 170(f)(8) (>= $250 contemporaneous written acknowledgment).",
        ],
        [
            "IRC Sec. 170 (charitable deduction).",
            "IRC Sec. 170(b) (AGI percentage limits).",
            "IRC Sec. 170(f)(8) (substantiation).",
            "IRC Sec. 170(f)(11) (qualified appraisal for non-cash > $5K).",
        ],
        "State charitable-contribution rules vary; some states cap or modify federal deduction.",
        "",
        [],
    ),
    (
        "qcd-from-ira",
        "Qualified Charitable Distribution from IRA",
        "IRC Sec. 408(d)(8)",
        "IRA owner age 70 1/2+ directs up to $105,000 (2024) annually from Traditional IRA directly to qualifying charity; counts toward RMD; not included in AGI.",
        [
            "IRA owner age 70 1/2 or older at the time of distribution.",
            "Distribution direct from custodian to qualifying charity (not to taxpayer first).",
            "Annual cap $105,000 / individual (2024 - verify year-specific).",
            "Charity must be public Sec. 170(b)(1)(A) charity (not DAF, private foundation, supporting organization).",
        ],
        [
            "Direct IRA custodian to send check / wire to qualifying charity.",
            "Counts toward RMD requirement (Sec. 401(a)(9)).",
            "AGI exclusion = full distribution (no Sec. 170 deduction; no AGI inclusion).",
            "Substantiate as charitable-contribution receipt.",
        ],
        [
            "IRC Sec. 408(d)(8) (QCD).",
            "IRC Sec. 401(a)(9) (RMD).",
            "Sec. 170(b)(1)(A) (qualifying charity).",
        ],
        "State conformity to federal QCD AGI exclusion varies; check per-state file.",
        "SECURE 2.0 increased QCD inflation indexing.",
        [],
    ),
    (
        "solo-401k",
        "Solo 401(k) for Self-Employed",
        "IRC Sec. 401(k)",
        "Self-employed taxpayer with no employees (other than spouse) establishes a Solo 401(k) combining employee elective deferrals + employer profit-sharing contributions for a high tax-deferred limit.",
        [
            "Self-employed status (Schedule C / 1099-NEC / partnership).",
            "No common-law employees other than spouse.",
            "Plan established by required deadline (post-SECURE Act, 401(k) plans can be established by tax-return due date with extensions for the year).",
        ],
        [
            "Establish plan document (prototype or custom).",
            "Elective deferrals up to Sec. 402(g) limit ($23,000 / $30,500 50+ 2024).",
            "Employer profit-sharing up to 25% of net SE earnings (capped at Sec. 415(c) $69,000 combined limit 2024).",
            "Spouse may also defer if engaged in the business.",
            "Annual Form 5500-EZ required when plan assets exceed $250K.",
        ],
        [
            "IRC Sec. 401(k).",
            "IRC Sec. 402(g) (elective deferral limit).",
            "IRC Sec. 415(c) (annual limit).",
            "IRC Sec. 408 (rollover availability).",
        ],
        "No state-specific eligibility issues.",
        "SECURE 2.0 (Pub. L. 117-328 div. T) reduced administrative burden; allowed for post-year-end establishment.",
        [],
    ),
    (
        "cash-balance-plan",
        "Cash-Balance Defined-Benefit Plan",
        "IRC Sec. 412 / Sec. 401(a)",
        "Closely-held business establishes a cash-balance defined-benefit plan; high-earning owner-employee (often combined with 401(k) profit-sharing) achieves tax deductions of $200K-$300K+ annually.",
        [
            "Stable, profitable closely-held business.",
            "Older owner-employee with shorter time horizon to retirement (boosts actuarial contribution).",
            "Willing to fund employee benefits proportionally if non-discrimination tests apply.",
            "Plan document drafted by ERISA attorney / actuary.",
        ],
        [
            "Engage plan actuary and ERISA attorney for plan design.",
            "Coordinate with 401(k) profit-sharing for combined benefit.",
            "Annual actuarial valuation per Sec. 430 funding rules.",
            "Top-heavy testing; non-discrimination testing.",
            "Form 5500 annual filing.",
        ],
        [
            "IRC Sec. 412 (minimum funding).",
            "IRC Sec. 401(a) (qualified plans).",
            "IRC Sec. 415(b) (benefit limit; $275K 2024).",
            "IRC Sec. 416 (top-heavy).",
        ],
        "No state-specific issues for plan establishment; state pension protection laws may apply.",
        "",
        [],
    ),
    (
        "hsa-as-retirement",
        "HSA as Long-Term Retirement Vehicle",
        "IRC Sec. 223",
        "HDHP-eligible taxpayer maximizes HSA contributions, pays current medical expenses out of pocket (saving receipts), and reimburses years later from HSA - capturing triple-tax-free growth.",
        [
            "Eligible Individual under Sec. 223(c)(1): HDHP coverage; no other health coverage; not enrolled in Medicare; not a dependent of another taxpayer.",
            "Annual contribution limit ($4,150 self / $8,300 family 2024 + $1,000 catch-up at 55+).",
        ],
        [
            "Open HSA at qualified custodian.",
            "Contribute up to annual limit.",
            "Invest in growth-oriented options.",
            "Pay medical expenses out of pocket; retain receipts.",
            "Reimburse later (no time limit on reimbursement of qualified medical expenses).",
        ],
        [
            "IRC Sec. 223 (HSA).",
            "IRC Sec. 223(c) (eligible individual; HDHP).",
            "IRC Sec. 223(d) (qualified medical expenses).",
        ],
        "California and New Jersey do NOT conform to federal HSA tax treatment; HSA contributions and growth are state-taxable in those states.",
        "",
        [],
    ),
    (
        "roth-conversion-ladder",
        "Roth Conversion Ladder",
        "IRC Sec. 408A(d)(3)",
        "Taxpayer converts portions of Traditional IRA to Roth across multiple years to manage marginal-rate exposure, especially before TCJA bracket sunsets (12/31/2025; verify OBBBA modifications).",
        [
            "Sufficient pre-tax IRA balance.",
            "Liquidity to pay conversion tax from non-IRA sources (otherwise reduces effective benefit).",
            "Marginal-rate runway in current year (room within current bracket before reaching higher tier).",
            "IRMAA cliff awareness for Medicare-eligible taxpayers.",
        ],
        [
            "Project marginal rates across 5-10 year horizon.",
            "Compute conversion amount that fills current-year bracket without crossing into higher tier.",
            "Repeat annually; maintain log of conversion amounts and 5-year holding-period clocks per conversion.",
            "Coordinate with QCD opportunities at age 70 1/2+.",
        ],
        [
            "IRC Sec. 408A(d)(3) (conversion).",
            "IRC Sec. 408(d)(2) (pro-rata rule).",
            "IRC Sec. 1839(i) (IRMAA tiers).",
        ],
        "State conformity to federal Roth conversion taxability is generally rolling.",
        "TCJA bracket schedule sunsets 12/31/2025 absent extension; OBBBA may have modified - route to `irc-section-lookup` for verification.",
        [],
    ),
    (
        "state-residency-shift",
        "State-Residency Planning",
        "(state-specific)",
        "High-income taxpayer establishes domicile in low- or no-tax state to reduce state-income-tax exposure on portfolio income, capital gains, retirement distributions.",
        [
            "Genuine intent to make new state the domicile (not just physical presence).",
            "Severance of ties to former state (sell home, change driver's license, voter registration, business affiliations).",
            "Document new state's residency requirements (typically 183-day physical presence + permanent place of abode + intent).",
            "Watch out for prior-state convenience-of-employer rules (NY, DE, NE, PA, AR variations).",
        ],
        [
            "Establish physical presence in new state per its statutory test.",
            "Change driver's license, voter registration, vehicle registration.",
            "Update tax-return filings and PO box / mailing addresses.",
            "Document with calendar / receipts / utility bills if challenged.",
            "Prior-state may continue to claim taxation under domicile rules; defend with documentation.",
        ],
        [
            "Per-state statutes and regulations - see `references/states/<XX>.md` per state.",
        ],
        "Each state has its own residency / domicile test. Prior-state may claim continued taxation; document carefully. Route to `tax-research-state-income` per-state file.",
        "",
        [],
    ),
    # ---------- Entity (10) ----------
    (
        "ptet-election",
        "Pass-Through Entity Tax Election",
        "IRC Sec. 164; Notice 2020-75",
        "S-corp / partnership / LLC elects to pay state income tax at the entity level; deduction at entity reduces federal taxable income; owner receives state credit. Workaround for Sec. 164(b)(6) $10K SALT cap.",
        [
            "State has enacted PTET (most states have by 2024).",
            "Entity is eligible PTE under state law (S-corp / partnership; some states include LLC; some exclude single-member LLCs).",
            "Election made by deadline (varies by state; some require pre-payment).",
        ],
        [
            "Identify state PTET deadline (per `references/states/<XX>.md`).",
            "File state PTET election form (e.g., CA Form 3804, NY ETP, NJ BAIT).",
            "Make required pre-payment if applicable.",
            "Deduct state PTET at entity level under Notice 2020-75.",
            "Credit state PTET against owner's state income tax on K-1.",
        ],
        [
            "IRC Sec. 164 (state-tax deduction).",
            "Notice 2020-75 (federal-deduction framework).",
            "IRC Sec. 164(b)(6) (SALT cap; bypassed at entity level).",
            "Per-state statutes.",
        ],
        "PTET is state-by-state; eligibility and deadline vary widely. Always route to `tax-research-state-income/<XX>.md`.",
        "TCJA Sec. 164(b)(6) $10K cap sunsets 12/31/2025 absent extension. OBBBA may have modified - if SALT cap repealed, PTET workaround becomes less valuable.",
        [],
    ),
    (
        "s-corp-reasonable-comp",
        "S-Corp Reasonable Compensation Optimization",
        "IRC Sec. 162; Sec. 1366",
        "Owner-employee of closely-held S-corp pays reasonable W-2 wages (per Mayson factors / Watson framework), then takes balance as distributions to avoid FICA on the distribution portion.",
        [
            "S-corp has positive net income.",
            "Owner-employee performs services for corporation.",
            "Reasonable-compensation analysis based on industry comparables, role, hours.",
            "Watson v. United States, 668 F.3d 1008 (8th Cir. 2012) framework.",
        ],
        [
            "Annual reasonable-compensation study (industry comparables, internal data).",
            "Adjust W-2 wages to land within defensible range.",
            "Document board-resolution / compensation-committee deliberations.",
            "Coordinate with 401(k) elective deferrals.",
            "Route to `predict-reasonable-comp` for substantive analysis.",
        ],
        [
            "IRC Sec. 162(a)(1) (reasonable comp).",
            "IRC Sec. 1366(e) (S-corp reasonable-comp framework).",
            "Watson v. United States, 668 F.3d 1008 (8th Cir. 2012).",
            "Treas. Reg. Sec. 31.3121(d)-1.",
        ],
        "No state-specific eligibility; some states (e.g., NJ) impose entity-level S-corp tax that affects calculation.",
        "",
        [],
    ),
    (
        "accountable-plan",
        "Accountable Plan Reimbursement",
        "IRC Sec. 62(c)",
        "Employer reimburses employees / owner-employees for business expenses under an accountable plan; reimbursements are pre-tax (no FICA, no income tax) and deductible at entity level.",
        [
            "Three Sec. 62(c) conditions: business connection, substantiation within reasonable time, return of excess.",
            "Written plan document.",
            "Substantiation procedures and forms.",
        ],
        [
            "Adopt written accountable-plan policy.",
            "Implement expense-report forms with required substantiation (date, amount, business purpose, receipts).",
            "Establish return-of-excess procedure.",
            "Train employees on submission requirements.",
            "Audit periodically for compliance.",
        ],
        [
            "IRC Sec. 62(c).",
            "Treas. Reg. Sec. 1.62-2 (general rules).",
            "Treas. Reg. Sec. 1.62-2(g) (substantiation timing).",
        ],
        "No state-specific issues; states generally conform.",
        "",
        [],
    ),
    (
        "cost-segregation",
        "Cost Segregation + Bonus Depreciation",
        "IRC Sec. 168(k); Sec. 179",
        "Real-property buyer engages a cost-segregation engineer to reclassify components of building purchase / construction into shorter-life Sec. 1245 categories (5, 7, 15-year) for accelerated depreciation, often combined with Sec. 168(k) bonus.",
        [
            "Acquired or constructed depreciable real property.",
            "Sufficient basis to support reclassification analysis.",
            "Service in a trade or business or income-producing activity.",
            "Sec. 168(k) bonus available for the year (60% 2024, 40% 2025, 20% 2026 - verify OBBBA).",
        ],
        [
            "Engage qualified cost-segregation engineer for study.",
            "Reclassify components per the study (e.g., 5-year personal property, 15-year land improvements).",
            "Apply Sec. 168(k) bonus to qualifying components.",
            "Apply Sec. 179 expensing as applicable.",
            "Form 3115 / Sec. 481(a) catch-up if cost-seg done after placed-in-service.",
        ],
        [
            "IRC Sec. 168(k) (bonus depreciation).",
            "IRC Sec. 179 (expensing).",
            "IRC Sec. 263A (UNICAP / capitalization).",
            "Rev. Proc. 2015-13 (Sec. 481 method change).",
        ],
        "State conformity to federal Sec. 168(k) bonus varies; some states decouple from bonus. Cost-seg-driven federal acceleration may not flow through to state.",
        "Sec. 168(k) phase-down: 60% (2024); 40% (2025); 20% (2026); 0% (2027). OBBBA may have modified - route to `irc-section-lookup`.",
        [],
    ),
    (
        "section-179-expensing",
        "Section 179 Expensing",
        "IRC Sec. 179",
        "Taxpayer elects to expense up to $1.16M (2024) of qualifying tangible personal property in the year placed in service, subject to taxable-income and Sec. 179 phase-out limits.",
        [
            "Qualifying property: tangible personal property used > 50% in trade or business.",
            "Sec. 179(b)(1) annual limit ($1.16M 2024).",
            "Sec. 179(b)(2) phaseout begins at $2.89M of qualifying property purchases (2024).",
            "Sec. 179(b)(3) taxable-income limitation: cannot create or increase NOL.",
        ],
        [
            "Identify qualifying property placed in service during the year.",
            "Compute Sec. 179 expense election on Form 4562.",
            "Coordinate with Sec. 168(k) bonus for residual property.",
            "Track Sec. 179 carryforward if taxable-income limit binding.",
        ],
        [
            "IRC Sec. 179 (expensing).",
            "Treas. Reg. Sec. 1.179-1 (eligibility).",
            "Form 4562.",
        ],
        "State conformity to Sec. 179 limits varies; some states cap at lower amounts. Route to `tax-research-state-income`.",
        "Annual limit indexed for inflation; verify year-specific Rev. Proc.",
        [],
    ),
    (
        "section-1202-qsbs",
        "Section 1202 QSBS Exclusion",
        "IRC Sec. 1202",
        "Domestic C-corp shareholder excludes up to 100% of gain on sale of QSBS held > 5 years; cap is greater of $10M or 10x basis per issuer.",
        [
            "Domestic C-corp.",
            "Aggregate gross assets <= $50M (Sec. 1202(c)(2)(A)) at issuance and immediately after.",
            "Active business (Sec. 1202(e)) - 80% of assets in qualified trade or business.",
            "Not an excluded business (Sec. 1202(e)(3) - SSTB-like list, banking, insurance, hotels, restaurants, oil-and-gas).",
            "Stock acquired at original issuance after 8/10/1993 (100% exclusion only for stock acquired after 9/27/2010).",
            "Held > 5 years.",
        ],
        [
            "Document gross-assets test at issuance.",
            "Document active-business compliance annually.",
            "Track 5-year holding period from issuance.",
            "Report exclusion on Form 8949 with code Q.",
            "Consider Sec. 1045 rollover if reinvesting in replacement QSBS within 60 days.",
        ],
        [
            "IRC Sec. 1202 (QSBS exclusion).",
            "IRC Sec. 1202(c) (qualifying stock).",
            "IRC Sec. 1202(d) ($10M / 10x basis cap).",
            "IRC Sec. 1202(e) (active-business test).",
            "IRC Sec. 1045 (rollover).",
        ],
        "California and Pennsylvania do NOT conform to federal Sec. 1202 exclusion; state-tax remains. Route to `tax-research-state-income/CA.md` and `PA.md`.",
        "OBBBA (Pub. L. 119-XX, 2025) may have modified Sec. 1202 thresholds or cap. Route to `irc-section-lookup` for verification.",
        [],
    ),
    (
        "section-1045-rollover",
        "Section 1045 QSBS Rollover",
        "IRC Sec. 1045",
        "Taxpayer rolls over Sec. 1202 gain by reinvesting proceeds in replacement QSBS within 60 days, deferring gain recognition until eventual sale of replacement.",
        [
            "Original QSBS held > 6 months.",
            "Replacement is QSBS (must satisfy Sec. 1202(c) gross-assets and active-business tests).",
            "Reinvestment within 60 days of sale.",
        ],
        [
            "Sell original QSBS.",
            "Identify replacement QSBS.",
            "Reinvest proceeds within 60-day window.",
            "Elect Sec. 1045 rollover on tax return.",
            "Track basis carryover to replacement; eventual gain on replacement recognized at later sale (subject to its own Sec. 1202 if held > 5 years).",
        ],
        [
            "IRC Sec. 1045.",
            "IRC Sec. 1202 (underlying QSBS rules).",
        ],
        "CA / PA non-conformity flows through; state gain may be recognized on initial sale.",
        "",
        [],
    ),
    (
        "section-163j-rptb-election",
        "Section 163(j) Real-Property-Trade-or-Business Election",
        "IRC Sec. 163(j)(7)(B)",
        "Real-estate taxpayer irrevocably elects to be excepted from Sec. 163(j) interest-expense limitation in exchange for giving up Sec. 168(k) bonus on real property.",
        [
            "Trade or business is a real-property trade or business per Sec. 469(c)(7)(C).",
            "Sec. 163(j) limitation otherwise binding (3-year average gross receipts > $30M 2024).",
            "Willing to forgo Sec. 168(k) bonus on real property (must use 30 / 40-year ADS).",
        ],
        [
            "Confirm RPTB qualification under Sec. 469(c)(7)(C).",
            "Make irrevocable Sec. 163(j)(7)(B) election on timely-filed return.",
            "Switch real property to ADS (30 / 40-year recovery).",
            "Maintain election in subsequent years (irrevocable).",
        ],
        [
            "IRC Sec. 163(j) (interest limitation).",
            "IRC Sec. 163(j)(7)(B) (RPTB election).",
            "IRC Sec. 469(c)(7)(C) (definition of RPTB).",
            "IRC Sec. 168(g) (ADS).",
        ],
        "State conformity to Sec. 163(j) varies; some states decouple.",
        "ATI computation switched from EBITDA to EBIT post-2022 (TCJA Sec. 13301). OBBBA may have reverted - verify.",
        [],
    ),
    (
        "opportunity-zones",
        "Qualified Opportunity Zones",
        "IRC Sec. 1400Z-2",
        "Taxpayer reinvests capital gain into a Qualified Opportunity Fund (QOF) within 180 days; defers gain until 12/31/2026; original gain reduced 10% if held 5+ years; appreciation on QOF investment held 10+ years tax-free.",
        [
            "Eligible capital gain to invest.",
            "Investment within 180 days of gain recognition.",
            "QOF satisfies Sec. 1400Z-2(d) requirements (90% Opportunity Zone property test).",
        ],
        [
            "Realize eligible gain (capital gain only; NOT ordinary income).",
            "Within 180 days, invest in QOF.",
            "Elect Sec. 1400Z-2 deferral on Form 8949 with code Z.",
            "Hold QOF investment per holding-period schedule.",
            "Recognize deferred gain by 12/31/2026 (or earlier triggering event).",
            "Tax-free appreciation if held 10+ years.",
        ],
        [
            "IRC Sec. 1400Z-1 (QOZ designation).",
            "IRC Sec. 1400Z-2 (investment rules).",
            "Treas. Reg. Sec. 1.1400Z-2 (final regulations 2019-2020).",
            "Form 8949 (reporting).",
        ],
        "State conformity to Sec. 1400Z-2 deferral varies; CA, NC, MA, MS do not conform.",
        "TCJA Sec. 13823 created Sec. 1400Z-2; deferral recognition due 12/31/2026. OBBBA may have modified or extended - verify.",
        [],
    ),
    (
        "r-and-d-280c-election",
        "Section 41 R&D Credit + Section 280C Reduced Credit Election",
        "IRC Sec. 41; Sec. 280C(c)",
        "Taxpayer claims Sec. 41 research credit and elects under Sec. 280C(c)(2) to take a reduced credit (credit x (1 - corporate rate)) in exchange for keeping the Sec. 174 deduction whole.",
        [
            "Qualifying research activities under Sec. 41(d) four-part test.",
            "QREs computed per Sec. 41(b).",
            "Sec. 280C election made on timely-filed (with extensions) original return.",
        ],
        [
            "Conduct four-part test analysis (Sec. 41(d)).",
            "Compute QREs and credit (regular method or ASC).",
            "Elect Sec. 280C(c)(2) on Form 6765 if avoiding Sec. 174 add-back.",
            "Document business components for FAQ 25 amended-return scrutiny if relevant.",
            "Route to `predict-r-and-d-credit` for substantive analysis.",
        ],
        [
            "IRC Sec. 41 (R&D credit).",
            "IRC Sec. 41(d) (four-part test).",
            "IRC Sec. 280C(c) (deduction add-back).",
            "IRC Sec. 174 (R&E capitalization).",
            "Form 6765.",
        ],
        "State R&D credit interplay varies; many states have supplementary credits (CA, MN, NJ, etc.).",
        "Sec. 174 capitalization-and-amortization for years after 12/31/2021 (TCJA). OBBBA may have reverted to immediate expensing - verify.",
        [],
    ),
    # ---------- Real-estate / specialized (5) ----------
    (
        "like-kind-exchange-1031",
        "Section 1031 Like-Kind Exchange",
        "IRC Sec. 1031",
        "Taxpayer defers gain on disposition of real property held for productive use or investment by exchanging for like-kind real property; QI safe harbor; 45-day identification / 180-day completion.",
        [
            "Real property only (post-TCJA).",
            "Held for productive use in trade or business or for investment.",
            "Like-kind exchange (real property for real property).",
            "QI safe harbor: no constructive receipt by taxpayer.",
            "45-day identification + 180-day completion.",
        ],
        [
            "Engage qualified intermediary; review for disqualified-person status.",
            "Sell relinquished property; QI holds proceeds.",
            "Identify replacement property within 45 days.",
            "Close on replacement within 180 days.",
            "Compute boot recognition and basis carryover.",
            "Route to `predict-1031-qualification` for substantive analysis.",
        ],
        [
            "IRC Sec. 1031 (post-TCJA real-property only).",
            "Treas. Reg. Sec. 1.1031(a)-1 through Sec. 1.1031(k)-1.",
            "Treas. Reg. Sec. 1.1031(k)-1(g)(4) (QI safe harbor).",
            "Rev. Proc. 2000-37 (reverse exchanges).",
        ],
        "California Sec. 18032 imposes annual Form 3840 reporting until deferred gain is recognized in CA. PA did NOT conform pre-2023 for individuals.",
        "TCJA Sec. 13303 limited Sec. 1031 to real property (post-12/31/2017).",
        [],
    ),
    (
        "real-estate-professional",
        "Real-Estate Professional (REPS)",
        "IRC Sec. 469(c)(7)",
        "Taxpayer satisfies the two-pronged 750-hour / more-than-half-of-personal-services test to escape Sec. 469 passive-activity classification on rental real estate, deducting rental losses against ordinary income.",
        [
            "Per-spouse test (one spouse can qualify).",
            "More than half of personal services in real-property trades or businesses.",
            "More than 750 hours in real-property trades or businesses with material participation.",
            "Each property must satisfy Sec. 1.469-5T material participation OR Sec. 1.469-9(g) aggregation election in effect.",
            "Contemporaneous log discipline (Bailey, Hakkak).",
        ],
        [
            "Track hours by property and activity type with daily log.",
            "Aggregate via Sec. 1.469-9(g) election if applicable.",
            "Confirm material participation per property under Sec. 1.469-5T.",
            "File Form 4562 / Schedule E.",
            "Route to `predict-real-estate-pro` for substantive analysis.",
        ],
        [
            "IRC Sec. 469(c)(7).",
            "Treas. Reg. Sec. 1.469-5T (material participation).",
            "Treas. Reg. Sec. 1.469-9 (definitions, aggregation).",
            "Bailey v. Commissioner, T.C. Memo. 2001-296.",
            "Hakkak v. Commissioner, T.C. Memo. 2020-46.",
        ],
        "State PAL conformity varies; some states (CA) decouple from federal Sec. 469 framework.",
        "",
        [],
    ),
    (
        "str-loophole",
        "Short-Term-Rental \"Loophole\"",
        "Treas. Reg. Sec. 1.469-1T(e)(3)(ii)",
        "STR (average customer use <= 7 days) is NOT a 'rental activity' under Sec. 469; treated as trade or business; material-participation analysis under Sec. 1.469-5T applies without REPS.",
        [
            "Average customer rental period <= 7 days OR <= 30 days with significant personal services.",
            "Material participation per Sec. 1.469-5T.",
            "Active management substantiated.",
        ],
        [
            "Confirm average rental period via booking data.",
            "Manage actively (turnover, repairs, listing optimization).",
            "Maintain hour log per Sec. 1.469-5T tests (1, 3, 4 most commonly).",
            "Apply Sec. 168(k) bonus + cost-segregation for major depreciation.",
            "Route to `predict-real-estate-pro` for STR-specific analysis.",
        ],
        [
            "Treas. Reg. Sec. 1.469-1T(e)(3)(ii).",
            "Treas. Reg. Sec. 1.469-5T.",
        ],
        "State PAL conformity varies.",
        "",
        [],
    ),
    (
        "installment-sale-453",
        "Section 453 Installment Sale",
        "IRC Sec. 453",
        "Taxpayer sells property for deferred payments; gain recognized pro-rata as payments received under installment method.",
        [
            "Sale of property (NOT inventory; NOT publicly-traded securities for individuals).",
            "At least one payment received in a year after sale year.",
            "Sec. 453(b)(1) eligible.",
        ],
        [
            "Document sale terms with note / installment agreement.",
            "Compute gross profit ratio per Sec. 453.",
            "Recognize gain pro-rata as payments received.",
            "Sec. 453A interest charge if installment receivable > $5M (corporate) / $150K (individual at year-end).",
            "Form 6252 reporting.",
        ],
        [
            "IRC Sec. 453.",
            "IRC Sec. 453A (interest charge).",
            "Treas. Reg. Sec. 15A.453-1 (regulations).",
            "Form 6252.",
        ],
        "State conformity to federal Sec. 453 generally rolling.",
        "",
        ["Distinguish from monetized installment sale Dirty-Dozen scheme; legitimate Sec. 453 sales are different."],
    ),
    (
        "self-directed-ira-re",
        "Self-Directed IRA Real Estate",
        "IRC Sec. 408; Sec. 4975",
        "Self-directed IRA holds real estate as an asset; rental income / appreciation grows tax-deferred (or tax-free in Roth) within the IRA.",
        [
            "Self-directed IRA custodian.",
            "Real estate held in IRA's name.",
            "All expenses paid from IRA; all income flows to IRA.",
            "No prohibited transactions under Sec. 4975 (self-dealing, related-party rentals, personal use).",
        ],
        [
            "Open self-directed IRA at custodian.",
            "Fund IRA via contributions / rollovers.",
            "Direct custodian to purchase real estate.",
            "Manage carefully to avoid Sec. 4975 prohibited transactions.",
            "UBIT (Sec. 511) consideration if leveraged real estate (Sec. 514 UDFI).",
        ],
        [
            "IRC Sec. 408 (IRAs).",
            "IRC Sec. 4975 (prohibited transactions).",
            "IRC Sec. 511 (UBIT).",
            "IRC Sec. 514 (debt-financed property).",
        ],
        "State property tax may apply at the IRA-asset level.",
        "",
        ["High Sec. 4975 prohibited-transaction risk if not strictly managed; consequences include disqualification of entire IRA."],
    ),
    # ---------- Estate / gift (5) ----------
    (
        "annual-exclusion-gifting",
        "Section 2503(b) Annual Exclusion Gifting",
        "IRC Sec. 2503(b)",
        "Donor makes annual gifts of up to $19,000 (2025) per donee per year, free of gift tax and without using lifetime exclusion.",
        [
            "Present-interest gift required (Sec. 2503(b)(2)).",
            "Per-donee, per-year cap (verify year-specific Rev. Proc.).",
            "Spousal split permitted with consent (Sec. 2513).",
        ],
        [
            "Identify donees and gift amounts.",
            "Make gifts within calendar year.",
            "If gift in trust, use Crummey withdrawal power for present-interest qualification.",
            "Form 709 filing if other gifts trigger requirement (split-gift consent).",
        ],
        [
            "IRC Sec. 2503(b).",
            "IRC Sec. 2503(b)(2) (present interest).",
            "IRC Sec. 2513 (split gifts).",
            "Crummey v. Commissioner, 397 F.2d 82 (9th Cir. 1968).",
        ],
        "State gift-tax considerations: most states do not impose gift tax (CT is the major exception).",
        "",
        [],
    ),
    (
        "spousal-portability-dsue",
        "Spousal Portability / DSUE",
        "IRC Sec. 2010(c)(4)",
        "Surviving spouse uses predeceased spouse's unused basic exclusion amount via portability election on Form 706.",
        [
            "Predeceased spouse died with U.S. estate.",
            "Form 706 filed timely (or under Rev. Proc. 2022-32 5-year automatic extension for estates not required to file).",
            "Portability election made on the return.",
        ],
        [
            "If predeceased estate is large enough to require Form 706, file timely.",
            "If under threshold, use Rev. Proc. 2022-32 5-year extension.",
            "Mark 'FILED PURSUANT TO REV. PROC. 2022-32 TO ELECT PORTABILITY' on top of Form 706 if applicable.",
            "Surviving spouse's exclusion = own basic exclusion + DSUE.",
        ],
        [
            "IRC Sec. 2010(c)(4).",
            "Rev. Proc. 2022-32 (late portability relief).",
            "Treas. Reg. Sec. 20.2010-1(c) (anti-clawback).",
        ],
        "State estate tax may have its own portability framework or none at all (HI has portability; MD, MN, OR do not).",
        "Sec. 2010 basic exclusion sunsets 12/31/2025 absent extension; OBBBA may have modified - verify.",
        [],
    ),
    (
        "grat-zeroed-out",
        "\"Zeroed-Out\" GRAT (Grantor Retained Annuity Trust)",
        "IRC Sec. 2702",
        "Grantor transfers appreciating asset to GRAT; receives annuity for term computed using Sec. 7520 rate; remainder to family. Properly structured zeroed-out GRAT produces near-zero gift; appreciation above Sec. 7520 rate passes free of gift tax.",
        [
            "Asset expected to appreciate above Sec. 7520 rate.",
            "Grantor must survive the term (Sec. 2036(a)(1) inclusion if not).",
            "Annuity computed to equal PV of contribution at Sec. 7520 rate.",
        ],
        [
            "Engage estate-planning attorney for GRAT trust document.",
            "Compute Sec. 7520-rate-based annuity.",
            "Transfer asset to GRAT.",
            "Receive annuity payments during term.",
            "Remainder passes to beneficiaries at end of term.",
            "Walton v. Commissioner, 115 T.C. 589 (2000) approved zeroed-out GRAT.",
        ],
        [
            "IRC Sec. 2702 (special valuation).",
            "IRC Sec. 7520 (valuation rate).",
            "IRC Sec. 2036 (retained interests).",
            "Walton v. Commissioner, 115 T.C. 589 (2000).",
        ],
        "State estate tax may not recognize federal GRAT structure; check per-state file.",
        "",
        [],
    ),
    (
        "ilit",
        "Irrevocable Life Insurance Trust",
        "IRC Sec. 2042; Sec. 2702",
        "Grantor transfers life insurance policy or cash to ILIT; trust holds policy outside grantor's estate; death benefit paid to trust beneficiaries free of estate tax (if Sec. 2042 incidents-of-ownership avoided).",
        [
            "Grantor has life-insurance need.",
            "Willing to give up incidents of ownership over policy (Sec. 2042).",
            "Trust funded with annual gifts (Crummey withdrawal powers for present-interest qualification).",
            "Sec. 2035 3-year rule: existing policy transferred to ILIT pulled back into estate if grantor dies within 3 years.",
        ],
        [
            "Engage estate-planning attorney for ILIT trust document.",
            "Trustee acquires new policy on grantor's life (avoids Sec. 2035 3-year issue).",
            "Annual contributions to ILIT to fund premium; Crummey letters issued for present-interest qualification.",
            "Trustee pays premium from trust assets.",
            "Death benefit paid to trust beneficiaries.",
        ],
        [
            "IRC Sec. 2042 (life-insurance inclusion).",
            "IRC Sec. 2035 (3-year transfer rule).",
            "IRC Sec. 2503(b) (annual exclusion via Crummey).",
            "Crummey v. Commissioner, 397 F.2d 82 (9th Cir. 1968).",
        ],
        "State insurance regulation and ILIT compliance vary.",
        "",
        [],
    ),
    (
        "charitable-remainder-trust",
        "Charitable Remainder Trust (CRT/CRAT/CRUT)",
        "IRC Sec. 664",
        "Grantor transfers asset to CRT; receives annuity (CRAT) or unitrust (CRUT) for term or life; remainder to qualifying charity. Captures charitable deduction + income stream + capital-gain deferral on contributed assets.",
        [
            "Sec. 664 qualifying CRT structure.",
            "Annuity or unitrust paid to grantor / spouse / non-charitable beneficiaries for term (max 20 years) or life.",
            "Remainder of at least 10% of FMV at funding goes to qualifying Sec. 170 charity.",
            "5% minimum / 50% maximum unitrust / annuity rate.",
        ],
        [
            "Engage estate-planning attorney for CRT trust document.",
            "Transfer appreciated asset to CRT.",
            "CRT sells asset (no gain recognition at trust level).",
            "Trust pays annuity / unitrust to grantor; tax character per Sec. 664(b) tier system.",
            "Charitable remainder distribution at end of term.",
            "Sec. 170 deduction = PV of charitable remainder.",
        ],
        [
            "IRC Sec. 664 (CRT).",
            "IRC Sec. 170 (charitable deduction).",
            "Treas. Reg. Sec. 1.664-1 through Sec. 1.664-4.",
        ],
        "State charitable-contribution rules vary.",
        "",
        [],
    ),
]


HEADER_TEMPLATE = """# {title}

**Slug:** `{slug}`
**Primary IRC section:** {irc}

## Summary

{summary}

## Eligibility

{eligibility}

## Mechanics

{mechanics}

## Citations

{citations}

## State interplay

{state_notes}

## Recent legislation impact

{legislation_notes}

{warnings_section}
## Cross-references

- See `shared/strategy-list.md` for the canonical strategy index.
- See `references/index.md` for navigation across all 30 strategies.
- For substantive analysis on contested positions, route to the
  relevant prediction or research skill (see SKILL.md hard rules).
"""


def write_strategy(slug, title, irc, summary, eligibility, mechanics, citations, state_notes, legislation_notes, warnings):
    eligibility_md = "\n".join(f"- {item}" for item in eligibility)
    mechanics_md = "\n".join(f"{i+1}. {item}" for i, item in enumerate(mechanics))
    citations_md = "\n".join(f"- {item}" for item in citations)
    legislation_md = legislation_notes if legislation_notes else "No material recent-legislation impact identified at this draft."
    warnings_section = ""
    if warnings:
        warnings_section = "## Warnings\n\n" + "\n".join(f"- **WARNING:** {w}" for w in warnings) + "\n\n"

    content = HEADER_TEMPLATE.format(
        title=title,
        slug=slug,
        irc=irc,
        summary=summary,
        eligibility=eligibility_md,
        mechanics=mechanics_md,
        citations=citations_md,
        state_notes=state_notes,
        legislation_notes=legislation_md,
        warnings_section=warnings_section,
    )
    target = OUT / f"{slug}.md"
    target.write_text(content, encoding="utf-8")


def write_index():
    lines = ["# Strategy index — 30 entries\n",
             "Cross-references for the `planning-strategy-library` skill. See\n",
             "`shared/strategy-list.md` for the canonical list with metadata.\n\n",
             "## Strategies\n"]
    for slug, title, irc, *_ in STRATEGIES:
        lines.append(f"- [{title}]({'strategies/' + slug + '.md'}) (`{slug}`) - {irc}")
    target = OUT.parent / "index.md"
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    print(f"Writing {len(STRATEGIES)} strategy files to {OUT}...")
    for s in STRATEGIES:
        write_strategy(*s)
    write_index()
    print(f"Wrote {len(STRATEGIES)} strategy files + index.md.")


if __name__ == "__main__":
    main()
