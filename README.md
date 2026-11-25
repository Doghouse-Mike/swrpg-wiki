# SWRPG Wiki

The [Star Wars RPG (FFG) Obsidian vault](https://github.com/Doghouse-Mike/SWRPG-Obsidian-Vault)
published as a website with [Quartz](https://quartz.jzhao.xyz/).

**Site:** https://doghouse-mike.github.io/swrpg-wiki/

Content is from the [Star Wars RPG (FFG) fandom wiki](https://star-wars-rpg-ffg.fandom.com/)'s
contributors, licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
The Quartz code is MIT (see `LICENSE.txt`).

## How it works

This repo holds only Quartz and its config. The notes are **not** committed here:
`.github/workflows/deploy.yml` checks the vault repo out into `content/` on every build,
runs `tools/make-index.py` to turn the vault's main page into the homepage, builds and
deploys to GitHub Pages.

The site rebuilds when:

- something is pushed to this repo (branch `v5`),
- someone runs the workflow by hand (Actions → Deploy → Run workflow),
- every night at 04:17 UTC (picks up vault changes),
- the vault repo sends a `vault-updated` `repository_dispatch` (optional, see below).

All frontmatter is kept: the properties panel shows every field (except `title`, which is
already the heading), and the vault's `.base` files render as Bases pages under `/bases/`.

## Differences from upstream Quartz (keep these on upgrade)

| What | Where | Why |
| --- | --- | --- |
| `.bases-table { position: static }` | `quartz/styles/custom.scss` | The theme layer ships Obsidian's Bases CSS, whose `position: absolute` (for virtual scrolling) makes every Base table invisible. |
| Explorer scroll fix | `quartz/plugins/emitters/componentResources.ts` (`Fork (swrpg-quartz)` comment) | `@quartz-community/explorer` 1.1.1 `scrollIntoView`s the active note on first load, which scrolls the whole page down on deep links. |

Upgrade with `npx quartz upgrade` (pulls upstream `v5`), then re-check both patches.

## Building locally

```bash
git clone https://github.com/Doghouse-Mike/SWRPG-Obsidian-Vault content
python3 tools/make-index.py content
npm ci && npx quartz plugin install
npx quartz build --serve     # http://localhost:8080
```

A full build of the ~3,600 notes takes about 6 minutes.
