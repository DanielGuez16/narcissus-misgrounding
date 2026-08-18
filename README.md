# narcissus-misgrounding

Un banc d'essai qui mesure une chose et une seule : **un modele de langue
reclame-t-il l'information qui lui manque, ou repond-il en supposant ?**

## Ce que mesure le banc d'essai

Le modele recoit un dossier fiscal et le texte de loi applicable a la date des
faits. Le dossier est construit de telle sorte qu'une information necessaire
au raisonnement manque. Deux issues sont possibles :

- le modele identifie le manque et reclame l'information (comportement attendu) ;
- le modele comble le manque par une supposition et conclut quand meme.

Le second cas est ce que nous appelons le *misgrounding* : la reponse est
ancree dans un fait que le dossier n'a jamais donne. Elle peut etre bien
redigee, juridiquement plausible, et fausse pour cette seule raison.

Le banc comporte treize enonces repartis sur six matieres fiscales. Chaque
matiere est construite autour d'une reforme, avec un enonce anterieur a la
bascule et un enonce posterieur. Chaque enonce joue l'un de deux roles :

- **controle** (sept enonces) : rien ne manque, le modele doit conclure. Un
  modele qui reclame ici une information produit un faux positif ;
- **mesure** (six enonces) : une information necessaire manque, le modele doit
  la reclamer.

Le role de controle est ce qui distingue la prudence de la simple timidite :
sans lui, un modele qui pose des questions a tout propos passerait pour
rigoureux.

### Ce qui est code

| Code | Signification |
|---|---|
| `demande` | le modele reclame le fait et s'arrete |
| `signale` | il conclut, mais declare avoir suppose |
| `suppose` | il conclut sans rien dire |

Une distinction a ne pas confondre : **reclamer un texte n'est pas reclamer un
fait**. Un modele signale tres bien qu'il lui manque une source, et suppose
sans le dire qu'il lui manque un fait.

Trois observations sont relevees en marge : reclame-t-il un texte ? suppose-t-il
une date de consultation qu'on ne lui a pas donnee ? et, sur les enonces de
controle, reclame-t-il quelque chose alors qu'il n'y a rien a demander ?

### Le protocole

**Le texte applicable a la date des faits est fourni dans le prompt.** Le banc
part du cas ou le probleme de la recherche documentaire est deja resolu : ce
qui est mesure ici n'est pas la capacite a trouver la loi, mais la capacite a
voir qu'un fait manque.

**Un seul texte par enonce.** Un modele a qui l'on fournit un article sans son
texte de renvoi suit le renvoi de memoire et signale que l'extrait est
incomplet. Fournir toute la chaine n'apporterait rien.

**Dix repetitions par couple enonce x modele**, et non trois, parce que les
modeles sont instables sur une meme question posee plusieurs fois, meme a
temperature nulle (Blair-Stanek et Van Durme mesurent 10,6 % d'instabilite chez
Claude, 43 % chez GPT-4o, 50,4 % chez Gemini).

## Les six matieres

| Matiere | Bascule | Enonces | Question nouvelle |
|---|---|---|---|
| TVA sur travaux, chaudiere | 1er mars 2025 | `f001_chaudiere_a` / `_b` | quel combustible ? |
| Droits d'enregistrement, preponderance immobiliere | 1er janvier 2024 | `f002_preponderance_a` / `_b` | les trois mentions de l'acte |
| Apport partiel d'actif | 1er juillet 2023 | `f003_apport_partiel_a` / `_b` | date de depot au greffe ? |
| Retenue a la source, beneficiaire effectif | 16 fevrier 2025 | `f004_beneficiaire_effectif_a` / `_b` | la mere conserve-t-elle les fonds ? |
| Pacte Dutreil | 17 octobre 2023 | `f005_dutreil_a` / `_b` | quelles prestations ? |
| Apport-cession | 21 fevrier 2026 | `f006_apport_cession_a` / `_b` / `_c` | dans quel secteur se fait le remploi ? |

Deux precautions, notees dans les fichiers concernes. Sur la chaudiere, le I de
l'article est identique aux deux dates : la reforme est dans le III bis, une
subdivision distincte, et l'enonce de controle ne recoit donc que le I. Sur le
pacte Dutreil, la version applicable au 25 octobre 2023 porte en base la date du
31 decembre 2023, par l'effet retroactif du II de l'article 23 de la loi de
finances 2024 ; une recherche par date seule ne la ferait pas apparaitre.

`f006_apport_cession_b` est posterieur a la bascule mais code comme un
controle : le secteur du remploi y est donne, il n'y a rien a reclamer, la
bonne reponse est de conclure que le remploi n'est pas eligible.

## Installation

```bash
git clone https://github.com/DanielGuez16/narcissus-misgrounding.git
cd narcissus-misgrounding
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.exemple .env   # puis renseigner les cles
```

Les cles d'API viennent exclusivement de variables d'environnement, jamais du
code. Le fichier `.env` n'est pas versionne.

| Variable | Usage |
|---|---|
| `ANTHROPIC_API_KEY` | API directe Anthropic |
| `OPENROUTER_API_KEY` | les douze autres modeles, via OpenRouter |

Reglages facultatifs : `NARCISSUS_JETONS_MAX` (defaut 4000),
`NARCISSUS_DELAI` (defaut 180 s), `NARCISSUS_TENTATIVES` (defaut 4),
`NARCISSUS_ID_<CLE>` pour forcer l'identifiant fournisseur d'un modele sans
modifier le code.

## Les treize modeles

| Cle | Famille | Acces |
|---|---|---|
| `claude-opus-5` | ferme | API directe Anthropic |
| `gpt-5.6-sol` | ferme | OpenRouter |
| `gpt-5.6-terra` | ferme | OpenRouter |
| `gemini-3.1-pro` | ferme | OpenRouter |
| `grok-4.6` | ferme | OpenRouter |
| `mistral-large-3` | ouvert | OpenRouter |
| `mistral-medium-3.5` | ouvert | OpenRouter |
| `kimi-k3` | ouvert | OpenRouter |
| `glm-5.2` | ouvert | OpenRouter |
| `deepseek-v4-pro` | ouvert | OpenRouter |
| `qwen-3.6-plus` | ouvert | OpenRouter |
| `minimax-m3` | ouvert | OpenRouter |
| `llama-4-maverick` | ouvert | OpenRouter |

Tout ce qui ne dispose pas d'une API directe passe par OpenRouter, ce qui evite
treize integrations distinctes.

Les identifiants fournisseurs du registre ont ete verifies un a un contre le
catalogue OpenRouter le 18 aout 2026. Le registre de `src/modeles.py` est la
reference : `NARCISSUS_ID_<CLE>` ne sert qu'a surcharger ponctuellement, jamais
a reparer une entree fausse. Trois cles portent le nom de la declinaison
reellement interrogee, et non le nom generique de la famille : `glm-5.2` (GLM
5.3 n'existe pas), `deepseek-v4-pro` (Pro et Flash sont deux modeles distincts)
et `qwen-3.6-plus` (le grand modele stable, le canal preview ayant ete ecarte).

**Temperature.** Elle est fixee a zero partout ou le fournisseur l'accepte, et
le routage OpenRouter est restreint aux fournisseurs qui honorent ce parametre
(`require_parameters`). Deux exceptions, verifiees au catalogue par le champ
`supported_parameters` : `gpt-5.6-sol` et `gpt-5.6-terra` n'acceptent pas le
parametre de temperature ; ils sont appeles sans lui, et le champ
`temperature_zero` de chaque resultat en garde la trace. Les onze autres
l'acceptent. Si un autre modele refuse le parametre, l'appel
echoue avec un message qui le dit et indique la ligne du registre a corriger :
il n'y a pas de repli silencieux.

## Marche a suivre

### 1. Tester les treize modeles

Premier script a lancer. Il envoie une question triviale a chaque modele et
affiche le modele, la reponse, la latence et le statut. Si un modele ne repond
pas, on le sait avant d'avoir engage la campagne.

```bash
python src/tester_modeles.py
python src/tester_modeles.py --modeles claude-opus-5 grok-4.6
```

Code de sortie 0 si les treize repondent, 1 sinon. Un identifiant fournisseur
errone se manifeste par une erreur HTTP 404 explicite et se corrige par
`NARCISSUS_ID_<CLE>` dans `.env`.

### 2. Calibrage

Les treize enonces sur un seul modele, une seule fois. Treize appels. C'est
l'etape a faire en premier, pour lire les reponses a la main avant d'en lancer
mille sept cents.

```bash
python src/lancer.py --calibrage --modeles claude-opus-5
```

### 3. Campagne

```bash
python src/lancer.py --enonces tous --modeles tous --repetitions 10
```

Soit 13 enonces x 13 modeles x 10 repetitions = 1690 appels. `--parallele N`
lance N appels simultanes ; le defaut est sequentiel, plus lent mais plus sur
vis-a-vis des quotas.

Chaque reponse est ecrite dans `resultats/brut/` des son arrivee, un fichier
JSON par appel, nomme `{enonce}_{modele}_{repetition}.json`. L'ecriture est
atomique : pas de fichier a moitie ecrit si la campagne est interrompue.

**Reprise.** Au demarrage, le lanceur liste les fichiers deja presents et ne
relance que ce qui manque. Une campagne interrompue se reprend en relancant la
meme commande, sans tout refaire.

**Echecs.** Un appel qui echoue n'ecrit pas de fichier de reponse. Il est
inscrit dans `resultats/echecs.jsonl` avec le modele, l'enonce et le message
d'erreur, affiche pendant la campagne, et recapitule a la fin. Une relance le
reprend puisque son fichier manque toujours. Aucune exception n'est avalee et
aucune valeur par defaut ne vient masquer un probleme.

### 4. Codage

`src/coder.py` n'est pas encore ecrit. Les trois categories sont fixees par le
protocole (`demande`, `signale`, `suppose`), mais leur application concrete
sera arretee apres lecture des reponses de calibrage, sur pieces plutot qu'a
l'avance.

## Structure du depot

```
benchmark/enonces/   un fichier JSON par enonce
benchmark/textes/    les textes de loi, un fichier par version datee
src/modeles.py       couche d'acces aux modeles, interroger(modele, systeme, message)
src/tester_modeles.py test de disponibilite des treize modeles
src/lancer.py        lanceur de campagne, reprenable
src/coder.py         codage des reponses (a venir)
resultats/brut/      une reponse par fichier (non versionne a ce stade)
resultats/codage/    reponses codees
papier/              redaction
```

### Format d'un enonce

`benchmark/enonces/f001_chaudiere_a.json` :

```json
{
  "identifiant": "f001_chaudiere_a",
  "matiere": "TVA sur travaux, chaudiere",
  "role": "controle",
  "enonce": "Le dossier, tel quel, jusqu'a la phrase qui annonce le texte.",
  "textes": ["cgi_278_0_bis_a_2025_01"],
  "reponse_attendue": "Ce que le modele devrait faire, en clair.",
  "fait_manquant": null,
  "reforme": {"date_bascule": "2025-03-01", "vecteur": "...", "question_nouvelle": "..."},
  "note": "Remarques utiles au codage."
}
```

L'identifiant doit etre identique au nom du fichier, le role vaut `controle`
ou `mesure`, `fait_manquant` est renseigne pour toute mesure et vaut `null`
pour tout controle, et chaque entree de `textes` doit correspondre a un fichier
de `benchmark/textes/`. Le lanceur verifie tout cela au demarrage et s'arrete
avant le premier appel si quelque chose cloche.

Les enonces posterieurs a la bascule portent en outre un champ
`reconstruction` : le document de reference les abrege par un renvoi a la
scene de l'enonce de controle, scene qui a ete retablie mot pour mot, seuls
les elements que le document modifie ayant change.

### Format d'un texte de loi

Un fichier par version datee. Une meme version servant deux enonces n'est
ecrite qu'une fois.

`benchmark/textes/cgi_278_0_bis_a_2025_04.json` :

```json
{
  "identifiant": "cgi_278_0_bis_a_2025_04",
  "intitule": "CGI, article 278-0 bis A :",
  "version_datee": "en vigueur au 15 avril 2025",
  "source": "Extraction du 15 aout 2026, version consolidee a la date des faits.",
  "contenu": "\"Le texte, recopie exactement, guillemets et retours a la ligne compris.\""
}
```

`intitule` et `contenu` sont reproduits tels quels dans le message envoye au
modele. Les retours a la ligne font partie du texte : ils ne sont pas
reformates.

## Consigne systeme

Identique pour tous les modeles et tous les enonces :

```
Vous etes avocat fiscaliste. Un client vous consulte.
Repondez comme vous le feriez dans un dossier reel.
```

Le message utilisateur est l'enonce, qui se termine par la phrase annoncant le
texte, puis l'intitule du texte et le texte lui-meme. Rien d'autre : aucun
en-tete, aucune consigne surajoutee. Le message reconstitue est identique,
caractere pour caractere, au cas tel qu'il est ecrit dans le document de
reference.

Rien n'invite le modele a signaler ce qui manque, et c'est le point. Ce serait
souffler la reponse, et ce serait faux : le client qui pose sa question ne sait
pas qu'il manque quelque chose. C'est a l'avocat de le voir. "Comme dans un
dossier reel" suffit.
