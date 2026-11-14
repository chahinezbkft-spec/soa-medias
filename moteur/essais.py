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


def e20261105_2():
    """Série « fais-le pour… » : ton rythme. Timelapse de la journée avec l'heure qui défile (horloge 07:00 → 22:30,
    horaires réels du studio 7j/7). Idées de Chahinez SOA-20261104-02 + SOA-20261103-03. Style classe, 1 effet signature : horloge."""
    GC = "saturate(.82) sepia(.2) contrast(1.06) brightness(.94)"

    def v(clip, st, zoom=(1.04, 1.12), speed=1.0, grade=GC):
        return {"type": "video", "clip": clip, "start": st, "zoom": list(zoom), "grade": grade, "speed": speed, "extra": 0.9, "ease": "inout"}

    def t(lines, at, style, y, anim="mask", **kw):
        d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim, "align": "left", "x": 8.9,
             "dur": 1.0, "ease": "inout", "stagger": 0.12}
        d.update(kw); return d

    TOPV = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.86), rgba(42,28,22,.5) 30%, rgba(42,28,22,.25) 50%, rgba(42,28,22,.2))"}
    BOTV = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.2), rgba(42,28,22,.3) 45%, rgba(42,28,22,.82))"}
    GR = {"type": "grain", "opacity": .07}

    def clock(a, b, label, y=230, at=0.15, dur=1.3):
        return {"type": "clock", "x": 96, "y": y, "at": at, "from": a, "to": b, "dur": dur, "label": label}

    return {"scenes": [
        # 1. accroche : arrivée au studio (QR code), horloge sur 07:00 ; texte en bas (visage en haut du plan)
        {"dur": 2.4, "in": "fade", "layers": [
            v("IMG_4613", 0.0, (1.0, 1.08)), BOTV,
            clock(420, 420, "ouvert 7j/7", y=1080, at=0.0, dur=0.1),
            t(["fais-le pour"], (0.0, 9), "edito", 75.5, color=CREME),
            t(["*ton~rythme.*"], (0.15, 9), "edito", 82, color=CAR), GR]},
        # 2. séance digitale : l'heure avance (avant le boulot)
        {"dur": 2.0, "in": "window", "windowDur": 0.9, "windowFrom": 22, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_9319", 4.2, (1.1, 1.02)), TOPV,
            clock(420, 480, "avant le boulot ?", at=0.2, dur=1.2),
            t(["en digital,"], (0.5, 9), "edito", 27, color=CREME),
            t(["*à~ton~heure.*"], (0.7, 9), "edito", 33.5, color=CAR), GR]},
        # 3. cours coaché : midi
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.7, "layers": [
            v("IMG_6836", 3.2, (1.02, 1.1)), TOPV,
            clock(480, 750, "à la pause déj ?", at=0.15, dur=1.2),
            t(["en coaché,"], (0.45, 9), "edito", 27, color=CREME),
            t(["*7~places~max.*"], (0.65, 9), "edito", 33.5, color=CAR), GR]},
        # 4. fin de journée, bougies : jusqu'à 22:30
        {"dur": 2.2, "in": "dissolve", "dissolve": 0.7, "layers": [
            v("IMG_0822", 1.0, (1.12, 1.02), speed=0.8, grade="saturate(.8) sepia(.28) contrast(1.06) brightness(.78)"), TOPV,
            clock(750, 1350, "après le dîner ?", at=0.15, dur=1.4),
            t(["ou tard le soir."], (0.5, 9), "edito", 27, color=CREME),
            t(["*jusqu'à~22h30.*"], (0.75, 9), "edito", 33.5, color=CAR), GR]},
        # 5. fin crème : offre
        {"dur": 2.8, "in": "dissolve", "dissolve": 0.7, "out": "fadeblack", "layers": [
            {"type": "color", "color": CREME}, {"type": "grain", "opacity": .1},
            t(["SOA"], (0.3, 9), "logo", 18, anim="track", color=CHOC),
            t(["coaché · digital · hybride"], (0.45, 9), "caps", 36, anim="track", color=CAN),
            t(["fais-le pour"], (0.6, 9), "edito", 44, color=CHOC),
            t(["*ton~rythme.*"], (0.85, 9), "edito", 50.5, color=CAN),
            {"type": "rule", "x": 96, "y": 1110, "w": 300, "at": 1.2, "color": CAN},
            t(["pack découverte"], (1.3, 9), "caps", 62, anim="track", color=CHOC),
            t(["1 coachée + 1 digitale · 36 €"], (1.45, 9), "caps", 65.5, anim="track", color=CHOC),
            t(["@soa.reformer · lien en bio"], (1.7, 9), "caps", 88, anim="fade", color=CAN)]},
    ]}


def serie_faislepour_toi():
    """Série hebdo « fais-le pour… » (1 épisode par semaine, idée de Chahinez SOA-20261104-03) : fais-le pour toi. Prêt, à programmer la semaine du 9 nov. Une personne seule en séance
    digitale, casque sur les oreilles. Style classe ; 2 effets signature : mot géant DERRIÈRE la personne (accroche)
    + interrupteur « mode ne pas déranger »."""
    GC = "saturate(.82) sepia(.2) contrast(1.06) brightness(.94)"

    def v(clip, st, zoom=(1.04, 1.12), speed=1.0, grade=GC):
        return {"type": "video", "clip": clip, "start": st, "zoom": list(zoom), "grade": grade, "speed": speed, "extra": 0.9, "ease": "inout"}

    def t(lines, at, style, y, anim="mask", **kw):
        d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim, "align": "left", "x": 8.9,
             "dur": 1.0, "ease": "inout", "stagger": 0.12}
        d.update(kw); return d

    TOPV = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.86), rgba(42,28,22,.5) 30%, rgba(42,28,22,.25) 50%, rgba(42,28,22,.2))"}
    GR = {"type": "grain", "opacity": .07}
    Z1 = (1.0, 1.07)

    return {"scenes": [
        # 1. accroche : « toi. » géant DERRIÈRE la personne allongée (casque) ; visage en bas à droite, rien dessus
        {"dur": 2.6, "in": "fade", "layers": [
            v("IMG_9319", 5.0, Z1), {"type": "dim", "color": "rgba(42,28,22,.22)"}, TOPV,
            t(["fais-le pour"], (0.0, 9), "edito", 14, color=CREME),
            t(["toi."], (0.2, 9), "giant", 46.5, color=CREME, size=430, dur=1.1),
            {"type": "cutout", "clip": "IMG_9319", "start": 5.0, "zoom": list(Z1), "ease": "inout", "grade": GC, "extra": 0.9},
            GR]},
        # 2. le casque posé sur le chariot (plongée)
        {"dur": 1.9, "in": "dissolve", "dissolve": 0.6, "layers": [
            v("IMG_6639", 7.0, (1.12, 1.02)), TOPV,
            t(["ton casque,"], (0.3, 9), "edito", 12, color=CREME),
            t(["*ton~programme.*"], (0.5, 9), "edito", 18.5, color=CAR), GR]},
        # 3. le doigt lance la séance sur l'écran : interrupteur « ne pas déranger »
        {"dur": 2.1, "in": "window", "windowDur": 0.8, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_6650", 4.0, (1.02, 1.1)), TOPV,
            t(["ta séance,"], (0.3, 9), "edito", 12, color=CREME),
            t(["*rien~qu'à~toi.*"], (0.5, 9), "edito", 18.5, color=CAR),
            {"type": "toggle", "x": 96, "y": 1560, "at": 1.2, "inAt": 0.7, "label": "ne pas déranger", "size": 56}, GR]},
        # 4. plan large : seul·e sur son reformer, à son heure
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.6, "layers": [
            v("IMG_9499", 2.0, (1.0, 1.08)), TOPV,
            t(["seul·e sur ton reformer,"], (0.3, 9), "edito", 8, color=CREME, size=96),
            t(["*à~ton~heure.*"], (0.5, 9), "edito", 13.5, color=CAR, size=96), GR]},
        # 5. fin crème : offre
        {"dur": 2.8, "in": "dissolve", "dissolve": 0.7, "out": "fadeblack", "layers": [
            {"type": "color", "color": CREME}, {"type": "grain", "opacity": .1},
            t(["SOA"], (0.3, 9), "logo", 18, anim="track", color=CHOC),
            t(["coaché · digital · hybride"], (0.45, 9), "caps", 36, anim="track", color=CAN),
            t(["fais-le pour"], (0.6, 9), "edito", 44, color=CHOC),
            t(["*toi.*"], (0.85, 9), "edito", 50.5, color=CAN),
            {"type": "rule", "x": 96, "y": 1110, "w": 300, "at": 1.2, "color": CAN},
            t(["pack découverte"], (1.3, 9), "caps", 62, anim="track", color=CHOC),
            t(["1 coachée + 1 digitale · 36 €"], (1.45, 9), "caps", 65.5, anim="track", color=CHOC),
            t(["@soa.reformer · lien en bio"], (1.7, 9), "caps", 88, anim="fade", color=CAN)]},
    ]}


def e20261106_2():
    """Tendance TikTok « Why Would I Deceive You? » (NewEngen, 05/11/2026 ; Banque d'idées SOA-20261105-INES-03) :
    la promesse du coach « plus que 5 »… et le compteur qui continue. Humour tendre, style classe, 1 effet signature : compteur serif."""
    GC = "saturate(.82) sepia(.2) contrast(1.06) brightness(.94)"

    def v(clip, st, zoom=(1.04, 1.12), speed=1.0, grade=GC, **kw):
        d = {"type": "video", "clip": clip, "start": st, "zoom": list(zoom), "grade": grade, "speed": speed, "extra": 0.9, "ease": "inout"}
        d.update(kw); return d

    def t(lines, at, style, y, anim="mask", **kw):
        d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim, "align": "left", "x": 8.9,
             "dur": 1.0, "ease": "inout", "stagger": 0.12}
        d.update(kw); return d

    TOPV = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.86), rgba(42,28,22,.5) 30%, rgba(42,28,22,.25) 50%, rgba(42,28,22,.2))"}
    GR = {"type": "grain", "opacity": .07}

    return {"scenes": [
        # 1. accroche : la promesse (texte en haut, au-dessus du coach)
        {"dur": 2.3, "in": "fade", "layers": [
            v("IMG_6610", 1.0, (1.0, 1.08)), TOPV,
            t(["ton coach de Pilates :"], (0.0, 9), "caps", 9, anim="track", color=CAR),
            t(["« plus que *5.* »"], (0.05, 9), "edito", 13, color=CREME, size=150), GR]},
        # 2. vidéo en haut, compteur serif qui continue sur aplat cannelle
        {"dur": 2.6, "in": "dissolve", "dissolve": 0.6, "bpm": 120, "layers": [
            {"type": "color", "color": CAN}, {"type": "grain", "opacity": .12},
            v("IMG_6752", 2.0, (1.1, 1.18), box=[0, 0, 1080, 1060]),
            {"type": "counter", "from": 5, "to": 9, "at": 0.2, "dur": 1.8, "style": "numserif", "x": 8.9, "y": 66, "align": "left", "color": CREME},
            t(["« pourquoi je te"], (0.9, 9), "edito", 81, color=CREME, size=96),
            t(["*mentirais~?* »"], (1.1, 9), "edito", 86.5, color=CAR, size=96), GR]},
        # 3. la réaction (texte en haut, visage au centre jamais couvert)
        {"dur": 2.2, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_6801", 1.6, (1.02, 1.1)), TOPV,
            t(["(spoiler :"], (0.2, 9), "edito", 9, color=CREME),
            t(["*c'était~pas~5.)*"], (0.45, 9), "edito", 15.5, color=CAR), GR]},
        # 4. fin crème : offre
        {"dur": 2.8, "in": "dissolve", "dissolve": 0.7, "out": "fadeblack", "layers": [
            {"type": "color", "color": CREME}, {"type": "grain", "opacity": .1},
            t(["SOA"], (0.3, 9), "logo", 18, anim="track", color=CHOC),
            t(["coaché · digital · hybride"], (0.45, 9), "caps", 36, anim="track", color=CAN),
            t(["et tu reviens"], (0.6, 9), "edito", 44, color=CHOC),
            t(["*quand~même.*"], (0.85, 9), "edito", 50.5, color=CAN),
            {"type": "rule", "x": 96, "y": 1110, "w": 300, "at": 1.2, "color": CAN},
            t(["pack découverte"], (1.3, 9), "caps", 62, anim="track", color=CHOC),
            t(["1 coachée + 1 digitale · 36 €"], (1.45, 9), "caps", 65.5, anim="track", color=CHOC),
            t(["@soa.reformer · lien en bio"], (1.7, 9), "caps", 88, anim="fade", color=CAN)]},
    ]}


def e20261107_2():
    """Tendance TikTok « Money can't buy happiness, but… » (Pepper Agency, 02/11/2026) adaptée en français :
    « l'argent ne fait pas le bonheur… mais ». Montage de petits bonheurs du studio. Style classe, 1 effet signature :
    étiquette 36 € qui tombe et se balance sur le carton final."""
    GC = "saturate(.82) sepia(.2) contrast(1.06) brightness(.94)"

    def v(clip, st, zoom=(1.04, 1.12), speed=1.0, grade=GC, **kw):
        d = {"type": "video", "clip": clip, "start": st, "zoom": list(zoom), "grade": grade, "speed": speed, "extra": 0.9, "ease": "inout"}
        d.update(kw); return d

    def t(lines, at, style, y, anim="mask", **kw):
        d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim, "align": "left", "x": 8.9,
             "dur": 0.7, "ease": "inout", "stagger": 0.1}
        d.update(kw); return d

    TOPV = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.86), rgba(42,28,22,.5) 30%, rgba(42,28,22,.25) 50%, rgba(42,28,22,.2))"}
    BOTV = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.2), rgba(42,28,22,.3) 50%, rgba(42,28,22,.85))"}
    GR = {"type": "grain", "opacity": .07}

    return {"scenes": [
        # 1. accroche : le proverbe, en haut (la personne est petite, au centre du plan large)
        {"dur": 2.0, "in": "cut", "bpm": 120, "layers": [
            v("IMG_3764", 1.0, (1.0, 1.08)), TOPV,
            t(["l'argent ne fait pas"], (0.0, 9), "edito", 11, color=CREME, dur=0.6),
            t(["*le~bonheur…*"], (0.1, 9), "edito", 17.5, color=CAR, dur=0.6), GR]},
        # 2. arrivée au studio : texte en bas (visages en haut du plan)
        {"dur": 1.8, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_4610", 0.2, (1.02, 1.1)), BOTV,
            t(["mais arriver"], (0.15, 9), "edito", 78, color=CREME),
            t(["*à~ton~cours,*"], (0.3, 9), "edito", 84.5, color=CAR), GR]},
        # 3. le fou rire sur le reformer : texte en haut, le visage reste au centre
        {"dur": 1.8, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_6805", 4.0, (1.0, 1.06)), TOPV,
            t(["les fous rires"], (0.15, 9), "edito", 9, color=CREME),
            t(["*sur~le~reformer,*"], (0.3, 9), "edito", 15.5, color=CAR), GR]},
        # 4. le matcha d'après
        {"dur": 1.8, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_9300", 1.2, (1.04, 1.12)), TOPV,
            t(["le matcha"], (0.2, 9), "edito", 9, color=CREME),
            t(["*d'après…*"], (0.35, 9), "edito", 15.5, color=CAR), GR]},
        # 5. les rires sur le canapé : texte en bas (visages au milieu)
        {"dur": 1.9, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_3342", 4.5, (1.0, 1.06)), BOTV,
            t(["ça y ressemble"], (0.15, 9), "edito", 80, color=CREME),
            t(["*beaucoup.*"], (0.3, 9), "edito", 86.5, color=CAR), GR]},
        # 6. fin cannelle : l'étiquette 36 € tombe et se balance
        {"dur": 2.7, "in": "dissolve", "dissolve": 0.6, "out": "fadeblack", "layers": [
            {"type": "color", "color": CAN}, {"type": "grain", "opacity": .12},
            t(["le bonheur,"], (0.1, 9), "edito", 12, color=CREME),
            t(["*ça~se~teste.*"], (0.25, 9), "edito", 18.5, color=CAR),
            {"type": "pricetag", "x": 200, "y": 720, "at": 0.6, "scale": 1.6, "kicker": "pack découverte", "value": "36 €", "sub": "1 coachée + 1 digitale"},
            t(["coaché · digital · hybride"], (1.2, 9), "caps", 74, anim="track", color=CREME),
            t(["Pilates reformer à La Varenne"], (1.35, 9), "caps", 78, anim="track", color=CAR),
            t(["@soa.reformer · lien en bio"], (1.6, 9), "caps", 88, anim="fade", color=CREME)]},
    ]}


def _kit():
    GC = "saturate(.82) sepia(.2) contrast(1.06) brightness(.94)"

    def v(clip, st, zoom=(1.04, 1.12), speed=1.0, grade=GC, **kw):
        d = {"type": "video", "clip": clip, "start": st, "zoom": list(zoom), "grade": grade, "speed": speed, "extra": 0.9, "ease": "inout"}
        d.update(kw); return d

    def t(lines, at, style, y, anim="mask", **kw):
        d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim, "align": "left", "x": 8.9,
             "dur": 0.8, "ease": "inout", "stagger": 0.1}
        d.update(kw); return d
    return GC, v, t


TOPV = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.86), rgba(42,28,22,.5) 30%, rgba(42,28,22,.25) 50%, rgba(42,28,22,.2))"}
BOTV = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.2), rgba(42,28,22,.3) 50%, rgba(42,28,22,.85))"}
GR = {"type": "grain", "opacity": .07}


def fin_creme(l1, l2, t):
    return {"dur": 2.8, "in": "dissolve", "dissolve": 0.7, "out": "fadeblack", "layers": [
        {"type": "color", "color": CREME}, {"type": "grain", "opacity": .1},
        t(["SOA"], (0.3, 9), "logo", 18, anim="track", color=CHOC),
        t(["coaché · digital · hybride"], (0.45, 9), "caps", 36, anim="track", color=CAN),
        t([l1], (0.6, 9), "edito", 44, color=CHOC),
        t([l2], (0.85, 9), "edito", 50.5, color=CAN),
        {"type": "rule", "x": 96, "y": 1110, "w": 300, "at": 1.2, "color": CAN},
        t(["pack découverte"], (1.3, 9), "caps", 62, anim="track", color=CHOC),
        t(["1 coachée + 1 digitale · 36 €"], (1.45, 9), "caps", 65.5, anim="track", color=CHOC),
        t(["@soa.reformer · lien en bio"], (1.7, 9), "caps", 88, anim="fade", color=CAN)]}


def e20261108_1():
    """Tendance « Reasons why you don't need to… » (Pepper Agency, 02/11/2026) : la blague est dans le texte,
    format liste. Adaptation SOA pour les débutant·es intimidé·es : « tu n'as pas besoin d'être souple ».
    Style classe ; 1 effet signature : carnet (fond rayé + vidéos encadrées + notes épinglées)."""
    GC, v, t = _kit()
    CB = "14px solid #F3EADC"
    return {"scenes": [
        # 1. accroche : texte en haut, les membres sont allongé·es dans la moitié basse
        {"dur": 2.2, "in": "fade", "bpm": 120, "layers": [
            v("IMG_1152", 0.3, (1.0, 1.08)), TOPV,
            t(["les raisons pour lesquelles"], (0.0, 9), "caps", 9, anim="track", color=CAR),
            t(["tu n'as pas besoin"], (0.05, 9), "edito", 13, color=CREME),
            t(["*d'être~souple.*"], (0.2, 9), "edito", 19.5, color=CAR), GR]},
        # 2. carnet : raisons 1 et 2
        {"dur": 3.2, "in": "dissolve", "dissolve": 0.6, "layers": [
            {"type": "stripes"},
            {"type": "card", "clip": "IMG_9322", "start": 0.2, "box": [70, 300, 470, 660], "at": 0.1, "tilt": -5, "tiltEnd": -3, "grade": GC, "border": CB},
            {"type": "note", "x": 560, "y": 420, "w": 470, "at": 0.4, "rot": 4, "kicker": "raison n°1", "text": "les ressorts s'adaptent à toi."},
            {"type": "card", "clip": "IMG_4378", "start": 3.5, "box": [560, 1080, 450, 640], "at": 1.0, "tilt": 6, "tiltEnd": 3, "grade": GC, "border": CB},
            {"type": "note", "x": 70, "y": 1180, "w": 470, "at": 1.3, "rot": -4, "kicker": "raison n°2", "text": "un coach te corrige. 7 places max."},
            {"type": "grain", "opacity": .1}]},
        # 3. carnet : raison 3
        {"dur": 2.4, "in": "dissolve", "dissolve": 0.5, "layers": [
            {"type": "stripes"},
            {"type": "card", "clip": "IMG_6812", "start": 2.0, "box": [90, 260, 560, 800], "at": 0.1, "tilt": -4, "tiltEnd": -2, "grade": GC, "border": CB},
            {"type": "note", "x": 440, "y": 1160, "w": 520, "at": 0.45, "rot": 3, "kicker": "raison n°3", "text": "tout le monde a commencé un jour."},
            {"type": "grain", "opacity": .1}]},
        fin_creme("pas souple ?", "*viens~quand~même.*", t),
    ]}


def e20261108_2():
    """Tendance « tiny text » (Pepper Agency, 02/11/2026) : de minuscules textes qu'il faut mettre en pause pour lire.
    Style classe ; 2 effets signature : mot géant DERRIÈRE la personne (« pause. ») + le petit texte caché."""
    GC, v, t = _kit()
    Z1 = (1.0, 1.06)

    def tiny(s, at, y, color=CREME):
        return t([s], (at, 9), "small", y, anim="fade", color=color, size=24, dur=0.4)

    return {"scenes": [
        # 1. accroche : « pause. » géant derrière la membre jambes en l'air (visage bas, rien dessus)
        {"dur": 2.6, "in": "fade", "bpm": 120, "layers": [
            v("B63B1107", 1.0, Z1), {"type": "dim", "color": "rgba(42,28,22,.25)"}, TOPV,
            t(["lis le petit texte."], (0.0, 9), "edito", 10, color=CREME, size=100),
            t(["pause."], (0.2, 9), "giant", 47, color=CREME, size=300, dur=1.0),
            {"type": "cutout", "clip": "B63B1107", "start": 1.0, "zoom": list(Z1), "ease": "inout", "grade": GC, "extra": 0.9},
            tiny("bravo, tu as mis pause. ton corps aussi aimerait bien.", 0.6, 16), GR]},
        # 2. cours coaché : texte en haut, au-dessus des têtes
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_3300", 2.0, (1.02, 1.1)), TOPV,
            t(["en coaché,"], (0.1, 9), "edito", 8, color=CREME),
            t(["*7~places~max.*"], (0.25, 9), "edito", 14.5, color=CAR),
            tiny("(7 reformers, 1 coach, et personne ne te juge.)", 0.5, 21.5), GR]},
        # 3. séance digitale : le doigt lance la séance
        {"dur": 2.0, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_6650", 4.5, (1.02, 1.1)), TOPV,
            t(["en digital,"], (0.2, 9), "edito", 8, color=CREME),
            t(["*à~ton~heure.*"], (0.35, 9), "edito", 14.5, color=CAR),
            tiny("(7j/7, de 7h à 22h30. oui, même le dimanche soir.)", 0.6, 21.5), GR]},
        # 4. le matcha fouetté
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_9450", 5.0, (1.06, 1.0)), TOPV,
            t(["et après…"], (0.1, 9), "edito", 8, color=CREME),
            t(["*le~matcha.*"], (0.25, 9), "edito", 14.5, color=CAR),
            tiny("(on ne te force pas. mais presque.)", 0.5, 21.5), GR]},
        fin_creme("tu as tout lu ?", "*tu~mérites~ça.*", t),
    ]}


def e20261109_2():
    """Tendance « hook à l'écran, liste complète en légende » (tryvolume.app, santé & bien-être, mesuré le 08/11/2026) :
    une accroche courte sur du b-roll, 3 points à l'écran, la liste entière dans la légende TikTok.
    « avant ton premier cours de Pilates… ». Style classe ; 1 effet signature : compteur serif (1 → 2 → 3).
    Texte et chiffres dans le haut de l'image (plafond), les visages sont dans la moitié basse."""
    GC, v, t = _kit()

    def num(a, b):
        return {"type": "counter", "from": a, "to": b, "at": 0.1, "dur": 0.7, "style": "numserif", "x": 8.9, "y": 15,
                "align": "left", "color": CAR}

    def kick(s):
        return t([s], (0.15, 9), "caps", 27.5, anim="track", color=CREME)

    return {"scenes": [
        # 1. accroche : plan large du cours, texte en haut (plafond)
        {"dur": 2.4, "in": "fade", "bpm": 120, "layers": [
            v("IMG_3754", 2.5, (1.0, 1.08)), TOPV,
            t(["avant ton premier"], (0.0, 9), "edito", 9, color=CREME),
            t(["cours de *Pilates…*"], (0.12, 9), "edito", 15.5, color=CAR),
            t(["(la liste complète est en légende)"], (0.6, 9), "small", 22, anim="fade", color=CREME), GR]},
        # 2. n°1 : la coach corrige
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_4126", 7.0, (1.02, 1.1)), TOPV,
            num(0, 1), kick("ce que personne ne te dit"),
            t(["7 places max :"], (0.3, 9), "edito", 32, color=CREME),
            t(["*le~coach~te~voit.*"], (0.45, 9), "edito", 38.5, color=CAR), GR]},
        # 3. n°2 : une membre seule sur son reformer
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_3962", 1.5, (1.04, 1.12)), {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.9), rgba(42,28,22,.72) 42%, rgba(42,28,22,.3) 60%, rgba(42,28,22,.2))"},
            num(1, 2), kick("ce que personne ne te dit"),
            t(["tu peux venir"], (0.3, 9), "edito", 32, color=CREME),
            t(["*seul·e.*"], (0.45, 9), "edito", 38.5, color=CAR), GR]},
        # 4. n°3 : le matcha d'après (texte en bas : le haut est occupé par le pichet)
        {"dur": 2.0, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_9451", 3.5, (1.04, 1.1)), BOTV,
            {"type": "counter", "from": 2, "to": 3, "at": 0.1, "dur": 0.7, "style": "numserif", "x": 8.9, "y": 62,
             "align": "left", "color": CAR},
            t(["le matcha d'après :"], (0.3, 9), "edito", 79, color=CREME),
            t(["*sacré.*"], (0.45, 9), "edito", 85.5, color=CAR), GR]},
        fin_creme("ton premier cours ?", "*on~t'attend.*", t),
    ]}


def e20261110_2():
    """Tendance « entrée au ralenti » (son « Pray For Me », New Engen, mise à jour du 05/11/2026) : des entrées filmées
    au ralenti, énergie « personnage principal ». Adaptation SOA : « ton entrée au cours de Pilates » (rue → QR code →
    porte → studio → reformer). Style classe ; 2 effets signature : ralenti (speed 0.5–0.6) + texte qui tourne autour
    de l'offre 36 € sur le carton final. Textes hors des visages : ciel / plafond en haut, jambes en bas."""
    GC, v, t = _kit()
    RING = "coaché · digital · hybride · coaché · digital · hybride · "
    return {"scenes": [
        # 1. accroche : arrivée dans la rue au ralenti, texte dans le ciel (visages au milieu de l'image)
        {"dur": 2.2, "in": "fade", "bpm": 120, "layers": [
            v("IMG_2206", 6.0, (1.0, 1.06), speed=0.5), TOPV,
            t(["ton entrée au cours"], (0.0, 9), "edito", 7, color=CREME),
            t(["de *Pilates~:*"], (0.12, 9), "edito", 13.5, color=CAR),
            t(["(version ralenti)"], (0.6, 9), "caps", 19, anim="track", color=CREME, size=32), GR]},
        # 2. le QR code à la porte : visage en haut du plan, texte en bas
        {"dur": 1.6, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_4612", 1.3, (1.02, 1.08), speed=0.6), BOTV,
            t(["le QR code,"], (0.15, 9), "edito", 79, color=CREME),
            t(["*scanné.*"], (0.3, 9), "edito", 85.5, color=CAR), GR]},
        # 3. la porte poussée (de dos), texte en bas
        {"dur": 1.6, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_4614", 0.2, (1.0, 1.06), speed=0.6), BOTV,
            t(["la porte,"], (0.15, 9), "edito", 79, color=CREME),
            t(["*poussée.*"], (0.3, 9), "edito", 85.5, color=CAR), GR]},
        # 4. le coach accueille : texte au plafond
        {"dur": 1.8, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_4618", 0.8, (1.02, 1.08), speed=0.6), TOPV,
            t(["le coach,"], (0.2, 9), "edito", 8, color=CREME),
            t(["*déjà~là.*"], (0.35, 9), "edito", 14.5, color=CAR), GR]},
        # 5. le cours s'installe : texte au plafond
        {"dur": 1.8, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_3934", 9.5, (1.0, 1.06), speed=0.6), TOPV,
            t(["et là…"], (0.15, 9), "edito", 8, color=CREME),
            t(["*ton~moment.*"], (0.3, 9), "edito", 14.5, color=CAR), GR]},
        # 6. fin crème : le texte tourne autour de l'offre
        {"dur": 2.8, "in": "dissolve", "dissolve": 0.6, "out": "fadeblack", "layers": [
            {"type": "color", "color": CREME}, {"type": "grain", "opacity": .1},
            t(["SOA"], (0.2, 9), "logo", 11, anim="track", color=CHOC),
            t(["ton entrée,"], (0.35, 9), "edito", 21, color=CHOC),
            t(["*on~t'attend.*"], (0.55, 9), "edito", 27.5, color=CAN),
            {"type": "circletext", "cx": 540, "cy": 1060, "r": 270, "text": RING, "speed": 22, "size": 40, "at": 0.6, "color": CAN},
            t(["36 €"], (0.8, 9), "numserif", 55, anim="fade", color=CHOC, align="center", x=50, size=200),
            t(["pack découverte · 1 coachée + 1 digitale"], (1.2, 9), "caps", 76, anim="track", color=CHOC),
            t(["Pilates reformer à La Varenne"], (1.35, 9), "caps", 80, anim="track", color=CAN),
            t(["@soa.reformer · lien en bio"], (1.6, 9), "caps", 88, anim="fade", color=CAN)]},
    ]}


def e20261111_1():
    """Tendance « ✕ puis ✓ sans un mot » (Volume, sport/fitness, mesuré le 09/11/2026 : la mauvaise option barrée,
    la bonne cochée, de courts libellés, aucune parole). Adaptation SOA : « ce soir, ✕ ou ✓ ? » (le canapé vs la séance).
    Style classe ; 1 effet signature : interrupteur iOS « mode Pilates » qui s'allume. Textes en haut, loin des visages."""
    GC, v, t = _kit()

    def mark(sym, col, y):
        return t([sym], (0.05, 9), "edito", y, anim="fade", color=col, size=130, dur=0.4)

    return {"scenes": [
        # 1. accroche : le studio aux bougies le soir (aucun visage)
        {"dur": 2.0, "in": "fade", "bpm": 120, "layers": [
            v("IMG_0867", 1.0, (1.0, 1.08)), TOPV,
            t(["la version sans un mot"], (0.0, 9), "caps", 9, anim="track", color=CAR),
            t(["ce soir,"], (0.05, 9), "edito", 13, color=CREME),
            t(["*✕~ou~✓~?*"], (0.2, 9), "edito", 19.5, color=CAR), GR]},
        # 2. ✕ : le canapé dans la pénombre
        {"dur": 1.6, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_0708", 0.0, (1.06, 1.12)), TOPV,
            mark("✕", CAR, 8),
            t(["le canapé."], (0.15, 9), "edito", 16, color=CREME),
            t(["*(encore.)*"], (0.35, 9), "edito", 22.5, color=CAR), GR]},
        # 3. ✓ : le QR code de réservation sur le téléphone + interrupteur « mode Pilates »
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_6625", 3.6, (1.02, 1.08)), TOPV,
            mark("✓", CREME, 8),
            t(["tu réserves."], (0.15, 9), "edito", 16, color=CREME),
            {"type": "toggle", "x": 96, "y": 470, "at": 0.9, "inAt": 0.4, "label": "mode Pilates"}, GR]},
        # 4. ✓ : la séance du soir aux bougies
        {"dur": 1.8, "in": "window", "windowDur": 0.6, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_0704", 1.5, (1.0, 1.06), grade="saturate(.85) sepia(.22) contrast(1.08) brightness(1.15)"), TOPV,
            mark("✓", CREME, 8),
            t(["ton moment"], (0.15, 9), "edito", 16, color=CREME),
            t(["*à~toi.*"], (0.3, 9), "edito", 22.5, color=CAR), GR]},
        # 5. ✓ : le matcha fouetté
        {"dur": 1.7, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_9297", 1.0, (1.04, 1.1)), TOPV,
            mark("✓", CREME, 8),
            t(["le matcha"], (0.15, 9), "edito", 16, color=CREME),
            t(["*d'après.*"], (0.3, 9), "edito", 22.5, color=CAR), GR]},
        fin_creme("ce soir, coche", "*la~bonne~case.*", t),
    ]}


def e20261111_2():
    """Tendance « long texte empilé sur un clip court » (Volume, mesuré le 09/11/2026 : « les phrases que… »,
    texte qui s'accumule sur quelques secondes de vidéo). Adaptation SOA : « ce que tu entends à chaque cours de Pilates ».
    Style classe ; 1 effet signature : mot rempli de vidéo (« Pilates ») sur aplat cannelle. Les phrases s'empilent en haut
    de l'image ; plans POV (aucun visage) puis plan large où les membres sont dans la moitié basse."""
    GC, v, t = _kit()
    PH = [(["« on inspire… »"], CREME), (["« les épaules loin des oreilles. »"], CREME), (["« on rentre le nombril. »"], CREME),
          (["« ça tremble ? c'est normal. »"], CREME), (["*«~et…~on~relâche.~»*"], CAR)]
    Y0, DY = 8, 6.4

    def stack(upto, first_new):
        L = []
        for i, (lines, col) in enumerate(PH[:upto]):
            at = (0.1 + 0.75 * (i - first_new)) if i >= first_new else -5
            L.append(t(lines, (at, 99), "edito", Y0 + DY * i, color=col, size=64, out=False, dur=0.5))
        return L

    DEEP = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.92), rgba(42,28,22,.75) 36%, rgba(42,28,22,.25) 50%, rgba(42,28,22,.15))"}

    def sc(clip, st, upto, first_new, dur, zoom=(1.02, 1.1), tin="cut"):
        return {"dur": dur, "in": tin, "out": "cut", "layers": [v(clip, st, zoom), DEEP] + stack(upto, first_new) + [GR]}

    return {"scenes": [
        # 1. accroche : « Pilates » rempli de vidéo sur aplat cannelle
        {"dur": 2.2, "in": "fade", "bpm": 120, "layers": [
            {"type": "color", "color": CAN}, {"type": "grain", "opacity": .1},
            t(["ce que tu entends"], (0.0, 9), "edito", 22, color=CREME),
            t(["à *chaque~cours~de*"], (0.12, 9), "edito", 28.5, color=CAR),
            {"type": "cliptext", "clip": "IMG_2513", "start": 1.0, "lines": ["Pilates"], "size": 270, "y": 38, "at": 0.25},
            t(["(on a tout noté)"], (0.7, 9), "caps", 62, anim="track", color=CREME, size=30)]},
        sc("IMG_3002", 0.3, 2, 0, 2.2),
        sc("IMG_7151", 0.5, 4, 2, 2.2),
        sc("IMG_2519", 0.5, 5, 4, 1.8, zoom=(1.0, 1.06)),
        fin_creme("tu les entends ?", "*viens~les~vivre.*", t),
    ]}


def e20261112_1():
    """Tendance TikTok « go go go » (Ramdam, 10/11/2026) : la voix intérieure « go go go » sur quelqu'un qui avance
    lentement. Adaptation SOA : en Pilates on va lentement… mais ton cerveau, lui : go go go. Style classe ;
    1 effet signature : mot géant DERRIÈRE la personne (« go go go » derrière les jambes, visage en bas, rien dessus)."""
    GC, v, t = _kit()
    Z1 = (1.0, 1.06)
    return {"scenes": [
        # 1. accroche : « go go go » géant derrière les jambes ; la tête est en bas à gauche, texte en haut
        {"dur": 2.6, "in": "fade", "bpm": 120, "layers": [
            v("IMG_9422", 0.0, Z1), {"type": "dim", "color": "rgba(42,28,22,.22)"}, TOPV,
            t(["ton cerveau en *Pilates~:*"], (0.0, 9), "edito", 9, color=CREME, size=96),
            t(["go go"], (0.2, 9), "giant", 33, color=CREME, size=300, dur=0.9),
            t(["go."], (0.45, 9), "giant", 47, color=CAR, size=300, dur=0.9),
            {"type": "cutout", "clip": "IMG_9422", "start": 0.0, "zoom": list(Z1), "ease": "inout", "grade": GC, "extra": 0.9},
            GR]},
        # 2. la coach, assise à côté : « lentement. » (texte au plafond, visages au milieu)
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_2183", 3.0, (1.02, 1.1)), TOPV,
            t(["la coach :"], (0.1, 9), "edito", 8, color=CREME),
            t(["*«~lentement.~»*"], (0.25, 9), "edito", 14.5, color=CAR), GR]},
        # 3. la coach accompagne la jambe : le cerveau insiste
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_6470", 1.0, (1.02, 1.1)), TOPV,
            t(["ton cerveau :"], (0.1, 9), "edito", 8, color=CREME),
            t(["*go~go~go~go.*"], (0.25, 9), "edito", 14.5, color=CAR), GR]},
        # 4. le cours au ralenti
        {"dur": 2.2, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_6747", 0.5, (1.0, 1.06), speed=0.6), TOPV,
            t(["spoiler :"], (0.2, 9), "edito", 8, color=CREME),
            t(["*lentement,~c'est~plus~dur.*"], (0.35, 9), "edito", 14.5, color=CAR, size=96), GR]},
        fin_creme("ton cerveau : go.", "*ton~corps~:~merci.*", t),
    ]}


def e20261112_2():
    """Tendance TikTok « No, that doesn't make any sense » (Ramdam, 03/11/2026) : une situation contradictoire à l'écran,
    réponse « ça n'a aucun sens ». Adaptation SOA, accroche de saison : « je commence en janvier »… alors que le studio
    est ouvert ce soir. Style classe ; 1 effet signature : horloge (18:30 → 22:30). Textes au plafond, loin des visages."""
    GC, v, t = _kit()
    return {"scenes": [
        # 1. accroche : le studio aux bougies (aucun visage)
        {"dur": 2.4, "in": "fade", "bpm": 120, "layers": [
            v("IMG_0830", 1.0, (1.0, 1.08)), TOPV,
            t(["tout le monde en novembre :"], (0.0, 9), "caps", 9, anim="track", color=CAR),
            t(["« je commence"], (0.05, 9), "edito", 13, color=CREME),
            t(["*en~janvier.~»*"], (0.2, 9), "edito", 19.5, color=CAR), GR]},
        # 2. le cours bat son plein
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_3298", 0.5, (1.02, 1.1)), TOPV,
            t(["non, attends…"], (0.1, 9), "edito", 8, color=CREME),
            t(["*ça~n'a~aucun~sens.*"], (0.25, 9), "edito", 14.5, color=CAR), GR]},
        # 3. le soir, aux bougies : horloge jusqu'à 22:30
        {"dur": 2.4, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_0851", 0.5, (1.02, 1.1), grade="saturate(.85) sepia(.22) contrast(1.06) brightness(1.15)"), TOPV,
            {"type": "clock", "x": 96, "y": 230, "at": 0.15, "from": 1110, "to": 1350, "dur": 1.4, "label": "ouvert 7j/7"},
            t(["le studio est ouvert"], (0.5, 9), "edito", 27, color=CREME, size=96),
            t(["*ce~soir.*"], (0.7, 9), "edito", 32.5, color=CAR, size=96), GR]},
        # 4. le cours : d'ici janvier
        {"dur": 2.0, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_4118", 0.3, (1.0, 1.06)), TOPV,
            t(["d'ici janvier :"], (0.2, 9), "edito", 8, color=CREME),
            t(["*7~semaines~de~rythme.*"], (0.35, 9), "edito", 14.5, color=CAR, size=92), GR]},
        fin_creme("c'est maintenant qu'on", "*construit~un~rythme.*", t),
    ]}


def e20261113_1():
    """Tendance TikTok « Oh no, I'm so cringe » (Ramdam, 10/11/2026) : on avoue en texte une vieille croyance ou une
    ancienne phase un peu gênante. Adaptation SOA : « oh non… j'ai vraiment cru que le Pilates, c'était s'étirer ».
    Style classe ; 1 effet signature : carnet (fond rayé + vidéo encadrée + note épinglée « mon carnet, avant SOA »).
    Textes au plafond ou en bas, jamais sur un visage."""
    GC, v, t = _kit()
    CB = "14px solid #F3EADC"
    return {"scenes": [
        # 1. accroche + carnet : l'ancienne croyance, notée comme dans un journal
        {"dur": 3.0, "in": "fade", "bpm": 120, "layers": [
            {"type": "stripes"},
            t(["oh non…"], (0.0, 9), "edito", 8, color=CREME, size=110),
            t(["*j'ai~vraiment~cru~ça.*"], (0.15, 9), "edito", 14.5, color=CAR, size=96),
            {"type": "card", "clip": "IMG_9319", "start": 3.5, "box": [70, 560, 470, 700], "at": 0.3, "tilt": -5, "tiltEnd": -3, "grade": GC, "border": CB},
            {"type": "note", "x": 560, "y": 760, "w": 460, "at": 0.7, "rot": 4, "kicker": "mon carnet, avant SOA", "text": "le Pilates ? des étirements tranquilles."},
            {"type": "grain", "opacity": .1}]},
        # 2. l'effort, en vrai (visage au milieu : texte au plafond)
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.5, "layers": [
            v("IMG_6788", 4.0, (1.0, 1.06)), TOPV,
            t(["spoiler :"], (0.1, 9), "edito", 8, color=CREME),
            t(["*ça~travaille.~beaucoup.*"], (0.25, 9), "edito", 14.5, color=CAR, size=96), GR]},
        # 3. la planche sur la barre (visages au milieu : texte au plafond)
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_6726", 3.0, (1.0, 1.06)), TOPV,
            t(["la planche sur le Reformer :"], (0.1, 9), "caps", 8, anim="track", color=CAR),
            t(["*«~tranquille~»,~disait-on.*"], (0.2, 9), "edito", 12, color=CREME, size=96), GR]},
        # 4. fin de cours, les mains sur le visage (texte en bas)
        {"dur": 2.0, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_6794", 1.5, (1.0, 1.05)), BOTV,
            t(["moi, en fin de cours :"], (0.2, 9), "edito", 78, color=CREME, size=92),
            t(["*plus~jamais~«~tranquille~».*"], (0.35, 9), "edito", 84.5, color=CAR, size=92), GR]},
        fin_creme("« tranquille » ?", "*viens~vérifier.*", t),
    ]}


def e20261113_2():
    """Tendance « I just wanna… » (son « Housewife » de Tate McRae ; Later 06/11/2026, NewEngen 05/11/2026 ;
    Banque d'idées SOA-20261112-INES-03) : « je veux juste… » sur des plans lifestyle. Adaptation SOA : un créneau
    à 21h, un coach qui corrige, 7 places, un matcha. Style classe ; 1 effet signature : étiquette 36 € qui tombe
    sur le carton final. Textes au plafond, loin des visages."""
    GC, v, t = _kit()
    return {"scenes": [
        # 1. accroche : le studio du soir aux bougies (aucun visage)
        {"dur": 2.4, "in": "fade", "bpm": 120, "layers": [
            v("IMG_0867", 2.0, (1.0, 1.08)), TOPV,
            t(["je veux juste…"], (0.0, 9), "edito", 9, color=CREME, size=110),
            t(["*un~créneau~à~21h.*"], (0.3, 9), "edito", 15.5, color=CAR), GR]},
        # 2. la coach corrige (visages au milieu)
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_1043", 0.2, (1.0, 1.06)), TOPV,
            t(["je veux juste…"], (0.0, 9), "caps", 8, anim="track", color=CAR),
            t(["*quelqu'un~qui~me~corrige.*"], (0.15, 9), "edito", 11.5, color=CREME, size=92), GR]},
        # 3. le cours : 7 places
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_7250", 1.0, (1.0, 1.05)), TOPV,
            t(["je veux juste…"], (0.0, 9), "caps", 6, anim="track", color=CAR),
            t(["*7~places,~pas~70.*"], (0.15, 9), "edito", 9.5, color=CREME, size=92), GR]},
        # 4. le matcha
        {"dur": 2.0, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_9449", 0.3, (1.04, 1.12)), TOPV,
            t(["et…"], (0.15, 9), "edito", 9, color=CREME),
            t(["*un~matcha.*"], (0.3, 9), "edito", 15.5, color=CAR), GR]},
        # 5. fin cannelle : l'étiquette 36 € tombe et se balance
        {"dur": 2.8, "in": "dissolve", "dissolve": 0.6, "out": "fadeblack", "layers": [
            {"type": "color", "color": CAN}, {"type": "grain", "opacity": .12},
            t(["c'est pas"], (0.1, 9), "edito", 12, color=CREME),
            t(["*trop~demander.*"], (0.25, 9), "edito", 18.5, color=CAR),
            {"type": "pricetag", "x": 200, "y": 720, "at": 0.6, "scale": 1.6, "kicker": "pack découverte", "value": "36 €", "sub": "1 coachée + 1 digitale"},
            t(["coaché · digital · hybride"], (1.2, 9), "caps", 74, anim="track", color=CREME),
            t(["Pilates Reformer · La Varenne"], (1.35, 9), "caps", 78, anim="track", color=CAR),
            t(["@soa.reformer · lien en bio"], (1.6, 9), "caps", 88, anim="fade", color=CREME)]},
    ]}


def e20261114_1():
    """Tendance « Answer in one word » (New Engen, mise à jour du 05/11/2026 ; Banque d'idées SOA-20261105-INES-04) :
    une question, réponse obligatoire en un seul mot. Adaptation SOA (samedi = « le rituel d'après ») :
    « ta séance de Pilates en un mot ? » → lentement. tremblements. fierté. … matcha.
    Style classe ; 1 effet signature : texte qui tourne autour du verre de matcha. Textes au plafond, loin des visages."""
    GC, v, t = _kit()
    RING = "le rituel d'après · le rituel d'après · le rituel d'après · "

    def mot(w):
        return t([f"*«~{w}~»*"], (0.1, 9), "edito", 10, color=CREME, size=150)

    def kick(s):
        return t([s], (0.0, 9), "caps", 6, anim="track", color=CAR)

    return {"scenes": [
        # 1. accroche : le studio en lumière du jour (personnes petites, au milieu de l'image)
        {"dur": 2.0, "in": "fade", "bpm": 120, "layers": [
            v("IMG_0897", 0.3, (1.0, 1.08)), TOPV,
            t(["ta séance de Pilates"], (0.0, 9), "edito", 8, color=CREME),
            t(["*en~un~mot~?*"], (0.12, 9), "edito", 14.5, color=CAR, size=130),
            t(["(un seul. pas deux.)"], (0.6, 9), "caps", 21, anim="track", color=CREME, size=30), GR]},
        # 2. la coach ajuste (têtes vers 30 % : texte au-dessus)
        {"dur": 1.6, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_4218", 2.0, (1.0, 1.06)), TOPV, kick("réponse n°1"), mot("lentement."), GR]},
        # 3. fentes synchronisées (visages au milieu)
        {"dur": 1.6, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_3069", 0.5, (1.0, 1.06)), TOPV, kick("réponse n°2"), mot("tremblements."), GR]},
        # 4. à genoux, bras dans les sangles (visages au milieu)
        {"dur": 1.6, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_2717", 0.5, (1.0, 1.06)), TOPV, kick("réponse n°3"), mot("fierté."), GR]},
        # 5. le matcha versé : le texte tourne autour du verre (aucun visage)
        {"dur": 2.4, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_9451", 9.6, (1.02, 1.06)), TOPV,
            kick("et après la séance :"),
            t(["*«~matcha.~»*"], (0.15, 9), "edito", 10, color=CREME, size=150),
            {"type": "circletext", "cx": 540, "cy": 1330, "r": 330, "text": RING, "speed": 20, "size": 36, "at": 0.4, "color": CREME},
            GR]},
        fin_creme("et toi, en un mot ?", "*dis-le~en~commentaire.*", t),
    ]}


def e20261114_2():
    """Movember (tout novembre ; SocialPilot 30/10/2026) + Banque d'idées SOA-20261112-INES-04 « ton pote dit que le
    Pilates, c'est pas pour lui » : récit en 3 temps (minute 0 / 10 / 45), puis compteur des jours qui restent.
    Style classe ; 1 effet signature : compteur serif 30 → 16 (jours restants de novembre au 14/11).
    Textes au plafond ou en bas, jamais sur un visage."""
    GC, v, t = _kit()
    return {"scenes": [
        # 1. accroche : deux potes debout dans le studio (têtes vers 30 % : texte au-dessus)
        {"dur": 2.4, "in": "fade", "bpm": 120, "layers": [
            v("IMG_6778", 0.5, (1.0, 1.06)), TOPV,
            t(["movember"], (0.0, 9), "caps", 5.5, anim="track", color=CAR),
            t(["ton pote :"], (0.1, 9), "edito", 9.5, color=CREME, size=110),
            t(["*«~pas~pour~moi.~»*"], (0.3, 9), "edito", 16, color=CAR, size=120), GR]},
        # 2. minute 10 : allongés, l'effort (visages au milieu)
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_6782", 1.2, (1.0, 1.05)), TOPV,
            t(["minute 10 :"], (0.0, 9), "caps", 6, anim="track", color=CAR),
            t(["*«~ah.~d'accord.~»*"], (0.1, 9), "edito", 10, color=CREME, size=120), GR]},
        # 3. minute 45 : le poing levé (visage au milieu)
        {"dur": 2.0, "in": "dissolve", "dissolve": 0.4, "layers": [
            v("IMG_6800", 1.0, (1.0, 1.05)), TOPV,
            t(["minute 45 :"], (0.0, 9), "caps", 6, anim="track", color=CAR),
            t(["*«~on~revient~quand~?~»*"], (0.1, 9), "edito", 10, color=CREME, size=110), GR]},
        # 4. le groupe s'étire : compteur en bas (têtes en haut, jambes en bas)
        {"dur": 2.6, "in": "window", "windowDur": 0.7, "windowFrom": 24, "layers": [
            {"type": "color", "color": CREME},
            v("IMG_6826", 2.2, (1.02, 1.08)), BOTV,
            {"type": "counter", "from": 30, "to": 16, "at": 0.2, "dur": 1.2, "style": "numserif", "x": 8.9, "y": 66,
             "align": "left", "color": CAR},
            t(["jours de Movember"], (0.5, 9), "edito", 79, color=CREME, size=96),
            t(["*pour~l'emmener.*"], (0.65, 9), "edito", 85.5, color=CAR, size=110), GR]},
        fin_creme("ton binôme ?", "*on~vous~attend.*", t),
    ]}


if __name__ == "__main__":
    name = sys.argv[1]
    spec = globals()[name]()
    num = name.split("_")[-1]
    date = name[1:9]
    base = f"SOA-essai-{date}-{num}" if name[1:5].isdigit() else "SOA-" + name.replace("_", "-")
    if len(sys.argv) > 2 and sys.argv[2] == "still":
        still(spec, [float(x) for x in sys.argv[3].split(",")], os.path.join(OUT, f"_{name}.jpg"))
    else:
        render(spec, os.path.join(OUT, base + ".mp4"))
    print("ok")
