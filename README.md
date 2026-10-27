# VibesSandbox

Agent working area for the LazarusForge project — a staging and verification zone, **not** LazarusForge doctrine.

## Purpose

- Hold Vibe's baseline pulls, verification reports, ruling lists, and other working artifacts produced while auditing or supporting `ksarith/LazarusForge`.
- Keep those artifacts reviewable and citable without touching the governed repository.

## Governance boundary

- **Nothing here is LazarusForge doctrine.** Files in this repo carry no Spec Gate, Status, or Unknowns weight, and must not be cited as source inside LazarusForge.
- **LazarusForge `main` remains human-merge-only.** Vibe never edits or pushes to `ksarith/LazarusForge` without explicit authorization from the human governing authority; changes there flow through the established commit-batch process.
- This sandbox is maintained at Vibe's discretion, per the governing authority's instruction of 2026-10-26.

## Contents

| File | What it is |
|---|---|
| `PKC_Ruling_List.md` | Decision-ready list of the Parked Concerns requiring human rulings, with recommended dispositions and a 2026-10-26 status note marking which have since been enacted. |
| `Decision_Brief_2026-10-27.md` | Vibe's decision-ready material for the human ruling session: pin-vs-retire options (with recommendation), PKC-033 authorization scope, PKC-001 hold-vs-investigate. Nothing here is doctrine. |
| `Decision_Brief_2026-10-27b.md` | Follow-up decision brief for the twelve Parked Concerns still open after the 2026-10-27 rulings, plus the sweep-prompt candidate and the RIP-011 semantics. Nothing here is doctrine. |
| `Baseline_Pull_2026-10-26.md` | Vibe's full baseline pull of LazarusForge `main` at commit f79c0b6: five-sweep verification, findings, and a 100-file version table. Includes a staleness banner recording post-baseline fixes. |