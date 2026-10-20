# 21 — grant deck

A 20-slide, 16:9 application deck for an Ethereum ecosystem grant, plus the
written application text.

The deck was rebuilt in the visual language of **ethereum.org**: warm paper,
ink-outlined "sticker" cards, pastel accents, flat editorial illustration and a
serif accent face — instead of the previous dark investor template. Photography
is deliberately phone-shaped and amateur: vertical, overcast, slightly crooked,
so a reviewer reads it as "a resident took this" rather than "a stock shoot".
The street-furniture photos show contemporary benches, racks and shelters in
modern neighbourhoods, not postcard streets.

## What the deck asks for

**$21,000 over 6 months**, of which **70% is artist fees**. The campaign is
21 commissioned murals by 21 paid artists in 9 cities; the 21 protocol (open
registry + per-task escrow) is the receipt underneath it. Code is not in the
budget — the team writes it.

## Files

| Path | What it is |
|---|---|
| `build/21-grant-deck.pdf` | **The deliverable.** 20 pages, 1280×720 pt, embedded fonts. |
| `application.md` | The same content as copy-paste text for a grant form (EN + short RU version). |
| `preview/p01…p20.png` | Rendered page previews (1.5× scale) for quick review in a browser. |
| `art/` | Five flat illustrations in the ethereum.org style (cover, city upgrade, artist wall, contractors, artist kit). |
| `photos/` | Six phone-style photographs (bench before/after, modern bike rack, solar shelter, contemporary plaza, crew). |
| `tools/` | The generator: `theme.py` (design system), `uikit.py` (UI kit), `build.py` (slides). |

All illustrations and photographs are AI-generated placeholder material.
Replace them with real commissions and real photographs before submitting — the
`art/` and `photos/` filenames are the only contract between the deck and the
image files.

## Rebuilding

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install reportlab pypdfium2 pillow
cd tools && python3 build.py --preview
```

`--preview` re-renders the PNG previews as well. Everything except the
illustrations and photos is vector, so the PDF stays sharp at any zoom.

## Editing

- **Text and numbers live in `build.py`**, one function per slide, top to bottom
  in reading order (`s01` … `s20`). The `NN / 20` footer comes from `TOTAL`.
- **Colours, fonts, cards and doodles** are defined once in `tools/theme.py`.
  The illustration background is `#FAF2DE`, identical to `theme.PAPER`, which is
  why images can be dropped on the page without a frame.
- **Slides** `s12`–`s20` also live in `application.md`; keep the two in sync.

## Notes on the visual pass

- **Illustrations** are flat, ink-outlined and pastel, drawn on `#FAF2DE`, so they
  drop onto the page with no frame. `artist-kit.png` illustrates what an open
  kit actually is; `contractor-duo.png` puts two bidders next to the bid sheet.
- **Photographs** are vertical, overcast and slightly crooked, with wet paving
  and autumn leaves — the look of a phone snapshot in a modern neighbourhood,
  not a postcard. The street furniture in them is contemporary: oak-and-concrete
  benches, powder-coated loop racks, a sedum-roofed solar shelter.
- **The interface** leans into ethereum.org's playfulness: rotated sticker
  chips, hand-drawn arrows, sparkles and one very large button. Every one of
  them carries a sentence, never decoration for its own sake.
- **Contractor bids** are visible in three places now: the bid sheet (`s05`),
  the itemised quote (`s05`), and a `3 BIDS · 1 WINNER` label on every item in
  the street-furniture kit (`s07`).

## Slide map

| # | Slide | Why it is there |
|---|---|---|
| 01 | Cover | Ask, artist share, three proof chips |
| 02 | The problem | Ticket, small fixes, invisible contractors + a resident's photo |
| 03 | The upgrade | What the protocol changes, in plain language |
| 04 | The protocol | Seven steps, public/private split |
| 05 | Contractor bids | Itemised public bids, line-by-line quote |
| 06 | One task | Bench, nine days, iPhone before/after + ledger |
| 07 | The kit | Modern street furniture with specs and unit costs |
| 08 | Verification | Evidence package, attestations, release |
| 09 | The cultural layer | The 21 mural programme |
| 10 | The artist deal | Open call → consent → 50% → wall → 50% + record |
| 11 | Why Ethereum | Neutral settlement, global rail, permanent record |
| 12 | The product | Six app screens |
| 13 | Interface | Palette, type, components, phone mockup |
| 14 | Budget | $21,000, line by line, 70% to artists |
| 15 | Milestones | Five payments tied to walls that exist |
| 16 | Team | Three people, one curator per city, 21 artists |
| 17 | Metrics | Targets, not traction |
| 18 | Risks | Artist, owner, weather, evidence, escrow |
| 19 | After the grant | Sustainability and what stays open |
| 20 | Close | The ask |

## What to fill in before submitting

1. `s16` (team) — the three `[name] · [github / linkedin]` fields and the curator.
2. Confirm the ask. `$21,000 / 6 months` appears on `s01`, `s14`, `s20` and in
   `application.md`; keep them in sync.
3. City list, if partners are already named — `s09`, `s15`, `s16`.
4. Sweep the deck for `[` to make sure no placeholder survived.

## Honesty rules baked into the deck

- Every number that is a target is labelled as a target (`s17` is titled
  "Targets, not traction").
- The bench story on `s06` is explicitly marked as a demo scenario.
- The mural programme is described as commissioned and consented only; no slide
  implies trespassing or painting without permission.
- "70% to artists" is a budget line, not a claim about past spending.
- No token, no fake traction, no invented partnerships. Photography and
  illustration are placeholders and are labelled as such here.

## Language

The deck is in English because Ethereum grant reviewers read English. A short
Russian summary is at the end of `application.md`.
