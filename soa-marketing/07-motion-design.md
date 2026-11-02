# SOA — Brief motion design (reels « pro », pas du texte posé sur une vidéo)

À lire par Tom et Nina (et par Claude Code sur l'ordinateur) avant chaque montage.
Référence visuelle : `reels/SOA-demo-motion.mp4` (démo des effets).

## Le principe
Un reel SOA doit **bouger comme une pub de marque** : chaque scène a un effet d'entrée, un effet de texte et un élément graphique. Jamais deux scènes de suite avec le même effet. Jamais un texte qui apparaît juste en fondu sur une vidéo fixe.

Recette d'un reel de 10 à 15 s :
1. **Accroche (0–2 s)** : un effet fort tout de suite (mot géant rempli de vidéo, compteur, ouverture en cercle, coup de zoom). Le texte se lit en moins d'1 seconde.
2. **Développement (2–10 s)** : 3 à 5 scènes, coupes toutes les 1,5 à 2,5 s, effets variés, au moins un élément graphique (panneau couleur, bandeau défilant, carte vidéo, soulignement dessiné).
3. **Fin (2–3 s)** : panneau chocolat qui glisse, « coaché · digital · hybride », offre 36 € encadrée, @soa.reformer.
4. **Tempo** : caler les scènes sur 120 BPM (une pulsation tous les 0,5 s, paramètre `bpm`) pour que le son tendance ajouté ensuite tombe juste.

## La boîte à effets du moteur (`moteur/stage.html`)
Transitions d'entrée de scène (`in`) : `cut`, `zoom`, `punch` (coup de zoom), `whip` (glissé rapide flouté), `wipe` (panneau cannelle/chocolat qui balaie, avec `wipeColor`), `iris` (ouverture en cercle), `spin` (rotation + zoom), `up`, `flash`, `fade`.
Transitions de sortie (`out`) : `cut`, `zoom`, `whip`, `wipe`, `fadeblack`.
Options de scène : `bpm` (pulsation au tempo), `shake` (secousse d'impact).

Animations de texte (`anim`) :
- `mask` : les mots montent derrière une ligne (effet éditorial, à utiliser souvent) ;
- `letters` : lettre par lettre avec flou et rotation ;
- `track` : lettres très espacées qui se resserrent (pour les petits repères en capitales) ;
- `swipe` : les mots glissent de gauche en biais ;
- `scale` : rebond élastique (humour, punchlines) ;
- `slam`, `pop`, `words`, `rise`, `fade`, `type` (machine à écrire).

Éléments graphiques (`type` de calque) :
- `cliptext` : mot géant **rempli par la vidéo** (ex. « Pilates » sur aplat cannelle) ;
- `counter` : chiffre qui défile (7 places, 7j/7, 36 €…) ;
- `panel` : aplat de couleur qui glisse (écran partagé, fond de texte, fin) ;
- `card` : vidéo dans une carte inclinée avec bord crème (effet « photo posée ») ;
- `ticker` : bandeau de texte qui défile (« matcha · reformer · … ») ;
- `underline` : trait dessiné à la main sous un mot ;
- `video` avec `box` + `slide` : vidéo en écran partagé qui glisse ;
- `leak` : lumière chaude qui passe ; `grain` : grain pellicule (à mettre sur toutes les scènes) ;
- `bubble` : bulles de conversation (format texto).

## Règles de marque
- Charte v5 « SOA cannelle » (`02-voix-et-charte.md`) : cannelle, chocolat, caramel, crème ; pas de bleu, pas de noir et blanc.
- Typo : Inter Tight grasse + Instrument Serif italique pour le mot émotion ; manuscrit en touche seulement.
- « Pilates » toujours avec un P majuscule. Tutoiement, écriture neutre.
- Des gens à l'image, des personnes qui ont donné leur accord.
- Pas de musique dans le fichier : Chahinez ajoute le son tendance au moment de publier.

## Prompts prêts à coller dans Claude Code
**Monter un reel à partir d'une idée**
> Lis CLAUDE.md, soa-marketing/07-motion-design.md et 02-voix-et-charte.md. Monte un reel de 12 s sur « [idée / accroche] » avec les vidéos de rushes/. Recette : accroche avec un effet fort (cliptext ou counter), 4 scènes aux transitions toutes différentes (iris, whip, wipe, punch), au moins un panneau couleur et un bandeau défilant, fin avec l'offre. Tempo 120 BPM. Montre-moi d'abord 6 images de contrôle, puis rends la vidéo dans sortie/.

**Rendre un reel existant plus « motion design »**
> Reprends le reel [nom] de moteur/reels2.py et refais-le en version motion design selon 07-motion-design.md : change chaque transition, remplace les textes en fondu par des animations mask / letters / swipe, ajoute grain, un panneau cannelle et un soulignement sur le mot clé. Garde le texte et la durée.

**Décliner une tendance**
> Voici une tendance : [lien ou description]. Adapte-la à SOA en 2 versions de 8 à 10 s selon 07-motion-design.md (une humour, une esthétique), avec les rushes disponibles. Indique pour chacune le type de son à mettre.
