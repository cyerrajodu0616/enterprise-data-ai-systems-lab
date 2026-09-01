# Redesign the Daily HTML Recap as an Interactive Study Experience

## Context and root cause

`daily-artifacts/day-02/recap.html` currently presents all primary navigation at lines 31–35 as links to Markdown/source files. The content itself is a long sequence of always-expanded sections. The result is readable but not an effective interactive study interface: clicking navigation leaves the recap, scanning is difficult, and interview practice is not surfaced as a mode.

The repository requires each recap to remain self-contained with no CDN or external runtime. Source artifacts must remain accessible because Markdown is the durable source of truth, but source links should be secondary rather than the main study navigation.

## Exact files

Modify:

- `daily-artifacts/day-02/recap.html` — replace the current layout and navigation while preserving all factual/evidence content.
- `daily-artifacts/_template/recap.html` — establish the reusable interactive shell for future days.
- `DAILY_ARTIFACT_GUIDELINES.md` — strengthen the HTML recap policy at lines 33–35.

Do not modify Day 2 Markdown artifacts, `CURRENT_SESSION.md`, `LAB_BACKLOG.md`, or `ROADMAP.md`. Preserve unrelated `daily-artifacts/.DS_Store` without staging it.

## Exact navigation replacement

Current Day 2 primary navigation at lines 31–35:

```html
<nav aria-label="Source artifacts">
  <a href="lesson.md">Lesson</a><a href="quiz.md">Quiz attempt</a><a href="quiz-review.md">Quiz review</a>
  <a href="interview-cheat-sheet.md">5-minute cheat sheet</a><a href="experiment.md">Experiment</a>
  <a href="results.md">Results</a><a href="implementation/README.md">Implementation</a><a href="../../LAB_BACKLOG.md">Lab backlog</a>
</nav>
```

Replace that file-oriented primary navigation with this semantic structure, using final labels/IDs that match the completed page:

```html
<a class="skip-link" href="#main-content">Skip to study content</a>
<nav class="study-nav" aria-label="Study sections">
  <a href="#overview">Overview</a>
  <a href="#reasoning">Reasoning</a>
  <a href="#joins">Join strategies</a>
  <a href="#diagnosis">Diagnosis</a>
  <a href="#interview">Interview practice</a>
</nav>
<main id="main-content">
  <!-- Self-contained study sections and interactive controls. -->
</main>
<details class="sources">
  <summary>Source files and evidence provenance</summary>
  <!-- Preserve all current Markdown/implementation/backlog links here. -->
</details>
```

Current policy at `DAILY_ARTIFACT_GUIDELINES.md` lines 33–35:

```markdown
## HTML recap policy

`recap.html` is a portable study artifact, not the source of truth. It must be self-contained HTML/CSS with no required CDN or external runtime and must link to the Markdown, implementation, test, and experiment files. Include problem, mental-model change, key internals, visual explanation where useful, quiz review, implementation summary, evidence, failure/debugging lesson, interview explanation, architecture bridge, and next step. Clearly label unexecuted experiments and hypothetical projections.
```

Retain that content and append the reusable internal-navigation, progressive-enhancement, source-provenance, meaningful-interaction, responsive, and accessibility requirements described below.

## Day 2 design

Create a polished self-contained HTML/CSS/JavaScript study application with progressive enhancement:

1. A compact hero showing day/topic and clear status chips.
2. A sticky internal navigation bar whose controls scroll to HTML sections rather than opening Markdown.
3. A visible study-mode selector:
   - **Learn** — conceptual and reasoning sections;
   - **Diagnose** — Stop/Assess framework, weak-answer examples, debugging ladder, skew/cardinality;
   - **Interview** — vocabulary upgrades, join-strategy decision guide, 60-second response, and Amex STAR story;
   - **All** — every section.
4. Search/filter across section titles and content, with a no-results message.
5. Accessible collapsible reasoning cards using native `<details>/<summary>` where practical; default key orientation content open and deeper details collapsed.
6. “Expand all” and “Collapse all” controls.
7. A join-strategy comparison component for Broadcast Hash Join, Sort-Merge Join, and Nested Loop.
8. Clear visual diagrams for build/probe, Exchange→Sort→SortMergeJoin, skew versus oversized partitions, salting compatibility, cardinality multiplication, and the debugging hierarchy.
9. An interactive interview-practice panel that can reveal/hide the 60-second answer without altering content.
10. A secondary, collapsible **Source files** area containing links to Markdown, implementation, experiment, results, and backlog. Source links remain normal file links and are not the primary navigation.
11. A theme toggle that respects the initial system preference and uses local storage only when available; content must work if JavaScript is disabled.
12. Responsive layouts, visible keyboard focus, skip link, semantic landmarks, accessible labels, motion reduction, and adequate contrast.

Keep all current evidence boundaries: Day 2 coding/experiments remain deferred and measured evidence remains none. Preserve every supplied factual scenario and the limited Amex statement without embellishment.

## Reusable template and policy

Update `daily-artifacts/_template/recap.html` with the same accessible interactive shell but generic placeholder sections. It must remain useful without JavaScript and must not contain completed answers.

Update `DAILY_ARTIFACT_GUIDELINES.md` so future recaps:

- use internal HTML navigation for the primary study experience;
- treat source-file links as a secondary provenance area;
- use progressive enhancement and remain readable without JavaScript;
- provide meaningful interaction only when it improves studying (navigation, filtering, disclosure, practice), not decorative animation;
- preserve accessibility, responsive behavior, self-containment, evidence labels, and source links.

## Verification

- Validate that primary study controls use internal targets/buttons and do not navigate to Markdown.
- Validate every source-file link resolves.
- Confirm no HTTP resources, CDN dependencies, external scripts, or external stylesheets.
- Confirm all interactive controls have accessible names and keyboard-operable native semantics.
- Confirm content is readable with JavaScript disabled.
- Confirm reduced-motion behavior and responsive styling exist.
- Confirm Day 2 status/evidence text is unchanged in meaning.
- Open locally for visual review when a browser is available.
- Run `git diff --check` and review the complete diff.

Do not commit or push until separately requested.
