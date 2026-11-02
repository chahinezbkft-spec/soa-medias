"""
Moteur de reels SOA en motion design.
- Les vidéos sont d'abord découpées en images (ffmpeg), recadrées en 1080x1920.
- Chaque image du reel est composée dans une page HTML (vidéo + textes animés + transitions)
  et capturée par Playwright, puis encodée en H.264.
Spécification d'un reel : liste de scènes (voir build_* dans reels.py).
"""
import json, os, subprocess, shutil, math, sys
from playwright.sync_api import sync_playwright

W, H, FPS = 1080, 1920, 30  # sortie verticale Instagram / TikTok
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RUSH = os.path.join(ROOT, "rushes")
CACHE = os.path.join(HERE, "cache")
CHROME = os.environ.get("SOA_CHROME")  # vide = Chromium de Playwright
os.makedirs(CACHE, exist_ok=True)


def find(name):
    for f in os.listdir(RUSH):
        if f.startswith(name):
            return f"{RUSH}/{f}"
    raise FileNotFoundError(name)


def frames(clip, start, dur, speed=1.0, crop=None):
    """Extrait les images d'un extrait, recadrées 9:16 1080x1920. Retourne la liste des fichiers."""
    key = f"{clip}_{start}_{dur}_{speed}_{crop}".replace("/", "_").replace(" ", "")
    d = f"{CACHE}/{key}"
    n = int(round(dur * FPS))
    if os.path.isdir(d) and len(os.listdir(d)) >= n:
        return [f"{d}/{i:04d}.jpg" for i in range(1, n + 1)]
    os.makedirs(d, exist_ok=True)
    src = find(clip)
    vf = []
    if speed != 1.0:
        vf.append(f"setpts=PTS/{speed}")
    if crop:  # crop = "w:h:x:y" en pixels source
        vf.append(f"crop={crop}")
    vf += [f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos", f"crop={W}:{H}", f"fps={FPS}"]
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-i", src, "-t", str(dur / speed if speed != 1 else dur),
                    "-vf", ",".join(vf), "-frames:v", str(n), "-q:v", "3", f"{d}/%04d.jpg"], check=True)
    got = sorted(os.listdir(d))
    files = [f"{d}/{g}" for g in got]
    while len(files) < n:  # complète en répétant la dernière image
        files.append(files[-1])
    return files[:n]


PAGE = open(os.path.join(os.path.dirname(__file__), "stage.html"), encoding="utf-8").read()


def render(spec, out):
    """spec = {"scenes":[{dur, layers:[...]}]} ; rend un mp4 muet."""
    tmp = out + ".part.mp4"
    total = sum(s["dur"] for s in spec["scenes"])
    # pré-extraction des images vidéo
    for s in spec["scenes"]:
        for L in s["layers"]:
            if L["type"] in ("video", "cliptext", "card"):
                L["frames"] = ["file://" + f for f in frames(L["clip"], L.get("start", 0), s["dur"] + L.get("extra", 0), L.get("speed", 1.0), L.get("crop"))]
    html = os.path.join(HERE, "_stage.html")
    open(html, "w", encoding="utf-8").write(PAGE.replace("/*SPEC*/null", json.dumps(spec)))
    nf = int(round(total * FPS))
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", "-movflags", "+faststart", tmp],
                          stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": CHROME} if CHROME else {}), args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto("file://" + html)
        pg.wait_for_function("window.ready === true", timeout=20000)
        for i in range(nf):
            pg.evaluate(f"window.seek({i / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        b.close()
    ff.stdin.close()
    if ff.wait() != 0:
        raise RuntimeError("ffmpeg")
    os.replace(tmp, out)
    return out


def still(spec, t, out):
    """Capture une seule image à l'instant t (pour vérifier avant le rendu complet)."""
    for s in spec["scenes"]:
        for L in s["layers"]:
            if L["type"] in ("video", "cliptext", "card") and "frames" not in L:
                L["frames"] = ["file://" + f for f in frames(L["clip"], L.get("start", 0), s["dur"] + L.get("extra", 0), L.get("speed", 1.0), L.get("crop"))]
    html = os.path.join(HERE, "_stage.html")
    open(html, "w", encoding="utf-8").write(PAGE.replace("/*SPEC*/null", json.dumps(spec)))
    with sync_playwright() as p:
        b = p.chromium.launch(**({"executable_path": CHROME} if CHROME else {}), args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto("file://" + html)
        pg.wait_for_function("window.ready === true", timeout=20000)
        for k, tt in enumerate(t if isinstance(t, list) else [t]):
            pg.evaluate(f"window.seek({tt})")
            pg.screenshot(path=out.replace(".jpg", f"-{k}.jpg"), type="jpeg", quality=88)
        b.close()
