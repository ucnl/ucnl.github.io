# AGENTS.md

This repository is the source of https://docs.unavlab.com. Its documentation is being synchronized RU → EN under a fixed procedure.

1. Read `CLAUDE.md` in full before any work. It is the governing procedure for every agent, not only Claude: hard rules, document anatomy, links, style and terminology, sync markers, batches, review checklist and PR template.
2. Then read `.github/docs-sync/executor_rules.md` (approved amendments to the translation rules), `.github/docs-sync/glossary.md` (authoritative terminology) and `.github/docs-sync/REPORT.md` (inventory, maintainer decisions, batch plan). The checker is `.github/docs-sync/docsync.py` (`brief`, `check`, `marker`; never run it without arguments).
3. Roles of `CLAUDE.md` section 0:
   - An agent that supports subagents defines them in its own agent-definition format, analogous to `.claude/agents/docs-translator.md`. It needs an executor (one document per task) and an independent reviewer for RU sources over 30 KB. It then works as orchestrator and controller.
   - An agent without subagents performs the roles itself, in separate passes. It translates one document per the executor brief (section 8.2). It then reviews it against the controller checklist (section 8.3) as if someone else had written it. For RU sources over 30 KB it adds a third, independent line-by-line pass.
   - In both cases: one document per commit.
4. Maintainer decisions:
   - all DECIDE recommendations in `REPORT.md` are accepted;
   - the English legal name is UCNL LLC;
   - product names are always written in mixed case in EN text: uWave, uWave Max, RedWave, RedBase, RedNode, RedNav, RedLine, Zima;
   - never write uWAVE, RedWAVE, RedBASE, RedNODE, RedNAV, RedLINE, ZIMA;
   - acronyms (RWLT, WAYU, A3S, F4105, RedGTR, GIB), file names, link targets, URLs, image paths, code and identifiers are unchanged;
   - RU is the source of truth; EN-only content is removed and listed in the PR description.
   - language-specific formatting of dates and numbers is not a discrepancy if the underlying date or numerical value is unchanged; use normal English formatting, normalize or verify equivalent forms during review, and preserve actual values, units, precision, model codes and identifiers.
5. Never modify files under `documentation/RU/`, binary assets, or the other out-of-scope paths listed in `CLAUDE.md` section 1. Never commit to `master`, never force-push or rewrite history.
6. Communicate with the maintainer in Russian.
