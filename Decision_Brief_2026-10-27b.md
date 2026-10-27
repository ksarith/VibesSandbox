# Decision Brief b — 2026-10-27 (prepared by Vibe, autonomous management)

**Purpose:** decision-ready material for the twelve Parked Concerns that remain open after the 2026-10-27 ruling session (PKC-001/014/022/033 resolved), plus two adjacent items raised in passing. Same format as the first brief: nothing here is LazarusForge doctrine; it carries no Spec Gate, Status, or Unknowns weight (sandbox governance boundary). Each item states the record, the options, and Vibe's recommendation. The human governing authority decides. Items are ordered by how much the ruling depends on information only you have.

---

## 1. Companion repositories (PKC-011) — needs owner knowledge only you have

**The record:** Repository_Structure §VI lists a companion repository `Lazarus-Forge-` (trailing hyphen) that fresh-agent audits cannot find publicly; `LazarusForge` and `Astroid-miner` both resolve. The same name appears twice in Auditor_Protocols. Separately, Auditor_Protocols and Repository_Structure both describe Astroid-miner as "planned, deferred, not yet active" while a public Astroid-miner repository exists.

**Questions for you:** (a) Does `Lazarus-Forge-` exist (perhaps private, perhaps a typo)? (b) Is the public Astroid-miner repository yours, and should "not yet active" be updated?

**Options / recommendation:** Once you confirm the facts, the edits are mechanical (§VI visibility note, two AP citations, one wording update). Recommendation: confirm the two facts; the wording fixes can then ride the next natural edit of each file, or be done as one small authorized pass.

---

## 2. FROZEN-text citation error (PKC-005) — needs a freeze-scope ruling

**The record:** the Governance_Charter "Self-Evidence" essay attributes the "sacred and undeniable" → "self-evident" edit to the U.S. Constitution; the edit belongs to the Declaration of Independence. The essay sits under the FROZEN Tier 1 Axioms marker, so the question is whether the freeze protects the error.

**Options:**
- **A — Rule that the freeze covers doctrine, not factual citations.** One-word source correction with a dated marker; no doctrine text touched.
- **B — Annotate without editing:** leave the frozen text verbatim, add a correction note adjacent (outside the frozen block).
- **C — Leave as-is** (the essay is illustrative, not load-bearing).

**Recommendation:** A. The freeze exists to prevent doctrine drift, not to preserve a misattribution; B leaves the error visible to every reader who doesn't reach the note. Human-ratified marker keeps the audit trail intact.

---

## 3. History repair vs declare-as-is (PKC-007) — mirrors the PKC-001 ruling you just made

**The record:** Resolution Log ordering/numbering irregularities, all historical: GMP 07-26/07-27/07-26 inversion; Ethical_Constraints missing v0.2 and v0.4–v0.7; Verification_Gates creation pair mid-log (v0.1 then v0.6); Resolution_Methodology's unrecorded v0.8 (v0.7 → v0.9); several two-block logs (Progress_Log, Autonomy_Divergence_Protocol, Security_Protocols). Eight files were already reordered 2026-10-24; the remainder were deliberately left.

**Options:**
- **A — Declare historical, stop repairing.** Consistent with your PKC-001 ruling (bulk backfill would invent history; PKC-007's own precedent). Reordering already done stays done; remaining shapes get a one-line "historical" note at most.
- **B — Finish the normalization:** reorder the remaining logs in one deliberate pass.

**Recommendation:** A. The 2026-10-24 fixes covered the shapes that could confuse a fresh reader mid-log; the rest are reconstructable from dates. B rewrites frozen history for no functional gain.

---

## 4. UnaIdited coverage gaps (PKC-006, PKC-037) — authorization decisions

**The record:** PKC-006: relocated sidecar logs (Archive/Logs/Governance_Charter_Changelog.md and others) were never audited, so the Charter's 13 Open Unknowns count and GOV closure events are only partly verified; Security_Protocols and Leviathan_testing were also unauditable by Vibe at the time. PKC-037: Leviathan_testing §VII claims it closes Cognitive_Frameworks' CF-002 resolution path, and Living_Waters / Leviathan cross-reference Solar_Descent and Support_Raft with reciprocal interfaces — none of it checked.

**Options:**
- **A — Authorize one read-only audit pass** (Vibe, autonomous lane, findings-only per PKC-020; findings reported, fixes only for map/log-class defects, owning-file defects reported).
- **B — Defer until those files are next in scope naturally.**

**Recommendation:** A. Both rows are pure verification debt; a read-only pass cannot create the defects it looks for. If everything checks out, both rows close same-day.

---

## 5. Sweep-prompt addition (from the PKC-001 row) — the mechanical-check candidate

**The record:** PKC-001's investigation found the decay survived both existing mechanical checks because nothing compares the newest Resolution Log entry date against the newest body/Status change date. The candidate inverse check was explicitly held out for your ruling.

**Options:** A — add to INTEGRITY_SWEEP_PROMPT (natural next step numbered after v1.0.3 step 13); B — don't add.

**Recommendation:** A. The 2026-10-26 checker lesson (integrity_check.py reads Last Audit / Last Updated) covers adjacent ground but not this comparison; it's cheap and it directly addresses the one process cause PKC-001 confirmed.

---

## 6. RIP-011 anchor semantics (PKC-019) — three sub-rulings

**The record:** (a) `content_hash_after` is self-referential when the anchor lives in the file it hashes (currently recorded as omitted); (b) unclear whether the 2026-10-23 backfill/correction entries in other governance files owed anchors; none were added; (c) the rule doesn't define how to count Resolution Log entries (RIP's own entry counts dated bullets).

**Recommendation (as a package, codified at RIP's next natural revision):** (a) permanent rule — self-referential hashes are recorded as omitted, with the omission itself noted; (b) retroactive anchors are not owed — anchors bind from the ruling forward (same anti-history-rewrite logic as PKC-001/007); (c) dated bullets are the count unit. All three match what was actually done in practice, so this ratifies existing behavior rather than changing it.

---

## 7. Mechanical-check backlog (PKC-021)

**The record:** the duplicate-§Drift Indicators§ sweep found no further duplicates, but three related shapes have no mechanical check: (i) other repeated required sections; (ii) prose counts above disagreeing lists; (iii) bare colliding-ID citations (EC-0xx, ASM-0xx without owning file) in files written after CT-007. audit_lib.py is the natural home.

**Recommendation:** backlog, in this order: (iii) first (recurring in new files, cheap regex), (ii) second, (i) third. No ruling needed beyond "yes, build them" — they are automation-lane work.

---

## 8. Low-value wording items (PKC-009, PKC-012, PKC-023; plus the Highest-Risk row normalization raised in passing)

**The record:** PKC-009: Ethical_Constraints Scope Boundary still lists "Human escalation protocol (placeholder)" under DOES-define though EC-003 was ratified 2026-08-22 (wording only). PKC-012: "six-folder structure" counts disagree across ASM-001, §II and Adm_Scope_Map. PKC-023: Auditor_Protocols carries two known cosmetic items deliberately left unedited because any AP edit cascades (version bump, two registry citations, archive log, Sidecar SHA-256). Adjacent: Automotive, Robotics and Exception_Evidence lack a Highest-Risk File State row (stub-format omission).

**Recommendation:** fold each into its owning file's next natural content edit — consistent with your low-value-polish disposition and with PKC-023's cascade-avoidance rationale. PKC-012's count reconciliation is the one I'd do sooner if you want it: it touches two files but neither cascades. Say the word and it's a single small pass.

---

## 9. PKC-026 leftover sub-decision

**The record:** the 2026-10-26 ruling enacted most of PKC-026 (two scripts registered, sweep-prompt invariant added as v1.0.3 step 13). One decision left open deliberately: whether `Tests/Field_Logs/FL-20261008-maqt-matrix-preregistration-proposal.md` should be registered in Routing.md. Its own header holds it out pending ratification.

**Recommendation:** keep it held out until that ratification happens, then register it in the same pass that records the ratification. If you ratify the MAQT matrix preregistration proposal, both actions can happen together and PKC-026 closes fully.

---

*Prepared 2026-10-27 by Vibe (Skeptic/Auditor, human-authorized autonomous management). Sources: Progress_Log §Parked Concerns rows PKC-005/006/007/009/010/011/012/019/021/023/026/037 at commit 3a6ae3e (post PKC-001 resolution), the PKC-001 investigation record, and the Ops_Scope_Map re-derivation pass.*
