"""Design system for the 21 grant deck — ethereum.org-inspired light theme.

Page geometry is 1280 x 720 pt (16:9). All public helpers take a top-left
origin (x, y measured from the top of the page) because that is how the slides
are laid out visually.

The look: warm paper, ink outlines, pastel accents, rounded "sticker" cards with
a hard offset shadow, hand-drawn doodles and flat editorial illustrations. The
illustrations are generated on a #FAF2DE background, which is exactly PAPER, so
they can be dropped on the page without a frame.
"""
import math
import os
from contextlib import contextmanager

from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
ART = os.path.join(os.path.dirname(HERE), "art")
PHOTOS = os.path.join(os.path.dirname(HERE), "photos")
A = ASSETS
OUT = os.path.join(os.path.dirname(HERE), "build")
PREVIEW = os.path.join(os.path.dirname(HERE), "preview")

W, H = 1280, 720
M = 72  # outer margin

# ---------------------------------------------------------------- palette
PAPER = HexColor("#FAF2DE")       # page, identical to the illustration background
PAPER_2 = HexColor("#F2E8D2")     # secondary surface
WHITE = HexColor("#FFFDF7")       # cards
INK = HexColor("#17161B")
INK_SOFT = HexColor("#3C3A44")
MUT = HexColor("#6B675E")
MUT_DIM = HexColor("#9A9487")
LINE = HexColor("#E3D7BC")
LINE_SOFT = HexColor("#EDE3CC")
SHADOW = HexColor("#E7DBC0")

VIOLET = HexColor("#6C24DF")
VIOLET_SOFT = HexColor("#EDE2FF")
VIOLET_DEEP = HexColor("#41128B")
TEAL = HexColor("#12B98A")
TEAL_SOFT = HexColor("#E2FAF1")
YELLOW = HexColor("#F6C445")
YELLOW_SOFT = HexColor("#FFF3C4")
CORAL = HexColor("#F0603F")
CORAL_SOFT = HexColor("#FFE6DE")
SKY = HexColor("#6F9BF5")
SKY_SOFT = HexColor("#E7F0FF")
PINK = HexColor("#FF51BC")
PINK_SOFT = HexColor("#FCE2F1")

# aliases used by older slide code
TXT = INK
PANEL = WHITE
PANEL_2 = PAPER_2
PANEL_3 = LINE_SOFT
MINT = TEAL
SAND = YELLOW
ALERT = CORAL
BLUE = SKY
PAPER_INK = INK
PAPER_MUT = MUT

ACCENTS = (VIOLET, TEAL, CORAL, SKY, PINK)


def alpha(color, a):
    return Color(color.red, color.green, color.blue, alpha=a)


def mix(c1, c2, t):
    return Color(c1.red + (c2.red - c1.red) * t,
                 c1.green + (c2.green - c1.green) * t,
                 c1.blue + (c2.blue - c1.blue) * t)


# ---------------------------------------------------------------- fonts
_FONT_FILES = {
    "Geist": "Geist-Regular.ttf",
    "Geist-Light": "Geist-Light.ttf",
    "Geist-Med": "Geist-Medium.ttf",
    "Geist-Semi": "Geist-SemiBold.ttf",
    "Geist-Bold": "Geist-Bold.ttf",
    "Mono": "GeistMono-Regular.ttf",
    "Mono-Med": "GeistMono-Medium.ttf",
    "Mono-Semi": "GeistMono-SemiBold.ttf",
    "Serif": "InstrumentSerif-Regular.ttf",
    "Serif-It": "InstrumentSerif-Italic.ttf",
}
R, L, MED, SEMI, BOLD = "Geist", "Geist-Light", "Geist-Med", "Geist-Semi", "Geist-Bold"
MONO, MONO_MED, MONO_SEMI = "Mono", "Mono-Med", "Mono-Semi"
SERIF, SERIF_IT = "Serif", "Serif-It"


def register_fonts():
    for name, fn in _FONT_FILES.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, fn)))


# ---------------------------------------------------------------- geometry
def ty(y):
    """top-origin y -> reportlab y"""
    return H - y


def sw(text, font, size, tracking=0.0):
    w = pdfmetrics.stringWidth(text, font, size)
    if tracking and len(text) > 1:
        w += tracking * (len(text) - 1)
    return w


@contextmanager
def rotated(c, cx, cy, deg):
    """Rotate everything drawn inside around a top-origin point."""
    c.saveState()
    c.translate(cx, ty(cy))
    c.rotate(deg)
    c.translate(-cx, -ty(cy))
    yield
    c.restoreState()


# ---------------------------------------------------------------- primitives
def rect(c, x, y, w, h, fill=None, stroke=None, lw=1, r=0, dash=None):
    c.saveState()
    if dash:
        c.setDash(dash)
    if fill is not None:
        c.setFillColor(fill)
    if stroke is not None:
        c.setStrokeColor(stroke)
    c.setLineWidth(lw)
    if r:
        c.roundRect(x, ty(y) - h, w, h, r, stroke=1 if stroke is not None else 0,
                    fill=1 if fill is not None else 0)
    else:
        c.rect(x, ty(y) - h, w, h, stroke=1 if stroke is not None else 0,
               fill=1 if fill is not None else 0)
    c.restoreState()


def hline(c, x1, y, x2, color=LINE, lw=0.9, dash=None):
    c.saveState()
    if dash:
        c.setDash(dash)
    if hasattr(color, "alpha") and color.alpha < 1:
        c.setStrokeAlpha(color.alpha)
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x1, ty(y), x2, ty(y))
    c.restoreState()


def vline(c, x, y1, y2, color=LINE, lw=0.9, dash=None):
    c.saveState()
    if dash:
        c.setDash(dash)
    if hasattr(color, "alpha") and color.alpha < 1:
        c.setStrokeAlpha(color.alpha)
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x, ty(y1), x, ty(y2))
    c.restoreState()


def text(c, x, y, s, font=R, size=12, color=INK, tracking=0.0, align="left"):
    """Draw a single line. y is the baseline offset from the top."""
    w = sw(s, font, size, tracking)
    if align == "right":
        x -= w
    elif align == "center":
        x -= w / 2
    c.saveState()
    if hasattr(color, "alpha") and color.alpha < 1:
        c.setFillAlpha(color.alpha)
    t = c.beginText(x, ty(y))
    t.setFont(font, size)
    t.setFillColor(color)
    t.setCharSpace(tracking)
    t.textOut(s)
    c.drawText(t)
    c.restoreState()
    return w


def label(c, x, y, s, color=MUT, size=8.4, tracking=1.7, align="left"):
    return text(c, x, y, s.upper(), MONO_MED, size, color, tracking, align)


def rtext(c, x, y, parts, size=12, align="left", tracking=0.0):
    """Draw runs with different fonts/colours on one baseline.

    parts = [(txt, font, color), ...] — returns the total width.
    """
    total = sum(sw(t, f, size, tracking) for t, f, _ in parts)
    if align == "right":
        x -= total
    elif align == "center":
        x -= total / 2
    cx = x
    for t, f, col in parts:
        cx += text(c, cx, y, t, f, size, col, tracking)
    return total


def wrap(s, font, size, maxw, tracking=0.0):
    words = s.split()
    lines, cur = [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if sw(trial, font, size, tracking) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def para(c, x, y, w, s, font=R, size=12, leading=None, color=INK,
         tracking=0.0, align="left", max_lines=99):
    leading = leading or size * 1.45
    lines = wrap(s, font, size, w, tracking)[:max_lines]
    for i, ln in enumerate(lines):
        text(c, x, y + i * leading, ln, font, size, color, tracking, align)
    return y + len(lines) * leading


def bullets(c, x, y, w, items, font=R, size=11, leading=17, color=INK,
            gap=9, bullet_color=VIOLET, bullet_char="\u2014"):
    cy = y
    for it in items:
        text(c, x, cy, bullet_char, MONO, size - 1, bullet_color, 0.6)
        end = para(c, x + 16, cy, w - 16, it, font, size, leading, color)
        cy = end + gap
    return cy


# ---------------------------------------------------------------- brand
def diamond(c, x, y, h, color=VIOLET, outline=False, lw=1.1):
    """Ethereum-style diamond, h = total height, anchored at top-center."""
    w = h * 0.62
    cx = x
    top = ty(y)
    mid = top - h * 0.62
    bot = top - h
    p = c.beginPath()
    p.moveTo(cx, top)
    p.lineTo(cx + w / 2, mid)
    p.lineTo(cx, bot)
    p.lineTo(cx - w / 2, mid)
    p.close()
    c.saveState()
    if outline:
        c.setStrokeColor(color)
        c.setLineWidth(lw)
        c.drawPath(p, stroke=1, fill=0)
    else:
        c.setFillColor(color)
        c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


def logotype(c, x, y, size, color=INK, accent=VIOLET, tracking=-0.04):
    """Wordmark: '21' with a small diamond dot. y = baseline of the glyphs."""
    tr = tracking * size
    txt = "21"
    c.saveState()
    c.setFillColor(color)
    t = c.beginText(x, ty(y))
    t.setFont(BOLD, size)
    t.setCharSpace(tr)
    t.textOut(txt)
    c.drawText(t)
    c.restoreState()
    w = sw(txt, BOLD, size, tr)
    diamond(c, x + w + size * 0.24, y - size * 0.24, size * 0.5, accent)
    return w + size * 0.6


# ---------------------------------------------------------------- cards & stickers
def card(c, x, y, w, h, fill=WHITE, stroke=LINE, r=16, lw=1, shadow=True,
         shadow_dy=5, shadow_color=None, dash=None):
    if shadow:
        rect(c, x, y + shadow_dy, w, h, fill=shadow_color or SHADOW, r=r)
    rect(c, x, y, w, h, fill=fill, stroke=stroke, r=r, lw=lw, dash=dash)


def chip(c, x, y, txt_, fg=INK, bg=None, stroke=None, size=8.2, h=20, padx=10,
         font=MONO_MED, tracking=0.6, rot=0, shadow=False):
    w = sw(txt_, font, size, tracking) + padx * 2
    if rot:
        with rotated(c, x + w / 2, y + h / 2, rot):
            return chip(c, x, y, txt_, fg, bg, stroke, size, h, padx, font,
                        tracking, 0, shadow)
    if shadow:
        rect(c, x, y + 2.5, w, h, fill=SHADOW, r=h / 2)
    if bg is not None:
        rect(c, x, y, w, h, fill=bg, stroke=stroke, r=h / 2, lw=0.9)
    elif stroke is not None:
        rect(c, x, y, w, h, fill=None, stroke=stroke, r=h / 2, lw=0.9)
    text(c, x + padx, y + h / 2 + size * 0.35, txt_, font, size, fg, tracking)
    return w


def badge(c, cx, cy, r, s, fill=VIOLET, fg=WHITE, size=None, font=MED, rot=0):
    """Round sticker with a number or a short glyph."""
    size = size or r * 0.95
    if rot:
        with rotated(c, cx, cy, rot):
            badge(c, cx, cy, r, s, fill, fg, size, font)
        return
    c.saveState()
    c.setFillColor(SHADOW)
    c.circle(cx + 1, ty(cy + 2.5), r, stroke=0, fill=1)
    c.setFillColor(fill)
    c.circle(cx, ty(cy), r, stroke=0, fill=1)
    c.restoreState()
    text(c, cx, cy + size * 0.35, s, font, size, fg, 0, "center")


def sparkle(c, x, y, s, color=YELLOW):
    """Four-point doodle star, anchored at its centre."""
    p = c.beginPath()
    p.moveTo(x, ty(y) - s)
    p.curveTo(x + s * 0.12, ty(y) - s * 0.16, x + s * 0.16, ty(y) - s * 0.12,
              x + s, ty(y))
    p.curveTo(x + s * 0.16, ty(y) + s * 0.12, x + s * 0.12, ty(y) + s * 0.16,
              x, ty(y) + s)
    p.curveTo(x - s * 0.12, ty(y) + s * 0.16, x - s * 0.16, ty(y) + s * 0.12,
              x - s, ty(y))
    p.curveTo(x - s * 0.16, ty(y) - s * 0.12, x - s * 0.12, ty(y) - s * 0.16,
              x, ty(y) - s)
    p.close()
    c.saveState()
    c.setFillColor(color)
    c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


def squiggle(c, x, y, w, color=VIOLET, amp=2.4, lw=1.6, waves=None):
    """Hand-drawn wavy underline."""
    waves = waves or max(2, int(w / 16))
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.setLineCap(1)
    p = c.beginPath()
    p.moveTo(x, ty(y))
    step = w / waves
    for i in range(waves):
        x0 = x + i * step
        p.curveTo(x0 + step * 0.3, ty(y - amp), x0 + step * 0.7, ty(y + amp),
                  x0 + step, ty(y))
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def marker(c, x, y, w, h=10, color=YELLOW, a=0.55):
    """Highlighter band behind a word. Draw before the text."""
    c.saveState()
    c.setFillColor(alpha(color, a))
    c.roundRect(x, ty(y), w, h, h / 2, stroke=0, fill=1)
    c.restoreState()


def underline_hand(c, x, y, w, color=VIOLET):
    squiggle(c, x, y, w, color, 2.2, 1.5)


def tape(c, cx, cy, w=56, h=18, rot=-6, color=None):
    """Semi-transparent washi tape strip."""
    color = color or alpha(YELLOW, 0.65)
    with rotated(c, cx, cy, rot):
        rect(c, cx - w / 2, cy - h / 2, w, h, fill=color, r=2)


def doodle_arrow(c, x1, y1, x2, y2, color=INK, lw=1.4, curve=0.18):
    """Loose curved arrow, used sparingly to point at things."""
    c.saveState()
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.setLineCap(1)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    nx, ny = -(y2 - y1), (x2 - x1)
    ln = math.hypot(nx, ny) or 1
    cx, cy = mx + nx / ln * ln * curve, my + ny / ln * ln * curve
    p = c.beginPath()
    p.moveTo(x1, ty(y1))
    p.curveTo(cx, ty(cy), cx, ty(cy), x2, ty(y2))
    c.drawPath(p, stroke=1, fill=0)
    ang = math.atan2(y2 - cy, x2 - cx)
    for s in (0.5, -0.5):
        c.line(x2, ty(y2), x2 - 7 * math.cos(ang + s), ty(y2) - 7 * math.sin(ang + s))
    c.restoreState()


# ---------------------------------------------------------------- images
def photo(c, path, x, y, w, h, r=12, border=None, bw=5, shadow=False):
    """Cover-cropped photo with rounded corners, optional white border/shadow."""
    from PIL import Image
    iw, ih = Image.open(path).size
    s = max(w / iw, h / ih)
    dw, dh = iw * s, ih * s
    if border is not None:
        rect(c, x - bw, y - bw, w + bw * 2, h + bw * 2, fill=border,
             r=r + bw if r else 0)
    if shadow:
        rect(c, x + 1, y + 5, w, h, fill=SHADOW, r=r)
    c.saveState()
    p = c.beginPath()
    if r:
        p.roundRect(x, ty(y) - h, w, h, r)
    else:
        p.rect(x, ty(y) - h, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.drawImage(path, x + (w - dw) / 2, ty(y) - h + (h - dh) / 2, dw, dh,
                mask="auto")
    c.restoreState()


def illustration(c, path, x, y, w, h=None, r=0):
    """Flat illustration on the paper background; no frame needed."""
    from PIL import Image
    iw, ih = Image.open(path).size
    h = h or w * ih / iw
    c.saveState()
    if r:
        p = c.beginPath()
        p.roundRect(x, ty(y) - h, w, h, r)
        c.clipPath(p, stroke=0, fill=0)
    c.drawImage(path, x, ty(y) - h, w, h, mask="auto")
    c.restoreState()
    return h


def polaroid(c, path, x, y, w, h, pad=9, cap=None, rot=0, shadow=True,
             cap_h=None, r=10):
    """White-framed photo with a mono caption underneath, stuck on at an angle."""
    cap_h = cap_h if cap_h is not None else (24 if cap else 0)
    total_w, total_h = w + pad * 2, h + pad * 2 + cap_h
    cx, cy = x + total_w / 2, y + total_h / 2
    with rotated(c, cx, cy, rot):
        card(c, x, y, total_w, total_h, fill=WHITE, stroke=LINE, r=6,
             lw=0.9, shadow=shadow, shadow_dy=6)
        photo(c, path, x + pad, y + pad, w, h, r=r)
        if cap:
            text(c, x + pad + 2, y + pad + h + cap_h * 0.68, cap, MONO, 7.6,
                 MUT, 0.3)
    return total_w, total_h


def phone_shot(c, path, x, y, w, h, rot=0, shadow=True, caption=None,
               time_="14:32"):
    """An iPhone-shaped frame around a photo: reads instantly as a phone snap."""
    body_r = w * 0.13
    with rotated(c, x + w / 2, y + h / 2, rot):
        if shadow:
            rect(c, x + 2, y + 7, w, h, fill=SHADOW, r=body_r)
        rect(c, x, y, w, h, fill=INK, r=body_r)
        photo(c, path, x + 5, y + 5, w - 10, h - 10, r=body_r - 4)
        # status bar + notch
        rect(c, x + w / 2 - 16, y + 9, 32, 7, fill=INK, r=4)
        text(c, x + 14, y + 19, time_, MONO_MED, 5.4, WHITE, 0.2)
        text(c, x + w - 14, y + 19, "5G", MONO_MED, 5.4, WHITE, 0.2, "right")
        # camera button hint
        rect(c, x - 3.5, y + h * 0.28, 2.5, 22, fill=INK, r=1.2)
        rect(c, x - 3.5, y + h * 0.28 + 28, 2.5, 34, fill=INK, r=1.2)
        if caption:
            text(c, x, y + h + 15, caption, MONO, 7.4, MUT, 0.2)


# ---------------------------------------------------------------- chrome
def page(c, bg=PAPER, grain=None):
    c.setFillColor(bg)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    if grain:
        c.saveState()
        c.setFillAlpha(0.25)
        c.drawImage(grain, 0, 0, W, H, mask="auto")
        c.restoreState()


def footer(c, idx, section=""):
    hline(c, M, H - 46, W - M, alpha(INK, 0.10))
    text(c, M, H - 34, "21  \u2014  Ethereum-native civic infrastructure",
         MONO, 8, MUT_DIM, 0.8)
    if section:
        text(c, W / 2, H - 34, section.upper(), MONO, 8, MUT_DIM, 1.2, "center")
    text(c, W - M, H - 34, f"{idx:02d} / 20", MONO, 8, MUT_DIM, 0.8, "right")


def head(c, kicker, title, sub=None, width=960, subw=660, y=112, size=38,
         leading=42):
    label(c, M, 60, kicker, VIOLET, 8.4, 1.8)
    end = para(c, M, y, width, title, MED, size, leading, INK, -0.5)
    if sub:
        end = para(c, M, end + 4, subw, sub, R, 11.6, 17, MUT)
    return end


# ---------------------------------------------------------------- grain
def make_grain(path, w=1280, h=720, strength=7, seed=7):
    """Very subtle paper grain overlay."""
    import random

    from PIL import Image
    random.seed(seed)
    img = Image.new("RGBA", (w, h))
    px = img.load()
    for yy in range(h):
        for xx in range(w):
            v = random.randint(90, 190)
            px[xx, yy] = (v, v, v, random.randint(0, strength))
    img.save(path)
    return path
