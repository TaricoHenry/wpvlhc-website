# Publish to GitHub Pages

Repository: [TaricoHenry/wpvlhc-website](https://github.com/TaricoHenry/wpvlhc-website). The configured project address is <https://taricohenry.github.io/wpvlhc-website/>; this address is not a claim that deployment has succeeded.

## 1. Keep the source at the repository root

The repository root must contain `.github/workflows/`, `.ruby-version`, `_config.yml`, `Gemfile`, `Gemfile.lock`, `index.html`, and the authoring folders. Do not wrap them in a `wpvlhc-aog-jekyll/` directory. GitHub only discovers workflows directly in the root `.github/workflows/` directory.

Generated files (`_site/`, `.jekyll-cache/`, `.jekyll-metadata`, `.bundle/`, and `vendor/`) stay ignored. The local `wpvlhc-aog-jekyll-source.zip` archive is ignored by Git and excluded from the published site. Keep the old WordPress installation and database outside this repository.

## 2. Set the site address

`_config.yml` is set to `url: "https://taricohenry.github.io"` and `baseurl: "/wpvlhc-website"`. For another hosting destination:

| Hosting choice | `url` | `baseurl` |
| --- | --- | --- |
| User/organization site | `https://YOUR-ACCOUNT.github.io` | `""` |
| Project repository | `https://YOUR-ACCOUNT.github.io` | `"/YOUR-REPOSITORY"` |
| Custom domain | `https://your-domain.example` | `""` |

Do not put the repository name into `url` or add a trailing slash to `baseurl`. The Pages workflow overrides these values with GitHub's actual origin and base path so canonical URLs, assets, sitemap, and redirects match the deployment. For local preview at <http://localhost:4000>, run `bundle exec jekyll serve --livereload --baseurl ""`.

## 3. Enable the custom publishing workflow

1. In [Settings → Pages](https://github.com/TaricoHenry/wpvlhc-website/settings/pages), under **Build and deployment → Source**, select **GitHub Actions**.
2. Commit and push the corrected repository layout using your preferred Git workflow. Until pushed, GitHub still sees the old nested files.
3. The workflow runs on pushes to `main`. Once the root workflow is on GitHub, you can also run **Actions → Build and deploy GitHub Pages → Run workflow**.
4. Review the deployment's `github-pages` environment URL after it succeeds.

If the first push happens before Pages is enabled, configuration may fail. Enable Pages and rerun the workflow. Do not choose the default branch-based Jekyll builder: this project uses Jekyll 4 and its own locked Ruby dependencies.

The build job installs the locked gems, builds in production mode, checks links/assets, and uploads only `_site/`. The deployment job receives the minimum Pages/OIDC permissions it needs. Pull requests run checks with both a root URL and a repository-prefix URL; they do not publish.

## 4. Optional custom domain

Configure the custom domain and DNS in your repository's Pages settings, enable HTTPS once available, and set `_config.yml` to the same origin with an empty `baseurl`. No speculative `CNAME` file is included. See [GitHub's custom-domain guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

## Troubleshooting

- **`Could not locate the included file 'sections/leadership.html'`:** the [October 31 failed run](https://github.com/TaricoHenry/wpvlhc-website/actions/runs/41239971420) used GitHub's default Jekyll 3.10 builder at the repository root, while the site's configuration, includes, and workflows were nested in `wpvlhc-aog-jekyll/`. The include exists; the builder was looking in the wrong directory. Keep the source and workflows at the repository root and select **GitHub Actions** as described above. Rerunning the old `pages build and deployment` job alone will not apply this fix.
- **Missing images or styles:** confirm the repository path, and use `relative_url` for internal links. Run the subpath check from the README.
- **Workflow missing:** ensure `.github/workflows/` was copied into the new repository root, including its leading dot.
- **Wrong canonical domain:** set `url`, or confirm that `configure-pages` metadata is reaching the build command.
- **404 on old WordPress URLs:** the migrated ministry, calendar, and event routes have static redirects. Query-string URLs such as `/?p=183` need redirects at the old host; GitHub Pages cannot apply WordPress rewrite rules.
- **Dependencies fail on a new computer:** use the Ruby version in `.ruby-version`, run `bundle install`, and keep the lockfile. Do not install gems with the macOS system Ruby.

References: [Jekyll directory structure](https://jekyllrb.com/docs/structure/), [GitHub custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
