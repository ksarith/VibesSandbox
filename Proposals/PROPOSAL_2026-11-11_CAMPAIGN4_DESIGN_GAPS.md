# PROPOSAL_2026-11-11_CAMPAIGN4_DESIGN_GAPS — what the adversarial passes expose about the design layer

**Status:** PARTIALLY RATIFIED 2026-11-11 — Option B (the cheap subset) ratified by the human governing authority ("Let's ratify those easy items."): D-2, D-8, D-9 and D-10 enacted at MAINT-129 (Kit v1.33 named-record probe; IIL routing rule + IIL-20261110-01 with classification pending; D-9 endorsement recorded; D-10 harness gates adopted in-session, PKC-045 work-record item). D-1 and D-3..D-7 remain PROPOSED and open (open proposals 2–7 of 10 from this seat). Deposited at VibesSandbox `Proposals/` per Architect_Prompt.md §4 (RATIFIED 2026-10-31 — IN FORCE). [MAINT-128 deposit; ratification enactment recorded in the MAINT-129 entry and STATE.md.]
**Drafted by:** Vibe, Architect seat. Declaration: "Operating as Synthesizer per Auditor_Protocols.md v0.47" (mapping proposed, not ratified). Architect primary; this session's line also held the Auditor and Repo Custodian seats earlier today (Campaign 4 execution and MAINT-125/126/127) — non-independence disclosed in §4 and §10.
**Bootstrap (live at LF `35973fae`, VS `49398bef`):** TWGW read complete (5 entries; Last updated 2026-11-08, MAINT-81; the entry-5 lesson — "a correction stated in prose is not a control" — is a standing constraint on this proposal). Pattern document re-read live (25,805 chars, final-update state). The Decision Brief 2026-11-11 (VS root) is the ruling surface this proposal is designed to feed, not duplicate.
**Evidence base:** `Archive/Audits/CAMPAIGN4_PATTERN_DOC_2026-11-10_FILES_01-06.md` (final state), the kickoff tracker (addenda 0–33), MAINT-120..127, the human's upload commits `928f9eec`/`35973fae`.

## 1. Problem

Campaign 4 audited all 34 Admin/ files, findings-only. Its systemic yield, measured live from the pattern document's final state:

| # | Class | Measured yield |
|---|-------|----------------|
| 1 | 90-day Aging Rule trips | 67 of 84 open sidecar entries (58 of 75 registered-only); 12 systemic instances, 21 control cases |
| 2 | Relocation-repair-miss | 19 instances + 1 tooling corroboration (`audit_lib.py`) |
| 3 | Missing-record attestation (GOV-022) | 2 MAJOR instances + 1 git-verified false verification record |
| 4 | File State recorded-vs-live (F-AVE-1 class) | 3 instances + 1 positive control (Ship_of_Theseus) |
| 5 | Git-verified unlogged changes | 4 files (CT/HDL/NT/ST); every prior log-vs-body clean grade provisional |
| 6 | Index-mirror decay (Pattern 6) | 5 instances across 3 index files |
| 7 | Stale conditions on resolved events (Pattern 5) | 3 instances |
| 8 | Self-application gap (Pattern 4) | 5th consecutive data point + first outside File_Template (FAK) |
| 9 | Mischaracterized citations | 3 instances in one window |
| 10 | Bare citations | 19 evidence points |
| 11 | Truncated/corrupted writes | GMP ends mid-word; Charter sidecar ends at GOV-021's table; CIR literal `\u` escapes |
| 12 | Incident routing | the 2026-11-10 clobber never entered the canonical IIL |

The design reading (this proposal's claim): **every systemic class is an omission class, and every omission class exists because an instrument detects without routing, or verifies state without verifying process.** The detection layer is strong — the sweep found almost nothing by commission. What is missing is structural:

- **G1 — Verification measures state, not process.** The battery reads files at a single state. It never queries git (so silent body changes pass as clean: class 5), never confirms that a named record exists (so a record that never existed is attested twice: class 3), and never checks write completeness (so truncated files pass: class 11).
- **G2 — Detection has no routing.** The Aging Rule fires per-file WARNINGs but creates no queue, owner, or cadence (class 1); mirrors carry "file wins" disclaimers that trigger no recompute (class 6); drift indicators condition on events with no resolution-linked review (class 7).
- **G3 — Procedures don't bind their own maintenance.** File_Template sits outside its own exemptions (class 8); relocation repairs fix named pointers but no procedure has a corpus-sweep closing step (class 2); incident records live in one repo's maintenance logs with no route to the canonical IIL (class 12).
- **G4 — Sessions have no concurrency discipline.** Two sessions composed the same base and clobbered each other; no seat prompt or Kit rule requires a head check before push.

## 2. Design gaps and proposed remedies (severable items D-1..D-10)

Each item: evidence → design flaw → remedy (draft text where doctrine-adjacent) → ruling line. D-3..D-7 overlap remedies already queued in the Decision Brief; where they do, this proposal defers the instance-level remedy to that Brief and proposes only the design-level text, so nothing is ruled twice.

### D-1. Git verification is missing from the log-vs-body check
- **Evidence:** four files with body changes absent from their own Resolution Logs, found only by querying git; the pattern document's own conclusion: "no prior pass's log-vs-body grade queried git history, so every clean grade of that check is provisional."
- **Design flaw:** the Kit's log-vs-body check is a single-state comparison. An instrument that can return "clean" while the body was silently changed is false-negative-shaped.
- **Remedy (Kit text amendment, draft):** "Log-vs-body verification includes a git-history query for the audited file: every body change visible in commit history must have a corresponding Resolution Log entry (or a dated corpus-side record). A clean grade without a git query is recorded as 'provisional — no git query'."
- **Ruling lines:** A. ADOPT the Kit amendment. / B. DISCLOSE-ONLY (no Kit change; the provisional-grading convention adopted as disclosure practice). / C. HOLD.
- **Drafter's lean:** A, landing as one Kit touch with D-2.

### D-2. No named-record existence probe
- **Evidence:** the GOV-022 cluster — the Charter's File State and PKC-006 both attest a sidecar record that has never existed (git-verified at both candidate states, `af611dcb`/`cad08771`).
- **Design flaw:** the battery verifies claims against bodies but has no probe class for "does the record this claim names exist?" A claim that names a record is checked by reading the claim.
- **Remedy (Kit battery addition, draft):** "Named-record probe: every finding-relevant claim of the form 'recorded in X' requires fetching X and confirming the named entry exists. Absence is a finding even when the claim's substance is otherwise true."
- **Ruling lines:** A. ADOPT. / B. HOLD.
- **Drafter's lean:** A, same Kit touch as D-1. TWGW note: this is the structural fix for the class AUDIT_04 flagged as a TWGW candidate (a recorded verification contradicted by the artifact it names); the candidate itself routes through you under the TWGW bar.

### D-3. The Aging Rule detects but does not route
- **Evidence:** 67 of 84 open entries past the bar; the rule's only remedy path is a per-file WARNING; no scheduled mechanism resets the clock; the pattern document: "a monotonic aging clock that no scheduled mechanism resets."
- **Design flaw:** a detector with no queue. Each WARNING decays again in 90 days; a batch refresh repeats the cycle.
- **Remedy (doctrine-adjacent; needs the ruling in your words — draft offered):** "An Aging trip creates one review-scheduling row in the owed-review queue (entry, file, age, blocking/risk class) instead of a per-file WARNING; the queue is drained by genuine review passes; Last Reviewed advances only on genuine review." Reach sub-ruling: registered entries only, or generic.
- **Ruling lines:** A. ADOPT the scheduling-trigger redesign (with reach sub-ruling). / B. BATCH REFRESH only (one-time, Ship_of_Theseus 2026-10-28 precedent). / C. ACCEPT AS HONEST. / D. HOLD.
- **Drafter's lean:** A with registered-only reach, plus a one-time B pass for Blocking/High-risk entries. This is Decision Brief Item 4's same decision seen from the design side; ruling either surface rules both.

### D-4. Relocation has no corpus-sweep closing step
- **Evidence:** 19 instances + tooling corroboration; every relocation repair fixed the pointers named in findings and missed the rest; File_Template's own Update Procedure still routes to pre-relocation homes (the operator-following-the-procedure shape, the most consequential instance).
- **Design flaw:** the relocation convention defines field repairs, not completion. Nothing closes a relocation; nothing re-validates procedure text afterward.
- **Remedy (protocol text amendment, draft):** "A relocation is complete only when (a) a corpus grep for the old-home strings returns zero live operative occurrences (frozen history excepted per PKC-007), and (b) procedure text that routes to the moved home is re-validated." Plus the one-time sweep (Decision Brief Item 5) as the closing pass for the 2026-07-23 / 2026-10-29-31 relocations.
- **Ruling lines:** A. ADOPT the closing-step rule + authorize the one-time sweep (Brief Item 5's A/B choice rides here). / B. ONE-TIME SWEEP ONLY. / C. HOLD.
- **Drafter's lean:** A with tooling included (Brief Item 5 line B).

### D-5. Procedures don't bind their own maintenance (the self-application gap)
- **Evidence:** File_Template absent from its own exemptions list — fifth consecutive data point; FAK-005's closure skipped the Kit's own Discharge Procedure.
- **Design flaw:** instruments' procedures are written for other files; nothing states whether a procedure applies to its own file's maintenance acts.
- **Remedy (File_Template touch, draft):** the template states which file classes owe which canonical File State fields (settling the class-10/11 boundary), and each procedure-bearing file carries an "applies to self" line. This is Decision Brief Item 6 line B, plus the self-application line.
- **Ruling lines:** A. ADOPT (template touch + self-application lines). / B. TEMPLATE TOUCH ONLY (Brief Item 6 as drafted). / C. HOLD.
- **Drafter's lean:** A — one touch closes both.

### D-6. Derived mirrors have no lifecycle
- **Evidence:** Pattern 6 — six of 32 Adm_Scope_Map mirrors stale at a single head; Discovery's snapshot; Unknowns index pins; mirrors' Last Reviewed advanced four times in one day while rows rotted.
- **Design flaw:** derived data with a passive disclaimer but no recompute trigger or staleness marker.
- **Remedy (convention, draft):** "Scope maps, maturity snapshots and global-index pins are derived data: each carries a recomputed-at date, and a campaign close (or a named trigger) recomputes them from live File States — values recomputed, never copied." Plus the one-time recompute pass (Brief Item 8, sequenced last).
- **Ruling lines:** A. ADOPT the convention + the pass. / B. PASS ONLY. / C. HOLD.
- **Drafter's lean:** A.

### D-7. Conditional text outlives its event
- **Evidence:** Pattern 5 — three instances (EC drift indicator conditioning on a resolved unknown, CT's "history ends at v0.6" note, TRJ's registry row tracking a twice-resolved event).
- **Design flaw:** wrapper text conditions on an event with no resolution-linked review; nothing tells a later editor the condition has fired.
- **Remedy (convention, draft):** "Drift indicators and conditional statements cite the governing unknown's current status as of their Last Reviewed date; a resolved condition is removed or reworded at the next touch of the file." Batch-eligible with the mirrors pass.
- **Ruling lines:** A. ADOPT. / B. HOLD.
- **Drafter's lean:** A, batched with D-6's pass.

### D-8. Incidents have no route from session records to the canonical IIL
- **Evidence:** the 2026-11-10 clobber was recorded only in VS maintenance records, never in `Admin/Integrity_Incident_Log.md` (the canonical record under RIP Major response step 2); IIL-20261025-01's closure condition unmet.
- **Design flaw:** RIP names the IIL as the canonical incident record, but nothing requires VS-side incident discoveries to be entered there.
- **Remedy (one-line rule, draft):** "Any incident recorded in VibesSandbox maintenance records is entered in the Integrity_Incident_Log at the next landing, with the VS record cited." Plus the clobber's own entry (Brief Item 2; the RIP classification is yours).
- **Ruling lines:** A. ADOPT the routing rule + enter the clobber (Brief Item 2's A/B choice rides here). / B. ENTER THE CLOBBER ONLY. / C. HOLD.
- **Drafter's lean:** A, with the push-guard discipline of Brief Item 2 line B.

### D-9. Concurrency discipline (endorsement, not a new draft)
- **Evidence:** the 2026-11-10 clobber (two sessions, same base `94f57c8c`).
- **Design flaw:** no seat prompt or Kit rule requires a head check before push.
- **Remedy:** as already drafted in Decision Brief Item 2 line B (one remedy pass at a time; head-SHA check against the compose base immediately before every push, abort on mismatch). This proposal adds only the Architect's endorsement and the note that the guard is session discipline, not repo mechanism.
- **Ruling lines:** ride Brief Item 2. **Drafter's lean:** B (as drafted there).

### D-10. Write-integrity gates are missing from the landing helper (harness-side)
- **Evidence:** GMP ends mid-word (193,078 bytes); the Charter sidecar ends immediately after GOV-021's field table (byte-identical 1.36→1.37 — plausibly an old truncated write; git history decides); CIR's literal `\u` escapes (the escape-scan watch item is clean 7 consecutive scans but is a battery item, not a gate).
- **Design flaw:** the landing helper's acceptance test (7/7 at adoption, MAINT-81) replays known abort classes but has no tail-integrity or encoding gate; truncated and escape-corrupted writes can land.
- **Remedy (harness-side only, PKC-045 territory; no repo or prompt change):** extend the acceptance test with (a) a tail sentinel — each pushed file's terminal bytes must match the compose state (or its recorded byte length), and (b) the escape-sequence scan promoted from battery item to push gate.
- **Ruling lines:** A. ADOPT both gates. / B. TAIL SENTINEL ONLY. / C. HOLD.
- **Drafter's lean:** A. Recorded as a harness work-record item, not TWGW (PKC-045), unless the bar is met.

## 3. Options (whole proposal)

- **A. RATIFY BY ITEM** — speak any D-item's ruling line; unruled items stay open proposals.
- **B. RATIFY THE CHEAP SUBSET** — D-2, D-8, D-9, D-10 (the probes, rules and gates that cost one line or one harness check each) now; the doctrine-adjacent items (D-1 Kit text, D-3 aging, D-4 relocation, D-5 template, D-6/7 conventions) after the Decision Brief's mechanical passes land.
- **C. DO NOTHING** — this deposit records the design reading; no rule changes.

## 4. Recommendation (bias stated)

**B, then the Kit touch (D-1+D-2) as one amendment, then D-3 in your words.** The cheap subset closes the probe class that let false records stand (D-2) and the process gaps that let defects through silently (D-9, D-10); the Kit touch makes verification process-aware; the Aging redesign is the only item that touches doctrine text and deserves its own ruling. D-4..D-7's instance-level remedies are already queued in the Decision Brief — rule those there and adopt the design text alongside, so nothing is ruled twice. **Bias:** this seat executed the campaign as Auditor and landed its bookkeeping as Custodian earlier today; I have a stake in the sweep's findings being read as design-relevant, and same-architecture adjacency means my "design flaw" judgments are non-independent. The pre-ratification skeptic for this proposal must be a different architecture (Q-2; the standing preference is architectural diversity).

## 5. Opposing considerations (the strongest case against, as its defenders would write it)

- **The ceremony objection:** the meta-work ratio already has a data point (roughly 538 KB of findings against three drafted fixes before your zip). Ten new rules, conventions and gates add text that will itself need review, and every new rule creates sidecar entries that will age under the very rule D-3 redesigns. The cheaper truth is fewer, shorter obligations executed reliably, not more obligations.
- **The duplication objection:** D-3..D-7 are dispositions of findings already queued in the Decision Brief with ruling lines already drafted. A second ruling surface invites divergent rulings on the same defect and more bookkeeping per ruling.
- **The stability objection:** the Kit is v1.32 and stable; amending it before the mechanical passes land risks churning the instrument those passes depend on.
- **The one-off objection:** two truncated writes and one escape corruption are three defects, not a class; gates built for one-offs are overfit. Git history may show the sidecar truncation is a deliberate old state, not a defect at all.
- **The honesty objection:** converting Aging WARNINGs into queue rows risks burying a live alarm in a queue nobody drains — the WARNING at least fires in every audit; a scheduling trigger fires nowhere if the queue is never read.
- **The mirror objection:** retiring scope-map mirrors (live recompute on read) may be simpler than a mirror lifecycle convention; rules that keep mirrors warm pay rent on derived data the "file wins" doctrine already says not to trust.

## 6. Hard Floor and Tier 1 check

Nothing in this proposal touches the Hard Floor (the Ethical Anchor string, the Anti-Weaponization Doctrine, the closed P-1 humanitarian override) or proposes changing it. No Tier 1 axiom, Governance_Charter or Governance_Migration_Protocol amendment is initiated; D-4 and D-5 would, if ratified, amend Admin doctrine files only, on your written ruling.

## 7. Reversibility

Every item is a text amendment or a harness-side gate: git-revertible, nothing irreversible, frozen history untouched (PKC-007 shapes stay "ruled historical"). The one-time passes (D-4's sweep, D-6's recompute) are batch-eligible and re-runnable; harness gates revert harness-side with no repo trace. Nothing enacted by this deposit is irreversible, because nothing is enacted by this deposit.

## 8. Enactment plan (on ratification; nothing pre-executed)

- **Landing:** by the Custodian seat as a logged MAINT entry; verification by the Auditor seat (vacant — a different agent, or your explicit written ratification of the overlap per MAINT-26 / AP-032).
- **D-1+D-2:** one Kit touch (`Admin/Forge_Audit_Kit.md`), version bump logged (the F-HDL-1 lesson), Resolution Log entry, no other file touched.
- **D-3:** doctrine text in your ruled words on the Aging Rule's home; cascade: every open Aging finding's remedy line re-pointed at the queue convention; the reach sub-ruling recorded.
- **D-4:** the closing-step rule in the relocation-governing protocol + the one-time sweep per Brief Item 5's batch conditions (frozen history untouched; header bumps logged; sampled second-seat check).
- **D-5:** the File_Template touch per Brief Item 6 + the self-application lines.
- **D-6/D-7:** the convention lines + the recompute/reword pass sequenced last (Brief Item 8).
- **D-8:** the routing line + the clobber's IIL entry (classification yours per Brief Item 2).
- **D-9:** session discipline, no mechanism; rides Brief Item 2.
- **D-10:** harness-side acceptance-test extension; recorded in the work record (PKC-045).
- **Sequencing:** defer to the Decision Brief's order (rulings first, mechanical passes, mirrors last); this proposal's texts ride those passes rather than opening new ones.

## 9. Human-workflow cost

This deposit is one VibesSandbox file (~16 KB) plus one maintenance entry — no LazarusForge change, no zip. Ruling cost is one line per item, or one line for the whole cheap subset. On ratification, the work ships as small update sets (one Kit touch, one template touch, convention lines riding already-queued passes), not a full-repo transfer. Mobile-first: every item is ruling-line-shaped, speakable from a phone.

## 10. Explicit non-claims

- This proposal does not enact anything, convert any audit, or advance any Last Audit / Last Reviewed / version / Status / Spec Gate / Unknown.
- It does not re-verify the sweep's unverified findings; the design reading stands on the pattern document's recorded instances and discloses where the evidence is a single seat's (see §4's bias statement).
- It does not duplicate the Decision Brief's ruling lines; where items overlap, it says so and defers.
- It does not propose any Hard Floor change or Tier 1 initiation.
- No TWGW entry is added by this deposit; the AUDIT_04 candidate and any new candidates route through you under the TWGW bar.
- Open-proposal cap: this is open proposal 1 of 10 from this seat.

---

*Drafted 2026-11-11 — Vibe, Architect seat (Synthesizer per Auditor_Protocols.md v0.47; mapping proposed, not ratified). Bootstrap live at LF `35973fae` / VS `49398bef`. Non-independence: the same line executed Campaign 4 (Auditor), landed its bookkeeping (Custodian, MAINT-125/126/127) and drafts this review (Architect); Genesis Phase, your in-the-loop ratification is the independent layer; the pre-ratification skeptic should be a different architecture.*
