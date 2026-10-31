# Publish to GitHub Pages later

This guide prepares a **new repository whose root is this Jekyll folder**. No repository creation, commit, remote change, or deployment was performed during the migration.

## 1. Prepare your repository

Copy the **contents** of `website/jekyll/` into your new repository root, including `.github/`, `.ruby-version`, `.gitignore`, and `.editorconfig`. Copy source files only: omit `_site/`, `.jekyll-cache/`, `.jekyll-metadata`, `.bundle/`, and `vendor/` if present. Your new repository should have `_config.yml`, `Gemfile`, and `index.html` directly at its root.

The old `website/wpvlhc-aog/` folder contains a local WordPress installation and database. Keep it as a private migration backup, outside the new public repository. The workflows assume the Jekyll folder has become the repository root; they do not run automatically from its nested location in the old workspace.

## 2. Set the site address

In `_config.yml`, set `url` and `baseurl` for local production-style builds:

| Hosting choice | `url` | `baseurl` |
| --- | --- | --- |
| User/organization site | `https://YOUR-ACCOUNT.github.io` | `""` |
| Project repository | `https://YOUR-ACCOUNT.github.io` | `"/YOUR-REPOSITORY"` |
| Custom domain | `https://your-domain.example` | `""` |

Do not put the repository name into `url` or add a trailing slash to `baseurl`. These examples are placeholders, not a configured live address. The Pages workflow overrides these values with GitHub's actual origin and base path so canonical URLs, assets, sitemap, and redirects match the deployment.

## 3. Enable publishing when ready

1. Create your repository and add the source files using your preferred Git workflow.
2. In **Settings → Pages → Build and deployment**, select **GitHub Actions**.
3. Use a `main` default branch, or update `branches: [main]` in `.github/workflows/pages.yml` to your branch name.
4. In **Actions**, run **Build and deploy GitHub Pages**. A push to `main` will also run it.
5. Review the deployment's `github-pages` environment URL after it succeeds.

If the first push happens before Pages is enabled, configuration may fail. Enable Pages and rerun the workflow. Do not choose the default branch-based Jekyll builder: this project uses Jekyll 4 and its own locked Ruby dependencies.

The build job installs the locked gems, builds in production mode, checks links/assets, and uploads only `_site/`. The deployment job receives the minimum Pages/OIDC permissions it needs. Pull requests run checks with both a root URL and a repository-prefix URL; they do not publish.

## 4. Optional custom domain

Configure the custom domain and DNS in your repository's Pages settings, enable HTTPS once available, and set `_config.yml` to the same origin with an empty `baseurl`. No speculative `CNAME` file is included. See [GitHub's custom-domain guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

## Troubleshooting

- **Missing images or styles:** confirm the repository path, and use `relative_url` for internal links. Run the subpath check from the README.
- **Workflow missing:** ensure `.github/workflows/` was copied into the new repository root, including its leading dot.
- **Wrong canonical domain:** set `url`, or confirm that `configure-pages` metadata is reaching the build command.
- **404 on old WordPress URLs:** the migrated ministry, calendar, and event routes have static redirects. Query-string URLs such as `/?p=183` need redirects at the old host; GitHub Pages cannot apply WordPress rewrite rules.
- **Dependencies fail on a new computer:** use the Ruby version in `.ruby-version`, run `bundle install`, and keep the lockfile. Do not install gems with the macOS system Ruby.

References: [Jekyll directory structure](https://jekyllrb.com/docs/structure/), [GitHub custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
