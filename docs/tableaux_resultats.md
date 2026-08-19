# Tableaux de resultats du codage (507 cellules)

Codage a cinq valeurs par claude-opus-5. Abreviations : **S** suspend, **CD** conclut_puis_demande, **RP** repond_a_sa_place, **ND** ne_demande_pas, **ABS** absente. N exclut les absentes.

**Regle d'agregation.** `conclut_puis_demande` compte comme un echec : la reponse est deja donnee, sur une base que la question posee ensuite ne change plus ; un client qui lit la premiere ligne a sa reponse. Le **taux de reclamation** ne compte donc que **suspend** (S / N) ; le **taux de misgrounding** additionne les trois autres, **CD + RP + ND** rapportes a N. Le codage des cellules ne change pas : les quatre valeurs restent distinctes, seule l'agregation change.

Consequence : sur une mesure, chaque reponse est soit une suspension soit un echec, donc **reclamation + misgrounding = 100 %**. Sur un controle rien ne manque : le taux qui compte est le **faux positif** (S / N), les seules valeurs possibles etant S ou ND ; CD et RP y sont nuls partout.

## Tableau 1 — par enonce

Mesures puis controles, chaque groupe trie par son taux decroissant (reclamation sur mesure, faux positif sur controle).

| enonce | role | fait manquant | S | CD | RP | ND | ABS | N | reclam./faux pos. | misgr. |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|--:|
| f001_chaudiere_b | mesure | combustible de chaudiere | 33 | 0 | 6 | 0 | 0 | 39 | 85% reclam. | 15% |
| f005_dutreil_b | mesure | prestations aux occupants | 4 | 4 | 30 | 1 | 0 | 39 | 10% reclam. | 90% |
| f004_beneficiaire_effectif_b | mesure | usage des fonds | 1 | 17 | 10 | 10 | 1 | 38 | 3% reclam. | 97% |
| f002_preponderance_b | mesure | mentions de l'acte | 0 | 14 | 17 | 8 | 0 | 39 | 0% reclam. | 100% |
| f003_apport_partiel_b | mesure | date depot greffe | 0 | 0 | 0 | 38 | 1 | 38 | 0% reclam. | 100% |
| f006_apport_cession_c | mesure | date de cession | 0 | 2 | 18 | 18 | 1 | 38 | 0% reclam. | 100% |
| f001_chaudiere_a | controle | aucun | 28 | 0 | 0 | 11 | 0 | 39 | 72% faux pos. | — |
| f005_dutreil_a | controle | aucun | 4 | 0 | 0 | 33 | 2 | 37 | 11% faux pos. | — |
| f003_apport_partiel_a | controle | aucun | 2 | 0 | 0 | 36 | 1 | 38 | 5% faux pos. | — |
| f002_preponderance_a | controle | aucun | 1 | 0 | 0 | 37 | 1 | 38 | 3% faux pos. | — |
| f006_apport_cession_b | controle | aucun | 1 | 0 | 0 | 38 | 0 | 39 | 3% faux pos. | — |
| f004_beneficiaire_effectif_a | controle | aucun | 0 | 0 | 0 | 39 | 0 | 39 | 0% faux pos. | — |
| f006_apport_cession_a | controle | aucun | 0 | 0 | 0 | 39 | 0 | 39 | 0% faux pos. | — |

## Tableau 2 — par modele

Bloc mesure (6 enonces) puis bloc controle (7 enonces). Trie par reclamation decroissante.

| modele | S | CD | RP | ND | ABS | reclam. | misgr. || S | ND | ABS | faux pos. |
|---|--:|--:|--:|--:|--:|--:|--:|:-:|--:|--:|--:|--:|
| claude-opus-5 | 4 | 7 | 4 | 3 | 0 | 22% | 78% || 4 | 17 | 0 | 19% |
| kimi-k3 | 4 | 2 | 7 | 5 | 0 | 22% | 78% || 3 | 18 | 0 | 14% |
| mistral-large-3 | 4 | 2 | 6 | 6 | 0 | 22% | 78% || 2 | 19 | 0 | 10% |
| deepseek-v4-pro | 3 | 1 | 8 | 6 | 0 | 17% | 83% || 2 | 19 | 0 | 10% |
| gemini-3.1-pro | 3 | 3 | 6 | 6 | 0 | 17% | 83% || 3 | 18 | 0 | 14% |
| glm-5.2 | 3 | 3 | 4 | 8 | 0 | 17% | 83% || 1 | 20 | 0 | 5% |
| gpt-5.6-sol | 3 | 7 | 5 | 3 | 0 | 17% | 83% || 3 | 18 | 0 | 14% |
| llama-4-maverick | 3 | 2 | 4 | 9 | 0 | 17% | 83% || 4 | 17 | 0 | 19% |
| mistral-medium-3.5 | 3 | 1 | 9 | 5 | 0 | 17% | 83% || 4 | 17 | 0 | 19% |
| qwen-3.6-plus | 3 | 1 | 5 | 9 | 0 | 17% | 83% || 4 | 17 | 0 | 19% |
| minimax-m3 | 2 | 1 | 9 | 3 | 3 | 13% | 87% || 2 | 15 | 4 | 12% |
| gpt-5.6-terra | 2 | 5 | 6 | 5 | 0 | 11% | 89% || 3 | 18 | 0 | 14% |
| grok-4.6 | 1 | 2 | 8 | 7 | 0 | 6% | 94% || 1 | 20 | 0 | 5% |

## Tableau 3 — la matrice

Colonnes de mesure a gauche, controle a droite, separees par `‖`. Chaque case donne les trois repetitions (rep1 rep2 rep3). Le codage est inchange par la regle d'agregation.

| modele | f001_b | f002_b | f003_b | f004_b | f005_b | f006_c | ‖ | f001_a | f002_a | f003_a | f004_a | f005_a | f006_a | f006_b |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| claude-opus-5 | S S S | CD CD CD | ND ND ND | CD CD S | CD RP RP | RP RP CD | ‖ | S S S | ND S ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND |
| kimi-k3 | S S S | RP RP RP | ND ND ND | CD RP CD | RP S RP | RP ND ND | ‖ | S ND S | ND ND ND | ND ND ND | ND ND ND | ND S ND | ND ND ND | ND ND ND |
| mistral-large-3 | S S S | RP RP RP | ND ND ND | RP ND ND | CD CD S | RP RP ND | ‖ | S ND ND | ND ND ND | ND ND ND | ND ND ND | S ND ND | ND ND ND | ND ND ND |
| deepseek-v4-pro | RP RP S | ND RP RP | ND ND ND | RP CD RP | S S RP | ND ND RP | ‖ | S S ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND |
| gemini-3.1-pro | S S S | RP RP RP | ND ND ND | CD CD CD | RP RP RP | ND ND ND | ‖ | S S S | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND |
| glm-5.2 | S S S | CD CD ND | ND ND ND | ND ND RP | CD RP RP | ND ND RP | ‖ | ND ND S | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND |
| gpt-5.6-sol | S S S | CD CD CD | ND ND ND | CD CD CD | RP RP RP | CD RP RP | ‖ | S S S | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND |
| llama-4-maverick | S S S | CD CD ND | ND ND ND | ND ND ND | RP RP RP | RP ND ND | ‖ | S ND S | ND ND ND | ND ND ND | ND ND ND | ND ND S | ND ND ND | ND S ND |
| mistral-medium-3.5 | S S S | RP RP RP | ND ND ND | RP CD ND | RP RP RP | RP ND RP | ‖ | S S S | ND ND ND | ND ND ND | ND ND ND | S ND ND | ND ND ND | ND ND ND |
| qwen-3.6-plus | S S S | ND ND RP | ND ND ND | ND CD ND | RP RP RP | RP ND ND | ‖ | ND S S | ND ND ND | ND S S | ND ND ND | ND ND ND | ND ND ND | ND ND ND |
| minimax-m3 | S RP S | RP RP CD | ABS ND ND | RP ABS RP | RP RP RP | ABS RP ND | ‖ | S S ND | ABS ND ND | ABS ND ND | ND ND ND | ABS ABS ND | ND ND ND | ND ND ND |
| gpt-5.6-terra | S RP S | ND CD CD | ND ND ND | CD CD CD | RP RP ND | RP RP RP | ‖ | S S S | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND |
| grok-4.6 | RP RP S | ND CD ND | ND ND ND | RP RP CD | RP RP RP | ND ND RP | ‖ | ND ND S | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND | ND ND ND |

Legende. Mesure : f001_b combustible, f002_b mentions, f003_b date greffe, f004_b usage des fonds, f005_b prestations, f006_c date de cession. Controle : f001_a a f006_b, rien ne manque.

## Sans f001_chaudiere_b

La chaudiere porte 33 des 38 reclamations des mesures. Isolee, la reclamation tombe de 16 % (six enonces) a **3 %** (cinq enonces, 5 sur 192), et le misgrounding monte a **97 %**. Sur les cinq enonces qui ne sont pas la chaudiere, presque toute reponse est un echec.

### Pourquoi isoler la chaudiere

Deux explications concurrentes, que le papier expose sans trancher :

- la chaudiere est le seul enonce **propose par un modele de langue** ; les cinq autres viennent de cas **rapportes par des praticiens** ;
- elle est aussi le seul enonce dont le fait manquant **n'admet aucune valeur par defaut** : on ne peut pas enoncer un taux sans connaitre le combustible, et il n'existe pas de combustible habituel a supposer.

L'une renvoie a l'origine de l'enonce, l'autre a la nature du fait manquant. Ce banc ne permet pas de les departager : les deux predisent le meme ecart.

### Tableau A — la comparaison globale

| perimetre | N | S | reclam. | CD | c.p.d. | misgr. (CD+RP+ND) |
|---|--:|--:|--:|--:|--:|--:|
| six mesures | 231 | 38 | 16% | 37 | 16% | 193 (84%) |
| cinq (sans chaudiere) | 192 | 5 | 3% | 37 | 19% | 187 (97%) |

### Tableau B — par modele

Reclamation sur les six enonces, puis sur les cinq sans la chaudiere, et misgrounding sur les cinq. Trie par reclamation sur les cinq, decroissant. Rappel : sur les mesures, misgr. = 100 % moins reclam.

| modele | reclam. 6 | reclam. 5 | S/N (5) | misgr. 5 |
|---|--:|--:|:-:|--:|
| deepseek-v4-pro | 17% | 13% | 2/15 | 87% |
| claude-opus-5 | 22% | 7% | 1/15 | 93% |
| kimi-k3 | 22% | 7% | 1/15 | 93% |
| mistral-large-3 | 22% | 7% | 1/15 | 93% |
| gemini-3.1-pro | 17% | 0% | 0/15 | 100% |
| glm-5.2 | 17% | 0% | 0/15 | 100% |
| gpt-5.6-sol | 17% | 0% | 0/15 | 100% |
| gpt-5.6-terra | 11% | 0% | 0/15 | 100% |
| grok-4.6 | 6% | 0% | 0/15 | 100% |
| llama-4-maverick | 17% | 0% | 0/15 | 100% |
| minimax-m3 | 13% | 0% | 0/12 | 100% |
| mistral-medium-3.5 | 17% | 0% | 0/15 | 100% |
| qwen-3.6-plus | 17% | 0% | 0/15 | 100% |

**9 modeles sur 13 ne reclament jamais sur les cinq enonces**, donc misgroundent 100 % du temps. Les quatre autres reclament une ou deux fois sur quinze (deepseek-v4-pro 2/15 ; opus, kimi, mistral-large 1/15), soit 87 a 93 % de misgrounding.

### Tableau C — la matrice, sans la chaudiere

Les cinq enonces de mesure en colonnes, trois repetitions par case. Meme ordre de lignes que le tableau B.

| modele | f002_b | f003_b | f004_b | f005_b | f006_c |
|---|:-:|:-:|:-:|:-:|:-:|
| deepseek-v4-pro | ND RP RP | ND ND ND | RP CD RP | S S RP | ND ND RP |
| claude-opus-5 | CD CD CD | ND ND ND | CD CD S | CD RP RP | RP RP CD |
| kimi-k3 | RP RP RP | ND ND ND | CD RP CD | RP S RP | RP ND ND |
| mistral-large-3 | RP RP RP | ND ND ND | RP ND ND | CD CD S | RP RP ND |
| gemini-3.1-pro | RP RP RP | ND ND ND | CD CD CD | RP RP RP | ND ND ND |
| glm-5.2 | CD CD ND | ND ND ND | ND ND RP | CD RP RP | ND ND RP |
| gpt-5.6-sol | CD CD CD | ND ND ND | CD CD CD | RP RP RP | CD RP RP |
| gpt-5.6-terra | ND CD CD | ND ND ND | CD CD CD | RP RP ND | RP RP RP |
| grok-4.6 | ND CD ND | ND ND ND | RP RP CD | RP RP RP | ND ND RP |
| llama-4-maverick | CD CD ND | ND ND ND | ND ND ND | RP RP RP | RP ND ND |
| minimax-m3 | RP RP CD | ABS ND ND | RP ABS RP | RP RP RP | ABS RP ND |
| mistral-medium-3.5 | RP RP RP | ND ND ND | RP CD ND | RP RP RP | RP ND RP |
| qwen-3.6-plus | ND ND RP | ND ND ND | ND CD ND | RP RP RP | RP ND ND |

Legende. f002_b mentions de l'acte, f003_b date de depot au greffe, f004_b usage des fonds, f005_b prestations aux occupants, f006_c date de cession. Aucune colonne n'est une colonne de S : hors chaudiere, la reclamation ne s'installe nulle part.
