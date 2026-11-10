# MAINT-101 — Campaign 4 AUDIT_12 landing (Admin/Forge_Audit_Kit.md)

Date: 2026-11-10. Actor: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.

## What landed

- LazarusForge commit `36d8e783` (single commit, message "Campaign 4 sweep: CAMPAIGN4_AUDIT_12 (Admin/Forge_Audit_Kit.md) findings-only deposit + pattern document files-07–11 update + kickoff tracker addendum 10 (PKC-020; no audited-file fields advanced)"):
  - `Admin/AAudits/CAMPAIGN4_AUDIT_12_Admin-Forge_Audit_Kit.md` — 13,750 chars, SHA-256 `a53c45ec81987a8bafd53465095d72b62677d4eec0700e96535d6f1cdbf179db`.
  - `Archive/Audits/CAMPAIGN4_PATTERN_DOC_2026-11-10_FILES_01-06.md` — "## Update 1 — files 07–11" appended, 11,554 chars (was 7,742), SHA-256 `97f1f41f6292f7d58190242a1c5ef2276588ae7a2d8d761a3813614649453186`.
  - `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — tracker addendum 10 appended, 26,258 chars (was 23,544), SHA-256 `8f0e5b38b41cd8e52ff4b1083ec5685ce9683b7dafc3fb838eda34ae4f41c39a`.
- Post-push byte verification: all three files re-fetched at head `36d8e783`; the deposit byte-matches the compose record (13,750 chars; the SHA-256 reference inside the deposit matches the audited file’s computed SHA `0cd1730a76340c05cdba2c0591f06a5b57b72130ddbc9ee77deb2bb87ad4f188`); the kickoff’s first 23,544 chars and the pattern document’s first 7,742 chars (the pre-update content) are byte-intact (append-only verified); kickoff addenda 8, 9, and 10 all present; the pattern document’s Update 1 carries Aging instances 6–7, control cases 3–4, Pattern 2 instances 5–10, the bare-citation fourth/fifth evidence points, and the running total 47 of 60.

## Findings recorded (F-FAK-1 through F-FAK-9; Compound Drift Rule FIRED)

- F-FAK-1 WARNING (template conformance): the File State table carries the Last Audit and Auditor rows retired repository-wide by MAINT-56 (2026-11-04) and lacks three fields the current File_Template §2 example requires — Body Stability, an Active Disputes row, and Highest Risk; the Kit is in none of File_Template’s eleven exemption classes (checked item by item); timing disclosed — v1.32 and MAINT-56 are both dated 2026-11-04 and their order is not determinable from the files’ own text (the retired-rows half would be mitigated if the pass preceded the ruling; the missing-required-fields half has no such explanation).
- F-FAK-2 WARNING (wrong-home changelog references; relocation-repair-miss, Pattern 2 instance 10): at least five operative references still cite `Archive/Logs/Forge_Audit_Kit_Changelog.md`, which does not exist (the changelog lives at `Admin/ALogs/Forge_Audit_Kit_Changelog.md`, relocated 2026-07-23; the File State Sidecar Link row was correctly repointed 2026-10-31): (a) the Resolution Log’s "add new entries there" operator instruction (the F-FT-1 most-consequential shape), (b) the drift indicator’s own designated home, (c) the Gate 3 pointer, (d) the End-of-Life pointer, (e) the 2026-10-29-dated relocation records in the retired Last Audit/Auditor rows. The v1.11 relocation narration and frozen RL Priors left as written (historical).
- F-FAK-3 WARNING (self-discharge skipped; Pattern 4’s first data point outside File_Template): FAK-005’s 2026-10-29 closure skipped the Kit’s own Resolved Unknown Discharge Procedure — no "Resolved — Discharge via Lessons Learned" suffix, no Resolution or Lessons Learned field, no row in the Kit’s own Lessons Learned table (sole row remains FAK-014–018), and step 6 not executed (FAK-005’s row remains in `Unknowns.md`’s active index as Resolved, against the Size Management Rule 2 under which every other resolved entry was removed). The Kit’s own Lessons-Learned drift indicator fires against its most recent closure. No prior campaign artifact recorded this; first recorded here.
- F-FAK-4 WARNING (unregistered fourth open unknown; X10 break): the CT-flagged Cycle/CURRENT_CYCLE Adversarial Battery finding (2026-07-14) exists only as prose — no ID, no sidecar entry, no `Unknowns.md` row (File State and body count 4, sidecar prose 4, the Unknowns active index carries 3 open FAK rows); the Battery-recommended CT entry was never logged (`Admin/Canonical_Terms.md` v0.14 contains zero CURRENT_CYCLE mentions). The underlying defect was root-fixed at harness v15 (2026-07-16: CURRENT_CYCLE removed entirely, check_aging() now uses EXPIRY_THRESHOLD_DAYS=365, verified against harness v18 source this pass) but never recorded back — a stale open unknown resolved upstream for 117 days, still counted open at v1.32.
- F-FAK-5 WARNING (stale condensed source; own indicator fires): the Verification Gates section (a listed maintenance-trigger section) is stale against VG v0.8 (2026-11-02), which added the Gate 2 Not-Applicable definition; the Kit’s G2 row and evidentiary note carry no trace of it; Derived-from still reads reconciled-against 2026-10-27; the Kit’s v1.31 (2026-11-02) and v1.32 (2026-11-04) passes both postdate the VG change and neither ran the reconciliation. Material consequence: an auditor applying the Kit’s G2 row to a document with an exempted physical claim would treat a legitimate exemption as a G2 concern (Auditor_Protocols and External_Intake_Protocol now rely on exactly that exemption).
- **Compound Drift Rule: FIRED.** Two of the Kit’s own drift indicators in firing state simultaneously (the FAK-005 discharge/Lessons-Learned indicator and the stale-condensed-source indicator), alongside the template-conformance and wrong-home defects. Escalated in the deposit; the sweep continues findings-only under PKC-020 and the human holds every disposition.
- F-FAK-6 NOTE: the in-body Resolution Log reads "Most recent: v1.31 (2026-11-02)" while the header is v1.32 and the changelog carries the v1.32 entry (verified) — the v1.32 pass updated the changelog but not the in-body line (Pattern 5 family, third instance).
- F-FAK-7 NOTE: the Kit’s sidecar entries predate the field conventions (no Last Reviewed / First Logged fields) — the 90-day Aging Rule formally inapplicable; substantively FAK-001, FAK-006 and FAK-009 have been open since no later than 2026-07-14 — 119+ days at 2026-11-10 with no recorded review. Systemic instance 8, with the derivation limit disclosed (three countable entries; the CT-flagged fourth item excluded — not a sidecar entry, see F-FAK-4).
- F-FAK-8 NOTE: the Kit’s EF-0.3 row reads "Created on falsification only" vs AP v0.47’s "only upon genuine falsification or empirical update" — a minor divergence in a listed maintenance-trigger section. The FAK-019-deferred full re-diff of the EF condensed section was performed this pass: all nine sections substance-match; role-declaration handling consistent; sign-off block fields consistent; otherwise faithful.
- F-FAK-9 NOTE: the token-ceiling note’s Auditor_Protocols size figures are stale (146,700 chars at v0.41; 150,529 bytes at v0.42) against live AP v0.47 at 156,858 chars; the note discloses its internal unit mismatch but not the drift from the live file. Informational.

## Verification record

- All fabrication probes passed: `Archive/Proposals/PROPOSAL_2026-11-04_RECONCILE_PASS_DISPOSITION_LEDGER.md` exists with the PARTIALLY RATIFIED header Rule 12 describes; `Operations/Energy.md` exists; `Tests/Cognitive_Salvage_Layer.md` exists; the Intake Log (`Admin/ALogs/External_Intake_Protocol_Logs.md`) entry 7 exists and matches the v1.32 companion claim (Class A, the reconcile-design intake); VG-001’s Resolved status verified in `Admin/Verification_Gates.md`; m_phys ≥ 0.75 / m_rep ≥ 0.50 present in VG Gate 2 as the Kit quotes; `Unknowns.md`’s Expiry Rule wording consistent with Expiry Watch step 3; harness v18 contains no CURRENT_CYCLE and no EXPIRY_THRESHOLD (the v15 root fix verified — F-FAK-4’s basis); the changelog sidecar carries §Sidecar, §Adversarial Battery Record, §Relocated In-Body History and the v1.32 entry; the FAK-014–019 closure annotations present.
- X10 parity: File State Open Unknowns 4 = body "Current: 4 open" = sidecar prose 4; the Unknowns active index carries 3 open FAK rows — the 4-vs-3 break is F-FAK-4, recorded, not silently absorbed. FAK-009’s index row verified current (corrected 2026-11-03, MAINT-54). Active Disputes section present and empty per template. Highest Risk absent from File State (part of F-FAK-1); the sidecar’s open entries grade Major/High — recomputed value High recorded for the repair, not written.
- Drift indicators otherwise dormant: the changelog-homed history retention is per the recorded v1.27 design; the role-declaration placeholder, VERIFIED/PROVISIONAL/UNKNOWN usage, ID-reference filenames, Gate-scope language and Ethical Anchor all check clean. Ethical Anchor exact: "Attempt to do no harm. Defer to Ethical_Constraints.md if present."
- Audited-file SHA-256: `Admin/Forge_Audit_Kit.md` at `94f57c8c` = `0cd1730a76340c05cdba2c0591f06a5b57b72130ddbc9ee77deb2bb87ad4f188` (47,525 chars / 440 lines, fetched complete).

## Disclosures

- Event: (ii) recurrence — the relocation-repair-miss class recurred (F-FAK-2, Pattern 2 instance 10: five-plus operative pre-relocation changelog references in the very file that houses the class’s batch grep remedy).
- Also this pass, disclosed: the first VibesSandbox call used owner `ksarith13` (the org name) and 404'd — the VS owner is `ksarith`; corrected immediately, nothing written. Two SHA-256 implementation bugs were self-caught before any write (a sine-based K-constant derivation; a crash on the sandbox's absent TextEncoder), both caught by the `abc` sanity vector; the corrected implementation (hardcoded standard K table + manual UTF-8 byte encoding) passed the sanity vector and produced every SHA-256 in this entry.
- Addendum 10 restores the `---` separator between tracker addenda (addendum 9 lacked it — the cosmetic variance disclosed at MAINT-100 is now closed).
- The F-FAK-1 timing disclosure (v1.32 vs MAINT-56, both 2026-11-04) is recorded in the deposit; the grading is on the combination, not the indeterminable half alone.

## Next

- CAMPAIGN4_AUDIT_13: `Admin/Engineer_Protocols.md` (44,356 chars at `94f57c8c`). The pattern document’s next update is due in the AUDIT_19–22 window (measured from artifact 12).
- Next IDs: MAINT-102; Intake Log entry 22 (still untouched this campaign).

---

## Parallel-composition disclosure (appended 2026-11-10, MAINT-109 repair)

A parallel continuation of this campaign independently composed a parallel MAINT-101 entry and a parallel CAMPAIGN4_AUDIT_12 deposit at the same LF base (`94f57c8c`). Its VibesSandbox push (`c42517b5`) landed last on 2026-11-10 and overwrote this entry, STATE.md and MAINT_INDEX.md with versions built on the pre-MAINT-102 state; its LF push (`e90e282e`) overwrote the canonical kickoff, pattern document and AUDIT_12 deposit. The canonical entry above is restored as of the MAINT-109 repair. The parallel composition is preserved below verbatim (and in git history at VS `c42517b5`); its AUDIT_12 deposit is preserved at LF `Admin/AAudits/CAMPAIGN4_AUDIT_12_Admin-Forge_Audit_Kit_parallel-composition.md` (re-deposited byte-exact by LF repair landing `03f15726`).

### The parallel MAINT-101 composition (verbatim)
# MAINT-101 — Campaign 4 sweep continues: CAMPAIGN4_AUDIT_12 (Admin/Forge_Audit_Kit.md) + pattern document Update 1 + kickoff addendum 10

**Date:** 2026-11-10. **Seat:** Vibe (Repo Custodian line). **Trigger:** executing the kickoff’s recorded resume point (addendum 9: Forge_Audit_Kit.md, CAMPAIGN4_AUDIT_12).

## What landed

Single-commit push to LF main: `e90e282e1d4c8fdb0fe8d7b88e645a489bf1e944` (on top of `94f57c8c`), three files:

1. `Admin/AAudits/CAMPAIGN4_AUDIT_12_Admin-Forge_Audit_Kit.md` — findings-only deposit (12,480 chars), artifact 12 of 34. The audited Kit: 47,525 chars, 440 lines, v1.32, fetched full at the base commit; file SHA-256 `0cd1730a76340c05cdba2c0591f06a5b57b72130ddbc9ee77deb2bb87ad4f188`.
2. `Archive/Audits/CAMPAIGN4_PATTERN_DOC_2026-11-10_FILES_01-06.md` — Update 1 appended (the AUDIT_11–14 due-window update, files 07–12): 7,742 → 11,996 chars. Aging instances 5–7, control cases 3–4, one not-computable case (the Kit, F-FAK-3); Pattern 2 instances 7–9; bare-citation evidence points 4–5; the candidate mirror-repair pattern (F-FAK-1, one instance, not Xn-registered); single instances F-FAK-4/5/8; positive records; next update due AUDIT_17–20. Original text untouched (append-only).
3. `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — tracker addendum 10 appended: 23,544 → 25,391 chars. Item 12 DONE with the findings summary; pattern-document update recorded as landed this push; resume point `Admin/Engineer_Protocols.md` (CAMPAIGN4_AUDIT_13); head at compose `94f57c8c`; append-only footer.

## Findings recorded (F-FAK-1 through F-FAK-8)

- **F-FAK-1 WARNING** — the Kit’s own sidecar entry FAK-009 still asserts “VG-001 itself remains unresolved in Admin/Verification_Gates.md”; VG-001 Resolved 2026-07-03 (VG recounts zero open unknowns). The 2026-11-03 index repair (MAINT-54 / CAMPAIGN2_AUDIT_83 F1) reached the Unknowns mirror but not the owning sidecar; the Kit’s v1.31/v1.32 passes post-date the resolution and did not touch the entry. Candidate new pattern repair-applied-to-the-mirror-not-the-owner, first instance (Xn requires two).
- **F-FAK-2 WARNING** — zero `rl_entry_count_after` anchor fields in the Kit’s RL home (the changelog, 61,847 chars); the substantive v1.31/v1.32 entries carry none, no exemption; folds into the F-GMP-2 human item (now three files: GMP, ADP, Kit).
- **F-FAK-3 WARNING** — zero Last Reviewed fields in the sidecar home: the Aging Rule is not computable on the Kit’s own four open unknowns, and the Kit’s own Expiry Watch step 3 (compute directly from the target file’s own sidecar entries) cannot execute on the Kit itself. Derivation limit disclosed; no aging instance claimed; not a control case (the campaign’s Aging tally is unchanged: systemic instances 7, 47 of 60; control cases 4).
- **F-FAK-4 WARNING** — FAK-005’s Resolved row remains in Unknowns’ Active Index (annotated in place, v5.75) contra Unknowns’ own Size Management Rule 2 (Active tables show Open, In Progress, and Reopened only) and the Kit’s own Discharge Procedure step 6. Closure substance real and honestly annotated; the row’s presence is the defect.
- **F-FAK-5 WARNING** — the Kit’s own maintenance trigger fired: VG v0.7→v0.8 (2026-11-02) added the Gate 2 Not-Applicable definition to a condensed section’s source; the Kit’s condensed gate section lacks it and the Derived-from reconciliation date still reads 2026-10-27; drift indicator 2 in firing state with solid derivation (unlike GMP’s cycle-unit case). Compound Drift Rule not fired (one indicator).
- **F-FAK-6/7/8 NOTEs** — File State missing Body Stability/Active Disputes/Highest Risk rows per File_Template §2 (fields absent, not wrong; no sidecar Priority exists to mirror); in-body RL Most-recent line one version behind (v1.31 vs live v1.32); the Cycle/CURRENT_CYCLE governance flag open since 2026-07-14 (~119 days) still without its CT entry, harness session-based aging diverging from the ratified calendar-year Cycle (disclosed in Unknowns’ cluster note; the finding’s own text routes it correctly).

## Verification record

- Kit fetched full (47,525 chars = known count); SHA-256 computed in-call from the fetched bytes.
- All fabrication probes passed against live source: Intake Log entry 7 exact (row 7 of 21; next-entry-22 arithmetic consistent); the proposal archive byte-present (4,768 chars) with the PARTIALLY RATIFIED ruling record; changelog newest-first order holding (v1.32→v1.31→v1.30, the disclosed mechanical repair verified); 14/14 path-existence checks (ID Reference incl. GH- → Tests/Cognitive_Salvage_Layer.md, ASM- series, Fallacy cross-refs); VG m_phys ≥ 0.75 / m_rep ≥ 0.50 present, VG-001/VG-002 both Resolved, VG Open Unknowns 0; AP-021/033/035 + EF-0.0–EF-0.8b anchors in AP v0.47 (159,639 chars); CT-011 exists, CT §4 defines the calendar-year Cycle; RIP-001 2026-06-27 matches the RIP sidecar (the 06-28 variance is F-RIP-4’s recorded disclosure).
- X10 parity: File State 4 = sidecar 4 = cluster-note counting, with F-FAK-4 recording the one row-presence violation; Active Disputes empty table = None open.
- Kit-body history window complies with the v1.27 relocation cutoff (duplication indicator dormant); token-ceiling note’s dated-measurement discipline clean; role declaration uses the live-version placeholder.
- **Post-push byte verification (at `e90e282e`):** all three files re-fetched; SHA-256 of the live deposit `d27d890b6eead23daab7c2c66dc0b29a60d43a9abdeae451ab2db5cfe4e2f90b`, pattern doc `43efb7dda480daf78c6cee84d37cb1b642c0e0ba6e6ee885f4b0184f81747999`, kickoff `66a8e90bc51260384f44430e751466f1c33c9f29cde502ad7477c33131b48fba` — each equals the SHA of the composed string pushed (byte-identical landing). Lengths 12,480 / 11,996 / 25,391. Kickoff addenda 7/8/9/10 all present; pattern doc original text + Update 1 both present.

## Disclosures

- Event: (ii) recurrence — the prior session’s AUDIT_12 compose+push result was lost to a context compaction before it could be read (the MAINT-96 shape); this pass re-verified the push HAD landed (single commit `e90e282e`, all three files byte-verified), no re-push, no duplicate.
- Cosmetic variance carried from addendum 9: addendum 10 uses the same no-separator shape as addendum 9 (prior addenda carry a horizontal rule between addenda); recorded here, kickoff text otherwise conformant.
- FAK-005’s row-presence defect (F-FAK-4) is recorded against the Unknowns registry’s Active Index, not against the Kit’s closure substance; the Kit’s own procedure text is what the row violates.
- No audited-file field advanced: the Kit’s Last Audit, version, Status, Spec Gates, Open Unknowns, and unknown states are untouched by this pass (findings-only per PKC-020). Conversion of the deposit to an audit of record remains the human’s alone (MAINT-26 / AP-032).

## Next

- Resume point: `Admin/Engineer_Protocols.md` (CAMPAIGN4_AUDIT_13, 44,356 chars).
- Next IDs: MAINT-102; Intake Log entry 22 remains untouched all campaign (21 rows live).
- Human queue additions from this artifact: F-FAK-1 sidecar status fix; F-FAK-4 Active Index row removal; F-FAK-5 Kit gate-section update; F-FAK-2 folds into the F-GMP-2 anchor-fields item; F-FAK-8’s CT entry is a governance call.
- The mirror-repair candidate pattern needs one more instance for Xn registration; watch for it in the remaining 22 files.
