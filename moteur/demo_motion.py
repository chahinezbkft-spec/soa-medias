import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import render, still
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sortie")
G = "saturate(.88) sepia(.18) contrast(1.04)"
CAN, CHOC, CAR, CREME = "#7A4636", "#3A2820", "#B88A63", "#EFE5DA"
def vid(clip, st, zoom=(1.0, 1.1), **kw):
    d = {"type": "video", "clip": clip, "start": st, "zoom": list(zoom), "grade": G}; d.update(kw); return d
def txt(lines, at, style="hook", y=50, anim="mask", **kw):
    d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim}; d.update(kw); return d
FX = [{"type": "grain"}]
def demo():
    return {"scenes": [
        # 1. le mot Pilates rempli de vidéo, sur aplat cannelle
        {"dur": 1.9, "in": "cut", "out": "whip", "layers": [
            {"type": "color", "color": CAN},
            {"type": "cliptext", "clip": "IMG_9426", "start": 4.2, "lines": ["Pilates"], "size": 380, "y": 36, "at": 0.05},
            txt(["la varenne · saint-maur"], (0.35, 9), "kicker", y=58, anim="track", color=CREME),
            txt(["ça se passe *ici.*"], (0.7, 9), "mid", y=64, anim="mask"),
        ] + FX},
        # 2. ouverture en cercle + titre masqué + soulignement dessiné
        {"dur": 2.3, "in": "iris", "out": "wipe", "wipeColor": CHOC, "layers": [
            vid("IMG_6724", 2.0, (1.05, 1.18)),
            {"type": "dim", "color": "rgba(42,28,22,.35)"},
            txt(["ce que", "ton coach"], (0.25, 9), "big", y=64, anim="mask", align="left", x=8.5, stagger=0.08),
            txt(["*voit.*"], (0.7, 9), "big", y=78, anim="letters", align="left", x=30),
            {"type": "underline", "x": 320, "y": 1570, "w": 430, "at": 1.1},
        ] + FX},
        # 3. écran partagé : vidéo qui glisse + compteur géant sur cannelle, au tempo
        {"dur": 2.0, "in": "cut", "out": "whip", "bpm": 120, "layers": [
            {"type": "color", "color": CAN},
            {"type": "video", "clip": "IMG_3062", "start": 2.0, "zoom": [1.1, 1.2], "grade": G, "box": [0, 0, 1080, 1060], "slide": "y", "slideFrom": -1100, "at": 0},
            {"type": "counter", "from": 0, "to": 7, "at": 0.35, "dur": 0.9, "style": "giant", "y": 72, "x": 50, "color": CREME},
            txt(["places max par cours"], (0.6, 9), "kicker", y=86, anim="track", color=CREME),
        ] + FX},
        # 4. carte vidéo inclinée + bandeau défilant
        {"dur": 2.2, "in": "whip", "out": "wipe", "wipeColor": CAN, "layers": [
            {"type": "color", "color": CHOC},
            {"type": "ticker", "text": "matcha · reformer · matcha · reformer ·", "y": 230, "size": 96, "color": CAR, "speed": 300, "rotate": -4},
            {"type": "card", "clip": "IMG_3342", "start": 0.4, "box": [150, 420, 780, 1020], "at": 0.05, "tilt": -8, "tiltEnd": -3, "grade": G, "border": "10px solid #EFE5DA"},
            txt(["le rituel"], (0.45, 9), "big", y=82, anim="swipe", align="left", x=8.5),
            txt(["*d'après.*"], (0.7, 9), "big", y=89.5, anim="swipe", align="left", x=30, color=CAR),
            {"type": "leak", "opacity": .55},
        ] + FX},
        # 5. punch + secousse, texte élastique
        {"dur": 1.6, "in": "punch", "out": "zoom", "shake": True, "bpm": 120, "layers": [
            vid("IMG_6801", 6.5, (1.1, 1.0)),
            {"type": "dim", "color": "rgba(42,28,22,.4)"},
            txt(["fous rires"], (0.1, 9), "big", y=44, anim="scale", stagger=0.1),
            txt(["*inclus.*"], (0.4, 9), "big", y=54, anim="scale", color=CAR),
        ] + FX},
        # 6. fin : panneau qui glisse + offre
        {"dur": 2.6, "in": "zoom", "out": "fadeblack", "layers": [
            vid("IMG_9059", 1.0, (1.12, 1.0)),
            {"type": "panel", "color": CHOC, "box": [0, 960, 1080, 960], "from": "bottom", "at": 0.15, "dur": 0.55},
            txt(["coaché · digital · hybride"], (0.45, 9), "kicker", y=56, anim="track"),
            txt(["découvre", "*les~2~mondes.*"], (0.6, 9), "big", y=67, anim="mask", align="left", x=8.5),
            txt(["1 coachée + 1 digitale · 36 €"], (1.1, 9), "boxed", y=82, anim="fade", align="left", x=8.5),
            txt(["@soa.reformer · lien en bio"], (1.3, 9), "kicker", y=90, anim="fade", align="left", x=8.5, color=CREME),
        ] + FX},
    ]}
if __name__ == "__main__":
    spec = demo()
    if len(sys.argv) > 1 and sys.argv[1] == "still":
        still(spec, [float(x) for x in sys.argv[2].split(",")], os.path.join(OUT, "_fx.jpg"))
    else:
        render(spec, os.path.join(OUT, "SOA-demo-motion.mp4"))
    print("ok")
