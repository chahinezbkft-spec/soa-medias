# SOA — 2 reels d'essai par jour, « ultra tendance »

Objectif : tester beaucoup d'accroches et de formats tendance pour trouver ceux qui font venir des gens de Saint-Maur et alentours. Les gagnants sont ensuite republiés en reel principal.

## Où ils sont publiés
- **TikTok** : 2 reels d'essai par jour, **12h30 et 17h30**.
- **Instagram** : les « reels d'essai » (montrés d'abord aux non-abonnés) ne sont disponibles qu'à partir de 1 000 abonnés. En attendant, on ne publie PAS ces essais sur Instagram (ça noierait le feed). Quand le compte passe 1 000 : même vidéos en type TRIAL_REEL.
- Toujours en **mode notification** (autoPublish false) : Chahinez ajoute le son tendance au moment de publier.

## Étape 1 — Trouver 2 tendances (Inès)
- Recherche web du jour : formats et sons qui montent sur TikTok / Reels (fitness, Pilates, lifestyle, humour du quotidien, « POV », « things that just make sense », « tell me without telling me », listes, avant/après, trends texte à l'écran).
- Ajouter les idées de Chahinez de la Banque d'idées (source « Chahinez ») en priorité.
- Garder seulement les tendances réalisables avec les rushes existants (texte à l'écran + plans du studio) ou demandant un plan très simple à tourner.
- Pour chaque tendance : nom, pourquoi elle marche, adaptation SOA, son conseillé (à chercher par Chahinez dans l'appli).

## Étape 2 — Écrire (Jules)
- Accroche lisible en moins d'1 seconde, 3 à 7 mots, tutoiement, écriture neutre, « Pilates » avec un P majuscule.
- 7 à 12 secondes, coupes rapides, une seule idée, fin : pack découverte 36 € ou « envoie-le à… ».
- Varier : humour, POV, mythe, liste, ASMR matcha, avant/après, local (Saint-Maur / La Varenne).

## Étape 3 — Monter (Tom + Nina)
- Moteur `moteur/` (voir CLAUDE.md), rushes dans `rushes/` (catalogue : `soa-marketing/catalogue-rushes/`).
- Ne pas réutiliser le même plan plus de 2 fois dans la semaine. Si les rushes manquent, le noter dans la liste des scènes à tourner.
- Couverture dans la charte v5 (`soa-marketing/modeles/couvertures_reels.py`).
- Vérifier 3 images par reel avant de valider.

## Étape 4 — Programmer (Sacha)
- Fichiers dans `reels/` et `img/` du dépôt GitHub, push, vérifier les liens (200).
- Metricool (marque 6506095) : TikTok, autoPublish false, tiktokData.title = la légende TikTok, autoAddMusic false, 12h30 et 17h30.
- Ne jamais doubler un créneau déjà pris, ne jamais reprogrammer un contenu déjà publié.

## Étape 5 — Apprendre (Hugo, chaque lundi)
- Classer les essais de la semaine par vues, partages, enregistrements, visites du profil.
- Les 2 meilleurs : refaits en reel principal (Instagram + TikTok) la semaine suivante.
- Les formats qui font moins de la moyenne 2 fois de suite : on arrête.

## Avec Claude Code sur l'ordinateur (optionnel)
Pour monter des rushes lourds (4K, plus de 10 Mo) directement depuis l'ordinateur :
« Lis CLAUDE.md et soa-marketing/06-reels-tendance.md, puis fais les 2 reels d'essai du jour avec les vidéos de rushes/ et mets-les dans sortie/. »
Ensuite, déposer les 2 MP4 de sortie/ dans le dossier Drive « Photos SOA / reels prêts » : la tâche du jour les programme.
