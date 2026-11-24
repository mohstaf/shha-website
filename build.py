#!/usr/bin/env python3
"""Build the SHHA website.

Each file in src/pages/ starts with a JSON block in an HTML comment:

    <!--meta {"title": "About", "description": "...", "nav": "about"} -->

The rest of the file is the page body. This script wraps every page in
src/layout.html, fills in {{> partial}} includes from src/partials/, copies
static/ and writes the finished site to public/.

Usage:  python3 build.py          build into public/
        python3 build.py --check  render every page without writing
"""

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "public"
SITE_NAME = "SHHA"
NAV_KEYS = ["about", "disorders", "help", "programmes", "news", "involved", "contact"]

META_RE = re.compile(r"^\s*<!--meta\s+(\{.*?\})\s*-->\s*", re.S)
INCLUDE_RE = re.compile(r"\{\{>\s*([\w-]+)\s*\}\}")


def include(text: str) -> str:
    def repl(m):
        path = SRC / "partials" / f"{m.group(1)}.html"
        if not path.exists():
            raise SystemExit(f"Missing partial: {path}")
        return include(path.read_text(encoding="utf-8").strip())
    return INCLUDE_RE.sub(repl, text)


def build_page(path: Path, layout: str) -> str:
    raw = path.read_text(encoding="utf-8")
    m = META_RE.match(raw)
    if not m:
        raise SystemExit(f"{path.name}: missing <!--meta {{...}} --> block")
    meta = json.loads(m.group(1))
    body = include(raw[m.end():])

    title = meta.get("title", "")
    full_title = meta.get("full_title") or (f"{title} | {SITE_NAME}" if title else SITE_NAME)
    lang = meta.get("lang", "en")
    html = layout
    for key in NAV_KEYS:
        html = html.replace(f"{{{{current:{key}}}}}", ' aria-current="page"' if meta.get("nav") == key else "")

    replacements = {
        "full_title": full_title,
        "description": meta.get("description", ""),
        "lang": lang,
        "lang_en": meta.get("lang_en", "index.html" if lang == "so" else path.name),
        "lang_so": meta.get("lang_so", "so.html"),
        "lang_current_en": ' aria-current="true"' if lang == "en" else "",
        "lang_current_so": ' aria-current="true"' if lang == "so" else "",
    }
    for key, value in replacements.items():
        html = html.replace(f"{{{{{key}}}}}", value)
    return html.replace("{{content}}", body.strip())


def main():
    layout = include((SRC / "layout.html").read_text(encoding="utf-8"))
    if "--check" in sys.argv:
        # Render every page in memory without writing anything.
        bad = []
        for page in sorted((SRC / "pages").glob("*.html")):
            if "{{" in build_page(page, layout):
                bad.append(page.name)
        if bad:
            raise SystemExit(f"Unfilled placeholders in: {', '.join(bad)}")
        print("All pages render.")
        return
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)
    pages = sorted((SRC / "pages").glob("*.html"))
    for page in pages:
        (OUT / page.name).write_text(build_page(page, layout), encoding="utf-8")
    leftover = [p.name for p in OUT.glob("*.html") if "{{" in p.read_text(encoding="utf-8")]
    if leftover:
        raise SystemExit(f"Unfilled placeholders in: {', '.join(leftover)}")
    print(f"Built {len(pages)} pages into {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
