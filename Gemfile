source 'https://rubygems.org'

# NOTE: this site used to rely on the "github-pages" meta-gem, which lets
# GitHub build the Jekyll site natively on every push. jekyll-scholar (used
# for the BibTeX-driven Publications page) is NOT on GitHub Pages' allowlist
# of plugins for that native build, so the site is now built and deployed by
# the GitHub Actions workflow in .github/workflows/build-deploy.yml instead.
# That means the plugins GitHub Pages used to activate implicitly now need
# to be listed explicitly here and in _config.yml's `plugins:` list.
gem "jekyll", "~> 4.3"
gem "kramdown", ">= 2.3.1"
gem "kramdown-parser-gfm"

group :jekyll_plugins do
  gem "jekyll-sitemap"
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "jekyll-scholar", "~> 7.0"
end

gem "webrick", "~> 1.8"
