# Apps

All apps are self-contained single-file Jekyll pages at `apps/{name}/index.md` using vanilla JS, scoped CSS variables, and the `app` layout.

## Café au Le

Coffee ordering app with push notifications via [ntfy.sh](https://ntfy.sh).

### Setup

Pick a random topic string (e.g. `cafe-au-le-x7k9m2p`) and use it in both steps below.

**Phone** — receive notifications:
1. Install the ntfy app ([iOS](https://apps.apple.com/app/ntfy/id1625396347) / [Android](https://play.google.com/store/apps/details?id=io.heckel.ntfy))
2. Tap **+**, enter your topic string, subscribe

**GitHub** — connect the app to your topic:
1. Add the topic as a GitHub repo secret:
   - **Terminal**: `gh secret set NTFY_TOPIC`
   - **Browser/mobile**: Repo → Settings → Secrets and variables → Actions → New repository secret → Name: `NTFY_TOPIC` (GitHub mobile app does not support secrets — use a phone browser in desktop mode)
2. After setting or changing the secret, trigger a rebuild (deploys only run on push):
   ```bash
   gh workflow run deploy.yml
   ```
3. For local development, create `_config_secrets.yml` (gitignored):
   ```yaml
   ntfy_topic: your-topic-here
   ```
4. Run locally with the secrets config:
   ```bash
   bundle exec jekyll serve --config _config.yml,_config_secrets.yml
   ```

### How it works

- The topic is injected at build time via GitHub Actions (never in source code)
- `_config_secrets.yml` is generated during CI from the `NTFY_TOPIC` secret
- Jekyll merges it via `--config _config.yml,_config_secrets.yml`
- Orders send a POST to `ntfy.sh/{topic}` which pushes to your phone

## Adding a New App

1. Create `apps/{name}/index.md`
2. Use frontmatter:
   ```yaml
   ---
   layout: app
   title: "App Title"
   permalink: /app-name/
   ---
   ```
3. Scope CSS with a container class and standard variables:
   ```css
   .my-app {
     --muted: #909498;
     --accent: #bf616a;
     --input-bg: #2d3033;
     --border: #444;
     --gold: #d4a843;
   }
   ```
4. Add the app to `_pages/apps.md`
