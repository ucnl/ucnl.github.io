# docs-sync: current state

State on 2026-10-09. `master` HEAD: `9e88c28a` (Phase 1 merged: `CLAUDE.md`, `REPORT.md`, `glossary.md`, `docsync.py`, agent definition).

This branch (`docs-sync/state`) is a status record for resuming the sync. It is not meant to be merged.

## Phases

| Phase | Status |
|---|---|
| 1. Inventory and plan | done, merged (#2) |
| 2. Translation batches | 26 of 30 batches pushed; 99 EN documents written; 4 batches (8 documents) remain |
| 3. Index pages, README, deferred links | not started (starts after all batch PRs are merged) |
| 4. Final QA | not started |

Maintainer decisions in force:
- All 52 DECIDE recommendations are accepted (`REPORT.md` → Decisions).
- The English legal name is `UCNL LLC`.
- `Zima2_fast_start` is translated.
- Product names are always mixed case in EN text: uWave, RedWave, RedBase, RedNode, RedNav, RedNav Host, RedLine, Zima. Acronyms stay: RWLT, WAYU, A3S, F4105, RedGTR, GIB. File names, link targets, code and identifiers are unchanged.

## Batch pull requests (all drafts, base `master`)

Every PR description follows `CLAUDE.md` section 11 and lists the open questions for the maintainer.

| PR | Branch | Docs | EN files |
|---|---|---|---|
| #3 | `docs-sync/zima-1` | 4 | Zima2B_Specification, Zima2_DataBrief, Zima2_Users_manual, Zima2_fast_start; also the latest `.github/docs-sync/docsync.py` |
| #4 | `docs-sync/zima-2` | 8 | Zima2B35, Zima2BK, Zima2L, Zima2R35, Zima2RK, Zima2R, Zima2uR specifications; Zima2_LBL_DataBrief |
| #5 | `docs-sync/zima-3` | 6 | Zima2_Protocol_Specification, Zima2 / Zima2K / Zima2-OEM35 passports, Zima2_version_history, ZimaR_wiring_diagram |
| #6 | `docs-sync/zima-4` | 1 | AzimuthConsole_manual |
| #7 | `docs-sync/zima-5` | 8 | Bat_n_link_box spec and manual, Zima2-35 passport, Zima_B, Zima_DataBrief, Zima_GNSS_requirements, Zima_R_OEM, Zima_R |
| #8 | `docs-sync/zima-6` | 2 | Zima_Users_manual, Zima2SL_Specification |
| #9 | `docs-sync/zima-7` | 3 | Zima_Protocol_Specification, AzimuthConsole_v1x, Zima2LX_Specification |
| #10 | `docs-sync/zima-8` | 1 | AzimuthSuite_manual |
| #11 | `docs-sync/uwave-1` | 8 | uWAVE_Family, uWAVE / Max / Max OEM / USBL Modem specifications, Modems_comparison, wiring diagram, uWave_publications |
| #13 | `docs-sync/uwave-2` | 2 | uWAVE_Protocol_Specification, uWave_technical_passport |
| #12 | `docs-sync/uwave-3` | 2 | uWAVE_FW_Updating, uWAVE/media.md |
| #14 | `docs-sync/redphone-1` | 5 | RedPhone_OS / RedPhone_DX specifications, RedPhone-DX protocol, RedPhone_OS_Users_manual, Phone_T passport |
| #16 | `docs-sync/redphone-2` | 5 | RedPhone_DX_Users_Manual, Phone_S passport, RedPhone_Specification, MDX and MOS specifications |
| #18 | `docs-sync/redphone-3` | 1 | RedPhone_PM |
| #17 | `docs-sync/redphone-4` | 2 | RedPhone_Users_Manual, RedPhone/media.md |
| #15 | `docs-sync/rwlt-1` | 5 | RWLT_Pinger_K, RWLT_GIB, RWLT_RF_Dongle, uNav_protocol_specification, RWLT_tech_pass |
| #19 | `docs-sync/wayu-1` | 7 | WAYU_DataBrief, Pinger, GIB, RF_Dongle, Users_Manual, tech_pass, WAYU/media.md |
| #21 | `docs-sync/redwave-1` | 6 | RedWAVE_DataBrief, RedBASE, RedBASE_old, RedNAV specifications, RedWAVE_Protocol_Specification, RedNAV_Host_Users_Manual |
| #25 | `docs-sync/redwave-2` | 1 | RedWAVE_Users_Manual |
| #24 | `docs-sync/redwave-3` | 2 | uGPSHub_Users_manual, RedNAV_PM |
| #20 | `docs-sync/redwave-4` | 1 | RedWave_tech_pass |
| #22 | `docs-sync/a3s-1` | 3 | A3S_packages, A3T_Datasheet, A3R_Datasheet |
| #23 | `docs-sync/transducers-1` | 5 | RT-1.332820-1, RT-1.524525-1-FF, RT-1.332820-2, RT-2.332820-2, RT-1.524525-2 specifications |
| #26 | `docs-sync/uswitch-1` | 1 | uSwitch_Specification |
| #27 | `docs-sync/accessories-1` | 7 | uPress, uSpeak, uClamp-S (Flange_rod_mound), Sub_batteries, Batpacks, Crimea-300, Crimea-300 OS |

All these PRs passed the controller review of `CLAUDE.md` 8.3. Documents larger than 30 KB of RU source also passed an independent review. CI status is shown on each PR.

Merging notes:
- Every batch appends its own `## Added in batch <slug>` section to `.github/docs-sync/glossary.md`. Merging one PR makes the others conflict in that file. Resolve the conflict by keeping all sections.
- #3 also carries the latest `docsync.py` (heading numbers with NBSP, extensionless links to file names with dots).

## Batch pushed without a PR yet

`docs-sync/f4105-1` (F4105, 3 documents):

| EN file | State |
|---|---|
| `F4105/F4105_DataBrief_en.md` | reviewed and approved |
| `F4105/F4105_tech_pass_en.md` | executor done, mechanical checks pass; controller reading pass pending |
| `F4105/F4105_Users_manual_en.md` | executor done, mechanical checks pass; controller reading pass and independent review (51 KB RU) pending |

Still to do in this batch:
- Align terms across the three files:
  - `стопорная гайка` → lock nut
  - `исполнительное устройство` → actuating device
  - `Стопорный палец` → lock pin (the passport says "Locking pin")
  - `Модуль программирования и передачи команд` (passport) → programming and command transmission unit
- Add the glossary rows (`## Added in batch f4105-1`).
- Open the draft PR.

Facts for the PR description:
- The F4105-SU panel is engraved in Russian (Антенна, Актуатор, Приемник, Зарядка, Запрос, Состояние, Питание, Вкл., Откл., Код 1, Код 2, Программа). EN translates the labels. List `F4105_SU_panel.png` and `F4105_SU.png` under Needs EN image.
- The maximum depth differs between documents: 100 m (data brief, BU specification), 200 m (passport) and 300 m (AU specification).

## Remaining Phase 2 batches (plan in `REPORT.md`)

| Batch | Documents | Prepared |
|---|---|---|
| `misc-1` | RedPhone_OS_MSDS, RedPhone_DX_MSDS (STALE) | briefs generated, not started |
| `misc-2` | WAYU_GIB_MSDS (MISSING), RedBase_v3_LiFEPO4_msds (STALE) | briefs generated, not started |
| `redline-1` | RedLine_Specification, RedLINE_Protocol_Specifications, RedLINE_wiring_diagram (all STALE) | briefs generated, not started |
| `a3s-2` | A3S_Users_Manual (MISSING, 146 KB) | not started; translate in parts, independent review |

Approach for the MSDS batches:
- The four RU MSDS files are one template, 95–97 % identical.
- Fully re-translate `RedPhone_OS_MSDS` first. Use the canonical GHS/REACH 16-section headings from the glossary. The existing EN files are weak machine translations: old legal name, "Fax machine", "is absent", Cyrillic left in.
- Derive the other three files from the approved OS file plus the RU differences.
- The supplier block uses `UCNL LLC`.
- The RedLine documents use the product name `RedLine`. The wiring diagram has an EN image variant (`RedLINE_wiring_diagram_en.png`).

## Resuming

1. Read `CLAUDE.md`, `REPORT.md`, this file, and the descriptions of the open PRs.
2. Recreate the working files in a scratchpad `$S`:
   - `.github/docs-sync/executor_rules.md` (this branch) → `$S/common_rules.md`. Adjust the scratchpad path in its first lines.
   - `.github/docs-sync/glossary_all_batches.md` (this branch) → `$S/ref/glossary_current.md`. It is the union of `glossary.md` and all `## Added in batch …` sections of the open PRs.
   - `.github/docs-sync/docsync.py` from `origin/docs-sync/zima-1` → `$S/docsync.py`.
   - Approved sibling EN files for reuse: `git show origin/docs-sync/<batch>:documentation/EN/<Family>/<file>` → `$S/ref/`.
3. One git worktree per batch, created from `origin/master` (`git worktree add -b docs-sync/<slug> $S/wt-<slug> origin/master`).
4. Per document:
   - `python3 $S/docsync.py brief <RU path> <all RU paths of the batch>` gives the facts block (links, image variants, counts, marker).
   - Write a prompt `$S/<batch>/p_<doc>.md` with the worktree, RU/EN paths, status, breadcrumb, reference files and the facts block.
   - Spawn `docs-translator` (up to 4 in parallel) with "read the brief file and follow it".
5. Review each result:
   - Run `python3 $S/docsync.py check <RU> <EN>`.
   - Read RU and EN side by side, line by line.
   - Fix small issues directly.
   - Commit one document per commit (`docs-sync: add|update <EN path>`) and push after each document.
6. Close each batch:
   - Append the glossary rows, both to `glossary.md` in the branch and to `$S/ref/glossary_current.md`.
   - Open a draft PR with the section 11 template.
7. After all batch PRs are merged: Phase 3, then Phase 4 (`CLAUDE.md` sections 9–10).

Items already known for Phase 3:
- Deferred RU links, e.g. RedWave user's manual Figure 9 → RedBASE_old.
- The `RWLT_RF_Dongle` link name.
- The F4105 index entries ("awakening" → wake-up).
- The Batpacks index title.

Items already known for Phase 4:
- Glossary `CONFLICT` rows, e.g. anchor rope / anchor line.
- Beam-angle `(3 dB)` wording in the transducer specifications that were not in a batch.
- Cyrillic residue in the existing EN MSDS files.
