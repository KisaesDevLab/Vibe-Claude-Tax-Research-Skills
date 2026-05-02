#!/usr/bin/env python3
"""
Parse the cross-reference table from
skills/planning-strategy-library/references/strategy-cross-reference.md
and emit machine-readable JSON at
skills/planning-strategy-library/references/strategy-relationships.json.

Reads the markdown table rows of the form:
| ID | Name | Combines with | Conflicts with | Mutually exclusive with |
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "skills" / "planning-strategy-library" / "references" / "strategy-cross-reference.md"
OUT = ROOT / "skills" / "planning-strategy-library" / "references" / "strategy-relationships.json"

# Mapping of ID -> filename slug for the addendum strategies (Parts 2-10).
# Strategies #1-#7 have no detail file (Part 1 not delivered) and are
# emitted with "detail_file": null.
ADDENDUM_SLUGS = {
    8: "group-health-insurance",
    9: "grouping-of-activities",
    10: "health-insurance-s-corp",
    11: "hra-merp",
    12: "bonus-and-section-179-depreciation",
    13: "maximize-business-deductions",
    14: "meals-and-entertainment",
    15: "nol-carryback-carryforward",
    16: "passive-income-pigs",
    17: "ptet-salt-workaround",
    18: "prepayment-of-expense",
    19: "qbi-deduction",
    20: "real-estate-professional-extended",
    21: "reasonable-comp-corp-owners",
    22: "reimbursement-business-expenses",
    23: "reimbursement-depreciation-s-corp-vehicle",
    24: "augusta-rule-280a-g",
    25: "rental-strategies",
    26: "short-term-rental",
    27: "startup-cost-optimization",
    28: "de-minimis-safe-harbor",
    29: "deferred-sales-trust",
    30: "worthless-stock-ordinary-loss",
    31: "c-corp-dividends",
    32: "capital-gain-offsets",
    33: "installment-sale",
    34: "qoz-reinvestment",
    35: "c-corp-state-tax-savings",
    36: "ev-credits",
    37: "late-penalties-interest",
    38: "misc-tax-credits",
    39: "r-and-d-credit-strategy",
    40: "state-tax-savings",
    41: "cost-segregation-extended",
    42: "c-corp-misc-deductions",
    43: "section-1202-qsbs-extended",
    44: "corporate-owned-vul",
    45: "section-127-education-assistance",
    46: "gifting-stock",
    47: "income-shifting-to-c-corp",
    48: "income-shifting-family-member",
    49: "hiring-kids",
    50: "wages-spouse-parents",
    51: "charitable-donation-appreciated",
    52: "charitable-llc",
    53: "charitable-planning",
    54: "donor-advised-fund",
    55: "family-limited-partnership",
    56: "unreimbursed-partnership-expenses",
    57: "529-savings-plan",
    58: "adoption-incentives",
    59: "amend-missed-deductions",
    60: "college-student-strategies",
    61: "education-credits",
    62: "flexible-spending-account",
    63: "hsa-optimization",
    64: "individual-planning-ideas",
    65: "married-filing-separate",
    66: "penalty-abatement",
    67: "primary-home-sale-exclusion",
    68: "employee-stock-options",
    69: "niit-minimization",
    70: "series-i-bond",
    71: "employer-benefit-package-review",
    72: "backdoor-roth-extended",
    73: "defined-benefit-cash-balance",
    74: "life-insurance-retirement-plan",
    75: "401k-pretax",
    76: "sep-ira",
    77: "simple-ira",
    78: "qcd",
    79: "roth-ira-contributions",
    80: "roth-ira-conversion",
    81: "sep-ira-self-employed",
    82: "solo-401k-employer-contributions",
    83: "traditional-ira-contributions",
    84: "accountable-plan-self-employed",
    85: "business-vehicle-self-employed",
    86: "choice-of-entity-se-tax",
    87: "health-insurance-self-employed",
    88: "home-office-deduction-self-employed",
    89: "bonus-179-depreciation-self-employed",
    90: "minimize-self-employment-tax",
    91: "prepayment-expense-self-employed",
    92: "split-entity-operations-vs-re",
    93: "de-minimis-safe-harbor-self-employed",
    94: "hiring-kids-self-employed",
}

ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]*)\s*\|\s*([^|]*)\s*\|\s*([^|]*)\s*\|\s*$"
)

def parse_refs(cell: str) -> list[str]:
    cell = cell.strip()
    if not cell or cell.lower() == "none" or cell.lower().startswith("none "):
        return []
    return [p.strip() for p in cell.split(",") if p.strip()]

def main() -> int:
    text = SRC.read_text(encoding="utf-8")
    rows: dict[int, dict] = {}
    for line in text.splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        sid = int(m.group(1))
        name = m.group(2).strip().rstrip("*").rstrip()
        # Strip the "(addendum Part 1 not delivered)" annotation
        name = re.sub(r"\s*\*\(addendum Part 1 not delivered\)\*\s*$", "", name)
        rows[sid] = {
            "id": sid,
            "name": name,
            "detail_file": ADDENDUM_SLUGS.get(sid),
            "delivered": sid >= 8,
            "combines_with": parse_refs(m.group(3)),
            "conflicts_with": parse_refs(m.group(4)),
            "mutually_exclusive_with": parse_refs(m.group(5)),
        }
    out = {
        "version": "1.0.0",
        "source": "skills/planning-strategy-library/references/strategy-cross-reference.md",
        "note": "Strategies #1-#7 from the addendum's Part 1 were not delivered; their rows are present for navigability but detail_file is null.",
        "strategies": [rows[k] for k in sorted(rows.keys())],
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    delivered = sum(1 for s in out["strategies"] if s["delivered"])
    skipped = sum(1 for s in out["strategies"] if not s["delivered"])
    print(f"Wrote {OUT.relative_to(ROOT)}")
    print(f"  Strategies: {len(out['strategies'])} total ({delivered} delivered, {skipped} skipped)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
