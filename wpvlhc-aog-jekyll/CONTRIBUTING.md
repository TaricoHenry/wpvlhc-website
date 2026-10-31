# Contributing

Use the Ruby version in `.ruby-version`. Read [README.md](README.md) for setup and [docs/content-guide.md](docs/content-guide.md) before editing church content.

1. Change source files, not `_site/` or the old WordPress installation.
2. Keep shared contact information in `_data/church.yml` and reuse existing layouts/includes.
3. Confirm factual church details and media permissions. Do not publish starter text, sample recordings, or unconfirmed schedules.
4. Use `relative_url` for internal template links and `absolute_url` for canonical metadata.
5. Run both production builds and link checks from the README.
6. Check affected pages on mobile and desktop, including keyboard navigation.

Do not add credentials, form submissions, SQL exports, or local configuration. Keep source assets small and document third-party assets in `docs/asset-credits.md`.

Dependency changes should update `Gemfile` and `Gemfile.lock` together. CSS uses native Sass modules and common breakpoints; frontend packages are not needed for ordinary content changes.
