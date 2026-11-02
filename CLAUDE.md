# SOA — atelier de montage des reels

Ce dossier sert à produire en série des reels Instagram / TikTok pour SOA, studio de Pilates Reformer
au 111 avenue du Bac, La Varenne (Saint-Maur-des-Fossés). Compte : @soa.reformer.

## Organisation
- `rushes/` : vidéos brutes du studio (fichiers iPhone, idéalement en 4K). Ne jamais les modifier ni les supprimer.
- `moteur/` : le moteur de montage en motion design.
  - `engine.py` découpe les vidéos en images et compose chaque image dans `stage.html` (textes animés, transitions, zooms, écran partagé, bulles de conversation), puis encode en MP4 1080x1920, 30 i/s, sans son.
  - `reels.py` et `reels2.py` contiennent les montages déjà faits (une fonction par reel). Les extraits sont désignés par le début du nom de fichier (ex. "IMG_6724") et un point de départ en secondes.
- `sortie/` : les reels rendus.

## Lancer un rendu
1. Installer une fois : Python 3, ffmpeg, puis `pip install playwright` et `python -m playwright install chromium`.
2. Rendu d'un reel : `python moteur/reels.py porte` (ou `python moteur/reels2.py local`).
3. Vérifier d'abord quelques images : `python moteur/reels.py porte still 1,4,8`.

## Charte (à respecter dans tous les montages)
- Typo Inter Tight (gras, minuscules) + Instrument Serif italique pour le mot accentué (`*mot*` dans le texte, `~` pour garder plusieurs mots ensemble, `_mot_` pour le doré).
- Couleurs : brun foncé #211B17, crème #F5EFE7, doré #D9B77E. Pas de noir et blanc.
- On tutoie, écriture neutre (« seul·e », « ami·e »), jamais uniquement au féminin.
- Accroche lisible dans la première seconde, coupes toutes les 1,5 à 2,5 s, fin avec l'offre :
  « coaché · digital · hybride » + « pack découverte : 1 coachée + 1 digitale · 36 € » (fonction END()) et @soa.reformer.
- Pas de musique dans le fichier : le son tendance est ajouté dans Instagram / TikTok.
- Ne montrer des visages que de personnes qui ont donné leur accord.

## Demandes types
- « Fais 10 variantes d'accroche du reel porte pour des reels d'essai. »
- « Regarde les nouvelles vidéos de rushes/, fais-en un catalogue et propose 5 reels. »
- « Rends tous les reels de reels2.py dans sortie/. »

## Ce dépôt (soa-medias) — utilisé par l'équipe marketing IA
- `soa-marketing/` : fiches de l'équipe (fondation, voix et charte, équipe, routines) + catalogue des rushes déjà analysés. **À lire avant toute production.**
- `reels/` et `img/` : médias publiés, servis publiquement via
  `https://raw.githubusercontent.com/chahinezbkft-spec/soa-medias/main/<chemin>` → c'est ce lien qu'on donne à Metricool.
- `rushes/` et `sortie/` : dossiers de travail locaux, **jamais commités** (voir .gitignore).
- Rushes : dossier Google Drive « Photos SOA » (id 1pwZH2YeC46nYcLUMIfA063e6qjHWRY6m). Les télécharger dans `rushes/` avec le connecteur Google Drive. Les fichiers de plus de ~10 Mo peuvent échouer : les signaler dans le récap plutôt que bloquer.
- Ne jamais utiliser de contenu personnel du Drive (mariage, photos privées) : uniquement le studio.
- Metricool : marque 6506095, fuseau Europe/Paris. Instagram reel = instagramData.type "REEL" ; carrousel = "POST". TikTok : tiktokData.title obligatoire = la légende TikTok ; autoAddMusic false pour les vidéos, true pour les carrousels photo.
