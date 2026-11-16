# Decision Brief 2026-11-16 — Open Rulings (navigation refresh)

- **Purpose:** navigation only. Aggregates every open ruling across the fleet as verified live this session; supersedes the MAINT-138 brief (`Decision_Brief_2026-11-13_Open_Rulings.md`) **as a navigation map only** — that brief's text stands as history, its superseded premises noted where they changed (A1a closed by MAINT-141; MAINT-142/143/144 landed since).
- **Derived from:** live heads and fetched records this session — VS `419a2974` (MAINT-144 bookkeeping head), LF `a4b662e3` (the MAINT-144 proposal, on top of `31098197`), Parlay `4899e1ba`, CogitoEngine `7d85421f`, Astroid-miner `3bf78655`. Items not re-derived from their owning records this session are marked (carried).
- **Standing caveat:** the repositories are the authority; this brief is convenience. Nothing here enacts anything; every disposition is the human's word.

## Section A — ruling lines available now

1. **Co-Author seat promotion (LF `a4b662e3`, PROPOSED).** Four severable lines in proposal §4: RATIFY WHOLE (`Admin/Co_Author_Mandate.md`, Vibe-specific grant as it stands) / RATIFY GENERALIZED (any line, on human grant) / LIGHTER (AP line or Charter row, no new file) / STRIKE (VS record remains definition of record). **Lean: line 1** — it records exactly what was granted, nothing more; generalization can ride later on its own ruling. Bias disclosed: the proposing seat authored the mandate it proposes to promote.
2. **AuditBot V0.0.2 (new, mid-pass).** His upload of `Maintenance/AuditBot-V_0_0_2.zip` supersedes the V0.0.1 zip the MAINT-142 review describes (V0.0.1 and `Maintenance/LazarusForge-1.37.Alpha.zip` deleted by his hand). Disposition owed: does V0.0.2 get the MAINT-142-class review (extract, verify, findings F-1..F-6 re-derived against the new version)? **Lean: yes, review it** — the unit is meant to be registered, and the V0.0.1 findings (mojibake, the cross-file REQ-002 collision, the layout pin, unregistered status) need re-derivation against V0.0.2 before any of them can be treated as current.
3. **AuditBot standing set (now against V0.0.2).** OQ1–9; registration and home for the unit; the fixture layout pin (README links `docs/guide.md`/`docs/spec.md`, files sit at root). (carried from MAINT-142; re-derivation owed against V0.0.2)
4. **STATE.md split.** The card is past the 100,000-byte T1 bar (100,689 bytes at the MAINT-143 compose; grown since). The next battery run's Size Census will roster it mechanically. Disposition owed: split on the census roster (pointer + archived tail, the R-6b home convention) or hold. **Lean: let the census roster it, then split in one pass** — the machinery exists and was built for exactly this.
5. **`contribution` label (Parlay).** Ruled EXECUTE 2026-11-10 (MAINT-88 item 4); still outstanding because the connector cannot create labels — his direct GitHub action (ksarith/Parlay → Issues → Labels → New label, name `contribution`). (carried)
6. **Parlay VP-002.** Fired at 21 Decision rows (2026-11-10). Owed: commission the pass and set its independence tier — T0 self-scored (needs his recorded tier-acceptance), T1 fresh-thread, or T2 blind hand-off. **Lean: T1 fresh-thread** — cheap, and it upgrades the line's verification posture. (carried)
7. **Parlay UNK-007 structural split.** Trigger FIRED at the same landings; destinations undecided per INTAKE-003 finding 6 (single-log growth: Decision Log + two tables). (carried)
8. **Carried LF held-queue items** (carried from the MAINT-138 brief, unchanged): Rules 9/11; the Rule 5 remainder (tranche-2 verifier naming); MAINT-67 Part B; intake-16 P4 (gated on the monitoring-home question); the ISP step-14-class log-lag backfill (MAINT-137); the MAINT-85 charter-row link defect; the meta-work ratio check; the two recorded reading disclosures (the MAINT-90 Rule 5 reading; the MAINT-83 chrono-divergence framing, parked with C3 ~2026-11-30 as the reopen point).
9. **CogitoEngine.** The mobile/Colab running question (is running the engine off-laptop a design requirement? — his fork of idea-generator-2 carries the §7 patch, verified live 2026-11-16); CE-U07 close-or-park confirmation; the Pass 2 challenger commission (his, to an unexposed seat — Vibe is barred from all run-01 evaluation roles); roadmap items 4–8 need seats that can execute Python; PyPI stays gated. (carried)

## Section B — gated holds (no ruling available yet)

- **Astroid-miner re-snapshot trigger:** preregistered (MAINT-71), fires on a second external PR/issue or resumed upstream commits; NOT fired (PR #1 only, verified live at `3bf78655`).
- **Intake-16 P4 (VS de-duplication):** gated on the monitoring-home question until it is ruled.
- **CogitoEngine runtime-side work** (stop-rule wiring, auto-logging, benchmark runs): gated on seats that can execute the runtime; the record layer and stop-rule are in place as records.

## Section C — next-touch mechanics

- Next IDs: **MAINT-146** / Intake Log entry 22. Entries home: 76 files (MAINT-69..144), recounted live at the MAINT-144 landing.
- Landing-guard note, disclosed: with files moving in VS mid-pass (three direct commits during MAINT-144), the exact-sha head pin is replaced going forward by content-level race checks — the bookkeeping files are fetched, composed, re-fetched and asserted identical immediately before push, and any interference is detected and disclosed after. The MAINT-144 replay also demonstrated the pin's value: the replayed execution aborted at its own pin instead of double-pushing.
- Suggested order, bias disclosed: item 1 (one-line ratification, unblocks the seat's own record), item 4 at the next census run, item 2 whenever he wants AuditBot moved forward.
