# Decision Brief 2026-10-28d — Campaign files 22–29 batch

**Prepared:** 2026-10-28, Vibe (Repo Custodian, delegated maintenance) — decision-ready material only; no LazarusForge changes made under this brief.
**Sources read in full:** sandbox `Audits/` AUDIT_22–AUDIT_29, AUDIT_20-22_CORRECTION_2026-10-28.md, CROSS_FILE_PATTERN_FINDINGS_Session5.md. LazarusForge head at their fetches: `eee122a`.
**Batch grades:** 0 CRITICAL / 0 MAJOR across all eight files (22: 2W/3N · 23: 1W/3N · 24: 1W/4N · 25: 5W/4N · 26: 2W/3N · 27: 3W/3N · 28: 2W/3N · 29: 1W/4N).
**Positives of record:** PKC-001's predictions held — Nothingness_Theorem confirmed clean, AVE confirmed as the control case, and both named decay instances (Experiments, HDL) were already RESOLVED in-file by human-directed corrections. The AUDIT_13→19 Highest-Risk value-parity streak ENDED at Environmental_Constraints (field correct). Two session-1 findings were adopted by the delegated stream 26 days later (AUDIT_02 F1, AUDIT_09 F4(a) — observed in GMP's header).

---

## Items for human ratification

### 1. Adm_Scope_Map index batch — RECOMMEND: enact (one delegated pass)
- **Kit entry Open Unknowns 7 → 5** (AUDIT_26 F1): stale against Kit v1.25's own File State and Unknowns v5.72 both; PKC-022 (2026-10-27, option B) closed FAK-014–019 by pin retirement. Fix with a dated PKC-022-citing note.
- **NT entry**: add `10 Open Unknowns (Tier 0 — internal-consistency audit only)` (AUDIT_26 F3 — only entry of 32 omitting the count).
- **CIR entry Risk field**: `CIR-001` (an ID, not a value) → `High (CIR-001)` (AUDIT_26 F4).
- **Experiments candidates-note clarification** (AUDIT_28 F5): one line — "candidates = priority unknown targets for future entries, not entries" — to keep the file's own drift indicator from firing on its own candidates note.

### 2. Candidate-file header-fields fix — RECOMMEND: enact; owning-file value wins
Two consecutive files carry no Highest Risk field (AUDIT_27 F1 — AVE; AUDIT_29 F1 — HDL). AVE's absence has already produced a four-way risk-representation divergence (sidecar "Medium (Placeholder)" / Discovery editorializes "Low" / map "unlabeled" / no header field).
- **AVE**: add Highest Risk `Medium (Placeholder — AVE-R1)` (own-sidecar maximum), plus Last Audit and Auditor.
- **HDL**: add Highest Risk (own File State; Discovery honestly says "unlabeled").
- Thereafter Discovery's maturity snapshot mirrors the owning file ("file wins" rule).

### 3. Environmental_Constraints staleness reconciliation — RECOMMEND: enact (one delegated pass; first post-ratification pass)
- **Lessons Learned row** still says "pending human ratification" 103 days after ENV-DS-001 was ratified (2026-07-17) — reconcile to executed (AUDIT_25 F2).
- **ENV-008 sidecar** narrates its FILE_REGISTRY verification as outstanding; the file's own Relationship section records it completed 2026-07-19 — advance the sidecar (AUDIT_25 F3).
- **EC-009 two spots** ("pending EC-009" in Scope Boundary; "resolution paths lead here" in Relationship) stale against EC-009 Ratified 2026-08-22 (Payment via Specification, no routing to this file) — reconcile both (AUDIT_25 F5).

### 4. ENV-008 status-class sub-question — RECOMMEND: re-status to Resolved (human confirm)
"Partially Addressed" is not among Auditor_Protocols' valid closure outcomes (Resolved/Discharged/Deferred/Superseded). The remaining verification was completed 2026-07-19. Recommend marking ENV-008 Resolved with a dated note; Unknowns v5.72 is unaffected either way (both ENV-007/008 already excluded from the active index).

### 5. Aging-Rule review pass, ENV cohort — RECOMMEND: extend mechanically
Eight non-resolved unknowns at 131/113 days stale Last Reviewed (AUDIT_25 F4) — same ratified class as the ST/ECN review pass enacted at `eee122a`. Dated review notes, no status change. (AUDIT_25 F8's "eight vs nine rows" drift-indicator wording fix may ride the same pass: "the eight ID-bearing rows".)

### 6. File_Template exemption-list additions — RECOMMEND: add both classes
- **Tier 0 class** (AUDIT_24 F1): practiced and honored corpus-wide, missing from the canonical exempt list — the PKC-017 gap class again.
- **Stub/scaffold/candidate family** (4 data points: IIL AUDIT_23 F1, AVE AUDIT_27 F2, Experiments AUDIT_28 F1, HDL AUDIT_29 F1): one exemption-class ruling covering the family instead of per-file dispositions — per the template's own counsel, "prefer exemption over forced retrofit."

### 7. AUDIT_20-22 correction disposition — RECOMMEND: ratify as the record
The dated correction maps PKC-001/PKC-007 rulings (2026-10-27) onto the issued findings: ADP F5 and RM F2/F4 shapes ruled historical (declare historical, stop repairing); bookkeeping-decay class declared historical, no bulk backfill; live content-staleness findings (ADP F1–F4/F6, CIR F2–F4, RM F1) unaffected. No grade changes; no edits to issued reports; future audits grade log-ordering shapes NOTE-class unless post-window.

### 8. Standing process conventions — RECOMMEND: ratify as standing practice
- **Adoption-verification**: every delegated-stream adoption is verified against fresh fetches, never taken on trust (Session 5 §1).
- **Fetch-completeness check**: large-file fetches verified non-truncated before checklist runs (held copies near ~63KB suspect; responses cap ~190KB — GMP §VII.8 body remains INCOMPLETE this session).

### 9. Import of the files-22–29 reports — RECOMMEND: enact as bookkeeping
Import AUDIT_22–29 + the correction + Session 5 to LazarusForge `Archive/Audits/` under the ratified CAMPAIGN_ prefix rule (extends the README stream-mapping note's coverage from 17–21 to 22–29). Claude-stream reports keep their numbering; no renumbering of issued reports.

---

## Carried (no action now)
- AP entry 4/6 (map) vs 5/6 (Discovery) divergence + AP "10 Open Unknowns" → **Auditor_Protocols audit (LAST)**, which also inherits the PKC-020 five-variant evidence set (NT/AVE/HDL bumped; Experiments annotated-in-field; CIR did not).
- QCC-R1 dangling reference (AVE-R1 Resolution Path) → Tests/ sweep (`Tests/Quorum_Agent_Conduct_Protocol.md`).
- GMP §VII.8 body + CIR_Gov §8.2.1 companion-reconciliation claims → targeted fresh fetches.
- EL-007 / CF-002 → Operations/ Architecture/ sweeps; ENV-010's Facilities.md Section VII rows → Architecture/ sweep.
- Unknowns v5.72 CE-005 row's stale GR-003 phrase → root-files sweep.
- X3 mechanical retrofit (three severity tiers documented; run with the registry open) and X5 Kit ID-Reference regeneration (add AVE-) remain queued pending human timing/scope — unchanged.
- The three previously recorded deferrable open questions (EC FROZEN markers — recommend yes; Charter "Active" vs EC "Exploration" — recommend Active governs; CIR-GOV-002 same-day mirroring — recommend exempt + in-file RL) remain carried.

## Campaign continuation
AP remains LAST per the approved sequence. AUDIT_20-22_CORRECTION's grading instruction (log-ordering shapes → NOTE-class per PKC-007) applies to the remaining files.

**Status:** awaiting human ruling; on ratification the enacted items will be logged as MAINT-13+ with per-commit shas.

**Open Parked Concern rows:** 5 open (PKC-009, -010, -021, -023, -026).
