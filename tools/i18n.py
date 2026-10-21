#!/usr/bin/env python3
"""Языковая оснастка 21.city.

Разметка хранит все языки прямо в HTML: <span lang="ru">…</span><span lang="en">…</span>.
Чтобы добавить язык, нужно развернуть такие пары в шесть копий. Этот скрипт
делает это механически, чтобы переводы не приходилось вставлять руками.

    python3 tools/i18n.py extract          # собрать каталог пар из HTML
    python3 tools/i18n.py apply            # развернуть пары по файлам перевода
    python3 tools/i18n.py check            # только проверить, что всё переведено

Файлы перевода: tools/i18n/<страница>.<язык>.json — массив объектов
{"ru": "исходный русский текст", "t": "перевод"}. Порядок и текст «ru»
сверяются с каталогом, поэтому перевод не может «съехать» на соседний блок.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I18N_DIR = os.path.join(ROOT, "tools", "i18n")

PAGES = [
    ("index", "index.html"),
    ("landing", "landing.html"),
]

# Языки, которые живут в разметке. Первый — язык по умолчанию.
LANGS = ["ru", "en", "es", "zh", "ja", "ko"]

PAIR = re.compile(
    r'<span lang="ru">(.*?)</span>\s*<span lang="en">(.*?)</span>', re.S
)


def page_pairs(path):
    with open(path, encoding="utf-8") as fh:
        html = fh.read()
    return html, PAIR.findall(html)


def catalog_path(name):
    return os.path.join(I18N_DIR, name + ".catalog.json")


def translation_path(name, lang):
    return os.path.join(I18N_DIR, "%s.%s.json" % (name, lang))


def cmd_extract():
    os.makedirs(I18N_DIR, exist_ok=True)
    for name, rel in PAGES:
        path = os.path.join(ROOT, rel)
        html, pairs = page_pairs(path)
        catalog = [{"ru": ru, "en": en} for ru, en in pairs]
        with open(catalog_path(name), "w", encoding="utf-8") as fh:
            json.dump(catalog, fh, ensure_ascii=False, indent=2)
        # уже развёрнутые файлы не трогаем, но предупреждаем
        print("%-8s %3d пар → %s" % (name, len(pairs), os.path.relpath(catalog_path(name), ROOT)))


def load_translations(name, lang, catalog):
    path = translation_path(name, lang)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if len(data) != len(catalog):
        raise SystemExit(
            "%s.%s.json: %d записей, а в каталоге %d — пересоберите перевод"
            % (name, lang, len(data), len(catalog))
        )
    for i, (item, src) in enumerate(zip(data, catalog)):
        if item.get("ru") != src["ru"]:
            raise SystemExit(
                "%s.%s.json: запись %d не совпадает с каталогом\n  в каталоге: %r\n  в файле:    %r"
                % (name, lang, i, src["ru"], item.get("ru"))
            )
        if not str(item.get("t", "")).strip():
            raise SystemExit("%s.%s.json: запись %d пуста" % (name, lang, i))
    return [item["t"] for item in data]


def cmd_apply():
    for name, rel in PAGES:
        path = os.path.join(ROOT, rel)
        with open(catalog_path(name), encoding="utf-8") as fh:
            catalog = json.load(fh)
        html, pairs = page_pairs(path)
        if len(pairs) != len(catalog):
            raise SystemExit(
                "%s: в разметке %d пар, а в каталоге %d — сначала extract" % (rel, len(pairs), len(catalog))
            )
        translations = {}
        for lang in LANGS:
            if lang in ("ru", "en"):
                continue
            tr = load_translations(name, lang, catalog)
            if tr is None:
                raise SystemExit("нет файла перевода: %s" % os.path.relpath(translation_path(name, lang), ROOT))
            translations[lang] = tr

        it = iter(range(len(catalog)))

        def repl(match):
            i = next(it)
            ru, en = match.group(1), match.group(2)
            out = ['<span lang="ru">%s</span>' % ru, '<span lang="en">%s</span>' % en]
            for lang in LANGS:
                if lang in ("ru", "en"):
                    continue
                out.append('<span lang="%s">%s</span>' % (lang, translations[lang][i]))
            return "".join(out)

        new_html = PAIR.sub(repl, html)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_html)
        print("%-8s развёрнуто пар: %d → %d языков" % (name, len(catalog), len(LANGS)))


def cmd_check():
    ok = True
    for name, rel in PAGES:
        with open(catalog_path(name), encoding="utf-8") as fh:
            catalog = json.load(fh)
        for lang in LANGS:
            if lang in ("ru", "en"):
                continue
            try:
                load_translations(name, lang, catalog)
            except SystemExit as exc:
                ok = False
                print("✗ %s" % exc)
    print("все переводы на месте" if ok else "есть пробелы в переводах")
    return 0 if ok else 1


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "extract":
        cmd_extract()
    elif cmd == "apply":
        cmd_apply()
    elif cmd == "check":
        sys.exit(cmd_check())
    else:
        raise SystemExit("команда: extract | apply | check")
