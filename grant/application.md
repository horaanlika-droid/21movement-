# 21 — grant application text

Copy-paste source for the written parts of an Ethereum ecosystem grant
(ESP-style form). Numbers match the deck: **$21,000 over 6 months**, of which
**70% goes directly to artists**.

The deck now has one centre of gravity: the **21 mural programme** — 21 paid,
commissioned walls in 9 cities — with the 21 payment/verification protocol
underneath it as the infrastructure that makes the money auditable.

Replace every `[…]` placeholder before submitting.

---

## Project name

21

## One-line description

A commissioned mural programme with a public ledger: 21 artists paint 21 walls
in 9 cities, each paid on time, each wall registered on Ethereum.

## Website / repo

- Website: `https://21.city` (in development)
- Repository: `https://github.com/21anlika-droid/21movement-`

## The ask, in one paragraph

We are asking for **$21,000 over six months**. Not for code — the team writes
that. The money goes to people: an average **$700 fee per artist** for 21 walls,
plus paint, lifts, scaffolding, insurance, consent paperwork, a local
photographer per city and a paid curator per city. Every payment is published,
every wall has a signed owner consent, and every artist keeps copyright.

## Problem

Cities can see problems and cannot pay the people who would fix them — or make
them worth looking at.

1. **Public art is commissioned late and paid last.** A wall is agreed, painted,
   and then the artist waits for a procurement cycle. The fee range in most
   municipal programmes is €300–€1,200, paid in 60–120 days.
2. **Small works fall through.** A €420 bench, a €950 bike rack: too small for
   procurement, too visible to ignore. They wait for a season that never comes.
3. **Nothing is verifiable afterwards.** A resident cannot find out who was paid,
   what was promised, or whether the wall still exists. Neither can a funder.

## What we are funding

**21 walls. 21 artists. 9 cities. 6 months.** One campaign, two layers:

- **The campaign (the visible part).** An open call per city, reviewed with a
  paid local curator. Signed owner consent and a removal clause before paint.
  Half the fee on the approved brief, half on photographic documentation. Each
  wall is a Proof-of-Place entry.
- **The protocol (the infrastructure).** An open registry and escrow so anyone —
  a city, a DAO, a funder — can fund the next 21 walls and audit this batch.
  Tasks, bids, attestations and payments stay queryable after the grant closes.

The protocol is not a separate ask. It is the receipt for the campaign.

## Why Ethereum

- **Neutral settlement.** No company sits between a funder's dollar and an
  artist's invoice.
- **A global rail.** USDC on Base reaches an artist without a bank account, in
  seconds; SEPA in EUR is the other option, chosen by the artist.
- **An immutable record.** Who was commissioned, what was promised, what was
  paid — queryable even if 21 disappears.
- **Composability.** Matching pools, retro funding and EAS attestations plug into
  the same registry with no new rails.

## What is different

- Non-custodial by construction: one escrow contract per task, no proxy admin
  above user funds.
- Rules pinned before money arrives; a task cannot be funded until its payment
  logic is immutable.
- Verification designed for an adversary with a camera: signed capture, geofence,
  dual attestation, 72-hour challenge window.
- No token, no presale, no paid placement, no revenue share taken from artists.

## Deliverables

| # | Deliverable | Acceptance criterion | Share |
|---|---|---|---|
| M1 | Open call + contracts | 21 signed artist contracts, 9 owner-consent letters, curator engaged | 10% |
| M2 | First 7 walls, 3 cities | 7 walls installed, photographed and registered | 30% |
| M3 | Walls 8–14 + documentation | 7 more walls, plus photo and short-film package per city | 25% |
| M4 | Walls 15–21, 9 cities | All 21 walls installed and registered; 21 artists paid in full | 25% |
| M5 | Exhibition + open kit | 21 walls shown publicly; the artist kit published under MIT | 10% |

## Budget

| Line item | USD |
|---|---|
| Artist fees, 21 walls × $700 average | 14,700 |
| Paint, wall prep, lift or scaffold | 2,100 |
| Local photographer + short film | 2,100 |
| Consent, permits, insurance | 1,050 |
| Open call + paid curator | 1,050 |
| **Total** | **21,000** |

If the grant is smaller, we paint fewer walls — not cheaper ones.

## The artist deal

- €300–€1,200 per wall, always published, paid in two tranches: 50% on the
  approved brief, 50% on documentation.
- Median payout: 5 days from approval.
- Artist keeps copyright and credit; 21 takes a licence to document.
- Removal clause signed up front; if the owner asks for the wall back, it is
  paid for.
- No wall starts before consent and insurance are on file.

## Success metrics (targets, reported at close-out)

- 21 walls commissioned and documented (proof-of-place entries)
- 21 artists paid, median under 7 days (payout timestamps)
- 9 cities with a signed owner consent (consent registry)
- 100% of walls with written owner consent
- 40 tasks published, verified and settled through the registry
- 25 contractors paid through escrow

Guardrails: zero unauthorised walls, artist payment median under 7 days, fraud
under 1% of released value, disputes under 8% of tasks.

## Risks

| Risk | Mitigation |
|---|---|
| Artist pulls out | Signed contract before the call closes; named backup artist per city; fee escrowed in two tranches |
| Owner revokes permission | Removal clause signed up front; registry marks the wall retired; documentation stays public |
| Weather and access | Two-week buffer per city; indoor walls in the mix; lift booked only after consent |
| Fraudulent evidence | In-app signed capture, C2PA credentials, geofence, phash dedupe, human spot audits |
| GPS spoofing | Cell/Wi-Fi corroboration, on-site reviewer above €1,000 |
| Escrow exploit | Two audits, invariant fuzzing, per-task caps, 3-of-5 guardian pause with 48h delay |
| Resident privacy | On-device blur, coarse public coordinates, off-chain personal data, DPIA before pilot 1 |

Open question we bring to reviewers: what is the minimum viable proof for a
€300 repair that still resists a determined faker?

## Team

Three people plus a paid curator per city. Most of the money leaves the building
on day one of each wall.

- **[Name]** — protocol & product. Solidity/Foundry, civic interfaces, PWA
  capture. Owns the escrow, the registry and the public task page.
- **[Name]** — programme lead. Open calls, consent paperwork, wall calendar with
  the local curator.
- **[Name]** — field producer. Lift, paint, photographer; makes sure every wall
  finishes on the day it was promised.
- **[Name]** — advisor, municipal procurement and public-art permissions.

## Sustainability

- Optional 1.5% fee on released escrow, capped and opt-in per city — never on
  artist fees.
- Hosted instance and support subscription for municipalities.
- Matching pools funded by partners, not by the protocol.
- Year 2: registry ownership renounced; contracts, indexer, client and the artist
  kit stay MIT.

---

## Короткая версия (RU)

**21** — кампания заказных муралов с публичной бухгалтерией: 21 художник
расписывает 21 стену в 9 городах, каждый получает гонорар вовремя, каждая стена
попадает в открытый реестр на Ethereum.

Просим **$21 000 на 6 месяцев**. Не на код — код команда пишет сама. Деньги
уходят людям: в среднем **$700 за стену** художнику, плюс краска, подготовка
стены, подъёмник, страховка, согласия собственников, местный фотограф и оплаченный
куратор в каждом городе. 70% бюджета — напрямую художникам.

**Почему Ethereum:** эскроу вместо посредника, USDC на Base доходит до художника
без банковского счёта, а обещания и выплаты остаются проверяемыми после
закрытия гранта. Без токена, без кастодиального хранения, лицензия MIT.

**Слой протокола** — тот же открытый реестр и эскроу: следующий город или фонд
может финансировать свои 21 стену по тем же правилам. Кампания — это видимая
часть, протокол — квитанция.

Если грант меньше — расписываем меньше стен, а не дешевле.
