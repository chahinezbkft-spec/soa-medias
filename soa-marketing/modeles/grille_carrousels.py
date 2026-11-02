"""Grille v4 : palette cannelle + typo v1 (Inter Tight / Instrument Serif), manuscrit en accent, aplats placés librement."""
import os
from playwright.sync_api import sync_playwright
from PIL import Image
import base_cannelle as g3
D=g3.D; P=g3.P
CAN,CHOC,CAR,CREME=g3.CAN,g3.CHOC,g3.CAR,g3.CREME
CSS=g3.CSS+f"""
.sans{{display:block;font-family:'Inter Tight';font-weight:700;font-size:118px;letter-spacing:-.05em;line-height:.92;text-transform:lowercase}}
.serif{{display:block;font-family:'Instrument Serif';font-style:italic;font-weight:400;font-size:150px;letter-spacing:-.02em;line-height:.9;margin-top:-6px}}
.h{{position:absolute;left:96px;right:96px}}
.tag{{display:inline-block;background:{CAR};color:{CHOC};font-family:'Inter Tight';font-weight:500;font-size:28px;padding:6px 16px;transform:rotate(-4deg);margin-bottom:26px}}
.ph{{filter:saturate(.88) sepia(.18) contrast(1.03)}}
.veil{{background:linear-gradient(to bottom,rgba(42,28,22,.30),rgba(42,28,22,.30) 35%,rgba(42,28,22,.82))}}
"""
def ph(img,sans,serif,tag=None,pos="50% 45%",off=150,lab=None):
    tg=f'<span class="tag">[ {tag} ]</span><br>' if tag else ""
    lb=f'<div class="lab" style="left:96px;top:96px">{lab}</div>' if lab else ""
    return g3.photo(img,f'''{lb}<div class="h" style="bottom:200px">{tg}<span class="sans">{sans}</span><span class="serif" style="padding-left:{off}px">{serif}</span></div>
      <div class="lab" style="left:96px;bottom:96px">@soa.reformer</div>''',pos=pos)
J=lambda f:os.path.join(D,f); Q=lambda f:os.path.join(P,f)
T=[
 ph(J("r-hyb.jpg"),"les 2 mondes","de SOA.",tag="nouveau",pos="50% 30%",lab="coaché · digital · hybride"),
 g3.solid(CAN,f'''<div class="lab" style="left:96px;top:96px">daily reminder</div>
   <div class="hand" style="position:absolute;left:96px;right:120px;top:420px;font-size:70px">fais-le le cœur brisé, fais-le en retard, fais-le quand même.</div>
   <div class="lab" style="left:96px;bottom:96px">@soa.reformer</div><div class="lab" style="right:96px;bottom:96px">novembre</div>'''),
 ph(Q("5C21792C-01D9-4A15-A97B-FEBD50F71995.jpg"),"pourquoi les sportifs","s'y mettent.",tag="pédagogie",off=110),
 ph(J("r-coach.jpg"),"ce que ton coach","voit.",pos="50% 45%",off=230),
 g3.photo(J("r-matcha.jpg"),f'''<div class="lab" style="left:96px;top:96px">18h : reformer · 19h : matcha</div>
   <div class="h" style="bottom:200px"><span class="sans">le rituel</span><span class="serif" style="padding-left:170px">d'après.</span></div>
   <div class="lab" style="left:96px;bottom:96px">@soa.reformer</div>''',pos="50% 55%"),
 g3.solid(CREME,f'''<div class="lab" style="left:96px;top:96px;color:{CAN}">c'est maintenant</div>
   <div class="h" style="top:430px;color:{CHOC}"><span class="sans" style="font-size:130px">un rythme,</span><span class="serif" style="font-size:165px;padding-left:120px;color:{CAN}">pas une résolution.</span>
   <p style="font-family:'Inter Tight';font-size:36px;line-height:1.4;margin-top:60px;max-width:700px">Coaché, digital ou les deux : tu construis ta semaine, on s'occupe du reste.</p></div>
   <div class="lab" style="left:96px;bottom:96px;color:{CHOC}">@soa.reformer</div>'''),
 g3.solid(CHOC,f'''<div class="lab" style="left:96px;top:96px;color:{CAR}">on l'entend souvent</div>
   <div class="h" style="top:470px"><span class="serif" style="font-size:150px;color:{CAR}">« c'est pas pour moi. »</span>
   <span class="sans" style="font-size:150px;margin-top:40px">spoiler :<br>si.</span></div>
   <div class="hand" style="position:absolute;right:110px;bottom:200px;font-size:40px;color:{CAR};transform:rotate(-6deg)">viens voir ↘</div>
   <div class="lab" style="left:96px;bottom:96px">@soa.reformer</div>'''),
 ph(Q("534A03E5-09DF-4225-8EFD-FA4BB2C9AEEE.jpg"),"le pilates,","et tout le reste.",off=90,lab="la communauté soa"),
 g3.photo(J("r-rires.jpg"),f'''<div class="lab" style="left:96px;top:96px">pack découverte</div>
   <div class="h" style="bottom:300px"><span class="sans">découvre</span><span class="serif" style="padding-left:120px">les 2 mondes.</span></div>
   <div style="position:absolute;left:96px;bottom:180px;border:1.5px solid {CREME};padding:14px 30px;font-family:'Inter Tight';font-size:28px;letter-spacing:.12em;text-transform:uppercase">1 coachée + 1 digitale · 36 €</div>
   <div class="lab" style="left:96px;bottom:96px">@soa.reformer · lien en bio</div>''',pos="50% 45%"),
]
out=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=g3.CHROME,args=["--allow-file-access-from-files"]); pg=b.new_page(viewport={"width":1080,"height":1440})
    for i,body in enumerate(T,1):
        h=os.path.join(D,f"_v4_{i}.html"); open(h,"w",encoding="utf-8").write(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
        pg.goto("file://"+h); pg.wait_for_timeout(500); f=os.path.join(D,f"v5-{i}.jpg"); pg.screenshot(path=f,type="jpeg",quality=90); out.append(f)
    b.close()
W,G=360,4; grid=Image.new("RGB",(3*W+2*G,3*480+2*G),"white")
for k,f in enumerate(out): grid.paste(Image.open(f).resize((W,480),Image.LANCZOS),((k%3)*(W+G),(k//3)*(480+G)))
grid.save(os.path.join(D,"grille-v5.jpg"),quality=90); print("ok")
