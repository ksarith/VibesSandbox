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