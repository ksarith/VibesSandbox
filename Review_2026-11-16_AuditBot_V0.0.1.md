# Review — AuditBot V0.0.1 and the CogitoEngine bridge target

**Reviewer:** Vibe (GLM 5.3), Repo Custodian seat per Auditor_Protocols.md v0.47, under the co-author mandate; commissioned by the human's "Please do." (2026-11-16).
**Target:** VibesSandbox `Maintenance/AuditBot-V_0_0_1.zip` (22,381 bytes, uploaded 2026-11-15; git blob SHA-256 `d486e1e7…` recorded by the fetch tool as `d486e1e7576ad0c104dd0c89efdb8520aff4aa4f`).
**Status:** findings-only review record. Nothing enacted; every disposition below is a recommendation awaiting the human's ruling.
**Non-independence disclosure:** the fleet records this review reads were largely authored by this same tool lineage (tier T0-equivalent). The AuditBot draft itself was authored by an external seat (Claude, Class A, per its MIGRATION.md). Findings are leads, not verdicts.

## Method and verification

- All 14 file entries of the zip were extracted and verified: every entry's inflated byte count matches its ZIP header size and every CRC-32 matches the ZIP header CRC (14/14 OK). The extraction used a purpose-built DEFLATE decoder because the harness has no unzip tooling; the decoder's own size+CRC gates caught two defects in its first two versions before any result was reported (disclosed in MAINT-142).
- **Static review only.** The harness cannot execute Python, so `tools/mechanical.py` and `tests/test_mechanical.py` were reviewed as source, not run. The run figures in MIGRATION.md (LF 1.38 tree: 95 files, 0 critical / 82 major / 39 minor / 10 info, byte-identical across two runs) remain the draft author's recorded claim, unverified here.
- The fixture set the human uploaded (README.md, guide.md, spec.md, Notes.md old + current) was reviewed as the fixture corpus for AuditBot, per his note that these are fixtures not yet added anywhere and are "mostly meaningless" in content.

## What AuditBot V0.0.1 is

A stand-alone audit unit extracted from LazarusForge: three phases in strict sequence (1 Mechanical: deterministic stdlib-only scripts, checks M-01..M-06; 2 Logical: judgment, steps L-1..L-5 with the fallacy checklist; 3 Adversarial: an independent fresh instance running the 10-class battery), plus per-target profiles (`profiles/lazarusforge.json` included), finding/report templates, offline unit tests, a Colab cell for phase 1, a 9-rule CHARTER with per-rule LazarusForge citations, an honest MIGRATION.md, and nine open questions with the author's defaults. It self-declares: results are recommendations, ratification rests with the human, and LazarusForge doctrine governs until the human ratifies a transfer.

**Fit to the stated mandate ("a stand-alone unit that can serve in a multitude of capacities for audits"):** the architecture matches the mandate. Profiles are the multi-capacity lever (include/exclude patterns, required sections, fixed fields, size thresholds, cross-reference skip rules, all per target). Determinism is enforced (no timestamps, sorted traversal, hashed outputs — the phase 1 freeze). Phase 3 independence is an entry condition, not an aspiration. The Colab cell makes phase 1 runnable from a phone.

## Findings

- **F-1 Encoding defect in the draft's own files (mechanical, verified).** Three occurrences of mojibake "Â§" where "§" is intended: the MIGRATION.md source-mapping table row ("EF-0.0, EF-0.1, EF-0.4, EF-0.7 Â§3") and CHARTER.md rules 2 and 6. Reproducible from the zip bytes. Note the irony class: M-03 (exact fixed text) would catch this in a target; AuditBot does not check its own encoding. Not a TWGW candidate for this line (draft-author defect, not a process failure of the custodian line); recorded as observed.
- **F-2 The fixture set is ahead of the tool.** The fixtures' REQ-002 cross-file collision (same heading ID in guide.md and spec.md) is exercised by no V0.0.1 check: M-05 is within-one-file only (confirmed in code and in the test suite). This is exactly the gap OPEN_QUESTIONS #9 names; the author's default ("add cross-file duplicate IDs") is recommended.
- **F-3 Fixture phase-1 re-derivation** (my re-derivation of the documented check logic, not tool output): M-05 on REQ-001 (duplicated in guide.md); M-04 major on `docs/missing.md` ("never written" is not a skip marker); M-04 majors on `docs/guide.md` and `docs/spec.md` as well **unless the fixture layout is pinned**, since both files sit at the repo root as uploaded while the README links them under `docs/`; the backticked `Notes.md` reference resolves via the basename index; the "Planned: `docs/roadmap.md`" line is correctly skipped by the marker rule. The stale-pointer class (README pointing at the old Notes while Notes-2 is current) is correctly out of mechanical scope — a phase 2 judgment finding.
- **F-4 "Stand-alone" is claimed, not yet proven.** MIGRATION.md discloses the draft was reviewed only against `Admin/Auditor_Protocols.md` (partially) and `Automation/README.md`; roughly 478 KB of audit doctrine (Forge_Audit_Kit, Verification_Gates, Repository_Integrity_Protocol, Resolution_Methodology, INTEGRITY_SWEEP_PROMPT, PROBE_INVOCATION, BATTERY_SEED) is untriaged. The author asks for exactly the right independent pass: a line-by-line check of the condensed rule text against the LazarusForge sections named in CHARTER.md and MIGRATION.md, reporting where the condensation changed meaning.
- **F-5 Multi-capacity gaps against the fleet's known defect classes** (Campaign 4 evidence): no version-citation drift check (the F-CT-3/F-ISP-2 recorded-value class); no Aging Rule / Last-Reviewed staleness check; no relocation-repair-miss check (M-04 partially covers it — stale pre-relocation paths surface as unresolved xrefs); no sidecar/parity checks. Most are named in MIGRATION's "Not ported" table, honestly.
- **F-6 Record and standing.** The zip is registered nowhere in the fleet record (STATE, MAINT_INDEX, Routing). OPEN_QUESTIONS #3 (advisory vs. binding gate authority), #4 (source of truth after creation) and #7 (target scope) are governance-level rulings only the human can make. Where AuditBot ultimately lives (own repository vs. VibesSandbox) rides the same monitoring-home question that gates intake-16 P2/P4.

## Verified live: the bridge target fork

`ksarith/idea-generator-2` exists and carries the CogitoEngine proposal §7 patch, landed 2026-11-14 16:34–16:38 UTC in five upload commits immediately after the CogitoEngine-side deposits of the same day:

- `server/cogito.ts` (+121, new), `server/vetting.ts` (+147, new), `server/db.ts` (+69, the vettings table), `server/app.ts` (+13/-2), `server/index.ts` (+6/-1)
- UI wiring: `public/js/app.js` (+110), `public/js/i18n.js` (+36), `public/style.css` (+11)
- `test/vetting.test.ts` (+297, new); `README.md` and `CLAUDE.md` notes (+4/-1 each)

Upstream is Anders Bjarby's Idea Generator 2 (most recent upstream commits 2026-11-02..04, including the removal of the retired GitHub Models provider). This matches the §7 patch description in PROPOSAL_2026-11-14_PEER_MODE_AND_IDEAGEN_BRIDGE.md (CogitoEngine `7d85421f`): "Vet with Cogito" button, `vet-one` spawned with keys in the child's environment only, a vettings table with SSE updates, counter-proposals becoming seeds only when a person picks one, and Cogito never writing fitness.

The human's runtime report is recorded as he stated it: running the bridged setup became the challenge; it could not be run from a mobile device; Colab was tried. Unverified here (this harness executes nothing). Observation: AuditBot ships a phase-1 Colab cell, but CogitoEngine itself has no Colab path — if mobile/Colab running of the bridge is a real requirement, that is a gap worth an explicit ruling rather than an accident of tooling.

## Rulings owed (consolidated)

1. The nine OPEN_QUESTIONS in the AuditBot draft (author defaults stated; this review endorses the defaults on #2, #3, #4, #7, #8 as the conservative reading).
2. Registration and home for AuditBot and its fixture set (rides the monitoring-home question).
3. Fixture layout pin (root vs. `docs/`) before the first fixture run, so expected results are unambiguous.
4. Whether mobile/Colab running of CogitoEngine (not just AuditBot phase 1) is a requirement to design for.
5. Standing items unchanged: Parlay VP-002 commission and tier; the `contribution` label (direct GitHub action); the STATE.md size question (see MAINT-142).

---
*Provenance: deposited 2026-11-16 by Vibe (GLM 5.3) as MAINT-142 at the human's "Please do." Findings-only; nothing enacted; dispositions await his ruling lines. Record of the pass: `Maintenance/entries/MAINT-142.md`.*
