# Editing and publishing content

All paths below are relative to the Jekyll repository root. Use UTF-8 text, two spaces for YAML indentation, and no tabs. Quote text containing `: ` or `#`. Keep paths starting with `/assets/` or `/contact/`; templates add the repository prefix using `relative_url`.

## Church information

Edit `_data/church.yml`. This is the shared source for email, phone numbers, address, Facebook, service times, livestream, and giving. Leave optional URLs as `""` until a verified destination exists. The site shows real contact alternatives automatically.

Service times are a list of confirmed descriptions:

```yaml
service_times:
  - "Sunday worship: your confirmed time"
```

Do not infer a weekly service time from the old one-off events. Replace the regional `map_url` with an exact church pin if one is verified. Giving links should point to the church's approved provider; payments are handled there.

## Homepage, navigation, leaders, and ministries

- `_data/home.yml`: hero, prayer, and visit copy. Keep the headline short enough for a mobile screen.
- `_data/navigation.yml`: ordered `title` / `url` pairs. Create the destination page before adding a link.
- `_data/leadership.yml`: names, roles, portraits, and an optional Facebook URL.
- `_data/ministries.yml`: ministry names and descriptions.
- `_data/services.yml`: service cards, images, and email enquiry subjects.

`index.html` controls the homepage section order. Shared sections live in `_includes/sections/`.

## News

1. Copy `docs/examples/news.md` into `_posts/`.
2. Rename it `YYYY-MM-DD-short-title.md` using the intended publication date.
3. Set `title`, `date`, and `description` between the `---` markers; write the article below.
4. Remove `published: false` when approved for publication.

News appears automatically on `/news/`, the homepage, and `/feed.xml`. Future-dated posts are hidden until a build happens after their date. GitHub Pages is not a scheduled publisher; rebuild after the publication time.

For a working draft use `_drafts/short-title.md`. Preview unpublished posts with `bundle exec jekyll serve --drafts --unpublished`. Never add those flags to the production workflow.

## Sermons

1. Copy `docs/examples/sermon.md` into `_sermons/short-title.md`.
2. Fill in the real title, date, preacher, description, and optional scripture.
3. Set `video_url` to the exact published video. An optional `audio_path` can point to a local audio file in `/assets/audio/`.
4. Remove `published: false` only after checking the content and recording link.

The site adds the sermon page and cards automatically, newest first. Videos are linked rather than embedded, so third-party players do not load on page visits. Keep large recordings on an appropriate media host.

## Events

1. Copy `docs/examples/event.md` into `_events/short-title.md` (or `short-title-2027.md` for a yearly event).
2. Set `starts_at` and `ends_at` as ISO timestamps **with an explicit offset**, e.g. `2027-05-26T08:00:00-04:00` for Guyana.
3. Add the location and description. Use `time_confirmed: true` when the schedule is confirmed; the time is shown in the site's Guyana timezone.
4. Remove `published: false` to publish.

The list sorts by `starts_at`, not the filename. Do not start event filenames with `YYYY-MM-DD` or give them a future `date` field: Jekyll treats that as a future publication date and can hide the detail page. The event schedule belongs in `starts_at` and `ends_at`, so upcoming events can be published today.

Events move into the archive after `ends_at` (or `starts_at` if no end is provided), **at the next build**. Run the Pages workflow to refresh the static archive after an event. There is no background event service or automatic weekly schedule.

The imported 2024 events keep their source UTC timestamps, but their clock times are hidden because the WordPress timezone was not configured for Guyana. Confirm the original timezone before enabling their times.

## Add a page

Create `_pages/your-page.md`:

```yaml
---
title: Your page title
description: A useful one-sentence summary.
permalink: /your-page/
---
Your page content here.
```

Markdown pages use the shared `page` layout. Set `wide: true` for a grid layout. To add reusable HTML inside Markdown, use `markdown="1"` on the container when needed. Internal links in Liquid templates should use `{{ '/contact/' | relative_url }}`; absolute domain paths without that filter break project-repository hosting.

## Images

Use descriptive, lowercase, hyphenated filenames in the appropriate `assets/images/` folder. Resize oversized photos before adding them. Include an `alt` description when the image conveys content, or `alt=""` when decorative, and include `width` / `height` to reduce layout shifts. All images except the top banner should normally use `loading="lazy"`.

## Before a change goes live

Build and run the checker from the README. Review the affected pages at desktop and mobile widths. Test navigation with the keyboard, inspect the actual enquiry/recording destination, and confirm dates, names, and contact details with the church. Restart the preview server after a configuration change.
