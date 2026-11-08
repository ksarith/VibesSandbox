# VibesSandbox

Agent working area for the LazarusForge project — a staging and verification zone, **not** LazarusForge doctrine.

## Purpose

- Hold Vibe's baseline pulls, verification reports, ruling lists, and other working artifacts produced while auditing or supporting `ksarith/LazarusForge`.
- Keep those artifacts reviewable and citable without touching the governed repository.

## Governance boundary

- **Nothing here is LazarusForge doctrine.** Files in this repo carry no Spec Gate, Status, or Unknowns weight, and must not be cited as source inside LazarusForge.
- **LazarusForge `main` remains human-merge-only.** Vibe never edits or pushes to `ksarith/LazarusForge` without explicit authorization from the human governing authority; changes there flow through the established commit-batch process.
- This sandbox is maintained at Vibe's discretion, per the governing authority's instruction of 2026-10-26.

## Maintenance records

- **Current maintenance state:** `Maintenance/STATE.md` — a convenience snapshot only, **not** an authority source; on any discrepancy the repositories govern.
- **Individual maintenance records:** `Maintenance/entries/MAINT-NN.md` (one file per pass, from MAINT-69 onward).
- **Navigation index:** `Maintenance/MAINT_INDEX.md` — a derived map; the entry files and the two frozen logs govern.
- **Frozen historical logs:** `Maintenance/MAINT_LOG_2026-10-28.md` and `Maintenance/MAINT_LOG_2026-10-29.md` (the pre-MAINT-69 monolith logs, frozen, never rewritten).
- **Decision briefs:** the `Decision_Brief_*.md` files at this repo's root.
- **Verification reports and audit deposits:** `Audits/`.
- **Archived project snapshots:** `Astroid-miner-AstroidMinerV0.07/` (working-tree copy; the canonical archive lives in LazarusForge — see the MAINT-71 records and the pending de-duplication ruling) and the `LazarusForge-1.33.Alpha.zip` / `LazarusForge-1.34.Alpha.zip` release archives under `Maintenance/`.

*(Section added 2026-11-08, MAINT-82, executing intake-16 P1 of the human-ruled MAINT-81 ruling set.)*

## Contents

| File | What it is |
|---|---|
| `PKC_Ruling_List.md` | Decision-ready list of the Parked Concerns requiring human rulings, with recommended dispositions and a 2026-10-26 status note marking which have since been enacted. |
| `Decision_Brief_2026-10-27.md` | Vibe's decision-ready material for the human ruling session: pin-vs-retire options (with recommendation), PKC-033 authorization scope, PKC-001 hold-vs-investigate. Nothing here is doctrine. |
| `Decision_Brief_2026-10-27b.md` | Follow-up decision brief for the twelve Parked Concerns still open after the 2026-10-27 rulings, plus the sweep-prompt candidate and the RIP-011 semantics. Nothing here is doctrine. |
| `Baseline_Pull_2026-10-26.md` | Vibe's full baseline pull of LazarusForge `main` at commit f79c0b6: five-sweep verification, findings, and a 100-file version table. Includes a staleness banner recording post-baseline fixes. |
| `Decision_Brief_2026-10-30.md` | X3 completion report (495 quals / 55 files), Unknowns.md + README.md disposition requests, and the 2026-10-30 direction that session logs live in this sandbox (front/back separation; template split option carried). Nothing here is doctrine. |
| `Maintenance/` | The maintenance-log architecture home (MAINT-69 onward): `STATE.md` convenience card, `MAINT_INDEX.md` derived index, per-entry records in `entries/`, and the two frozen historical logs. See the Maintenance records section above. |
