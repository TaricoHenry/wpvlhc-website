# WordPress → Jekyll migration

## Source inspected

The local WordPress copy is `../wpvlhc-aog/` relative to this folder. Public content was inspected from `app/sql/local.sql`, along with the `fse-spiritual` theme and `wp-content/uploads/2024/05/`. No database/user accounts, form submissions, credentials, configuration, or plugin files are included in the new site. The existing WordPress working tree was already modified before migration and was preserved.

## Content decisions

| Source | Jekyll destination / treatment |
| --- | --- |
| Saved home template (post 36) | `index.html`, `_data/home.yml`, section includes; preserves the layout's intent without WordPress block wrappers |
| Header/footer (7, 8) | Shared includes, centrally managed navigation and contact data |
| Leadership (45) | `_data/leadership.yml`, original portraits of Akini Cummings and Kwayon Duncan |
| Special services (84) | `_data/services.yml`, real email enquiry links for marriage, child dedication, funerals, and hall bookings |
| Ministry page (163) | `/ministries/`; all eight ministry names retained |
| Calendar page (176) | `/events/`; static upcoming/archive listing replaces the plugin calendar |
| Guyana Day Service (183) | Archived event dated May 26, 2024 |
| Youth Ministry event (189) | Archived event dated May 25, 2024 |
| Demo sermon block (89) | Not published: example sermon titles/descriptions had no recording URLs and were not verified church messages |
| WordPress “Hello world!” (1) | Retained in `_drafts/hello-world.md`, not published |
| Privacy page (3) | Replaced WordPress accounts/comments/cookies boilerplate with a short description of this static site's actual behaviour |
| Trashed pages, revisions, auto-drafts | Not migrated |
| Hidden stock-theme sections / lorem ipsum | Not migrated as genuine church content |

## Old URL continuity

Static `jekyll-redirect-from` redirects preserve these routes, including under a GitHub Pages repository path:

| Old route | New route |
| --- | --- |
| `/departments-and-teams-for-service/` | `/ministries/` |
| `/calendar-of-events/` | `/events/` |
| `/event/guyana-day-service/` | `/events/guyana-day-service-2024/` |
| `/event/youth-ministry/` | `/events/youth-ministry-2024/` |
| `/privacy-policy/` | Preserved |

Redirects are static HTML pages, not server-side 301 rules. If switching from a live WordPress domain, keep any needed host-level redirects there. GitHub Pages cannot resolve WordPress PHP routes, admin URLs, or query-string permalink IDs. Keep uploaded source-media URL redirects at the old host if other sites rely on them.

## Information to confirm before launch

- **Current contact information:** email, phone numbers, names, and roles are from the supplied snapshot, not a live church-directory check. The old footer's first phone label and its `tel:` target disagreed; the new phone link follows its displayed number, `+592 600 0200`.
- **Weekly service times:** none were established in the source. The site asks visitors to contact the church; add confirmed times to `_data/church.yml`.
- **Livestream and giving URLs:** the old buttons had no working destinations. Facebook and giving enquiries are used until approved links are configured.
- **Event times:** source events were saved as `UTC+0`, while Guyana uses a different offset. Their original timestamps are retained but clock times are not displayed until confirmed. They remain clearly archived.
- **Church map pin:** the source linked to Anna Catherina generally. No precise church coordinates were invented.
- **Sermons and news:** add real, approved content through the documented collections. Honest empty states link to the existing Facebook page in the meantime.

Email actions open the visitor's mail app; they do not submit forms, book a date, or confirm payment. No booking/payment backend has been invented. Theme stock images illustrate service categories rather than documenting actual church ceremonies.

## Scope and handoff

The new folder is a self-contained repository candidate, with conventional Jekyll content, shared layouts, self-hosted assets, documentation, locked dependencies, and GitHub Pages workflows. No commit, repository creation, remote update, or publication was performed. The old WordPress installation remains outside the site source.
