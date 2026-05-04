# State-board overlay — when state rules are stricter than AICPA

CPAs are licensed by state boards of accountancy, not by the AICPA.
State boards adopt their own rules of professional conduct and may
impose stricter independence, fee, conflict, or competence
requirements than the AICPA Code. When an engagement state is
supplied, the `compliance-aicpa-code` skill must consult the
applicable state board's rules and apply the stricter rule.

## Workflow

1. Capture the engagement state (`engagement_state` in intake).
2. Look up the state board URL in
   `shared/sources.json -> state_boards_of_accountancy.boards.<XX>`.
3. Check the known-stricter list below for hot zones. If the state
   is on the list, apply the stricter rule and emit
   `state_overlay_required: true` in the sidecar.
4. If the engagement state is not on the known-stricter list, the
   default is to apply the AICPA Code; emit
   `state_overlay_required: false` and note in the band rationale
   that a state-rule confirmation is the practitioner's residual
   responsibility.

## Known stricter states (high-confidence)

### California (Board of Accountancy)
- **URL**: https://www.dca.ca.gov/cba — laws and rules at
  https://www.dca.ca.gov/cba/laws-and-rules/index.shtml.
- **Independence**: CA Bus. & Prof. Code §§ 5070–5095; CCR Title 16
  §§ 50–99. Notably:
  - California Accountancy Regulations §62–§65 align with AICPA on
    most points but the Board has historically interpreted certain
    nonattest services more strictly.
  - SB 691 / AB 5 worker-classification overlay affects firm
    contractor relationships.
- **Indemnification limit**: Cal. Bus. & Prof. Code §5063.1 —
  restrictions on indemnification clauses in engagement letters.
- **Continuing education**: 80 hours / 2 years; 24 hours of A&A or
  fraud for licensees performing audits.

### New York (Board for Public Accountancy)
- **URL**: https://www.op.nysed.gov/professions/certified-public-accountants
- **Independence**: NY Education Law §7400–§7409; 8 NYCRR Part 29 (general
  rules of professional misconduct) + Subpart 70-1 (CPA-specific).
- **Mobility**: NY does not have a "no-notice" mobility law to the
  same extent as some states; out-of-state CPAs serving NY clients
  on attest engagements should confirm registration requirements.
- **CPE**: 40 hours / year; ethics required.

### Texas (State Board of Public Accountancy)
- **URL**: https://www.tsbpa.texas.gov — rules at
  https://www.tsbpa.texas.gov/general/board-rules.html.
- **Independence**: 22 TAC §§ 501.70–501.80 (rules of professional
  conduct); §501.73 specifically on independence.
  - TX Board's interpretation of nonattest services has historically
    been more conservative than AICPA on certain bookkeeping
    arrangements.
- **Practice mobility**: TX has practice privilege provisions but
  out-of-state firms doing TX attest work need to confirm firm
  registration with the Board.
- **CPE**: 120 hours / 3 years; 4 hours of ethics each reporting period.

## Other state overlays (research as needed)

The following states have rules that may diverge from AICPA on
specific points; the practitioner should confirm by reading the
state board's rules at the URL in `shared/sources.json`:

- **Florida** (DBPR-CPA): https://www.myfloridalicense.com/DBPR/certified-public-accounting
- **Illinois** (IDFPR): https://idfpr.illinois.gov/profs/cpa.html
  - Rules on attest engagements with privity-related limitations.
- **Massachusetts** (Board of Public Accountancy):
  https://www.mass.gov/orgs/board-of-public-accountancy
- **New Jersey** (Board of Accountancy):
  https://www.njconsumeraffairs.gov/acc
  - Indemnification restrictions on attest engagements.
- **Washington** (Board of Accountancy): https://acb.wa.gov

## Mobility and out-of-state engagements

The Uniform Accountancy Act mobility provisions (now adopted in all
55 jurisdictions in some form) generally permit a licensee in one
state to practice across state lines without additional licensure
when:
- The CPA holds a license in the principal-place-of-business state.
- The other state has a substantially-equivalent licensure standard.
- The CPA does NOT hold an office in the other state (firm
  registration may be required in some cases).

For attest engagements in another state, **firm registration** is a
separate question from individual mobility and varies by state.
NASBA's licensure database
(https://nasba.org/licensure/nasbalicensing) is the canonical lookup.

## Output requirements

When this overlay is invoked, the JSON sidecar MUST populate:
- `task.engagement_state`: the 2-letter state code.
- `state_overlay_required`: true if a stricter state rule applies;
  false otherwise.
- An `authorities[]` entry citing the state board rule with
  `authority_type: StateBoardRule` and `weight: binding_on_member`.

## Authority

State board rules are binding on licensees in that state. Cite the
state board's rule with the canonical URL from
`shared/sources.json -> state_boards_of_accountancy.boards.<XX>` and
pin-cite to the specific rule (e.g., "22 TAC §501.73(b)" for Texas).
The AICPA Code is the floor; state rules can only impose additional
requirements, never relax AICPA.
