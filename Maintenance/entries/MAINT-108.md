# MAINT-108 — Campaign 4 AUDIT_19 landing (Admin/Operational_Conventions.md)

Date: 2026-11-10. Actor: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.

## What landed

- LazarusForge commit `90acea4b` (single commit, message "Campaign 4 sweep: CAMPAIGN4_AUDIT_19 (Admin/Operational_Conventions.md) findings-only deposit + kickoff tracker addendum 17 (PKC-020; no audited-file fields advanced)"):
  - `Admin/AAudits/CAMPAIGN4_AUDIT_19_Admin-Operational_Conventions.md` — 11,402 chars, SHA-256 `d3c67a2d8d7ca5e990c6aaa666f1b83dced14b3945f4d3bedf7852921616bd47`.
  - `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — tracker addendum 17 appended, 39,793 chars (was 38,310), SHA-256 `d97fc62ff023b9b4111fa0ce9ccd1c2fdea4b2b2fdf19cf792b1d07684b2c904`.
- Post-push byte verification: both files re-fetched at head `90acea4b`; the deposit byte-matches the compose record (11,402 chars, SHA-256 recomputed equal, all F-OC markers present); the kickoff's first 38,310 chars are byte-identical to an independent old-head (`f476362a`) re-fetch (full-prefix equality, append-only verified); addendum 17 begins at the exact offset 38,310 with the expected `\n---\n\n## Tracker addendum 17` bytes; addenda 12–17 all present; the resume point reads Admin/Repository_Structure.md (CAMPAIGN4_AUDIT_20).
- Audited-file SHA-256: `Admin/Operational_Conventions.md` at `f476362a` = `b0f2b98dc3fd28a4624576fea64eb1908260ac7f5fef7608719563f64bdd329b` (17,890 chars / 18,016 bytes / 214 lines, fetched complete).
- Tooling note: the push_files result again carried no commit SHA field; the landing head was verified via list_commits (defect report already filed).

## Findings recorded (F-OC-1 through F-OC-4; Compound Drift Rule vacuously did not fire)

- F-OC-1 WARNING (Convention 8 cites the pre-relocation `Archive/Logs/Progress_Log_Changelog.md` home — both in its quotation of Progress_Log's rotation rule and in the supporting-sources line "migration history in both files' `Archive/Logs/` changelogs"; live tree: `Archive/Logs/` holds exactly two files (Discovery_Changelog.md, Unknowns_Changelog.md), the cited path fetch-fails, and the live changelog is `Admin/ALogs/Progress_Log_Changelog.md` (relocated 2026-10-30, MAINT-29); the citation was correct when written 2026-10-03 and wrong now; the 2026-11-05 MAINT-63 touch repaired Convention 4's two AP pointers in this same file with the same relocation as its subject and missed Convention 8; relocation-repair-miss, Pattern 2 instance 15).
- F-OC-2 NOTE (Convention 6's "all nine" Automation script count stale — live Automation/ holds twelve .py files, all twelve verified registered in Routing.md 12/12, so the rule's substance holds; time-scoped wording mitigates; the F-SEC-5 recorded-count family).
- F-OC-3 NOTE (Convention 4's generic check heuristic still routes the "similarly-named _Logs.md/_Changelog.md" check to `Archive/Logs/` only, which post-relocation holds no _Logs.md file at all; the MAINT-63 repair disclosed its scope as citation-form-only — residual recorded, not repaired).
- F-OC-4 NOTE (File State Auditor cell carries a doubled "prior:  Prior:" transition marker; cosmetic).
- Aging Rule vacuous (0 open unknowns — the campaign's ninth no-trip control case); Compound Drift Rule vacuously did not fire (class 9, no drift indicators).

## Verification record

- X10 three-way 0=0=0 (File State / Sidecar Link N/A / zero OC- IDs in Unknowns.md — its sole Operational_Conventions mention is the v5.79 companion-edits list); Highest Risk Low recomputes.
- Template exemption class 9 verified live in File_Template (exact declared terms, listed from 2026-10-25 PKC-017).
- Fabrication probes all passed: audit_lib.py's backtick-letter extractor rule code-true; integrity_check.py's suffix-capturing SIDECAR_ID_RE and Archive/ exclusion both live; the three Convention-2 files (Exception_Evidence, Multi_Agent_Quorum_Trial, Persistent_Cognition_Candidates) now carry the exact canonical Ethical Anchor — the 1.17-era drift repaired; EC-012-PR verified live in Unknowns.md; RM §9 exists and carries the "five separate occasions across one week" history verbatim; the Unknowns_Changelog 2026-09-10 migration note verbatim (14+1 versions stacked, caught when James asked directly); Adm_Scope_Map carries the OC entry (Convention 7's fix real); all five scope maps exist; Routing's Scope sentence on Automation/ verified.
- Live Convention 8 self-check: Progress_Log's rotating section holds 4 dated entries (within the five-entry cap); Unknowns.md's version block holds only v5.79 — no live violation of either rule.
- Out-of-scope observations recorded in the deposit: Unknowns.md's own header cites `Archive/Logs/AUDIT_HARNESS_CHANGELOG.md` and `Archive/Logs/Forge_Audit_Kit_Changelog.md` — both fetch-fail there, both live at `Admin/ALogs/` (same wrong-home class, outside the 34-file sweep scope); Progress_Log's Size-discipline paragraph still carries the stale home vs its updated rotation instruction (corroborates F-OC-1; its own audit is upcoming).
- Deliberate shapes recorded, not findings: the Last Audit/Auditor fields are the file's designated pass-record home per its class 9 exemption — the tension with MAINT-56's corpus-wide row retirement disclosed for the human's consolidated ruling if desired; Convention 6's pre-emptive-entry deviation self-annotated; no version string anywhere.

## Disclosures

- Event: (ii) recurrence — the wrong-home class recurs (F-OC-1, Pattern 2 instance 15); no new pattern established.
- Adjacency disclosed in the deposit: the Last Audit cell records this delegated line's predecessor passes (MAINT-63; the X3 retrofit) as auditors, including the MAINT-63 repair whose completeness F-OC-1 examines; audited as third-party content; non-independent with respect to this line's own prior repairs.
- No harness defects this artifact.

## Next

- CAMPAIGN4_AUDIT_20: `Admin/Repository_Structure.md`.
- Next IDs: MAINT-109; Intake Log entry 22 (still untouched this campaign).
