"""Couvertures de reels SOA (charte v5 cannelle), 1080x1920, titre dans la zone visible de la grille."""
import os, subprocess, glob, sys
from playwright.sync_api import sync_playwright
import base_cannelle as g3
D=g3.D; V=os.path.join(os.path.dirname(D),"soa","rushes","videos")
CAN,CHOC,CAR,CREME=g3.CAN,g3.CHOC,g3.CAR,g3.CREME
CSS=g3.CSS.replace("height:1440px","height:1920px")+f"""
.sans{{display:block;font-family:'Inter Tight';font-weight:700;font-size:118px;letter-spacing:-.05em;line-height:.92;text-transform:lowercase}}
.serif{{display:block;font-family:'Instrument Serif';font-style:italic;font-weight:400;font-size:150px;letter-spacing:-.02em;line-height:.9;margin-top:-6px}}
.h{{position:absolute;left:96px;right:96px}}
.ph{{filter:saturate(.88) sepia(.18) contrast(1.03)}}
.veil{{background:linear-gradient(to bottom,rgba(42,28,22,.30),rgba(42,28,22,.30) 40%,rgba(42,28,22,.82) 80%,rgba(42,28,22,.6))}}
"""
def frame(clip,t):
    out=os.path.join(D,"frames",f"{clip}_{t}.jpg")
    if not os.path.exists(out):
        src=[f for f in glob.glob(os.path.join(V,clip+"*"))][0]
        subprocess.run(["ffmpeg","-v","error","-y","-ss",str(t),"-i",src,"-frames:v","1","-q:v","2",out],check=True)
    return out
def ph(clip,t,sans,serif,lab=None,off=150,pos="50% 45%"):
    lb=f'<div class="lab" style="left:96px;top:330px">{lab}</div>' if lab else ""
    return f'''<div class="t"><img class="ph" src="file://{frame(clip,t)}" style="object-position:{pos}"><div class="veil"></div>{lb}
      <div class="h" style="bottom:640px"><span class="sans">{sans}</span><span class="serif" style="padding-left:{off}px">{serif}</span></div>
      <div class="lab" style="left:96px;bottom:300px">@soa.reformer</div></div>'''
def solid(color,inner): return f'<div class="t solid" style="background:{color}">{inner}</div>'
def solid_title(color,sans,serif,lab,ink=CREME,acc=CAR,off=120,note=None):
    n=f'<div class="hand" style="position:absolute;right:110px;top:1330px;font-size:42px;color:{acc};transform:rotate(-6deg)">{note}</div>' if note else ""
    return solid(color,f'''<div class="lab" style="left:96px;top:330px;color:{acc}">{lab}</div>
      <div class="h" style="top:640px;color:{ink}"><span class="sans" style="font-size:130px">{sans}</span><span class="serif" style="font-size:165px;padding-left:{off}px;color:{acc}">{serif}</span></div>{n}
      <div class="lab" style="left:96px;bottom:300px;color:{ink}">@soa.reformer</div>''')
COVERS={
 "versions": solid(CAN,f'''<div class="lab" style="left:96px;top:330px">daily reminder</div>
    <div class="hand" style="position:absolute;left:96px;right:120px;top:700px;font-size:72px">fais-le le cœur brisé, fais-le en retard, fais-le quand même.</div>
    <div class="lab" style="left:96px;bottom:300px">@soa.reformer</div>'''),
 "porte": ph("IMG_9122",1.5,"ta première séance","chez SOA.",lab="pov",off=200),
 "lets": ph("IMG_3342",0.4,"on teste le pilates","ce soir ?",off=260,pos="40% 45%"),
 "matcha": ph("IMG_9300",1.0,"le rituel","d'après.",lab="18h : reformer · 19h : matcha",off=170,pos="50% 55%"),
 "coachs": ph("IMG_6724",2.0,"ce que ton coach","voit.",off=230),
 "yesbut": ph("IMG_9426",4.5,"yes…","but.",lab="la vraie version",off=160,pos="50% 35%"),
 "hommes": ph("IMG_6822",2.0,"« c'est pas","pour moi. »",off=160),
 "journee": ph("IMG_3062",2.0,"7h → 22h30,","7j/7.",lab="une journée au studio",off=200),
 "outil": ph("IMG_9451",3.2,"l'outil, le carburant,","le travail.",off=120),
 "local": ph("IMG_2206",8.3,"si tu habites à saint-maur,","viens voir.",lab="la varenne",off=140,pos="75% 50%"),
 "checklist": solid_title(CREME,"5 signes que","tu as besoin du reformer.","checklist",ink=CHOC,acc=CAN,off=60,note="combien tu en coches ? ↘"),
 "mythes": ph("IMG_6817",6.0,"3 idées reçues","sur le pilates.",off=120),
 "avant_apres": ph("IMG_6794",1.5,"séance 1","vs séance 10.",off=140),
 "texto": solid_title(CHOC,"le texto de ta pote","à 18h12.","quand tu veux annuler",off=200,note="envoie-lui ↘"),
 "dix": ph("IMG_9420",1.5,"10 exercices,","10 secondes.",off=120),
 "premiere": ph("IMG_4615",0.5,"ta première séance,","étape par étape.",off=80),
 "duo": ph("IMG_3069",1.0,"viens","à deux.",lab="c'est plus fun",off=170),
 "pov_coach": solid_title(CAN,"pov : ton coach dit","« encore 10 ».","pilates reformer",off=80,note="tague ton binôme ↘"),
 "muscu": ph("IMG_6799",2.5,"tu fais de la muscu ?","ajoute ça.",off=200),
}
if __name__=="__main__":
    only=sys.argv[1:] or list(COVERS)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path=g3.CHROME,args=["--allow-file-access-from-files"]); pg=b.new_page(viewport={"width":1080,"height":1920})
        for k in only:
            h=os.path.join(D,"covers",f"_{k}.html"); open(h,"w",encoding="utf-8").write(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{COVERS[k]}</body></html>")
            pg.goto("file://"+h); pg.wait_for_timeout(450); pg.screenshot(path=os.path.join(D,"covers",f"cover-{k}.jpg"),type="jpeg",quality=88)
        b.close()
    print("ok",len(only))
