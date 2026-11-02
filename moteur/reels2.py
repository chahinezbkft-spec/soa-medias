"""Série 2 : nouveaux formats + variantes d'accroche pour les reels d'essai."""
import sys, os, copy
sys.path.insert(0, os.path.dirname(__file__))
import reels as R
from reels import V, T, END
from engine import render, still

OUT = R.OUT


def S(clip, start, dur, lines=None, y=22, style="hook", anim="words", zoom=(1.0, 1.12), dim=.25, tin="zoom", tout="zoom", extra=None):
    L = V(clip, start, zoom, dim=dim)
    if lines:
        L.append(T(lines, (0.12, 9), style, y=y, anim=anim))
    if extra:
        L += extra
    return {"dur": dur, "in": tin, "out": tout, "layers": L}


# ---------- nouveaux formats ----------

def local():
    """Accroche locale : « si tu habites à Saint-Maur… »."""
    return {"scenes": [
        S("IMG_2206", 3.0, 3.2, ["si tu habites à", "*Saint-Maur,*", "tu dois connaître", "cet endroit."], y=30, tin="cut", dim=.35),
        S("IMG_9122", 5.5, 1.6, ["un studio de", "*pilates~reformer*"], y=22),
        S("IMG_9057", 0.5, 1.6, ["7 places", "*par~cours.*"], y=22),
        S("IMG_3062", 1.0, 1.6, ["des coachs", "*qui~te~corrigent.*"], y=20),
        S("IMG_9300", 2.0, 1.6, ["un *matcha* après."], y=22),
        S("IMG_3342", 3.5, 1.8, ["et des gens", "*qu'on~adore.*"], y=78, tout="cut"),
        END(line2="au *111~av.~du~Bac.*"),
    ]}


def checklist():
    """Liste dense en boucle : 5 signes."""
    items = [("IMG_6822", 2.0, "1. ton dos tire", "après le bureau."),
             ("IMG_6794", 2.0, "2. tu sèches le sport", "depuis 3 semaines."),
             ("IMG_9426", 4.5, "3. tu veux des résultats", "sans te blesser."),
             ("IMG_6445", 6.0, "4. la salle", "t'ennuie."),
             ("IMG_3342", 4.5, "5. tu veux des potes", "de sport.")]
    sc = [S("IMG_6724", 2.0, 2.2, ["5 signes que tu as", "besoin du *reformer.*"], y=24, tin="cut", dim=.4)]
    for c, st, a, b in items:
        sc.append({"dur": 1.6, "in": "flash", "out": "cut", "layers": V(c, st, (1.05, 1.15), dim=.35) + [
            T([a, "*" + b.replace(" ", "~") + "*"], (0.05, 9), "mid", y=24, anim="words", stagger=0.04)]})
    sc.append(END(pill="combien tu en coches ? 👇"))
    return {"scenes": sc}


def mythes():
    """3 idées reçues."""
    def M(clip, st, faux, vrai):
        return {"dur": 2.8, "in": "zoom", "out": "zoom", "layers": V(clip, st, (1.0, 1.12), dim=.35) + [
            T(["« " + faux + " »"], (0.1, 9), "mid", y=20, anim="words", stagger=0.04),
            T(["_faux._"], (0.9, 9), "big", y=34, anim="slam", stagger=0),
            T([vrai], (1.3, 9), "small", y=82, anim="words", stagger=0.04)]}
    return {"scenes": [
        S("IMG_6817", 6.0, 2.2, ["3 idées reçues", "sur le *pilates.*"], y=24, tin="cut", dim=.4),
        M("IMG_6817", 8.0, "c'est que des étirements", "regarde ses bras trembler."),
        M("IMG_6801", 6.0, "c'est pour les femmes", "le cours des hommes est complet."),
        M("IMG_6445", 5.0, "c'est mou", "demande à tes abdos demain."),
        END(),
    ]}


def avant_apres():
    """Séance 1 vs séance 10 (écran partagé)."""
    def SP(top, ts, bot, bs, a, b):
        return {"dur": 4.0, "in": "flash", "out": "cut", "layers": [
            {"type": "video", "clip": top, "start": ts, "zoom": [1.0, 1.06], "grade": R.GRADE, "box": [0, 0, 1080, 952]},
            {"type": "video", "clip": bot, "start": bs, "zoom": [1.0, 1.06], "grade": R.GRADE, "box": [0, 968, 1080, 952]},
            {"type": "dim", "color": "rgba(22,17,14,.15)"}, {"type": "bar", "y": 952},
            T([a], (0.15, 9), "cap", y=10, anim="words"), T([b], (1.4, 9), "cap", y=60, anim="words")]}
    return {"scenes": [
        SP("IMG_6822", 2.0, "IMG_9426", 4.0, "séance 1 : _survivre._", "séance 10 : _voler._"),
        SP("IMG_6794", 1.5, "IMG_3069", 1.0, "séance 1 : « c'est quoi ce ressort ? »", "séance 10 : _en synchro._"),
        END(pill="ta séance 1, c'est quand ?"),
    ]}


def dix():
    """10 exercices en 10 secondes, montage rythmé."""
    clips = [("IMG_9426", 4.5), ("IMG_1467", 4.0), ("IMG_3069", 1.5), ("IMG_4848", 1.5), ("IMG_9316", 1.5),
             ("IMG_6445", 6.0), ("IMG_2182", 3.0), ("IMG_9331", 2.0), ("IMG_9424", 3.0), ("IMG_3062", 3.0)]
    sc = [S("IMG_9420", 1.5, 1.6, ["10 exercices.", "*10~secondes.*"], y=24, tin="cut", dim=.4, tout="cut")]
    for k, (c, st) in enumerate(clips, 1):
        sc.append({"dur": 1.0, "in": "flash" if k % 2 else "zoom", "out": "cut", "layers": V(c, st, (1.12, 1.0), dim=.15) + [
            T([str(k)], (0.0, 9), "big", y=84, anim="slam", stagger=0, out=False)]})
    sc.append(END(pill="lequel tu testes en premier ?"))
    return {"scenes": sc}


def premiere():
    """Ce qui t'attend à ta première séance, étape par étape."""
    steps = [("IMG_4615", 0.5, "1. on t'accueille", "par ton *prénom.*"),
             ("IMG_9420", 1.5, "2. chaussettes", "*antidérapantes.*"),
             ("IMG_6724", 2.0, "3. le coach t'explique", "*la~machine.*"),
             ("IMG_9362", 0.8, "4. on règle", "*tes~ressorts.*"),
             ("IMG_3062", 2.0, "5. 50 min", "*qui~passent~vite.*"),
             ("IMG_9300", 2.0, "6. et un matcha", "*pour~finir.*")]
    sc = [S("IMG_9122", 1.5, 2.4, ["ta première séance", "de *pilates~reformer,*", "étape par étape."], y=30, tin="cut", dim=.35)]
    for c, st, a, b in steps:
        crop = "405:720:430:0" if c == "IMG_9362" else None
        L = V(c, st, (1.0, 1.1), dim=.3, crop=crop)
        L.append(T([a, b], (0.08, 9), "mid", y=22, anim="words", stagger=0.04))
        sc.append({"dur": 1.8, "in": "zoom", "out": "zoom", "layers": L})
    sc[-1]["out"] = "cut"
    sc.append(END(pill="ta première séance t'attend"))
    return {"scenes": sc}


def texto():
    """Le texto de ta pote à 18h."""
    return {"scenes": [
        {"dur": 5.2, "in": "cut", "out": "zoom", "layers": V("IMG_2206", 0.5, (1.0, 1.08), dim=.5) + [
            T(["18h12"], (0.0, 9), "kicker", y=14, anim="fade"),
            {"type": "bubble", "side": "left", "text": "je suis claquée… on annule le pilates ?", "y": 400, "at": 0.3},
            {"type": "bubble", "side": "right", "text": "non. on a réservé 19h.", "y": 620, "at": 1.4},
            {"type": "bubble", "side": "right", "text": "je passe te chercher 🤎", "y": 790, "at": 2.3},
            {"type": "bubble", "side": "left", "text": "…ok", "y": 980, "at": 3.3}]},
        S("IMG_2206", 7.5, 1.8, ["19h00"], y=20, style="big", anim="slam"),
        S("IMG_3066", 0.2, 1.8, ["19h45"], y=20, style="big", anim="slam"),
        S("IMG_3342", 4.5, 2.6, ["20h10 :", "*«~merci~de~m'avoir~forcée~»*"], y=78, tout="cut"),
        END(pill="envoie-le à ta pote qui annule toujours"),
    ]}


def muscu():
    """Pour les habitués de la salle de muscu."""
    return {"scenes": [
        S("IMG_6822", 2.0, 2.6, ["tu fais de la *muscu~?*", "ajoute ça une fois", "par semaine."], y=26, tin="cut", dim=.4),
        S("IMG_6817", 6.0, 2.0, ["gainage *profond.*"], y=82, style="mid"),
        S("IMG_6724", 3.0, 2.0, ["mobilité de *hanche.*"], y=82, style="mid"),
        S("IMG_6799", 2.0, 2.0, ["un coach qui *te~voit.*"], y=82, style="mid"),
        S("b2_IMG_6829", 0.5, 2.2, ["et zéro *ego.*"], y=22, tout="cut"),
        END(),
    ]}


def duo():
    """Viens à deux."""
    return {"scenes": [
        S("IMG_2206", 3.0, 3.0, ["envoie ça à la personne", "avec qui tu veux", "*commencer.*"], y=28, tin="cut", dim=.38),
        S("IMG_4615", 0.5, 1.6, ["vous arrivez *ensemble.*"], y=22),
        S("IMG_3069", 1.0, 2.0, ["vous tremblez *ensemble.*"], y=20),
        S("IMG_3342", 4.5, 2.4, ["vous en riez *ensemble.*"], y=78, tout="cut"),
        END(pill="à deux, c'est plus facile de revenir"),
    ]}


def pov_coach():
    """POV : le coach dit « encore 10 »."""
    return {"scenes": [
        S("IMG_6799", 1.0, 2.6, ["POV : le coach dit", "*«~encore~10~»*"], y=22, tin="cut", dim=.35),
        S("IMG_6817", 7.0, 1.8, ["toi à 3 :"], y=22, style="mid"),
        S("IMG_6801", 8.0, 1.8, ["toi à 7 :"], y=22, style="mid"),
        S("IMG_6805", 2.0, 2.4, ["toi à 10 :"], y=22, style="mid", tout="cut"),
        END(),
    ]}


def mondes():
    """Coaché, digital ou hybride : les 2 mondes de SOA."""
    def M(clip, st, titre, l1, l2=None):
        lines = [l1] + ([l2] if l2 else [])
        return {"dur": 2.8, "in": "zoom", "out": "zoom", "layers": V(clip, st, (1.0, 1.1), dim=.3) + [
            T([titre], (0.1, 9), "big", y=16, anim="slam", stagger=0),
            T(lines, (0.45, 9), "mid", y=26, anim="words", stagger=0.04)]}
    sc = [S("IMG_6630", 0.5, 2.8, ["chez SOA, il y a", "*2~façons*", "de faire du pilates."], y=30, tin="cut", dim=.4),
          M("IMG_6724", 2.0, "*le~coaché*", "un coach, 7 places max."),
          M("IMG_1467", 3.0, "*le~digital*", "ton reformer + l'écran,", "à ton heure, 7j/7."),
          M("IMG_9426", 4.0, "*l'hybride*", "les deux dans ta semaine.")]
    sc[-1]["out"] = "cut"
    sc.append(END(pill="lequel est fait pour toi ?"))
    return {"scenes": sc}


def versions():
    """Tendance « do it heartbroken… do it anyway » : toutes les versions de toi ont leur place."""
    moods = ["*le~cœur~brisé.*", "*de~bonne~humeur.*", "*sans~énergie.*", "*en~retard.*", "*avec~le~trac.*",
             "*un~lundi.*", "*en~colère.*", "*sans~motivation.*", "*le~sourire~aux~lèvres.*"]
    shots = [("IMG_9415", 0.3, None), ("IMG_9362", 1.0, "405:720:470:0"), ("IMG_9415", 1.6, None),
             ("IMG_9362", 1.8, "405:720:380:0"), ("IMG_9415", 3.0, None), ("IMG_9362", 2.6, "405:720:520:0"),
             ("IMG_9415", 4.6, None), ("IMG_9362", 3.3, "405:720:430:0"), ("IMG_9415", 6.2, None)]
    sc = []
    for (clip, st, crop), m in zip(shots, moods):
        sc.append({"dur": 0.8, "in": "cut", "out": "cut", "layers": V(clip, st, (1.04, 1.08), crop=crop, dim=.22) + [
            T(["fais-le", m], (0.0, 9), "hook", y=44, anim="fade")]})
    sc.append({"dur": 1.8, "in": "cut", "out": "cut", "layers": V("IMG_9415", 7.2, (1.04, 1.1), dim=.25) + [
        T(["fais-le", "*quand~même.*"], (0.0, 9), "hook", y=44, anim="fade"),
        T(["🤍"], (0.5, 9), "mid", y=56, anim="pop")]})
    sc.append({"dur": 2.6, "in": "fade", "out": "zoom", "layers": V("IMG_6801", 6.0, (1.0, 1.08), dim=.4) + [
        T(["toutes les versions", "de toi ont leur", "place *ici.*"], (0.2, 9), "hook", y=46, anim="words")]})
    sc.append(END())
    return {"scenes": sc}


# ---------- variantes d'accroche (reels d'essai) ----------

def variant(base, hook_lines, y=24, kicker=None):
    spec = copy.deepcopy(base())
    sc = spec["scenes"][0]
    sc["layers"] = [L for L in sc["layers"] if L["type"] != "text"]
    if kicker:
        sc["layers"].append(T([kicker], (0.05, 9), "kicker", y=y - 9, anim="fade"))
    sc["layers"].append(T(hook_lines, (0.12, 9), "hook", y=y, anim="words"))
    return spec


def porte_b(): return variant(R.porte, ["ce qui t'attend à ta", "*première~séance*", "de pilates reformer."], y=36)
def porte_c(): return variant(R.porte, ["le studio de pilates", "dont tout le monde", "parle à *Saint-Maur.*"], y=36)
def coachs_b(): return variant(R.coachs, ["ton coach voit tout.", "*vraiment~tout.*"])
def coachs_c(): return variant(R.coachs, ["pourquoi tu ne", "progresses pas *seul·e*", "en pilates."])
def hommes_b(): return variant(R.hommes, ["« c'est pas", "un sport *pour~moi* »", "(spoiler : si)"])
def outil_b():
    spec = copy.deepcopy(R.outil())
    spec["scenes"][0]["layers"] = [L for L in spec["scenes"][0]["layers"] if L["type"] != "text"] + [
        T(["ce qu'il faut pour", "un *corps~plus~fort*"], (0.1, 9), "hook", y=46, anim="words")]
    return spec


ALL = ["versions", "mondes", "local", "checklist", "mythes", "avant_apres", "dix", "premiere", "texto", "muscu", "duo", "pov_coach",
       "porte_b", "porte_c", "coachs_b", "coachs_c", "hommes_b", "outil_b"]

if __name__ == "__main__":
    name = sys.argv[1]
    spec = globals()[name]()
    if len(sys.argv) > 2 and sys.argv[2] == "still":
        ts = [float(x) for x in sys.argv[3].split(",")]
        still(spec, ts, f"{OUT}/_{name}.jpg")
    else:
        render(spec, f"{OUT}/SOA-reel-{name}.mp4")
    print("ok")
