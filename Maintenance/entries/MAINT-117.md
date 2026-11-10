# MAINT-117 — Campaign 4 AUDIT_27 landing (Admin/Computational_Institutional_Reasoning.md)

Date: 2026-11-10. Actor: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.

## What landed

- LazarusForge push `cbd9f6c0bf779f84859e98cc7f1e3de540784b9f` (single push, message "CAMPAIGN4_AUDIT_27 (Admin/Computational_Institutional_Reasoning.md): findings-only deposit + kickoff tracker addendum 26 (append-only; PKC-020: no audited field advanced)"):
  - `Admin/AAudits/CAMPAIGN4_AUDIT_27_Admin-Computational_Institutional_Reasoning.md` — 8,685 chars, SHA-256 `cf513bc5eabeeb973e59a9ca68316bfc416ae6d6ca2daed619eade10d258699e`.
  - `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — tracker addendum 26 appended, 59,515 chars (was 57,508).
- Head re-check (the MAINT-109 process remedy): LF main verified at `9711630b` immediately before the push (the compose-and-push program re-checked the head as its first step; no intervening commit).
- Post-push byte verification: both files re-fetched at head `cbd9f6c0`; deposit length and SHA-256 match the compose-time values; kickoff 59,515 chars with addendum 26 present and the canonical addenda 1—25 intact.
- Audited file: `Admin/Computational_Institutional_Reasoning.md` at `9711630b` — 89,924 chars / 852 lines / 90,257 bytes, SHA-256 `e155c53e6b814c029e16fb3e4ae961dfce00d047577fe8412aaaf7565ff014a4`, Status Exploration, Version 0.31.

## Findings recorded (summary; full detail in the deposit)

- F-CIRF-1 WARNING: literal escape-sequence corruption in live File State — the Highest Risk row and Provenance note carry `\u03b31\u2013\u03b34` / `\u03a8` where the Greek glyphs belong, 4 occurrences verified live; probable introduction by the file's own 2026-10-29 Vibe-line passes (non-independence disclosed); new watch item: escape-sequence scan added to the campaign method.
- F-CIRF-2 WARNING: the Scope Boundary calls CIR_Gov a "Proposed–Not-Ratified layer" — PKC-031-retired vocabulary surviving in live prose written after the retirement.
- F-CIRF-3 NOTE: bare colliding "MAINT-11" citation in the X3 entry — twelfth grep-remedy evidence point.
- F-CIRF-4 NOTE: §7.4 harness pin last source-checked v16 vs live v18, self-disclosed.
- F-CIRF-5 NOTE: the human-ratified v0.30 section deferral aging (File State lacks four standard rows; the file seven standard sections; MAINT-56-retired Last Audit row conformant-at-touch); the Unknowns registration's "own sidecar" home ambiguity, derivation limit disclosed.
- F-CIRF-6 NOTE: verified-clean records (Kit CIR- prefix registration live; CF §IX.3 companion patch live; the §8.4 tracker matches Unknowns v5.79 field-for-field; both Tests/ targets live with the schema's mapping claims verified; Discovery five-theorem parity; γ3/γ4 citations qualified; Ethical Anchor exact; version parity held; zero Archive/ references).

## Control cases

- Aging NOT tripped (CIR-001 reviewed 2026-10-27, 14 days) — fifteenth no-trip control case, the first with a live review date rather than a vacuous one. Compound Drift vacuous (no drift indicators exist).

## Notes

- Disclosed non-independence: the file's last two touches were Vibe-line maintenance passes, and F-CIRF-1 records a defect those passes appear to have introduced; disclosed in the deposit per the kickoff standing disclosure.
- Canonical kickoff chain (addenda 1—25) verified intact at compose.

## Next

- CAMPAIGN4_AUDIT_28: `Admin/Environmental_Constraints.md`; the pattern document's Update 3 (files 22—27) planned for that landing within its due window (AUDIT_27—30).
- Next IDs: MAINT-118; Intake Log entry 22 (still untouched this campaign, 21 rows).
