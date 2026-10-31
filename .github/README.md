# Repository workflows

`workflows/check.yml` builds and checks root and subpath hosting on pull requests or manual runs. `workflows/pages.yml` builds, checks, and publishes on pushes to `main` or manual runs once GitHub Pages is enabled.

Keep this `.github/` directory at the repository root, alongside `Gemfile` and `_config.yml`. GitHub does not discover workflows inside a nested project folder. Select **GitHub Actions** as the Pages publishing source. See [setup instructions](../docs/github-pages.md).
