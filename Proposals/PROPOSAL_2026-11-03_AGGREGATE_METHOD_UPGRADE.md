# ARCHITECT PROPOSAL — Aggregate Method Upgrade (v1, OPEN)

**Seat:** Architect — Vibe (GLM 5.3, Mistral AI), appointed in writing by the human 2026-11-03. Role declaration: Operating as Synthesizer per Auditor_Protocols.md v0.46 (mapping proposed, not ratified).
**Status:** OPEN — awaiting independent skeptic review (Architect Prompt §4) and the human's ruling. Under the Genesis Phase relaxation the human may waive the skeptic step; either way nothing here is live until ratified. The four amendments are severable — the human may ratify any subset.
**Disclosures:** The same product line holds the Architect and Repo Custodian seats, ran this day's Auditor passes in Genesis Phase mode (GOV-008 open), wrote the five existing aggregates' dispositions, and executed the CAMPAIGN2 fixes whose evidence those dispositions cite — seat overlap disclosed; Q-2 invoked. Facts below were verified live at named heads on 2026-11-03, this session.

## 1. Problem

The aggregation method (`Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md`, blob `dd6497b9`, 6,700 chars, ratified 2026-10-31 per Brief 2026-10-30e Option A and naming Addendum #2) has four operative gaps, each surfaced by the first sweep (MAINT-34) and the deposits since:

**(a) The Rule 7 trigger is undefined for NOTE-grade findings.** Rule 7: create an aggregate only when every finding on the target has a disposition (no live passes). Live NOTEs carry dispositions invented ad hoc: `Admin/AAudits/AUDIT_AGGREGATE_Admin-Governance_Charter.md` (blob `0fa43628`, verified this session) rows B-N2 and B-N3 read "Standing-open" — defect vocabulary applied to non-defect records — while B-N1 and C-N1 read "Positive-record". Nothing in the ratified rules says whether a "Standing-open" NOTE blocks the trigger or ever clears.

**(b) PATTERN artifacts have no aggregation lane.** Addendum #2 registered TYPE=PATTERN, and CROSS_FILE_PATTERN_FINDINGS Sessions 1–11 exist (Sessions 10 and 11 verified live this session at `Archive/Audits/`; earlier sessions per the registry record). Per-target aggregates cannot carry cross-file pattern findings: no rule says where PATTERN dispositions live or how a target's aggregate references a pattern that spans it.

**(c) No coverage ledger.** Rule 7 requires knowing every finding on every target; no instrument tracks which targets hold which passes, which have aggregates, and which have neither. The 2026-11-03 Red-Team Sufficiency Review named a coverage ledger as an audit-sufficiency gap; the method needs the same instrument as trigger infrastructure.

**(d) Rule 5 is a rule without mechanics.** All five aggregates (`Admin/AAudits/AUDIT_AGGREGATE_Admin-{Economics,File_Template,Governance_Charter,Metrics_Scaffold,Ship_of_Theseus}.md`) sit at "Dispositions unverified (Rule 5 separate-verifier hand-off pending)" — each verified by live header read this session. The template defines who may NOT verify (the disposition writer) but not: the packet format, the check procedure, verifier eligibility while GOV-008 is open, the disagreement protocol, or the cadence when new passes fold into a verified aggregate.

## 2. Options

**Option A — do nothing.** Zero blast radius; the five aggregates remain unverifiable indefinitely (a pending hand-off with no defined procedure cannot complete), the trigger stays ambiguous on the grade the corpus produces most (NOTEs), PATTERN findings stay outside the map. Cost: the method's own outputs cannot complete their lifecycle.

**Option B — cheap: interpretation addendum only.** One dated addendum resolving (a) and (d) minimally: NOTEs never block the trigger; a three-sentence Rule 5 packet. Defers (b) and (c). Cost: one file touch; leaves PATTERN invisible and the trigger still un-computable at corpus scale.

**Option C — full upgrade: four severable amendments (Rules 8–11) plus one instrument.** Cost: 3–5 file touches on landing, one new bookkeeping file, a Custodian registration pass. All dated-addendum mechanics; nothing frozen touched; aggregates themselves are NOT edited at landing time (their changes go to their own §5 Addenda at next substantive touch).

## 3. Recommendation

Option C, with Rule 10 (coverage ledger) landing first — it is the infrastructure the other three cite. Bias stated: the seat that drafted this design is structurally invested in the full option rather than the cheap one; the skeptic pass exists to check exactly this.

- **Rule 8 — NOTE semantics (constrains Rule 7's application).** NOTE-grade findings are records, not defects. Valid NOTE dispositions are exactly: `Positive-record` | `Watch-carried` (replaces "Standing-open" for NOTEs; existing NOTE "Standing-open" rows are re-labelled `Watch-carried` at the aggregate's next substantive touch via dated addendum, never in place) | `Corrected-by-later-fact` | `Superseded by <Ref>`. NOTEs are always dispositioned at fold-in — they need no repair to be dispositioned — and therefore never block the Rule 7 trigger; the trigger gates on MAJOR/WARNING/F-grade findings only. Rule 3 (nothing dropped) is unchanged: NOTEs stay in the ledger.
- **Rule 9 — PATTERN crosswalk.** CROSS_FILE PATTERN artifacts do not fold into per-target aggregates (they are not target-scoped). Instead: (i) each per-target aggregate's §3 carries a one-line pointer for any PATTERN finding whose subject-set includes the target — pattern file, pattern ID, date; (ii) PATTERN dispositions live in the pattern files' own dated-addenda sections under the same evidence rule (Rule 4) and the same separate-verifier rule (Rule 5); (iii) a PATTERN finding blocks no per-target trigger — its disposition lifecycle runs in its home file.
- **Rule 10 — coverage ledger.** New bookkeeping instrument `Archive/Audits/AUDIT_COVERAGE_LEDGER.md`: one row per doctrine target — target | era-tags of passes held | aggregate ref (or "—") | open MAJOR/WARNING/F count at last count | Rule 7 trigger state (computable / blocked by <refs>) | last-counted date and counter. The Custodian updates it at every audit landing and fold-in; it advances no field anywhere (bookkeeping-map class, PKC-020). One instrument serves both the aggregation trigger and the Red-Team review's coverage recommendation.
- **Rule 11 — Rule 5 hand-off mechanics.** (i) Packet: the verifier receives the aggregate, the per-row evidence list (commit shas / ruling references), and a one-page check procedure. (ii) Checks: evidence resolves at live head; disposition label matches evidence type (Rule 4); each ledger row faithfully summarizes the original report text; counts re-derived. (iii) Eligibility: an agent other than the disposition writer; while GOV-008 is open, a different architecture wherever one exists (standing diversity preference) — same-product-line verification only under the Genesis Phase clause with the human's explicit waiver, disclosed per-row. (iv) Disagreement: the verifier never edits; a dated addendum row marks the disposition `Disputed` with evidence, and the row counts as `Asserted` until re-dispositioned. (v) Incremental verification: verified state is per-pass-window — a new fold-in does not reset prior verified rows; the header reads "verified through pass <X> (<agent>, <date>); pass <Y> rows unverified."

## 4. Opposing considerations

As its defenders would write it: the method is four days old and has completed exactly one sweep; not one Rule 5 verification has been executed yet. Amending an instrument before exercising it once is spec churn on untested doctrine — the Rule 5 packet in particular is better defined by the first verifier's lived experience than designed a priori. The NOTE re-labelling creates rework across five aggregates for zero finding-content change. The coverage ledger is a new drift surface that must be updated at every landing or it becomes the next stale-index finding — this corpus's most recurring defect class. PATTERN aggregation may be premature: eleven session files, one era, one auditor line. The disciplined move is to run the method as ratified, log the frictions as they bite, and amend once with evidence of failure rather than foresight.

## 5. Hard Floor and Tier 1 check

Touched: `Archive/Audits/AUDIT_AGGREGATE_TEMPLATE.md` (dated addendum only, per its own Rule 6 convention); a new `Archive/Audits/AUDIT_COVERAGE_LEDGER.md`; aggregate §3 pointers and NOTE re-labels at the aggregates' own next substantive touch (their §5 Addenda); Routing.md / Discovery.md registration (Custodian lane). No Tier 1 file; no FROZEN text; the Hard Floor (Ethical Anchor, Anti-Weaponization Doctrine, permanent P-1 closure) is untouched and this design does not depend on any of it.

## 6. Reversibility

Every change is a dated addendum or a new file. Undo: a dated supersession addendum to the template plus archive/delete of the ledger (with a Rename Registry entry if citations exist). Lost if reversed: the NOTE re-labels' audit trail (recoverable from git) and any Rule 11 verifier work already performed.

## 7. Enactment plan (Custodian lane, only after ratification)

- MAINT-NN: template dated addendum carrying the ratified subset of Rules 8–11; coverage ledger created with initial rows backfilled from the registry (target list and era tags from Routing.md's audit-artifact homes section); Routing.md and Discovery.md registration rows + header entry; SESSION_STATUS dated line; dual-home addendum.
- Cascade: the five aggregates are NOT edited in the same commit — their NOTE re-labels, §3 pattern pointers and header re-wording land at their next substantive touch via their own §5 Addenda (Rule 6 immutability respected).
- Verification checklist: ledger row count equals the registry's target count; trigger-state recomputation worked end-to-end on Admin/Governance_Charter.md as the example; blob SHAs of any relocated originals unchanged (none anticipated).
- Disclosure list: seat overlap (Architect = Repo Custodian = this day's Auditor line; Genesis Phase; Q-2 invoked); the five aggregates' dispositions were written by this same product line — the Rule 11 verifier must be named by the human.

## 8. Human-workflow cost

Small update set: one ruling (severable — "C all", "C but 10 first", "B", or item-by-item), two files to open (this proposal; the template addendum on landing), no full-repo transfer. The ledger adds one ~3–6 KB file at creation. Mobile-first compatible.

## 9. Explicit non-claims

This proposal does not: verify the five aggregates' dispositions (Rule 5 execution stays owed — Rule 11 defines the process and runs nothing); aggregate any PATTERN findings (Rule 9 says where they live; it creates none); re-grade any NOTE (the re-label is vocabulary only); advance any Status, Last Audit, Spec Gate or Unknown anywhere; amend AP-032 or the separate-audit-event rule; alter the naming convention (Addendum #2 stands); fill any Verified-by row; or constitute an audit of anything. Until ratified it is paper.

---
*Drafted 2026-11-03 by Vibe (GLM 5.3, Mistral AI) — Architect seat, human-appointed. OPEN: skeptic pass pending per Architect Prompt §4; not in force.*
