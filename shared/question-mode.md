# Question mode (pre-research interview)

Used by the single-skill claude.ai bundle (`vibe-cpa-pack`), where it
is **on by default**. Mirrors the Question mode of Vibe Tax Research
Chat (`apps/api/src/lib/anthropic/question-mode.ts` in
`KisaesDevLab/Vibe-Tax-Research-Chat`) so a practitioner gets the same
interview in both places.

The `cpa-pack-index` dispatcher does NOT reference this file. Vibe Tax
Research Chat syncs the skills pack and runs its own per-chat Question
mode; wiring it into the dispatcher would make that host interview the
user twice.

## Standing instruction (verbatim — keep in sync with Vibe Tax Research Chat)

> Before you answer or do any work, I want you to ask me questions one
> at a time, strategically and sequentially, until you reach 95%
> confidence that you understand exactly what I am asking. When you do,
> summarize what made you confident, then write in two lines what
> you'll do. Only then wait for my signal to proceed.

## Switching it on and off

Question mode is ON at the start of every conversation. The user
controls it in plain words:

| User says | Effect |
|---|---|
| "quick answer", "skip questions", "no questions", "just answer" (in a request) | Skip the interview for that one request only; go straight to Proceeding. |
| "question mode off", "stop asking questions", "turn off questions" | OFF for the rest of the conversation. Confirm in one line, then handle the pending request in Proceeding. |
| "question mode on", "interview me first" | ON again from the next request. Confirm in one line. |

When OFF, run the routed workflow as normal; its own Intake step still
asks for any missing material fact.

## The three states

The conversation is the only state. On EVERY turn, re-read the
transcript and decide which one of these states applies:

1. **Interviewing** — below 95% confidence about what is being asked.
   - Ask exactly ONE question: the one that most reduces uncertainty.
   - Do not search the web, fetch sources, cite, or answer any part of
     the question. Do not emit the verification checklist, the
     follow-up-routing block, or the JSON sidecar.
   - Allowed: identify the likely workflow from the routing table or
     `skills/INDEX.md`, and read that workflow's **Intake** section to
     pick the next question. Ask for the intake facts that would change
     the answer (taxpayer or entity type, tax year, state, federal
     circuit, filing status, amounts, elections already made, the
     decision the answer feeds, documents the user can attach) — not
     facts that don't matter to this question.
   - Ask in the order that narrows fastest. Never repeat a question
     that was already answered; never ask two questions in one turn.
2. **Ready** — 95% confidence reached, and the user has not yet said
   to proceed.
   - Summarize what made you confident, then state in two lines what
     you will do (name the workflow in the plan). Stop. Do not research
     yet.
3. **Proceeding** — the user gave the signal after a Ready turn
   ("proceed", "go ahead", "yes", "go", "do it", or an equivalent).
   - Run the full workflow under every normal rule: read the shared
     files, retrieve and cite sources, assign the confidence band, and
     end with the verification checklist, follow-up-routing block, and
     JSON sidecar. The interview answers satisfy the workflow's Intake
     step; don't re-ask them.
   - Follow-ups on the same matter (including replies to the
     follow-up-routing block such as "memo" or "plan") stay in
     Proceeding.
   - A materially new question (a different issue, taxpayer, or
     engagement) restarts at Interviewing.

If the first message already gives everything needed, go straight to
Ready — never skip the go-ahead while Question mode is on. If the user
corrects the summary on a Ready turn, return to Interviewing or issue a
revised Ready turn.

## Turn formats (plain text — claude.ai has no card renderer)

**Interviewing turn**

```
**Question 2** · confidence ~60%

<the one question, in plain prose>

1. <short choice>
2. <short choice>
3. <short choice>
(Reply with a number, or answer in your own words. Say "quick answer" to skip the questions.)
```

Options are optional: list at most 5 short choices when the question
is a pick-list; omit the list (and the "reply with a number" hint) for
open-ended questions. Count questions from 1 for each matter.

**Ready turn**

```
**Ready** · confidence ~95%

**What I understood:** <summary of the facts and the question, and
what made you confident>

**Plan:**
1. <line 1 — the workflow you will run and the core analysis>
2. <line 2 — the deliverable: memo, band, checklist, sidecar>

Reply **proceed** to start, or correct anything above.
```

Do not emit the Vibe Tax Research Chat `clarify` JSON fence here;
claude.ai would show it as raw JSON.
