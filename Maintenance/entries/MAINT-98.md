# MAINT-98 — Campaign 4 AUDIT_09 landing (Admin/Repository_Integrity_Protocol.md)

Date: 2026-11-10. Actor: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.

## What landed

- LazarusForge commit `e63f7904` (single commit, message "Campaign 4: CAMPAIGN4_AUDIT_09 (Admin/Repository_Integrity_Protocol.md) + kickoff tracker addendum 7 (findings-only per PKC-020)"):
  - `Admin/AAudits/CAMPAIGN4_AUDIT_09_Admin-Repository_Integrity_Protocol.md` — 11,354 chars, SHA-256 `72544a08db871176419b1f371078912552a4e1b8e9968d645267371ae157b318`.
  - `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — tracker addendum 7 appended, 19,259 chars, SHA-256 `21e64cfc79bc654da3ea1957484d0c8345b4b9380f998c952b4b8a0918662f0f`.
- Post-push byte verification: both files re-fetched at head `e63f7904`; SHA-256s match the compose-time records; the kickoff retains addenda 4 through 7 (byte-intact). intact: true.

## Findings recorded (F-RIP-1 through F-RIP-6)

- F-RIP-1 WARNING: Unknowns.md's Active Index RIP-005 row still pins "Security_Protocols.md … exists at v0.5" — the exact stale anchor the sidecar's own 2026-09-03 correction (RIP-AUD-004) removed from the sidecar and Status "since the same staleness would recur"; the repair missed the global index. Relocation-repair-miss family (campaign Pattern 2, instance 7); doubly stale per AUDIT_07's finding that Security_Protocols.md carries no current version string at all.
- F-RIP-2 WARNING: Aging Rule tripped 3/5 open entries — RIP-005 (2026-06-19, 144d), RIP-006 (2026-06-27, 136d), RIP-009 (2026-07-09, 124d); RIP-002 (68d) and RIP-007 (86d) clean. Systemic instance 6 of the campaign.
- F-RIP-3 NOTE: RIP-007 sidecar carries a duplicate orphan field table (main table Last Reviewed 2026-06-19; second table only "Last Reviewed 2026-08-16" appended after the Resolution Path). Aging computed on the later addendum (86d, no trip); ambiguity disclosed — if the main table governed, the count would be 4/5.
- F-RIP-4 NOTE: RIP-001 discharge date 2026-06-27 (sidecar) vs 2026-06-28 (Unknowns resolved-entries paragraph) — recurrence of the F-VG-2 class from CAMPAIGN4_AUDIT_04.
- F-RIP-5 NOTE: ~7 bare path citations in operative/narrative text (Integrity_Incident_Log.md ×2, Auditor_Protocols.md ×2, Verification_Gates.md ×2, Security_Protocols.md heading ×1) — MAINT-63's X3 pass covered colliding-ID prefixes only; batch-eligible with the F-SEC-2/F-SP-2 corpus-wide grep remedy (fourth evidence point).
- F-RIP-6 NOTE: Resolution Log ordering slip — the 2026-09-04 entry sits after the backfilled 2026-09-03 entry; ruled historical per the kickoff's PKC-007 standing rule.
- Compound Drift Rule did not fire: none of the file's own 18 Drift Indicators activated.

## Verification record

- Checks 1–11 otherwise clean and unusually strong: X10 four-way exact (File State 5 = sidecar open 5 = Unknowns index rows 5 = the log's own `open_unknowns_after` anchor 5); index Status/Priority parity field-for-field; Highest Risk High recomputes (RIP-005 High); Active Disputes 0 consistent; Ethical Anchor exact; RL anchors verified (18 dated bullets, 1,060 lines, head = Last Audit date).
- Fetched-file SHA-256: `Admin/Repository_Integrity_Protocol.md` at `19ec7fb5` = `d7793a0d66341a211cbcba18cdd719f571746510c52adb9cc01adb5674e4897f` (114,151 chars).
- RIP-002's "3 of 6 live" harness claim verified current against source: harness v18 + audit_lib.py implement exactly Ethical Anchor, required fields, and cross-reference checks; FROZEN validation, navigation spot-check, and sidecar↔index parity absent from both modules.
- Out-of-scope observation recorded in the deposit: UNK-009's span annotation covers resolved GOV-003 but not resolved RIP-001 (Unknowns.md owner pass item).

## Disclosures

- Event: (iii) harness defect — two minor items, both worked around and disclosed in the deposit: (a) `github_app.get_reference` not exposed in this connector build (full head SHA via `list_commits` with `fields:["sha"]`); (b) no client write_file in the run_typescript sandbox (first scratch-save failed; recovered via saved tool-result JSON + jq). Also: one compose call failed pre-push with a TypeError during content assembly (no write occurred); recomposed with per-element type validation and pushed clean. Directory-listing object shape re-confirmed (known class).

## Next

- CAMPAIGN4_AUDIT_10: `Admin/Governance_Migration_Protocol.md` (191,505 chars at the pre-campaign count — largest file in the sweep; two-pass read likely). Cross-file pattern document update due in the AUDIT_11–14 window.
- Next IDs: MAINT-99; Intake Log entry 22 (still untouched this campaign).
