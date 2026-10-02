#!/usr/bin/env python3
"""Build README.md from data/papers.yaml and scripts/README.template.md.

    python scripts/build_readme.py          # regenerate README.md
    python scripts/build_readme.py --check  # exit with status 1 if README.md is stale or the data is invalid

Requires PyYAML (pip install pyyaml).
"""
import argparse
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "papers.yaml"
TEMPLATE = ROOT / "scripts" / "README.template.md"
README = ROOT / "README.md"

TOC_TITLE = "📑 Contents"
REQUIRED = ("section", "name", "title", "venue", "year")


def slugify(text, seen):
    """Reproduce GitHub's heading anchors, including -1, -2 suffixes for repeats.

    GitHub keeps letters, marks, digits, connector punctuation, zero-width joiners, hyphens and spaces,
    so an emoji's variation selector (U+FE0F, a mark) stays in the anchor even though the emoji goes.
    """
    kept = (c for c in text.strip().lower()
            if c in "- ‌‍" or unicodedata.category(c).startswith(("L", "M", "Nd", "Nl", "Pc")))
    slug = "".join(kept).replace(" ", "-")
    base, n = slug, seen[slug]
    seen[base] += 1
    return f"{base}-{n}" if n else base


def escape(text):
    text = str(text).replace("|", r"\|").replace("*", r"\*").replace("[", r"\[").replace("]", r"\]")
    return text.replace("<", "&lt;").replace(">", "&gt;")


def code_cell(url):
    if not url:
        return "—"
    m = re.fullmatch(r"https://github\.com/([\w.-]+)/([\w.-]+)/?", url)
    if m:
        slug = f"{m.group(1)}/{m.group(2)}"
        return f"[![Star](https://img.shields.io/github/stars/{slug}?style=social&label=Star)]({url})"
    return f"[Code]({url})"


def paper_row(p):
    name = f"**{escape(p['name'])}**"
    if p.get("highlight"):
        name = "🌟 " + name
    title = escape(p["title"])
    if p.get("paper"):
        title = f"[{title}]({p['paper']})"
    venue = f"{escape(p['venue'])} {p['year']}"
    return f"| {name} | {title} | {venue} | {code_cell(p.get('code'))} |"


def render_table(papers):
    rows = sorted(papers, key=lambda p: (-int(p["year"]), str(p["name"]).lower()))
    lines = ["| Method | Paper | Venue | Code |", "|:--|:--|:--:|:--:|"]
    return "\n".join(lines + [paper_row(p) for p in rows])


def validate(data):
    errors = []
    ids = [s["id"] for s in data["sections"] if s.get("id")]
    for key, n in Counter(ids).items():
        if n > 1:
            errors.append(f"duplicate section id: {key}")
    seen = Counter()
    for i, p in enumerate(data["papers"]):
        for field in REQUIRED:
            if not p.get(field):
                errors.append(f"paper #{i} ({p.get('name')}) is missing '{field}'")
        if p.get("section") not in ids:
            errors.append(f"paper '{p.get('name')}' has unknown section '{p.get('section')}'")
        for field in ("paper", "code"):
            if p.get(field) and not str(p[field]).startswith("https://"):
                errors.append(f"paper '{p.get('name')}': {field} must be an https:// URL")
        seen[(str(p.get("title", "")).lower(), p.get("venue"), p.get("year"))] += 1
    for (title, venue, year), n in seen.items():
        if n > 1:
            errors.append(f"duplicate entry: {title} ({venue} {year})")
    return errors


def build(data):
    sections, papers = data["sections"], data["papers"]
    by_section = {}
    for p in papers:
        by_section.setdefault(p["section"], []).append(p)

    template = TEMPLATE.read_text(encoding="utf-8")
    seen = Counter()
    # Headings of the template that precede the paper list take their anchors first.
    for line in template.split("{{PAPER_LIST}}")[0].splitlines():
        m = re.match(r"#{1,6} (.+)", line)
        if m:
            slugify(m.group(1).replace("{{TOC_TITLE}}", TOC_TITLE), seen)
    top = "#" + slugify(TOC_TITLE, Counter())
    anchors = {}  # section id -> anchor, used by see_also links
    for s in sections:
        s["_anchor"] = slugify(f"{s.get('emoji', '')} {s['title']}" if s.get("emoji") else s["title"], seen)
        if s.get("id"):
            anchors[s["id"]] = s["_anchor"]
    for p in papers:
        p.setdefault("_anchor", anchors.get(p["section"]))

    toc, body = [], []
    for s in sections:
        level, title = s["level"], s["title"]
        indent = "  " * (level - 2)
        toc.append(f"{indent}- [{title}](#{s['_anchor']})")

        heading = f"{s['emoji']} {title}" if s.get("emoji") else title
        body.append(f"{'#' * level} {heading}\n")
        if s.get("figure"):
            body.append(f'<p align="center">\n  <img src="{s["figure"]}" width="{s.get("width", "90%")}" alt="{title}">\n</p>\n')
            if s.get("caption"):
                body.append(f'<p align="center"><em>{s["caption"]}</em></p>\n')
        if s.get("description"):
            body.append(f"{s['description'].strip()}\n")

        items = by_section.get(s.get("id"), [])
        if items:
            meta = [f"*{s['context']}*"] if s.get("context") else []
            count = f"{len(items)} paper{'s' if len(items) != 1 else ''}"
            meta.append(count)
            meta.append(f"[🔝 Back to top]({top})")
            body.append(" · ".join(meta) + "\n")
            table = render_table(items)
            if s.get("collapsed"):
                table = f"<details>\n<summary>Show {count}</summary>\n\n{table}\n\n</details>"
            body.append(table + "\n")
        if s.get("see_also"):
            names = {p["name"]: p for p in papers}
            links = [f"[{n}](#{names[n]['_anchor']})" for n in s["see_also"] if n in names]
            missing = [n for n in s["see_also"] if n not in names]
            if missing:
                raise SystemExit(f"see_also of '{title}' refers to unknown methods: {missing}")
            body.append("Also discussed in this direction: " + ", ".join(links) + ".\n")

    out = (template.replace("{{PAPER_COUNT}}", str(len(papers)))
           .replace("{{TOC_TITLE}}", TOC_TITLE)
           .replace("{{TOC}}", "\n".join(toc))
           .replace("{{PAPER_LIST}}", "\n".join(body).rstrip() + "\n"))
    return re.sub(r"\n{3,}", "\n\n", out)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="fail if README.md is out of date")
    args = parser.parse_args()

    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    readme = build(data)
    if args.check:
        if not README.exists() or README.read_text(encoding="utf-8") != readme:
            print("README.md is out of date: run `python scripts/build_readme.py` and commit the result.", file=sys.stderr)
            sys.exit(1)
        print(f"README.md is up to date ({len(data['papers'])} papers).")
        return
    README.write_text(readme, encoding="utf-8")
    print(f"Wrote README.md with {len(data['papers'])} papers.")


if __name__ == "__main__":
    main()
