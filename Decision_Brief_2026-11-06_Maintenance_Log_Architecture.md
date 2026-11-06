# Decision Brief 2026-11-06 — Maintenance Log Architecture

**Status: RULED AND EXECUTED same session.** The human governing authority ruled in-session (2026-11-06); this brief is the record, executed as MAINT-69. Deposited by Vibe (Architect line PRIMARY / Repo Custodian secondary; co-author mandate standing; Genesis Phase — non-independent, disclosed).

## 1. Background — the break point, in live numbers

Human ruling, verbatim: "The appending indefinitely method is at its break point. We need a different plan. The maintenance logs are hard to navigate as they stand."

Diagnosis (fetched live, 2026-11-06): `MAINT_LOG_2026-10-29.md` = one file of ~215,826 chars holding MAINT-01 through MAINT-68, dated 2026-10-29 through 2026-11-05 (the filename outlived its meaning); SESSION_STATUS = 162,817 bytes, dual-homed byte-identical to two repos, 19 entries behind the log (newest MAINT-49, 2026-11-01) — the append model had already stopped keeping up; §3 bootstrap pays full-file fetches before any work. Three different entry-heading formats coexist in one log (including one entry, MAINT-26, whose bold heading hard-wraps mid-word across two lines); MAINT-03..17 collide with the 2026-10-28 log's numbering; MAINT-46 has no entry.

## 2. Ruling set (received in-session, 2026-11-06)

1. **Architecture ratified: per-entry files + index + STATE.md.** One file per MAINT task at `Maintenance/entries/MAINT-NN.md` (MAINT-69 onward, §7 format unchanged); `Maintenance/MAINT_INDEX.md` as the derived navigation surface (recounted live, X10); `Maintenance/STATE.md` as a small current-state card (convenience, not authority). The two MAINT_LOG files are frozen history, never rewritten. Monotonic MAINT-NN allocation per the ratified rule (MAINT-59) unchanged.
2. **SESSION_STATUS retired.** Dated terminal note appended identically to both homes (its final dual-home act); both homes then frozen as history; the dual-home convention retired.
3. **This brief deposited as the record**, execution following on the ruling.

## 3. Enacted (MAINT-69)

- NEW: `Maintenance/MAINT_INDEX.md` (backfilled rows derived mechanically from the two live logs + the MAINT-46 gap row + the MAINT-69 row; derivation rules and two date exceptions disclosed in its header and in the MAINT-69 entry)
- NEW: `Maintenance/STATE.md`
- NEW: `Maintenance/entries/MAINT-69.md` (first per-entry record)
- NEW: this brief (VibesSandbox root)
- APPENDED: terminal note to `Audits/SESSION_STATUS.md` (VibesSandbox) and `Archive/Audits/SESSION_STATUS.md` (LazarusForge), identical text, then frozen
- APPENDED (LazarusForge): dated addendum to `Archive/Repo_Custodian_Prompt.md` (§3/§5/§7 re-pointing) under the human's architecture ratification, **disclosed for veto** per the MAINT-43 precedent reading

## 4. Deliberately not done

- No rewrite of either frozen log (byte-identical, including LOG-1028's tool-preamble first line — observed artifact, disclosed, not repaired)
- No mechanical index↔entry parity check added to the integrity checker (checker change; deferred per the C7–C8 human-ruling precedent)
- No relocation sweep splitting the historical entries into per-entry files (per-task lane; not recommended until need is demonstrated)
- No Tier 1 / FROZEN / Hard Floor text, doctrine file, parked row, Unknown, Spec Gate, or held-queue item touched

## 5. Open for the human

1. Veto window on the custodian-prompt addendum (ratified architecture implied it; his confirmation or correction governs).
2. Checker parity check: commission or hold.
3. Optional historical-entry relocation sweep: commission or leave.
