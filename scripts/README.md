# Verification tools

Run `python3 scripts/check_site.py` after a Jekyll build with `--baseurl ""`, from the repository root. For project-path builds pass the same `--baseurl /your-path` used by Jekyll. The default production configuration uses `/wpvlhc-website`, so a build without an override needs `python3 scripts/check_site.py --baseurl /wpvlhc-website`.

Uses only Python's standard library. Checks local targets/fragments, CSS assets, image attributes, duplicate IDs, headings/landmarks, feed/sitemap XML, leftover WordPress markup, and non-public source leaking into output. External destinations and visual layout need separate review.
