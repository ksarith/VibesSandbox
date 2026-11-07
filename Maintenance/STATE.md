# Maintenance STATE — LazarusForge Custodian Line

Current-state card, established 2026-11-06 (MAINT-69) under the human's maintenance-log architecture ruling. **Convenience only: the repositories are the authority; on any discrepancy the live repos govern. Verify at bootstrap.**

Last updated: 2026-11-07 (MAINT-76)

## Heads at last update

- LazarusForge main: `b0dd60c9` (post-MAINT-76 intake-16 landing; MAINT-75 fills landing in git history)
- VibesSandbox main: `c15d2ac4` (pre-MAINT-76 fetch; MAINT-75 commits in git history; human upload 2026-11-07 added `Maintenance/LazarusForge-1.34.Alpha.zip`)

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
- Rule 5 verification state (tranche-1; Claude named 2026-11-03): all five packets row-verified findings-only (reports 2026-11-05; Class A intakes 14–15 / MAINT-72–73); commit evidence supplied for all seven cited commits (six at MAINT-72, fee92b4 at MAINT-73) — failed-row and scope-change addenda + the F6 wording fix ENACTED 2026-11-07 (MAINT-74, human-ruled; LF `2d53cd8a` / VS `75e621a7`); Verified-by fills LANDED 2026-11-07 (MAINT-75: 50 cells, the verifier’s fill pass relayed by the human; four rows unfilled per convention: FT C-N3, SoT C-N2, MS B-C5, GC A-C5); still held for human ruling: Status-line replacement (all five aggregates), the two corrected-by-addendum rows’ and C-D1’s Rule 5 fills (verifier’s call), tranche-2 verifier unassigned (MAINT-59 standing gap)
- External review intake 16 (ChatGPT 1.35 + VS 0.0.3 review, MAINT-76): recommendations recorded, none enacted — rulings owed on P1 (sandbox README update; STATE head-label clarification), P2 (VS Astroid-miner de-duplication §1–§5 proposal + References pointer + water-doc provenance addendum), P4 (MAINT_INDEX-vs-entries parity-check proposal; checker untouched), and the re-snapshot-trigger monitoring home (the reviewer's weekly offer vs a custodian-side scheduled task; one home only)

## Where things live

- New entries: `Maintenance/entries/MAINT-NN.md` (from MAINT-69)
- Index: `Maintenance/MAINT_INDEX.md`
- Frozen history: `Maintenance/MAINT_LOG_2026-10-28.md`, `Maintenance/MAINT_LOG_2026-10-29.md`
- SESSION_STATUS.md: retired 2026-11-06 (dated terminal note); both homes frozen as history
