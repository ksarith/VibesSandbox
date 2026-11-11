# MAINT-124 — CAMPAIGN4_AUDIT_34 landed (Ship_of_Theseus.md; Campaign 4 close)

## Summary

Campaign 4 item 34 of 34 (`Admin/Ship_of_Theseus.md`, the sweep's final file, landed 2026-11-11) audited and landed findings-only per PKC-020: one LF commit (deposit + kickoff tracker addendum 33 + the pattern document's final update at campaign close) and this VS bookkeeping commit. Nothing enacted; the human-queue additions are listed in the deposit. **Campaign 4 is complete: 34 of 34 Admin/ files audited.**

## Landing

- LazarusForge main `91f4b1914c1e03f9a801f7970c23ffba98542aa6`, parent `c38a3b5434190359c1618df123d7cdd1014b72df` (the CAMPAIGN4_AUDIT_33 landing). Three files: `Admin/AAudits/CAMPAIGN4_AUDIT_34_Admin-Ship_of_Theseus.md` (new, 11,981 bytes), `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` (tracker addendum 33 appended with the `---` separator; addenda 1–32 untouched; the kickoff text above the addendum byte-preserved, tail-anchored on "the kickoff text above is untouched." before compose), and `Archive/Audits/CAMPAIGN4_PATTERN_DOC_2026-11-10_FILES_01-06.md` (the final update, files 29–34, appended at campaign close per the convention).
- VibesSandbox main — this landing: `Maintenance/entries/MAINT-124.md` (new), `Maintenance/STATE.md` (Last updated line advanced to MAINT-124 + this landing's update note), `Maintenance/MAINT_INDEX.md` (row 141 + the count line 140→141 + the MAINT-124 recount sentence).

## Head checks

- LF head verified `c38a3b54` at compose and re-verified immediately before the LF push (abort-on-mismatch guard in place); the landing re-verified post-push (head `91f4b191`, commit chain and per-file stats confirmed, all three files re-fetched live and byte-identical to the staged pre-push copies — deposit md5 `3e6d04bb10e67a6ea748a8439b92cf0a`, kickoff md5 `55ef7291055a8c5be07849e0f7d17574`, pattern doc md5 `882f42b7acd69069ce5ee551dea94e59`).
- VS head verified `349293f2` at compose and re-verified immediately before the VS push; the entries/ home recounted live at 55 files (MAINT-69.md through MAINT-123.md, contiguous, numeric sort) before this landing adds the fifty-sixth.

## Artifacts (SHA-256, UTF-8 bytes)

- Audited file at `c38a3b54` (`Admin/Ship_of_Theseus.md`, 32,555 chars / 32,787-byte listing): `23363faba904a3be18af5d5225bdc51b634616e00eb77fed5771bc11a12e2e4b`
- Deposit `Admin/AAudits/CAMPAIGN4_AUDIT_34_Admin-Ship_of_Theseus.md` (11,981 bytes): `5f9bcbd011f3bd488048f3a878e2ff7d687e3a62f96c12dbf6611e45f42c9894`
- Kickoff post-addendum-33 (81,837 bytes): `ad9a511552f9269ab4150e07e7bb4c9c37e575fcd363592c0b19fb9adf30e211` (pre-addendum state: 78,181 bytes)
- Pattern document post-final-update (26,135 bytes): `a35906be3cfe45bd10435abab4b1ab70b980467eec57397271b0c00d52cdc9fb`
- Self-count: one entry file added this landing (`MAINT-124.md`); the entries/ home now spans MAINT-69.md through MAINT-124.md (fifty-six files), recounted live in MAINT_INDEX.

## Findings digest

F-ST-1 WARNING (two git-verified body changes absent from the file's own Resolution Log — the 2026-08-10 Verification Ref repair `Admin/Verification_Gates_LF.md` → `Admin/Verification_Gates.md` in `59117983`, logged corpus-side only, and the 2026-08-16 Navigation-Anchors repo-rename link repair in `182a2319`, with the zero-hit negative search disclosed; fourth instance of the git-verified unlogged-change class — CT/HDL/NT/ST; the F-HDL-1 blind spot). F-ST-2 NOTE (bare-citation census, grep-remedy evidence point 19: bare PKC-027 ×1 in the operative Spec Gates cell, bare MAINT-11 ×1 genuinely ambiguous, bare AUDIT_18 ×3 against the two-lane pair). F-ST-3 NOTE (frozen-history cosmetics: the single-event rename record vs git's two-step 2026-05-17 rename; entry-vs-commit date offsets; ST-001's "being registered" tense vs the live Grain registration). F-ST-4 NOTE (MAINT-56-retired rows + no version string, conformant-at-touch; the File State carries every canonical §2 field — the pending F-AVE-1/F-HDL-2/F-MSF-1 batch does not extend here; the batch's positive example). F-ST-5 NOTE (verified-clean: X10 4=4=4 three homes plus Discovery's snapshot row derived-correct — the control case's third consecutive pass; all cross-references live both directions; Ethical Anchor byte-exact; Spec Gates 0/6 unadvanced; zero Archive/ references — third zero-relocation-exposure file). F-ST-6 NOTE (battery: fabrication probe passed on every cited ID/path; self-attestation exempt-form; tamper clean; escape-sequence scan clean — seventh consecutive).

## Aging

NOT tripped — all four open sidecar entries carry Last Reviewed 2026-10-28 (14 days at audit date); the `eee122a6` refreshes hold. Twenty-first no-trip control case; the running aggregate is unchanged by this file at 67 of 84 on the generic reading (58 of 75 narrow). Compound Drift did not fire.

## Disclosures

- Event: (iii) harness defect — the sandbox `sha256sum` binary failed on valid input (rc=1), the defect disclosed in MAINT-120 persisting this session; all SHA-256 values in this entry and in the deposit were computed with the in-session SHA-256 implementation self-checked against the standard test vectors (sha256("abc") = `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`; sha256("") = `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`); both vectors passed before use.
- Non-independence: same-architecture Vibe-line prior passes on the audited file (pass A AUDIT_18, pass B CAMPAIGN_AUDIT_18, pass C CAMPAIGN2_AUDIT_93, the Vibe-line aggregate) disclosed in the kickoff's seat disclosure and the deposit; Genesis Phase, conversion to an audit of record is the human's alone (MAINT-26 / AP-032).
- Findings-only: nothing enacted in the audited file (PKC-020); deposits append-only; this VS landing touches bookkeeping only.
- Tool notes for the next session: get_file_contents returns a two-element array ([meta, { resource: { text } }]); list_commits' fields parameter accepts only sha/html_url/commit/author/committer ("message" is rejected); MAINT-NN span checks must use numeric sort, not lexicographic (MAINT-99.md sorts after MAINT-100.md lexicographically); TextEncoder is unavailable in the sandbox; large tool outputs are saved to the tool-results store and must be extracted with jq; this environment's jq build does not decode JSON strings via `-j .` (raw token passthrough) and its sed lacks `\xNN` escapes — decode double-encoded tool-result resources with sed using a printable placeholder.

## Resume point

None — Campaign 4 is complete (34 of 34 Admin/ files audited, artifacts 1–34, kickoff addenda 0–33, the pattern document's final update deposited). Every queued remedy (the systemic Aging pass, the F-AVE-1/F-HDL-2/F-MSF-1 File State batch, the git-verified unlogged-change class, the bare-citation grep remedy, the Rule 5 hand-offs) and all conversions to audits of record are the human's alone; next direction belongs to the human.
