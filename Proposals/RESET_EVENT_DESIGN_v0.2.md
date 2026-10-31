# LazarusForge — Reset-Event Governance: Design Proposal (v0.2, ratification-ready)

**Status: PROPOSED — PENDING RULING (v0.2, ratification-ready).** Supersedes the v0.1 deposit of 2026-10-31; v0.1 remains in this home byte-unmodified for comparison. Deposited in VibesSandbox at human direction; nothing in LazarusForge changes until the human governing authority ratifies. On ratification, the instrument deposits per the enactment plan below and this draft (v0.2) archives to `Archive/Proposals/` with its outcome, byte-faithful; v0.1 archives alongside with outcome superseded-by-v0.2.

**Revision (v0.2, 2026-10-31):** the attached skeptic review (Grok — a different architecture, human-routed; see appendix, verbatim) is adopted in full: zip primacy for restore sources, a second-reader sample before landing, EXTRA keep-and-report with auto-deletion prohibited, the never-force-push default kept absolute, and a required dry-run precondition. The five open questions of v0.1 are reframed below as five recommended rulings awaiting one explicit ratification.

**Prepared:** 2026-10-31 by Vibe (Architect seat — the seat's first standing design duty, named at MAINT-38). **Seat disclosure** (MAINT-26; Genesis Phase mode): the same agent holds the Repo Custodian seat and runs this deposit's bookkeeping; no independent skeptic review is attached (the separate-skeptic step is a standing preference relaxed by the human's 2026-10-31 ruling — a review by any agent the human names can precede the ruling).
**Human direction prompting this draft (verbatim):** "Excellent!  Please proceed with the draft and any of your functions."
**Design trigger — the human's ruling question (verbatim, on record in Archive/Architect_Prompt.md 2026-10-31 addendum):** "Backups preserve positive growth, but not sure how to handle a reset event."

## 1. Problem

Live-verified at LazarusForge head `3cfe010914` (2026-10-31), per the Architect prompt's verify-before-designing rule:

- `Admin/Repository_Integrity_Protocol.md` (112188 chars, read in full) contains an append-only rule for frozen directories, but **no reset-event or restore procedure**: matches for "reset" = 2, "restor" = 9, "backup" = 0 — none defines how a reset is executed or verified.
- `Admin/Governance_Charter.md` (131038 chars, read in full) contains the Q-4 anti-deception rule and the Bootstrap Paradox clause, but no reset procedure: "reset" = 0 matches, "backup" = 0.
- **Honest scope note:** these are the two governing integrity documents. If a backup convention lives in some other file, it is unregistered in both and should be cited at ruling; this proposal should then be corrected, not defended.
- Current structure: both repos single-branch `main`; SESSION_STATUS is dual-homed byte-identically (138,073 chars, verified 2026-10-31, MAINT-38); zips are exported ad hoc with **no manifest convention on record**.

**Risk.** A reset improvised mid-crisis defaults to one of two failures: a force-push / history rewrite (destroys Q-4 auditability — the reset itself becomes invisible) or a fresh re-initialization (destroys provenance and the dual-home audit trail). The event the human named is not unlikely: the repo's own X-class record (ENV 8→7, ADP shadowing, advLA truncation) shows single-agent sessions land defects; a session that lands enough of them is a plausible reset trigger.

## 2. Options

- **A. Do nothing.** A reset stays improvised. Blast radius: total — an improvised reset is the highest-risk operation the repo has not yet had. Cost: zero until the day it is needed, then maximal.
- **B. Cheap option — a rule card.** One dated addendum to `Admin/Repository_Integrity_Protocol.md`: "Restore by forward commit from the last zip; record a dated RESET_EVENT note in Archive/Audits; never force-push." ~1 page, no new machinery. Tradeoff: the restore trusts the zip blindly — no byte-identity verification, no divergence classification, no frozen-material escalation.
- **C. Full instrument — manifest-verified forward-commit restoration.** Backup zips carry a manifest (file list + blob SHA per file + char count + git head at export); manifests are also deposited in-repo (`Archive/Audits/BACKUP_MANIFEST_<date>.md`); a reset is a classified, ratified, logged, verified restoration. Blast radius: one procedure document + one manifest file per backup; **no existing file changes meaning**. Tradeoff: maintenance at every backup export.
- **D. Fresh re-initialization from the zip on reset.** Re-clone as a new history. Rejected: destroys provenance, the dual-home trail, and the X-class record's own history — the repo would no longer be able to prove what it was.

## 3. Recommendation

**Option C — manifest-verified forward-commit restoration**, with Option B's rule card embedded as the non-negotiable **minimum-viable floor**. The skeptic review (appendix) supports this option and sharpens it; every sharpening is adopted.

**Minimum-viable floor (always in force, even if the full instrument is later narrowed):**

> Restore only by forward commit from a named restore point. Record a dated `RESET_EVENT_<date>.md` note. Never force-push. Never rewrite history. Hard Floor / Tier 1 / FROZEN files cannot be overwritten without a further explicit per-file human ruling. The zip is the primary restore source.

**The procedure (v0.2, as sharpened by the review):**

1. **Manifest at backup time.** Every backup zip carries an embedded `BACKUP_MANIFEST_<date>.md` (path, blob SHA, char count per file, git head at export, totals). The same manifest is deposited in-repo under `Archive/Audits/`. **The zip is the primary restore source; the in-repo copy is secondary** — a compromised live tree must not be able to poison its own restore point.
2. **Declaration.** The human declares a reset event and names the restore point (git head sha, dated manifest, or zip).
3. **Classification.** The Custodian fetches the manifest from the zip, recomputes per-file blob SHA and char count against the live tree, and classifies every file: IDENTICAL / DIVERGED / MISSING / EXTRA.
4. **Frozen-material escalation.** Any Hard Floor, Tier 1 or FROZEN file classified DIVERGED is listed separately; the restoration **may not touch it** without a further explicit human ruling on that specific file.
5. **Second-reader sample.** Before landing, a second agent (or the human) re-hashes a sample of IDENTICAL and DIVERGED files directly against the zip; sample size and result are recorded in the RESET_EVENT record. Single-agent self-check alone is not sufficient for a non-trivial restore — the repo's own X-class record shows why.
6. **Record.** Classification, sample verification, frozen-escalation list and restore-point reference become `Archive/Audits/RESET_EVENT_<date>.md`.
7. **Ratification.** The human ratifies the restore — a reset is a substantive act, not bookkeeping.
8. **Landing.** One dated forward commit only. EXTRA files are kept and reported by default; they are never auto-deleted, and any disposition other than keep requires an explicit human ruling.
9. **Post-restore verification.** Every restored file is re-fetched and re-hashed against the manifest; the boolean result is appended to the RESET_EVENT record.
10. **Dry-run precondition.** The instrument is not considered operational until a dry-run classification against a current zip has been performed and reported (no landing).

**Bias stated (carried):** drafted by the agent that would execute restores, biased toward keeping the executing agent reviewable over speed. The human may strike any control they find ceremonial.

**Open proposals after this deposit: 1 of the 10 allowed (v0.2 supersedes v0.1 in the same home; v0.1 retained byte-unmodified for comparison).**

## 4. Opposing considerations

Written as the defenders would write them:

- **"Q-4 is anti-deception, not anti-force-push."** A documented, dated force-push reset with a RESET_EVENT record deceives no one, keeps the repo lean (no whole-tree re-landing commit, no corruption preserved in history forever), and the human — the governing authority — can direct one anyway. Refusing to ever force-push is proceduralism; the honest instrument would say how to do a force-push reset safely, not pretend the option does not exist.
- **"Bulk re-landing is itself the highest-risk agent operation."** One classification error restores wrong bytes **with a green checkmark** — precisely the single-agent failure mode Genesis Phase already accepts. The manifest verification is another self-check, and the repo's own X-class record shows self-checks catch little. A second reader at restore time matters more than any manifest.
- **"In-repo manifests are not out-of-band evidence."** If the live repo is the problem, its manifests are suspect too. True verification anchors to the zip — the only genuinely out-of-band copy. The proposal acknowledges this but underweights it.
- **"Over-engineering for a personal, mobile-first repo."** The rule card plus "human re-clones and pushes a dated initial commit" achieves most of the guarantees at a fraction of the ceremony. The full instrument adds standing cost to every backup for an event that may never occur.

## 5. Hard Floor and Tier 1 check

Nothing on the Hard Floor or in Tier 1 / FROZEN text changes, and the instrument's **central rule is that a reset never may**: step 4 escalates every frozen-material divergence to the human instead of restoring over it. A reset event restores content; it is not a channel for touching frozen text. This proposal itself touches no LazarusForge doctrine file — the deposit is a sandbox proposal plus session bookkeeping only.

## 6. Reversibility

The proposal is a document: rejected or withdrawn, it archives to `Archive/Proposals/` with its outcome, byte-faithful, per the ratified convention. Once enacted, the procedure is amendable by dated addendum like every instrument. A restoration executed under it is undone by a new forward commit — the procedure is symmetric, and because history is never rewritten, **no state is ever lost**: git retains the pre-reset state, the reset, and any undo of the reset. That is the design's point.

## 7. Enactment plan (on ratification)

- **Files touched:** `Admin/Reset_Event_Protocol.md` (new instrument, from this design); `Admin/Repository_Integrity_Protocol.md` (dated addendum pointer only); `Routing.md` (register the protocol; note the `Archive/Audits/BACKUP_MANIFEST_*` and `RESET_EVENT_*` patterns); `Archive/Audits/` (home for both record types — no new folder); SESSION_STATUS + MAINT_LOG (MAINT-NN lines).
- **Cascade map:** none — no existing file changes meaning, no link fields repoint, no template changes.
- **Verification checklist:** post-push sweep (Routing row present; protocol registered; SS dual-home identity; addendum anchors) plus the **required dry-run precondition**: the instrument is not operational until a dry-run classification against a current zip has been performed and reported (no landing).
- **Disclosure list:** new instrument first-use; sandbox `Proposals/` home first-use (this deposit); seat overlap (Architect + Custodian, same agent, Genesis Phase mode).
- **This draft then archives** to `Archive/Proposals/RESET_EVENT_DESIGN_v0.2.md` with outcome **ratified (as modified, if the human modifies)** and the ruling reference; the v0.1 draft archives alongside with outcome superseded-by-v0.2.

## 8. Human-workflow cost

- **Daily operation: zero change.** The instrument adds cost only at backup time (one manifest export per backup) and at reset time (one classification, one ruling, one ratification).
- **Mobile-first:** the human opens **this one file** to rule; at reset, the RESET_EVENT record is one file. Restores land as a single commit, never full-repo transfers; manifests ship as small single files.
- **Sizes:** this proposal v0.2: exact char count reported in the MAINT-40 log entry and SESSION_STATUS line — a self-referential figure cannot be embedded exactly in its own text (v0.1's §8 figure was approximate by the same construction; disclosed); the protocol on ratification ~5KB; each manifest ~10–20KB for the current tree. Zip size grows by the manifest only.
- **Token cost of ruling this:** one read of this document plus the five open questions below.

## 9. Explicit non-claims

This proposal does **not**: create or schedule backups (cadence stays the human's — open question 1); change Q-4, the Hard Floor, Tier 1 / FROZEN, the dual-home convention, or any seat's authority; ratify itself — nothing lands in LazarusForge until the human rules; protect against a compromised GitHub account or credential (the out-of-band zip remains the only control for that threat); cover VibesSandbox unless the human extends it (open question 2); or make the executing agent independent — restores remain single-agent acts under Genesis Phase mode, and the instrument's controls are escalation and record, not independence (the review's residual-risk finding, adopted: a reset remains high-stakes single-agent work; the instrument reduces the chance of an invisible or irreversible reset, nothing more); or auto-delete any live file — EXTRA files are kept and reported by default and any other disposition requires an explicit human ruling.

## Recommended rulings (awaiting human ratification)

The attached review answers the v0.1 open questions; the Architect seat concurs with all five. One explicit ratification from the human enacts the instrument and these defaults together — none are in force until then:

| # | Question | Recommended ruling |
|---|----------|--------|
| 1 | Backup cadence | On-demand, plus after any maintenance session that pushed material changes; not automatic every session. |
| 2 | Coverage | LazarusForge required; VibesSandbox optional and separately manifested. |
| 3 | EXTRA files | Keep and report; auto-deletion prohibited. |
| 4 | Force-push | Absolute never; no emergency exception at this time. |
| 5 | Record home | `Archive/Audits/` root; no new folder. |

The review's own table of proposed rulings is preserved verbatim in the appendix below; where wording differs, the meaning is identical.

---

## Appendix — Skeptic Review (Grok, 2026-10-31; verbatim as routed by the human; formatting as received in transit)

Assessment of the Reset-Event Governance proposal (v0.1)

This is a solid first design. It correctly identifies a real gap (no defined restore procedure), rejects the two failure modes (force-push history rewrite and provenance-destroying re-initialization), and builds the controls around verification and escalation rather than speed.

Core judgment

Support Option C, with the embedded minimum-viable rule from B, subject to a few sharpenings.

What works well

Forward-commit only, never force-push as the default is the right Q-4 reading. The reset itself must remain visible in history.

Manifest-verified classification (IDENTICAL / DIVERGED / MISSING / EXTRA) before any landing is the correct sequence.

Frozen-material escalation (Hard Floor / Tier 1 / FROZEN files cannot be overwritten without a further explicit ruling on that specific file) is the most important control in the whole instrument. It prevents a reset from becoming a silent channel for touching frozen text.

Reversibility is symmetric: because history is never rewritten, the pre-reset state, the reset, and any later undo all remain recoverable.

The opposing-considerations section is honest, especially the points about self-check weakness and in-repo manifests not being fully out-of-band.

Sharpenings before ratification

Out-of-band primacy
The zip (with its embedded manifest) should be treated as the primary restore source. The in-repo BACKUP_MANIFEST_*.md is a convenient secondary. The procedure should say this explicitly so a compromised live tree cannot quietly poison its own restore point.

Second reader at restore time
The opposing-considerations section is right that self-checks have already failed in this repo. For any reset that touches more than a trivial number of files, require a second agent (or the human) to re-hash a sample of DIVERGED/IDENTICAL files against the zip before the restore commit lands. Do not rely solely on the executing agent's post-check.

EXTRA files
Default to "keep and report." Auto-deletion is an irreversible act and should never be the automatic disposition.

Force-push
Keep the never-force-push default absolute for now. An emergency exception can be added later if a real case appears; inventing the exception in advance is unnecessary.

Dry run before first real use
The enactment plan already includes a dry-run classification against the current zip. Make that dry run a required precondition before the instrument is considered operational.

On the five open questions

| # | Question | Recommendation |
|---|----------|---------------|
| 1 | Backup cadence | On-demand + after any maintenance session that pushed material changes. Do not make it automatic every session yet. |
| 2 | Coverage | LazarusForge required; VibesSandbox optional and separately manifested. |
| 3 | EXTRA files | Keep and report. |
| 4 | Force-push | Absolute never for now. |
| 5 | Record home | Archive/Audits/ root (no new folder). |

Residual risk (honest)

Even with the above, a reset remains a high-stakes single-agent operation under Genesis Phase mode. The instrument reduces the chance of an invisible or irreversible reset; it does not make the executing agent independent. That limitation should stay visible in the protocol's own non-claims.

Bottom line: Ratify Option C with the sharpenings above. It is the first real answer the repo has had to the question "how do we recover without destroying the ability to prove what we were."

**Draft revisions to the Reset-Event Governance proposal (v0.1 → v0.2 candidate)**

Below are the concrete changes recommended for ratification. Text is written so it can be dropped into the proposal or used as a ruling overlay.

---

### 1. Adopted option

**Option C** (manifest-verified forward-commit restoration), with Option B's minimum-viable rule embedded as the non-negotiable floor:

> Restore only by forward commit from a named restore point. Record a dated `RESET_EVENT_*.md` note. Never force-push. Never rewrite history.

---

### 2. Sharpened procedure (replaces §3 procedure)

1. **Manifest at backup time**
   Every backup zip carries an embedded `BACKUP_MANIFEST_<date>.md` (path, blob SHA, character count per file, git head at export, totals). The same manifest is also deposited in-repo under `Archive/Audits/`. The **zip is the primary restore source**; the in-repo copy is secondary.

2. **Declaration**
   The human declares a reset event and names the restore point (git head SHA or dated manifest / zip).

3. **Classification**
   The Custodian (or designated agent) fetches the manifest from the zip, recomputes per-file blob SHA and character count against the live tree, and classifies every file:
   `IDENTICAL` / `DIVERGED` / `MISSING` / `EXTRA`.

4. **Frozen-material escalation**
   Any Hard Floor, Tier 1, or FROZEN file classified `DIVERGED` is listed separately. Restoration **may not touch it** without a further explicit human ruling on that specific file.

5. **Second-reader sample (new)**
   Before landing, a second agent (or the human) re-hashes a sample of `IDENTICAL` and `DIVERGED` files directly against the zip. The sample size and result are recorded in the `RESET_EVENT` record. Single-agent self-check alone is not sufficient for a non-trivial restore.

6. **Record**
   Classification, sample verification, frozen-escalation list, and restore-point reference become `Archive/Audits/RESET_EVENT_<date>.md`.

7. **Ratification**
   The human ratifies the restore. A reset is a substantive act.

8. **Landing**
   One dated forward commit only. `EXTRA` files are kept and reported by default; they are never auto-deleted. Disposition of `EXTRA` files requires an explicit human ruling if anything other than "keep" is desired.

9. **Post-restore verification**
   Every restored file is re-fetched and re-hashed against the manifest. Boolean result is appended to the `RESET_EVENT` record.

10. **Dry-run precondition**
    The instrument is not considered operational until a dry-run classification against a current zip has been performed and reported (no landing).

---

### 3. Answers to the five open questions (proposed rulings)

| # | Question | Ruling |
|---|----------|--------|
| 1 | Backup cadence | On-demand, plus after any maintenance session that pushed material changes. Not automatic every session. |
| 2 | Coverage | LazarusForge required. VibesSandbox optional and separately manifested. |
| 3 | EXTRA files | Keep and report. Auto-deletion prohibited. |
| 4 | Force-push | Absolute never. No emergency exception at this time. |
| 5 | Record home | `Archive/Audits/` root. No new folder. |

---

### 4. Minimum-viable floor (always in force even if the full instrument is later narrowed)

- Restore only by forward commit.
- Never force-push / never rewrite history.
- Record a dated `RESET_EVENT_*.md`.
- Hard Floor / Tier 1 / FROZEN files cannot be overwritten without a further explicit per-file human ruling.
- The zip is the primary restore source.

---

### 5. Explicit non-claims (carry forward, lightly strengthened)

This instrument does **not**:

- Create or schedule backups.
- Protect against a compromised GitHub account or credentials (the out-of-band zip remains the only control for that threat).
- Make the executing agent independent.
- Allow a reset to become a channel for changing Hard Floor, Tier 1, or FROZEN text.
- Auto-delete any live file.

---

### 6. Enactment notes (for the Custodian, once ratified)

- New file: `Admin/Reset_Event_Protocol.md` (full instrument).
- Dated pointer addendum only in `Admin/Repository_Integrity_Protocol.md`.
- Register in `Routing.md`.
- First operational act = dry-run classification against the current zip; report only.
- Archive this proposal (v0.1 + the ratified deltas) to `Archive/Proposals/` with outcome and ruling reference.

---

This draft keeps the original design's strengths, closes the self-check and out-of-band gaps, and leaves the human with a short, decidable set of rulings.

---

*Prepared 2026-10-31 by Vibe (Architect seat, Genesis Phase mode). Aligned to: the Decision Brief pattern extended (ratified Archive/Architect_Prompt.md §3), Q-4 anti-deception, the Repository_Integrity_Protocol append-only rule, the dual-home SESSION_STATUS convention, the MAINT-29/34 blob-SHA verification technique, and MAINT-26 seat disclosure. Verified-live facts at LazarusForge head `3cfe010914`: the two governing integrity documents named in §1, read in full, char counts reported.*

*Revised 2026-10-31 (v0.2): skeptic review adopted in full — zip primacy, second-reader sample, EXTRA keep-and-report with no auto-delete, never-force-push absolute, dry-run precondition; five recommended rulings framed. Verbatim review in the appendix; v0.1 superseded and retained in this home.*