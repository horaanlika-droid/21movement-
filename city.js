/* 21.city — локальный черновик приложения.
   Механика: заявка с фото и координатами → карта → донаты в бюджет, пока
   контрагенты присылают КП → цель бюджета = минимальная цена КП → выбор
   подрядчика → аванс на материалы по обоснованию (голосуют донатеры) →
   работа → приёмка → эскроу платит, чек публичный.
   Данные живут в localStorage. Никаких серверов, токенов и сборов. */
(function () {
  "use strict";

  /* ============================================================ i18n */
  var I18N = {
    ru: {
      newest: "Сначала новые", funding: "Ближе к цели", tabHome: "Обзор", tabMap: "Карта", tabProjects: "Проекты", tabWallet: "Кошелёк", tabProfile: "Профиль",
      findProject: "Найти проект",
      questsNearby: "Квесты рядом", projectsNearby: "Проекты рядом", nearbyProjects: "Проекты рядом",
      all: "Все", projects: "Проекты", quests: "Квесты",
      forYou: "Для вас", popular: "Популярные", nearby: "Рядом",
      projectsTitle: "Проекты и квесты",
      projectsSub: "Городские проблемы с фото и координатами — и задания соседей",
      walletTitle: "Кошелёк", walletSub: "Ваши взносы в бюджеты городских проектов",
      inBudgets: "В бюджетах проектов",
      active: "Активные", contributed: "Мои взносы", completed: "Завершённые",
      you: "Вы", myProjects: "Мои проекты", myQuests: "Мои квесты", wallet: "Кошелёк",
      howWorks: "Как это работает", resetDemo: "Сбросить демо-данные",
      addToBudget: "Добавить в бюджет", donate: "Пожертвовать",
      other: "Другая", yourAmount: "Ваша сумма, €", yourName: "Имя (как показать)",
      submitOffer: "Подать КП", sendOffer: "Отправить КП",
      contractor: "Подрядчик / компания", price: "Цена, €", days: "Срок, дней",
      postNeed: "Сообщить о проблеме", whatHappened: "Что случилось", desc: "Подробнее",
      category: "Категория", publish: "Опубликовать", place: "Место", gotIt: "Понятно",
      locate: "Где я", newProblem: "Сообщить о проблеме",
      open: "Открыт", viewOnMap: "На карте", details: "Подробнее",
      offersShort: "КП", donationsShort: "донаты", addBudgetShort: "+ В бюджет",
      budgetTitle: "Бюджет проекта", of: "из",
      targetMin: "Цель — минимальное КП", targetEst: "Оценка автора — КП ещё не поступили",
      donors: "Внесли",
      offersTitle: "Коммерческие предложения", minPrice: "мин. цена",
      shortfall: "до минимального КП не хватает", canTopUp: "— бюджет можно дополнить, пока идут работы",
      accept: "Принять",
      chatTitle: "Чат проекта", chatPlaceholder: "Сообщение…", send: "Отправить",
      advanceTitle: "Аванс на материалы и работу",
      requestAdvance: "Запросить аванс", sendRequest: "Отправить запрос",
      advAmount: "Сумма аванса, €", advReason: "Обоснование",
      advBy: "запросил аванс", giveAdvance: "Дать аванс", declineAdvance: "Отказать",
      advVotersOnly: "Голосуют донатеры этого проекта",
      advToVote: "Внесите любую сумму, чтобы голосовать",
      advFor: "за", advAgainst: "против", yourVote: "Ваш голос",
      advOpenA: "Проголосовало", advOpenB: "из собранного", advRule: "нужно большинство по сумме взносов",
      advApproved: "Аванс одобрен", advRejected: "Аванс отклонён донатерами",
      advPaidNote: "выплачен подрядчику из эскроу", advRestNote: "в эскроу до приёмки",
      advReRequest: "Запросить заново", advDemoNote: "Подрядчик может запросить предоплату — с обоснованием",
      timelineTitle: "Как идёт проект", now: "сейчас",
      stage1: "Поддержка сообщества", stage1d: "соседи пополняют бюджет донатами",
      stage2: "Поиск подрядчиков", stage2d: "КП открыты, цель бюджета — минимальная цена",
      stage3: "Работа идёт", stage3d: "после выбора подрядчика",
      stage4: "Приёмка", stage4d: "подтвердить и заплатить",
      stage5: "Готово", stage5d: "результат публичный",
      chainNote: "В песочнице все шаги записываются только в этом браузере. Эскроу и выплаты симулируются; блокчейн не подключён.",
      demoPick: "Выбрать подрядчика (демо)", demoWorkDone: "Работы завершены (демо)", demoPay: "Подтвердить и оплатить (демо)",
      budgetReady: "Бюджет собран — можно заказывать",
      works: "работ",
      respond: "Откликнуться", responded: "Отклик отправлен",
      publishLive: "Заявка опубликована!",
      publishLiveD: "Соседи теперь видят её на карте и могут предлагать помощь и КП.",
      seedDonate: "Добавить €25 в бюджет", later: "Позже",
      becomeContractor: "Стать подрядчиком",
      becomeContractorD: "Помогайте району своими навыками. Получайте оплату за реальную работу.",
      contractorOn: "Вы подрядчик", myOffers: "Мои КП",
      offersSent: "КП отправлено", tasksDone: "Выполнено", earned: "Заработано",
      pickOnMap: "Ткните в карту, чтобы указать место",
      how1t: "1 · Поддержка сообщества", how1d: "Кто-то фотографирует сломанный асфальт у дома. Соседи рядом видят проблему на карте и пополняют бюджет проекта донатами.",
      how2t: "2 · Поиск подрядчиков", how2d: "Пока собираются донаты, контрагенты присылают коммерческие предложения. Цель бюджета — минимальная цена КП.",
      how3t: "3 · Работа", how3d: "Когда бюджет собран, выбирается лучшее КП и подрядчик приступает. Аванс на материалы — по обоснованию, голосованием донатеров.",
      how4t: "4 · Приёмка", how4d: "Соседи подтверждают результат — эскроу платит подрядчику.",
      how5t: "5 · Готово", how5d: "Чек остаётся публичным: каждый шаг виден, деньги ушли на работу.",
      t_donated: "€+AMOUNT в бюджет проекта. Это поможет привлечь КП и ускорить работу.",
      t_offer_new_min: "Цель бюджета пересчитана: €AMOUNT — минимальное КП.",
      t_offer_added: "КП отправлено. Оно видно всем в тендере проекта.",
      t_accepted: "КП принято. Работа начинается.",
      t_work_done: "Работы завершены. Ждём приёмку.",
      t_paid: "Эскроу выплачен подрядчику. Чек публичный.",
      t_adv_requested: "Запрос аванса отправлен донатерам проекта.",
      t_adv_approved: "Донатеры одобрили аванс — выплачен из эскроу.",
      t_adv_rejected: "Донатеры отклонили аванс.",
      t_adv_vote_y: "Голос учтён: за аванс.",
      t_adv_vote_n: "Голос учтён: против аванса.",
      t_vote: "Отметили: вам это тоже мешает.",
      t_unvote: "Отметка снята.",
      t_geo: "Обновлено: показываем проекты рядом с вами.",
      t_geo_err: "Не удалось узнать местоположение.",
      t_published: "Проект опубликован. Он на карте.",
      t_quest: "Отклик отправлен (демо).",
      t_contractor: "Теперь вы можете подавать КП на проекты района.",
      t_reset: "Демо-данные сброшены.",
      joinedAgo: "в проекте", m: "мес.",
      back: "Назад", project: "Проект",
      estLabel: "оценка", noOffersYet: "Пока нет КП — бюджет считается по оценке автора.",
      awaitingOffers: "ждём КП", chosen: "выбрано",
      emptyWallet: "Пока нет взносов. Найдите проект рядом и поддержите его.",
      emptyList: "Ничего не нашлось."
    },
    en: {
      newest: "Newest first", funding: "Closest to goal", tabHome: "Overview", tabMap: "Map", tabProjects: "Projects", tabWallet: "Wallet", tabProfile: "Profile",
      findProject: "Find a project",
      questsNearby: "Quests nearby", projectsNearby: "Projects nearby", nearbyProjects: "Nearby projects",
      all: "All", projects: "Projects", quests: "Quests",
      forYou: "For you", popular: "Popular", nearby: "Nearby",
      projectsTitle: "Projects & quests",
      projectsSub: "Civic problems with photos and coordinates — and neighbours’ tasks",
      walletTitle: "Wallet", walletSub: "Your contributions to civic project budgets",
      inBudgets: "In project budgets",
      active: "Active", contributed: "Contributed", completed: "Completed",
      you: "You", myProjects: "My projects", myQuests: "My quests", wallet: "Wallet",
      howWorks: "How it works", resetDemo: "Reset demo data",
      addToBudget: "Add to budget", donate: "Donate",
      other: "Other", yourAmount: "Your amount, €", yourName: "Name (to display)",
      submitOffer: "Submit an offer", sendOffer: "Send offer",
      contractor: "Contractor / company", price: "Price, €", days: "Days",
      postNeed: "Post a need", whatHappened: "What happened", desc: "Details",
      category: "Category", publish: "Publish", place: "Place", gotIt: "Got it",
      locate: "Where am I", newProblem: "Post a need",
      open: "Open", viewOnMap: "View on map", details: "Details",
      offersShort: "offers", donationsShort: "donations", addBudgetShort: "+ Add to budget",
      budgetTitle: "Project budget", of: "of",
      targetMin: "Target — the lowest offer", targetEst: "Author’s estimate — no offers yet",
      donors: "Contributors",
      offersTitle: "Commercial offers", minPrice: "lowest",
      accept: "Accept",
      chatTitle: "Project chat", chatPlaceholder: "Message…", send: "Send",
      advanceTitle: "Advance for materials and work",
      requestAdvance: "Request an advance", sendRequest: "Send request",
      advAmount: "Advance amount, €", advReason: "Justification",
      advBy: "requested an advance", giveAdvance: "Give the advance", declineAdvance: "Decline",
      advVotersOnly: "Only this project’s donors vote",
      advToVote: "Donate any amount to vote",
      advFor: "for", advAgainst: "against", yourVote: "Your vote",
      advOpenA: "Voted", advOpenB: "of collected", advRule: "a majority of contributed amount is needed",
      advApproved: "Advance approved", advRejected: "Advance declined by donors",
      advPaidNote: "paid to the contractor from escrow", advRestNote: "held in escrow until acceptance",
      advReRequest: "Request again", advDemoNote: "The contractor can request a prepayment — with a justification",
      timelineTitle: "How the project is going", now: "now",
      stage1: "Community support", stage1d: "neighbours add to the budget with donations",
      stage2: "Find contractors", stage2d: "offers are open, the target is the lowest price",
      stage3: "Work in progress", stage3d: "after the contractor is chosen",
      stage4: "Verification", stage4d: "confirm and pay",
      stage5: "Completed", stage5d: "the result is public",
      chainNote: "Sandbox: steps are stored only in this browser. Escrow and payouts are simulated; no blockchain is connected.",
      demoPick: "Pick contractor (demo)", demoWorkDone: "Work is done (demo)", demoPay: "Confirm and pay (demo)",
      budgetReady: "Budget ready — ready to order",
      works: "jobs",
      respond: "Accept", responded: "Response sent",
      publishLive: "Your request is live!",
      publishLiveD: "Neighbours can now see it on the map and send help and offers.",
      seedDonate: "Add €25 to the budget", later: "Later",
      becomeContractor: "Become a contractor",
      becomeContractorD: "Help your community with your skills. Get paid for real work.",
      contractorOn: "You are a contractor", myOffers: "My offers",
      offersSent: "Offers sent", tasksDone: "Completed", earned: "Earned",
      pickOnMap: "Tap the map to mark the place",
      how1t: "1 · Community support", how1d: "Someone photographs a broken sidewalk by their house. Neighbours nearby see the problem on the map and add to the project budget with donations.",
      how2t: "2 · Find contractors", how2d: "While donations accumulate, contractors send commercial offers. The budget target is the lowest offer.",
      how3t: "3 · Work", how3d: "Once the budget is ready, the best offer is chosen and the contractor starts. An advance for materials needs a justification and a vote of the donors.",
      how4t: "4 · Verification", how4d: "Neighbours confirm the result — escrow pays the contractor.",
      how5t: "5 · Completed", how5d: "The receipt stays public: every step is visible, the money went to the work.",
      t_donated: "€+AMOUNT to the project budget. This will help attract offers and speed up the work.",
      t_offer_new_min: "Budget target recalculated: €AMOUNT — the lowest offer.",
      t_offer_added: "Offer sent. It is visible to everyone in the project tender.",
      t_accepted: "Offer accepted. The work begins.",
      t_work_done: "Work finished. Waiting for verification.",
      t_paid: "Escrow has paid the contractor. The receipt is public.",
      t_adv_requested: "The advance request was sent to the project’s donors.",
      t_adv_approved: "The donors approved the advance — paid from escrow.",
      t_adv_rejected: "The donors declined the advance.",
      t_adv_vote_y: "Vote counted: for the advance.",
      t_adv_vote_n: "Vote counted: against the advance.",
      t_vote: "Marked: it bothers you too.",
      t_unvote: "Mark removed.",
      t_geo: "Updated: showing projects near you.",
      t_geo_err: "Could not get your location.",
      t_published: "Project published. It is on the map.",
      t_quest: "Response sent (demo).",
      t_contractor: "You can now submit offers for projects in your area.",
      t_reset: "Demo data reset.",
      joinedAgo: "joined", m: "mo ago",
      back: "Back", project: "Project",
      estLabel: "estimate", noOffersYet: "No offers yet — the budget follows the author’s estimate.",
      awaitingOffers: "awaiting offers", chosen: "chosen",
      emptyWallet: "No contributions yet. Find a project nearby and support it.",
      emptyList: "Nothing found."
    }
  };

  var CATS = {
    roads:     { ru: "Дороги",    en: "Roads",     c: "violet" },
    park:      { ru: "Парк",      en: "Park",      c: "teal"   },
    transport: { ru: "Остановки", en: "Stops",     c: "sky"    },
    bikes:     { ru: "Вело",      en: "Bikes",     c: "yellow" },
    clean:     { ru: "Уборка",    en: "Cleaning",  c: "coral"  },
    light:     { ru: "Свет",      en: "Lighting",  c: "pink"   },
    other:     { ru: "Другое",    en: "Other",     c: "mut"    }
  };
  var QCATS = {
    home:      { ru: "Дом и быт", en: "Home & Living", c: "yellow" },
    education: { ru: "Учёба",     en: "Education",     c: "violet" },
    tech:      { ru: "Техника",   en: "Tech",          c: "sky"    },
    pets:      { ru: "Питомцы",   en: "Pets",          c: "coral"  },
    other:     { ru: "Другое",    en: "Other",         c: "mut"    }
  };
  var SKILLS = ["repair", "construction", "carpentry", "painting", "electricity", "cleaning", "garden", "other"];
  var SKILL_LBL = {
    repair: { ru: "Ремонт", en: "Repair" }, construction: { ru: "Стройка", en: "Construction" },
    carpentry: { ru: "Плотницкое", en: "Carpentry" }, painting: { ru: "Покраска", en: "Painting" },
    electricity: { ru: "Электрика", en: "Electricity" }, cleaning: { ru: "Уборка", en: "Cleaning" },
    garden: { ru: "Сад", en: "Garden" }, other: { ru: "Другое", en: "Other" }
  };

  function T(k) {
    var d = I18N[state.lang] || I18N.ru;
    return d[k] != null ? d[k] : (I18N.ru[k] != null ? I18N.ru[k] : k);
  }
  function loc(obj) {
    if (obj == null) return "";
    if (typeof obj === "string") return obj;
    return obj[state.lang] != null ? obj[state.lang] : obj.ru;
  }

  /* ============================================================ seed */
  function seedData() {
    var now = Date.now(), D = 864e5;
    return {
      v: 1, seq: 100,
      lang: (typeof navigator !== "undefined" && /^en/i.test(navigator.language || "")) ? "en" : "ru",
      user: {
        name: "", joined: now - 61 * D, questsDone: 7, contributionsBase: 21,
        contractor: false, skills: [], home: [59.9377, 30.3129]
      },
      myPos: null,
      projects: [
        {
          id: 1, cat: "roads", stage: 1, votes: 12, voted: false, created: now - 5 * D,
          title: { ru: "Ремонт тротуара", en: "Repair the sidewalk" },
          near: { ru: "рядом с домом", en: "near my home" },
          desc: {
            ru: "Плитка треснула и провалилась, после дождя — лужа. Пешеходы обходят по газону, коляски не проехать. Давайте починим вместе.",
            en: "The pavement is broken and dangerous for pedestrians — an accessibility and safety issue. Let’s fix it together."
          },
          coords: [59.9398, 30.3157], estimate: 500, photo: "assets/img/projects/sidewalk.webp",
          donations: [
            { name: "Аня", amount: 35, ts: now - 4 * D },
            { name: "Алекс К.", amount: 30, ts: now - 3 * D },
            { name: "Пётр С.", amount: 30, ts: now - 2 * D },
            { you: true, amount: 25, ts: now - 2 * D }
          ],
          offers: [
            { id: 11, name: "Дорожник Пётр", rating: 4.8, reviews: 19, jobs: 6, price: 450, days: 7,
              msg: { ru: "Могу приехать на замер в четверг. Материалы считаю по факту, фото до и после пришлю в чат.", en: "I can come to measure on Thursday. Materials billed as used, before/after photos in the chat." } },
            { id: 12, name: "Асфальт-СПб", rating: 4.6, reviews: 31, jobs: 14, price: 480, days: 5,
              msg: { ru: "Работаем по тарифу, гарантия год. Начнём на следующей неделе.", en: "Fixed price, one-year warranty. We can start next week." } }
          ],
          chat: [
            { them: "Дорожник Пётр", text: { ru: "Здравствуйте! Видел проблему на карте, готов взяться.", en: "Hi! I saw the problem on the map, happy to take it." }, ts: now - 2 * D },
            { you: true, text: { ru: "Здравствуйте! Когда сможете на замер?", en: "Hi! When can you come to measure?" }, ts: now - 2 * D + 36e5 }
          ],
          contractor: null, advance: null
        },
        {
          id: 2, cat: "bikes", stage: 1, votes: 5, voted: false, created: now - 3 * D,
          title: { ru: "Починить велопарковку", en: "Fix the bike rack" },
          near: { ru: "у подъезда", en: "by the entrance" },
          desc: {
            ru: "Разболтало крепления, два крюка погнуты. Велосипеды падают вместе с парковкой.",
            en: "The fixings are loose and two hooks are bent. Bikes keep falling over with the rack."
          },
          coords: [59.9421, 30.3245], estimate: 200, photo: "assets/img/projects/bikerack.webp",
          donations: [
            { name: "Сергей", amount: 20, ts: now - 2 * D },
            { you: true, amount: 10, ts: now - 1 * D }
          ],
          offers: [
            { id: 21, name: "СварПром", rating: 4.7, reviews: 22, jobs: 9, price: 180, days: 3,
              msg: { ru: "Сварим на месте, усилим основание. Обойдётся дешевле нового.", en: "We will weld it in place and reinforce the base. Cheaper than a new one." } }
          ],
          chat: [], contractor: null, advance: null
        },
        {
          id: 3, cat: "clean", stage: 1, votes: 8, voted: false, created: now - 2 * D,
          title: { ru: "Убрать сквер после зимы", en: "Clean the park" },
          near: { ru: "сквер за школой", en: "the yard behind the school" },
          desc: {
            ru: "Ветви, мусор, песок с дорожек. Хочется сесть на лавочку и не увязнуть в грязи.",
            en: "Branches, litter, sand all over the paths. It would be nice to sit on a bench without stepping into mud."
          },
          coords: [59.9321, 30.3091], estimate: 300, photo: "assets/img/projects/park.webp",
          donations: [
            { name: "Ольга", amount: 35, ts: now - 1 * D },
            { you: true, amount: 10, ts: now - 12 * 36e5 }
          ],
          offers: [],
          chat: [], contractor: null, advance: null
        },
        {
          id: 4, cat: "transport", stage: 3, contractor: 41, votes: 21, voted: false, created: now - 8 * D,
          title: { ru: "Навес на трамвайной остановке", en: "Solar shelter at the tram stop" },
          near: { ru: "остановка у моста", en: "the stop by the bridge" },
          desc: {
            ru: "Стёкол нет, сидений нет, дождь как на улице. Ставим навес со скамейкой и солнечной подсветкой.",
            en: "No glass, no seats, rain gets in. We want a shelter with a bench and a solar light."
          },
          coords: [59.9475, 30.3238], estimate: 600, photo: "assets/img/projects/shelter.webp",
          donations: [
            { name: "Игорь", amount: 40, ts: now - 6 * D },
            { name: "Лена", amount: 30, ts: now - 4 * D },
            { name: "Марк", amount: 10, ts: now - 3 * D }
          ],
          offers: [
            { id: 41, name: "НавесПро", rating: 4.9, reviews: 17, jobs: 5, price: 520, days: 14,
              msg: { ru: "Поликарбонат, антивандальная скамейка, солнечная лента по краю.", en: "Polycarbonate, an anti-vandal bench, solar strip along the edge." } },
            { id: 42, name: "СтройМастер", rating: 4.5, reviews: 26, jobs: 11, price: 560, days: 10,
              msg: { ru: "Сделаем быстрее, но дороже. Гарантия два года.", en: "Faster but pricier. Two-year warranty." } }
          ],
          chat: [
            { them: "НавесПро", text: { ru: "КП принято, начинаем в понедельник. Материалы заказываем заранее.", en: "Offer accepted, we start on Monday. Materials are ordered in advance." }, ts: now - 2 * D },
            { them: "НавесПро", text: { ru: "Поставщику нужна предоплата 50% за поликарбонат — отправил запрос аванса с обоснованием.", en: "The supplier needs a 50% prepayment for the polycarbonate — I have sent an advance request with a justification." }, ts: now - 1 * D }
          ],
          advance: {
            amount: 60, by: "НавесПро", status: "open", ts: now - 1 * D,
            reason: {
              ru: "Закупка поликарбоната и крепежа: поставщик работает по предоплате 50%. Смету приложил в чат, остаток — после приёмки.",
              en: "Polycarbonate and fixings: the supplier requires a 50% prepayment. The itemised quote is in the chat; the rest is paid after acceptance."
            },
            votes: [
              { name: "Игорь", amount: 40, yes: true, ts: now - 20 * 36e5 },
              { name: "Лена", amount: 30, yes: false, ts: now - 18 * 36e5 }
            ]
          }
        },
        {
          id: 5, cat: "park", stage: 1, votes: 9, voted: false, created: now - 6 * D,
          title: { ru: "Посадить деревья в сквере", en: "Plant trees in the park" },
          near: { ru: "вдоль дорожки", en: "along the path" },
          desc: {
            ru: "Три липы и живая изгородь вместо вытоптанной земли. Полив — первые два сезона.",
            en: "Three lindens and a hedge instead of the trampled ground. Watering for the first two seasons."
          },
          coords: [59.9301, 30.3241], estimate: 400, photo: "assets/img/projects/trees.webp",
          donations: [{ name: "Даша", amount: 60, ts: now - 3 * D }],
          offers: [
            { id: 51, name: "ЗелёГрад", rating: 4.8, reviews: 12, jobs: 4, price: 350, days: 7,
              msg: { ru: "Саженцы с комом, приживаемость 90%. Приедем с поливом дважды.", en: "Root-balled saplings, 90% survival. We will come to water twice." } }
          ],
          chat: [], contractor: null, advance: null
        }
      ],
      quests: [
        { id: 61, cat: "home", price: 15, hours: 2, coords: [59.935, 30.31], created: now - 1 * D, accepted: false,
          title: { ru: "Помочь перевезти мебель", en: "Help me move furniture" } },
        { id: 62, cat: "education", price: 20, hours: 1.5, coords: [59.933, 30.319], created: now - 2 * D, accepted: false,
          title: { ru: "Репетиторство: математика, 9 класс", en: "Tutoring: math (grade 9)" } },
        { id: 63, cat: "tech", price: 25, hours: 1, coords: [59.947, 30.308], created: now - 12 * 36e5, accepted: false,
          title: { ru: "Починить ноутбук", en: "Fix my laptop" } },
        { id: 64, cat: "pets", price: 12, hours: 1, coords: [59.928, 30.32], created: now - 5 * 36e5, accepted: false,
          title: { ru: "Выгулять собаку", en: "Walk my dog" } }
      ]
    };
  }

  /* ============================================================ state */
  var LS = "21city.v1";
  var state;
  function load() {
    try {
      var raw = localStorage.getItem(LS);
      if (!raw) return null;
      var d = JSON.parse(raw);
      if (!d || d.v !== 1 || !Array.isArray(d.projects) || !Array.isArray(d.quests) || !d.user || !Array.isArray(d.user.home) || !Array.isArray(d.user.skills) || !Number.isFinite(d.seq)) return null;
      if (!d.projects.every(function (p) { return p && Number.isFinite(p.id) && p.title && Array.isArray(p.donations) && Array.isArray(p.offers) && Array.isArray(p.chat) && Array.isArray(p.coords); })) return null;
      if (d.lang !== "ru" && d.lang !== "en") d.lang = "ru";
      return d;
    } catch (e) { return null; }
  }
  function save() {
    try { localStorage.setItem(LS, JSON.stringify(state)); } catch (e) {
      toast(state.lang === "en" ? "Unable to save. Export your data from Profile." : "Не удалось сохранить данные. Сделайте экспорт в профиле.");
    }
  }

  /* ============================================================ helpers */
  function $(s, ctx) { return (ctx || document).querySelector(s); }
  function $$(s, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(s)); }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function eur(n) { return "€" + String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, "\u202F"); }
  function distKm(a, b) {
    if (!a || !b) return null;
    var R = 6371, dLat = (b[0] - a[0]) * Math.PI / 180, dLon = (b[1] - a[1]) * Math.PI / 180;
    var s = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(a[0] * Math.PI / 180) * Math.cos(b[0] * Math.PI / 180) *
      Math.sin(dLon / 2) * Math.sin(dLon / 2);
    return 2 * R * Math.asin(Math.sqrt(s));
  }
  function kmTxt(km) {
    if (km == null) return "";
    if (km < 1) return Math.max(50, Math.round(km * 1000 / 10) * 10) + " м";
    return (km < 10 ? Math.round(km * 10) / 10 : Math.round(km)) + " км";
  }
  function coordsTxt(c) {
    return c ? c[0].toFixed(4) + ", " + c[1].toFixed(4) : "—";
  }
  function relTime(ts) {
    var d = Date.now() - ts, h = d / 36e5;
    if (state.lang === "en") {
      if (h < 1) return "just now";
      if (h < 24) return Math.round(h) + " h ago";
      return Math.round(h / 24) + " d ago";
    }
    if (h < 1) return "только что";
    if (h < 24) return Math.round(h) + " ч назад";
    return Math.round(h / 24) + " дн назад";
  }
  function targetOf(p) {
    if (p.offers && p.offers.length) {
      return Math.min.apply(null, p.offers.map(function (o) { return o.price; }));
    }
    return p.estimate || 0;
  }
  function collectedOf(p) {
    return (p.donations || []).reduce(function (s, d) { return s + (d.amount || 0); }, 0);
  }
  function myDonated(p) {
    return (p.donations || []).filter(function (d) { return d.you; })
      .reduce(function (s, d) { return s + d.amount; }, 0);
  }
  function minOfferOf(p) {
    if (!p.offers || !p.offers.length) return null;
    return p.offers.reduce(function (m, o) { return o.price < m.price ? o : m; }, p.offers[0]);
  }
  function catOf(p) { return CATS[p.cat] || CATS.other; }
  function pos() { return state.myPos || state.user.home; }

  /* аванс: голосуют донатеры проекта, вес голоса — сумма взноса */
  function advSums(p) {
    var v = (p.advance && p.advance.votes) || [];
    var yes = 0, no = 0;
    v.forEach(function (x) { if (x.yes) yes += x.amount; else no += x.amount; });
    return { yes: yes, no: no, voted: yes + no };
  }
  function advStatus(p) {
    var a = p.advance;
    if (!a) return null;
    if (a.status === "approved" || a.status === "rejected") return a.status;
    var s = advSums(p), coll = collectedOf(p);
    if (coll > 0 && s.yes > coll / 2) { a.status = "approved"; return "approved"; }
    if (coll > 0 && s.no > coll / 2) { a.status = "rejected"; return "rejected"; }
    return "open";
  }

  var toastTimer = null;
  function toast(msg) {
    var el = $("#toast");
    el.textContent = msg;
    el.classList.add("is-on");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.classList.remove("is-on"); }, 2800);
  }

  /* ============================================================ cards */
  function stageChip(p) {
    var k, cls;
    if (p.stage >= 5) { k = "stage5"; cls = "teal"; }
    else if (p.stage === 4) { k = "stage4"; cls = "pink"; }
    else if (p.stage === 3) { k = "stage3"; cls = "sky"; }
    else {
      var coll = collectedOf(p), tgt = targetOf(p);
      if (tgt && coll >= tgt) { return '<span class="chip chip--soft chip--teal">' + T("budgetReady") + "</span>"; }
      k = "open";
      cls = p.offers && p.offers.length ? "violet" : "yellow";
    }
    var label = k === "open"
      ? (p.offers && p.offers.length
          ? T("open") + " · " + p.offers.length + " " + T("offersShort")
          : T("open") + " · " + T("awaitingOffers"))
      : T(k);
    return '<span class="chip chip--soft chip--' + cls + '">' + esc(label) + "</span>";
  }

  function projectCard(p, compact) {
    var coll = collectedOf(p), tgt = targetOf(p);
    var pct = tgt ? Math.min(100, Math.round(coll / tgt * 100)) : 0;
    var d = distKm(pos(), p.coords);
    var cat = catOf(p);
    var minO = minOfferOf(p);
    var photo = p.photo
      ? '<img class="pcard__img" src="' + esc(p.photo) + '" alt="" loading="lazy">'
      : '<div class="pcard__img pcard__img--empty"><span>21</span></div>';
    var meta = [];
    if (d != null) meta.push(kmTxt(d));
    meta.push(coordsTxt(p.coords));
    if (p.offers && p.offers.length) meta.push(p.offers.length + " " + T("offersShort"));
    else meta.push(T("estLabel") + " " + eur(p.estimate || 0));

    if (compact) {
      return '' +
        '<article class="pcard pcard--compact" data-project="' + p.id + '">' +
          '<div class="pcard__top">' +
            '<div><h3 class="pcard__t">' + esc(loc(p.title)) + '</h3>' +
            '<p class="pcard__meta num">' + meta.join(" · ") + '</p></div>' +
            stageChip(p) +
          '</div>' +
          '<div class="bar"><i style="width:' + pct + '%"></i></div>' +
          '<div class="pcard__nums"><b class="num">' + eur(coll) + "</b> " + T("of") +
            ' <span class="num">' + eur(tgt) + '</span>' +
            (minO ? ' <span class="mut">· ' + T("targetMin") + "</span>" : "") +
            '<button class="btn btn--sm btn--violet" type="button" data-donate="' + p.id + '">' + T("addBudgetShort") + "</button>" +
          "</div>" +
        "</article>";
    }

    return '' +
      '<article class="pcard" data-project="' + p.id + '">' +
        photo +
        '<div class="pcard__body">' +
          '<div class="pcard__chips">' +
            '<span class="chip chip--soft chip--' + cat.c + '">' + esc(loc(cat)) + "</span>" +
            stageChip(p) +
          "</div>" +
          '<h3 class="pcard__t">' + esc(loc(p.title)) + "</h3>" +
          '<p class="pcard__near">' + esc(loc(p.near)) + (d != null ? " · " + kmTxt(d) : "") + "</p>" +
          '<p class="pcard__desc">' + esc(loc(p.desc)) + "</p>" +
          '<p class="pcard__meta num">' + coordsTxt(p.coords) +
            ' <button class="linklike linklike--mono" type="button" data-showmap="' + p.id + '">' + T("viewOnMap") + " →</button></p>" +
          '<div class="pcard__budget">' +
            '<div class="pcard__nums"><b class="num">' + eur(coll) + "</b> " + T("of") +
              ' <span class="num">' + eur(tgt) + '</span> <span class="num pcard__pct">' + pct + "%</span></div>" +
            '<div class="bar' + (pct >= 100 ? " bar--full" : "") + '"><i style="width:' + pct + '%"></i></div>' +
            '<p class="pcard__tgt">' +
              (minO
                ? T("targetMin") + ": " + esc(minO.name) + " · " + eur(minO.price) + " · " + minO.days + " " + (state.lang === "en" ? "days" : "дн")
                : T("targetEst")) +
            "</p>" +
          "</div>" +
          '<div class="pcard__btns">' +
            '<button class="btn btn--sm" type="button" data-donate="' + p.id + '">' + T("addBudgetShort") + "</button>" +
            '<button class="btn btn--sm" type="button" data-offer="' + p.id + '">' + T("offersShort") + " (" + (p.offers ? p.offers.length : 0) + ")</button>" +
            '<button class="btn btn--sm btn--ghost" type="button" data-project="' + p.id + '">' + T("details") + "</button>" +
          "</div>" +
        "</div>" +
      "</article>";
  }

  function questCard(q, row) {
    var cat = QCATS[q.cat] || QCATS.other;
    var d = distKm(pos(), q.coords);
    if (row) {
      return '' +
        '<article class="qrow" data-quest="' + q.id + '">' +
          '<div class="qrow__main"><h3>' + esc(loc(q.title)) + "</h3>" +
          '<p class="num">' + eur(q.price) + " · " + q.hours + " " + (state.lang === "en" ? "h" : "ч") +
            (d != null ? " · " + kmTxt(d) : "") + " · " + relTime(q.created) + "</p></div>" +
          '<div class="qrow__side"><span class="chip chip--soft chip--' + cat.c + '">' + esc(loc(cat)) + "</span>" +
          (q.accepted
            ? '<span class="chip chip--soft chip--teal">' + T("responded") + "</span>"
            : '<button class="btn btn--sm btn--violet" type="button" data-accept-quest="' + q.id + '">' + T("respond") + "</button>") +
          "</div></article>";
    }
    return '' +
      '<article class="qcard" data-quest="' + q.id + '">' +
        '<span class="chip chip--soft chip--' + cat.c + '">' + esc(loc(cat)) + "</span>" +
        "<h3>" + esc(loc(q.title)) + "</h3>" +
        '<p class="num">' + eur(q.price) + " · " + q.hours + " " + (state.lang === "en" ? "h" : "ч") +
        (d != null ? " · " + kmTxt(d) : "") + "</p>" +
        (q.accepted
          ? '<span class="chip chip--soft chip--teal">' + T("responded") + "</span>"
          : '<button class="btn btn--sm btn--violet" type="button" data-accept-quest="' + q.id + '">' + T("respond") + "</button>") +
      "</article>";
  }

  /* ============================================================ views */
  var qsort = "forYou", plist = "all", wtab = "active", searchQ = "", catalogQ = "", catalogOrder = "near";

  function sortedProjects(list) {
    var arr = (list || state.projects).slice();
    var p = pos();
    arr.sort(function (a, b) {
      var da = distKm(p, a.coords), db = distKm(p, b.coords);
      if (da != null && db != null && Math.abs(da - db) > 0.05) return da - db;
      return b.created - a.created;
    });
    return arr;
  }
  function sortedQuests() {
    var arr = state.quests.slice();
    if (qsort === "popular") arr.sort(function (a, b) { return b.created - a.created; });
    else {
      var p = pos();
      arr.sort(function (a, b) {
        var da = distKm(p, a.coords), db = distKm(p, b.coords);
        if (da != null && db != null) return da - db;
        return b.created - a.created;
      });
    }
    return arr;
  }

  function renderHome() {
    var total = state.projects.reduce(function (sum, p) { return sum + collectedOf(p); }, 0);
    $("#communityStats").innerHTML = '<div><b>' + state.projects.length + '</b><span>' + T("projects") + '</span></div><div><b>' + eur(total) + '</b><span>' + (state.lang === "en" ? "in project budgets" : "в бюджетах проектов") + '</span></div>';
    $("#homeQuests").innerHTML = sortedQuests().map(function (q) { return questCard(q, false); }).join("");
    $("#homeProjects").innerHTML = sortedProjects().slice(0, 3)
      .map(function (p) { return projectCard(p, false); }).join("");
  }

  function renderMapList() {
    var q = searchQ.trim().toLowerCase();
    var arr = sortedProjects().filter(function (p) {
      if (!q) return true;
      return (loc(p.title) + " " + loc(p.desc) + " " + loc(p.near) + " " + loc(catOf(p))).toLowerCase().indexOf(q) >= 0;
    });
    $("#mapCount").textContent = arr.length ? arr.length + (state.lang === "en" ? " on the map" : " на карте") : "";
    $("#mapList").innerHTML = arr.length
      ? arr.map(function (p) { return projectCard(p, true); }).join("")
      : '<p class="empty">' + T("emptyList") + "</p>";
    refreshMarkers(arr);
  }

  function renderProjects() {
    var query = catalogQ.trim().toLowerCase();
    function matches(p) { return !query || (loc(p.title) + " " + loc(p.desc) + " " + loc(p.near)).toLowerCase().includes(query); }
    var projects = sortedProjects().filter(matches);
    if (catalogOrder === "new") projects.sort(function (a,b) { return b.created - a.created; });
    if (catalogOrder === "funding") projects.sort(function (a,b) { return collectedOf(b) / (targetOf(b) || 1) - collectedOf(a) / (targetOf(a) || 1); });
    var quests = sortedQuests().filter(matches);
    if (catalogOrder === "new") quests.sort(function (a,b) { return b.created - a.created; });
    var out = "";
    if (plist === "all" || plist === "projects") {
      out += projects.map(function (p) { return projectCard(p, false); }).join("");
    }
    if (plist === "all" || plist === "quests") {
      out += quests.map(function (q) { return questCard(q, true); }).join("");
    }
    $("#projList").innerHTML = out || '<p class="empty">' + T("emptyList") + "</p>";
  }

  function myProjectsList() {
    return state.projects.filter(function (p) { return myDonated(p) > 0; });
  }

  function renderWallet() {
    var mine = myProjectsList();
    var total = mine.reduce(function (s, p) { return s + myDonated(p); }, 0);
    $("#walletBalance").textContent = eur(total);
    if (wtab === "contributed") {
      var rows = [];
      state.projects.forEach(function (p) {
        (p.donations || []).forEach(function (d) {
          if (d.you) rows.push({ p: p, d: d });
        });
      });
      rows.sort(function (a, b) { return b.d.ts - a.d.ts; });
      $("#walletList").innerHTML = rows.length ? rows.map(function (r) {
        return '<article class="wrow" data-project="' + r.p.id + '">' +
          '<div><h3>' + esc(loc(r.p.title)) + '</h3><p class="num">' + relTime(r.d.ts) + "</p></div>" +
          '<b class="num">+' + eur(r.d.amount) + "</b></article>";
      }).join("") : '<p class="empty">' + T("emptyWallet") + "</p>";
      return;
    }
    var flt = wtab === "done"
      ? mine.filter(function (p) { return p.stage >= 5; })
      : mine.filter(function (p) { return p.stage < 5; });
    var out = flt.map(function (p) { return projectCard(p, false); }).join("");
    var box = $("#walletList");
    box.innerHTML = out || '<p class="empty">' + T("emptyWallet") + "</p>";
    $$(".pcard", box).forEach(function (el) {
      var p = byId(el.getAttribute("data-project"));
      if (!p) return;
      var y = myDonated(p);
      if (y) {
        var tag = document.createElement("p");
        tag.className = "pcard__youdon num";
        tag.textContent = (state.lang === "en" ? "You donated " : "Вы внесли ") + eur(y);
        el.appendChild(tag);
      }
    });
  }

  function renderProfile() {
    var u = state.user;
    $("#profileName").textContent = u.name || T("you");
    if (document.activeElement !== $("#profileNameInput")) $("#profileNameInput").value = u.name;
    var mine = myProjectsList();
    var contribs = state.projects.reduce(function (s, p) {
      return s + (p.donations || []).filter(function (d) { return d.you; }).length;
    }, 0);
    var months = Math.max(1, Math.round((Date.now() - u.joined) / (30 * 864e5)));
    $("#meJoined").textContent = T("joinedAgo") + " " + months + " " + T("m");
    $("#profileStats").innerHTML =
      '<div class="stat3"><b class="num">' + (u.questsDone + state.quests.filter(function (q) { return q.accepted; }).length) + "</b><span>" + (state.lang === "en" ? "quests" : "квестов") + "</span></div>" +
      '<div class="stat3"><b class="num">' + mine.length + "</b><span>" + (state.lang === "en" ? "projects" : "проекта") + "</span></div>" +
      '<div class="stat3"><b class="num">' + (u.contributionsBase + contribs) + "</b><span>" + (state.lang === "en" ? "contributions" : "взносов") + "</span></div>";
    $("#meProjectsN").textContent = mine.length;
    $("#meQuestsN").textContent = u.questsDone;
    var total = mine.reduce(function (s, p) { return s + myDonated(p); }, 0);
    $("#meWallet").textContent = eur(total);

    var box = $("#contractorBox");
    if (!box) return;
    if (!u.contractor) {
      box.innerHTML =
        '<h2>' + T("becomeContractor") + "</h2>" +
        '<p class="mut">' + T("becomeContractorD") + "</p>" +
        '<div class="chips chips--wrap">' + SKILLS.map(function (s) {
          var on = u.skills.indexOf(s) >= 0;
          return '<button class="chip chip--btn' + (on ? " is-on" : "") + '" type="button" data-skill="' + s + '">' + esc(loc(SKILL_LBL[s])) + "</button>";
        }).join("") + "</div>" +
        '<button class="btn btn--primary" type="button" id="btnContractor">' + T("becomeContractor") + "</button>";
    } else {
      var myOffers = [];
      state.projects.forEach(function (p) {
        (p.offers || []).forEach(function (o) { if (o.you) myOffers.push({ p: p, o: o }); });
      });
      var done = myOffers.filter(function (r) { return r.p.stage >= 5 && r.p.contractor === r.o.id; });
      var earned = done.reduce(function (s, r) { return s + r.o.price; }, 0);
      box.innerHTML =
        '<div class="cbx__head"><h2>' + T("contractorOn") + "</h2>" +
        '<p class="num">★ 4.8</p></div>' +
        '<div class="stats3">' +
          '<div class="stat3"><b class="num">' + myOffers.length + "</b><span>" + T("offersSent").toLowerCase() + "</span></div>" +
          '<div class="stat3"><b class="num">' + done.length + "</b><span>" + T("tasksDone").toLowerCase() + "</span></div>" +
          '<div class="stat3"><b class="num">' + eur(earned) + "</b><span>" + T("earned").toLowerCase() + "</span></div>" +
        "</div>" +
        '<h3 class="cbx__sub">' + T("myOffers") + "</h3>" +
        (myOffers.length
          ? myOffers.map(function (r) {
              var st = r.p.contractor === r.o.id ? (r.p.stage >= 5 ? T("stage5") : T("stage3")) : T("active");
              return '<div class="wrow" data-project="' + r.p.id + '"><div><h3>' + esc(loc(r.p.title)) + "</h3>" +
                '<p><span class="chip chip--soft">' + esc(st) + "</span></p></div>" +
                '<b class="num">' + eur(r.o.price) + "</b></div>";
            }).join("")
          : '<p class="mut">' + T("noOffersYet") + "</p>") +
        '<div class="chips chips--wrap">' + SKILLS.map(function (s) {
          var on = u.skills.indexOf(s) >= 0;
          return '<button class="chip chip--btn' + (on ? " is-on" : "") + '" type="button" data-skill="' + s + '">' + esc(loc(SKILL_LBL[s])) + "</button>";
        }).join("") + "</div>";
    }
  }

  /* ============================================================ detail */
  var detailId = null;

  function byId(id) {
    id = Number(id);
    for (var i = 0; i < state.projects.length; i++) if (state.projects[i].id === id) return state.projects[i];
    return null;
  }

  function timelineHtml(p) {
    var steps = [
      { t: T("stage1"), d: T("stage1d") },
      { t: T("stage2"), d: T("stage2d") },
      { t: T("stage3"), d: T("stage3d") },
      { t: T("stage4"), d: T("stage4d") },
      { t: T("stage5"), d: T("stage5d") }
    ];
    var cur = p.stage;
    var li = steps.map(function (s, i) {
      var n = i + 1, cls = "";
      if (n < cur) cls = "is-done";
      else if (n === cur) cls = "is-now";
      if (cur === 1 && n === 2) cls = "is-now";
      var badge = n < cur ? "✓" : n;
      var now = (cls === "is-now") ? ' <span class="tl__now">' + T("now") + "</span>" : "";
      return '<li class="' + cls + '"><span class="tl__n num">' + badge + "</span>" +
        "<div><b>" + esc(s.t) + now + "</b><span>" + esc(s.d) + "</span></div></li>";
    }).join("");
    var demo = "";
    var coll = collectedOf(p), tgt = targetOf(p), minO = minOfferOf(p);
    if (p.stage === 1 && minO && coll >= tgt) {
      demo = '<button class="btn btn--sm btn--violet" type="button" data-advance="' + p.id + '" data-to="3">' + T("demoPick") + ": " + esc(minO.name) + "</button>";
    } else if (p.stage === 3) {
      demo = '<button class="btn btn--sm" type="button" data-advance="' + p.id + '" data-to="4">' + T("demoWorkDone") + "</button>";
    } else if (p.stage === 4) {
      demo = '<button class="btn btn--sm btn--violet" type="button" data-advance="' + p.id + '" data-to="5">' + T("demoPay") + "</button>";
    }
    return '<div class="card card--tl"><h2 class="card__h">' + T("timelineTitle") + "</h2>" +
      '<ol class="tl">' + li + "</ol>" +
      (demo ? '<div class="tl__demo">' + demo + "</div>" : "") +
      '<p class="chain-note">' + T("chainNote") + "</p></div>";
  }

  /* -------- аванс: запрос с обоснованием + голосование донатеров */
  function advanceHtml(p) {
    if (p.stage < 3) return "";
    var a = p.advance;
    if (!a) {
      return '<div class="card card--adv">' +
        '<h2 class="card__h">' + T("advanceTitle") + "</h2>" +
        '<p class="mut adv__note">' + T("advDemoNote") + "</p>" +
        '<button class="btn btn--wide" type="button" data-advreq="' + p.id + '">' + T("requestAdvance") + "</button>" +
        "</div>";
    }
    var st = advStatus(p);
    var s = advSums(p), coll = collectedOf(p);
    var mine = myDonated(p);
    var myVote = null;
    a.votes.forEach(function (v) { if (v.you) myVote = v; });

    var voteRows = a.votes.map(function (v) {
      return '<span class="adv__voter' + (v.yes ? " adv__voter--yes" : " adv__voter--no") + '">' +
        (v.you ? "<b>" + T("you") + "</b>" : esc(v.name)) + " " + eur(v.amount) + " · " + (v.yes ? T("advFor") : T("advAgainst")) + "</span>";
    }).join("");

    var head = '<div class="adv__head"><b>' + esc(a.by || T("you")) + "</b> " + T("advBy") +
      ' <b class="num">' + eur(a.amount) + "</b></div>";
    var reason = '<p class="adv__reason">' + esc(loc(a.reason)) + "</p>";

    if (st === "approved") {
      return '<div class="card card--adv card--adv-ok">' +
        '<h2 class="card__h">' + T("advanceTitle") + "</h2>" + head + reason +
        '<p class="adv__status adv__status--ok"><span class="chip chip--soft chip--teal">✓ ' + T("advApproved") + "</span>" +
        ' <span class="num">' + eur(a.amount) + "</span> " + T("advPaidNote") + " · " + T("advRestNote") + " <span class=\"num\">" + eur(Math.max(0, coll - a.amount)) + "</span></p>" +
        (voteRows ? '<div class="adv__votes">' + voteRows + "</div>" : "") +
        "</div>";
    }
    if (st === "rejected") {
      return '<div class="card card--adv card--adv-no">' +
        '<h2 class="card__h">' + T("advanceTitle") + "</h2>" + head + reason +
        '<p class="adv__status"><span class="chip chip--soft chip--coral">' + T("advRejected") + "</span></p>" +
        (voteRows ? '<div class="adv__votes">' + voteRows + "</div>" : "") +
        '<button class="btn btn--wide" type="button" data-advreq="' + p.id + '">' + T("advReRequest") + "</button>" +
        "</div>";
    }
    var voteUi;
    if (mine > 0) {
      voteUi = '<div class="adv__btns">' +
        '<button class="btn btn--sm btn--violet" type="button" data-advvote="' + p.id + '" data-yes="1">' + T("giveAdvance") + "</button>" +
        '<button class="btn btn--sm" type="button" data-advvote="' + p.id + '" data-yes="0">' + T("declineAdvance") + "</button>" +
        (myVote ? '<span class="adv__mine">' + T("yourVote") + ": " + (myVote.yes ? T("advFor") : T("advAgainst")) + "</span>" : "") +
        "</div>";
    } else {
      voteUi = '<p class="adv__onlydonors"><b>' + T("advVotersOnly") + ".</b> " + T("advToVote") + "</p>" +
        '<button class="btn btn--sm btn--violet" type="button" data-donate="' + p.id + '">' + T("addBudgetShort") + "</button>";
    }
    return '<div class="card card--adv">' +
      '<h2 class="card__h">' + T("advanceTitle") + "</h2>" + head + reason +
      '<div class="adv__meter"><span class="adv__yes" style="width:' + (coll ? Math.min(100, Math.round(s.yes / coll * 100)) : 0) + '%"></span></div>' +
      '<p class="adv__open num">' + T("advOpenA") + " " + eur(s.voted) + " " + T("advOpenB") + " " + eur(coll) + " — " + T("advRule") + "</p>" +
      (voteRows ? '<div class="adv__votes">' + voteRows + "</div>" : "") +
      voteUi +
      "</div>";
  }

  function renderDetail(preserveScroll) {
    var p = byId(detailId);
    var box = $("#detailIn");
    if (!p) { closeDetail(); return; }
    var keepScroll = preserveScroll ? box.scrollTop : 0;
    var coll = collectedOf(p), tgt = targetOf(p);
    var pct = tgt ? Math.min(100, Math.round(coll / tgt * 100)) : 0;
    var minO = minOfferOf(p);
    var d = distKm(pos(), p.coords);
    var cat = catOf(p);

    var donors = (p.donations || []).slice().sort(function (a, b) { return b.amount - a.amount; });
    var donorRows = donors.slice(0, 4).map(function (dn) {
      return "<span>" + (dn.you ? "<b>" + T("you") + "</b>" : esc(dn.name || "—")) + " " + eur(dn.amount) + "</span>";
    }).join("");
    if (donors.length > 4) donorRows += '<span class="mut">+' + (donors.length - 4) + "…</span>";

    var offersHtml = (p.offers || []).length
      ? p.offers.slice().sort(function (a, b) { return a.price - b.price; }).map(function (o) {
          var isMin = minO && o.id === minO.id;
          var short = tgt - coll;
          return '<div class="offer' + (isMin ? " offer--min" : "") + '">' +
            '<div class="offer__head"><b>' + esc(o.name) + '</b>' +
            '<span class="num offer__rate">★ ' + o.rating + " (" + o.reviews + ") · " + o.jobs + " " + T("works") + "</span></div>" +
            '<p class="offer__msg">' + esc(loc(o.msg) || "") + "</p>" +
            '<div class="offer__row"><span class="num offer__price">' + eur(o.price) + " · " + o.days + " " + (state.lang === "en" ? "days" : "дн") + "</span>" +
            (isMin ? '<span class="chip chip--soft chip--yellow">' + T("minPrice") + "</span>" : "") +
            '<span class="offer__acts">' +
              (p.contractor === o.id
                ? '<span class="chip chip--soft chip--teal">' + T("chosen") + "</span>"
                : (p.stage < 3
                    ? '<button class="btn btn--sm btn--violet" type="button" data-accept="' + p.id + '" data-offer-id="' + o.id + '">' + T("accept") + "</button>"
                    : "")) +
            "</span></div>" +
            (isMin && short > 0 && p.stage < 3
              ? '<p class="offer__short num">' + T("shortfall") + " " + eur(short) + " " + T("canTopUp") + "</p>"
              : "") +
          "</div>";
        }).join("")
      : '<p class="mut">' + T("noOffersYet") + "</p>";

    var chat = (p.chat || []).map(function (m) {
      return '<div class="msg' + (m.you ? " msg--you" : "") + '">' +
        (m.you ? "" : '<span class="msg__who">' + esc(m.them || "") + "</span>") +
        "<p>" + esc(typeof m.text === "string" ? m.text : loc(m.text)) + "</p>" +
        '<span class="msg__t num">' + relTime(m.ts) + "</span></div>";
    }).join("");

    var photo = p.photo
      ? '<img class="det__img" src="' + esc(p.photo) + '" alt="">'
      : "";

    box.innerHTML =
      '<header class="det__head">' +
        '<button class="det__back" type="button" id="detBack">← <span>' + T("back") + "</span></button>" +
        '<span class="chip chip--soft">' + T("project") + "</span>" +
      "</header>" +
      photo +
      '<div class="det__body">' +
        '<h2 class="det__t">' + esc(loc(p.title)) + "</h2>" +
        '<p class="det__near">' + esc(loc(p.near)) + (d != null ? " · " + kmTxt(d) : "") + "</p>" +
        '<div class="det__chips">' +
          '<span class="chip chip--soft chip--' + cat.c + '">' + esc(loc(cat)) + "</span>" +
          stageChip(p) +
          '<button class="chip chip--btn' + (p.voted ? " is-on" : "") + '" type="button" data-vote="' + p.id + '">' +
            (state.lang === "en" ? "bothers me too" : "мне тоже мешает") + " +" + p.votes + "</button>" +
        "</div>" +
        '<p class="det__coords num">' + coordsTxt(p.coords) +
          ' <button class="linklike linklike--mono" type="button" data-showmap="' + p.id + '">' + T("viewOnMap") + " →</button></p>" +
        '<p class="det__desc">' + esc(loc(p.desc)) + "</p>" +

        '<div class="card card--budget">' +
          '<h2 class="card__h">' + T("budgetTitle") + "</h2>" +
          '<p class="budget__big"><b class="num">' + eur(coll) + "</b> " + T("of") +
            ' <span class="num">' + eur(tgt) + '</span> <span class="budget__pct num">' + pct + "%</span></p>" +
          '<div class="bar' + (pct >= 100 ? " bar--full" : "") + '"><i style="width:' + pct + '%"></i></div>' +
          '<p class="budget__tgt">' + (minO
            ? T("targetMin") + ": <b>" + esc(minO.name) + "</b> · " + eur(minO.price) + " · " + minO.days + " " + (state.lang === "en" ? "days" : "дн")
            : T("targetEst")) + "</p>" +
          (donorRows ? '<p class="budget__donors"><b>' + T("donors") + ":</b> " + donorRows + "</p>" : "") +
          (p.advance && p.advance.status === "approved"
            ? '<p class="budget__adv num">' + T("advanceTitle") + ": " + eur(p.advance.amount) + " → " + T("advPaidNote") + "</p>"
            : "") +
          '<button class="btn btn--primary btn--wide" type="button" data-donate="' + p.id + '">' + T("addToBudget") + "</button>" +
          '<p class="budget__micro">' +
            (state.lang === "en"
              ? "Your donation goes to the work, not to platform fees."
              : "Донат идёт в бюджет проекта и тратится на работу, а не на комиссии платформы.") + "</p>" +
        "</div>" +

        advanceHtml(p) +

        '<div class="card">' +
          '<h2 class="card__h">' + T("offersTitle") + " (" + (p.offers || []).length + ")</h2>" +
          offersHtml +
          (p.stage < 3 ? '<button class="btn btn--wide" type="button" data-newoffer="' + p.id + '">' + T("submitOffer") + "</button>" : "") +
        "</div>" +

        timelineHtml(p) +

        '<div class="card">' +
          '<h2 class="card__h">' + T("chatTitle") + "</h2>" +
          '<div class="chat">' + (chat || '<p class="mut">—</p>') + "</div>" +
          '<div class="chat__in">' +
            '<input type="text" id="chatText" maxlength="200" placeholder="' + esc(T("chatPlaceholder")) + '">' +
            '<button class="btn btn--sm btn--violet" type="button" id="chatSend">' +
              '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 12 21 3.5 15.5 21l-4-6.5L3.5 12Z"/></svg>' +
            "</button></div>" +
        "</div>" +
      "</div>";

    $("#detail").hidden = false;
    requestAnimationFrame(function () {
      $("#detail").classList.add("is-on");
      $("#detailIn").scrollTop = keepScroll;
    });
  }

  function openProject(id) {
    detailId = Number(id);
    renderDetail();
    if (!routing) history.pushState(null, "", "#/project/" + detailId);
    $("#detail").focus();
  }
  function closeDetail() {
    var el = $("#detail");
    el.classList.remove("is-on");
    detailId = null;
    if (!routing) history.pushState(null, "", "#/" + ($(".view.is-on").id.replace("view-", "")));
    setTimeout(function () { if (detailId == null) el.hidden = true; }, 240);
  }

  /* ============================================================ map */
  var map = null, markers = {}, meMarker = null, pickMode = false, draftCoords = null;

  function initMap() {
    if (map || typeof L === "undefined") return;
    var el = $("#map");
    if (!el) return;
    map = L.map(el, { zoomControl: false, attributionControl: true, scrollWheelZoom: false });
    map.setView(pos(), 15);
    L.tileLayer("https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>'
    }).addTo(map);
    L.control.zoom({ position: "bottomright" }).addTo(map);
    meMarkerUpdate();
    map.on("click", function (e) {
      if (!pickMode) return;
      pickMode = false;
      $("#map").classList.remove("is-picking");
      draftCoords = [e.latlng.lat, e.latlng.lng];
      var out = $("#nCoords");
      if (out) out.textContent = coordsTxt(draftCoords);
      toast(T("place") + ": " + coordsTxt(draftCoords));
      openModal("#mNew");
    });
    refreshMarkers();
  }
  function meMarkerUpdate() {
    if (!map) return;
    var p = pos();
    if (meMarker) meMarker.setLatLng(p);
    else {
      meMarker = L.circleMarker(p, { radius: 8, weight: 2.5, color: "#17161b", fillColor: "#6f9bf5", fillOpacity: 1 })
        .addTo(map).bindTooltip(state.lang === "en" ? "You" : "Вы");
    }
  }
  function refreshMarkers(list) {
    if (!map) return;
    var arr = list || state.projects;
    Object.keys(markers).forEach(function (id) {
      if (!arr.some(function (p) { return String(p.id) === id; })) {
        map.removeLayer(markers[id]); delete markers[id];
      }
    });
    arr.forEach(function (p, i) {
      var cat = catOf(p);
      var icon = L.divIcon({
        className: "",
        html: '<span class="pin pin--' + cat.c + '"><b class="num">' + (i + 1) + "</b></span>",
        iconSize: [34, 34], iconAnchor: [17, 17], popupAnchor: [0, -14]
      });
      if (markers[p.id]) {
        markers[p.id].setLatLng(p.coords).setIcon(icon);
        markers[p.id].setPopupContent(popupHtml(p));
      } else {
        markers[p.id] = L.marker(p.coords, { icon: icon })
          .addTo(map)
          .bindPopup(popupHtml(p), { closeButton: false, autoPan: false });
      }
    });
  }
  function popupHtml(p) {
    var coll = collectedOf(p), tgt = targetOf(p);
    return '<div class="pp" data-project="' + p.id + '"><b>' + esc(loc(p.title)) + "</b>" +
      '<span class="pp__meta num">' + eur(coll) + " / " + eur(tgt) + "</span>" +
      '<button class="pp__btn" type="button" data-project="' + p.id + '">' + T("details") + " →</button></div>";
  }

  /* ============================================================ modals */
  function openModal(sel) {
    var m = $(sel);
    m._returnFocus = document.activeElement;
    m.hidden = false;
    requestAnimationFrame(function () { m.classList.add("is-on"); var first = m.querySelector("input, button"); if (first) first.focus(); });
  }
  function closeModal(m) {
    m = m || $(".modal.is-on");
    if (!m) return;
    m.classList.remove("is-on");
    if (m._returnFocus && m._returnFocus.isConnected) m._returnFocus.focus();
    setTimeout(function () {
      if (!m.classList.contains("is-on")) m.hidden = true;
    }, 220);
  }

  var donateFor = null, donateAmt = 25;
  function openDonate(id) {
    var p = byId(id);
    if (!p) return;
    donateFor = p.id; donateAmt = 25;
    $("#dProject").textContent = loc(p.title) + " — " + eur(collectedOf(p)) + " " + T("of") + " " + eur(targetOf(p));
    $$("#dAmounts .amt").forEach(function (b) {
      b.classList.toggle("is-on", b.getAttribute("data-amt") === "25");
    });
    $("#dOtherWrap").hidden = true;
    $("#dOther").value = "";
    $("#dName").value = "";
    openModal("#mDonate");
  }
  function doDonate() {
    var p = byId(donateFor);
    if (!p) return;
    var amt;
    if (donateAmt === "other") {
      amt = Math.round(Number($("#dOther").value) || 0);
      if (amt < 1) return;
    } else {
      amt = Number(donateAmt) || 0;
      if (amt < 1) return;
    }
    var name = $("#dName").value.trim();
    if (!Number.isFinite(amt) || amt > 1000000) { toast(state.lang === "en" ? "Enter an amount from 1 to 1,000,000" : "Введите сумму от 1 до 1 000 000"); return; }
    p.donations.push({ you: true, name: name || state.user.name, amount: amt, ts: Date.now() });
    save();
    closeModal($("#mDonate"));
    toast(T("t_donated").replace("AMOUNT", amt));
    renderAll();
    if (detailId === p.id) renderDetail(true);
  }

  var offerFor = null;
  function openOffer(id) {
    var p = byId(id);
    if (!p) return;
    offerFor = p.id;
    $("#oProject").textContent = loc(p.title);
    $("#oName").value = state.user.contractor ? T("you") : "";
    $("#oPrice").value = "";
    $("#oDays").value = "";
    openModal("#mOffer");
  }
  function doOffer() {
    var p = byId(offerFor);
    if (!p) return;
    var name = $("#oName").value.trim();
    var price = Math.round(Number($("#oPrice").value));
    var days = Math.round(Number($("#oDays").value));
    if (!name) { $("#oName").focus(); return; }
    if (!Number.isFinite(price) || price < 1 || price > 1000000) { $("#oPrice").focus(); return; }
    if (!Number.isFinite(days) || days < 1 || days > 3650) { $("#oDays").focus(); return; }
    var wasMin = targetOf(p);
    p.offers.push({
      id: state.seq++, you: true, name: name, rating: 4.8, reviews: 24,
      jobs: state.user.contractor ? 6 : 0, price: price, days: days,
      msg: { ru: "Готов выполнить работы. Фото до и после пришлю в чат.", en: "Ready to do the work. I will send before and after photos in the chat." }
    });
    save();
    closeModal($("#mOffer"));
    if (price < wasMin) toast(T("t_offer_new_min").replace("AMOUNT", price));
    else toast(T("t_offer_added"));
    renderAll();
    if (detailId === p.id) renderDetail(true);
  }

  /* -------- аванс */
  var advFor = null;
  function openAdvance(id) {
    var p = byId(id);
    if (!p) return;
    advFor = p.id;
    $("#aAmount").value = "";
    $("#aReason").value = "";
    openModal("#mAdvance");
  }
  function doAdvanceRequest() {
    var p = byId(advFor);
    if (!p) return;
    var amount = Math.round(Number($("#aAmount").value) || 0);
    var reason = $("#aReason").value.trim();
    if (amount < 1) { $("#aAmount").focus(); return; }
    if (!reason) { $("#aReason").focus(); return; }
    p.advance = {
      amount: amount, by: T("you"), status: "open", ts: Date.now(),
      reason: reason, votes: []
    };
    save();
    closeModal($("#mAdvance"));
    toast(T("t_adv_requested"));
    renderAll();
    if (detailId === p.id) renderDetail(true);
  }
  function voteAdvance(id, yes) {
    var p = byId(id);
    if (!p || !p.advance) return;
    var mine = myDonated(p);
    if (mine <= 0) { toast(T("advVotersOnly")); return; }
    var existing = null;
    p.advance.votes.forEach(function (v) { if (v.you) existing = v; });
    if (existing) { existing.yes = !!yes; existing.amount = mine; existing.ts = Date.now(); }
    else p.advance.votes.push({ you: true, name: T("you"), amount: mine, yes: !!yes, ts: Date.now() });
    var st = advStatus(p);
    save();
    toast(st === "approved" ? T("t_adv_approved") : st === "rejected" ? T("t_adv_rejected") : (yes ? T("t_adv_vote_y") : T("t_adv_vote_n")));
    renderAll();
    if (detailId === p.id) renderDetail(true);
  }

  /* -------- new project wizard */
  var draftPhoto = null;
  function fillCats() {
    var sel = $("#nCat");
    sel.innerHTML = Object.keys(CATS).map(function (k) {
      return '<option value="' + k + '">' + esc(loc(CATS[k])) + "</option>";
    }).join("");
  }
  function openNew() {
    draftPhoto = null; draftCoords = null;
    $("#nPreview").hidden = true;
    $("#nPhotoBox").classList.remove("has-photo");
    $("#nTitleIn").value = "";
    $("#nDesc").value = "";
    $("#nEstimate").value = "";
    $("#nCoords").textContent = "—";
    openModal("#mNew");
  }
  function doPublish() {
    var title = $("#nTitleIn").value.trim();
    if (!title) { $("#nTitleIn").focus(); return; }
    var coords = draftCoords || pos();
    var est = Math.max(1, Math.round(Number($("#nEstimate").value) || 100));
    var p = {
      id: state.seq++, cat: $("#nCat").value || "other", stage: 1, votes: 0, voted: false,
      created: Date.now(), title: title, near: { ru: "рядом с домом", en: "near my home" },
      desc: $("#nDesc").value.trim() || { ru: "", en: "" },
      coords: coords, estimate: est, photo: draftPhoto || "",
      donations: [], offers: [], chat: [], contractor: null, advance: null
    };
    state.projects.unshift(p);
    save();
    closeModal($("#mNew"));
    toast(T("t_published"));
    /* как в референсе: первый взнос автора ускоряет поиск подрядчиков */
    var sheet = $("#mNew .sheet");
    var prev = sheet.innerHTML;
    sheet.innerHTML =
      '<h2>' + T("publishLive") + "</h2>" +
      '<p class="sheet__note">' + T("publishLiveD") + "</p>" +
      '<div class="seed">' +
        '<button class="btn btn--primary btn--wide" type="button" id="seed25">' + T("seedDonate") + "</button>" +
        '<button class="btn btn--wide" type="button" id="seedLater">' + T("later") + "</button>" +
      "</div>";
    openModal("#mNew");
    $("#seed25").addEventListener("click", function () {
      p.donations.push({ you: true, amount: 25, ts: Date.now() });
      save(); closeModal($("#mNew")); sheet.innerHTML = prev; wireNewForm();
      renderAll(); openProject(p.id);
      toast(T("t_donated").replace("AMOUNT", 25));
    });
    $("#seedLater").addEventListener("click", function () {
      closeModal($("#mNew")); sheet.innerHTML = prev; wireNewForm();
      renderAll(); openProject(p.id);
    });
  }
  function readPhoto(file, cb) {
    var fr = new FileReader();
    fr.onload = function () {
      var img = new Image();
      img.onload = function () {
        var max = 900, w = img.width, h = img.height, k = Math.min(1, max / Math.max(w, h));
        var c = document.createElement("canvas");
        c.width = Math.round(w * k); c.height = Math.round(h * k);
        c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
        cb(c.toDataURL("image/jpeg", 0.72));
      };
      img.src = fr.result;
    };
    fr.readAsDataURL(file);
  }
  function wireNewForm() {
    var photo = $("#nPhoto"), box = $("#nPhotoBox"), prev = $("#nPreview");
    if (!photo) return;
    photo.addEventListener("change", function () {
      var f = photo.files && photo.files[0];
      if (!f) return;
      readPhoto(f, function (dataUrl) {
        draftPhoto = dataUrl;
        prev.src = dataUrl; prev.hidden = false;
        box.classList.add("has-photo");
      });
    });
    $("#nGeo").addEventListener("click", function () {
      if (!navigator.geolocation) { toast(T("t_geo_err")); return; }
      navigator.geolocation.getCurrentPosition(function (g) {
        draftCoords = [g.coords.latitude, g.coords.longitude];
        $("#nCoords").textContent = coordsTxt(draftCoords);
        toast(T("place") + ": " + coordsTxt(draftCoords));
      }, function () { toast(T("t_geo_err")); }, { enableHighAccuracy: true, timeout: 8000 });
    });
    $("#nPick").addEventListener("click", function () {
      closeModal($("#mNew"));
      pickMode = true;
      $("#map").classList.add("is-picking");
      showView("map");
      toast(T("pickOnMap"));
    });
    $("#nGo").addEventListener("click", doPublish);
  }

  /* ============================================================ nav */
  var SUBS = {
    home: "21.city", map: { ru: "карта района", en: "the neighbourhood map" },
    projects: { ru: "проекты и квесты", en: "projects & quests" },
    wallet: { ru: "кошелёк", en: "wallet" }, profile: { ru: "профиль", en: "profile" }
  };
  function showView(v) {
    if (!SUBS[v]) v = "home";
    if (!routing) history.pushState(null, "", "#/" + v);
    $$(".tab").forEach(function (t) { if (t.getAttribute("data-view") === v) t.setAttribute("aria-current", "page"); else t.removeAttribute("aria-current"); });
    $$(".view").forEach(function (s) { s.classList.toggle("is-on", s.id === "view-" + v); });
    $$(".tab").forEach(function (t) { t.classList.toggle("is-on", t.getAttribute("data-view") === v); });
    var sub = SUBS[v];
    $("#headSub").textContent = typeof sub === "string" ? sub : loc(sub);
    $("#screen").scrollTop = 0;
    if (v === "map") {
      initMap();
      setTimeout(function () { if (map) map.invalidateSize(); }, 60);
    }
  }

  /* ============================================================ lang */
  function setLang(l, saveIt) {
    state.lang = l;
    var root = document.documentElement;
    root.setAttribute("lang", l);
    root.setAttribute("data-lang", l);
    document.title = l === "en"
      ? "21.city — civic projects and quests nearby"
      : "21.city — городские проекты и квесты рядом";
    $$("[data-set-lang]").forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-set-lang") === l ? "true" : "false");
    });
    $$("[data-i18n]").forEach(function (el) {
      var k = el.getAttribute("data-i18n");
      if (I18N.ru[k] != null) el.textContent = T(k);
    });
    var ms = $("#mapSearch");
    if (ms) ms.placeholder = l === "en" ? "Search projects, tasks, location…" : "Проект, задача, место…";
    if (saveIt) save();
    renderAll();
  }

  function renderAll() {
    renderHome();
    renderProjects();
    renderWallet();
    renderProfile();
    renderMapList();
    if (detailId != null && !$("#detail").hidden) renderDetail(true);
  }

  /* ============================================================ events */
  function wire() {
    document.addEventListener("click", function (e) {
      var t = e.target;

      var nav = t.closest && t.closest("[data-nav]");
      if (nav) { e.preventDefault(); showView(nav.getAttribute("data-nav")); return; }

      var tab = t.closest && t.closest(".tab");
      if (tab) { showView(tab.getAttribute("data-view")); return; }

      var lang = t.closest && t.closest("[data-set-lang]");
      if (lang) { setLang(lang.getAttribute("data-set-lang"), true); return; }

      var openNewBtn = t.closest && t.closest("[data-open-new]");
      if (openNewBtn) { openNew(); return; }

      var how = t.closest && t.closest("[data-how]");
      if (how) { openModal("#mHow"); return; }

      var close = t.closest && t.closest("[data-close]");
      if (close) { closeModal(close.closest(".modal")); return; }

      var advreq = t.closest && t.closest("[data-advreq]");
      if (advreq) { e.stopPropagation(); openAdvance(advreq.getAttribute("data-advreq")); return; }

      var advvote = t.closest && t.closest("[data-advvote]");
      if (advvote) {
        e.stopPropagation();
        voteAdvance(advvote.getAttribute("data-advvote"), advvote.getAttribute("data-yes") === "1");
        return;
      }

      var mdon = t.closest && t.closest("[data-donate]");
      if (mdon) { e.stopPropagation(); openDonate(mdon.getAttribute("data-donate")); return; }

      var moff = t.closest && t.closest("[data-newoffer]");
      if (moff) { e.stopPropagation(); openOffer(moff.getAttribute("data-newoffer")); return; }

      var moff2 = t.closest && t.closest("[data-offer]");
      if (moff2) { e.stopPropagation(); var pid = moff2.getAttribute("data-offer"); if (detailId !== Number(pid)) openProject(pid); return; }

      var showmap = t.closest && t.closest("[data-showmap]");
      if (showmap) {
        var sp = byId(showmap.getAttribute("data-showmap"));
        closeDetail(); showView("map");
        if (sp) { initMap(); if (map) { map.setView(sp.coords, 17, { animate: true }); if (markers[sp.id]) markers[sp.id].openPopup(); } }
        return;
      }

      var proj = t.closest && t.closest("[data-project]");
      if (proj && !t.closest("[data-donate],[data-offer],[data-showmap],[data-accept],[data-vote],[data-advvote],[data-advreq]")) {
        openProject(proj.getAttribute("data-project"));
        return;
      }

      var accept = t.closest && t.closest("[data-accept]");
      if (accept) {
        e.stopPropagation();
        var ap = byId(accept.getAttribute("data-accept"));
        var oid = Number(accept.getAttribute("data-offer-id"));
        if (ap) {
          ap.contractor = oid; ap.stage = 3; save();
          toast(T("t_accepted")); renderAll(); renderDetail(true);
        }
        return;
      }

      var adv = t.closest && t.closest("[data-advance]");
      if (adv) {
        var ap2 = byId(adv.getAttribute("data-advance"));
        var to = Number(adv.getAttribute("data-to"));
        if (ap2) {
          ap2.stage = to;
          if (to === 3) { var mo = minOfferOf(ap2); if (mo) ap2.contractor = mo.id; toast(T("t_accepted")); }
          if (to === 4) toast(T("t_work_done"));
          if (to === 5) toast(T("t_paid"));
          save(); renderAll(); renderDetail(true);
        }
        return;
      }

      var vote = t.closest && t.closest("[data-vote]");
      if (vote) {
        e.stopPropagation();
        var vp = byId(vote.getAttribute("data-vote"));
        if (vp) {
          vp.voted = !vp.voted;
          vp.votes += vp.voted ? 1 : -1;
          save(); toast(vp.voted ? T("t_vote") : T("t_unvote"));
          renderAll(); renderDetail(true);
        }
        return;
      }

      var q = t.closest && t.closest("[data-accept-quest]");
      if (q) {
        e.stopPropagation();
        var id = Number(q.getAttribute("data-accept-quest"));
        state.quests.forEach(function (qq) { if (qq.id === id) qq.accepted = true; });
        save(); toast(T("t_quest")); renderAll();
        return;
      }

      var qs = t.closest && t.closest("[data-qsort]");
      if (qs) {
        qsort = qs.getAttribute("data-qsort");
        $$("#questChips .chip").forEach(function (c) { c.classList.toggle("is-on", c === qs); });
        renderHome(); return;
      }

      var pl = t.closest && t.closest("[data-plist]");
      if (pl) {
        plist = pl.getAttribute("data-plist");
        $$("#projChips .chip").forEach(function (c) { c.classList.toggle("is-on", c === pl); });
        renderProjects(); return;
      }

      var wt = t.closest && t.closest("[data-wtab]");
      if (wt) {
        wtab = wt.getAttribute("data-wtab");
        $$("#walletTabs .chip").forEach(function (c) { c.classList.toggle("is-on", c === wt); });
        renderWallet(); return;
      }

      var sk = t.closest && t.closest("[data-skill]");
      if (sk) {
        var s = sk.getAttribute("data-skill");
        var i = state.user.skills.indexOf(s);
        if (i >= 0) state.user.skills.splice(i, 1); else state.user.skills.push(s);
        save(); renderProfile(); return;
      }

      if (t.closest && t.closest("#btnContractor")) {
        state.user.contractor = true; save(); renderProfile();
        toast(T("t_contractor"));
        return;
      }
    });

    /* modal backdrop click */
    $$(".modal").forEach(function (m) {
      m.addEventListener("click", function (e) { if (e.target === m) closeModal(m); });
    });

    /* donate amounts */
    $("#dAmounts").addEventListener("click", function (e) {
      var b = e.target.closest(".amt");
      if (!b) return;
      donateAmt = b.getAttribute("data-amt");
      $$("#dAmounts .amt").forEach(function (x) { x.classList.toggle("is-on", x === b); });
      $("#dOtherWrap").hidden = donateAmt !== "other";
      if (donateAmt === "other") $("#dOther").focus();
    });
    $("#dGo").addEventListener("click", doDonate);

    $("#oGo").addEventListener("click", doOffer);
    $("#aGo").addEventListener("click", doAdvanceRequest);

    /* chat */
    $("#detailIn").addEventListener("click", function (e) {
      if (e.target.closest && e.target.closest("#detBack")) { closeDetail(); return; }
      if (e.target.closest && e.target.closest("#chatSend")) {
        var p = byId(detailId);
        var inp = $("#chatText");
        if (p && inp && inp.value.trim()) {
          p.chat.push({ you: true, text: inp.value.trim(), ts: Date.now() });
          inp.value = ""; save(); renderDetail(true);
        }
      }
    });
    $("#detailIn").addEventListener("keydown", function (e) {
      if (e.key === "Enter" && e.target && e.target.id === "chatText") {
        var p = byId(detailId);
        if (p && e.target.value.trim()) {
          p.chat.push({ you: true, text: e.target.value.trim(), ts: Date.now() });
          e.target.value = ""; save(); renderDetail(true);
        }
      }
    });

    /* map */
    $("#mapSearch").addEventListener("input", function (e) {
      searchQ = e.target.value; renderMapList();
    });
    $("#btnLocate").addEventListener("click", function () {
      if (!navigator.geolocation) { toast(T("t_geo_err")); return; }
      navigator.geolocation.getCurrentPosition(function (g) {
        state.myPos = [g.coords.latitude, g.coords.longitude];
        save();
        if (map) { map.setView(state.myPos, 15); meMarkerUpdate(); }
        toast(T("t_geo"));
        renderAll();
      }, function () { toast(T("t_geo_err")); }, { enableHighAccuracy: true, timeout: 8000 });
    });

    /* profile */
    $("#btnReset").addEventListener("click", function () {
      if (!window.confirm(state.lang === "en" ? "Reset all local data? Export a backup first." : "Сбросить все локальные данные? Сначала сохраните экспорт.")) return;
      try { localStorage.removeItem(LS); } catch (e) {}
      var lang = state.lang;
      state = seedData(); state.lang = lang; save();
      setLang(state.lang, false);
      toast(T("t_reset"));
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Tab") {
        var dialog = $(".modal.is-on") || (!$("#detail").hidden ? $("#detail") : null);
        if (dialog) {
          var focusables = $$("button, input, select, textarea, a[href]", dialog).filter(function (el) { return !el.disabled && el.getClientRects().length; });
          var first = focusables[0], last = focusables[focusables.length - 1];
          if (first && e.shiftKey && (document.activeElement === first || document.activeElement === dialog)) { e.preventDefault(); last.focus(); }
          else if (last && !e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        }
      }
      if (e.key === "Escape") {
        if ($(".modal.is-on")) closeModal();
        else if (detailId != null && !$("#detail").hidden) closeDetail();
      }
    });
  }

  /* ============================================================ boot */
  var routing = false;
  function restoreRoute() {
    routing = true;
    var route = location.hash.slice(2).split("/");
    if (detailId != null) closeDetail();
    if (route[0] === "project" && byId(Number(route[1]))) { showView("projects"); openProject(Number(route[1])); }
    else showView(SUBS[route[0]] ? route[0] : "home");
    routing = false;
  }
  function boot() {
    state = load() || seedData();
    save();
    fillCats();
    wireNewForm();
    wire();
    setLang(state.lang, false);
    restoreRoute();
    window.addEventListener("popstate", restoreRoute);
    $("#catalogSearch").addEventListener("input", function (e) { catalogQ = e.target.value; renderProjects(); });
    $("#catalogSort").addEventListener("change", function (e) { catalogOrder = e.target.value; renderProjects(); });
    $("#profileForm").addEventListener("submit", function (e) { e.preventDefault(); var name = $("#profileNameInput").value.trim(); if (!name) return; state.user.name = name; save(); renderProfile(); toast(state.lang === "en" ? "Profile saved" : "Профиль сохранён"); });
    $("#btnExport").addEventListener("click", function () {
      var url = URL.createObjectURL(new Blob([JSON.stringify(state, null, 2)], { type: "application/json" }));
      var a = document.createElement("a"); a.href = url; a.download = "21city-backup-" + new Date().toISOString().slice(0,10) + ".json"; a.click(); setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    });
    setTimeout(function () {
      toast(state.lang === "en"
        ? "Demo: everything is stored in this browser"
        : "Демо: все данные хранятся в этом браузере");
    }, 900);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
