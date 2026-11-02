"""Grille v3 « cannelle » : couleur pleine texturée en damier avec photos chaudes, 3 voix typo."""
import os
from playwright.sync_api import sync_playwright
from PIL import Image

D = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(os.path.dirname(D), "soa", "rushes", "photos")
CHROME = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"
CAN, CHOC, CAR, CREME = "#7A4636", "#3A2820", "#B88A63", "#EFE5DA"
GRAIN = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/></filter>"
         "<rect width='300' height='300' filter='url(%23n)' opacity='.55'/></svg>\")")
CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1440px;overflow:hidden;-webkit-font-smoothing:antialiased;color:{CREME}}}
.t{{position:absolute;inset:0;overflow:hidden}}
.solid::after{{content:'';position:absolute;inset:0;background:{GRAIN};mix-blend-mode:soft-light;opacity:.5}}
.ph{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:saturate(.85) sepia(.22) contrast(1.03) brightness(.98)}}
.veil{{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(58,40,32,.05) 35%,rgba(58,40,32,.62))}}
.lab{{position:absolute;font-family:'Inter Tight';font-weight:500;font-size:22px;letter-spacing:.22em;text-transform:uppercase}}
.caps{{font-family:'Cormorant Garamond';font-weight:500;text-transform:uppercase;letter-spacing:-.01em;line-height:.9}}
.it{{font-family:'Cormorant Garamond';font-style:italic;font-weight:400}}
.script{{font-family:'Pinyon Script';font-weight:400;line-height:1}}
.hand{{font-family:'Homemade Apple';line-height:1.45}}
.c{{position:absolute;left:0;right:0;text-align:center}}
"""


def photo(img, inner, pos="50% 45%", veil=True):
    return f'<div class="t"><img class="ph" src="file://{img}" style="object-position:{pos}">{"<div class=veil></div>" if veil else ""}{inner}</div>'


def solid(color, inner):
    return f'<div class="t solid" style="background:{color}">{inner}</div>'


def tiles():
    J = lambda f: os.path.join(D, f)
    Q = lambda f: os.path.join(P, f)
    return [
        photo(J("r-hyb.jpg"), """
          <div class="lab" style="left:0;right:0;top:120px;text-align:center">coaché · digital · hybride</div>
          <div class="c" style="top:820px"><div class="caps" style="font-size:150px">les 2 mondes</div>
          <div class="script" style="font-size:150px;margin-top:-40px">de SOA</div></div>""", pos="50% 30%"),
        solid(CAN, """
          <div class="lab" style="left:72px;top:72px">daily reminder</div><div class="lab" style="right:72px;top:72px">soa · pilates reformer</div>
          <div class="hand c" style="top:440px;font-size:74px;padding:0 140px">fais-le le cœur brisé, fais-le en retard, fais-le quand même.</div>
          <div class="lab" style="left:72px;bottom:72px">novembre</div><div class="lab" style="right:72px;bottom:72px">@soa.reformer</div>"""),
        photo(J("r-matcha.jpg"), """
          <div class="lab" style="left:110px;top:600px;font-size:30px;line-height:1.6">18h : reformer.<br>19h : matcha.</div>
          <div style="position:absolute;left:110px;top:720px;width:1px;height:160px;background:#EFE5DA"></div>
          <div class="it" style="position:absolute;left:110px;bottom:150px;font-size:44px">le rituel d'après.</div>""", pos="50% 55%", veil=False),
        photo(Q("5C21792C-01D9-4A15-A97B-FEBD50F71995.jpg"), """
          <div class="c" style="top:840px"><div class="script" style="font-size:110px">pourquoi les</div>
          <div class="caps" style="font-size:132px;margin-top:-10px">sportifs<br>s'y mettent</div></div>"""),
        solid(CREME, f"""
          <div class="lab" style="left:0;right:0;top:250px;text-align:center;color:{CAN}">c'est maintenant</div>
          <div class="c" style="top:470px;color:{CHOC}"><div class="it" style="font-size:190px;line-height:.9">un rythme,</div>
          <div class="caps" style="font-size:118px;margin-top:20px">pas une<br>résolution.</div>
          <div style="font-family:'Inter Tight';font-size:32px;margin-top:60px;color:{CAN}">3 séances par semaine. Le reste suit.</div></div>
          <div class="lab" style="left:0;right:0;bottom:90px;text-align:center;color:{CHOC}">@soa.reformer</div>"""),
        photo(J("r-coach.jpg"), """
          <div class="c" style="top:860px"><div class="caps" style="font-size:120px">ce que ton coach</div>
          <div class="script" style="font-size:170px;margin-top:-30px">voit</div></div>"""),
        photo(Q("534A03E5-09DF-4225-8EFD-FA4BB2C9AEEE.jpg"), """
          <div class="hand" style="position:absolute;left:96px;top:250px;font-size:48px;max-width:640px">tu viens pour le pilates…</div>
          <div class="c" style="top:950px"><div class="caps" style="font-size:118px">tu restes pour</div><div class="script" style="font-size:150px;margin-top:-25px">tout le reste</div></div>"""),
        solid(CHOC, f"""
          <div class="lab" style="left:0;right:0;top:120px;text-align:center;color:{CAR}">quote of the day</div>
          <div class="c" style="top:470px"><div class="script" style="font-size:150px;color:{CAR}">c'est pas pour moi</div>
          <div class="caps" style="font-size:160px;margin-top:10px">spoiler :<br>si.</div></div>
          <div style="position:absolute;left:540px;top:1080px;width:1px;height:150px;background:{CAR}"></div>
          <div class="lab" style="left:0;right:0;bottom:90px;text-align:center">@soa.reformer</div>"""),
        photo(J("r-rires.jpg"), f"""
          <div class="c" style="top:700px"><div class="script" style="font-size:120px">découvre</div>
          <div class="caps" style="font-size:150px;margin-top:-10px">les 2 mondes</div>
          <div style="display:inline-block;margin-top:50px;border:1.5px solid {CREME};padding:18px 40px;font-family:'Inter Tight';font-size:30px;letter-spacing:.12em;text-transform:uppercase">1 coachée + 1 digitale · 36 €</div></div>
          <div class="lab" style="left:72px;bottom:72px">↗ lien en bio</div><div class="lab" style="right:72px;bottom:72px">@soa.reformer</div>"""),
    ]


if __name__ == "__main__":
    out = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1080, "height": 1440})
        for i, body in enumerate(tiles(), 1):
            h = os.path.join(D, f"_v3_{i}.html")
            open(h, "w", encoding="utf-8").write(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
            pg.goto("file://" + h); pg.wait_for_timeout(500)
            f = os.path.join(D, f"v3-{i}.jpg"); pg.screenshot(path=f, type="jpeg", quality=90); out.append(f)
        b.close()
    W, G = 360, 4
    grid = Image.new("RGB", (3 * W + 2 * G, 3 * 480 + 2 * G), "white")
    for k, f in enumerate(out):
        grid.paste(Image.open(f).resize((W, 480), Image.LANCZOS), ((k % 3) * (W + G), (k // 3) * (480 + G)))
    grid.save(os.path.join(D, "grille-v3-cannelle.jpg"), quality=90)
    print("ok")
