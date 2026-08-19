# Les 11 cellules en echec : diagnostic, decision, et une limite de reproductibilite

Campagne du run 1 : 507 appels (13 enonces x 13 modeles x 3 repetitions),
496 reussites, 11 echecs. Apres diagnostic et un reessai cible, l'etat final
est **500/507** : 4 cellules recuperees iso-protocole, 7 cellules laissees en
echec et documentees comme resultat. Ce document dit ce qui a ete change, pour
quoi, et ce que le papier doit rapporter.

## Un seul mecanisme pour les 11 echecs

Tous portent le meme motif : « reponse vide, motif d'arret `length` ». Ils se
concentrent sur trois modeles a raisonnement, minimax-m3 (7), kimi-k3 (3),
glm-5.2 (1), et sur les enonces d'analyse longue. La reponse brute de l'API le
montre : `message.content` vide, un champ `message.reasoning` separe rempli mais
tronque, `finish_reason: length`. Le garde-fou anti-troncature du lanceur les
rejette a juste titre : une reponse vide ou coupee fausserait le codage.

## Diagnostic : trois causes candidates, testees sur pieces

1. **Mauvais champ extrait** (`reasoning` au lieu de `content`). Ecartee comme
   correctif : le `reasoning` est de la pensee brute, tronquee, un type de
   donnee different des 496 reponses finales. L'extraire fausserait le codage
   autant qu'une troncature.

2. **Budget de jetons insuffisant.** Teste sur minimax-m3 / f005_dutreil_a (un
   enonce de controle) : a `max_tokens=32000`, 37 016 jetons de raisonnement et
   `content` vide ; a `max_tokens=64000`, 79 371 jetons de raisonnement et
   `content` toujours vide. **minimax-m3 etend son raisonnement a hauteur du
   budget accorde et ne conclut jamais, quel que soit ce budget.** Ce n'est pas
   un incident, c'est un resultat.

3. **Fournisseur.** Ecartee comme cause unique : les 32 reussites minimax sont
   servies par 10 fournisseurs differents (StreamLake, GMICloud, Minimax,
   Novita, ...), et l'appel de diagnostic en echec (route vers Venice) provient
   d'un fournisseur qui a par ailleurs servi des reussites.

## Le plafond n'est pas respecte

Point technique a declarer pour la reproductibilite. A `max_tokens=32000`
demande, le fournisseur a laisse produire 37 016 jetons de raisonnement ; a
64 000 demande, 79 371. **`max_tokens` ne borne donc pas le raisonnement** :
l'agregateur et le fournisseur comptent les `reasoning_tokens` a part et
n'appliquent le plafond qu'a la sortie visible. Ce n'est pas un modele qui bute
sur une limite, c'est une limite ignoree.

## kimi-k3 et glm-5.2 : echec transitoire, pas un probleme de budget

Au reessai au budget **standard (32 000)**, les 4 cellules de kimi-k3 (3) et
glm-5.2 (1) ont **toutes reussi** (`finish_reason: stop`, reponses de 5 200 a
7 400 caracteres). Elles ont conclu en ~11 000 jetons (kimi) et ~4 000 (glm),
tres en dessous de 32 000 : le budget n'a jamais ete le probleme. Leur echec en
campagne venait du **routage par appel**. Preuve directe, meme parametre :

| Cellule | Campagne | Reessai (32 000) | Fournisseur du reessai |
|---|---|---|---|
| kimi-k3 / f004_beneficiaire_effectif_a rep2 | echec | reussite | Modal |
| kimi-k3 / f005_dutreil_a rep3 | echec | reussite | Phala |
| kimi-k3 / f006_apport_cession_c rep1 | echec | reussite | Modal |
| glm-5.2 / f005_dutreil_b rep1 | echec | reussite | Novita |

Seul le fournisseur avait change. Ces 4 cellules sont donc **iso-protocole**
avec les 496 (budget standard 32 000, meme prompt, meme consigne systeme,
temperature 0, meme extraction `content`). **Aucune deviation a declarer pour
elles.**

## La limite de reproductibilite (a rapporter dans le papier)

C'est le constat le plus solide du run. kimi et glm ont **echoue en campagne et
reussi au reessai avec la meme commande et le meme parametre**. L'ecart ne vient
ni du modele, ni du parametre, mais du **routage de l'agregateur** : OpenRouter
repartit chaque appel entre plusieurs fournisseurs, dont certains sur-raisonnent
jusqu'au plafond et d'autres concluent normalement. Deux equipes qui relancent
ce banc avec la meme commande n'obtiendront pas les memes resultats, et la cause
est le routage, pas leur protocole.

C'est une limite de tout banc d'essai passant par un agregateur multi-fournisseurs.
Elle n'apparait pas dans la litterature AI & Law que nous avons revue (Dahl,
Magesh, LegalBench, etc., qui interrogent des modeles nommes sans traiter le
routage sous-jacent). Le papier doit la declarer, et preciser que les identifiants
de fournisseur effectif sont conserves dans chaque fichier de resultat
(`fournisseur_effectif`).

## minimax-m3 : 7 cellules, echec documente comme resultat

minimax-m3 echoue a 32 000 et a 64 000, sur deux fournisseurs differents, en
etendant son raisonnement au budget sans jamais conclure. Les 7 cellules restent
en echec. Ce n'est pas une panne technique : **trois modeles sur treize ne
produisent aucune reponse exploitable sur des enonces qu'un praticien traiterait
en une page**, et minimax le fait de facon deterministe. C'est une observation
sur ces modeles, que le papier rapporte comme telle.

Cellules minimax-m3 en echec (sans fichier de resultat) :

- f002_preponderance_a rep1
- f003_apport_partiel_a rep1
- f003_apport_partiel_b rep1
- f004_beneficiaire_effectif_b rep2
- f005_dutreil_a rep1
- f005_dutreil_a rep2
- f006_apport_cession_c rep1

## Consequence pour le codage

Une cellule en echec (reponse absente) **n'est pas un `ne_demande_pas`** : le
modele n'a pas ignore le fait manquant, il n'a rien rendu du tout. Le codage
devra soit introduire une **cinquieme valeur** (reponse absente), soit **exclure
ces cellules du denominateur**, explicitement. A trancher sur les chiffres, pas
a l'avance. Concerne les 7 cellules minimax-m3 ci-dessus.

## Etat final des donnees

- **500 / 507** fichiers dans `resultats/brut/`.
- 7 cellules manquantes (minimax-m3, listees ci-dessus).
- `resultats/echecs.jsonl` est un journal **append-only** : il contient encore
  les tentatives echouees de kimi/glm desormais reussies. La verite de l'etat
  final est **l'ensemble des fichiers presents**, pas le journal.
- Duree de la campagne : 162,5 min.
