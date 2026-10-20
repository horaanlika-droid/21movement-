# Fonts

Self-hosted `woff2`, subset for this page (Latin + the Cyrillic the Russian copy
uses). All families are under the **SIL Open Font License 1.1**; the copyright
stays with their authors.

| File | Family | Source | Used for |
|---|---|---|---|
| `geist-regular/medium/semibold/bold.woff2` | Geist | Vercel — <https://github.com/vercel/geist-font> | body, headings |
| `mono-regular/medium.woff2` | Geist Mono | Vercel | labels, figures, tables |
| `gaegu-400/700.woff2` | Gaegu | Kwon Sora / Google Fonts — <https://fonts.google.com/specimen/Gaegu> | every number: the childlike hand |
| `pangolin-latin.woff2`, `pangolin-cyrillic.woff2` | Pangolin | Google Fonts — <https://fonts.google.com/specimen/Pangolin> | handwritten notes, captions, quotes |

Notes:

- Gaegu is Latin + digits only. It has no `€`, `₽`, `×` or em dash, and no
  Cyrillic; those characters fall back to Pangolin (both are hands, so the
  fallback stays in the same voice).
- The subsets keep `U+0000–00FF`, `U+0400–045F`, punctuation, `€`, `₽`, `№` and
  arrows. If a new string needs a glyph outside that, re-subset instead of
  adding a second font.
- Not here on purpose: no webfont CDN. The page makes no third-party request.

## Rebuilding a subset

```bash
pip install fonttools brotli
python3 - <<'PY'
from fontTools.ttLib import TTFont
from fontTools import subset
UNI = "U+0000-00FF,U+0400-045F,U+2000-206F,U+20AC,U+20BD,U+2116,U+2190-2193,U+2212"
f = TTFont("source.ttf")
o = subset.Options(); o.flavor = "woff2"; o.layout_features = ["*"]
o.name_IDs = ["*"]; o.name_legacy = True; o.name_languages = ["*"]
s = subset.Subsetter(options=o); s.populate(unicodes=subset.parse_unicodes(UNI)); s.subset(f)
f.flavor = "woff2"; f.save("out.woff2")
PY
```

Only what the page actually sets is shipped: the serif accent used in the deck
(Instrument Serif) is not here because the handwriting took its place.

The Gaegu and Pangolin files came from the `@fontsource` npm packages (the
Google Fonts download endpoint is not always reachable from CI); the Geist and
Instrument files came from the grant deck's `grant/tools/fonts/` TTFs.
