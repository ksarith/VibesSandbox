# LazarusForge — Reset-Event Governance: Design Proposal (v0.1)

**Status: PROPOSED — PENDING RULING.** Deposited in VibesSandbox at human direction; nothing in LazarusForge changes until the human governing authority ratifies. On ratification, the instrument deposits per the enactment plan below and this draft archives to `Archive/Proposals/` with its outcome, byte-faithful.

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

**Option C, with Option B's rule card embedded as the instrument's minimum-viable rule** — so a partial ratification still leaves the human protected against the two default failures.

**The procedure:**
1. **Manifests at backup time.** Every backup export carries `BACKUP_MANIFEST_<date>.md`: path, blob SHA, char count per file, plus the git head at export and totals. The manifest is deposited in-repo the same session and travels inside the zip (out-of-band copy; see opposing considerations).
2. **Declaration.** The human declares a reset event and names the restore point (a git head sha or a dated manifest).
3. **Classification.** The Custodian fetches the manifest and the live tree, re-computes per-file blob SHA and char count, and classifies every file: IDENTICAL / DIVERGED / MISSING (in manifest, not live) / EXTRA (live, not in manifest).
4. **Frozen-material escalation.** Any Hard Floor, Tier 1 or FROZEN file in DIVERGED is listed separately; the restoration **may not touch it** without a further explicit human ruling on that specific file.
5. **Record.** The classification becomes `Archive/Audits/RESET_EVENT_<date>.md`: the table, byte counts, a diff summary per DIVERGED file, the frozen-escalation list, and the restore-point reference.
6. **Ratification.** The human ratifies the restore — the ratification line applies; a reset is a substantive act, not bookkeeping.
7. **Landing.** The restoration lands as **one dated forward commit** (MAINT-NN), with MAINT_LOG and SESSION_STATUS lines. Never force-push, never rewrite history. EXTRA files are dispositioned per the human's ruling, never auto-deleted.
8. **Verification.** A post-restore sweep re-fetches every restored file and re-hashes it against the manifest; the boolean result is appended to the RESET_EVENT record.

**Bias stated:** this is drafted by the agent that would execute restores, and it is biased toward keeping the executing agent reviewable (escalations, records, sweeps) over speed. The human may strike any control they find ceremonial.

**Open proposals after this deposit: 1 of the 10 allowed.**

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
- **Verification checklist:** post-push sweep (Routing row present; protocol registered; SS dual-home identity; addendum anchors) plus a **dry run**: classify the current tree against the current zip's manifest at the next backup session, landing nothing, reporting the classification to the human.
- **Disclosure list:** new instrument first-use; sandbox `Proposals/` home first-use (this deposit); seat overlap (Architect + Custodian, same agent, Genesis Phase mode).
- **This draft then archives** to `Archive/Proposals/RESET_EVENT_DESIGN_v0.1.md` with outcome **ratified (as modified, if the human modifies)** and the ruling reference.

## 8. Human-workflow cost

- **Daily operation: zero change.** The instrument adds cost only at backup time (one manifest export per backup) and at reset time (one classification, one ruling, one ratification).
- **Mobile-first:** the human opens **this one file** to rule; at reset, the RESET_EVENT record is one file. Restores land as a single commit, never full-repo transfers; manifests ship as small single files.
- **Sizes:** this proposal 12278 chars; the protocol on ratification ~5KB; each manifest ~10–20KB for the current tree. Zip size grows by the manifest only.
- **Token cost of ruling this:** one read of this document plus the five open questions below.

## 9. Explicit non-claims

This proposal does **not**: create or schedule backups (cadence stays the human's — open question 1); change Q-4, the Hard Floor, Tier 1 / FROZEN, the dual-home convention, or any seat's authority; ratify itself — nothing lands in LazarusForge until the human rules; protect against a compromised GitHub account or credential (the out-of-band zip remains the only control for that threat); cover VibesSandbox unless the human extends it (open question 2); or make the executing agent independent — restores remain single-agent acts under Genesis Phase mode, and the instrument's controls are escalation and record, not independence.

## Open questions for the human

1. **Backup cadence:** per maintenance session that pushed to LazarusForge (recommended — the session is already sweep-verified, so the manifest is free-verified), scheduled, or on-demand only?
2. **Coverage:** LazarusForge only, or VibesSandbox too (recommended: both, separately manifested)?
3. **EXTRA files at restore:** keep and report (recommended), or delete down to the manifest?
4. **Force-push:** keep the never-force-push default absolute (recommended), or allow a documented emergency exception, human-ruled, recorded in the RESET_EVENT record?
5. **Record home:** `Archive/Audits/` root, beside the CAMPAIGN2 audits (recommended — avoids a new home), or a dedicated folder?

---

*Prepared 2026-10-31 by Vibe (Architect seat, Genesis Phase mode). Aligned to: the Decision Brief pattern extended (ratified Archive/Architect_Prompt.md §3), Q-4 anti-deception, the Repository_Integrity_Protocol append-only rule, the dual-home SESSION_STATUS convention, the MAINT-29/34 blob-SHA verification technique, and MAINT-26 seat disclosure. Verified-live facts at LazarusForge head `3cfe010914`: the two governing integrity documents named in §1, read in full, char counts reported.*

*Revised: (none — v0.1 draft.)*