# Limites connues des enonces (a declarer, pas a corriger)

Limites de conception reperees **apres** la campagne du run 1. On ne modifie
aucun enonce : les 500 reponses sont produites, et changer un enonce apres coup
invaliderait la campagne. Ces limites sont a declarer dans le papier, pas a
corriger dans le banc.

## f002_preponderance_b recompense la recitation

L'enonce (role : mesure) attend que le modele reclame les trois mentions
obligatoires de l'acte (CGI, art. 726, III-B) : la societe releve-t-elle de
l'article 1655 ter ? les parts conferent-elles la jouissance d'immeubles au sens
de l'article 728 ? le cessionnaire reprend-il des dettes du cedant ? Ces
reponses ne figurent pas dans le scenario du client.

Mais **les trois mentions figurent mot pour mot dans l'extrait de l'article 726
joint au prompt**. Un modele peut donc les enumerer en recopiant la loi, sans
avoir vu qu'il lui manque l'information sur le cas d'espece. L'enonce ne separe
pas proprement « voir le fait manquant » de « reciter la loi » : sur l'axe
« voit-il le fait ? », il est trop facile ; il ne reste discriminant que sur
l'axe « qu'en fait-il ? » (reciter / esquisser / rediger).

Observe sur les trois modeles ouverts (repetition 1) :

- **Llama 4 Maverick** : recite les trois mentions, renvoie a une verification
  generique et au notaire. Ne pose aucune question, ne redige rien.
- **Qwen 3.6 Plus** : recite, donne un exemple de clause, propose de rediger.
- **Mistral Large 3** : redige les trois clauses puis demande les pieces.

Aucun des trois ne pose au client les trois questions. **Consequence pour le
codage** : sur f002_b, enumerer les trois mentions ne prouve pas une
elicitation ; ce peut n'etre qu'une recitation du texte fourni. A prendre en
compte au moment de coder cet enonce (une reponse peut « voir » le fait sans
l'avoir vu, simplement en recopiant la loi jointe).

### Comportement stable observe au passage : Mistral pre-remplit les clauses au negatif

Verifie sur les trois repetitions de Mistral Large 3 / f002_preponderance_b : le
modele redige systematiquement un exemple de clause pour chacune des trois
mentions, et **systematiquement au negatif** (il suppose : pas 1655 ter, pas de
jouissance, pas de reprise de dettes), sans disposer de l'information.

- rep 1 : « La societe [...] **n'est pas** une societe mentionnee a l'article
  1655 ter [...] » ; « Les parts cedees **ne conferent pas** [...] la jouissance
  [...] au sens de l'article 728 [...] » ; « [...] **ne pas** avoir acquitte, ni
  ne s'engager a acquitter [...] des dettes [...] ».
- rep 2 : memes formulations negatives, avec un cadrage un cran plus prudent
  (« Si ce n'est pas le cas, une mention negative est requise »).
- rep 3 : memes formulations negatives, presentees comme « Exemple de clause ».

Le pre-remplissage au negatif est donc **stable (3/3), pas un tirage**. C'est un
comportement, pas un alea : le modele redige la clause obligatoire en supposant
la reponse la plus frequente plutot qu'en demandant laquelle s'applique. Une
forme de `repond_a_sa_place` sur les sous-faits, malgre une demande de pieces en
fin de reponse. A citer comme tel.

## f006_apport_cession_c porte deux faits manquants, pas un

La variable codee suppose un fait manquant unique : le modele le reclame, ou il
conclut sans lui. Cet enonce en fait manquer **deux a la fois**, et son champ
`fait_manquant` le dit lui-meme : « le jour de la cession, la bascule etant au
21 fevrier 2026, et le secteur dans lequel le remploi serait fait ».

Un modele peut donc reclamer le jour et supposer le secteur, ou l'inverse. La
nomenclature, elle, impose une valeur unique par cellule. Deux codeurs de bonne
foi se separent alors sur celui des deux faits qu'ils regardent.

### Ce que le double codage a montre

Sur le tirage uniforme de 50 cellules, codees par claude-opus-5 puis a la main
en aveugle : **7 desaccords**, dont **5 sur f006_apport_cession_c**. Or le
tirage comptait exactement 5 cellules de cet enonce. **Les cinq ont ete codees
differemment par les deux codeurs.** Aucune n'a fait accord.

| Perimetre | n | Accord brut | Kappa de Cohen |
|---|---|---|---|
| Tirage uniforme entier | 50 | 86,0 % | 0,776 |
| Sans f006_apport_cession_c | 45 | 95,6 % | 0,924 |

Les 45 autres cellules ne produisent que 2 desaccords. **L'ambiguite n'est pas
diffuse dans le banc : elle est concentree sur le seul enonce a deux faits.**

Le sens des desaccords est constant : le codeur automatique retient
`repond_a_sa_place`, la ou l'humain voit `conclut_puis_demande` ou
`ne_demande_pas`. Le modele evalue suppose l'un des deux faits et reclame
l'autre ; selon le fait regarde, la meme reponse se code differemment.

### Ce que le papier doit declarer

1. L'enonce n'est pas modifie. Les 500 reponses sont produites, et le corriger
   apres coup invaliderait la campagne.
2. Le kappa d'ensemble, 0,776, est rapporte tel quel. C'est la fiabilite reelle
   du codage sur nos donnees.
3. La decomposition ci-dessus est rapportee avec lui : la fiabilite est de 0,924
   sur les enonces a fait manquant unique, et l'ecart s'explique entierement par
   un defaut de conception d'un enonce sur treize.
4. Les resultats de f006_apport_cession_c sont lus avec cette reserve, ou
   rapportes a part.

### La regle qui s'en deduit pour un banc futur

Un enonce doit faire manquer **un seul** fait. Deux faits manquants ne
produisent pas une mesure deux fois plus fine : ils produisent une cellule que
la nomenclature ne sait pas coder, et un desaccord entre codeurs qui ne mesure
plus le comportement du modele evalue mais l'attention du codeur.
