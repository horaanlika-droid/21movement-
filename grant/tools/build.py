import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.pdfgen import canvas as rl_canvas

import theme as T
import uikit as U
from theme import (ALERT, BLUE, BOLD, H, INK, L, LINE, LINE_SOFT, M, MED, MINT,
                   MONO, MONO_MED, MONO_SEMI, MUT, MUT_DIM, PANEL, PANEL_2,
                   PANEL_3, R, SAND, SEMI, TXT, VIO, VIO_DEEP, W, alpha,
                   fade, glow, hline, vline, label, logotype, page, para,
                   photo, rect, text, diamond)

T.register_fonts()
os.makedirs(T.OUT, exist_ok=True)
os.makedirs(T.PREVIEW, exist_ok=True)

GRAIN = os.path.join(T.OUT, "grain.png")
if not os.path.exists(GRAIN):
    T.make_grain(GRAIN)

A = T.ASSETS
TOTAL = 20


def foot(c, idx, section=""):
    T.footer(c, idx, section, dark=True)


# ============================================================ 01  cover
def s01(c, idx):
    page(c, True, GRAIN)
    photo(c, A + "/cover-mural.jpg", 640, 0, W - 640, H, overlay=INK, overlay_alpha=0.30)
    fade(c, 640, 0, 320, H, INK, 1.0, "left")
    fade(c, 640, 0, W - 640, 150, INK, 0.9, "top")
    fade(c, 640, H - 170, W - 640, 170, INK, 0.9, "bottom")
    glow(c, 200, 700, 440, VIO_DEEP, 0.12)

    logotype(c, M, 74, 26, TXT, VIO)
    label(c, M + 108, 82, "Ethereum-native civic infrastructure", MUT, 8.2, 1.5)
    label(c, W - M, 82, "Grant application \u00b7 2026", alpha(TXT, 0.65), 8.2, 1.5, "right")

    label(c, M, 238, "Ethereum ecosystem grant application", VIO, 9, 2.0)
    para(c, M, 302, 520, "Ethereum-native\ncivic infrastructure", MED, 50, 56, TXT, -0.6)
    para(c, M, 452, 440,
         "21 lets anyone report a real-world problem, fund the fix, hire the "
         "people who do the work, and verify the result \u2014 settled on Ethereum.",
         L, 13.5, 21, alpha(TXT, 0.70))

    y = 588
    hline(c, M, y - 26, 578, alpha(TXT, 0.16))
    x = M
    for k, v in (("Ask", "$75,000 / 10 mo."), ("Stage", "MVP + 3 city pilots"),
                 ("License", "Open source \u00b7 MIT")):
        label(c, x, y, k, MUT_DIM, 8, 1.5)
        text(c, x, y + 22, v, MED, 12.5, TXT, 0.1)
        x += 172
    foot(c, idx)


# ============================================================ 02  problem
def s02(c, idx):
    page(c, True, GRAIN)
    U.head(c, "01 \u2014 The problem",
           "Cities can see the problem.\nThey cannot coordinate the fix.",
           width=880)

    x = M
    y = 306
    items = [
        ("Reporting ends in a ticket.",
         "A photo to a hotline produces a reference number, not a budget. "
         "Residents never learn who decided, who was paid, or what actually "
         "happened."),
        ("Small works fall through.",
         "A \u20ac420 bench, a \u20ac950 bike rack, a \u20ac300 mural: too small for "
         "procurement, too visible to ignore. They wait for a season that never "
         "comes."),
        ("Public-goods funding stops at the screen.",
         "Crypto has capital, matching pools and governance tooling for digital "
         "work. There is no delivery layer for physical work."),
    ]
    for i, (h_, b) in enumerate(items):
        n = f"0{i + 1}"
        text(c, x, y + 15, n, MONO_MED, 9, VIO, 1.4)
        text(c, x + 30, y + 15, h_, MED, 13.5, TXT)
        para(c, x + 30, y + 36, 400, b, R, 10.4, 15.5, MUT)
        y += 88

    # evidence panel
    px, py, pw, ph = 700, 200, 504, 300
    photo(c, A + "/bench-before.jpg", px, py, pw, ph, r=10,
          overlay=INK, overlay_alpha=0.10)
    fade(c, px, py + ph - 150, pw, 150, INK, 0.92, "bottom")
    U.chip(c, px + 16, py + 16, "DEMO RECORD", alpha(TXT, 0.9), alpha(INK, 0.55),
         alpha(TXT, 0.25), 7.4, 17, 7)
    text(c, px + 16, py + ph - 52, "Ticket A-1142 \u00b7 Oosterpark", MED, 13, TXT)
    text(c, px + 16, py + ph - 32,
         "Reported 14 March \u00b7 still unrepaired 3 months later", R, 9.6, alpha(TXT, 0.62))
    text(c, px + 16, py + ph - 14,
         "no published budget \u00b7 no contractor \u00b7 no outcome record", MONO, 8, alpha(TXT, 0.60), 0.5)

    # why now
    y = 592
    hline(c, M, y - 22, W - M, LINE_SOFT)
    label(c, M, y, "Why this is buildable now", VIO, 8.4, 1.6)
    shifts = [("L2 fees", "a \u20ac4 settlement is\neconomically sane"),
              ("Personhood", "proof-of-personhood\nis usable"),
              ("Attestations", "EAS makes verified\nclaims portable"),
              ("Funding", "QF + retro funding\nis mature")]
    x = 392
    for k, v in shifts:
        U.dot(c, x + 1, y - 3, 1.9, VIO)
        text(c, x + 12, y, k, MED, 9.8, TXT)
        para(c, x + 12, y + 17, 158, v.replace("\n", " "), R, 8.6, 11.5, MUT)
        x += 220
    foot(c, idx, "The problem")


# ============================================================ 03  what 21 is
def s03(c, idx):
    page(c, True, GRAIN)
    U.head(c, "02 \u2014 The protocol",
           "A public protocol for getting real things done.",
           "21 turns a geotagged report into a funded, contracted and verified "
           "piece of work. The money moves through an on-chain escrow; the "
           "decision, the evidence and the payout stay public.")

    steps = [
        ("01", "Report", "Photo, location,\ncategory, urgency"),
        ("02", "Propose", "Contractors publish\nbudget + milestones"),
        ("03", "Fund", "Community + matching\npool fill escrow"),
        ("04", "Decide", "Eligible participants\nselect a proposal"),
        ("05", "Build", "Work happens in\nthe physical world"),
        ("06", "Verify", "Evidence + quorum\nof attestations"),
        ("07", "Settle", "Tranche released\nto the contractor"),
    ]
    x0, y0 = M, 330
    colw = (W - 2 * M) / 7
    # connecting rail
    hline(c, x0 + colw / 2, y0 + 30, W - M - colw / 2, LINE, 1)
    for i, (n, t, d) in enumerate(steps):
        cx = x0 + colw * i + colw / 2
        U.dot(c, cx, y0 + 30, 16, alpha(VIO, 0.10))
        U.dot(c, cx, y0 + 30, 11, PANEL, VIO, 0.8)
        text(c, cx, y0 + 33, n, MONO_MED, 8.4, VIO, 0.6, "center")
        text(c, cx, y0 + 70, t, MED, 13, TXT, 0.1, "center")
        para(c, cx, y0 + 90, colw - 18, d.replace("\n", " "), R, 9.2, 13, MUT,
             align="center")

    # principle strip
    y = 512
    hline(c, M, y, W - M, LINE_SOFT)
    principles = [
        ("Non-custodial", "21 never holds funds. A per-task escrow contract does."),
        ("Rule-bound", "Verification and payment rules are pinned before funding opens."),
        ("Composable", "Any city, DAO or funder can plug into the same registry."),
        ("Forkable", "MIT-licensed contracts and client. No lock-in for municipalities."),
    ]
    for i, (k, v) in enumerate(principles):
        x = M + i * ((W - 2 * M) / 4)
        text(c, x, y + 34, k, MED, 11.6, TXT)
        para(c, x, y + 52, (W - 2 * M) / 4 - 34, v, R, 9.4, 13.5, MUT)
    foot(c, idx, "The protocol")


# ============================================================ 04  end to end
def s04(c, idx):
    page(c, True, GRAIN)
    U.head(c, "03 \u2014 One task, end to end",
           "A broken bench in nine days.",
           "Demo scenario built from the product spec. Amounts and dates are "
           "illustrative, not reported results.")

    # photo pair
    px, py, pw, ph = M, 300, 336, 224
    photo(c, A + "/bench-before.jpg", px, py, pw, ph, r=8,
          overlay=INK, overlay_alpha=0.16)
    photo(c, A + "/bench-after.jpg", px + pw + 10, py, pw, ph, r=8,
          overlay=INK, overlay_alpha=0.10)
    U.chip(c, px + 12, py + 12, "DAY 0 \u00b7 REPORTED", TXT, alpha(INK, 0.55),
         alpha(TXT, 0.2), 7, 16, 6)
    U.chip(c, px + pw + 22, py + 12, "DAY 9 \u00b7 VERIFIED", MINT, alpha(INK, 0.55),
         None, 7, 16, 6)
    text(c, px, py + ph + 24, "Before \u2014 three missing slats, reported from the phone",
         R, 9.4, MUT)
    text(c, px + pw + 10, py + ph + 24, "After \u2014 replaced and re-fixed by Groenwerk BV",
         R, 9.4, MUT)

    # ledger
    x = 810
    label(c, x, 300, "Task ledger \u00b7 public by default", VIO, 8.2, 1.5)
    rows = [
        ("Day 0", "Task published", "\u20ac420 target", SAND),
        ("Day 1", "3 proposals received", "\u20ac380 \u2013 \u20ac455", TXT),
        ("Day 3", "84 residents voted", "62% Groenwerk", TXT),
        ("Day 4", "Escrow funded", "\u20ac420 in USDC", VIO),
        ("Day 7", "Milestone evidence", "6 photos + GPS", TXT),
        ("Day 9", "Dual attestation", "payment released", MINT),
    ]
    y = 322
    vline(c, x + 5, y + 8, y + 8 + 44 * (len(rows) - 1), LINE, 0.8)
    for t, a, b, col in rows:
        U.dot(c, x + 5, y + 8, 3.6, col)
        text(c, x + 22, y + 11, t, MONO, 8.2, MUT_DIM, 0.4)
        text(c, x + 70, y + 11, a, MED, 10.2, TXT)
        text(c, W - M, y + 11, b, MONO, 8.6, MUT, 0.2, "right")
        y += 44

    # footer note
    hline(c, M, 604, W - M, LINE_SOFT)
    label(c, M, 630, "What the resident gets", MUT_DIM, 8, 1.5)
    para(c, M + 190, 630, 300,
         "A public URL with the full history, the contractor's identity and the "
         "final payment.", R, 9.8, 14, MUT)
    label(c, 620, 630, "What the contractor gets", MUT_DIM, 8, 1.5)
    para(c, 826, 630, 340,
         "Milestone payments released in stablecoin the day verification clears "
         "\u2014 no 90-day invoice cycle.", R, 9.8, 14, MUT)
    foot(c, idx, "One task")


# ============================================================ 05  surfaces
def s05(c, idx):
    page(c, True, GRAIN)
    U.head(c, "04 \u2014 The product",
           "Six surfaces, one continuous workflow.",
           "Responsive web app plus an installable mobile PWA. Every screen below "
           "is part of the MVP scope, not a future release.")

    frames = [
        ("Explore", "Map-first discovery with live task markers", "map"),
        ("Project", "Evidence, budget, milestones, discussion", "project"),
        ("Report", "Photo, GPS, category \u2014 under 60 seconds", "report"),
        ("Proposals", "Competing bids with itemised budgets", "proposals"),
        ("Contractor", "Bids, contracts, evidence, payouts", "workspace"),
        ("Completed", "Before / after and the payment record", "done"),
    ]
    cw, ch = 356, 172
    for i, (title, desc, kind) in enumerate(frames):
        col, row = i % 3, i // 3
        x = M + col * (cw + 30)
        y = 232 + row * 216
        U.browser(c, x, y, cw, ch, url="21.city/" + kind)
        c.saveState()
        p = c.beginPath()
        p.roundRect(x, T.ty(y) - ch, cw, ch, 10)
        c.clipPath(p, stroke=0, fill=0)
        U.window_content(c, x, y + 22, cw, ch - 22, kind)
        c.restoreState()
        text(c, x, y + ch + 22, f"0{i + 1}  ", MONO, 8, VIO, 1.2)
        text(c, x + 22, y + ch + 22, title, MED, 10.6, TXT)
        text(c, x + 22 + T.sw(title, MED, 10.6) + 12, y + ch + 22, desc, R, 8.8, MUT)
    foot(c, idx, "Product")


# ============================================================ 06  trust
def s06(c, idx):
    page(c, True, GRAIN)
    U.head(c, "05 \u2014 Verification",
           "Money moves only when the street agrees.",
           "A photo alone is not proof. 21 combines device-signed capture, "
           "geofencing, independent attestors and an economic challenge window.")

    rows = [
        ("Device-signed capture", "Photos are taken in-app: EXIF, GPS, gyroscope and "
                                  "a hardware-backed signature are hashed and stored with the file."),
        ("Proximity, not claims", "The capture must fall inside the task geofence; "
                                  "high-value tasks require a reviewer visit."),
        ("Dual attestation", "A citizen attestor and a city partner sign the milestone. "
                             "A random reviewer is added above \u20ac1,000."),
        ("Challenge window", "72 hours to dispute with a staked bond. Losing a dispute "
                             "costs the bond; winning returns it plus a share of the fee."),
        ("Reputation that cannot be bought", "Scores come from verified work only "
                                             "(ERC-5192, non-transferable) and decay without activity."),
    ]
    y = 236
    for i, (k, v) in enumerate(rows):
        text(c, M, y + 12, f"0{i + 1}", MONO_MED, 8.6, VIO, 1.2)
        text(c, M + 30, y + 12, k, MED, 12, TXT)
        para(c, M + 30, y + 32, 470, v, R, 10, 15, MUT)
        hline(c, M, y + 68, 560, LINE_SOFT)
        y += 76

    # evidence package panel
    x, y0, w, h = 636, 226, 568, 372
    U.card(c, x, y0, w, h, fill=PANEL, stroke=LINE, r=14)
    text(c, x + 22, y0 + 30, "Evidence package", MED, 12.5, TXT)
    U.chip(c, x + w - 132, y0 + 16, "VERIFIED", MINT, alpha(MINT, 0.10), alpha(MINT, 0.35), 7.2, 17, 8)
    photo(c, A + "/bench-after.jpg", x + 22, y0 + 48, 176, 112, r=6)
    meta = [
        ("Content hash", "bafkrei\u2026 4f2c"),
        ("Captured", "2026-03-23T09:14Z"),
        ("GPS", "52.35821, 4.91357 \u00b1 6 m"),
        ("Within geofence", "yes \u00b7 11 m from task"),
        ("Milestone", "M2 \u00b7 re-fix + paint"),
    ]
    my = y0 + 62
    for k, v in meta:
        text(c, x + 216, my, k, MONO, 7.6, MUT_DIM, 0.5)
        text(c, x + 216, my + 13, v, MONO, 8.4, TXT, 0.2)
        my += 32
    hline(c, x + 22, y0 + 182, x + w - 22, LINE_SOFT)
    label(c, x + 22, y0 + 204, "Attestations", MUT_DIM, 7.6, 1.4)
    atts = [("Citizen", "0x8a\u20264c1", MINT), ("City partner", "0x1f\u20269be", MINT),
            ("Reviewer", "0x6c\u20262d7", MINT)]
    for i, (role, addr, col) in enumerate(atts):
        ax = x + 22 + i * 176
        U.card(c, ax, y0 + 216, 164, 52, fill=PANEL_2, stroke=LINE_SOFT, r=8)
        U.dot(c, ax + 16, y0 + 232, 3.2, col)
        text(c, ax + 26, y0 + 235, role, MED, 9.4, TXT)
        text(c, ax + 26, y0 + 250, addr, MONO, 7.6, MUT_DIM, 0.3)
        text(c, ax + 26, y0 + 261, "signed \u00b7 09:41", MONO, 6.8, MUT_DIM, 0.3)
    label(c, x + 22, y0 + 278, "Evidence files", MUT_DIM, 7.4, 1.4)
    for i, (nm, sz) in enumerate((("P1020431", "3.2 MB"), ("P1020434", "2.9 MB"),
                                  ("P1020440", "3.4 MB"), ("site mp4", "18 MB"))):
        fx = x + 22 + i * 136
        photo(c, T.A + ("/bench-after.jpg" if i < 3 else "/crew.jpg"), fx, y0 + 288,
              124, 28, r=3, overlay=INK, overlay_alpha=0.12)
        text(c, fx, y0 + 328, nm, MONO, 6.4, MUT, 0.2)
        text(c, fx + 124, y0 + 328, sz, MONO, 6, MUT_DIM, 0.2, "right")
    # settlement footer
    rect(c, x + 1, y0 + 346, w - 2, 18, fill=alpha(VIO, 0.07))
    hline(c, x + 1, y0 + 346, x + w - 1, alpha(VIO, 0.28), 0.7)
    text(c, x + 22, y0 + 359,
         "Escrow tranche 2 released 09:41 UTC", MONO, 7.2, alpha(VIO, 1.0), 0.3)
    text(c, x + w - 22, y0 + 359, "\u20ac210  \u00b7  tx 0x4c9\u20262a1", MONO, 7.2,
         MUT, 0.3, "right")
    foot(c, idx, "Verification")


# ============================================================ 07  governance
def s07(c, idx):
    page(c, True, GRAIN)
    U.head(c, "06 \u2014 Governance",
           "Funding buys outcomes, not votes.",
           "Each project publishes its rules before the first euro arrives. The "
           "rules hash is pinned on-chain, so the game cannot change mid-round.")

    cards = [
        ("Who may vote", "Three configurable profiles",
         ["Resident: proof-of-personhood inside a 2 km radius",
          "Contributor: any wallet above a \u20ac5 floor",
          "Partner: city wallet, advisory weight only"]),
        ("How money is weighted", "Default profile: one person, one vote",
         ["A \u20ac5 and a \u20ac500 contribution carry equal voice",
          "Token-weighted modes require an explicit opt-in by the city",
          "Quadratic matching from the 21 pool, capped per project"]),
        ("How a winner is chosen", "Approval vote, 5-day window",
         ["Quorum: 25% of eligible voters, minimum 20 people",
          "No quorum \u2192 partner + council decide, rationale published",
          "Losers' proposals stay open for other rounds"]),
    ]
    for i, (k, sub, items) in enumerate(cards):
        x = M + i * 372
        U.card(c, x, 232, 348, 214, fill=PANEL, stroke=LINE, r=12)
        label(c, x + 20, 258, f"0{i + 1}", VIO, 8, 1.4)
        text(c, x + 20, 286, k, MED, 13, TXT)
        text(c, x + 20, 304, sub, R, 9.4, MUT_DIM)
        yy = 332
        for it in items:
            U.dot(c, x + 24, yy - 3, 1.8, VIO)
            yy = para(c, x + 34, yy, 298, it, R, 9.2, 13.5, MUT) + 10

    # matching illustration
    y = 486
    hline(c, M, y, W - M, LINE_SOFT)
    label(c, M, y + 26, "Quadratic matching, illustrated", VIO, 8, 1.5)
    text(c, M, y + 52, "Pool \u20ac1,000 \u00b7 3 projects", MONO, 8.4, MUT, 0.3)
    text(c, M, y + 82, "Every contribution is square-rooted before it counts, so "
                       "twenty small donors outrank one large one.",
         R, 9.2, MUT_DIM)

    demo = [("Bench repair", "\u20ac460", 0.46), ("Bike rack", "\u20ac160", 0.16),
            ("Mural: 21", "\u20ac380", 0.38)]
    bx = 520
    bw = W - M - bx - 90
    yy = y + 22
    for name, amt, share in demo:
        text(c, bx, yy, name, R, 9.2, MUT)
        text(c, W - M, yy, amt, MONO, 9, TXT, 0.2, "right")
        U.progress(c, bx, yy + 8, bw, share, 3.5, VIO)
        yy += 30

    # rule hash strip
    ry = 600
    U.card(c, M, ry, W - 2 * M, 42, fill=PANEL_2, stroke=LINE_SOFT, r=8)
    U.chip(c, M + 16, ry + 11, "RULES HASH", VIO, alpha(VIO, 0.08), alpha(VIO, 0.3), 7, 18, 8)
    text(c, M + 116, ry + 26, "0x9d2e71\u2026c40b  \u00b7  pinned at funding open  \u00b7  "
                              "quorum 25%  \u00b7  5-day vote  \u00b7  one-person-one-vote",
         MONO, 8.2, MUT, 0.2)
    text(c, W - M - 16, ry + 26, "editable only with 72h timelock", R, 8.4,
         MUT_DIM, 0, "right")
    foot(c, idx, "Governance")


# ============================================================ 08  campaign
def s08(c, idx):
    page(c, True, GRAIN)
    U.head(c, "07 \u2014 The cultural layer",
           "21 is a number anyone can paint.",
           "A commissioned, always-authorised mural programme runs alongside the "
           "protocol. It is how a civic tool becomes recognisable on a street in "
           "Lagos or Lisbon without a translation.")

    blocks = [
        ("Commission, never tag", "Every wall has a signed owner consent, a removal "
                                  "clause and a paid artist. The registry refuses "
                                  "locations without a permission record."),
        ("21 murals in 21 cities", "Year one: \u20ac300\u2013\u20ac1,200 per wall, funded by the "
                                   "campaign pool and local sponsors. Each is a "
                                   "Proof-of-Place entry on-chain."),
        ("The number is the message", "No slogan to translate, no logo to explain. "
                                      "Two digits, painted by hand, pointing back to "
                                      "a working protocol."),
    ]
    y = 250
    for i, (k, v) in enumerate(blocks):
        label(c, M, y, f"0{i + 1}", VIO, 8, 1.4)
        text(c, M + 26, y + 2, k, MED, 12.5, TXT)
        para(c, M + 26, y + 22, 470, v, R, 9.8, 14.5, MUT)
        y += 96

    photo(c, A + "/artist-mural.jpg", 636, 214, 568, 300, r=12,
          overlay=INK, overlay_alpha=0.08)
    U.chip(c, 652, 230, "COMMISSIONED \u00b7 BERLIN", TXT, alpha(INK, 0.6),
         alpha(TXT, 0.25), 7, 17, 7)
    fade(c, 636, 454, 568, 60, INK, 0.55, "bottom")
    text(c, 652, 500, "Artist: paid 50% on brief, 50% on documentation", R, 9, alpha(TXT, 0.75))

    # stats strip
    y = 552
    hline(c, M, y - 16, W - M, LINE_SOFT)
    stats = [("21", "cities in year one"), ("\u20ac300\u20131,200", "artist fee per wall"),
             ("100%", "consented walls"), ("1", "permanent registry entry per mural")]
    for i, (a, b) in enumerate(stats):
        x = M + i * ((W - 2 * M) / 4)
        text(c, x, y + 30, a, MED, 22, TXT, -0.4)
        text(c, x, y + 48, b, R, 9.2, MUT)
    foot(c, idx, "The 21 campaign")


# ============================================================ 09  brand
def s09(c, idx):
    page(c, True, GRAIN)
    U.head(c, "08 \u2014 Design system",
           "Serious enough for a treasury.\nSimple enough for a phone.",
           "A compact system ships with the MVP: tokens, components, interaction "
           "states and usage rules, documented in a public Storybook.")

    # ---- wordmark
    U.card(c, M, 250, 420, 268, fill=PANEL, stroke=LINE, r=12)
    label(c, M + 24, 276, "Wordmark", MUT_DIM, 7.4, 1.5)
    t = c.beginText(M + 22, T.ty(382))
    t.setFont(BOLD, 112)
    t.setFillColor(TXT)
    t.setCharSpace(-5)
    t.textOut("21")
    c.drawText(t)
    T.diamond(c, M + 196, 322, 42, VIO)
    text(c, M + 24, 414, "Build the world together.", MED, 14, MUT)
    hline(c, M + 24, 434, M + 396, LINE_SOFT)
    text(c, M + 24, 456, "Lockup: app icon  \u00b7  sticker  \u00b7  wall  \u00b7  favicon",
         MONO, 7.6, MUT_DIM, 0.6)
    text(c, M + 24, 480, "Geist Sans + Geist Mono  \u00b7  OFL  \u00b7  no gradients, no glow",
         R, 8.8, MUT_DIM)

    # ---- palette
    px = 548
    label(c, px, 276, "Palette", MUT_DIM, 7.4, 1.5)
    swatches = [(TXT, "Paper", "#F3F1EC"), (T.PANEL_2, "Graphite", "#16161C"),
                (VIO, "Signal violet", "#8B7CFF"), (T.VIO_DEEP, "Deep violet", "#5343D6"),
                (T.MINT, "Verified", "#7FDCC0"), (SAND, "Sand", "#E4D3B2")]
    for i, (col, name, hexv) in enumerate(swatches):
        sx = px + (i % 3) * 226
        sy = 292 + (i // 3) * 84
        rect(c, sx, sy, 132, 40, fill=col, stroke=LINE, r=5, lw=0.6)
        text(c, sx + 148, sy + 18, name, R, 8.8, TXT)
        text(c, sx + 148, sy + 31, hexv, MONO, 7.2, MUT_DIM, 0.4)

    # ---- type scale
    ty_ = 474
    label(c, px, ty_, "Type scale", MUT_DIM, 7.4, 1.5)
    text(c, px, ty_ + 34, "Display 56 / 60", MED, 26, TXT, -0.4)
    text(c, px + 250, ty_ + 34, "Title 30 / 36", MED, 15, TXT)
    text(c, px + 250, ty_ + 56, "Body 13 / 19", L, 12.4, MUT)
    text(c, px + 250, ty_ + 76, "LABEL 8.5 / MONO / 1.5", MONO_MED, 8, VIO, 1.4)

    # ---- components
    y = 566
    hline(c, M, y - 22, W - M, LINE_SOFT)
    label(c, M, y, "Components", MUT_DIM, 7.4, 1.5)
    bx = M
    bx += U.chip(c, bx, y + 14, "REPORT AN ISSUE", T.INK, VIO, None, 8, 30, 15) + 10
    bx += U.chip(c, bx, y + 18, "EXPLORE MAP", TXT, None, LINE, 8, 22, 12) + 10
    bx += U.chip(c, bx, y + 18, "VERIFIED", MINT, alpha(MINT, 0.1), alpha(MINT, 0.35), 7.2, 22, 9) + 10
    bx += U.chip(c, bx, y + 18, "VOTING OPEN", SAND, alpha(SAND, 0.08), alpha(SAND, 0.3), 7.2, 22, 9) + 10
    bx += U.chip(c, bx, y + 18, "PENDING \u00b7 12s", TXT, None, alpha(VIO, 0.45), 7.2, 22, 9) + 10
    bx += U.chip(c, bx, y + 18, "INSUFFICIENT FUNDS", ALERT, None, alpha(ALERT, 0.4), 7.2, 22, 9) + 10

    label(c, M, y + 66, "Lifecycle", MUT_DIM, 7.4, 1.5)
    text(c, M, y + 86,
         "draft \u2192 proposals \u2192 voting \u2192 funding \u2192 in progress \u2192 "
         "verification \u2192 settled", MONO, 8.2, MUT, 0.2)
    text(c, W - M, y + 86, "one colour, one word, one next action per state",
         R, 8.6, MUT_DIM, 0, "right")
    foot(c, idx, "Design system")


# ============================================================ 10  architecture
def s10(c, idx):
    page(c, True, GRAIN)
    U.head(c, "09 \u2014 Architecture",
           "Boring where it matters.\nVerifiable where it counts.",
           "TypeScript end to end, Foundry for contracts, no custodial backend.")

    # layers
    layers = [
        ("Clients", 244, [("Next.js web app", "Map, tasks, wallet, governance"),
                          ("Mobile PWA", "Camera, GPS, offline queue")]),
        ("Application", 336, [("tRPC API", "Auth, drafts, media, moderation"),
                              ("Ponder indexer", "On-chain events \u2192 Postgres")]),
        ("Storage & identity", 428, [("IPFS + Filecoin", "Content-addressed evidence"),
                                     ("EAS + ENS", "Partner attestations, names")]),
        ("Ethereum", 520, [("Base L2 contracts", "Registry, escrow, governance"),
                           ("L1 anchor", "Daily merkle root of the registry")]),
    ]
    for name, y, node_list in layers:
        label(c, M, y + 12, name, MUT_DIM if name != "Ethereum" else VIO, 7.4, 1.5)
        for i, (t, d) in enumerate(node_list):
            x = 200 + i * 320
            U.card(c, x, y - 14, 300, 56, fill=PANEL if name != "Ethereum" else PANEL_2,
                 stroke=LINE if name != "Ethereum" else alpha(VIO, 0.35), r=8)
            text(c, x + 16, y + 4, t, MED, 10.6, TXT)
            text(c, x + 16, y + 22, d, R, 8.6, MUT)
        if name != "Ethereum":
            U.arrow(c, 660, y + 44, 660, y + 74, MUT_DIM, 0.8, 4)

    # side notes
    x = 872
    notes = [("Gas per task", "< $0.02 on Base"),
             ("Contract standard", "Solidity 0.8 / Foundry"),
             ("Upgrade policy", "Immutable core + factory"),
             ("Data on-chain", "State + hashes, never media"),
             ("Who can pause", "3-of-5 guardian, 48h delay")]
    U.card(c, x, 196, W - M - x, 340, fill=PANEL, stroke=LINE, r=12)
    label(c, x + 18, 222, "Constraints", MUT_DIM, 7.4, 1.4)
    yy = 246
    for k, v in notes:
        text(c, x + 18, yy, k, R, 8.6, MUT_DIM)
        text(c, x + 18, yy + 15, v, MED, 9.6, TXT)
        hline(c, x + 18, yy + 26, W - M - 18, LINE_SOFT)
        yy += 50

    # trust boundary
    U.card(c, M, 594, W - 2 * M, 52, fill=PANEL_2, stroke=LINE_SOFT, r=8)
    label(c, M + 18, 616, "Trust boundary", MUT_DIM, 7.4, 1.4)
    text(c, M + 18, 634,
         "Funds live in escrow contracts. The 21 server can censor a list, but it "
         "cannot move, freeze or redirect a single euro.", R, 9.4, MUT)
    foot(c, idx, "Architecture")


# ============================================================ 11  contracts
def s11(c, idx):
    page(c, True, GRAIN)
    U.head(c, "10 \u2014 Smart contracts",
           "Eight small contracts, one escrow per task.",
           "Immutable core deployed by a factory, so each task gets its own escrow "
           "address and its own accounting. No proxy admin can touch user funds.")

    rows = [
        ("TaskRegistry", "Canonical task record: geohash, category, media CID, status", "core"),
        ("ProposalBook", "Bids, itemised budgets, milestone schedule, withdrawal", "core"),
        ("FundingPool", "Contributions, refunds on failure, matching accounting", "core"),
        ("Escrow", "Per-task USDC, milestone tranches, release conditions", "value"),
        ("Verification", "Attestation quorum, evidence CIDs, challenge window", "core"),
        ("Dispute", "Staked arbiters, slashing, escalation to council", "core"),
        ("Reputation", "Non-transferable score from verified completions", "side"),
        ("Treasury", "Matching pool, Safe multisig + 72h timelock", "side"),
    ]
    y = 226
    for name, desc, kind in rows:
        U.card(c, M, y, 636, 40, fill=PANEL if kind != "value" else PANEL_2,
             stroke=LINE if kind != "value" else alpha(VIO, 0.4), r=7)
        text(c, M + 16, y + 24, name, MONO_MED, 9.4, TXT, 0.2)
        text(c, M + 186, y + 24, desc, R, 8.8, MUT)
        U.dot(c, M + 616, y + 20, 2.6, VIO if kind == "value" else LINE)
        y += 46

    # escrow state machine
    sx, sy = 760, 226
    label(c, sx, sy - 8, "Escrow lifecycle", VIO, 8, 1.5)
    states = [("Draft", "rules pinned"), ("Funded", "target reached"),
              ("Building", "tranche 1 out"), ("Review", "evidence in"),
              ("Settled", "balance released")]
    yy = sy + 18
    for i, (st, note) in enumerate(states):
        U.card(c, sx, yy, 220, 44, fill=PANEL, stroke=LINE, r=7)
        U.dot(c, sx + 18, yy + 22, 3.2, VIO if i < 4 else MINT)
        text(c, sx + 32, yy + 20, st, MED, 9.8, TXT)
        text(c, sx + 32, yy + 33, note, R, 7.6, MUT_DIM)
        if i < 4:
            U.arrow(c, sx + 110, yy + 44, sx + 110, yy + 56, MUT_DIM, 0.8, 4)
        yy += 56

    # dispute branch
    U.card(c, sx + 236, sy + 130, 150, 96, fill=PANEL, stroke=alpha(ALERT, 0.35), r=7)
    text(c, sx + 250, sy + 152, "Disputed", MED, 9.4, ALERT)
    para(c, sx + 250, sy + 168, 122, "Escrow frozen. Arbiters stake, review, decide.",
         R, 7.6, 10.5, MUT)
    text(c, sx + 250, sy + 206, "max 14 days", MONO, 7, MUT_DIM, 0.4)
    U.arrow(c, sx + 220, sy + 178, sx + 236, sy + 178, ALERT, 0.8, 4)

    U.card(c, M, 596, W - 2 * M, 40, fill=PANEL_2, stroke=LINE_SOFT, r=7)
    text(c, M + 16, 621,
         "Escrow rules are hashed and emitted on TaskPublished. A task cannot be "
         "funded until its payment logic is immutable.", R, 9.2, MUT)
    foot(c, idx, "Contracts")


# ============================================================ 12  security
def s12(c, idx):
    page(c, True, GRAIN)
    U.head(c, "11 \u2014 Security & threat model",
           "The attacker is a person with a camera.",
           "Physical-world verification has adversarial failure modes that a normal "
           "audit does not catch. Each one is handled explicitly.")

    cols = ["Threat", "Why it is real", "Mitigation in the MVP"]
    xs = [M, 332, 760]
    y = 232
    hline(c, M, y, W - M, LINE)
    for i, col in enumerate(cols):
        label(c, xs[i], y - 10, col, MUT_DIM, 7.4, 1.5)
    y += 10
    rows = [
        ("Fabricated or AI-generated proof",
         "A model can draw a fixed bench in seconds.",
         "In-app capture only, signed device metadata, C2PA content credentials, phash dedupe, human spot audits."),
        ("GPS spoofing",
         "Mock locations are one developer setting away.",
         "Geofence + cell/Wi-Fi corroboration, on-site reviewer above \u20ac1,000, anomalous-radius flags."),
        ("Reporter\u2013contractor collusion",
         "The easiest way to extract money from a pool.",
         "Role separation, random reviewer panel, reputation at risk, payout caps for new addresses."),
        ("Sybil voting",
         "Free wallets, cheap votes.",
         "Personhood-gated eligibility, snapshot at vote open, one-person-one-vote as the default."),
        ("Escrow bug or exploit",
         "Contracts hold real money on day one.",
         "Two independent audits, invariant fuzzing, per-task caps, 3-of-5 guardian pause with 48h delay."),
        ("Privacy of residents",
         "Photos contain faces, plates and windows.",
         "On-device blur, coarse public coordinates, off-chain personal data, GDPR DPIA before pilot 1."),
    ]
    row_h = 52
    for i, (a, b, cc_) in enumerate(rows):
        yy = y + 12 + i * row_h
        if i % 2 == 0:
            rect(c, M - 12, yy - 4, W - 2 * M + 24, row_h - 8,
                 fill=alpha(PANEL, 0.6), r=5)
        text(c, xs[0], yy + 20, a, MED, 9.8, TXT)
        para(c, xs[1], yy + 20, 360, b, R, 9, 12.5, MUT, max_lines=2)
        para(c, xs[2], yy + 20, 400, cc_, R, 9, 12.5, MUT, max_lines=2)
        hline(c, M, yy + row_h - 10, W - M, LINE_SOFT, 0.5)

    text(c, M, 602, "Open question we bring to reviewers: what is the minimum viable "
                    "proof for a \u20ac300 repair that still resists a determined "
                    "faker?", L, 9.6, MUT_DIM)
    foot(c, idx, "Security")


# ============================================================ 13  roadmap
def s13(c, idx):
    page(c, True, GRAIN)
    U.head(c, "12 \u2014 Roadmap",
           "Ten months from spec to three live cities.",
           "Every milestone ships something a reviewer can open, test or audit. "
           "Nothing is marked done without a public artefact.")

    x0, y0 = 356, 262
    colw = (W - M - x0) / 10
    hline(c, x0, y0 - 14, W - M, LINE)
    for i in range(10):
        text(c, x0 + colw * i + colw / 2, y0 - 22, f"M{i + 1}", MONO, 7.6, MUT_DIM, 0.8, "center")
        if i:
            vline(c, x0 + colw * i, y0 - 14, 560, LINE_SOFT, 0.5)

    bars = [
        ("Spec, threat model, design system", 0, 1.5, MUT),
        ("Contracts v1 + invariant tests", 1, 1.6, VIO),
        ("Web app alpha: report \u2192 task \u2192 map", 2, 1.8, VIO),
        ("Funding, voting, escrow UI", 3.2, 1.6, VIO),
        ("Verification, dispute, reputation", 4.4, 1.8, VIO),
        ("Two independent audits + fixes", 5.4, 1.6, SAND),
        ("Mainnet on Base \u00b7 pilot city 1", 6.2, 1.2, MINT),
        ("Contractor workspace + mobile PWA", 6.8, 1.4, MINT),
        ("Pilot cities 2 and 3", 7.6, 1.6, MINT),
        ("Open-source release, SDK, public report", 9, 1.0, TXT),
    ]
    y = y0 + 18
    for name, start, dur, col in bars:
        text(c, M, y + 12, name, R, 8.6, TXT)
        bx = x0 + start * colw
        bw = max(6, dur * colw)
        rect(c, bx, y + 4, bw, 12, fill=alpha(col, 0.28 if col != MUT else 0.12), r=3)
        rect(c, bx, y + 4, bw, 12, fill=None, stroke=alpha(col, 0.55), r=3, lw=0.6)
        y += 30

    # gate markers
    gates = [(6.2, "audit gate"), (10, "close-out")]
    for gx, name in gates:
        pass

    y = 596
    hline(c, M, y, W - M, LINE_SOFT)
    label(c, M, y + 24, "Release gates", MUT_DIM, 7.4, 1.5)
    gates_text = [("M6", "audits closed \u00b7 no critical or high findings open"),
                  ("M7", "first real euro spent through escrow"),
                  ("M10", "three pilots, public report, open SDK")]
    for i, (g, t) in enumerate(gates_text):
        x = 356 + i * 350
        U.chip(c, x, y + 12, g, VIO, alpha(VIO, 0.08), alpha(VIO, 0.3), 7, 18, 7)
        text(c, x + 40, y + 26, t, R, 9, MUT)
    foot(c, idx, "Roadmap")


# ============================================================ 14  milestones
def s14(c, idx):
    page(c, True, GRAIN)
    U.head(c, "13 \u2014 Milestones",
           "What the grant actually pays for.",
           "Acceptance criteria are written as artefacts, not intentions. Each "
           "milestone is reviewed before the next tranche is released.")

    rows = [
        ("M1", "Protocol spec + threat model", "Published RFC, 2 external reviews", 5),
        ("M2", "Contracts on testnet", "90%+ coverage, invariants fuzzed, testnet deploy", 10),
        ("M3", "Alpha app: report \u2192 task \u2192 escrow", "A bench task completed end-to-end on testnet", 15),
        ("M4", "Verification + dispute modules", "Dual attestation and a resolved dispute in a live drill", 10),
        ("M5", "Two independent audits", "Reports published; all critical/high fixed", 20),
        ("M6", "Base mainnet launch", "Verified contracts, per-task cap, guardian live", 10),
        ("M7", "Three city pilots", "3 partners, 20 tasks each, real payouts", 20),
        ("M8", "Open source + SDK", "MIT release, docs, 3 external integrators", 10),
    ]
    y = 216
    hline(c, M, y, W - M, LINE)
    heads = [("", M), ("Milestone", M + 60), ("Acceptance criterion", 420)]
    for t, x in heads:
        if t:
            label(c, x, y - 10, t, MUT_DIM, 7.4, 1.4)
    label(c, 1044, y - 10, "Share", MUT_DIM, 7.4, 1.4, "right")
    y += 12
    for code, name, crit, share in rows:
        text(c, M, y + 16, code, MONO_MED, 8.4, VIO, 1.0)
        text(c, M + 60, y + 16, name, MED, 10.4, TXT)
        para(c, 420, y + 16, 560, crit, R, 9.2, 12.5, MUT, max_lines=2)
        text(c, 1044, y + 16, f"{share}%", MONO, 9, TXT, 0.3, "right")
        U.progress(c, 1064, y + 12, 56, share / 25, 3.5, alpha(VIO, 0.8))
        hline(c, M, y + 32, W - M, LINE_SOFT, 0.5)
        y += 44

    text(c, M, 606, "Cumulative release: 15% by M2, 40% by M4, 70% by M6, 100% at "
                    "close-out. An unmet criterion means an unpaid milestone, "
                    "not a renegotiation.", L, 9.4, MUT_DIM)
    foot(c, idx, "Milestones")


# ============================================================ 15  budget
def s15(c, idx):
    page(c, True, GRAIN)
    U.head(c, "14 \u2014 Budget",
           "$75,000, allocated line by line.",
           "People, audits and pilots. No token, no marketing spend, no margin hidden "
           "in the total.")

    items = [
        ("Smart contracts, tests, two audits", 24000, VIO),
        ("Product, frontend, mobile PWA", 18000, alpha(VIO, 0.8)),
        ("Backend, indexer, storage pipeline", 9500, alpha(VIO, 0.62)),
        ("Verification, dispute and reviewer tooling", 7500, alpha(VIO, 0.48)),
        ("Three city pilots and the mural programme", 9000, MINT),
        ("Design system, documentation, Storybook", 4000, alpha(MINT, 0.7)),
        ("Legal, GDPR review, operations, travel", 3000, SAND),
    ]
    total = sum(i[1] for i in items)

    # stacked bar
    bx, bw, by = M, W - 2 * M, 230
    xx = bx
    for name, amt, col in items:
        wseg = bw * amt / total
        rect(c, xx, by, wseg - 2, 26, fill=col, r=3)
        xx += wseg
    text(c, bx, by + 52, "Total $75,000  \u00b7  10 months  \u00b7  2 FTE + 1 part-time",
         MONO, 8.6, MUT, 0.5)

    # table
    y = 326
    hline(c, M, y, W - M, LINE)
    label(c, M, y - 10, "Line item", MUT_DIM, 7.4, 1.4)
    label(c, 860, y - 10, "Share", MUT_DIM, 7.4, 1.4)
    label(c, 1204, y - 10, "USD", MUT_DIM, 7.4, 1.4, "right")
    y += 16
    for name, amt, col in items:
        rect(c, M, y + 10, 6, 6, fill=col, r=1.5)
        text(c, M + 18, y + 16, name, R, 9.8, TXT)
        U.progress(c, 860, y + 11, 160, amt / 24000, 3, alpha(col, 0.9))
        text(c, 1036, y + 16, f"{amt / total * 100:.0f}%", MONO, 8.4, MUT_DIM, 0.3)
        text(c, 1204, y + 16, f"${amt:,}", MONO, 9, TXT, 0.2, "right")
        hline(c, M, y + 30, W - M, LINE_SOFT, 0.5)
        y += 36

    text(c, M, 630, "If the grant is smaller than requested, the audits and the "
                    "mainnet launch are the last things we cut.", L, 9.4, MUT_DIM)
    foot(c, idx, "Budget")


# ============================================================ 16  team
def s16(c, idx):
    page(c, True, GRAIN)
    U.head(c, "15 \u2014 Team",
           "Three roles, named before the first tranche.",
           "21 is a small team plus one municipal advisor. Replace the bracketed "
           "fields with names and profile links before submission.")

    people = [
        ("Protocol lead", "contracts",
         "Solidity and Foundry, escrow design, one prior public-goods deployment. "
         "Owns M1\u2013M6 and both audits."),
        ("Product & design lead", "product",
         "Civic interfaces, map and form UX, accessible design systems. "
         "Owns M3, M7 and the pilot onboarding."),
        ("Full-stack engineer", "backend",
         "Next.js, indexer, media pipeline, PWA capture and offline queue. "
         "Owns M3 and M7."),
    ]
    for i, (role, key, desc) in enumerate(people):
        x = M + i * 372
        U.card(c, x, 222, 348, 168, fill=PANEL, stroke=LINE, r=12)
        c.saveState()
        c.setFillColor(PANEL_3)
        c.circle(x + 42, T.ty(264), 20, stroke=0, fill=1)
        c.restoreState()
        text(c, x + 42, 270, role[0], MED, 14, MUT, 0, "center")
        text(c, x + 74, 260, role, MED, 11.6, TXT)
        text(c, x + 74, 276, key, MONO, 7.2, VIO, 0.8)
        text(c, x + 24, 302, "[name]  \u00b7  [github / linkedin]", MONO, 7.8, MUT_DIM, 0.3)
        para(c, x + 24, 322, 300, desc, R, 9.2, 13.5, MUT)
        text(c, x + 24, 376, "commitment: full time, 10 months", MONO, 6.8, MUT_DIM, 0.3)

    # advisor
    U.card(c, M, 418, 660, 116, fill=PANEL_2, stroke=LINE_SOFT, r=10)
    label(c, M + 20, 442, "Advisor", MUT_DIM, 7.4, 1.4)
    text(c, M + 20, 466, "Municipal procurement + public-art permissions", MED, 10.2, TXT)
    para(c, M + 20, 482, 610, "A former city procurement officer reviews pilot "
                              "contracts, consent templates and the mural programme "
                              "before any wall is touched.  [name \u00b7 organisation]",
         R, 8.8, 12.5, MUT)

    # how we work
    U.card(c, 752, 418, 452, 116, fill=PANEL, stroke=LINE, r=10)
    label(c, 772, 442, "How we work", MUT_DIM, 7.4, 1.4)
    rules = ["Public roadmap, public repo, weekly demo",
             "Every payment in milestone tranches",
             "No token, no presale, no paid listings"]
    yy = 468
    for r_ in rules:
        U.dot(c, 776, yy - 3, 1.9, VIO)
        text(c, 788, yy, r_, R, 9, MUT)
        yy += 20

    # what we still need
    hline(c, M, 566, W - M, LINE_SOFT)
    label(c, M, 588, "Open role funded by tranche 2", MUT_DIM, 7.4, 1.4)
    text(c, M, 610, "Verification & field-operations lead \u2014 runs reviewer panels "
                    "in the three pilot cities.", R, 9.4, MUT)
    label(c, 760, 588, "Not applying for", MUT_DIM, 7.4, 1.4)
    text(c, 760, 610, "Marketing budget, token liquidity, or exchange listings.",
         R, 9.4, MUT)
    foot(c, idx, "Team")


# ============================================================ 17  metrics
def s17(c, idx):
    page(c, True, GRAIN)
    U.head(c, "16 \u2014 Success metrics",
           "Targets, not traction.",
           "21 is pre-launch. These are the numbers we commit to reporting at "
           "close-out, with the methodology published alongside them.")

    metrics = [
        ("3", "city partners under a signed pilot agreement"),
        ("60", "tasks published, verified and settled"),
        ("\u20ac45k", "value moved through escrow"),
        ("25", "contractors paid, median payout < 24h"),
        ("21", "commissioned murals registered on-chain"),
        ("500", "unique participants with proof-of-personhood"),
    ]
    for i, (big, small) in enumerate(metrics):
        col, row = i % 3, i // 3
        x = M + col * 376
        y = 226 + row * 150
        U.card(c, x, y, 352, 128, fill=PANEL, stroke=LINE, r=10)
        text(c, x + 22, y + 54, big, MED, 32, TXT, -1)
        para(c, x + 22, y + 78, 300, small, R, 9.4, 13, MUT)

    # guardrail metrics
    U.card(c, M, 528, W - 2 * M, 92, fill=PANEL_2, stroke=LINE_SOFT, r=10)
    label(c, M + 20, 552, "Guardrail metrics \u2014 we fail if these move the wrong way", ALERT, 7.4, 1.4)
    guard = [("Fraud rate", "< 1% of released value"), ("Dispute rate", "< 8% of tasks"),
             ("Time to first proposal", "< 72h median"), ("Repeat contractors", "> 40%")]
    for i, (k, v) in enumerate(guard):
        x = M + 24 + i * 272
        text(c, x, 580, v, MED, 10.2, TXT)
        text(c, x, 596, k, R, 8.4, MUT_DIM)
    foot(c, idx, "Metrics")


# ============================================================ 18  why eth
def s18(c, idx):
    page(c, True, GRAIN)
    U.head(c, "17 \u2014 Why Ethereum",
           "Because the alternative is a database\nsomeone else controls.",
           "A civic platform that holds public money should not be able to rewrite "
           "its own history. Ethereum gives 21 four properties no SaaS can offer.")

    reasons = [
        ("Neutral settlement", "No company sits between a resident's euro and a "
                               "contractor's invoice. The escrow is the counterparty."),
        ("A global payment rail", "USDC on Base pays a contractor in Nairobi or "
                                  "Nijmegen in seconds, without a bank account."),
        ("Composable public goods", "Quadratic funding, retro funding, EAS "
                                     "attestations and Safe treasuries plug in unchanged."),
        ("Permanent public record", "What was promised, funded and delivered stays "
                                    "queryable \u2014 even if 21 disappears."),
    ]
    for i, (k, v) in enumerate(reasons):
        x = M + (i % 2) * 568
        y = 236 + (i // 2) * 118
        text(c, x, y, f"0{i + 1}", MONO_MED, 8.4, VIO, 1.2)
        text(c, x + 30, y, k, MED, 12.6, TXT)
        para(c, x + 30, y + 22, 470, v, R, 9.6, 14, MUT)

    # what we do not do
    U.card(c, M, 476, 660, 144, fill=PANEL_2, stroke=LINE_SOFT, r=10)
    label(c, M + 20, 500, "What 21 deliberately does not do", MUT_DIM, 7.4, 1.4)
    no = ["No token sale and no speculative asset",
          "No custody of user funds at any point",
          "No paid placement of projects or contractors",
          "No growth metrics that are not on-chain verifiable"]
    yy = 526
    for n in no:
        text(c, M + 20, yy, "\u00d7", MONO, 9, alpha(ALERT, 0.8))
        text(c, M + 36, yy, n, R, 9.4, MUT)
        yy += 22

    # ecosystem ask
    U.card(c, 752, 476, 452, 144, fill=PANEL, stroke=alpha(VIO, 0.3), r=10)
    label(c, 772, 500, "Where the grant fits", VIO, 7.4, 1.4)
    para(c, 772, 524, 412,
         "21 is public-goods infrastructure: an open registry and escrow any city, "
         "DAO or funding round can build on. The grant funds the protocol and the "
         "first three proofs, not a company's growth.", R, 9.4, 14, MUT)
    foot(c, idx, "Why Ethereum")


# ============================================================ 19  after
def s19(c, idx):
    page(c, True, GRAIN)
    U.head(c, "18 \u2014 After the grant",
           "Built to outlive the funding round.",
           "The protocol is open source and unowned. Revenue, if any, is optional "
           "and capped; the public instance stays free for residents.")

    cols = [
        ("01", "Sustainable by design",
         ["Optional 1.5% fee on released escrow, capped and opt-in per city",
          "Hosted instance + support subscription for municipalities",
          "Matching pools funded by partners, not by the protocol"]),
        ("02", "Progressive decentralisation",
         ["M1\u2013M6: core team ships, guardian multisig holds pause rights",
          "M7\u2013M10: council elected by contributors, parameters on-chain",
          "Year 2: registry ownership renounced; fee switch under token-less vote"]),
        ("03", "What stays open",
         ["Contracts, indexer and client under MIT",
          "Public data export: every task, attestation and payment",
          "A documented schema so other cities can fork without us"]),
    ]
    for i, (n, k, items) in enumerate(cols):
        x = M + i * 372
        text(c, x, 236, n, MONO, 8.4, VIO, 1.2)
        text(c, x, 258, k, MED, 12.4, TXT)
        yy = 290
        for it in items:
            U.dot(c, x + 3, yy - 3, 1.9, VIO)
            yy = para(c, x + 14, yy, 320, it, R, 9.2, 13.5, MUT) + 12

    # next phase
    U.card(c, M, 470, W - 2 * M, 148, fill=PANEL, stroke=LINE, r=12)
    label(c, M + 24, 496, "If the pilot works, the next eighteen months look like", MUT_DIM, 7.4, 1.4)
    steps = [("10 cities", "EU + one emerging-market\nmunicipality"),
             ("300 tasks", "recurring maintenance,\nnot one-off demos"),
             ("\u20ac1m escrow", "mostly partner-funded\nmatching pools"),
             ("1 SDK", "any civic org can run\ntheir own instance")]
    for i, (a, b) in enumerate(steps):
        x = M + 24 + i * 272
        text(c, x, 522, a, MED, 20, TXT, -0.4)
        para(c, x, 542, 240, b.replace("\n", " "), R, 8.8, 12, MUT)
    text(c, M, 604, "The registry stays public, the code stays MIT, and the three "
                    "pilots decide whether this is real.", L, 10, MUT_DIM)
    foot(c, idx, "After the grant")


# ============================================================ 20  close
def s20(c, idx):
    page(c, True, GRAIN)
    photo(c, A + "/cover-mural.jpg", 0, 0, W, H, overlay=INK, overlay_alpha=0.72)
    fade(c, 0, 0, 1080, H, INK, 0.96, "left")
    fade(c, 0, 0, W, 160, INK, 0.75, "top")
    fade(c, 0, H - 160, W, 160, INK, 0.8, "bottom")
    glow(c, 940, 560, 420, VIO_DEEP, 0.16)

    logotype(c, M, 74, 24, TXT, VIO)
    label(c, M, 214, "The ask", VIO, 9, 2.0)
    para(c, M, 300, 720, "Build the world\ntogether.", MED, 56, 62, TXT, -1)
    para(c, M, 446, 540,
         "$75,000 over ten months to ship the contracts, audit them, launch on "
         "Base and settle real work in three cities.", L, 13.5, 21, alpha(TXT, 0.75))

    # deliverable chips
    chips = ["Escrow protocol", "Open-source app", "3 city pilots", "21 murals"]
    x = M
    for ch in chips:
        x += U.chip(c, x, 512, ch.upper(), TXT, alpha(TXT, 0.06), alpha(TXT, 0.2),
                    7.4, 26, 12) + 10

    hline(c, M, 606, 720, alpha(TXT, 0.16))
    text(c, M, 636, "21.city", MED, 12, TXT, 0.2)
    text(c, M + 110, 636, "hello@21.city", MONO, 9.4, MUT, 0.3)
    text(c, M + 250, 636, "github.com/21-movement", MONO, 9.4, MUT, 0.3)

    text(c, W - M, 636, "Thank you.", MED, 12, alpha(TXT, 0.6), 0, "right")
    foot(c, idx)


SLIDES = [s01, s02, s03, s04, s05, s06, s07, s08, s09, s10, s11, s12, s13, s14,
          s15, s16, s17, s18, s19, s20]
assert len(SLIDES) == TOTAL


def build(path):
    c = rl_canvas.Canvas(path, pagesize=(W, H))
    c.setTitle("21 \u2014 Ethereum-native civic infrastructure")
    c.setAuthor("21")
    c.setSubject("Ethereum ecosystem grant application \u2014 2026")
    c.setKeywords("Ethereum, public goods, civic infrastructure, escrow, grant")
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
            pg = doc[i].render(scale=1.1).to_pil()
            pg.save(os.path.join(T.PREVIEW, f"p{i + 1:02d}.png"))
        print("previews:", len(doc))
