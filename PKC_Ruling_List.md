# Human Ruling List — Parked Concerns Triage

**Status note (2026-10-26):** This list was drafted 2026-10-25 before the five-sweep enactment. Since then the human governing authority resolved several items: PKC-031 (Proposed retired), PKC-004/024 (Risk/Priority vocabulary), PKC-025 (Unknowns.md derivative-index exception), PKC-013 (RS-001), PKC-015 (IIL intake), PKC-017, PKC-020 (findings-only rule), PKC-029, PKC-035, PKC-038 (option A), PKC-039 and PKC-041 are enacted. Treat the Recommended Disposition text below as historical; the problem statements remain source-accurate.


**Source:** `Progress_Log.md` §Parked Concerns (rows PKC-001–040), Last Reviewed 2026-10-25.
**Status:** Decision-ready draft. Nothing in this document is applied; each item records a recommended disposition only.
**Rule honored:** every problem statement below is taken from the parked row itself, not re-derived from an agent summary. A prior Grok draft of this list restated 10 of 16 concerns incorrectly and was discarded.

---

## Group 1 — Vocabulary & status doctrine (highest leverage; decide first)

### PKC-031 — Status "Proposed" used by eight files, including one that has already run
**Problem:** File_Template and Canonical_Terms name Exploration / Draft / Specification as the designations; "Proposed" is used by eight files (Robotics, Automotive, Exception_Evidence, CIR_Gov, both Chrono files, Multi_Agent_Quorum_Trial, KIT_REGRESSION_PACK). The Chrono pilot has run (procedurally complete 2026-10-19) and still reads Proposed — so a completed exploratory dry run has no label at all.
**Recommended disposition:** Register "Proposed" as a fourth valid designation **and** add a post-execution label for completed-but-unconfirmed work (the pilot). Apply once, repo-wide, to all eight files in one pass.
**Downstream:** Eight files reclassified in one edit; the pilot's real state becomes visible; clears the vocabulary failure the audit itself surfaced.

### PKC-004 + PKC-024 — Risk values in Priority columns (one defect class)
**Problem:** File_Template already limits Highest Risk to Low/Medium/High, so Critical was never a valid value there (PKC-004). The same conflation sits in ~15 more rows of Unknowns.md's "Priority (Promo)" column: CIR-GOV-001, EM-001–003, AS-002/003, GK-002–004, ST-001–003, EL-001–004 (PKC-024). The PKC-024 rows were **not** checked against their sidecars — some may be deliberate.
**Recommended disposition:** One ruling: Risk and Priority are distinct fields, never interchangeable. Add the one-line note under File_State in File_Template (PKC-004, a convention change so not yet applied), then check the ~15 Unknowns.md rows against their owning sidecars before correcting — not a blind find/replace.
**Downstream:** Clears PKC-004 and PKC-024 together; removes a recurring audit-friction class.

### PKC-025 — Unknowns.md cannot be formally audited, yet every audit relies on it
**Problem:** Unknowns.md has a version header but no File State block, Scope Boundary or Ethical Anchor, so under Auditor_Protocols' Audit Entry Conditions it fails its own auditability bar.
**Recommended disposition:** Add a minimal File State block to Unknowns.md rather than documenting an exemption — the file is load-bearing for every sweep, and an exemption would be doctrine about evidence rather than a fix.
**Downstream:** Every future audit of Unknowns.md becomes formally valid; PKC-034's SC-H registration work also passes through this file.

---

## Group 2 — Log, version and bookkeeping policy

### PKC-002 — Trailing Status sections drift from headers
**Problem:** Governance_Migration_Protocol still shows v0.9 / 2026-07-31; Verification_Gates contradicted its own header until 2026-10-23. Choose: maintain trailing Status sections, retire them in favor of the Resolution Log, or add a header check to the audit kit.
**Recommended disposition:** Retire trailing Status version-history in favor of the Resolution Log, and add the header check to the sweep prompt. Maintaining two parallel histories is the documented failure mode (see PKC-029, same shape).
**Downstream:** One convention replaces per-file drift; reduces the check surface PKC-001 depends on.

### PKC-029 — Canonical_Terms version discipline
**Problem:** Header v0.7 (2026-07-05), Status section ends at v0.6; the 2026-08-17, 2026-09-14 and 2026-09-23 body passes were never versioned; six sidecar entries still show Last Reviewed 2026-06-24. Decide whether those passes warrant bumps and what the sidecar review-cadence policy is.
**Recommended disposition:** Bump once to acknowledge the unversioned passes (record as a single reconciliation entry), then fold the cadence rule into the PKC-002 decision so there is one versioning policy, not two.
**Downstream:** Resolves the version-string variant noted under PKC-001; prevents recurrence in AP-029-driven edit classes (links to PKC-039).

### PKC-039 — Do reference corrections bump versions and get logged?
**Problem:** Persistent_Cognition_Candidates header reads Version 0.16 with no log entry recording the bump (last versioned entry v0.15, 2026-09-27); the 2026-10-20 reference correction under AP-029 is logged as "no content change" though it edited a fit note. AP-029-driven edits will recur.
**Recommended disposition:** Rule that a reference correction which changes live file content (even one fit note) is a content change: it bumps the version and is logged as such. Purely mechanical fixes (path/name only, byte-identical meaning) are logged without a bump.
**Downstream:** Gives a standing answer for every future AP-029 pass; pairs naturally with PKC-035.

### PKC-035 — Must a pass that changes content tied to an unknown bump that sidecar's Last Reviewed?
**Problem:** Hydrologic_Resource_Cascade's 2026-06-30 pass turned HR-UNK-002 (contaminant exceedance) into a defined Containment Mode, but HR-UNK-002's Last Reviewed is still 2026-06-28. Cognitive_Salvage_Layer bumped sidecar dates where touched — the two files disagree on policy.
**Recommended disposition:** Yes: any pass that substantively changes content tied to an unknown bumps that sidecar's Last Reviewed (aligning to Cognitive_Salvage_Layer's practice). Do not retroactively bump HR-UNK-002 without a real review date — record it as a known miss until Hydrologic is next reviewed.
**Downstream:** One policy for all sidecars; closes the HRC/CSL divergence; PKC-040's missing Last Reviewed fields get the same rule.

### PKC-018 — Resolution Log heading level split (16 files `###` vs 15 `##`)
**Problem:** 16 Admin files nest the Resolution Log under `###` (including File_Template itself), 15 use `##`. The repo-wide split, not any one file, is the concern.
**Recommended disposition:** Standardize on `###` under Auditor Notes & Unknowns — that is the majority and the pattern File_Template itself models. Apply in one deliberate pass; do not batch with PKC-001's backfill question.
**Downstream:** One convention; 15 files touched once, mechanically.

### PKC-007 — Historical Resolution Log ordering/numbering irregularities
**Problem:** All in history: GMP inversions and missing versions, Ethical_Constraints missing v0.2 and v0.4–v0.7, Verification_Gates out-of-order creation pair, this file's own two-block log, Security_Protocols' three-block log, and others (six already reordered 2026-10-24).
**Recommended disposition:** Declare as-is. These are historical records; rewriting them backfills nothing and risks the same annotation-without-marker defect PKC-001 already caught in Autonomy_Divergence_Protocol. Add one line to Resolution_Methodology noting historical logs predate the ordering convention.
**Downstream:** Clears PKC-007 without touching frozen history; PKC-016's GMP edit stays the only §VII.6 change.

### PKC-020 — Does a findings-only pseudo-audit advance Last Audit?
**Problem:** The 2026-08-10/11 Grok findings-only wave covers nine files; five left headers untouched, Nothingness_Theorem shows the opposite precedent (body-changing pass bumped Last Audit), and a split policy is available: body-changing passes must bump; findings-only passes undecided.
**Recommended disposition:** Ratify the split policy: body-changing passes must bump Last Audit (Nothingness_Theorem precedent); findings-only passes record in the Resolution Log with a note, and do **not** bump Last Audit. Then add the inverse header-vs-log freshness check to the sweep prompt so both halves are mechanically caught.
**Downstream:** Retroactively legitimizes the five untouched headers in the August wave; closes the same question raised on Hardware_Diversity_Ladder, Economics and Security_Protocols.

---

## Group 3 — Structural and naming decisions

### PKC-003 — `ASM-` assumption IDs collide across files
**Problem:** Charter ASM-001–006, GMP ASM-001–005, Verification_Gates ASM-001–004, Security_Protocols SEC-ASM-001–006, Economics ASM-001–005, Engineer_Protocols and Auditor_Protocols ASM-001–00x — different content each; twelve files in the family. Impact on cross-references not yet checked.
**Recommended disposition:** Per-file prefixes at the next Canonical_Terms revision (e.g. `GC-ASM-`, `GMP-ASM-`, `VG-ASM-`). First check cross-reference impact, then migrate in one pass with redirects noted in each file's log. This is the only repo-wide naming fix pending.
**Downstream:** One namespace decision covers twelve files; bare `ASM-0xx` citations (PKC-021's third shape) become resolvable.

### PKC-012 — "Six-folder structure" wording is internally inconsistent
**Problem:** ASM-001 counts root among six; §II calls Automation/ and Archive/ non-domain layers on top of six content domains; the repo has seven physical directories plus root. Adm_Scope_Map carries its own folder counts.
**Recommended disposition:** Adopt ASM-001's definition as canonical (six content domains), amend §II to say "six content domains plus two non-domain layers plus root files," and align Adm_Scope_Map's counts in the same edit.
**Downstream:** Three-way reconciliation in one pass; removes a persistent auditor confusion.

### PKC-013 — RS-001 deferred while `Automation/` now holds eleven `.py` files and a `.zip`
**Problem:** The non-markdown file-type review procedure has been deferred "until a concrete case arises," but the concrete case has quietly arrived: eleven Python files already exist, including `audit_lib.py` — the natural home of the mechanical checks proposed under PKC-021 and PKC-001.
**Recommended disposition:** Define the review procedure now. The deferral condition has been met, and PKC-040's automation work depends on exactly these files being in-scope.
**Downstream:** Unblocks treating Automation/ files as auditable; required before the audit_lib.py check additions.

### PKC-015 — Does the October bookkeeping decay count as RIP-class integrity incidents?
**Problem:** Integrity_Incident_Log has had zero entries since its 2026-08-16 creation, while its own Drift Indicators list "recorded only in Progress_Log and never entered here" as decay. Ruling needed: do the Progress_Log orphaned-entry rotation and PKC-001's decay count, or sit below the intake bar?
**Recommended disposition:** Yes on PKC-001's decay (33 of 47 files with stale bookkeeping is squarely RIP-class); no on the orphaned-entry rotation (it followed the documented rotation rule and is not an incident). Log the PKC-001 decay as the file's first entry once the shared-cause question is answered.
**Downstream:** Gives Integrity_Incident_Log its first real intake and a concrete calibration of its intake bar.

---

## Group 4 — Small, self-contained wording rulings

### PKC-004-adjacent (PKC-008) — GMP-011's "Classification Disputes" heading does not exist yet
**Problem:** GMP-011 routes dispute logging to this file under a heading that has never been created (zero active disputes).
**Recommended disposition:** Create on first use, and record that decision here so the gap is no longer an open question.
**Downstream:** Closes the row without touching GMP (avoiding the PKC-023 cascade).

### PKC-016 — GMP §VII.6 still lists item 1 as "not yet executed," but it was done 2026-09-23
**Problem:** The GMP-011 minimum dispute rule was recorded 2026-09-23; Hardware_Diversity_Ladder's mirrored item was corrected 2026-10-23, but GMP's own copy was left because §VII.6 is Candidate-specification text. No third live copy exists.
**Recommended disposition:** Fix GMP's copy now, in the same edit style as Hardware_Diversity_Ladder's — the "Candidate-specification" caution protects against *rewriting* §VII.6, not against marking a completed checklist item complete.
**Downstream:** One edit; the two mirrored items agree again.

### PKC-017 — Two wording questions (Operational_Conventions' Template-Exemption; HDL's Spec Gates note)
**Problem:** (a) Operational_Conventions has no Resolution Log (its three passes live only in Last Audit) — should the exemption say so explicitly? (b) Hardware_Diversity_Ladder's 2026-08-11 entry says "Spec Gates N/A / left locked" while File State says 0/6.
**Recommended disposition:** Yes to both, as one-line edits: state the exemption explicitly, and add one sentence to HDL recording that the gates remain deliberately locked (which also matches the PKC-027 Ship_of_Theseus precedent).
**Downstream:** Clears the row; reduces the next auditor's re-derivation load.

---

## Execution notes for the Governing Authority pass

1. **Decide Group 1 first** — the three vocabulary rulings collapse the largest number of downstream rows (eight files for PKC-031; ~15 rows for PKC-004/024; all future audits for PKC-025).
2. **PKC-001 remains parked and High-weight.** Nothing in Group 2 authorizes bulk header/log backfilling until the shared-cause question is answered. PKC-015's recommended intake explicitly waits on it.
3. **The only pre-MAQT Cycle 1 blocker is not on this list** — it is PKC-038 (mechanical bucket): decide which of the MAQT role cards vs protocol is canonical *before* the run.
4. **Recommended decision order:** PKC-031 → PKC-004/024 → PKC-025 → PKC-020 → PKC-002/029 → PKC-003 → the remainder in any order.

---

*Each item above cites `Progress_Log.md` §Parked Concerns as its sole source. Recommended dispositions are proposals only; per row rule 3, the human governing authority decides when a row is picked up, and Status changes happen in place.*