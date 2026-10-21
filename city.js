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
      emptyList: "Ничего не нашлось.",
      badAmount: "Введите сумму от 1 до 1 000 000",
      bothersMeToo: "мне тоже мешает",
      budgetMicro: "Донат идёт в бюджет проекта и тратится на работу, а не на комиссии платформы.",
      confirmReset: "Сбросить все локальные данные? Сначала сохраните экспорт.",
      dAgo: " дн назад",
      docTitle: "21.city — городские проекты и квесты рядом",
      hAgo: " ч назад",
      inBudgetsStat: "в бюджетах проектов",
      justNow: "только что",
      kmUnit: " км",
      mUnit: " м",
      onTheMap: " на карте",
      profileSaved: "Профиль сохранён",
      saveError: "Не удалось сохранить данные. Сделайте экспорт в профиле.",
      searchPh: "Проект, задача, место…",
      statContribs: "взносов",
      statProjects: "проекта",
      statQuests: "квестов",
      t_demo: "Демо: все данные хранятся в этом браузере",
      unitDays: "дн",
      unitHours: "ч",
      youDonated: "Вы внесли ",
      bandText: "Пять шагов: от фото проблемы до публичного чека. Соседи пополняют бюджет, подрядчики присылают предложения, эскроу платит после приёмки.",
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
      emptyList: "Nothing found.",
      badAmount: "Enter an amount from 1 to 1,000,000",
      bothersMeToo: "bothers me too",
      budgetMicro: "Your donation goes to the work, not to platform fees.",
      confirmReset: "Reset all local data? Export a backup first.",
      dAgo: " d ago",
      docTitle: "21.city — civic projects and quests nearby",
      hAgo: " h ago",
      inBudgetsStat: "in project budgets",
      justNow: "just now",
      kmUnit: " km",
      mUnit: " m",
      onTheMap: " on the map",
      profileSaved: "Profile saved",
      saveError: "Unable to save. Export your data from Profile.",
      searchPh: "Search projects, tasks, location…",
      statContribs: "contributions",
      statProjects: "projects",
      statQuests: "quests",
      t_demo: "Demo: everything is stored in this browser",
      unitDays: "days",
      unitHours: "h",
      youDonated: "You donated ",
      shortfall: "short of the lowest offer",
      canTopUp: "— the budget can still be topped up while work is going",
      bandText: "Five steps: from a photo of the problem to a public receipt. Neighbours fund the budget, contractors send offers, escrow pays after acceptance.",
    },
    es: {
      newest: "Primero los nuevos",
      funding: "Más cerca del objetivo",
      tabHome: "Resumen",
      tabMap: "Mapa",
      tabProjects: "Proyectos",
      tabWallet: "Monedero",
      tabProfile: "Perfil",
      findProject: "Buscar proyecto",
      questsNearby: "Misiones cercanas",
      projectsNearby: "Proyectos cercanos",
      nearbyProjects: "Proyectos cercanos",
      all: "Todos",
      projects: "Proyectos",
      quests: "Misiones",
      forYou: "Para ti",
      popular: "Populares",
      nearby: "Cerca",
      projectsTitle: "Proyectos y misiones",
      projectsSub: "Problemas urbanos con fotos y coordenadas — y tareas de los vecinos",
      walletTitle: "Monedero",
      walletSub: "Tus aportes a los presupuestos de proyectos urbanos",
      inBudgets: "En presupuestos de proyectos",
      active: "Activos",
      contributed: "Mis aportes",
      completed: "Completados",
      you: "Tú",
      myProjects: "Mis proyectos",
      myQuests: "Mis misiones",
      wallet: "Monedero",
      howWorks: "Cómo funciona",
      resetDemo: "Restablecer los datos de demo",
      addToBudget: "Añadir al presupuesto",
      donate: "Donar",
      other: "Otra",
      yourAmount: "Tu importe, €",
      yourName: "Nombre (cómo mostrarlo)",
      submitOffer: "Enviar una oferta",
      sendOffer: "Enviar oferta",
      contractor: "Contratista / empresa",
      price: "Precio, €",
      days: "Plazo, días",
      postNeed: "Informar de un problema",
      whatHappened: "Qué ha pasado",
      desc: "Detalles",
      category: "Categoría",
      publish: "Publicar",
      place: "Lugar",
      gotIt: "Entendido",
      locate: "Dónde estoy",
      newProblem: "Informar de un problema",
      open: "Abierto",
      viewOnMap: "Ver en el mapa",
      details: "Detalles",
      offersShort: "ofertas",
      donationsShort: "donaciones",
      addBudgetShort: "+ Al presupuesto",
      budgetTitle: "Presupuesto del proyecto",
      of: "de",
      targetMin: "Objetivo: la oferta más baja",
      targetEst: "Estimación del autor: todavía no hay ofertas",
      donors: "Han aportado",
      offersTitle: "Ofertas comerciales",
      minPrice: "precio mínimo",
      shortfall: "faltan para la oferta más baja",
      canTopUp: "— el presupuesto se puede completar mientras hay obra",
      accept: "Aceptar",
      chatTitle: "Chat del proyecto",
      chatPlaceholder: "Mensaje…",
      send: "Enviar",
      advanceTitle: "Anticipo para materiales y trabajo",
      requestAdvance: "Solicitar anticipo",
      sendRequest: "Enviar solicitud",
      advAmount: "Importe del anticipo, €",
      advReason: "Justificación",
      advBy: "solicitó un anticipo",
      giveAdvance: "Dar el anticipo",
      declineAdvance: "Rechazar",
      advVotersOnly: "Solo votan los donantes de este proyecto",
      advToVote: "Dona cualquier cantidad para votar",
      advFor: "a favor",
      advAgainst: "en contra",
      yourVote: "Tu voto",
      advOpenA: "Han votado",
      advOpenB: "de lo recaudado",
      advRule: "se necesita la mayoría del importe aportado",
      advApproved: "Anticipo aprobado",
      advRejected: "Anticipo rechazado por los donantes",
      advPaidNote: "pagado al contratista desde el escrow",
      advRestNote: "queda en el escrow hasta la recepción",
      advReRequest: "Solicitar de nuevo",
      advDemoNote: "El contratista puede pedir un anticipo, con su justificación",
      timelineTitle: "Cómo va el proyecto",
      now: "ahora",
      stage1: "Apoyo de la comunidad",
      stage1d: "los vecinos suman al presupuesto con donaciones",
      stage2: "Buscar contratistas",
      stage2d: "ofertas abiertas; el objetivo es el precio más bajo",
      stage3: "Obra en curso",
      stage3d: "después de elegir contratista",
      stage4: "Verificación",
      stage4d: "confirmar y pagar",
      stage5: "Completado",
      stage5d: "el resultado es público",
      chainNote: "Sandbox: los pasos se guardan solo en este navegador. El escrow y los pagos están simulados; no hay blockchain conectada.",
      demoPick: "Elegir contratista (demo)",
      demoWorkDone: "Obra terminada (demo)",
      demoPay: "Confirmar y pagar (demo)",
      budgetReady: "Presupuesto completo: ya se puede encargar",
      works: "trabajos",
      respond: "Responder",
      responded: "Respuesta enviada",
      publishLive: "¡Solicitud publicada!",
      publishLiveD: "Ahora los vecinos la ven en el mapa y pueden ofrecer ayuda y ofertas.",
      seedDonate: "Añadir 25 € al presupuesto",
      later: "Más tarde",
      becomeContractor: "Hazte contratista",
      becomeContractorD: "Ayuda a tu barrio con tus habilidades. Gana por el trabajo que haces de verdad.",
      contractorOn: "Eres contratista",
      myOffers: "Mis ofertas",
      offersSent: "Ofertas enviadas",
      tasksDone: "Completados",
      earned: "Ganado",
      pickOnMap: "Toca el mapa para marcar el lugar",
      how1t: "1 · Apoyo de la comunidad",
      how1d: "Alguien fotografía la acera rota de su portal. Los vecinos cercanos ven el problema en el mapa y suman al presupuesto del proyecto con donaciones.",
      how2t: "2 · Buscar contratistas",
      how2d: "Mientras se acumulan las donaciones, llegan ofertas comerciales. El objetivo del presupuesto es la oferta más baja.",
      how3t: "3 · Obra",
      how3d: "Con el presupuesto listo se elige la mejor oferta y empieza el contratista. Un anticipo para materiales necesita justificación y el voto de los donantes.",
      how4t: "4 · Verificación",
      how4d: "Los vecinos confirman el resultado — el escrow paga al contratista.",
      how5t: "5 · Completado",
      how5d: "El recibo se queda público: cada paso se ve, el dinero fue a la obra.",
      t_donated: "€+AMOUNT al presupuesto del proyecto. Ayudará a atraer ofertas y acelerar la obra.",
      t_offer_new_min: "Objetivo recalculado: €AMOUNT, la oferta más baja.",
      t_offer_added: "Oferta enviada. Todo el mundo la ve en la licitación del proyecto.",
      t_accepted: "Oferta aceptada. Empieza la obra.",
      t_work_done: "Obra terminada. Falta la verificación.",
      t_paid: "El escrow pagó al contratista. El recibo es público.",
      t_adv_requested: "La solicitud de anticipo se envió a los donantes del proyecto.",
      t_adv_approved: "Los donantes aprobaron el anticipo: se paga desde el escrow.",
      t_adv_rejected: "Los donantes rechazaron el anticipo.",
      t_adv_vote_y: "Voto registrado: a favor del anticipo.",
      t_adv_vote_n: "Voto registrado: en contra del anticipo.",
      t_vote: "Marcado: a ti también te molesta.",
      t_unvote: "Marca retirada.",
      t_geo: "Actualizado: mostramos los proyectos cerca de ti.",
      t_geo_err: "No se pudo obtener tu ubicación.",
      t_published: "Proyecto publicado. Ya está en el mapa.",
      t_quest: "Respuesta enviada (demo).",
      t_contractor: "Ahora puedes enviar ofertas a los proyectos del barrio.",
      t_reset: "Datos de demo restablecidos.",
      joinedAgo: "en el proyecto",
      m: "meses",
      back: "Atrás",
      project: "Proyecto",
      estLabel: "estimación",
      noOffersYet: "Aún no hay ofertas: el presupuesto sigue la estimación del autor.",
      awaitingOffers: "esperando ofertas",
      chosen: "elegido",
      emptyWallet: "Todavía no hay aportes. Find a proyecto cercano y apóyalo.",
      emptyList: "No se ha encontrado nada.",
      inBudgetsStat: "en presupuestos de proyectos",
      onTheMap: " en el mapa",
      youDonated: "Has aportado ",
      statQuests: "misiones",
      statProjects: "proyectos",
      statContribs: "aportes",
      unitDays: "días",
      unitHours: "h",
      mUnit: " m",
      kmUnit: " km",
      justNow: "ahora mismo",
      hAgo: " h atrás",
      dAgo: " d atrás",
      docTitle: "21.city — proyectos urbanos y misiones cerca",
      searchPh: "Proyecto, tarea, lugar…",
      budgetMicro: "Tu donación va al presupuesto del proyecto y se gasta en la obra, no en comisiones de la plataforma.",
      badAmount: "Introduce un importe entre 1 y 1 000 000",
      confirmReset: "¿Restablecer todos los datos locales? Exporta una copia antes.",
      profileSaved: "Perfil guardado",
      t_demo: "Demo: todos los datos se guardan en este navegador",
      saveError: "No se pudieron guardar los datos. Exporta desde el perfil.",
      bothersMeToo: "a mí también me molesta",
      bandText: "Cinco pasos: de la foto del problema al recibo público. Los vecinos financian el presupuesto, los contratistas envían ofertas y el escrow paga tras la aceptación.",
    },
    zh: {
      newest: "最新优先",
      funding: "最接近目标",
      tabHome: "概览",
      tabMap: "地图",
      tabProjects: "项目",
      tabWallet: "钱包",
      tabProfile: "个人资料",
      findProject: "找项目",
      questsNearby: "附近的任務",
      projectsNearby: "附近的项目",
      nearbyProjects: "附近的项目",
      all: "全部",
      projects: "项目",
      quests: "任务",
      forYou: "为你推荐",
      popular: "热门",
      nearby: "附近",
      projectsTitle: "项目与任务",
      projectsSub: "带照片和坐标的城市问题 —— 以及邻居们的任务",
      walletTitle: "钱包",
      walletSub: "你对城市项目预算的投入",
      inBudgets: "项目预算中",
      active: "进行中",
      contributed: "我的投入",
      completed: "已完成",
      you: "你",
      myProjects: "我的项目",
      myQuests: "我的任务",
      wallet: "钱包",
      howWorks: "运作方式",
      resetDemo: "重置演示数据",
      addToBudget: "加入预算",
      donate: "捐赠",
      other: "其他",
      yourAmount: "你的金额，€",
      yourName: "昵称（展示用）",
      submitOffer: "提交报价",
      sendOffer: "发送报价",
      contractor: "承包方 / 公司",
      price: "价格，€",
      days: "工期，天数",
      postNeed: "报告问题",
      whatHappened: "发生了什么",
      desc: "详情",
      category: "类别",
      publish: "发布",
      place: "地点",
      gotIt: "明白了",
      locate: "我在哪",
      newProblem: "报告问题",
      open: "开放中",
      viewOnMap: "在地图上查看",
      details: "详情",
      offersShort: "报价",
      donationsShort: "捐款",
      addBudgetShort: "+ 加入预算",
      budgetTitle: "项目预算",
      of: "/",
      targetMin: "目标 — 最低报价",
      targetEst: "作者估价 —— 尚未收到报价",
      donors: "参与者",
      offersTitle: "商业报价",
      minPrice: "最低价",
      shortfall: "距离最低报价还差",
      canTopUp: "—— 施工期间仍可继续补充预算",
      accept: "接受",
      chatTitle: "项目聊天",
      chatPlaceholder: "消息…",
      send: "发送",
      advanceTitle: "材料与施工预付款",
      requestAdvance: "申请预付款",
      sendRequest: "发送申请",
      advAmount: "预付款金额，€",
      advReason: "理由说明",
      advBy: "申请了预付款",
      giveAdvance: "同意预付款",
      declineAdvance: "拒绝",
      advVotersOnly: "仅本项目的捐助者可投票",
      advToVote: "捐款任意金额即可投票",
      advFor: "赞成",
      advAgainst: "反对",
      yourVote: "你的投票",
      advOpenA: "已投票",
      advOpenB: "/ 已募集",
      advRule: "需要按捐款金额的多数",
      advApproved: "预付款已批准",
      advRejected: "预付款被捐助者否决",
      advPaidNote: "已从托管支付给承包方",
      advRestNote: "验收前仍在托管中",
      advReRequest: "重新申请",
      advDemoNote: "承包方可以申请预付款 —— 需附理由说明",
      timelineTitle: "项目进展",
      now: "现在",
      stage1: "社区支持",
      stage1d: "邻居们用捐款补充预算",
      stage2: "寻找承包方",
      stage2d: "报价开放，目标为最低价",
      stage3: "施工中",
      stage3d: "选定承包方后",
      stage4: "验收",
      stage4d: "确认并付款",
      stage5: "完成",
      stage5d: "结果公开",
      chainNote: "沙盒：所有步骤只保存在此浏览器中。托管与支付均为模拟，未接入区块链。",
      demoPick: "选择承包方（演示）",
      demoWorkDone: "施工完成（演示）",
      demoPay: "确认并付款（演示）",
      budgetReady: "预算已凑齐 —— 可以下单",
      works: "单",
      respond: "回应",
      responded: "回应已发送",
      publishLive: "申请已发布！",
      publishLiveD: "邻居们现在能在地图上看到它，并可以提供帮助和报价。",
      seedDonate: "往预算里加 €25",
      later: "稍后",
      becomeContractor: "成为承包方",
      becomeContractorD: "用你的技能帮助街区，靠真实的工作获得报酬。",
      contractorOn: "你是承包方",
      myOffers: "我的报价",
      offersSent: "已发送报价",
      tasksDone: "已完成",
      earned: "已赚取",
      pickOnMap: "点击地图以标记位置",
      how1t: "1 · 社区支持",
      how1d: "有人拍下家门口裂开的人行道。附近的邻居在地图上看到问题，用捐款为项目预算添砖加瓦。",
      how2t: "2 · 寻找承包方",
      how2d: "在捐款积累的同时，商业报价陆续到来。预算目标是最低报价。",
      how3t: "3 · 施工",
      how3d: "预算就绪后选出最佳报价，承包方开工。材料预付款需要理由说明，并由捐助者投票。",
      how4t: "4 · 验收",
      how4d: "邻居们确认结果 —— 托管付款给承包方。",
      how5t: "5 · 完成",
      how5d: "收据保持公开：每一步都看得见，钱花在了工程上。",
      t_donated: "€+AMOUNT 已加入项目预算。这有助于招来报价、加快施工。",
      t_offer_new_min: "预算目标已重算：€AMOUNT —— 最低报价。",
      t_offer_added: "报价已发送，项目招标中所有人都能看到。",
      t_accepted: "报价已接受，开工。",
      t_work_done: "施工完成，等待验收。",
      t_paid: "托管已支付给承包方，收据公开。",
      t_adv_requested: "预付款申请已发送给项目捐助者。",
      t_adv_approved: "捐助者已批准预付款 —— 已从托管支付。",
      t_adv_rejected: "捐助者否决了预付款。",
      t_adv_vote_y: "投票已记录：赞成预付款。",
      t_adv_vote_n: "投票已记录：反对预付款。",
      t_vote: "已标记：这个问题也困扰你。",
      t_unvote: "已取消标记。",
      t_geo: "已更新：显示你附近的项目。",
      t_geo_err: "无法获取你的位置。",
      t_published: "项目已发布，已出现在地图上。",
      t_quest: "回应已发送（演示）。",
      t_contractor: "现在你可以在街区项目上提交报价了。",
      t_reset: "演示数据已重置。",
      joinedAgo: "已加入项目",
      m: "个月",
      back: "返回",
      project: "项目",
      estLabel: "估价",
      noOffersYet: "还没有报价 —— 预算按作者估价计算。",
      awaitingOffers: "等待报价",
      chosen: "已选定",
      emptyWallet: "还没有投入。找找附近的项目，支持它。",
      emptyList: "没有找到任何内容。",
      inBudgetsStat: "项目预算中",
      onTheMap: " 个在地图上",
      youDonated: "您已投入 ",
      statQuests: "个任务",
      statProjects: "个项目",
      statContribs: "次投入",
      unitDays: "天",
      unitHours: "小时",
      mUnit: " 米",
      kmUnit: " 公里",
      justNow: "刚刚",
      hAgo: " 小时前",
      dAgo: " 天前",
      docTitle: "21.city —— 附近的城市项目与任务",
      searchPh: "项目、任务、地点…",
      budgetMicro: "捐款进入项目预算，花在工程上，而不是平台手续费。",
      badAmount: "请输入 1 到 1,000,000 之间的金额",
      confirmReset: "重置所有本地数据？请先导出备份。",
      profileSaved: "资料已保存",
      t_demo: "演示：所有数据都保存在这个浏览器里",
      saveError: "无法保存数据，请在个人资料中导出。",
      bothersMeToo: "我也受影响",
      bandText: "五个步骤：从拍下问题到公开收据。邻居们出资，承包方给出报价，验收后托管付款。",
    },
    ja: {
      newest: "新しい順",
      funding: "目標に近い順",
      tabHome: "概要",
      tabMap: "地図",
      tabProjects: "プロジェクト",
      tabWallet: "ウォレット",
      tabProfile: "プロフィール",
      findProject: "プロジェクトを探す",
      questsNearby: "近くのクエスト",
      projectsNearby: "近くのプロジェクト",
      nearbyProjects: "近くのプロジェクト",
      all: "すべて",
      projects: "プロジェクト",
      quests: "クエスト",
      forYou: "あなたへのおすすめ",
      popular: "人気",
      nearby: "近く",
      projectsTitle: "プロジェクトとクエスト",
      projectsSub: "写真と座標付きの街の問題 — そして隣人のクエスト",
      walletTitle: "ウォレット",
      walletSub: "街のプロジェクトの予算へのあなたの寄付",
      inBudgets: "プロジェクトの予算へ",
      active: "進行中",
      contributed: "私の寄付",
      completed: "完了",
      you: "あなた",
      myProjects: "自分のプロジェクト",
      myQuests: "自分のクエスト",
      wallet: "ウォレット",
      howWorks: "しくみ",
      resetDemo: "デモデータをリセット",
      addToBudget: "予算に加える",
      donate: "寄付する",
      other: "その他",
      yourAmount: "金額, €",
      yourName: "表示する名前",
      submitOffer: "見積もりを出す",
      sendOffer: "見積もりを送る",
      contractor: "施工者 / 会社",
      price: "価格, €",
      days: "工期, 日数",
      postNeed: "問題を報告する",
      whatHappened: "何が起きましたか",
      desc: "詳細",
      category: "カテゴリー",
      publish: "公開する",
      place: "場所",
      gotIt: "了解",
      locate: "現在地",
      newProblem: "問題を報告する",
      open: "募集中",
      viewOnMap: "地図で見る",
      details: "詳細",
      offersShort: "見積",
      donationsShort: "寄付",
      addBudgetShort: "+ 予算に",
      budgetTitle: "プロジェクトの予算",
      of: "/",
      targetMin: "目標 — 最安の見積り",
      targetEst: "投稿者の見積もり — まだ見積りがありません",
      donors: "参加者",
      offersTitle: "民間見積もり",
      minPrice: "最安値",
      shortfall: "最安値まであと",
      canTopUp: "— 作業中は予算を追加できます",
      accept: "採用",
      chatTitle: "プロジェクトのチャット",
      chatPlaceholder: "メッセージ…",
      send: "送信",
      advanceTitle: "資材・工事の前払い",
      requestAdvance: "前払いを申請",
      sendRequest: "申請を送る",
      advAmount: "前払い金額, €",
      advReason: "理由",
      advBy: "前払いを申請しました",
      giveAdvance: "前払いを出す",
      declineAdvance: "見送る",
      advVotersOnly: "投票できるのはこのプロジェクトの寄付者だけ",
      advToVote: "いくらでも寄付すれば投票できます",
      advFor: "賛成",
      advAgainst: "反対",
      yourVote: "あなたの投票",
      advOpenA: "投票済み",
      advOpenB: "/ 集めた額",
      advRule: "寄付金額の過半数の賛成が必要です",
      advApproved: "前払いが承認されました",
      advRejected: "寄付者に否認されました",
      advPaidNote: "エスクロから施工者に支払済み",
      advRestNote: "検収までエスクロに残ります",
      advReRequest: "もう一度申請する",
      advDemoNote: "施工者は前払いを申請できます（理由の提示が必要）",
      timelineTitle: "プロジェクトの進捗",
      now: "現在",
      stage1: "コミュニティのサポート",
      stage1d: "隣人が寄付で予算を積み上げます",
      stage2: "施工者を探す",
      stage2d: "見積もりを公開中、目標は最安値",
      stage3: "作業中",
      stage3d: "施工者選定後",
      stage4: "検収",
      stage4d: "確認して支払う",
      stage5: "完了",
      stage5d: "結果は公開",
      chainNote: "サンドボックス：記録はこのブラウザ内にのみ保存されます。エスクロと支払いはシミュレーションで、暗号資産は接続されていません。",
      demoPick: "施工者を選ぶ（デモ）",
      demoWorkDone: "作業完了（デモ）",
      demoPay: "確認して支払う（デモ）",
      budgetReady: "予算がそろった — 依頼できます",
      works: "件",
      respond: "応募する",
      responded: "応募を送信しました",
      publishLive: "依頼を公開しました！",
      publishLiveD: "隣人たちは地図でそれを見て、手伝いや見積もりを送れます。",
      seedDonate: "予算に 25 € を加える",
      later: "あとで",
      becomeContractor: "施工者になる",
      becomeContractorD: "あなたの腕で街を支援。実際の作業に対する報酬を受け取れます。",
      contractorOn: "あなたは施工者です",
      myOffers: "自分の見積もり",
      offersSent: "送信した見積もり",
      tasksDone: "完了した作業",
      earned: "収益",
      pickOnMap: "地図をタップして場所を指定",
      how1t: "1 · コミュニティのサポート",
      how1d: "ある人が家の前の壊れた歩道を撮ります。近くの隣人たちは地図で問題を見て、寄付でプロジェクトの予算を積み上げます。",
      how2t: "2 · 施工者を探す",
      how2d: "寄付が集まるあいだに、民間の見積もりが届きます。予算の目標は最安値です。",
      how3t: "3 · 作業",
      how3d: "予算がそろったら最良の見積もりを選び、施工者が着手します。資材の前払いは理由の提示と寄付者の投票が必要です。",
      how4t: "4 · 検収",
      how4d: "隣人が結果を確認します — エスクロが施工者に支払います。",
      how5t: "5 · 完了",
      how5d: "領収書は公開のまま：すべての過程が見え、お金は工事に使われました。",
      t_donated: "プロジェクト予算に €+AMOUNT を追加しました。見積もりを集め、作業を早める助けになります。",
      t_offer_new_min: "予算の目標を再計算しました：€AMOUNT が最安の見積りです。",
      t_offer_added: "見積もりを送信しました。プロジェクトの入札でみんなが見られます。",
      t_accepted: "見積もりを採用しました。作業が始まります。",
      t_work_done: "作業が完了しました。検収を待っています。",
      t_paid: "エスクロから施工者に支払いました。領収書は公開です。",
      t_adv_requested: "前払いの申請を寄付者に送りました。",
      t_adv_approved: "寄付者が前払いを承認しました — エスクロから支払いました。",
      t_adv_rejected: "寄付者は前払いを却下しました。",
      t_adv_vote_y: "投票を受け付けました：前払いに賛成。",
      t_adv_vote_n: "投票を受け付けました：前払いに反対。",
      t_vote: "マークしました：この問題、あなたにも迷惑です。",
      t_unvote: "マークを取り消しました。",
      t_geo: "更新しました：近くのプロジェクトを表示します。",
      t_geo_err: "現在地を取得できませんでした。",
      t_published: "プロジェクトを公開しました。地図にあります。",
      t_quest: "応募を送信しました（デモ）。",
      t_contractor: "これからは街のプロジェクトに見積りを出せます。",
      t_reset: "デモデータをリセットしました。",
      joinedAgo: "参加中",
      m: "か月",
      back: "戻る",
      project: "プロジェクト",
      estLabel: "見積もり",
      noOffersYet: "まだ見積もりはありません — 予算は投稿者の見積もりにもとづきます。",
      awaitingOffers: "見積もり待ち",
      chosen: "採用済み",
      emptyWallet: "まだ寄付がありません。近くのプロジェクトを探して応援してください。",
      emptyList: "何も見つかりませんでした。",
      inBudgetsStat: "プロジェクトの予算へ",
      onTheMap: " 件が地図に",
      youDonated: "あなたの寄付 ",
      statQuests: "クエスト",
      statProjects: "プロジェクト",
      statContribs: "回の寄付",
      unitDays: "日",
      unitHours: "時間",
      mUnit: " メートル",
      kmUnit: " キロメートル",
      justNow: "たった今",
      hAgo: " 時間前",
      dAgo: " 日前",
      docTitle: "21.city — 街のプロジェクトとクエスト",
      searchPh: "プロジェクト・タスク・場所…",
      budgetMicro: "寄付はプロジェクトの予算に入り、プラットフォーム手数料ではなく工事に使われます。",
      badAmount: "1 から 1,000,000 までの金額を入力してください",
      confirmReset: "ローカルデータをすべてリセットしますか？先にエクスポートしてください。",
      profileSaved: "プロフィールを保存しました",
      t_demo: "デモ：すべてのデータはこのブラウザ内に保存されます",
      saveError: "データを保存できませんでした。プロフィールからエクスポートしてください。",
      bothersMeToo: "私も迷惑しています",
      bandText: "5 ステップ：問題の写真から公開の領収書まで。隣人が予算に出資し、施工者が見積もりを出し、検収後にエスクロが支払います。",
    },
    ko: {
      newest: "최신순",
      funding: "목표에 가까운 순",
      tabHome: "개요",
      tabMap: "지도",
      tabProjects: "프로젝트",
      tabWallet: "지갑",
      tabProfile: "프로필",
      findProject: "프로젝트 찾기",
      questsNearby: "가까운 퀘스트",
      projectsNearby: "가까운 프로젝트",
      nearbyProjects: "가까운 프로젝트",
      all: "전체",
      projects: "프로젝트",
      quests: "퀘스트",
      forYou: "추천",
      popular: "인기",
      nearby: "가까운",
      projectsTitle: "프로젝트와 퀘스트",
      projectsSub: "사진과 좌표가 있는 도시 문제 — 그리고 이웃의 퀘스트",
      walletTitle: "지갑",
      walletSub: "도시 프로젝트 예산에 대한 당신의 출연",
      inBudgets: "프로젝트 예산에",
      active: "진행 중",
      contributed: "나의 출연",
      completed: "완료",
      you: "나",
      myProjects: "내 프로젝트",
      myQuests: "내 퀘스트",
      wallet: "지갑",
      howWorks: "작동 방식",
      resetDemo: "데모 데이터 초기화",
      addToBudget: "예산에 더하기",
      donate: "후원하기",
      other: "직접 입력",
      yourAmount: "금액, €",
      yourName: "표시할 이름",
      submitOffer: "견적 제출",
      sendOffer: "견적 보내기",
      contractor: "시공업체 / 회사",
      price: "가격, €",
      days: "기간, 일수",
      postNeed: "문제 신고하기",
      whatHappened: "무슨 일이 있었나요",
      desc: "자세히",
      category: "분류",
      publish: "게시",
      place: "장소",
      gotIt: "알겠습니다",
      locate: "내 위치",
      newProblem: "문제 신고하기",
      open: "진행 중",
      viewOnMap: "지도에서 보기",
      details: "자세히",
      offersShort: "견적",
      donationsShort: "후원",
      addBudgetShort: "+ 예산에",
      budgetTitle: "프로젝트 예산",
      of: "/",
      targetMin: "목표 — 최저 견적",
      targetEst: "작성자 예상 — 아직 견적이 없습니다",
      donors: "참여자",
      offersTitle: "업체 견적",
      minPrice: "최저가",
      shortfall: "최저 견적까지 부족",
      canTopUp: "— 작업 중에는 예산을 더 채울 수 있습니다",
      accept: "수락",
      chatTitle: "프로젝트 채팅",
      chatPlaceholder: "메시지…",
      send: "보내기",
      advanceTitle: "자재·작업 선급금",
      requestAdvance: "선급금 요청",
      sendRequest: "요청 보내기",
      advAmount: "선급금 금액, €",
      advReason: "사유",
      advBy: "선급금을 요청했습니다",
      giveAdvance: "선급금 지급",
      declineAdvance: "거부",
      advVotersOnly: "이 프로젝트 후원자만 투표할 수 있습니다",
      advToVote: "얼마든지 후원하면 투표할 수 있습니다",
      advFor: "찬성",
      advAgainst: "반대",
      yourVote: "내 투표",
      advOpenA: "투표함",
      advOpenB: "/ 모인 금액",
      advRule: "후원 금액의 과반수가 필요합니다",
      advApproved: "선급금 승인",
      advRejected: "후원자가 선급금을 거부",
      advPaidNote: "에스크로에서 시공업체에게 지급됨",
      advRestNote: "검수 전까지 에스크로에 보관",
      advReRequest: "다시 요청하기",
      advDemoNote: "시공업체는 선급금을 요청할 수 있습니다 — 사유를 함께",
      timelineTitle: "프로젝트 진행",
      now: "지금",
      stage1: "커뮤니티 지원",
      stage1d: "이웃들이 후원금으로 예산을 채웁니다",
      stage2: "시공업체 찾기",
      stage2d: "견적을 공개 중, 목표는 최저가",
      stage3: "작업 중",
      stage3d: "시공업체 선정 후",
      stage4: "검수",
      stage4d: "확인하고 지불",
      stage5: "완료",
      stage5d: "결과는 공개",
      chainNote: "샌드박스: 단계는 이 브라우저에만 저장됩니다. 에스크로와 지급은 시뮬레이션이며, 블록체인은 연결되지 않았습니다.",
      demoPick: "시공업체 선택 (데모)",
      demoWorkDone: "작업 완료 (데모)",
      demoPay: "확인 후 지급 (데모)",
      budgetReady: "예산이 모였습니다 — 의뢰할 수 있습니다",
      works: "건",
      respond: "응하기",
      responded: "응답을 보냈습니다",
      publishLive: "요청이 게시되었습니다!",
      publishLiveD: "이웃들이 이제 지도에서 보고 도움과 견적을 보낼 수 있습니다.",
      seedDonate: "예산에 €25 추가",
      later: "나중에",
      becomeContractor: "시공업체 되기",
      becomeContractorD: "당신의 기술로 동네를 돕고, 실제 작업에 대한 보상을 받으세요.",
      contractorOn: "시공업체입니다",
      myOffers: "내 견적",
      offersSent: "보낸 견적",
      tasksDone: "완료한 작업",
      earned: "수입",
      pickOnMap: "지도를 눌러 위치를 지정하세요",
      how1t: "1 · 커뮤니티 지원",
      how1d: "누군가 집 앞에서 금 간 보도를 사진으로 남깁니다. 가까운 이웃들이 지도에서 문제를 보고 후원금으로 프로젝트 예산을 채웁니다.",
      how2t: "2 · 시공업체 찾기",
      how2d: "후원이 쌓이는 동안 업체 견적이 들어옵니다. 예산 목표는 가장 낮은 견적입니다.",
      how3t: "3 · 작업",
      how3d: "예산이 모이면 가장 좋은 견적을 고르고 시공업체가 착수합니다. 자재 선급금은 사유와 후원자 투표가 필요합니다.",
      how4t: "4 · 검수",
      how4d: "이웃들이 결과를 확인합니다 — 에스크로가 시공업체에게 지급합니다.",
      how5t: "5 · 완료",
      how5d: "영수증은 공개로 남습니다: 모든 단계가 보이고 돈은 작업에 쓰였습니다.",
      t_donated: "프로젝트 예산에 €+AMOUNT 이 추가되었습니다. 견적을 모으고 작업을 앞당기는 데 도움이 됩니다.",
      t_offer_new_min: "예산 목표가 다시 계산되었습니다: €AMOUNT — 최저 견적입니다.",
      t_offer_added: "견적을 보냈습니다. 프로젝트 입찰에서 모두에게 보입니다.",
      t_accepted: "견적이 수락되었습니다. 작업이 시작됩니다.",
      t_work_done: "작업이 끝났습니다. 검수를 기다립니다.",
      t_paid: "에스크로에서 시공업체에게 지급했습니다. 영수증은 공개입니다.",
      t_adv_requested: "선급금 요청을 후원자에게 보냈습니다.",
      t_adv_approved: "후원자가 선급금을 승인했습니다 — 에스크로에서 지급했습니다.",
      t_adv_rejected: "후원자가 선급금을 거부했습니다.",
      t_adv_vote_y: "투표가 반영되었습니다: 선급금 찬성.",
      t_adv_vote_n: "투표가 반영되었습니다: 선급금 반대.",
      t_vote: "표시했습니다: 이 문제 저도 불편합니다.",
      t_unvote: "표시를 취소했습니다.",
      t_geo: "갱신했습니다: 가까운 프로젝트를 보여줍니다.",
      t_geo_err: "위치를 가져오지 못했습니다.",
      t_published: "프로젝트가 게시되었습니다. 지도에 있습니다.",
      t_quest: "응답을 보냈습니다 (데모).",
      t_contractor: "이제 동네 프로젝트에 견적을 낼 수 있습니다.",
      t_reset: "데모 데이터를 초기화했습니다.",
      joinedAgo: "참여 중",
      m: "개월",
      back: "뒤로",
      project: "프로젝트",
      estLabel: "예상",
      noOffersYet: "아직 견적이 없습니다 — 예산은 작성자의 예상으로 계산합니다.",
      awaitingOffers: "견적 대기 중",
      chosen: "선정됨",
      emptyWallet: "아직 출연이 없습니다. 가까운 프로젝트를 찾아 후원해 보세요.",
      emptyList: "아무것도 찾지 못했습니다.",
      inBudgetsStat: "프로젝트 예산에",
      onTheMap: "건이 지도에",
      youDonated: "후원 금액 ",
      statQuests: "퀘스트",
      statProjects: "프로젝트",
      statContribs: "번 후원",
      unitDays: "일",
      unitHours: "시간",
      mUnit: " m",
      kmUnit: " km",
      justNow: "방금",
      hAgo: " 시간 전",
      dAgo: " 일 전",
      docTitle: "21.city — 가까운 도시 프로젝트와 퀘스트",
      searchPh: "프로젝트, 작업, 장소…",
      budgetMicro: "후원은 프로젝트 예산으로 들어가 플랫폼 수수료가 아니라 작업에 쓰입니다.",
      badAmount: "1에서 1,000,000 사이의 금액을 입력하세요",
      confirmReset: "로컬 데이터를 모두 초기화할까요? 먼저 내보내기를 하세요.",
      profileSaved: "프로필을 저장했습니다",
      t_demo: "데모: 모든 데이터는 이 브라우저에 저장됩니다",
      saveError: "데이터를 저장하지 못했습니다. 프로필에서 내보내세요.",
      bothersMeToo: "저도 불편합니다",
      bandText: "다섯 단계: 문제 사진부터 공개 영수증까지. 이웃들이 예산을 채우고, 업체가 견적을 내며, 검수 후 에스크로가 지급합니다.",
    }
  };

  /* ============================================================ языки */
  /* Шесть языков в разметке и в словаре. Код BCP-47: ru, en, es, zh, ja, ko. */
  var LANGS = [
    { code: "ru", name: "Русский" },
    { code: "en", name: "English" },
    { code: "es", name: "Español" },
    { code: "zh", name: "中文" },
    { code: "ja", name: "日本語" },
    { code: "ko", name: "한국어" }
  ];
  function isLang(l) {
    for (var i = 0; i < LANGS.length; i++) if (LANGS[i].code === l) return true;
    return false;
  }
  function guessLang() {
    var nav = (typeof navigator !== "undefined" && (navigator.language || navigator.userLanguage)) || "";
    var l = String(nav).toLowerCase();
    if (/^(ru|be|uk)/.test(l)) return "ru";
    if (/^(zh|chinese)/.test(l)) return "zh";
    if (/^ja/.test(l)) return "ja";
    if (/^ko/.test(l)) return "ko";
    if (/^es/.test(l)) return "es";
    if (/^en/.test(l)) return "en";
    return "ru";
  }

  var CATS = {
    roads:     { ru: "Дороги", en: "Roads", es: "Vías", zh: "道路", ja: "道路", ko: "도로",     c: "violet" },
    park:      { ru: "Парк", en: "Park", es: "Parque", zh: "公园", ja: "公園", ko: "공원",      c: "teal"   },
    transport: { ru: "Остановки", en: "Stops", es: "Paradas", zh: "站点", ja: "停留所", ko: "정류장",     c: "sky"    },
    bikes:     { ru: "Вело", en: "Bikes", es: "Bicis", zh: "自行车", ja: "自転車", ko: "자전거",     c: "yellow" },
    clean:     { ru: "Уборка", en: "Cleaning", es: "Limpieza", zh: "清洁", ja: "清掃", ko: "청소",  c: "coral"  },
    light:     { ru: "Свет", en: "Lighting", es: "Alumbrado", zh: "照明", ja: "照明", ko: "조명",  c: "pink"   },
    other:     { ru: "Другое", en: "Other", es: "Otros", zh: "其他", ja: "その他", ko: "기타",     c: "mut"    }
  };
  var QCATS = {
    home:      { ru: "Дом и быт", en: "Home & Living", es: "Hogar y día a día", zh: "家居生活", ja: "家庭と生活", ko: "집과 생활", c: "yellow" },
    education: { ru: "Учёба", en: "Education", es: "Estudio", zh: "学习", ja: "学習", ko: "학습",     c: "violet" },
    tech:      { ru: "Техника", en: "Tech", es: "Tecnología", zh: "技术", ja: "技術", ko: "기술",          c: "sky"    },
    pets:      { ru: "Питомцы", en: "Pets", es: "Mascotas", zh: "宠物", ja: "ペット", ko: "반려동물",          c: "coral"  },
    other:     { ru: "Другое", en: "Other", es: "Otros", zh: "其他", ja: "その他", ko: "기타",         c: "mut"    }
  };
  var SKILLS = ["repair", "construction", "carpentry", "painting", "electricity", "cleaning", "garden", "other"];
  var SKILL_LBL = {
    repair: { ru: "Ремонт", en: "Repair", es: "Reparación", zh: "维修", ja: "修理", ko: "수리" }, construction: { ru: "Стройка", en: "Construction", es: "Construcción", zh: "施工", ja: "建築", ko: "건설" },
    carpentry: { ru: "Плотницкое", en: "Carpentry", es: "Carpintería", zh: "木工", ja: "木工", ko: "목공" }, painting: { ru: "Покраска", en: "Painting", es: "Pintura", zh: "粉刷", ja: "塗装", ko: "도장" },
    electricity: { ru: "Электрика", en: "Electricity", es: "Electricidad", zh: "电工", ja: "電気工事", ko: "전기" }, cleaning: { ru: "Уборка", en: "Cleaning", es: "Limpieza", zh: "清洁", ja: "清掃", ko: "청소" },
    garden: { ru: "Сад", en: "Garden", es: "Jardín", zh: "园艺", ja: "庭仕事", ko: "정원" }, other: { ru: "Другое", en: "Other", es: "Otros", zh: "其他", ja: "その他", ko: "기타" }
  };

  function T(k) {
    var d = I18N[state.lang] || I18N.ru;
    if (d[k] != null) return d[k];
    if (I18N.en[k] != null) return I18N.en[k];
    return I18N.ru[k] != null ? I18N.ru[k] : k;
  }
  function loc(obj) {
    if (obj == null) return "";
    if (typeof obj === "string") return obj;
    if (obj[state.lang] != null) return obj[state.lang];
    if (obj.ru != null) return obj.ru;
    if (obj.en != null) return obj.en;
    return "";
  }

  /* ============================================================ seed */
  function seedData() {
    var now = Date.now(), D = 864e5;
    return {
      v: 1, seq: 100,
      lang: guessLang(),
      user: {
        name: "", joined: now - 61 * D, questsDone: 7, contributionsBase: 21,
        contractor: false, skills: [], home: [59.9377, 30.3129]
      },
      myPos: null,
      projects: [
        {
          id: 1, cat: "roads", stage: 1, votes: 12, voted: false, created: now - 5 * D,
          title: { ru: "Ремонт тротуара", en: "Repair the sidewalk", es: "Reparar la acera", zh: "修人行道", ja: "歩道を直す", ko: "보도 고치기" },
          near: { ru: "рядом с домом", en: "near my home", es: "cerca de casa", zh: "就在我家附近", ja: "家の近く", ko: "집 근처" },
          desc: {
            ru: "Плитка треснула и провалилась, после дождя — лужа. Пешеходы обходят по газону, коляски не проехать. Давайте починим вместе.",
             en: "The pavement is broken and dangerous for pedestrians — an accessibility and safety issue. Let’s fix it together.",
             es: "Las baldosas están rajadas y hundidas; después de la lluvia queda un charco. Los peatones rodean por el césped y las sillas de ruedas no pasan. Arreglémoslo juntos.",
             zh: "地砖裂开并塌陷，雨后积水。行人只能绕草坪走，婴儿车过不去。我们一起修好吧。",
             ja: "タイルが割れて沈み、雨のあとは水たまりになります。歩行者は芝生を迂回し、ベビーカーも通れません。一緒に直しましょう。",
             ko: "타일이 깨지고 꺼져서 비 오면 물이 고입니다. 보행자는 잔디를 돌아가고 유모차도 지나가기 어렵습니다. 같이 고쳐 봅시다."
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
              msg: { ru: "Могу приехать на замер в четверг. Материалы считаю по факту, фото до и после пришлю в чат.", en: "I can come to measure on Thursday. Materials billed as used, before/after photos in the chat.", es: "Puedo ir a medir el jueves. Los materiales se facturan según lo usado; mando fotos antes y después en el chat.", zh: "周四我可以上门量尺。材料按实际用量结算，前后照片我会发到聊天里。", ja: "木曜日に測りに伺えます。資材は実使用分で計算し、前後の写真はチャットに送ります。", ko: "목요일에 실측하러 갈 수 있습니다. 자재는 실제 사용량으로 정산하고, 전후 사진은 채팅으로 보내겠습니다." } },
            { id: 12, name: "Асфальт-СПб", rating: 4.6, reviews: 31, jobs: 14, price: 480, days: 5,
              msg: { ru: "Работаем по тарифу, гарантия год. Начнём на следующей неделе.", en: "Fixed price, one-year warranty. We can start next week.", es: "Precio cerrado, un año de garantía. Empezamos la semana que viene.", zh: "按固定价报价，一年保修。下周开工。", ja: "定額で、保証は 1 年。来週から着手します。", ko: "정액 견적으로 보장은 1년. 다음 주부터 시작합니다." } }
          ],
          chat: [
            { them: "Дорожник Пётр", text: { ru: "Здравствуйте! Видел проблему на карте, готов взяться.", en: "Hi! I saw the problem on the map, happy to take it.", es: "¡Hola! He visto el problema en el mapa, me hago cargo.", zh: "你好！我在地图上看到这个问题，我来接。", ja: "こんにちは！地図で問題を見つけました。やらせてください。", ko: "안녕하세요! 지도에서 문제를 봤습니다, 맡겠습니다." }, ts: now - 2 * D },
            { you: true, text: { ru: "Здравствуйте! Когда сможете на замер?", en: "Hi! When can you come to measure?", es: "¡Hola! ¿Cuándo puedes venir a medir?", zh: "你好！您什么时候可以来量尺？", ja: "こんにちは！測りに来るのはいつですか？", ko: "안녕하세요! 언제 실측하러 오시나요?" }, ts: now - 2 * D + 36e5 }
          ],
          contractor: null, advance: null
        },
        {
          id: 2, cat: "bikes", stage: 1, votes: 5, voted: false, created: now - 3 * D,
          title: { ru: "Починить велопарковку", en: "Fix the bike rack", es: "Arreglar el aparcamiento de bicis", zh: "修自行车停放架", ja: "駐輪場の修理", ko: "자전거 거치대 수리" },
          near: { ru: "у подъезда", en: "by the entrance", es: "junto al portal", zh: "单元门口", ja: "エントランス横", ko: "현관 옆" },
          desc: {
            ru: "Разболтало крепления, два крюка погнуты. Велосипеды падают вместе с парковкой.",
             en: "The fixings are loose and two hooks are bent. Bikes keep falling over with the rack.",
             es: "Los anclajes están flojos y dos ganchos doblados. Las bicis se caen con el soporte.",
             zh: "固定件松了，两个挂钩也弯了。自行车停放架一倒，车就跟着摔。",
             ja: "固定が緩んで、フック 2 つが曲がっています。駐輪ごと倒れます。",
             ko: "고정구가 느슨해지고 고리 두 개가 휘었습니다. 자전거가 거치대와 함께 쓰러집니다."
          },
          coords: [59.9421, 30.3245], estimate: 200, photo: "assets/img/projects/bikerack.webp",
          donations: [
            { name: "Сергей", amount: 20, ts: now - 2 * D },
            { you: true, amount: 10, ts: now - 1 * D }
          ],
          offers: [
            { id: 21, name: "СварПром", rating: 4.7, reviews: 22, jobs: 9, price: 180, days: 3,
              msg: { ru: "Сварим на месте, усилим основание. Обойдётся дешевле нового.", en: "We will weld it in place and reinforce the base. Cheaper than a new one.", es: "Lo soldamos aquí y reforzamos la base. Sale más barato que uno nuevo.", zh: "我们上门焊接并加固底座，比换新的便宜。", ja: "現場で溶接し、土台を補強します。新品より安く済みます。", ko: "현장에서 용접하고 밑단을 보강합니다. 새 제품보다 쌉니다." } }
          ],
          chat: [], contractor: null, advance: null
        },
        {
          id: 3, cat: "clean", stage: 1, votes: 8, voted: false, created: now - 2 * D,
          title: { ru: "Убрать сквер после зимы", en: "Clean the park", es: "Limpiar el parque", zh: "清理冬后的街心公园", ja: "冬の後の公園を片付ける", ko: "겨울 지나고 공원 정리하기" },
          near: { ru: "сквер за школой", en: "the yard behind the school", es: "el patio de detrás del colegio", zh: "学校后面的小公园", ja: "学校裏の広場", ko: "학교 뒤 뜰" },
          desc: {
            ru: "Ветви, мусор, песок с дорожек. Хочется сесть на лавочку и не увязнуть в грязи.",
             en: "Branches, litter, sand all over the paths. It would be nice to sit on a bench without stepping into mud.",
             es: "Ramas, basura, arena por los senderos. Da gusto sentarse en un banco sin hundir los pies en el barro.",
             zh: "树枝、垃圾、路上的沙子。真想能坐在长椅上而不会陷进泥里。",
             ja: "枝、ゴミ、道に撒いた砂。ベンチに座って泥に埋まらないようにしたいです。",
             ko: "나뭇가지, 쓰레기, 길에 모래가 잔뜩. 벤치에 앉아 진흙에 빠지지 않게 하고 싶습니다."
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
          title: { ru: "Навес на трамвайной остановке", en: "Solar shelter at the tram stop", es: "Marquesina solar en la parada del tranvía", zh: "有顶候车亭（太阳能照明）", ja: "トラム停留所のソーラーシェルター", ko: "트램 정류장太阳能 쉘터" },
          near: { ru: "остановка у моста", en: "the stop by the bridge", es: "la parada junto al puente", zh: "桥边的车站", ja: "橋のそばの停留所", ko: "다리 옆 정류장" },
          desc: {
            ru: "Стёкол нет, сидений нет, дождь как на улице. Ставим навес со скамейкой и солнечной подсветкой.",
             en: "No glass, no seats, rain gets in. We want a shelter with a bench and a solar light.",
             es: "Sin vidrio, sin asientos, entra la lluvia igual. Queremos una marquesina con banco y luz solar.",
             zh: "没有玻璃，没有座位，下雨跟淋在外面一样。要装一个带长椅和太阳能灯的顶棚。",
             ja: "ガラスも座席もなく、雨は街中で降るのと同じ。ベンチとソーラーライトのあるシェルターを建てます。",
             ko: "유리와 좌석이 없고 비가 밖에서 내리는 것과 같습니다. 벤치와 태양광 조명이 있는 쉘터를 세우겠습니다."
          },
          coords: [59.9475, 30.3238], estimate: 600, photo: "assets/img/projects/shelter.webp",
          donations: [
            { name: "Игорь", amount: 40, ts: now - 6 * D },
            { name: "Лена", amount: 30, ts: now - 4 * D },
            { name: "Марк", amount: 10, ts: now - 3 * D }
          ],
          offers: [
            { id: 41, name: "НавесПро", rating: 4.9, reviews: 17, jobs: 5, price: 520, days: 14,
              msg: { ru: "Поликарбонат, антивандальная скамейка, солнечная лента по краю.", en: "Polycarbonate, an anti-vandal bench, solar strip along the edge.", es: "Policarbonato, banco antivandálico y tira solar en el borde.", zh: "聚碳酸酯板材、防破坏长椅、边缘一圈太阳能灯带。", ja: "ポリカルボネート、耐破壊ベンチ、縁のソーラーストリップ。", ko: "폴리카보네이트, 파손 방지용 벤치, 가장자리의 태양광 스트립." } },
            { id: 42, name: "СтройМастер", rating: 4.5, reviews: 26, jobs: 11, price: 560, days: 10,
              msg: { ru: "Сделаем быстрее, но дороже. Гарантия два года.", en: "Faster but pricier. Two-year warranty.", es: "Más rápido, pero más caro. Dos años de garantía.", zh: "做得更快，但更贵。两年保修。", ja: "早く済みますが、価格は高くなります。保証は 2 年。", ko: "더 빠르지만 더 비쌉니다. 보장은 2년." } }
          ],
          chat: [
            { them: "НавесПро", text: { ru: "КП принято, начинаем в понедельник. Материалы заказываем заранее.", en: "Offer accepted, we start on Monday. Materials are ordered in advance.", es: "Oferta aceptada, empezamos el lunes. Los materiales se piden por adelantado.", zh: "报价已接受，下周一开工。材料提前预订。", ja: "お見積りを受けました。月曜日に着手します。資材は先に手配します。", ko: "견적이 수락되었습니다. 월요일부터 시작하고 자재는 미리 주문합니다." }, ts: now - 2 * D },
            { them: "НавесПро", text: { ru: "Поставщику нужна предоплата 50% за поликарбонат — отправил запрос аванса с обоснованием.", en: "The supplier needs a 50% prepayment for the polycarbonate — I have sent an advance request with a justification.", es: "El proveedor pide un 50% de prepago del policarbonato: he enviado la solicitud de anticipo con su justificación.", zh: "供应商要求对聚碳酸酯板材预付 50%，我已附上理由提交预付款申请。", ja: "サプライヤーはポリカルボネートに 50% の前払いを求めているので、理由付きで前払い申請を出しました。", ko: "공급업체가 폴리카보네이트 선금 50%를 요구해서 사유와 함께 선금 요청을 보냈습니다." }, ts: now - 1 * D }
          ],
          advance: {
            amount: 60, by: "НавесПро", status: "open", ts: now - 1 * D,
            reason: {
              ru: "Закупка поликарбоната и крепежа: поставщик работает по предоплате 50%. Смету приложил в чат, остаток — после приёмки.",
               en: "Polycarbonate and fixings: the supplier requires a 50% prepayment. The itemised quote is in the chat; the rest is paid after acceptance.",
               es: "Compra de policarbonato y herrajes: el proveedor trabaja con un 50% de prepago. Adjunté el presupuesto en el chat; el resto se paga tras la recepción.",
               zh: "采购聚碳酸酯板材和紧固件：供应商按 50% 预付款合作。明细已发在聊天里，余款验收后支付。",
               ja: "ポリカルボネートと金具の仕入れ：サプライヤーは 50% 前払いで対応します。内訳はチャットに送りました。残額は検収後に支払います。",
               ko: "폴리카보네이트와 경첩 자재 구입: 공급업체는 50% 선금 거래입니다. 내역서는 채팅에 올렸고, 잔금은 검수 후 지급합니다."
            },
            votes: [
              { name: "Игорь", amount: 40, yes: true, ts: now - 20 * 36e5 },
              { name: "Лена", amount: 30, yes: false, ts: now - 18 * 36e5 }
            ]
          }
        },
        {
          id: 5, cat: "park", stage: 1, votes: 9, voted: false, created: now - 6 * D,
          title: { ru: "Посадить деревья в сквере", en: "Plant trees in the park", es: "Plantar árboles en el parque", zh: "在街心公园种树", ja: "公園に木を植える", ko: "공원에 나무 심기" },
          near: { ru: "вдоль дорожки", en: "along the path", es: "a lo largo del sendero", zh: "沿着小路", ja: "小道の沿い", ko: "길가 따라" },
          desc: {
            ru: "Три липы и живая изгородь вместо вытоптанной земли. Полив — первые два сезона.",
             en: "Three lindens and a hedge instead of the trampled ground. Watering for the first two seasons.",
             es: "Tres tilos y un seto vivo en lugar del suelo pisado. Riego durante las dos primeras temporadas.",
             zh: "三棵椴树加一道绿篱，代替被踩秃的地面。前两个季节负责浇水。",
             ja: "踏みに荒れた土地の代わりに、並木 3 本と生垣を。最初の 2 季は水遣いをします。",
             ko: "밟혀 다해진 땅 대신 느티나무 세 그루와 울타리. 처음 두 계절은 물을 줍니다."
          },
          coords: [59.9301, 30.3241], estimate: 400, photo: "assets/img/projects/trees.webp",
          donations: [{ name: "Даша", amount: 60, ts: now - 3 * D }],
          offers: [
            { id: 51, name: "ЗелёГрад", rating: 4.8, reviews: 12, jobs: 4, price: 350, days: 7,
              msg: { ru: "Саженцы с комом, приживаемость 90%. Приедем с поливом дважды.", en: "Root-balled saplings, 90% survival. We will come to water twice.", es: "Plantones con cepo, 90% de supervivencia. Iremos dos veces a regar.", zh: "带土球的苗木，成活率 90%。我们会来浇两次水。", ja: "根鉢つきの苗木、生着率 90%。水遣いに 2 度伺います。", ko: "뿌리째苗, 생존율 90%. 물주러 두 번 방문합니다." } }
          ],
          chat: [], contractor: null, advance: null
        }
      ],
      quests: [
        { id: 61, cat: "home", price: 15, hours: 2, coords: [59.935, 30.31], created: now - 1 * D, accepted: false,
          title: { ru: "Помочь перевезти мебель", en: "Help me move furniture", es: "Ayudar a mover muebles", zh: "帮忙搬家具", ja: "家具の運びを手伝ってほしい", ko: "가구 옮기는 걸 도와주세요" } },
        { id: 62, cat: "education", price: 20, hours: 1.5, coords: [59.933, 30.319], created: now - 2 * D, accepted: false,
          title: { ru: "Репетиторство: математика, 9 класс", en: "Tutoring: math (grade 9)", es: "Clases particulares: matemáticas (9.º)", zh: "家教：数学（九年级）", ja: "個人レッスン：数学（中3）", ko: "과외: 수학 (중3)" } },
        { id: 63, cat: "tech", price: 25, hours: 1, coords: [59.947, 30.308], created: now - 12 * 36e5, accepted: false,
          title: { ru: "Починить ноутбук", en: "Fix my laptop", es: "Arreglar mi portátil", zh: "修笔记本电脑", ja: "ノートパソコンを直して", ko: "노트북 고치기" } },
        { id: 64, cat: "pets", price: 12, hours: 1, coords: [59.928, 30.32], created: now - 5 * 36e5, accepted: false,
          title: { ru: "Выгулять собаку", en: "Walk my dog", es: "Pasear a mi perro", zh: "遛狗", ja: "犬の散歩のお手伝い", ko: "내 개 산책시키기" } }
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
      if (!isLang(d.lang)) d.lang = "ru";
      return d;
    } catch (e) { return null; }
  }
  function save() {
    try { localStorage.setItem(LS, JSON.stringify(state)); } catch (e) {
      toast(T("saveError"));
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
    if (km < 1) return Math.max(50, Math.round(km * 1000 / 10) * 10) + T("mUnit");
    return (km < 10 ? Math.round(km * 10) / 10 : Math.round(km)) + T("kmUnit");
  }
  function coordsTxt(c) {
    return c ? c[0].toFixed(4) + ", " + c[1].toFixed(4) : "—";
  }
  function relTime(ts) {
    var d = Date.now() - ts, h = d / 36e5;
    if (h < 1) return T("justNow");
    if (h < 24) return Math.round(h) + T("hAgo");
    return Math.round(h / 24) + T("dAgo");
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
                ? T("targetMin") + ": " + esc(minO.name) + " · " + eur(minO.price) + " · " + minO.days + " " + (T("unitDays"))
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
          '<p class="num">' + eur(q.price) + " · " + q.hours + " " + (T("unitHours")) +
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
        '<p class="num">' + eur(q.price) + " · " + q.hours + " " + (T("unitHours")) +
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
    $("#communityStats").innerHTML = '<div><b>' + state.projects.length + '</b><span>' + T("projects") + '</span></div><div><b>' + eur(total) + '</b><span>' + (T("inBudgetsStat")) + '</span></div>';
    $("#homeQuests").innerHTML = sortedQuests().map(function (q) { return questCard(q, false); }).join("");
    $("#homeProjects").innerHTML = sortedProjects().slice(0, 3)
      .map(function (p) { return projectCard(p, false); }).join("");
  }

  function emptyHtml(msg) {
    return '<div class="empty"><img class="empty__art" src="assets/img/ill-empty.webp" alt="" loading="lazy" width="1408" height="768"><p>' + esc(msg) + "</p></div>";
  }

  function renderMapList() {
    var q = searchQ.trim().toLowerCase();
    var arr = sortedProjects().filter(function (p) {
      if (!q) return true;
      return (loc(p.title) + " " + loc(p.desc) + " " + loc(p.near) + " " + loc(catOf(p))).toLowerCase().indexOf(q) >= 0;
    });
    $("#mapCount").textContent = arr.length ? arr.length + (T("onTheMap")) : "";
    $("#mapList").innerHTML = arr.length
      ? arr.map(function (p) { return projectCard(p, true); }).join("")
      : emptyHtml(T("emptyList"));
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
    $("#projList").innerHTML = out || emptyHtml(T("emptyList"));
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
      }).join("") : emptyHtml(T("emptyWallet"));
      return;
    }
    var flt = wtab === "done"
      ? mine.filter(function (p) { return p.stage >= 5; })
      : mine.filter(function (p) { return p.stage < 5; });
    var out = flt.map(function (p) { return projectCard(p, false); }).join("");
    var box = $("#walletList");
    box.innerHTML = out || emptyHtml(T("emptyWallet"));
    $$(".pcard", box).forEach(function (el) {
      var p = byId(el.getAttribute("data-project"));
      if (!p) return;
      var y = myDonated(p);
      if (y) {
        var tag = document.createElement("p");
        tag.className = "pcard__youdon num";
        tag.textContent = (T("youDonated")) + eur(y);
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
      '<div class="stat3"><b class="num">' + (u.questsDone + state.quests.filter(function (q) { return q.accepted; }).length) + "</b><span>" + (T("statQuests")) + "</span></div>" +
      '<div class="stat3"><b class="num">' + mine.length + "</b><span>" + (T("statProjects")) + "</span></div>" +
      '<div class="stat3"><b class="num">' + (u.contributionsBase + contribs) + "</b><span>" + (T("statContribs")) + "</span></div>";
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
            '<div class="offer__row"><span class="num offer__price">' + eur(o.price) + " · " + o.days + " " + (T("unitDays")) + "</span>" +
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
            (T("bothersMeToo")) + " +" + p.votes + "</button>" +
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
            ? T("targetMin") + ": <b>" + esc(minO.name) + "</b> · " + eur(minO.price) + " · " + minO.days + " " + (T("unitDays"))
            : T("targetEst")) + "</p>" +
          (donorRows ? '<p class="budget__donors"><b>' + T("donors") + ":</b> " + donorRows + "</p>" : "") +
          (p.advance && p.advance.status === "approved"
            ? '<p class="budget__adv num">' + T("advanceTitle") + ": " + eur(p.advance.amount) + " → " + T("advPaidNote") + "</p>"
            : "") +
          '<button class="btn btn--primary btn--wide" type="button" data-donate="' + p.id + '">' + T("addToBudget") + "</button>" +
          '<p class="budget__micro">' +
            T("budgetMicro") + "</p>" +
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
        .addTo(map).bindTooltip(T("you"));
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
    if (!Number.isFinite(amt) || amt > 1000000) { toast(T("badAmount")); return; }
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
      msg: { ru: "Готов выполнить работы. Фото до и после пришлю в чат.", en: "Ready to do the work. I will send before and after photos in the chat.", es: "Listo para hacer el trabajo. Mando fotos antes y después en el chat.", zh: "我来做这件事，前后照片会发到聊天里。", ja: "作業を引き受けます。前後の写真はチャットに送ります。", ko: "작업은 제가 맡겠습니다. 전후 사진은 채팅으로 보내겠습니다." }
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
      created: Date.now(), title: title, near: { ru: "рядом с домом", en: "near my home", es: "cerca de casa", zh: "就在我家附近", ja: "家の近く", ko: "집 근처" },
      desc: $("#nDesc").value.trim() || { ru: "", en: "", es: "", zh: "", ja: "", ko: "" },
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
    home: "21.city", map: { ru: "карта района", en: "the neighbourhood map", es: "el mapa del barrio", zh: "街区地图", ja: "区の地図", ko: "동네 지도" },
    projects: { ru: "проекты и квесты", en: "projects & quests", es: "proyectos y misiones", zh: "项目与任务", ja: "プロジェクトとクエスト", ko: "프로젝트와 퀘스트" },
    wallet: { ru: "кошелёк", en: "wallet", es: "monedero", zh: "钱包", ja: "ウォレット", ko: "지갑" }, profile: { ru: "профиль", en: "profile", es: "perfil", zh: "个人资料", ja: "プロフィール", ko: "프로필" }
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
    if (!isLang(l)) l = "ru";
    state.lang = l;
    var root = document.documentElement;
    root.setAttribute("lang", l);
    root.setAttribute("data-lang", l);
    document.title = T("docTitle");
    $$("[data-set-lang]").forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-set-lang") === l ? "true" : "false");
    });
    var code = $("#langCode");
    if (code) code.textContent = l.toUpperCase();
    $$("[data-i18n]").forEach(function (el) {
      var k = el.getAttribute("data-i18n");
      if (I18N.ru[k] != null) el.textContent = T(k);
    });
    var ms = $("#mapSearch");
    if (ms) ms.placeholder = T("searchPh");
    var menu = $("#langMenu");
    if (menu) menu.open = false;
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
      if (!window.confirm(T("confirmReset"))) return;
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
    $("#profileForm").addEventListener("submit", function (e) { e.preventDefault(); var name = $("#profileNameInput").value.trim(); if (!name) return; state.user.name = name; save(); renderProfile(); toast(T("profileSaved")); });
    $("#btnExport").addEventListener("click", function () {
      var url = URL.createObjectURL(new Blob([JSON.stringify(state, null, 2)], { type: "application/json" }));
      var a = document.createElement("a"); a.href = url; a.download = "21city-backup-" + new Date().toISOString().slice(0,10) + ".json"; a.click(); setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    });
    setTimeout(function () {
      toast(T("t_demo"));
    }, 900);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
