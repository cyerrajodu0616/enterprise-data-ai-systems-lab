# Add a responsive recap index and publish it with GitHub Pages

## Feature context

The repository contains two standalone HTML recap pages:

- `daily-artifacts/day-01/recap.html`
- `daily-artifacts/day-02/recap.html`

Both pages already contain `<meta name="viewport" content="width=device-width, initial-scale=1">` and responsive CSS, so they can be viewed on phones and iPads without changing either recap. The missing pieces are a discoverable root landing page and an automated GitHub Pages deployment.

The Git remote is `https://github.com/cyerrajodu0616/enterprise-data-ai-systems-lab.git`. There is currently no root `index.html`, no `.github/` workflow, and no `.nojekyll` file. The current working branch at planning time is `technical-sharpness/day-01-completion`; deployment must occur only after these changes are merged or pushed to the repository's actual default branch.

## Change 1: create the responsive landing page

**File:** `index.html` (new file, lines 1-101)

There is no before block because the file does not exist.

Create the file with this exact content:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Mobile-friendly study recaps from the Enterprise Data & AI Systems Lab.">
  <title>Enterprise Data &amp; AI Systems Lab — Study Recaps</title>
  <style>
    :root {
      color-scheme: light dark;
      --bg: #f4f7fb;
      --panel: #ffffff;
      --text: #142033;
      --muted: #58677c;
      --line: #cfdae8;
      --accent: #2855d9;
      --shadow: 0 12px 35px rgba(27, 45, 79, .09);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.55;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #0d1422;
        --panel: #151f30;
        --text: #eef4ff;
        --muted: #acbad0;
        --line: #33435c;
        --accent: #8eacff;
        --shadow: 0 14px 40px rgba(0, 0, 0, .25);
      }
    }
    * { box-sizing: border-box; }
    body { margin: 0; background: var(--bg); color: var(--text); }
    header {
      background: linear-gradient(135deg, #183a9e, #2855d9 58%, #167c72);
      color: #fff;
      padding: clamp(2.25rem, 7vw, 5rem) max(1rem, calc((100vw - 72rem) / 2));
    }
    header p { max-width: 48rem; margin-bottom: 0; }
    .eyebrow { text-transform: uppercase; letter-spacing: .12em; font-size: .78rem; font-weight: 800; opacity: .85; }
    h1 { margin: .45rem 0 .8rem; font-size: clamp(2rem, 6vw, 4rem); line-height: 1.05; }
    main { max-width: 72rem; margin: auto; padding: clamp(1rem, 4vw, 2rem) 1rem 4rem; }
    .intro { color: var(--muted); max-width: 60rem; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr)); gap: 1rem; margin-top: 1.5rem; }
    .card {
      display: flex;
      flex-direction: column;
      min-height: 15rem;
      padding: 1.25rem;
      border: 1px solid var(--line);
      border-radius: 1rem;
      background: var(--panel);
      box-shadow: var(--shadow);
    }
    .card h2 { margin: .2rem 0 .5rem; font-size: 1.35rem; }
    .card p { color: var(--muted); }
    .status { font-size: .8rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; color: var(--accent); }
    .button {
      display: inline-flex;
      justify-content: center;
      align-items: center;
      min-height: 2.75rem;
      margin-top: auto;
      padding: .65rem 1rem;
      border-radius: .65rem;
      background: var(--accent);
      color: var(--bg);
      font-weight: 800;
      text-decoration: none;
    }
    .button:focus-visible { outline: 3px solid var(--text); outline-offset: 3px; }
    footer { max-width: 72rem; margin: auto; padding: 0 1rem 2rem; color: var(--muted); }
  </style>
</head>
<body>
  <header>
    <div class="eyebrow">Technical Sharpness</div>
    <h1>Study Recaps</h1>
    <p>Mobile-friendly daily lessons from the Enterprise Data &amp; AI Systems Lab. Open a recap to review concepts, reasoning, evidence boundaries, and interview takeaways.</p>
  </header>
  <main>
    <h2>Available recaps</h2>
    <p class="intro">Each recap is a standalone page that works in a modern browser on phones, tablets, and desktop screens.</p>
    <div class="grid">
      <article class="card">
        <div class="status">Week 1 · Day 1</div>
        <h2>SQL/Oracle Execution to Distributed Spark Execution</h2>
        <p>Partitions, tasks, stages, shuffle boundaries, skew, lineage-based recovery, and retry safety.</p>
        <a class="button" href="daily-artifacts/day-01/recap.html">Open Day 1 recap</a>
      </article>
      <article class="card">
        <div class="status">Week 1 · Day 2</div>
        <h2>Join Internals</h2>
        <p>Join strategies, data movement, skew, cardinality, AQE, salting, diagnosis, and interview practice.</p>
        <a class="button" href="daily-artifacts/day-02/recap.html">Open Day 2 recap</a>
      </article>
    </div>
  </main>
  <footer>Enterprise Data &amp; AI Systems Lab</footer>
</body>
</html>
```

### Constraints and gotchas

- Keep links relative so the site works at the GitHub project URL (`/enterprise-data-ai-systems-lab/`) rather than assuming a user-site root.
- Do not list `daily-artifacts/_template/recap.html`; it is an incomplete authoring template, not a finished study page.
- Do not alter the two existing recap pages as part of this change.
- When future days are completed, add a card only for a real `daily-artifacts/day-XX/recap.html` file.

## Change 2: add the GitHub Pages deployment workflow

**File:** `.github/workflows/pages.yml` (new file, lines 1-41)

There is no before block because the file does not exist.

The local remote HEAD is confirmed as `origin/main`. Before implementation, run `git remote show origin` or query GitHub once more to ensure that the remote default branch has not changed. Replace `main` below only if that check reports a different default branch.

Create the file with this content after confirming the branch:

```yaml
name: Deploy static site to Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Validate tutorial index and accessibility basics
        run: python3 scripts/validate_tutorial_index.py

      - name: Configure Pages
        uses: actions/configure-pages@v5

      - name: Upload site
        uses: actions/upload-pages-artifact@v3
        with:
          path: .

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Constraints and gotchas

- GitHub repository Settings → Pages → Build and deployment must use **GitHub Actions**. This is repository configuration, not a file edit.
- Deployment is an external state change. Enable Pages and push/merge only with the repository owner's authorization.
- The workflow publishes the checked-out repository as a static artifact. It must never contain credentials or generated secret files.
- The expected site URL is `https://cyerrajodu0616.github.io/enterprise-data-ai-systems-lab/`, subject to GitHub Pages being enabled and the workflow succeeding.

## Change 3: document the tutorial publication rule

**File:** `DAILY_ARTIFACT_GUIDELINES.md` (existing file, replace lines 33-43)

Before:

```markdown
## HTML recap policy

`recap.html` is a portable study artifact, not the source of truth. It must be self-contained HTML/CSS with no required CDN or external runtime and must link to the Markdown, implementation, test, and experiment files. Include problem, mental-model change, key internals, visual explanation where useful, quiz review, implementation summary, evidence, failure/debugging lesson, interview explanation, architecture bridge, and next step. Clearly label unexecuted experiments and hypothetical projections.

Use `daily-artifacts/_template/recap.html` as the required interactive shell for every completed day. Primary navigation must stay inside the HTML study experience; links to Markdown, implementation, experiments, results, and backlog belong in a secondary **Source files and evidence provenance** area.

Use progressive enhancement: the complete lesson must remain readable when JavaScript is unavailable. Meaningful interaction may support internal navigation, study-mode filtering, search, disclosure, and interview practice; avoid decorative animation that does not improve learning. Preserve semantic landmarks, keyboard operation, visible focus, reduced-motion support, responsive layout, adequate contrast, honest evidence labels, and resolvable source links.

## Completion rule

A day is complete only when its package is reviewed, the HTML renders correctly, evidence is honest, `CURRENT_SESSION.md` is updated, and everything is committed and pushed. If an artifact is not applicable, explain why in `lesson.md` rather than leaving an ambiguous placeholder.
```

After:

```markdown
## HTML recap policy

`recap.html` is a portable study artifact, not the source of truth. It must be self-contained HTML/CSS with no required CDN or external runtime and must link to the Markdown, implementation, test, and experiment files. Include problem, mental-model change, key internals, visual explanation where useful, quiz review, implementation summary, evidence, failure/debugging lesson, interview explanation, architecture bridge, and next step. Clearly label unexecuted experiments and hypothetical projections.

Use `daily-artifacts/_template/recap.html` as the required interactive shell for every completed day. Primary navigation must stay inside the HTML study experience; links to Markdown, implementation, experiments, results, and backlog belong in a secondary **Source files and evidence provenance** area.

Use progressive enhancement: the complete lesson must remain readable when JavaScript is unavailable. Meaningful interaction may support internal navigation, study-mode filtering, search, disclosure, and interview practice; avoid decorative animation that does not improve learning. Preserve semantic landmarks, keyboard operation, visible focus, reduced-motion support, responsive layout, adequate contrast, honest evidence labels, and resolvable source links.

Every new completed tutorial at `daily-artifacts/day-XX/recap.html` must be linked from the root `index.html` in the same change. It must include a declared document language, a non-empty title, a viewport meta tag, and an `<h1>` heading. Run `python3 scripts/validate_tutorial_index.py` before committing; GitHub Pages deployment must fail when a completed tutorial is missing from the index or any of these accessibility basics is absent.

## Completion rule

A day is complete only when its package is reviewed, the HTML renders correctly, the tutorial is linked from `index.html`, `scripts/validate_tutorial_index.py` passes, evidence is honest, `CURRENT_SESSION.md` is updated, and everything is committed and pushed. If an artifact is not applicable, explain why in `lesson.md` rather than leaving an ambiguous placeholder.
```

## Change 4: add the enforcement script

**File:** `scripts/validate_tutorial_index.py` (new file, lines 1-95)

There is no before block because the file does not exist.

Create the file with this exact content:

```python
#!/usr/bin/env python3
"""Validate that completed HTML tutorials are indexed and minimally accessible."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
TUTORIAL_PATTERN = "daily-artifacts/day-[0-9][0-9]/recap.html"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.has_language = False
        self.has_viewport = False
        self.has_h1 = False
        self.in_title = False
        self.title_parts: list[str] = []
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html" and values.get("lang", "").strip():
            self.has_language = True
        elif tag == "meta" and values.get("name", "").lower() == "viewport":
            self.has_viewport = bool(values.get("content", "").strip())
        elif tag == "h1":
            self.has_h1 = True
        elif tag == "title":
            self.in_title = True
        elif tag == "a" and values.get("href"):
            self.links.add(values["href"].split("#", 1)[0])

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def has_title(self) -> bool:
        return bool("".join(self.title_parts).strip())


def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def main() -> int:
    errors: list[str] = []
    if not INDEX.is_file():
        print("ERROR: index.html does not exist", file=sys.stderr)
        return 1

    index_parser = parse(INDEX)
    tutorials = sorted(ROOT.glob(TUTORIAL_PATTERN))
    if not tutorials:
        errors.append("no completed tutorial recap pages were found")

    for tutorial in tutorials:
        relative = tutorial.relative_to(ROOT).as_posix()
        if relative not in index_parser.links:
            errors.append(f"{relative} is not linked from index.html")

        page = parse(tutorial)
        checks = {
            "document language": page.has_language,
            "non-empty title": page.has_title,
            "viewport meta tag": page.has_viewport,
            "h1 heading": page.has_h1,
        }
        for label, passed in checks.items():
            if not passed:
                errors.append(f"{relative} is missing {label}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(tutorials)} indexed tutorial page(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### Enforcement behavior and scope

- The glob deliberately matches only two-digit completed-day directories and excludes `daily-artifacts/_template/recap.html`.
- The validator uses only the Python standard library, so the GitHub runner needs no package installation.
- The index link must use the repository-relative path without a leading slash, matching the project-site hosting requirement.
- These automated checks enforce discoverability and accessibility basics. Manual keyboard, contrast, responsive-layout, and interaction checks remain required by `DAILY_ARTIFACT_GUIDELINES.md`.

## Verification

1. Confirm all new files parse cleanly and `git diff --check` reports no whitespace errors.
2. Serve the repository root locally with a static HTTP server; do not validate only through `file://` URLs.
3. Open `/index.html` at phone width (approximately 390 px), iPad portrait (approximately 768 px), and desktop width.
4. Verify both cards remain readable, buttons meet a minimum 44 px touch target, and no horizontal scrolling occurs.
5. Follow both recap links and confirm they return HTTP 200.
6. Confirm the Day 2 theme, search, study-mode filters, expand/collapse controls, and answer reveal still work.
7. Run `python3 scripts/validate_tutorial_index.py` and confirm it reports two indexed tutorial pages.
8. Temporarily remove one tutorial card from a disposable copy of `index.html` and confirm the validator exits nonzero; restore it before committing.
9. After merge/push and Pages configuration, confirm the deployment workflow succeeds and open `https://cyerrajodu0616.github.io/enterprise-data-ai-systems-lab/` on the mobile/iPad browser.
