# 21 — grant deck

A 20-slide, 16:9 application deck for an Ethereum ecosystem grant, plus the
written application text.

## Files

| Path | What it is |
|---|---|
| `build/21-grant-deck.pdf` | **The deliverable.** 20 pages, 1280×720 pt, embedded fonts, print-safe. |
| `application.md` | The same content as copy-paste text for a grant form (EN + short RU version). |
| `preview/p01…p20.png` | Rendered page previews (2× scale) for quick review in a browser. |
| `assets/` | Photography used in the deck (AI-generated placeholders — replace with real photos). |
| `tools/` | The generator: `theme.py` (design system), `uikit.py` (UI kit), `build.py` (slides). |

## Rebuilding

```bash
pip install reportlab pypdfium2 pillow
cd tools && python3 build.py --preview
```

`--preview` re-renders the PNG previews as well. Everything is vector except the
photography, so the PDF stays sharp at any zoom.

## Editing

- **Text and numbers live in `build.py`**, one function per slide, top to bottom
  in reading order (`s01` … `s20`). Page numbers in the footer come from the
  slide index — adding or removing a slide updates the `NN / 20` count only if
  you also change `TOTAL` and the `assert` at the bottom.
- **Colours and type** are defined once in `tools/theme.py` (`INK`, `VIO`,
  `MINT`, `SAND`, …). Change them there, not per slide.
- **Photography** is referenced from `tools/theme.py` → `ASSETS`. Replace files
  in `assets/` with the same names and rebuild.

## What to fill in before submitting

1. `s16` (team) — the three `[name] · [github / linkedin]` fields and the advisor.
2. Confirm the ask. `$75,000 / 10 months` appears on `s01`, `s15`, `s20` and in
   `application.md`; keep them in sync.
3. Pilot cities, if partners are already named — `s04`, `s13`, `s17`.
4. Sweep the deck for `[` to make sure no placeholder survived.

## Honesty rules baked into the deck

- Every number that is a target is labelled as a target (`s17` is titled
  "Targets, not traction").
- The bench story on `s04` is explicitly marked as a demo scenario.
- The mural programme is described as commissioned and consented only; no slide
  implies trespassing or painting without permission.
- No token, no fake traction, no invented partnerships.

## Language

The deck is in English because Ethereum grant reviewers read English. A short
Russian summary is at the end of `application.md` if you need to circulate it
locally.
