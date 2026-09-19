# AVDASI 2 docs

Avionics resources for AVDASI 2 (CADE20005, Aerospace Vehicle Design and Systems Integration) at the University of Bristol, published at <https://avdasi2.github.io/docs/>.

The site is built with [Zensical](https://zensical.org) in the Bristol Flight Lab theme shared with the CADE30008 Flight Dynamics & Control course.

## Quick start

You need Python 3.10 or later.

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./scripts/fetch-example-code.sh     # example scripts into docs/code/
.venv/bin/zensical serve            # live preview at http://localhost:8000/docs/
```

Pushing to `main` builds the site and publishes it to the `gh-pages` branch (`.github/workflows/ci.yml`).

## Layout

| Path | Contents |
|---|---|
| `zensical.toml` | Site configuration and navigation |
| `docs/` | Site pages |
| `docs/stylesheets/flightlab.css` | Flight Lab theme, copied from the control course; keep the two in step |
| `docs/stylesheets/course.css` | AVDASI 2 additions to the theme |
| `docs/assets/brand/` | University and Flight Lab artwork used by the theme. Don't edit it here |
| `docs/code/` | Example code, fetched from [avdasi2-avionics-demo](https://github.com/AVDASI2/avdasi2-avionics-demo) at build time. Not committed |

## Snapshots and rollback

Earlier states are kept as Git tags:

| Tag | What it is |
|---|---|
| `v2025-26-mkdocs` | Source as taught in 2025-26, on MkDocs Material |
| `v2025-26-site` | The `gh-pages` branch as last deployed by MkDocs |

To look at an old version, run `git switch --detach v2025-26-mkdocs`. To put the old site back live, push the tag over `gh-pages`:

```bash
git push --force origin v2025-26-site^{commit}:refs/heads/gh-pages
```
