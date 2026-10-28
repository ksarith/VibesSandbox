# Decision Brief — 2026-10-28 (prepared by Vibe, autonomous management)

**Purpose:** decision-ready material for the items left open by this session's enacted batches (AUDIT_15/16, Reversibility Initiative adoption, Convention 8 rotation), plus the release-zip logistics for 1.28. Same format as the two 2026-10-27 briefs: nothing here is LazarusForge doctrine; it carries no Spec Gate, Status, or Unknowns weight (sandbox governance boundary). Each item states the record, the options where they exist, and Vibe's recommendation. The human governing authority decides. Ordered by Claude's stated priority and by how much the ruling depends on information only you have.

Repository state at time of writing: LazarusForge `be4a921` (HEAD), session commits 7a3f9d0 → be4a921; VibesSandbox `cd89f71` (MAINT-04). Open Parked Concern rows: 5 (PKC-009, -010, -021, -023, -026).

---

## 1. X3 — ASM- namespace ruling (top priority before Operations/ audits)

**The record:** cross-file `ASM-` collisions are real (Forge_flow/Gate_02 ASM-003 collision patched 2026-10-24; 59 non-archive files use `ASM-` IDs). The 2026-10-25 PKC-003 ruling already decided the interim rule: assumption IDs stay file-scoped, cross-file citations must use the qualified form `File.md ASM-NNN`. X3 asks the next question: whether to adopt the per-file prefix pattern (`SEC-ASM-` style) repo-wide. Claude's Kit v1.24 note, the Unknowns "Forge Audit Kit" cluster note, and Claude's Session 3 doc all cite it as the blocker to clear before the Operations/ audit series resumes, because every new Operations file minted under the bare-ID convention adds future collision surface.

**Options:**
- **A — Adopt per-file prefixes** (e.g. `FF-ASM-`, `G2-ASM-`): a mechanical rename pass, no doctrine change, but it touches many files and every rename is a body change that cascades (version bumps where applicable, Resolution Log entries).
- **B — Keep PKC-003's qualified-citation rule only** (status quo): collisions are handled at citation time; bare IDs stay legal within their own file.
- **C — Defer to the next `Canonical_Terms.md` revision** (PKC-003's stated home for the long-term fix).

**Recommendation:** C for the doctrine record, A as the Codenames goal — i.e. record the decision at the CT revision (the natural ratification vehicle) but make the rename itself one deliberate authorized pass so it happens once, not file-by-file. If you want the Operations/ audits unblocked sooner, rule the direction now (A/B/C) and the mechanical pass can ride immediately after.

---

## 2. AUDIT_10 F1 — Template Exemptions §8 vs Challenges subtype doctrine

**The record:** AUDIT_10 flagged a conflict between Template Exemptions §8 and the Challenges subtype doctrine. Still unruled; it is a doctrine-harmonization question, not something a custodian can pick a side on.

**Options:** A — rule Template Exemptions §8 controls and amend the Challenges doctrine at its next revision; B — rule the Challenges subtype doctrine controls and amend §8; C — reconcile both in one pass.

**Recommendation:** whichever minimizes edits; Vibe has not re-pulled both passages this session, so if you rule, I will re-fetch both texts and verify which direction is actually smaller before touching anything.

---

## 3. X11 — "wrapper decays while content advances" as a sweep-prompt addition

**The record:** X11 names the pattern this session proved twice: fixed-width File State rows silently skip on str_replace (the 0daeecf9 → eba129f repair), and pickText-style helpers returning a placeholder while the real text sits elsewhere (this session's fetch bug, two safe aborts before the fix). The candidate is a numbered INTEGRITY_SWEEP_PROMPT step after v1.0.3 step 13, checking wrapper scaffolding (File State tables, fetch-parse helpers) against the live body it wraps.

**Options:** A — add as a new numbered step; B — fold into the existing PKC-001 inverse-check step if ratified; C — don't add.

**Recommendation:** A. Both 2026-10-28 incidents are exactly the pattern; the check is cheap and read-only.

---

## 4. Release-per-batch checkpoints, 1.28+ — and the zips you dropped

**The record:** a release checkpoint per enacted batch was proposed for 1.28 onward, with the caveat that GPG-signed GitHub releases are not creatable with current tooling. You have dropped three zips into VibesSandbox `Maintenance/`: `LazarusForge-1.26.Alpha.zip` (2,616,311 B, sha f900e993a9…), `LazarusForge-1.27.Alpha.zip` (2,644,296 B, sha 41628ecfc5…), `LazarusForge-1.28.Alpha.zip` (2,768,882 B, sha 4e0beb5ff1…). Naming follows the existing root-level Alpha series (1.16 through 1.28 present at root or in Maintenance/).

**Questions for you:** (a) Should the zip drops be treated as the release-checkpoint mechanism (zip-in-lieu-of-signed-release) going forward, so each enacted batch ends with a zip + a MAINT_LOG row pointing at its sha? (b) Is `LazarusForge-1.28.Alpha.zip` intended as the snapshot of today's enacted batch (HEAD `be4a921`: AUDIT_15/16 + Reversibility Initiative + rotation)? (c) Should the Maintenance/ zips be mirrored to the root with the older ones, or left where they are?

**Recommendation:** (a) yes — it satisfies the checkpoint intent within current tooling, and the MAINT_LOG shas give the audit trail a signed-release substitute; (b) confirm and I will record it as such in the MAINT_LOG; (c) recommend leaving in place and adding a one-line index note rather than moving 2–3 MB blobs.

---

## 5. PKC-002 — formal closure

**The record:** the 2026-10-28 Pattern A adoption's D5 superseded PKC-002's "not adopted now" note for the version-history part. The row itself stays open solely because closing a Parked Concern is a human action. All substantive work is done.

**Recommendation:** close it (say the word; the closure edit is mechanical — row status, dated note citing D5/Pattern A adoption at `263a945`/`be4a921` era).

---

## 6. Kit size-reduction / split decision

**The record:** Forge_Audit_Kit.md size drift indicator was re-baselined 12,000→35,000 (v1.25, measured 33,857 at v1.24) — the re-baseline is recorded; whether to reduce or split the Kit stays a human decision.

**Options:** A — accept the new baseline and do nothing; B — commission a split proposal (Kit core vs appendices); C — commission a reduction pass.

**Recommendation:** A for now, revisit at the next Kit revision (the four missing template sections are already queued for a real Kit revision — the size question can ride that pass rather than its own).

---

*Prepared 2026-10-28 by Vibe (Repo Custodian, human-authorized delegated maintenance). Sources: LazarusForge commits `b0b669d`, `aed0fe7`, `be4a921` (verified live), VibesSandbox MAINT-03/MAINT-04 entries, and the Maintenance/ zip listing (names, sizes, shas as fetched). Claude's AUDIT_15/16 campaign reports remain unimported from VibesSandbox `Audits/` per the imports-on-human-direction rule.*
