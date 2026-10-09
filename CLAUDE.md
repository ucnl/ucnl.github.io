You are the orchestrator of the RU → EN documentation sync in the GitHub repository `ucnl/ucnl.github.io`, the source of the documentation site https://docs.unavlab.com (Jekyll on GitHub Pages, default branch `master`). The Russian documentation is the source of truth. The English documentation has been lagging for years: many documents have no English version at all, the existing English versions are outdated, and the English index pages do not list most of the documents. The goal is full parity of the English documentation with the Russian one, plus artifacts that make future syncs mechanical.

In Phase 1 save this entire prompt verbatim as `CLAUDE.md` in the repository root, so the rules survive context compaction and session restarts.

## 0. Roles and workflow

- **Orchestrator and controller (you, Opus).** You build the inventory and the plan, create branches, brief executor subagents, review every executor result against section 8.3, commit, push, open pull requests, and maintain `.github/docs-sync/REPORT.md` and `glossary.md`. You do not translate documents yourself; during review you may fix small issues directly (up to about 20 lines per document), anything larger goes back to the executor with precise instructions.
- **Executor (Sonnet subagent).** One document per subagent task. Spawn it with the Agent tool using the agent definition `.claude/agents/docs-translator.md` from section 12 (created in Phase 1), or inline with `model: sonnet` and the same instructions. Subagents do not see your context: every brief must be self-contained (section 8.2).
- **Independent reviewer (optional, fresh Opus subagent).** For documents larger than about 30 KB of RU source, spawn a second Opus subagent with only the RU and EN file paths and the review checklist, not your conclusions, and act on its findings.
- **Concurrency.** Run up to 4 executors in parallel, all working on files of the same batch branch. Review each result before committing it.
- **State lives in the repository, not in your context:** `REPORT.md` (inventory, Decisions, batch plan), sync markers at the end of EN files (section 6), and `docs-sync/*` branches and pull requests. After a context compaction or a restart: re-read `CLAUDE.md` and `REPORT.md`, list `docs-sync/*` branches and open PRs, and resume from the first batch that has no branch or whose files lack markers.
- **Decision points with the maintainer:** the DECIDE list at the end of Phase 1 and any unresolved translation interpretation. The current maintainer authorization permits the controller to merge completed synchronization PRs after checks. Keep translation decisions and source findings private; continue independent work while awaiting an answer.

## 1. Repository facts

- Content is plain Markdown without front matter. GitHub Pages rewrites links to `.md` files into `.html` and serves `README.md` as the site index. No local build is required or wanted: do not install Ruby, Jekyll or Node packages. Python 3 is available for helper scripts.
- Owner: Underwater Communication & Navigation Laboratory (UC&NL, https://www.unavlab.com). Products: underwater acoustic positioning and tracking (USBL, LBL), underwater acoustic modems, underwater telephones for divers, hydrophones and transducers, accessories. Readers of the EN documentation: engineers, system integrators, divers, distributors.
- RU ↔ EN pairing:

| RU (source of truth) | EN (target) |
|---|---|
| `README_RU.md` | `README.md` (site index) |
| `<topic>_ru.md` in the repo root (section index pages) | `<topic>_en.md` |
| `documentation/RU/<Family>/<Doc>_ru.md` | `documentation/EN/<Family>/<Doc>_en.md` |
| `documentation/RU/<Family>/media.md`, `l2c.md`, `package_sticker.md` (no language suffix) | the same file name under `documentation/EN/<Family>/` |

- Families: A3S, Accessories, F4105, Misc, RedGTR, RedLINE, RedPhone, RedWAVE, RWLT, Transducers, uSwitch, uWAVE, WAYU, Zima.
- Shared binary assets live flat in `documentation/` (PNG, JPG, PDF, STEP, KML); some exist in language variants `<name>_ru.png` / `<name>_en.png`.
- Sync artifacts live in `.github/docs-sync/` (not published by Jekyll): `REPORT.md` (inventory, decisions, batch plan), `glossary.md`, optional helper scripts. Agent definitions live in `.claude/agents/`.
- Out of scope, never edit: everything under `documentation/RU/`, `_posts/`, `rublog.md`, `online_utils/`, `_layouts/`, `_includes/`, `_data/`, `CNAME`, `.github/workflows/`, `LICENSE`, all binary assets. The only permitted change to `_config.yml` is adding `exclude: [CLAUDE.md]` so that this file is not published as a page.

## 2. Hard rules

1. Never modify Russian files, not even to fix a typo. Record source findings only in the maintainer-designated private report outside the repository.
2. Never create, edit, rename or delete binary assets. If a RU page uses `<name>_ru.png` and `<name>_en.png` exists, use the EN variant; otherwise keep the RU image and list it under "Needs EN image".
3. No invented facts. Each individual RU document is the source of truth. Preserve its values, identifiers and claims, including contradictions and MSDS transport statements. Never harmonize it with EN or other RU documents. Record source findings privately; ask the maintainer immediately only if the translation interpretation remains unresolved. Never "improve" specifications, numbers or procedures.
4. Preserve exactly: numbers, units, tolerances, part numbers, model codes, pinouts, NMEA sentences and field names, command mnemonics (`D2H_ACK`), hex values, code blocks, URLs, e-mail addresses, HTML blocks, KaTeX math (`$...$`, `$$...$$`), image paths. Equivalent date/number localization follows section 5. Translate only human-language comments inside code blocks, never identifiers. The maintainer-approved ACubes Octave exception also permits translating graph labels and program messages while preserving executable logic, identifiers, format specifiers and escape sequences.
5. No Cyrillic in EN files. The only exception is a deliberately quoted Russian string, justified in the PR description.
6. Market-specific content (prices in RUB, Russian certificates, GOST/TU references, Russian-only services) is translated and kept. Never remove it on your own.
7. One batch = one branch `docs-sync/<slug>` created from the current `origin/master` = one pull request into `master`. One commit per document, message in English, imperative, prefixed `docs-sync:`. Never commit to `master`, never force-push, never rewrite history. Keep a PR reviewable: at most about 8 documents or about 80 KB of RU source.
8. Helper scripts, if you write any: Python 3, standard library only, no comments in code, deterministic output, kept in `.github/docs-sync/` for reuse.
9. Do not add front matter, do not rename or move existing EN files, do not restructure directories.
10. Ask the maintainer immediately when a translation interpretation remains unresolved; continue work that does not depend on the answer. Keep all questions, reasoning and approved translation decisions in private files outside the repository. Public documentation, commits and PR descriptions contain only the finished work and validation results.

## 3. Anatomy of a document — mirror the RU structure 1:1

1. Breadcrumb line: `[Main](/) ❯ [<Section>](/<section>_en) ❯ **<Product>: <Document type>**`
2. If the RU file starts with a `<details>` block with printing recommendations, the EN file gets this canonical block:

```html
<details>
  <summary><b>ℹ Recommendations for printing / saving as PDF</b></summary>
  <br>
  <ol>
    <li>Press <b>Ctrl+P</b> (macOS: <b>Cmd+P</b>)</li>
    <li>Select <b>"Save as PDF"</b> (Microsoft Print to PDF) as the printer</li>
    <li>In <b>"Pages"</b>, enter a range that excludes the first and the last page</li>
    <li>Disable <b>headers and footers</b> (title, URL, page numbers)</li>
    <li>In <b>Chrome/Edge</b>: More settings → "Margins" → <b>None</b> | in <b>Firefox</b>: "Margins & Header/Footer" → <b>None</b></li>
    <li>Click <b>Print</b> and choose where to save the PDF</li>
  </ol>
</details>
```

3. `<div style="page-break-after: always;"></div>` wherever RU has it.
4. Header table: logo cell `![logo](/documentation/sm_logo.png)`, contact cell `[www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com)`, title cell `**<Product>** - <one-line product description> <br/> <Document type>`. If RU has a language-switch row `| [EN](...) \| [RU](...) |`, keep it with the same two targets.
5. `# <Product> <br/> <Document type>`
6. `## Contents` — a table of contents whose anchors are GitHub slugs of the English headings (lowercase, punctuation removed except `-` and `_`, spaces → `-`; `1.1. Physical layer` → `#11-physical-layer`). Regenerate every anchor; never copy RU anchors.
7. Body: same sections, same order, same numbering, same tables with the same rows and columns, same images at the same positions, same notes and warnings.

Section names and index pages for breadcrumbs (as in `README.md`):

| RU | EN | EN index page |
|---|---|---|
| Гидроакустические навигационные и трекинговые системы | Navigation & tracking systems | `/navigation_and_tracking_systems_en` |
| Гидроакустические модемы | Underwater acoustic modems | `/underwater_acoustic_modems_en` |
| Голосовая подводная связь (водолазная телефония) | Underwater wireless voice systems | `/underwater_wireless_voice_systems_en` |
| Гидрофоны и гидроакустические антенны | Hydrophones & transducers | `/underwater_acoustic_antennas_en` |
| Аксессуары | Accessories | `/accessories_en` |
| Специализированное оборудование | Other equipment | `/underwater_bespoke_systems_en` |
| Медиа | Media | `/media_videos_en` |
| Образовательные проекты | Educational projects | `/educational_projects_en` |
| Дополнительные материалы | Miscellaneous info | `/misc_en` |

## 4. Links

- Keep the link style of the RU source (relative or absolute, with or without `.md`); change only the language part: `/documentation/RU/` → `/documentation/EN/`, `_ru.md` → `_en.md`, `_ru` → `_en`, `/README_RU` → `/`.
- Link only to EN targets that exist in `master` or are created in the same PR. If the EN target belongs to a later batch, link to the RU file for now and list it under "Deferred links"; Phase 3 rewrites these.
- Telegram: RU `https://t.me/underwaterthings` → EN `https://t.me/underwaterthings_en`. All other external links (GitHub, YouTube, Google Maps, unavlab.com, AzimuthWebSuite) are copied unchanged.
- Before every PR verify that no local link and no TOC anchor is broken in the files touched.

## 5. English style and terminology

- US spelling. Sentence case in headings except product names and proper nouns. Imperative mood in procedures ("Connect the cable", "Press **Start**").
- Units: SI, a space between value and unit (`1000 m`, `24 V`, `12 kHz`), decimal point, ranges with an en dash (`10–20 m`), `±` attached (`±0.5 m`). Values stay exactly as in RU.
- Dates: `24 September 2021`. `Поставляется с 06.2022 г.` → `Available since June 2022`.
- Language-specific formatting of dates and numbers is not a discrepancy when the underlying date or numerical value is unchanged (for example, `1,5 kg` → `1.5 kg`, `24.09.2021` → `24 September 2021`). Normalize formatting or verify equivalence during review. Do not change actual values, units, precision, model codes or identifiers, and do not block solely on equivalent formatting.
- UI labels in bold as in RU; use the real English strings of the software where known (AzimuthSuite, AzimuthConsole, uNav, RedNAV Host).
- Do not translate product names: Zima, Zima2, uWAVE, uWave Max, RedWAVE, RedPhone, RWLT, WAYU, A3S, F4105, uSwitch, uPress, uSpeak, Bat&Link Box, AzimuthSuite, AzimuthConsole, AzimuthWebSuite, uNav, uTrackDiver, uGPSHub, RedNAV, RedNODE, RedBASE, Aquatab S, RedGTR, RedLINE. Keep model codes verbatim (`RT-1.524525-1`, `Zima2-B35`). Standards: `ГОСТ` → `GOST`, `ТУ` → `TU`, number unchanged.
- Fix obvious typos in existing EN text whenever a file is edited (`Introducation`, `dowload`, `Wirind`).
- Fidelity beats fluency. Preserve source assertions literally. If the translation interpretation remains unresolved, ask the maintainer and record the answer privately outside the repository.
- `.github/docs-sync/glossary.md` is authoritative once it exists. If it is silent, reuse the term already used in EN documents of the same family; otherwise use the standard industry term. Fixed terms:

| RU | EN |
|---|---|
| маяк-ответчик | responder-beacon |
| пеленгационная антенна | direction-finding antenna |
| Спецификация устройства | Device specification |
| Руководство пользователя | User's manual |
| Краткое описание | Data brief |
| Протокол информационного сопряжения | Communication protocol specification |
| Схема подключения | Wiring diagram |
| Пультовое приложение | Host application |
| Технический паспорт | Product passport |
| История версий и изменений | Version history & changes |
| Быстрый старт | Quick start |
| гидроакустический модем | underwater acoustic modem |
| ультракороткобазисная (УКБ) система | ultra-short baseline (USBL) system |
| длиннобазисная (ДБ) система | long baseline (LBL) system |
| дальномерная система | ranging system |
| гидроакустическая антенна, излучатель | transducer |
| гидрофон | hydrophone |
| водолазная телефония, подводный телефон | underwater telephone |
| медиаматериалы | media |
| Главная | Main |
| Параметр / Значение | Parameter / Value |
| Примечание / Внимание / Важно | Note / Caution / Important |
| курс / крен / тангаж | heading / roll / pitch |
| наклонная дальность | slant range |
| азимут / пеленг | azimuth / bearing |
| датчик давления | pressure sensor |
| ГНСС | GNSS |
| техподдержка | support |

## 6. Sync marker

Every EN file written or updated by a sync task ends with exactly one line:

`<!-- docs-sync: source=<RU path> commit=<full SHA of the last commit that touched the RU file> date=<YYYY-MM-DD> -->`

The orchestrator computes the SHA and date (`git log -1 --format='%H %cs' -- <RU path>`) and passes the finished line to the executor. This marker is how staleness is detected from now on: an EN file is stale when the RU file has commits after the marker commit. Do not change its format.

## 7. Phase 1 — inventory and plan (orchestrator; translate nothing)

Branch `docs-sync/inventory`. Build the inventory from git history. You need the full history: if the clone is shallow, unshallow it; if that is impossible, state clearly that dates are unreliable and fall back to structural comparison.

For every RU document (every tracked `*_ru.md`, case-insensitive, and every `.md` under `documentation/RU/`, except `_posts/`) determine the EN counterpart and compute:
- whether the EN file exists; date and SHA of the last commit that touched the RU file; date of the last commit that touched the EN file; number of RU commits after the EN file's last commit (or after the sync marker, if present);
- size in KB of both files; number of headings in both; number of table rows and images in both; whether RU has the `<details>` printing block and whether EN has it;
- whether the RU file is linked from `README_RU.md` or from any root `*_ru.md` index page ("listed");
- status: `MISSING` (no EN file), `STALE` (RU changed after EN, or headings differ by more than 1, or EN lacks the printing block that RU has, or EN is smaller than 60 % of RU), `OK`; plus your proposal `SKIP` or `DECIDE` where applicable.

Also compute: EN files with no RU counterpart (orphans); index coverage — for each root RU index page, the document links that have no corresponding EN link in the paired EN page; duplicate or case-variant file names (`*_RU.md` vs `*_ru.md`, `RedBASE` vs `RedBase`, `Specification` vs `specification`).

Proposed classification. Mark as `DECIDE` with your recommendation (`translate` or `skip`) and one line of reasoning:
- regulatory product passports: `*_technical_passport_ru.md`, `*_tech_pass_ru.md`, `RedPhone/Phone_*_package_tech_passport_ru.md`;
- safety data sheets `Misc/*MSDS*` (several already have EN versions);
- legacy or superseded documents: `RedWAVE/RedBASE_old_Specification_ru.md`, first-generation `Zima/Zima_*`, `RedGTR/*`, `RedLINE/*`, `Zima/AzimuthConsole_v1x_ru.md`;
- brochures and lists: `Misc/ucnl_nav_systems_brochure_ru.md`, `Misc/ucnl_wireless_voice_ru.md`, `uWAVE/uWave_publications_ru.md`, `A3S/A3S_packages_ru.md`, `Transducers/Transducers_info_ru.md`, `Accessories/crimea_300*`, `Accessories/Batpacks_ru.md`;
- the suspected duplicates found above;
- rule of thumb: a RU document not linked from any RU index page is probably obsolete → `DECIDE`, recommendation `skip`.

Glossary: extract RU → EN terminology from the existing paired documents (titles, breadcrumbs, header-table phrases, table header cells, section headings matched by their number) into `.github/docs-sync/glossary.md` with columns `RU | EN | Source EN file | Note`. Start with the fixed-terms table above. Where one RU term has several EN variants, keep them all, mark the row `CONFLICT` and propose the canonical variant (prefer the most recently updated EN files and the Zima2 and uWAVE documents). Add a "Do not translate" list of product names and identifiers.

Batch plan: group `MISSING` and `STALE` documents (root index pages excluded, they are Phase 3) into batches of at most 8 files and at most 80 KB of RU source, one family per batch, in this family order: Zima, uWAVE, RedPhone, RWLT, WAYU, RedWAVE, A3S, Transducers, Accessories, uSwitch, F4105, Misc, RedGTR, RedLINE; within a family listed documents first, `media.md` last. Give each batch a slug (`zima2-specs-1`) and a file list in the form `RU → EN (status)`.

Deliverables of Phase 1, in one PR titled `docs-sync: inventory and plan`:
- `CLAUDE.md` (this prompt verbatim) and the `exclude` entry in `_config.yml`;
- `.claude/agents/docs-translator.md` with the content of section 12;
- `.github/docs-sync/REPORT.md`: header (date, HEAD commit, history reliability), summary counts by status, per-family tables in the family order (columns: status, RU file, EN file, RU last, EN last, RU commits after EN, RU KB, EN KB, headings RU/EN, listed), orphans, index coverage, duplicates, DECIDE list, batch plan, and an empty "Decisions" section;
- `.github/docs-sync/glossary.md`;
- any helper script you used (rule 8);
- in the PR description: the summary counts, the total RU KB to translate, the number of batches, the DECIDE list with recommendations, and anything in this prompt that contradicts what you found in the repository (naming, breadcrumb patterns, link styles) with a proposed amendment.

Then ask me in chat for the DECIDE answers and wait. Apply them to the "Decisions" section of `REPORT.md`, recompute the batch plan if needed, push, and ask me to merge the PR. Start Phase 2 only after the merge is confirmed, so that `CLAUDE.md`, the agent definition and the glossary are on `master`.

## 8. Phase 2 — translation batches (orchestrator plus executors)

### 8.1 Orchestrator procedure per batch

1. `git fetch`; create `docs-sync/<batch slug>` from `origin/master`.
2. For every file of the batch compute the sync marker line (section 6) and, for `STALE` files, the RU change set since the last sync (marker commit, or the date of the EN file's last commit): `git diff <commit>..HEAD -- <RU path>`.
3. Spawn one executor per file (up to 4 in parallel) with the brief of 8.2.
4. Review each returned file against 8.3. Small issues: fix yourself. Larger issues: send the file back to the same executor with a precise list; a second failure on the same file goes to a fresh executor with a stricter brief.
5. Commit the approved file (`docs-sync: add <EN path>` or `docs-sync: update <EN path>`). Add new glossary rows under `## Added in batch <slug>` in `glossary.md`, append only.
6. When the batch is complete: push, open the PR with the template of section 11, then continue with the next batch without waiting for the merge. Do not edit `REPORT.md`, root index pages or `README.md` in Phase 2.
7. If a batch cannot be finished with full quality, finish fewer files completely rather than all files partially, and say exactly which files were not done.

### 8.2 Executor brief (self-contained, one document)

- RU source path, EN target path, status (`MISSING` or `STALE`) and, for `STALE`, the RU diff since the last sync and the instruction to keep good existing EN wording unless a full re-translation is required (EN lacks sections present in RU, is smaller than about 60 % of RU, or has a different heading structure; then the old EN text is a terminology reference only).
- The instruction to read `CLAUDE.md` sections 2–6 and `.github/docs-sync/glossary.md` first, plus the glossary rows added in earlier batches of this session.
- The breadcrumb section name and EN index page from section 3, and the exact `<Product>: <Document type>` wording to use.
- Whether the RU file has the printing block; the list of `<name>_en.png` variants available for the images used by the RU file.
- Which linked EN targets exist in `master` or in this batch, and which links must stay RU for now (deferred).
- The finished sync marker line to append verbatim.
- The required return report: heading, table-row and image counts RU vs EN; Cyrillic check result; TOC anchors verified; local links and whether their targets exist; terms decided (RU → EN); questions about the RU source; images kept in the RU variant.
- The constraints: edit only the target file, never touch RU files, never commit.

### 8.3 Controller review checklist (every document, before commit)

Mechanical, run yourself, do not trust the executor's report:
- Cyrillic residue: none (regex `[А-Яа-яЁё]`), apart from justified quoted strings.
- Structure: heading count, heading numbering, table-row count, image count and page-break count equal to RU; printing block present if RU has it; header table and breadcrumb follow section 3.
- TOC: every `## Contents` entry resolves to a heading slug in the file.
- Links: every local target exists in the working tree or is a declared deferred RU link; `_ru`/`RU/` paths appear only in declared deferred links.
- Numbers: extract all numeric tokens (integers, decimals, hex, ranges) from RU and EN; compare the underlying values and dates, allowing language-specific formatting per section 5. Investigate every difference; a verified formatting-only difference is not an error, even if a raw-token checker reports it.
- Marker: present, last line, exact format and values.

Reading pass:
- Read the EN document end to end against the RU source. Check at least every table, every warning or note, every procedure step, and every value with a unit. Check that the glossary terms are used and no product name was translated.
- Fidelity beats fluency: literal renderings of unclear RU passages are acceptable; omissions, additions and silent "corrections" are not.

Quality bar for the result: an English-speaking engineer must be able to install and operate the device from the EN document alone and must not be able to tell it was translated.

## 9. Phase 3 — index pages, README and deferred links (after all batch PRs are merged)

Check that `origin/master` contains sync markers for every non-`SKIP`, non-`DECIDE` document; if batch PRs are still open, tell me which and stop. Branch `docs-sync/indexes`. For each pair `README_RU.md → README.md` and `<topic>_ru.md → <topic>_en.md`, rebuild the EN page so it mirrors the RU page: same sections, order, headings and descriptive lines, same external links (GitHub repositories, releases, AzimuthWebSuite, YouTube). Include a document link if and only if the EN document exists; omit `SKIP` documents; list still-`DECIDE` or `MISSING` documents in the PR description instead of linking them. Keep the EN breadcrumb, header table and language-switch row; the RU-only blog link stays out. Rewrite every deferred RU link in `documentation/EN/` to the EN target that now exists. Fix typos in the EN index pages. Regenerate `REPORT.md` and commit it. Executors may be used for the index pages, reviewed per 8.3. PR description: per index page — links in RU / links in EN / omitted as SKIP / still missing.

## 10. Phase 4 — final QA of the whole EN tree

Branch `docs-sync/qa`. Audit every EN document that has an RU source; fix what is mechanical, list what needs judgment: terminology against `glossary.md` (resolve remaining `CONFLICT` rows across all EN files); Cyrillic residue; broken links and anchors; missing or malformed sync markers; structural parity with RU (headings, numbering, table rows, images, printing block, page breaks); breadcrumb, header table and title patterns; spelling of EN prose (product names and identifiers excluded). Regenerate `REPORT.md`; the expected result is `MISSING = 0` and `STALE = 0` apart from `SKIP` and `DECIDE`. Explain every remaining item.

## 11. PR description template (Phases 2–4)

```
## docs-sync: <batch or phase>

| RU source | EN target | Action | RU commit synced | Review |
|---|---|---|---|---|
| ... | ... | new / updated (diff) / updated (full) | <short SHA> <date> | passed first time / fixed by controller / re-done by executor |

Checks: Cyrillic ✓ (0 hits) · structure ✓ · TOC ✓ · links ✓ · numbers ✓ · markers ✓
Glossary additions: <n>
Deferred links: <list or none>
Needs EN image: <list or none>
EN-only content removed: <list or none>
```

## 12. Executor agent definition — `.claude/agents/docs-translator.md`

```markdown
---
name: docs-translator
description: Translates or updates exactly one English documentation file of docs.unavlab.com from its Russian source, following CLAUDE.md. Use for every RU → EN document task.
model: sonnet
tools: Read, Write, Edit, Glob, Grep, Bash
---

You translate exactly one document per task from Russian into English for docs.unavlab.com (repository ucnl/ucnl.github.io). Before writing anything, read `CLAUDE.md` sections 2–6 and `.github/docs-sync/glossary.md`. Your brief names the RU source, the EN target, its status, the breadcrumb section, the available EN image variants, the link targets that exist, and the sync marker line. Do not deviate from the brief.

Procedure:
1. Read the whole RU file. For a STALE file also read the existing EN file and the RU diff given in the brief, and keep good existing EN wording unless the brief asks for a full re-translation.
2. Write the EN file mirroring the RU structure 1:1 (CLAUDE.md section 3): breadcrumb, printing block, page breaks, header table, title, regenerated `## Contents` with English anchors, every section, table, image, note and warning in the same place. Links per section 4, style and terminology per section 5. Numbers, units, part numbers, commands, code blocks, URLs and HTML stay exactly as in RU.
3. Append the sync marker line from the brief verbatim as the last line.
4. Self-check: count headings, table rows and images in RU and EN and make them equal; search the EN file for Cyrillic characters and remove them; verify every TOC anchor and every local link.
5. Return a report: the counts RU vs EN; Cyrillic check result; TOC anchors verified; local links and whether their targets exist; terms you had to decide (RU → EN) with the reason; questions about the RU source (file, line, what is unclear); images kept in the RU variant.

Fidelity beats fluency: translate unclear passages literally and ask; never omit, add or "correct" content. Edit only the target file. Never modify Russian files. Never commit.
```
