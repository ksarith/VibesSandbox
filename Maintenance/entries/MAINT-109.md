# MAINT-109 — Parallel-composition clobber discovered and repaired (Campaign 4, the AUDIT_12 window)

Date: 2026-11-10. Actor: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.

## Event

A parallel continuation of this same campaign independently executed CAMPAIGN4_AUDIT_12 through CAMPAIGN4_AUDIT_19 (LF `36d8e783` → `90acea4b`; VS MAINT-101 → MAINT-108) while this session's own AUDIT_12 composition — made at the same LF base `94f57c8c`, before the parallel chain landed — was in flight. This session's pushes landed last (last-writer-wins) and overwrote canonical state with parallel-composition state:

- LF `e90e282e` (parented on `90acea4b`): the kickoff reverted from 39,793 chars (canonical addenda 10–17) to 25,391 chars (the parallel addendum 10 alone); the pattern document's canonical Update 1 (11,554 chars) was replaced by a parallel composition (11,996 chars); the canonical AUDIT_12 deposit (13,750 chars) was replaced by the parallel composition (12,480 chars).
- VS `c42517b5`: `Maintenance/entries/MAINT-101.md` (canonical, 10,320 chars) replaced by the parallel composition (7,354 chars); STATE.md and MAINT_INDEX.md reverted to pre-MAINT-102 content (rows 119–125 and the MAINT-108 recount lost from the live files). The entries/ directory beyond MAINT-101 was untouched (MAINT-102..108 intact).

Discovery: post-push git-history inspection — the live kickoff lacked the addenda the MAINT-102..108 entries reference, and the LF commit history showed the parallel chain below the clobbering push.

## Repair (nothing enacted beyond record restoration; findings-only discipline unaffected)

- LF landing `03f15726e9245df8f62f460998eedeb2cef6a0d4` (single push): the kickoff restored to the canonical chain state (39,793 chars, addenda 10–17) + kickoff tracker addendum 18 appended (the event, the duplicate addendum-10 numbering, the parallel texts' locations); the pattern document restored to the canonical Update 1 (11,554 chars, SHA `97f1f41f6292f7d58190242a1c5ef2276588ae7a2d8d761a3813614649453186`; the parallel Update 1 not re-deposited — a single living aggregation — preserved in git history at `e90e282e`); the canonical AUDIT_12 deposit restored (13,750 chars, SHA `a53c45ec81987a8bafd53465095d72b62677d4eec0700e96535d6f1cdbf179db`); the parallel AUDIT_12 composition re-deposited byte-exact at `Admin/AAudits/CAMPAIGN4_AUDIT_12_Admin-Forge_Audit_Kit_parallel-composition.md` (12,480 chars, SHA `d27d890b6eead23daab7c2c66dc0b29a60d43a9abdeae451ab2db5cfe4e2f90b`) so both parallel audits are visible to the human. Post-push byte verification: all four files re-fetched at the new head and byte-compared equal.
- VS repair landing (this entry's landing, single push): `Maintenance/entries/MAINT-101.md` restored to the canonical entry (10,320 chars) + a dated parallel-composition disclosure appended containing the parallel composition verbatim; STATE.md restored to the MAINT-108 state (52,107 chars) + a dated repair note appended with the post-repair heads; MAINT_INDEX.md restored to the MAINT-108 state (40,101 chars) + this row (126) + the count line updated to the live recount (41 entries/ files = 126 rows). Post-push byte verification performed after landing.

## Classification

New event class: a parallel-session last-writer-wins clobber of append-only campaign records. Distinct from the MAINT-96 lost-push-result family (there, a push's result was lost but the write landed intact; here, later writes silently reverted earlier ones). Root cause: two continuations of the same delegated line running concurrently against the same bases without coordination; the kickoff's single-tracker design assumed a single lineage. Candidate process remedy (the human's to rule): a pre-compose head re-check immediately before every push, and a push-time head assertion (abort if main moved past the compose base) — the connector's push operation does not currently support an expected-parent assertion, so the check is procedural.

## Next

- The sweep resumes at the canonical chain's resume point: `Admin/Repository_Structure.md` (CAMPAIGN4_AUDIT_20).
- Next IDs: MAINT-110; Intake Log entry 22 (still untouched this campaign, 21 rows).
