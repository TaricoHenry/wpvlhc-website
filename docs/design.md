# Design and layout

The Jekyll site follows the customized **FSE Spiritual** WordPress source, including its saved database templates rather than just the untouched theme screenshot.

## Visual rules

- Orange `#e8772e` is the original accent; charcoal `#2e2d2a` and the dark `#15181b` footer also come from the theme.
- Poppins is self-hosted in regular, semibold, and bold weights.
- The wide content container is 1170px, matching the theme setting.
- The homepage uses the original church image with a dark overlay, a large centered welcome message, and clear calls to visit or connect online.
- Section headings retain the eyebrow, centered title, and short orange rule.
- The original leadership portraits, service images, and prayer photo are reused.
- White and light grey sections alternate, with a dark contact-rich footer.

Text links use a darker orange and orange buttons use dark text for readable contrast. Mobile layouts stack cards, and navigation becomes a keyboard-operable expandable menu. Links remain available if JavaScript is disabled. The site supports a skip link, visible focus, reduced motion, semantic headings, and descriptive image alternatives.

## Files to change

| Purpose | File |
| --- | --- |
| Brand colours, container width | `_sass/_tokens.scss` |
| Type, element defaults, focus, motion | `_sass/_base.scss` |
| Grids, sections, footer, breakpoints | `_sass/_layout.scss` |
| Hero, buttons, header/menu, cards | `_sass/_components.scss` |
| Sass entry point | `assets/css/main.scss` |
| Menu interactions | `assets/js/main.js` |

Breakpoints use 64rem for the main navigation, 48rem for stacked content, and 32rem for narrow cards. Check at about 375px, 768px, and 1440px after changing layout rules. Avoid editing `_site/assets/css/main.css`: it is generated.
