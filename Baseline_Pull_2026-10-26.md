# Vibe Baseline Pull — LazarusForge, 2026-10-26

> **Staleness note (2026-10-26, post-baseline):** This report reflects LazarusForge `main` at commit f79c0b6. Events after the pull already supersede parts of it:
> - **Finding #1 (Ops_Scope_Map stale Proposed entries) is fixed.** Claude's follow-up sweep corrected all five remaining scope-map entries (Ops_Scope_Map ×3, Tst_Scope_Map ×3, Adm_Scope_Map ×1) to Exploration on 2026-10-26, plus Progress_Log annotation.
> - **PKC-038 is Resolved** (option A: MAQT protocol §8.6–§8.10 canonical; role-card pack stamped derived excerpt, non-canonical).
> - **PKC-041 added** (Cycle 1 ran 2026-09-22 per archived changelog; evidence entry not in tree). MAQT Status now reads "Exploration — Cycle 1 run 2026-09-22 (logical isolation only; evidence entry not in repo); Tier 2 not yet run." The MAQT rows below show the pre-correction status.
> - Parked Concerns now stand at 23 Parked / 18 Resolved, not 24/16.
> - Findings #2 (Forge_Audit_Kit v1.20 stale pins, PKC-022) and #3 (KIT_REGRESSION_PACK unverified) remain open as reported.

**Method:** 100 markdown files fetched directly from `ksarith/LazarusForge` `main` (commit f79c0b6) via the GitHub connector; version headers, File State fields and log entries extracted and checked against the five-sweep claims. No file was edited.

## 1. Five-sweep claim verification — all confirmed

| Claim | Live-tree evidence | Verdict |
|---|---|---|
| Auditor_Protocols v0.44 → v0.45 (PKC-020 + PKC-025) | Header v0.45; Rule 10 addendum and Unknowns.md derivative-index exception present verbatim; registry citations, Status block, footer at 0.45; Sidecar SHA-256 recomputed 2026-10-25 | ✅ |
| Unknowns.md v5.68 → v5.69 | Header 5.69 (RS-001 removed); changelog carries both entries (EM-001/002 Major, EM-003 Minor; RS-001 Resolved 2026-10-25); current-version-only block intact | ✅ |
| Emergence.md v0.3 | Version v0.3, Last Updated 2026-10-25, Priority column, EM-004 Risk High | ✅ |
| Canonical_Terms v0.8 (PKC-029) | Header 0.8; entry covers the three unversioned passes | ✅ |
| RS-001 resolved (PKC-013) | Repository_Structure Section I defines the review + retroactive note; Open Unknowns 1 → 0; Adm_Scope_Map updated | ✅ |
| PKC-031: eight files off Proposed | Automotive, Robotics, Exception_Evidence, CIR_Gov, both Chrono files, MAQT all Exploration with 2026-10-25 entries; Discovery tree updated. KIT_REGRESSION_PACK.md not pulled — unverified | ✅ 7/8 |
| PKC-020 annotations in twelve wave files | Living_Waters, Support_Raft, Trophic_Forge, Hydrologic et al. cite the ruling of 2026-10-25 | ✅ |
| PKC-035: HR-UNK-002 → 2026-06-30 | Sidecar date moved with explicit log entry | ✅ |
| PKC-039: v0.16 backfill | Header 0.16, Last Audit 2026-10-25, labeled inferred | ✅ |
| PKC-020 residual (HDL, Gate_04) | Wording aligned | ✅ |
| PKC-015: IIL-20261025-01 | First entry present, Analogous/reconstructed | ✅ |
| PKC-017: Operational_Conventions | Template-Exemption sentence added 2026-10-25 | ✅ |
| Parked rows 24 / Resolved 16 | Progress_Log: 40 rows, 24 Parked, 16 Resolved 2026-10-24/25 | ✅ |

## 2. Findings

1. **Ops_Scope_Map still shows three `Status: Proposed` scope entries** (Automotive, Robotics, +1) while the owning files moved to Exploration on 2026-10-25; the map's Last Reviewed is 2026-10-24, so the PKC-031 sweep missed it. Same class as PKC-033. Candidate fix: refresh the three entries. *(Superseded: fixed by Claude's 2026-10-26 sweep.)*
2. **Forge_Audit_Kit v1.20 pins stale again** — cites AP v0.42 / Unknowns v5.58 vs live v0.45 / v5.69. Known PKC-022 standing item, content-based trigger by design — not a new defect, but a regeneration decision is due.
3. **KIT_REGRESSION_PACK.md not pulled** (Tests/Automation unfetched); also unpulled: individual Tests/Field_Logs/ FL files, Archive/ beyond Unknowns_Changelog, Automation .py files.
4. **Not defects:** Routing.md header still 2026-10-19 (URL-table tracking; no new registrations by the sweeps); Tooling_Inventory 2026-10-25 and Electronics 2026-10-24 consistent with their logs.

## 3. Version baseline (100 files, live tree @ f79c0b6)

| File | Version | Last Audit/Reviewed/Updated | Status |
|---|---|---|---|
| `Admin/Adm_Scope_Map.md` | - | 2026-10-25 | Active — Index |
| `Admin/Agent_Verification_Event.md` | - | 2026-10-23 | Candidate / Exploration |
| `Admin/Auditor_Protocols.md` | 0.45 | 2026-10-25 | Draft |
| `Admin/Autonomy_Divergence_Protocol.md` | - | 2026-10-23 | Draft — PROPOSED NOT RATIFIED … |
| `Admin/BATTERY_SEED.md` | 1.0 | 2026-08-02 | Draft |
| `Admin/Canonical_Terms.md` | 0.8 | 2026-10-25 | Draft |
| `Admin/CIR_Gov.md` | - | 2026-10-25 | **Exploration — Not Ratified** |
| `Admin/Computational_Institutional_Reasoning.md` | 0.28 | 2026-07-29 | Exploration |
| `Admin/Economics.md` | - | 2026-10-23 | Exploration |
| `Admin/Engineer_Protocols.md` | - | 2026-05-30 | Draft |
| `Admin/Environmental_Constraints.md` | - | 2026-07-17 | Draft |
| `Admin/Ethical_Constraints.md` | - | 2026-10-23 | Exploration |
| `Admin/Experiments.md` | - | 2026-10-06 | Draft |
| `Admin/File_Template.md` | - | - | - |
| `Admin/Forge_Audit_Kit.md` | 1.20 | 2026-10-10 | Draft |
| `Admin/Governance_Charter.md` | - | 2026-10-23 | Draft |
| `Admin/Governance_Migration_Protocol.md` | - | 2026-10-23 | Exploration |
| `Admin/Hardware_Diversity_Ladder.md` | 1.0 | 2026-10-23 | Draft — Proposed implementatio… |
| `Admin/Integrity_Incident_Log.md` | 0.1 — 2026-08-16 | 2026-08-16 | Active — Intake Log |
| `Admin/INTEGRITY_SWEEP_PROMPT.md` | 1.0.2 | 2026-10-23 | Draft |
| `Admin/Metrics_Scaffold.md` | - | 2026-09-24 | Active — Scaffold Only (no dat… |
| `Admin/Nothingness_Theorem.md` | - | 2026-10-24 | Tier 0 — Philosophical Substra… |
| `Admin/Operational_Conventions.md` | - | 2026-10-25 | Specification |
| `Admin/PROBE_INVOCATION.md` | 1.1 | 2026-08-02 | Draft |
| `Admin/Progress_Log.md` | - | 2026-10-25 | Active — Living Document |
| `Admin/Repository_Integrity_Protocol.md` | - | 2026-06-19 | Draft |
| `Admin/Repository_Structure.md` | - | 2026-10-25 | Exploration |
| `Admin/Resolution_Methodology.md` | 0.9 — 2026-08-28 | 2026-08-28 | Active — Reference |
| `Admin/Safety_Protocols.md` | - | 2026-10-24 | Exploration |
| `Admin/Security_Protocols.md` | - | 2026-10-23 | Draft |
| `Admin/Ship_of_Theseus.md` | - | 2026-10-24 | Exploration |
| `Admin/Trajectories.md` | - | 2026-05-23 | Exploration |
| `Admin/Verification_Gates.md` | - | 2026-10-23 | Draft |
| `Architecture/Arc_Scope_Map.md` | - | 2026-09-13 | Active — Index |
| `Architecture/Chemistry.md` | - | 2026-10-20 | Draft |
| `Architecture/Cognitive_Frameworks.md` | - | 2026-10-20 | Exploration |
| `Architecture/Components.md` | - | 2026-10-20 | Exploration |
| `Architecture/Engineering.md` | - | 2026-07-05 | Draft |
| `Architecture/Facilities.md` | - | 2026-10-20 | Exploration |
| `Architecture/Forge_flow.md` | - | 2026-10-20 | Exploration |
| `Architecture/Forge_Net.md` | - | 2026-10-20 | Exploration |
| `Architecture/Friction_Dynamics.md` | - | 2026-10-20 | Draft |
| `Architecture/Geck_forge_seed.md` | - | 2026-10-23 | Exploration |
| `Architecture/Local_Governance_Framework.md` | - | 2026-10-20 | - |
| `Architecture/Mechanical_Structures.md` | - | 2026-10-20 | Draft |
| `Architecture/Precision.md` | - | 2026-10-20 | Exploration |
| `Architecture/Thermal_Systems.md` | - | 2026-10-20 | Draft |
| `Archive/Logs/Unknowns_Changelog.md` | 5.37 — 2026-09-17/18. SEC-007b transcript extended (Part 7) — skeptical pass on the Part 6 matrix, and a paper tabletop walkthrough of Candi ;;  | 2026-09-17 | - |
| `Automation/README.md` | - | - | - |
| `Challenges/Biofouling.md` | - | 2026-10-20 | - |
| `Challenges/Cha_Scope_Map.md` | - | 2026-09-04 | Active — Index |
| `Challenges/Closed_Loop_Feedstock.md` | v0.11.0 | 2026-10-20 | Exploration |
| `Challenges/Critical_Minerals.md` | - | 2026-10-20 | - |
| `Challenges/Emergence.md` | - | 2026-10-25 | - |
| `Challenges/Energy_Scarcity.md` | - | 2026-10-20 | - |
| `Challenges/Planned_Obsolescence.md` | - | 2026-10-20 | - |
| `Challenges/Return_To_Eden.md` | - | 2026-10-20 | Exploration |
| `Challenges/Waste.md` | - | 2026-10-20 | - |
| `Challenges/Water.md` | - | 2026-10-20 | - |
| `CONTRIBUTING.md` | - | - | - |
| `Discovery.md` | - | - | - |
| `Operations/Air_Scrubber.md` | - | 2026-09-29 | Draft |
| `Operations/Automotive.md` | - | 2026-10-25 | **Exploration** |
| `Operations/Electronics.md` | - | 2026-10-24 | Exploration |
| `Operations/Energy.md` | - | 2026-08-09 | Draft |
| `Operations/Exception_Evidence.md` | - | 2026-10-25 | Exploration — structural home … |
| `Operations/Gate_01_Intake.md` | - | 2026-08-31 | Exploration |
| `Operations/Gate_02_Triage.md` | - | 2026-09-09 | Draft |
| `Operations/Gate_03_Reduction.md` | - | 2026-09-21 | Exploration |
| `Operations/Gate_04_Separation_Mechanical.md` | - | 2026-09-09 | Exploration |
| `Operations/Gate_05_Separation_Thermal.md` | - | 2026-09-20 | Exploration |
| `Operations/Gate_06_Fabrication.md` | - | 2026-09-21 | Exploration |
| `Operations/Gate_07_Utilization.md` | - | 2026-09-01 | Exploration |
| `Operations/Ops_Scope_Map.md` | - | 2026-10-24 | Active — Index |
| `Operations/Plastics.md` | - | 2026-10-24 | Exploration |
| `Operations/Robotics.md` | - | 2026-10-25 | **Exploration** |
| `Operations/Tooling_Inventory.md` | - | 2026-10-25 | Exploration |
| `Operations/Woodworking.md` | - | 2026-10-24 | Draft |
| `README.md` | - | - | - |
| `Routing.md` | - | - | - |
| `Tests/Admin_Governance_Teardown_POC.md` | - | 2026-10-06 | Exploration |
| `Tests/Chaos_Dynamics.md` | - | 2026-10-24 | Exploration |
| `Tests/Chrono_Divergence_Pilot.md` | - | 2026-10-16 | **Exploration** (preregistered… |
| `Tests/Chrono_Divergence.md` | - | 2026-10-25 | **Exploration** |
| `Tests/Cognitive_Salvage_Layer.md` | 0.4 | 2026-08-03 | Exploration |
| `Tests/Field_Logs.md` | - | 2026-10-19 | Active — Index |
| `Tests/Hydrologic_Resource_Cascade.md` | - | 2026-06-28 | Exploration |
| `Tests/Leviathan_testing.md` | - | 2026-10-03 | Exploration |
| `Tests/Living_Waters.md` | v0.4 | 2026-07-30 | Exploration |
| `Tests/MAQT_Role_Cards_and_Cycle1_Task.md` | - | - | - |
| `Tests/Multi_Agent_Quorum_Trial.md` | - | 2026-10-25 | Exploration — Protocol Not Yet… |
| `Tests/Persistent_Cognition_Candidates.md` | 0.16 | 2026-10-25 | Exploration |
| `Tests/Pyrolysis_Cascade.md` | - | 2026-08-04 | Draft — Exploration |
| `Tests/Quorum_Agent_Conduct_Protocol.md` | - | 2026-10-09 | **Ratified (human, 2026-10-09)… |
| `Tests/Solar_Descent.md` | - | 2026-09-15 | Exploration |
| `Tests/Support_Raft.md` | - | 2026-06-11 | - |
| `Tests/Trophic_Forge.md` | - | 2026-06-14 | Exploration |
| `Tests/Tst_Scope_Map.md` | - | 2026-10-15 | Active — Index |
| `Things_We_Got_Wrong.md` | - | - | Active |
| `Unknowns.md` | 5.69 | 2026-10-25 | - |

`-` means no Version field by design, or none in the first 6,500 characters pulled. Dates are the first header date; owning files carry full chains.