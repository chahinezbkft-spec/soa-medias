import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine import render, still
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "sortie")
os.makedirs(OUT, exist_ok=True)
G = "saturate(.82) sepia(.2) contrast(1.06) brightness(.94)"
CAN, CHOC, CAR, CREME = "#7A4636", "#3A2820", "#B88A63", "#EFE5DA"
def vid(clip, st, zoom=(1.04, 1.12), speed=1.0, **kw):
    d = {"type": "video", "clip": clip, "start": st, "zoom": list(zoom), "grade": G, "speed": speed, "extra": 0.9, "ease": "inout"}; d.update(kw); return d
def txt(lines, at, style, y, anim="mask", **kw):
    d = {"type": "text", "lines": lines, "at": list(at), "style": style, "y": y, "anim": anim, "align": "left", "x": 8.9, "dur": 1.0, "ease": "inout", "stagger": 0.12}
    d.update(kw); return d
VEIL = {"type": "dim", "color": "linear-gradient(to bottom, rgba(42,28,22,.25), rgba(42,28,22,.25) 45%, rgba(42,28,22,.78))"}
GR = {"type": "grain", "opacity": .07}
def classe():
    return {"scenes": [
        # 1. ouverture cinéma : bandes chocolat, lente poussée, titre éditorial
        {"dur": 3.0, "in": "fade", "layers": [
            vid("IMG_9426", 3.6, (1.0, 1.12), speed=0.6), VEIL,
            {"type": "bars", "h": 200},
            txt(["soa · la varenne"], (0.3, 9), "caps", 16, anim="track", color=CAR),
            txt(["un rythme,"], (0.7, 9), "edito", 66, color=CREME),
            txt(["*pas~une~résolution.*"], (1.1, 9), "edito", 72.5, color=CAR),
            {"type": "rule", "x": 96, "y": 1500, "w": 220, "at": 1.6, "color": CAR}, GR]},
        # 2. fenêtre qui s'agrandit sur fond crème
        {"dur": 2.8, "in": "window", "windowDur": 1.1, "layers": [
            {"type": "color", "color": CREME},
            {"type": "video", "clip": "IMG_6724", "start": 2.0, "zoom": [1.1, 1.0], "grade": G, "extra": 0.9, "ease": "inout", "box": [0, 0, 1080, 1920]},
            VEIL,
            txt(["le coaché"], (0.9, 9), "caps", 72, anim="track", color=CAR),
            txt(["un coach qui"], (1.1, 9), "edito", 79, color=CREME),
            txt(["*te~voit~vraiment.*"], (1.35, 9), "edito", 85.5, color=CREME), GR],
         "windowFrom": 26},
        # 3. diptyque : deux vidéos séparées par un filet crème
        {"dur": 2.8, "in": "dissolve", "dissolve": 0.9, "layers": [
            {"type": "color", "color": CREME},
            {"type": "video", "clip": "IMG_1467", "start": 3.0, "zoom": [1.15, 1.25], "grade": G, "extra": 0.9, "box": [0, 0, 536, 1920], "ease": "inout"},
            {"type": "video", "clip": "IMG_3062", "start": 2.0, "zoom": [1.25, 1.15], "grade": G, "extra": 0.9, "box": [544, 0, 536, 1920], "ease": "inout"},
            VEIL,
            txt(["coaché · digital · hybride"], (0.5, 9), "caps", 76, anim="track", color=CAR),
            txt(["à toi de choisir"], (0.8, 9), "edito", 83, color=CREME),
            txt(["*ton~rythme.*"], (1.05, 9), "edito", 89.5, color=CREME), GR]},
        # 4. le chiffre, en serif, sur cannelle
        {"dur": 2.6, "in": "dissolve", "dissolve": 0.8, "layers": [
            {"type": "color", "color": CAN}, {"type": "grain", "opacity": .12},
            txt(["par cours, jamais plus"], (0.3, 9), "caps", 22, anim="track", color=CREME),
            {"type": "counter", "from": 1, "to": 7, "at": 0.4, "dur": 1.6, "style": "numserif", "x": 8.9, "y": 46, "align": "left", "color": CREME},
            {"type": "rule", "x": 96, "y": 1250, "w": 888, "at": 0.9, "dur": 1.2, "color": CAR},
            txt(["places."], (1.2, 9), "edito", 71, color=CREME)]},
        # 5. ralenti matcha
        {"dur": 2.6, "in": "dissolve", "dissolve": 0.8, "layers": [
            vid("IMG_9300", 0.6, (1.08, 1.0), speed=0.5), VEIL,
            txt(["le rituel"], (0.6, 9), "edito", 79, color=CREME),
            txt(["*d'après.*"], (0.85, 9), "edito", 85.5, color=CAR), GR]},
        # 6. fin crème, sobre
        {"dur": 3.0, "in": "dissolve", "dissolve": 0.8, "out": "fadeblack", "layers": [
            {"type": "color", "color": CREME}, {"type": "grain", "opacity": .1},
            txt(["SOA"], (0.3, 9), "logo", 20, anim="track", color=CHOC),
            txt(["découvre"], (0.6, 9), "edito", 46, color=CHOC),
            txt(["*les~2~mondes.*"], (0.85, 9), "edito", 52.5, color=CAN),
            {"type": "rule", "x": 96, "y": 1150, "w": 300, "at": 1.3, "color": CAN},
            txt(["1 coachée + 1 digitale · 36 €"], (1.5, 9), "caps", 64, anim="track", color=CHOC),
            txt(["@soa.reformer · lien en bio"], (1.8, 9), "caps", 88, anim="fade", color=CAN)]},
    ]}
if __name__ == "__main__":
    spec = classe()
    for s in spec["scenes"]:
        if s.get("in") == "dissolve" or True:
            pass
    if len(sys.argv) > 1 and sys.argv[1] == "still":
        still(spec, [float(x) for x in sys.argv[2].split(",")], os.path.join(OUT, "_cl.jpg"))
    else:
        render(spec, os.path.join(OUT, "SOA-demo-classe.mp4"))
    print("ok")
