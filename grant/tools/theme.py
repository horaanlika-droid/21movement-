"""Design system for the 21 grant deck.

Page geometry is 1280 x 720 pt (16:9). All public helpers take a top-left
origin (x, y measured from the top of the page) because that is how the slides
are laid out visually.
"""
import os

from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
A = ASSETS
OUT = os.path.join(os.path.dirname(HERE), "build")
PREVIEW = os.path.join(os.path.dirname(HERE), "preview")

W, H = 1280, 720
M = 76  # outer margin

# ---------------------------------------------------------------- palette
INK = HexColor("#08080A")
INK_SOFT = HexColor("#0C0C0F")
PANEL = HexColor("#111116")
PANEL_2 = HexColor("#16161C")
PANEL_3 = HexColor("#1D1D24")
LINE = HexColor("#2B2B34")
LINE_SOFT = HexColor("#202027")
TXT = HexColor("#F3F1EC")
MUT = HexColor("#8E8E9B")
MUT_DIM = HexColor("#5C5C68")
VIO = HexColor("#8B7CFF")
VIO_DEEP = HexColor("#5343D6")
BLUE = HexColor("#7BA7FF")
SAND = HexColor("#E4D3B2")
MINT = HexColor("#7FDCC0")
ALERT = HexColor("#E58A6B")

PAPER = HexColor("#F2F0EA")
PAPER_2 = HexColor("#E7E3D9")
PAPER_INK = HexColor("#131316")
PAPER_MUT = HexColor("#6C6A62")


def alpha(color, a):
    return Color(color.red, color.green, color.blue, alpha=a)


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
}
R, L, MED, SEMI, BOLD = "Geist", "Geist-Light", "Geist-Med", "Geist-Semi", "Geist-Bold"
MONO, MONO_MED, MONO_SEMI = "Mono", "Mono-Med", "Mono-Semi"


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


def hline(c, x1, y, x2, color=LINE, lw=0.75, dash=None):
    c.saveState()
    if dash:
        c.setDash(dash)
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x1, ty(y), x2, ty(y))
    c.restoreState()


def vline(c, x, y1, y2, color=LINE, lw=0.75, dash=None):
    c.saveState()
    if dash:
        c.setDash(dash)
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x, ty(y1), x, ty(y2))
    c.restoreState()


def text(c, x, y, s, font=R, size=12, color=TXT, tracking=0.0, align="left",
         alpha_=None):
    """Draw a single line. y is the baseline offset from the top."""
    w = sw(s, font, size, tracking)
    if align == "right":
        x -= w
    elif align == "center":
        x -= w / 2
    c.saveState()
    t = c.beginText(x, ty(y))
    t.setFont(font, size)
    t.setFillColor(color if alpha_ is None else alpha(color, alpha_))
    t.setCharSpace(tracking)
    t.textOut(s)
    c.drawText(t)
    c.restoreState()
    return w


def label(c, x, y, s, color=MUT, size=8.6, tracking=1.7, align="left"):
    return text(c, x, y, s.upper(), MONO_MED, size, color, tracking, align)


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


def para(c, x, y, w, s, font=R, size=12, leading=None, color=TXT,
         tracking=0.0, align="left", max_lines=99):
    leading = leading or size * 1.45
    lines = wrap(s, font, size, w, tracking)[:max_lines]
    for i, ln in enumerate(lines):
        text(c, x, y + i * leading, ln, font, size, color, tracking, align)
    return y + len(lines) * leading


def bullets(c, x, y, w, items, font=R, size=11.5, leading=19, color=TXT,
            gap=9, bullet_color=VIO, bullet_char="\u2014"):
    cy = y
    for it in items:
        text(c, x, cy, bullet_char, MONO, size - 1, bullet_color, 0.6)
        end = para(c, x + 16, cy, w - 16, it, font, size, leading, color)
        cy = end + gap
    return cy


# ---------------------------------------------------------------- brand
def diamond(c, x, y, h, color=VIO, outline=False, lw=1.1):
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


def logotype(c, x, y, size, color=TXT, accent=VIO, tracking=-0.04):
    """Wordmark: '21' with a small diamond dot. y = top of the glyphs."""
    tr = tracking * size
    txt = "21"
    c.saveState()
    c.setFillColor(color)
    t = c.beginText(x, ty(y) - size * 0.0)
    t.setFont(BOLD, size)
    t.setCharSpace(tr)
    t.textOut(txt)
    c.drawText(t)
    c.restoreState()
    w = sw(txt, BOLD, size, tr)
    diamond(c, x + w + size * 0.26, y + size * 0.26, size * 0.52, accent)
    return w + size * 0.6


def pill(c, x, y, txt_, fg=TXT, bg=None, stroke=LINE, size=8.6, padx=9,
         h=20, font=MONO_MED, tracking=1.2):
    w = sw(txt_, font, size, tracking) + padx * 2
    if bg is not None:
        rect(c, x, y, w, h, fill=bg, stroke=None, r=h / 2)
    if stroke is not None:
        rect(c, x, y, w, h, fill=None, stroke=stroke, r=h / 2, lw=0.8)
    text(c, x + padx, y + h / 2 + size * 0.34, txt_, font, size, fg, tracking)
    return w


# ---------------------------------------------------------------- images
def photo(c, path, x, y, w, h, r=0, overlay=None, overlay_alpha=0.0):
    from PIL import Image
    iw, ih = Image.open(path).size
    s = max(w / iw, h / ih)
    dw, dh = iw * s, ih * s
    c.saveState()
    p = c.beginPath()
    if r:
        p.roundRect(x, ty(y) - h, w, h, r)
    else:
        p.rect(x, ty(y) - h, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.drawImage(path, x + (w - dw) / 2, ty(y) - h + (h - dh) / 2, dw, dh,
                mask="auto")
    if overlay is not None and overlay_alpha > 0:
        c.setFillColor(alpha(overlay, overlay_alpha))
        c.rect(x, ty(y) - h, w, h, stroke=0, fill=1)
    c.restoreState()


_RAMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build", "ramps")


def _ramp(color, kind, amax, w, h, reverse=False):
    """Cached RGBA gradient tile, used instead of PDF shadings (which ignore
    alpha and would paint opaque blocks over photography)."""
    from PIL import Image
    os.makedirs(_RAMP_DIR, exist_ok=True)
    key = "%s-%s-%.3f-%dx%d-%d" % (color.hexval()[2:], kind, amax, w, h, reverse)
    path = os.path.join(_RAMP_DIR, key + ".png")
    if not os.path.exists(path):
        n = 256
        a = Image.new("L", (n, n))
        px = a.load()
        for yy in range(n):
            for xx in range(n):
                if kind == "v":
                    t = yy / (n - 1)
                elif kind == "h":
                    t = xx / (n - 1)
                else:
                    d = (((xx - n / 2) ** 2 + (yy - n / 2) ** 2) ** 0.5) / (n / 2)
                    t = 1.0 - min(1.0, d)  # brightest at the centre
                if reverse:
                    t = 1 - t
                px[xx, yy] = int(255 * amax * t)
        a = a.resize((max(2, w), max(2, h)), Image.BILINEAR)
        img = Image.new("RGBA", (max(2, w), max(2, h)),
                        (int(color.red * 255), int(color.green * 255),
                         int(color.blue * 255), 0))
        img.putalpha(a)
        img.save(path)
    return path


def glow(c, cx, cy, radius, color=VIO, a=0.16):
    d = int(radius * 2)
    path = _ramp(color, "r", a, d, d)
    c.drawImage(path, cx - radius, ty(cy) - radius, d, d, mask="auto")


def fade(c, x, y, w, h, color=INK, amax=1.0, solid="left"):
    """Solid colour at the `solid` edge, falling to fully transparent at the
    opposite edge."""
    kind = "h" if solid in ("left", "right") else "v"
    # the ramp is opaque at t=1; flip so that `solid` maps to the opaque edge
    reverse = solid in ("left", "top")
    path = _ramp(color, kind, amax, int(w), int(h), reverse)
    c.drawImage(path, x, ty(y) - h, w, h, mask="auto")


def gradient_rect(c, x, y, w, h, color, amax=0.9, solid="bottom"):
    fade(c, x, y, w, h, color, amax, solid)


# ---------------------------------------------------------------- chrome
def page(c, dark=True, grain=None):
    c.setFillColor(INK if dark else PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    if grain:
        c.saveState()
        c.setFillAlpha(0.55)
        c.drawImage(grain, 0, 0, W, H, mask="auto")
        c.restoreState()


def footer(c, idx, section="", dark=True):
    col = MUT_DIM if dark else PAPER_MUT
    hline(c, M, H - 54, W - M, LINE_SOFT if dark else alpha(PAPER_INK, 0.12))
    text(c, M, H - 42, "21  \u2014  Ethereum-native civic infrastructure",
         MONO, 8.4, col, 1.1)
    if section:
        text(c, W / 2, H - 42, section.upper(), MONO, 8.4, col, 1.4, "center")
    text(c, W - M, H - 42, f"{idx:02d} / 20", MONO, 8.4, col, 1.1, "right")


def title_block(c, kicker, headline, sub=None, dark=True, y=None, width=760):
    y = y if y is not None else 122
    col = TXT if dark else PAPER_INK
    mcol = MUT if dark else PAPER_MUT
    label(c, M, y - 26, kicker, VIO if dark else VIO_DEEP)
    end = para(c, M, y + 12, width, headline, MED, 34, 40, col)
    if sub:
        para(c, M, end + 12, width - 40, sub, L, 13, 20, mcol)
    return end


# ---------------------------------------------------------------- grain
def make_grain(path, w=1280, h=720, strength=10, seed=7):
    """Subtle film grain layer, drawn once as a translucent PNG."""
    import random

    from PIL import Image
    random.seed(seed)
    img = Image.new("RGBA", (w, h))
    px = img.load()
    for yy in range(h):
        for xx in range(w):
            v = random.randint(0, 255)
            px[xx, yy] = (v, v, v, random.randint(0, strength))
    img.save(path)
    return path
