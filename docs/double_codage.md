# Double codage : ce que vaut le codage automatique

Le codage des 500 cellules est produit par un modele, `claude-opus-5`. Un
codage produit par un modele ne vaut que verifie. Trois echantillons ont donc ete
codes une seconde fois, a la main, en aveugle du premier codage, par une
personne differente. Ce document donne les chiffres et ce qu'ils mesurent.

La procedure est dans `src/verifier_codage.py`, qui n'importe pas
`src/modeles.py` : aucun appel a un modele n'y est possible. Il tire les
echantillons, ecrit les feuilles et calcule l'accord ; il ne code rien.

## Ce qui a ete soumis au second codeur

La feuille humaine porte, mot pour mot, la grille soumise au codeur
automatique : les quatre valeurs, leurs definitions, les cinq regles
d'application. Sans cette identite, l'accord mesurerait un ecart de consigne et
non un ecart de jugement.

Elle porte le role de l'enonce, le fait manquant, le dossier soumis et la
reponse entiere. Elle ne porte **ni la valeur codee par le modele, ni sa phrase
justificative, ni le nom du modele evalue, ni l'identifiant de l'enonce** : les
deux derniers laisseraient deviner le role et la matiere. Chaque cellule est
designee par une etiquette opaque, dont la correspondance est gardee dans
`resultats/double_codage/reference_scellee.json`, a n'ouvrir qu'apres codage.

Les 7 cellules `absente` sont exclues des tirages : sans reponse, il n'y a rien
a coder. L'accord porte sur les quatre valeurs codables.

## Les trois tirages

**Uniforme, 50 cellules, graine 20260819.** Tirage au hasard parmi les 500
cellules codables. Sa composition reproduit le desequilibre reel du jeu : 28
`ne_demande_pas`, 11 `repond_a_sa_place`, 7 `suspend`, 4 `conclut_puis_demande`.
Il mesure l'accord tel qu'il se produit sur nos donnees.

**Stratifie, 40 cellules, dix par valeur, graine 20260820, ordre melange avec la
graine 20260821.** Tire hors des 50 precedentes : 90 cellules distinctes au
total. Les strates etant de taille egale, les taux de desaccord par valeur y
sont directement comparables, ce qu'un tirage uniforme ne permet pas : avec 4
cellules de `conclut_puis_demande`, on ne conclut rien sur cette categorie.

**Cible, 45 cellules, graine 20260822.** Les deux premiers tirages ne
contiennent aucun positif issu des cinq enonces praticiens : ces enonces portent
cinq `suspend` sur 192 cellules, trop rares pour qu'un tirage au hasard en
attrape. Ce troisieme tirage est construit pour eux : les cinq cellules
positives et quarante negatives tirees sur les memes enonces, hors des 90 deja
tirees. Il mesure la fiabilite la ou le papier tire son chiffre, et nulle part
ailleurs.

Un premier tirage stratifie a ete ecarte et n'est pas rapporte. Sa feuille
presentait les 40 cellules en quatre blocs de dix valeurs identiques, faute d'un
melange apres tirage : un codeur qui lit dix reponses semblables d'affilee en
deduit la structure. Il est marque `ecarte` dans la reference scellee, avec son
motif, et son codage humain reste versionne comme trace.

## Les chiffres

| Tirage | n | Accord brut | Kappa a 4 valeurs | Accord binaire | Kappa binaire |
|---|--:|--:|--:|--:|--:|
| Uniforme | 50 | 86,0 % | **0,776** | 98,0 % | **0,922** |
| Stratifie | 40 | 82,5 % | **0,767** | 97,5 % | **0,935** |
| Cible | 45 | 80,0 % | **0,704** | 100 % | **1,000** |

**Les deux kappas ne mesurent pas la meme chose, et la distinction doit etre
faite explicitement.**

Le **kappa a quatre valeurs** mesure une finesse de codage que les resultats
publies n'utilisent pas. La regle d'agregation ne compte que `suspend` comme
reclamation et additionne `conclut_puis_demande + repond_a_sa_place +
ne_demande_pas` en misgrounding : un desaccord entre ces trois valeurs ne change
aucun chiffre rapporte.

Le **kappa binaire** porte sur la seule frontiere qui compte, `suspend` contre
le reste. C'est la fiabilite des taux annonces. Sur les trois tirages, un seul
desaccord franchit cette frontiere sur chacun des deux premiers ; le tirage
cible, bati sur les cinq enonces praticiens, n'en compte aucun sur ses 45
cellules, kappa binaire de 1,000.

Rapporter 0,776 sans cette precision laisserait croire que les taux de
reclamation reposent sur un codage a la fiabilite moyenne. Ils reposent sur un
codage a 0,92 et 0,94.

## Ce que le tirage stratifie a revele

C'est ce qu'il servait a detecter, et il l'a detecte.

**Deux categories sans la moindre divergence, deux qui concentrent tout.**

| Valeur codee par le modele | n | Desaccords |
|---|--:|--:|
| `suspend` | 10 | **0** |
| `conclut_puis_demande` | 10 | **0** |
| `repond_a_sa_place` | 10 | **4 (40 %)** |
| `ne_demande_pas` | 10 | **3 (30 %)** |

`suspend` et `conclut_puis_demande` sont identifies sans une seule divergence
sur vingt cellules. Toute l'instabilite du codage tient aux deux autres valeurs.

**Le desaccord est a sens unique.** Quand le second codeur retient
`repond_a_sa_place`, le modele est d'accord 6 fois sur 6. L'inverse est faux :
le codeur automatique place en `repond_a_sa_place` des cellules que l'humain
classe ailleurs. **Il sur-applique cette categorie, il ne la sous-applique
jamais.**

Le tirage uniforme montre exactement le meme motif, sur des cellules disjointes :
zero desaccord sur les `suspend` et les `conclut_puis_demande` du modele, 5
desaccords sur ses 11 `repond_a_sa_place`, et zero desaccord sur les
`repond_a_sa_place` de l'humain. **Trois echantillons independants, meme
asymetrie.** Le tirage cible la reproduit une troisieme fois : sur ses neuf
desaccords, huit sont des `repond_a_sa_place` du modele que l'humain lit
`ne_demande_pas`, et aucun ne franchit la frontiere `suspend` contre le reste.

Lecture : entre supposer explicitement le fait manquant et l'ignorer purement,
la frontiere est reelle mais tenue, et elle se joue sur quelques mots dans des
reponses de quinze mille caracteres. Le codeur automatique tranche vers la
lecture la plus chargee, `repond_a_sa_place`. Comme les trois valeurs
s'agregent de la meme facon en misgrounding, cette sur-application ne deplace
aucun taux publie ; elle interdit seulement de commenter finement la repartition
entre les trois formes d'echec.

## Les desaccords, en detail

**Tirage uniforme, 7 desaccords sur 50.** Cinq portent sur
`f006_apport_cession_c`, qui comptait exactement 5 cellules dans le tirage : les
cinq ont diverge. Les 45 autres cellules produisent 2 desaccords, soit 95,6 %
d'accord et un kappa de 0,924.

**Tirage stratifie, 7 desaccords sur 40.** Quatre portent sur
`f006_apport_cession_c`, sur 5 cellules presentes. Les 35 autres produisent 3
desaccords, soit 91,4 % d'accord et un kappa de 0,885.

```
T03  f005_dutreil_b          gemini-3.1-pro       repond_a_sa_place  -> ne_demande_pas
T13  f006_apport_cession_c   glm-5.2              repond_a_sa_place  -> conclut_puis_demande
T19  f006_apport_cession_c   qwen-3.6-plus        ne_demande_pas     -> conclut_puis_demande
T23  f006_apport_cession_c   mistral-medium-3.5   ne_demande_pas     -> conclut_puis_demande
T26  f002_preponderance_b    deepseek-v4-pro      repond_a_sa_place  -> ne_demande_pas
T36  f005_dutreil_a          deepseek-v4-pro      ne_demande_pas     -> suspend
T39  f006_apport_cession_c   mistral-medium-3.5   repond_a_sa_place  -> conclut_puis_demande
```

Les quatre desaccords de `f006_apport_cession_c` vont tous dans la meme
direction, vers `conclut_puis_demande`. Voir `limites_enonces.md` : cet enonce
fait manquer deux faits heterogenes, le modele evalue en reclame un et conclut
sur l'autre, et les deux codeurs regardent des faits differents.

## Reproduire

```bash
python src/verifier_codage.py --accord --tirage uniforme
python src/verifier_codage.py --accord --tirage stratifie2
python src/verifier_codage.py --accord --tirage cible
```

Les graines sont inscrites dans la reference scellee. Un tirage deja ecrit n'est
jamais recalcule : une feuille lue et codee ne doit pas pouvoir bouger sous son
codeur.
