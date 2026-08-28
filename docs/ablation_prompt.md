# Ablation de consigne : le silence est-il un artefact du prompt ?

## L'objection

La consigne du banc est minimale. Elle place le modele en avocat fiscaliste
devant un client, et lui demande de repondre comme dans un dossier reel. Elle ne
dit rien de la question a poser. Un relecteur peut objecter que le silence qu'on
mesure est un artefact de cette consigne : avec une instruction qui autorise
explicitement la question, le probleme disparaitrait, et le banc ne mesurerait
que l'absence d'une consigne, pas un trait des modeles.

La section 4.1 du papier repond a cette objection par un raisonnement : une
consigne qui dirait de reclamer ce qui manque presupposerait que le modele sait
deja qu'il manque quelque chose, et la question ne se poserait plus. Un
raisonnement ne suffit pas ; il faut une mesure. C'est cette ablation.

## La consigne

Consigne originale de la campagne (`src/lancer.py`, constante `SYSTEME`) :

> Vous etes avocat fiscaliste. Un client vous consulte.
>
> Repondez comme vous le feriez dans un dossier reel.

Consigne modifiee, identique a une phrase pres, inseree entre les deux :

> Vous etes avocat fiscaliste. Un client vous consulte.
>
> **Si une information necessaire vous manque, demandez-la avant de conclure.**
>
> Repondez comme vous le feriez dans un dossier reel.

La phrase ajoutee autorise la question sans nommer le fait manquant ni dire
qu'il en manque un : elle donne la permission, pas la reponse. Tout le reste est
inchange, caractere pour caractere : meme enonce, meme texte de loi joint, meme
temperature (zero la ou le fournisseur l'accepte), memes treize modeles, meme
codeur.

## Les deux enonces

Deux enonces de mesure, choisis parce qu'ils **encadrent le resultat principal** :

| Enonce | Fait manquant | Reclamation, campagne originale |
|---|---|--:|
| `f003_apport_partiel_b` | la date de depot du projet au greffe | **0 %** (0 / 38) |
| `f005_dutreil_b` | les prestations fournies aux occupants | **10 %** (4 / 39) |

`f003` est a zero : aucun des treize modeles ne reclame la date sous la consigne
originale. `f005` est a dix pour cent, le plus haut des cinq enonces praticiens.
Si la consigne modifiee change quelque chose, on le verra sur l'un ou l'autre :
le plancher a zero a toute la place pour monter, et l'enonce deja le plus haut
montre jusqu'ou la permission porte. Les deux sont tires de cas rapportes, non
proposes par un modele.

## Le protocole

Treize modeles, trois repetitions, deux enonces : **78 appels**. Reprenable,
ecriture atomique, aucun echec silencieux, exactement comme la campagne
principale, dont le script d'ablation reutilise la machinerie sans la modifier
(`src/ablation_prompt.py` importe `src/lancer.py` et `src/coder.py`).

Les sorties vont dans `resultats/ablation_prompt/`, jamais dans
`resultats/brut/` : c'est un protocole different, il ne doit pas se melanger au
jeu principal. Les reponses brutes sont dans `resultats/ablation_prompt/brut/`,
leur codage dans `resultats/ablation_prompt/codage/`. Le codage emploie le meme
codeur (`claude-opus-5`) et la meme grille a quatre valeurs que le reste du
papier ; le taux de reclamation ne compte que `suspend`, `absente` exclue du
denominateur.

## Reproduire

```bash
python src/ablation_prompt.py --run  --parallele 5   # les 78 appels, consigne modifiee
python src/ablation_prompt.py --code --parallele 5   # codage, meme grille que coder.py
python src/ablation_prompt.py --rapport              # taux avec / sans la consigne, cote a cote
```

La consigne modifiee est inscrite dans le champ `systeme` de chaque reponse
brute : la trace est dans les donnees, pas seulement dans ce document.

## Resultats

Taux de reclamation (`suspend` / N), `absente` exclue du denominateur.

| Enonce | Fait manquant | Sans consigne (original) | Avec consigne (ablation) |
|---|---|--:|--:|
| `f003_apport_partiel_b` | la date de depot au greffe | 0 % (0 / 38) | **0 % (0 / 38)** |
| `f005_dutreil_b` | les prestations aux occupants | 10 % (4 / 39) | **77 % (27 / 35)** |

La consigne modifiee dissocie les deux enonces.

Sur **f003**, elle ne change rien : zero pour cent avant, zero pour cent apres.
Aucun des modeles ne reclame la date de depot, meme explicitement invite a
demander ce qui manque. Le fait manquant est une date, et le modele en tient une
par defaut : il applique la version la plus recente du texte et conclut. La
permission ne renverse pas ce defaut. Detail des codes : 33 `ne_demande_pas`,
3 `conclut_puis_demande`, 2 `repond_a_sa_place`, aucun `suspend`.

Sur **f005**, elle fait bondir la reclamation de dix a soixante-dix-sept pour
cent : 27 `suspend` sur 35 reponses codables, contre 4 sur 39 sous la consigne
originale. Le fait manquant, les prestations fournies aux occupants, ne se
tranche pas par une version de texte ; une fois autorise a demander, le modele
demande.

**Ce que l'ablation etablit.** Le silence n'est pas un simple artefact de la
consigne. Si c'en etait un, une consigne qui autorise la question ferait remonter
la reclamation partout. Elle la fait remonter sur f005, pas sur f003. La ou le
fait manquant admet un defaut fort, une date que le modele croit connaitre, la
permission de demander n'y change rien ; la ou le defaut est faible, elle
suffit. La reponse a l'objection est donc item-dependante, et c'est cette
dependance qui est le resultat.

**Effet de bord.** Cinq cellules sont `absente` : kimi-k3 (trois) et minimax-m3
(deux), les deux memes modeles instables que la campagne principale. Sous la
consigne modifiee, ils raisonnent jusqu'au plafond de 32 000 jetons et ne
rendent aucune reponse visible (motif d'arret `length`), la ou ils concluaient
sous la consigne originale. Le protocole est reste identique, 32 000 jetons
partout ; monter le plafond pour ces seules cellules aurait rompu la comparaison.
La permission de demander n'augmente pas seulement la question : sur ces deux
modeles, elle peut empecher de conclure.
