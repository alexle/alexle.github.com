# alexanderle.com

Personal blog built with Jekyll and deployed to GitHub Pages.

## Development

Use Ruby 3.2 to match CI. Node.js and npm are also required.

```bash
bundle install
npm install
npm run jekyll:serve
```

The local server includes drafts at <http://127.0.0.1:4000>. To enable app secrets, use:

```bash
bundle exec jekyll serve --config _config.yml,_config_secrets.yml --drafts
```

## Validation

```bash
npm test
npm run build
```

Use `npm run lint:fix` to repair SCSS lint errors. The pre-commit hook runs SCSS linting and checks staged post filenames.

Post filenames must use `YYYY-MM-DD-kebab-case-title.markdown` or the `.md` extension.

## Publishing

The [deployment workflow](.github/workflows/deploy.yml) builds pull requests and deploys `main` to GitHub Pages.

GitHub Issues support mobile publishing through two workflows:

- Apply `new-post` to publish an issue body immediately.
- Apply `draft` to save the issue body in `_drafts/`.
- Apply `publish` to publish the draft associated with that issue.
- Add `Tags: tag1, tag2` on its own line to set post tags.

See [create-post-from-issue.yml](.github/workflows/create-post-from-issue.yml) and [draft-post-from-issue.yml](.github/workflows/draft-post-from-issue.yml) for lifecycle details.

## Repository automation

- [optimize-images.yml](.github/workflows/optimize-images.yml) optimizes changed images. Add post images under `assets/` and reference them as `![Alt text](/assets/image.jpg)`.
- [link-checker.yml](.github/workflows/link-checker.yml) checks content links on relevant pushes, weekly, or on demand.
