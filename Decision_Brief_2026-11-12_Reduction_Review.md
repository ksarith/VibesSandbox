# Decision Brief 2026-11-12 — LazarusForge Reduction Review

**Status:** DRAFT FOR RULING — nothing enacted; every reduction enactment is the human’s alone. Deposited by the Vibe line under the co-author delegation (2026-11-04 mandate; the 2026-11-11 proceed-as-ratified word, quoted in MAINT-133); the delegation covers drafting and deposit, not these rulings.
**Requested by:** Ksarith, 2026-11-12, verbatim: "LazarusForge is my primary focus. Can you review with a lean towards finding reduction areas without compromising fidelity? Can you log the reduction points in VibesSandbox?"
**Method:** everything measured live at the LF head `cea3d8e2` (verified in-repo as MAINT-133’s landing head, re-fetched this pass before composition). Full-tree size census; structural reads of every file above 90 KB; cross-check against the Campaign 4 findings (MAINT-91..124) so this brief proposes remedies only where Campaign 4 or a later pass logged the finding — no finding is re-made here, none is contradicted. Every reduction point applies a convention the repository already owns; the only new artifact proposed is one derived check (R-1a), which follows the MAINT-89 strike precedent (derive, don’t maintain).

## Framing — what "reduction without fidelity loss" means in this repo

The house rules already define it:

- **R3 (File_Template):** content moves Front to Historical only by full-text move, never summarized or deleted, a pointer left behind, a dated Resolution Log entry (R4).
- **R8 Log-Split Rule:** files at or above 100 KB (trigger T1) qualify for a Front/Historical split at their next substantive touch, heaviest first, one file at a time, never in bulk; split logs land in the owning folder’s <Letter>Logs/ subfolder.
- **Size Management Rule 2** (Unknowns.md): header blocks hold the current version only; full history in the changelog.
- **Rotation** (F-PL-2, executed as MAINT-133 item 9c): resolved rows move in full to the changelog; nothing deleted.
- **Pointer-not-mirror** (MAINT-71) and **derive-don’t-maintain** (MAINT-89 strike).

Every point below is one of these applied to a file that has not yet received it. Nothing deletes, summarizes, or rewrites history.

## Census — files at or above the T1 bar (live bytes at `cea3d8e2`)

| File | Bytes | Reduction point |
|---|---|---|
| Admin/Governance_Migration_Protocol.md | 198,207 | R-3 (largest file; in-body version history; Last Audit cell accumulating Prior narratives) |
| Routing.md | 186,953 | R-2 (56,490-char header block, 27 retained "Prior:" narratives; no root log home) |
| Architecture/Forge_flow.md | 180,960 | R-1 queue only |
| Admin/Auditor_Protocols.md | 158,871 | R-1; its own log home is itself past T1 (R-6) |
| Admin/Ethical_Constraints.md | 153,308 | R-1 queue only |
| Admin/Progress_Log.md | 132,452 | R-1 (rotation home exists; body still past T1) |
| Admin/Governance_Charter.md | 131,691 | R-1 (changelog exists at 79 KB) |
| Admin/Security_Protocols.md | 121,828 | R-1; R-5 class (Last Audit cell) |
| Unknowns.md | 115,332 | R-1 (version block already current-only) |
| Admin/Repository_Integrity_Protocol.md | 114,889 | R-1; R-5 class |
| Architecture/Chemistry.md | 108,107 | R-1 queue only |
| Admin/Canonical_Terms.md | 100,570 | R-1; R-5 class |
| Admin/ALogs/Progress_Log_Changelog.md | 289,199 | R-6 (a log home itself past T1) |
| Admin/ALogs/Auditor_Protocols_Logs.md | 202,280 | R-6 (a log home itself past T1) |
| Archive/Logs/Unknowns_Changelog.md | 192,297 | R-4 (a live log in Archive/, still receiving entries) |

Fifteen files, about 2.49 MB combined, all past the size bar the repository set for itself in the ratified Log-Split Rule. Nearby but under the bar (context only): Computational_Institutional_Reasoning.md 91 KB, Discovery.md 75 KB.

## Reduction points

### R-1 — The T1 split queue is real, growing, and tracked nowhere live (F-FT-3, quantified)

CAMPAIGN4_AUDIT_05 F-FT-3 already recorded the tension: the split-queue deferral "lives only in the maintenance record." This census quantifies it: fifteen files past T1 at `cea3d8e2`, and the queue has no live home. R8 executes splits at each file’s next substantive touch, so nothing is violated — but nothing tells the next touch that the file is queued.

**Ruling lines (pick one):**

- **R-1a. RATIFY the derived roster:** add a size-census (T1) check to Automation/integrity_check.py’s C-rules so the queue self-reports every run. Derived from live files, never maintained by hand (MAINT-89 strike precedent); the C7/C8 precedent shows checker additions go through him.
- **R-1b. RATIFY the roster as a dated appendix to this brief** (a frozen snapshot, re-derived at each future C-rules run).
- **R-1c. HOLD** (R8’s next-touch mechanics are sufficient; no roster).

### R-2 — Routing.md: a 56 KB header of accumulated pass narratives, and no log home for a root file

Measured at `cea3d8e2`: the block before the first section heading is 56,490 characters — about 30% of the file — holding the current "Last updated" narrative plus 27 retained "Prior:" full-paragraph narratives; the file tail carries dated historical notes back to 2026-08-09. Each MAINT pass that touches Routing prepends another narrative that stays. Routing.md has no <FILE>_Log.md home: R8 names per-folder <Letter>Logs/ homes, and the root has none.

**Reduction (R3/R8/Size-Rule-2 mechanics):** at next touch, move the Prior narratives and tail history notes verbatim to a Routing log home; keep the header to the current-version narrative plus a pointer line.

**Ruling lines:**

- **R-2a. RATIFY with a root home** (for example Logs/Routing_Log.md; requires naming the root home — a small R8 amendment).
- **R-2b. RATIFY with the log in Admin/ALogs/** (cross-folder; needs an R8 note recording the exception).
- **R-2c. HOLD.**

### R-3 — Governance_Migration_Protocol.md: full in-body version history in the largest file

The Status section carries the complete v0.3 through v0.9 version entries in-body — the same block the 2026-11-11 tail restoration (MAINT-130 Item 9a) had to repair from git, itself evidence the block is handled often and at risk. Its File State Last Audit cell additionally accumulates "Prior:" narratives (the R-5 pattern). No GMP log home exists.

**Reduction:** relocate the version entries verbatim to a GMP log home under Admin/ALogs/ (the Kit v1.27 history-relief pass of 2026-10-29 and Unknowns Rule 4 are the precedents), pointer and dated Resolution Log entry left in the file.

**Ruling lines:** **R-3a. RATIFY** (relocation as above) / **R-3b. HOLD** (the Status block’s maintain-or-retire question, Progress_Log PKC-002, is already open — rule that first).

### R-4 — Unknowns_Changelog.md is a live log living in Archive/, past T1

Archive/Logs/Unknowns_Changelog.md (192,297 bytes) still receives entries (v5.81 landed in MAINT-130). R8 froze the existing Archive/Logs changelogs "in place" and relocated only the five Admin-owned ones — but this file is not frozen history; it is the live companion of a root file, and Archive/ is the append-only prior-state home. The split-brain is visible in Unknowns.md’s own header, which routes to the Archive path.

**Ruling lines:**

- **R-4a. RELOCATE** to a root log home (R8 amendment note, dated RL entry, the Archive copy untouched with a pointer — pointer-not-mirror, MAINT-71).
- **R-4b. RATIFY AS EXCEPTION** (recorded on R8’s exception list; the file stays in Archive/ by rule, not by drift).
- **R-4c. HOLD.**

### R-5 — The MAINT-56 retirement is incomplete, and Last Audit cells regrew into narrative bulk

MAINT-56 (2026-11-04) retired the Last Audit/Auditor File State rows across the enforcement set (checker rule C4 retired with them). Campaign 4 then found retired rows still carried in at least nine files (F-FAK-1, F-CT-5, F-SEC-4, F-ISP-4, F-EXP-3, F-IIL-3, F-NT-5, the F-ENV-6 family, F-RM-1’s Last Audit cell), and MAINT-132/133 prepended new Last Audit/Auditor narratives in Security_Protocols, Cognitive_Salvage_Layer and Cognitive_Frameworks. In Governance_Migration_Protocol.md the Last Audit cell itself accumulates "Prior:" narratives — the Routing-header growth pattern, inside a table cell. The full accounts already live in each file’s Resolution Log; the cells duplicate them.

**Reduction:** a one-line Last Audit cell format (date + seat + Resolution Log entry pointer); the full narrative stays in the RL; the MAINT-56 retirement is completed file-by-file at next touch, heaviest first, never in bulk. This also resolves the F-FAK-1 tension (required fields missing while retired rows are carried) under one convention.

**Ruling lines:**

- **R-5a. COMPLETE THE RETIREMENT** (one-line cells; next-touch rollout).
- **R-5b. RATIFY NARRATIVE CELLS** with an explicit length cap (the practice becomes the rule).
- **R-5c. HOLD** (the Campaign 4 findings stand; no remedy).

### R-6 — The split log homes are themselves past T1

Admin/ALogs/Progress_Log_Changelog.md (289,199 bytes) and Admin/ALogs/Auditor_Protocols_Logs.md (202,280 bytes) are the destinations the split rule built, and they now exceed the same 100 KB bar. File_Template names "whole-log split triggers" for logs; the mechanics for splitting a log home (volume or year segmentation with pointer rows) are not yet specified.

**Ruling lines:** **R-6a. RATIFY whole-log split mechanics** (segment at next touch, naming per R8, pointer rows left) / **R-6b. ACCEPT AS HONEST** (log homes are Historical by definition; their size costs no audit purity — the T2 rationale does not reach them) / **R-6c. HOLD.**

### R-7 — VibesSandbox-side observations (home turf; smaller rulings, nothing enacted)

- **STATE.md, 83,010 bytes:** the bootstrap card accumulates a retained-heads block plus an update note per pass. The card’s purpose (bootstrap in one read) degrades as it grows. Options: (i) cap the retained-heads block — keep the last three, move the rest verbatim to a dated appendix file; (ii) cap the update notes the same way; (iii) leave as-is and revisit at the C3 review (~2026-11-30), where the log-surface questions are already parked.
- **Snapshot zips:** Maintenance/LazarusForge-1.36.Alpha.zip (3.7 MB) continues the MAINT-71/72 snapshot practice; the re-snapshot trigger is preregistered and pointer-not-mirror exists. Observation only: a keep-latest-plus-pointers convention for future zips is available if wanted; not proposed as a ruling item.

### R-8 — What not to reduce (the fidelity guard list)

Reduction that deletes, summarizes, or rewrites is out of scope by house rules (R3). Specifically protected, not candidates:

- Archive/ frozen history, the frozen MAINT_LOGs, the SESSION_STATUS terminal notes (PKC-007).
- The Campaign 1–4 audit deposits and the aggregates (findings-only records, PKC-020).
- The sidecar Last Reviewed tables (load-bearing for the D-3 owed-review routing).
- The per-entry MAINT files, MAINT_INDEX, and STATE’s append-only notes (the MAINT-69 architecture).
- The Unknowns.md active index body and the Automation/ scripts (both registered; the Candidate3 base/hybrid pair and its zip are documented and were ruled 2026-10-26).

## Non-duplication check

- F-FT-3 (split-queue tension): referenced and quantified in R-1, not re-made.
- F-PL-2 (rotation): already executed (MAINT-133 item 9c); its mechanics are cited, not re-proposed.
- The retired-rows findings (F-FAK-1 and kin): stand as logged; R-5 proposes the remedy only.
- MAINT-87’s VS open items (RELEASES register, VS de-duplication, the SESSION_STATUS T1 split): the split closed in MAINT-90; the other two remain open there and are not re-proposed here.
- The C3 review (~2026-11-30) holds the EVENT_LOG (Option C) and first-Brief Item 7 B/C questions; R-7’s STATE options defer to it rather than preempt it.

## Resume point

Each reduction executes only on his ruling line; R8’s next-touch discipline governs all sequencing; the heaviest-first order is proposed, not enacted. Next ID: MAINT-135.
