# Decision Brief — 2026-10-28b (prepared by Vibe, Repo Custodian — decision batch 2)

**Purpose:** decision-ready material for the batch opened by the campaign's files 17–21 sweep (AUDIT_17–21 + CROSS_FILE_PATTERN_FINDINGS_Session4, all findings-only, PKC-020) plus the stack-ups those audits queued. Same governance boundary as the 2026-10-27/27b/28 briefs: nothing here is LazarusForge doctrine until ruled; this brief carries no Spec Gate, Status, or Unknowns weight (sandbox governance boundary). Each item states the record, the options, and Vibe's recommendation. The human governing authority decides.

Repository state at time of writing: LazarusForge `982e958` (HEAD; AUDIT_17–19 filed + Metrics_Scaffold AUDIT_17 F1–F3 enactment live). VibesSandbox `52c468a` (MAINT-08). Campaign: files 1–21 DONE; next file 22 = `Admin/Resolution_Methodology.md` (Auditor_Protocols last per the approved sequence). Open Parked Concern rows: 5 (PKC-009, -010, -021, -023, -026).

---

## 1. X10 — Highest Risk parity: corpus-wide one-pass recompute (Session 4's queued sweep recommendation)

**The record:** three consecutive confirmed instances of File State `Highest Risk` understating its own sidecar's maximum Risk — Trajectories (AUDIT_13 F5: Medium vs TR-003 High), Ship_of_Theseus (AUDIT_18, both streams: Medium vs ST-004 High), Economics (AUDIT_19, both streams: Medium vs ECN-002 High / Priority Critical) — plus the structural variant at files 20–21: ADP and CIR cannot be parity-checked at all because their sidecars lack Risk fields (AUDIT_20 F4, AUDIT_21 F2). Session 4 recommends a single pass: recompute every File State Highest Risk against its own sidecar, adding missing Risk fields where sidecars lack them.

**Options:** A — fix the three confirmed headers (+ their Adm_Scope_Map entries) now, defer the corpus pass; B — authorize the full one-pass recompute (Admin/ first), the three confirmed fixes as its first actions; C — issue a scoping ruling instead (Highest Risk = doctrine-level risk, not the sidecar maximum), recorded against all three findings.

**Recommendation:** B. The streak is consecutive and the structural variant means per-file fixes leave the class open; the pass is mechanical and delegable in one go. C only if the field is intended to mean something else.

## 2. Aging Rule — consolidated aged-entry review pass

**The record:** Ship_of_Theseus ST-001–004 unreviewed 124–177 days (AUDIT_18 F1) and Economics' five open ECN entries 114–145 days (AUDIT_19 F2) — both beyond the 90-day mandatory re-audit condition; findings-only passes correctly did not advance the fields. The early-2026 cohort is likely broadly overdue.

**Options:** A — authorize a corpus-wide aged-entry pass: enumerate every sidecar entry >90 days stale, review each against current reality, advance Last Reviewed with dated notes where the entry still holds, or open its resolution path where it doesn't; B — review only the named ST/ECN entries; C — defer to each owning file's next substantive touch.

**Recommendation:** A, with a triage list produced first and date-advances enacted same-session where genuinely confirmable. Priority: ECN-002 (Critical, blocking TR-001) and ST-004 (High, Epistemic-Blocking) first.

## 3. ADP (AUDIT_20 F1–F6) — enactment

**The record:** Autonomy_Divergence_Protocol: six WARNINGs, all wrapper/pointer decay against content the campaign called "the strongest safety-relevant work audited so far": stale Scope Boundary DOES-NOTs (F1); Cross-References "GOV-021 registration pending" though registered 2026-07-27 (F2); "AP-013 (Open)" ×2 though Resolved 2026-08-19 (F3); mandatory sections absent + a Sidecar Link pointing at a nonexistent anchor + no structured sidecars for GOV-021b/c (F4); Resolution Log newest-first broken mid-file — six 08-11/08-12 entries below five 07-19 entries (F5); bare EC-001/CF-002 citations (F6).

**Options:** A — enact all six in one body-changing pass; B — enact the pointer repairs (F1–F3, F5, F6) now, sections + sidecars (F4) at the next substantive revision; C — hold for a dedicated wrapper pass.

**Recommendation:** A. Same pattern as the ratified Metrics_Scaffold F1–F3 batch, larger (ADP ≈ 66 KB); F4 and the pointer repairs belong together because the Sidecar Link fix presumes the sidecar section exists.

## 4. CIR (AUDIT_21 F1–F4) — wrapper retrofit scope

**The record:** Computational_Institutional_Reasoning (86 KB, largest file audited): the corpus's worst X11 instance — no Resolution Log (changelog lives inside the Last Audit cell, itself leading-dated 2026-07-29 while the body advanced to v0.29), no sidecar section (CIR-001 tracker lacks Risk/Priority/Type/Owner fields) (F2); bare AP-006/CF-004 in §6.2 rule headings + bare CF- IDs in File State (F3); Spec Gates names only G1/G3/G4 against the six-gate checklist (F4); Last Audit leading date stale vs the body-changing v0.27/v0.28 passes (F1).

**Options:** A — full template retrofit now (all missing sections + all four fixes); B — minimal wrapper repair now (extract a proper Resolution Log from the Last Audit cell, bump Last Audit with a dated annotation, give CIR-001 the full field set, qualify bare citations, complete Spec Gates to all six gates), full sections at the next substantive revision; C — defer CIR entirely to a dedicated pass after the remaining Admin files.

**Recommendation:** B. The minimal repair closes every graded WARNING; the full section set is better ridden on the file's next substantive revision than forced into this batch.

## 5. Canonical_Terms registry maintenance pass (AUDIT_19 F3, campaign stream)

**The record:** CT's ID-prefix registry still narrates the ECN- renumbering as "pending" though executed in Economics 2026-07-06, and repeats CT-007's erroneous EC-008 claim four months later — the X9 sub-shape (stale fact fixed where the last pass looked, surviving in the third place).

**Options:** A — small CT pass (v0.11 → v0.12): registry updated to ECN- executed; erroneous EC-008 claim corrected; B — fold into the eventual bare-ID/namespace work; C — leave for CT's next substantive revision.

**Recommendation:** A. Narrow, mechanical, un-dates two live claims; Version String Registry discipline applies (v0.11 → v0.12, all registered occurrences in the same pass). CT-007 itself stays Open for the within-Admin EC- collision per the 2026-10-28 ruling note — this is bookkeeping, not a closure.

## 6. ST-004's unfulfilled routing promise (AUDIT_18 F3, campaign stream)

**The record:** ST-004's 2026-06-26 resolution path promised "Route to Admin/Security_Protocols.md for cryptographic implementation"; Security_Protocols' sidecar has no corresponding entry (scoped to the SP fetch at 6dea6e08). A High-risk, Epistemic-Blocking security unknown with no receiving record.

**Options:** A — register the reciprocal unknown in SP's sidecar (next SEC- ID, cross-referencing ST-004 as its source: sub-threshold cumulative state-drift detection); B — reword ST-004's promise to match reality (no SP routing owed); C — leave as a recorded finding only.

**Recommendation:** A — the gap is real and security-relevant and SP is the right home; but registering a new unknown is a governance act, hence this ruling request.

## 7. Mechanical citation/vocabulary repair pass

**The record:** (a) the PKC-003 qualified-citation rule is in force, yet fresh bare-citation violations keep surfacing: Ship_of_Theseus bare AP-012 (AUDIT_18 F2, campaign stream), ADP bare EC-001/CF-002 (AUDIT_20 F6), CIR bare AP-006/CF-004 + bare CF- in File State (AUDIT_21 F3) — AUDIT_09/11-class survivors; (b) the internal-stream AUDIT_19 F3 (a different finding from the campaign's F3 — see item 8): Economics' Lessons Learned row uses "Governance" as Evidence Type and "High" as Confidence, both outside the canonical column vocabularies in File_Template. Note the two streams' AUDIT_19 F3 findings differ on the same file — a live illustration of item 8.

**Options:** A — one mechanical pass over the audited Admin files: qualify every bare cross-file citation per `File.md ID` form + conform the Economics Lessons Learned row (Audit Review / Measured fit the entry's substance); B — fix bare citations only inside the ADP/CIR enactment passes, leaving Ship_of_Theseus and the vocabulary item for later; C — fold everything into the eventual bare-ID retrofit.

**Recommendation:** A. Enforcement of in-force rules, not new doctrine; small, mechanical, closes four graded findings. Does not preempt the X3 full namespace doctrine (per-file prefixes), which stays deferred to the next CT revision per the 2026-10-28 brief item 1.

## 8. Audit-stream numbering collision

**The record:** two audit streams now both use AUDIT_NN filenames with different findings sets on the same files — repo-internal AUDIT_17–19 live in LazarusForge `Archive/Audits/`; campaign AUDIT_17–21 live in VibesSandbox `Audits/`. Grades differ (e.g., both streams' AUDIT_18/19 share F1/F2 but diverge at F3). The campaign's own note: "disambiguation prefix recommended for human ruling, dated mapping note suffices — no renumbering."

**Options:** A — renumber one stream; B — keep numbering; add a dated disambiguation mapping note (which report is which, where each lives, which findings each carries) to LazarusForge `Archive/Audits/README.md` and the sandbox SESSION_STATUS; C — prefix future campaign reports (e.g. `CAMPAIGN_AUDIT_22_…`) as a standing naming rule.

**Recommendation:** B now, plus C as the standing rule going forward. No renumbering of issued reports.

## 9. Campaign report imports + release checkpoint

**The record:** campaign AUDIT_15/16 and AUDIT_18–21 + Session 1–4 pattern docs + SESSION_STATUS live only in VibesSandbox; imports to LazarusForge have been "on human direction only" since MAINT-03. The ratified zip-in-lieu-of-signed-release checkpoint (2026-10-28 brief item 4) is unexercised since 1.28.Alpha, which predates `fee92b4` through `982e958`.

**Questions:** (a) import the campaign reports into LazarusForge `Archive/Audits/` verbatim as frozen records (the item-8 mapping note carries attribution)? (b) drop `LazarusForge-1.29.Alpha.zip` snapshotting HEAD after this batch's enactments, sha recorded in the MAINT_LOG?

**Recommendation:** (a) yes — the audit trail should be durable in the canonical repo, not only the sandbox; (b) yes, after enactments, same mechanism as 1.28.

---

## Carried (no decision requested this batch)

- Campaign continues at file 22 = `Admin/Resolution_Methodology.md`; Auditor_Protocols remains last per the approved sequence.
- X11 sweep-prompt step 15 already enacted (INTEGRITY_SWEEP_PROMPT v1.0.5). Session 4's positive-method register (enumerate-all-occurrences before closing a stale fact; block-level truth-basis labels; no circumstantial-date backfill) is queued for the Auditor_Protocols audit as the campaign instructed.
- X3 full namespace doctrine (per-file prefixes) remains deferred to the next CT revision; items 5 and 7 do not preempt it.
- Three legacy open questions (EC Tier 1 FROZEN markers; Charter ownership-table "Active" vs EC "Exploration"; same-day open-and-resolved mirroring exemption) stay recorded, not blocking — recommend ruling them at their owning files' next audits rather than blind from here.

*Prepared 2026-10-28 by Vibe (Repo Custodian, human-authorized delegated maintenance). Sources: campaign AUDIT_17–21 + CROSS_FILE_PATTERN_FINDINGS_Session4 + SESSION_STATUS (VibesSandbox `52c468a`); internal AUDIT_17–19 (LazarusForge `Archive/Audits/`); MAINT-03…MAINT-08; Decision Briefs 2026-10-27/27b/28. No LazarusForge file changes with this brief.*
