# MAINT-115 — Campaign 4 AUDIT_25 landing (Admin/Experiments.md)

Date: 2026-11-10. Actor: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.

## What landed

- LazarusForge commit `51c552036c95aca951dec1ea2f9ac6380e1a53a9` (single push, message "CAMPAIGN4_AUDIT_25 (Admin/Experiments.md): findings-only deposit + kickoff tracker addendum 24 (append-only; PKC-020: no audited field advanced)"):
  - `Admin/AAudits/CAMPAIGN4_AUDIT_25_Admin-Experiments.md` — 9,376 chars, SHA-256 `a2f9516bdfec7b7f3286426f4599ba2a561003996864507bcbb14b0b669b59d4`.
  - `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — tracker addendum 24 appended, 55,790 chars (was 53,105).
- Pre-compose and pre-push head re-checks (the MAINT-109 process remedy): LF main verified at `3ef1733a` at both checkpoints; no intervening commit.
- Post-push byte verification: both files re-fetched at head `51c55203`; deposit length and SHA-256 match the compose-time values; kickoff length 55,790 with addendum 24 present and the canonical addenda 1–23 intact.
- Audited file: `Admin/Experiments.md` at `3ef1733a` — 12,341 chars / 141 lines / 12,444 bytes, SHA-256 `c3765f6c5725a46b387ebe7ff539bef67aa38b7b51c558ac0dd18bd1579a5b1d`.

## Findings recorded

F-EXP-1 WARNING Entry Schema internal contradiction ("Five fields required" over an eight-field schema table of which only three are named mandatory; the figure reads as a carryover from EF-0.3's five-field Epistemic Ledger, verified live in AP v0.47, and the 2026-10-28 clarification repeats it); F-EXP-2 WARNING the 2026-11-05 MAINT-63 qualification pass paired CF-001 with a non-owning file (the candidates note cites `Operations/Electronics.md` CF-001; the true owner is `Architecture/Cognitive_Frameworks.md` per CF's own sidecar and Electronics.md's 2026-10-30 retrofit record; EN-001 and CE-003 in the same sentence verified correct — the F-EIP-1/F-TRJ-3 mischaracterization class, introduced by the repair pass itself); F-EXP-3 NOTE post-retirement Last Audit/Auditor write 2026-11-05 (the F-ISP-4/F-IIL-3 class, third instance); F-EXP-4 NOTE Auditor cell "prior:  Prior:" duplication (the F-OC-4/F-IIL-5 class); F-EXP-5 NOTE Aging vacuous, fourteenth no-trip control case, Compound Drift vacuous; F-EXP-6 NOTE verified-clean records (X10 0=0=0, Ethical Anchor exact, the EF-0.8b sentence verbatim, the Anti-Distortion Clause live, AP-010 framing accurate, both Field_Logs examples live in the Tests/Field_Logs.md index, the Tests/ trio live, Routing registration Explicit, RL five entries, FT exemption class 11 live, append-only intact).

## Notes

- The audited file carries two prior Vibe-line passes (the 2026-10-28 candidates-note clarification; the 2026-11-05 MAINT-63 execution pass, which is itself the subject of F-EXP-2); non-independence disclosed in the deposit per the kickoff's standing disclosure.
- Canonical chain (kickoff addenda 1–23) verified intact at compose.

## Next

- CAMPAIGN4_AUDIT_26: `Admin/CIR_Gov.md`.
- Next IDs: MAINT-116; Intake Log entry 22 (still untouched this campaign, 21 rows).
