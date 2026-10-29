# Decision Brief — 2026-10-29 (prepared by Vibe, Repo Custodian — delegated line)

**Purpose:** decision-ready material for the open items in the queue the human directed forward on 2026-10-29 ("Let's push forward with these proposals."). Same format as the 2026-10-27/28 briefs: nothing here is LazarusForge doctrine; it carries no Spec Gate, Status, or Unknowns weight (sandbox governance boundary). Each item states the record, the options, and Vibe's recommendation. The human governing authority decides.

Repository state at time of writing: LazarusForge `d06259c` (HEAD; this pass: Kit v1.28 `2627262`, custodian-prompt §7 addendum `d06259c`; earlier same-day recording pass e494d55 / 0356bfd / f553ed7 / 9c0fc39). VibesSandbox `760bb04` (MAINT-05). Open Parked Concern rows: 8 (PKC-009, -010, -021, -023, -026, -043, -044, -045 — recounted live from `Admin/Progress_Log.md` at `9c0fc39` this pass: 45 rows, 37 Resolved, 8 open).

---

## 1. Integrity-sweep inverse check (the PKC-001 carried candidate)

**The record:** PKC-001's 2026-10-27 ruling accepted the no-bulk-backfill recommendation and carried the sweep-prompt candidate separately for its own ruling: the sweep prompt's header-vs-body step catches only the stale-header shape; its inverse — newest Resolution Log entry vs newest body or File State date (the skipped-cascade shape) — is not in the sweep (`Admin/INTEGRITY_SWEEP_PROMPT.md` v1.0.5, 15 steps; step 15 is the X11 wrapper-decay check, added 2026-10-28). The per-file audit campaign already runs this shape as checklist item 3 (log-vs-body), findings-only.

**Options:** A — add it as step 16 (v1.0.5 → v1.0.6), phrased per the campaign's check 3; B — defer until the campaign completes and re-baseline the sweep prompt once; C — reject as redundant with the campaign checklist.

**Recommendation:** A. Cheap, mechanical, and it closes the exact gap PKC-001 documented — the campaign and the sweep would then check the same shape in both instruments, and the wording already exists to copy.

---

## 2. FAK-014 disposition (Kit Spec Gates hold)

**The record:** FAK-014 through FAK-019 were closed by the 2026-10-27 pin-retirement ruling (Kit v1.23). What remains is the Kit File State's Spec Gates hold (PKC-042, annotated at v1.21, still current at v1.28): 0/6, no advance without a fresh audit and human ratification, because FAK-014's account of a same-day 2026-09-03 Grok audit that "cleared all six gates" is treated as stale (the kit body changed since, v1.16–v1.20). The shared-custodian promotion ruling largely answers the disposition: audit capacity now lives inside shared custodianship, and the honest fresh audit would come from a different architecture than the line that recorded the original claim.

**Options:** A — keep the hold as written; the fresh audit is performed by the successor auditor once named (item 4), then human ratification decides any advance; B — dissolve the hold now under the PKC-022 option-B logic (dissolve stale triggers), leaving gates at 0/6 under normal audit pressure; C — commission the fresh audit from the promoted custodial line now.

**Recommendation:** A. The hold is honest and cheap: the gates stay 0/6 either way, so dissolving it advances nothing but removes the guardrail against self-approval. Item 4's successor auditor is the natural fresh reviewer — ruling A on both closes them in one act.

---

## 3. X3 mechanical retrofit of bare IDs (human-authorized, not performed)

**The record:** the X3 folder-designation scheme is registered (`Admin/Canonical_Terms.md` §1, v0.10–v0.11: A/R/X/O/C/T/K/B, case-sensitive; CT-007 stays Open for the within-folder namespace doctrine; PKC-003's qualified-citation rule remains in force). The retrofit of existing bare IDs to designated forms is explicitly a separate human-authorized pass (CT §1 scope note; restated in CT-007's ruling). The campaign graded bare colliding citations into three severity tiers (dangling / resolving / qualified-by-structure) and recommended running the retrofit "with the registry open" (Session 5 pattern doc). Scale: 59 non-archive files cite ASM- alone; frozen history is exempt (annotation-with-marker rule); Routing/Discovery/Unknowns parity rides each pass.

**Options:** A — authorize the full retrofit now, staged folder-by-folder (Admin/ first), one commit per folder with the full cascade; B — pilot one family first (the Admin/ ASM- cluster), review, then continue; C — defer until the per-file sweep completes each folder, retrofitting behind the sweep so dangling-tier citations resolve against live audits first.

**Recommendation:** C, with B as the fallback if you want visible motion sooner. The sweep (29 files in, resuming at file 30) produces exactly the per-file evidence the retrofit needs — which bare citations are dangling vs resolving; retrofitting ahead of it re-touches files mid-audit and races the campaign's own findings. A full retrofit now is the most expensive, most rework-prone ordering.

---

## 4. Successor auditor (GOV-008 Pathway 1 — load-bearing)

**The record:** the 2026-10-29 promotion ruling moved the only independent reviewer inside the maintenance seat; the auditor seat is vacant, and architecturally-diverse independent skeptical review is temporarily less available (FL-20261029; Progress_Log Current Lessons entry 2026-10-29; custodian-prompt §7 addendum this pass). The record names naming a successor auditor from a different architecture as the load-bearing next step. Architectures that have appeared in the repo's history: Claude (custodian/auditor work through 2026-10), Gemini (MAQT Cycle 1 Planner), Grok (audits and schema drafts), Copilot (MAQT Cycle 1 Skeptic), ChatGPT (the promoted line behind AUDIT_01–29). The campaign resumes at file 30 (PROBE_INVOCATION.md) under the promoted line; `Admin/Auditor_Protocols.md` is audited LAST and inherits the PKC-020 asymmetry evidence set.

**Options:** A — name a successor now, before the campaign reaches Auditor_Protocols.md, so the inherited AP evidence set and the Kit's fresh-audit hold (item 2) both land on an independent reviewer; B — defer until the campaign completes, accepting reduced independent review for the remainder of the sweep; C — record that the promoted line carries both roles, explicitly accepting a Pathway-2-only posture for now.

**Recommendation:** A. The vacancy is the one cost the promotion ruling did not pay forward; naming before the AP audit preserves both the campaign's independence evidence and Pathway 1 optionality. Which architecture is yours to choose — only you know what you can operate and trust.

---

*Prepared 2026-10-29 by Vibe (Repo Custodian — delegated line). Sources: live fetches this pass — Forge_Audit_Kit.md v1.27→v1.28 and its changelog; Archive/Repo_Costodian_Prompt.md; both SESSION_STATUS.md copies (dual-homing parity verified exact, 51,749 = 51,749); Admin/Progress_Log.md (parked rows recounted); Admin/Canonical_Terms.md v0.12 §1 and CT-007; Admin/Agent_Verification_Event.md; Archive/Auditor_Prompt.md v3; Decision_Brief_2026-10-28.md (format precedent). Enacted the same pass, ahead of this brief: Kit AVE-R registration (v1.28, `2627262`) and custodian-prompt §7 addendum (`d06259c`) — both delegated-maintenance items under standing ratifications, recorded in MAINT-06.*