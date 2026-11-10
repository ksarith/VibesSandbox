# MAINT-105 — Campaign 4 AUDIT_16 landing (Admin/PROBE_INVOCATION.md)

Date: 2026-11-10. Actor: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.

## What landed

- LazarusForge commit `6763b5f6` (single commit, message "Campaign 4 sweep: CAMPAIGN4_AUDIT_16 (Admin/PROBE_INVOCATION.md) findings-only deposit + kickoff tracker addendum 14 (PKC-020; no audited-file fields advanced)"):
  - `Admin/AAudits/CAMPAIGN4_AUDIT_16_Admin-PROBE_INVOCATION.md` — 12,453 chars, SHA-256 `657868aa71ca16b2e0597e751fe2af286d68f5ba61cba493fe82f1b087026c22`.
  - `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — tracker addendum 14 appended, 34,640 chars (was 32,448), SHA-256 `55cdd18f80279dd7a677a763b84240146b47d7c9b811283b2a17e358088b2c31`.
- Post-push byte verification: both files re-fetched at head `6763b5f6`; the deposit byte-matches the compose record (12,453 chars, all F-PI markers present); the kickoff's first 32,448 chars (the pre-addendum content) are byte-intact (append-only verified); kickoff addenda 12, 13, and 14 all present; the resume point reads Admin/BATTERY_SEED.md (CAMPAIGN4_AUDIT_17).
- Audited-file SHA-256: `Admin/PROBE_INVOCATION.md` at `aa35b129` = `e329cb4cb34aa918d8aa353ec5925db5f4c054dde5f092b3d416ddc1856dee46` (20,554 chars / 168 lines, fetched complete).

## Findings recorded (F-PI-1 through F-PI-6; Compound Drift Rule vacuously did not fire)

- F-PI-1 WARNING (cross-file; the source-prevails chain terminates in a stale destination): How-To step 4 logs "per the Invocation Record fields in `Admin/Auditor_Protocols.md` §Mission Drift Review", but that live subsection still routes records to the pre-relocation `Archive/Logs/Auditor_Protocols_Logs.md` — v0.29 text written 2026-07-26, three days after the 2026-07-23 relocation; the 2026-10-31 repair fixed PROBE's step 4 but not the governing source subsection, and on conflict the source prevails by the file's own fence; CAMPAIGN4_AUDIT_01 did not record it; relocation-repair-miss, Pattern 2 instance 12.
- F-PI-2 NOTE (the CAMPAIGN_AUDIT_30 F2 four-labels-vs-five evidence-scale divergence unremedied at v1.4; folds into the F-ISP-6 class-6 harmonization option).
- F-PI-3 NOTE (Derived-from pins AP v0.31 vs live v0.47 — the CAMPAIGN_AUDIT_30 F5 recurrence, the F-FAK-6 class; mitigated by the source-prevails fence).
- F-PI-4 NOTE (unqualified colliding-range "MAINT-15" citation in the operative Last Audit cell — MAINT-15 exists in both frozen logs with different content; the content uniquely identifies LOG-1029's; the cell predates MAINT-63's straggler batch and is not in its touched-file list; batch-eligible sixth evidence point for the bare-citation grep remedy).
- F-PI-5 NOTE (MAINT-56-retired Last Audit/Auditor rows carried, conformant-at-touch — latest write 2026-10-31, before the 2026-11-04 retirement).
- F-PI-6 NOTE (Verification Ref = single AP section, not FT-mandated Verification_Gates.md — the recorded class-6 family, third instance per ISP's v1.0.2 RL record).
- Aging Rule vacuous (0 open unknowns — the campaign's sixth no-trip control case; the mechanism-level unknown AP-030 verified open and aging at AP); Compound Drift Rule vacuously did not fire (class 6, no indicators).

## Verification record

- FT exemption class 6 confirmed live ("Operational seeds and invocation templates" — PROBE_INVOCATION named verbatim; verified during AUDIT_15); template checks adapted, absent sections not findings.
- Source reconciliation performed in full against AP v0.47 §Mission Drift Review: Trigger Cadence (5/60d) matches How-To step 1; the eight axiom names match AP Phase B and the Charter's FROZEN Tier 1 block ("Axiom P-1 — Preservation of Life", line 101); the Silent→Atrophied quoted rule matches; the log-derived counter design matches.
- The step-4 destination verified live: `Admin/ALogs/Auditor_Protocols_Logs.md` (199,945 chars) carries the AP-030 Invocation Record, the Cycle 1 record and the second-rater record; `Automation/cold_session_bundler.py` present (16,295 chars, implements AP-017).
- The v1.4 fixes in place (blank output cells; Cycle 1 ratings restored to the appendix, consistent three ways with the RL and the sidecar record); the v1.3 blanking rules present in step 3 and the appendix note; the v1.4 entry's "CAMPAIGN_AUDIT_30 did not mention it" claim verified true against the 2026-10-29 report.
- Discovery snapshot parity: PROBE_INVOCATION row reads Draft with the same Spec Gates wording — File State and snapshot agree (contrast F-ISP-1).
- X10 three-way parity exact (0 = 0 = AP-030 mechanism-level); Ethical Anchor exact; both ==== delimiters present; the 2026-10-29 MAINT-15 instrument change corroborated by the MAINT_INDEX LOG-1029 row.

## Disclosures

- Event: (ii) recurrence — the stale-pin class (F-PI-3, CAMPAIGN_AUDIT_30 F5), the evidence-label vocabulary divergence (F-PI-2, CAMPAIGN_AUDIT_30 F2), the retired-rows class (F-PI-5) and the recorded Verification Ref family (F-PI-6, the F-ISP-6 class) all recurred; one new Pattern 2 instance established (F-PI-1, instance 12).
- Adjacency disclosed in the deposit: Vibe lines authored this file's v1.2–v1.4 passes and its Last Audit cells; those records are audited as third-party content; the pass is non-independent with respect to this line's own repairs.
- No tooling defects this pass: all fetches arrived plain; the SHA-256 implementation reused unchanged, the sanity vector passing before use.
- Out-of-scope observations recorded in the deposit: Status remains "Draft" while the instrument has a completed human-ruled Cycle 1 (File State and Discovery agree; any promotion mirrors AUDIT_31 F2 and is the human's alone); AP-030's sidecar entry still has no field table (the AUDIT_01 F4 recurrence, AP's audit record).

## Next

- CAMPAIGN4_AUDIT_17: `Admin/BATTERY_SEED.md` (FT exemption class 6 — seed payload; template checks adapt).
- Next IDs: MAINT-106; Intake Log entry 22 (still untouched this campaign).
