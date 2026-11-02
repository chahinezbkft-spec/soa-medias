"""Grille test : 9 couvertures SOA dans la charte adaptée (format grille 3:4, 1080x1440)."""
import os
from playwright.sync_api import sync_playwright
from PIL import Image

D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(os.path.dirname(D), "soa", "rushes", "photos")
CHROME = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1440px;overflow:hidden;font-family:'Inter Tight';-webkit-font-smoothing:antialiased}
.t{position:absolute;inset:0;overflow:hidden}
.ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:saturate(.9) sepia(.08) contrast(1.02)}
.voile{position:absolute;left:0;right:0;bottom:0;height:62%;background:linear-gradient(to bottom,rgba(33,27,23,0),rgba(33,27,23,.74))}
.h{position:absolute;left:96px;right:96px;color:#FBFAF7}
.sans{display:block;font-weight:700;font-size:118px;letter-spacing:-.05em;line-height:.92;text-transform:lowercase}
.serif{display:block;font-family:'Instrument Serif';font-style:italic;font-weight:400;font-size:150px;letter-spacing:-.02em;line-height:.9;margin-top:-6px}
.tag{display:inline-block;background:#D9B77E;color:#211B17;font-weight:500;font-size:30px;padding:6px 16px;transform:rotate(-4deg);margin-bottom:26px}
.handle{position:absolute;left:50%;bottom:72px;transform:translateX(-50%);border:2px solid currentColor;border-radius:12px;padding:8px 22px;font-weight:500;font-size:24px;letter-spacing:.08em;text-transform:uppercase}
.count{position:absolute;right:72px;top:72px;font-weight:500;font-size:24px;letter-spacing:.1em}
.note{font-family:'Caveat';font-weight:500;font-size:62px;transform:rotate(-6deg);position:absolute}
.pill{display:flex;align-items:center;gap:22px;background:#FBFAF7;color:#211B17;border-radius:999px;height:96px;padding:0 36px 0 16px;font-weight:500;font-size:36px;margin-top:22px}
.pill b{width:64px;height:64px;border-radius:50%;background:#211B17;color:#FBFAF7;display:flex;align-items:center;justify-content:center;font-weight:600;font-size:28px}
.cap{font-weight:500;font-size:26px;letter-spacing:.1em;text-transform:uppercase;color:#6F655B}
.hl{background:#D9B77E;padding:2px 12px;color:#211B17}
"""


def photo(img, sans, serif, tag=None, y=None, pos="50% 40%", offset=150, voile=True):
    tg = f'<span class="tag">[ {tag} ]</span><br>' if tag else ""
    top = f"top:{y}px" if y else "bottom:230px"
    return f"""<div class="t" style="background:#211B17"><img class="ph" src="file://{img}" style="object-position:{pos}">
    {'<div class="voile"></div>' if voile else ''}
    <div class="h" style="{top}">{tg}<span class="sans">{sans}</span><span class="serif" style="padding-left:{offset}px">{serif}</span></div>
    <div class="handle" style="color:#FBFAF7">@soa.reformer</div></div>"""


def tiles():
    J = lambda f: os.path.join(D, f)
    Q = lambda f: os.path.join(P, f)
    return [
        photo(J("r-hyb.jpg"), "les 2 mondes", "de SOA.", tag="nouveau", pos="50% 35%"),
        photo(Q("5C21792C-01D9-4A15-A97B-FEBD50F71995.jpg"), "pourquoi les sportifs", "s'y mettent.", tag="pédagogie", offset=120),
        # transition fond encre + vignette
        f"""<div class="t" style="background:#211B17;color:#FBFAF7">
        <img src="file://{J('r-ressorts.jpg')}" style="position:absolute;right:96px;top:150px;width:360px;height:450px;object-fit:cover;border:10px solid #FBFAF7;transform:rotate(3deg)">
        <div class="note" style="left:130px;top:430px;color:#D9B77E">même un lundi ↘</div>
        <div class="h" style="bottom:300px"><span class="sans" style="font-size:150px">fais-le</span><span class="serif" style="font-size:190px;padding-left:120px">quand même.</span></div>
        <div class="handle">@soa.reformer</div></div>""",
        photo(J("r-matcha.jpg"), "le rituel", "d'après.", pos="50% 50%", offset=180),
        # stat fond lin
        f"""<div class="t" style="background:#F3F0EB;color:#211B17">
        <div class="cap" style="position:absolute;left:96px;top:120px">coaché · par cours</div>
        <div style="position:absolute;left:80px;top:150px;font-family:'Instrument Serif';font-style:italic;font-size:620px;line-height:1">7</div>
        <div class="note" style="left:420px;top:420px;color:#211B17">oui, vraiment ↙</div>
        <div class="h" style="top:820px;color:#211B17"><span class="sans" style="font-size:110px">places max.</span>
        <p style="margin-top:36px;font-size:38px;line-height:1.4;max-width:760px"><span class="hl">un coach qui te voit vraiment</span>, pas une salle où tu te caches au fond.</p></div>
        <div class="handle" style="color:#211B17">@soa.reformer</div></div>""",
        photo(J("r-coach.jpg"), "ce que ton coach", "voit.", tag="pédagogie", pos="50% 45%", offset=220),
        photo(Q("534A03E5-09DF-4225-8EFD-FA4BB2C9AEEE.jpg"), "tu viens pour le pilates,", "tu restes pour…", offset=60),
        photo(J("r-rires.jpg"), "« c'est pas", "pour moi. »", pos="50% 45%", offset=160),
        # CTA fond encre
        f"""<div class="t" style="background:#211B17;color:#FBFAF7">
        <div class="h" style="top:250px"><span class="sans" style="font-size:130px">découvre</span><span class="serif" style="font-size:170px;padding-left:110px">les 2 mondes.</span>
        <div style="margin-top:70px;max-width:760px">
        <div class="pill"><b>1</b>une séance coachée</div><div class="pill"><b>2</b>une séance digitale</div><div class="pill"><b>→</b>36 € · lien en bio</div></div></div>
        <div class="note" style="right:110px;bottom:200px;color:#D9B77E">à toi de choisir ↘</div>
        <div class="handle">@soa.reformer</div></div>""",
    ]


if __name__ == "__main__":
    out = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1080, "height": 1440})
        for i, body in enumerate(tiles(), 1):
            h = os.path.join(D, f"_t{i}.html")
            open(h, "w", encoding="utf-8").write(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
            pg.goto("file://" + h)
            pg.wait_for_timeout(500)
            f = os.path.join(D, f"tile-{i}.jpg")
            pg.screenshot(path=f, type="jpeg", quality=90)
            out.append(f)
        b.close()
    W, G = 360, 6
    grid = Image.new("RGB", (3 * W + 2 * G, 3 * 480 + 2 * G), "white")
    for k, f in enumerate(out):
        grid.paste(Image.open(f).resize((W, 480), Image.LANCZOS), ((k % 3) * (W + G), (k // 3) * (480 + G)))
    grid.save(os.path.join(D, "grille-test-soa.jpg"), quality=90)
    print("ok")
