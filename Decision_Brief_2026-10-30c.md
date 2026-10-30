# Decision Brief — 2026-10-30c (File_Template log-split option: review)

- Author: Vibe, Repo Custodian (delegated line, human-ruled Decision Brief 2026-10-29 item 4A).
- Status: DECISION-READY, AWAITING HUMAN RULING. Nothing here is LazarusForge doctrine; no LazarusForge file was touched by this review.

## 0. What is being reviewed

The carried "File_Template split option" (Decision Brief 2026-10-30 §0, human direction: open, no ruling requested at that time). The question: **should resolution/change logs be physically split out of doctrine files into sibling log files, or stay in-file?** The user asked for this review 2026-10-30, while MDR rater runs are held pending the README rebuild.

## 1. What the repository already has (measured)

- **Pattern A** (adopted 2026-10-28, all defaults D1–D7): an in-file `## Historical Record` boundary. Front = current doctrine; Historical = append-only evidence. Migration at next substantive touch, **never by bulk sweep**. Pilots (Plastics/Woodworking) not yet run.
- **R8 already legalizes relocated logs**: a file whose Resolution Log lives in `Archive/Logs/` keeps one pointer line under Historical Record. The relocation is an allowed form of Historical — so a physical split is *already in-rules*; the open question is whether to use it, and how far.
- **Pattern B (per-file sibling log files) was explicitly not proposed** at Pattern A adoption; no `logs/`/`audits/` subfolders.
- **Rotation changelogs already exist and absorb entropy**: 7 files in `Archive/Logs/` (Progress_Log_Changelog 240,915 chars; Unknowns_Changelog 184,265; Auditor_Protocols_Logs 183,634; Governance_Charter_Changelog 65,108; Forge_Audit_Kit_Changelog 62,279; AUDIT_HARNESS_CHANGELOG 23,051; Discovery_Changelog 7,377). The 20%/Aging rules already push overflow out of live files.
- **Largest live files carrying in-file logs** (chars): Progress_Log 174,140 · Auditor_Protocols 157,497 · Ethical_Constraints 152,274 · Governance_Charter 130,734. Unknowns.md ~1,007 lines, under its 1,200-line compression trigger.

## 2. The measured driver: per-pass fetch cost

Every custodian edit pass must fetch the whole target file before editing. At the session level, fetches of 150–240k-char files are the dominant tool-cost item, and the session has a hard ~8MB budget — the X3 and sweep sessions repeatedly paid it. A front file with its log split out is permanently cheaper to fetch for every future pass. This is the strongest *new* argument for a split; it did not exist when Pattern A was adopted.

## 3. Options

**(A) Status quo — Pattern A in-file only.** Logs stay in-file behind the Historical boundary; Prior-chains migrate at next touch (R7); rotation changelogs keep absorbing overflow. Zero new mechanics, zero migration. Cost: live files keep growing; fetch cost keeps rising; the 20% sidecar rule does not govern Resolution Log bulk.

**(B) Full physical split — every non-exempt file's Resolution Log moves to `Archive/Logs/<FILE>_Log.md` (R8 pointer form).** Maximum front-file slimming. Costs: a corpus-wide migration campaign — exactly the bulk sweep Pattern A's adoption forbids, and the kind of new large campaign Grok's release assessment (human-endorsed) said to avoid before held items are dispositioned; every future pass edits two files (two fetches, two blob shas, two pushes, cross-file parity risk); checks C7/C8 (release-diff) need two-file variants; frozen-history text would move (R3-legal, but a mass move is high-blast-radius).

**(C) Threshold-gated split — R8 on trigger, per file.** Keep the status quo mechanics, but add one standing rule: when a file hits its own rotation trigger, its 20%/aging threshold, or a substantive touch that would push its Resolution Log past a set size (e.g., the log exceeding ~20–25% of the file), its log splits to `Archive/Logs/` at that touch — one file at a time, same migration-at-touch discipline as Pattern A, frozen history moved only under R3/R4 per file. No bulk campaign; the biggest files (Progress_Log, Auditor_Protocols, Ethical_Constraints) split first, at their next qualifying touch.

## 4. Custodian analysis

- **Lean: Option C.** It captures the fetch-cost win where it is largest, inherits Pattern A's already-adopted migration-at-touch discipline instead of inventing a new campaign, and respects the "no new large maintenance sweep" principle. Option B's marginal benefit over C is small (C reaches the same end-state for the heavy files within one touch-cycle each); its marginal cost is a bulk campaign plus a permanent two-file-per-edit tax.
- **Option A is defensible** if you value single-file integrity (C1–C8 stay one-file checks) above session economics.
- **Interactions to record regardless of ruling:**
  - *MDR comparability:* the canonical inputs are README + Charter Tier 1 Axioms + Discovery. If Governance_Charter's log splits before the rater runs, record it as an **instrument change** (the axioms section itself is Front and would not move, but the input hash changes — same rule as the 1.29/1.30 README ruling: record version + hash per run, don't mix).
  - *Unknowns generator (HOLD, intended end-state):* unaffected — it derives from owning-file Unknown tables, not Resolution Logs.
  - *C7/C8:* any split requires the checks to be restated for the two-file form (pointer present; log file append-only between releases).
  - *Unknowns.md compression trigger:* separate mechanism; a split does not substitute for the 1,200-line compression decision, which stays human-held.
- **What a ruling would need to fix if C is chosen:** the split threshold (log ≥ 20% of file, or a fixed char/line figure), the naming convention (`<FILE>_Log.md` matches the existing Auditor_Protocols_Logs.md precedent), and whether the three heaviest files get split at their *next* touch or only at their next *qualifying* (threshold-hitting) touch.

## 5. Ruling requested

1. Log-split disposition: **A (status quo) / B (full split) / C (threshold-gated, custodian lean)**.
2. If C: threshold value and naming convention confirmation.
3. Whether the Charter counts as instrument-relevant for MDR runs if its log splits before the rater runs (custodian assumes yes — record as instrument change; confirm).

## 6. Carried items unaffected

MAQT_Role_Cards 24 held quals · Energy_Scarcity EC-002 ×3 · Unknowns.md 304 hold · operational-prompt-template family exemption · redundant-qualification rules (enacted) · LA row-name deviations · MDR Cycle 1 dispositions + model-family record · Claude P-1 measurement proposal · AUDIT_30/31 wrapper findings · successor-auditor naming · File_Template split option (this brief) · parked rows 45/37/8 · campaign audit PAUSED at CAMPAIGN_AUDIT_32 (explicit human direction only).
