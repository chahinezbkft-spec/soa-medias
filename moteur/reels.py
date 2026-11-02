import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from engine import render, still

GRADE = "saturate(.95) contrast(1.04) sepia(.06)"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sortie")
os.makedirs(OUT, exist_ok=True)


def V(clip, start, zoom=(1.0, 1.08), pan=(0, 0, 0, 0), speed=1.0, crop=None, dim=.25):
    L = [{"type": "video", "clip": clip, "start": start, "zoom": list(zoom), "pan": list(pan), "speed": speed, "grade": GRADE}]
    if crop: L[0]["crop"] = crop
    if dim: L.append({"type": "dim", "color": f"rgba(22,17,14,{dim})"})
    return L


def T(lines, at=(0.1, 99), style="hook", y=50, anim="words", **kw):
    d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim}
    d.update(kw)
    return d


def outil():
    """Tendance « l'outil, le carburant, le travail » version SOA."""
    return {"scenes": [
        {"dur": 2.2, "in": "cut", "out": "zoom", "layers": V("IMG_9362", 0.6, (1.0, 1.15), crop="405:720:430:0", dim=.2) + [
            T(["l'outil."], (0.15, 9), "big", y=46, anim="slam", stagger=0),
            T(["SOA · version pilates"], (0.45, 9), "kicker", y=56, anim="fade")]},
        {"dur": 2.4, "in": "zoom", "out": "zoom", "layers": V("IMG_9451", 3.2, (1.05, 1.18), dim=.15) + [
            T(["le *carburant.*"], (0.2, 9), "big", y=30, anim="slam", stagger=0.12)]},
        {"dur": 2.6, "in": "zoom", "out": "zoom", "layers": V("IMG_3068", 1.0, (1.0, 1.1), dim=.2) + [
            T(["le *travail.*"], (0.2, 9), "big", y=22, anim="slam", stagger=0.12)]},
        {"dur": 2.4, "in": "zoom", "out": "cut", "layers": V("IMG_6812", 2.0, (1.08, 1.0), dim=.25) + [
            T(["et quelqu'un", "qui te *corrige.*"], (0.2, 9), "hook", y=78, anim="words")]},
        {"dur": 3.0, "in": "flash", "out": "fadeblack", "layers": V("IMG_9060", 2.0, (1.12, 1.0), dim=.35) + [
            T(["pilates reformer", "à *La~Varenne.*"], (0.35, 9), "hook", y=52, anim="words"),
            T(["1 coachée + 1 digitale · 36 €"], (0.9, 9), "pill", y=70, anim="pop", stagger=0.04)]},
    ]}


OFFER = "découvre les 2 mondes · 1 coachée + 1 digitale · 36 €"


def END(clip="IMG_9059", start=1.0, line2="à *La~Varenne.*", pill=None, dur=3.4):
    """Écran de fin : les 3 façons de pratiquer + l'offre découverte hybride."""
    L = V(clip, start, (1.12, 1.0), dim=.45) + [
        T(["coaché · digital · hybride"], (0.15, 9), "kicker", y=36, anim="fade"),
        T(["pilates reformer", line2], (0.3, 9), "hook", y=46, anim="words")]
    if pill and pill != OFFER:
        L.append(T([pill], (0.8, 9), "pill", y=62, anim="pop", stagger=0.03))
        L.append(T(["pack découverte : 1 coachée + 1 digitale · *36~€*"], (1.15, 9), "small", y=71, anim="fade"))
    else:
        L.append(T(["pack découverte"], (0.75, 9), "small", y=60, anim="fade"))
        L.append(T(["1 coachée + 1 digitale · 36 €"], (0.85, 9), "pill", y=66, anim="pop", stagger=0.03))
    L.append(T(["@soa.reformer · lien en bio"], (1.3, 9), "small", y=79, anim="fade"))
    return {"dur": dur, "in": "flash", "out": "fadeblack", "layers": L}


def lets():
    """Tendance « Let's… » : invitations ignorées, puis explosion pour le pilates."""
    cuts = [("IMG_2206", 8.3), ("IMG_4615", 0.8), ("IMG_3066", 0.3), ("IMG_6805", 2.8), ("IMG_9300", 2.5),
            ("b2_IMG_6829", 1.3), ("IMG_3342", 3.0), ("IMG_6801", 7.5)]
    sc = [{"dur": 5.6, "in": "cut", "out": "zoom", "layers": V("IMG_2206", 2.2, (1.0, 1.08), dim=.42) + [
        {"type": "bubble", "side": "left", "text": "on se fait un brunch dimanche ?", "y": 420, "at": 0.3},
        {"type": "bubble", "side": "right", "text": "bof.", "y": 600, "at": 1.1},
        {"type": "bubble", "side": "left", "text": "on va courir demain matin ?", "y": 760, "at": 1.9},
        {"type": "bubble", "side": "right", "text": "non.", "y": 940, "at": 2.6},
        {"type": "bubble", "side": "left", "text": "on teste le pilates reformer ce soir ?", "y": 1100, "at": 3.5}]},
          {"dur": 1.2, "in": "zoom", "out": "zoom", "layers": V("IMG_3342", 0.4, (1.05, 1.15), dim=.38) + [
              T(["OUI."], (0.0, 9), "big", y=50, anim="slam", stagger=0)]}]
    for k, (c, st) in enumerate(cuts):
        sc.append({"dur": 0.5, "in": "flash" if k % 3 == 0 else "zoom", "out": "cut", "layers": V(c, st, (1.15, 1.0), dim=.1)})
    sc.append(END())
    return {"scenes": sc}


def porte():
    """POV : première fois chez SOA."""
    return {"scenes": [
        {"dur": 3.6, "in": "cut", "out": "zoom", "layers": V("IMG_9122", 1.5, (1.0, 1.1), dim=.3) + [
            T(["POV"], (0.1, 9), "kicker", y=30, anim="fade"),
            T(["tu passes la porte", "de SOA pour la", "*première~fois.*"], (0.25, 9), "hook", y=40, anim="words")]},
        {"dur": 2.2, "in": "zoom", "out": "zoom", "layers": V("IMG_9059", 1.5, (1.1, 1.0), dim=.3) + [
            T(["on connaît", "ton *prénom.*"], (0.15, 9), "hook", y=24, anim="words")]},
        {"dur": 2.4, "in": "zoom", "out": "zoom", "layers": V("IMG_6725", 3.0, (1.0, 1.1), dim=.2) + [
            T(["on corrige", "ta *posture.*"], (0.15, 9), "hook", y=20, anim="words")]},
        {"dur": 2.2, "in": "zoom", "out": "zoom", "layers": V("IMG_3066", 0.0, (1.05, 1.12), dim=.2) + [
            T(["7 personnes.", "*pas~30.*"], (0.15, 9), "hook", y=20, anim="words")]},
        {"dur": 2.2, "in": "zoom", "out": "zoom", "layers": V("IMG_9300", 2.0, (1.0, 1.12), dim=.15) + [
            T(["un matcha", "*après.*"], (0.15, 9), "hook", y=22, anim="words")]},
        {"dur": 2.6, "in": "zoom", "out": "cut", "layers": V("IMG_6805", 2.0, (1.05, 1.0), dim=.2) + [
            T(["et l'envie", "de *revenir.*"], (0.2, 9), "hook", y=78, anim="words")]},
        END("IMG_0852", 2.5),
    ]}


def coachs():
    """Pédagogie : ce qu'un coach voit."""
    return {"scenes": [
        {"dur": 3.0, "in": "cut", "out": "zoom", "layers": V("IMG_6724", 2.0, (1.0, 1.12), dim=.3) + [
            T(["ce qu'un coach voit", "et que toi, *non.*"], (0.15, 9), "hook", y=22, anim="words")]},
        {"dur": 2.2, "in": "zoom", "out": "zoom", "layers": V("IMG_6725", 4.0, (1.05, 1.15), dim=.2) + [
            T(["ta hanche qui *s'ouvre.*"], (0.1, 9), "mid", y=82, anim="words")]},
        {"dur": 2.2, "in": "zoom", "out": "zoom", "layers": V("IMG_6710", 2.0, (1.05, 1.15), dim=.2) + [
            T(["ton épaule qui *monte.*"], (0.1, 9), "mid", y=82, anim="words")]},
        {"dur": 2.2, "in": "zoom", "out": "zoom", "layers": V("IMG_6472", 4.0, (1.05, 1.15), dim=.2) + [
            T(["ton bassin qui *bascule.*"], (0.1, 9), "mid", y=82, anim="words")]},
        {"dur": 2.8, "in": "zoom", "out": "cut", "layers": V("IMG_6752", 3.0, (1.0, 1.1), dim=.3) + [
            T(["c'est pour ça qu'on est", "*7~max.*"], (0.15, 9), "hook", y=22, anim="words")]},
        END(),
    ]}


def matcha():
    """ASMR : le rituel d'après-séance."""
    return {"scenes": [
        {"dur": 3.2, "in": "fade", "out": "cut", "layers": V("IMG_9297", 1.0, (1.0, 1.08), dim=.1) + [
            T(["le rituel", "*d'après-séance.*"], (0.4, 9), "hook", y=20, anim="words")]},
        {"dur": 3.0, "in": "flash", "out": "cut", "layers": V("IMG_9300", 1.0, (1.0, 1.1), dim=.05)},
        {"dur": 3.4, "in": "zoom", "out": "zoom", "layers": V("IMG_9451", 3.2, (1.05, 1.15), dim=.05)},
        {"dur": 2.8, "in": "zoom", "out": "cut", "layers": V("IMG_3342", 4.0, (1.0, 1.08), dim=.15) + [
            T(["à boire", "*ensemble.*"], (0.2, 9), "hook", y=22, anim="words")]},
        END(),
    ]}


def SPLIT(top, tst, bot, bst, ytxt, btxt, dur=4.2):
    return {"dur": dur, "in": "flash", "out": "cut", "layers": [
        {"type": "video", "clip": top, "start": tst, "zoom": [1.0, 1.08], "grade": GRADE, "box": [0, 0, 1080, 952]},
        {"type": "video", "clip": bot, "start": bst, "zoom": [1.0, 1.08], "grade": GRADE, "box": [0, 968, 1080, 952]},
        {"type": "dim", "color": "rgba(22,17,14,.18)"},
        {"type": "bar", "y": 952},
        T(["_yes_ : " + ytxt], (0.15, 9), "cap", y=10, anim="words", stagger=0.05),
        T(["_but_ : " + btxt], (1.6, 9), "cap", y=60, anim="words", stagger=0.05)]}


def yesbut():
    return {"scenes": [
        SPLIT("IMG_9426", 4.5, "IMG_6794", 2.0, "une séance de reformer", "tes abdos demain matin."),
        SPLIT("IMG_3066", 0.2, "IMG_6799", 2.5, "7 places par cours", "le coach te voit. tout le temps."),
        SPLIT("IMG_9300", 1.5, "b2_IMG_6829", 0.5, "le matcha d'après", "tu voudras revenir demain."),
        END(),
    ]}


def hommes():
    """Mythe : « le pilates, c'est pas pour moi »."""
    return {"scenes": [
        {"dur": 2.8, "in": "cut", "out": "zoom", "layers": V("IMG_6822", 2.0, (1.0, 1.12), dim=.35) + [
            T(["« le pilates,", "c'est *pas~pour~moi.* »"], (0.15, 9), "hook", y=24, anim="words")]},
        {"dur": 2.0, "in": "zoom", "out": "zoom", "layers": V("IMG_6799", 2.5, (1.05, 1.15), dim=.2) + [
            T(["dis ça à *lui.*"], (0.1, 9), "hook", y=82, anim="words")]},
        {"dur": 2.0, "in": "zoom", "out": "zoom", "layers": V("IMG_6724", 4.0, (1.05, 1.15), dim=.2) + [
            T(["ou à *lui.*"], (0.1, 9), "hook", y=82, anim="words")]},
        {"dur": 3.0, "in": "zoom", "out": "cut", "layers": V("b2_IMG_6829", 0.0, (1.0, 1.08), dim=.25) + [
            T(["le reformer,", "c'est pour *tout~le~monde.*"], (0.2, 9), "hook", y=22, anim="words")]},
        END(),
    ]}


def journee():
    """Une journée au studio, de 7h à 22h30, montage rythmé."""
    seq = [("IMG_9122", 1.0, "7h00", "le studio ouvre."), ("IMG_9046", 1.0, "9h30", "cours coaché."),
           ("IMG_3062", 2.0, "12h30", "la pause déj'."), ("IMG_9297", 1.5, "15h00", "matcha time."),
           ("IMG_6445", 5.0, "18h30", "le cours complet."), ("IMG_0867", 4.0, "22h30", "dernière séance.")]
    sc = []
    for k, (c, st, h, txt) in enumerate(seq):
        sc.append({"dur": 1.6, "in": "cut" if k == 0 else "zoom", "out": "zoom", "layers": V(c, st, (1.0, 1.12), dim=.3) + [
            T([h], (0.05, 9), "big", y=44, anim="slam", stagger=0),
            T([txt], (0.25, 9), "mid", y=53, anim="words")]})
    sc.append(END("IMG_9059", 1.0, "ouvert *7j/7.*", "réserve en ligne · lien en bio"))
    return {"scenes": sc}


if __name__ == "__main__":
    name = sys.argv[1]
    spec = globals()[name]()
    if len(sys.argv) > 2 and sys.argv[2] == "still":
        ts = [float(x) for x in sys.argv[3].split(",")]
        still(spec, ts, f"{OUT}/_{name}.jpg")
    else:
        render(spec, f"{OUT}/SOA-reel-{name}.mp4")
    print("ok")
