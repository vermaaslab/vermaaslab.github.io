#!/usr/bin/env python3
"""Sanitize a Better BibTeX export for use with jekyll-scholar.

Strips artifacts that come from Better BibTeX's LaTeX-safety escaping but
that our (non-LaTeX) Liquid/CSL rendering pipeline doesn't decode cleanly:

- BibTeX's protective-brace `\relax` no-op (e.g. "{\relax Jeremy}" used to
  stop BibTeX's name parser from treating a capitalized word as a lowercase
  "von" particle) -- harmless in real LaTeX, but prints literally otherwise.
- LaTeX math-mode escaped angle brackets ("{$<$}inf{$>$}") that Better BibTeX
  emits when a field (usually a title, from upstream publisher/CrossRef
  metadata) contains raw HTML-ish subscript tags like "<inf>...</Inf>".
  These decode back into literal, often case-mismatched, unclosed HTML tags
  that corrupt the rest of the rendered page -- so they're stripped outright
  rather than converted, since the site doesn't need literal subscripts here.

Usage: sanitize_bib.py <path/to/references.bib>  (rewrites the file in place)
"""
import re
import sys


def sanitize(text):
    text = re.sub(r"\{\\relax\s+([^}]*)\}", r"\1", text)
    text = re.sub(r"\\relax\s*", "", text)
    text = re.sub(r"\{\$<\$\}/?[A-Za-z0-9]*\{\$>\$\}", "", text)
    return text


def main():
    if len(sys.argv) != 2:
        print("usage: sanitize_bib.py <path/to/references.bib>", file=sys.stderr)
        sys.exit(1)
    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        original = f.read()
    cleaned = sanitize(original)
    if cleaned != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"sanitized {path}")
    else:
        print(f"{path} already clean")


if __name__ == "__main__":
    main()
