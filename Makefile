# Makefile for vermaaslab.github.io
#
# BIBSRC points at the Better BibTeX auto-export file Zotero keeps up to
# date from the "MyPapers" collection. Override it on the command line if a
# given machine's Zotero data lives somewhere else, e.g.:
#   make freshbib BIBSRC=/some/other/path/MyPapers.bib
BIBSRC ?= $(HOME)/Documents/Zotero/MyPapers.bib
BIBDST := _bibliography/references.bib

.PHONY: freshbib serve build clean

## Copy the latest Zotero/Better BibTeX export into the site's bibliography.
freshbib:
	@test -f "$(BIBSRC)" || (echo "No bib file at $(BIBSRC) -- pass BIBSRC=/path/to/MyPapers.bib" && exit 1)
	cp "$(BIBSRC)" "$(BIBDST)"
	@echo "Updated $(BIBDST) from $(BIBSRC)"
	@echo "Next: git add $(BIBDST) && git commit -m 'Refresh bibliography' && git push"

## Build the site locally (requires bundle install once: `bundle install`).
build:
	bundle exec jekyll build

## Serve the site locally with live reload for previewing changes.
serve:
	bundle exec jekyll serve --livereload

## Remove local build output.
clean:
	rm -rf _site .jekyll-cache
