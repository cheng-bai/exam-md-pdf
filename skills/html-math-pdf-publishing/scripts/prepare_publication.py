#!/usr/bin/env python3
"""Prepare a sibling, static HTML edition and an ASCII Vivliostyle entry."""

import argparse
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup


def normalized_text(node):
    copy = BeautifulSoup(str(node), "html.parser")
    for item in copy.select("script, style"):
        item.decompose()
    return re.sub(r"\s+", "", copy.get_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Already rendered HTML baseline")
    parser.add_argument("--output", required=True, type=Path, help="New HTML in the same directory")
    parser.add_argument("--title", required=True)
    parser.add_argument("--author", default="chengbai")
    parser.add_argument("--density", choices=("standard", "compact"), default="standard")
    parser.add_argument("--prefix", default="publication", help="Unique ASCII build-file prefix")
    parser.add_argument("--replace", action="store_true", help="Replace only the named generated outputs")
    args = parser.parse_args()
    source = args.source.expanduser().resolve(strict=True)
    output = args.output.expanduser().absolute()
    if output.suffix.lower() != ".html":
        parser.error("--output must end in .html")
    if output.parent.resolve() != source.parent or output.resolve() == source:
        parser.error("Write a different sibling HTML to preserve relative resources and the source")
    if not re.fullmatch(r"[a-z][a-z0-9-]*", args.prefix):
        parser.error("--prefix must be a lowercase ASCII filename stem")
    if output.is_symlink():
        parser.error("Refusing a symlink output")

    doc = BeautifulSoup(source.read_text(encoding="utf-8"), "html.parser")
    if not doc.head or not doc.body:
        parser.error("Input needs explicit head and body elements")
    if doc.select(".katex-error, .katex-render-error, mjx-merror"):
        parser.error("Formula errors must be fixed before layout")
    if any(not node.select_one(".katex, mjx-container, svg") for node in doc.select(".math")):
        parser.error("Render raw .math nodes first with the project's existing math renderer")
    ids = [node["id"] for node in doc.select("[id]")]
    if len(ids) != len(set(ids)):
        parser.error("Duplicate IDs must be fixed before generating TOC targets")
    if not doc.select_one("h1,h2,h3,h4,h5,h6"):
        parser.error("A publication with an automatic TOC needs headings")
    before = normalized_text(doc.body)
    used = set(ids)
    for index, heading in enumerate(doc.select("h1,h2,h3,h4,h5,h6"), 1):
        if heading.get("id"):
            continue
        candidate = f"section-{index:03d}"
        while candidate in used:
            candidate += "-h"
        used.add(candidate)
        heading["id"] = candidate

    css = output.parent / f"{args.prefix}-layout.css"
    alias = output.parent / f"{args.prefix}-entry.html"
    config = output.parent / f"{args.prefix}.config.mjs"
    targets = (output, css, alias, config, output.with_suffix(".pdf"))
    for target in targets:
        if (target.exists() or target.is_symlink()) and not args.replace:
            parser.error(f"Existing output requires a new prefix or explicit --replace: {target}")
        if target.is_dir():
            parser.error(f"Refusing to replace directory: {target}")
        if target != alias and target.is_symlink():
            parser.error(f"Refusing to replace symlink: {target}")
    if len(set(target.absolute() for target in targets)) != len(targets):
        parser.error("Output paths collide")
    if any(target.resolve() == source for target in targets):
        parser.error("A generated path would overwrite the input source")

    assets = Path(__file__).resolve().parent.parent / "assets"
    css_text = (assets / "paged.css").read_text(encoding="utf-8")
    if args.density == "compact":
        css_text += "\n" + (assets / "compact.css").read_text(encoding="utf-8")
    doc.head.append(doc.new_tag("link", rel="stylesheet", href=css.name))
    author = doc.select_one('meta[name="author"]')
    if author:
        author["content"] = args.author
    else:
        doc.head.append(doc.new_tag("meta", attrs={"name": "author", "content": args.author}))
    if doc.title:
        doc.title.string = args.title
    else:
        title = doc.new_tag("title")
        title.string = args.title
        doc.head.append(title)
    assert normalized_text(doc.body) == before
    settings = {
        "title": args.title, "author": args.author, "language": doc.html.get("lang", "zh-CN"),
        "size": "A4", "theme": "./" + css.name,
        "entry": [{"rel": "contents"}, {"path": alias.name, "title": args.title}],
        "toc": {"title": "目录", "sectionDepth": 3},
        "output": output.with_suffix(".pdf").name,
        "workspaceDir": "./." + args.prefix + "-cache",
    }
    output.write_text("<!doctype html>\n" + str(doc.html), encoding="utf-8")
    css.write_text(css_text, encoding="utf-8")
    if alias.exists() or alias.is_symlink():
        alias.unlink()
    alias.symlink_to(output.name)
    config.write_text("export default " + json.dumps(settings, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
    print(json.dumps({"html": str(output), "config": str(config), "entry": str(alias),
                      "density": args.density, "body_text_preserved": True}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
