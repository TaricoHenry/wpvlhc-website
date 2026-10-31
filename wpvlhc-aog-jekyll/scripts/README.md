# Verification tools

Run `python3 scripts/check_site.py` after a Jekyll build, from the repository root. For project-path builds pass the same `--baseurl /your-path` used by Jekyll.

Uses only Python's standard library. Checks local targets/fragments, CSS assets, image attributes, duplicate IDs, headings/landmarks, feed/sitemap XML, leftover WordPress markup, and non-public source leaking into output. External destinations and visual layout need separate review.
