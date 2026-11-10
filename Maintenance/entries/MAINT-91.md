# MAINT-91 — Campaign 4 opened: adversarial sweep of Admin/ (findings-only)

**Date:** 2026-11-10
**Direction (human, verbatim):** "The adversarial pass is needed throughout the repository. Can you preserve your findings and then start a sweep of adversarial passes for the admin folder?"
**Seat:** Vibe (GLM 5.3 Flash architecture), co-author mandate; auditor-pass discipline observed (findings-only per PKC-020; nothing enacted; no Last Audit, version, Status, gate, or unknown advanced on any audited file).

## What landed

**LazarusForge, two commits, audit artifacts only (deposit carve-out):**

1. **LF `b7cdecf8`** (on top of `242eabd2`, the MAINT-90 head, verified unchanged at compose):
   - `Admin/AAudits/CAMPAIGN4_AUDIT_01_Admin-Auditor_Protocols.md` — the 2026-11-10 session's audit of `Admin/Auditor_Protocols.md` v0.47 preserved verbatim as findings: checks 1–11 (all VERIFIED CLEAN except as noted), findings F1 (bare `Forge_Net.md` path in Scope Boundary, WARNING), F2 (Unknowns.md active index lists 9 AP rows vs File State's 10 — Rule 7 side undecided, WARNING), F3 (90-day Aging Rule tripped on 8 of 10 open AP entries, WARNING), F4 (AP-030 sidecar entry has no field table, NOTE), F5 ("companion doctrine repository" self-reference ambiguity, NOTE), F6 (20% Metadata Guardrail's interaction with relocated sidecars unstated; sidecar 56% of combined word count, NOTE). The AP sidecar SHA-256 was independently recomputed this session and matches the recorded `c68ed28a…` exactly — the AP-036 recompute-on-log remedy verified holding.
   - `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — Campaign 4 definition: 34-file Admin/ scope (constitutional core first), per-file method (Auditor Prompt §3.3 checks 1–11 derived from live source + adversarial probes: fabrication, self-attestation, tamper, staleness, X10/X11 watches), grading and escalation rules, TWGW discipline, and the sweep tracker/resume point (SESSION_STATUS stays retired per MAINT-69; the kickoff artifact is the tracker).
2. **LF `d098543d`**: `Admin/AAudits/CAMPAIGN4_AUDIT_02_Admin-Ethical_Constraints.md` — adversarial pass on `Admin/Ethical_Constraints.md` v0.18: checks 1–11 (VERIFIED CLEAN except as noted; GOV-019 citation verified resolving in the Charter's relocated sidecar, not dangling; Security_Protocols still Draft/0-6 so its gating indicator remains live), findings F-EC-1 (stale drift indicator still gating on "before EC-008 is resolved" — EC-008 Ratified 2026-08-22; recurrence of the EC-AUD-003 class, WARNING), F-EC-2 (Aging Rule tripped: EC-006 190 days, EC-015 128, EC-010 93; EC-014 near-trip at 87 — second instance of the systemic pattern, WARNING), F-EC-3 (fabrication probe clean, NOTE).

**VibesSandbox, this commit:** this entry + MAINT_INDEX row 108 + STATE.md update (heads, Last updated, Campaign 4 record line). No Intake Log entry (no external intake this pass).

## Early campaign signal

Both passes completed so far found the repository-wide 90-day Aging Rule tripped (AP: 8 of 10 open entries; EC: 3 of 7). Recorded in the kickoff as a systemic-pattern candidate for one consolidated remedy ruling rather than per-file WARNINGs; the human rules. All other bookkeeping checked (counts, hashes, anchors, version strings, Highest Risk parity) verified clean against live source on both files.

## Disclosures

Event: (iii) harness defect — three harness-side defects this session, none landed anything wrong: (1) the sandbox `sha256sum` binary is non-functional (throws on any input); SHA-256 was computed with a pure-TypeScript implementation verified against the `abc` test vector before use; (2) a filesystem read path truncated the 201,432-char sidecar at exactly 63,637 chars with no usable resume cursor — the same ~63 KB silent-truncation class the Auditor Prompt §2 documents; detected by size comparison and re-fetched complete; (3) the `jq -j` extraction shim emitted JSON-quoted text instead of raw strings (the TWGW-003/PKC-045 lesson class; caught by head-byte inspection, re-extracted with `-r`). Post-push verification: both LF deposits and all three VS files fetched back at their landing heads and checked structurally (head/tail markers, row placement, count lines).
