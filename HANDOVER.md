# WPVLHC AOG — handover for the next Codex project

Prepared October 31, 2026. This records the state at handover; inspect the new checkout before assuming it is unchanged.

## Repository follow-up — October 31, 2026

The user created [TaricoHenry/wpvlhc-website](https://github.com/TaricoHenry/wpvlhc-website) after the migration. Its first two Pages builds failed because the Jekyll source and `.github/workflows/` were committed inside `wpvlhc-aog-jekyll/`. GitHub ran its default Jekyll 3.10 builder at the outer repository root and could not find `sections/leadership.html`.

The local correction moves the source, including hidden files and workflows, directly to the Git repository root. `_config.yml` now has the project address (`https://taricohenry.github.io`, `/wpvlhc-website`), and the local source ZIP is excluded from publishing. Use the current [README](README.md) commands: clear `baseurl` explicitly when previewing or checking root hosting.

These follow-up changes are uncommitted. The user must select **GitHub Actions** in repository **Settings → Pages**, then commit/push the corrected layout to run the custom Jekyll 4 workflow. No commit, push, settings change, or deployment was made by Codex. The original migration record below is historical; its unknown-repository/address statements predate this follow-up.

## Start here

The WordPress-to-Jekyll migration has been implemented and verified locally. Continue working on this Jekyll site in the new project. The user wants the original church style preserved, conventional structure, clear documentation, and eventual GitHub Pages hosting.

**The user explicitly requested no commits.** Codex has made no commits, pushes, remote changes, or deployment. The user created the repository after migration; the local follow-up above corrects its layout. Preserve the no-commit boundary unless the user gives new instructions.

Read [README.md](README.md), then the focused guides below. Inspect Git status and any project instructions before editing. Preserve existing user changes.

## What belongs in the new project

The contents of the old workspace's `website/jekyll/` folder become the **new repository root**. `_config.yml`, `Gemfile`, `index.html`, this handover, and `.github/` should be directly inside that root.

Copy hidden source files too: `.github/`, `.ruby-version`, `.gitignore`, and `.editorconfig`. Omit generated/local files: `_site/`, `.jekyll-cache/`, `.jekyll-metadata`, `.sass-cache/`, `.bundle/`, and `vendor/`.

The old workspace was `/Users/tarico/git/Personal/WPVLHC-AOG`. Its `website/wpvlhc-aog/` folder is a preserved local WordPress backup, with a database, configuration, and logs. It had extensive pre-existing changes and was not modified by this migration. **Do not bring that backup into the new public repository.** The Jekyll build is independent of it; the next project does not need it to run.

## Implemented site

- Homepage with church-photo banner, leadership, sermons, special services, prayer requests, visit information, and news.
- About, ministries, sermons, events, contact, news, privacy, and custom 404 pages.
- Reusable layouts, includes, cards, and data-driven content.
- News posts and dedicated event/sermon collections, with copyable unpublished examples.
- Responsive navigation with progressive enhancement, a skip link, visible focus, and Escape-key dismissal.
- Self-hosted Poppins fonts and original church/leadership images, with asset provenance and licences documented.
- SEO metadata, canonical URLs, RSS, sitemap, robots file, and redirects for migrated WordPress routes.
- Offline built-site checker, locked dependencies, and prepared GitHub Actions checks/publishing.
- README files explaining each authoring area, plus editing, design, migration, and hosting guides.

## Technical baseline

| Item | Current choice |
| --- | --- |
| Generator | Jekyll 4.4.1, declared as `~> 4.4` in `Gemfile` |
| Ruby | 3.4.1 in `.ruby-version` |
| Templates/content | Liquid, HTML, Markdown, YAML |
| Styles | Sass modules, compiled by Jekyll |
| Browser script | Plain JavaScript for navigation |
| Checker | Python 3 standard library; no Python packages required |
| Plugins | `jekyll-feed`, `jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-redirect-from` |
| Lockfile platforms | Apple Silicon macOS and x86-64 Linux |
| Site timezone | `America/Guyana` |
| Hosting | GitHub Pages via the included custom Actions workflow |

There is no npm build, database, WordPress runtime, booking backend, payment processing, or on-site form submission. Email links open the visitor's mail app. Videos use external recording links rather than embedded players.

## Where to edit

| Task | Location |
| --- | --- |
| Contact details, service times, social/giving/stream URLs | `_data/church.yml` |
| Homepage copy | `_data/home.yml` |
| Main navigation | `_data/navigation.yml` |
| Leaders and portraits | `_data/leadership.yml`, `assets/images/leadership/` |
| Ministry/service cards | `_data/ministries.yml`, `_data/services.yml` |
| Homepage composition | `index.html`, `_includes/sections/` |
| Main page content | `_pages/` |
| News, drafts, events, sermons | `_posts/`, `_drafts/`, `_events/`, `_sermons/` |
| Shared document/page templates | `_layouts/`, `_includes/` |
| Brand colours and sizing | `_sass/_tokens.scss` |
| Typography, grids, components | Other files in `_sass/` |
| Mobile navigation behaviour | `assets/js/main.js` |
| Configuration and public-build exclusions | `_config.yml` |
| Offline verification | `scripts/check_site.py` |

## Design decisions to preserve

The source was the customized **FSE Spiritual** WordPress theme and its saved database templates, not just the stock theme screenshot. The original visual identity is orange `#e8772e`, charcoal `#2e2d2a`, a dark `#15181b` footer, Poppins, and a 1170px content container. Text links use darker orange for contrast; orange buttons use dark text.

Keep the church-photo hero, actual leadership portraits, centered section headings with orange rules, alternating white/light-grey sections, and contact-rich footer. The layout was reviewed on desktop and phones. See [docs/design.md](docs/design.md) for the implementation map.

## Content decisions and known gaps

1. **No invented church news or sermons.** The WordPress sermon entries were theme demos without verified recordings. Public sermon/news lists currently show useful Facebook alternatives. `_posts/` and `_sermons/` contain explanatory READMEs, not genuine entries. The original WordPress starter post is retained only in `_drafts/hello-world.md`.
2. **Two real 2024 event records were retained as archive entries.** They are Guyana Day Service on May 26 and Youth Ministry on May 25. Their source timezone was `UTC+0`; timestamps were preserved but clock times are hidden with `time_confirmed: false` pending confirmation.
3. **Weekly service times are unknown.** `_data/church.yml` has `service_times: []`. Ask for confirmed times when that information is needed; do not infer them from the old one-off events.
4. **Giving and livestream destinations are not configured.** Their values are empty strings. The site uses giving enquiries and the source Facebook page until real URLs are supplied.
5. **The map points to Anna Catherina generally.** An exact church pin was not available in the source.
6. **Names, roles, email, and phone numbers come from the snapshot.** They need current church confirmation before launch. A mismatched WordPress phone target was corrected to follow its displayed number.
7. **Some service images are illustrative stock photos.** They do not document actual church ceremonies or the hall. Keep the credits; do not invent an unrestricted licence for church assets.

These are content/configuration gaps, not unfinished payment, booking, streaming, or calendar integrations. Expand functionality only when requested.

## Important implementation traps

- **Use `relative_url` for internal template links and assets.** The site must work at both `/` and a project path such as `/repository-name`. Use `absolute_url` for absolute metadata where needed.
- **Do not prefix event filenames with `YYYY-MM-DD`.** Use `_events/event-name.md` or `event-name-2027.md`. A future date prefix can make Jekyll omit the event detail page even while the listing links to it. The schedule belongs in `starts_at` and `ends_at`, with explicit offsets; do not set a future publication `date` on an upcoming event.
- **Jekyll 4.4 does not accept `build --url`.** Production domain overrides must come from a configuration file. The Pages workflow generates a temporary YAML override using GitHub's origin/base-path outputs.
- **The site is static.** Upcoming/archive status and future news visibility change only when it is rebuilt. No scheduled rebuild automation has been configured.
- **Drafts stay private in normal builds.** Do not add `--drafts`, `--unpublished`, or `--future` to production to work around content mistakes.
- **Do not edit `_site/`.** It is disposable output. Documentation and authoring files, including this handover, are excluded from the build.
- **Use the selected Ruby version.** The old Mac's shell sometimes fell back to system Ruby despite installed newer tools. Check `ruby --version` and `bundle --version` before diagnosing gem failures. No temporary gem installation or machine-specific path is needed by the project.

## Run and verify in the new checkout

From the new repository root, with Ruby 3.4.1 selected:

```sh
bundle install
bundle exec jekyll serve --livereload --baseurl ""
```

Preview at <http://localhost:4000>. Restart after `_config.yml` changes. Stop the preview before switching to other build output if necessary.

```sh
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter --baseurl ""
python3 scripts/check_site.py

JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter --baseurl /preview-site
python3 scripts/check_site.py --baseurl /preview-site
```

The checker covers internal links/fragments, CSS assets, image attributes, duplicate IDs, page headings/landmarks, feed/sitemap XML, leftover WordPress markup, and publication boundaries. It does not check external destinations or replace browser review.

### Checks already completed

The source at migration handover passed production builds and link checks for root hosting (15 HTML pages, 320 local links/assets) and `/preview-site` hosting (15 pages, 290 local links/assets). Isolated populated-content fixtures exercised news, sermon, and future-event pages (18 pages, 377 local links/assets), including confirmed Guyana times, canonical URLs, feeds, and redirects.

Desktop homepage review at 1440px and phone review at 375px found no horizontal overflow or broken images on the main pages. Mobile menu behaviour, Escape dismissal, and focus return passed. No homepage browser-console warnings/errors were observed. Workflow/site/data YAML and JavaScript syntax were checked.

The temporary fixtures and preview server are not part of the site. GitHub Actions has **not** run against the future repository; Linux support is represented in the lockfile but no hosted deployment is claimed. Details: [docs/verification.md](docs/verification.md).

## GitHub Pages state

`url` and `baseurl` now target `https://taricohenry.github.io/wpvlhc-website/`. The custom workflow overrides them with GitHub metadata. The default Pages builder failed on the old nested layout; no successful hosted deployment is claimed. Select **GitHub Actions** as the Pages source and push the local layout correction to run the intended workflow.

- `.github/workflows/check.yml` checks root/subpath builds on pull requests or manual runs; it does not publish.
- `.github/workflows/pages.yml` builds, checks, and deploys on pushes to `main` or manual runs once Pages is enabled. It gets the actual domain and base path from GitHub and uploads only `_site/`.
- The workflow files must be at the new repository root. They do not activate from their nested location inside the old workspace.
- When the user is ready, follow [docs/github-pages.md](docs/github-pages.md): select **GitHub Actions** as the Pages source, check the default branch, configure the address, and run the workflow. No speculative custom domain or `CNAME` was added.

## Suggested first steps for the next session

1. Read this handover and the new project's instructions; inspect its root and Git status.
2. Confirm that all source and hidden files were carried over, then run the documented build/check commands.
3. Continue with the user's next requested change. Preserve the existing design and content decisions unless asked to revise them.
4. As launch preparation becomes relevant, collect confirmed service times, current contact/leadership details, exact map pin, real sermon/news content, and approved giving/livestream URLs.
5. Leave committing and publishing to the user until they authorize those actions.

## Documentation index

- [README.md](README.md): setup, layout, and everyday changes.
- [docs/content-guide.md](docs/content-guide.md): content conventions and publishing examples.
- [docs/github-pages.md](docs/github-pages.md): new repository and hosting setup.
- [docs/design.md](docs/design.md): visual identity and responsive rules.
- [docs/migration.md](docs/migration.md): source mapping, redirects, and content decisions.
- [docs/asset-credits.md](docs/asset-credits.md): image/font provenance and licences.
- [docs/verification.md](docs/verification.md): verification record and limits.
- [CONTRIBUTING.md](CONTRIBUTING.md): editing and verification conventions.
