import os
import re
import sys
import json
import posixpath
import subprocess
import urllib.parse
from collections import OrderedDict, defaultdict

FAMILY_ORDER = ["Zima", "uWAVE", "RedPhone", "RWLT", "WAYU", "RedWAVE", "A3S", "Transducers", "Accessories", "uSwitch", "F4105", "Misc", "RedGTR", "RedLINE"]
BATCH_MAX_FILES = 8
BATCH_MAX_KB = 80.0
SIZE_RATIO = 0.6
SYNC_DIR = ".github/docs-sync"
MARKER_RE = re.compile(r"<!-- docs-sync: source=(\S+) commit=([0-9a-f]{40}) date=(\d{4}-\d{2}-\d{2}) -->")
CYR_RE = re.compile(r"[А-Яа-яЁё]")
CASE_NAMES = {"uWAVE": "uWave", "RedWAVE": "RedWave", "RedNODE": "RedNode", "RedBASE": "RedBase", "RedNAV": "RedNav", "RedLINE": "RedLine", "ZIMA": "Zima"}
CASE_RE = re.compile(r"(?<![\w/.\-])(" + "|".join(CASE_NAMES) + r")(?!\w)")
CASE_STRIP_RES = [re.compile(r"\]\([^)]*\)"), re.compile(r"`[^`]*`"), re.compile(r"\b(?:href|src)\s*=\s*\"[^\"]*\"", re.I), re.compile(r"https?://\S+"), re.compile(r"<!--.*?-->")]
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*?)[ \t#]*$")
TABLE_RE = re.compile(r"^\s*\|")
IMG_MD_RE = re.compile(r"!\[[^\]]*\]\(")
IMG_HTML_RE = re.compile(r"<img\b", re.I)
PAGEBREAK_RE = re.compile(r"page-break-after", re.I)
DETAILS_RE = re.compile(r"<details>\s*<summary>(.*?)</summary>", re.I | re.S)
LINK_MD_RE = re.compile(r"\]\(\s*<?([^)\s>]*)>?(?:\s+\"[^\"]*\")?\s*\)")
LINK_HTML_RE = re.compile(r"\b(?:href|src)\s*=\s*\"([^\"]*)\"", re.I)
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def git(*args):
    return subprocess.run(["git"] + list(args), capture_output=True, text=True, check=True).stdout


def read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


class Repo:
    def __init__(self):
        self.root = git("rev-parse", "--show-toplevel").strip()
        os.chdir(self.root)
        self.files = sorted(set(git("ls-files", "--cached", "--others", "--exclude-standard").splitlines()))
        self.fileset = set(self.files)
        self.lower = defaultdict(list)
        for f in self.files:
            self.lower[f.lower()].append(f)
        self.shallow = git("rev-parse", "--is-shallow-repository").strip() == "true"
        self.commit_count = None
        excl = [":(exclude)" + SYNC_DIR, ":(exclude).claude", ":(exclude)CLAUDE.md", ":(exclude)_config.yml"]
        out = git("log", "-1", "--format=%H %cs", "--", ".", *excl).split()
        self.snapshot_sha, self.snapshot_date = out[0], out[1]
        self.commit_count = int(git("rev-list", "--count", self.snapshot_sha).strip())
        self._log = {}

    def last(self, path):
        if path not in self._log:
            out = git("log", "-1", "--format=%H %cs", "--", path).split()
            self._log[path] = (out[0], out[1]) if out else (None, None)
        return self._log[path]

    def count_after(self, sha, path):
        if not sha:
            return None
        try:
            return int(git("rev-list", "--count", sha + "..HEAD", "--", path).strip())
        except subprocess.CalledProcessError:
            return None


def strip_fences(text):
    out = []
    fence = None
    for line in text.splitlines():
        m = FENCE_RE.match(line)
        if fence is None:
            if m and not (m.group(1)[0] == "`" and "`" in m.group(2)):
                fence = m.group(1)
                continue
            out.append(line)
        elif m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not m.group(2).strip():
            fence = None
    return out


def metrics(path):
    text = read(path)
    lines = strip_fences(text)
    body = "\n".join(lines)
    heads = []
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            heads.append((len(m.group(1)), m.group(2).strip()))
    printing = False
    for m in DETAILS_RE.finditer(text):
        s = m.group(1).lower()
        if "pdf" in s or "печат" in s or "print" in s:
            printing = True
            break
    marker = None
    mm = list(MARKER_RE.finditer(text))
    if mm:
        marker = mm[-1].groups()
    return {
        "bytes": len(text.encode("utf-8")),
        "chars": len(text),
        "headings": len(heads),
        "heads": heads,
        "rows": sum(1 for l in lines if TABLE_RE.match(l)),
        "images": len(IMG_MD_RE.findall(body)) + len(IMG_HTML_RE.findall(body)),
        "pagebreaks": len(PAGEBREAK_RE.findall(body)),
        "printing": printing,
        "cyrillic": len(CYR_RE.findall(text)),
        "marker": marker,
    }


def extract_links(text):
    body = "\n".join(strip_fences(text))
    return [m.group(1) for m in LINK_MD_RE.finditer(body)] + [m.group(1) for m in LINK_HTML_RE.finditer(body)]


def resolve(repo, page, target):
    t = target.strip().replace("\\", "/")
    if not t or t.startswith("#") or SCHEME_RE.match(t) or t.startswith("//"):
        return None, None
    t = t.split("#", 1)[0].split("?", 1)[0]
    t = urllib.parse.unquote(t)
    if not t:
        return None, None
    if t.startswith("/"):
        p = posixpath.normpath(t.lstrip("/")) if t != "/" else ""
    else:
        p = posixpath.normpath(posixpath.join(posixpath.dirname(page), t))
    while p == ".." or p.startswith("../"):
        p = p[3:]
    if p in ("", "."):
        return "README.md", "ok"
    cands = [p]
    base, ext = posixpath.splitext(p)
    if ext.lower() == ".html":
        cands.append(base + ".md")
    if ext == "":
        cands += [p + ".md", p + "/README.md", p + "/index.md"]
    for c in cands:
        if c in repo.fileset:
            return c, "ok"
    for c in cands:
        if c.lower() in repo.lower:
            return repo.lower[c.lower()][0], "case"
    return p, "broken"


def norm_stem(name):
    s = name.lower()
    s = re.sub(r"\.md$", "", s)
    s = re.sub(r"_(ru|en)$", "", s)
    return re.sub(r"[^a-z0-9]", "", s)


def is_ru_doc(path):
    if path.startswith("_posts/") or not path.lower().endswith(".md"):
        return False
    if path.startswith("documentation/RU/"):
        return True
    return bool(re.search(r"_ru\.md$", path, re.I))


def canonical_en(ru):
    if ru == "README_RU.md":
        return "README.md"
    if ru.startswith("documentation/RU/"):
        p = "documentation/EN/" + ru[len("documentation/RU/"):]
    else:
        p = ru
    return re.sub(r"_ru\.md$", "_en.md", p, flags=re.I)


def family_of(path):
    parts = path.split("/")
    if len(parts) >= 4 and parts[0] == "documentation" and parts[1] in ("RU", "EN"):
        return parts[2]
    return None


def is_en_doc(path):
    if not path.lower().endswith(".md"):
        return False
    if path.startswith("documentation/EN/"):
        return True
    return "/" not in path and (bool(re.search(r"_en\.md$", path, re.I)) or path == "README.md")


def load_table(path, section):
    if not os.path.exists(path):
        return OrderedDict()
    text = read(path)
    m = re.search(r"^## " + re.escape(section) + r"\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    rows = OrderedDict()
    if not m:
        return rows
    for line in m.group(1).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or set(cells[0]) <= set("-: ") or cells[0].lower() in ("ru file", "ru source"):
            continue
        rows[cells[0]] = cells[1:]
    return rows


def load_decisions(report_path):
    rows = load_table(report_path, "Decisions")
    out = OrderedDict()
    for k, v in rows.items():
        d = v[0].lower() if v else ""
        if d in ("translate", "skip"):
            out[k] = (d, v[1] if len(v) > 1 else "")
    return out


def load_proposals(path):
    out = OrderedDict()
    if not os.path.exists(path):
        return out
    for line in read(path).splitlines():
        if not line.strip() or line.startswith("path\t"):
            continue
        parts = line.split("\t")
        out[parts[0]] = (parts[1], parts[2], parts[3] if len(parts) > 3 else "")
    return out


def kb(n):
    return "%.1f" % (n / 1024.0)


def inventory(repo):
    ru_docs = [f for f in repo.files if is_ru_doc(f)]
    en_docs = [f for f in repo.files if is_en_doc(f)]
    root_pages = [f for f in ru_docs if "/" not in f]
    index_links = defaultdict(list)
    positions = defaultdict(dict)
    for page in ["README_RU.md"] + sorted(p for p in root_pages if p != "README_RU.md"):
        for t in extract_links(read(page)):
            r, st = resolve(repo, page, t)
            if r and r != page:
                index_links[r].append(page)
                positions[page].setdefault(r, len(positions[page]))
    home = {}
    for fam in set(family_of(d) for d in ru_docs if family_of(d)):
        counts = sorted(((-sum(1 for r in positions[pg] if family_of(r) == fam), pg) for pg in positions))
        home[fam] = counts[0][1] if counts and counts[0][0] < 0 else None
    pages = sorted(positions)
    order = {}
    for d in ru_docs:
        fam = family_of(d)
        if fam and home.get(fam) and d in positions[home[fam]]:
            order[d] = (0, "", positions[home[fam]][d])
        else:
            hits = [(pg, positions[pg][d]) for pg in pages if d in positions[pg]]
            order[d] = (1,) + hits[0] if hits else (2, "", 0)
    inbound = defaultdict(set)
    for d in ru_docs:
        for t in extract_links(read(d)):
            r, st = resolve(repo, d, t)
            if r and r != d and r in repo.fileset:
                inbound[r].add(d)
    en_claimed = {}
    pairs = OrderedDict()
    for ru in ru_docs:
        exp = canonical_en(ru)
        en, how = None, None
        if exp in repo.fileset:
            en, how = exp, "exact"
        elif exp.lower() in repo.lower:
            en, how = repo.lower[exp.lower()][0], "case"
        pairs[ru] = {"expected": exp, "en": en, "match": how}
        if en:
            en_claimed[en] = ru
    for ru, p in pairs.items():
        if p["en"] or "/" not in ru:
            continue
        fam = family_of(ru)
        ns = norm_stem(posixpath.basename(ru))
        cands = []
        for en in en_docs:
            if en in en_claimed or family_of(en) != fam:
                continue
            ne = norm_stem(posixpath.basename(en))
            if len(min(ns, ne, key=len)) >= 8 and (ns.startswith(ne) or ne.startswith(ns)):
                cands.append(en)
        if len(cands) == 1:
            p["en"], p["match"] = cands[0], "alias"
            en_claimed[cands[0]] = ru
    rows = []
    for ru, p in pairs.items():
        mr = metrics(ru)
        ru_sha, ru_date = repo.last(ru)
        row = {"ru": ru, "en": p["en"], "expected": p["expected"], "match": p["match"], "family": family_of(ru) or "(root)",
               "root": "/" not in ru, "ru_sha": ru_sha, "ru_date": ru_date, "ru_m": mr,
               "listed": ru in index_links, "listed_in": sorted(set(index_links.get(ru, []))),
               "order": order.get(ru, (2, "", 0)), "inbound": sorted(inbound.get(ru, set()))}
        reasons = []
        if not p["en"]:
            row.update({"status": "MISSING", "en_date": None, "en_sha": None, "after": None, "en_m": None})
        else:
            me = metrics(p["en"])
            en_sha, en_date = repo.last(p["en"])
            base = me["marker"][1] if me["marker"] else en_sha
            after = repo.count_after(base, ru)
            row.update({"en_m": me, "en_sha": en_sha, "en_date": en_date, "after": after, "marker": bool(me["marker"])})
            if after:
                reasons.append("changed")
            if abs(mr["headings"] - me["headings"]) > 1:
                reasons.append("headings")
            if mr["printing"] and not me["printing"]:
                reasons.append("print")
            if me["chars"] < SIZE_RATIO * mr["chars"]:
                reasons.append("size")
            row["status"] = "STALE" if reasons else "OK"
        row["reasons"] = reasons
        rows.append(row)
    orphans = []
    for en in en_docs:
        if en in en_claimed:
            continue
        ns = norm_stem(posixpath.basename(en))
        near = [r for r in ru_docs if family_of(r) == family_of(en) and norm_stem(posixpath.basename(r)) and
                (ns.startswith(norm_stem(posixpath.basename(r))) or norm_stem(posixpath.basename(r)).startswith(ns))]
        orphans.append({"en": en, "near": near, "date": repo.last(en)[1], "bytes": metrics(en)["bytes"]})
    return rows, orphans, index_links, en_claimed, pairs


def index_coverage(repo, pairs):
    out = []
    for ru_page in ["README_RU.md"] + sorted(p for p in pairs if "/" not in p and p != "README_RU.md"):
        en_page = pairs[ru_page]["en"]
        ru_targets = []
        for t in extract_links(read(ru_page)):
            r, st = resolve(repo, ru_page, t)
            if r and (r in pairs) and r not in ru_targets:
                ru_targets.append(r)
        en_targets = set()
        broken = []
        if en_page:
            for t in extract_links(read(en_page)):
                r, st = resolve(repo, en_page, t)
                if r:
                    if st == "ok":
                        en_targets.add(r)
                    else:
                        broken.append((t, st))
        missing = []
        for r in ru_targets:
            e = pairs[r]["en"] or pairs[r]["expected"]
            if e not in en_targets:
                missing.append((r, e, bool(pairs[r]["en"])))
        ru_broken = []
        for t in extract_links(read(ru_page)):
            r, st = resolve(repo, ru_page, t)
            if r and st != "ok":
                ru_broken.append((t, st))
        out.append({"ru": ru_page, "en": en_page, "ru_links": len(ru_targets), "missing": missing, "en_broken": broken, "ru_broken": ru_broken})
    return out


def duplicates(repo, rows, orphans):
    md = [f for f in repo.files if f.lower().endswith(".md") and (f.startswith("documentation/") or "/" not in f)]
    groups = defaultdict(list)
    for f in md:
        groups[f.lower()].append(f)
    exact_case = [g for g in groups.values() if len(g) > 1]
    upper_suffix = [f for f in md if re.search(r"_(RU|EN)\.md$", f) or re.search(r"\.MD$", f)]
    tokens = defaultdict(set)
    tokfiles = defaultdict(set)
    for f in md:
        base = re.sub(r"\.md$", "", posixpath.basename(f), flags=re.I)
        for tok in re.split(r"[_\-.]", base):
            if len(tok) >= 4 and re.search(r"[A-Za-z]", tok):
                tokens[tok.lower()].add(tok)
                tokfiles[tok].add(f)
    variants = []
    for low in sorted(tokens):
        if len(tokens[low]) > 1:
            variants.append([(v, sorted(tokfiles[v])) for v in sorted(tokens[low])])
    mismatched = [r for r in rows if r["match"] in ("case", "alias")]
    sims = []
    ru_docs = [r["ru"] for r in rows if not r["root"]]
    sets = {}
    for d in ru_docs:
        ls = set(l.strip() for l in strip_fences(read(d)) if len(l.strip()) > 25 and not l.strip().startswith(("<li>", "<summary>", "[Главная]", "| [www.", "| :---")))
        sets[d] = ls
    for i, a in enumerate(ru_docs):
        for b in ru_docs[i + 1:]:
            sa, sb = sets[a], sets[b]
            if not sa or not sb:
                continue
            j = len(sa & sb) / float(len(sa | sb))
            if j >= 0.5:
                sims.append((a, b, j))
    return exact_case, upper_suffix, variants, mismatched, sims


def md_cell(s):
    return str(s).replace("|", "\\|")


def fmt_file(path, repo_root_rel=True):
    if not path:
        return "—"
    return "`" + path + "`"


def short(path):
    return path.split("/", 3)[-1] if path.startswith("documentation/") else path


def build_plan(rows, decisions, proposals):
    plan = []
    for fam in FAMILY_ORDER:
        cand = []
        for r in rows:
            if r["root"] or r["family"] != fam or r["status"] not in ("MISSING", "STALE"):
                continue
            eff = effective(r, decisions, proposals)
            if eff in ("SKIP", "DECIDE-skip"):
                continue
            cand.append(r)
        cand.sort(key=lambda r: (posixpath.basename(r["ru"]) == "media.md", not r["listed"], tuple(r["order"]) if r["listed"] else (), r["ru"].lower()))
        bins = []
        for r in cand:
            k = r["ru_m"]["bytes"] / 1024.0
            pool = bins[-1:] if posixpath.basename(r["ru"]) == "media.md" else bins
            target = None
            for b in pool:
                if len(b[0]) < BATCH_MAX_FILES and b[1] + k <= BATCH_MAX_KB:
                    target = b
                    break
            if target is None:
                target = [[], 0.0]
                bins.append(target)
            target[0].append(r)
            target[1] += k
        for i, b in enumerate(bins, 1):
            plan.append((fam.lower() + "-" + str(i), fam, b[0], b[1]))
    return plan


def effective(r, decisions, proposals):
    if r["ru"] in decisions:
        return "SKIP" if decisions[r["ru"]][0] == "skip" else "TRANSLATE"
    if r["ru"] in proposals and proposals[r["ru"]][0] == "DECIDE":
        return "DECIDE-" + proposals[r["ru"]][1]
    if r["ru"] in proposals and proposals[r["ru"]][0] == "SKIP":
        return "SKIP"
    return ""


def render(repo, rows, orphans, coverage, dups, decisions, proposals, old_decisions_block):
    L = []
    w = L.append
    w("# RU → EN documentation sync: inventory and plan")
    w("")
    w("Generated by `python3 .github/docs-sync/docsync.py report` (Python 3, standard library). Do not edit by hand except the **Decisions** section, which the script preserves and applies on every run. Proposals for the DECIDE list live in `.github/docs-sync/proposals.tsv`.")
    w("")
    w("Other subcommands: `marker <RU path>` prints the sync marker line for a RU file; `check <RU path> <EN path>` runs the mechanical part of the controller review (Cyrillic, structure counts, heading numbering, printing block, TOC anchors, local links, numbers, marker); `terms` prints RU → EN term candidates from the existing pairs; `json` dumps the inventory.")
    w("")
    w("| Item | Value |")
    w("|---|---|")
    w("| Snapshot date | %s |" % repo.snapshot_date)
    w("| Content HEAD commit | `%s` |" % repo.snapshot_sha)
    w("| History | %s |" % ("SHALLOW clone — dates and commit counts are unreliable, structural comparison only" if repo.shallow else "full history (%d commits up to the content HEAD commit), dates and commit counts are reliable" % repo.commit_count))
    w("| Staleness rule | `STALE` = RU has commits after the EN file's last commit (or after its sync marker), or headings differ by more than 1, or EN lacks the printing block RU has, or EN has fewer than 60 % of the RU characters |")
    w("")
    w("Legend. `Listed`: linked from `README_RU.md` or a root `*_ru.md` page. `Notes`: `changed` RU changed after EN, `headings` heading count differs by more than 1, `print` printing block missing in EN, `size` EN under 60 % of RU characters, `marker` EN carries a sync marker, `alias`/`case` EN name differs from the canonical name. `Proposal`: `DECIDE-translate` / `DECIDE-skip` awaiting the maintainer, `SKIP`/`TRANSLATE` decided.")
    w("")
    w("## Summary")
    w("")
    docs = [r for r in rows if not r["root"]]
    roots = [r for r in rows if r["root"]]
    cnt = defaultdict(int)
    for r in docs:
        cnt[r["status"]] += 1
    eff_cnt = defaultdict(int)
    for r in docs:
        e = effective(r, decisions, proposals)
        if e:
            eff_cnt[e] += 1
    w("| Scope | Total | MISSING | STALE | OK |")
    w("|---|---:|---:|---:|---:|")
    w("| Documents under `documentation/RU/` | %d | %d | %d | %d |" % (len(docs), cnt["MISSING"], cnt["STALE"], cnt["OK"]))
    rc = defaultdict(int)
    for r in roots:
        rc[r["status"]] += 1
    w("| Root pages (`README_RU.md`, `*_ru.md`; Phase 3) | %d | %d | %d | %d |" % (len(roots), rc["MISSING"], rc["STALE"], rc["OK"]))
    w("")
    w("| Proposal / decision | Documents |")
    w("|---|---:|")
    for k in ("DECIDE-translate", "DECIDE-skip", "TRANSLATE", "SKIP"):
        w("| %s | %d |" % (k, eff_cnt[k]))
    w("")
    plan = build_plan(rows, decisions, proposals)
    tot_kb = sum(b[3] for b in plan)
    nfiles = sum(len(b[2]) for b in plan)
    w("Batch plan: **%d batches**, **%d documents**, **%.1f KB** of RU source (MISSING and STALE documents, `DECIDE-skip` and `SKIP` excluded, root pages excluded)." % (len(plan), nfiles, tot_kb))
    w("")
    w("## Inventory by family")
    for fam in FAMILY_ORDER:
        fr = [r for r in docs if r["family"] == fam]
        if not fr:
            continue
        w("")
        w("### %s" % fam)
        w("")
        w("| Status | RU file | EN file | RU last | EN last | RU commits after EN | RU KB | EN KB | Headings RU/EN | Listed | Rows RU/EN | Images RU/EN | Print RU/EN | Notes | Proposal |")
        w("|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|---|---|")
        for r in sorted(fr, key=lambda r: r["ru"].lower()):
            w(row_line(r, decisions, proposals))
    other = [r for r in docs if r["family"] not in FAMILY_ORDER]
    if other:
        w("")
        w("### Other")
        w("")
        w("| Status | RU file | EN file | RU last | EN last | RU commits after EN | RU KB | EN KB | Headings RU/EN | Listed | Rows RU/EN | Images RU/EN | Print RU/EN | Notes | Proposal |")
        w("|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|---|---|")
        for r in other:
            w(row_line(r, decisions, proposals))
    w("")
    w("### Root pages (Phase 3)")
    w("")
    w("| Status | RU file | EN file | RU last | EN last | RU commits after EN | RU KB | EN KB | Headings RU/EN | Listed | Rows RU/EN | Images RU/EN | Print RU/EN | Notes | Proposal |")
    w("|---|---|---|---|---|---:|---:|---:|---|---|---|---|---|---|---|")
    for r in sorted(roots, key=lambda r: (r["ru"] != "README_RU.md", r["ru"])):
        w(row_line(r, decisions, proposals))
    w("")
    w("## Orphans (EN files without an RU counterpart)")
    w("")
    if orphans:
        w("| EN file | EN last | EN KB | Closest RU file | Note |")
        w("|---|---|---:|---|---|")
        for o in orphans:
            w("| `%s` | %s | %s | %s | %s |" % (o["en"], o["date"], kb(o["bytes"]), ", ".join("`%s`" % x for x in o["near"]) or "—", proposals.get(o["en"], ("", "", ""))[2] if o["en"] in proposals else ""))
    else:
        w("None.")
    w("")
    w("## Index coverage")
    w("")
    w("For each root RU page: RU links to documents that have no corresponding link in the paired EN page. `EN exists` tells whether the EN document is already there (then Phase 3 only has to add the link).")
    w("")
    w("| RU page | EN page | RU document links | Missing in EN | of which EN exists | Broken links in EN page |")
    w("|---|---|---:|---:|---:|---:|")
    for c in coverage:
        w("| `%s` | %s | %d | %d | %d | %d |" % (c["ru"], fmt_file(c["en"]), c["ru_links"], len(c["missing"]), sum(1 for m in c["missing"] if m[2]), len(c["en_broken"])))
    for c in coverage:
        if not c["missing"] and not c["en_broken"] and not c["ru_broken"]:
            continue
        w("")
        w("<details><summary><code>%s</code> → <code>%s</code></summary>" % (c["ru"], c["en"] or "—"))
        w("")
        if c["missing"]:
            w("| RU target | EN equivalent | EN exists |")
            w("|---|---|---|")
            for m in c["missing"]:
                w("| `%s` | `%s` | %s |" % (m[0], m[1], "yes" if m[2] else "no"))
            w("")
        if c["en_broken"]:
            w("Broken or case-mismatched links in the EN page: " + ", ".join("`%s` (%s)" % (md_cell(t), s) for t, s in c["en_broken"]))
            w("")
        if c["ru_broken"]:
            w("Broken or case-mismatched links in the RU page (report only, RU is never edited): " + ", ".join("`%s` (%s)" % (md_cell(t), s) for t, s in c["ru_broken"]))
            w("")
        w("</details>")
    exact_case, upper_suffix, variants, mismatched, sims = dups
    w("")
    w("## Duplicates and naming variants")
    w("")
    w("### RU ↔ EN pairs whose EN name differs from the canonical name")
    w("")
    if mismatched:
        w("| RU file | Canonical EN name | Existing EN file | Kind | Handling |")
        w("|---|---|---|---|---|")
        for r in mismatched:
            w("| `%s` | `%s` | `%s` | %s | update the existing EN file in place (rule 9: no renames); Phase 3 links to it |" % (r["ru"], r["expected"], r["en"], r["match"]))
    else:
        w("None.")
    w("")
    w("### Files whose paths differ only in letter case")
    w("")
    w("None." if not exact_case else "\n".join("- " + ", ".join("`%s`" % x for x in g) for g in exact_case))
    w("")
    w("### Upper-case language suffixes or extensions")
    w("")
    w("None." if not upper_suffix else "\n".join("- `%s`" % x for x in upper_suffix))
    w("")
    w("### Case variants of the same token in file names")
    w("")
    w("| Token variants | Files |")
    w("|---|---|")
    for v in variants:
        parts = []
        for tok, files in v:
            parts.append("**%s** (%d): %s" % (tok, len(files), ", ".join("`%s`" % short(f) for f in files[:6]) + (" …" if len(files) > 6 else "")))
        w("| %s | %s |" % (" / ".join(t for t, _ in v), "<br>".join(parts)))
    w("")
    w("### RU documents with largely identical content")
    w("")
    w("Jaccard similarity of distinct non-trivial lines ≥ 0.5.")
    w("")
    if sims:
        w("| RU file A | RU file B | Similarity |")
        w("|---|---|---:|")
        for a, b, j in sorted(sims, key=lambda x: -x[2]):
            w("| `%s` | `%s` | %.2f |" % (a, b, j))
    else:
        w("None.")
    w("")
    w("## DECIDE list")
    w("")
    dl = [r for r in rows if r["ru"] in proposals and proposals[r["ru"]][0] == "DECIDE"]
    w("| # | File | Status | Listed | RU KB | Category | Recommendation | Reason | Decision |")
    w("|---:|---|---|---|---:|---|---|---|---|")
    byru = dict((r["ru"], r) for r in dl)
    items = []
    for k, v in proposals.items():
        if v[0] != "DECIDE":
            continue
        if k in byru:
            r = byru[k]
            items.append((k, r["status"], "yes" if r["listed"] else "no", kb(r["ru_m"]["bytes"])))
        else:
            items.append((k, "ORPHAN", "—", "—"))
    for i, (path, status, listed, size) in enumerate(items, 1):
        p = proposals[path]
        cat, _, reason = p[2].partition(":")
        dec = decisions.get(path, ("—", ""))[0]
        w("| %d | `%s` | %s | %s | %s | %s | %s | %s | %s |" % (i, path, status, listed, size, cat.strip(), p[1], md_cell(reason.strip()), dec))
    w("")
    w("## Batch plan")
    w("")
    w("Families in the order of CLAUDE.md section 7. Within a family the documents are taken in this order: listed documents in the order of the family's main RU index page, then documents listed only elsewhere, then unlisted documents, `media.md` last; each document goes into the first batch of its family that still has room (at most %d files and %d KB of RU source), `media.md` into the last batch. A single document larger than the limit forms its own batch. Slugs are the `docs-sync/<slug>` branch names." % (BATCH_MAX_FILES, BATCH_MAX_KB))
    w("")
    w("| Batch | Family | Files | RU KB |")
    w("|---|---|---:|---:|")
    for slug, fam, items, k in plan:
        w("| `%s` | %s | %d | %.1f |" % (slug, fam, len(items), k))
    for slug, fam, items, k in plan:
        w("")
        w("### `%s` — %s, %d files, %.1f KB" % (slug, fam, len(items), k))
        w("")
        for r in items:
            tag = r["status"]
            e = effective(r, decisions, proposals)
            if e:
                tag += ", " + e
            if r["status"] == "STALE":
                tag += "; " + ", ".join(r["reasons"])
            w("- `%s` → `%s` (%s) — %s KB" % (r["ru"], r["en"] or r["expected"], tag, kb(r["ru_m"]["bytes"])))
    w("")
    w("## Decisions")
    w("")
    if old_decisions_block is not None:
        w(old_decisions_block.strip("\n"))
    else:
        w("Maintainer decisions on the DECIDE list. `Decision` is `translate` or `skip`; the script applies this table on every run.")
        w("")
        w("| RU file | Decision | Note |")
        w("|---|---|---|")
    w("")
    return "\n".join(L)


def row_line(r, decisions, proposals):
    ru = r["ru_m"]
    en = r.get("en_m")
    notes = list(r["reasons"])
    if r.get("marker"):
        notes.append("marker")
    if r["match"] in ("case", "alias"):
        notes.append(r["match"])
    if r["ru_m"]["cyrillic"] == 0 and not r["root"]:
        notes.append("no-cyrillic-in-RU")
    if en and en["cyrillic"]:
        notes.append("cyrillic-in-EN(%d)" % en["cyrillic"])
    e = effective(r, decisions, proposals)
    return "| %s | `%s` | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
        r["status"], short(r["ru"]), ("`%s`" % short(r["en"])) if r["en"] else "—", r["ru_date"] or "—", r.get("en_date") or "—",
        "—" if r.get("after") is None else r["after"], kb(ru["bytes"]), kb(en["bytes"]) if en else "—",
        "%d/%s" % (ru["headings"], en["headings"] if en else "—"), "yes" if r["listed"] else "no",
        "%d/%s" % (ru["rows"], en["rows"] if en else "—"), "%d/%s" % (ru["images"], en["images"] if en else "—"),
        "%s/%s" % ("y" if ru["printing"] else "n", ("y" if en["printing"] else "n") if en else "—"), ", ".join(notes), e)


def cmd_report(repo):
    report = os.path.join(SYNC_DIR, "REPORT.md")
    decisions = load_decisions(report)
    proposals = load_proposals(os.path.join(SYNC_DIR, "proposals.tsv"))
    old_block = None
    if os.path.exists(report):
        m = re.search(r"^## Decisions\s*$(.*?)(?=^## |\Z)", read(report), re.M | re.S)
        if m:
            old_block = m.group(1)
    rows, orphans, index_links, en_claimed, pairs = inventory(repo)
    coverage = index_coverage(repo, pairs)
    dups = duplicates(repo, rows, orphans)
    out = render(repo, rows, orphans, coverage, dups, decisions, proposals, old_block)
    with open(report, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print("written", report)


def cmd_json(repo):
    rows, orphans, index_links, en_claimed, pairs = inventory(repo)
    for r in rows:
        for k in ("ru_m", "en_m"):
            if r.get(k):
                r[k] = {a: b for a, b in r[k].items() if a != "heads"}
    print(json.dumps({"rows": rows, "orphans": orphans}, ensure_ascii=False, indent=1, sort_keys=True))


def cmd_marker(repo, ru):
    sha, date = repo.last(ru)
    print("<!-- docs-sync: source=%s commit=%s date=%s -->" % (ru, sha, date))


def case_problems(text):
    out = []
    fence = None
    for i, line in enumerate(text.splitlines(), 1):
        m = FENCE_RE.match(line)
        if fence is None:
            if m and not (m.group(1)[0] == "`" and "`" in m.group(2)):
                fence = m.group(1)
                continue
        else:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not m.group(2).strip():
                fence = None
            continue
        clean = line
        for r in CASE_STRIP_RES:
            clean = r.sub(" ", clean)
        segments = clean.split("|") if TABLE_RE.match(clean) else [clean]
        for seg in segments:
            for cm in CASE_RE.finditer(seg):
                rest = CASE_RE.sub(" ", seg)
                if not re.search(r"[a-z]", rest):
                    continue
                out.append("product name case line %d: %s -> %s" % (i, cm.group(1), CASE_NAMES[cm.group(1)]))
    return out


def cmd_check(repo, ru, en):
    mr, me = metrics(ru), metrics(en)
    text = read(en)
    problems = []
    for i, line in enumerate(text.splitlines(), 1):
        if CYR_RE.search(line):
            problems.append("cyrillic line %d: %s" % (i, line.strip()[:120]))
    problems.extend(case_problems(text))
    for k in ("headings", "rows", "images", "pagebreaks"):
        if mr[k] != me[k]:
            problems.append("%s RU=%d EN=%d" % (k, mr[k], me[k]))
    rn = [h[1].split(" ")[0] for h in mr["heads"] if re.match(r"^\d+(\.\d+)*\.?\s", h[1])]
    en_n = [h[1].split(" ")[0] for h in me["heads"] if re.match(r"^\d+(\.\d+)*\.?\s", h[1])]
    if rn != en_n:
        problems.append("heading numbering differs: RU=%s EN=%s" % (rn, en_n))
    if mr["printing"] != me["printing"]:
        problems.append("printing block RU=%s EN=%s" % (mr["printing"], me["printing"]))
    slugs = defaultdict(int)
    anchors = set()
    for lvl, h in me["heads"]:
        s = slug(h)
        n = slugs[s]
        slugs[s] += 1
        anchors.add(s if n == 0 else "%s-%d" % (s, n))
    for a in re.findall(r"<a\s+(?:name|id)\s*=\s*\"([^\"]+)\"", text, re.I):
        anchors.add(a)
    for a in re.findall(r"<div\s+id\s*=\s*\"([^\"]+)\"", text, re.I):
        anchors.add(a)
    switch = set()
    for line in text.splitlines():
        if "[EN](" in line and "[RU](" in line:
            switch.update(x.strip() for x in re.findall(r"\[RU\]\(([^)\s]+)\)", line))
    for t in extract_links(text):
        tt = t.strip()
        if tt.startswith("#"):
            if urllib.parse.unquote(tt[1:]) not in anchors:
                problems.append("anchor not found: %s" % tt)
            continue
        m = SELF_RE.match(tt)
        r, st = resolve(repo, en, (m.group(1) or "/") if m else tt)
        if r is None:
            continue
        if st != "ok":
            problems.append("local link %s: %s" % (st, tt))
        if re.search(r"(_ru(\.md|\.html)?$|/RU/)", r, re.I) and tt not in switch:
            problems.append("RU link, must be a declared deferred link: %s" % tt)
    lines = text.rstrip("\n").splitlines()
    exp = "<!-- docs-sync: source=%s commit=%s date=%s -->" % ((ru,) + repo.last(ru))
    if not lines or lines[-1] != exp:
        problems.append("marker missing or wrong; expected: " + exp)
    if len(MARKER_RE.findall(text)) != 1:
        problems.append("marker count %d" % len(MARKER_RE.findall(text)))
    nr, ne = numbers(read(ru)), numbers(text)
    miss = sorted((nr - ne).elements())
    extra = sorted((ne - nr).elements())
    if miss or extra:
        problems.append("numbers only in RU: %s" % miss[:80])
        problems.append("numbers only in EN: %s" % extra[:80])
    print("RU %s: headings=%d rows=%d images=%d pagebreaks=%d printing=%s" % (ru, mr["headings"], mr["rows"], mr["images"], mr["pagebreaks"], mr["printing"]))
    print("EN %s: headings=%d rows=%d images=%d pagebreaks=%d printing=%s" % (en, me["headings"], me["rows"], me["images"], me["pagebreaks"], me["printing"]))
    print("\n".join(problems) if problems else "ALL CHECKS PASSED")


def slug(h):
    s = re.sub(r"<[^>]+>", "", h)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = s.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.U)
    return s.replace(" ", "-")


def numbers(text):
    from collections import Counter
    text = MARKER_RE.sub("", text)
    text = re.sub(r"\]\([^)]*\)", "]()", text)
    text = re.sub(r"\b(?:href|src|name|id)\s*=\s*\"[^\"]*\"", "", text, flags=re.I)
    return Counter(re.findall(r"0x[0-9A-Fa-f]+|\d+(?:[.,]\d+)?", text))


NUM_HEAD_RE = re.compile(r"^((?:\d+|[A-Z])(?:\.\d+)*)\.?\s+(.*)$")


def clean_term(t):
    t = re.sub(r"<sup>.*?</sup>", "", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = t.replace("**", "").replace("`", "").replace("\\|", "|")
    t = re.sub(r"\s+", " ", t).strip(" :;,.-—")
    return t


def table_blocks(lines):
    out = []
    i = 0
    while i < len(lines) - 1:
        if TABLE_RE.match(lines[i]) and re.match(r"^\s*\|[\s:|-]+\|?\s*$", lines[i + 1]) and "-" in lines[i + 1]:
            head = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            body = []
            j = i + 2
            while j < len(lines) and TABLE_RE.match(lines[j]):
                body.append([c.strip() for c in lines[j].strip().strip("|").split("|")])
                j += 1
            out.append((head, body))
            i = j
        else:
            i += 1
    return out


def term_pairs(ru, en):
    rt, et = read(ru), read(en)
    rl, el = strip_fences(rt), strip_fences(et)
    pairs = []

    def add(a, b, kind):
        a, b = clean_term(a), clean_term(b)
        if a and b and CYR_RE.search(a) and not CYR_RE.search(b) and len(a.split()) <= 10:
            pairs.append((a, b, kind))

    rb = [l for l in rl[:5] if "❯" in l]
    eb = [l for l in el[:5] if "❯" in l]
    if rb and eb:
        rs, es = [x.strip() for x in rb[0].split("❯")], [x.strip() for x in eb[0].split("❯")]
        if len(rs) == len(es):
            for a, b in zip(rs, es):
                add(a, b, "breadcrumb")
            last_r, last_e = clean_term(rs[-1]), clean_term(es[-1])
            if ":" in last_r and ":" in last_e:
                add(last_r.split(":", 1)[0], last_e.split(":", 1)[0], "breadcrumb")
                add(last_r.split(":", 1)[1], last_e.split(":", 1)[1], "breadcrumb")

    def title_cell(lines):
        for l in lines[:40]:
            if l.startswith("| [www.unavlab.com]"):
                cells = [c.strip() for c in l.strip().strip("|").split("|")]
                return cells[-1]
        return None
    rc, ec = title_cell(rl), title_cell(el)
    if rc and ec:
        rs, es = re.split(r"<br\s*/?>", rc), re.split(r"<br\s*/?>", ec)
        if len(rs) == len(es):
            for a, b in zip(rs, es):
                if " - " in a and " - " in b:
                    add(a.split(" - ", 1)[1], b.split(" - ", 1)[1], "header")
                else:
                    add(a, b, "header")
    rh = [h for h in metrics(ru)["heads"]]
    eh = [h for h in metrics(en)["heads"]]
    r1 = [h[1] for h in rh if h[0] == 1]
    e1 = [h[1] for h in eh if h[0] == 1]
    if r1 and e1:
        rs, es = re.split(r"<br\s*/?>", r1[0]), re.split(r"<br\s*/?>", e1[0])
        if len(rs) == len(es):
            for a, b in zip(rs, es):
                add(a, b, "title")
    rn = OrderedDict()
    for lvl, h in rh:
        m = NUM_HEAD_RE.match(h)
        if m:
            rn.setdefault(m.group(1), m.group(2))
    en_n = OrderedDict()
    for lvl, h in eh:
        m = NUM_HEAD_RE.match(h)
        if m:
            en_n.setdefault(m.group(1), m.group(2))
    for k, a in rn.items():
        if k in en_n:
            lat = set(x.lower() for x in re.findall(r"[A-Za-z][A-Za-z0-9_]+", clean_term(a)))
            blat = set(x.lower() for x in re.findall(r"[A-Za-z][A-Za-z0-9_]+", clean_term(en_n[k])))
            if lat <= blat:
                add(a, en_n[k], "heading")
    ru_un = [(lvl, h) for lvl, h in rh if not NUM_HEAD_RE.match(h) and lvl > 1]
    en_un = [(lvl, h) for lvl, h in eh if not NUM_HEAD_RE.match(h) and lvl > 1]
    if len(ru_un) == len(en_un) and [x[0] for x in ru_un] == [x[0] for x in en_un]:
        for (la, a), (lb, b) in zip(ru_un, en_un):
            add(a, b, "heading")
    rtab, etab = table_blocks(rl), table_blocks(el)
    if len(rtab) == len(etab):
        for (rh_, rbody), (eh_, ebody) in zip(rtab, etab):
            if len(rh_) == len(eh_):
                for a, b in zip(rh_, eh_):
                    add(a, b, "table-head")
            if len(rbody) == len(ebody) and len(rh_) == 2 and len(eh_) == 2:
                for ra, ea in zip(rbody, ebody):
                    if len(ra) >= 2 and len(ea) >= 2:
                        na = re.findall(r"\d+(?:\.\d+)?", ra[1])
                        nb = re.findall(r"\d+(?:\.\d+)?", ea[1])
                        if na == nb:
                            add(ra[0], ea[0], "table-row")
    return pairs


def cmd_terms(repo):
    rows, orphans, index_links, en_claimed, pairs = inventory(repo)
    agg = OrderedDict()
    for r in rows:
        if not r["en"]:
            continue
        for a, b, kind in term_pairs(r["ru"], r["en"]):
            key = a.lower()
            ent = agg.setdefault(key, {"ru": a, "variants": OrderedDict()})
            vkey = b.lower()
            v = ent["variants"].setdefault(vkey, {"en": b, "files": [], "kinds": set(), "dates": []})
            v["files"].append(r["en"])
            v["kinds"].add(kind)
            v["dates"].append(r.get("en_date") or "")
    out = []
    for key in sorted(agg):
        ent = agg[key]
        for vk, v in ent["variants"].items():
            out.append("\t".join([ent["ru"], v["en"], str(len(v["files"])), max(v["dates"]), ",".join(sorted(v["kinds"])), ";".join(sorted(set(short(f) for f in v["files"]))), str(len(ent["variants"]))]))
    print("\n".join(out))


SELF_RE = re.compile(r"^https?://(?:www\.)?docs\.unavlab\.com(/[^\s)\"]*)?", re.I)


def cmd_brief(repo, ru, batch):
    rows, orphans, index_links, en_claimed, pairs = inventory(repo)
    row = [r for r in rows if r["ru"] == ru][0]
    batch_ru = set(batch) | {ru}
    text = read(ru)
    print("RU source: %s" % ru)
    print("EN target: %s (%s)" % (row["en"] or row["expected"], row["status"] + ("; " + ", ".join(row["reasons"]) if row["reasons"] else "")))
    print("Printing <details> block in RU: %s" % ("yes" if row["ru_m"]["printing"] else "no"))
    first = [l for l in text.splitlines()[:5] if "❯" in l]
    print("RU breadcrumb: %s" % (first[0] if first else "none"))
    if row["en"]:
        sha, date = repo.last(row["en"])
        print("EN last commit: %s %s; RU commits since: %s" % (sha, date, row["after"]))
    print("Counts RU: headings=%d rows=%d images=%d pagebreaks=%d" % (row["ru_m"]["headings"], row["ru_m"]["rows"], row["ru_m"]["images"], row["ru_m"]["pagebreaks"]))
    if row.get("en_m"):
        print("Counts EN now: headings=%d rows=%d images=%d pagebreaks=%d" % (row["en_m"]["headings"], row["en_m"]["rows"], row["en_m"]["images"], row["en_m"]["pagebreaks"]))
    print("Links:")
    seen = set()
    for t in extract_links(text):
        tt = t.strip()
        if tt in seen or not tt:
            continue
        seen.add(tt)
        m = SELF_RE.match(tt)
        target = (m.group(1) or "/") if m else tt
        if not m and (SCHEME_RE.match(tt) or tt.startswith("#") or tt.startswith("//")):
            continue
        r, st = resolve(repo, ru, target)
        if r is None:
            continue
        kind = "absolute docs.unavlab.com link" if m else "local link"
        if r in pairs:
            en = pairs[r]["en"] or pairs[r]["expected"]
            if r in batch_ru:
                state = "EN created in this batch"
            elif pairs[r]["en"]:
                state = "EN exists in master"
            else:
                state = "EN MISSING: deferred, keep the RU link"
            print("  - %s `%s` -> RU `%s` -> EN `%s`: %s" % (kind, tt, r, en, state))
        elif r.lower().endswith(".md"):
            print("  - %s `%s` -> `%s` (%s)" % (kind, tt, r, st))
        else:
            print("  - %s `%s` -> asset `%s` (%s), keep unchanged" % (kind, tt, r, st))
    print("Images with language variants:")
    for img in sorted(set(re.findall(r"[/\\\w.\-]+_ru\.(?:png|jpe?g|gif|svg)", text, re.I))):
        cand = re.sub(r"_ru\.", "_en.", img, flags=re.I)
        base = cand.lstrip("/")
        print("  - `%s`: EN variant `%s` %s" % (img, cand, "exists" if base in repo.fileset else "does not exist (keep RU image, list under Needs EN image)"))
    print(cmd_marker_line(repo, ru))


def cmd_marker_line(repo, ru):
    sha, date = repo.last(ru)
    return "Marker: <!-- docs-sync: source=%s commit=%s date=%s -->" % (ru, sha, date)


def main():
    repo = Repo()
    if len(sys.argv) < 2:
        print("usage: docsync.py report | json | terms | brief <RU path> [<batch RU path> ...] | marker <RU path> | check <RU path> <EN path>")
        sys.exit(2)
    elif sys.argv[1] == "report":
        cmd_report(repo)
    elif sys.argv[1] == "json":
        cmd_json(repo)
    elif sys.argv[1] == "terms":
        cmd_terms(repo)
    elif sys.argv[1] == "brief":
        cmd_brief(repo, sys.argv[2], sys.argv[3:])
    elif sys.argv[1] == "marker":
        cmd_marker(repo, sys.argv[2])
    elif sys.argv[1] == "check":
        cmd_check(repo, sys.argv[2], sys.argv[3])
    else:
        print("usage: docsync.py report | json | terms | brief <RU path> [<batch RU path> ...] | marker <RU path> | check <RU path> <EN path>")
        sys.exit(2)


if __name__ == "__main__":
    main()
