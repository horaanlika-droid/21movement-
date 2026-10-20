/* 21 — small, dependency-free page script.
   Language is not a translation layer: both languages live in the HTML,
   this only flips the attribute the CSS keys on. */
(function () {
  "use strict";

  var root = document.documentElement;
  var STORE = "21.lang";
  var titles = {
    ru: "21 — число это PR, квест это продукт",
    en: "21 — the number is the PR, the quest is the product"
  };
  var descriptions = {
    ru: "21 — число, которое может нарисовать кто угодно, и эскроу-обмен услугами под ним. Заявка на грант Ethereum: минимальный раунд €7 500, моё время в смете, без токена и логотипа.",
    en: "A number anyone can paint, and an escrowed exchange of services under it. An Ethereum grant application with a €7,500 floor, my hours in the budget, no token and no logo."
  };

  function storedLang() {
    try {
      var v = localStorage.getItem(STORE);
      return v === "ru" || v === "en" ? v : null;
    } catch (e) {
      return null;
    }
  }

  function setLang(lang, save) {
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
    if (save) {
      try { localStorage.setItem(STORE, lang); } catch (e) {}
    }
  }

  var initial = storedLang();
  if (!initial) {
    var m = /[?&]lang=(ru|en)\b/.exec(window.location.search);
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
