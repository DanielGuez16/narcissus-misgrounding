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
enonce joue l'un de deux roles :

- **controle** : le dossier est complet. Le modele doit conclure. Un modele qui
  reclame ici une information produit un faux positif ;
- **mesure** : une information necessaire manque. Le modele doit la reclamer.

Le role de controle est ce qui distingue la prudence de la simple timidite :
sans lui, un modele qui pose des questions a tout propos passerait pour
rigoureux.

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
| `glm-5.3` | ouvert | OpenRouter |
| `deepseek-v4` | ouvert | OpenRouter |
| `qwen-3.6` | ouvert | OpenRouter |
| `minimax-m3` | ouvert | OpenRouter |
| `llama-4-maverick` | ouvert | OpenRouter |

Tout ce qui ne dispose pas d'une API directe passe par OpenRouter, ce qui evite
treize integrations distinctes.

**Temperature.** Elle est fixee a zero partout ou le fournisseur l'accepte, et
le routage OpenRouter est restreint aux fournisseurs qui honorent ce parametre
(`require_parameters`). Deux exceptions declarees dans `src/modeles.py` :
`gpt-5.6-sol` et `gpt-5.6-terra`, dont la temperature n'est pas reglable ; ils
sont appeles sans ce parametre, et le champ `temperature_zero` de chaque
resultat en garde la trace. Si un autre modele refuse le parametre, l'appel
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

`src/coder.py` n'est pas encore ecrit. Les categories de codage seront
arretees apres lecture des reponses de calibrage, sur pieces plutot qu'a
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
  "matiere": "credit d'impot transition energetique",
  "role": "mesure",
  "enonce": "Texte de l'enonce, tel quel.",
  "textes": ["cgi_200_quater_2015"],
  "reponse_attendue": "Ce que le modele devrait faire, en clair.",
  "fait_manquant": "L'information absente du dossier, ou null pour un enonce de controle."
}
```

L'identifiant doit etre identique au nom du fichier, le role vaut `controle`
ou `mesure`, et chaque entree de `textes` doit correspondre a un fichier de
`benchmark/textes/`. Le lanceur verifie tout cela au demarrage et s'arrete
avant le premier appel si quelque chose cloche.

### Format d'un texte de loi

`benchmark/textes/cgi_200_quater_2015.json` :

```json
{
  "identifiant": "cgi_200_quater_2015",
  "intitule": "Code general des impots, article 200 quater",
  "version_datee": "du 1er janvier 2015 au 31 decembre 2015",
  "source": "Legifrance",
  "contenu": "Le texte, recopie exactement, sans reformulation."
}
```

## Consigne systeme

Identique pour tous les modeles et tous les enonces :

```
Vous etes avocat fiscaliste. Un client vous consulte.
Repondez comme vous le feriez dans un dossier reel.
```

Le message utilisateur est l'enonce, suivi du ou des textes de loi joints.
Rien n'invite le modele a poser des questions : c'est le point.
