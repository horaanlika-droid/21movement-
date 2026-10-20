# 21.city — the app and the mockup

Two things live in `docs/` and are published on GitHub Pages:

- [`docs/index.html`](index.html) — **the app** (bilingual RU/EN): a civic-projects
  mockup in the ethereum.org visual language. Someone photographs a broken
  sidewalk with coordinates; neighbours see it on the map, add to the project
  budget with donations while commercial offers (КП) come in from contractors;
  **the budget target is the lowest offer**; the requester accepts an offer, the
  work happens, escrow pays after acceptance, the receipt stays public.
- [`docs/landing.html`](landing.html) — the grant-application landing (the old
  `index.html`): the number as the campaign, the exchange underneath it, and the
  budget written from the bottom up.

It is a static site — no build step, no framework. The app keeps its state in
`localStorage`; the only runtime libraries are self-hosted
([Leaflet](assets/vendor/leaflet) for the map). Open `docs/index.html` or serve
the folder:

```bash
python3 -m http.server 8080 --directory docs
# http://localhost:8080
```

## The mechanics implemented

1. **Community support** — a report (photo + coordinates from geolocation or a
   map tap) appears on the map; neighbours nearby see the distance, mark “bothers
   me too” and donate into the project budget. The requester seeds the first €25.
2. **Finding contractors** — while donations accumulate, contractors submit
   commercial offers (price, days, rating). The **budget target is recalculated
   to the minimum offer price** the moment it arrives; before any offers the
   author’s estimate is the provisional target.
3. **Work** — an offer is accepted (chat with the contractor, before/after). The
   contractor can **request an advance for materials and work — with a
   justification**; the project’s donors vote to give it or not (a majority of
   the contributed amount releases the advance from escrow; non-donors are
   asked to donate first).
4. **Verification** — neighbours confirm the result; escrow pays the rest.
5. **Completed** — the receipt is public.

## How the page is put together

| Path | What it is |
|---|---|
| `index.html` | The app shell: five tabs (Home, Map, Projects, Wallet, Profile), the project detail overlay and the modals. |
| `city.css` | The app’s design tokens and layout — the same paper/ink/sticker language as the landing. On desktop the app sits in a phone-shaped column on a sheet of paper. |
| `city.js` | All app logic: state (localStorage), i18n, cards, the map, donations, offers, the timeline, the wizard. |
| `landing.html` + `style.css` + `app.js` | The grant landing, unchanged in spirit: language switch and scroll reveal. |
| `assets/vendor/leaflet/` | Self-hosted Leaflet 1.9.4 (BSD-2-Clause) so the app has zero external runtime dependencies. Map tiles: CARTO Voyager over OpenStreetMap data. |
| `assets/img/projects/` | Generated placeholder photos for the seeded projects (resized copies of `grant/photos/`). |
| `assets/fonts/` | Self-hosted, subset `woff2`: Geist, Geist Mono, Gaegu (the child’s hand for numbers), Pangolin (handwritten notes, Latin + Cyrillic). |

**Language.** The shell holds both languages in the markup
(`<span lang="ru">…</span><span lang="en">…</span>`); dynamic strings live in an
i18n dictionary in `city.js` (`I18N`). The RU/EN pill in the header switches
both, and seeded data carries `{ru, en}` pairs.

**Seeds.** Five projects around 59.9398, 30.3157 and four quests, matching the
reference mockups. “Reset demo data” in the profile returns everything to the
seed. User photos are downscaled to ~900 px and stored as data URLs in
`localStorage`.

## Publishing on GitHub Pages

The site is served by **Deploy from a branch** (branch `main`, folder `/(root)`):
the root [`index.html`](../index.html) immediately redirects to `docs/`, which
opens the app. Nothing needs to be switched on beyond Pages itself
(Settings → Pages → Deploy from a branch, main, /(root)).

The [workflow](../.github/workflows/pages.yml) is the alternative path: if you
flip Settings → Pages → Source to **GitHub Actions**, it deploys `docs/` on every
push to `main`. While branch deploys are on, the workflow detects it, stays
green and skips the deploy with a warning instead of fighting the branch
deployment.

Either way the app ends up at `https://<owner>.github.io/21movement-/`.

## Honesty

The illustrations and photographs are generated placeholders. The app claims no
signed city, partner or artist; the numbers are demo arithmetic, not promises.
No token, no paid placement, no paid paint without the owner’s consent. There is
no server: every “donation” and “offer” lives only in your browser.
