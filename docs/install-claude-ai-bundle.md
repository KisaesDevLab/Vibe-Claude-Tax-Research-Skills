---
title: "Vibe CPA Pack for claude.ai"
subtitle: "Installation and usage guide — single-skill bundle (46 workflows)"
---

# What this is

`vibe-cpa-pack.zip` is the whole Vibe CPA Skills pack packaged as
**one** claude.ai skill. You no longer upload 46 separate skills. The
bundle has:

- **One entry point** (`SKILL.md`). This is the pack dispatcher. It
  reads your request and picks the right specialist workflow.
- **45 specialist workflows** (`skills/<name>/WORKFLOW.md`), each with
  its reference files. These cover federal, entity, payroll,
  international, procedure, estate/gift, and 51-jurisdiction state
  research; predictions; return summaries; notice responses; planning
  and the strategy library; elections; lookups and calculators;
  SSTS / Circular 230; AICPA Code, SSARS, SAS, SSAE / SOC, SQMS;
  engagement letters; workpapers; and FASB ASC research.
- **A file reader** (`read.py`). claude.ai accepts at most 200 files
  per skill ZIP, so the four large reference folders (strategies,
  state files, elections, engagement letters) are each packed into
  one file. Claude runs `read.py` to pull out a single entry.
- **The shared rules** (`shared/`): citation discipline, the
  authority hierarchy, confidence bands, compliance checklists, the
  output schema, and the canonical primary-source URL list.

Claude loads only the dispatcher at first. It opens a workflow and
its references only when your question needs them, so the large
reference library does not crowd your conversation.

> **Professional use only.** Outputs are research aids for licensed
> CPAs, EAs, and attorneys. They are not tax, legal, or accounting
> advice. The practitioner must complete the verification checklist
> on every output before relying on it. See `DISCLAIMER.md` and
> `LICENSE` (Business Source License 1.1) inside the ZIP.

# Requirements

| Item | Requirement |
|---|---|
| Plan | A claude.ai plan that supports custom skills (Pro, Max, Team, or Enterprise). |
| Code execution | **Required.** Skills read their files through Claude's code-execution environment. Turn on the code-execution / file-creation capability in Settings. On Team and Enterprise, an owner may need to enable it for the organization. |
| Web search / fetch | **Strongly recommended.** The pack retrieves primary sources live (uscode.house.gov, eCFR, IRS.gov, state agency sites). Without web access, Claude can't verify current law. It will mark unverified points with `[CITATION NEEDED — search: …]` instead of citing. |
| File | `vibe-cpa-pack.zip`, uploaded as-is. Do not unzip it first. |

# Installation

1. Open **claude.ai → Settings → Capabilities**. Newer layouts may
   place skills under a *Skills* or *Customize* section.
2. Confirm **code execution / file creation** is on.
3. In the **Skills** area, choose **Upload skill** (or **Add skill →
   Upload**) and select `vibe-cpa-pack.zip`.
4. Make sure the toggle next to **vibe-cpa-pack** is **on**.
5. If you previously uploaded individual Vibe CPA skills, turn those
   off. Duplicate skills compete for the same requests.

**Teams and firms.** On Team and Enterprise plans, an owner can
usually provision a skill for the whole organization from the admin
settings, so each staff member doesn't upload it separately. Check
your organization's admin console for the current option.

## Check the installation

Start a new chat and send:

> Which Vibe CPA workflow would you use for a question about whether
> a part-time horse-breeding activity is a hobby?

Claude should name `predict-hobby-loss` and briefly explain why. If
it answers generically without naming a workflow, see
*Troubleshooting* below. (Asking *which workflow* is not a research
request, so Question mode doesn't need to interview you for it. If
Claude asks a question first, that is Question mode working; answer
it or say "quick answer".)

# Using the pack

You don't need to name a workflow. Describe the task the way you
would to a colleague. Claude interviews you first (see *Question
mode* below), names the workflow it will use, and after your go-ahead
follows that workflow's analysis → conclusion steps.

## Question mode (on by default)

Before it researches anything, Claude asks you questions **one at a
time** until it is about 95% confident it understands exactly what
you are asking. This is the same Question mode as Vibe Tax Research
Chat. Each turn is one of three stages:

1. **Interviewing.** One question per turn, usually with numbered
   options. Reply with a number or in your own words. The questions
   come from the intake facts the chosen workflow needs: taxpayer
   type, tax year, state, circuit, amounts, and so on. Claude does no
   searching or citing in this stage.
2. **Ready.** Claude summarizes what it understood and gives a
   two-line plan. Nothing happens until you reply **proceed** (or
   "go ahead", "yes"). If the summary is wrong, correct it instead.
3. **Proceeding.** Claude runs the full workflow and returns the
   complete output described in *Reading an output*. Follow-ups on
   the same matter, such as "memo", don't restart the interview. A
   new question does.

A short exchange looks like this:

> **You:** Is my client's horse-breeding activity a hobby?
>
> **Claude:** **Question 1** · confidence ~40%. Which tax years are
> at issue, and has the activity shown a profit in any of them?
>
> **You:** 2021–2025, losses every year.
>
> **Claude:** **Question 2** · confidence ~65%. Is this an IRS
> exam, or planning before filing? 1. Open exam  2. Notice received
> 3. Planning
>
> **You:** 3
>
> *(…two or three more questions…)*
>
> **Claude:** **Ready** · confidence ~95%. **What I understood:** …
> **Plan:** 1. Run `predict-hobby-loss` on the nine §1.183-2(b)
> factors… 2. Return a band, disclosure call, and checklist. Reply
> **proceed** to start.

| To… | Say |
|---|---|
| Skip the interview for one request | "quick answer" or "skip questions" (in the request) |
| Turn it off for the rest of the chat | "question mode off" |
| Turn it back on | "question mode on" |

Give the key facts in your first message and the interview gets
shorter. If the first message has everything, Claude goes straight
to Ready.

## Example requests

| You want… | Try asking |
|---|---|
| Federal research memo | "Research whether a §1202 QSBS exclusion survives a C-to-S conversion. Taxpayer is in the 9th Circuit, tax year 2025." |
| Recent legislation | "What IRC sections did OBBBA amend that affect §174 R&E expensing?" |
| Worker classification | "Is a delivery driver in California who uses her own car and sets her own hours a W-2 or 1099 worker?" |
| Hobby loss / profit motive | "Schedule C horse-breeding losses four of the last five years — apply the §183 factors." |
| State income tax | "NY convenience-of-employer rule for a remote employee living in New Jersey." |
| Sales / use tax | "Does a Colorado seller with $150K of SaaS sales into Washington have nexus?" |
| Return summary | Attach a 1040 PDF: "Summarize this return and flag planning opportunities." |
| IRS notice | Paste or attach a CP2000: "Draft a response plan for this notice." |
| Planning | "What should this S-corp owner do before year-end?" (then supply facts) |
| Elections | "Give me §83(b) election language and the filing deadline." |
| Penalties / due dates | "Compute §6651 failure-to-file and failure-to-pay penalties plus interest for a 2024 return filed 8 months late with a $40,000 balance." |
| Engagement letter | "Draft a 1040 engagement letter including the FTC Safeguards clause." |
| Audit / attest | "Under AU-C 570, what going-concern procedures apply to a nonissuer?" |
| GAAP | "ASC 842 classification for a 7-year equipment lease with a bargain purchase option." |
| Workpapers | "Build a PBC list and lead-sheet index for a first-year manufacturing audit." |

If routing is unclear, ask: *"Which Vibe CPA workflow fits this?"*
To force a specific workflow, name it: *"Use the
tax-research-state-income workflow for this."*

## Better results

- **Give the material facts up front:** taxpayer type, tax year,
  state, and federal circuit (for Golsen weighting). The workflows
  ask for missing facts that matter. Supplying them first saves a
  round trip.
- **Attach source documents** (returns, notices, K-1s, contracts) as
  PDFs or text. Remove SSNs and other identifiers first. The
  workflows redact what they see, but don't rely on that.
- **Keep web search on** so citations are retrieved, not
  recalled.

# Reading an output

Every substantive answer follows the same structure:

1. **Analysis and conclusion.** Authorities are weighted under Treas.
   Reg. §1.6662-4(d)(3). AICPA and FASB questions use their own
   authority ladders.
2. **Confidence band:** HIGH, MODERATE, LOW, or SPECULATIVE, mapped
   to "should / will", substantial authority, reasonable basis (with
   disclosure), and below reasonable basis. A recommendation for
   Form 8275 / 8275-R / 8886 disclosure appears when it applies.
3. **Authorities.** Each one has its citation, URL, retrieval date,
   and a short verbatim quote.
4. **Verification checklist.** SSTS §1.1 and §2.3; Circular 230
   §§10.22, 10.35, 10.37; negative-treatment review. The AICPA Code,
   engagement-letter, and GAAP modules appear when relevant.
   **You complete this checklist, not Claude.**
5. **Follow-up options.** You can package the result (`memo` or
   `open-point` list) or carry it forward (`plan`, `workpaper`,
   `resolution`, `return`). Reply with the word, e.g. *"memo"*, and
   the pack runs the matching workflow.
6. **JSON sidecar.** A machine-readable record of the analysis that
   matches `shared/output-schema.json`. You can store it in the
   workpaper file or ignore it.

## Built-in safeguards

- **`[CITATION NEEDED — search: …]`** means Claude could not retrieve
  a primary source for that statement. It writes the search it would
  run instead of inventing a cite. Resolve every one of these before
  relying on the output.
- **State files marked `status: stub`** contain agency entry points
  only. A state conclusion that rests only on a stub file is capped
  at LOW confidence.
- **Treasury Regulations** are flagged for Skidmore review after
  *Loper Bright* (2024). Chevron deference is never assumed.
- **No citator.** The pack uses free sources and cannot detect
  implicit overrules the way KeyCite or Shepard's can. For
  high-stakes positions, run your own citator check.
- **Listed and Dirty-Dozen transactions** (e.g., §831(b)
  micro-captives, syndicated conservation easements) always carry a
  warning banner and Form 8886 flag.

# Troubleshooting

| Symptom | Fix |
|---|---|
| Claude answers generically and names no workflow | Make sure the skill toggle is on and code execution is enabled. Start a new chat, or say "use the vibe-cpa-pack skill". |
| "I can't read that file" or missing references | Code execution is off or blocked by an org policy. Ask your admin to enable it. |
| Many `[CITATION NEEDED]` sentinels | Web search is off or a source site was unreachable. Turn web search on and ask Claude to retry the retrieval. |
| An older single skill answers instead | Disable the individually uploaded Vibe CPA skills. |
| "Zip contains too many files (maximum 200)" | You have an older build (421 files). Download the current ZIP (about 170 files) or rebuild it with the script below. |
| Claude keeps asking questions | That is Question mode. Answer the question, reply "proceed" on the Ready turn, or say "question mode off". |
| Upload rejected | Upload the original ZIP without re-zipping it. The ZIP must contain one top-level `vibe-cpa-pack/` folder with `SKILL.md` inside. |

# Updating

To build a new bundle after the repository changes, run this from the
repository root:

```
python3 scripts/build-claude-ai-bundle.py
```

This writes `dist/vibe-cpa-pack.zip` and checks the result: the
200-file limit, the description length, the SKILL.md line count, that no nested skill
files remain, and that every `shared/…` or `skills/…` path cited in
the bundle exists. In claude.ai, delete or turn off the old version,
then upload the new ZIP.

# License and disclaimer

Vibe CPA Skills © 2026 Kisaes LLC, licensed under the Business Source
License 1.1. Use is limited to the Additional Use Grant in `LICENSE`
(non-production evaluation, education, and the personal practice of a
licensed CPA, EA, or attorney advising fewer than 100 clients). For other
production use, contact Kisaes LLC. The
pack does not provide tax, legal, or accounting advice; see
`DISCLAIMER.md`.
