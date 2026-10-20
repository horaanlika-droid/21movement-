# 21 — grant application text

Copy-paste source for the written parts of an Ethereum ecosystem grant
(ESP-style form). Numbers match the deck: **$75,000 over 10 months**.
Replace every `[…]` placeholder before submitting.

---

## Project name

21

## One-line description

Ethereum-native civic infrastructure: report a real-world problem, fund the fix,
hire the people who do the work, and verify the result — settled on-chain.

## Website / repo

- Website: `https://21.city` (in development)
- Repository: `https://github.com/horaanlika-droid/21movement-`

## Problem

Cities can see problems and cannot coordinate fixes.

1. **Reporting ends in a ticket.** A photo to a hotline produces a reference
   number, not a budget. Residents never learn who decided, who was paid, or
   what actually happened.
2. **Small works fall through.** A €420 bench, a €950 bike rack, a €300 mural:
   too small for procurement, too visible to ignore. They wait for a season that
   never comes.
3. **Public-goods funding stops at the screen.** Crypto has capital, matching
   pools and governance tooling for digital work. There is no delivery layer for
   physical work.

## Solution

21 is an open protocol plus a web/PWA client that turns a geotagged report into
a funded, contracted and verified piece of work:

1. **Report** — photo, GPS, category, urgency (under 60 seconds on mobile).
2. **Propose** — contractors publish itemised budgets, milestones and timelines.
3. **Fund** — community contributions and a matching pool fill a per-task escrow.
4. **Decide** — eligible participants select a proposal under rules published
   before funding opened (default: one person, one vote).
5. **Build** — work happens in the physical world.
6. **Verify** — device-signed evidence, geofence checks, dual attestation and a
   72-hour challenge window.
7. **Settle** — escrow releases a milestone tranche to the contractor.

Everything that matters — who was selected, what was promised, what was paid —
is queryable by anyone, including after 21 the company stops existing.

## Why Ethereum

- **Neutral settlement.** No company sits between a resident's euro and a
  contractor's invoice. The escrow is the counterparty.
- **A global payment rail.** USDC on Base pays a contractor in Nairobi or
  Nijmegen in seconds, without a bank account.
- **Composable public goods.** Quadratic funding, retro funding, EAS
  attestations and Safe treasuries plug in unchanged.
- **Permanent public record.** Promises, funding and delivery stay verifiable.

## What is different

- Non-custodial by construction: one escrow contract per task, no proxy admin
  above user funds.
- Rules are pinned before money arrives; a task cannot be funded until its
  payment logic is immutable.
- Verification is designed for an adversary with a camera, not for a happy path.
- No token, no presale, no paid placement.

## Deliverables

| # | Deliverable | Acceptance criterion | Share |
|---|---|---|---|
| M1 | Protocol spec + threat model | Published RFC, 2 external reviews | 5% |
| M2 | Contracts on testnet | 90%+ coverage, invariants fuzzed, testnet deploy | 10% |
| M3 | Alpha app: report → task → escrow | A bench task completed end-to-end on testnet | 15% |
| M4 | Verification + dispute modules | Dual attestation and a resolved dispute in a live drill | 10% |
| M5 | Two independent audits | Reports published; all critical/high fixed | 20% |
| M6 | Base mainnet launch | Verified contracts, per-task cap, guardian live | 10% |
| M7 | Three city pilots | 3 partners, 20 tasks each, real payouts | 20% |
| M8 | Open source + SDK | MIT release, docs, 3 external integrators | 10% |

## Budget

| Line item | USD |
|---|---|
| Smart contracts, tests, two audits | 24,000 |
| Product, frontend, mobile PWA | 18,000 |
| Backend, indexer, storage pipeline | 9,500 |
| Verification, dispute and reviewer tooling | 7,500 |
| Three city pilots and the mural programme | 9,000 |
| Design system, documentation, Storybook | 4,000 |
| Legal, GDPR review, operations, travel | 3,000 |
| **Total** | **75,000** |

If the grant is smaller than requested, the audits and the mainnet launch are the
last things we cut.

## Success metrics (targets, reported at close-out)

- 3 city partners under a signed pilot agreement
- 60 tasks published, verified and settled
- €45k of value moved through escrow
- 25 contractors paid, median payout under 24 hours
- 21 commissioned murals registered on-chain
- 500 unique participants with proof-of-personhood

Guardrails: fraud under 1% of released value, disputes under 8% of tasks, median
time to first proposal under 72 hours, more than 40% repeat contractors.

## Team

- **[Name]** — protocol lead. Solidity/Foundry, escrow design, prior public-goods
  deployment. Owns M1–M6 and both audits.
- **[Name]** — product & design lead. Civic interfaces, map and form UX,
  accessible design systems. Owns M3, M7.
- **[Name]** — full-stack engineer. Next.js, indexer, media pipeline, PWA capture.
  Owns M3, M7.
- **[Name]** — advisor, municipal procurement and public-art permissions.

## Risks

| Risk | Mitigation |
|---|---|
| Fraudulent evidence | In-app signed capture, C2PA credentials, geofence, phash dedupe, human spot audits |
| GPS spoofing | Cell/Wi-Fi corroboration, on-site reviewer above €1,000 |
| Reporter–contractor collusion | Role separation, random reviewer panel, payout caps for new addresses |
| Sybil voting | Personhood-gated eligibility, snapshot at vote open |
| Escrow exploit | Two audits, invariant fuzzing, per-task caps, 3-of-5 guardian pause with 48h delay |
| Resident privacy | On-device blur, coarse public coordinates, off-chain personal data, DPIA before pilot 1 |

Open question we bring to reviewers: what is the minimum viable proof for a
€300 repair that still resists a determined faker?

## Sustainability

- Optional 1.5% fee on released escrow, capped and opt-in per city.
- Hosted instance and support subscription for municipalities.
- Matching pools funded by partners, not by the protocol.
- Year 2: registry ownership renounced; contracts, indexer and client stay MIT.

## Cultural layer (the 21 campaign)

A commissioned, always-authorised mural programme runs alongside the protocol:
21 walls in 21 cities in year one, €300–€1,200 per wall, each with signed owner
consent, a removal clause and a paid artist. Unauthorised graffiti is explicitly
out of scope — the registry refuses locations without a permission record.

---

## Короткая версия (RU)

**21** — открытый Ethereum-протокол, который связывает цифровую координацию и
деньги с реальными работами в городе: житель фотографирует проблему, подрядчики
предлагают сметы, сообщество финансирует и выбирает решение, деньги лежат в
эскроу на задачу и выплачиваются по факту проверенного результата.

Просим **$75 000 на 10 месяцев**: контракты, два аудита, приложение (веб + PWA),
запуск на Base и три городских пилота. Без токена и без кастодиального хранения
средств, лицензия MIT.

Отдельный слой — кампания «21»: легальные заказные муралы с цифрой 21 в 21 городе
(у каждого — согласие собственника стены и оплаченный художник). Цифра не требует
перевода и работает как мем; протокол за ней — как инфраструктура.
