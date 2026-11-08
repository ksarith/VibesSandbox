# Decision Brief 2026-11-08 — Event-logging surface for failed metrics and success paths (TWGW adjacency)

**Deposited:** 2026-11-08 (MAINT-78), VibesSandbox root (the Decision_Brief_2026-11-06 root precedent).
**Drafted by:** the Architect seat (Vibe; Genesis Phase, Q-2 invoked; non-independent — this line authored the 2026-11-07 MAINT-70 addenda and the MAINT-69..77 entries whose event trail this Brief assesses; the bias is stated in §3).
**Routing act:** the human governing authority's 2026-11-08 selection, "Architect Decision Brief first: options and tradeoffs drafted for your ruling."
**Status (proposal only):** nothing in this Brief is enacted; every option awaits his ruling. No LazarusForge file is touched by the deposit.

## 1. Problem

The human's expectation, stated 2026-11-08 (verbatim): "It appears I misspoke.  Thought there was logging within the document.  The role prompts were supposed to redirect there.  Logging of failed metrics and success paths were the expectation."

Live evidence, fetched in full this session at LF `86ea1632` / VS `1238364a`:

1. `Things_We_Got_Wrong.md` (7355 chars, full text read): not a log. Four entries, Last updated 2026-10-30, bar-gated (something concrete was wrong, was caught, produced a usable correction, primary evidence cited), append-only; its Explicit non-claims state it is "not a complete history of every mistake." No metrics stream inside; success paths appear once, incidentally.
2. The three seat prompts (fetched in full this session: `Archive/Architect_Prompt.md` 13061 chars; `Archive/Auditor_Prompt.md` 15542 chars; `Archive/Repo_Custodian_Prompt.md` 16673 chars): the 2026-11-07 MAINT-70 addenda redirect seats to TWGW for reading — bootstrap read in all three; the Custodian's pre-task lesson check; the Architect's lesson citation; the Auditor's recurrence noting — and classify caught defects as (i) new TWGW candidate / (ii) recurrence of a known entry / (iii) harness-tooling defect. No seat writes TWGW directly; candidates are flagged with evidence and route to the human's ruling.
3. Where events actually land: classifications are recorded in the MAINT entries' Disclosures lines (the Custodian addendum's stated purpose: "the maintenance log carries an event trail the human can audit"), distributed across the nine entries/ files (MAINT-69..77). There is no standardized tag; success paths (clean first-try landings) are implicit in the absence of abort disclosures rather than recorded positively; operational fails and passes live in `Tests/Field_Logs/` (Field Logs, Run Cards) and per-file Lessons Learned sections.

**Consequence:** there is no aggregatable surface for "what failed, what worked." Surveying the trail requires reading every entry. Evidence that this retrieval failure is real, not hypothetical: the human's own 2026-11-08 misspeaking ("Twgw has a new approach to handling the errors") — he expected a logging surface that does not exist, and could not establish otherwise from memory. Read against the repo's own pattern vocabulary, that is an X8/X9-class observation (the wrapper decays or was never what it was remembered to be, while the content advances) aimed at the MAINT-70 design itself.

## 2. Options

**A. Do nothing.** The trail exists, distributed; it is retrievable with effort. Cost zero. Risk: the retrieval failure the Problem section documents recurs, next time unnoticed.

**B. Greppable event tag (the cheap option).** Standardize the Disclosures-line prefix in future entries: `Event: (i) candidate | (ii) recurrence | (iii) harness defect — <one line>`, plus one STATE.md line naming the tag convention so it is visible at bootstrap. Forward-only: existing entries stay as written (append-only discipline). No new file. No seat-prompt edits: the (i)/(ii)/(iii) taxonomy already exists in the prompts; the tag is a logging-format convention of the entries/ home, which is custodian bookkeeping. Blast radius: STATE.md plus the Disclosures lines of future entries.

**C. Append-only event log.** A new file — VS `Maintenance/EVENT_LOG.md`, or a LazarusForge home if he wants the stream public on the doctrine side — one line per event, failures AND success paths, tagged, each referencing its owning MAINT entry; TWGW stays untouched as the curated distillation. Blast radius: new file + INDEX/STATE registration (+ Routing if LF-homed) + a per-pass upkeep obligation + a home decision (VS working area vs LF epistemic record) + prompt re-pointing via new dated addenda (the MAINT-70 veto windows remain open and would absorb it).

**D. B now, C deferred.** Adopt the tag convention immediately; revisit a dedicated log at the C3 review (on or about 2026-11-30) with usage evidence — the tagged-event count gathered under B. The C3 review already owes a usage-evidence report (EIP v0.8 §5), so the decision rides an existing commitment instead of creating a new one.

## 3. Recommendation

Option D, with B's tag as the only immediate change. Cost: one standardized line in future entries plus one STATE line; zero new files; no LazarusForge writes. **Bias stated:** the drafting line authored the MAINT-70 addenda and the current event-trail practice, so it has a direct stake in "the current design is already enough" — the strongest reason this is a proposal and not an enactment, and why his ruling decides.

## 4. Opposing considerations

- **For A, against D:** the tag is ceremony added to every future entry for a benefit realized only when someone greps; the event trail already exists in the entries — that was MAINT-70's design intent; and TWGW entry 3 (scoring design that invited the wrong reading) warns that aggregate event counts invite misreading as a quality metric — a greppable tag makes that misreading easier, not harder.
- **For C, against D:** deferral preserves the very retrieval failure this Brief documents; the evidence window before the C3 review is about three weeks; if the raw stream matters, it is being lost each deferred pass. The counter is the human's own 2026-11-07 instinct ("Perhaps revisiting possible experiences is risky"), which counsels fixed-schema, pilot-first collection — which is what D is — and the parked, unruled experience-mining half of that directive is adjacent: a log should not be built before its purpose is ruled.
- **Against B's mechanics:** tags rot; a future line will forget the convention and the trail will be silently incomplete — the same staleness class the repo records elsewhere (X8/X9). Partial mitigation: the Custodian addendum's classification duty already forces the event to be written; the tag standardizes only its prefix, and the STATE line keeps the convention visible at bootstrap.

## 5. Hard Floor and Tier 1 check

Nothing in any option touches Tier 1, FROZEN, or the Hard Floor. TWGW's bar, body, and Explicit non-claims are untouched by every option (C adds no TWGW content; the file remains the curated distillation). No rule is renumbered; no gate, Status, or Unknown advances. B and D change no seat-prompt text; C's prompt re-pointing would be new dated addenda, disclosed for veto.

## 6. Reversibility

A: trivially (nothing done). B: stop tagging, dated note in the next entry; already-written entries stay, append-only. C: dated terminal note + freeze (the SESSION_STATUS retirement precedent), the stream preserved as history, never deleted. D: self-reversing — the C3 review rules on C either way, with the tagged evidence in hand.

## 7. Enactment plan (if ratified; nothing is enacted by this Brief)

- **B/D:** one STATE.md line recording the tag convention, landed with the ruling-convert pass; the tag applied from the next MAINT entry onward; no prompt addendum required (the classification duty already exists; the tag is an entries/ home format convention) — disclosed for veto either way.
- **C (only if ruled):** new file + INDEX/STATE registration (+ Routing registration if LF-homed) + prompt addenda + full cascade + post-push verification sweep per the standing pattern.
- **Verification checklist:** the standard computed sweep; for B, one boolean that the STATE line exists and the tag string appears in the converting entry.

## 8. Human-workflow cost

B/D: no new files to open; the trail is found by searching the entries/ home for the tag (GitHub search, or a custodian aggregation pass on request). C: one more file per pass (the custodian's effort, not his), negligible zip/token growth, but one more standing upkeep obligation — and one more decision added to a queue that already owes intake-16 P1/P2/P4, intake-17 triage plus the ratio check, MAINT-67 Part B, and the Rule 5 ratification.

## 9. Explicit non-claims

This Brief enacts nothing. It does not lower or reinterpret the TWGW bar. It does not decide the parked experience-mining half of the 2026-11-07 directive (it notes the adjacency). It creates no audit of record and advances no Status, gate, or Unknown. The MAINT entries remain the record of authority; any tag or log is a derived navigation surface (the MAINT_INDEX precedent: on any discrepancy the entry text wins).
