# docs-sync: current state

State on 2026-10-09. Master HEAD: `ee5bf833e0ca57c04c48c22d923bbefc3446d8fc` (all Phase 2 batches, repository rules and Phase 3 merged).

This branch (`docs-sync/state`) is a progress record and is not intended for merge.

## Phases

| Phase | Status |
|---|---|
| 1. Inventory and plan | Completed and merged (#2) |
| 2. Translation batches | 30 of 30 batches merged; 107 EN documents |
| 3. Index pages, README and deferred links | Completed and merged (#36): 13 root pages, 29 deferred links in 8 documents |
| 4. Final QA | In progress on docs-sync/qa: 27 legacy documents and whole-tree validation |

## Batch pull requests

All batch PRs below are merged into master. Each document passed the controller review and current mechanical checks. RU sources larger than 30 KB also received an independent line-by-line review.

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
| #31 | `docs-sync/f4105-1` | 3 | F4105_DataBrief, F4105_tech_pass, F4105_Users_manual |
| #32 | `docs-sync/redline-1` | 3 | RedLine_Specification, RedLINE_Protocol_Specifications, RedLINE_wiring_diagram |
| #33 | `docs-sync/misc-1` | 2 | RedPhone_OS_MSDS, RedPhone_DX_MSDS |
| #34 | `docs-sync/misc-2` | 2 | WAYU_GIB_MSDS, RedBase_v3_LiFEPO4_msds |
| #35 | `docs-sync/a3s-2` | 1 | A3S_Users_Manual |

## Repository instructions

Merged PR #30 (`docs-sync/agents-md`) adds AGENTS.md, the corresponding Jekyll exclusion, Codex translator/reviewer definitions, and the approved date/number localization rule in AGENTS.md and CLAUDE.md.

## Remaining Phase 2 work

All 30 translation batches are complete and merged. Progress PR #28 is closed; this branch remains available as a state record.

## Resuming

1. Read CLAUDE.md, the approved executor rules, the full glossary and the maintainer's latest instructions.
2. Fetch origin and inspect the current PR and branch state.
3. Continue the remaining batch work, if any, with one document per commit and push after each reviewed document.
4. Keep all `Added in batch` glossary sections when merging master into batch branches; do not rebase or rewrite history.
5. Start Phase 3 only after all batch PRs are merged. Then update indexes, README and deferred links, and perform Phase 4 QA.

The complete glossary through the completed batches is stored in `glossary_all_batches.md`. The latest checker, executor rules and complete glossary are on master.
