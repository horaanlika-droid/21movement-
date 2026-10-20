"""UI kit helpers for the 21 grant deck."""
import math
import os
import random

from reportlab.lib.colors import HexColor

import theme as T
from theme import (BLUE, LINE, LINE_SOFT, MINT, MONO, MONO_MED, MUT, MUT_DIM,
                   PANEL, PANEL_2, PANEL_3, SAND, SEMI, BOLD, MED, R, L, TXT,
                   VIO, VIO_DEEP, alpha, hline, label, rect, text, sw, ty,
                   photo)


def card(c, x, y, w, h, fill=PANEL, stroke=LINE, r=12, lw=0.8):
    if fill is not None:
        rect(c, x, y, w, h, fill=fill, r=r)
    if stroke is not None:
        rect(c, x, y, w, h, fill=None, stroke=stroke, r=r, lw=lw)


def chip(c, x, y, txt_, fg=TXT, bg=None, stroke=LINE, size=8.4, h=19, padx=8,
         font=MONO_MED, tracking=0.8):
    w = sw(txt_, font, size, tracking) + padx * 2
    rect(c, x, y, w, h, fill=bg, stroke=stroke, r=h / 2, lw=0.7)
    text(c, x + padx, y + h / 2 + size * 0.33, txt_, font, size, fg, tracking)
    return w


def head(c, kicker, title, sub=None, width=1020, subw=720):
    label(c, T.M, 96, kicker, VIO)
    y = T.para(c, T.M, 148, width, title, MED, 30, 36, TXT, -0.35)
    if sub:
        y = T.para(c, T.M, y + 6, subw, sub, L, 12.5, 19, MUT)
    return y


def kv(c, x, y, k, v, w=150, vfont=MED, vsize=13, ksize=8):
    label(c, x, y, k, MUT_DIM, ksize, 1.5)
    text(c, x, y + 20, v, vfont, vsize, TXT, 0.05)


def stat(c, x, y, big, small, color=TXT, size=26, w=200):
    text(c, x, y + size * 0.78, big, MED, size, color, -0.6)
    T.para(c, x, y + size * 0.78 + 18, w, small, R, 9.6, 13, MUT, max_lines=3)


def progress(c, x, y, w, pct, h=4, color=VIO, track=PANEL_3):
    rect(c, x, y, w, h, fill=track, r=h / 2)
    if pct > 0:
        rect(c, x, y, max(h, w * pct), h, fill=color, r=h / 2)


def dot(c, x, y, r, fill=VIO, ring=None, ring_w=1.0):
    c.saveState()
    c.setFillColor(fill)
    c.circle(x, ty(y), r, stroke=0, fill=1)
    if ring is not None:
        c.setStrokeColor(ring)
        c.setLineWidth(ring_w)
        c.circle(x, ty(y), r, stroke=1, fill=0)
    c.restoreState()


def arrow(c, x1, y1, x2, y2, color=MUT_DIM, lw=0.9, head_=4.5):
    c.saveState()
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(lw)
    c.line(x1, ty(y1), x2, ty(y2))
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (0.45, -0.45):
        a = ang + math.pi + s
        c.line(x2, ty(y2), x2 + head_ * math.cos(ang + math.pi - s * 0.0) * 0,
               ty(y2))
    c.restoreState()
    _arrowhead(c, x2, y2, ang, head_, color)


def _arrowhead(c, x, y, ang, size, color):
    p = c.beginPath()
    p.moveTo(x, ty(y))
    p.lineTo(x - size * math.cos(ang - 0.42), ty(y) + size * math.sin(ang - 0.42))
    p.lineTo(x - size * math.cos(ang + 0.42), ty(y) + size * math.sin(ang + 0.42))
    p.close()
    c.saveState()
    c.setFillColor(color)
    c.drawPath(p, stroke=0, fill=1)
    c.restoreState()


def avatar(c, x, y, r, initials, bg=PANEL_3, fg=MUT):
    c.saveState()
    c.setFillColor(bg)
    c.circle(x, ty(y), r, stroke=0, fill=1)
    c.restoreState()
    text(c, x, y + 3.4, initials, MONO_SEMI if False else MONO_MED, r * 0.95, fg,
         0.4, "center")


def browser(c, x, y, w, h, url="21.city/explore", dark=True):
    card(c, x, y, w, h, fill=PANEL, stroke=LINE, r=10)
    rect(c, x, y, w, 22, fill=PANEL_2, r=10)
    rect(c, x, y + 11, w, 11, fill=PANEL_2)
    for i, col in enumerate((T.ALERT, SAND, MINT)):
        dot(c, x + 13 + i * 10, y + 11, 2.4, alpha(col, 0.55))
    text(c, x + w / 2, y + 14.6, url, MONO, 7.2, MUT_DIM, 0.3, "center")
    hline(c, x, y + 22, x + w, LINE, 0.7)


def phone(c, x, y, w=132, h=272):
    card(c, x, y, w, h, fill=PANEL, stroke=LINE, r=18, lw=1.0)
    rect(c, x + w / 2 - 16, y + 7, 32, 7, fill=INK_R, r=4)
    rect(c, x + 4, y + 20, w - 8, h - 30, fill=PANEL_2, r=14)


def window_content(c, x, y, w, h, kind):
    """Miniature app screens for the product gallery (fits a 356 x 150 frame)."""
    rect(c, x, y, w, h, fill=PANEL_2, r=0)
    if kind == "map":
        rect(c, x, y, w, 22, fill=PANEL_3)
        text(c, x + 10, y + 15, "Explore", MED, 8, TXT)
        U_chip = chip
        U_chip(c, x + 58, y + 4, "24 OPEN", VIO, PANEL_2, VIO_DEEP, 5.4, 14, 6)
        U_chip(c, x + w - 46, y + 4, "All", MUT, PANEL, LINE, 5.4, 14, 6)
        map_mock(c, x, y + 22, w, h - 22, compact=True, labels=False,
                 markers=[(0.22, 0.30, "", VIO), (0.44, 0.62, "", MINT),
                          (0.68, 0.36, "", SAND), (0.84, 0.72, "", VIO)])
        card(c, x + 8, y + h - 46, 150, 38, fill=alpha(T.INK, 0.88), stroke=LINE, r=6, lw=0.6)
        text(c, x + 16, y + h - 28, "Broken bench \u00b7 420", MED, 6.6, TXT)
        text(c, x + 16, y + h - 17, "\u20ac362 raised \u00b7 41 people", MONO, 5.4, MUT, 0.2)
    elif kind == "project":
        photo(c, T.A + "/bench-before.jpg", x, y, w * 0.44, h,
              overlay=T.INK, overlay_alpha=0.25)
        px = x + w * 0.44 + 10
        text(c, px, y + 18, "Broken bench, Oosterpark", MED, 7.6, TXT)
        label(c, px, y + 30, "AMSTERDAM \u00b7 14 MAR", MUT_DIM, 5, 0.8)
        progress(c, px, y + 40, w * 0.56 - 22, 0.86, 3)
        text(c, px, y + 52, "\u20ac362 of \u20ac420  \u00b7  41 supporters", MONO, 5.4, TXT)
        for i, (s_, col) in enumerate((("Milestone 1 \u00b7 site prep", MINT),
                                       ("Milestone 2 \u00b7 re-fix + paint", SAND))):
            card(c, px, y + 62 + i * 24, w * 0.56 - 22, 19, fill=PANEL, stroke=LINE_SOFT, r=3)
            dot(c, px + 7, y + 71.5 + i * 24, 1.9, col)
            text(c, px + 13, y + 74 + i * 24, s_, R, 5.2, MUT)
        text(c, px, y + 122, "▸ Verified evidence attached", MONO, 5.2, MINT, 0.2)
    elif kind == "report":
        text(c, x + 10, y + 16, "Report a problem", MED, 7.6, TXT)
        rect(c, x + 10, y + 24, w - 20, 52, fill=PANEL_3, r=4)
        text(c, x + w / 2, y + 54, "+  take photo", MONO, 5.8, MUT, 0.6, "center")
        for i, s_ in enumerate(("Location pinned \u00b7 52.3582 N", "Category \u00b7 Public furniture")):
            card(c, x + 10, y + 81 + i * 18, w - 20, 14, fill=PANEL, stroke=LINE_SOFT, r=3)
            text(c, x + 16, y + 91 + i * 18, s_, R, 5.2, MUT)
        rect(c, x + 10, y + 120, w - 20, 15, fill=VIO, r=3)
        text(c, x + w / 2, y + 130, "Publish task", MED, 5.4, T.INK, 0.2, "center")
    elif kind == "proposals":
        text(c, x + 10, y + 16, "3 proposals \u00b7 voting open", MED, 7.6, TXT)
        for i, (n, amt) in enumerate((("Groenwerk BV", "\u20ac412"), ("Studio Tak", "\u20ac455"),
                                      ("M. de Vries", "\u20ac380"))):
            card(c, x + 10, y + 26 + i * 38, w - 20, 33, fill=PANEL,
                 stroke=(alpha(VIO, 0.5) if i == 0 else LINE_SOFT), r=4)
            avatar(c, x + 24, y + 42.5 + i * 38, 6.4, n[:1], PANEL_3, MUT)
            text(c, x + 35, y + 40 + i * 38, n, MED, 6.2, TXT)
            text(c, x + 35, y + 50 + i * 38, "9 days \u00b7 2 milestones \u00b7 4.8", R, 5, MUT_DIM)
            text(c, x + w - 20, y + 43 + i * 38, amt, MONO, 6.2, TXT, align="right")
        text(c, x + 10, y + 146, "closes in 2 days 14 h", MONO, 5.2, MUT_DIM, 0.3)
    elif kind == "workspace":
        text(c, x + 10, y + 16, "Contractor desk", MED, 7.6, TXT)
        for i, (s_, col) in enumerate((("Install bike rack \u00b7 M2", SAND),
                                       ("Mural: 21 \u00b7 M1", VIO),
                                       ("Park clean-up \u00b7 M1", MINT))):
            card(c, x + 10, y + 26 + i * 30, w - 20, 25, fill=PANEL, stroke=LINE_SOFT, r=4)
            text(c, x + 18, y + 42 + i * 30, s_, R, 5.8, TXT)
            dot(c, x + w - 20, y + 38.5 + i * 30, 2.2, col)
        rect(c, x + 10, y + 120, (w - 26) / 2, 16, fill=PANEL_3, r=3)
        text(c, x + 10 + (w - 26) / 4, y + 131, "Upload evidence", R, 5.2, MUT, 0.2, "center")
        rect(c, x + 16 + (w - 26) / 2, y + 120, (w - 26) / 2, 16, fill=VIO, r=3)
        text(c, x + 16 + (w - 26) * 0.75, y + 131, "Claim \u20ac210", MED, 5.2, T.INK, 0.2, "center")
    elif kind == "done":
        photo(c, T.A + "/bench-after.jpg", x, y, w, 62, overlay=T.INK, overlay_alpha=0.12)
        chip(c, x + 8, y + 6, "VERIFIED", MINT, T.INK, None, 5, 12, 5)
        text(c, x + 10, y + 82, "Completed in 9 days", MED, 7.6, TXT)
        text(c, x + 10, y + 94, "\u20ac420 released \u00b7 Groenwerk BV", R, 5.4, MUT)
        text(c, x + 10, y + 110, "BEFORE", MONO, 4.8, MUT_DIM, 0.6)
        text(c, x + 10 + (w - 20) / 2 + 6, y + 110, "AFTER", MONO, 4.8, MUT_DIM, 0.6)
        photo(c, T.A + "/bench-before.jpg", x + 10, y + 114, (w - 26) / 2, 30)
        photo(c, T.A + "/bench-after.jpg", x + 16 + (w - 26) / 2, y + 114,
              (w - 26) / 2, 30)


# ------------------------------------------------------------------ map
INK_R = T.INK


def map_mock(c, x, y, w, h, markers=None, compact=False, labels=True):
    c.saveState()
    p = c.beginPath()
    p.roundRect(x, ty(y) - h, w, h, 0)
    c.clipPath(p, stroke=0, fill=0)
    rect(c, x, y, w, h, fill=HexColor("#0A0A0D"))
    rnd = random.Random(21)

    # park / water
    c.setFillColor(HexColor("#101A15"))
    c.rect(x + w * 0.06, ty(y) - h * 0.52, w * 0.26, h * 0.3, stroke=0, fill=1)
    c.setFillColor(HexColor("#0C1420"))
    c.rect(x + w * 0.62, ty(y) - h, w * 0.4, h * 0.26, stroke=0, fill=1)

    # blocks
    col_w = w / (5 if compact else 7)
    row_h = h / (4 if compact else 5)
    for i in range(9):
        for j in range(7):
            bx = x + i * col_w + rnd.uniform(-4, 4)
            by = y + j * row_h + rnd.uniform(-3, 3)
            bw = col_w - rnd.uniform(7, 14)
            bh = row_h - rnd.uniform(7, 13)
            if bw < 6 or bh < 6:
                continue
            if bx > x + w or by > y + h:
                continue
            shade = rnd.choice(("#17171D", "#1A1A21", "#141419", "#1D1D25"))
            c.setFillColor(HexColor(shade))
            c.rect(bx, ty(by) - bh, bw, bh, stroke=0, fill=1)
    # diagonal avenue
    c.setStrokeColor(HexColor("#08080B"))
    c.setLineWidth(9)
    c.line(x + w * 0.1, ty(y), x + w * 0.85, ty(y) - h)
    c.saveState()
    c.setStrokeColor(HexColor("#242430"))
    c.setLineWidth(0.5)
    c.setDash(3, 4)
    c.line(x + w * 0.1, ty(y), x + w * 0.85, ty(y) - h)
    c.restoreState()

    # markers
    if markers:
        for (mx, my, name, col) in markers:
            cx, cy = x + mx * w, y + my * h
            if labels and not compact:
                lab_w = sw(name, MED, 8.2, 0.1) + 22
                card(c, cx + 9, cy - 9, lab_w, 18, fill=alpha(T.INK, 0.9), stroke=LINE, r=9, lw=0.6)
                dot(c, cx + 19, cy, 2.6, col)
                text(c, cx + 25, cy + 2.9, name, MED, 8.2, TXT, 0.1)
            c.saveState()
            c.setFillColor(alpha(col, 0.16))
            c.circle(cx, ty(cy), 11, stroke=0, fill=1)
            c.restoreState()
            dot(c, cx, cy, 5.2, col)
            dot(c, cx, cy, 2.0, T.INK)
    c.restoreState()
