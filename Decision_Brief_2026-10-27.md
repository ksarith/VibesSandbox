# Decision Brief — 2026-10-27 (prepared by Vibe, autonomous management)

**Purpose:** decision-ready material for the human ruling session recommended by the Grok assessment (2026-10-27). Nothing here is LazarusForge doctrine; it carries no Spec Gate, Status, or Unknowns weight (sandbox governance boundary). Each section states the options, the record evidence, and Vibe's recommendation. The human governing authority decides.

---

## 1. Pin-vs-retire for derived artifacts (PKC-022 / FAK-014–019; folds in PKC-014's BATTERY_SEED pin)

**The record:**
- Seven staleness occurrences logged (FAK-014 through FAK-019), each found by chance, an external sweep, or an audit — never by the pin itself doing its job.
- The v1.20 mitigation (2026-10-10) already replaced the pin's operative function: the maintenance trigger is content-based (a plain version increment is not a trigger), and the reconciliation check at audit start is doctrine.
- The v1.22 pass (2026-10-27) was the first cycle where the content trigger fired and was honored — 2-day lag, human-authorized, no chance discovery involved.
- BATTERY_SEED's v0.32 pin lags 13 versions with zero functional consequence, because the seed copies no AP content (findings-only check, 2026-10-27).

**Options:**
- **A — Keep light pins + periodic targeted refreshes (current path).** Cost: one FAK-style row per stale cycle, forever; the kit's Open Unknowns list grows monotonically. Benefit: an at-a-glance mismatch cue.
- **B — Retire version pins** (keep the source-file list and a reconciled-against *date*; the audit-start reconciliation check remains the staleness defense). Removes the entire recurring defect class. Risk: loses the passive visual cue — but no historical staleness was ever caught by that cue before an audit or sweep found it anyway.
- **C — Hybrid:** pin only what the kit actually condenses (AP sections), drop pins on sources where only entry-level changes occur (Unknowns). Halves the noise; keeps a two-tier convention (more doctrine to maintain).

**Vibe's recommendation: B**, applied to both Forge_Audit_Kit and BATTERY_SEED in one ruling. The content-based trigger plus the audit-start check already exist as ratified doctrine and demonstrably do the work; the pin now generates findings without preventing any. If you prefer a softer step, C is defensible for the kit but should not be extended to BATTERY_SEED (nothing it contains is version-sensitive).

---

## 2. PKC-033 — Ops_Scope_Map Does/Does-not re-derivation (authorization request)

**Scope of the proposed autonomous cycle:**
- 14 entries in `Operations/Ops_Scope_Map.md` (Air_Scrubber, Automotive, Electronics, Energy, Exception_Evidence, Gate_01–07, Plastics, Robotics, Tooling_Inventory, Woodworking).
- For each: read the owning file's live File State and Scope Boundary, re-derive the entry's Status / Spec Gates / Open Unknowns / Risk counts and the full Does / Does-not text, and correct drift. Same method as the map's 2026-08-08 build and 2026-09-13 content-accuracy pass, both of which caught real errors (the UNK-008 three-file staleness pattern; the Gate_02 mechanism-vs-workflow tension).
- Known stale ground already flagged in the row: Plastics (halogenated-polymer triage, EC-013 descent sequence missing from its Does line), Air_Scrubber and the Gates (content gained after 2026-08-08), plus everything filed since the 2026-09-13 pass (Automotive/Robotics stubs, Exception_Evidence, EV-006–008 in Energy).
- Deliverable: one map commit + Resolution Log entry; any owning-file defects found along the way are reported, not fixed in-pass, unless you re-authorize the 2026-08-08 fix-along-the-way instruction.
- Estimate: single focused cycle; the owning-file reads dominate (14 files, several large).

**Vibe's recommendation: authorize**, with the fix-along-the-way instruction restated explicitly either way (the 2026-08-08 pass fixed errors in-pass per your direct instruction; PKC-026-era practice reports-then-fixes instead — pick one so the cycle's behavior is unambiguous).

---

## 3. PKC-001 — shared-cause question on header/log decay (hold or investigate)

**The record:** the row (High weight) holds that 33 of 47 files showed stale bookkeeping in two shapes; the question is whether the decay had a shared cause, and no bulk header/log backfill is authorized until it is answered. The PKC-015 intake of the decay into Integrity_Incident_Log explicitly waits on this answer.

**Options:**
- **Hold.** The decay is historical; the bookkeeping has been maintained since 2026-10-23; nothing currently regenerates the defect. Cost: IIL keeps waiting for its first intake, and the row stays the largest Parked hold.
- **Investigate now (autonomous, read-only):** reconstruct what the pre-2026-10-23 sessions actually did (dates of last Resolution Log entries vs body edits across the five named files), determine whether one process gap explains both shapes, and report. Estimate: one focused read-only cycle; no backfill, no edits.

**Vibe's recommendation: investigate now, read-only.** The question is answerable from the repo's own records, it unblocks PKC-015's intake (already ruled Yes on the decay itself), and a read-only pass cannot produce the annotation-without-marker defect the row warns about. If the investigation cannot reach a confident answer, that finding is itself the row's answer and it closes as "no shared cause determinable — declare decay historical."

---

## 4. Verified from the record (no action needed)

- **No residual unexplained gate holds.** PKC-042's 2026-10-27 repo-wide sweep (every live file with a Spec Gates field) annotated all four anomaly files with hold reasons and confirmed the control cases already documented theirs. Grok's "confirm none remain" is satisfied by that sweep; a fresh re-sweep is redundant unless you want one.
- **BATTERY_SEED role-declaration string:** cosmetic, defer (Grok item 4 agreed).
- **Autonomous lane:** unchanged — hygiene, cross-reviews, derivation audits, annotation, recommendation prep in lane; gate promotion, Tier 1/FROZEN, Status advancement, ratification remain human-only.

---

*Prepared 2026-10-27 by Vibe (Skeptic/Auditor, human-authorized autonomous management). Sources: Progress_Log §Parked Concerns (PKC-001, PKC-014, PKC-022, PKC-033, PKC-042 rows), Forge_Audit_Kit v1.22 + changelog (FAK-019), BATTERY_SEED findings-only entry, Ops_Scope_Map live tree, and the Grok assessment as relayed by the human.*
