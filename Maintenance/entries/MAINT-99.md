# MAINT-99 — Campaign 4 AUDIT_10 landing (Admin/Governance_Migration_Protocol.md)

Date: 2026-11-10. Actor: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.

## What landed

- LazarusForge commit `e24e443d` (single commit, message "CAMPAIGN4_AUDIT_10: Governance_Migration_Protocol.md adversarial deposit (findings F-GMP-1..7) + kickoff tracker addendum 8"):
  - `Admin/AAudits/CAMPAIGN4_AUDIT_10_Admin-Governance_Migration_Protocol.md` — 13,904 chars, SHA-256 `6a049e738b0f7c47c0dd487a6822f5503037937a383ed5464c746ad4e95007f0`.
  - `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — tracker addendum 8 appended, 22,058 chars, SHA-256 `b12c124630518c6c94dc0b5474cdbd2bb5641390e209730b9b04a567d6ffa341`.
- Post-push byte verification: both files re-fetched at head `e24e443d`; byte-identical to the compose-time records; the kickoff retains addenda 6 through 8 (byte-intact).

## Findings recorded (F-GMP-1 through F-GMP-7)

- F-GMP-1 WARNING (file integrity): the file ends mid-word inside the trailing `## Status` block ("…GMP-013 updated as a second consumer of its al") — byte-verified live (193,078 bytes = the API-reported size, so the file's true stored state, not fetch truncation); not explained by the recorded deliberate-non-update decision (which does cover the v0.10-vs-v0.9 Status omission). Repair intersects the pending maintain-vs-retire decision; the human's call.
- F-GMP-2 WARNING (process compliance): RIP-011's ratified anchor rule not applied in GMP's own Resolution Log — zero anchor fields (`rl_entry_count_after` etc.) across all five post-ratification entries (2026-10-26 through 2026-11-05), no exemption logged; RIP's own equivalent passes carried anchors.
- F-GMP-3 WARNING (stale claims): Relationship section — "Security_Protocols.md — exists at v0.5 (2026-06-19)" (the F-RIP-1 formula; campaign Pattern 2 instance 8, with the 2026-10-23 Relationship-section repair having touched this very section and left the pin) and "SEC-007 is the deepest blocker" (SEC-007a resolved 2026-08-22; SEC-007b sole remaining per Unknowns' Critical Watch).
- F-GMP-4 WARNING (staleness): Aging Rule tripped 2/4 open entries — GMP-003 107d, GMP-013 107d (both Last Reviewed 2026-07-26); GMP-002 68d and GMP-004 53d clean. Systemic instance 7; campaign running total 47 of 60 open entries.
- F-GMP-5 NOTE: Resolution Log ordering inversions (v0.6 after v0.7; 07-16 after 07-19 ×2; ascending tail) — ruled historical per the kickoff's PKC-007 standing rule.
- F-GMP-6 NOTE: the file's own drift indicator "GMP-002 remains unresolved after three audit cycles of Governance_Charter.md" appears in firing state — GMP-002 continuously open 158 days across numerous Charter audit passes; the indicator's cycle unit is not precisely defined, derivation limit disclosed, hence NOTE.
- F-GMP-7 NOTE: ~10 bare path citations in operative/sidecar text (Security_Protocols ×3, Trajectories ×4, CIR_Gov ×1, Governance_Charter ×2) — all targets resolve at Admin/ root, form-only per PKC-003; batch-eligible with the F-SEC-2/F-SP-2/F-RIP-5 grep remedy (fifth evidence point). The bare colliding-ID set (GOV-008 etc.) is deliberately preserved per MAINT-63's recorded straggler enumeration — not a finding.
- Compound Drift Rule did not fire: exactly one of the file's own indicators is in a firing state (F-GMP-6); the rule requires multiple concurrent indicators.

## Verification record

- Checks 1–11 otherwise clean: X10 4=4=4 exact (File State = sidecars = Unknowns index; statuses Open×4; Priorities field-for-field GMP-003 Major / GMP-004 Major / GMP-002 Minor / GMP-013 Minor); Highest Risk High recomputes (GMP-004 High); Active Disputes 0; Ethical Anchor exact; Scope Boundary re-derivation clean incl. the live Fork Reconciliation Track naming.
- Fabrication probe PASSES on the flagship cross-refs: TR-GOV-001 live in Admin/Trajectories.md (v3+ table, pointer to Admin/Hardware_Diversity_Ladder.md, explicit non-claim language); Admin/Hardware_Diversity_Ladder.md exists (v1.2, four-tier Tier 0–3); Admin/CIR_Gov.md §8.2 exists exactly as §VII.8 cites it; Forge_Audit_Kit.md's Verification Maturity Model section present (v1.32); Charter GOV-018/F1–F6 per CAMPAIGN4_AUDIT_03.
- Fetched-file SHA-256: `Admin/Governance_Migration_Protocol.md` at `e63f7904` = `180fb10e26b5d2ebb0a2ee9a6f0739737bff07dcce385d6fed06384788ef0ff7` (191,505 chars / 193,078 bytes, exact API-size match — the sweep's largest file, fetched complete).
- GMP-013's "no tooling" claim verified current: harness v18 + audit_lib.py implement three checks only, no EQD/quorum metadata verification.
- Out-of-scope observations recorded in the deposit: Unknowns resolved-entries notes missing for GMP-001/GMP-006 and the GMP-004 note not annotated for SEC-007a's resolution; Hardware_Diversity_Ladder.md header v1.2 vs its RL's latest version action 1.0→1.1 (its own audit, sweep item 31).

## Disclosures

- Event: (iii) harness defect — one `get_file_contents` response (the GMP fetch) arrived double-JSON-encoded (resource.text was a JSON string literal rather than plain markdown), unlike all prior fetches; decoded and byte-verified against the API-reported size before any finding was derived, no impact on findings. Also this pass: one pre-flight compose failed pre-push with a self-caught TypeError (byte count passed where the SHA helper expected a byte array; no write occurred) and a directory listing was dropped from a saved tool-result (both recovered by re-fetch); short SHAs do not resolve as refs (known class — full SHA used); `list_commits` fields enum excludes "message" (`commit` used).

## Next

- CAMPAIGN4_AUDIT_11: `Admin/Autonomy_Divergence_Protocol.md`. The cross-file pattern document update is DUE in this window (AUDIT_11–14): the artifact-06 pattern doc gains Aging-Rule instances 6–7, Pattern 2 instances 7–8, and the bare-citation remedy's fifth evidence point.
- Next IDs: MAINT-100; Intake Log entry 22 (still untouched this campaign).
