# 21.city — the mockup

The landing page for the grant application: the number as the campaign, the
exchange underneath it, and the budget written from the bottom up.

It is a static site — no build step, no framework, no dependency. Open
`index.html` or serve the folder.

```bash
python3 -m http.server 8080 --directory docs
# http://localhost:8080
```

## Publishing on GitHub Pages

Two ways; both need Pages switched on once in **Settings → Pages**.

**A. GitHub Actions (recommended).** The workflow
[`.github/workflows/pages.yml`](../.github/workflows/pages.yml) deploys `docs/`
on every push to `main`. It asks Pages to enable itself (`enablement: true`); if
the token is not allowed to, set **Source: GitHub Actions** by hand once.

**B. Branch folder.** Settings → Pages → *Deploy from a branch* → branch
`main`, folder `/docs`. No workflow involved.

The site ends up at `https://<owner>.github.io/21movement-/`.

## How the page is put together

| Path | What it is |
|---|---|
| `index.html` | The page. Both languages are in the markup, not in a JSON file. |
| `style.css` | Design tokens, layout, the hand-drawn details. |
| `app.js` | Language switch and the scroll reveal. Nothing else. |
| `assets/fonts/` | Self-hosted, subset `woff2`: Geist (400–700), Geist Mono, Gaegu (the child's hand, digits), Pangolin (the handwritten notes, Latin + Cyrillic). |
| `assets/img/` | `cover-21`, `artist-wall`, `project-block` — the graffiti art, kept large; `favicon.png`; `og.jpg` for link previews. |

**Language.** `index.html` holds `<span lang="ru">…</span><span lang="en">…</span>`
side by side. `html[data-lang]` and one CSS rule pick one; the script only flips
the attribute and remembers the choice. With JS off, Russian is shown and the
page still works.

**Handwriting.** Two faces, two jobs:

- **Gaegu** (Korean handwriting, childlike) is used for every number: the huge
  `21`, the section numerals `1–5`, the figures in the budget and the dates.
  Digits are the same in both languages, so the page keeps one voice when it
  switches.
- **Pangolin** (hand-lettered, Cyrillic + Latin) is used for written notes,
  captions and the pull quotes. Gaegu has no Cyrillic and no `€`, so it cannot
  carry the Russian copy.

The big graffiti `21` stays as art (`cover-21.webp`, `artist-wall.webp`) — the
handwriting is the page's own writing around it, not a replacement for it.

**Editing.** Copy is in `index.html`; colours, spacing and type are tokens at the
top of `style.css`. Keep both languages in sync when you change a sentence —
there is no fallback.

## The numbers on the page

The page names a **floor**, not a wish: €7,500 for six months in one city, with
the code time in the budget at 250 ₽ an hour (the rate the author earns cooking,
960 hours → €2,500 at €1 = 96 ₽). Every other line is a unit price × quantity,
and the table adds up exactly to €7,500. Above that floor the original split
(45/15/15/10/6/5/4) applies again.

Edit the table, the stacked bar and the milestone amounts together — they are
three views of the same arithmetic, and the bar widths are inline percentages.

## Honesty

The illustrations and photographs are generated placeholders and are labelled as
such in the footer. The page claims no signed city, partner or artist. No token,
no paid placement, no paid paint without the owner's consent.

## Fonts

All four families are under the SIL Open Font License and are subset to the
characters this page uses; the licence texts are in
[`assets/fonts/README.md`](assets/fonts/README.md).
