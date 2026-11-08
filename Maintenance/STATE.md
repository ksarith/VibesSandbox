# Maintenance STATE — LazarusForge Custodian Line

Current-state card, established 2026-11-06 (MAINT-69) under the human's maintenance-log architecture ruling. **Convenience only: the repositories are the authority; on any discrepancy the live repos govern. Verify at bootstrap.**

Last updated: 2026-11-08 (MAINT-78)

## Heads at last update

- LazarusForge main: `86ea1632` (post-MAINT-77 intake-17 landing; the Rule 5 and intake-16 landings in git history)
- VibesSandbox main: `1238364a` (pre-MAINT-78 fetch; the MAINT-77 intake-17 landing and its post-push verification addendum in git history)

## Bootstrap-critical versions (verify live; never trust this card over the files)

- `Admin/Forge_Audit_Kit.md`: v1.32
- `Admin/File_Template.md`: Last updated 2026-11-04
- `Unknowns.md`: v5.79
- `Admin/Progress_Log.md` parked rows: recount from the live table (45 rows / 37 Resolved / 8 open at 2026-11-06: PKC-009, -010, -021, -023, -026, -043, -044, -045)
- `Admin/Auditor_Protocols.md`: v0.47 (role-declaration source)

## Held queue (awaiting human ruling; as recorded at MAINT-68)

- MAINT-65 ratification + the F1–F8 ruling lines (MAINT-66)
- GOV-007 repair
- `Admin/Unknowns.md` pointer repairs
- AP F1/F2/F3; AP three-phase disposition
- Checker investigation
- MAINT-67 Part B mandate question
- Astroid-miner re-snapshot trigger (registered MAINT-71 addendum, 2026-11-07): fires on a second external PR/issue or resumed upstream commits; on firing a re-snapshot is owed (record: LF `Archive/Astroid-miner/PROVENANCE.md`)
- Rule 5 verification state (tranche-1; Claude named 2026-11-03): all five packets row-verified findings-only (reports 2026-11-05; Class A intakes 14–15 / MAINT-72–73); commit evidence supplied for all seven cited commits (six at MAINT-72, fee92b4 at MAINT-73) — failed-row and scope-change addenda + the F6 wording fix ENACTED 2026-11-07 (MAINT-74, human-ruled; LF `2d53cd8a` / VS `75e621a7`); Verified-by fills LANDED 2026-11-07 (MAINT-75: 50 cells, the verifier’s fill pass relayed by the human; four rows unfilled per convention: FT C-N3, SoT C-N2, MS B-C5, GC A-C5); still held for human ruling: Status-line replacement (all five aggregates); the two corrected-by-addendum rows’ and C-D1’s Rule 5 fills — the verifier’s call is now RECORDED (2026-11-08, intake 17 / MAINT-77: leave all three as-is, with reasoning; the reviewer reserves the human’s override, so his ratification is the outstanding ruling); tranche-2 verifier unassigned (MAINT-59 standing gap)
- External review intake 16 (ChatGPT 1.35 + VS 0.0.3 review, MAINT-76): recommendations recorded, none enacted — rulings owed on P1 (sandbox README update; STATE head-label clarification), P2 (VS Astroid-miner de-duplication §1–§5 proposal + References pointer + water-doc provenance addendum), P4 (MAINT_INDEX-vs-entries parity-check proposal; checker untouched), and the re-snapshot-trigger monitoring home (the reviewer's weekly offer vs a custodian-side scheduled task; one home only)
- External review intake 17 (Claude re-sync/held-queue review, MAINT-77): triage recommendations recorded, none enacted — his word owed on the worksheet pass for the cheap/mechanical cluster (GOV-007 repair + the seven `Admin/Unknowns.md` pointer repairs, one MAINT-61-style worksheet), the meta-work-to-fixes ratio check, and ratification of the verifier’s Rule 5 leave-as-is call (above)
- Decision Brief 2026-11-08 (event-logging surface for failed metrics and success paths, MAINT-78): drafted and deposited at the VibesSandbox root per his direction; awaiting his ruling — Option A (do nothing) / B (greppable event tag in future MAINT Disclosures lines) / C (append-only event-log file) / D (B now; C deferred to the C3 review with usage evidence); nothing enacted

## Where things live

- New entries: `Maintenance/entries/MAINT-NN.md` (from MAINT-69)
- Index: `Maintenance/MAINT_INDEX.md`
- Frozen history: `Maintenance/MAINT_LOG_2026-10-28.md`, `Maintenance/MAINT_LOG_2026-10-29.md`
- SESSION_STATUS.md: retired 2026-11-06 (dated terminal note); both homes frozen as history
