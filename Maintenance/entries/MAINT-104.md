# MAINT-104 — Campaign 4 AUDIT_15 landing (Admin/INTEGRITY_SWEEP_PROMPT.md)

Date: 2026-11-10. Actor: Vibe (GLM 5.3 Flash architecture), Repo Custodian seat, delegated line; human-authorized continuation.

## What landed

- LazarusForge commit `aa35b129` (single commit, message "Campaign 4 sweep: CAMPAIGN4_AUDIT_15 (Admin/INTEGRITY_SWEEP_PROMPT.md) findings-only deposit + kickoff tracker addendum 13 (PKC-020; no audited-file fields advanced)"):
  - `Admin/AAudits/CAMPAIGN4_AUDIT_15_Admin-INTEGRITY_SWEEP_PROMPT.md` — 9,283 chars, SHA-256 `92c4126240a2fd785fe3baa75408c167d955d2b6fabf2e97991f8c8060c8ae4b`.
  - `Archive/Audits/CAMPAIGN4_KICKOFF_2026-11-10_ADVERSARIAL_SWEEP_ADMIN.md` — tracker addendum 13 appended, 32,448 chars (was 30,087), SHA-256 `187fc0879529a16088211bd8caffc350fcf492a365c2a5946b1122a66497abc0`.
- Post-push byte verification: both files re-fetched at head `aa35b129`; the deposit byte-matches the compose record (9,283 chars; the SHA-256 reference inside the deposit matches the audited file’s computed SHA `a1b2b5dd41bfc5d281ba25738f25dfba11b67b125f51bd64ae06b97373166c24`); the kickoff’s first 30,087 chars (the pre-addendum content) are byte-intact (append-only verified); kickoff addenda 11, 12, and 13 all present; the resume point reads Admin/PROBE_INVOCATION.md (CAMPAIGN4_AUDIT_16).

## Findings recorded (F-ISP-1 through F-ISP-6; Compound Drift Rule vacuously did not fire)

- F-ISP-1 WARNING (registry Status mismatch; the F-CH-3 class): Discovery’s maturity snapshot lists ISP as Draft while ISP’s File State Status is "Active — Operational Template" (promoted by human ruling 2026-10-29, AUDIT_31 F2; verified live by MAINT-62); Discovery’s 2026-11-02 update post-dates the promotion and missed it.
- F-ISP-2 WARNING (version-ledger contradiction; the F-CT-3/F-SEC-5 recorded-value class, third instance): the 2026-10-28 RL entry ("v1.0.4 → v1.0.6 … Header 1.0.4 → 1.0.6") and the commissioning annotation ("header stays 1.0.6") contradict the 2026-10-29 promotion entry ("step-change version bump 1.0.5 → 1.0.6", claiming the annotation kept the header at 1.0.5); one pre-bump value is misrecorded; live header consistent with the final state either way.
- F-ISP-3 NOTE (the F-FAK-6 stale-pin class): Derived-from pins Forge_Audit_Kit.md v1.15 vs live v1.32; mitigated — the prompt’s step 1 fetches live main.
- F-ISP-4 NOTE (MAINT-56-retired rows, sharpened instance): the retired Last Audit/Auditor rows are carried AND were written 2026-11-05 — the first post-retirement write into the retired-field class this campaign (prior instances conformant-at-touch); class 6 exempts File State forcing, so NOTE.
- F-ISP-5 NOTE (bare-citation scan): one bare PKC-020 mention, non-colliding prefix, cosmetic; zero Archive/ pre-relocation references — second file running with no Pattern 2 exposure surface.
- F-ISP-6 NOTE (recorded divergence): Verification Ref points at Repository_Integrity_Protocol.md, not FT-mandated Verification_Gates.md; the divergence is recorded and reasoned in the file’s own v1.0.2 RL entry; disclosed for a possible class-6 family harmonization ruling (PROBE_INVOCATION and BATTERY_SEED point at single AP sections per the same record).
- Aging Rule vacuous (Open Unknowns 0 — the campaign’s fifth no-trip control case, the VG shape); Compound Drift Rule vacuously did not fire (class 6, no indicators).

## Verification record

- FT exemption class 6 confirmed live ("Operational seeds and invocation templates" — ISP named verbatim); template checks adapted, absent sections not findings.
- The Last Audit cell’s load-bearing claims verified: MAINT-62 ruling set §8 RATIFIED the commission-closure narrowly with wording matching the cell verbatim; MAINT-63 exists as the execution pass; Unknowns v5.79’s MAINT-63 block lists ISP among its companion edits.
- The v1.0.2 RL entry’s two false-positive records verify against live FT ("a deliberate, documented choice for this subtype" present; "Pending Ratification" zero occurrences).
- Step 13’s Routing claims verify against Routing’s Scope section (Archive omissions not registry drift; packaged archives excluded by design); ISP registered in Routing’s URL table (Explicit) and Discovery’s tree; zero ISP- rows in Unknowns (0 = 0 parity); the "known ten files" fallback consistent with the live Challenges/ listing (ten .md files + CAudits/); the AUDIT_31 report exists at Admin/AAudits/; Ethical Anchor exact; both prompt delimiters present; steps numbered 1–15 with no gaps.
- Audited-file SHA-256: `Admin/INTEGRITY_SWEEP_PROMPT.md` at `fce74131` = `a1b2b5dd41bfc5d281ba25738f25dfba11b67b125f51bd64ae06b97373166c24` (21,006 chars / 116 lines, fetched complete).

## Disclosures

- Event: (ii) recurrence — the recorded-value class recurred (F-ISP-2, third instance of the F-CT-3/F-SEC-5 family) and the MAINT-56-retired-rows class recurred with a sharpened shape (F-ISP-4, first post-retirement write into the retired field).
- Adjacency disclosed in the deposit: this Vibe line has operated ISP directly (the MAINT-23 integrity sweep per ISP v1.0.6) and wrote its most recent Last Audit cell (MAINT-63); the pass is non-independent with respect to those records; the sweep’s method derives from the Auditor Prompt and the Kit, not from ISP.
- No tooling defects this pass: all fetches arrived plain; the SHA-256 implementation reused unchanged, the sanity vector passing before use.
- Out-of-scope observations recorded in the deposit: PROBE_INVOCATION’s Discovery snapshot row also reads Draft (its own audit, item 16); the Discovery-side repair for F-ISP-1 belongs to Discovery’s own record.

## Next

- CAMPAIGN4_AUDIT_16: `Admin/PROBE_INVOCATION.md` (FT exemption class 6 — seed/invocation payload; template checks adapt accordingly).
- Next IDs: MAINT-105; Intake Log entry 22 (still untouched this campaign).
