import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine import render, still
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "sortie")
os.makedirs(OUT, exist_ok=True)
G = "saturate(.85) sepia(.18) contrast(1.05) brightness(.95)"
CAN, CHOC, CAR, CREME = "#7A4636", "#3A2820", "#B88A63", "#EFE5DA"
def vid(clip, st, zoom=(1.0, 1.08), **kw):
    d = {"type": "video", "clip": clip, "start": st, "zoom": list(zoom), "grade": G, "extra": 0.9, "ease": "inout"}; d.update(kw); return d
def txt(lines, at, style, y, anim="mask", **kw):
    d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim, "align": "left", "x": 8.9, "dur": 0.9, "ease": "inout", "stagger": 0.1}
    d.update(kw); return d
GR = {"type": "grain", "opacity": .07}
VEIL = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.2), rgba(42,28,22,.2) 50%, rgba(42,28,22,.75))"}
def spec():
    return {"scenes": [
        # 1. le mot géant DERRIÈRE la personne
        {"dur": 3.0, "in": "fade", "layers": [
            vid("IMG_9426", 3.4), {"type": "dim", "color": "rgba(42,28,22,.25)"},
            txt(["la varenne · saint-maur"], (0.2, 9), "caps", 12, anim="track", color=CREME),
            txt(["Pilates"], (0.15, 9), "giant", 30, anim="mask", align="center", x=50, color=CREME, dur=1.1),
            {"type": "cutout", "clip": "IMG_9426", "start": 3.4, "zoom": [1.0, 1.08], "ease": "inout", "grade": G, "extra": 0.9},
            txt(["*ça~se~passe~ici.*"], (1.2, 9), "edito", 86, color=CREME), GR]},
        # 2. carnet : vidéos encadrées + note épinglée sur fond rayé
        {"dur": 3.0, "in": "dissolve", "dissolve": 0.7, "layers": [
            {"type": "stripes"},
            txt(["les 2 mondes"], (0.1, 9), "edito", 10, anim="mask", color=CREME),
            {"type": "card", "clip": "IMG_6724", "start": 2.0, "box": [70, 380, 470, 640], "at": 0.2, "tilt": -5, "tiltEnd": -3, "grade": G, "border": "14px solid #F3EADC"},
            {"type": "note", "x": 540, "y": 470, "w": 440, "at": 0.55, "rot": 4, "kicker": "monde n°1", "text": "le coaché : un coach, 7 places max."},
            {"type": "card", "clip": "IMG_1467", "start": 3.0, "box": [560, 1130, 440, 600], "at": 0.9, "tilt": 6, "tiltEnd": 3, "grade": G, "border": "14px solid #F3EADC"},
            {"type": "note", "x": 80, "y": 1210, "w": 430, "at": 1.25, "rot": -4, "kicker": "monde n°2", "text": "le digital : ton reformer, à ton heure."},
            {"type": "grain", "opacity": .1}]},
        # 3. widget horloge + interrupteur
        {"dur": 2.6, "in": "dissolve", "dissolve": 0.7, "layers": [
            vid("IMG_3062", 2.0, (1.1, 1.0)), VEIL,
            {"type": "clock", "x": 96, "y": 260, "at": 0.2, "from": 420, "to": 1350, "dur": 1.4, "label": "ouvert 7j/7"},
            {"type": "toggle", "x": 96, "y": 1450, "at": 1.4, "inAt": 0.8, "label": "mode digital"},
            txt(["à ton heure."], (0.9, 9), "edito", 86, color=CREME), GR]},
        # 4. texte qui tourne autour du matcha
        {"dur": 2.6, "in": "dissolve", "dissolve": 0.7, "layers": [
            vid("IMG_9300", 0.6, (1.06, 1.0), speed=0.5), {"type": "dim", "color": "rgba(42,28,22,.28)"},
            {"type": "circletext", "cx": 560, "cy": 1180, "r": 360, "at": 0.2, "speed": 22, "size": 44, "text": "le rituel d'après · matcha · le rituel d'après · matcha ·"},
            txt(["le rituel"], (0.5, 9), "edito", 12, color=CREME),
            txt(["*d'après.*"], (0.75, 9), "edito", 18.5, color=CAR), GR]},
        # 5. fin : interrupteur « pack découverte » + étiquette 36 € qui se balance
        {"dur": 3.2, "in": "dissolve", "dissolve": 0.7, "out": "fadeblack", "layers": [
            vid("IMG_3342", 0.4, (1.05, 1.0)), {"type": "dim", "color": "rgba(42,28,22,.5)"},
            txt(["découvre"], (0.2, 9), "edito", 8, color=CREME),
            txt(["*les~2~mondes.*"], (0.45, 9), "edito", 14.5, color=CAR),
            {"type": "pricetag", "x": 100, "y": 400, "at": 0.8, "kicker": "pack découverte", "value": "36 €", "sub": "1 coachée + 1 digitale"},
            {"type": "toggle", "x": 96, "y": 1500, "at": 1.9, "inAt": 1.4, "label": "je réserve"},
            txt(["@soa.reformer · lien en bio"], (2.2, 9), "caps", 90, anim="fade", color=CREME), GR]},
    ]}
if __name__ == "__main__":
    s = spec()
    if len(sys.argv) > 1 and sys.argv[1] == "still":
        still(s, [float(x) for x in sys.argv[2].split(",")], os.path.join(OUT, "_in.jpg"))
    else:
        render(s, os.path.join(OUT, "SOA-demo-inspi.mp4"))
    print("ok")
