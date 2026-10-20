"""21 — grant deck. Ethereum-native civic infrastructure, ethereum.org look.

20 slides, 1280 x 720 pt, all text in code. Run `python3 build.py --preview`
from this folder to rebuild the PDF and the PNG previews.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.pdfgen import canvas as rl_canvas

import theme as T
import uikit as U
from theme import (CORAL, CORAL_SOFT, H, INK, INK_SOFT, L, LINE, LINE_SOFT, M,
                   MED, MONO, MONO_MED, MUT, MUT_DIM, PAPER, PAPER_2, PINK,
                   PINK_SOFT, R, SEMI, SERIF, SERIF_IT, SHADOW, SKY, SKY_SOFT,
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
TOTAL = 20


def foot(c, idx, section=""):
    footer(c, idx, section)


def step_badge(c, cx, cy, n, col, r=17):
    U.badge(c, cx, cy, r, n, col, WHITE, r * 0.82, MED)


# ============================================================ 01  cover
def s01(c, idx):
    page(c)
    illustration(c, ART + "/cover-city.png", 762, -70, 478)

    logotype(c, M, 82, 26, INK, VIOLET)
    label(c, M + 96, 80, "Ethereum-native civic infrastructure", MUT, 8.0, 1.5)
    chip(c, W - M - 104, 64, "GRANT 2026", VIOLET, WHITE, alpha(VIOLET, 1),
         7.2, 22, 9, rot=3, shadow=True)

    sparkle(c, 566, 196, 9, YELLOW)
    sparkle(c, 700, 300, 6, CORAL)
    label(c, M, 196, "Ethereum ecosystem grant \u00b7 application", VIOLET, 8.6, 1.9)

    text(c, M, 268, "The city,", MED, 54, INK, -1.2)
    text(c, M, 336, "upgraded", SERIF_IT, 66, VIOLET, -0.6)
    w_up = T.sw("upgraded", SERIF_IT, 66, -0.6)
    text(c, M + w_up + 2, 336, ".", MED, 54, INK, -1.2)
    squiggle(c, M + 2, 352, w_up - 4, TEAL, 2.6, 2.2, 7)

    para(c, M, 396, 500,
         "21 turns a report about a broken bench into paid, verified work: "
         "residents report, contractors bid, the street decides, and the "
         "receipt stays public on Ethereum.",
         R, 12.4, 19, MUT)

    # ask card
    card(c, M, 486, 566, 100, fill=WHITE, stroke=LINE, r=18, shadow=True, shadow_dy=6)
    cols = [("Ask", "$21,000", "6 months, one round"),
            ("To artists", "70%", "21 fees, paid on time"),
            ("For code", "$0", "we build it ourselves")]
    for i, (k, v, s) in enumerate(cols):
        x = M + 24 + i * 180
        label(c, x, 512, k, MUT_DIM, 7.2, 1.4)
        text(c, x, 542, v, MED, 21, INK, -0.5)
        text(c, x, 562, s, R, 7.8, MUT)
        if i:
            vline(c, x - 16, 506, 572, LINE_SOFT, 0.9)

    x = M
    for ch, bg in (("21 MURALS", YELLOW_SOFT), ("9 CITIES", TEAL_SOFT),
                   ("21 ARTISTS PAID", VIOLET_SOFT)):
        x += chip(c, x, 612, ch, INK, bg, alpha(INK, 0.12), 7.2, 24, 11,
                  rot=-1.5 + x % 3) + 9
    text(c, M, 660, "21.city  \u00b7  hello@21.city", MONO, 8.4, MUT_DIM, 0.4)
    text(c, 646, 660, f"{idx:02d} / {TOTAL}", MONO, 8.4, MUT_DIM, 0.8, "right")


# ============================================================ 02  problem
def s02(c, idx):
    page(c)
    T.head(c, "01 \u2014 The problem",
           "Cities can see the problem.\nThey can't find the \u20ac420.",
           "Every day a report turns into a reference number, and a small repair "
           "waits for a season that never comes.", width=760, subw=520, y=108,
           size=36, leading=41)

    items = [
        ("Reports end in a ticket.",
         "A photo to a hotline returns a case number, not a budget. Nobody learns "
         "who decided, who was paid, or what happened next.", VIOLET),
        ("Small fixes fall through.",
         "\u20ac420 for a bench, \u20ac950 for a bike rack: too small for procurement, "
         "too visible to ignore. They wait for a season that never comes.", TEAL),
        ("Contractors stay invisible.",
         "The people who could fix it never see the job. The city never sees their "
         "price. The resident sees nothing at all.", CORAL),
    ]
    y = 268
    for i, (h_, b, col) in enumerate(items):
        step_badge(c, M + 16, y + 2, f"0{i + 1}", col, 16)
        text(c, M + 46, y + 7, h_, MED, 13.4, INK)
        para(c, M + 46, y + 28, 430, b, R, 9.9, 15, MUT)
        y += 104

    # resident's photo, stuck on the page
    polaroid(c, PHOTOS + "/bench-broken.jpg", 812, 205, 318, 402, pad=9,
             cap="TICKET A-1142 \u00b7 OOSTERPARK \u00b7 DAY 91", rot=2.2)
    tape(c, 900, 200, 66, 19, -5, alpha(YELLOW, 0.7))
    chip(c, 762, 596, "PHOTO: A RESIDENT'S PHONE", WHITE, INK, None, 6.8, 20, 9, rot=-2)

    # footnote
    hline(c, M, 612, 700, alpha(INK, 0.12))
    label(c, M, 636, "What is missing", MUT_DIM, 7.4, 1.5)
    text(c, M + 148, 636, "A budget. A bid. A name. A receipt.", MED, 11.4, INK, 0.1)
    foot(c, idx, "The problem")


# ============================================================ 03  the upgrade
def s03(c, idx):
    page(c)
    T.head(c, "02 \u2014 The upgrade",
           "Not another app. An upgrade\nfor the street corner.",
           "Cities already have crews, budgets and rules. 21 replaces the missing "
           "layer between a report and a paid invoice \u2014 and makes the result visible.",
           width=720, subw=520, y=106, size=36, leading=41)

    rows = [
        ("From tickets to tasks", VIOLET,
         "A report becomes a task with a budget, a deadline and a public URL."),
        ("From procurement to bids", TEAL,
         "Contractors publish itemised quotes. Residents choose under rules fixed "
         "before the money arrives."),
        ("From repairs to authorship", CORAL,
         "Every fix is documented, and every wall is painted by a paid artist, "
         "with the owner's written consent."),
    ]
    y = 268
    for i, (h_, col, b) in enumerate(rows):
        rect(c, M, y - 6, 7, 42, fill=col, r=3.5)
        text(c, M + 22, y + 8, h_, MED, 13.2, INK)
        para(c, M + 22, y + 28, 470, b, R, 9.8, 14.6, MUT)
        y += 92

    illustration(c, ART + "/upgrade-block.png", 626, 182, 646)
    chip(c, 1116, 182, "v21", VIOLET, WHITE, None, 8.6, 27, 10, rot=7, shadow=True)

    card(c, M, 566, W - 2 * M, 74, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 592, "The upgrade is additive", VIOLET, 7.4, 1.5)
    text(c, M + 22, 618,
         "Cities keep their crews, budgets and procurement rules. 21 adds the "
         "missing part: a public task record, competitive bids and a receipt "
         "anyone can audit.", R, 9.6, MUT)
    foot(c, idx, "The upgrade")


# ============================================================ 04  protocol
def s04(c, idx):
    page(c)
    T.head(c, "03 \u2014 The protocol",
           "Seven steps from a photo\nto a paid invoice.",
           "One continuous workflow. Every step leaves a public artefact: a task, "
           "a bid, a vote, a photo, a payment.", width=760, subw=560, y=106,
           size=36, leading=41)

    steps = [
        ("01", "Report", "Photo, GPS, category. Under 60 seconds on a phone.", VIOLET),
        ("02", "Propose", "Contractors publish itemised budgets and milestones.", TEAL),
        ("03", "Fund", "Neighbours, the city and a matching pool fill escrow.", YELLOW),
        ("04", "Decide", "Eligible residents pick a bid; rules were pinned first.", SKY),
        ("05", "Build", "Work happens in the street, in daylight, by named people.", CORAL),
        ("06", "Verify", "Signed capture, geofence, attestations, 72 h to object.", PINK),
        ("07", "Settle", "Escrow releases the tranche to the contractor.", VIOLET),
    ]
    x0, rail_y = M + 10, 318
    colw = (W - 2 * M - 20) / 7
    band_w = W - 2 * M - 20
    rect(c, x0 + 20, rail_y - 1.5, band_w - 40, 3, fill=LINE, r=2)
    for i, (n, t, d, col) in enumerate(steps):
        cx = x0 + colw * i + colw / 2
        U.badge(c, cx, rail_y, 21, n, col, WHITE, 13, MED)
        text(c, cx, rail_y + 52, t, MED, 13.2, INK, 0, "center")
        para(c, cx - colw / 2 + 6, rail_y + 72, colw - 12, d, R, 8.5, 12.2, MUT,
             align="center")

    # notes under the rail
    card(c, M, 468, 552, 118, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 494, "Public by default", VIOLET, 7.4, 1.5)
    for i, s_ in enumerate(("who bid, and for how much",
                            "who voted, and on which rules",
                            "who was paid, and for which milestone")):
        U.dot(c, M + 26, 518 + i * 20, 2.4, VIOLET)
        text(c, M + 38, 522 + i * 20, s_, R, 9.2, MUT)

    card(c, 648, 468, 560, 118, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, 670, 494, "Private by design", TEAL, 7.4, 1.5)
    for i, s_ in enumerate(("faces and plates blurred on the device",
                            "coarse public coordinates, never your door",
                            "personal data off-chain, deleteable on request")):
        U.dot(c, 674, 518 + i * 20, 2.4, TEAL)
        text(c, 686, 522 + i * 20, s_, R, 9.2, MUT)
    foot(c, idx, "The protocol")


# ============================================================ 05  contractor bids
def s05(c, idx):
    page(c)
    T.head(c, "04 \u2014 Contractor bids",
           "Bids arrive itemised,\nin public.",
           "A contractor needs a phone and a price list. No tender documents, no "
           "90-day invoice cycle, no relationship with city hall required.",
           width=700, subw=520, y=106, size=36, leading=41)

    bids = [
        ("Groenwerk BV", "Bench repair \u00b7 Amsterdam", "\u20ac412", "9 days",
         "24-month warranty", True),
        ("Studio Tak", "Bench repair + repaint \u00b7 Utrecht", "\u20ac455", "12 days",
         "24-month warranty", False),
        ("M. de Vries", "Bench repair \u00b7 Rotterdam", "\u20ac380", "7 days",
         "9-month warranty", False),
    ]
    y = 248
    for name, sub, price, days, warranty, selected in bids:
        card(c, M, y, 520, 84, fill=WHITE if not selected else VIOLET_SOFT,
             stroke=VIOLET if selected else LINE, r=16, lw=1.4 if selected else 1,
             shadow=True, shadow_dy=5)
        U.avatar(c, M + 34, y + 34, 17, name[:1], WHITE if selected else PAPER_2,
                 VIOLET if selected else INK_SOFT)
        text(c, M + 62, y + 32, name, MED, 12.2, INK)
        text(c, M + 62, y + 50, sub, R, 8.4, MUT)
        text(c, M + 62, y + 68, f"{days} \u00b7 {warranty}", MONO, 7.2, MUT_DIM, 0.2)
        text(c, M + 496, y + 36, price, MED, 19, INK, -0.4, "right")
        if selected:
            chip(c, M + 404, y + 58, "SELECTED", WHITE, VIOLET, None, 6.5, 18, 8,
                 rot=-2)
        y += 98

    # bid detail
    x, y0, w, h = 640, 210, 568, 350
    card(c, x, y0, w, h, fill=WHITE, stroke=LINE, r=18, shadow=True, shadow_dy=6)
    label(c, x + 24, y0 + 28, "Winning bid \u00b7 line by line", VIOLET, 7.4, 1.5)
    text(c, x + 24, y0 + 54, "Groenwerk BV", MED, 15, INK)
    chip(c, x + w - 116, y0 + 38, "\u20ac412 TOTAL", VIOLET, VIOLET_SOFT, None,
         7, 22, 9)

    lines = [("Oak slats, 6 pcs, FSC", "\u20ac114"),
             ("Stainless fixings", "\u20ac24"),
             ("Labour, 2 \u00d7 4 h", "\u20ac236"),
             ("Transport + old-slat disposal", "\u20ac38")]
    ly = y0 + 88
    for k, v in lines:
        text(c, x + 24, ly, k, R, 9.2, MUT)
        text(c, x + w - 24, ly, v, MONO, 8.8, INK, 0.2, "right")
        hline(c, x + 24, ly + 10, x + w - 24, LINE_SOFT, 0.8)
        ly += 34
    text(c, x + 24, ly + 4, "Total, no surprises", MED, 10.6, INK)
    text(c, x + w - 24, ly + 4, "\u20ac412", MED, 13, VIOLET, 0.2, "right")
    hline(c, x + 24, ly + 16, x + w - 24, alpha(INK, 0.2), 1.2)

    rect(c, x + 24, y0 + h - 58, w - 48, 34, fill=PAPER, r=10)
    text(c, x + 38, y0 + h - 36,
         "Every line is editable in the bid form. No lump sums, no allowances.",
         R, 8.4, MUT)

    # bottom numbers
    hline(c, M, 602, W - M, alpha(INK, 0.12))
    stats = [("3", "bidders per task"), ("18%", "price spread"),
             ("6 h", "to first bid"), ("24 h", "to payout after verification")]
    for i, (a, b) in enumerate(stats):
        x = M + i * 272
        text(c, x, 634, a, MED, 19, INK, -0.4)
        text(c, x + T.sw(a, MED, 19, -0.4) + 10, 634, b, R, 8.6, MUT)
    foot(c, idx, "Contractor bids")


# ============================================================ 06  end to end
def s06(c, idx):
    page(c)
    T.head(c, "05 \u2014 One task, end to end",
           "A bench in Oosterpark.\nNine days, start to receipt.",
           "Demo scenario from the product spec. Amounts and dates are "
           "illustrative, not reported results.", width=720, subw=540, y=106,
           size=36, leading=41)

    phone_shot(c, PHOTOS + "/bench-broken.jpg", 78, 226, 168, 340, rot=-2.5,
               caption="DAY 0 \u00b7 REPORTED BY A RESIDENT")
    doodle_arrow(c, 260, 392, 304, 372, VIOLET, 1.6, 0.25)
    phone_shot(c, PHOTOS + "/bench-fixed.jpg", 320, 226, 168, 340, rot=2.0,
               caption="DAY 9 \u00b7 FIXED AND ATTESTED")

    x = 590
    label(c, x, 226, "Task ledger \u00b7 public by default", VIOLET, 7.6, 1.5)
    rows = [
        ("Day 0", "Task published", "\u20ac420 target", YELLOW),
        ("Day 1", "3 bids received", "\u20ac380 \u2013 \u20ac455", INK_SOFT),
        ("Day 3", "84 residents voted", "62% Groenwerk", INK_SOFT),
        ("Day 4", "Escrow funded", "\u20ac420 in USDC", VIOLET),
        ("Day 7", "Milestone evidence", "6 photos + GPS", INK_SOFT),
        ("Day 9", "Dual attestation", "payment released", TEAL),
    ]
    y = 250
    vline(c, x + 6, y + 8, y + 8 + 44 * (len(rows) - 1), LINE, 1)
    for t, a, b, col in rows:
        U.dot(c, x + 6, y + 8, 4.2, col)
        text(c, x + 24, y + 12, t, MONO, 8, MUT_DIM, 0.4)
        text(c, x + 72, y + 12, a, MED, 10.4, INK)
        text(c, W - M, y + 12, b, MONO, 8.4, MUT, 0.2, "right")
        y += 44

    card(c, x, 540, W - M - x, 78, fill=WHITE, stroke=LINE, r=14, shadow=True)
    label(c, x + 18, 564, "What the resident keeps", VIOLET, 7.2, 1.4)
    text(c, x + 18, 588,
         "A public URL with the full history, the contractor's name and the final "
         "payment.", R, 9.2, MUT)
    text(c, x + 18, 604, "21.city/t/oosterpark-bench", MONO, 7.8, MUT_DIM, 0.2)

    text(c, M, 610, "Payments land the day verification clears \u2014 not in the next quarter.",
         R, 9.0, MUT_DIM)
    foot(c, idx, "One task")


# ============================================================ 07  street furniture
def s07(c, idx):
    page(c)
    T.head(c, "06 \u2014 The kit",
           "Modern street furniture,\npriced line by line.",
           "Every task template carries a specification, so three contractors bid "
           "on the same object \u2014 same material, same life, same repair.",
           width=760, subw=600, y=104, size=34, leading=39)

    tiles = [
        ("Lijn bench", PHOTOS + "/plaza.jpg", "Cast concrete base, FSC oak top",
         "30 yr base \u00b7 12 yr top", "\u20ac420"),
        ("Lus rack", PHOTOS + "/bike-rack.jpg", "Powder-coated steel loops",
         "20 yr \u00b7 6 bikes", "\u20ac950"),
        ("Sedum shelter", PHOTOS + "/shelter.jpg", "Steel + glass, sedum roof, 340 Wp",
         "25 yr \u00b7 off-grid", "\u20ac6,400"),
    ]
    for i, (name, p, spec, life, price) in enumerate(tiles):
        x = M + i * 384
        card(c, x, 202, 368, 258, fill=WHITE, stroke=LINE, r=16, shadow=True,
             shadow_dy=6)
        photo(c, p, x + 8, 210, 352, 146, r=10)
        text(c, x + 20, 382, name, MED, 12.4, INK)
        text(c, x + 348, 382, price, MED, 12.4, VIOLET, 0, "right")
        text(c, x + 20, 400, spec, R, 8.4, MUT)
        text(c, x + 20, 418, life, MONO, 7.2, MUT_DIM, 0.2)
        chip(c, x + 20, 428, "SPEC SHEET \u00b7 V21", INK, PAPER, alpha(INK, 0.14),
             6.2, 18, 7)

    # spec table
    y = 496
    hline(c, M, y, W - M, alpha(INK, 0.15))
    heads = [(M, "ITEM"), (330, "MATERIAL"), (700, "DESIGN LIFE"),
             (930, "UNIT COST"), (1208, "REPAIR")]
    for hx, h_ in heads:
        label(c, hx, y - 8, h_, MUT_DIM, 6.8, 1.4,
              "right" if hx == 1208 else "left")
    rows = [("Lijn bench", "Concrete + oak", "30 / 12 yr", "\u20ac420", "2 h"),
            ("Lus rack", "Powder-coated steel", "20 yr", "\u20ac950", "4 h"),
            ("Sedum shelter", "Steel, glass, sedum, PV", "25 yr", "\u20ac6,400", "2 days"),
            ("Zon light", "Solar LED, 5-day autonomy", "15 yr", "\u20ac780", "3 h"),
            ("Rond planter", "Recycled concrete", "30 yr", "\u20ac310", "1 h")]
    y += 16
    for name, mat, life, cost, repair in rows:
        text(c, M, y + 12, name, MED, 8.8, INK)
        text(c, 330, y + 12, mat, R, 8.4, MUT)
        text(c, 700, y + 12, life, MONO, 7.8, MUT, 0.2)
        text(c, 930, y + 12, cost, MONO, 8.2, INK, 0.2)
        text(c, 1208, y + 12, repair, MONO, 7.8, MUT_DIM, 0.2, "right")
        hline(c, M, y + 19, W - M, LINE_SOFT, 0.7)
        y += 25
    foot(c, idx, "The kit")


# ============================================================ 08  verification
def s08(c, idx):
    page(c)
    T.head(c, "07 \u2014 Verification",
           "Proof first. Then money.",
           "A photo alone is not proof. 21 combines signed capture, a geofence, "
           "independent attestors and a 72-hour window to object.", width=700,
           subw=520, y=106, size=36, leading=41)

    rows = [
        ("Signed capture", "Photos are taken inside the app. EXIF, GPS, gyroscope "
                           "and a device signature are hashed and stored with the file."),
        ("Proximity, not claims", "The capture must fall inside the task geofence; "
                                  "anything above \u20ac1,000 gets a reviewer visit."),
        ("Dual attestation", "A resident attestor and a city partner sign each "
                             "milestone. Above \u20ac1,000, a random reviewer is added."),
        ("A real challenge window", "72 hours to dispute with a staked bond. Lose "
                                    "and the bond pays the reviewer; win and it comes back."),
    ]
    y = 240
    for i, (k, v) in enumerate(rows):
        text(c, M, y + 10, f"0{i + 1}", MONO_MED, 8.4, VIOLET, 1.2)
        text(c, M + 28, y + 10, k, MED, 11.6, INK)
        para(c, M + 28, y + 28, 430, v, R, 9.4, 14, MUT)
        hline(c, M, y + 66, 520, LINE_SOFT)
        y += 78

    # evidence card
    x, y0, w, h = 580, 210, 628, 386
    card(c, x, y0, w, h, fill=WHITE, stroke=LINE, r=18, shadow=True, shadow_dy=6)
    text(c, x + 22, y0 + 32, "Evidence package", MED, 12.6, INK)
    chip(c, x + w - 122, y0 + 18, "VERIFIED", TEAL, TEAL_SOFT, alpha(TEAL, 0.5),
         7, 20, 9)
    photo(c, PHOTOS + "/bench-fixed.jpg", x + 22, y0 + 50, 178, 118, r=10)
    meta = [("Content hash", "bafkrei\u2026 4f2c"),
            ("Captured", "2026-03-23T09:14Z"),
            ("GPS", "52.35821, 4.91357 \u00b1 6 m"),
            ("Within geofence", "yes \u00b7 11 m from task"),
            ("Milestone", "M2 \u00b7 re-fix + paint")]
    my = y0 + 58
    for k, v in meta:
        text(c, x + 216, my, k, MONO, 7.0, MUT_DIM, 0.4)
        text(c, x + 216, my + 13, v, MONO, 8.0, INK, 0.2)
        my += 28

    hline(c, x + 22, y0 + 194, x + w - 22, LINE_SOFT)
    label(c, x + 22, y0 + 214, "Attestations", MUT_DIM, 7.2, 1.4)
    atts = [("Citizen", "0x8a\u20264c1", TEAL), ("City partner", "0x1f\u20269be", SKY),
            ("Reviewer", "0x6c\u20262d7", VIOLET)]
    for i, (role, addr, col) in enumerate(atts):
        ax = x + 22 + i * 196
        card(c, ax, y0 + 222, 184, 52, fill=PAPER, stroke=LINE_SOFT, r=10,
             lw=0.8, shadow=False)
        U.dot(c, ax + 16, y0 + 238, 3.4, col)
        text(c, ax + 28, y0 + 242, role, MED, 9.4, INK)
        text(c, ax + 28, y0 + 256, addr, MONO, 7.2, MUT_DIM, 0.2)
        text(c, ax + 28, y0 + 267, "signed \u00b7 09:41", MONO, 6.4, MUT_DIM, 0.2)

    rect(c, x + 1, y0 + 300, w - 2, 42, fill=VIOLET_SOFT)
    text(c, x + 22, y0 + 326,
         "Tranche 2 released \u00b7 09:41 UTC", MONO, 7.6, VIOLET_DEEP, 0.3)
    text(c, x + w - 22, y0 + 326, "\u20ac210  \u00b7  tx 0x4c9\u20262a1", MONO, 7.6,
         INK_SOFT, 0.3, "right")
    text(c, x + 22, y0 + 366,
         "Escrow is frozen by default: a missed attestation means no payment, not a polite reminder.",
         R, 8.2, MUT)
    foot(c, idx, "Verification")


# ============================================================ 09  artists
def s09(c, idx):
    page(c)
    T.head(c, "08 \u2014 The cultural layer",
           "21 is a number anyone\ncan paint.",
           "A commissioned, always-authorised mural programme runs alongside the "
           "protocol. It is how a civic tool becomes recognisable on a street in "
           "Lagos or Lisbon without a translation.", width=720, subw=470, y=104,
           size=36, leading=41)

    blocks = [
        ("Commission, never tag", VIOLET,
         "Every wall has a signed owner consent, a removal clause and a paid artist. "
         "The registry refuses locations without a permission record."),
        ("One artist per wall", TEAL,
         "Year one: 21 walls in 9 cities, \u20ac300\u2013\u20ac1,200 per wall. Each work is a "
         "Proof-of-Place entry, so the number and the place stay linked."),
        ("The number is the message", CORAL,
         "No slogan to translate, no logo to explain. Two digits, painted by hand, "
         "pointing back to a working protocol."),
    ]
    y = 268
    for i, (k, col, v) in enumerate(blocks):
        U.dot(c, M + 4, y + 4, 4.2, col)
        text(c, M + 20, y + 8, k, MED, 12.2, INK)
        para(c, M + 20, y + 28, 452, v, R, 9.2, 14, MUT)
        y += 100

    illustration(c, ART + "/artist-wall.png", 588, 190, 632)
    chip(c, 1160, 172, "BERLIN \u00b7 2026", WHITE, INK, None, 6.6, 20, 8, rot=4)

    hline(c, M, 548, W - M, alpha(INK, 0.15))
    stats = [("21", "walls commissioned"), ("21", "artists paid"),
             ("9", "cities in 6 months"), ("100%", "consented walls")]
    for i, (a, b) in enumerate(stats):
        x = M + i * 284
        text(c, x, 596, a, MED, 34, INK, -1.0)
        text(c, x, 618, b, R, 9, MUT)
    foot(c, idx, "The 21 campaign")


# ============================================================ 10  artist deal
def s10(c, idx):
    page(c)
    T.head(c, "09 \u2014 The artist deal",
           "Paid before the paint dries.",
           "No exposure, no revenue share, no waiting for the grant to close. "
           "Half on the brief, half on documentation, five days median.", width=800,
           subw=600, y=106, size=36, leading=41)

    steps = [
        ("Open call", "A public call per city, reviewed with a local curator.",
         "fee band", VIOLET, "\u20ac300\u20131,200 per wall"),
        ("Owner consent", "Signed permission, removal clause, insurance binder.",
         "before paint", TEAL, "one page, no lawyer"),
        ("50% on brief", "Half the fee lands when the sketch is approved.",
         "day 1", YELLOW, "SEPA or USDC"),
        ("Wall painted", "Materials, lift and prep covered separately.",
         "days 2\u20135", CORAL, "producer on site"),
        ("50% + record", "Final half on photo documentation and a registry entry.",
         "day 6", SKY, "median 5 days"),
    ]
    x0, y0, cw, gap = M, 256, 204, 18
    for i, (k, d, tag, col, fact) in enumerate(steps):
        x = x0 + i * (cw + gap)
        card(c, x, y0, cw, 190, fill=WHITE, stroke=LINE, r=14, shadow=True,
             shadow_dy=5)
        U.badge(c, x + 26, y0 + 30, 14, str(i + 1), col, WHITE, 11, MED)
        text(c, x + 18, y0 + 70, k, MED, 11.2, INK)
        para(c, x + 18, y0 + 90, cw - 36, d, R, 8.6, 12.6, MUT)
        text(c, x + 18, y0 + 132, fact, MONO, 7.0, MUT_DIM, 0.2)
        chip(c, x + 18, y0 + 150, tag.upper(), col, alpha(col, 0.10),
             alpha(col, 0.45), 6.2, 18, 7)

    card(c, M, 480, 552, 128, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 506, "Artist contract, plain language", VIOLET, 7.4, 1.5)
    for i, s_ in enumerate(("Artist keeps copyright and credit; 21 gets a licence to document.",
                            "Removal clause: the owner can ask for the wall back, paid.",
                            "No wall starts before consent and insurance are on file.")):
        U.dot(c, M + 26, 530 + i * 22, 2.2, VIOLET)
        text(c, M + 38, 534 + i * 22, s_, R, 8.6, MUT)

    card(c, 648, 480, 560, 128, fill=TEAL_SOFT, stroke=alpha(TEAL, 0.4), r=16,
         shadow=True)
    label(c, 670, 506, "How the money arrives", TEAL, 7.4, 1.5)
    text(c, 670, 538, "SEPA in EUR or USDC on Base \u2014 the artist chooses.", MED, 10.6, INK)
    text(c, 670, 558, "Median payout: 5 days from approval, not from a funding round.",
         R, 9.0, INK_SOFT)
    text(c, 670, 584, "Escrow is only used for contractor work, never for artist fees.",
         MONO, 7.2, MUT, 0.2)
    foot(c, idx, "Artist deal")


# ============================================================ 11  why eth
def s11(c, idx):
    page(c)
    T.head(c, "10 \u2014 Why Ethereum",
           "The receipt should outlive\nthe grant.",
           "A civic platform that moves public money should not be able to rewrite "
           "its own history. Ethereum gives 21 four properties no SaaS can offer.",
           width=760, subw=580, y=106, size=36, leading=41)

    reasons = [
        ("Neutral settlement", VIOLET,
         "No company sits between a resident's euro and a contractor's invoice. "
         "The escrow is the counterparty."),
        ("A global payment rail", TEAL,
         "USDC on Base pays a contractor in Nairobi or Nijmegen in seconds, "
         "without a bank account."),
        ("Composable public goods", YELLOW,
         "Quadratic funding, retro funding, EAS attestations and Safe treasuries "
         "plug in unchanged."),
        ("A permanent public record", CORAL,
         "What was promised, funded and delivered stays queryable \u2014 even if 21 "
         "the company disappears."),
    ]
    for i, (k, col, v) in enumerate(reasons):
        x = M + (i % 2) * 572
        y = 250 + (i // 2) * 100
        rect(c, x, y - 16, 44, 44, fill=alpha(col, 0.14), r=12, stroke=None)
        U.dot(c, x + 22, y + 6, 7, col)
        text(c, x + 58, y + 2, k, MED, 12.4, INK)
        para(c, x + 58, y + 22, 450, v, R, 9.4, 13.6, MUT)

    card(c, M, 462, 552, 132, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 488, "What 21 deliberately does not do", MUT_DIM, 7.4, 1.4)
    for i, s_ in enumerate(("No token sale and no speculative asset",
                            "No custody of user funds at any point",
                            "No paid placement of projects or contractors",
                            "No growth metric that is not on-chain verifiable")):
        text(c, M + 22, 514 + i * 22, "\u00d7", MONO, 9, alpha(CORAL, 0.9))
        text(c, M + 38, 514 + i * 22, s_, R, 8.8, MUT)

    card(c, 648, 462, 560, 132, fill=VIOLET_SOFT, stroke=alpha(VIOLET, 0.35),
         r=16, shadow=True)
    label(c, 670, 488, "What actually goes on-chain", VIOLET, 7.4, 1.4)
    text(c, 670, 516, "who was selected  \u00b7  what was promised  \u00b7  what was paid",
         MONO, 8.0, VIOLET_DEEP, 0.2)
    text(c, 670, 542, "Not on-chain: faces, plates, addresses, phone numbers.",
         R, 9.0, INK_SOFT)
    text(c, 670, 566, "Media stays content-addressed off-chain; the hash is forever.",
         R, 8.4, MUT)
    foot(c, idx, "Why Ethereum")


# ============================================================ 12  product
def s12(c, idx):
    page(c)
    T.head(c, "11 \u2014 The product",
           "Six screens, one continuous workflow.",
           "Responsive web app plus an installable mobile PWA. Every screen below "
           "is MVP scope, not a future release.", width=900, subw=700, y=104,
           size=34, leading=39)

    frames = [
        ("Explore", "Map-first discovery with live tasks", "map"),
        ("Project", "Evidence, budget, milestones, discussion", "project"),
        ("Report", "Photo, GPS, category \u2014 under 60 seconds", "report"),
        ("Bids", "Competing quotes with itemised budgets", "proposals"),
        ("Contractor", "Bids, contracts, evidence, payouts", "workspace"),
        ("Completed", "Before / after and the payment record", "done"),
    ]
    cw, ch = 360, 176
    for i, (title, desc, kind) in enumerate(frames):
        col, row = i % 3, i // 3
        x = M + col * (cw + 28)
        y = 214 + row * 216
        U.browser(c, x, y, cw, ch, url="21.city/" + kind)
        c.saveState()
        p = c.beginPath()
        p.roundRect(x, T.ty(y) - ch, cw, ch, 12)
        c.clipPath(p, stroke=0, fill=0)
        U.window_content(c, x, y + 24, cw, ch - 24, kind)
        c.restoreState()
        text(c, x, y + ch + 24, f"0{i + 1}", MONO, 7.8, VIOLET, 1.2)
        text(c, x + 20, y + ch + 24, title, MED, 10.4, INK)
        text(c, x + 20 + T.sw(title, MED, 10.4) + 10, y + ch + 24, desc, R, 8.4, MUT)
    foot(c, idx, "Product")


# ============================================================ 13  interface
def s13(c, idx):
    page(c)
    T.head(c, "12 \u2014 Interface",
           "Friendly on purpose.",
           "Civic software usually looks like a form. Ours looks like something a "
           "neighbour would send you: warm paper, big targets, one clear action.",
           width=700, subw=520, y=104, size=36, leading=41)

    # palette
    label(c, M, 250, "Palette", MUT_DIM, 7.2, 1.5)
    swatches = [(PAPER, "Paper", "#FAF2DE"), (INK, "Ink", "#17161B"),
                (VIOLET, "Signal", "#6C24DF"), (TEAL, "Verified", "#12B98A"),
                (YELLOW, "Attention", "#F6C445"), (CORAL, "Alert", "#F0603F"),
                (SKY, "Info", "#6F9BF5"), (PINK, "Joy", "#FF51BC")]
    for i, (col, name, hexv) in enumerate(swatches):
        sx = M + (i % 4) * 118
        sy = 266 + (i // 4) * 74
        rect(c, sx, sy, 42, 42, fill=col, stroke=alpha(INK, 0.14), r=12, lw=0.9)
        text(c, sx + 52, sy + 16, name, R, 8.6, INK)
        text(c, sx + 52, sy + 29, hexv, MONO, 6.4, MUT_DIM, 0.2)

    # type
    label(c, M, 430, "Type", MUT_DIM, 7.2, 1.5)
    text(c, M, 470, "Display", MED, 30, INK, -0.8)
    text(c, M + 132, 470, "Geist", MONO, 8, MUT_DIM, 0.3)
    text(c, M, 502, "Accent", SERIF_IT, 30, VIOLET, -0.3)
    text(c, M + 132, 502, "Instrument Serif Italic", MONO, 8, MUT_DIM, 0.3)
    text(c, M, 530, "Body 12 / 19", R, 11.4, MUT)
    text(c, M + 132, 530, "LABEL 8 / MONO / 1.6", MONO_MED, 8, VIOLET, 1.4)

    # components
    label(c, M, 570, "Components", MUT_DIM, 7.2, 1.5)
    bx = M
    bx += chip(c, bx, 584, "REPORT A PROBLEM", WHITE, VIOLET, None, 7.4, 30, 13) + 8
    bx += chip(c, bx, 588, "EXPLORE MAP", INK, WHITE, alpha(INK, 0.18), 7.4, 22, 11) + 8
    bx += chip(c, bx, 588, "VERIFIED", TEAL, TEAL_SOFT, alpha(TEAL, 0.45), 7, 22, 9) + 8
    bx += chip(c, bx, 588, "VOTING OPEN", YELLOW, YELLOW_SOFT, alpha(YELLOW, 0.6), 7, 22, 9)
    U.progress(c, M, 634, 300, 0.62, 8, VIOLET)
    text(c, M + 314, 641, "\u20ac362 of \u20ac420", MONO, 7.6, MUT, 0.2)

    # phone
    px, py, pw, ph = 948, 190, 200, 424
    rect(c, px + 2, py + 8, pw, ph, fill=SHADOW, r=26)
    rect(c, px, py, pw, ph, fill=INK, r=26)
    rect(c, px + 6, py + 6, pw - 12, ph - 12, fill=WHITE, r=22)
    rect(c, px + pw / 2 - 20, py + 12, 40, 8, fill=INK, r=4)
    text(c, px + 20, py + 38, "Report", MED, 11, INK)
    text(c, px + pw - 20, py + 38, "\u00d7", R, 12, MUT_DIM, 0, "right")
    photo(c, PHOTOS + "/bench-broken.jpg", px + 16, py + 52, pw - 32, 132, r=12)
    chip(c, px + 24, py + 62, "IN-APP CAMERA", WHITE, alpha(INK, 0.7), None,
         6, 16, 6)
    text(c, px + 16, py + 206, "Broken bench", MED, 10.4, INK)
    text(c, px + 16, py + 222, "52.3582 N \u00b7 Oosterpark", MONO, 6.6, MUT, 0.2)
    for i, (s_, bg) in enumerate((("Street furniture", VIOLET_SOFT),
                                  ("This week", YELLOW_SOFT),
                                  ("Photo + GPS attached", TEAL_SOFT))):
        chip(c, px + 16, py + 238 + i * 26, s_.upper(), INK, bg, None, 6.2, 20, 8)
    rect(c, px + 16, py + ph - 58, pw - 32, 34, fill=VIOLET, r=12)
    text(c, px + pw / 2, py + ph - 36, "Publish task", MED, 10, WHITE, 0.2, "center")
    text(c, px + pw / 2, py + ph - 14, "1 of 3 steps", MONO, 5.8, MUT_DIM, 0.2, "center")
    foot(c, idx, "Interface")


# ============================================================ 14  budget
def s14(c, idx):
    page(c)
    T.head(c, "13 \u2014 Budget",
           "Why the ask is $21,000.",
           "We are not asking anyone to pay for code. The team writes it. The one "
           "thing we cannot do ourselves is pay artists on time.", width=800,
           subw=620, y=104, size=36, leading=41)

    items = [
        ("Artist fees, 21 walls \u00d7 $700 avg", 14700, VIOLET),
        ("Paint, wall prep, lift or scaffold", 2100, TEAL),
        ("Local photographer + short film", 2100, YELLOW),
        ("Consent, permits, insurance", 1050, CORAL),
        ("Open call + paid curator", 1050, SKY),
    ]
    total = sum(i[1] for i in items)

    # headline number
    text(c, M, 258, "$21,000", SERIF, 74, INK, -1)
    text(c, M + 300, 250, "over 6 months", MED, 13, MUT)
    text(c, M + 300, 268, "21 artists \u00b7 21 walls \u00b7 9 cities", R, 9.4, MUT)
    chip(c, M + 300, 282, "CODE: $0", VIOLET, VIOLET_SOFT, None, 7, 22, 9, rot=-2)

    # stacked bar
    bx, bw, by = M, W - 2 * M, 330
    xx = bx
    for name, amt, col in items:
        wseg = bw * amt / total
        rect(c, xx, by, wseg - 3, 24, fill=col, r=4)
        xx += wseg
    text(c, M, by + 46, "70% of the ask goes straight to artists. Nothing is spent on "
                        "marketing, tokens or exchange listings.", R, 9.4, MUT)

    # table
    y = 432
    hline(c, M, y, W - M, alpha(INK, 0.15))
    label(c, M, y - 10, "Line item", MUT_DIM, 7.2, 1.4)
    label(c, 878, y - 10, "Share", MUT_DIM, 7.2, 1.4)
    label(c, W - M, y - 10, "USD", MUT_DIM, 7.2, 1.4, "right")
    y += 18
    for name, amt, col in items:
        rect(c, M, y + 11, 8, 8, fill=col, r=2.5)
        text(c, M + 20, y + 18, name, R, 9.6, INK)
        U.progress(c, 878, y + 12, 150, amt / 14700, 5, col)
        text(c, 1052, y + 18, f"{amt / total * 100:.0f}%", MONO, 8.2, MUT_DIM, 0.3)
        text(c, W - M, y + 18, f"${amt:,}", MONO, 9, INK, 0.2, "right")
        hline(c, M, y + 30, W - M, LINE_SOFT, 0.7)
        y += 34

    card(c, M, 606, W - 2 * M, 34, fill=WHITE, stroke=LINE_SOFT, r=10, lw=0.8, shadow=False)
    text(c, M + 16, 628, "If the grant is smaller, we paint fewer walls \u2014 not cheaper ones.",
         R, 9.0, MUT)
    text(c, W - M - 16, 628, "$21,000 total", MED, 11, INK, 0, "right")
    foot(c, idx, "Budget")


# ============================================================ 15  milestones
def s15(c, idx):
    page(c)
    T.head(c, "14 \u2014 Milestones",
           "Five payments, each tied\nto walls that exist.",
           "No milestone is closed on a slide. Each one ships something a reviewer "
           "can visit, photograph or open.", width=760, subw=560, y=106, size=34,
           leading=39)

    rows = [
        ("M1", "Month 1", "Open call + 21 contracts",
         "21 signed artist contracts, 9 owner-consent letters, curator engaged",
         10, 2100, VIOLET),
        ("M2", "Months 2\u20133", "First 7 walls, 3 cities",
         "7 walls installed, photographed and registered with proof-of-place",
         30, 6300, TEAL),
        ("M3", "Months 3\u20134", "Walls 8\u201314 + documentation",
         "7 more walls, plus a photo and short-film package per city",
         25, 5250, YELLOW),
        ("M4", "Months 4\u20135", "Walls 15\u201321, 9 cities",
         "All 21 walls installed and registered; 21 artists paid in full",
         25, 5250, CORAL),
        ("M5", "Month 6", "Exhibition + open kit",
         "21 walls shown publicly; the artist kit published under MIT",
         10, 2100, SKY),
    ]
    y = 236
    hline(c, M, y, W - M, alpha(INK, 0.15))
    label(c, M, y - 10, "", MUT_DIM)
    label(c, 100, y - 10, "Milestone", MUT_DIM, 7.2, 1.4)
    label(c, 470, y - 10, "Acceptance criterion", MUT_DIM, 7.2, 1.4)
    label(c, 1010, y - 10, "Share", MUT_DIM, 7.2, 1.4, "right")
    label(c, W - M, y - 10, "Release", MUT_DIM, 7.2, 1.4, "right")
    y += 16
    for code, month, name, crit, share, amount, col in rows:
        U.badge(c, M + 14, y + 22, 14, code, col, WHITE, 9.4, MED)
        text(c, M + 40, y + 16, month, MONO, 7.2, MUT_DIM, 0.3)
        text(c, M + 40, y + 32, name, MED, 10.4, INK)
        para(c, 470, y + 22, 470, crit, R, 8.8, 12.4, MUT, max_lines=2)
        text(c, 1010, y + 26, f"{share}%", MONO, 8.6, INK, 0.2, "right")
        text(c, W - M, y + 26, f"${amount:,}", MED, 10.2, INK, 0.2, "right")
        hline(c, M, y + 44, W - M, LINE_SOFT, 0.7)
        y += 54

    card(c, M, 560, W - 2 * M, 86, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 584, "Cumulative release", VIOLET, 7.2, 1.4)
    cum = [("M1", 10), ("M2", 40), ("M3", 65), ("M4", 90), ("M5", 100)]
    for i, (k, v) in enumerate(cum):
        x = M + 24 + i * 216
        text(c, x, 612, k, MONO, 7.2, MUT_DIM, 0.4)
        U.progress(c, x + 22, 607, 120, v / 100, 6, alpha(VIOLET, 0.85))
        text(c, x + 148, 613, f"{v}%", MONO, 7.6, MUT, 0.2)
    text(c, M + 24, 636, "An unmet criterion means an unpaid milestone, not a renegotiation.",
         R, 8.4, MUT_DIM)
    foot(c, idx, "Milestones")


# ============================================================ 16  team
def s16(c, idx):
    page(c)
    T.head(c, "15 \u2014 Team",
           "Three people, one curator,\n21 artists.",
           "Small by design. Most of the money leaves the building on day one of "
           "each wall, on its way to the person holding the brush.", width=780,
           subw=600, y=106, size=34, leading=39)

    people = [
        ("Protocol & product", "contracts \u00b7 app \u00b7 escrow", VIOLET,
         "Solidity and Foundry, civic interfaces, PWA capture. Owns the escrow, "
         "the registry and the public task page.", "[name]  \u00b7  [github]"),
        ("Programme lead", "cities \u00b7 artists \u00b7 permissions", TEAL,
         "Runs the open calls, the consent paperwork and the wall calendar with "
         "the local curator in each city.", "[name]  \u00b7  [linkedin]"),
        ("Field producer", "build \u00b7 lift \u00b7 documentation", CORAL,
         "Books the lift, the paint and the photographer; makes sure every wall "
         "finishes on the day it was promised.", "[name]  \u00b7  [linkedin]"),
    ]
    for i, (role, key, col, desc, link) in enumerate(people):
        x = M + i * 384
        card(c, x, 218, 368, 196, fill=WHITE, stroke=LINE, r=16, shadow=True,
             shadow_dy=6)
        rect(c, x + 22, 240, 42, 42, fill=alpha(col, 0.15), r=12)
        text(c, x + 43, 268, role[0], MED, 16, col, 0, "center")
        text(c, x + 78, 258, role, MED, 11.6, INK)
        text(c, x + 78, 274, key, MONO, 6.8, MUT, 0.3)
        para(c, x + 22, 302, 324, desc, R, 9.0, 13.4, MUT)
        hline(c, x + 22, 358, x + 346, LINE_SOFT, 0.8)
        text(c, x + 22, 380, link, MONO, 7.6, MUT, 0.3)
        text(c, x + 346, 380, "full time \u00b7 6 months", MONO, 6.6, MUT_DIM, 0.3, "right")

    card(c, M, 438, 700, 106, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 462, "Curator \u00b7 paid, one per city", VIOLET, 7.2, 1.4)
    text(c, M + 22, 486, "Local curator, selected with the city", MED, 10.6, INK)
    para(c, M + 22, 502, 650,
         "They shortlist artists, sit on the open call and write the wall notes. "
         "Paid from the budget line, never asked to work for visibility.", R, 8.8,
         12.6, MUT)

    card(c, 796, 438, 412, 106, fill=TEAL_SOFT, stroke=alpha(TEAL, 0.4), r=16,
         shadow=True)
    label(c, 818, 462, "The 21 artists", TEAL, 7.2, 1.4)
    text(c, 818, 486, "Paid per wall, credited by name", MED, 10.6, INK)
    text(c, 818, 506, "No equity. No tokens. No exposure.", R, 9.2, INK_SOFT)
    text(c, 818, 524, "Fee range \u20ac300\u2013\u20ac1,200, always published.", MONO, 7.0, MUT, 0.2)

    hline(c, M, 574, W - M, alpha(INK, 0.12))
    label(c, M, 598, "Open role, funded by tranche 2", MUT_DIM, 7.2, 1.4)
    text(c, M, 620, "Verification & field-operations lead \u2014 runs reviewer panels in the pilot cities.",
         R, 9.2, MUT)
    label(c, 780, 598, "Not applying for", MUT_DIM, 7.2, 1.4)
    text(c, 780, 620, "Marketing budget, token liquidity, or exchange listings.",
         R, 9.2, MUT)
    foot(c, idx, "Team")


# ============================================================ 17  metrics
def s17(c, idx):
    page(c)
    T.head(c, "16 \u2014 Success metrics",
           "Targets, not traction.",
           "21 is pre-launch. These are the numbers we commit to publishing at "
           "close-out, with the raw registry export next to them.", width=820,
           subw=620, y=106, size=36, leading=41)

    metrics = [
        ("21", "walls commissioned and documented", "proof-of-place entries", VIOLET),
        ("21", "artists paid, median 5 days", "payout timestamps", TEAL),
        ("9", "cities with a signed consent", "owner permission records", YELLOW),
        ("100%", "walls with written owner consent", "consent registry", CORAL),
        ("40", "tasks published, verified and settled", "registry events", SKY),
        ("25", "contractors paid through escrow", "payout timestamps", PINK),
    ]
    for i, (big, small, src, col) in enumerate(metrics):
        col_i, row = i % 3, i // 3
        x = M + col_i * 384
        y = 226 + row * 142
        card(c, x, y, 368, 128, fill=WHITE, stroke=LINE, r=16, shadow=True,
             shadow_dy=5)
        rect(c, x + 1, y + 10, 6, 108, fill=col, r=3)
        text(c, x + 24, y + 52, big, MED, 32, INK, -0.9)
        para(c, x + 24, y + 82, 300, small, R, 9.2, 12.6, MUT)
        text(c, x + 24, y + 112, "source: " + src, MONO, 6.4, MUT_DIM, 0.2)

    card(c, M, 524, W - 2 * M, 106, fill=WHITE, stroke=LINE, r=16, shadow=True)
    label(c, M + 22, 548, "Guardrails \u2014 we fail if these move the wrong way",
          CORAL, 7.2, 1.4)
    guard = [("Unauthorised walls", "0, ever"), ("Artist payment median", "< 7 days"),
             ("Fraud rate", "< 1% of released value"), ("Disputes", "< 8% of tasks")]
    for i, (k, v) in enumerate(guard):
        x = M + 24 + i * 276
        text(c, x, 578, v, MED, 11, INK)
        text(c, x, 598, k, R, 8.2, MUT_DIM)
    text(c, M + 24, 620, "Every number is a target for month six, not a result. The methodology ships with the report.",
         R, 8.0, MUT_DIM)
    foot(c, idx, "Metrics")


# ============================================================ 18  risks
def s18(c, idx):
    page(c)
    T.head(c, "17 \u2014 Risks",
           "What could go wrong,\nand what we do about it.",
           "A mural programme and a payment protocol have different failure modes. "
           "Both are written down before the first euro moves.", width=780,
           subw=560, y=106, size=34, leading=39)

    xs = [M, 330, 770]
    y = 250
    hline(c, M, y, W - M, alpha(INK, 0.18))
    for i, col in enumerate(("Threat", "Why it is real", "Mitigation in the MVP")):
        label(c, xs[i], y - 10, col, MUT_DIM, 7.2, 1.5)
    y += 8
    rows = [
        ("Artist pulls out",
         "A wall is booked, a fee is committed, the artist disappears.",
         "Signed contract before the open call closes; a named backup artist per city; the fee is escrowed in two tranches."),
        ("Owner revokes permission",
         "Buildings change hands; a new owner wants a plain wall.",
         "Removal clause signed up front; the registry marks the wall retired; the documentation stays public."),
        ("Weather and access",
         "Rain, scaffolding permits and festival weeks move the calendar.",
         "Two-week buffer per city; indoor walls in the mix; the lift is booked only after consent."),
        ("Fabricated evidence",
         "A model can draw a fixed bench in seconds.",
         "In-app capture only, signed metadata, C2PA credentials, perceptual-hash dedupe, human spot audits."),
        ("GPS spoofing",
         "Mock locations are one developer setting away.",
         "Geofence plus cell/Wi-Fi corroboration; a reviewer visits anything above \u20ac1,000."),
        ("Escrow bug",
         "Contracts hold real money from day one.",
         "Two audits before mainnet, invariant fuzzing, per-task caps, 3-of-5 guardian pause with 48 h delay."),
    ]
    row_h = 54
    for i, (a, b, cc_) in enumerate(rows):
        yy = y + 10 + i * row_h
        if i % 2 == 0:
            rect(c, M - 12, yy - 6, W - 2 * M + 24, row_h - 6, fill=WHITE, r=8)
        text(c, xs[0], yy + 22, a, MED, 9.6, INK)
        para(c, xs[1], yy + 22, 380, b, R, 8.8, 12.2, MUT, max_lines=2)
        para(c, xs[2], yy + 22, 430, cc_, R, 8.8, 12.2, MUT, max_lines=2)

    text(c, M, 626, "Open question we bring to reviewers: what is the minimum viable proof for a \u20ac300 repair "
                    "that still resists a determined faker?", L, 9.2, MUT_DIM)
    foot(c, idx, "Risks")


# ============================================================ 19  after
def s19(c, idx):
    page(c)
    T.head(c, "18 \u2014 After the grant",
           "Built to outlive the round.",
           "The artist kit and the protocol are open source. Revenue, if any, is "
           "optional and capped; the public instance stays free for residents.",
           width=780, subw=620, y=106, size=34, leading=39)

    cols = [
        ("01", "Sustainable by design", VIOLET,
         ["Optional 1.5% fee on released escrow, capped and opt-in per city",
          "Hosted instance + support subscription for municipalities",
          "Matching pools funded by partners, not by the protocol"]),
        ("02", "Progressive, slowly", TEAL,
         ["M1\u2013M5: core team ships, guardian multisig holds pause rights",
          "Year 1: a council elected by contributors, parameters on-chain",
          "Year 2: registry ownership renounced; fee switch under token-less vote"]),
        ("03", "What stays open", CORAL,
         ["Contracts, indexer and client under MIT",
          "The artist kit: call template, contract, consent form, spec sheets",
          "A public export of every task, attestation and payment"]),
    ]
    for i, (n, k, col, items) in enumerate(cols):
        x = M + i * 372
        U.badge(c, x + 14, 232, 14, n, col, WHITE, 9.4, MED)
        text(c, x + 38, 238, k, MED, 12.2, INK)
        yy = 270
        for it in items:
            U.dot(c, x + 4, yy - 3, 2.2, col)
            yy = para(c, x + 16, yy, 320, it, R, 8.9, 13, MUT) + 12

    card(c, M, 428, W - 2 * M, 138, fill=WHITE, stroke=LINE, r=18, shadow=True,
         shadow_dy=6)
    label(c, M + 24, 454, "If the pilot works, the next eighteen months look like",
          MUT_DIM, 7.2, 1.4)
    steps = [("21 cities", "the full campaign, one wall\nin each city"),
             ("200 walls", "recurring artist commissions,\nnot one-off demos"),
             ("\u20ac1m escrow", "mostly partner-funded\nmatching pools"),
             ("1 kit", "any civic group can run\ntheir own edition")]
    for i, (a, b) in enumerate(steps):
        x = M + 24 + i * 272
        text(c, x, 492, a, MED, 22, INK, -0.5)
        para(c, x, 514, 240, b.replace("\n", " "), R, 8.6, 12, MUT)

    text(c, M, 620, "The registry stays public, the artist kit stays MIT, and the first 21 walls decide whether this is real.",
         L, 9.6, MUT_DIM)
    foot(c, idx, "After the grant")


# ============================================================ 20  close
def s20(c, idx):
    page(c)
    illustration(c, ART + "/artist-wall.png", 470, 178, 810)
    chip(c, 1196, 192, "21", VIOLET, WHITE, None, 11, 38, 12, rot=8, shadow=True)

    logotype(c, M, 84, 26, INK, VIOLET)
    label(c, M, 214, "The ask", VIOLET, 8.8, 1.9)
    text(c, M, 292, "Let's paint", MED, 54, INK, -1.2)
    text(c, M, 358, "21", SERIF_IT, 76, VIOLET, -1)
    squiggle(c, M + 2, 374, 96, TEAL, 2.8, 2.4, 4)

    para(c, M, 418, 420,
         "$21,000 over six months to pay 21 artists, install 21 walls in 9 cities, "
         "and leave behind an open kit any city can copy.", R, 12, 18.5, MUT)

    card(c, M, 514, 420, 96, fill=WHITE, stroke=LINE, r=16, shadow=True, shadow_dy=6)
    text(c, M + 22, 548, "21.city", MED, 15, INK, 0.2)
    text(c, M + 22, 570, "hello@21.city  \u00b7  github.com/21-movement", MONO, 7.6,
         MUT, 0.3)
    text(c, M + 22, 592, "Open source \u00b7 MIT \u00b7 no token", MONO, 7.0, MUT_DIM, 0.4)

    text(c, M, 654, "Thank you. Bring a wall.", MED, 11, MUT_DIM, 0.2)
    text(c, W - M, 654, f"{idx:02d} / {TOTAL}", MONO, 8.4, MUT_DIM, 0.8, "right")


SLIDES = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14,
          s15, s16, s17, s18, s19, s20]
assert len(SLIDES) == TOTAL


def build(path):
    c = rl_canvas.Canvas(path, pagesize=(W, H))
    c.setTitle("21 \u2014 Ethereum-native civic infrastructure")
    c.setAuthor("21")
    c.setSubject("Ethereum ecosystem grant application \u2014 2026")
    c.setKeywords("Ethereum, public goods, civic infrastructure, escrow, grant, murals")
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
