/* 21 — small, dependency-free page script.
   Language is not a translation layer: all six languages live in the HTML,
   this only flips the attribute the CSS keys on. */
(function () {
  "use strict";

  var root = document.documentElement;
  var STORE = "21.lang";
  var LANGS = ["ru", "en", "es", "zh", "ja", "ko"];
  var titles = {
    ru: "21 — число это PR, квест это продукт",
    en: "21 — the number is the PR, the quest is the product",
    es: "21 — el número es PR, la misión es el producto",
    zh: "21 —— 数字就是公关，任务才是产品",
    ja: "21 —— 数字が PR、クエストがプロダクト",
    ko: "21 —— 숫자가 PR, 퀘스트가 제품"
  };
  var descriptions = {
    ru: "21 — число, которое может нарисовать кто угодно, и эскроу-обмен услугами под ним. Заявка на грант Ethereum: минимальный раунд €7 500, моё время в смете, без токена и логотипа.",
    en: "A number anyone can paint, and an escrowed exchange of services under it. An Ethereum grant application with a €7,500 floor, my hours in the budget, no token and no logo.",
    es: "Un número que cualquiera puede pintar y un intercambio de servicios en escrow bajo él. Una solicitud de subsidy de Ethereum con un mínimo de 7.500 €, mis horas en el presupuesto, sin token ni logo.",
    zh: "一个谁都能画出来的数字，以及它下面以托管为保障的服务交换。一份 Ethereum 资助申请：门槛 €7,500，工时计入预算，没有代币，也没有标识。",
    ja: "誰でも描ける数字と、その下にあるエスクロ付きサービス交換。Ethereum グラント申請：下限 7,500 €、工数を予算に計上、トークンもロゴもなし。",
    ko: "누구나 그릴 수 있는 숫자와 그 아래의 에스크로 서비스 교환. Ethereum 보조금 신청: 하한 €7,500, 제 시간은 예산에 반영, 토큰도 로고도 없습니다."
  };

  function isLang(l) { return LANGS.indexOf(l) >= 0; }

  function storedLang() {
    try {
      var v = localStorage.getItem(STORE);
      return isLang(v) ? v : null;
    } catch (e) {
      return null;
    }
  }

  function setLang(lang, save) {
    if (!isLang(lang)) lang = "ru";
    root.setAttribute("lang", lang);
    root.setAttribute("data-lang", lang);
    document.title = titles[lang];
    var meta = document.querySelector('meta[name="description"]');
    if (meta) meta.setAttribute("content", descriptions[lang]);
    var buttons = document.querySelectorAll("[data-set-lang]");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].setAttribute(
        "aria-pressed",
        buttons[i].getAttribute("data-set-lang") === lang ? "true" : "false"
      );
    }
    var code = document.getElementById("langCode");
    if (code) code.textContent = lang.toUpperCase();
    var menu = document.getElementById("langMenu");
    if (menu) menu.open = false;
    if (save) {
      try { localStorage.setItem(STORE, lang); } catch (e) {}
    }
  }

  var initial = storedLang();
  if (!initial) {
    var m = /[?&]lang=(ru|en|es|zh|ja|ko)\b/.exec(window.location.search);
    if (m) initial = m[1];
  }
  if (initial) setLang(initial, false);

  document.addEventListener("click", function (event) {
    var btn = event.target.closest && event.target.closest("[data-set-lang]");
    if (!btn) return;
    setLang(btn.getAttribute("data-set-lang"), true);
  });

  /* Reveal sections as they enter. Content is never hidden without JS:
     the .js class gates the initial opacity in the stylesheet. */
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var items = document.querySelectorAll(".reveal");

  if (!("IntersectionObserver" in window) || reduce) {
    for (var j = 0; j < items.length; j++) items[j].classList.add("is-in");
    return;
  }

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        io.unobserve(entry.target);
      });
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
  );

  for (var k = 0; k < items.length; k++) io.observe(items[k]);
})();
