"""UI kit helpers for the 21 grant deck — light, friendly, hand-built."""
import math
import random

from reportlab.lib.colors import HexColor

import theme as T
from theme import (CORAL, CORAL_SOFT, INK, LINE, LINE_SOFT, MED, MONO, MONO_MED,
                   MUT, MUT_DIM, PAPER, PAPER_2, PINK, R, SKY, SKY_SOFT, TEAL,
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
              r=0, focus=0.45)
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
        photo(c, T.PHOTOS + "/bench-fixed.jpg", x, y, w, 58, r=0, focus=0.42)
        chip(c, x + 8, y + 7, "VERIFIED", TEAL, WHITE, None, 5.0, 13, 6)
        text(c, x + 10, y + 78, "Completed in 9 days", MED, 7.6, INK)
        text(c, x + 10, y + 89, "\u20ac420 released \u00b7 Groenwerk BV", T.R, 5.2, MUT)
        text(c, x + 10, y + 103, "BEFORE", MONO, 4.6, MUT_DIM, 0.6)
        text(c, x + 10 + (w - 20) / 2 + 6, y + 103, "AFTER", MONO, 4.6, MUT_DIM, 0.6)
        photo(c, T.PHOTOS + "/bench-broken.jpg", x + 10, y + 107, (w - 26) / 2, 36,
              r=3, focus=0.55)
        photo(c, T.PHOTOS + "/bench-fixed.jpg", x + 16 + (w - 26) / 2, y + 107,
              (w - 26) / 2, 36, r=3, focus=0.55)


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


# ================================================================ quest exchange
def quest_row(c, x, y, w, h, cat, title, meta, price, col=VIOLET, offers=3,
              small=False):
    """One card in the quest feed."""
    card(c, x, y, w, h, fill=WHITE, stroke=LINE_SOFT, r=6, lw=0.7, shadow=False)
    rect(c, x, y, 3, h, fill=col, r=1.5)
    fs = 0.78 if small else 1.0
    text(c, x + 9, y + 12 * fs, title, MED, 6.6 * fs, INK)
    text(c, x + 9, y + 21 * fs, meta, R, 5.2 * fs, MUT_DIM)
    text(c, x + w - 8, y + 12 * fs, price, MONO_MED, 6.4 * fs, INK, 0.1, "right")
    text(c, x + w - 8, y + 21 * fs, f"{offers} offers", MONO, 4.8 * fs, MUT_DIM,
         0.2, "right")


def quest_screen(c, x, y, w, h, kind="feed", compact=False):
    """Quest-exchange screens, drawn to fit the given rect (top-left origin)."""
    k = 0.85 if compact else 1.0
    rect(c, x, y, w, h, fill=WHITE)

    if kind == "feed":
        text(c, x + 10, y + 17, "Near you", MED, 8.6 * k, INK)
        chip(c, x + w - 74, y + 6, "TODAY", VIOLET, VIOLET_SOFT, None, 5.0, 13, 6)
        for i, (t, bg) in enumerate((("Tutoring", VIOLET_SOFT), ("Repairs", TEAL_SOFT),
                                      ("Care", YELLOW_SOFT))):
            chip(c, x + 10 + i * 54, y + 25, t.upper(), INK, bg, None, 4.6, 12, 5)
        rows = [("Tutoring", "Maths, 2 sessions", "Tue + Thu \u00b7 1 h", "\u20ac40", VIOLET, 3),
                ("Repairs", "Bike, new chain", "Saturday \u00b7 45 min", "\u20ac25", TEAL, 5),
                ("Care", "Dutch conversation", "2 \u00d7 45 min", "\u20ac30", YELLOW, 2),
                ("Repairs", "Shelf, 2 holes", "This week", "\u20ac35", CORAL, 4),
                ("Tutoring", "CV + cover letter", "One evening", "\u20ac20", VIOLET, 6),
                ("Care", "Dog, two walks", "Fri \u00b7 2 \u00d7 30 min", "\u20ac15", TEAL, 2)]
        yy = y + 43
        for cat, title, meta, price, col, n in rows:
            if yy + 30 > y + h:
                break
            quest_row(c, x + 9, yy, w - 18, 28 * k, cat, title, meta, price, col,
                      offers=n, small=compact)
            yy += 32 * k
        if yy + 52 < y + h:
            text(c, x + 10, yy + 8, "YOUR QUESTS", MONO, 4.6, MUT_DIM, 0.8)
            quest_row(c, x + 9, yy + 13, w - 18, 26 * k, "Repairs",
                      "Bench, 2 slats", "waiting for offers", "\u20ac420", VIOLET,
                      offers=0, small=compact)
            yy += 46 * k
        if yy + 14 < y + h:
            rect(c, x + 9, y + h - 20, w - 18, 14, fill=VIOLET, r=4)
            text(c, x + w / 2, y + h - 10, "ASK FOR SOMETHING", MED, 5.0, WHITE,
                 0.6, "center")

    elif kind == "quest":
        text(c, x + 10, y + 17, "Psychology session", MED, 8.0 * k, INK)
        chip(c, x + w - 56, y + 6, "\u20ac30", VIOLET, VIOLET_SOFT, None, 5.0, 13, 6)
        for i, s_ in enumerate(("2 \u00d7 45 min, online or in the park",
                                "Asked by \u00b7 M., 24, Rotterdam",
                                "Needs \u00b7 a supervised trainee")):
            text(c, x + 10, y + 32 + i * 10 * k, s_, R, 5.0 * k, MUT)
        line_y = y + 66 * k
        hline(c, x + 10, line_y, x + w - 10, LINE_SOFT, 0.6)
        text(c, x + 10, line_y + 11, "3 offers", MED, 5.6 * k, INK)
        for i, (n, p) in enumerate((("A. \u00b7 trainee, 2 yrs", "\u20ac28"),
                                     ("L. \u00b7 GZ-psycholoog", "\u20ac45"),
                                     ("S. \u00b7 peer supporter", "\u20ac20"))):
            yy = line_y + 18 + i * 19 * k
            if yy + 16 > y + h - 22:
                break
            card(c, x + 10, yy, w - 20, 16 * k, fill=PAPER, stroke=LINE_SOFT, r=3,
                 lw=0.5, shadow=False)
            dot(c, x + 17, yy + 8 * k, 1.9, VIOLET if i == 0 else MUT_DIM)
            text(c, x + 24, yy + 10.5 * k, n, R, 4.9 * k, INK)
            text(c, x + w - 18, yy + 10.5 * k, p, MONO, 4.9 * k, MUT, 0.1, "right")
        text(c, x + 10, y + h - 40, "A. answers in 2 h on average", MONO, 4.2,
             MUT_DIM, 0.2)
        text(c, x + 10, y + h - 30, "Reward is already in escrow \u00b7 confirmation "
             "releases it", MONO, 4.2, MUT_DIM, 0.2)
        rect(c, x + 10, y + h - 20, w - 20, 14, fill=VIOLET, r=4)
        text(c, x + w / 2, y + h - 10, "Choose an offer", MED, 5.0, WHITE, 0.3,
             "center")

    elif kind == "offers":
        text(c, x + 10, y + 17, "Offers on your quest", MED, 7.6 * k, INK)
        text(c, x + 10, y + 28, "\u20ac30 reward \u00b7 held in escrow", MONO, 4.8, MUT_DIM, 0.2)
        for i, (n, role, price, note) in enumerate((
                ("A.", "Trainee, 2 yrs", "\u20ac28", "Thu evening or Sat morning"),
                ("L.", "GZ-psycholoog", "\u20ac45", "I can start this week"),
                ("S.", "Peer supporter", "\u20ac20", "Sliding scale if needed"))):
            yy = y + 37 + i * 33 * k
            if yy + 30 > y + h:
                break
            card(c, x + 10, yy, w - 20, 29 * k, fill=WHITE,
                 stroke=(alpha(VIOLET, 0.55) if i == 0 else LINE_SOFT), r=5, lw=0.7,
                 shadow=False)
            avatar(c, x + 22, yy + 15 * k, 6.4, n[:1], VIOLET_SOFT, VIOLET)
            text(c, x + 33, yy + 12 * k, f"{n} \u00b7 {role}", MED, 5.2 * k, INK)
            text(c, x + 33, yy + 21 * k, note, R, 4.6 * k, MUT_DIM)
            text(c, x + w - 18, yy + 15 * k, price, MONO_MED, 6.0 * k, INK, 0.1, "right")
        text(c, x + 10, y + h - 22, "6 finished quests \u00b7 1 dispute \u00b7 answer "
             "rate 94%", MONO, 4.4, MUT_DIM, 0.2)
        text(c, x + 10, y + h - 10, "Pick one \u00b7 escrow locks \u00b7 72 h to confirm",
             MONO, 4.6, MUT_DIM, 0.2)

    elif kind == "ask":
        text(c, x + 10, y + 17, "Ask for something", MED, 8.0 * k, INK)
        rect(c, x + 10, y + 27, w - 20, 22, fill=PAPER, stroke=LINE_SOFT, r=4, lw=0.6)
        text(c, x + 16, y + 41, "What do you need?", R, 5.2, MUT_DIM)
        for i, (t, bg) in enumerate((("Tutoring", VIOLET_SOFT), ("Repairs", TEAL_SOFT),
                                      ("Care", YELLOW_SOFT), ("Other", PAPER_2))):
            chip(c, x + 10 + i * 48, y + 55, t.upper(), INK, bg, None, 4.4, 12, 5)
        rows = (("Reward", "\u20ac30"), ("When", "This week"),
                ("Where", "Online or the park"), ("Proof", "Both sides confirm"),
                ("Cancel", "free until day 2"))
        for i, (kk, vv) in enumerate(rows):
            yy = y + 74 + i * 14 * k
            text(c, x + 10, yy, kk, MONO, 4.6, MUT_DIM, 0.4)
            text(c, x + w - 10, yy, vv, R, 5.0, INK, 0, "right")
            hline(c, x + 10, yy + 5, x + w - 10, LINE_SOFT, 0.5)
        rect(c, x + 10, y + h - 22, w - 20, 15, fill=VIOLET, r=4)
        text(c, x + w / 2, y + h - 12, "Post quest \u00b7 no money moves yet", MED, 4.8,
             WHITE, 0.2, "center")

    elif kind == "pay":
        photo(c, T.PHOTOS + "/bench-broken.jpg", x, y, w, h * 0.55, r=0, focus=0.5)
        chip(c, x + 8, y + 7, "BOTH SIDES CONFIRMED", TEAL, WHITE, None, 4.6, 12, 6)
        text(c, x + 10, y + h * 0.55 + 16, "\u20ac30 released", MED, 8.0 * k, INK)
        text(c, x + 10, y + h * 0.55 + 27, "A. \u00b7 tutoring \u00b7 2 sessions", R, 5.0, MUT)
        text(c, x + 10, y + h * 0.55 + 44, "tx 0x4c9\u20262a1", MONO, 4.6, MUT_DIM, 0.2)
        text(c, x + 10, y + h * 0.55 + 56, "\u2605 \u2605 \u2605 \u2605 \u2606  added to A.'s record",
             R, 4.8, MUT_DIM)


# ------------------------------------------------------------------ device frames
def tablet(c, x, y, w, h, url=None):
    """Tablet body; returns the inner screen rect."""
    rect(c, x + 2, y + 6, w, h, fill=T.SHADOW, r=12)
    rect(c, x, y, w, h, fill=INK, r=12)
    rect(c, x + 7, y + 7, w - 14, h - 14, fill=WHITE, r=6)
    if url:
        text(c, x + 18, y + 20, url, MONO, 5.0, MUT_DIM, 0.3)
        hline(c, x + 7, y + 25, x + w - 7, LINE_SOFT, 0.6)
    return x + 7, y + 7, w - 14, h - 14


def kiosk(c, x, y, w, h):
    """Street information column with a screen; returns the screen rect."""
    rect(c, x + 3, y + 7, w, h, fill=T.SHADOW, r=16)
    rect(c, x, y, w, h, fill=INK, r=16)
    rect(c, x + 8, y + 8, w - 16, h - 16, fill=WHITE, r=10)
    rect(c, x + 8, y + h - 44, w - 16, 36, fill=VIOLET_SOFT, r=8)
    text(c, x + w / 2, y + h - 24, "TAP \u00b7 SCAN \u00b7 ASK", MONO, 4.6, VIOLET, 0.5,
         "center")
    return x + 8, y + 8, w - 16, h - 52


def chalk_number(c, x, y, s, color=WHITE, rot=-4, lw=2.2, alpha_=0.9, shadow=True):
    """Hand-chalked '21' over photos: rough strokes, no font."""
    if shadow:
        with T.rotated(c, x, y, rot):
            _chalk(c, x + 2.2, y + 2.2, s, T.alpha(INK, 0.30), lw + 1.6)
    with T.rotated(c, x, y, rot):
        _chalk(c, x, y, s, T.alpha(color, alpha_), lw)


def _chalk(c, x, y, s, color, lw):
    c.saveState()
    c.setStrokeColor(color)
    c.setLineCap(1)
    c.setLineWidth(lw)
    # 2
    p = c.beginPath()
    p.moveTo(x - s * 0.42, T.ty(y - s * 0.34))
    p.curveTo(x - s * 0.40, T.ty(y - s * 0.85), x + s * 0.14, T.ty(y - s * 0.86),
              x + s * 0.13, T.ty(y - s * 0.46))
    p.curveTo(x + s * 0.12, T.ty(y - s * 0.22), x - s * 0.10, T.ty(y - s * 0.12),
              x - s * 0.42, T.ty(y + s * 0.16))
    p.lineTo(x + s * 0.16, T.ty(y + s * 0.16))
    c.drawPath(p, stroke=1, fill=0)
    # 1
    p = c.beginPath()
    p.moveTo(x + s * 0.34, T.ty(y - s * 0.44))
    p.lineTo(x + s * 0.60, T.ty(y - s * 0.78))
    p.lineTo(x + s * 0.60, T.ty(y + s * 0.16))
    c.drawPath(p, stroke=1, fill=0)
    c.restoreState()


def sticker(c, cx, cy, r, rot=6):
    """Round '21' sticker that anyone could slap on a broken thing."""
    T.badge(c, cx, cy, r, "21", VIOLET, WHITE, r * 0.72, MED, rot=rot)
    with T.rotated(c, cx, cy + r + 7, rot):
        pass
