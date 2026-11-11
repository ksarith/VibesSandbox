# MAINT-129 — Cheap subset ratified and enacted: D-2, D-8, D-9, D-10 (PROPOSAL_2026-11-11_CAMPAIGN4_DESIGN_GAPS option B)

## Summary
The human ruling "Let's ratify those easy items." (2026-11-11) is recorded as Option B of the Architect proposal: the cheap subset D-2/D-8/D-9/D-10 ratified; D-1 and D-3..D-7 remain open proposals (open proposals 2–7 of 10). Enacted by this (Custodian) seat as the proposal §8 assigns:
- **D-2** — Kit touch: `Admin/Forge_Audit_Kit.md` v1.32 → v1.33; the named-record probe added to the Verification Gates section as a dated note bullet (draft text verbatim; motivating instance: the GOV-022 cluster — a sidecar record attested twice that git shows never existed); Last Audit + Auditor advanced; in-kit Resolution Log entry (the "Most recent: v1.31" line demoted to "Prior:" — disclosed); companion v1.33 entry in `Admin/ALogs/Forge_Audit_Kit_Changelog.md`.
- **D-8** — IIL: routing row added to "When to log here vs elsewhere" (draft text verbatim); IIL-20261110-01 logged (the 2026-11-10 parallel-composition clobber) with Severity and RIP classification deliberately pending the human (Decision Brief 2026-11-11 Item 2); Resolution Log entry; Last Audit + Auditor advanced; append-only discipline kept, no prior entry edited.
- **D-9** — endorsement recorded, no mechanism: the Architect seat endorses the Brief Item 2 line B discipline (one remedy pass at a time; head-SHA check against the compose base immediately before every push, abort on mismatch); session discipline, not repo mechanism; applied to this pass's own landings.
- **D-10** — harness-side, no repo change: acceptance-test gates adopted in-session from this pass onward — (a) tail sentinel (every pushed file's terminal bytes and length verified against the compose state by post-push re-fetch), (b) escape-sequence scan promoted from battery item to pre-push gate (introduced text must scan clean; clean on all three LF files this pass). Recorded as a PKC-045 harness work-record item, not TWGW.

## Landing
- LF one commit `79e1896ff96452797cd2fb0efd38e9f795dfa01c` on top of `35973fae` (3 files: Forge_Audit_Kit.md, Admin/ALogs/Forge_Audit_Kit_Changelog.md, Admin/Integrity_Incident_Log.md).
- VS — this landing: proposal Status → PARTIALLY RATIFIED; MAINT-129 entry; STATE (Last updated → MAINT-129 + end-of-file update note); MAINT_INDEX (new row + count 145→146 + recount).

## Head checks
- LF `35973faea459a77e3e105e4b13b79e66b3fe9719` verified live immediately before the LF push; VS `6aab69e99d9c59e3ab439e90cf34d5c4ede1694b` verified live immediately before this push; entries/ recounted live (sixty files, MAINT-69..128, contiguous) before this sixty-first.

## Disclosures
- Event: (i) first occurrence — first ratification-and-enactment of a proposal from the Architect seat. Event: (ii) recurrence — the MAINT-80 Event tag convention applied here after its MAINT-125..127 omission (recorded at MAINT-128; the retrofit question is still the human's).
- Non-independence: the same line drafted the proposal (Architect), records the human's ratification and enacts it (Custodian); Genesis Phase — the human's in-the-loop ruling is the independent layer; the auditor seat is vacant, so post-landing verification is same-line self-verification (MAINT-26 / AP-032 posture), disclosed.
- Home choices disclosed: the D-8 routing rule landed as a row in the IIL's own "When to log here vs elsewhere" table (the log's routing surface) rather than an RIP amendment — the lighter, in-place option; RIP untouched. The D-2 probe landed as a dated note bullet in the Kit's Verification Gates section (that section's established dated-note pattern) rather than a new Fallacy Checklist item (which would renumber the checklist). The proposal's one-touch plan (D-1+D-2) was not followed because D-1 is not ratified; D-2 landed standalone, so a later D-1 ratification is a second Kit touch.
- IIL-20261110-01's classification is deliberately pending: the proposal and the Decision Brief both reserve RIP classification to the human (Brief Item 2).
- Nothing else advanced: no Spec Gate, no Unknown, no Status change beyond the fields named; frozen history untouched (PKC-007); the IIL's frozen IIL-20261025-01 entry untouched.

## Resume point
- Open: D-1, D-3, D-4, D-5, D-6, D-7 (open proposals 2–7 of 10; the proposal recommends the Kit touch D-1+D-2 note is now superseded — D-2 has landed, so D-1 would be its own touch); all Decision Brief 2026-11-11 Items 1–10 (IIL-20261110-01's classification rides Item 2); the two-file bookkeeping gap (MAINT-127); the corpus-wide `Repo_Costodian` grep; the "Connective Tissue"/"Synthesizer" role-mapping ratification; the auditor-seat vacancy / successor question. Next direction belongs to the human.
