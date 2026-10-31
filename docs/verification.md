# Migration verification

Verified locally on October 31, 2026, with Ruby 3.4.1 and Jekyll 4.4.1.

| Check | Result |
| --- | --- |
| Production build with strict front matter | Passed |
| Root-hosted build | 15 HTML pages; 320 local links/assets checked |
| Project path `/preview-site` | 15 HTML pages; 290 local links/assets checked |
| Feed and sitemap XML | Parsed successfully |
| Project-path canonical URLs and old-route redirects | Passed |
| Authoring files / WordPress runtime excluded from output | Passed |
| Isolated sample news, sermon, future event | 18 pages; 377 local links/assets checked |
| Future event detail page, confirmed Guyana time, upcoming/archive states | Passed |
| JavaScript syntax, workflow YAML, site/data YAML | Passed |
| Desktop homepage at 1440px | Reviewed in browser |
| Homepage and all main pages at 375px | No horizontal overflow or broken images detected |
| Mobile menu, Escape dismissal, focus return | Passed |
| Homepage browser console | No warnings or errors observed |

The populated-content tests used a temporary source copy outside this website, so no test announcements, recordings, or events are published. Both honest empty states and populated layouts were exercised. Event files use descriptive names without date prefixes so future event schedules do not suppress their detail pages.

The lockfile includes both Apple Silicon macOS and x86-64 Linux platforms. GitHub Actions workflows were checked locally as configuration; they have not run against a new repository or published anything. External Facebook/Maps/email destinations were carried over or derived from the supplied contact information, not submitted to or changed during verification.

For repeatable checks, use the commands in the [README](../README.md). For launch information still needing confirmation, see [migration notes](migration.md).

## Repository-layout correction — October 31, 2026

Inspected the public Actions run [41239971420](https://github.com/TaricoHenry/wpvlhc-website/actions/runs/41239971420). It failed in the default Pages Jekyll 3.10 build because it searched the repository-root `_includes/` while the project, configuration, and custom workflows were nested inside `wpvlhc-aog-jekyll/`.

Moved the project files to the Git repository root without staging, committing, or pushing. Preserved the site content/assets and locked dependencies. Merged the existing root ignore rules with the project's rules, and excluded the local source ZIP from publishing.

Verified from the corrected root with Ruby 3.4.1, Bundler 2.6.2, and Jekyll 4.4.1:

| Check | Result |
| --- | --- |
| Production build, explicit root path | 15 HTML pages; 290 local links/assets; passed |
| Production build, `/preview-site` | 15 HTML pages; 290 local links/assets; passed |
| Production build, configured `/wpvlhc-website` | 15 HTML pages; 290 local links/assets; passed |
| Homepage canonical and sitemap URLs | Expected project origin and repository path |
| Root workflow locations and YAML syntax | Passed |
| Source ZIP and handover excluded from output | Passed; original ZIP retained locally |

No templates, styles, browser behavior, church content, or dependency versions changed. Browser review was not repeated for the filesystem/hosting correction. The custom workflow still needs a hosted run after the user selects **GitHub Actions** in Pages settings and pushes the corrected layout. No repository setting was changed and no hosted deployment success is claimed.
