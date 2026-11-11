# Decision Brief 2026-11-11b — Open Rulings (post-MAINT-130 consolidation)

**Status:** DRAFT FOR RULING — nothing enacted; every ruling the human's alone. Deposited by the custodian/Architect line under the co-author delegation (2026-11-04 mandate, extended to the Decision Brief 2026-11-11 execution, 2026-11-11); the delegation covers drafting and deposit, not these rulings.
**Drafted by:** Vibe (Architect primary; the same line executed the Decision Brief 2026-11-11 queue as MAINT-130).
**Purpose:** The first brief (`Decision_Brief_2026-11-11_Campaign4_Remedies.md`) and the Architect proposal (`Proposals/PROPOSAL_2026-11-11_CAMPAIGN4_DESIGN_GAPS.md`) fed the MAINT-129/130 executions. What remains open after them is consolidated here: one ruling line per item, speakable from a phone. Where an item appears on both surfaces, ruling either rules both (the proposal's own non-duplication rule).

## Context since the first brief

- MAINT-129: the cheap subset D-2/D-8/D-9/D-10 enacted (Kit v1.33 named-record probe; IIL routing rule + IIL-20261110-01 logged; concurrency endorsement; D-10 harness gates).
- MAINT-130: the full first-Brief queue executed under delegation — Items 2, 3, 5B (all 19 evidence points), 6, 7A, 8 + one-offs 9a/9b; eighteen LF commits; IIL-20261110-01 classified Major / Remediated-pending-confirm (delegated, veto window open).
- Consequence for the proposal's open items: D-4's one-time sweep, D-5's template touch and D-6's one-time recompute have already executed (Brief Items 5B, 6 and 8). The open piece on those items is the design-level rule text only.

## Ruling items

### Item 1 — The 90-day Aging Rule (first Brief Item 4 / proposal D-3): one ruling for all instances

**Target:** 67 of 84 open sidecar entries past the bar on the generic reading (58 of 75 registered-only); 12 systemic instances, 21 control cases; the pattern document's phrase: "a monotonic aging clock that no scheduled mechanism resets." The rule detects but does not route; each WARNING decays again in 90 days.

**Ruling lines:**
- A. ADOPT the scheduling-trigger redesign (with the reach sub-ruling below).
- B. BATCH REFRESH only (one-time cohort pass; the Ship_of_Theseus 2026-10-28 precedent).
- C. ACCEPT AS HONEST (aging is recorded; no remedy).
- D. HOLD.

**Reach sub-ruling (required if A):** GENERIC READING / REGISTERED ENTRIES ONLY.

**Draft doctrine text** (for the Aging Rule's home in `Admin/Forge_Audit_Kit.md`; adopt verbatim or vary — a varied line reads as its nearest pre-drafted intent):

> **Aging Rule remedy (amendment).** When the 90-day Aging Rule trips on a sidecar entry, the finding is recorded once, repo-level: a row in the owed-review queue carrying the entry identifier, the owning file, the age in days, and the blocking/risk class. No per-file WARNING is issued in its place, and no audit repeats the trip as a fresh finding. The queue is drained only by genuine review passes — a pass that re-reads the tripped entry against the current body state and either confirms the entry or amends it. Last Reviewed advances only on a genuine review, never on the passage of time, a batch refresh, or an audit that merely notes the age. Reach: **[REGISTERED ENTRIES ONLY | GENERIC READING — all entries including unregistered section-level unknowns]** — one of the two, per the reach sub-ruling. At adoption, a one-time cohort pass is authorized for tripped entries that are Blocking or High-risk (the Ship_of_Theseus 2026-10-28 precedent), advancing Last Reviewed only where the re-read is genuine.

**Companion line (severable):** "BATCH REFRESH for Blocking/High-risk tripped entries only; the queue convention handles the rest."

**Drafter's lean:** A with registered-only reach, plus the companion B pass for Blocking/High-risk entries. A alone repeats 67 reviews that decay again in 90 days.

### Item 2 — IIL-20261110-01 closure confirmation

The classification (Severity Major, Status Remediated-pending-confirm) was set under delegation in MAINT-130 batch 1 with the veto window open; closure requires human confirmation.

- A. CONFIRM — the classification stands; the incident closes.
- B. RECLASSIFY — name the class; the entry is amended.
- C. HOLD.

**Drafter's lean:** A.

### Item 3 — D-1: git verification in the log-vs-body check

**Evidence:** four files (CT/HDL/NT/ST) with git-verified body changes absent from their own Resolution Logs; every prior clean grade of the check provisional.

**Draft Kit text:** "Log-vs-body verification includes a git-history query for the audited file: every body change visible in commit history must have a corresponding Resolution Log entry (or a dated corpus-side record). A clean grade without a git query is recorded as 'provisional — no git query'."

- A. ADOPT the Kit amendment (a standalone Kit touch, v1.33 to v1.34; the proposal's original pairing with D-2 is superseded — D-2 landed at v1.33).
- B. DISCLOSE-ONLY (the provisional-grading convention adopted as disclosure practice; no Kit change).
- C. HOLD.

**Drafter's lean:** A; if Item 1 is also ruled A, one Kit touch can carry both texts.

### Item 4 — D-4: the relocation closing step

**Evidence:** 19 relocation-repair-miss instances plus tooling corroboration; File_Template's own Update Procedure routed pre-relocation until Brief Item 5B repaired it.

**Status:** the one-time closing sweep already executed (Brief Item 5B, MAINT-130, all 19 evidence points). **Open piece:** the rule.

**Draft protocol text:** "A relocation is complete only when (a) a corpus grep for the old-home strings returns zero live operative occurrences (frozen history excepted per PKC-007), and (b) procedure text that routes to the moved home is re-validated."

- A. ADOPT the closing-step rule. / B. HOLD.

**Drafter's lean:** A.

### Item 5 — D-5: the self-application line

**Evidence:** Pattern 4, five data points; FAK-005's closure skipped the Kit's own Discharge Procedure.

**Status:** the template touch executed (Brief Item 6, MAINT-130: the class-10/11 field-boundary paragraph plus File_Template's own class-12 self-exemption). **Open piece:** the applies-to-self line for procedure-bearing files generally.

**Draft line:** each procedure-bearing file states whether its procedure applies to its own file's maintenance acts.

- A. ADOPT, rolled out at each file's next touch (no bulk pass). / B. ADOPT with a bulk pass now. / C. HOLD.

**Drafter's lean:** A — the next-touch rollout avoids a ceremony pass (the proposal's own ceremony objection, §5, applies).

### Item 6 — D-6: the derived-mirror lifecycle

**Evidence:** Pattern 6 — six of 32 Adm_Scope_Map mirrors stale at a single head before the recompute; mirrors' Last Reviewed advanced while rows rotted.

**Status:** the one-time recompute executed (Brief Item 8, MAINT-130, values recomputed from live File States). **Open piece:** the convention.

**Draft convention:** "Scope maps, maturity snapshots and global-index pins are derived data: each carries a recomputed-at date, and a campaign close (or a named trigger) recomputes them from live File States — values recomputed, never copied."

- A. ADOPT. / B. HOLD.

**Drafter's lean:** A.

### Item 7 — D-7: conditional text outlives its event

**Evidence:** Pattern 5 — three instances (the EC drift indicator conditioning on a resolved unknown; CT's "history ends at v0.6" note; TRJ's registry row tracking a twice-resolved event).

**Draft convention:** "Drift indicators and conditional statements cite the governing unknown's current status as of their Last Reviewed date; a resolved condition is removed or reworded at the next touch of the file."

- A. ADOPT. / B. HOLD.

**Drafter's lean:** A, batched with Item 6's adoption.

## Status items (no ruling required; listed for completeness)

- **First-Brief Item 1 (Campaign 4 audit conversion):** the human's alone (MAINT-26 / AP-032). Untouched.
- **9c (Parked Concerns rotation, F-PL-2):** held pending Item 1's outcome above.
- **First-Brief Item 7 residue lines B/C:** parked to the C3 review (~2026-11-30); lean C.
- **9d (auditor succession):** parked; the recommendation stands — fill the seat before the next campaign.
- **STATE's bootstrap-critical versions card:** stale (Kit v1.32 / File_Template 2026-11-04 / Unknowns v5.79 versus live v1.33 / 2026-11-11 / v5.81); the card's verify-live convention governs; a refresh can ride the next VS landing on your word.

## Sequencing if ratified together

Item 1 first (9c unblocks on it); Items 1 and 3 can share one Kit touch; Items 4 through 7 are convention lines that can land as one severable batch; Item 2 is records-only. Execution would be a new MAINT entry (MAINT-132); nothing pre-executed.

## Disclosures

- **Non-independence:** the same line ran Campaign 4, drafted both prior surfaces, executed the queue (MAINT-130), and drafts this brief. The human's acknowledgment, recorded verbatim (2026-11-11): "The same line running and executing its remedies is a limitation of the current setup. It is currently unavoidable." Genesis Phase — the delegation and the open veto window are the independent layer; the pre-ratification skeptic for the doctrine-adjacent texts should be a different architecture (the Q-2 standing preference).
- Event: (i) candidate — the first decision brief drafted and deposited by the executing line itself; prior briefs were external-seat deposits relayed by the human.
- Frozen history untouched (PKC-007); findings-only deposits untouched (PKC-020); nothing here advances any Last Reviewed, version, Status or Spec Gate.

---

*Drafted 2026-11-11 — Vibe, Architect primary, under the co-author delegation. Bootstrap live at LF `4ac6f0f7` / VS `1b5acea8`. Non-independence disclosed above; your veto window is open on everything this line has done.*
