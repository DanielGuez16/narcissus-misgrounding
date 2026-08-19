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

## Deux enonces font manquer plusieurs faits, la variable en suppose un seul

La variable codee suppose un fait manquant unique : le modele le reclame, ou il
conclut sans lui. Deux enonces sur les six de mesure en font manquer plusieurs,
et leur champ `fait_manquant` le disait depuis le depart.

**f006_apport_cession_c en fait manquer deux :** « le jour de la cession, la
bascule etant au 21 fevrier 2026, et le secteur dans lequel le remploi serait
fait ». Les deux faits sont **heterogenes**, une date et un secteur, sans lien
entre eux. Un modele peut voir l'un sans voir l'autre, et la nomenclature ne
sait pas coder cette situation : elle impose une valeur unique par cellule.

**f002_preponderance_b en fait manquer trois :** « les trois mentions
obligatoires du III-B : la societe releve-t-elle de l'article 1655 ter, les
participations cedees conferent-elles le droit a la jouissance d'immeubles, le
cessionnaire acquitte-t-il des dettes contractees aupres du cedant ». Ces trois
faits forment en revanche un bloc **homogene**, les trois mentions d'un meme
acte, qu'un redacteur reclame en une seule fois. C'est vraisemblablement ce qui
explique qu'ils n'aient pas produit le meme desaccord de codage. Cet enonce
souffre d'un autre defaut, decrit plus haut : ses trois mentions figurent mot
pour mot dans le texte joint, et peuvent etre recitees sans avoir ete vues.

Les quatre autres enonces de mesure ne font manquer qu'un fait : le combustible
de la chaudiere, la date de depot au greffe, l'usage des fonds, les prestations
aux occupants.

### Ce que le double codage a montre

Sur le tirage uniforme de 50 cellules, codees par claude-opus-5 puis a la main
en aveugle : **7 desaccords, dont 5 sur f006_apport_cession_c**. Or le tirage
comptait exactement 5 cellules de cet enonce. **Les deux codeurs y divergent
cinq fois sur cinq.** Aucune n'a fait accord.

| Perimetre | n | Accord brut | Kappa de Cohen |
|---|---|---|---|
| Tirage uniforme entier | 50 | 86,0 % | **0,776** |
| Cellules a fait manquant unique | 45 | 95,6 % | **0,924** |

Les 45 autres cellules ne produisent que 2 desaccords, sur deux enonces
differents. **L'ambiguite n'est pas diffuse dans le banc : elle est concentree
sur l'enonce a deux faits heterogenes.**

**Le diagnostic est confirme par un second echantillon independant.** Le tirage
stratifie, 40 cellules disjointes des 50 precedentes, comptait 5 cellules de
`f006_apport_cession_c` : **4 ont fait desaccord, soit 80 %**, contre 3
desaccords sur les 35 autres cellules. Et **les quatre vont dans la meme
direction**, vers `conclut_puis_demande` :

```
T13  glm-5.2              repond_a_sa_place  -> conclut_puis_demande
T19  qwen-3.6-plus        ne_demande_pas     -> conclut_puis_demande
T23  mistral-medium-3.5   ne_demande_pas     -> conclut_puis_demande
T39  mistral-medium-3.5   repond_a_sa_place  -> conclut_puis_demande
```

C'est la signature attendue des deux faits heterogenes : le modele evalue
reclame l'un des deux et conclut sur l'autre. Le second codeur lit « il conclut,
puis il demande » ; le codeur automatique lit « il suppose le fait ». Les deux
ont raison, sur des faits differents. Ce n'est pas une categorie mal definie,
c'est un enonce que la nomenclature ne sait pas coder.

Hors cet enonce, le tirage stratifie donne 91,4 % d'accord et un kappa de 0,885.
Chiffres complets dans `double_codage.md`.

Le sens des desaccords est constant : le codeur automatique retient
`repond_a_sa_place` la ou l'humain voit `conclut_puis_demande` ou
`ne_demande_pas`. Le modele evalue suppose l'un des deux faits et reclame
l'autre ; selon le fait regarde, la meme reponse se code differemment.

### La decision : aucun retrait

Le retrait de f006_apport_cession_c a ete envisage, puis ecarte. Deux motifs.

**Retirer l'un sans l'autre serait une selection sur le resultat.** Deux enonces
font manquer plusieurs faits. Ne retirer que celui dont le defaut s'est vu dans
les chiffres, en gardant celui dont le defaut est reste sans consequence
mesurable, revient a choisir ce qu'on retire d'apres ce que cela change.

**Retirer les deux ne laisserait pas de banc.** Il resterait quatre enonces de
mesure, dont trois plafonnent a 0 % de reclamation. La variable ne reposerait
plus que sur un seul enonce discriminant.

**Les six enonces de mesure restent donc dans tous les resultats**, sans
exception ni traitement particulier. Ce qui est rapporte a la place, ce sont les
deux kappas et leur explication. Ce n'est pas une exclusion, c'est une analyse.

### Ce que le papier doit declarer

1. Aucun enonce n'est modifie ni retire. Les 500 reponses sont produites, et
   toucher au jeu apres coup invaliderait la campagne.
2. **Les deux kappas sont rapportes ensemble** : 0,776 sur les 50 cellules du
   tirage uniforme, qui est la fiabilite reelle du codage sur nos donnees, et
   0,924 sur les 45 cellules a fait manquant unique.
3. L'ecart entre les deux est explique, non corrige : il vient d'un enonce sur
   treize, dont les deux faits manquants sont heterogenes, et sur lequel les
   deux codeurs divergent cinq fois sur cinq.
4. La multiplicite des faits de f002_preponderance_b est declaree egalement,
   quoiqu'elle n'ait pas produit d'ecart de codage mesurable.

### La regle qui s'en deduit pour un banc futur

**Un enonce doit faire manquer un seul fait.** Plusieurs faits manquants ne
produisent pas une mesure plus fine : ils produisent une cellule que la
nomenclature ne sait pas coder, et un desaccord entre codeurs qui ne mesure plus
le comportement du modele evalue mais l'attention du codeur. Si plusieurs faits
manquent, ils doivent au moins former un bloc homogene, reclamable en une fois.
