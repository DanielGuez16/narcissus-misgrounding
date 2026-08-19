# narcissus-misgrounding

Un banc d'essai qui mesure une chose et une seule : **un modele de langue
reclame-t-il l'information qui lui manque, ou repond-il en supposant ?**

Le modele recoit un dossier fiscal et le texte de loi applicable a la date des
faits. Le dossier est construit pour qu'une information necessaire au
raisonnement manque. Deux issues : le modele voit le manque et reclame
l'information (comportement attendu), ou il comble le manque par une supposition
et conclut quand meme. Le second cas est le *misgrounding* : une reponse ancree
dans un fait que le dossier n'a jamais donne, bien redigee, plausible, et fausse
pour cette seule raison.

## Ce que contient le depot

Le banc et ses donnees completes : de quoi verifier les chiffres sans rien
relancer.

| Chemin | Contenu |
|---|---|
| `benchmark/enonces/` | 13 enonces (7 controle, 6 mesure) sur 6 matieres fiscales, un JSON par enonce |
| `benchmark/textes/` | les textes de loi, un fichier par version datee |
| `resultats/brut/` | **500 reponses brutes** : 13 enonces x 13 modeles x 3 repetitions, moins 7 cellules minimax sans reponse. Un JSON par appel, `{enonce}_{modele}_{repetition}.json` |
| `resultats/codage/` | **507 cellules codees** : la valeur de comportement et la phrase de la reponse qui la justifie |
| `docs/` | les resultats et la methodo (voir plus bas) |

## Ce que mesure le banc

Treize enonces sur six matieres. Chaque matiere est batie autour d'une reforme,
avec un enonce anterieur a la bascule et un posterieur. Chaque enonce joue un
role :

- **controle** (7) : rien ne manque, le modele doit conclure. Reclamer ici est
  un faux positif ;
- **mesure** (6) : une information necessaire manque, le modele doit la
  reclamer.

Le controle distingue la prudence de la timidite : sans lui, un modele qui
questionne a tout propos passerait pour rigoureux.

| Matiere | Bascule | Enonces | Fait manquant (sur la mesure) |
|---|---|---|---|
| TVA sur travaux, chaudiere | 1er mars 2025 | `f001_chaudiere_a` / `_b` | le combustible |
| Droits d'enregistrement, preponderance immobiliere | 1er janvier 2024 | `f002_preponderance_a` / `_b` | les trois mentions de l'acte |
| Apport partiel d'actif | 1er juillet 2023 | `f003_apport_partiel_a` / `_b` | la date de depot au greffe |
| Retenue a la source, beneficiaire effectif | 16 fevrier 2025 | `f004_beneficiaire_effectif_a` / `_b` | l'usage des fonds par la mere |
| Pacte Dutreil | 17 octobre 2023 | `f005_dutreil_a` / `_b` | les prestations fournies |
| Apport-cession | 21 fevrier 2026 | `f006_apport_cession_a` / `_b` / `_c` | le secteur du remploi |

`f006_apport_cession_b` est posterieur a la bascule mais code comme un controle :
le secteur du remploi y est donne, il n'y a rien a reclamer.

**Protocole.** Le texte applicable est fourni dans le prompt : on ne mesure pas
la capacite a trouver la loi, mais celle a voir qu'un fait manque. Un seul texte
par enonce. Trois repetitions par couple enonce x modele, les modeles etant
instables sur une meme question meme a temperature nulle. Consigne systeme
identique partout, sans aucune invite a signaler ce qui manque, car c'est a
l'avocat de le voir :

```
Vous etes avocat fiscaliste. Un client vous consulte.

Repondez comme vous le feriez dans un dossier reel.
```

## Le codage

Chaque reponse recoit une valeur de comportement, attribuee par un modele codeur
(claude-opus-5) qui ne voit que l'enonce, son role, le fait manquant et la
reponse, jamais le texte de loi. Il rend la valeur **et** la phrase de la reponse
qui la justifie, verifiee mot pour mot par le script.

| Valeur | Signification |
|---|---|
| `suspend` | il reclame le fait manquant et ne conclut pas (attendu sur une mesure) |
| `conclut_puis_demande` | il conclut sur d'autres elements, puis reclame le fait |
| `repond_a_sa_place` | il conclut sur une supposition portant sur le fait manquant |
| `ne_demande_pas` | il ignore le fait manquant et conclut |
| `absente` | pas de reponse (les 7 cellules minimax) ; marquee par le script, jamais soumise au codeur |

Le codeur, ses regles et son calibrage sont dans
[docs/codage_calibrage.md](docs/codage_calibrage.md).

## Ou lire les resultats

- [docs/tableaux_resultats.md](docs/tableaux_resultats.md) : les tableaux
  complets (par enonce, par modele, la matrice), la regle d'agregation, et le
  resultat hors chaudiere.
- [docs/resultat_paire_f001.md](docs/resultat_paire_f001.md) : le resultat
  central, la paire controle/mesure de la chaudiere et l'axe "un defaut plausible
  est-il disponible".
- [docs/cellules_relancees.md](docs/cellules_relancees.md) : les 11 cellules en
  echec, diagnostic, et une limite de reproductibilite (le routage OpenRouter).
- [docs/limites_enonces.md](docs/limites_enonces.md) : limites de conception des
  enonces, a declarer.

## Rejouer, ou recoder sans rejouer

Les donnees sont deja dans le depot ; ces etapes ne servent qu'a les regenerer.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.exemple .env    # renseigner ANTHROPIC_API_KEY et OPENROUTER_API_KEY
```

Les cles viennent exclusivement de l'environnement, jamais du code ; `.env`
n'est pas versionne.

```bash
python src/tester_modeles.py                                       # les 13 modeles repondent-ils ?
python src/lancer.py --enonces tous --modeles tous --repetitions 3 # la campagne, 507 appels -> resultats/brut/
python src/coder.py                                                # code resultats/brut/ -> resultats/codage/
```

**Recoder sans relancer la campagne.** `src/coder.py` lit les reponses de
`resultats/brut/` : on peut changer les regles du codeur et recoder les 507
cellules sans refaire un seul appel de campagne.

**Reprise.** Lanceur comme codeur listent au demarrage ce qui est deja produit
et ne refont que ce qui manque ; ecriture atomique, aucun echec silencieux. Une
commande interrompue se reprend a l'identique. Les echecs sont journalises dans
`resultats/echecs.jsonl`.

## Les treize modeles

`claude-opus-5` via l'API directe Anthropic ; les douze autres via OpenRouter :
`gpt-5.6-sol`, `gpt-5.6-terra`, `gemini-3.1-pro`, `grok-4.6`, `mistral-large-3`,
`mistral-medium-3.5`, `kimi-k3`, `glm-5.2`, `deepseek-v4-pro`, `qwen-3.6-plus`,
`minimax-m3`, `llama-4-maverick`. Le registre de `src/modeles.py` fait foi. La
temperature est fixee a zero partout ou le fournisseur l'accepte ; le champ
`temperature_zero` de chaque resultat garde la trace des trois exceptions.

Reglages facultatifs par variables d'environnement : `NARCISSUS_JETONS_MAX`
(defaut 32000), `NARCISSUS_DELAI` (600 s), `NARCISSUS_TENTATIVES` (6),
`NARCISSUS_PLAFOND_ATTENTE` (60 s), `NARCISSUS_ID_<CLE>` pour forcer
l'identifiant fournisseur d'un modele sans toucher au code.
