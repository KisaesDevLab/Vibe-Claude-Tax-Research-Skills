---
name: treas-reg-lookup
description: |
  Resolves Treasury Regulation references to canonical eCFR text and
  identifies the Treasury Decision (TD) that promulgated or last
  amended the regulation. Distinguishes final / temporary / proposed
  regulations and applies the post-Loper Bright Skidmore-review
  caveat for regulations interpreting ambiguous statutes. Use when
  the user asks "what does Treas. Reg. §X say", "look up Reg. §X",
  "is this a final or temporary reg", "TD XXXX", "Treasury
  Decision", or "is this reg post-Chevron". Make sure to use this
  skill whenever the user mentions a Treasury Regulation by number,
  a Treasury Decision number, or asks about regulation status
  (final / temporary / proposed).
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# treas-reg-lookup — Treasury Regulation resolution

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/treasury-decisions.md` — distinguishing TDs from
   codified Treas. Reg. (per BUILD_PLAN).

## Operative authority

- Treasury Regulations at eCFR Title 26:
  https://www.ecfr.gov/current/title-26
- Treasury Decisions in Federal Register:
  https://www.federalregister.gov/agencies/internal-revenue-service
- Loper Bright Enterprises v. Raimondo, 144 S. Ct. 2244 (2024) —
  ended Chevron deference.
- Skidmore v. Swift & Co., 323 U.S. 134 (1944) — replacement
  framework.

## Workflow

### 1. Intake

- Treasury Regulation citation (e.g., "Treas. Reg. §1.199A-5(b)
  (2)(xiv)") OR Treasury Decision number (e.g., "TD 9899") OR
  topical query.

### 2. eCFR resolution

1. Navigate eCFR Title 26 at
   `https://www.ecfr.gov/current/title-26`.
2. The eCFR organizes Treasury Regulations by part, subpart,
   section.
3. Find the cited section and pull the operative subsection /
   paragraph.
4. Identify the regulation type:
   - Final regulation: numbered §1.X-Y (no "T" suffix).
   - Temporary regulation: numbered §1.X-YT.
   - Proposed regulation: not in eCFR; in Federal Register.
5. Cite as `TreasReg` with `weight: regulation`. Include
   `quoted_text` (≤75 words), `pin_cite`, `retrieved_date`.

### 3. Treasury Decision identification

Each Treasury Regulation in eCFR has an "Authority" or
"Source" annotation citing the TD that promulgated or amended
the regulation.

To find the TD:
1. In the eCFR section view, scroll to the "Authority" or
   "Source" annotation.
2. Note the TD number(s).
3. Optionally, look up the TD in the Federal Register at
   `https://www.federalregister.gov/agencies/internal-revenue-service`.

### 4. Post-Loper Bright posture

If the regulation interprets an ambiguous statutory provision,
flag `chevron_replaced: true` in the citation entry. Note that
post-Loper Bright (June 2024), courts review regulations under
Skidmore: thoroughness, reasoning validity, consistency,
persuasiveness.

For pre-Loper Bright Treasury Regs that previously commanded
Chevron deference, the practitioner should:
- Continue to cite the Reg as authority (it remains in force
  unless amended or superseded).
- Note the Skidmore-review framework.
- Consider whether a new judicial challenge may succeed under
  Loper Bright.

### 5. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`. Cite
the Treasury Reg with `weight: regulation` and
`chevron_replaced: true` when the Reg interprets ambiguous
statute.

If a Treasury Decision is also cited (separate from the codified
Reg), tag as `TreasuryDecision` with `weight: regulation`.

## Hard rules

- Always pull current eCFR text; do not rely on cached or
  paraphrased Reg text.
- Always identify regulation status: final / temporary /
  proposed.
- Always set `chevron_replaced: true` when the Reg interprets
  ambiguous statute (post-Loper Bright).
- For proposed regulations, tag `weight: regulation` but note in
  the sidecar narrative that it is proposed (not yet binding;
  taxpayer may rely under §1.6662-3(b)(3) reasonable basis).
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Note Skidmore-review framework for
post-Loper Bright Treasury Reg reliance.
