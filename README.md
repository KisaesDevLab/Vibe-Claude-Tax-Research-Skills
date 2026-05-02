# Vibe CPA Skills

A Claude Skills pack for U.S. CPAs. 37+ skills covering federal
research, prediction, return summary, planning (incl. multi-year
sunset / phase-out tracking), state research for all 50 states +
DC, IRC + Public Law lookup with USC Classification Table workflow,
penalty / interest computation, due-date calculation, and a 30-
strategy planning library — all with strict citation discipline,
AICPA SSTS / Circular 230 compliance scaffolding, and post-Loper
Bright Skidmore-review caveats for Treasury Regulations.

> **Beta status.** This is `v1.0.0-beta`. State per-state files
> ship as `status: stub` and require practitioner promotion before
> use in HIGH-confidence engagements. See
> [docs/state-stub-promotion.md](docs/state-stub-promotion.md).

## Why this exists

Commercial CPA tools (Holistiplan, Blue J Tax, TaxPlanIQ, CPA
Pilot, TaxGPT) are subscription-only and opaque about citation
discipline. Vibe CPA Skills is a publicly-distributed alternative
built from primary sources only:

- Direct citation to IRC sections via USLM canonical URLs.
- Direct citation to Treasury Regulations via eCFR.
- Public-Law-to-USC workflow per `shared/legislation-tracking.md`.
- Free-source mitigation of citator gaps (DAWSON Today's Opinions,
  Federal Register IRS feed).
- AICPA SSTS / Circular 230 verification checklist on every
  output.

## Installation

### Claude Code

```bash
claude /plugin marketplace add KisaesDevLab/vibe-claude-tax-research-skills
claude /plugin install vibe-cpa-pack@kisaes-cpa-skills
```

See [docs/install-claude-code.md](docs/install-claude-code.md).

### claude.ai web app

Per-skill ZIP upload. See
[docs/install-claude-ai.md](docs/install-claude-ai.md).

## Skills index

### Always-on dispatcher (1)

| Skill | Description |
|---|---|
| [cpa-pack-index](skills/cpa-pack-index) | Always-on dispatcher; routes user input to the appropriate specialist skill. |

### Research (5 federal + 2 state shell + 1 estate-gift)

| Skill | Coverage |
|---|---|
| [tax-research-federal](skills/tax-research-federal) | Federal income-tax research with full authority hierarchy walk |
| [tax-research-entity](skills/tax-research-entity) | Subchapter C / K / S routing with check-the-box |
| [tax-research-payroll](skills/tax-research-payroll) | FICA / FUTA / TFRP / withholding |
| [tax-research-international](skills/tax-research-international) | Inbound / outbound / treaty / CFC / GILTI / FDII / FBAR |
| [tax-research-procedure](skills/tax-research-procedure) | Audits / SOL / Tax Court / CDP / DOJ Tax |
| [tax-research-state-income](skills/tax-research-state-income) | All 50 states + DC; state-router protocol |
| [tax-research-state-salesuse](skills/tax-research-state-salesuse) | All 50 states + DC; sales / use; Wayfair nexus |
| [tax-research-estate-gift](skills/tax-research-estate-gift) | §§ 2010 / 2503 / 2522 / 2055 / 2056 + GST §§ 2611 / 2632 |

### Prediction (12)

| Skill | Question |
|---|---|
| [predict-worker-classification](skills/predict-worker-classification) | Employee vs. contractor (federal + state ABC test) |
| [predict-hobby-loss](skills/predict-hobby-loss) | § 183 nine factors + presumption |
| [predict-reasonable-comp](skills/predict-reasonable-comp) | Watson framework + multi-factor |
| [predict-real-estate-pro](skills/predict-real-estate-pro) | § 469(c)(7) REPS qualification |
| [predict-material-participation](skills/predict-material-participation) | Seven § 1.469-5T tests |
| [predict-qbi-eligibility](skills/predict-qbi-eligibility) | § 199A QBI / SSTB / W-2 / UBIA |
| [predict-1031-qualification](skills/predict-1031-qualification) | § 1031 like-kind + 45/180 + QI safe harbor |
| [predict-economic-substance](skills/predict-economic-substance) | § 7701(o) + § 6662(b)(6) strict liability |
| [predict-debt-vs-equity](skills/predict-debt-vs-equity) | § 385 + circuit-specific multi-factor |
| [predict-innocent-spouse](skills/predict-innocent-spouse) | § 6015(b)/(c)/(f) + Rev. Proc. 2013-34 |
| [predict-reasonable-cause](skills/predict-reasonable-cause) | FTA + § 6651 / § 6662 + Boyle / McMahan |
| [predict-r-and-d-credit](skills/predict-r-and-d-credit) | § 41 four-part + ASC + § 174 capitalization |

### Summary + notice (3)

| Skill | Description |
|---|---|
| [return-summary-1040](skills/return-summary-1040) | Form 1040 line keys + red-flag catalog |
| [return-summary-entity](skills/return-summary-entity) | 1120 / 1120-S / 1065 line keys + red-flag catalog |
| [notice-response](skills/notice-response) | CP / Letter / LT triage with response templates |

### Planning (4 + 3 catalog/elections)

| Skill | Description |
|---|---|
| [planning-actions-1040](skills/planning-actions-1040) | Individual planning checklist (17 categories) |
| [planning-actions-entity](skills/planning-actions-entity) | Entity planning checklist (16 categories) |
| [planning-multi-year](skills/planning-multi-year) | Sunset / phase-out / phase-in calendar |
| [planning-strategy-library](skills/planning-strategy-library) | 30 curated + 87 extended-reference addendum strategies (#8–#94) with cross-reference matrix |
| [s-corp-strategy-catalog](skills/s-corp-strategy-catalog) | 10 S-corp strategies mapped to Form 1120-S lines |
| [schedule-c-strategy-catalog](skills/schedule-c-strategy-catalog) | 10 Schedule C / SE strategies mapped to Schedule C / Form 8829 lines |
| [tax-elections-library](skills/tax-elections-library) | 24 tax elections with authority, deadlines, and sample language |

### Utilities (5)

| Skill | Description |
|---|---|
| [irc-section-lookup](skills/irc-section-lookup) | USC + Public-Law-to-USC workflow per `shared/legislation-tracking.md` |
| [treas-reg-lookup](skills/treas-reg-lookup) | eCFR resolution + TD identification + Loper Bright caveat |
| [form-line-explainer](skills/form-line-explainer) | Form / line / box / schedule explainer |
| [due-date-calculator](skills/due-date-calculator) | §§ 6072/6075/6213/6320/6330/6511/6654/6655/7503 |
| [penalty-interest-calc](skills/penalty-interest-calc) | §§ 6601/6621/6651/6654/6655/6662/6663/6672 |

### Compliance (1)

| Skill | Description |
|---|---|
| [compliance-ssts-circular230](skills/compliance-ssts-circular230) | SSTS § 1.1 / § 2.3 + Circular 230 §§ 10.22/10.35/10.37 walk |

## State coverage

All 50 states + DC = 51 jurisdictions. Each is documented in:

- `skills/tax-research-state-income/references/states/<XX>.md`
- `skills/tax-research-state-salesuse/references/states/<XX>.md`

102 state-stub files total. Each carries a `status` field:
`stub` (default) → `draft` → `reviewed` → `verified`.

State coverage matrix:

| Code | State | Income tax | Sales tax | Notes |
|---|---|---|---|---|
| AL | Alabama | yes | yes + SALT-J locals | |
| AK | Alaska | no | local-only via ARSSTC | |
| AZ | Arizona | yes | yes + city TPT | |
| AR | Arkansas | yes | yes | |
| CA | California | yes | yes via CDTFA | AB5; PTET; FTB |
| CO | Colorado | yes | yes + ~70 home-rule cities | |
| CT | Connecticut | yes | yes | DRS |
| DE | Delaware | yes | no (gross receipts) | |
| DC | District of Columbia | yes | yes | |
| FL | Florida | no | yes | |
| GA | Georgia | yes | yes | |
| HI | Hawaii | yes | yes (GET) | DOTAX |
| ID | Idaho | yes | yes | |
| IL | Illinois | yes (flat) | yes + local | IDOR |
| IN | Indiana | yes | yes | |
| IA | Iowa | yes | yes | |
| KS | Kansas | yes | yes | |
| KY | Kentucky | yes | yes | |
| LA | Louisiana | yes | yes + parish | |
| ME | Maine | yes | yes | |
| MD | Maryland | yes | yes | Comptroller |
| MA | Massachusetts | yes + 4% surtax >$1M | yes | DOR |
| MI | Michigan | yes | yes | |
| MN | Minnesota | yes | yes | |
| MS | Mississippi | yes | yes | |
| MO | Missouri | yes | yes | |
| MT | Montana | yes | no | |
| NE | Nebraska | yes | yes | |
| NV | Nevada | no | yes | |
| NH | New Hampshire | no (I&D repealed 2025) | no | M&R tax |
| NJ | New Jersey | yes | yes | BAIT PTET |
| NM | New Mexico | yes | yes (GRT) | |
| NY | New York | yes | yes | NYS DTF; convenience-rule |
| NC | North Carolina | yes | yes | |
| ND | North Dakota | yes | yes | |
| OH | Ohio | yes | yes | |
| OK | Oklahoma | yes | yes | |
| OR | Oregon | yes + transit tax | no | |
| PA | Pennsylvania | yes (flat) | yes + local EIT | |
| RI | Rhode Island | yes | yes | |
| SC | South Carolina | yes | yes | |
| SD | South Dakota | no | yes | Wayfair originator |
| TN | Tennessee | no (Hall repealed) | yes | F&E tax for entities |
| TX | Texas | no | yes | margin tax for entities |
| UT | Utah | yes | yes | |
| VT | Vermont | yes | yes | |
| VA | Virginia | yes | yes | |
| WA | Washington | cap-gains-only | yes + B&O | |
| WV | West Virginia | yes | yes | |
| WI | Wisconsin | yes | yes | |
| WY | Wyoming | no | yes | |

## Authority discipline

Every citation in the JSON sidecar `authorities[]` array includes:
`authority_type`, `citation`, `url`, `retrieved_date`,
`quoted_text` (≤75 words verbatim), `weight`. See
[shared/citation-discipline.md](shared/citation-discipline.md) for
the full discipline.

Authority weighting follows Treas. Reg. § 1.6662-4(d)(3)(iii). See
[shared/authority-hierarchy.md](shared/authority-hierarchy.md).

When a primary source is unreachable, skills emit the sentinel
`[CITATION NEEDED — search: <query>]` rather than fabricating.

## Compliance posture

Every output carries an SSTS / Circular 230 verification
checklist:

- AICPA SSTS § 1.1 (realistic possibility), § 2.3 (estimates).
- Circular 230 § 10.22 (diligence), § 10.35 (competence), § 10.37
  (written advice / reasonable-practitioner standard).
- Form 8275 / 8275-R / 8886 disclosure flagging.

For high-stakes positions, the negative-treatment-review residual
practitioner responsibility is flagged: free-source citation
discipline cannot detect implicit overrules with the same coverage
as a commercial citator (KeyCite, Shepard's, BCite, Citator 2nd).

## Public-Law tracking

The `irc-section-lookup` skill implements the 6-step Public-Law-
to-USC workflow per
[shared/legislation-tracking.md](shared/legislation-tracking.md):

1. Resolve popular name → Public Law via Popular Name Tool.
2. Pull Classification Tables for affected USC sections.
3. Verify each affected section's current text via USLM.
4. Locate JCT Bluebook / committee reports / Greenbook / CBO.
5. Check Federal Register IRS feed for proposed regs / TDs.
6. Optional Cite Checker.

Common Public Laws covered: TCJA (Pub. L. 115-97), CARES
(Pub. L. 116-136), ARPA (Pub. L. 117-2), IIJA (Pub. L. 117-58),
CHIPS (Pub. L. 117-167), IRA (Pub. L. 117-169), SECURE 2.0
(Pub. L. 117-328 div. T), OBBBA (Pub. L. 119-XX, 2025).

See [docs/legislation-tracking-howto.md](docs/legislation-tracking-howto.md).

## Examples

The `examples/` directory contains worked example prompts and
expected JSON sidecars for representative use cases:

- [research-federal](examples/research-federal) — § 199A QBI for
  CPA solo practitioner.
- [predict-worker-classification](examples/predict-worker-classification)
  — California rideshare driver.
- [return-summary-1040](examples/return-summary-1040) — 1040
  with QBI red flag.
- [notice-response](examples/notice-response) — CP2000 disagree.
- [state-research-CA](examples/state-research-CA) — California
  PTET deadline.
- [state-research-NY-convenience-rule](examples/state-research-NY-convenience-rule)
  — NY convenience-of-employer for NJ remote worker.
- [legislation-tracking-OBBBA](examples/legislation-tracking-OBBBA)
  — OBBBA impact on § 199A via Public-Law-to-USC workflow.

## Validation

```bash
# Full validation:
./scripts/validate.sh full

# Phase-specific:
./scripts/validate.sh phase 6

# Skill-specific:
./scripts/validate.sh skill <slug>

# Eval harness:
./scripts/run-evals.sh full
```

CI runs `validate.sh full` and `run-evals.sh full` on every PR.
URL-liveness check is gated by `SKIP_URL_CHECK=1` for offline /
sandboxed development.

## License

[Business Source License 1.1](LICENSE) (BUSL-1.1). Free for
non-commercial use; commercial use requires a license from
Kisaes LLC.

## Disclaimer

[DISCLAIMER.md](DISCLAIMER.md). This pack is informational only;
not tax, legal, or accounting advice. Consult a licensed
practitioner for engagement-specific advice.

## Contributing

[CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome. Strong preference
for state-stub promotions (`stub` → `draft` → `reviewed` →
`verified`) and additional eval cases.

## Author

Kurt Kohrumel ([@KisaesDevLab](https://github.com/KisaesDevLab)),
CPA, founder of Kisaes LLC and the Vibe family of self-hosted CPA
software (sibling repo: Vibe-Trial-Balance).

## Changelog

[CHANGELOG.md](CHANGELOG.md). Versions follow semver. Current:
`v1.0.0-beta`.
