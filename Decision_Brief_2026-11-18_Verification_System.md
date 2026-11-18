# Decision Brief 2026-11-18 — Verification System (replacing ratification-trust, at his directive)

- **Purpose:** design + pre-drafted ruling lines. Deposited under the Co-Author mandate (standing primary since his 2026-11-18 word "Please elevate to the role of Co-Author.", definition of record `Co_Author_Mandate.md`, LazarusForge `Archive/`). Nothing enacted; every line below awaits his ruling.
- **His directive, verbatim (2026-11-18):** "The other agents hyperfocus on ratification, thinking it is my duty alone. We still need the verification system in place to replace the ratification. I will not always be around (just not going anywhere anytime soon)."
- **Scoping note:** this brief deliberately does NOT move ratification off him anywhere it is currently required. What it does is route the non-doctrine burden (routine verification, re-checks, counts, staleness, package checks) into machinery that does not need his eyes, so his ratification is spent only where doctrine and risk actually demand a human. "Verification gates as replacement for reliance on him" was already the fleet's 2026-11-02 direction; this is its operating plan.

## 1. What exists today (all verified live this session or in the cited passes)

- **Deterministic machine layer:** AuditBot V0.0.3 (standing package as of MAINT-151; `Maintenance/AuditBot-V_0_0_3.zip`): phase 1 mechanical (M-01..M-06, stdlib, deterministic, hashed outputs), phase 2 logical, phase 3 adversarial; 29/29 self-tests; the Colab cell makes phase 1 runnable from a phone.
- **Count and coverage layer:** the audit coverage ledger (Table I/II) with the regen script, frozen fixtures, and the reconcile check (MAINT-84/85).
- **Repo integrity layer:** `Automation/integrity_check.py` v0.4 with the Size Census roster (T1 bar 100,000 bytes SI) and fixture test (MAINT-136).
- **Cadence layer:** the Custodian Review-and-Corrections Cycle, scheduled Tue/Fri 22:00 CT (task `e6a7ddcd`), whole fleet, fixes + briefs.
- **Discipline layers:** the landing guard (fetch, compose, re-fetch-and-assert-identical), the event-tag convention (`Event: (i)/(ii)/(iii)`), TWGW, append-only records, the X10 recount rule.

## 2. The gap (why he is still the single point)

1. **Same-lineage circularity.** Nearly every layer above was built by this line. Self-verification is T0-equivalent by definition (disclosed every pass), so the one independent thing that currently exists is his ratification. Removing him without adding an independent layer would LOWER assurance, not raise it.
2. **The Rule 5 verifier is unnamed.** Re-grade adjudication, the verification packet, and the tranche-2 remainder all queue behind a name. Naming a Vibe-built tool (AuditBot) would re-create the circularity one layer up: the tool's author would then adjudicate disputes about the tool's outputs.
3. **Runtime gap.** The harness executes no Python. Package checks and battery runs need a runner outside this harness (Actions, Colab, or another lineage's machine). Until one is standing, phase-1 runs stay claims-by-record, not re-runs.
4. **No standing independent-lineage channel.** Different-lineage checks (Claude, Grok) arrive only when he hand-routes them (Class A). That is the ratification bottleneck under another name: it needs him for every routing.

## 3. The independence ladder (pre-drafted vocabulary; definitions only, nothing enacted)

- **T3 — machine, human-independent:** deterministic scripts + frozen fixtures; output reproducible by anyone with the pinned inputs. Highest standing after fixtures are independently reviewed.
- **T2 — different product line, structured hand-off:** Claude/Grok (or any other lineage) executing a verification WORKSHEET: inputs are pinned SHAs and fixed checklists; outputs are findings files; no trust in the executing agent's judgment is required beyond executing the steps. Routing needs him ONCE per channel, not per check, if a standing channel is established.
- **T1 — fresh thread, same line:** a new session of this line with no carried context, verifying against records only. Cheap; catches drift, not lineage bias.
- **T0 — same session / same lineage:** what most passes disclose today.

**Target posture:** routine verification at T3/T2; his ratification reserved for doctrine changes, ratings disputes, scope grants, and any new liberty. The AuditBot three-phase design already encodes this (phase 1 machine, phase 3 "independent fresh instance").

## 4. The AuditBot set as ruled this pass (MAINT-151) and what remains

- **Ruled/executed 2026-11-18:** V0.0.3 is the standing package; V0.0.2 retired (deleted); V0.0.1 already deleted by his hand. F-3's fail-closed default (empty findings exit 2 without `--allow-empty`) stands since MAINT-147, veto window unchanged. Fixture layout pin: closed in V0.0.2 per the MAINT-146 re-derivation.
- **Remaining, staged in ruling lines below:** the independent-lineage check of V0.0.3; the CHARTER/MIGRATION-vs-LF line-by-line comparison (the F-4 class: ~478 KB of doctrine untriaged); OPEN_QUESTIONS 1–9 (the 2026-11-16 review endorses the conservative defaults on #2, #3, #4, #7, #8; #1 gate authority, #5, #6 and #9 cross-file duplicate IDs remain open; #9 is already recommended as V0.0.4 work); the five fixture files' registration home (rides the monitoring-home question, unchanged).

## 5. Ruling lines (severable; he may rule freely outside them)

1. **V1 — commission the V0.0.3 independent check.** Preferred: T2, routed to a different lineage with the worksheet below. Alternates: GitHub Actions run of the 29-test suite (machine-tier, same-lineage-authored fixtures disclosed), or the Colab phase-1 cell run from his phone. Pre-drafted line: *"V1: commission the independent check, T2 worksheet to a different lineage; the worksheet is deposited and fixed for the run."*
2. **V2 — adopt the endorsed OQ defaults.** *"V2: OPEN_QUESTIONS defaults adopted on #2, #3, #4, #7, #8 as reviewed; #1, #5, #6 remain open with owners noted; #9 scheduled as V0.0.4 work."*
3. **V3 — F-3 default.** *"V3: F-3's fail-closed (exit 2, vacuous marker) default accepted"* — or veto to the exit-0 variant.
4. **V4 — name the Rule 5 verifier (tranche-2 remainder).** Options: (a) a different-lineage agent named after the V0.0.3 check passes (my lean: the adjudication layer should not share lineage with the pass layer); (b) AuditBot for mechanical counts only, with re-grade adjudication held for a different lineage; (c) leave unnamed until V0.0.4 + F-4 triage. Pre-drafted: *"V4: verifier = [name], tier [T2/T3], adjudication scope per Rule 5 as ratified; effective on the V0.0.3 independent check passing."*
5. **V5 — CRC adoption.** *"V5: AuditBot phase 1 (fixtures + self-audit) joins the Friday CRC run once the independent check passes; findings-only, escalations stay briefs."*
6. **V6 — the standing direction, recorded.** *"V6: recorded as standing: routine verification rides the machine and worksheet layers; his ratification is reserved for doctrine, disputes, scope, and new liberties; succession design returns at the C3 review (~2026-11-30) with usage evidence."*

## 6. Hard Floor and reversibility

- Nothing here touches Tier 1/FROZEN/Hard Floor, the Ethical Anchor string, or any governing protocol text. Ratification authority is nowhere weakened: no ruling line removes any required human word; V6 records a division of labor, not a delegation of it.
- All lines are reversible; the machinery is already in the record; a "do nothing" outcome costs only the continued T0 disclosures.

---

*Deposited 2026-11-18 by Vibe (GLM 5.3, Mistral AI) — Co-Author seat, standing primary (his 2026-11-18 word; definition of record: `Co_Author_Mandate.md`, LF `Archive/`), Architect secondary, Repo Custodian under the mandate's relaxed separation. Operating per Auditor_Protocols.md v0.47. Bias disclosed: the machinery proposed is largely machinery this line built; that is exactly why the independent check (V1) leads the queue. Non-independence: T0-equivalent.*
