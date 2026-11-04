# SOA — Brief motion design (reels « classe », pas du texte posé sur une vidéo)

À lire par Tom et Nina (et par Claude Code sur l'ordinateur) avant chaque montage.
Références validées par Chahinez :
- `reels/SOA-demo-classe.mp4` : le style de base (élégant, éditorial) ;
- `reels/SOA-demo-inspi.mp4` : catalogue des effets « signature », tirés de ses vidéos d'inspiration.
`reels/SOA-demo-motion.mp4` est l'ancienne démo jugée « cheap » : à ne PAS imiter.

## Le principe
Un reel SOA doit faire **marque premium**, comme une pub de mode ou de café : calme, éditorial, précis.
- **1 ou 2 effets signature par reel, pas plus.** La démo inspi montre tous les effets ensemble pour voir le style ; un vrai reel en choisit un ou deux qui servent l'idée.
- **Ne jamais cacher un visage** : aucun texte, étiquette, widget ou note posé sur une tête. Placer les éléments au-dessus des têtes ou dans les zones vides, et vérifier sur les images de contrôle pendant toute la durée de l'élément (il bouge).
- Texte aligné à gauche, marges de 96 px ; pas de mise en page centrée « 2020 ».
- Transitions douces par défaut (`dissolve`, `window`, `fade`) ; les effets forts (punch, whip, spin, shake, scale) seulement pour un reel humour, et jamais deux fois de suite.
- Étalonnage chaud sur toutes les vidéos (`grade`), voile chocolat léger, grain discret (`grain` opacity 0.07).

Recette d'un reel de 10 à 15 s :
1. **Accroche (0–2 s)** : lisible en moins d'1 seconde ; idéalement l'effet signature ici (mot derrière la personne, horloge, texte autour d'un objet).
2. **Développement (2–10 s)** : 3 à 5 scènes, coupes toutes les 1,5 à 2,5 s.
3. **Fin (2–3 s)** : « coaché · digital · hybride » ou « découvre les 2 mondes », offre 36 € (étiquette ou cadre), @soa.reformer.
4. **Tempo** : scènes calées sur 120 BPM (paramètre `bpm`) pour que le son ajouté ensuite tombe juste.

## Les effets signature (moteur `moteur/stage.html`)
| Effet | Calque | Quand l'utiliser |
|---|---|---|
| Mot géant **derrière** la personne | `text` style `giant` + `cutout` (même clip, même zoom) par-dessus | Accroche ; plan où une personne bouge devant un fond simple |
| Carnet / scrapbook | `stripes` (fond rayé chocolat) + `card` (vidéo encadrée inclinée) + `note` (papier épinglé : kicker + texte) | Expliquer 2 ou 3 choses (les 2 mondes, ce qu'il y a au studio) |
| Horloge | `clock` (from/to en minutes, ex. 420 → 1350 = 07:00 → 22:30, label) | Horaires, « à ton heure », autonomie |
| Interrupteur iOS | `toggle` (label, s'allume à `at`) | « mode digital », « je réserve », POV |
| Étiquette prix | `pricetag` (kicker, value, sub) qui tombe et se balance | Fin avec l'offre 36 € |
| Texte qui tourne | `circletext` (cx, cy, r, text, speed) | Autour d'un objet : verre de matcha, reformer, logo |
| Mot rempli de vidéo | `cliptext` | Accroche sur aplat cannelle |
| Compteur serif | `counter` style `numserif` | Chiffres : 7 places, 7j/7, 36 € |
| Vidéo dans un cadre | transition `window`, ou `card` | Respiration entre deux plans plein écran |

Autres outils : `panel`, `ticker`, `underline`, `rule`, `bars` (bandes cinéma), `leak`, `bubble` (texto), styles de texte `edito`, `caps`, `numserif`, animations `mask` (par défaut), `track`, `letters`, `type`.
Exemples complets à copier : `moteur/exemples/classe.py` et `moteur/exemples/inspi.py`.

À venir quand l'accueil aura filmé quelqu'un face caméra (avec accord) : sous-titres mot à mot en serif, captures qui apparaissent puis personne en incrustation, même phrase dite dans plusieurs lieux.

## Installation (une fois)
Python 3, ffmpeg, `pip install playwright rembg onnxruntime pillow`, puis `python -m playwright install chromium`.
`rembg` sert à détourer la personne pour l'effet « mot derrière » (le modèle se télécharge au premier usage ; ~3 s par image, prévoir quelques minutes par scène).

## Règles de marque
- Charte v5 « SOA cannelle » (`02-voix-et-charte.md`) : cannelle, chocolat, caramel, crème ; pas de bleu, pas de noir et blanc.
- Typo : Inter Tight grasse + Instrument Serif italique pour le mot émotion ; manuscrit en touche seulement.
- « Pilates » toujours avec un P majuscule. Tutoiement, écriture neutre.
- Des gens à l'image, uniquement des personnes qui ont donné leur accord.
- Pas de musique dans le fichier : Chahinez ajoute le son au moment de publier.

## Prompts prêts à coller dans Claude Code
**Monter un reel à partir d'une idée**
> Lis CLAUDE.md, soa-marketing/07-motion-design.md et 02-voix-et-charte.md. Monte un reel de 12 s sur « [idée / accroche] » avec les vidéos de rushes/, dans le style de moteur/exemples/classe.py. Choisis 1 ou 2 effets signature adaptés à l'idée (pas plus), aucun élément sur un visage, fin avec l'offre. Montre-moi d'abord 6 images de contrôle, puis rends la vidéo dans sortie/.

**Rendre un reel existant plus « classe »**
> Reprends le reel [nom] de moteur/reels2.py et refais-le selon 07-motion-design.md : transitions douces, texte à gauche en mask, étalonnage chaud, grain, et 1 effet signature sur l'accroche. Garde le texte et la durée.

**Décliner une tendance**
> Voici une tendance : [lien ou description]. Adapte-la à SOA en 2 versions de 8 à 10 s selon 07-motion-design.md (une humour, une esthétique), avec les rushes disponibles. Indique pour chacune le type de son à mettre.
