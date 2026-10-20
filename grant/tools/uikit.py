"""UI kit helpers for the 21 grant deck — light, friendly, hand-built."""
import math
import random

from reportlab.lib.colors import HexColor

import theme as T
from theme import (CORAL, CORAL_SOFT, INK, LINE, LINE_SOFT, MED, MONO, MONO_MED,
                   MUT, MUT_DIM, PAPER, PAPER_2, PINK, SKY, SKY_SOFT, TEAL,
                   TEAL_SOFT, VIOLET, VIOLET_SOFT, WHITE, YELLOW, YELLOW_SOFT,
                   alpha, card, chip, hline, label, photo, rect, sw, text, ty)

INK_SOFT = T.INK_SOFT


def head(c, kicker, title, sub=None, width=1020, subw=700):
    return T.head(c, kicker, title, sub, width, subw)


def badge(c, cx, cy, r, s, fill=VIOLET, fg=WHITE, size=None, font=MED, rot=0):
    return T.badge(c, cx, cy, r, s, fill, fg, size, font, rot)


def kv(c, x, y, k, v, w=150, vfont=MED, vsize=12, ksize=7.8):
    label(c, x, y, k, MUT_DIM, ksize, 1.4)
    text(c, x, y + 19, v, vfont, vsize, INK, 0.05)


def stat(c, x, y, big, small, color=INK, size=26, w=200):
    text(c, x, y + size * 0.78, big, MED, size, color, -0.6)
    T.para(c, x, y + size * 0.78 + 18, w, small, T.R, 9.4, 12.5, MUT, max_lines=3)


def progress(c, x, y, w, pct, h=5, color=VIOLET, track=LINE_SOFT):
    rect(c, x, y, w, h, fill=track, r=h / 2)
    if pct > 0:
        rect(c, x, y, max(h, w * pct), h, fill=color, r=h / 2)


def dot(c, x, y, r, fill=VIOLET, ring=None, ring_w=1.0):
    c.saveState()
    c.setFillColor(fill)
    c.circle(x, ty(y), r, stroke=0, fill=1)
    if ring is not None:
        c.setStrokeColor(ring)
        c.setLineWidth(ring_w)
        c.circle(x, ty(y), r, stroke=1, fill=0)
    c.restoreState()


def avatar(c, x, y, r, initials, bg=VIOLET_SOFT, fg=VIOLET, size=None):
    c.saveState()
    c.setFillColor(bg)
    c.circle(x, ty(y), r, stroke=0, fill=1)
    c.restoreState()
    text(c, x, y + (size or r * 0.62), initials, MONO_MED, size or r * 0.85,
         fg, 0.2, "center")


def browser(c, x, y, w, h, url="21.city/explore", chrome_h=24):
    """Light browser window."""
    card(c, x, y, w, h, fill=WHITE, stroke=LINE, r=12, lw=1, shadow=True,
         shadow_dy=5)
    rect(c, x, y, w, chrome_h, fill=PAPER_2, r=12)
    rect(c, x, y + chrome_h / 2, w, chrome_h / 2, fill=PAPER_2)
    for i, col in enumerate((CORAL, YELLOW, TEAL)):
        dot(c, x + 15 + i * 10, y + chrome_h / 2, 2.6, col)
    pill_w = w * 0.54
    px = x + (w - pill_w) / 2
    rect(c, px, y + 5, pill_w, chrome_h - 10, fill=WHITE, stroke=LINE_SOFT, r=7)
    text(c, px + 9, y + chrome_h / 2 + 2.6, url, MONO, 6.4, MUT_DIM, 0.2)
    hline(c, x, y + chrome_h, x + w, LINE, 0.8)
    return chrome_h


def phone(c, x, y, w=150, h=300, rot=0, shadow=True):
    """Empty phone body; returns the inner screen rect."""
    with T.rotated(c, x + w / 2, y + h / 2, rot) if rot else _null():
        if shadow:
            rect(c, x + 2, y + 7, w, h, fill=T.SHADOW, r=w * 0.13)
        rect(c, x, y, w, h, fill=INK, r=w * 0.13)
        rect(c, x + 5, y + 5, w - 10, h - 10, fill=WHITE, r=w * 0.11)
        rect(c, x + w / 2 - 17, y + 9, 34, 7, fill=INK, r=4)
    return x + 5, y + 5, w - 10, h - 10


class _null:
    def __enter__(self):
        return None

    def __exit__(self, *a):
        return False


def window_content(c, x, y, w, h, kind):
    """Miniature app screens for the product gallery (fit a 356 x 150 frame)."""
    rect(c, x, y - 6, w, 6, fill=WHITE)
    if kind == "map":
        rect(c, x, y, w, 24, fill=WHITE)
        text(c, x + 10, y + 15.5, "Explore", MED, 8.4, INK)
        chip(c, x + 54, y + 5, "24 OPEN", VIOLET, VIOLET_SOFT, None, 5.2, 14, 6)
        chip(c, x + w - 48, y + 5, "All", MUT, PAPER_2, LINE_SOFT, 5.2, 14, 6)
        map_mock(c, x, y + 24, w, h - 24, compact=True, labels=False,
                 markers=[(0.22, 0.30, "", VIOLET), (0.44, 0.62, "", TEAL),
                          (0.68, 0.36, "", CORAL), (0.84, 0.72, "", VIOLET)])
        card(c, x + 8, y + h - 46, 156, 38, fill=WHITE, stroke=LINE, r=8, lw=0.8)
        text(c, x + 16, y + h - 28, "Broken bench \u00b7 420", MED, 6.6, INK)
        text(c, x + 16, y + h - 17, "\u20ac362 raised \u00b7 41 people", MONO, 5.2, MUT, 0.2)
    elif kind == "project":
        photo(c, T.PHOTOS + "/bench-fixed.jpg", x, y, w * 0.46, h,
              r=0)
        px = x + w * 0.46 + 9
        text(c, px, y + 16, "Bench, Oosterpark", MED, 7.6, INK)
        label(c, px, y + 27, "Amsterdam \u00b7 14 mar", MUT_DIM, 4.8, 0.7)
        progress(c, px, y + 36, w * 0.54 - 20, 0.86, 3)
        text(c, px, y + 48, "\u20ac362 of \u20ac420  \u00b7  41 supporters", MONO, 5.2, INK)
        for i, (s_, col) in enumerate((("Milestone 1 \u00b7 site prep", TEAL),
                                       ("Milestone 2 \u00b7 re-fix + paint", YELLOW))):
            card(c, px, y + 57 + i * 22, w * 0.54 - 20, 17, fill=PAPER, stroke=LINE_SOFT,
                 r=4, lw=0.7, shadow=False)
            dot(c, px + 7, y + 65.5 + i * 22, 1.9, col)
            text(c, px + 13, y + 68 + i * 22, s_, T.R, 5.1, MUT)
        text(c, px, y + 116, "\u2713 Verified evidence attached", MONO, 5.1, TEAL, 0.2)
    elif kind == "report":
        rect(c, x, y, w, 24, fill=WHITE)
        text(c, x + 10, y + 15.5, "Report a problem", MED, 8.4, INK)
        rect(c, x + 10, y + 28, w - 20, 42, fill=PAPER, stroke=LINE_SOFT, r=7, lw=0.7)
        chip(c, x + 20, y + 41, "+  TAKE PHOTO", VIOLET, VIOLET_SOFT, None, 5.4, 16, 7)
        for i, s_ in enumerate(("Location pinned \u00b7 52.3582 N",
                                "Category \u00b7 Street furniture",
                                "Urgency \u00b7 This week")):
            card(c, x + 10, y + 76 + i * 18, w - 20, 14, fill=WHITE, stroke=LINE_SOFT,
                 r=4, lw=0.6, shadow=False)
            text(c, x + 16, y + 85.5 + i * 18, s_, T.R, 5.0, MUT)
        rect(c, x + 10, y + 133, w - 20, 15, fill=VIOLET, r=4)
        text(c, x + w / 2, y + 143, "Publish task", MED, 5.4, WHITE, 0.2, "center")
    elif kind == "proposals":
        text(c, x + 10, y + 16, "3 proposals \u00b7 voting open", MED, 7.6, INK)
        for i, (n, amt) in enumerate((("Groenwerk BV", "\u20ac412"), ("Studio Tak", "\u20ac455"),
                                      ("M. de Vries", "\u20ac380"))):
            card(c, x + 10, y + 25 + i * 37, w - 20, 32, fill=WHITE,
                 stroke=(alpha(VIOLET, 0.55) if i == 0 else LINE_SOFT), r=6, lw=0.8,
                 shadow=False)
            avatar(c, x + 25, y + 41 + i * 37, 7.4, n[:1], VIOLET_SOFT, VIOLET)
            text(c, x + 37, y + 38 + i * 37, n, MED, 6.2, INK)
            text(c, x + 37, y + 48 + i * 37, "9 days \u00b7 2 milestones \u00b7 4.8\u2605", T.R, 4.9, MUT_DIM)
            text(c, x + w - 20, y + 41 + i * 37, amt, MONO, 6.2, INK, 0.2, "right")
        text(c, x + 10, y + 143, "closes in 2 days 14 h", MONO, 5.0, MUT_DIM, 0.3)
    elif kind == "workspace":
        rect(c, x, y, w, 24, fill=WHITE)
        text(c, x + 10, y + 15.5, "Contractor desk", MED, 8.4, INK)
        for i, (s_, col, amt) in enumerate((("Install bike rack \u00b7 M2", TEAL, "\u20ac950"),
                                            ("Mural: 21 \u00b7 M1", VIOLET, "\u20ac300"),
                                            ("Park clean-up \u00b7 M1", YELLOW, "\u20ac180"))):
            card(c, x + 10, y + 30 + i * 29, w - 20, 24, fill=WHITE, stroke=LINE_SOFT,
                 r=5, lw=0.7, shadow=False)
            text(c, x + 17, y + 45 + i * 29, s_, T.R, 5.8, INK)
            text(c, x + w - 20, y + 45 + i * 29, amt, MONO, 5.4, MUT, 0.2, "right")
            dot(c, x + w - 66, y + 41.5 + i * 29, 2.3, col)
        rect(c, x + 10, y + 121, (w - 27) / 2, 16, fill=PAPER_2, r=4)
        text(c, x + 10 + (w - 27) / 4, y + 132, "Upload evidence", T.R, 5.0, MUT, 0.2, "center")
        rect(c, x + 17 + (w - 27) / 2, y + 121, (w - 27) / 2, 16, fill=VIOLET, r=4)
        text(c, x + 17 + (w - 27) * 0.75, y + 132, "Claim \u20ac210", MED, 5.0, WHITE, 0.2, "center")
    elif kind == "done":
        photo(c, T.PHOTOS + "/bench-fixed.jpg", x, y, w, 58, r=0)
        chip(c, x + 8, y + 7, "VERIFIED", TEAL, WHITE, None, 5.0, 13, 6)
        text(c, x + 10, y + 78, "Completed in 9 days", MED, 7.6, INK)
        text(c, x + 10, y + 89, "\u20ac420 released \u00b7 Groenwerk BV", T.R, 5.2, MUT)
        text(c, x + 10, y + 103, "BEFORE", MONO, 4.6, MUT_DIM, 0.6)
        text(c, x + 10 + (w - 20) / 2 + 6, y + 103, "AFTER", MONO, 4.6, MUT_DIM, 0.6)
        photo(c, T.PHOTOS + "/bench-broken.jpg", x + 10, y + 107, (w - 26) / 2, 36, r=3)
        photo(c, T.PHOTOS + "/bench-fixed.jpg", x + 16 + (w - 26) / 2, y + 107,
              (w - 26) / 2, 36, r=3)


# ------------------------------------------------------------------ map
def map_mock(c, x, y, w, h, markers=None, compact=False, labels=True):
    """Pastel map: paper blocks, mint park, sky water, soft roads."""
    c.saveState()
    p = c.beginPath()
    p.roundRect(x, ty(y) - h, w, h, 0)
    c.clipPath(p, stroke=0, fill=0)
    rect(c, x, y, w, h, fill=HexColor("#F1EADB"))
    rnd = random.Random(21)

    # water + park
    c.setFillColor(HexColor("#DDEBFF"))
    c.rect(x + w * 0.60, ty(y) - h, w * 0.42, h * 0.28, stroke=0, fill=1)
    c.setFillColor(HexColor("#D8F2E5"))
    c.rect(x + x * 0 + w * 0.06, ty(y) - h * 0.56, w * 0.24, h * 0.30, stroke=0, fill=1)

    col_w = w / (5 if compact else 7)
    row_h = h / (4 if compact else 5)
    for i in range(9):
        for j in range(7):
            bx = x + i * col_w + rnd.uniform(-4, 4)
            by = y + j * row_h + rnd.uniform(-3, 3)
            bw = col_w - rnd.uniform(7, 14)
            bh = row_h - rnd.uniform(7, 13)
            if bw < 6 or bh < 6 or bx > x + w or by > y + h:
                continue
            shade = rnd.choice(("#FFFDF7", "#FBF5E6", "#F7EFDC", "#FFF9EC"))
            c.setFillColor(HexColor(shade))
            c.rect(bx, ty(by) - bh, bw, bh, stroke=0, fill=1)
            c.setStrokeColor(HexColor("#E8DEC8"))
            c.setLineWidth(0.4)
            c.rect(bx, ty(by) - bh, bw, bh, stroke=1, fill=0)

    # avenue
    c.setStrokeColor(HexColor("#FFFDF7"))
    c.setLineWidth(9)
    c.line(x + w * 0.1, ty(y), x + w * 0.85, ty(y) - h)
    c.saveState()
    c.setStrokeColor(HexColor("#D9CDB2"))
    c.setLineWidth(0.6)
    c.setDash(3, 4)
    c.line(x + w * 0.1, ty(y), x + w * 0.85, ty(y) - h)
    c.restoreState()

    if markers:
        for (mx, my, name, col) in markers:
            cx, cy = x + mx * w, y + my * h
            if labels and not compact:
                lab_w = sw(name, MED, 8.0, 0.1) + 22
                card(c, cx + 9, cy - 9, lab_w, 18, fill=WHITE, stroke=LINE, r=9,
                     lw=0.6, shadow=False)
                dot(c, cx + 19, cy, 2.6, col)
                text(c, cx + 25, cy + 2.8, name, MED, 8.0, INK, 0.1)
            c.saveState()
            c.setFillColor(alpha(col, 0.18))
            c.circle(cx, ty(cy), 11, stroke=0, fill=1)
            c.restoreState()
            dot(c, cx, cy, 5.0, col)
            dot(c, cx, cy, 2.0, WHITE)
    c.restoreState()
