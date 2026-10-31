# Page layouts

`default.html` owns the HTML document and shared header/footer. `page.html` adds a page title and content container. `post.html`, `event.html`, and `sermon.html` extend `page` with content-specific details. Defaults in `_config.yml` select layouts automatically.

Page content is injected through Liquid's `content` variable. Edit layouts only when the change should apply to every page of that type.
