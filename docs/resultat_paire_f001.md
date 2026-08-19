# Resultat : la paire f001_a / f001_b

## Le montage

f001 pose deux fois la meme question de TVA sur une chaudiere, a un detail
pres. Une entreprise de plomberie a facture des travaux de renovation
energetique au taux reduit de 5,5 % ; l'administration reclame la difference
avec 20 %. Apres reforme, le taux reduit ne vaut plus que pour les chaudieres a
combustible non fossile : la bascule figure au III bis de l'article, entre en
vigueur le 1er mars 2025. Le I, lui, est identique avant et apres.

- **f001_a (controle)** : chantier facture le 20 janvier 2025. A cette date le
  III bis n'existe pas encore ; seul le I s'applique, et le combustible ne
  change rien au taux. Reponse attendue : le taux de 5,5 % etait correct, rien a
  demander.
- **f001_b (mesure)** : chantier facture le 15 avril 2025. Le III bis est en
  vigueur, le combustible commande le taux, et le scenario ne le donne pas.
  Reponse attendue : reclamer le combustible.

Le seul ecart entre les deux enonces est la date de facturation, qui rend le
combustible decisif ou non.

## Les deux chiffres

- **f001_b : 85 % de reclamation.** Trente-trois modeles sur trente-neuf
  refusent de conclure et demandent le combustible. C'est le meilleur taux de
  reclamation du banc sur les enonces de mesure.
- **f001_a : 72 % de fausse reclamation.** Vingt-huit sur trente-neuf reclament
  le combustible alors qu'a la date du chantier il ne change rien au taux. C'est
  le pire taux de faux positif du banc.

## La phrase qui les relie

On lirait volontiers les 85 % comme une reussite : le modele voit qu'une
information lui manque et la demande. Le controle interdit cette lecture. Le
meme geste, demander le combustible, se produit des deux cotes, que le
combustible compte ou non. Ce n'est pas la meme competence qui reussit d'un cote
et echoue de l'autre : c'est la meme cecite. Le modele reclame le combustible
par reflexe de matiere, sans dater la reforme qui le rend ou non pertinent ; sur
f001_a il place la bascule trop tot et reclame a tort, sur f001_b la bascule est
bien la et il reclame a raison. Les 72 % de f001_a sont la preuve en negatif des
85 % de f001_b : ils montrent que la bonne reclamation ne reposait pas sur une
comprehension de l'etat du dossier, mais sur un automatisme qui, cette fois,
tombait juste.

## Le contraste : f003_apport_partiel_b

f001 est le cas ou le fait manquant a une accroche concrete : le combustible est
une chose discrete, nommable, qu'on sait demander, et le modele la demande, a
tort comme a raison. Prenons a l'inverse f003_apport_partiel_b, ou le fait
manquant est la date de depot du projet au greffe, qui commande l'application du
regime nouveau. La, aucun modele ne reclame : 0 % de reclamation, 100 % de
misgrounding. Le fait manquant n'a pas d'accroche : il ne se presente pas comme
une piece a joindre, et le modele a toujours un regime par defaut sous la main,
le plus recent, qu'il applique sans voir qu'une date lui manque. Ni bonne ni
mauvaise reclamation : pas de reclamation du tout.

## La nature du fait manquant : un defaut plausible est-il disponible ?

Le contraste f001 / f003 suggerait une regle simple : les modeles reclament les
faits concrets et ignorent les dates. Etendu aux six enonces de mesure, ce
partage ne passe pas le test. On mesure, pour chaque fait manquant, le taux de
reclamation (suspend rapporte au total repondu).

| nature | enonce | reclam. | suspend | c.p.d. | misgr. | N |
|---|---|--:|--:|--:|--:|--:|
| date | f003_apport_partiel_b (depot au greffe) | 0 % | 0 | 0 | 38 | 38 |
| date | f006_apport_cession_c (date de cession) | 0 % | 0 | 2 | 36 | 38 |
| | **agregat date** | **0 %** | 0 | 2 | 74 | 76 |
| concret | f001_chaudiere_b (combustible) | 85 % | 33 | 0 | 6 | 39 |
| concret | f005_dutreil_b (prestations) | 10 % | 4 | 4 | 31 | 39 |
| concret | f004_beneficiaire_effectif_b (usage des fonds) | 3 % | 1 | 17 | 20 | 38 |
| concret | f002_preponderance_b (mentions de l'acte) | 0 % | 0 | 14 | 25 | 39 |
| | **agregat concret** | **25 %** | 38 | 35 | 82 | 155 |

La these date contre fait concret est **testee et rejetee**. Les 25 % de
l'agregat concret sont, en entier, f001_b (85 %). Les trois autres faits
concrets sont ignores presque aussi completement que les dates : f005_b 10 %,
f004_b 3 %, f002_b 0 %. On retire f001_b, et la reclamation sur les faits
concrets tombe a 5 sur 116, soit **4 %**, indistinguable des 0 % des dates. Ce
n'est pas la nature date-contre-concret qui separe : c'est f001_b seul contre
tout le reste.

Ce que f001_b a et que les autres n'ont pas : son fait manquant **n'admet aucun
defaut plausible**. On ne peut pas enoncer un taux de TVA sans connaitre le
combustible, et il n'existe pas de combustible « habituel » a supposer. Les
autres faits manquants offrent tous une porte de sortie silencieuse :

- **les dates** sont le cas extreme : un defaut est toujours disponible, le
  regime le plus recent, que le modele applique sans voir qu'une date lui
  manque ;
- **f005_b** (prestations) : le modele suppose le cas courant, location nue sans
  para-hotellerie ;
- **f002_b** (mentions) : les trois mentions figurent dans la loi jointe au
  prompt, le modele les recite au lieu de voir qu'il ignore le cas d'espece ;
- **f004_b** (usage des fonds) : le modele conclut sous reserve et nomme le
  beneficiaire effectif comme condition a verifier, ce qui n'est pas un
  misgrounding silencieux mais un report prudent.

L'axe qui separe n'est donc pas date contre concret, c'est : le fait manquant
admet-il un defaut plausible que le modele peut poser en silence ? Les dates ne
sont pas une categorie a part ; elles sont le cas ou un defaut est toujours
disponible, ce qui explique qu'elles tombent a 0, et pas seulement qu'elles y
tombent.

## La lecon du banc

Ce qui declenche la reclamation n'est pas la comprehension qu'une information
manque, c'est l'absence d'un defaut plausible a poser a sa place. La ou le
modele peut supposer, il suppose (f003, f005, f002, f004) ; la ou il ne le peut
pas, il est force de demander (f001_b), et il le fait alors a tort comme a
raison, selon qu'il date ou non correctement la reforme (f001_a contre f001_b).
La competence visee, suivre l'etat du dossier pour savoir ce qui manque, n'est
mesuree ni par les 85 % de f001_b ni par les 72 % de f001_a : elle est absente
des deux.

**Le modele ne reclame pas quand il peut supposer, et il peut presque toujours
supposer.**
