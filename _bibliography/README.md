# Adding a publication to the site

Publications are no longer hand-edited YAML (`_data/publist.yml` is retired).
The Publications page now renders directly from `_bibliography/references.bib`
via the `jekyll-scholar` plugin.

## Normal case: you added a paper to Zotero

1. Make sure the item is in (or drag it into) your **MyPapers** Zotero collection.
   Better BibTeX (BBT) keeps its usual auto-export of that collection up to
   date at `~/Documents/Zotero/MyPaper.bib` (Zotero's normal export location --
   nothing to change there).
2. (Optional) Curate how it appears on the site by adding lines to the item's
   **Extra** field in Zotero, one per line, using `=` (not `:`) so text passes
   through unescaped and markdown links survive:

   ```
   tex.highlight = 1
   tex.image = my-cover.png
   tex.abstract = One sentence describing why this paper is cool.
   tex.news1 = Selected for the journal cover!
   tex.news2 = There's also a [news writeup](https://example.edu/story) about this.
   ```

   - `tex.highlight = 1` -- features the paper in the "Highlights" section (with
     image + description); omit it (or leave it off) for the plain Full List entry.
   - `tex.image` -- filename under `images/pubpic/` (or a relative path) for the
     cover image shown in Highlights.
   - `tex.abstract` -- one-line description shown in Highlights.
   - `tex.news1` -- short, bold flag (award, cover pick, etc.)
   - `tex.news2` -- longer note/summary; markdown links (`[text](url)`) work.
3. BBT re-exports `~/Documents/Zotero/MyPaper.bib` automatically as soon as
   you save the item.
4. From the repo root: `make freshbib` copies that file into
   `_bibliography/references.bib`.
5. `git add _bibliography/references.bib && git commit -m "Add <paper>" && git push`.
   The GitHub Actions workflow (`.github/workflows/build-deploy.yml`) rebuilds
   and redeploys the site automatically.

No Jekyll/Ruby installation is required for this -- only git, make, and Zotero.

## One-time setup per computer

Nothing Zotero-side to configure -- BBT already auto-exports the **MyPapers**
collection to its normal location. If a given machine keeps its Zotero data
somewhere other than `~/Documents/Zotero/MyPaper.bib`, override it on the
command line: `make freshbib BIBSRC=/path/to/MyPaper.bib`. Zotero's own sync
keeps the library itself consistent across machines.

## Fields jekyll-scholar/the site templates use

Standard BibTeX fields (`title`, `author`, `journal`, `volume`, `pages`, `year`,
`doi`, `url`) render the citation line. The custom `tex.*` fields above map to
plain custom BibTeX fields (`abstract`, `image`, `highlight`, `news1`, `news2`)
that the two custom rendering templates read:

- `_layouts/highlight.html` -- "Highlights" cards, laid out as a CSS grid
  (used for entries with `highlight = 1`)
- `_layouts/full.html` -- the plain "Full List" entries (used for everything)

These live under `_layouts/`, not `_bibliography/` -- jekyll-scholar's
`bibliography_template`/`-T` option only resolves against Jekyll's layout
registry (built from `_layouts/`), so a template placed anywhere else is
silently ignored (it prints its own filename as literal text instead).

## Bib sanitization

Publisher/CrossRef metadata occasionally contains raw formatting artifacts
(e.g. HTML-ish subscript tags embedded in a title) that Better BibTeX escapes
for LaTeX safety on export, but that decode back into broken/unclosed HTML
once run through our (non-LaTeX) rendering pipeline. `make freshbib` runs
`scripts/sanitize_bib.py` on the copied file automatically to strip known
offenders (BibTeX's `\relax` protective brace, LaTeX math-mode-escaped angle
brackets). If a future paper's title/author renders oddly, check the raw
`.bib` entry for stray backslash commands or escaped brackets and extend
that script.

## Draft abstracts

For papers that don't have a `tex.abstract` yet, a `tex.abstract_draft` line may
be sitting in the item's Extra field instead -- these are AI-drafted, grounded
in the paper's real journal abstract, and are **not** read by the site
templates (only `abstract` is). Review the draft in Zotero, edit it to taste,
then rename the Extra-field key from `tex.abstract_draft` to `tex.abstract`
(and delete/keep the draft line as you prefer) to make it live. Setting
`tex.highlight = 1` at the same time will feature the paper in Highlights.

## Migration note

`_bibliography/references.bib` was bootstrapped from the old `_data/publist.yml`
(37 papers). All 37 items' `tex.highlight`/`tex.image`/`tex.abstract`/`tex.news1`/
`tex.news2` curation has been copied into the corresponding items' Extra field
in the **MyPapers** Zotero collection (via the Zotero Web API), so `make freshbib`
followed by a BBT export now reproduces the old site's Highlights/news exactly.

`_data/publist.yml` itself has NOT been deleted -- it's now unused by the site
but kept as a reference for a little while longer.
