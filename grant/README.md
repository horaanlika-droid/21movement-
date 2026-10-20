# 21 — grant deck

A 22-slide, 16:9 application deck for an Ethereum ecosystem grant, plus the
written application text. Built in the visual language of **ethereum.org**: warm
paper, ink-outlined sticker cards, pastel accents, flat editorial illustration and
a serif accent face. Photography stays deliberately phone-shaped and amateur:
vertical, overcast, slightly crooked, so a reviewer reads it as "a resident took
this".

## What the deck argues

Two layers, one number.

**The mark.** 21 is the campaign, and it is a number on purpose: you cannot
confiscate it, copyright it or make it need a translation. Chalk on asphalt, a
marker on a lift door, a sticker on a broken bench, a construction hoarding, a
five-second TikTok. Amateur is the format — polish would kill it. The number has
to become a meme before it becomes a brand: ten templates, a six-second script, a
stencil in every caption, and **one large PR agency on retainer**, paid per
published placement and per settled quest rather than per impression. Every mark
points at the task page under it, and a free MIT kit (stencil, stickers, chalk
templates) lets anyone print their own. We pay for consented walls, artists, film
and the kit; we never pay for illegal paint and never instruct anyone to break a
rule.

**The exchange.** Under the number sits a demand-first services board: a person
posts what they need — a tutor, a handyman, a psychologist — names a reward and a
deadline, and offers arrive from named people. The asker chooses, the work
happens, both sides confirm, escrow pays, the record stays. The unit is medium:
an hour, a session, a visit, a small fix. Above it sit two larger sizes on the
same protocol — a civic task for one object (a bench, a bike rack, a tram stop),
and a **project** for a whole street, school roof or construction site: budget,
timeline, open tender, milestone escrow, and each milestone splittable into
quests. No dispatch algorithm, no commission taken from the worker before the
work exists, no paid placement.

**No total ask.** The deck fixes the *split*, not a sum: 45% quest and project
rewards in escrow, 15% consented walls and artists, 15% PR and kit, 10%
verification, 6% safety/legal, 5% infrastructure, 4% reserve. A smaller round buys
fewer quests and fewer walls, never cheaper ones. Code is $0 — the team writes it.

## Files

| Path | What it is |
|---|---|
| `build/21-grant-deck.pdf` | **The deliverable.** 22 pages, 1280×720 pt, embedded fonts. |
| `application.md` | The same content as copy-paste text for a grant form (EN + short RU version). |
| `preview/p01…p22.png` | Rendered page previews (1.2× scale) for quick review in a browser. |
| `art/` | Flat illustrations in the ethereum.org style: `cover-21`, `meme-wall`, `quest-exchange`, `devices`, `stencil-kit`, `project-block` (used), plus the earlier `cover-city`, `upgrade-block`, `artist-wall`, `contractor-duo`, `artist-kit` (kept, unused in this version). |
| `photos/` | Six phone-style photographs (bench before/after, bike rack, solar shelter, plaza, crew). Used for the quest screens, the "mark on broken things" page and the PR wall. |
| `tools/` | The generator: `theme.py` (design system), `uikit.py` (UI kit, quest screens, device frames), `build.py` (slides). |

All illustrations and photographs are AI-generated placeholder material. Replace
them with real commissions and real photographs before submitting — the `art/`
and `photos/` filenames are the only contract between the deck and the files.

## Rebuilding

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install reportlab pypdfium2 pillow
cd tools && python3 build.py --preview
```

`--preview` re-renders the PNG previews as well. Everything except the
illustrations and photos is vector, so the PDF stays sharp at any zoom.

## Editing

- **Text and numbers live in `build.py`**, one function per slide, top to bottom in
  reading order (`s01` … `s22`). The `NN / 22` footer comes from `TOTAL`.
- **Colours, fonts, cards and doodles** are defined once in `tools/theme.py`. The
  illustration background is `#FAF2DE`, identical to `theme.PAPER`, which is why
  images drop onto the page without a frame.
- **Quest screens** (`uikit.quest_screen`) draw the miniature app: `feed`,
  `quest`, `offers`, `ask`, `pay`. `uikit.chalk_number` draws the hand-chalked 21
  over a photo without using a font, so it reads as paint rather than typography.
  `build.project_page` draws the public project page on slide 11.
- **Slides `s15`–`s22`** also live in `application.md`; keep the two in sync.

## Slide map

| # | Slide | Why it is there |
|---|---|---|
| 01 | Cover | The number is the PR, the quest is the product; no total ask |
| 02 | The problem | Tickets, DMs, invisible supply + a resident's photo |
| 03 | The mark | Why a number: unownable, amateur, every mark is a link |
| 04 | Mark on infrastructure | Chalked bench, marked lift door, stickered tram stop; a mark is a hyperlink |
| 05 | The exchange | Demand first: ask → offers → choose → work → confirm |
| 06 | Anatomy of a quest | Six fields, a medium unit, why not a gig app |
| 07 | One quest, end to end | Psychology session, three screens, public ledger |
| 08 | Trust | Escrow, two-sided confirmation, disputes, safety rules |
| 09 | Civic layer | The same machinery on a bench in Oosterpark |
| 10 | Two doors | Personal quest vs civic task, side by side |
| 11 | Scale | Quest → civic task → project; large city problems and construction sites, paid by milestone |
| 12 | Devices | Phone, tablet, desktop, kiosk, TV; one codebase |
| 13 | Interface | Palette, type, components, the phone screen |
| 14 | The PR machine | Make 21 a meme: one large agency, TikTok formats, what we count, guardrails |
| 15 | The kit | Stencil, stickers, chalk, the three PR waves, what we won't do |
| 16 | Budget | Shares, not sums; no total anywhere |
| 17 | What a round buys | Three scope shapes, each with a project, and the floor |
| 18 | Milestones | Five releases in percentages |
| 19 | Team | Three people, one large PR partner, paid curators and creators |
| 20 | Metrics | Targets with sources, plus guardrails |
| 21 | Risks | Hijacked mark, illegal paint, cold board, safety, practice, escrow |
| 22 | Close | Bring a wall. Bring a quest. |

## What to fill in before submitting

1. `s19` (team) — the three `[name] · [github / linkedin]` fields and the curator.
2. `s14` (PR) — the agency, once one is chosen; do not invent a logo wall.
3. City list, if partners are already named — `s17`, `s18`, `s19`.
4. Sweep the deck for `[` to make sure no placeholder survived.
5. Do **not** add a total ask: `s01`, `s16`, `s22` and `application.md` all argue
   against naming one.

## Honesty rules baked into the deck

- Every number that is a target is labelled as a target (`s20` is titled
  "Targets, not traction").
- The quest story on `s07`, the bench on `s09` and the project page on `s11` are
  explicitly demo scenarios. No city, developer or construction partner is claimed
  as signed.
- The mark is described as consented where we pay, and as other people's art where
  we don't. No slide implies trespassing or painting without permission — the
  construction hoarding is explicitly "with the owner's consent".
- "Shares, not sums" is a real constraint, not a rhetorical dodge: percentages are
  what we can commit to without inventing a figure.
- No token, no fake traction, no invented partnerships, no purchased engagement.
  Photography and illustration are placeholders and are labelled as such here.

## Language

The deck is in English because Ethereum grant reviewers read English. A short
Russian summary is at the end of `application.md`.
