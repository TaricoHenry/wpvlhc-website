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
