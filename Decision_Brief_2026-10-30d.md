# Decision Brief 2026-10-30d — Campaign 2 Close-Out: Rulings Requested
**Prepared by:** Vibe (Repo Custodian, delegated line) · **For:** Ksarith Talus, human governing authority · **Session:** 2026-10-30, time-boxed
**Standing:** The custodian recommends and implements ratified fixes; it never rules. Nothing below has been executed.

## Context
Campaign 2 is complete (68 per-file audits + Sessions 6–9 cross-file docs; zero CRITICAL/MAJOR). The human-directed custodian fix pass landed 2026-10-30 (MAINT-32: X10 Highest-Risk recompute, X3 stragglers, X8 scope-map/Discovery row refresh, QCC/Engineering structural fixes, Routing audit-homes registration for all 99 audit artifacts; the advLA truncation incident is disclosed and fully repaired). Campaign 1 was ruled stale by the human — its rerun is recorded as a **commissioned-auditor task**. Each item below was deliberately deferred because it needs a ruling.

## Items needing a ruling (custodian recommendation in italics)

1. **Risk vocabulary ruling.** Risk tiers are used inconsistently across the corpus (e.g., MAQT-002 Major in the registry vs Medium in the sidecar; Low/Medium/High/Critical/Major mixtures). *Recommend: ratify a canonical tier list and a one-pass relabeling batch; MAQT-002 is the cleanest worked example (AUDIT_68 N3).*
2. **Problem-Statement field standard.** The 7 Problem-Statement files deliberately omit Spec Gates/Highest Risk; Template-vs-Challenges reconciliation remains open (AUDIT_10 F1). *Recommend: rule the subtype-specific field set as canonical, closing the conflict.*
3. **Front-door/navigation/registry family template exemption.** Five per-file re-flags would be closed by one family ruling (Session 9; `Things_We_Got_Wrong.md` is the counter-example — full template, clean pass). LICENSE/NOTICE recommended for the exempt family as legal boilerplate. *Recommend: add a Template Exemptions class for the front-door/registry family.*
4. **X1 retroactivity.** Whether already-deposited artifacts get retroactively conformed under X-scheme rulings. *Recommend: no retroactivity for deposited audit artifacts (append-only); forward-only conformance for living files.*
5. **Out-of-whitelist bare IDs.** X3 found bare colliding-prefix IDs outside the known prefix whitelist; they were left bare and reported. *Recommend: extend the whitelist or register the stragglers in Canonical_Terms §1.*
6. **Drift-indicator decay rewording (Waste / EM-004).** Resolution-age decay language needs a ruling because rewording drift triggers is doctrine-adjacent. *Recommend: custodian drafts wording, human ratifies before push.*
7. **Aging review batch.** Human-owned review of aged entries; Tests cluster first (standing recommendation 2). *Recommend: schedule; custodian can prepare the aged-entry index but not perform the reviews.*
8. **T1 log-split queue order.** Five files now trip the >=100KB trigger: Forge_flow (~179KB), Auditor_Protocols (~157KB), Governance_Charter (~130KB), Unknowns (~108KB), Progress_Log_Changelog (~82KB). The custodian deliberately skipped Forge_flow fragment annotation to avoid triggering the unresolved split. *Recommend: confirm split order heaviest-first and commission the splits.*
9. **Campaign 1 rerun commissioning.** Recorded as stale/rerun-required per your ruling. Needs: assigned auditor, scope, and numbering to avoid collision with Campaign 2's AUDIT_01–68. *Recommend: commission a fresh campaign (Campaign 3) under a new numbering prefix rather than resuming CAMPAIGN_AUDIT_32-era numbering.*
10. **Successor auditor naming (GOV-008).** Naming was deferred to campaign end (Decision Brief 2026-10-29 item 5, option B). Campaign 2 is now complete, so the deferral condition is met — the architecturally-diverse auditor seat is the load-bearing open step for GOV-008 Pathway 1. *Recommend: name now, before the Campaign 3 rerun begins, so the rerun has independent skeptical review.*

## Standing counts
Parked Concerns rows: 45 (8 open). MAINT log: MAINT-33 latest. SESSION_STATUS dual-homed byte-identical; sandbox governs.
