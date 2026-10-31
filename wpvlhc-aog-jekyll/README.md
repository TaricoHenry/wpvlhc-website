# WPVLHC AOG — Jekyll website

The standalone website for **World Prayer Vision Life Healing Center AOG**, Anna Catherina, Guyana. This folder is the **root of the new website repository**: copy its contents, including hidden files, into your new repository.

Built with Jekyll 4, Liquid, Sass, and a small navigation script. No WordPress, database, npm installation, or paid theme is required.

Continuing in a new Codex project? Read [HANDOVER.md](HANDOVER.md) for the current state, decisions, verification, known gaps, and next steps.

## Run locally

Install Ruby **3.4.1** (see `.ruby-version`), Bundler, and Python 3 (for the link checker). Use a Ruby version manager rather than the macOS system Ruby. Then run these commands **inside this folder**:

```sh
bundle install
bundle exec jekyll serve --livereload
```

Open <http://localhost:4000>. Stop the server with `Ctrl+C`. Restart after changing `_config.yml`.

## Verify before publishing

```sh
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py

# Also check a GitHub Pages project-repository path:
JEKYLL_ENV=production bundle exec jekyll build --baseurl /preview-site
python3 scripts/check_site.py --baseurl /preview-site
```

The checker verifies internal links and fragments, CSS assets, image attributes, page landmarks, feed/sitemap XML, and that authoring files are excluded from the public output. It does not contact external websites or replace a browser/accessibility review. `_site/` is disposable build output; never edit it.

## Where everything lives

```text
.
├── _config.yml           # Site settings, collections, defaults, build exclusions
├── _data/               # Church contact details, navigation, leadership, services
├── _drafts/             # Unpublished news drafts
├── _events/             # One Markdown file per event
├── _includes/           # Reusable header, footer, cards, homepage sections
│   └── sections/        # Leadership, sermons, special services
├── _layouts/            # Shared page, post, event, sermon HTML templates
├── _pages/              # About, ministries, contact, news, sermons, events, privacy
├── _posts/              # Published news: YYYY-MM-DD-title.md
├── _sass/               # Colours, typography, layout, reusable components
├── assets/
│   ├── css/             # Sass entry point → /assets/css/main.css
│   ├── fonts/           # Self-hosted Poppins and its licence
│   ├── images/          # Church, leadership, and services image folders
│   └── js/              # Accessible mobile navigation
├── docs/                # Setup, editing, design, migration notes, content examples
├── scripts/             # Offline built-site checker
├── .github/workflows/   # Pull-request checks and future GitHub Pages publishing
├── Gemfile              # Ruby dependencies
├── Gemfile.lock         # Reproducible dependency versions
├── index.html           # Homepage: section order and composition
├── 404.html             # Custom missing-page screen
└── robots.txt           # Crawler directions and sitemap location
```

Each authoring area has a short README explaining its role. Those READMEs are excluded from the published site.

## Make common changes

| Change | Edit |
| --- | --- |
| Email, phone, address, Facebook, giving link, service times | `_data/church.yml` |
| Homepage headline and introduction | `_data/home.yml` |
| Navigation links | `_data/navigation.yml` |
| Leaders and portraits | `_data/leadership.yml`, `assets/images/leadership/` |
| Ministries or service enquiries | `_data/ministries.yml`, `_data/services.yml` |
| Colours and sizing | `_sass/_tokens.scss` |
| Page content | `_pages/` |
| Add a news post, sermon, or event | Follow [the content guide](docs/content-guide.md) |

## GitHub Pages, when you're ready

Follow [docs/github-pages.md](docs/github-pages.md). The included workflow builds and checks the site before deployment, and obtains the correct domain and repository path from GitHub. You still need to create your repository and select **GitHub Actions** as its Pages source. Nothing has been committed or deployed as part of this migration.

## Migration notes

The orange/charcoal palette, Poppins type, church banner, leadership portraits, ministry list, special services, and contact details come from the WordPress source. Two 2024 events are preserved as **past events**. Theme demo sermons and the WordPress starter post are not published as genuine church content. Booking and prayer actions use email/phone; online giving appears only when a real destination is configured.

See [migration decisions](docs/migration.md), [design notes](docs/design.md), and [asset provenance](docs/asset-credits.md). The original WordPress copy is outside this folder and has not been modified. Do not copy its database, configuration, plugins, or logs into the new website repository.
