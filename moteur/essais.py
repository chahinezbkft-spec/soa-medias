"""Reels d'essai TikTok « ultra tendance » (méthode soa-marketing/06-reels-tendance.md).
Une fonction par reel d'essai, nommée par date. Rendu : python moteur/essais.py e20261103_1 [still 0.5,4,9]
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import render, still

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sortie")
os.makedirs(OUT, exist_ok=True)
G = "saturate(.88) sepia(.18) contrast(1.04)"
CAN, CHOC, CAR, CREME = "#7A4636", "#3A2820", "#B88A63", "#EFE5DA"
FX = [{"type": "grain"}]


def vid(clip, st, zoom=(1.0, 1.1), **kw):
    d = {"type": "video", "clip": clip, "start": st, "zoom": list(zoom), "grade": G}; d.update(kw); return d


def txt(lines, at, style="hook", y=50, anim="mask", **kw):
    d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim}; d.update(kw); return d


def dim(a=.35):
    return {"type": "dim", "color": f"rgba(42,28,22,{a})"}


TOP = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.78), rgba(42,28,22,.45) 45%, rgba(42,28,22,.15) 75%)"}


def fin(clip, st, pill=None):
    """Carton final charte : panneau chocolat, coaché · digital · hybride, pack 36 €, @soa.reformer."""
    L = [vid(clip, st, (1.12, 1.0)),
         {"type": "panel", "color": CHOC, "box": [0, 900, 1080, 1020], "from": "bottom", "at": 0.1, "dur": 0.5},
         txt(["coaché · digital · hybride"], (0.4, 9), "kicker", y=53, anim="track", align="left", x=8.5),
         txt(["Pilates reformer", "à *La~Varenne.*"], (0.55, 9), "hook", y=62, anim="mask", align="left", x=8.5)]
    if pill:
        L.append(txt([pill], (0.9, 9), "pill", y=73, anim="pop", align="left", x=8.5))
    L.append(txt(["pack découverte : 1 coachée + 1 digitale · 36 €"], (1.1, 9), "small", y=80.5, anim="fade", align="left", x=8.5))
    L.append(txt(["@soa.reformer · lien en bio"], (1.3, 9), "kicker", y=86.5, anim="fade", align="left", x=8.5, color=CREME))
    return {"dur": 2.6, "in": "wipe", "wipeColor": CAN, "out": "fadeblack", "layers": L + FX}


def e20261103_1():
    """Tendance « Loading / Recharged » : batterie 1 % → 100 % (Banque d'idées SOA-20261102-03)."""
    def step(clip, st, a, b, line, tin, tout, anim, extra=None, dur=1.8):
        L = [vid(clip, st, (1.04, 1.16)), dim(.25), TOP,
             {"type": "panel", "color": CHOC, "box": [70, 260, 520, 250], "at": 0, "dur": 0.01},
             {"type": "counter", "from": a, "to": b, "at": 0.05, "dur": 1.0, "style": "giant", "suffix": "%",
              "y": 20, "x": 9.5, "align": "left", "color": CREME},
             txt([line], (0.3, 9), "mid", y=33, anim=anim, align="left", x=8.5)]
        return {"dur": dur, "in": tin, "out": tout, "bpm": 120, "layers": L + (extra or []) + FX}
    return {"scenes": [
        # accroche : la batterie à 1 %
        {"dur": 2.0, "in": "cut", "out": "whip", "layers": [
            vid("IMG_9311", 0.2, (1.0, 1.1)), dim(.35), TOP,
            {"type": "panel", "color": CHOC, "box": [70, 760, 430, 290], "at": 0.3, "dur": 0.3},
            txt(["ta batterie"], (0.0, 9), "hook", y=24, anim="mask", align="left", x=8.5),
            txt(["après *ta~journée~:*"], (0.15, 9), "hook", y=31, anim="mask", align="left", x=8.5),
            {"type": "counter", "from": 1, "to": 1, "at": 0.35, "dur": 0.1, "style": "giant", "suffix": "%", "y": 47, "x": 9.5, "align": "left", "color": CREME},
            txt(["chargement…"], (0.6, 9), "kicker", y=58, anim="track", align="left", x=9, color=CREME),
        ] + FX},
        step("IMG_7151", 0.5, 1, 27, "on s'allonge.", "whip", "zoom", "swipe"),
        step("IMG_1039", 1.0, 27, 64, "on gaine *(fort).*", "punch", "wipe", "mask"),
        step("IMG_6792", 6.0, 64, 89, "on rit *beaucoup.*", "iris", "whip", "scale",
             extra=[{"type": "leak", "opacity": .45}]),
        # 100 % : le matcha
        {"dur": 2.0, "in": "whip", "out": "cut", "shake": True, "layers": [
            vid("IMG_9452", 0.6, (1.08, 1.0)), dim(.25), TOP,
            {"type": "panel", "color": CHOC, "box": [70, 260, 790, 250], "at": 0, "dur": 0.01},
            {"type": "panel", "color": CAN, "box": [70, 540, 420, 200], "at": 0.4, "dur": 0.35},
            {"type": "counter", "from": 89, "to": 100, "at": 0.0, "dur": 0.6, "style": "giant", "suffix": "%", "y": 20, "x": 9.5, "align": "left", "color": CREME},
            txt(["*à~bloc.*"], (0.5, 9), "big", y=33.5, x=9, anim="letters", align="left", color=CREME),
            {"type": "underline", "x": 110, "y": 760, "w": 330, "at": 0.9},
        ] + FX},
        fin("IMG_3354", 2.5, pill="tu es à combien ce soir ?"),
    ]}


def e20261103_2():
    """Humour « mon reformer » (Banque d'idées SOA-20261026-02)."""
    return {"scenes": [
        {"dur": 2.2, "in": "cut", "out": "whip", "layers": [
            vid("IMG_1461", 0.0, (1.0, 1.12)), dim(.3), TOP,
            txt(["quand quelqu'un", "prend *mon~reformer.*"], (0.05, 9), "hook", y=24, anim="mask", align="left", x=8.5, stagger=0.06),
            {"type": "underline", "x": 470, "y": 590, "w": 470, "at": 0.8},
        ] + FX},
        {"dur": 1.8, "in": "whip", "out": "zoom", "layers": [
            vid("IMG_1466", 0.0, (1.1, 1.2)), dim(.3), TOP,
            {"type": "panel", "color": CHOC, "box": [190, 540, 720, 190], "at": 0.4, "dur": 0.35},
            txt(["celui près de la vitrine."], (0.1, 9), "mid", y=24, anim="swipe", align="left", x=8.5),
            txt(["*avec~la~vue.*"], (0.55, 9), "big", y=32.5, anim="swipe", align="left", x=20, color=CAR),
        ] + FX},
        {"dur": 2.0, "in": "punch", "out": "wipe", "wipeColor": CHOC, "shake": True, "layers": [
            vid("IMG_2717", 0.4, (1.0, 1.12)), dim(.3), TOP,
            txt(["il n'a jamais été à moi."], (0.05, 9), "mid", y=22, anim="words", align="left", x=8.5),
            txt(["mais je l'ai", "*adopté.*"], (0.6, 9), "big", y=33, anim="scale", align="left", x=8.5, stagger=0.08),
        ] + FX},
        {"dur": 2.0, "in": "cut", "out": "whip", "bpm": 120, "layers": [
            {"type": "color", "color": CAN},
            {"type": "video", "clip": "IMG_3061", "start": 0.3, "zoom": [1.1, 1.2], "grade": G, "box": [0, 0, 1080, 1060], "slide": "y", "slideFrom": -1100, "at": 0},
            {"type": "counter", "from": 0, "to": 7, "at": 0.3, "dur": 0.8, "style": "giant", "y": 70, "x": 9.5, "align": "left", "color": CREME},
            txt(["places par cours."], (0.5, 9), "mid", y=79, anim="mask", align="left", x=8.5),
            txt(["*réserve~tôt.*"], (0.8, 9), "big", y=87, anim="mask", align="left", x=8.5, color=CAR),
        ] + FX},
        fin("IMG_3354", 6.0, pill="tague ton binôme de reformer"),
    ]}


def e20261104_1():
    """Tendance « pose ton téléphone » : post-it manuscrit qui s'écrit mot à mot (Banque d'idées SOA-20261103-06, idée de Chahinez)."""
    POSTIT = [{"type": "panel", "color": CREME, "box": [70, 230, 560, 690], "at": 0, "dur": 0.01},
              {"type": "panel", "color": CAR, "box": [250, 204, 200, 52], "at": 0, "dur": 0.01}]
    BLOCS = [(["pose~ton", "téléphone"], 19.4), (["et~viens"], 27.3), (["bouger."], 32.6), (["(puis~boire", "un~matcha)"], 41.4)]

    def note(k, t0):
        """Les blocs déjà écrits restent ; le bloc k s'écrit lettre par lettre à partir de t0."""
        L = []
        for i, (lines, y) in enumerate(BLOCS[:k + 1]):
            col = CAN if i == 3 else CHOC
            L.append(txt(lines, ((t0 if i == k else -5), 99), "hand", y=y, anim="type", align="left", x=11,
                         color=col, size=74, width=480, stagger=0.045, out=False))
        return L

    def sc(clip, st, k, dur, zoom=(1.02, 1.12)):
        return {"dur": dur, "in": "cut", "out": "cut", "layers": [vid(clip, st, zoom), dim(.18)] + POSTIT + note(k, 0.05) + FX}

    return {"scenes": [
        sc("IMG_4850", 0.0, 0, 2.2, (1.0, 1.08)),     # membre au téléphone sur le reformer
        sc("IMG_4618", 0.4, 1, 1.9),                  # arrivée en cours, le coach accueille
        sc("IMG_2707", 1.2, 2, 1.9),                  # cours : jambes en l'air
        sc("IMG_9451", 2.6, 3, 2.5, (1.0, 1.06)),     # le matcha versé sur le lait
        fin("IMG_9060", 1.5, pill="envoie-le à ton binôme matcha"),
    ]}


if __name__ == "__main__":
    name = sys.argv[1]
    spec = globals()[name]()
    num = name.split("_")[1]
    date = name[1:9]
    if len(sys.argv) > 2 and sys.argv[2] == "still":
        still(spec, [float(x) for x in sys.argv[3].split(",")], os.path.join(OUT, f"_{name}.jpg"))
    else:
        render(spec, os.path.join(OUT, f"SOA-essai-{date}-{num}.mp4"))
    print("ok")
