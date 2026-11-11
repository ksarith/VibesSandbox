# MAINT-125 — CUSTODIAN_FIX landed (Adm_Scope_Map.md stale custodian-prompt pointer repair; human-directed fix-pass)

## Summary

Standalone custodian fix-pass (not an audit deposit): the typo'd pointer `Archive/Repo_Costodian_Prompt.md` (transposed "sto") in `Admin/Adm_Scope_Map.md` repaired to the live `Archive/Repo_Custodian_Prompt.md`, path-only, on the human's explicit 2026-11-11 "proceed" direction on the flagged candidate. One LF commit; this VS bookkeeping commit records it. Nothing else changed; no audit performed.

## Landing

- LazarusForge main `f3d744bc3806b00e20c7e3118bc908b5bf83e927`, parent `91f4b1914c1e03f9a801f7970c23ffba98542aa6` (the CAMPAIGN4_AUDIT_34 landing). One file modified (+4/−2 lines): `Admin/Adm_Scope_Map.md` — (1) the Purpose custodial roles note's pointer repointed; (2) the Last Reviewed cell's newest-segment pointer repointed; (3) Last Reviewed advanced with a new 2026-11-11 fix-pass segment; (4) a newest-first Resolution Log entry added with full disclosure. The 2026-10-29 frozen Resolution Log entry left as written per the PKC-007 frozen-history precedent.
- VibesSandbox main — this landing: `Maintenance/entries/MAINT-125.md` (new), `Maintenance/STATE.md` (Last updated line advanced to MAINT-125 + this landing's update note), `Maintenance/MAINT_INDEX.md` (row 142 + the count line 141→142 + the MAINT-125 recount sentence).

## Head checks

- LF head verified `91f4b191` (the CAMPAIGN4_AUDIT_34 landing) at compose and re-verified immediately before the push (abort-on-mismatch guard in place); the repair re-verified post-push (head `f3d744bc`, chain and per-file stats confirmed — 1 file modified, +4/−2 — and the file re-fetched live, SHA-256 matching the pre-push computed value).
- VS head verified `086cae69` (MAINT-124) at compose and re-verified immediately before the VS push; the entries/ home recounted live at 56 files (MAINT-69.md through MAINT-124.md, contiguous, numeric sort) before this landing adds the fifty-seventh.

## Artifacts (SHA-256, UTF-8 bytes)

- `Admin/Adm_Scope_Map.md` pre-repair (46,214 chars at `91f4b191`): `d7da81c6a13a7bcfa1a8dc846780bc986ef0999938d648122dc1dac67337c9d1`
- `Admin/Adm_Scope_Map.md` post-repair (47,708 chars, live-verified at `f3d744bc`): `766d1a56c760a201a4b2f530e580d2346169e44c105ce657d900c74c4d7cad5e`
- Self-count: one entry file added this landing (`MAINT-125.md`); the entries/ home now spans MAINT-69.md through MAINT-125.md (fifty-seven files), recounted live in MAINT_INDEX.

## Findings digest

None new — this was a repair, not an audit. The defect repaired was flagged during the custodian bootstrap: the roles note's spelling does not match the live `Archive/Repo_Custodian_Prompt.md` (16,673 bytes, verified present at `91f4b191`; the typo'd target does not exist in the tree). Verification after repair: operative typo occurrences 0; the string `Repo_Costodian_Prompt.md` survives exactly 3 times (the frozen 2026-10-29 Resolution Log entry + 2 mentions in the new repair prose describing the fix) and `Repo_Custodian_Prompt.md` 4 times (2 operative pointers + 2 in prose); the 2026-10-29 Resolution Log entry untouched; Status/Open Unknowns/scope entries/Gaps Exposed spot-checked unchanged.

## Aging

Not applicable — no audit performed, no sidecar entries reviewed; the Aging aggregate is unchanged by this landing (67 of 84 on the generic reading, 58 of 75 narrow).

## Disclosures

- Non-independence: the repairing line (Vibe, Repo Custodian — delegated) is also the seat the repaired custodial roles note describes; the fix was flagged to the human before execution and executed on the human's explicit 2026-11-11 "proceed". Disclosed in the file's own Resolution Log entry as well.
- Scope: path-only repair; no scope entry, count, Risk field, Status, Spec Gate, or Unknown changed; not a full-folder re-audit.
- Frozen history: the 2026-10-29 Resolution Log entry carrying the typo left as written per the PKC-007 frozen-history precedent.
- One guard abort before the successful push: the first push attempt aborted in-call (nothing pushed) because the guard expected 1 remaining typo occurrence post-repair, but the repair prose itself mentions the old path twice — correct expectations are 3 typo-string / 4 correct-path occurrences. The guard worked as designed; the identical edits were re-run with the corrected guard and pushed.
- Open follow-up (human's): the `Repo_Costodian` spelling may exist in other files — only `Adm_Scope_Map.md` was checked; a corpus-wide grep is a cheap candidate follow-up left to the human.
- Tool notes for the next session: get_commit's parameter is `sha` (not `ref`); get_file_contents returns a two-element array ([meta, { resource: { text } }]) and a directory returns a flat array; list_commits' fields parameter accepts only sha/html_url/commit/author/committer; MAINT-NN span checks must use numeric sort, not lexicographic; TextEncoder is unavailable in the sandbox; the sandbox `sha256sum` binary remains broken (MAINT-120 defect) — use the in-session SHA-256 implementation self-checked against the standard test vectors; large tool outputs are saved to the tool-results store and must be extracted with jq; this jq build does not decode JSON strings via `-j .` and its sed lacks `\xNN` escapes.

## Resume point

None — the fix-pass is complete and verified on both sides. The auditor seat remains vacant; the "Connective Tissue" role mapping remains proposed pending the human's explicit confirmation; every Campaign 4 queued remedy (the systemic Aging pass, the F-AVE-1/F-HDL-2/F-MSF-1 File State batch, the git-verified unlogged-change class, the bare-citation grep remedy, the Rule 5 hand-offs) and all conversions to audits of record remain the human's alone; next direction belongs to the human.
