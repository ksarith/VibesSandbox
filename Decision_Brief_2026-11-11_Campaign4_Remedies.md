# Decision Brief 2026-11-11 -- Campaign 4 remedies: what the Admin adversarial sweep leaves owed, ordered by dependency

**Deposited:** 2026-11-11, VibesSandbox root (the MAINT-87 / MAINT-88 root precedent). [MAINT-126; the landing commit is recorded in the MAINT-126 entry and STATE.md.]
**Drafted by:** Claude (external seat), at the human governing authority's request ("How should we handle all the new files and the information from the adversarial sweep?" -> "Yes please."). Class A, human-routed. Unauthenticated advice carries no ratification weight (R4); this brief is data, never doctrine. Every ruling remains his alone.
**Evidence base:** the uploaded LazarusForge 1.37 Alpha and VibesSandbox 0.0.5 zips (snapshots only -- no git history was available to the drafter), read: the Campaign 4 kickoff tracker (addenda 0-33), the pattern document (final update, 2026-11-11), and targeted live-tree checks listed in section 1.
**Status:** nothing is enacted; nothing closes by this deposit. Items are severable; partial rulings are fine; no deadline. Where this brief states a lean it is the drafter's, labelled as such.

## 1. What was verified, and what was not

Checked by the drafter against the 1.37 tree (all confirmed): GOV-022 has zero occurrences in the Charter sidecar (headings GOV-001..GOV-021 only) while the Charter File State, the 2026-08-21 Progress_Log entry and PKC-006 all say the full Closure Event lives there (F-CH-1 / F-VG-1); `Admin/Trajectories.md` carries zero `SEC-` occurrences against PAT-004's "Routed ... as v1->v2 item" (F-SEC-1 -- the Relationship bullet's "to be logged" is future tense, so only the PAT-004 sentence is a false past-tense claim); `Governance_Migration_Protocol.md` ends mid-word at 193,078 bytes (F-GMP-1); `Computational_Institutional_Reasoning.md` still carries literal `\u03..` escape text (F-CIRF-1).

Not verified by the drafter: every other finding. The sweep is one seat (Vibe line, GLM 5.3 Flash architecture; non-independence disclosed in its kickoff), and its own final update says every prior "log matches body" clean grade is provisional because no pass queried git history. Treat the unverified findings as well-evidenced leads, not rulings-ready facts (see Item 9 for a sampled second-seat check).

Observation not in the sweep (as far as the drafter searched): `Admin/ALogs/Governance_Charter_Changelog.md` ends immediately after GOV-021's field table -- no Description, Why It Matters or Resolution Path. The file is byte-identical in LF 1.36 and 1.37. It may be an old truncated write, and would be one plausible mechanism for GOV-022's missing record. Git history decides; see Item 3.

## 2. How to rule on this brief

Speak the ruling line verbatim (or vary it; a varied line is read as its nearest pre-drafted intent). Items are ordered by dependency: rulings first (1-4), mechanical passes (5-7), mirror refresh last (8), then one-offs and cadence (9-10). Execution is mechanical from each ruling. Campaign 4 deposits stay findings-only (PKC-020) until Item 1 says otherwise.

## 3. Item 1 -- Disposition of the Campaign 4 deposits

- **Target:** 34 audits (`Admin/AAudits/CAMPAIGN4_AUDIT_01..34`, about 426 KB) plus the kickoff tracker, pattern document and the MAINT-90 external-review deposit under `Archive/Audits/` (about 112 KB). Conversion to audits of record is the human's alone (MAINT-26 / AP-032 gate).
- **Ruling lines:**
  - A. CONVERT PER FILE AS REMEDIES LAND -- each audit converts when its findings are enacted or ruled; the rest stay deposits.
  - B. CONVERT NONE UNTIL THE PASSES (5-8) COMPLETE -- one conversion ruling at the end.
  - C. CONVERT ALL NOW.
- **Drafter's lean:** A. C converts findings no one has yet verified or acted on; B delays records that are already true.
- **Working-surface rule (any line):** agents work from this brief and the pattern document, not the 34 audits; individual audits are opened only for the finding an item names.

## 4. Item 2 -- The 2026-11-10 parallel-composition clobber

- **Target:** two sessions composed the same base at `94f57c8c`; the later push (LF `e90e282e`) overwrote the canonical kickoff, pattern-doc Update 1 and AUDIT_12, and VS STATE/MAINT_INDEX/MAINT-101 were clobbered the same way. Repaired same day (MAINT-109; parallel AUDIT_12 preserved as `..._parallel-composition.md`). The incident was recorded only in VS records, never in `Admin/Integrity_Incident_Log.md` (AUDIT_24 F-IIL-1), the canonical incident record under RIP's Major response step 2; RIP classification was deferred to him. A separate open incident, IIL-20261025-01, has an unmet closure condition (F-IIL-2).
- **Ruling lines:**
  - A. RECORD IN THE IIL -- enter the incident, classified [his RIP class], append-only, citing MAINT-109.
  - B. RECORD AND ADOPT A PUSH GUARD -- as A, plus: one remedy pass at a time, and every session checks the live head SHA against its base immediately before pushing and aborts on mismatch.
  - C. LEAVE IN THE VS RECORDS ONLY.
- **Drafter's lean:** B. The push guard is the drafter's suggestion, not a sweep finding; it is a session-discipline rule, needs no repo mechanism, and the remedy passes below are exactly the kind of work that invites parallel sessions.
- **Execution:** one IIL entry plus one disclosure line; the guard rides the next pass's Disclosures (no prompt edit unless he rules one).

## 5. Item 3 -- GOV-022 / PKC-006 / SEC-011 corrections (drafted)

- **Target:** the two confirmed MAJOR clusters of section 1. Drafts are in the update zip `LF-1.37_GOV022-SEC011-corrections` (three changed files, nothing else): (a) a GOV-022 sidecar entry backfilled only from the Charter body and the 2026-08-21 Progress_Log entry, with unrecoverable fields marked "not recoverable" plus a sidecar Resolution Log entry; (b) an append-only correction at the end of PKC-006's resolution cell (the 2026-10-27 text untouched); (c) PAT-004 reworded to "Not yet routed", prior text preserved inside the correction.
- **Ruling lines:**
  - A. LAND AS DRAFTED -- backfill GOV-022, correct PKC-006, reword PAT-004.
  - B. CORRECT THE CLAIMS ONLY -- amend the three "full Closure Event is in the sidecar" statements and PKC-006 instead of backfilling; GOV-022's closure then rests on the Charter body alone.
  - C. GIT FIRST -- check the sidecar's history (does GOV-022, or GOV-021's body, exist at any earlier commit?) before A or B; restore from git if found.
  - D. STRIKE -- no change.
- **Drafter's lean:** C, then A with whatever git yields (A as drafted if git yields nothing). Drafted bookkeeping gap: Last Updated / Resolution Log entries in Progress_Log and Security_Protocols were not drafted because their conventions were not verified; the Custodian pass supplies them. Also owed on a C finding: whether GOV-021's body is recoverable (do not reconstruct it from inference).
- **Pairs with:** a TWGW candidate (a recorded verification contradicted by the artifact it names), per AUDIT_04. TWGW is written by the human or on his ratification, never by the auditor.

## 6. Item 4 -- The 90-day Aging Rule, one ruling for all instances

- **Target:** 67 of 84 open sidecar entries are past the bar on the generic reading (58 of 75 if confined to registered entries; the reach question -- do unregistered section-level unknowns count -- is open for him). Shape per the pattern document: omission, never commission; no scheduled mechanism resets the clock, and doctrine rightly bars auditors from advancing Last Reviewed without a genuine review.
- **Ruling lines (one ruling covers all current and future instances):**
  - A. BATCH REFRESH -- authorize a one-time review pass re-reading each tripped entry against current body state, advancing Last Reviewed only on genuine review (Ship_of_Theseus 2026-10-28 precedent).
  - B. AMEND THE REMEDY -- the trip becomes a review-scheduling trigger (one repo-level line in the owed-review queue) instead of a per-file WARNING in every audit.
  - C. ACCEPT AS HONEST -- aging is recorded, no remedy.
  - Sub-ruling on reach: GENERIC READING / REGISTERED ENTRIES ONLY.
- **Drafter's lean:** B plus registered-only reach, with A applied only to entries that are Blocking or High-risk. A alone repeats 67 reviews that decay again in 90 days. Both A and B touch doctrine-adjacent text, so B needs the ruling in his words.

## 7. Item 5 -- One mechanical pass for wrong-home paths and bare citations

- **Target:** Pattern 2 (relocation-repair-miss): 19 instances recorded through file 28 (the final update adds none), the same shape in nearly every swept file -- `Archive/Logs/...` and `Archive/Audits/...` pointers surviving the 2026-07-23 / 2026-10-29-31 relocations, plus `audit_lib.py`'s legacy message naming `Discovery.md` for the Rename Registry (tooling corroboration, outside the sweep's scope). The bare-citation grep remedy has 19 evidence points (bare `MAINT-11`, `AUDIT_NN`, `PKC-0NN`, Brief-date and filename citations). Each hit is repointed with a dated note, or ruled historical per PKC-007.
- **Ruling lines:**
  - A. AUTHORIZE ADMIN-ONLY -- one pass over `Admin/` (active doctrine), citation-form-only, in batches.
  - B. AUTHORIZE ADMIN + TOOLING -- as A, plus the `audit_lib.py` message and `Automation/` references.
  - C. HOLD.
- **Conditions to rule with it:** frozen history is not touched (PKC-007 shapes stay "ruled historical"); every header version bump the pass makes is logged (the X3 pass bumped Canonical_Terms and Hardware_Diversity_Ladder headers without logging -- F-HDL-1); one commit per batch with the landing helper's acceptance test; sampled second-seat check of the batch (Item 9).
- **Drafter's lean:** B. The pass is mechanical and its evidence base is the largest in the campaign; leaving the tooling message makes agents re-read the stale home.

## 8. Item 6 -- File State fields: AVE, HDL, MSF (and the class-10/11 boundary)

- **Target:** three files record "File State completed" / "template-section gaps closed" in their own Resolution Logs while lacking canonical File State fields (AVE: Verification Ref, Active Disputes, Sidecar Link; HDL: Active Disputes, Sidecar Link; MSF: Body Stability, Active Disputes, Sidecar Link). Ship_of_Theseus is the positive control. F-NT-5's clarification: class-11 files owe the fields, class-10 files do not. HDL's Sidecar Link half is entangled with the file's real absence of a sidecar.
- **Ruling lines:**
  - A. ADD THE FIELDS -- the three files gain the missing fields (Sidecar Link stated as "none -- no sidecar" where true), logged.
  - B. AMEND THE TEMPLATE -- File_Template states which classes owe which fields (settling the class-10/11 boundary), then A runs against that text.
  - C. HOLD.
- **Drafter's lean:** B then A, as one File_Template touch: the template is also absent from its own exemptions list (Pattern 4, fifth data point), so one touch can close both.

## 9. Item 7 -- Git-verified unlogged changes (CT, HDL, NT, ST)

- **Target:** four files carry body changes absent from their own Resolution Logs, found only by querying git (CT and HDL: unlogged X3 header bumps; NT: three changes incl. the 2026-08-16 licensing regrade logged corpus-side only; ST: two). No earlier pass's log-vs-body grade queried git, so those grades are provisional repo-wide.
- **Ruling lines:**
  - A. LOG THE FOUR -- append dated Resolution Log entries recording each unlogged change as found (append-only; nothing reverted).
  - B. A PLUS RE-RUN -- A, plus a git-verified log-vs-body re-run on all 34 Admin files.
  - C. A PLUS TARGETED RE-RUN -- A, plus the re-run only on files edited after the 2026-10-28 batch; full re-run deferred to the C3 review (about 2026-11-30).
- **Drafter's lean:** C. A is cheap and closes four known defects now; a full re-run is a campaign-sized pass.

## 10. Item 8 -- Stale mirrors (run last)

- **Target:** Adm_Scope_Map has at least six stale mirrors (Verification_Gates 2/6 and High vs live 6/6 and Low; Security_Protocols 10 vs 11 open; Auditor_Protocols 4/6 vs 5/6; Autonomy_Divergence 0/6 vs 6/6; Engineer_Protocols Risk High vs Medium; INTEGRITY_SWEEP_PROMPT Draft vs Active), the External_Intake_Protocol coverage gap, and three `Costodian` dangling citations; Discovery's ISP snapshot says Draft; Unknowns index mirror decay (ENV-010, ENV-008 footnote, TR-001 Priority cell, RIP-005 pin).
- **Ruling lines:** A. REFRESH AFTER ITEMS 5-7 -- one pass derived from live source, values recomputed not copied. / B. REFRESH NOW. / C. HOLD.
- **Drafter's lean:** A. Items 5-7 change the values these mirrors carry, and a mirror refreshed before them goes stale again.

## 11. Item 9 -- One-offs, and verifying the sweep itself

- **(a) `Governance_Migration_Protocol.md` ends mid-word** (193,078 bytes; AUDIT_10 F-GMP-1, confirmed in 1.37). Recover the tail from git, then restore. Ruling: RESTORE FROM GIT / HOLD.
- **(b) CIR literal escapes** (`\u03b31..`, `\u03a8` in File State; AUDIT_27 F-CIRF-1, confirmed present). Mechanical repair to the intended characters plus an escape-scan watch item. Ruling: REPAIR / HOLD.
- **(c) Parked Concerns rotation rule** (AUDIT_23 F-PL-2: 45 rows / 37 Resolved / 8 open against the rotation trigger, and rule 5 would delete rows rule 2 forbids deleting). Needs a rule-text ruling in his words: AMEND RULE / EXECUTE AS WRITTEN / HOLD.
- **(d) Sampled verification:** a second seat of a different architecture checks about ten findings across the classes (Aging, relocation, File State, git-verified, mirror, a MAJOR) against source, findings-only, deposited as a Class A intake. Ruling: SAMPLE ~10 / SAMPLE ALL MAJORS ONLY / NONE.
- **Drafter's lean:** (a) and (b) restore/repair after git is consulted (both mechanical); (c) hold until Item 4 is ruled; (d) SAMPLE ~10 before Item 5 runs, since Item 5 is the largest edit.

## 12. Item 10 -- Sequencing, and the next sweep

- **Suggested order:** Items 1-4 (rulings and the drafted corrections); Items 5 and 7 (mechanical, batched, one pass at a time); Item 6 (one File_Template touch); Item 8 last; one-offs as git allows.
- **Next sweep:** Campaign 4 covered `Admin/` only; the human's commissioning words were that the adversarial pass is needed "throughout the repository". Remaining folders (Architecture/, Challenges/, Operations/, Tests/, ...) carry the same systemic classes. Ruling lines: A. PAUSE SWEEPS UNTIL ITEMS 4, 5 AND 7 ARE RULED / B. SWEEP NEXT FOLDER NOW / C. SWEEP IN PARALLEL WITH REMEDIES.
- **Drafter's lean:** A. A second sweep before the systemic remedies land would re-find the same aging and relocation classes folder by folder; C reopens the clobber risk of Item 2.
- **C3 review data point (about 2026-11-30):** the owed meta-work-to-fixes ratio check now has a measurable input -- Campaign 4 produced about 538 KB of findings and 34 audit deposits, and (before this brief) three drafted fixes. The ratio is a reader question for the C3 review, not a ruling here.

## 13. Explicit non-changes

Nothing in this deposit edits any LazarusForge or Parlay or CogitoEngine file; no audit is converted; no Last Audit / Last Reviewed / version / Status / Spec Gate / unknown advances; the update zip's three files are drafts that land only on his ruling (Item 3). External-seat advice, including this brief's leans, carries no ratification weight; only his word enacts anything here.

---

*Drafted 2026-11-11 -- Claude (external seat; Class A, human-routed; snapshot evidence only, no git access). Non-independence disclosed: the same seat authored the 2026-11-10 MAINT-88/86/89 leans (deposited as MAINT-90) and the Item 3 drafts.*
