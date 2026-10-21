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

- [`grant/build/21-grant-deck.pdf`](grant/build/21-grant-deck.pdf) — 23-slide deck in the ethereum.org visual language; slide 09 is *The philosophy*: the six Ethereum principles below, each with the mechanic that already enforces it. The ask is a **floor of €7,500** for six months in one city, with the code hours at 250 ₽/h (€2,500); above the floor the split is fixed at 45% quest and project rewards in escrow, 15% consented walls and artists, 15% PR and kit, 10% verification, 6% safety, 5% infra, 4% reserve
- [`grant/application.md`](grant/application.md) — the same content as copy-paste text (EN + RU)
- [`grant/preview/`](grant/preview) — page previews
- **The app**, published at the root of GitHub Pages: civic problems on a map, donations into project budgets while commercial offers come in (the target is the lowest offer), escrow after acceptance — plus the grant landing at [`landing.html`](landing.html). The site root opens the app directly.

## Философия Ethereum — шесть принципов

Проект связан с Ethereum не только визуально: интерфейс, правила, лендинг, заявка
и дек говорят об одних и тех же шести принципах. Это не «крипта» и не обещание
сети — это форма договорённости без начальника: правила опубликованы до денег, их
нельзя переписать задним числом в свою пользу, и они одинаковы для министерства и
для подростка с трафаретом. Черновик при этом честно остаётся черновиком:
блокчейна, ключей и движения денег в нём нет, принципы описывают то, как правила
записаны уже сейчас — в интерфейсе и в тестах.

| Принцип | Что это значит | Где видно в продукте |
|---|---|---|
| **Достоверная нейтральность** · credible neutrality | Базовый слой не выбирает победителей и не может переписать правила под одного участника | Нет платных мест, алгоритма выдачи и менеджера: цель бюджета — минимальное опубликованное КП, правило видно в интерфейсе и закреплено тестами |
| **Без разрешения** · permissionless | Никому не нужно согласование, чтобы пользоваться сетью | Нарисовать число, опубликовать просьбу, прислать КП, пополнить бюджет и проверить результат может любой; набор MIT, у числа нет владельца |
| **Минимум доверия** · minimal trust | Опора на правила, которые исполняются как опубликованы, а не на обещание компании | Награда зафиксирована до начала работы, аванс даёт большинство по сумме взносов, выплата — после подтверждения обеих сторон |
| **Проверяй, а не верь** · verify, don't trust | Состояние может проверить любой, вместо веры в отчёт | Просьба, отклики, выбор, фото «до и после» и чек публичны: сосед проверяет скамейку, донор видит каждый евро |
| **Общее благо** · public goods | То, чем пользуются все, финансируют осознанно, а не вынимают из пользователей | Число, набор, чеки и код открыты; без токена, пресейла и процента с исполнителя |
| **Нет владельца** · no owner | Протокол, который никто не выключит для одного человека; владение отдают, а не держат | Директор не отменяет закрытый квест, компания не держит деньги; код остаётся MIT, на второй год владение реестром передаётся |

Где это живёт: секция «Философия» на лендинге (`landing.html#philosophy`, шесть
языков), блок принципов в модалке «Как это работает» приложения (`index.html`,
словарь `city.js`), раздел *The philosophy* в заявке
([`grant/application.md`](grant/application.md)) и слайд 09 дека
([`grant/build/21-grant-deck.pdf`](grant/build/21-grant-deck.pdf)). Тесты
проверяют, что принципы есть на всех шести языках и что рядом с ними сказано про
отсутствие блокчейна в черновике.

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
| `assets/img/community-garden.webp` | AI-generated neighbourhood illustration with neighbours — no mascot character. |
| `assets/img/ill-*.webp` | Eight more flat-vector illustrations (quests, map, wallet, tools, meeting, empty state, profile, how-it-works). Same ivory ground `#FAF2DE` as the app background, no text, no mascot. |
| `assets/img/favicon.png` | Favicon — рукописная «21» на фирменном фиолетовом (180×180, она же apple-touch-icon). |
| `tests/app.test.cjs` | Ten integration tests running the real app script in jsdom. |
| `city.js` | All app logic: state (localStorage), i18n, cards, the map, donations, offers, the timeline, the wizard. |
| `landing.html` + `style.css` + `app.js` | The grant landing: language switch and scroll reveal. |
| `assets/vendor/leaflet/` | Self-hosted Leaflet 1.9.4 (BSD-2-Clause) so the app has zero external runtime dependencies. Map tiles: CARTO Voyager over OpenStreetMap data. |
| `assets/img/projects/` | Generated placeholder photos for the seeded projects (resized copies of `grant/photos/`). |
| `assets/fonts/` | Self-hosted, subset `woff2`: Geist, Geist Mono, Gaegu (the child’s hand for numbers), Pangolin (handwritten notes, Latin + Cyrillic). CJK falls back to the system stack (PingFang SC, Hiragino, Yu Gothic, Malgun Gothic, Noto CJK). |
| `tools/i18n.py` + `tools/i18n/*.json` | Extraction and translation pipeline for the six languages: `python3 tools/i18n.py extract|apply|check`. |

**Language.** Six languages: Russian, English, Spanish, Chinese, Japanese and
Korean. The shell holds the static strings in the markup
(`<span lang="ru">…</span><span lang="en">…</span>…`); a single CSS rule hides
every `lang` attribute that does not match `html[data-lang]`. Dynamic strings
live in the `I18N` dictionary in `city.js` (`ru`/`en`/`es`/`zh`/`ja`/`ko` keys,
with `ru → en` fallback for missing entries); seeded data carries the same six
ways. The header dropdown (`#langMenu`) switches the language, the choice is
stored in `localStorage` and also accepted as `?lang=`. `T(key)` resolves a
dictionary entry, `loc(obj)` a `{ru, en, es, zh, ja, ko}` pair.

**Seeds.** Five projects and four quests, matching the reference mockups.
“Reset demo data” in the profile returns everything to the seeds. The seed
language follows the browser (`navigator.language`).


---

## Сессия 20.10.2026 — рабочий черновик v0.2

### Что сделано

- Вместо экрана телефона на десктопе — широкий адаптивный workspace: верхняя
  навигация, сетки карточек, отдельная панель проекта; на мобильном — нижнее меню.
- Визуальное направление: светлый фон, свободное пространство, тонкие рамки,
  лавандовые акценты и доброжелательные иллюстрации, вдохновлённые ethereum.org.
  Это собственные иллюстрации, не официальные персонажи Ethereum.
- Сгенерирована иллюстрация района с жителями. Маскота в проекте нет вообще:
  Смайл и прежний Росток удалены из разметки, стилей и файлов, иллюстрация района
  перегенерирована без персонажа, а фасикон и OG-карточка несут только знак «21».
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
npm test       # 10 интеграционных тестов: проходят
npm run check # синтаксис city.js и app.js: проходит
```

Тесты проверяют запуск, каталог, именные взносы и сохранение, КП и минимальную
цену, профиль и безопасный вывод имени, маршруты, публикацию и отклик на квест,
повреждённый JSON и подтверждение сброса, переключение всех шести языков в
приложении и на лендинге. Это DOM-тесты, **не проверка пикселей**.
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

## Сессия 21.10.2026 — иллюстрации, единый фон, шесть языков

### Что сделано

- **Иллюстрации.** Восемь новых плоских векторных иллюстраций: квесты, карта,
  кошелёк, инструменты, встреча района, пустое состояние, профиль и «как это
  работает». Все девять картинок (включая `community-garden.webp`) переведены в
  WebP и перекрашены в один фон `#FAF2DE`, поэтому вставляются без рамок и
  «наложения». Иллюстрации не декоративные: карта, каталог, кошелёк, профиль,
  модалка «как это работает» и пустое состояние каталога получили свои картинки.
  Персонажа-маскота по-прежнему нет, текста на картинках нет.
- **Фон приложения = фон картинок.** Бумага `--paper:#faf2de`, светлая подложка
  `--paper-2:#f2e8d2`, белые карточки `--white:#fffdf7`, фиолетовый акцент
  `--violet:#6c24df`; фон страницы `#f1ead4`. Иллюстрации на фоне и в белых
  карточках стоят бесшовно.
- **Шесть языков: RU, EN, ES, ZH, JA, KO.** Переведены разметка приложения
  (28 пар строк), лендинг (211 строк), словарь интерфейса `city.js` (184 ключа
  на язык) и сид-данные. Переключатель в шапке — выпадающее меню с шестью
  кнопками, язык сохраняется в `localStorage`, принимается `?lang=`, новый язык
  подставляется в `<title>`, подсказку поиска и `html[lang]`.
  Переводы динамических строк идут через `T(key)` с откатом `текущий → en → ru`,
  пары сид-данных — через `loc(obj)`. Иероглифы и кана печатают системными
  шрифтами (PingFang SC, Hiragino, Yu Gothic, Malgun Gothic, Noto CJK).
- **Инструменты.** `tools/i18n.py extract|apply|check` переносит строки в
  JSON-каталоги, применяет переводы и проверяет, что в ключах нет артефактов
  и потерянных языков. `tools/i18n/city.i18n.json` — словари ES/ZH/JA/KO
  интерфейса, `tools/i18n/city.seed.json` — переводы сид-объектов.
- **Тесты.** Добавлены два теста: переключение шести языков в приложении
  (включая перевод сид-карточек) и переключение языков на лендинге.

### Как проверять

```bash
python3 -m http.server 8080 --bind 0.0.0.0
npm ci && npm test && npm run check
python3 tools/i18n.py check
```

Живой предпросмотр поднимается статическим сервером на порту 8080.

---

## Сессия 21.10.2026 — связь с философией Ethereum на всех поверхностях

### Что сделано

- **Смысл.** Сформулированы шесть принципов, которыми проект связан с философией
  Ethereum: достоверная нейтральность, без разрешения, минимум доверия, проверяй
  а не верь, общее благо, нет владельца. У каждого принципа есть механика, которая
  закрепляет его уже в черновике, и честная оговорка: блокчейна, ключей и движения
  денег в черновике нет, принципы описывают то, как правила записаны сейчас.
- **Заявка.** В [`grant/application.md`](grant/application.md) добавлен раздел
  *The philosophy — what 21 takes from Ethereum*: таблица «принцип → что это
  значит в Ethereum → как закреплено в 21» и абзац *What this is not*; в короткой
  RU-версии появился абзац «Философия Ethereum». Раздел *Why Ethereum* оставлен
  про рельсы (эскроу, USDC, запись) и начинается со ссылки на философию.
- **Дек.** [`grant/build/21-grant-deck.pdf`](grant/build/21-grant-deck.pdf) стал
  23-страничным: новый слайд 09 «The philosophy» (шесть карточек: принцип, что он
  значит в Ethereum, строка *IN 21* с механикой, внизу — оговорка про локальный
  черновик). Номера разделов 08–20 сдвинуты на 09–21, `TOTAL` и футер обновлены,
  превью `preview/p01…p23.png` пересобраны.
- **Лендинг.** Новая секция `#philosophy` (пункт «Философия» в навигации): лид про
  «договариваться без начальника», шесть карточек принципов и карточка «Честно о
  черновике». Всё на шести языках через `tools/i18n` (229 пар в каталоге).
- **Приложение.** В модалке «Как это работает» (`index.html`) под пятью шагами
  появился блок `prin` с шестью принципами и пометкой про отсутствие блокчейна;
  строки живут в словаре `city.js` на шести языках и продублированы в
  `tools/i18n/city.i18n.json`. Стили — в `city.css`.
- **Тесты.** Добавлены два: принципы в модалке на всех шести языках (словарь, а не
  фолбэк) + оговорка про блокчейн рядом; секция лендинга на шести языках и ссылка
  в навигации. Было 10 тестов, стало 12.
- **Оснастка.** Найден и обойдён подводный камень `tools/i18n.py apply`: на уже
  развёрнутой разметке команда дублирует es/zh/ja/ko-спаны (регулярка ловит только
  пару ru+en). Новые пары разворачивались точечно, каталоги и файлы переводов
  пересогласованы по порядку; `python3 tools/i18n.py check` проходит.

### Как проверять

```bash
python3 -m http.server 8080 --bind 0.0.0.0   # приложение и лендинг
npm ci && npm test && npm run check          # 12 тестов, синтаксис
python3 tools/i18n.py check                  # переводы на месте
cd grant/tools && python3 build.py --preview # дек (нужны reportlab, pypdfium2, pillow)
```

Живой предпросмотр поднимается статическим сервером: `/` — приложение,
`/landing.html` — лендинг с новой секцией «Философия».

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
7. **Иллюстрации**: восемь новых иллюстраций уже переведены в WebP и стоят
   под реальными состояниями (каталог, карта, кошелёк, профиль, пустой каталог).
   Дальше — AVIF и иллюстрация успешной приёмки. Маскот не возвращается —
   иллюстрация района уже без персонажа; иллюстрации добавлять под реальные
   состояния, а не как декор без функции.

**Готовность следующего этапа:** два разных пользователя видят одну заявку;
роли ограничивают действия; после перезагрузки сохраняются предложения и этап;
есть тесты API и browser smoke; README описывает запуск и ограничения.
