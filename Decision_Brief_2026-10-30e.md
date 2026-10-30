# Decision_Brief_2026-10-30e.md — Audit-Artifact Aggregation System (duplicate-coverage consolidation)

**Status:** PROPOSED — ruling requested
**Issued:** 2026-10-30 · **Preparer:** Vibe (Repo Custodian, general appointment 2026-10-30)
**Human direction prompting this brief (verbatim):** "There are multiples of some of the audits. We need a system to aggregate the duplicates. That should preserve the logic while limiting the repo file size. It can be added to the list, too, if need be."

---

## 1. Inventory (verified live at LazarusForge head 3e83324b, 2026-10-30)

Five audited files carry **two independent audit reports each** — every pair is two genuine passes (different dates, heads, or audit lanes), not a copy-paste artifact. All sit in `Admin/AAudits/`. Three dated addenda exist alongside their targets.

| Audited file | Report A | Report B | Combined chars |
|---|---|---|---|
| Admin/Governance_Charter.md | AUDIT_01 (C1 stream, 10-27, 6,992) | CAMPAIGN2_AUDIT_03 (C2, 10-30, 6,598) | 13,590 |
| Admin/File_Template.md | AUDIT_10 (C1, 10-27, 12,558) | CAMPAIGN2_AUDIT_01 (C2, 10-30, 4,801) | 17,359 |
| Admin/Metrics_Scaffold.md | AUDIT_17 (C1 custodian pseudo-audit, 10-28, 6,125) | CAMPAIGN_AUDIT_17 (C1 VibesSandbox stream, 10-28, 7,885) | 14,010 |
| Admin/Ship_of_Theseus.md | AUDIT_18 (custodian, 10-28, 7,624) | CAMPAIGN_AUDIT_18 (stream, 10-28, 9,120) | 16,744 |
| Admin/Economics.md | AUDIT_19 (custodian, 10-28, 7,962) | CAMPAIGN_AUDIT_19 (stream, 10-28, 11,225) | 19,187 |

Dated addenda (small; fold into their targets' ledgers): AUDIT_13_CORRECTION_2026-10-28 (1,738); CAMPAIGN_AUDIT_20-22_CORRECTION_2026-10-28 (6,361); AUDIT_01-05_TEMPLATE_RESOLUTION_2026-10-27 (5,309).

**Cause of the multiples:** (a) the 2026-10-28 Campaign-1 collision — two audit lanes (custodian pseudo-audit sequence and the VibesSandbox Skeptic/Auditor stream) ran the same sequence numbers 17–19 (the stream itself flagged this as "the audit-stream numbering collision (F2)" in CAMPAIGN_AUDIT_17); and (b) Campaign 2's authorized re-coverage of Governance_Charter and File_Template at PKC-020 depth. Campaign 2's other 66 reports have single coverage; the cross-file pattern docs (Sessions 1–9) are single per scope.

## 2. The proposed system — AUDIT_AGGREGATE convention

**Per audited file with ≥2 reports**, the custodian creates one `AUDIT_AGGREGATE_<Folder>-<File>.md` in the same Audits home. Required content (the "logic-preservation floor"):

1. **Provenance table** — for every pass: report path, date, auditor + lane, head-at-fetch, fetched size, blob SHA.
2. **Findings ledger** — every finding from every pass, verbatim ID + severity + one-line summary, with a **disposition** column: Enacted (by which fix pass) / Superseded (by which later finding, with the supersession reason) / Standing-open / Closed-by-human-ruling. Nothing is dropped: a finding absent from the later pass is carried as "not re-tested" with its original grade.
3. **Cross-pass logic map** — what changed between passes and why (head drift, rulings landing mid-window, MAINT-32 recompute effects); explicitly marks which pass's checklist result is authoritative for each check now.
4. **Pointer block** — where the superseded originals live after relocation, with their blob SHAs for integrity verification.

**Disposition of the originals (the size lever):** the superseded reports are **relocated, never edited and never deleted** — byte-identical moves under the R8/MAINT-29 relocation precedent, full text retained in git history, with disclosure in the aggregate's provenance table and a dated line in SESSION_STATUS. Issued-report immutability (the campaign's honesty rule) is preserved: content bits unchanged, only path.

**Future-proofing — T3 aggregation trigger:** whenever a target accumulates ≥2 reports (or an Audits home exceeds 25 artifacts), the custodian runs an aggregation sweep as ordinary delegated maintenance; new passes after an aggregate exists are appended to the aggregate's ledger at deposit time, so the system is self-maintaining. The Session pattern docs remain the cross-file layer, untouched.

**Explicit non-claims:** the aggregate is bookkeeping, not an audit of record — it re-checks nothing and advances no Status/Last Audit/Spec Gate; AP--032 separate-audit-event rule unchanged; an aggregate may be corrected only by dated addendum.

## 3. Options

**A. Aggregate + in-repo Superseded subfolder (custodian lean).** Originals move to `<Home>/Superseded/` (e.g. `Admin/AAudits/Superseded/`). Repo keeps everything; active-home size drops ~80KB; future fetch cost drops because the Audits home is what tooling pulls. All five targets aggregate now; addenda move alongside their targets.

**B. Aggregate + off-repo originals.** Originals relocate to a VibesSandbox audit-archive folder; LazarusForge keeps the aggregates (with blob SHA + sandbox pointer). Maximum repo-size reduction (~93KB incl. addenda); trade-off: LazarusForge no longer self-contained for its own audit provenance — weaker against the repo's "nothing discarded without accounting" ethos even with git history.

**C. Index-only.** A per-home `AUDIT_INDEX.md` listing passes per target; no relocation. Cheapest, but no size reduction — does not meet the stated goal.

**Recommendation:** **Option A**, with the aggregate ledger format from §2 as the codified template (a dated addendum to `Archive/Repo_Costodian_Prompt.md` on enactment). Estimated result for the current corpus: 10 superseded reports + 3 addenda leave the active Admin/AAudits listing; 5 aggregates (~8–12KB each) replace them; net active-home reduction ≈ 55–65KB and a proportionally smaller per-audit fetch surface.

## 4. Rulings requested

1. Adopt A / B / C (or a variant).
2. Confirm the aggregate ledger format (§2.1–2.4) as the codified template.
3. Confirm the T3 trigger (≥2 reports per target, or >25 artifacts per home) as ordinary delegated maintenance going forward.
4. Confirm relocation-not-editation of issued reports is compliant with the campaign's immutability rule as argued (content unchanged, path only, disclosed).
5. Whether Brief 2026-10-30d's successor-auditor for the Campaign 1 rerun should inherit the aggregate-reading convention (recommended: yes — the rerun reads aggregates, not five parallel report stacks).

*Nothing in LazarusForge was changed by this brief. Ruling requested; added to the open-rulings list.*
