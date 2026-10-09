# Common rules for every RU → EN sync task (docs.unavlab.com)

Repository: `/home/user/ucnl.github.io`. The batch branch named in your brief is already checked out — do not switch branches, do not commit, do not touch any file except your EN target. Never edit RU files.

Scratchpad with reference files: `/tmp/claude-0/-home-user-ucnl-github-io/79387ef7-0970-58eb-92b2-d74054cfd9f4/scratchpad/` (below: `$S`).

## Read first, in full

1. `CLAUDE.md` sections 2–6 (hard rules, document anatomy, links, style and terminology, sync marker).
2. `$S/ref/glossary_current.md` — the authoritative glossary including the rows added in earlier batches (section `## Added in batch …` at the end). Use the **bold** canonical variant of every CONFLICT row. Follow its "How to use" rules: ALL CAPS mirroring, `MAXIMUM` spelled out (not `MAX.`) unless RU abbreviates, `underwater acoustic` (never `hydroacoustic`), Cyrillic look-alikes. The product name case rule below overrides the glossary's older "keep the RU spelling" wording.
3. The reference EN files named in your brief (latest approved translations of sibling documents): reuse their wording for identical RU passages so that sibling documents read the same.

## Amendments to CLAUDE.md section 3 approved for this sync (they override section 3 where they differ)

- **Header table:** mirror the RU header table cell by cell. RU specifications use a 2 × 2 table: `| ![logo](/documentation/sm_logo.png) | <product image> |`, `| :---: | ---: |`, `| [www.unavlab.com](https://www.unavlab.com/) <br/> [support@unavlab.com](mailto:support@unavlab.com) | <title cell> |`. Keep the same images and column layout; translate only the title cell text (pattern: `**<Product>** - <one-line description> <br/> Device specification`).
- **H1 title and `## Contents`:** only where RU has them. TOC entries are regenerated as same-page anchors of the EN headings (GitHub slugs: lowercase, punctuation removed except `-` and `_`, spaces → `-`). Never copy RU percent-encoded anchors.
- **Heading case:** where RU writes a heading or table label in ALL CAPS, EN keeps ALL CAPS; elsewhere sentence case. Keep the RU heading numbering exactly.
- **Breadcrumb:** exactly the line given in your brief.
- **Printing block:** if RU has the `<details>` printing block, use the canonical EN block from CLAUDE.md section 3.2 verbatim, same position. `<div style="page-break-after: always;"></div>` exactly where RU has it.
- **Links:** keep the RU link style (relative/absolute, `.md`/`.html`/no extension, anchors) and change only the language part (`/documentation/RU/` → `/documentation/EN/`, `_ru.md` → `_en.md`, `_ru.html` → `_en.html`, `_ru` → `_en`, `/README_RU` → `/`). Absolute links to `https://docs.unavlab.com/documentation/RU/…` are local links too: rewrite them the same way (keep the absolute form) when the EN target exists. Links your brief lists as **deferred** must keep pointing to the RU document; only their link text is translated. If the RU link is relative (e.g. `Zima2LX_Specification_ru.md` or `../RWLT/x_ru.md`), rewrite it to the absolute RU path (`/documentation/RU/Zima/Zima2LX_Specification_ru.md`), because a relative link copied into `documentation/EN/` would point to a non-existent file; absolute RU links stay as they are. Images, PDFs, STEP files and external links are copied unchanged.
- **Cyrillic image placeholders:** an image whose target is a Cyrillic word (e.g. `![zima2_sl](ОЖИДАЕТСЯ)`) gets the target `PENDING` (e.g. `![zima2_sl](PENDING)`); report it under "Needs EN image".
- **Footnote anchors** (`<a name="footnote1">`, `[1](#footnote1)`) and other HTML anchors and HTML comments are kept exactly (translate human text inside HTML comments).
- **Cyrillic look-alikes are errors:** `°С` (Cyrillic С) → `°C`, Cyrillic `х` as a multiplication sign → `x`, `Ф` as a diameter sign → `Ø`. The final EN file must contain zero characters matching `[А-Яа-яЁё]`.
- **Numbers:** every number, unit value, tolerance, range, model code and identifier stays exactly as in RU (fix EN values that differ from RU). Unit symbols become SI/English (`мм` → `mm`, `Вт` → `W`, `мсек` → `ms`, `бит/с` → `bit/s`, `дБ` → `dB`, `мкПа` → `μPa`); keep `+/-` and `..` ranges exactly as RU writes them in tables.
- **RU typos** are translated as the intended word and reported as questions.
- **Product name case (maintainer decision, overrides any older rule):** in EN text product names are always mixed case — `uWave`, `uWave Max`, `uWave Max OEM`, `uWave USBL Modem`, `RedWave`, `RedBase`, `RedNode`, `RedNav`, `RedLine`, `Zima`, `Zima-B` — never `uWAVE`, `RedWAVE`, `RedBASE`, `RedNODE`, `RedNAV`, `RedLINE`, `ZIMA`, even where RU writes capitals (running text, link texts, breadcrumb, H1, header cells). Acronyms stay (`RWLT`, `WAYU`, `A3S`, `F4105`, `RedGTR`, `GIB`). Never change file/directory names, link targets, URLs, image paths, code blocks or identifiers (`uWAVE_ALib`, `uWAVELib`, `RedBASE_Config`). Labels RU writes entirely in ALL CAPS stay ALL CAPS. `docsync.py check` reports violations as `product name case`.
- **STALE documents:** for a diff-based update keep good existing EN wording, but compare the whole RU with the whole EN and fix every discrepancy (missing or extra rows, sentences, footnotes; wrong values; untranslated words; non-canonical glossary terms; typos), not only the lines in the RU diff. For a full re-translation, overwrite the file; the old EN text is a terminology reference only.

## Self-check (mandatory)

Run from the repository root:
`python3 $S/docsync.py check <RU path> <EN path>`
and fix everything it reports until it prints `ALL CHECKS PASSED`. The only acceptable remaining lines are `RU link, must be a declared deferred link: …` for links your brief lists as deferred; justify anything else in your report.

## Return report (plain text, concise)

What you changed (for STALE files) or created; counts RU vs EN (headings, table rows, images, page breaks); Cyrillic check result; every local link with its target, whether it exists, and which links you left as deferred RU links; terms you decided that are not in the glossary (RU → EN, reason); questions about the RU source (line number, what is unclear); images kept in the RU variant / needing an EN image; the final output of the `check` command.

Fidelity beats fluency: never omit, add or "correct" content; translate unclear passages literally and ask. Quality bar: an English-speaking engineer must be able to install and operate the device from the EN document alone and must not be able to tell it was translated.
