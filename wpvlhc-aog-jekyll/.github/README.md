# Repository workflows

`workflows/check.yml` builds and checks root and subpath hosting on pull requests or manual runs. `workflows/pages.yml` builds, checks, and publishes on pushes to `main` or manual runs once GitHub Pages is enabled.

These workflows become active only when `.github/` is at the new repository root. See [setup instructions](../docs/github-pages.md).
