# Treasury Decisions (TDs) vs codified Treasury Regulations

## What is a Treasury Decision?

A Treasury Decision (TD) is the Federal Register issuance vehicle
through which Treasury and the IRS promulgate or amend Treasury
Regulations. The TD itself is published in the Federal Register;
the codified rule appears in the eCFR as Title 26.

| Form | Authority status |
|---|---|
| Treasury Decision (Federal Register) | `TreasuryDecision` / `regulation` |
| Codified rule (eCFR §1.X-Y) | `TreasReg` / `regulation` |
| Proposed regulation (Federal Register, REG-XXXXXX) | `TreasReg` / `regulation` (note proposed status; not binding) |

Cite both the TD and the codified rule when relevant; the TD
provides the issuance date and preamble (which contains
explanatory text not codified).

## TD numbering

TDs are numbered sequentially. Recent examples:
- TD 9899 — final regulations on §163(j) (post-TCJA).
- TD 9908 — final regulations on §245A.
- TD 9947 — final regulations on §1061 carried-interest.
- TD 9956 — final regulations on §250 FDII.

The TD number does NOT correlate to the Reg section it amends;
multiple TDs can amend the same Reg, and a single TD can amend
multiple Regs.

## How to find the TD that promulgated a Reg

1. Navigate to the eCFR section.
2. Scroll to the bottom of the section to the "Authority" or
   "Source" annotation.
3. The annotation cites the original TD and any amending TDs.

Example: Treas. Reg. §1.199A-1 source annotation typically cites
TD 9847 (final QBI regs, 2019) and any subsequent amendments.

## How to find a TD in the Federal Register

1. Go to
   `https://www.federalregister.gov/agencies/internal-revenue-service`.
2. Search by TD number (e.g., "TD 9899").
3. The Federal Register entry includes:
   - Preamble (explanatory commentary).
   - Effective date.
   - Applicability date (often retroactive).
   - Text of the regulation.

## Preamble vs codified text

The TD's preamble contains:
- Explanation of the rule's purpose.
- Discussion of comments received on the proposed reg.
- Effective and applicability dates.
- Examples and clarifications NOT codified.

The codified text (eCFR) contains:
- The operative regulatory rule.
- Examples that are part of the rule itself.

For interpretive questions, the preamble is persuasive evidence
of Treasury's intent. Cite the preamble as part of the TD
citation:

```json
{
  "authority_type": "TreasuryDecision",
  "citation": "TD 9899, 85 Fed. Reg. 56846 (Sept. 14, 2020), preamble at Section IV",
  "url": "https://www.federalregister.gov/...",
  "retrieved_date": "[YYYY-MM-DD]",
  "quoted_text": "[verbatim ≤75 words from preamble]",
  "weight": "regulation"
}
```

## Proposed regulations

Proposed regs are published in the Federal Register but not in
eCFR. They are NOT binding; taxpayers may rely on them under
§1.6662-3(b)(3) reasonable-basis if the proposed reg is
substantively reasonable, but the IRS may issue final regs that
differ.

Proposed reg numbering: REG-XXXXXX-YY (where YY is year suffix).

For high-stakes positions, distinguish between:
- Reliance on a proposed reg as substantial authority (sometimes
  appropriate under §6662(d)(2)(B)(i)).
- Reliance on a proposed reg as the closest authority (less
  comfortable; consider Form 8275 disclosure).

## Temporary regulations

Temporary regulations (suffix "T") are issued under §7805(e),
have force of law for 3 years from issuance, and must be paired
with a contemporaneous Notice of Proposed Rulemaking.

Temporary regs are codified in eCFR alongside final regs.

| Status | eCFR designation |
|---|---|
| Final | §1.X-Y |
| Temporary | §1.X-YT |
| Proposed | (Federal Register only — not eCFR) |

## Authority hierarchy

Per `shared/authority-hierarchy.md`:

| Reg type | Tier | Weight | Notes |
|---|---|---|---|
| Final TreasReg (codified) | 3 | regulation | Skidmore review post-Loper Bright |
| Temporary TreasReg | 3 | regulation | Same; expires 3 years from issuance unless replaced |
| Proposed TreasReg | (not authority) | persuasive_non_authority at most | Reliance possible under §1.6662-3(b)(3) |
| Treasury Decision (issuance) | 3 | regulation | Cite alongside codified rule |

## Loper Bright posture

Loper Bright Enterprises v. Raimondo, 144 S. Ct. 2244 (2024)
ended Chevron deference. For Treasury Regulations interpreting
ambiguous statutory provisions:

1. Set `chevron_replaced: true` in the citation entry.
2. Note that courts now review under Skidmore framework
   (thoroughness, reasoning validity, consistency, persuasiveness).
3. The Reg remains in force unless amended or superseded; courts
   will defer to the Reg's interpretation if persuasive.
4. For new judicial challenges to existing Regs, the analysis is
   fact-intensive.

For Treasury Regulations interpreting unambiguous statute, Loper
Bright is less impactful — the Reg simply implements the statute.

## Practitioner audit-defense file

- [ ] Treasury Reg cited with eCFR-current text.
- [ ] Reg status confirmed: final / temporary / proposed.
- [ ] TD that promulgated or amended the Reg identified.
- [ ] Effective date / applicability date verified.
- [ ] Loper Bright posture documented for ambiguous-statute regs.
- [ ] Federal Register IRS feed checked for subsequent TDs that
  may have amended the Reg.

## Common practitioner errors

- Citing a Reg by section without confirming it is FINAL (not
  temporary or proposed).
- Quoting Reg text from a treatise or commercial database without
  verifying against eCFR.
- Ignoring the TD that promulgated the Reg (the TD's preamble
  often contains crucial interpretive context).
- Failing to flag `chevron_replaced: true` post-Loper Bright.
- Treating temporary regs as if they were final (different
  authority dynamics; Treas. Reg. §1.7805-3(c) requires NPRM).
- Treating proposed regs as binding authority.
