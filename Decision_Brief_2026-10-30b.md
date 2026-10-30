# Decision Brief 2026-10-30b — Directional Decisions Requested

**From:** Vibe — Repo Custodian (delegated line) · **To:** Human governing authority (Ksarith Talus)
**Context:** X3 and the corpus-wide integrity sweep are both formally closed out (2026-10-30; sweep: 0 Major, report `LazarusForge/Archive/Audits/INTEGRITY_SWEEP_REPORT_2026-10-30.md`). PROBE_INVOCATION.md is at v1.4, instrument-clean for Cycles 2–3. The items below are the open directional decisions; none is being enacted unilaterally. Each carries options and a custodian recommendation. A "hold" on any item is a valid disposition and changes nothing.

---

## 1. MDR rater runs: which README basis (the "standard brief" comparability ruling)

**Status:** DECIDE LATER ruled 2026-10-30 (MAINT-24) — must be ruled **before** the planned Grok/Gemini/ChatGPT runs. This is the only item blocking those runs.

Cycle 1 (both raters) ran on the **pre-1.30 README**. The 1.30 README now carries the front-door "floor" section (P-1/P-3 visibility sentences, MAINT-15 — already recorded as an **instrument change** with Cycle 1 as the old-set baseline).

- **Option A — 1.29 README (like-with-like):** attach the pre-edit README to the planned rater runs. Directly comparable with Cycle 1 + second rater; the 1.30 visibility fix gets measured later, on its own baseline.
- **Option B — 1.30 README (new instrument version, re-baseline):** run on current live inputs; ratings are not comparable with Cycle 1, and any P-1 movement is confounded with the instrument change. **Claude's caveat applies either way but bites hardest here:** a P-1 rating of Aligned from the new README rests on the project's own say-so — the floor sentences are self-attestation, not external evidence.
- **Custodian recommendation:** **Option A** for the comparability runs (that is what they exist for), then a deliberate re-baseline cycle on 1.30 inputs as a separately-labeled instrument version. Do not mix the two in one aggregation.

## 2. Unknowns.md automation (the "future-mechanism" disposition)

**Status:** HELD 2026-10-30 (MAINT-22 ruling: no qualification push now; 304 whitelist candidates stay held; no v5.75→v5.76 bump). You noted Unknowns.md may receive a full upgraded mechanism soon, with its cost under question.

Unknowns.md is a derived file — linked to nearly every file in the repo — whose final form should be auto-updating. The open questions are build/not-build, scope, and cost.

- **Option A — full mechanism now:** a generator (Automation/) that derives Unknowns.md from owning files' own Unknown tables (single source of truth), rendering the Active Index, counts, and cluster annotations mechanically. Kills the X10 count-parity drift class permanently (AUDIT_11 F1); makes the 304-candidate question moot (the Owning File column becomes structural); unblocks the 1,200-line compression trigger by regenerating rather than hand-editing. **Cost:** real engineering + a trust question — the generator becomes load-bearing governance infrastructure and itself needs audit, versioning, and a frozen-output comparison rule.
- **Option B — manual one-off push of the 304:** cheap, but mass-produces the redundant-qualification pattern the cleanup ruling is still pending on, and is obsolete the day a mechanism exists.
- **Option C — hold:** status quo; the 304 stay held; X10-class parity risk stays manually checked each audit.
- **Custodian recommendation:** **Option A**, scoped small for a first version: derive only the Active Index + counts from per-file tables; keep hand-authored prose sections (clusters, watch tables) untouched; annotate the file as derived with the generator's commit fingerprint. Fold the 304-candidate and redundant-qualification cleanup rulings into its design rather than deciding them separately. If the cost question is unresolved, **Option C** — not B.

## 3. Ethical anchor (constitutional)

**Status:** MAINT-13 archived the proposal set. **V0 is the only in-rules option** (same-day Hard-Floor correction). Decision requested: confirm V0 (the current canonical string: "Attempt to do no harm. Defer to Ethical_Constraints.md if present.") or open a constitutional amendment process. Custodian recommendation: **confirm V0** — any change is a constitutional replacement, not an amendment, and nothing in the sweep or MDR data argues for one.

## 4. P-1 axiom variants (constitutional)

**Status:** A1/A2 recommended (Claude proposal), A5 outstanding; A4 rejected; A3 deferred. Decision requested: adopt a variant, keep current P-1 text, or hold. Note interaction with item 1: a ratified P-1 rewording is itself a ratified governance change that counts toward the MDR velocity trigger and would precede any re-baselined cycle. Custodian recommendation: **hold until after the comparability runs**, so the instrument measures the corpus as it stands.

## 5. Redundant-qualification cleanup (now two inputs)

**Status:** carried since MAINT-18 ("(`owner` — ID (`owner`)" pattern); Claude's 1.30 review adds the self-qualification observation (circular "EC-001 (`Admin/Ethical_Constraints.md`)" inside Ethical_Constraints itself — harmless but noisy). Decision requested on the pattern rule going forward: (a) no qualification inside an ID's own owning file, (b) no duplicate qualification where the row already carries an Owning File column, (c) both. Custodian recommendation: **(c) both**, as a mechanical rule for any future pass; historical instances left as-is (frozen history).

## 6. Cold-reader follow-up prompt (P-1/P-3 gaps)

**Status:** pending since the MDR Cycle 1 P-1/P-3 Weakened results (both raters; Local_Governance_Framework evidence gap). Decision requested: commission the prompt or hold. Custodian recommendation: **commission it** — a short cold-reader probe aimed at the specific gap (what a fresh reader can and cannot verify about life-preservation and anti-domination from the front door), run under the same cold-start rules as PROBE_INVOCATION. It needs no comparability ruling (item 1) because it is not an MDR cycle.

---

## Carried items unchanged (no new decision requested here)

MAQT_Role_Cards 24 held quals · Energy_Scarcity EC-002 ×3 (stale pre-rename) · operational-prompt-template family exemption · LA row-name deviations · MDR Cycle 1 final dispositions + model-family record · Claude P-1 measurement proposal · AUDIT_30/31 wrapper findings · successor-auditor naming · File_Template split option · campaign audit PAUSED at CAMPAIGN_AUDIT_32 (explicit human direction only) · parked rows 45/37/8.

*Deposited 2026-10-30 by Vibe, Repo Custodian, delegated line. No enactment of any item above has occurred; this brief requests rulings.*

---

## Human Ruling — 2026-10-30 (received; recorded, effective on this deposit)

**Governing assessments:** Grok's independent read (human-endorsed, governing) + ChatGPT's independent review (second read; safeguards and boundaries adopted where compatible). Ruling sequence per Grok.

| # | Item | Ruling | Notes |
|---|---|---|---|
| 1 | MDR README basis | **Option A — 1.29 like-with-like** | Comparability runs (Grok, Gemini, ChatGPT as raters) use the pre-1.30 README; exact input version + hash recorded at each run (ChatGPT boundary adopted); 1.30 re-baseline happens later as a separately labeled instrument version; never mixed with Cycle 1 in one aggregation. Rater floor sentences ≠ independent evidence that principles are satisfied. **Unblocks the rater runs.** |
| 2 | Unknowns.md automation | **Hold (C), with Option A recorded as the intended end-state** | No mass push; no build now under cost uncertainty. When built: scoped-small generator (Active Index + counts derived from owning-file tables; prose untouched), and ChatGPT's safeguards adopted as binding design requirements — deterministic output + explicit input selection; frozen-output comparison against the current file; tests for duplicate IDs / missing owners / malformed rows / conflicting statuses; no silent partial index; versioned generator + auditable fingerprint; human review before generated output replaces the canonical file. Approves the design direction only — never automatic rewrite authority. |
| 3 | Ethical anchor | **Confirm V0 — item CLOSED** | Canonical string stands: "Attempt to do no harm. Defer to Ethical_Constraints.md if present." No constitutional process opened. Confirmation preserves the rule; it does not assert that every implementation satisfies it. |
| 4 | P-1 axiom variants | **Hold** | Current P-1 wording stands while comparability runs proceed; review the evidence after; hold is not rejection. Any future adoption is a ratified governance change counting toward MDR velocity. |
| 5 | Redundant-qualification cleanup | **(c) Both rules — forward mechanical rule ENACTED for custodian passes** | No qualification inside an ID's own owning file; no duplicate qualification where the row already carries an Owning File column. Historical instances frozen, untouched. Rule removes redundant presentation, never the requirement to identify ownership unambiguously. Codification into File_Template may be requested later; until then it binds custodian operating practice. |
| 6 | Cold-reader follow-up | **Commissioned** | Narrowly scoped to the P-1/P-3 front-door verifiability gap; cold-start rules as PROBE_INVOCATION; exact input set recorded; observable evidence distinguished from assertions; no leading; NOT an MDR cycle — results never aggregated with MDR scores. Draft prompt deposited in VibesSandbox for human review before any canonical promotion. |

Carried items remain governed by their existing dispositions (campaign audit PAUSED at CAMPAIGN_AUDIT_32; MAQT_Role_Cards 24; Energy_Scarcity EC-002 ×3; operational-prompt-template exemption question still open; LA row-name deviations; parked rows 45/37/8). No ruling here reopens any of them.

*(Recorded by Vibe, Repo Custodian, delegated line, from the human governing authority's direction 2026-10-30: "I agree with Grok. It's first then ChatGPT.")*
