"""21 — grant deck. The number, and the exchange underneath it.

23 slides, 1280 x 720 pt, all text in code. Run `python3 build.py --preview`
from this folder to rebuild the PDF and the PNG previews.

The ask is a floor, not a wish: €7,500 for six months in one city, with the
code hours in the budget at the author's own wage. Above the floor the split is
written as shares of whatever round funds it.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.pdfgen import canvas as rl_canvas

import theme as T
import uikit as U
from theme import (CORAL, CORAL_SOFT, H, INK, INK_SOFT, L, LINE, LINE_SOFT, M,
                   MED, MONO, MONO_MED, MUT, MUT_DIM, PAPER, PAPER_2, PINK,
                   HAND, HAND_B, PINK_SOFT, R, SEMI, SERIF, SERIF_IT, SHADOW, SKY,
                   SKY_SOFT,
                   TEAL, TEAL_SOFT, VIOLET, VIOLET_DEEP, VIOLET_SOFT, W, WHITE, YELLOW,
                   YELLOW_SOFT, alpha, card, chip, diamond, doodle_arrow, footer,
                   hline, illustration, label, logotype, marker, page, para,
                   photo, polaroid, phone_shot, rect, rtext, sparkle, squiggle,
                   tape, text, vline)

T.register_fonts()
os.makedirs(T.OUT, exist_ok=True)
os.makedirs(T.PREVIEW, exist_ok=True)

ART = T.ART
PHOTOS = T.PHOTOS
TOTAL = 23


def foot(c, idx, section=""):
    footer(c, idx, section)


def step_badge(c, cx, cy, n, col, r=17):
    U.badge(c, cx, cy, r, n, col, WHITE, r * 0.82, MED)


def stat3(c, x, y, w, h, cols):
    """Card with three small stat columns: (label, value, sub)."""
    card(c, x, y, w, h, fill=WHITE, stroke=LINE, r=18, shadow=True, shadow_dy=6)
    cw = (w - 48) / 3
    for i, (k, v, s) in enumerate(cols):
        cx = x + 24 + i * cw
        label(c, cx, y + 28, k, MUT_DIM, 7.0, 1.4)
        text(c, cx, y + 58, v, MED, 20, INK, -0.5)
        text(c, cx, y + 78, s, R, 7.8, MUT)
        if i:
            vline(c, cx - 12, y + 22, y + h - 20, LINE_SOFT, 0.9)


# ============================================================ 01  cover
def s01(c, idx):
    page(c)
    illustration(c, ART + "/cover-21.png", 690, 132, 530)

    logotype(c, M, 26, 26, INK, VIOLET)
    label(c, M + 96, 80, "the mark, and the exchange under it", MUT, 8.0, 1.5)
    chip(c, W - M - 104, 64, "GRANT 2026", VIOLET, WHITE, alpha(VIOLET, 1),
         7.2, 22, 9, rot=3, shadow=True)

    sparkle(c, 566, 214, 8, YELLOW)
    sparkle(c, 636, 372, 5.5, PINK)
    label(c, M, 200, "Ethereum ecosystem grant \u00b7 application", VIOLET, 8.6, 1.9)

    text(c, M, 360, "21", HAND_B, 176, INK, -4)
    squiggle(c, M + 6, 372, 170, TEAL, 3.0, 2.6, 4)

    text(c, M + 212, 262, "The number is the PR.", SERIF_IT, 30, VIOLET, -0.3)
    text(c, M + 212, 302, "The quest is the product.", SERIF_IT, 30, VIOLET, -0.3)

    para(c, M, 402, 576,
         "Anyone can chalk 21 on asphalt, spray it on a wall, or stencil it next "
         "to a broken lift. Under the mark runs a board where a person asks for "
         "what they need \u2014 a tutor, a plumber, a psychologist \u2014 offers "
         "arrive, the work happens, escrow pays.", R, 12.2, 18.6, MUT)

    stat3(c, M, 484, 576, 104, [
        ("The floor", "\u20ac7,500", "the smallest round that moves"),
        ("Above it", "Same split", "45 / 15 / 15, at any size"),
        ("For code", "250 \u20b9/h", "my wage, 960 hours"),
    ])

    x = M
    for ch, bg in (("NO TOKEN", YELLOW_SOFT), ("NO LOGO", TEAL_SOFT),
                   ("MIT KIT", VIOLET_SOFT)):
        x += chip(c, x, 610, ch, INK, bg, alpha(INK, 0.12), 7.2, 24, 11,
                  rot=-1.5 + x % 3) + 9
    text(c, W - M, 626, "21.city  \u00b7  hello@21.city", MONO, 8.0, MUT_DIM, 0.4,
         "right")
    text(c, W - M, 646, f"{idx:02d} / {TOTAL}", MONO, 8.0, MUT_DIM, 0.8, "right")


# ============================================================ 02  problem
def s02(c, idx):
    page(c)
    T.head(c, "01 \u2014 The problem",
           "The city can see the problem. So can the neighbour who could fix it.",
           "Two failures, one missing layer: nothing turns a need into a bounded, "
           "paid, verifiable job.", width=716, subw=520, y=106, size=34, leading=40)

    items = [
        ("Reports end in a ticket.",
         "A photo to a hotline returns a case number, not a budget. Nobody learns "
         "who decided, who was paid, or what happened next. A street rebuild goes "
         "the other way: one big contract, a hoarding, no timeline.", VIOLET),
        ("Helpful neighbours live in DMs.",
         "A tutor hour, a bike repair, an hour with a psychologist: people find "
         "each other in group chats, pay cash, cancel twice \u2014 and nothing is "
         "recorded.", TEAL),
        ("Supply stays invisible until hired.",
         "The person who could do the work never sees the need; the person with "
         "the need never sees the price. An agency or an ad sits in between.",
         CORAL),
    ]
    y = 282
    for i, (h_, b, col) in enumerate(items):
        step_badge(c, M + 16, y + 2, f"0{i + 1}", col, 16)
        text(c, M + 46, y + 7, h_, MED, 13.4, INK)
        para(c, M + 46, y + 28, 436, b, R, 9.9, 15, MUT)
        y += 100

    polaroid(c, PHOTOS + "/bench-broken.jpg", 812, 208, 318, 366, pad=9,
             cap="CHALKED 21 \u00b7 OOSTERPARK \u00b7 DAY 91", rot=2.2)
    tape(c, 900, 202, 66, 19, -5, alpha(YELLOW, 0.7))
    chip(c, 800, 142, "PHOTO: A RESIDENT'S PHONE", WHITE, INK, None, 6.8, 20, 9,
         rot=-2)

    hline(c, M, 610, 700, alpha(INK, 0.12))
    label(c, M, 634, "What is missing", MUT_DIM, 7.4, 1.5)
    text(c, M + 152, 634, "A bounded ask. Public offers. Escrow. A receipt.",
         MED, 11.4, INK, 0.1)
    foot(c, idx, "The problem")


# ============================================================ 03  the mark
def s03(c, idx):
    page(c)
    T.head(c, "02 \u2014 The mark",
           "Not a campaign. A number anyone can paint.",
           "A slogan needs translation, a logo needs a licence, a brand needs a "
           "budget. Two digits need none of that \u2014 and they say which era you "
           "belong to: the one where the person next to the problem can fix it.",
           width=712, subw=500, y=104, size=36, leading=41)

    blocks = [
        ("Unbannable, unownable", VIOLET,
         "You cannot confiscate a number or copyright two digits. Nobody has to "
         "ask us for permission, and we cannot sell the right to use it."),
        ("Amateur is the format", TEAL,
         "Chalk on asphalt, a marker on a lift door, a sticker on a broken bench, "
         "a five-second TikTok of the spray. Polish would kill it: the point is "
         "that it looks made by a person."),
        ("Every mark is a link", CORAL,
         "The number points at the board under it \u2014 a quest, a reward, an "
         "escrow, a receipt. The paint is the ad; the finished work is the proof."),
    ]
    y = 296
    for i, (k, col, v) in enumerate(blocks):
        U.dot(c, M + 4, y + 4, 4.2, col)
        text(c, M + 20, y + 8, k, MED, 12.4, INK)
        para(c, M + 20, y + 28, 500, v, R, 9.2, 14, MUT)
        y += 96

    illustration(c, ART + "/meme-wall.png", 660, 132, 550)
    chip(c, 1170, 150, "ROTTERDAM \u00b7 03:40", WHITE, INK, None, 6.4, 20, 8, rot=4)

    card(c, 660, 470, 548, 140, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, 682, 494, "Where our money goes \u2014 and doesn't", VIOLET, 7.2, 1.4)
    para(c, 682, 516, 504,
         "We pay for consented walls, artists, photographers and the kit. We never "
         "pay for illegal paint, and we never instruct anyone to break a rule. The "
         "mark travels without us \u2014 that is the point of choosing a number.",
         R, 9.0, 13.6, MUT)
    chip(c, 682, 566, "STENCIL", INK, PAPER, alpha(INK, 0.14), 6.4, 18, 8)
    chip(c, 758, 566, "STICKER", INK, PAPER, alpha(INK, 0.14), 6.4, 18, 8)
    chip(c, 836, 566, "CHALK", INK, PAPER, alpha(INK, 0.14), 6.4, 18, 8)
    text(c, W - 40, 568, "no permission needed", MONO, 6.8, MUT_DIM, 0.3, "right")

    chip(c, M, 594, "THE NUMBER IS THE ONLY BRIEF", VIOLET, WHITE, None, 6.8, 24,
         11, rot=-2, shadow=True)
    text(c, M + 252, 612, "No tagline. No mascot. No translation.", R, 8.8,
         MUT_DIM)
    foot(c, idx, "The mark")


# ============================================================ 04  the mark on broken things
def s04(c, idx):
    page(c)
    T.head(c, "03 \u2014 The mark on the infrastructure",
           "A number on the thing that is broken.",
           "A bench, a pothole, a lift, an overflowing bin: the mark turns a public "
           "eyesore into an address. Two digits, one task page, and a photo anyone "
           "can retake.", width=740, subw=560, y=104, size=36, leading=41)

    shots = [(PHOTOS + "/bench-broken.jpg", "CHALK \u00b7 OOSTERPARK", -3.0, 0.45),
             (PHOTOS + "/bike-rack.jpg", "MARKER \u00b7 LIFT 2", 1.6, 0.55),
             (PHOTOS + "/shelter.jpg", "STICKER \u00b7 TRAM STOP", -1.4, 0.4)]
    for i, (p, cap, rot, focus) in enumerate(shots):
        x = M + i * 232
        photo(c, p, x, 218, 214, 292, r=10, border=WHITE, bw=7, shadow=True,
              focus=focus)
        U.chalk_number(c, x + 150, 470, 66, WHITE, rot=-6 + i * 3, lw=3.4, alpha_=0.95)
        label(c, x + 2, 538, cap, MUT, 6.6, 1.4)
        if i < 2:
            text(c, x + 226, 470, "\u00b7 \u00b7 \u00b7", MONO, 8, MUT_DIM, 1.0, "center")

    x, w = 790, 418
    card(c, x, 210, w, 112, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, x + 20, 234, "A mark is a hyperlink", VIOLET, 7.2, 1.4)
    para(c, x + 20, 256, 378,
         "21 + the place = a task page. The page holds the ask, the offers, the "
         "money and the before/after. Reading it needs no app, no account, no "
         "permission.", R, 8.8, 13.2, MUT)

    for i, s_ in enumerate((
            "Anyone can open the task behind a mark \u2014 and become the asker.",
            "If the thing gets fixed, the mark is crossed out and stays in the record.",
            "If it never gets fixed, the page shows how long it has been waiting.")):
        U.dot(c, x + 4, 372 + i * 42, 2.4, VIOLET)
        para(c, x + 16, 368 + i * 42, 396, s_, R, 8.8, 12.8, MUT)

    card(c, x, 500, w, 140, fill=PAPER_2, stroke=alpha(INK, 0.10), r=14,
         shadow=False)
    text(c, x + 20, 534, "TASK \u00b7 21/A1142", MONO_MED, 8.6, VIOLET_DEEP, 0.6)
    text(c, x + 20, 558, "Bench, slats broken", MED, 13, INK)
    text(c, W - 20, 556, "\u20ac420", MED, 14, INK, 0, "right")
    text(c, x + 20, 578, "asked by a resident \u00b7 4 offers \u00b7 escrow funded",
         R, 8.4, MUT)
    chip(c, x + 20, 598, "OPEN \u00b7 DAY 6", TEAL, WHITE, None, 6.2, 18, 8)
    text(c, W - 20, 611, "deadline 22 oct", MONO, 6.6, MUT_DIM, 0.3, "right")
    foot(c, idx, "The mark on infrastructure")


# ============================================================ 05  the exchange
def s05(c, idx):
    page(c)
    T.head(c, "04 \u2014 The exchange",
           "Supply does not show up. Demand does.",
           "21 is a board, not a catalogue: someone posts what they need, offers "
           "arrive, the asker picks. No agency, no dispatch algorithm, no ranking "
           "for sale.", width=560, subw=500, y=104, size=34, leading=39)

    steps = [
        ("01", "Ask", "One paragraph, a reward ceiling and a deadline. Two minutes, "
                      "no CV.", VIOLET),
        ("02", "Offers arrive", "Named people with a price, a time and a track "
                                "record. Three offers is normal; one is enough.", TEAL),
        ("03", "Choose", "The asker decides. Offers appear in the order they came "
                         "in \u2014 never boosted, never ranked by spend.", YELLOW),
        ("04", "Do the work", "Online or in the street. The reward is already in "
                              "escrow, so nobody works on a promise.", CORAL),
        ("05", "Confirm", "Both sides confirm; escrow releases; the record stays. "
                          "72 hours to raise a dispute.", SKY),
    ]
    y = 268
    for n, k, d, col in steps:
        step_badge(c, M + 15, y, n, col, 14)
        text(c, M + 42, y + 4, k, MED, 11.8, INK)
        para(c, M + 42, y + 22, 452, d, R, 9.0, 13.4, MUT)
        y += 66

    illustration(c, ART + "/quest-exchange.png", 604, 150, 604)
    chip(c, 604, 138, "ASK \u00b7 OFFER \u00b7 DONE", WHITE, INK, alpha(INK, 0.16),
         6.4, 20, 8, rot=-2)
    sparkle(c, 1180, 168, 6, YELLOW)

    card(c, 604, 498, 604, 142, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, 626, 522, "Four rules, no exceptions", VIOLET, 7.2, 1.4)
    rules = [("A medium unit", "one hour, one session, one visit. Big projects are split."),
             ("No cash off-platform", "if it leaves escrow, it leaves the record."),
             ("No paid placement", "no promoted offers, no bought reviews."),
             ("Reputation is earned", "per finished quest, and cannot be bought.")]
    for i, (k, v) in enumerate(rules):
        cx = 626 + (i % 2) * 296
        cy = 550 + (i // 2) * 40
        text(c, cx, cy, k, MED, 8.6, INK)
        text(c, cx, cy + 13, v, R, 7.6, MUT)
    foot(c, idx, "The exchange")


# ============================================================ 06  anatomy
def s06(c, idx):
    page(c)
    T.head(c, "05 \u2014 Anatomy of a quest",
           "Bounded, priced, provable.",
           "A quest is the smallest unit of work two strangers can trust. "
           "Everything the exchange needs fits on one card.", width=760, subw=600,
           y=104, size=36, leading=41)

    cards = [
        ("The ask", VIOLET, "Plain language, 400 characters. What, where, when \u2014 "
                            "not a job description copied from a portal."),
        ("Scope per quest", TEAL, "One hour, one session, one visit, one small fix. "
                                  "A big project is split, never swallowed."),
        ("Reward", YELLOW, "A fixed amount, funded into escrow before the first "
                           "offer is even shown."),
        ("Deadline", CORAL, "A date and an hour. Not \u201csoon\u201d, not "
                            "\u201cflexible\u201d, not \u201cASAP\u201d."),
        ("Proof", SKY, "Both sides confirm and attach a note or a photo. Silence "
                       "is not consent."),
        ("Who may answer", PINK, "Anyone with a profile. ID check above \u20ac50, "
                                 "category checks where the law asks."),
    ]
    for i, (k, col, v) in enumerate(cards):
        cx = M + (i % 3) * 384
        cy = 232 + (i // 3) * 142
        card(c, cx, cy, 368, 128, fill=WHITE, stroke=LINE, r=16, shadow=True,
             shadow_dy=5)
        rect(c, cx + 1, cy + 12, 6, 104, fill=col, r=3)
        text(c, cx + 24, cy + 32, f"0{i + 1}", MONO, 7.4, MUT_DIM, 1.2)
        text(c, cx + 24, cy + 56, k, MED, 13, INK)
        para(c, cx + 24, cy + 76, 316, v, R, 8.8, 13, MUT)

    card(c, M, 526, 552, 108, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 550, "Why medium complexity", VIOLET, 7.2, 1.4)
    para(c, M + 22, 568, 508,
         "Low enough to finish in an afternoon, high enough that reputation "
         "matters: tutoring, translation, bike repair, hairdressing, supervised "
         "psychology, handyman, CV review, moving a sofa.", R, 8.8, 13.2, MUT)

    card(c, 648, 526, 560, 108, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, 670, 550, "Why not a gig app", CORAL, 7.2, 1.4)
    para(c, 670, 568, 516,
         "No dispatch algorithm deciding who eats, no commission taken from the "
         "worker before the work exists, no rating that punishes turning a shift "
         "down. The ask is public; the answer is a person.", R, 8.8, 13.2, MUT)
    foot(c, idx, "Anatomy of a quest")


# ============================================================ 07  quest end to end
def s07(c, idx):
    page(c)
    T.head(c, "06 \u2014 One quest, end to end",
           "A psychology session. Nine days, no invoice.",
           "Demo scenario from the product spec. Amounts, names and dates are "
           "illustrative, not reported results.", width=700, subw=560, y=104,
           size=34, leading=39)

    frames = [("The ask", "21.city/q/ps-04", "quest", 0.60),
              ("The offers", "21.city/q/ps-04/offers", "offers", 0.93),
              ("Done", "21.city/q/ps-04/done", "pay", 0.86)]
    for i, (lab, url, kind, at) in enumerate(frames):
        x = M + i * 232
        label(c, x, 214, lab, MUT_DIM, 6.8, 1.4)
        U.browser(c, x, 224, 214, 244, url=url)
        U.quest_screen(c, x, 248, 214, 220, kind=kind)
        if i < 2:
            doodle_arrow(c, x + 218, 346, x + 230 + 0, 346, MUT_DIM, 1.2, 0.1)

    text(c, M, 498, "The asker is M., 24, Rotterdam. The provider is A., a supervised "
                    "trainee. \u20ac30 sits in escrow from hour one.", R, 8.6, MUT)
    text(c, M, 518, "Both screens are the same page, one tap apart \u2014 nothing to "
                    "install.", R, 8.6, MUT_DIM)

    x = 790
    label(c, x, 214, "Quest ledger \u00b7 public by default", VIOLET, 7.0, 1.5)
    rows = [
        ("Day 0", "Quest posted", "\u20ac30 ceiling", YELLOW),
        ("Day 0", "Reward funded", "\u20ac30 in escrow", VIOLET),
        ("Day 1", "3 offers", "\u20ac20 \u2013 \u20ac45", INK_SOFT),
        ("Day 2", "Offer chosen", "A., trainee", INK_SOFT),
        ("Day 4", "Session 1", "45 min, online", INK_SOFT),
        ("Day 7", "Session 2", "45 min, the park", INK_SOFT),
        ("Day 8", "Both confirmed", "nothing disputed", TEAL),
        ("Day 9", "Escrow released", "\u20ac30 + record", TEAL),
    ]
    y = 240
    vline(c, x + 6, y + 8, y + 8 + 34 * (len(rows) - 1), LINE, 1)
    for t, a, b, col in rows:
        U.dot(c, x + 6, y + 8, 3.8, col)
        text(c, x + 22, y + 12, t, MONO, 7.2, MUT_DIM, 0.4)
        text(c, x + 66, y + 12, a, MED, 9.6, INK)
        text(c, W - M, y + 12, b, MONO, 7.8, MUT, 0.2, "right")
        y += 34

    card(c, x, 524, W - M - x, 116, fill=WHITE, stroke=LINE, r=14, shadow=True)
    label(c, x + 18, 548, "What A. keeps", VIOLET, 7.0, 1.4)
    para(c, x + 18, 570, 396, "A public record of work done \u2014 not a five-star "
         "average that punishes a bad week.", R, 8.8, 12.8, MUT)
    text(c, x + 18, 604, "21.city/q/ps-04", MONO, 7.4, MUT_DIM, 0.2)
    text(c, x + 18, 624, "Settlement in seconds. No invoice, no 30-day terms.",
         R, 8.2, MUT_DIM)

    card(c, M, 548, 500, 92, fill=VIOLET_SOFT, stroke=alpha(VIOLET, 0.35), r=14,
         shadow=True)
    label(c, M + 18, 572, "Why this quest, and not a search engine", VIOLET, 7.0, 1.4)
    text(c, M + 18, 596, "The reward is visible, the offers are named, and the money "
                         "is already held.", R, 8.8, INK_SOFT)
    text(c, M + 18, 618, "Three people replied in 19 hours. Nobody paid for placement.",
         R, 8.2, MUT)
    foot(c, idx, "One quest")


# ============================================================ 08  trust
def s08(c, idx):
    page(c)
    T.head(c, "07 \u2014 Trust, without a boss",
           "Money waits. Then it moves.",
           "Escrow is the only reason two strangers meet. No company account holds "
           "the reward: one contract per quest, released by rules pinned before "
           "the ask is funded.", width=700, subw=540, y=104, size=36, leading=41)

    rows = [
        ("Funded before offers", "A quest cannot collect offers until the reward is "
                                 "in escrow. No maybes, no invoice afterwards."),
        ("Two-sided confirmation", "The asker confirms the work; the provider "
                                   "confirms the handover. Silence is not consent: "
                                   "72 hours, then a reviewer steps in."),
        ("Dispute, not drama", "A dispute freezes the release and opens a three-step "
                               "panel: evidence, a call, a decision. Both sides stay "
                               "on the record."),
        ("Safety is a product rule", "Public first meetings, no cash off-platform, no "
                                     "medical claims, ID above \u20ac50, and a one-tap "
                                     "report that pauses a profile."),
    ]
    y = 250
    for i, (k, v) in enumerate(rows):
        text(c, M, y + 10, f"0{i + 1}", MONO_MED, 8.4, VIOLET, 1.2)
        text(c, M + 28, y + 10, k, MED, 11.6, INK)
        para(c, M + 28, y + 28, 434, v, R, 9.2, 13.8, MUT)
        hline(c, M, y + 66, 500, LINE_SOFT)
        y += 80

    x, y0, w, h = 560, 196, 648, 440
    card(c, x, y0, w, h, fill=WHITE, stroke=LINE, r=18, shadow=True, shadow_dy=6)
    text(c, x + 22, y0 + 34, "Quest record", MED, 12.6, INK)
    chip(c, x + w - 118, y0 + 18, "RELEASED", TEAL, TEAL_SOFT, alpha(TEAL, 0.5),
         7, 20, 9)

    meta = [("Reward", "\u20ac30 \u00b7 USDC on Base"),
            ("Provider", "A. \u00b7 0x8a\u2026 4c1"),
            ("Asker", "M. \u00b7 0x1f\u2026 9be"),
            ("Category check", "supervised trainee \u00b7 valid"),
            ("Released", "2026-10-09T09:41Z"),
            ("Transaction", "0x4c9\u2026 2a1")]
    my = y0 + 62
    for k, v in meta:
        text(c, x + 22, my, k, MONO, 6.8, MUT_DIM, 0.4)
        text(c, x + 22, my + 14, v, MONO, 8.0, INK, 0.2)
        hline(c, x + 22, my + 22, x + w - 22, LINE_SOFT, 0.6)
        my += 32

    label(c, x + 22, y0 + 276, "Confirmations", MUT_DIM, 7.2, 1.4)
    atts = [("Asker", "0x1f\u20269be", TEAL), ("Provider", "0x8a\u20264c1", VIOLET),
            ("Reviewer", "not needed", MUT_DIM)]
    for i, (role, addr, col) in enumerate(atts):
        ax = x + 22 + i * 206
        card(c, ax, y0 + 286, 194, 54, fill=PAPER, stroke=LINE_SOFT, r=10,
             lw=0.8, shadow=False)
        U.dot(c, ax + 16, y0 + 302, 3.4, col)
        text(c, ax + 28, y0 + 306, role, MED, 9.4, INK)
        text(c, ax + 28, y0 + 320, addr, MONO, 7.0, MUT_DIM, 0.2)
        text(c, ax + 28, y0 + 332, "signed" if i < 2 else "\u2014", MONO, 6.2,
             MUT_DIM, 0.2)

    rect(c, x + 1, y0 + 356, w - 2, 40, fill=VIOLET_SOFT)
    text(c, x + 22, y0 + 381, "\u20ac30 released \u00b7 09:41 UTC", MONO, 7.6,
         VIOLET_DEEP, 0.3)
    text(c, x + w - 22, y0 + 381, "tx 0x4c9\u20262a1", MONO, 7.6, INK_SOFT, 0.3,
         "right")
    para(c, x + 22, y0 + 414, w - 44,
         "If the confirmation never comes, the money stays frozen. Frozen is a "
         "valid state \u2014 it is not a polite reminder.", R, 8.4, 12, MUT)
    foot(c, idx, "Trust")


# ============================================================ 08b  philosophy
def s08b(c, idx):
    page(c)
    T.head(c, "08 \u2014 The philosophy",
           "Six principles, borrowed from Ethereum.",
           "Ethereum's contribution is not a currency, it is a way of agreeing "
           "without a boss: the rules are published before the money, nobody "
           "rewrites them afterwards in their own favour, and they are the same "
           "for a ministry and for a teenager with a stencil. 21 takes that shape "
           "and leaves out the speculation.",
           width=900, subw=700, y=104, size=34, leading=39)

    items = [
        ("Credible neutrality", VIOLET,
         "The base layer does not pick winners, and its operator cannot edit the "
         "rules for one participant.",
         "No paid placement and no dispatch algorithm: the target is the lowest "
         "published offer, recalculated by a rule, not by our judgement."),
        ("Permissionless", TEAL,
         "Nobody needs approval to use the network, and no gate decides who may.",
         "Anyone can paint the number, publish an ask, send an offer or verify a "
         "result; the kit is MIT and the mark has no owner."),
        ("Minimal trust", SKY,
         "You rely on rules that execute as published, not on a company's promise.",
         "The reward is fixed before the work, an advance needs a majority of the "
         "money contributed, payment follows both confirmations."),
        ("Verify, don't trust", YELLOW,
         "Anyone can inspect the state themselves instead of believing a report.",
         "Ask, offers, choice, before and after photos and the receipt stay "
         "public: a neighbour checks the bench, a donor follows each euro."),
        ("Public goods", CORAL,
         "Things everyone can use are funded deliberately, not extracted from "
         "users.",
         "The number, the kit, the receipts and the code are open; no token, no "
         "presale, no cut from the person doing the work."),
        ("No owner", PINK,
         "A protocol nobody can switch off for one person; ownership is given up "
         "rather than kept.",
         "No CEO cancels a settled quest and no company holds the funds; "
         "everything stays MIT, year 2 renounces registry ownership."),
    ]
    cw, ch, gap = 365, 164, 18
    x0, y0 = M, 236
    for i, (name, col, why, mech) in enumerate(items):
        cx = x0 + (i % 3) * (cw + gap)
        cy = y0 + (i // 3) * (ch + gap)
        card(c, cx, cy, cw, ch, fill=WHITE, stroke=LINE, r=16, shadow=True,
             shadow_dy=5)
        U.dot(c, cx + 22, cy + 26, 5, col)
        text(c, cx + 38, cy + 31, name, MED, 12.4, INK, -0.2)
        label(c, cx + cw - 20, cy + 27, "0%d" % (i + 1), MUT_DIM, 7.0, 1.4, "right")
        para(c, cx + 22, cy + 56, cw - 44, why, R, 8.8, 12.2, MUT, max_lines=2)
        label(c, cx + 22, cy + 92, "IN 21", col, 6.8, 1.5)
        para(c, cx + 22, cy + 106, cw - 44, mech, R, 8.8, 12.2, INK_SOFT,
             max_lines=3)

    yn = y0 + 2 * (ch + gap) + 12
    hline(c, M, yn, W - M, alpha(INK, 0.14))
    para(c, M, yn + 22, 780,
         "The published draft is local: no blockchain, no keys, no money moved. "
         "These are the rules as they are already written \u2014 in the interface "
         "and in the tests. Ethereum later adds one thing: they stop depending "
         "on us.", R, 9.2, 13.2, MUT_DIM, max_lines=3)
    text(c, W - M, yn + 28, "PHILOSOPHY \u00b7 NOT A TOKEN", MONO, 7.2, MUT_DIM,
         1.2, "right")
    foot(c, idx, "The philosophy")


# ============================================================ 09  civic layer
def s09(c, idx):
    page(c)
    T.head(c, "09 \u2014 The same machinery, in public space",
           "A bench in Oosterpark. Nine days, start to receipt.",
           "The same ask, offers and escrow \u2014 with the city as one of the "
           "askers and a repair as the deliverable. This is the layer the number "
           "sits on.", width=720, subw=540, y=104, size=34, leading=39)

    phone_shot(c, PHOTOS + "/bench-broken.jpg", 78, 226, 168, 330, rot=-2.5,
               caption="DAY 0 \u00b7 CHALKED BY A RESIDENT")
    doodle_arrow(c, 260, 388, 304, 370, VIOLET, 1.6, 0.25)
    phone_shot(c, PHOTOS + "/bench-fixed.jpg", 320, 226, 168, 330, rot=2.0,
               caption="DAY 9 \u00b7 FIXED AND ATTESTED")

    x = 560
    label(c, x, 226, "Task ledger \u00b7 public by default", VIOLET, 7.4, 1.5)
    rows = [
        ("Day 0", "Task published", "\u20ac420 target", YELLOW),
        ("Day 1", "3 bids received", "\u20ac380 \u2013 \u20ac455", INK_SOFT),
        ("Day 3", "84 residents voted", "62% Groenwerk", INK_SOFT),
        ("Day 4", "Escrow funded", "\u20ac420 in USDC", VIOLET),
        ("Day 7", "Milestone evidence", "6 photos + GPS", INK_SOFT),
        ("Day 9", "Dual attestation", "payment released", TEAL),
    ]
    y = 252
    vline(c, x + 6, y + 8, y + 8 + 42 * (len(rows) - 1), LINE, 1)
    for t, a, b, col in rows:
        U.dot(c, x + 6, y + 8, 4.2, col)
        text(c, x + 24, y + 12, t, MONO, 7.8, MUT_DIM, 0.4)
        text(c, x + 72, y + 12, a, MED, 10.2, INK)
        text(c, W - M, y + 12, b, MONO, 8.2, MUT, 0.2, "right")
        y += 42

    card(c, x, 526, W - M - x, 96, fill=WHITE, stroke=LINE, r=14, shadow=True)
    label(c, x + 18, 550, "What the resident keeps", VIOLET, 7.0, 1.4)
    text(c, x + 18, 574, "A public URL with the history, the contractor's name and "
                         "the final payment.", R, 9.0, MUT)
    text(c, x + 18, 596, "21.city/t/oosterpark-bench", MONO, 7.6, MUT_DIM, 0.2)
    text(c, x + 18, 612, "Paid by neighbours, a city budget or a matching pool \u2014 "
                         "the quest does not care.", R, 8.0, MUT_DIM)

    text(c, M, 600, "Same escrow, same proof, same receipt.", R, 9.0, MUT_DIM)
    text(c, M, 620, "The only difference is who answers.", R, 9.0, MUT_DIM)
    foot(c, idx, "Civic layer")


# ============================================================ 10  two doors
def s10(c, idx):
    page(c)
    T.head(c, "10 \u2014 One protocol, two doors",
           "A quest for a person. A task for a street.",
           "Both are the same object: a bounded ask with a reward and a proof. Only "
           "the payer and the verifier change.", width=820, subw=620, y=104,
           size=34, leading=39)

    xs = [M, 392, 800]
    y = 236
    hline(c, M, y, W - M, alpha(INK, 0.16))
    label(c, xs[0], y - 10, "Same object, two doors", MUT_DIM, 7.0, 1.4)
    label(c, xs[1], y - 10, "Personal quest", VIOLET, 7.4, 1.5)
    label(c, xs[2], y - 10, "Civic task", TEAL, 7.4, 1.5)
    y += 10
    rows = [
        ("Payer", "The asker, or a funder buying rewards in bulk",
         "Neighbours, a city budget, a matching pool"),
        ("Verifier", "Both sides confirm, then a reviewer on dispute",
         "Resident attestor + city partner + 72 h window"),
        ("Proof", "A note or a photo, attached to the record",
         "Signed capture, geofence, before and after"),
        ("Where", "Online, or anywhere in the city",
         "Public space only, with owner consent"),
        ("Cap", "One session, one visit, one small fix",
         "A per-task cap set by whoever funds it"),
        ("Dispute", "Panel: evidence, call, decision",
         "Same panel, plus a staked challenge window"),
    ]
    row_h = 50
    for i, (k, a, b) in enumerate(rows):
        yy = y + i * row_h
        if i % 2 == 0:
            rect(c, M - 12, yy + 2, W - 2 * M + 24, row_h - 6, fill=WHITE, r=8)
        text(c, xs[0], yy + 26, k, MED, 10.2, INK)
        para(c, xs[1], yy + 26, 380, a, R, 8.8, 12.2, MUT, max_lines=2)
        para(c, xs[2], yy + 26, 386, b, R, 8.8, 12.2, MUT, max_lines=2)
    hline(c, M, y + 6 * row_h - 8, W - M, LINE_SOFT, 0.8)

    card(c, M, 566, 552, 82, fill=VIOLET_SOFT, stroke=alpha(VIOLET, 0.35), r=14,
         shadow=True)
    label(c, M + 20, 588, "On-chain", VIOLET, 7.0, 1.4)
    text(c, M + 20, 610, "reward \u00b7 selection \u00b7 confirmation \u00b7 payment \u00b7 "
                         "reputation", MONO, 7.6, VIOLET_DEEP, 0.2)
    text(c, M + 20, 630, "No custody: every reward sits in its own contract.",
         R, 8.2, INK_SOFT)

    card(c, 648, 566, 560, 82, fill=WHITE, stroke=LINE, r=14, shadow=True)
    label(c, 668, 588, "Off-chain", TEAL, 7.0, 1.4)
    text(c, 668, 610, "names \u00b7 addresses \u00b7 session notes \u00b7 photos",
         MONO, 7.6, MUT, 0.2)
    text(c, 668, 630, "Hashes on-chain. Personal data deletable on request.",
         R, 8.2, MUT)
    foot(c, idx, "One protocol, two doors")


# ============================================================ 11  scale
def project_page(c, x, y, w, h):
    """Public project page: budget, milestones, tender, quests underneath."""
    U.browser(c, x, y, w, h, url="21.city/p/oosterpark-oost")
    y0 = y + 24
    label(c, x + 20, y0 + 16, "Public project \u00b7 street rebuild", MUT_DIM, 6.2, 1.4)
    chip(c, x + w - 132, y0 + 8, "OPEN TENDER", TEAL, TEAL_SOFT,
         alpha(TEAL, 0.4), 5.8, 16, 8)
    text(c, x + 20, y0 + 38, "Oosterpark Oost, Amsterdam", MED, 14, INK, -0.2)
    text(c, x + 20, y0 + 52,
         "Stadsdeel Oost + 3 housing corporations \u00b7 published 12 sep",
         R, 8.0, MUT)
    text(c, x + 20, y0 + 74, "\u20ac1.4m committed \u00b7 4 milestones", MED, 9.2, INK)
    text(c, x + w - 20, y0 + 74, "36% released", MONO, 7.4, TEAL, 0.2, "right")
    U.progress(c, x + 20, y0 + 84, w - 40, 0.36, 6, TEAL)
    rows = [
        ("M1", "Fencing + site survey", "PAID", "\u20ac90k", TEAL),
        ("M2", "Drains + water", "PAID", "\u20ac420k", TEAL),
        ("M3", "Pavement + benches", "LIVE", "\u20ac680k", VIOLET),
        ("M4", "Planting + hoarding art", "TENDER", "\u20ac210k", CORAL),
    ]
    ry = y0 + 102
    for code, name, status, amount, col in rows:
        card(c, x + 20, ry, w - 40, 26, fill=PAPER, stroke=LINE_SOFT, r=6, lw=0.7,
             shadow=False)
        U.dot(c, x + 34, ry + 13, 3.2, col)
        text(c, x + 46, ry + 12, f"{code} \u00b7 {name}", MED, 8.0, INK)
        text(c, x + w - 150, ry + 12, status, MONO, 5.6, col, 0.6, "right")
        text(c, x + w - 36, ry + 12, amount, MONO, 7.2, INK, 0.1, "right")
        ry += 30
    hline(c, x + 20, ry - 2, x + w - 20, LINE_SOFT, 0.7)
    text(c, x + 20, ry + 14, "12 quests under this project \u00b7 3 open now",
         MED, 8.4, INK)
    text(c, x + 20, ry + 27,
         "Each milestone pays on proof and can be split into quests.",
         R, 7.8, MUT)


def s11(c, idx):
    page(c)
    T.head(c, "11 \u2014 Scale",
           "A bench. A street. A whole construction site.",
           "The unit stays medium; the project does not. A city problem or a "
           "building site is published as a project page \u2014 budget, milestones, "
           "open tender \u2014 and paid out in quest-sized pieces, each with its own "
           "proof.", width=1060, subw=760, y=100, size=34, leading=39)

    tiers = [
        ("01", "Quest", "One person, one hour.", VIOLET,
         "A tutor, a psychologist, a handyman. Payer: a neighbour."),
        ("02", "Civic task", "One object, one fix.", TEAL,
         "A bench, a bike rack, a pothole. Payer: neighbours or a city budget."),
        ("03", "Project", "One block, one build.", CORAL,
         "A street, a school roof, a construction site. Payer: a city, a developer, "
         "a housing corporation."),
    ]
    for i, (n, k, sub, col, payer) in enumerate(tiers):
        x = M + i * 384
        card(c, x, 206, 368, 92, fill=WHITE, stroke=LINE, r=16, shadow=True,
             shadow_dy=5)
        U.badge(c, x + 30, 236, 14, n, col, WHITE, 9.6, MED)
        text(c, x + 52, 232, k, MED, 12.4, INK)
        text(c, x + 52, 246, sub, R, 8.2, MUT)
        para(c, x + 24, 266, 320, payer, R, 7.8, 11, MUT)

    project_page(c, M, 318, 580, 300)
    illustration(c, ART + "/project-block.png", 676, 318, 532)

    card(c, 700, 528, 484, 76, fill=WHITE, stroke=LINE, r=14, shadow=True)
    label(c, 720, 548, "The largest legal wall in the city", CORAL, 6.8, 1.3)
    para(c, 720, 562, 448,
         "A construction fence already has an owner. With consent, the mark goes "
         "there \u2014 plus a QR to the project page.", R, 8.0, 11.6, MUT)
    chip(c, 720, 582, "WITH THE OWNER'S CONSENT", INK, PAPER, alpha(INK, 0.14),
         5.6, 16, 8)
    foot(c, idx, "Scale")


# ============================================================ 12  devices
def s12(c, idx):
    page(c)
    T.head(c, "12 \u2014 Every device, one interface",
           "It has to work on the phone in a pocket.",
           "One responsive web app, installable as a PWA. Same data on five classes "
           "of device \u2014 including the kiosk for people who carry none of them, "
           "and the TV in a community centre.", width=556, subw=520, y=104,
           size=34, leading=39)

    blocks = [
        ("Phone first", VIOLET,
         "Built at 360 px, thumb-reachable actions, one decision per screen. Works "
         "one-handed, in the rain, with gloves on."),
        ("Then everything else", TEAL,
         "Tablet split view for offers, desktop for the review queue, kiosk for the "
         "street, TV for the community centre. One codebase \u2014 no second app."),
        ("Cheap to load", CORAL,
         "Under 150 KB of initial JS, no autoplay video, asks queued offline and "
         "sent when the signal returns."),
    ]
    y = 258
    for k, col, v in blocks:
        U.dot(c, M + 4, y + 4, 4.0, col)
        text(c, M + 20, y + 8, k, MED, 12.0, INK)
        para(c, M + 20, y + 28, 512, v, R, 9.0, 13.6, MUT)
        y += 74

    illustration(c, ART + "/devices.png", 640, 132, 568)
    chip(c, 1066, 470, "360 px \u2192 4K", WHITE, INK, alpha(INK, 0.16), 6.4, 19, 8,
         rot=-2)

    devs = [("Phone", "360\u2013430 px \u00b7 PWA install \u00b7 camera capture", VIOLET),
            ("Tablet", "split view \u00b7 offers and evidence side by side", TEAL),
            ("Desktop", "1280 px+ \u00b7 review queue, audits, exports", YELLOW),
            ("Kiosk", "public screen \u00b7 QR hands the quest to a phone", CORAL),
            ("TV", "any browser \u00b7 what the street asks for, no login", PINK)]
    for i, (k, v, col) in enumerate(devs):
        x = M + i * 231.5
        card(c, x, 496, 210, 96, fill=WHITE, stroke=LINE, r=14, shadow=True,
             shadow_dy=5)
        rect(c, x + 1, 508, 5, 72, fill=col, r=2.5)
        text(c, x + 18, 526, k, MED, 11.4, INK)
        para(c, x + 18, 544, 176, v, R, 8.0, 11.6, MUT)

    text(c, M, 622, "Tested on a \u20ac120 Android phone, a five-year-old laptop and "
                    "a 1080p TV before every release.", R, 8.8, MUT_DIM)
    foot(c, idx, "Devices")


# ============================================================ 13  interface
def s13(c, idx):
    page(c)
    T.head(c, "13 \u2014 Interface",
           "Warm on purpose, big on purpose.",
           "Civic software usually looks like a form. This looks like a message from "
           "a neighbour: paper colour, big targets, one action per screen \u2014 and "
           "the number as the only logo.", width=712, subw=560, y=104, size=34,
           leading=39)

    label(c, M, 286, "Palette", MUT_DIM, 7.0, 1.5)
    swatches = [(PAPER, "Paper", "#FAF2DE"), (INK, "Ink", "#17161B"),
                (VIOLET, "Signal", "#6C24DF"), (TEAL, "Verified", "#12B98A"),
                (YELLOW, "Attention", "#F6C445"), (CORAL, "Alert", "#F0603F"),
                (SKY, "Info", "#6F9BF5"), (PINK, "Joy", "#FF51BC")]
    for i, (col, name, hexv) in enumerate(swatches):
        sx = M + (i % 4) * 122
        sy = 300 + (i // 4) * 64
        rect(c, sx, sy, 38, 38, fill=col, stroke=alpha(INK, 0.14), r=11, lw=0.9)
        text(c, sx + 46, sy + 15, name, R, 8.2, INK)
        text(c, sx + 46, sy + 27, hexv, MONO, 6.0, MUT_DIM, 0.2)

    label(c, M, 448, "Type", MUT_DIM, 7.0, 1.5)
    text(c, M, 484, "Display", MED, 27, INK, -0.7)
    text(c, M + 118, 484, "Geist", MONO, 7.4, MUT_DIM, 0.3)
    text(c, M, 514, "Accent", SERIF_IT, 27, VIOLET, -0.3)
    text(c, M + 118, 514, "Instrument Serif Italic", MONO, 7.4, MUT_DIM, 0.3)
    text(c, M, 540, "Body 12 / 19", R, 10.6, MUT)
    text(c, M + 118, 540, "LABEL 8 / MONO / 1.6", MONO_MED, 7.4, VIOLET, 1.4)

    label(c, M, 574, "Components", MUT_DIM, 7.0, 1.5)
    bx = M
    bx += chip(c, bx, 588, "ASK FOR SOMETHING", WHITE, VIOLET, None, 6.8, 28, 12) + 8
    bx += chip(c, bx, 592, "MAKE AN OFFER", INK, WHITE, alpha(INK, 0.18), 6.8, 22, 10) + 8
    bx += chip(c, bx, 592, "IN ESCROW", VIOLET, VIOLET_SOFT, alpha(VIOLET, 0.4), 6.6, 22, 9)
    U.progress(c, M, 630, 300, 0.62, 8, VIOLET)
    text(c, M + 314, 637, "\u20ac18 of \u20ac30 claimed", MONO, 7.2, MUT, 0.2)

    px, py, pw, ph = 962, 186, 214, 440
    rect(c, px + 2, py + 8, pw, ph, fill=SHADOW, r=26)
    rect(c, px, py, pw, ph, fill=INK, r=26)
    rect(c, px + 6, py + 6, pw - 12, ph - 12, fill=WHITE, r=22)
    rect(c, px + pw / 2 - 20, py + 12, 40, 8, fill=INK, r=4)
    U.quest_screen(c, px + 10, py + 28, pw - 20, ph - 74, kind="feed")
    chip(c, px + pw - 30, py + ph - 24, "21", VIOLET, WHITE, None, 8.0, 26, 10,
         rot=8, shadow=True)
    chip(c, 690, 560, "ONE NUMBER, NO LOGO", VIOLET, WHITE, None, 7.2, 26, 12,
         rot=-4, shadow=True)
    doodle_arrow(c, 872, 578, 930, 578, VIOLET, 1.5, 0.12)
    sparkle(c, 884, 542, 6, YELLOW)
    sparkle(c, 676, 522, 4.5, PINK)
    foot(c, idx, "Interface")


# ============================================================ 14  PR machine
def clip_frame(c, path, x, y, w, h, caption, focus=0.5, chalk=True,
               chalk_xy=(0.64, 0.76), chalk_size=0.40):
    """A vertical, phone-shot clip: photo, chalked number, playback chrome."""
    rect(c, x + 2, y + 6, w, h, fill=SHADOW, r=20)
    rect(c, x, y, w, h, fill=INK, r=20)
    ph = h - 58
    photo(c, path, x + 4, y + 4, w - 8, ph, r=14, focus=focus)
    if chalk:
        U.chalk_number(c, x + w * chalk_xy[0], y + ph * chalk_xy[1],
                       w * chalk_size, WHITE, rot=-7, lw=2.5, alpha_=0.95)
    cx, cy = x + w / 2, y + ph / 2
    c.saveState()
    c.setFillColor(alpha(WHITE, 0.86))
    c.circle(cx, T.ty(cy), 13, stroke=0, fill=1)
    c.setFillColor(INK)
    p = c.beginPath()
    p.moveTo(cx - 3.4, T.ty(cy) + 6.4)
    p.lineTo(cx + 6.2, T.ty(cy))
    p.lineTo(cx - 3.4, T.ty(cy) - 6.4)
    p.close()
    c.drawPath(p, stroke=0, fill=1)
    c.restoreState()
    rect(c, x + 4, y + h - 54, w - 8, 50, fill=WHITE, r=10)
    U.badge(c, x + 18, y + h - 37, 8, "21", VIOLET, WHITE, 6.2, MED)
    text(c, x + 30, y + h - 40, "@a.neighbour", MED, 5.8, INK)
    text(c, x + 12, y + h - 26, caption, MONO, 4.6, MUT, 0.2)
    U.progress(c, x + 12, y + h - 14, w - 24, 0.36, 2.4, VIOLET)


def s14(c, idx):
    page(c)
    T.head(c, "14 \u2014 The PR machine",
           "21 has to become a meme, not an ad.",
           "One large PR agency on retainer, paid per published placement and per "
           "settled quest \u2014 not for impressions. The formats are cheap on "
           "purpose: a number, a phone, a wall, six seconds.", width=1000,
           subw=760, y=100, size=34, leading=39)

    label(c, M, 222, "What people actually film", MUT, 7.0, 1.6)
    clips = [
        (PHOTOS + "/bench-broken.jpg", "01 \u00b7 CHALK, 6 SEC",
         "chalk \u00b7 6 sec \u00b7 oosterpark", 0.52, True, (0.66, 0.78), 0.40),
        (PHOTOS + "/crew.jpg", "02 \u00b7 BEFORE / AFTER, 15 SEC",
         "fixed \u00b7 9 days \u00b7 receipt", 0.48, True, (0.80, 0.80), 0.32),
        (ART + "/project-block.png", "03 \u00b7 THE HOARDING, 9 SEC",
         "hoarding \u00b7 9 sec \u00b7 permit", 0.5, False, (0.64, 0.76), 0.40),
        (PHOTOS + "/bike-rack.jpg", "04 \u00b7 FIND THE 21, 30 SEC",
         "marker \u00b7 30 sec \u00b7 lift 2", 0.55, True, (0.68, 0.80), 0.38),
    ]
    for i, (path, cap, meta, focus, chalk, cxy, csize) in enumerate(clips):
        x = M + i * 152
        clip_frame(c, path, x, 232, 136, 220, meta, focus=focus, chalk=chalk,
                   chalk_xy=cxy, chalk_size=csize)
        label(c, x, 468, cap, MUT, 6.0, 1.1)

    card(c, M, 488, 592, 140, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 20, 512, "The meme is the media plan", VIOLET, 7.2, 1.4)
    para(c, M + 20, 532, 548,
         "A brand ages; a number doesn't. 21 looks like it was already there, "
         "which is why it fits the era without a caption explaining it.",
         R, 9.0, 13.4, MUT)
    bx = M + 20
    for ch, bg in (("TEN TEMPLATES", VIOLET_SOFT), ("ONE NUMBER", TEAL_SOFT),
                   ("NO EXPLANATION", YELLOW_SOFT)):
        bx += chip(c, bx, 560, ch, INK, bg, None, 5.8, 18, 8) + 7
    text(c, M + 20, 602, "We don't need it liked. We need it repeated.",
         MED, 10.6, INK)
    squiggle(c, M + 20, 612, 300, TEAL, 2.0, 1.8, 5)

    card(c, 684, 232, 524, 150, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, 706, 256, "One large agency, three jobs \u00b7 above the floor", VIOLET, 7.0, 1.4)
    jobs = [
        ("01", "Buy reach by the unit",
         "20 creators per city, paid per published placement. Invoices public."),
        ("02", "Seed the format",
         "A six-second TikTok script, ten meme templates, the stencil in every caption."),
        ("03", "Hand it over",
         "City permissions, consented walls, a QR to the task page in every video."),
    ]
    for i, (n, k, d) in enumerate(jobs):
        y = 278 + i * 34
        text(c, 706, y + 9, n, MONO, 6.6, VIOLET, 0.6)
        text(c, 730, y + 9, k, MED, 8.8, INK)
        text(c, 730, y + 20, d, R, 7.4, MUT)

    card(c, 684, 394, 524, 112, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, 706, 418, "What we count", TEAL, 7.0, 1.4)
    stats = [("Settled quests", "per 1,000 views, not CPM."),
             ("Marks we didn't pay for", "photographed by strangers."),
             ("Cost per settled quest", "published every month.")]
    for i, (k, d) in enumerate(stats):
        x = 706 + i * 166
        text(c, x, 446, k, MED, 8.2, INK)
        text(c, x, 459, d, R, 7.2, MUT)
    text(c, 706, 490, "Reach is a means. A finished, paid quest is the only result.",
         R, 7.8, MUT_DIM)

    card(c, 684, 518, 524, 110, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, 706, 542, "Guardrails", CORAL, 7.0, 1.4)
    para(c, 706, 562, 484,
         "No paid engagement, no bots, no fake accounts, no astroturfed "
         "testimonials. Every creator discloses the fee.", R, 8.0, 12, MUT)
    text(c, 706, 594, "The number travels without us. That is the point.",
         MED, 8.4, INK)
    bx = chip(c, 706, 604, "NO LOGO \u00b7 NO SLOGAN", INK, PAPER,
              alpha(INK, 0.14), 5.6, 16, 8) + 8
    chip(c, 706 + bx, 604, "AT THE FLOOR: NO AGENCY", VIOLET, VIOLET_SOFT, None,
         5.6, 16, 8)
    foot(c, idx, "The PR machine")


# ============================================================ 15  the kit
def s15(c, idx):
    page(c)
    T.head(c, "15 \u2014 The kit, and how it travels",
           "Nobody needs our permission to paint it.",
           "A stencil, a sticker sheet, a six-line README, published under MIT and "
           "printed locally. That is the whole distribution strategy \u2014 with the "
           "campaign behind it.", width=620, subw=530, y=104, size=34, leading=39)

    label(c, M, 258, "In the kit", VIOLET, 7.0, 1.5)
    kit = ["An A4 stencil: two strokes, one cut, any colour.",
           "A sticker sheet: twelve 21s, for broken things.",
           "A chalk template for asphalt and one for a lift door.",
           "A task-ticket template to photograph next to the mark.",
           "A six-second vertical video script, with no speaking.",
           "The rules on the first line of the sheet: ask the owner."]
    y = 280
    for i, s_ in enumerate(kit):
        text(c, M, y, f"{i + 1:02d}", MONO, 7.0, MUT_DIM, 0.8)
        text(c, M + 26, y, s_, R, 9.4, INK if i < 5 else VIOLET)
        hline(c, M, y + 8, 592, LINE_SOFT, 0.6)
        y += 30

    card(c, M, 474, 540, 146, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 20, 498, "Three waves", VIOLET, 7.2, 1.4)
    waves = [("Wave 1 \u00b7 month 1", "three creators paid per placement; an agency "
                                         "and 20 creators above the floor."),
             ("Wave 2 \u00b7 months 2\u20134", "city permissions make walls legal; every "
                                              "settled quest posts its own before/after."),
             ("Wave 3 \u00b7 months 4\u20136", "groups we have never met print the "
                                              "sheet. The only metric we cannot buy.")]
    wy = 522
    for k, v in waves:
        text(c, M + 20, wy, k, MED, 8.6, INK)
        wy = para(c, M + 148, wy, 372, v, R, 8.2, 12, MUT) + 8

    illustration(c, ART + "/stencil-kit.png", 660, 132, 548)
    chip(c, 1166, 156, "PRINT IT YOURSELF", WHITE, INK, None, 6.4, 20, 8, rot=3)

    card(c, 660, 456, 548, 148, fill=CORAL_SOFT, stroke=alpha(CORAL, 0.35), r=16,
         shadow=True)
    label(c, 682, 480, "What we will not do", CORAL, 7.2, 1.4)
    para(c, 682, 502, 504,
         "We don't pay for illegal paint, we don't instruct anyone to break a rule, "
         "and we don't claim ownership of a number. Consented walls get artists and "
         "fees; everything else is other people's art, at their own risk.",
         R, 9.0, 13.6, INK_SOFT)
    text(c, 682, 578, "The kit is the campaign. The board is what makes it true.",
         MED, 9.4, INK)
    foot(c, idx, "The kit")


# ============================================================ 16  the floor
def s16(c, idx):
    page(c)
    T.head(c, "16 \u2014 The floor",
           "The floor, in units.",
           "\u20ac7,500 is the smallest round that moves: six months, one city, one "
           "person full-time. Every line is a unit price \u00d7 a quantity, and the "
           "table adds up exactly.",
           width=680, subw=600, y=104, size=38, leading=42)

    # left — the number itself, in a hand
    label(c, M, 236, "The floor \u00b7 six months, one city", VIOLET, 7.2, 1.5)
    text(c, M, 318, "\u20ac", SEMI, 52, VIOLET, -1)
    text(c, M + 34, 318, "7,500", HAND_B, 118, INK, -2)
    squiggle(c, M + 4, 330, 250, TEAL, 2.6, 2.4, 5)
    text(c, M, 352, "my wage, not a market rate", HAND, 20, VIOLET, 0.2)

    # left — the split that returns above the floor
    card(c, M, 386, 552, 244, fill=WHITE, stroke=LINE, r=16, shadow=True,
         shadow_dy=6)
    label(c, M + 22, 410, "Above the floor \u00b7 same split at any size",
          VIOLET, 7.0, 1.4)
    rows = [("45%", "quest and project rewards in escrow"),
            ("15%", "consented walls, artists, materials"),
            ("15%", "PR and the kit"),
            ("10%", "verification and field ops"),
            ("6%", "safety, legal, insurance"),
            ("5%", "ops and infrastructure"),
            ("4%", "reserve")]
    yy = 436
    for pct, what in rows:
        text(c, M + 22, yy, pct, MONO_MED, 8.6, VIOLET, 0.4)
        text(c, M + 70, yy, what, R, 9.0, INK_SOFT)
        yy += 20
    para(c, M + 22, 578, 508,
         "My hours do not take a share: they stay at cost. A smaller round ships "
         "fewer quests and walls \u2014 never cheaper ones.",
         R, 8.4, 12, MUT)

    # right — the arithmetic
    x0, x1, x2 = 672, 980, 1208
    label(c, x0, 236, "Line", MUT_DIM, 7.0, 1.4)
    label(c, x1, 236, "Unit", MUT_DIM, 7.0, 1.4)
    label(c, x2, 236, "\u20ac", MUT_DIM, 7.0, 1.4, "right")
    hline(c, x0, 248, x2, alpha(INK, 0.15))

    budget = [
        ("Code \u2014 protocol, PWA, contract, kit", "250 \u20b9/h \u00d7 960 h",
         "2,500", True),
        ("Quest rewards in escrow", "\u20ac30 \u00d7 60", "1,800", False),
        ("Consented walls \u2014 fee, paint, lift", "\u20ac300 \u00d7 3", "900",
         False),
        ("Verification and attestors", "60 checks + panel", "400", False),
        ("PR \u2014 creators, per placement", "\u20ac100 \u00d7 3", "300", False),
        ("Kit \u2014 stencil, stickers, chalk", "\u20ac0.50 \u00d7 500", "250",
         False),
        ("Safety, legal, insurance", "at cost", "400", False),
        ("Infrastructure", "\u20ac25 \u00d7 6", "150", False),
        ("Reserve", "10.7%", "800", False),
    ]
    y = 268
    for name, unit, total, is_code in budget:
        if is_code:
            rect(c, 660, y - 8, 560, 26, fill=VIOLET_SOFT, r=6)
            chip(c, 1112, y - 8, "AT COST", VIOLET, WHITE, None, 5.0, 14, 6)
        text(c, x0 + 12, y, name, R, 9.0, INK)
        text(c, x1, y, unit, MONO, 7.2, MUT)
        text(c, x2 - 12, y, total, MONO_MED, 8.8, INK, 0.2, "right")
        hline(c, x0, y + 10, x2, LINE_SOFT, 0.6)
        y += 30

    hline(c, x0, y + 2, x2, alpha(INK, 0.15))
    text(c, x0 + 12, y + 26, "The floor", MED, 11, INK)
    text(c, x2 - 12, y + 30, "\u20ac7,500", HAND_B, 28, INK, 0, "right")
    para(c, 660, y + 52, 548,
         "At the floor there is no agency retainer: three creators, paid per "
         "published placement. Above it, wave 1 is an agency and 20 creators a city.",
         R, 8.2, 12, MUT)
    foot(c, idx, "The floor")


# ============================================================ 17  grant shapes
def s17(c, idx):
    page(c)
    T.head(c, "17 \u2014 What a round buys",
           "One floor, then scope.",
           "The unit prices set the floor; the round sets the ceiling. These are the "
           "three shapes the programme takes, priced in scope \u2014 not in promises.",
           width=800, subw=620, y=104, size=34, leading=39)

    sizes = [
        ("01", "The floor \u00b7 \u20ac7,500", "One city, one board", VIOLET, [
            "60 quests, 3 consented walls",
            "A street project page + kiosk pilot",
            "Kit v1 under MIT",
            "3 creators, no agency retainer",
            "10 askers recruited by hand"]),
        ("02", "About \u20ac30,000", "Three cities, a real record", TEAL, [
            "250 quests, 9 consented walls",
            "2 projects: a street, a construction site",
            "Agency wave 1: 20 creators a city",
            "Verification panel + kiosk pilot",
            "Kit v1 in two languages"]),
        ("03", "About \u20ac100,000", "Nine cities, the whole campaign", CORAL, [
            "900 quests, 21 consented walls",
            "3 large projects, paid by milestone",
            "Kiosks in three cities",
            "A public export anyone can audit",
            "Kit v2 in three languages \u00b7 PR waves 2\u20133"]),
    ]
    for i, (n, kick, title, col, bullets_) in enumerate(sizes):
        x = M + i * 384
        card(c, x, 226, 368, 280, fill=WHITE, stroke=LINE, r=16, shadow=True,
             shadow_dy=6)
        U.badge(c, x + 28, 256, 14, n, col, WHITE, 9.4, MED)
        text(c, x + 54, 262, kick.upper(), MONO_MED, 7.0, col, 1.2)
        text(c, x + 24, 300, title, MED, 15, INK, -0.2)
        hline(c, x + 24, 316, x + 344, LINE_SOFT, 0.8)
        yy = 344
        for b in bullets_:
            U.dot(c, x + 4, yy - 3, 2.2, col)
            yy = para(c, x + 18, yy, 320, b, R, 9.0, 13.2, MUT) + 14
        chip(c, x + 24, 462, "SAME SOFTWARE \u00b7 SAME ESCROW", INK, PAPER,
             alpha(INK, 0.14), 6.0, 18, 7)

    card(c, M, 536, W - 2 * M, 82, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 558, "The floor is arithmetic", VIOLET, 7.2, 1.4)
    text(c, M + 22, 584, "Every line is a unit price \u00d7 a quantity. Below it we "
                         "ship the kit, one city and the escrow contract \u2014 and "
                         "say publicly that is what happened.", R, 9.2, MUT)
    text(c, W - M - 22, 584, "a floor, not a wish", MONO, 7.4, MUT_DIM, 0.3, "right")
    foot(c, idx, "What a round buys")


# ============================================================ 18  milestones
def s18(c, idx):
    page(c)
    T.head(c, "18 \u2014 Milestones",
           "Paid when it exists.",
           "Shares, not sums: each milestone releases a fixed percentage of whatever "
           "the grant turns out to be. No milestone closes on a slide.",
           width=780, subw=580, y=104, size=34, leading=39)

    chip(c, 922, 146, "PAID WHEN IT EXISTS", VIOLET, WHITE, None, 7.8, 26, 12,
         rot=3, shadow=True)
    sparkle(c, 900, 128, 6.5, YELLOW)
    sparkle(c, 1166, 186, 4.5, TEAL)

    rows = [
        ("M1", "Month 1", "Board live + kit v1",
         "1 city live: ask, offers, escrow, settlement. Kit v1 published. 10 quests done.",
         10, VIOLET),
        ("M2", "Months 2\u20133", "3 cities, 150 quests",
         "150 quests completed, 7 consented walls, first dispute resolved in public.",
         30, TEAL),
        ("M3", "Months 3\u20134", "Public space + first project",
         "Civic tasks live with attestors; 60 repairs settled; first project page "
         "(a street) with milestone escrow; kiosk pilot.",
         25, YELLOW),
        ("M4", "Months 4\u20135", "9 cities, 900 quests, 3 projects",
         "900 quests, 21 consented walls, 3 large projects paid by milestone; "
         "100% of walls with written consent.",
         25, CORAL),
        ("M5", "Month 6", "Kit v2 + open export",
         "Everything exported, kit v2 under MIT, exhibition of the 21 walls.",
         10, SKY),
    ]
    y = 234
    hline(c, M, y, W - M, alpha(INK, 0.15))
    label(c, 100, y - 10, "Milestone", MUT_DIM, 7.2, 1.4)
    label(c, 470, y - 10, "Acceptance criterion", MUT_DIM, 7.2, 1.4)
    label(c, 1030, y - 10, "Share", MUT_DIM, 7.2, 1.4, "right")
    y += 16
    for code, month, name, crit, share, col in rows:
        U.badge(c, M + 14, y + 22, 14, code, col, WHITE, 9.4, MED)
        text(c, M + 40, y + 16, month, MONO, 7.2, MUT_DIM, 0.3)
        text(c, M + 40, y + 32, name, MED, 10.4, INK)
        para(c, 470, y + 22, 500, crit, R, 8.8, 12.4, MUT, max_lines=2)
        text(c, 1030, y + 26, f"{share}%", MONO, 8.6, INK, 0.2, "right")
        hline(c, M, y + 44, 1030, LINE_SOFT, 0.7)
        y += 54

    card(c, M, 560, W - 2 * M, 86, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 584, "Cumulative release", VIOLET, 7.2, 1.4)
    cum = [("M1", 10), ("M2", 40), ("M3", 65), ("M4", 90), ("M5", 100)]
    for i, (k, v) in enumerate(cum):
        x = M + 24 + i * 216
        text(c, x, 612, k, MONO, 7.2, MUT_DIM, 0.4)
        U.progress(c, x + 22, 607, 120, v / 100, 6, alpha(VIOLET, 0.85))
        text(c, x + 148, 613, f"{v}%", MONO, 7.6, MUT, 0.2)
    text(c, M + 24, 636, "An unmet criterion means an unpaid milestone, not a "
                         "renegotiation.", R, 8.4, MUT_DIM)
    foot(c, idx, "Milestones")


# ============================================================ 19  team
def s19(c, idx):
    page(c)
    T.head(c, "19 \u2014 Team",
           "One person, and a phone full of strangers.",
           "At the floor it is me, full-time, plus a paid curator and paid creators "
           "per city. The other two roles are the plan for a larger round \u2014 not "
           "people claimed as signed.", width=820, subw=640, y=104, size=34, leading=39)

    people = [
        ("Protocol & product", "contracts \u00b7 escrow \u00b7 app", VIOLET,
         "Former active graffiti artist: a wall network across a dozen countries. "
         "Writes the Solidity contracts, the PWA capture flow and the kiosk build.",
         "[name]  \u00b7  [github]", "full time \u00b7 6 months"),
        ("Programme lead", "cities \u00b7 walls \u00b7 permissions", TEAL,
         "Runs the consented walls, the open calls and the consent paperwork with a "
         "paid curator in each city.", "[name]  \u00b7  [linkedin]",
         "at a larger round"),
        ("Field ops & trust", "attestors \u00b7 disputes \u00b7 safety", CORAL,
         "Recruits attestors, runs the dispute panel, and enforces the safety rules "
         "when a quest goes wrong in public.", "[name]  \u00b7  [linkedin]",
         "at a larger round"),
    ]
    for i, (role, key, col, desc, link, note) in enumerate(people):
        x = M + i * 384
        card(c, x, 208, 368, 190, fill=WHITE, stroke=LINE, r=16, shadow=True,
             shadow_dy=6)
        rect(c, x + 22, 230, 42, 42, fill=alpha(col, 0.15), r=12)
        text(c, x + 43, 258, role[0], MED, 16, col, 0, "center")
        text(c, x + 78, 248, role, MED, 11.4, INK)
        text(c, x + 78, 264, key, MONO, 6.6, MUT, 0.3)
        para(c, x + 22, 292, 324, desc, R, 9.0, 13.4, MUT)
        hline(c, x + 22, 350, x + 346, LINE_SOFT, 0.8)
        text(c, x + 22, 372, link, MONO, 7.4, MUT, 0.3)
        text(c, x + 346, 372, note, MONO, 6.4, MUT_DIM, 0.3, "right")

    card(c, M, 422, 552, 116, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 446, "PR partner \u00b7 above the floor, one retainer", VIOLET, 7.0, 1.4)
    text(c, M + 22, 470, "Creators, not ad inventory", MED, 10.4, INK)
    para(c, M + 22, 488, 508,
         "A large agency places 20 creators per city on the number; we pay for reach "
         "the way we pay for paint \u2014 by the unit, invoice published. At the "
         "floor this card is empty: three creators, per placement.", R, 8.6, 12.6, MUT)

    card(c, 648, 422, 560, 116, fill=TEAL_SOFT, stroke=alpha(TEAL, 0.4), r=16,
         shadow=True)
    label(c, 670, 446, "Curators & creators \u00b7 paid per city", TEAL, 7.0, 1.4)
    text(c, 670, 470, "Never asked to work for visibility", MED, 10.4, INK)
    text(c, 670, 492, "Curator: shortlists artists, sits on the open call.", R, 8.6,
         INK_SOFT)
    text(c, 670, 508, "Creator: films the mark, names the city, keeps the fee.", R,
         8.6, INK_SOFT)
    text(c, 670, 526, "Both on invoice. Both named in the close-out report.", MONO,
         6.8, MUT, 0.2)

    hline(c, M, 560, W - M, alpha(INK, 0.12))
    label(c, M, 584, "Open role, funded by tranche 2", MUT_DIM, 7.0, 1.4)
    text(c, M, 606, "Verification & safety lead \u2014 runs reviewer panels in the "
                    "pilot cities.", R, 9.0, MUT)
    label(c, 780, 584, "Not applying for", MUT_DIM, 7.0, 1.4)
    text(c, 780, 606, "A marketing department, a token, an office.",
         R, 9.0, MUT)
    foot(c, idx, "Team")


# ============================================================ 20  metrics
def s20(c, idx):
    page(c)
    T.head(c, "20 \u2014 Success metrics",
           "Targets, not traction.",
           "21 is pre-launch. These are the numbers we commit to publishing at "
           "close-out, with the raw registry export next to them.", width=820,
           subw=620, y=104, size=36, leading=41)

    chip(c, 936, 138, "RECEIPTS, NOT VIBES", PINK, WHITE, None, 7.8, 28, 13,
         rot=-3, shadow=True)
    sparkle(c, 906, 174, 6, YELLOW)
    sparkle(c, 1180, 174, 4.5, VIOLET)

    metrics = [
        ("60", "quests completed through escrow", "escrow events", VIOLET),
        ("7 days", "median from ask to confirmed", "timestamps", TEAL),
        ("40%", "askers who post a second quest", "repeat asks", YELLOW),
        ("21", "walls in the registry \u2014 3 paid by us", "consent registry", CORAL),
        ("0", "euros paid outside escrow", "reconciliation", SKY),
        ("5", "device classes tested every week", "release checklist", PINK),
    ]
    for i, (big, small, src, col) in enumerate(metrics):
        col_i, row = i % 3, i // 3
        x = M + col_i * 384
        y = 222 + row * 142
        card(c, x, y, 368, 128, fill=WHITE, stroke=LINE, r=16, shadow=True,
             shadow_dy=5)
        rect(c, x + 1, y + 10, 6, 108, fill=col, r=3)
        text(c, x + 24, y + 52, big, MED, 32, INK, -0.9)
        para(c, x + 24, y + 82, 300, small, R, 9.2, 12.6, MUT)
        text(c, x + 24, y + 112, "source: " + src, MONO, 6.4, MUT_DIM, 0.2)

    card(c, M, 520, W - 2 * M, 106, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 544, "Guardrails \u2014 we fail if these move the wrong way",
          CORAL, 7.2, 1.4)
    guard = [("Off-escrow payments", "0, ever"), ("Disputes", "< 8% of quests"),
             ("Fraud", "< 1% of released value"), ("Walls without consent", "0")]
    for i, (k, v) in enumerate(guard):
        x = M + 24 + i * 276
        text(c, x, 574, v, MED, 11, INK)
        text(c, x, 594, k, R, 8.2, MUT_DIM)
    text(c, M + 24, 616, "Floor targets; a larger round scales the same metrics to "
                         "250 and 900 quests, 9 and 21 paid walls. Targets for month "
                         "six, not results.", R, 8.0, MUT_DIM)
    foot(c, idx, "Metrics")


# ============================================================ 21  risks
def s21(c, idx):
    page(c)
    T.head(c, "21 \u2014 Risks",
           "What could go wrong, and what we do about it.",
           "A meme and a marketplace fail differently. Both failure lists are written "
           "down before the first euro moves.", width=780, subw=560, y=104, size=34,
           leading=39)

    xs = [M, 336, 782]
    y = 246
    hline(c, M, y, W - M, alpha(INK, 0.18))
    for i, col in enumerate(("Threat", "Why it is real", "Mitigation in the MVP")):
        label(c, xs[i], y - 10, col, MUT_DIM, 7.2, 1.5)
    y += 8
    rows = [
        ("The mark gets hijacked",
         "Anyone can paint 21, including people we would not choose.",
         "We never claim ownership. The task page is the only canonical link, and the kit states the rules on its first line."),
        ("Illegal paint in our name",
         "Stencils travel; walls have owners.",
         "We never pay or instruct. Consented walls get artists and fees; the kit says ask first, in three languages."),
        ("A cold, empty board",
         "An empty board attracts nobody, and the number stops meaning anything.",
         "Seed three paid civic tasks per city and 20 askers recruited by curators, before any PR spend."),
        ("Two strangers meet",
         "In-person quests carry real physical risk.",
         "Public first meetings, ID above \u20ac50, panic button, no cash off-platform, one-tap report that pauses a profile."),
        ("Bad work, bad practice",
         "An unsupervised therapist, a repair that fails in a week.",
         "Category rules, supervised trainees only, a 14-day workmanship window, delisting after two upheld disputes."),
        ("Escrow bug",
         "Contracts hold real money from day one.",
         "Two audits before mainnet, invariant fuzzing, per-quest caps, 3-of-5 guardian pause with 48 h delay."),
    ]
    row_h = 54
    for i, (a, b, cc_) in enumerate(rows):
        yy = y + 10 + i * row_h
        if i % 2 == 0:
            rect(c, M - 12, yy - 6, W - 2 * M + 24, row_h - 6, fill=WHITE, r=8)
        text(c, xs[0], yy + 22, a, MED, 9.4, INK)
        para(c, xs[1], yy + 22, 386, b, R, 8.8, 12.2, MUT, max_lines=2)
        para(c, xs[2], yy + 22, 426, cc_, R, 8.8, 12.2, MUT, max_lines=2)

    text(c, M, 626, "Open question for reviewers: what is the smallest proof that a "
                    "stranger did the work \u2014 and how few clicks should it cost?",
         L, 9.2, MUT_DIM)
    foot(c, idx, "Risks")


# ============================================================ 22  close
def s22(c, idx):
    page(c)
    illustration(c, ART + "/cover-21.png", 660, 148, 560)
    chip(c, 1196, 168, "21", VIOLET, WHITE, None, 11, 38, 12, rot=8, shadow=True)

    logotype(c, M, 26, 26, INK, VIOLET)
    label(c, M + 96, 80, "the mark, and the exchange under it", MUT, 8.0, 1.5)
    label(c, M, 204, "The ask", VIOLET, 8.8, 1.9)

    text(c, M, 274, "Bring a wall.", MED, 42, INK, -1.0)
    text(c, M, 322, "Bring a quest.", SERIF_IT, 44, VIOLET, -0.8)
    squiggle(c, M + 4, 338, 320, TEAL, 2.8, 2.4, 6)

    para(c, M, 372, 500,
         "The floor is \u20ac7,500: six months, one city, one person, sixty quests, "
         "three walls. Whatever arrives above it is split the same way \u2014 quest "
         "and project rewards first, consented walls second, the kit always.",
         R, 11.6, 17.6, MUT)

    card(c, M, 486, 500, 96, fill=WHITE, stroke=LINE, r=16, shadow=True, shadow_dy=6)
    text(c, M + 22, 520, "21.city", MED, 15, INK, 0.2)
    text(c, M + 22, 542, "hello@21.city  \u00b7  github.com/horaanlika-droid/21movement-",
         MONO, 7.4, MUT, 0.3)
    text(c, M + 22, 564, "Open source \u00b7 MIT \u00b7 no token \u00b7 a floor, not a wish",
         MONO, 7.0, MUT_DIM, 0.4)

    text(c, M, 620, "Paint the number. Then post the task.", HAND, 13, MUT_DIM, 0.2)
    text(c, W - M, 646, f"{idx:02d} / {TOTAL}", MONO, 8.0, MUT_DIM, 0.8, "right")
    chip(c, 596, 606, "STENCIL \u00b7 STICKER \u00b7 CHALK", INK, PAPER,
         alpha(INK, 0.14), 6.4, 20, 8, rot=-2)


SLIDES = [s01, s02, s03, s04, s05, s06, s07, s08, s08b, s09, s10,
          s11, s12,
          s13, s14, s15, s16, s17, s18, s19, s20, s21, s22]
assert len(SLIDES) == TOTAL


def build(path):
    c = rl_canvas.Canvas(path, pagesize=(W, H))
    c.setTitle("21 \u2014 the number and the exchange")
    c.setAuthor("21")
    c.setSubject("Ethereum ecosystem grant application \u2014 2026")
    c.setKeywords("Ethereum, public goods, civic infrastructure, escrow, grant, "
                  "mutual aid, quests, construction, projects, murals")
    for i, fn in enumerate(SLIDES, start=1):
        fn(c, i)
        c.showPage()
    c.save()


if __name__ == "__main__":
    out = os.path.join(T.OUT, "21-grant-deck.pdf")
    build(out)
    print("wrote", out)
    if "--preview" in sys.argv:
        import pypdfium2 as pdfium
        doc = pdfium.PdfDocument(out)
        for i in range(len(doc)):
            pg = doc[i].render(scale=1.2).to_pil()
            pg.save(os.path.join(T.PREVIEW, f"p{i + 1:02d}.png"))
        print("previews:", len(doc))
