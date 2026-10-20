# 21movement

**21** — a number anyone can paint, and an escrowed exchange of services under it.

Someone posts what they need — a tutor, a handyman, a psychologist — names a
reward and a deadline. Named people send offers, the asker chooses, the work
happens, both sides confirm, escrow pays, and the receipt stays public. The same
protocol runs civic tasks in public space (a bench, a bike rack, a tram stop) and
larger projects — a street rebuild, a school roof, a construction site — published
with a budget, an open tender and milestone escrow, then split into quest-sized
pieces.

The campaign is the number itself. It cannot be banned, copyrighted or translated,
and it looks best when it is amateur: chalk on asphalt, a sticker on a broken
bench, a construction hoarding, a six-second TikTok. The goal is for 21 to become
a meme rather than an ad: one large PR agency on retainer, paid per published
placement and per settled quest. A free MIT kit — stencil, stickers, chalk
templates — lets anyone print their own.

The grant application lives in [`grant/`](grant/README.md):

- [`grant/build/21-grant-deck.pdf`](grant/build/21-grant-deck.pdf) — 22-slide deck in the ethereum.org visual language; the ask is a **floor of €7,500** for six months in one city, with the code hours at 250 ₽/h (€2,500); above the floor the split is fixed at 45% quest and project rewards in escrow, 15% consented walls and artists, 15% PR and kit, 10% verification, 6% safety, 5% infra, 4% reserve
- [`grant/application.md`](grant/application.md) — the same content as copy-paste text (EN + RU)
- [`grant/preview/`](grant/preview) — page previews
- **The app**, published at the root of GitHub Pages: civic problems on a map, donations into project budgets while commercial offers come in (the target is the lowest offer), escrow after acceptance — plus the grant landing at [`landing.html`](landing.html). The site root opens the app directly.

## The app — [`index.html`](index.html)

A bilingual (RU/EN), local-first application draft inspired by the ethereum.org visual language.
Someone photographs a broken sidewalk with coordinates; neighbours see it on the
map, add to the project budget with donations while commercial offers (КП) come
in from contractors; **the budget target is the lowest offer**; the requester
accepts an offer, the work happens, escrow pays after acceptance, the receipt
stays public.

It is a static site — no build step, no framework. The app keeps its state in
`localStorage`; the only runtime libraries are self-hosted
([Leaflet](assets/vendor/leaflet) for the map). Open `index.html` or serve the
repo root:

```bash
python3 -m http.server 8080
# http://localhost:8080
```

### The mechanics implemented

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

### Files

| Path | What it is |
|---|---|
| `index.html` | The app shell: five tabs (Home, Map, Projects, Wallet, Profile), the project detail overlay and the modals. |
| `city.css` | The app’s design tokens and layout — the same paper/ink/sticker language as the landing. Base component styles; the responsive workspace overrides live in `workspace.css`. |
| `workspace.css` | Responsive desktop workspace, mobile navigation, lavender / ivory theme. |
| `assets/img/community-garden.png` | AI-generated neighbourhood illustration with neighbours and the Sprout character. |
| `assets/img/mascot-sprout.png` | AI-generated original mascot: Sprout / Росток. |
| `tests/app.test.cjs` | Eight integration tests running the real app script in jsdom. |
| `city.js` | All app logic: state (localStorage), i18n, cards, the map, donations, offers, the timeline, the wizard. |
| `landing.html` + `style.css` + `app.js` | The grant landing: language switch and scroll reveal. |
| `assets/vendor/leaflet/` | Self-hosted Leaflet 1.9.4 (BSD-2-Clause) so the app has zero external runtime dependencies. Map tiles: CARTO Voyager over OpenStreetMap data. |
| `assets/img/projects/` | Generated placeholder photos for the seeded projects (resized copies of `grant/photos/`). |
| `assets/fonts/` | Self-hosted, subset `woff2`: Geist, Geist Mono, Gaegu (the child’s hand for numbers), Pangolin (handwritten notes, Latin + Cyrillic). |

**Language.** The shell holds both languages in the markup
(`<span lang="ru">…</span><span lang="en">…</span>`); dynamic strings live in an
i18n dictionary in `city.js` (`I18N`). The RU/EN pill in the header switches
both, and seeded data carries `{ru, en}` pairs.

**Seeds.** Five projects and four quests, matching the reference mockups.
“Reset demo data” in the profile returns everything to the seeds.


---

## Сессия 20.10.2026 — рабочий черновик v0.2

### Что сделано

- Вместо экрана телефона на десктопе — широкий адаптивный workspace: верхняя
  навигация, сетки карточек, отдельная панель проекта; на мобильном — нижнее меню.
- Визуальное направление: светлый фон, свободное пространство, тонкие рамки,
  лавандовые акценты и доброжелательные иллюстрации, вдохновлённые ethereum.org.
  Это собственные иллюстрации, не официальные персонажи Ethereum.
- Сгенерированы иллюстрация района с жителями и маскот **Росток / Sprout**:
  лавандовый персонаж с листочками и набором инструментов. Иллюстрация — на главной,
  отдельный маскот — в профиле.
- Каталог: текстовый поиск по проектам и квестам, фильтры типов, сортировка
  проектов по расстоянию, новизне и доле собранного бюджета, пустое состояние.
  У квестов сортировка по наполнению бюджета не применяется.
- Статистика района рассчитывается из текущих данных, не зашита в интерфейс.
- Редактируемое имя профиля, экспорт всего состояния в JSON, подтверждение сброса.
- Маршруты `#/home`, `#/map`, `#/projects`, `#/wallet`, `#/profile`,
  `#/project/1`; раздел или проект открывается по ссылке и после перезагрузки.
  Ссылки на пользовательские проекты работают только в браузере, где они созданы.
- Уточнена маркировка песочницы: реальные деньги не списываются, блокчейн не подключён.
- Исправления: взнос с именем теперь остаётся взносом текущего пользователя;
  пустая цена КП не превращается в €1; повреждённое хранилище обрабатывается;
  ошибка сохранения больше не скрывается молча. Добавлены фокус в модалках,
  удержание Tab внутри диалога и корректный приоритет Escape.

### Запуск и проверки

Приложение по-прежнему не требует сборки или npm для работы:

```bash
python3 -m http.server 8080 --bind 0.0.0.0
# открыть http://localhost:8080
```

Node.js 22+ нужен только для инструментов разработки:

```bash
npm ci
npm test       # 8 интеграционных тестов: проходят
npm run check # синтаксис city.js и app.js: проходит
```

Тесты проверяют запуск, каталог, именные взносы и сохранение, КП и минимальную
цену, профиль и безопасный вывод имени, маршруты, публикацию и отклик на квест,
повреждённый JSON и подтверждение сброса. Это DOM-тесты, **не проверка пикселей**.
Попытка запуска headless Chromium в этой среде заблокирована отсутствующей
системной библиотекой `libnspr4.so`; визуальная проверка desktop/mobile остаётся
отдельным пунктом следующей сессии. Live preview поднимается статическим сервером.

### Границы текущего черновика

Это работающий **однопользовательский локальный frontend**, не production-сервис.
Заявки, чат, предложения и бюджет существуют только в `localStorage` под ключом
`21city.v1`; данные между устройствами не синхронизируются. Авторизации, API,
базы данных, реальных переводов, смарт-контрактов, модерации и защиты ролей пока
нет. Переключение этапов и рейтинги подрядчиков — демонстрационные. Фото проектов
и новые иллюстрации сгенерированы. Карта требует интернет-доступа к тайлам CARTO / OSM.
Экспорт JSON есть; импорт ещё не реализован. Не используйте черновик для реальных
сборов средств. При очистке браузера локальные данные теряются.

## Задание на следующую сессию

**Цель: превратить локальный черновик в совместный тестовый MVP, не подключая
реальные платежи до определения правил и модели безопасности.**

1. **Начать с проверки UI в браузере** на 390, 768 и 1440 px: главная, каталог,
   карта, создание заявки, модалки, панель проекта, профиль, RU/EN. Проверить
   отсутствие горизонтального переполнения, фокус и навигацию назад/вперёд.
   Добавить Playwright smoke-тесты в среде с установленным Chromium.
2. **Согласовать backend и роли**: житель, автор, подрядчик, проверяющий.
   Выбрать хранилище/авторизацию, затем выделить репозиторий данных из `city.js`
   (localStorage-адаптер оставить для offline/demo). Не переписывать существующие
   сценарии ради новой верстки и не терять сохранённые данные.
3. **Реализовать вертикальный сценарий через API**: вход → заявка с фото и
   координатами → предложение → выбор подрядчика → выполнение → приёмка.
   Права проверять на сервере; участник не должен сам назначать себе роль
   проверяющего или переводить чужие проекты на следующий этап.
4. **Финансовая модель**: явно разделить предварительные обещания взносов,
   тестовое эскроу и реальные платежи; определить условия недостатка бюджета,
   авансов, отказа, отмены и возврата. Зафиксировать инварианты тестами. Не
   обещать on-chain запись до настоящей интеграции и аудита.
5. **Данные и надёжность**: добавить валидируемый импорт JSON с версией схемы,
   подтверждением и миграциями; покрыть переполнение хранилища и повреждённые
   структуры; довести валидацию всех числовых полей и загрузки изображений.
6. **Завершить доступность**: семантические кнопки открытия карточек, возврат
   фокуса из панели проекта, недоступный фон диалогов, локализованные aria-label,
   обработка недоступных тайлов карты, ошибок геолокации и пустых состояний.
7. **Иллюстрации**: подготовить оптимизированные WebP/AVIF из текущих PNG;
   сохранить узнаваемость Ростка. Новых персонажей добавлять под реальные
   состояния (пустой каталог, успешная приёмка), а не как декор без функции.

**Готовность следующего этапа:** два разных пользователя видят одну заявку;
роли ограничивают действия; после перезагрузки сохраняются предложения и этап;
есть тесты API и browser smoke; README описывает запуск и ограничения.
