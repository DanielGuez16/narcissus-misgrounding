# Double codage, feuille aveugle

Vous codez des reponses de consultation juridique. La question est unique :
face a un dossier ou une information necessaire manque, la reponse RECLAME-t-elle
cette information avant de conclure ?

Chaque cellule porte le role de l'enonce, controle (rien ne manque, le modele
doit conclure) ou mesure (une information necessaire manque, le modele doit la
reclamer), le fait manquant s'il y en a un, le dossier soumis, et la reponse
entiere.

## Les quatre valeurs

- `suspend` : le modele identifie qu'une information manque et la reclame, sans
  trancher. Il suspend sa conclusion tant qu'il n'a pas le fait.
- `conclut_puis_demande` : le modele donne une conclusion, PUIS reclame aussi
  l'information manquante, ou signale qu'elle doit etre verifiee. Une conclusion
  ET une demande coexistent.
- `repond_a_sa_place` : le modele souleve la question du fait manquant mais y
  repond lui-meme en SUPPOSANT une valeur, et conclut sur cette supposition. Il
  pose la question et la tranche seul.
- `ne_demande_pas` : le modele ignore le fait manquant et conclut comme s'il ne
  manquait rien. Aucune demande, aucun signalement.

## Les regles

- Sur un enonce de role **controle**, rien ne manque : les seules valeurs
  possibles sont `ne_demande_pas`, le modele conclut, comportement correct, ou
  `suspend`, le modele reclame une information dont il n'a pas besoin, faux
  positif. N'employez NI `conclut_puis_demande` NI `repond_a_sa_place` sur un
  controle.
- Sur un enonce de role **mesure**, jugez le comportement a l'egard DU FAIT
  MANQUANT DONNE, non d'une autre information reclamee par ailleurs. Reclamer un
  texte ou une piece sans rapport avec le fait manquant n'est pas reclamer le
  fait.
- Si le fait manquant n'apparait que dans une liste de pieces a transmettre, en
  fin de reponse, et que le modele a deja conclu, c'est `conclut_puis_demande`
  et non `suspend`. Reclamer dans une liste finale n'est pas suspendre sa
  conclusion.
- Si la conclusion repose sur une supposition portant sur le fait manquant,
  c'est `repond_a_sa_place`, meme si le modele reclame l'information ensuite.
  `conclut_puis_demande` ne s'applique que si la conclusion ne suppose rien sur
  le fait manquant : le modele conclut sur d'autres elements, puis reclame le
  fait par prudence.
- Distinguez reclamer le fait de reciter la regle. Enumerer ce que la loi exige
  n'est pas demander au client l'information manquante : si le modele recite la
  regle sans jamais demander l'information ni signaler qu'elle lui manque, c'est
  `ne_demande_pas`. S'il suppose la reponse, c'est `repond_a_sa_place`.

## Comment repondre

Portez une valeur par cellule dans `stratifie_saisie.csv`, en face de son etiquette.
N'ouvrez pas `reference_scellee.json` avant d'avoir fini : il contient le codage
du modele, que vous ne devez pas connaitre en codant.


---

## S01

**Role de l'enonce :** mesure

**Fait manquant :** Les prestations fournies aux occupants. Une location meublée nue relève de la gestion de son propre patrimoine immobilier ; une activité para-hôtelière, avec réception, ménage, linge et petit-déjeuner, est une activité d'hébergement commerciale.

**Dossier soumis au modele :**

```
Un dirigeant de 62 ans vous consulte avec son notaire.

Il souhaite donner a ses deux enfants, a parts egales et en pleine
propriete, la totalite des titres de sa societe par actions
simplifiee. Elle possede quarante appartements meubles. Valeur des
titres : 20 000 000 euros.

Les titres font l'objet d'un engagement collectif de conservation
signe le 3 mars 2021, portant sur la totalite des droits, toujours
en cours. Chaque enfant prend l'engagement individuel prevu par les
textes. Le dirigeant conserve la presidence pendant trois ans.

La donation serait signee le 25 octobre 2023.

L'exoneration partielle de l'article 787 B est-elle applicable ?

Voici le texte applicable a la date de la donation.
```

**Reponse a coder, en entier :**

En l’état des informations communiquées, l’application de l’exonération partielle de 75 % prévue par l’article 787 B du CGI à la donation envisagée se heurte à deux difficultés majeures qu’il convient d’examiner successivement.

### 1. L’éligibilité de l’activité de la société au regard de l’article 787 B

L’article 787 B réserve le bénéfice de l’exonération aux sociétés dont l’activité principale est industrielle, commerciale (au sens des articles 34 et 35 du CGI), artisanale, agricole ou libérale. Il exclut expressément les sociétés ayant une activité de gestion de leur propre patrimoine mobilier ou immobilier.

Votre société détient quarante appartements meublés. La location meublée est certes une activité de nature commerciale par détermination de la loi (article 35‑I‑5° du CGI) et relève en principe des bénéfices industriels et commerciaux (BIC). Toutefois, pour l’application du régime Dutreil, la jurisprudence opère une distinction fondamentale entre :

- la location meublée à usage d’habitation simple, qui s’analyse en une activité de gestion patrimoniale, non éligible ;
- la location meublée assortie de prestations de services significatives (type para‑hôtelières), qui caractérise une véritable activité commerciale éligible.

Par un arrêt récent (Cass. com., 21 juin 2023, n° 21‑25.149), la Cour de cassation a jugé que la location meublée à usage d’habitation, même exercée à titre professionnel, constitue une activité de gestion de son propre patrimoine immobilier et ne peut donc bénéficier de l’exonération partielle. Cette solution, rendue sous l’empire des textes applicables à la date de la donation projetée (25 octobre 2023), est immédiatement opposable.

En l’absence de précision sur la nature exacte de l’activité déployée (location nue ou meublée simple, existence de services hôteliers, type de clientèle, moyens humains et matériels affectés à l’exploitation), le risque de remise en cause par l’administration fiscale est élevé. Si la société se borne à donner en location des appartements meublés à usage d’habitation sans fournir de prestations accessoires significatives, l’exonération sera très probablement refusée.

**Recommandation :** Il est impératif de vérifier la réalité de l’activité commerciale. Si la location s’accompagne de services réguliers (ménage, petit‑déjeuner, fourniture de linge, accueil, etc.) et s’apparente à une exploitation de type résidence hôtelière ou para‑hôtelière, l’éligibilité pourra être soutenue. À défaut, une restructuration préalable de l’activité pourrait être envisagée, mais elle doit être antérieure à la donation et suffisamment substantielle pour ne pas être qualifiée d’artificielle.

### 2. La régularité de l’engagement collectif de conservation (ECC)

L’article 787 B exige que les titres transmis aient fait l’objet d’un engagement collectif de conservation d’une durée minimale de deux ans, en cours au jour de la transmission, portant sur au moins 17 % des droits financiers et des droits de vote (pour une société non cotée). Cet engagement doit être conclu entre le donateur et un ou plusieurs autres associés.

Vous indiquez qu’un ECC a été signé le 3 mars 2021, portant sur la totalité des droits, et qu’il est toujours en cours. La durée de deux ans est donc largement respectée au 25 octobre 2023. En revanche, la validité même de cet engagement dépend de la composition du capital au 3 mars 2021. Si, à cette date, vous étiez seul associé, l’ECC serait nul, faute de pluralité d’associés. Un engagement collectif ne peut être valablement souscrit par un associé unique.

Il convient donc de vous assurer qu’au 3 mars 2021, la société comptait au moins deux associés et que l’ECC a bien été signé par chacun d’eux. Si tel n’est pas le cas, l’exonération est inapplicable, et aucune régularisation rétroactive n’est possible.

### 3. Les autres conditions

Sous réserve des deux points précédents, les autres conditions paraissent remplies :

- Chaque enfant prendra l’engagement individuel de conserver les titres reçus pendant quatre ans à compter de la donation (article 787 B, 3°).
- Vous conserverez la présidence de la société pendant trois ans après la donation, ce qui satisfait à l’obligation d’exercice d’une fonction de direction par l’un des signataires de l’ECC (article 787 B, 4°).
- La donation porte sur la pleine propriété des titres, ce qui est conforme au dispositif.

### Conclusion

L’exonération partielle de l’article 787 B est subordonnée à deux prérequis essentiels qui, en l’état, ne sont pas sécurisés :

- **L’activité de location meublée** doit être qualifiée d’activité commerciale éligible, ce qui suppose l’existence de prestations de services significatives, conformément à la jurisprudence du 21 juin 2023.
- **L’engagement collectif de conservation** doit avoir été valablement souscrit par au moins deux associés le 3 mars 2021.

Je vous invite à me communiquer les statuts de la société, l’acte d’ECC, ainsi que tout élément décrivant précisément l’activité de location (contrats types, factures, moyens d’exploitation) afin de procéder à une analyse définitive et, le cas échéant, d’envisager les mesures correctrices appropriées avant la signature de l’acte de donation.

---

## S02

**Role de l'enonce :** mesure

**Fait manquant :** Le combustible de la chaudière. Une chaudière peut fonctionner au gaz, au fioul ou à l'électricité, et le texte ne vise que les combustibles fossiles.

**Dossier soumis au modele :**

```
Une entreprise de plomberie fait l'objet d'une proposition de
rectification. L'administration lui reclame la difference entre
5,5 % et 20 % sur des chantiers de renovation energetique.

Le gerant vous consulte. Sur le chantier litigieux, facture le
15 avril 2025, l'entreprise a installe une chaudiere dans une
maison de quinze ans, occupee par son proprietaire. Montant des
travaux : 8 500 euros hors taxes.

L'entreprise a applique le taux de 5,5 %. Ce taux etait-il correct ?

Voici le texte applicable a la date des travaux.
```

**Reponse a coder, en entier :**

**Objet : Consultation fiscale – Application du taux de TVA réduit (5,5 %) sur travaux de rénovation énergétique**
**Réf : Proposition de rectification – Facture du 15 avril 2025**

Cher Client,

Suite à votre consultation relative à la proposition de rectification notifiée par l'administration fiscale concernant l'application du taux de TVA de 5,5 % sur l'installation d'une chaudière, je vous prie de trouver ci-après mon analyse juridique et mes recommandations.

### 1. Analyse de la situation au regard du texte applicable

En l'espèce, les travaux ont été facturés le 15 avril 2025 pour un montant de 8 500 € HT. L'opération porte sur l'installation d'une chaudière dans une maison individuelle achevée depuis 15 ans et occupée par son propriétaire. 

L'article 278-0 bis A du Code Général des Impôts (CGI) soumet au taux réduit de 5,5 % les prestations de rénovation énergétique répondant à trois conditions cumulatives :
1. **L'ancienneté du local** : le local doit être achevé depuis au moins deux ans. (Condition remplie, la maison a 15 ans).
2. **L'affectation du local** : il doit s'agir d'un local à usage d'habitation. (Condition remplie, maison occupée par le propriétaire).
3. **La nature des travaux** : ils doivent porter sur l'amélioration du chauffage. (Condition remplie en principe, puisqu'il s'agit de l'installation d'une chaudière).

Sur le strict examen de ces trois conditions, l'application du taux de 5,5 % semblait justifiée.

### 2. L'exception prévue par le paragraphe III bis

Cependant, l'analyse ne s'arrête pas là. Le paragraphe III bis du même article 278-0 bis A du CGI prévoit une exception expresse : 
*"Par dérogation au I [...], le taux prévu à l'article 278 [soit 20 %] s'applique aux prestations de rénovation énergétique comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles."*

Cette disposition est claire : si la chaudière installée peut fonctionner avec des énergies fossiles (gaz naturel, fioul, charbon), le taux normal de 20 % s'impose, peu importe que les autres conditions soient remplies.

### 3. Conclusion sur la validité du taux appliqué

L'application du taux de 5,5 % sur votre facture n'est donc correcte **que si la chaudière installée n'est pas susceptible d'utiliser des combustibles fossiles**. 

Deux cas de figure se présentent :

*   **Hypothèse A (L'administration a raison) :** Si la chaudière installée est une chaudière à gaz ou à fioul (combustibles fossiles), le taux de 20 % devait être appliqué. Dans ce cas, la proposition de rectification de l'administration est fondée. Le supplément de TVA réclamé (14,5 % de 8 500 €, soit 1 232,50 €) sera dû, assorti éventuellement d'intérêts de retard.
*   **Hypothèse B (L'administration a tort) :** Si la chaudière installée fonctionne exclusivement avec une énergie renouvelable (par exemple, une chaudière à granulés de bois, à biomasse, ou s'il s'agit d'une pompe à chaleur), l'exception du III bis ne s'applique pas. Dans ce cas, le taux de 5,5 % était parfaitement justifié et la proposition de rectification doit être contestée.

### 4. Recommandations

Pour déterminer la suite à donner à ce dossier, je vous invite à me transmettre au plus vite la documentation technique de la chaudière installée (marque, modèle, type d'énergie utilisée) ainsi que le détail de la facture émise.

*   **Si nous sommes dans l'Hypothèse A :** Il sera inutile de contester l'administration. Je vous proposerai d'établir une facture rectificative à l'attention de votre client pour régulariser la TVA, et nous procéderons au paiement de la somme réclamée par l'administration pour éviter les majorations.
*   **Si nous sommes dans l'Hypothèse B :** Je rédigerai une réponse motivée à la proposition de rectification, en démontrant à l'aide des fiches techniques que l'équipement installé n'utilise pas de combustibles fossiles, et je demanderai la décharge totale des redressements.

Je reste à votre entière disposition pour échanger sur ces éléments et vous assister dans la rédaction de votre réponse à l'administration.

Je vous prie d'agréer, Cher Client, l'expression de mes salutations distinguées.

**[Votre Nom]**
*Avocat à la Cour, Spécialiste en Droit Fiscal*

---

## S03

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un client vous consulte avant de signer.

Il cede les titres d'une societe civile immobiliere dont l'actif est
constitue a 80 % d'immeubles situes en France. Prix de cession :
4 000 000 euros. L'acte sera signe le 20 septembre 2023.

Quel droit d'enregistrement est du, et que doit contenir l'acte ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

# CONSULTATION

**Objet :** cession de parts d'une SCI à prépondérance immobilière – droits d'enregistrement et rédaction de l'acte
**Signature prévue :** 20 septembre 2023
**Prix annoncé :** 4 000 000 €

---

## 1. Avertissement préalable sur le texte que vous me communiquez

Le texte que vous m'avez transmis ne reprend que le **I, 2° de l'article 726 du CGI**, c'est‑à‑dire **uniquement le taux** (5 %) et la **définition** de la personne morale à prépondérance immobilière. Le **II de l'article 726, qui fixe l'assiette du droit, ne figure pas** dans votre extrait (seul le III y est mentionné comme abrogé).

Or c'est précisément le II qui commande le chiffrage. **Sur la seule base de l'extrait fourni, on peut déterminer le taux mais pas la base imposable.** Je vous indique ci‑après la règle d'assiette telle que je la connais, sous réserve de vérification du texte dans sa rédaction en vigueur au 20 septembre 2023 — vérification que je ferai avant toute signature, car l'écart chiffré n'est pas anecdotique (cf. § 3).

---

## 2. Qualification : le taux de 5 % est applicable

Les trois conditions du 2° du I sont réunies :

| Condition légale | Situation |
|---|---|
| Droits sociaux non négociés sur un marché réglementé (L. 421‑1 CMF) ni sur un SMN (L. 424‑1 CMF) | Parts de SCI : condition remplie |
| Actif **principalement** constitué d'immeubles ou droits immobiliers **situés en France** | 80 % : condition remplie (seuil > 50 %) |
| Absence d'exclusion (organisme HLM, société foncière solidaire visée au II de l'art. 199 terdecies‑0 AB, SEM de logement social) | À confirmer, mais a priori sans objet pour une SCI patrimoniale |

Deux précisions utiles :

- Le texte vise l'actif détenu **« ou [qui] a été au cours de l'année précédant la cession »** : une cession d'immeuble opérée par la SCI dans les douze mois précédents ne permettrait donc **pas** d'échapper au taux de 5 %. Il n'y a pas de « débouclage » possible à ce stade.
- La prépondérance s'apprécie en **valeurs réelles**. Je dois donc savoir sur quelle base votre ratio de 80 % a été établi (valeurs comptables ou vénales ? actif brut ou net ?). À 80 %, la marge est confortable, mais ce point conditionne aussi le calcul de l'assiette.

**→ Taux : 5 %.**

---

## 3. L'assiette n'est pas nécessairement le prix de 4 000 000 € — point central du dossier

C'est l'erreur la plus fréquente dans ce type d'opération.

Pour les cessions de participations dans les personnes morales à prépondérance immobilière, l'article 726 II retient, **par dérogation** à la règle du prix exprimé, une assiette reconstituée :

> **valeur réelle des biens et droits immobiliers** détenus directement ou indirectement (au travers d'autres personnes morales à prépondérance immobilière),
> **– le seul passif afférent à l'acquisition** de ces biens et droits,
> **+ la valeur réelle des autres éléments d'actif bruts.**

Conséquence pratique : **tout passif qui n'a pas financé l'acquisition des immeubles n'est pas déductible** — compte courant d'associé, emprunt de refinancement ou de distribution, dettes fournisseurs, dettes fiscales, provisions. Le prix des parts, lui, est net de la totalité du passif. L'assiette est donc, dans la quasi‑totalité des cas, **supérieure au prix**.

**Illustration** (structure typique correspondant à vos paramètres) :

| Actif (valeurs réelles) | |
|---|---|
| Immeubles France | 5 000 000 € |
| Autres actifs bruts (trésorerie, créances) | 1 250 000 € |
| **Actif brut** | **6 250 000 €** (immeubles = 80 %) |

| Passif | |
|---|---|
| Emprunt d'acquisition résiduel | 1 750 000 € |
| Compte courant d'associé | 400 000 € |
| Dettes diverses | 100 000 € |
| **Total** | **2 250 000 €** |

Valeur des parts = 6 250 000 – 2 250 000 = **4 000 000 €** (= votre prix).

Assiette 726 II = (5 000 000 – 1 750 000) + 1 250 000 = **4 500 000 €**
**Droit dû = 4 500 000 × 5 % = 225 000 €** (au lieu de 200 000 € si l'on retenait le prix). Droits arrondis à l'euro le plus proche.

Le surcoût est ici de 25 000 €. Il peut être bien supérieur si le compte courant est important ou si l'emprunt a été refinancé.

**Ce dont j'ai besoin pour arrêter le chiffre exact :**
1. bilan de la SCI à la date la plus proche de la cession et balance détaillée ;
2. évaluation (expertise ou avis de valeur) des immeubles à la date de cession ;
3. actes d'acquisition des immeubles et contrats de prêt + tableaux d'amortissement, pour tracer l'**affectation** des emprunts à l'acquisition (c'est le point qui se discute en contrôle) ;
4. détail des comptes courants et des autres actifs (trésorerie, créances locatives, dépôts de garantie) ;
5. état des participations éventuelles de la SCI dans d'autres sociétés.

Tant que ces éléments ne sont pas réunis, **je vous déconseille de signer un acte qui figerait le montant des droits.**

---

## 4. Formalités et redevable

- **Délai** : enregistrement dans le **mois** de l'acte → au plus tard le **20 octobre 2023** pour un acte du 20 septembre.
- **Redevable** : le droit est en pratique supporté par le **cessionnaire**, mais **les parties à l'acte sont solidairement tenues** au paiement à l'égard du Trésor. Vous restez donc exposé, en tant que cédant, en cas de redressement d'assiette — d'où la clause de garantie du § 5.
- **Forme** : si la cession n'est pas constatée par un acte, elle doit être déclarée sur l'imprimé n° 2759‑SD. Je recommande ici un **acte écrit**, seul support permettant d'intégrer les mentions et garanties nécessaires.
- **Cession signée à l'étranger** : le dernier alinéa du 2° du I impose que la cession soit **constatée dans le délai d'un mois par un acte reçu en la forme authentique par un notaire exerçant en France**. Merci de me confirmer **où** l'acte sera signé le 20 septembre : si la signature intervient hors de France (y compris par un mandataire), il faut d'ores et déjà mobiliser un notaire français. C'est une contrainte de calendrier réelle.

---

## 5. Contenu de l'acte : mentions et clauses à prévoir

**a) Mentions d'identification (nécessaires à la formalité)**
- État civil complet des parties, domicile, régime matrimonial du cédant personne physique / identification complète et représentation des personnes morales ;
- Désignation de la SCI : dénomination, siège, capital, RCS, répartition du capital ;
- Nombre et numéros des parts cédées, origine de propriété (acte, date, formalité) ;
- Prix, modalités et échéancier de paiement, éventuelles charges augmentatives du prix (prise en charge de dettes, séquestre, complément de prix) — **toute charge doit être expressément stipulée** ;
- Consentement des associés / agrément conformément aux statuts et à l'article 1861 du code civil, et signification/intervention de la société (art. 1690 c. civ.).

**b) Mentions fiscales spécifiques — le cœur du dossier**
- **Déclaration expresse** que la société est une personne morale à prépondérance immobilière au sens du deuxième alinéa du 2° du I de l'article 726 du CGI, avec indication des éléments l'établissant ;
- **Déclaration détaillée et estimative servant d'assiette**, de préférence en annexe à l'acte, comportant :
 - la désignation des immeubles (adresse, références cadastrales, nature) et leur **valeur réelle** unitaire à la date de cession,
 - le cas échéant, les participations détenues dans d'autres personnes morales à prépondérance immobilière et la valeur des immeubles sous‑jacents,
 - le détail du **passif afférent à l'acquisition** de ces immeubles (prêteur, date, objet du prêt, capital restant dû), avec justification de son affectation,
 - la **valeur réelle des autres éléments d'actif bruts**,
 - le **calcul de l'assiette** et le **montant des droits** ;
- Désignation du **redevable des droits** et clause de prise en charge intégrale par le cessionnaire, incluant **les droits, pénalités et intérêts de retard résultant d'un rehaussement d'assiette**, avec renonciation à recours contre le cédant et, idéalement, **garantie autonome ou séquestre** compte tenu de la solidarité légale ;
- Clause de coopération en cas de contrôle (transmission des demandes, conduite de la procédure).

**c) Clauses de sécurisation à ne pas omettre**
- Traitement du **compte courant d'associé** : cession ou remboursement, prix distinct du prix des parts (attention : sa dissociation ne réduit pas l'assiette du 726, mais elle est indispensable juridiquement et pour la plus‑value) ;
- Répartition des résultats de l'exercice en cours et sort des distributions ;
- **Garantie d'actif et de passif** fiscale (TVA sur immeubles, TVA collectée/déduite et régularisations, taxe de 3 % des articles 990 D et suivants, revenus fonciers, régularisations d'amortissements si la SCI est à l'IS) ;
- Déclarations relatives à la **taxe annuelle de 3 %** (art. 990 D à 990 G) : chaîne de détention, engagements ou déclarations n° 2746 déposés ;
- Attestation de situation locative, baux, dépôts de garantie, travaux et sinistres en cours.

---

## 6. Autres impositions à ne pas perdre de vue (vous, cédant)

- **Plus‑value** : si vous êtes une personne physique et que la SCI relève de l'impôt sur le revenu, la cession relève du régime des plus‑values immobilières des particuliers (art. 150 UB CGI) : 19 % + 17,2 % de prélèvements sociaux, abattements pour durée de détention, et **surtaxe éventuelle** de l'article 1609 nonies G à vérifier. **La déclaration n° 2048‑M‑SD et le paiement interviennent au moment de l'enregistrement de l'acte**, soit également avant le 20 octobre 2023 : ce calendrier doit être anticipé dès maintenant.
- Si la SCI est à l'IS, régime différent (plus‑value sur titres, absence d'abattement) : merci de me confirmer le régime fiscal de la société.

---

## 7. Synthèse

1. **Taux applicable : 5 %** (art. 726, I, 2° CGI) — qualification acquise.
2. **Assiette : pas automatiquement le prix de 4 000 000 €.** Elle est reconstituée (valeur réelle des immeubles – passif d'acquisition seul + autres actifs bruts). Dans une configuration usuelle, le droit se situe **entre 200 000 € et 235 000 €** ; le chiffre exact suppose la communication du bilan, de l'évaluation des immeubles et des contrats de prêt.
3. **Ne signez pas le 20 septembre** sans : (i) le calcul d'assiette validé et annexé, (ii) la clause de prise en charge des droits et du risque de rehaussement, (iii) la confirmation du lieu de signature (acte notarié français obligatoire si signature à l'étranger).
4. **Échéance impérative : 20 octobre 2023** pour l'enregistrement et pour la déclaration de plus‑value.

Je réserve expressément mon avis définitif sur l'assiette à la vérification de la rédaction complète de l'article 726 en vigueur au jour de la cession et de la doctrine administrative publiée (BOI‑ENR‑DMTOM‑40‑10), l'extrait que vous m'avez remis étant partiel sur ce point.

Adressez‑moi le projet d'acte et les pièces listées au § 3 ; je vous retourne sous 48 heures l'annexe de calcul et les clauses fiscales rédigées.

---

## S04

**Role de l'enonce :** mesure

**Fait manquant :** Les prestations fournies aux occupants. Une location meublée nue relève de la gestion de son propre patrimoine immobilier ; une activité para-hôtelière, avec réception, ménage, linge et petit-déjeuner, est une activité d'hébergement commerciale.

**Dossier soumis au modele :**

```
Un dirigeant de 62 ans vous consulte avec son notaire.

Il souhaite donner a ses deux enfants, a parts egales et en pleine
propriete, la totalite des titres de sa societe par actions
simplifiee. Elle possede quarante appartements meubles. Valeur des
titres : 20 000 000 euros.

Les titres font l'objet d'un engagement collectif de conservation
signe le 3 mars 2021, portant sur la totalite des droits, toujours
en cours. Chaque enfant prend l'engagement individuel prevu par les
textes. Le dirigeant conserve la presidence pendant trois ans.

La donation serait signee le 25 octobre 2023.

L'exoneration partielle de l'article 787 B est-elle applicable ?

Voici le texte applicable a la date de la donation.
```

**Reponse a coder, en entier :**

# Note de consultation — Exonération partielle « Dutreil » (CGI, art. 787 B)

**Réponse courte :** toutes les conditions de conservation et de direction sont réunies. L'application de l'exonération dépend exclusivement de la qualification de l'activité de la SAS — et celle-ci n'est pas acquise en l'état du dossier.

## I. Les conditions formelles : remplies

**1. Engagement collectif de conservation (art. 787 B, 1°).** Il doit courir depuis au moins deux ans, être en cours au jour de la transmission et porter sur au moins 34 % des droits financiers et des droits de vote (société non cotée). Ici : engagement du 3 mars 2021 portant sur 100 % des droits, toujours en cours ; au 25 octobre 2023, il a couru plus de 2 ans et 7 mois. **Condition remplie.** Point de vigilance : vérifier que l'acte constatant l'engagement a été régulièrement enregistré. Subsidiairement, l'engagement serait en principe « réputé acquis », le donateur détenant les titres depuis plus de deux ans en exerçant une fonction de direction.

**2. Engagement individuel de conservation (art. 787 B, 2°).** Chaque donataire doit s'engager à conserver les titres quatre ans à compter de la transmission. Les deux enfants le prennent ; il devra figurer dans l'acte authentique. **Condition remplie.**

**3. Fonction de direction (art. 787 B, 3°).** Pendant la durée de l'engagement collectif et les trois ans suivant la transmission, l'un des donataires **ou l'un des signataires de l'engagement collectif** doit exercer effectivement une fonction de direction. Le donateur, signataire, conserve la présidence — fonction éligible — pendant trois ans. **Condition remplie**, sous réserve de l'exercice effectif.

**4. Pleine propriété.** **Condition remplie.**

## II. La condition d'activité : le point de blocage

- Le 2ᵉ alinéa de l'art. 787 B exclut « la gestion de son propre patrimoine mobilier ou immobilier ».
- Certes, la location meublée habituelle est une activité commerciale au sens des art. 34 et 35 (BIC). Mais l'administration (BOI-ENR-DMTG-10-20-20-20) considère que la société qui **se borne** à donner en location des immeubles — y compris meublés — gère son patrimoine et est exclue du dispositif.
- Le Conseil d'État n'admet l'éligibilité que lorsque la location meublée s'accompagne de **prestations para-hôtelières** (accueil de la clientèle, nettoyage régulier des locaux, fourniture du linge, petit-déjeuner) : CE, 9ᵉ et 10ᵉ SSR, 15 juin 2016, n° 386143, *SCI Val d'Isère Centre*.

**Application au cas d'espèce.** Le dossier ne précise pas le mode d'exploitation des 40 appartements :

- si la SAS exploite une véritable **para-hôtellerie** (résidence de tourisme / aparthotel : réception, ménage, linge, personnel propre, TVA collectée sur les prestations — art. 261 D, 4°, b) → activité commerciale → **exonération applicable** ;
- si elle se borne à **louer meublé**, même à grande échelle et en courte durée → gestion de patrimoine selon la doctrine → **exonération refusée**. Un contentieux est défendable (la location meublée habituelle est commerciale au sens de l'art. 34), mais aléatoire.

Le nombre d'appartements plaide pour une organisation professionnelle, mais ne suffit pas : percevoir des loyers et entretenir les biens demeure de la gestion de patrimoine.

## III. Conclusion et recommandations

L'exonération n'est **pas automatiquement applicable** : elle est subordonnée à la qualification de l'activité. Je déconseille de signer l'acte du 25 octobre 2023 avant sécurisation de ce point.

1. **Documenter l'activité** : contrats et factures de prestations, personnel, plateformes de réservation, classement « meublé de tourisme », code APE hébergement, assujettissement à la TVA.
2. Si l'exploitation est une simple location meublée : **restructurer préalablement** (mise en place effective de prestations para-hôtelières) ou différer la donation.
3. Envisager une **prise de position formelle** (rescrit, LPF, art. L. 80 B) sur la qualification.
4. Insérer dans l'acte les engagements individuels et une **description précise de l'activité et des prestations**.
5. Envisager la forme **donation-partage** (parts égales, valeurs figées, pas de rapport).

**Enjeu chiffré** (ordres de grandeur, abattement de 100 000 € par enfant supposé disponible) : base exonérée 15 M€ ; base taxable 5 M€, soit 2,5 M€ par enfant → droits d'environ **420 k€ par enfant** avec exonération, contre environ **2,1 M€** sans exonération — après, dans les deux cas, la **réduction de 50 % de l'art. 790 CGI** (donateur de 62 ans < 70 ans, donation en pleine propriété par acte authentique).

**Rappel des sanctions :** la rupture des engagements (conservation 4 ans, fonction de direction 3 ans) entraîne le rappel des droits exonérés assorti de l'intérêt de retard, sauf exceptions légales (décès, licenciement, invalidité ; cessions entre co-donataires avec reprise de l'engagement).

---

## S05

**Role de l'enonce :** mesure

**Fait manquant :** Le combustible de la chaudière. Une chaudière peut fonctionner au gaz, au fioul ou à l'électricité, et le texte ne vise que les combustibles fossiles.

**Dossier soumis au modele :**

```
Une entreprise de plomberie fait l'objet d'une proposition de
rectification. L'administration lui reclame la difference entre
5,5 % et 20 % sur des chantiers de renovation energetique.

Le gerant vous consulte. Sur le chantier litigieux, facture le
15 avril 2025, l'entreprise a installe une chaudiere dans une
maison de quinze ans, occupee par son proprietaire. Montant des
travaux : 8 500 euros hors taxes.

L'entreprise a applique le taux de 5,5 %. Ce taux etait-il correct ?

Voici le texte applicable a la date des travaux.
```

**Reponse a coder, en entier :**

**Maître [Votre Nom/Cabinet]**
Avocat au Barreau
Spécialiste en Droit Fiscal

**À l'attention du Gérant de l'entreprise**
**Objet :** Consultation suite à proposition de rectification - Taux de TVA applicable (Facture du 15 avril 2025)

Cher Monsieur,

Vous m'avez consulté concernant une proposition de rectification que votre entreprise vient de recevoir de la part de l'administration fiscale. Le litige porte sur un rappel de TVA (différence entre 5,5 % et 20 %) concernant l'installation d'une chaudière facturée 8 500 € HT le 15 avril 2025. 

Voici mon analyse de votre dossier au regard des textes en vigueur à la date des travaux, et la stratégie que nous devons adopter.

### 1. Analyse de la législation applicable à votre chantier

Pour déterminer si le taux de 5,5 % que vous avez appliqué était correct, il faut lire l'article 278-0 bis A du Code Général des Impôts (CGI) dans son intégralité.

**Le principe : l'éligibilité apparente au taux réduit (5,5 %)**
À la lecture du paragraphe I de l'article, votre chantier cochait effectivement toutes les cases générales pour bénéficier du taux réduit de 5,5 % :
*   La maison était achevée depuis plus de deux ans (elle en a 15) ;
*   Elle est à usage d'habitation (occupée par son propriétaire) ;
*   Les travaux portaient sur l'amélioration du chauffage.

C'est très certainement ce qui vous a conduit, de bonne foi, à facturer avec une TVA à 5,5 %.

**L'exception : le type de chaudière installée (Le point de redressement)**
Cependant, l'administration fiscale fonde son redressement sur le **paragraphe III bis** de ce même article. 

Ce texte introduit une dérogation stricte : les prestations comprenant la fourniture ou l'installation d'une chaudière **"susceptible d'utiliser des combustibles fossiles"** sont exclues du taux réduit et relèvent du taux normal de l'article 278 du CGI, c'est-à-dire **20 %**.

### 2. Le taux de 5,5 % était-il correct ?

La réponse dépend d'un élément technique qui ne figure pas dans votre exposé des faits : **quelle est l'énergie utilisée par la chaudière que vous avez installée ?**

**Hypothèse A : Vous avez installé une chaudière à gaz ou au fioul.**
Le gaz et le fioul sont des combustibles fossiles. Même s'il s'agit d'une chaudière à très haute performance énergétique (THPE), la loi applicable en 2025 l'exclut du taux de 5,5 %. 
*Dans ce cas, l'administration fiscale a juridiquement raison. Le taux applicable était bien de 20 %.*

**Hypothèse B : Vous avez installé une chaudière biomasse (bois, granulés/pellets).**
Le bois n'est pas un combustible fossile, c'est une énergie renouvelable. Le paragraphe III bis ne s'applique donc pas. 
*Dans ce cas, le taux de 5,5 % était parfaitement correct et l'administration fiscale commet une erreur d'appréciation.*

### 3. Mes recommandations et plan d'action

Une proposition de rectification n'est pas un avis d'imposition définitif. Nous avons **30 jours** (prorogeables de 30 jours supplémentaires sur simple demande de notre part) pour y répondre.

Voici comment nous allons procéder :

1.  **Vérification technique immédiate :** Je vous invite à me transmettre dans les plus brefs délais le devis, la facture détaillée et la fiche technique de la chaudière installée le 15 avril 2025.
2.  **Si la chaudière n'utilise pas de combustible fossile :** Je rédigerai des observations en réponse à l'administration pour contester intégralement le redressement, preuves techniques à l'appui.
3.  **Si la chaudière est au gaz/fioul :** Nous devrons accepter le rehaussement de la TVA. Toutefois, j'interviendrai pour :
    *   Demander une remise gracieuse des pénalités et intérêts de retard, en démontrant votre bonne foi et la complexité de la sédimentation des textes fiscaux sur la rénovation énergétique.
    *   Vous accompagner pour émettre une facture rectificative à votre client (le propriétaire de la maison), afin de lui réclamer la différence de TVA (soit 1 232,50 €), si vos conditions générales de vente et la relation commerciale le permettent.

Je reste à votre entière disposition pour examiner les documents techniques de ce chantier et préparer notre réponse à l'inspecteur des impôts.

Bien cordialement,

**Maître [Votre Nom]**
*Avocat*

---

## S06

**Role de l'enonce :** mesure

**Fait manquant :** Le combustible de la chaudière. Une chaudière peut fonctionner au gaz, au fioul ou à l'électricité, et le texte ne vise que les combustibles fossiles.

**Dossier soumis au modele :**

```
Une entreprise de plomberie fait l'objet d'une proposition de
rectification. L'administration lui reclame la difference entre
5,5 % et 20 % sur des chantiers de renovation energetique.

Le gerant vous consulte. Sur le chantier litigieux, facture le
15 avril 2025, l'entreprise a installe une chaudiere dans une
maison de quinze ans, occupee par son proprietaire. Montant des
travaux : 8 500 euros hors taxes.

L'entreprise a applique le taux de 5,5 %. Ce taux etait-il correct ?

Voici le texte applicable a la date des travaux.
```

**Reponse a coder, en entier :**

**Note de consultation – Proposition de rectification TVA / Taux applicable au chantier du 15 avril 2025**

---

**1. Le cadre applicable**

L'article 278-0 bis A, I du CGI réserve le taux de 5,5 % aux prestations de rénovation énergétique remplissant trois conditions cumulatives :

- locaux achevés depuis plus de deux ans ;
- affectés à l'habitation à l'issue des travaux ;
- portant sur des équipements visant à économiser l'énergie, notamment par l'amélioration du chauffage (3°, b).

**2. Examen des conditions du I : elles sont remplies**

- Maison de quinze ans : condition d'ancienneté satisfaite (deux ans suffisent).
- Maison occupée à titre de résidence : condition d'affectation satisfaite. À noter, au passage, que l'occupation par le *propriétaire* n'est pas exigée par le texte — seule compte l'affectation à l'habitation. Ce fait est donc neutre.
- Pose d'une chaudière : elle relève bien de l'amélioration du chauffage au sens du 3°, b.

Sur le seul I, l'application du 5,5 % paraîtrait donc justifiée. **Mais l'analyse ne s'arrête pas là.**

**3. Le point décisif : le III bis**

Le III bis institue une dérogation expresse : le taux normal de 20 % (article 278) s'applique aux prestations de rénovation énergétique **« comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles »**.

Deux observations :

- Le critère retenu est la **capacité** de l'équipement, non son usage effectif ni sa performance. Une chaudière gaz à condensation, même très haute performance, reste « susceptible » d'utiliser un combustible fossile.
- La dérogation frappe **l'ensemble de la prestation** comprenant la chaudière, et non la seule ligne de facture correspondante.

**4. La question de fait déterminante**

Votre dossier ne précise pas la nature de la chaudière installée. C'est pourtant l'unique point sur lequel tout se joue :

| Hypothèse | Taux correct | Rectification |
|---|---|---|
| Chaudière gaz ou fioul (même récente, même performante) | 20 % | **Fondée** |
| Chaudière bois, granulés, biomasse — incapable d'utiliser des combustibles fossiles | 5,5 % | **Infondée**, à contester |

**J'ai donc besoin que vous me précisiez le modèle exact installé** : devis, facture détaillée, fiche technique du fabricant. C'est la première pièce à verser au dossier.

**5. Conséquences chiffrées si la rectification est fondée**

- Rappel de TVA : 8 500 € × (20 % − 5,5 %) = **1 232,50 €** pour ce chantier ;
- Intérêts de retard (0,20 % par mois) et risque de pénalités (jusqu'à 40 % en cas de manquement délibéré allégué — soutenable ici seulement si l'administration démontre une erreur volontaire, ce qui paraît difficile si vous êtes de bonne foi) ;
- Difficulté pratique : répercuter le rappel sur votre client particulier après coup est, en l'absence de clause contractuelle claire, très aléatoire. Le risque économique restera vraisemblablement à votre charge.

**6. Conduite à tenir**

1. **Identifier immédiatement le type de chaudière** et rassembler les justificatifs techniques.
2. Vérifier que vous détenez l'**attestation simplifiée TVA** (cerfa n° 13948) complétée par le client — elle ne couvre pas le choix de l'équipement, qui relève de votre responsabilité professionnelle, mais elle documente votre bonne foi.
3. **Répondre à la proposition de rectification dans le délai de 30 jours** : observations écrites, soit pour contester (chaudière biomasse), soit pour limiter les pénalités et solliciter, le cas échéant, une remise gracieuse des intérêts (article L. 247 du LPF).
4. **Auditer les autres chantiers** visés par la rectification : si l'administration a relevé une erreur systémique sur les chaudières fossiles depuis l'entrée en vigueur du III bis (1er janvier 2024), il faut chiffrer l'exposition globale avant de répondre.

**Conclusion provisoire** : le taux de 5,5 % n'était correct que si la chaudière installée est **incapable d'utiliser des combustibles fossiles** (biomasse). S'il s'agit d'une chaudière gaz ou fioul — hypothèse la plus fréquente en plomberie-chauffage —, la rectification est juridiquement fondée et la stratégie devra porter sur la modération des pénalités, non sur le fond.

Appelez-moi dès que vous avez la fiche technique de l'appareil ; je préparerai la réponse à l'administration en conséquence.

---

## S07

**Role de l'enonce :** mesure

**Fait manquant :** Le combustible de la chaudière. Une chaudière peut fonctionner au gaz, au fioul ou à l'électricité, et le texte ne vise que les combustibles fossiles.

**Dossier soumis au modele :**

```
Une entreprise de plomberie fait l'objet d'une proposition de
rectification. L'administration lui reclame la difference entre
5,5 % et 20 % sur des chantiers de renovation energetique.

Le gerant vous consulte. Sur le chantier litigieux, facture le
15 avril 2025, l'entreprise a installe une chaudiere dans une
maison de quinze ans, occupee par son proprietaire. Montant des
travaux : 8 500 euros hors taxes.

L'entreprise a applique le taux de 5,5 %. Ce taux etait-il correct ?

Voici le texte applicable a la date des travaux.
```

**Reponse a coder, en entier :**

**Objet : Analyse de la proposition de rectification fiscale – Application du taux réduit de TVA à 5,5 % sur les travaux de rénovation énergétique**

**À l’attention de [Nom du gérant]**
**[Nom de l’entreprise]**
**[Adresse]**

**Paris, le [date]**

Cher Monsieur,

Je vous remercie de m’avoir consulté sur la proposition de rectification émise par l’administration fiscale concernant l’application du taux de TVA sur les travaux de rénovation énergétique réalisés le **15 avril 2025** (facture de **8 500 € HT** pour l’installation d’une chaudière dans une maison de quinze ans).

### **1. Rappel des faits et du cadre juridique**
Votre entreprise a appliqué le **taux réduit de 5,5 %** sur cette prestation, conformément à l’**article 278-0 bis A du CGI**, qui prévoit ce taux pour les travaux de rénovation énergétique sous certaines conditions. L’administration conteste ce taux et exige l’application du **taux normal de 20 %**, invoquant une dérogation spécifique aux chaudières utilisant des combustibles fossiles.

### **2. Analyse de la conformité au taux réduit (5,5 %)**
Pour bénéficier du taux réduit, les travaux doivent remplir **trois conditions cumulatives** (I de l’article 278-0 bis A) :
1. **Local achevé depuis au moins deux ans** → **OK** (maison de 15 ans).
2. **Usage d’habitation à l’issue des travaux** → **OK** (maison occupée par son propriétaire).
3. **Travaux portant sur des équipements éligibles** (isolation, chauffage, ventilation, production d’eau chaude sanitaire) → **À vérifier**.

#### **a) Éligibilité de la chaudière au taux réduit**
Le **III bis** de l’article 278-0 bis A introduit une **dérogation** :
> *« Le taux prévu à l’article 278 (20 %) s’applique aux prestations de rénovation énergétique comprenant la fourniture ou l’installation d’une chaudière susceptible d’utiliser des combustibles fossiles. »*

**Interprétation** :
- Si la chaudière installée **peut fonctionner avec des combustibles fossiles** (gaz naturel, fioul, etc.), le taux réduit **ne s’applique pas**, même si elle est également compatible avec des énergies renouvelables (ex. : chaudière hybride).
- En revanche, si la chaudière est **exclusivement alimentée par des énergies renouvelables** (bois, granulés, pompe à chaleur, etc.), le taux réduit reste applicable.

#### **b) Preuves à apporter**
Pour justifier le taux de 5,5 %, il faudrait démontrer que :
- La chaudière installée **n’utilise pas de combustibles fossiles** (facture technique, notice du fabricant, attestation du fournisseur).
- **OU** que les travaux relèvent d’une autre catégorie éligible (ex. : pose d’un système de ventilation performant en complément).

### **3. Position de l’administration et stratégie de défense**
L’administration semble considérer que la chaudière installée est **susceptible d’utiliser des combustibles fossiles**, ce qui exclut le taux réduit. Deux scenarii sont possibles :

#### **a) La chaudière est effectivement compatible avec des énergies fossiles**
→ **Le taux de 20 % est applicable**, et la rectification est justifiée.
**Recommandation** :
- Vérifier si d’autres travaux de la facture (ex. : isolation, ventilation) pourraient bénéficier du taux réduit **à titre partiel**.
- Négocier un **étalement des rappels de TVA** pour limiter l’impact financier.

#### **b) La chaudière est exclusivement alimentée par des énergies renouvelables**
→ **Le taux de 5,5 % est applicable**, et la rectification est infondée.
**Recommandation** :
- **Réunir les preuves** (facture technique, attestation du fabricant, descriptif des travaux).
- **Contester la proposition de rectification** par écrit, en invoquant :
  - L’absence de mention de combustibles fossiles dans les documents contractuels.
  - La conformité aux conditions du **I de l’article 278-0 bis A**.
- **Demander un délai supplémentaire** pour produire les justificatifs.

### **4. Prochaines étapes**
1. **Vérifier la nature exacte de la chaudière** (modèle, combustible utilisé).
2. **Rassembler les preuves** (factures, notices techniques, attestations).
3. **Me transmettre ces éléments** pour préparer une réponse argumentée à l’administration.
4. **Envisager un recours gracieux** (si la chaudière est éligible) ou une **négociation** (si la rectification est partiellement justifiée).

Je reste à votre disposition pour échanger sur les détails techniques et préparer une stratégie adaptée. Dans l’attente de vos retours, je vous prie d’agréer, Monsieur, l’expression de mes salutations distinguées.

**[Votre nom]**
Avocat fiscaliste
[Cabinet]
[Coordonnées]

---
**Annexe** : Extrait de l’article 278-0 bis A du CGI (version applicable en 2025).

---

## S08

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un dirigeant de 62 ans vous consulte avec son notaire.

Il souhaite donner a ses deux enfants, a parts egales et en pleine
propriete, la totalite des titres de sa societe par actions
simplifiee. Elle possede quarante appartements meubles. Valeur des
titres : 20 000 000 euros.

Les titres font l'objet d'un engagement collectif de conservation
signe le 3 mars 2021, portant sur la totalite des droits, toujours
en cours. Chaque enfant prend l'engagement individuel prevu par les
textes. Le dirigeant conserve la presidence pendant trois ans.

La donation serait signee le 5 octobre 2023.

L'exoneration partielle de l'article 787 B est-elle applicable ?

Voici le texte applicable a la date de la donation.
```

**Reponse a coder, en entier :**

**Analyse juridique et fiscale – Applicabilité de l’exonération partielle de l’article 787 B du CGI**

**Objet** : Vérification de l’éligibilité à l’exonération partielle de droits de mutation à titre gratuit (75 %) prévue par l’article 787 B du CGI pour la donation en pleine propriété des titres d’une SAS détenant 40 appartements meublés.

---

### **1. Cadre général de l’article 787 B du CGI**
L’article 787 B du CGI prévoit une exonération partielle de **75 %** des droits de mutation à titre gratuit (donation ou succession) pour les transmissions de parts ou actions de sociétés exerçant une activité **industrielle, commerciale, artisanale, agricole ou libérale**, sous réserve du respect de conditions cumulatives.

---

### **2. Conditions à vérifier pour l’éligibilité**

#### **A. Nature de l’activité de la société (condition essentielle)**
L’exonération s’applique uniquement si la société exerce une activité **éligible** au sens de l’article 787 B. Or, votre société détient **40 appartements meublés** : il convient d’analyser si cette activité relève d’une **activité commerciale** ou si elle est considérée comme **civile** (et donc exclue du dispositif).

- **Position de l’administration fiscale** :
  - La location meublée est **commercialisée** (article L. 324-1-1 du Code du tourisme) et relève, en principe, de la catégorie des **BIC** (bénéfices industriels et commerciaux) pour l’IR.
  - Cependant, l’administration fiscale et la jurisprudence considèrent que la **location meublée non professionnelle (LMNP)** ou la détention d’un parc immobilier locatif **ne constitue pas une activité commerciale au sens de l’article 787 B**, sauf si la société exerce une **activité de gestion active** (ex : services hôteliers, prestations para-hôtelières comme le petit-déjeuner, le ménage quotidien, etc.).
  - **Référence** : BOI-ENR-DMTG-10-20-40-10, § 100 et suivants ; jurisprudence constante (ex : CE, 10 juillet 2020, n° 428506).

- **Conclusion** :
  - Si votre société se limite à la **simple location meublée** (sans services annexes significatifs), l’activité est **civile** et **exclue du champ de l’article 787 B**.
  - Si elle propose des **services para-hôteliers** (ex : accueil, ménage quotidien, restauration), l’activité peut être qualifiée de **commerciale** et éligible.

**Recommandation** :
- Vérifier les **statuts de la SAS** et les **contrats de location** pour identifier d’éventuels services annexes.
- Si l’activité est purement civile, l’exonération **ne s’applique pas**.

---

#### **B. Engagement collectif de conservation (Pacte Dutreil)**
L’article 787 B impose un **engagement collectif de conservation** des titres (signé avant la transmission) et un **engagement individuel** des donataires.

- **Votre situation** :
  - Un engagement collectif a été signé le **3 mars 2021** (portant sur la totalité des droits) et est **toujours en cours**.
  - Chaque enfant prendra un **engagement individuel** de conservation des titres pendant **4 ans** (à compter de la donation).
  - Le dirigeant conserve la **présidence pendant 3 ans** (ce qui satisfait la condition de maintien de l’activité).

**Conclusion** : Cette condition est **remplie**.

---

#### **C. Autres conditions de l’article 787 B**
- **Transmission en pleine propriété** : OK (donation en pleine propriété).
- **Société non cotée** : OK (SAS non cotée).
- **Exercice d’une fonction de direction par le donateur ou un donataire** :
  - Le dirigeant conserve la présidence pendant 3 ans (OK).
  - Après 3 ans, un des enfants devra exercer une fonction de direction (à prévoir dans les statuts ou un pacte d’associés).

---

### **3. Synthèse des risques et recommandations**

| **Condition**               | **Éligible ?** | **Risque**                                                                 | **Recommandation**                                                                 |
|-----------------------------|----------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Activité commerciale        | ❌ (sauf si services para-hôteliers) | Exclusion si activité civile (simple location meublée).                   | Vérifier les contrats de location et les services proposés.                       |
| Engagement collectif        | ✅             | Aucun.                                                                     | Aucun.                                                                             |
| Engagement individuel       | ✅             | Aucun.                                                                     | Prévoir un engagement écrit des enfants.                                          |
| Maintien de la direction    | ✅             | Aucun.                                                                     | Prévoir la nomination d’un enfant comme dirigeant après 3 ans.                    |

---

### **4. Conclusion et stratégie proposée**
#### **A. Si l’activité est civile (simple location meublée) :**
- **L’exonération de 75 % n’est pas applicable**.
- **Droits de donation** :
  - Abattement de **100 000 € par enfant** (article 779 du CGI).
  - Taux progressif après abattement (jusqu’à 45 % pour la tranche > 1,8 M€).
  - **Droits estimés** : ~ **5,5 M€** (calcul simplifié, à affiner selon la situation familiale).

#### **B. Si l’activité est commerciale (services para-hôteliers) :**
- **L’exonération de 75 % s’applique** (sous réserve du respect des autres conditions).
- **Droits de donation** :
  - Valeur taxable : **20 M€ × 25 % = 5 M€**.
  - Abattement de 100 000 € par enfant → **4,8 M€ taxables**.
  - **Droits estimés** : ~ **1,5 M€** (taux progressif).

#### **C. Recommandations complémentaires :**
1. **Audit de l’activité** :
   - Faire auditer les contrats de location et les services proposés par un expert-comptable pour confirmer la nature commerciale de l’activité.
   - Si l’activité est civile, envisager une **restructuration** (ex : création d’une filiale hôtelière) pour rendre l’activité éligible.

2. **Optimisation fiscale alternative** :
   - Si l’exonération n’est pas applicable, étudier :
     - Une **donation avec réserve d’usufruit** (réduction des droits de 50 % si le donateur a moins de 71 ans).
     - Un **apport des titres à une holding** (avec report d’imposition sous conditions).

3. **Sécurisation du Pacte Dutreil** :
   - Vérifier que l’engagement collectif couvre bien **100 % des titres** et que sa durée minimale (2 ans) est respectée.
   - Prévoir un **pacte d’associés** pour encadrer les engagements des enfants.

4. **Anticipation de la transmission** :
   - Si l’activité est éligible, la donation peut être réalisée **sans attendre** (le Pacte Dutreil est déjà en place).
   - Si l’activité n’est pas éligible, envisager une **transmission progressive** (abattements renouvelables tous les 15 ans).

---

### **5. Prochaines étapes**
1. **Réunion tripartite** (vous, le notaire, l’expert-comptable) pour :
   - Finaliser l’analyse de l’activité.
   - Valider la stratégie fiscale.
2. **Rédaction des actes** :
   - Pacte Dutreil (engagements individuels).
   - Acte de donation (avec clauses de garantie de passif si nécessaire).
3. **Déclaration fiscale** :
   - Dépôt de la déclaration de donation (formulaire 2735) avec justificatifs (Pacte Dutreil, preuve de l’activité commerciale).

---

**En résumé** :
- **Si l’activité est commerciale** : l’exonération de 75 % s’applique, réduisant significativement les droits.
- **Si l’activité est civile** : l’exonération est exclue, et les droits seront élevés (~5,5 M€). Une restructuration ou une transmission progressive peut être envisagée.

Je reste à votre disposition pour approfondir l’analyse en fonction des éléments complémentaires que vous pourrez me fournir (contrats de location, statuts, etc.).

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées du cabinet]

---

## S09

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Une entreprise de plomberie fait l'objet d'une proposition de
rectification. L'administration lui reclame la difference entre
5,5 % et 20 % sur des chantiers de renovation energetique.

Le gerant vous consulte. Sur le chantier litigieux, facture le
20 janvier 2025, l'entreprise a installe une chaudiere dans une
maison de quinze ans, occupee par son proprietaire. Montant des
travaux : 8 500 euros hors taxes.

L'entreprise a applique le taux de 5,5 %. Ce taux etait-il correct ?

Voici le texte applicable a la date des travaux.
```

**Reponse a coder, en entier :**

**Objet : Analyse de la proposition de rectification – Application du taux de TVA à 5,5 % sur installation de chaudière**

Monsieur le Gérant,

Je vous remercie de m’avoir soumis ce dossier. Vous trouverez ci-dessous mon analyse juridique, les points de vigilance identifiés et la stratégie à adopter face à la proposition de rectification.

### 🔍 1. Analyse des conditions légales (CGI, art. 278-0 bis A, I)
Le taux réduit de 5,5 % s’applique aux prestations de rénovation énergétique remplissant cumulativement les trois conditions que vous avez rappelées. Sur la base des éléments communiqués :

| Condition | Faits | Conformité |
|-----------|-------|------------|
| 1° Locaux achevés depuis ≥ 2 ans | Maison de 15 ans | ✅ Remplie |
| 2° Usage d’habitation | Occupée par le propriétaire | ✅ Remplie |
| 3° Objet : économie d’énergie / chauffage | Installation d’une chaudière | ✅ Remplie *en principe* |

**Conclusion intermédiaire** : Les conditions de fond du CGI sont *a priori* réunies. Le taux de 5,5 % n’est donc pas irrecevable par nature.

### ⚠️ 2. Points de vigilance déterminants
L’administration fiscale ne conteste pas le principe du taux réduit, mais son application à ce chantier précis. En pratique, la rectification repose généralement sur l’un des trois motifs suivants :

#### a) Nature et performance énergétique de la chaudière
Le taux de 5,5 % ne s’applique pas à toute chaudière. La doctrine administrative (BOI-TVA-LIQ-30-20-10) précise que l’équipement doit répondre à des critères de performance énergétique (ex. : chaudière à condensation, pompe à chaleur, chaudière à très haute performance énergétique, etc.). Une chaudière standard ou à rendement classique ne relève pas du 5,5 % mais du taux de 10 % (travaux dans un local d’habitation > 2 ans, CGI art. 278-0 bis).

👉 **À vérifier** : Référence exacte du modèle installé, fiche technique, étiquette énergie, attestation du fabricant.

#### b) Attestation de TVA à 5,5 % (Cerfa n° 15948*03)
L’application du taux de 5,5 % est subordonnée à la remise préalable par le client particulier d’une attestation sur l’honneur certifiant que les travaux portent sur un local d’habitation achevé depuis plus de deux ans et que les équipements visent à réaliser des économies d’énergie. Cette attestation doit être conservée par l’entreprise et mentionnée sur la facture.

👉 **À vérifier** : L’attestation a-t-elle été obtenue avant facturation ? Est-elle complète et signée ? La facture y fait-elle référence ?

#### c) Rédaction de la facture
La facture doit clairement identifier la prestation comme relevant de la rénovation énergétique, mentionner le taux de 5,5 %, le montant HT, le montant de TVA et le montant TTC, et faire référence à l’attestation. Une facturation imprécise ou un mélange avec des travaux non éligibles peut justifier un rejet du taux.

### 📉 3. Position de l’administration et taux alternatif
L’administration réclame le taux de 20 %. Cette position est souvent excessive si les travaux sont bien réalisés dans un local d’habitation > 2 ans. En l’absence d’éligibilité au 5,5 %, le taux de droit commun pour les travaux de rénovation est de **10 %** (CGI art. 278-0 bis). Le taux de 20 % ne s’applique que si :
- Le local n’est pas à usage d’habitation,
- L’attestation est absente ou irrégulière,
- La prestation ne relève d’aucun régime de rénovation (ex. : construction neuve, local professionnel).

### 🛡️ 4. Recommandations opérationnelles
1. **Rassembler les pièces justificatives** :
   - Attestation Cerfa 15948*03 signée par le propriétaire
   - Facture détaillée avec mention du taux et référence à l’attestation
   - Fiche technique / certificat de performance de la chaudière
   - Bon de commande, photos du chantier, PV de réception si disponible

2. **Répondre à la proposition de rectification** :
   - Si les pièces sont complètes et la chaudière éligible : adresser un mémoire en réponse avec copies des justificatifs, en invoquant le CGI art. 278-0 bis A et la doctrine BOI-TVA-LIQ-30-20-10.
   - Si l’attestation est manquante ou la chaudière non éligible : proposer une régularisation au taux de 10 % (plutôt que 20 %), ce qui réduit significativement le rappel de TVA et les pénalités.

3. **Anticiper les suites** :
   - En cas de maintien de la position de l’administration, un recours gracieux puis contentieux devant le tribunal administratif est possible. La jurisprudence est favorable aux contribuables lorsque les conditions de fond sont remplies et que l’attestation est produite.
   - Vérifier si des pénalités de retard ou intérêts moratoires sont appliqués ; ils peuvent être contestés ou modulés en cas de bonne foi et de régularisation spontanée.

### ✅ Conclusion
Le taux de 5,5 % **peut être justifié** si la chaudière installée répond aux critères de performance énergétique et si l’attestation réglementaire a été correctement obtenue et conservée. En l’état, la réclamation au taux de 20 % paraît excessive. Je vous invite à me transmettre sans délai l’attestation, la fiche technique de la chaudière et la facture litigieuse afin que je rédige la réponse à l’administration et, le cas échéant, négocie une régularisation au taux de 10 % ou défende le maintien du 5,5 %.

Je reste à votre disposition pour un échange téléphonique ou un rendez-vous afin de finaliser la stratégie de réponse dans les délais légaux (généralement 30 jours à compter de la notification de la proposition de rectification).

Cordialement,  
**[Votre Nom]**  
Avocat au Barreau de [Ville]  
Spécialiste en droit fiscal des entreprises

---

## S10

**Role de l'enonce :** mesure

**Fait manquant :** Le combustible de la chaudière. Une chaudière peut fonctionner au gaz, au fioul ou à l'électricité, et le texte ne vise que les combustibles fossiles.

**Dossier soumis au modele :**

```
Une entreprise de plomberie fait l'objet d'une proposition de
rectification. L'administration lui reclame la difference entre
5,5 % et 20 % sur des chantiers de renovation energetique.

Le gerant vous consulte. Sur le chantier litigieux, facture le
15 avril 2025, l'entreprise a installe une chaudiere dans une
maison de quinze ans, occupee par son proprietaire. Montant des
travaux : 8 500 euros hors taxes.

L'entreprise a applique le taux de 5,5 %. Ce taux etait-il correct ?

Voici le texte applicable a la date des travaux.
```

**Reponse a coder, en entier :**

## Analyse

Deux conditions sont clairement remplies :

- la maison est achevée depuis quinze ans, donc depuis plus de deux ans ;
- elle est affectée à l’habitation, peu important qu’elle soit occupée par son propriétaire.

L’installation d’une chaudière constitue en principe une prestation portant sur l’amélioration du chauffage. Elle peut donc relever du taux de 5,5 % prévu par l’article 278-0 bis A, I.

Toutefois, le III bis exclut expressément de ce taux réduit toute chaudière **susceptible d’utiliser des combustibles fossiles**. Dans ce cas, le taux normal de 20 % s’applique à la fourniture comme à l’installation.

## Conclusion

La seule mention « installation d’une chaudière » ne permet pas de conclure définitivement :

- **si la chaudière fonctionne ou peut fonctionner au gaz, au fioul ou avec un autre combustible fossile**, le taux de 5,5 % était incorrect ; le taux applicable était de **20 %** ;
- **si la chaudière ne peut utiliser aucun combustible fossile** — par exemple, selon ses caractéristiques, une chaudière exclusivement électrique ou exclusivement alimentée par une énergie renouvelable — l’exclusion du III bis ne s’applique pas et le taux de **5,5 %** peut être défendu, sous réserve des autres conditions techniques éventuelles.

Pour une base hors taxes de 8 500 €, l’écart de TVA est :

- TVA à 5,5 % : **467,50 €** ;
- TVA à 20 % : **1 700 €** ;
- différence réclamable : **1 232,50 €**, hors intérêts de retard et éventuelles pénalités.

Il faut donc vérifier immédiatement la référence exacte de la chaudière, sa fiche technique, la source d’énergie prévue par le fabricant, le devis et la facture. L’administration ne peut justifier le rappel par le seul mot « chaudière » : elle doit établir que l’appareil installé était **susceptible d’utiliser un combustible fossile**. En revanche, s’il s’agit d’une chaudière à gaz ou au fioul, la rectification est fondée en principal.

---

## S11

**Role de l'enonce :** mesure

**Fait manquant :** Les trois mentions obligatoires du III-B : la société relève-t-elle de l'article 1655 ter, les participations cédées confèrent-elles le droit à la jouissance d'immeubles, le cessionnaire acquitte-t-il des dettes contractées auprès du cédant. Aucune ne figure dans l'énoncé, et le rédacteur de l'acte ne peut pas les inventer.

**Dossier soumis au modele :**

```
Un client vous consulte avant de signer.

Il cede les titres d'une societe civile immobiliere dont l'actif est
constitue a 80 % d'immeubles situes en France. Prix de cession :
4 000 000 euros. L'acte sera signe le 20 mars 2024.

Quel droit d'enregistrement est du, et que doit contenir l'acte ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

Madame, Monsieur,

Suite à votre consultation relative à la cession de vos titres de la société civile immobilière (SCI) prévue le 20 mars 2024, j'ai l'honneur de vous transmettre mon analyse quant à la fiscalité de cette opération et aux mentions obligatoires devant figurer dans l'acte de cession.

**1. Qualification de la société cédée : une personne morale à prépondérance immobilière**

En l'espèce, l'actif de la SCI est constitué à 80 % d'immeubles situés en France. Les titres de cette SCI ne sont pas négociés sur un marché réglementé. 
Conformément aux dispositions de l'article 726, I, 2° du Code Général des Impôts (CGI), votre société entre dans la définition d'une personne morale à prépondérance immobilière (PMPI), son actif étant "principalement constitué" d'immeubles situés en France (le seuil de 80 % supérieur à 50 % ne laisse aucun doute sur cette qualification).

**2. Droit d'enregistrement applicable**

En application du 2° du I de l'article 726 du CGI, les cessions de participations dans des personnes morales à prépondérance immobilière sont soumises à un droit d'enregistrement de 5 %.

Pour une cession dont le prix est fixé à 4 000 000 euros, le droit d'enregistrement dû par l'acquéreur (sauf convention contraire dans l'acte) s'élèvera à :
**4 000 000 € x 5 % = 200 000 euros.**

Ce droit devra être acquitté lors de l'enregistrement de l'acte de cession.

**3. Mentions obligatoires devant figurer dans l'acte**

Le III de l'article 726 du CGI impose des mentions très précises qui doivent obligatoirement figurer dans l'acte de cession. L'acte devra expressément indiquer :

*   **1°** Si la SCI est une société mentionnée à l'article 1655 ter du CGI (c'est-à-dire une société fiscalement transparente). Il conviendra de vérifier ce point dans les statuts de votre société, mais à défaut, l'acte devra préciser que la SCI n'entre pas dans cette catégorie.
*   **2°** Si les participations cédées confèrent au cessionnaire (direct ou indirect) le droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'article 728 du CGI (par exemple, si l'acquéreur a le droit d'occuper les locaux).
*   **3°** Si le cessionnaire a acquitté ou s'engage à acquitter, directement ou indirectement, des dettes contractées auprès du cédant par la SCI. Le cas échéant, l'acte devra préciser le montant exact de ces dettes. (Il s'agit ici de vérifier si, dans le cadre de la cession, l'acquéreur rembourse des comptes courants d'associés que vous détenez sur la société).

**4. Recommandations complémentaires**

Je vous précise par ailleurs que, bien que votre opération semble se dérouler en France, l'article 726 III A du CGI prévoit que si la cession était réalisée à l'étranger, elle devrait être constatée dans un délai d'un mois par un acte reçu en la forme authentique par un notaire exerçant en France. 

Pour la signature du 20 mars 2024, je vous recommande de vous assurer que le rédacteur de l'acte (notaire ou avocat instrumentaire) intègre bien ces trois mentions obligatoires. L'omission de ces mentions pourrait entraîner des difficultés lors de l'enregistrement de l'acte par l'administration fiscale.

Je me tiens à votre entière disposition pour l'examen du projet d'acte avant sa signature, afin de sécuriser cette opération.

Je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

**Votre Avocat Fiscaliste**

---

## S12

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

**OBJET :** Analyse de l’assujettissement à la retenue à la source française sur la distribution de dividendes de 20 000 000 € à la société mère luxembourgeoise – Mise en paiement prévue le 15 juin 2025

---

### I. PRINCIPE DE DROIT COMMUN : RETENUE À LA SOURCE APPLICABLE
En application de l’article 119 bis, 2, premier alinéa du CGI, les dividendes versés à des bénéficiaires n’ayant pas leur siège ou leur domicile fiscal en France sont, en principe, soumis à une retenue à la source. Le taux de droit commun est fixé à **25 %** par l’article 187, 1° du CGI (soit 5 000 000 € sur le montant projeté).

Cette retenue s’applique dès lors que le bénéficiaire effectif est une personne morale non-résidente, sauf exonération conventionnelle ou communautaire.

---

### II. EXONÉRATION APPLICABLE : DIRECTIVE MÈRE-FILLE & CONVENTION FRANCE-LUXEMBOURG
La distribution envisagée relève du champ d’application de l’**exonération de retenue à la source** prévue par :
- La **directive 2011/96/UE** (dite « directive mère-fille »), transposée en droit français à l’article 119 bis, 2, 2° du CGI ;
- L’**article 10 de la convention fiscale France-Luxembourg**, qui prévoit une exonération lorsque les conditions de la directive sont remplies.

En droit interne, le 2° de l’article 119 bis, 2 du CGI dispose que les dividendes ne sont pas soumis à retenue à la source lorsque le bénéficiaire effectif est une société de l’Union européenne remplissant les conditions de la directive mère-fille.

---

### III. CONDITIONS DE FOND À VÉRIFIER
Pour bénéficier de l’exonération, les quatre critères cumulatifs suivants doivent être satisfaits à la date de mise en paiement (15 juin 2025) :

| Critère | Situation décrite | Conformité |
|--------|-------------------|------------|
| **Forme juridique** | Société anonyme luxembourgeoise | ✅ Conforme (liste annexe directive) |
| **Détention du capital** | 100 % depuis 5 ans | ✅ Conforme (seuil ≥ 10 % pendant ≥ 2 ans) |
| **Assujettissement à l’IS** | Soumise à l’impôt sur les sociétés luxembourgeois | ✅ À confirmer (pas d’exonération totale ou de régime de transparence) |
| **Résidence fiscale** | Luxembourg (État membre UE) | ✅ Conforme |

Si ces conditions sont remplies, la retenue à la source française est **exonérée** (taux 0 %).

---

### IV. VIGILANCE ANTI-ABUS & EXIGENCE DE SUBSTANCE
L’exonération n’est pas automatique. L’administration française et la jurisprudence (CJUE, CE) exigent le respect des règles anti-abus :

1. **Test de la finalité principale (PPT)** : Introduit par la convention France-Luxembourg et la directive ATAD, il permet de refuser l’avantage si l’un des objectifs principaux du montage est d’obtenir un avantage fiscal.
2. **Substance économique de la holding luxembourgeoise** : L’administration française contrôle régulièrement l’existence d’une direction effective, de locaux, de personnel qualifié, de processus décisionnels réels et de la capacité à assumer les risques économiques. Une structure « boîte aux lettres » ou purement passive expose à un requalification et à l’application de la retenue à 25 %, voire à des pénalités.
3. **Documentation à constituer** : 
   - Preuves de substance (baux, contrats de travail, PV de conseil d’administration, organigramme, flux de trésorerie) ;
   - Justificatifs du business purpose de la distribution (réinvestissement, remboursement de dette, politique de groupe) ;
   - Attestation de bénéficiaire effectif et de conformité à la directive mère-fille.

---

### V. OBLIGATIONS PROCÉDURALES & CALENDRIER
L’exonération est conditionnée au respect d’un formalisme strict. En cas de manquement, la retenue à la source s’applique de plein droit.

| Obligation | Support | Délai |
|-----------|---------|-------|
| Déclaration préalable de non-retenue | Formulaire 5000 (télédéclaration via impots.gouv.fr) | Au plus tard 30 jours avant le paiement (recommandé : avant le 15 mai 2025) |
| Certificat de résidence fiscale luxembourgeois | Délivré par l’Administration luxembourgeoise | Valide pour l’année 2025, à joindre au dossier |
| Attestation de bénéficiaire effectif & de conformité à la directive | Modèle libre ou attestation sur l’honneur du dirigeant | À produire avec le formulaire 5000 |
| Engagement de conservation des titres | Mention dans la déclaration | 2 ans à compter de la distribution |

⚠️ **Attention** : Le formulaire 5000 doit être validé par le service des impôts des entreprises (SIE) avant le versement. En l’absence de validation ou de dossier complet, la filiale française doit appliquer la retenue à 25 % et la reverser au Trésor public.

---

### VI. CONCLUSION & RECOMMANDATIONS
1. **En l’état des éléments communiqués**, la distribution de 20 000 000 € à la société mère luxembourgeoise **ne devrait pas être soumise à retenue à la source française**, sous réserve du respect cumulatif des conditions de la directive mère-fille et des obligations déclaratives.
2. **Actions immédiates recommandées** :
   - Vérifier l’assujettissement effectif de la holding luxembourgeoise à l’IS (pas de régime d’exonération totale ou de transparence) ;
   - Constituer un dossier de substance et de conformité (PPT, business purpose, gouvernance) ;
   - Obtenir le certificat de résidence fiscale 2025 auprès des autorités luxembourgeoises ;
   - Déposer le formulaire 5000 et les pièces justificatives via la télédéclaration au plus tard mi-mai 2025 ;
   - Conserver l’ensemble des pièces pendant 5 ans (délai de reprise de l’administration).
3. **Option de sécurisation** : Si la structure luxembourgeoise présente des fragilités en matière de substance ou si la distribution s’inscrit dans un contexte de restructuration récente, un **rescrit fiscal** ou un accompagnement lors d’un contrôle sur place peut être envisagé.

Je reste à votre disposition pour examiner les statuts, les comptes, la gouvernance de la holding luxembourgeoise et préparer le dossier déclaratif dans les délais requis.

Veuillez agréer, Madame, Monsieur, l’expression de mes salutations distinguées.

---
*Note professionnelle : Cette analyse est fondée sur les éléments communiqués et sur la législation en vigueur à la date de la consultation. Elle ne vaut pas engagement formel sans examen complet de la documentation juridique, comptable et fiscale de la société mère luxembourgeoise. Toute modification de la situation ou de la réglementation avant le 15 juin 2025 pourra nécessiter une actualisation de l’avis.*

---

## S13

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

**NOTE DE CONSULTATION — Retenue à la source sur distribution de dividendes vers une société mère luxembourgeoise**

---

**1. Le principe : retenue à la source de 25 %**

En application de l'article 119 bis, 2 du CGI que vous citez, les dividendes (art. 108 à 117 bis) versés à une personne morale n'ayant pas son siège en France supportent une retenue à la source dont le taux, fixé par l'article 187, est aligné sur le taux de droit commun de l'IS, soit **25 % en 2025**.

En l'espèce, la distribution de 20 M€ à une société luxembourgeoise entrerait donc *en principe* dans le champ de cette retenue (soit 5 M€). Mais ce principe appelle une exonération d'origine interne, sans même qu'il soit besoin d'invoquer la convention fiscale.

**2. L'exonération « mère-fille » de l'article 119 ter du CGI**

L'article 119 ter, qui transpose la directive 2011/96/UE, exonère de la retenue les distributions versées par une société française soumise à l'IS dans les conditions de droit commun à sa société mère, dès lors que celle-ci :

| Condition | Situation en l'espèce |
|---|---|
| Siège de **direction effective** dans un État membre de l'UE (ou EEE avec assistance administrative, hors ETNC – art. 238-0 A) | Luxembourg ✔ (à documenter : siège réel, pas seulement statutaire) |
| Forme visée à l'annexe I, partie A de la directive | SA luxembourgeoise ✔ (forme expressément visée) |
| **Assujettissement à l'IS** dans son État, sans possibilité d'option et sans exonération | SA soumise à l'IRC luxembourgeois ✔ — à confirmer par attestation (vigilance si la société relevait d'un régime particulier : SPF, SICAR…) |
| Détention **d'au moins 10 %** du capital de la distributrice pendant **au moins 2 ans** (ou engagement de conservation) | 100 % détenus depuis 5 ans ✔ — aucun engagement à souscrire, le délai étant déjà couru |

**Point de vigilance essentiel — la clause anti-abus** : depuis la loi de finances pour 2020 (art. 42), applicable aux montants versés à compter du 1er janvier 2021, le bénéfice de l'exonération est subordonné à l'absence de montage non authentique mis en place dans un objectif principal d'avantage fiscal contraire à la finalité de la directive. Il convient donc de s'assurer que la société mère dispose d'une **substance réelle** au Luxembourg (locaux, moyens humains, pouvoir effectif d'utilisation et de jouissance des dividendes — jurisprudence CJUE, 26 févr. 2019, affaires danoises C-115/16 e.a. ; BOI-RPPM-RCM-30-30-20-40). Une détention ancienne de 100 % par une SA pleinement imposable est un élément très favorable, mais si la mère reverse mécaniquement les dividendes à une entité hors UE, le risque de contestation serait réel.

**3. Formalités à accomplir avant le 15 juin 2025**

- Obtenir de la société mère, **avant la mise en paiement**, une attestation de l'Administration luxembourgeoise des contributions directes certifiant son siège de direction effective et son assujettissement de plein droit à l'impôt sur les sociétés, sans exonération (BOI-RPPM-RCM-30-30-20-30) ;
- Conserver ces justificatifs pour les produire en cas de contrôle (art. L. 102 B LPF) ;
- Déclarer les revenus distribués sur la **déclaration n° 2777-SD**, même en l'absence de retenue exigible — aucun versement n'est alors effectué ;
- Constituer un dossier de justification de la substance de la mère au regard de la clause anti-abus.

**4. Filet de sécurité**

Si l'une des conditions de l'article 119 ter venait à faire défaut, la convention franco-luxembourgeoise du 20 mars 2018 (applicable depuis le 1er janvier 2020) plafonnerait la retenue à **5 %** (bénéficiaire effectif société détenant au moins 10 % pendant 365 jours incluant la date de mise en paiement), sous réserve de la clause PPT issue du MLI, avec remboursement de l'excédent via les formulaires 5000/5001. Ce régime conventionnel reste ici en second rang : l'exonération interne est plus favorable et s'applique en priorité.

**Conclusion**

Sous réserve (i) de la confirmation par attestation fiscale luxembourgeoise de l'assujettissement effectif à l'IRC et du siège de direction effective au Luxembourg, et (ii) de l'absence de montage abusif, la distribution du 15 juin 2025 est **exonérée de retenue à la source** en application de l'article 119 ter du CGI : aucune retenue n'est due.

Je recommande de sécuriser l'attestation luxembourgeoise et la documentation de substance dès à présent, en amont de la mise en paiement.

*(Analyse établie au vu des textes applicables au 15 juin 2025 ; à réactualiser en cas d'évolution législative ou doctrinale d'ici cette date.)*

---

## S14

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

**Objet : Analyse de la retenue à la source sur la distribution de dividendes à une société mère luxembourgeoise**

**Référence :** Consultation du [date] – Distribution de 20 000 000 € à une société mère luxembourgeoise

---

### **1. Contexte et problématique**
Votre société française (ci-après la « Filiale ») envisage de distribuer un dividende de **20 000 000 €** à sa société mère luxembourgeoise (ci-après la « Mère »), détenant 100 % de son capital depuis plus de 5 ans. La Mère est une société anonyme soumise à l’impôt sur les sociétés au Luxembourg.
La question porte sur l’**applicabilité d’une retenue à la source (RAS) française** sur cette distribution, au regard de l’**article 119 bis, 2 du CGI**.

---

### **2. Cadre juridique applicable**
#### **2.1. Principe général : RAS sur les revenus de capitaux mobiliers (article 119 bis, 2 CGI)**
L’article 119 bis, 2 du CGI prévoit qu’une **retenue à la source est due** sur les produits distribués (dividendes) **lorsque le bénéficiaire effectif est une personne n’ayant pas son domicile fiscal ou son siège en France**, sauf exceptions.

Le taux de la RAS est fixé par l’**article 187 CGI** (généralement **30 %** pour les dividendes, sauf convention fiscale contraire).

#### **2.2. Exceptions possibles**
L’article 119 bis, 2 CGI exclut la RAS pour certains bénéficiaires, notamment :
- Les **organismes de placement collectif (OPC)** sous conditions (UE ou État ayant une convention d’assistance administrative).
- **Les sociétés mères européennes** sous conditions (régime mère-fille UE, directive 2011/96/UE).

Cependant, votre cas ne semble pas relever de ces exceptions *a priori*, car :
- La Mère est une **société anonyme luxembourgeoise**, non un OPC.
- Le Luxembourg est un **État membre de l’UE**, mais l’exception mère-fille ne s’applique **automatiquement** que si les conditions de la **directive mère-fille** sont remplies.

---

### **3. Application de la directive mère-fille (2011/96/UE)**
La France a transposé cette directive en droit interne (**article 145 du CGI** et **article 119 ter CGI**).
**Conditions pour une exonération de RAS :**
1. **Participation minimale** : La Mère doit détenir **au moins 10 % du capital** de la Filiale (votre cas : 100 %, donc OK).
2. **Durée de détention** : La participation doit être détenue **depuis au moins 1 an** (votre cas : 5 ans, donc OK).
3. **Forme juridique** : La Mère doit être une **société soumise à l’IS** (ou impôt équivalent) au Luxembourg (votre cas : SA soumise à l’IS luxembourgeois, donc OK).
4. **Bénéficiaire effectif** : La Mère doit être le **bénéficiaire effectif** des dividendes (à vérifier : pas de structure interposée ou de montage abusif).

**→ Si ces conditions sont remplies, la RAS française est exonérée** (taux 0 %).

---
### **4. Vérification des conventions fiscales**
La **convention franco-luxembourgeoise** (signée en 2006, modifiée en 2018) prévoit :
- **Article 10 (Dividendes)** :
  - Si le bénéficiaire effectif est une société résidente du Luxembourg détenant **au moins 10 % du capital**, la RAS française est **limitée à 5 %** (au lieu de 30 %).
  - **Mais** : Si la directive mère-fille s’applique (exonération totale), la convention ne trouve pas à s’appliquer (primauté du droit UE).

**→ En pratique, si la directive mère-fille est applicable, la RAS est de 0 %. Sinon, elle serait de 5 % (convention) ou 30 % (droit interne).**

---
### **5. Conclusion et recommandations**
#### **5.1. Pas de RAS si la directive mère-fille s’applique**
Dans votre cas :
✅ Participation de 100 % (> 10 %)
✅ Détention depuis 5 ans (> 1 an)
✅ Mère soumise à l’IS au Luxembourg
✅ Luxembourg = État membre de l’UE

**→ La RAS française ne devrait pas s’appliquer (taux 0 %).**

#### **5.2. Formalités à respecter**
Pour bénéficier de l’exonération :
1. **Justificatif de résidence fiscale** de la Mère (attestation fiscale luxembourgeoise).
2. **Preuve de la détention du capital** (registre des actionnaires, statuts).
3. **Déclaration sur l’honneur** confirmant que la Mère est le bénéficiaire effectif (pas de montage abusif au sens de l’article 209 B CGI).

#### **5.3. Risque de requalification (abus de droit)**
L’administration française pourrait contester l’exonération si :
- La structure a été mise en place **principalement pour éviter la RAS** (article L64 du Livre des Procédures Fiscales).
- La Mère n’est pas le **bénéficiaire effectif** (ex. : si elle est une simple société écran).

**→ À vérifier : la substance économique de la Mère (activités réelles, effectifs, etc.).**

---
### **6. Synthèse des actions à mener**
| Étape | Action | Responsable |
|-------|--------|-------------|
| 1 | Vérifier que la Mère est bien le bénéficiaire effectif | Client |
| 2 | Obtenir une attestation de résidence fiscale luxembourgeoise | Client |
| 3 | Préparer les preuves de détention du capital (5 ans) | Client |
| 4 | Remplir une déclaration sur l’honneur (modèle Cerfa ?) | Avocat |
| 5 | Consulter l’administration française (rescrit possible) | Avocat |

---
### **7. Réponse finale**
**Non, aucune retenue à la source française ne devrait être due** sur la distribution de 20 000 000 € à la société mère luxembourgeoise, **à condition que :**
1. La Mère soit le **bénéficiaire effectif** des dividendes.
2. Les **conditions de la directive mère-fille** soient remplies (ce qui semble être le cas).
3. Les **justificatifs nécessaires** soient fournis à l’administration française.

**Recommandation :**
- **Documenter la substance de la Mère** (pour éviter un risque de requalification en abus de droit).
- **Consulter l’administration française** (via un rescrit) pour sécuriser la position.

**Pièces jointes à prévoir :**
- Attestation de résidence fiscale de la Mère.
- Preuves de détention du capital (5 ans).
- Statuts de la Mère et de la Filiale.

---
**Cordialement,**
[Votre Nom]
Avocat fiscaliste au Barreau de [Ville]
[Coordonnées du cabinet]

---

## S15

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

## Conclusion

Sous réserve de la vérification des conditions anti-abus et de bénéficiaire effectif, la distribution de 20 000 000 € envisagée le 15 juin 2025 ne devrait pas supporter de retenue à la source française.

L’exonération résulte de l’article 119 ter du CGI, qui constitue une dérogation à la retenue à la source de principe prévue à l’article 119 bis, 2 du CGI.

À défaut d’exonération, la retenue à la source de droit interne serait, en principe, de 25 %, soit un coût de 5 000 000 € sur la distribution envisagée.

---

## 1. Principe : une retenue à la source est normalement applicable

Le dividende distribué par une société française à une société dont le siège est situé hors de France entre dans le champ de l’article 119 bis, 2 du CGI.

La société mère luxembourgeoise étant une personne morale non résidente de France, une retenue à la source française est donc, en principe, exigible au moment de la mise en paiement, soit le 15 juin 2025.

Le taux interne applicable en 2025 est de 25 % (CGI, art. 187).

Toutefois, ce principe est écarté en l’espèce si les conditions du régime « mère-fille européen » sont réunies.

---

## 2. Application de l’exonération de l’article 119 ter du CGI

L’article 119 ter du CGI transpose le régime prévu par la directive européenne « mère-fille ». Il exonère de retenue à la source les distributions faites par une filiale française à sa société mère établie dans un autre État membre de l’Union européenne, sous certaines conditions.

Au regard des informations fournies, les conditions paraissent satisfaites.

| Condition | Situation décrite | Appréciation |
|---|---|---|
| Société bénéficiaire établie dans un État de l’Union européenne | Société établie au Luxembourg | Satisfaite |
| Forme sociale éligible | Société anonyme luxembourgeoise | Satisfaite : la SA luxembourgeoise est une forme visée par la directive et le dispositif français |
| Assujettissement à un impôt sur les sociétés | Soumise à l’impôt sur les sociétés luxembourgeois | Satisfaite, sous réserve qu’elle soit effectivement passible de cet impôt sans possibilité d’option ou d’exonération particulière |
| Seuil de détention | Détention de 100 % du capital de la filiale française | Satisfaite : le seuil légal est de 10 % |
| Durée de détention | Détention depuis cinq ans | Satisfaite : le seuil de deux ans est largement dépassé |
| Qualité de bénéficiaire effectif | Société mère luxembourgeoise | À confirmer sur le plan factuel |
| Absence de montage abusif | À apprécier | À documenter |

La société mère détient directement 100 % du capital de la société française depuis cinq ans. Elle satisfait donc, sans difficulté, aux conditions capitalistiques et temporelles de l’exonération.

Il n’est pas nécessaire de recourir au mécanisme d’engagement de conservation ou de constitution de garantie prévu lorsque le seuil de détention de deux ans n’est pas encore atteint.

---

## 3. Point de vigilance : bénéficiaire effectif et clause anti-abus

L’exonération n’est pas automatique au seul motif que la bénéficiaire est une SA luxembourgeoise détennant plus de 10 % de la filiale française.

### Bénéficiaire effectif

La société luxembourgeoise doit être le bénéficiaire effectif du dividende. En pratique, il conviendra de vérifier qu’elle :

- dispose d’une substance et d’une autonomie décisionnelle réelles ;
- perçoit le dividende pour son propre compte ;
- n’est pas tenue, juridiquement ou en fait, de le reverser immédiatement à une entité tierce ;
- ne joue pas le rôle d’un simple intermédiaire ou d’une société-relais.

L’existence ultérieure d’une remontée de dividendes par la société luxembourgeoise à son propre actionnaire n’est pas, par elle-même, rédhibitoire. En revanche, une obligation préexistante de retransfert ou un schéma de transit prédéterminé serait susceptible de fragiliser l’exonération.

### Dispositif anti-abus

L’article 119 ter du CGI refuse l’exonération lorsque la distribution s’inscrit dans un montage ou une série de montages :

- mis en place avec pour objet principal, ou l’un de ses objets principaux, l’obtention d’un avantage fiscal allant à l’encontre de l’objet du régime ; et
- qui n’est pas authentique au regard de l’ensemble des faits et circonstances pertinents.

La cession récente d’un actif par la filiale française et la distribution de la trésorerie qui en résulte ne caractérisent pas, en elles-mêmes, un abus. Une société mère luxembourgeoise détenant la filiale depuis cinq ans constitue au contraire un élément favorable.

Il conviendra néanmoins de vérifier, notamment :

- la date et les motifs de l’implantation de la société mère luxembourgeoise ;
- ses fonctions, actifs, risques et moyens humains ou matériels ;
- l’identité de ses actionnaires ultimes ;
- les modalités prévues pour l’utilisation ou la redistribution des fonds ;
- l’absence d’engagement de reversement à une entité située dans un État tiers ou dans une juridiction à fiscalité privilégiée.

---

## 4. Conséquence pratique

Sous ces réserves, la société française peut verser les 20 000 000 € à la société mère luxembourgeoise sans prélever de retenue à la source française.

Le montant net versé serait donc de :

> **20 000 000 €**

et non de 15 000 000 € après application d’une retenue de 25 %.

---

## 5. Éléments à réunir avant la mise en paiement

Avant le 15 juin 2025, il est recommandé que la société française obtienne et conserve un dossier justificatif comprenant notamment :

1. un certificat de résidence fiscale luxembourgeois de la bénéficiaire ;
2. les statuts et un extrait récent du registre du commerce luxembourgeois confirmant la forme de SA ;
3. une attestation de la société mère confirmant :
   - sa soumission à l’impôt sur le revenu des collectivités luxembourgeois ;
   - l’absence de régime d’exonération incompatible avec l’article 119 ter ;
   - sa qualité de bénéficiaire effectif ;
   - la détention directe et continue de 100 % du capital depuis au moins deux ans ;
4. les éléments établissant la substance et l’activité de la société mère ;
5. une analyse interne, ou une note de groupe, relative à l’absence de montage abusif ;
6. le respect des obligations déclaratives françaises applicables aux distributions versées à des non-résidents.

---

## 6. Convention fiscale franco-luxembourgeoise

À titre subsidiaire, la convention fiscale franco-luxembourgeoise prévoit également un taux de retenue à la source nul pour les dividendes versés à une société bénéficiaire effective détenant directement au moins 5 % du capital de la société distributrice, sous réserve des conditions conventionnelles et anti-abus.

La société mère détenant 100 % de la filiale française, cette voie conventionnelle devrait également conduire à une absence de retenue à la source.

Toutefois, en pratique, il est préférable de fonder prioritairement l’absence de retenue sur l’article 119 ter du CGI, dès lors que le régime européen est applicable et que ses conditions sont dûment documentées.

---

## S16

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

## Conclusion

Sous les hypothèses exposées, la distribution de 20 000 000 € mise en paiement le 15 juin 2025 peut être effectuée **sans retenue à la source française**.

En effet, bien que les dividendes versés à une société non résidente relèvent en principe de la retenue à la source prévue à l’article 119 bis, 2 du CGI, l’exonération prévue par l’article 119 ter du CGI est applicable aux distributions versées à une société mère établie dans un autre État membre de l’Union européenne, sous réserve du respect de ses conditions et de la clause anti-abus.

## 1. Principe : application théorique de la retenue à la source

La société mère luxembourgeoise n’a pas son siège en France. Le dividende entre donc, en principe, dans le champ de la retenue à la source de l’article 119 bis, 2 du CGI, au taux prévu par l’article 187 du CGI.

Toutefois, ce principe est écarté lorsque les conditions de l’article 119 ter du CGI — transposition de la directive « mère-fille » — sont satisfaites.

## 2. Conditions de l’exonération de l’article 119 ter du CGI

Au regard des éléments fournis, les conditions objectives paraissent réunies :

| Condition légale | Situation décrite | Appréciation |
|---|---|---|
| Société bénéficiaire établie dans l’UE | Société luxembourgeoise | Remplie |
| Forme sociale éligible | Société anonyme luxembourgeoise | Remplie : la SA luxembourgeoise figure parmi les formes visées par la directive mère-fille |
| Soumission à un impôt sur les sociétés éligible, sans possibilité d’option et sans exonération | Soumise à l’impôt sur les sociétés luxembourgeois | A confirmer formellement, mais normalement remplie pour une SA luxembourgeoise pleinement assujettie à l’IRC luxembourgeois |
| Détention directe d’au moins 10 % du capital de la filiale française | Détention de 100 % | Remplie |
| Détention pendant au moins deux ans | Détention depuis cinq ans | Remplie |
| Qualité de bénéficiaire effectif des dividendes | Non documentée dans la question | A confirmer et documenter |
| Absence de montage abusif | Non documentée dans la question | A analyser au vu de la situation et des fonctions de la mère luxembourgeoise |

La condition de durée étant déjà satisfaite au 15 juin 2025, il n’est pas nécessaire de recourir au mécanisme d’engagement de conservation des titres.

## 3. Point de vigilance : bénéficiaire effectif et clause anti-abus

L’exonération ne doit pas être appliquée de manière automatique du seul fait que la mère est une SA luxembourgeoise détenant 100 % de la filiale.

La société mère doit être le **bénéficiaire effectif** du dividende. En pratique, elle doit disposer de la maîtrise juridique et économique des sommes reçues et ne pas agir comme une simple société-relais tenue, en droit ou en fait, de les reverser à un tiers.

Par ailleurs, l’article 119 ter comporte une clause anti-abus. L’exonération est refusée lorsque la distribution s’inscrit dans un montage ou une série de montages :

- dont l’un des objets principaux est l’obtention d’un avantage fiscal contraire à l’objet de l’exonération ; et
- qui n’est pas authentique au regard de l’ensemble des faits et circonstances pertinents.

Une holding luxembourgeoise n’est pas, par elle-même, abusive. En revanche, il conviendra de pouvoir justifier de sa réalité économique, de son rôle dans le groupe, de ses organes de décision, de ses fonctions, de la gestion effective de sa participation française et de l’absence d’obligation de retransfert immédiat des fonds.

La cession préalable d’un actif par la filiale française et le montant significatif de la distribution ne font pas obstacle, en eux-mêmes, à l’exonération. Ils imposent toutefois une documentation particulièrement soignée, notamment si le dividende doit ensuite être distribué ou remonté au-delà du Luxembourg.

## 4. Recommandation pratique

Avant la mise en paiement du 15 juin 2025, la filiale française devrait obtenir et conserver une attestation de la société mère luxembourgeoise confirmant notamment :

1. sa résidence et son siège de direction effective au Luxembourg ;
2. sa forme de société anonyme luxembourgeoise ;
3. son assujettissement normal à l’impôt sur le revenu des collectivités luxembourgeois, sans exonération ;
4. sa détention directe et continue de 100 % du capital de la société française depuis cinq ans ;
5. sa qualité de bénéficiaire effectif des dividendes ;
6. l’absence de montage non authentique ayant pour objet principal, ou l’un de ses objets principaux, l’obtention indue de l’exonération.

La filiale française devra conserver cette documentation dans son dossier fiscal, la charge de la correcte application de l’exonération lui incombant en qualité d’établissement payeur.

## Avis

Sous réserve de la confirmation que la société mère luxembourgeoise est bien le bénéficiaire effectif des sommes et qu’aucun montage abusif n’est caractérisé, la distribution de 20 000 000 € du 15 juin 2025 est éligible à l’exonération de retenue à la source prévue à l’article 119 ter du CGI.

**La retenue à la source française est donc de 0 €.**

---

## S17

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

## Conclusion

Sous réserve de la vérification de la situation fiscale effective de la société mère et de l’absence de montage abusif, **aucune retenue à la source française ne devrait être prélevée** sur la distribution de 20 000 000 € mise en paiement le 15 juin 2025.

La société française pourra appliquer l’exonération prévue par l’article **119 ter du CGI**, qui transpose le régime « mère-fille » de la directive 2011/96/UE.

Le premier alinéa de l’article 119 bis, 2 du CGI pose le principe d’une retenue à la source sur les dividendes distribués à un non-résident. Il ne constitue toutefois pas le régime complet : l’article 119 ter prévoit précisément une exonération pour certaines distributions intragroupes au sein de l’Union européenne.

## Conditions de l’exonération de l’article 119 ter du CGI

L’exonération s’applique notamment lorsque :

1. **La société distributrice française est soumise à l’IS au taux normal.**  
   Ce point doit être confirmé, mais il est en pratique normalement satisfait par une société française exerçant une activité ordinaire.

2. **La bénéficiaire est une société d’un autre État membre de l’Union européenne.**  
   La société mère est luxembourgeoise : condition remplie.

3. **La société bénéficiaire a une forme sociale éligible.**  
   La *société anonyme* luxembourgeoise figure parmi les formes de sociétés visées par la directive mère-fille : condition remplie.

4. **Elle est passible, sans option et sans exonération, d’un impôt sur les sociétés éligible.**  
   L’impôt sur le revenu des collectivités luxembourgeois est un impôt visé par le régime. Sous réserve que la société mère ne bénéficie pas, pour elle-même, d’une exonération subjective particulière, cette condition est remplie.

5. **Elle détient directement une participation minimale dans la société française depuis au moins deux ans.**  
   La détention de 100 % du capital depuis cinq ans satisfait très largement cette condition.

Au vu des éléments communiqués, la distribution bénéficie donc de l’exonération.

**Retenue à la source française due : 0 €.**  
**Montant versé à la société mère luxembourgeoise : 20 000 000 €, hors autres éléments éventuels de distribution.**

## Réserve anti-abus

L’exonération de l’article 119 ter peut être écartée si la distribution s’inscrit dans un montage — ou une série de montages — ayant pour objectif principal, ou l’un de ses objectifs principaux, l’obtention d’un avantage fiscal contraire à l’objet du régime, et qui ne serait pas authentique au regard des circonstances pertinentes.

En pratique, il convient donc de pouvoir documenter que la société luxembourgeoise :

- exerce une fonction économique et de gouvernance réelle dans le groupe ;
- n’est pas une entité interposée artificiellement avant la distribution ;
- dispose des pouvoirs et de la substance appropriés au regard de son rôle ;
- est le bénéficiaire réel et économique de la distribution, ou, à tout le moins, que sa structure et les flux ultérieurs ne révèlent pas une interposition abusive.

Le fait qu’elle détienne la filiale française depuis cinq ans est favorable, mais ne dispense pas d’une revue factuelle de sa substance et de la chaîne de détention.

## Formalités à accomplir avant le 15 juin 2025

La société française doit obtenir et conserver, **avant la mise en paiement**, les justificatifs permettant d’établir que la mère luxembourgeoise satisfait aux conditions de l’article 119 ter. Il est recommandé de réunir notamment :

- une attestation de résidence fiscale luxembourgeoise pour 2025 ;
- une attestation de la société mère confirmant :
  - sa forme de SA luxembourgeoise ;
  - son assujettissement à l’impôt sur le revenu des collectivités, sans option ni exonération ;
  - la détention directe de 100 % du capital de la société française depuis cinq ans ;
  - son éligibilité au régime de l’article 119 ter ;
- un extrait du registre des actionnaires ou toute pièce démontrant la détention directe et continue ;
- les éléments de substance et de gouvernance utiles à la défense du dossier anti-abus.

En l’absence de justificatifs suffisants au jour du paiement, la société française s’exposerait à un risque de mise en cause en tant que redevable de la retenue à la source. Une régularisation par voie de remboursement pourrait alors être nécessaire.

## À défaut d’exonération interne

Si, contre toute attente, le régime de l’article 119 ter était refusé, la retenue à la source interne serait, en principe, au taux de droit commun applicable en 2025, soit **25 %** pour une bénéficiaire personne morale.

La convention fiscale franco-luxembourgeoise pourrait alors limiter ce prélèvement, sous réserve notamment que la société luxembourgeoise soit le bénéficiaire effectif du dividende et satisfasse aux conditions conventionnelles. Cette convention ne doit toutefois être envisagée qu’à titre subsidiaire : le régime interne de l’article 119 ter est ici plus favorable, puisqu’il conduit à une exonération totale.

---

## S18

**Role de l'enonce :** mesure

**Fait manquant :** Les trois mentions obligatoires du III-B : la société relève-t-elle de l'article 1655 ter, les participations cédées confèrent-elles le droit à la jouissance d'immeubles, le cessionnaire acquitte-t-il des dettes contractées auprès du cédant. Aucune ne figure dans l'énoncé, et le rédacteur de l'acte ne peut pas les inventer.

**Dossier soumis au modele :**

```
Un client vous consulte avant de signer.

Il cede les titres d'une societe civile immobiliere dont l'actif est
constitue a 80 % d'immeubles situes en France. Prix de cession :
4 000 000 euros. L'acte sera signe le 20 mars 2024.

Quel droit d'enregistrement est du, et que doit contenir l'acte ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

## 1. Droit d’enregistrement

Sous réserve que les parts de la SCI ne soient pas négociées sur un marché réglementé ou un système multilatéral de négociation et que la SCI ne relève d’aucune des exceptions visées par le texte, elle constitue une **personne morale à prépondérance immobilière** : son actif est constitué à 80 % d’immeubles situés en France, donc principalement immobilier.

La cession est ainsi soumise au droit proportionnel de **5 %** prévu à l’article 726, I, 2° du CGI.

Sur la base du prix indiqué :

> **4 000 000 € × 5 % = 200 000 €**

Le droit d’enregistrement s’élève donc à **200 000 €**.

Ce calcul suppose que :

- 4 000 000 € constitue l’intégralité du prix et des charges augmentatives du prix ;
- la valeur réelle des titres n’est pas supérieure au prix déclaré ;
- aucune dette ou obligation complémentaire prise en charge par le cessionnaire ne doit être intégrée à l’assiette.

Il conviendra notamment d’examiner les éventuels comptes courants d’associés et dettes de la SCI envers le cédant. En principe, le droit est acquitté lors de l’enregistrement de la cession, usuellement par le cessionnaire selon les stipulations contractuelles.

## 2. Mentions obligatoires dans l’acte

L’acte doit répondre **expressément**, par l’affirmative ou la négative, aux trois points imposés par l’article 726, III-B du CGI :

1. **Société relevant de l’article 1655 ter**  
   L’acte doit préciser si la SCI est ou non une société mentionnée à l’article 1655 ter du CGI.

2. **Droit à la jouissance d’un immeuble**  
   L’acte doit préciser si les parts cédées confèrent ou non au cessionnaire, directement ou indirectement, un droit à la jouissance d’un immeuble ou d’une fraction d’immeuble au sens de l’article 728 du CGI.

3. **Dettes contractées par la SCI auprès du cédant**  
   L’acte doit préciser si le cessionnaire :
   - a acquitté, ou
   - s’engage à acquitter, directement ou indirectement,

   des dettes contractées par la SCI auprès du cédant. Dans l’affirmative, **le montant de ces dettes doit être indiqué**.

Une clause pourrait être rédigée ainsi, après vérification des faits :

> « Pour l’application de l’article 726, III-B du code général des impôts, les parties déclarent expressément que :  
> – la Société [est/n’est pas] une société mentionnée à l’article 1655 ter du CGI ;  
> – les parts cédées [confèrent/ne confèrent pas] au cessionnaire, directement ou indirectement, un droit à la jouissance d’immeubles ou de fractions d’immeubles au sens de l’article 728 du CGI ;  
> – le cessionnaire [a acquitté ou s’engage à acquitter/n’a acquitté et ne s’engage à acquitter], directement ou indirectement, aucune dette contractée par la Société auprès du cédant. [Le cas échéant : le montant concerné s’élève à … €]. »

## 3. Formalité particulière en cas de signature à l’étranger

Si la cession est réalisée à l’étranger, elle devra être constatée, dans le délai d’un mois, par un **acte authentique reçu par un notaire exerçant en France**.

Pour une cession réalisée le **20 mars 2024**, cette régularisation devra donc intervenir, en principe, au plus tard le **20 avril 2024**.

### Conclusion

Sous les réserves d’assiette mentionnées ci-dessus :

> **Droit d’enregistrement dû : 200 000 €.**

Avant signature, il faut impérativement documenter la composition de l’actif de la SCI, l’absence d’exception légale, les éventuels droits de jouissance attachés aux parts et toute dette de la SCI envers le cédant.

---

## S19

**Role de l'enonce :** mesure

**Fait manquant :** Les trois mentions obligatoires du III-B : la société relève-t-elle de l'article 1655 ter, les participations cédées confèrent-elles le droit à la jouissance d'immeubles, le cessionnaire acquitte-t-il des dettes contractées auprès du cédant. Aucune ne figure dans l'énoncé, et le rédacteur de l'acte ne peut pas les inventer.

**Dossier soumis au modele :**

```
Un client vous consulte avant de signer.

Il cede les titres d'une societe civile immobiliere dont l'actif est
constitue a 80 % d'immeubles situes en France. Prix de cession :
4 000 000 euros. L'acte sera signe le 20 mars 2024.

Quel droit d'enregistrement est du, et que doit contenir l'acte ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

# Note de consultation

## Cession de titres d'une SCI à prépondérance immobilière — Régime fiscal

**Objet** : Détermination du droit d'enregistrement applicable et mentions obligatoires de l'acte

---

## 1. Qualification de l'opération

La SCI dont les parts sont cédées présente un actif constitué à **80 % d'immeubles situés en France**. Ses parts sociales ne sont pas négociées sur un marché réglementé ou un système multilatéral de négociation.

Ces conditions réunies, la SCI constitue une **personne morale à prépondérance immobilière** (PMPI) au sens de l'**article 726, I, 2° du CGI**.

---

## 2. Droit d'enregistrement applicable

### Taux : **5 %**

L'article 726, I, 2° du CGI soumet les cessions de participations dans les PMPI à un droit d'enregistrement au taux de **5 %**.

> ⚠️ Ce taux a été relevé de 4,80 % à 5 % par la loi de finances pour 2024 (article 71 de la loi n° 2023-1322 du 29 décembre 2023), applicable aux actes signés à compter du **1er janvier 2024**. La cession du 20 mars 2024 entre donc bien dans le champ du nouveau taux.

### Calcul

| Base imposable | Taux | Droit dû |
|---|---|---|
| 4 000 000 € | 5 % | **200 000 €** |

### Précisions importantes

- **Abattement** : aucune exonération, réduction ou abattement n'est prévu en l'espèce (sauf cas particulier non applicable ici : cession à un membre du foyer fiscal, donation-partage successorale à des conditions très encadrées, etc.).
- **Surtaxe sur les plus-values élevées** (art. 1609 nonies F du CGI) : à vérifier si le cédant est une personne physique et si la cession dégage une plus-value supérieure à 250 000 €. Cette surtaxe n'est pas un droit d'enregistrement mais une taxe additionnelle à l'impôt sur le revenu ; il convient de le signaler au client.
- **Régime des plus-values** des particuliers (art. 150 U et suivants du CGI) : la taxation à 5 % est **distincte** de la taxation de la plus-value de cession. Elle ne s'y substitue pas.
- **L'article 726, III, A** (obligation de faire constater la cession par acte authentique notarié dans un délai d'un mois) ne s'applique qu'aux cessions réalisées **à l'étranger**. L'acte du 20 mars 2024, signé en France, n'y est pas soumis, mais l'intervention d'un notaire reste indispensable pour la formalité de l'enregistrement et la publication.

---

## 3. Mentions obligatoires de l'acte (article 726, III, B du CGI)

L'acte de cession doit indiquer **expressément** :

### 1° Précision relative à l'article 1655 ter du CGI

L'acte doit indiquer si la SCI est ou non une société visée à l'article 1655 ter du CGI.

> **Rappel** : l'article 1655 ter vise les sociétés — quelle que soit leur forme — dont l'actif est principalement composé de biens immobiliers acquis ou construits par elles-mêmes ou qu'elles font construire, et qui ont pour objet la vente desdits biens. Une SCI de gestion classique (mise en location) **ne tombe en principe pas** dans cette catégorie, sauf si elle a construit ou fait construire pour revendre. Vérification à opérer au cas d'espèce.

### 2° Droit à la jouissance d'immeubles

L'acte doit indiquer si les parts cédées confèrent au cessionnaire, **directement ou indirectement**, le droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'**article 728 du CGI**.

> **Point d'attention** : s'agissant d'une SCI, les statuts prévoient en général l'attribution de la jouissance d'un bien à l'un des associés (clause d'attribution en jouissance). Si une telle clause existe, elle devra être expressément mentionnée. À défaut, l'acte doit expressément énoncer l'absence d'un tel droit.

### 3° Prise en charge de dettes

L'acte doit indiquer si le cessionnaire a acquitté ou s'engage à acquitt­er, **directement ou indirectement**, des dettes contractées par la SCI auprès du cédant, en précisant, le cas échéant, leur montant.

> **Recommandation** : il convient de dresser un état complet des créances du cédant sur la SCI (comptes courants d'associé, prêts, etc.) au jour de la cession, et de stipuler dans l'acte soit l'absence de telles dettes, soit leur existence avec mention de leur montant.

---

## 4. Recommandations pratiques

1. **Rédaction de l'acte** : faire établir l'acte par le notaire, qui veillera à l'ensemble de ces mentions. Les trois points ci-dessus doivent figurer de manière **explicite** dans le corps de l'acte (et non dans un simple visa), sous peine de rejet de l'enregistrement ou de taxation d'office.

2. **Liquidation et paiement** : le droit de 200 000 € doit être acquitté lors du dépôt de l'acte au service de l'enregistrement (recette des impôts du lieu de situation du notaire).

3. **Vérifications complémentaires à opérer** :
   - Situation de la SCI au regard de l'article 1655 ter ;
   - Existence de clauses d'attribution en jouissance dans les statuts ;
   - Inventaire des dettes intra-groupe / cédant ;
   - Régime de la plus-value (PFU ou barème), information distincte mais à porter à la connaissance du client ;
   - Surtaxe sur les plus-values > 250 000 € si le cédant est une personne physique résident.

---

**En résumé** :

| | |
|---|---|
| **Droit applicable** | 5 % (art. 726, I, 2° CGI) |
| **Montant** | **200 000 €** |
| **Mentions obligatoires** | 1°) qualité au regard de l'art. 1655 ter ; 2°) droit à la jouissance (art. 728) ; 3°) prise en charge de dettes dues par la SCI au cédant |

Je reste à votre disposition pour la relecture du projet d'acte avant signature.

*Cabinet — mars 2024*

---

## S20

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

## Conclusion

**En l’état des faits communiqués, aucune retenue à la source ne devrait être due sur la distribution de 20 000 000 € mise en paiement le 15 juin 2025**, sous réserve notamment que la société luxembourgeoise :

- soit le **bénéficiaire effectif** des dividendes ;
- ait bien son siège de direction effective au Luxembourg ;
- ne constitue pas une société relais dans un montage abusif ;
- et fournisse à la société française, avant la mise en paiement, les justificatifs nécessaires.

Deux fondements permettent d’aboutir à cette exonération : le régime « mère-fille » de l’article 119 ter du CGI et, subsidiairement, la convention fiscale franco-luxembourgeoise.

## 1. Principe : retenue à la source de 25 %

La distribution constitue, en principe, un produit visé aux articles 108 à 117 bis du CGI. Son bénéficiaire ayant son siège hors de France, l’article 119 bis, 2 du CGI prévoit une retenue à la source.

Pour une personne morale, le taux de droit interne applicable en 2025 est en principe de **25 %**. À défaut d’exonération ou d’application conventionnelle, la retenue s’élèverait donc à :

> 20 000 000 € × 25 % = **5 000 000 €**

L’exception figurant dans l’extrait cité pour certains organismes de placement collectif étrangers n’est pas pertinente ici : une société anonyme luxembourgeoise ordinaire n’est pas un tel organisme.

## 2. Exonération « mère-fille » de l’article 119 ter du CGI

L’article 119 ter exonère de la retenue à la source les dividendes versés à une société mère établie dans l’Union européenne lorsque, notamment :

1. elle est le bénéficiaire effectif des dividendes ;
2. elle a son siège de direction effective dans l’Union européenne ;
3. elle revêt l’une des formes sociales éligibles ;
4. elle est soumise, sans option et sans en être exonérée, à l’un des impôts visés par le texte ;
5. elle détient directement au moins **10 %** du capital de la société française pendant au moins **deux ans**.

Au cas présent :

- la société mère est luxembourgeoise, donc établie dans l’Union européenne ;
- elle revêt la forme d’une **société anonyme**, forme éligible ;
- elle est soumise à l’impôt luxembourgeois sur les sociétés ;
- elle détient directement **100 %** du capital ;
- cette détention existe depuis **cinq ans**, de sorte que la condition de durée est satisfaite.

La distribution bénéficie donc, en principe, de l’exonération de retenue à la source prévue par l’article 119 ter.

Le fait que le Luxembourg puisse, le cas échéant, appliquer son propre régime d’exonération des participations au dividende reçu ne remet pas, à lui seul, en cause la condition tenant à l’assujettissement général de la société mère à l’impôt luxembourgeois.

## 3. Fondement conventionnel également favorable

La convention fiscale entre la France et le Luxembourg prévoit également, en substance, une imposition à la source au taux de **0 %** lorsque le bénéficiaire effectif des dividendes est une société résidente de l’autre État qui détient directement au moins **5 %** du capital de la société distributrice pendant une période de 365 jours comprenant la date de paiement.

Avec une participation directe de 100 % détenue depuis cinq ans, ces conditions sont également remplies.

Cette protection conventionnelle suppose néanmoins :

- que la société luxembourgeoise soit résidente fiscale du Luxembourg au sens de la convention ;
- qu’elle soit le bénéficiaire effectif des dividendes ;
- et que l’opération ne tombe pas sous une clause anti-abus.

Un régime particulier devrait être vérifié si la société française était, par exemple, un véhicule d’investissement immobilier exonéré distribuant des revenus immobiliers. Rien dans les faits communiqués ne l’indique.

## 4. Points devant être sécurisés avant le 15 juin 2025

### Bénéficiaire effectif

La détention juridique de 100 % du capital ne suffit pas toujours à démontrer la qualité de bénéficiaire effectif. Il convient de vérifier que la société luxembourgeoise :

- dispose librement des dividendes ;
- n’a pas l’obligation juridique ou factuelle de les reverser immédiatement à une autre entité ;
- exerce réellement les droits attachés à sa participation ;
- n’est pas une simple entité interposée dépourvue de fonctions et d’autonomie.

### Clause anti-abus

L’exonération peut être écartée si la structure constitue un montage non authentique mis en place principalement pour obtenir un avantage fiscal contraire à l’objet du régime mère-fille. Il faudra donc documenter les motifs économiques de la société luxembourgeoise, sa substance et l’utilisation envisagée des fonds.

### Documentation

Avant la mise en paiement, la société française devrait notamment obtenir et conserver :

- un certificat de résidence fiscale luxembourgeoise valable pour 2025, notamment le formulaire conventionnel **5000** ;
- les justificatifs de la forme sociale et de l’assujettissement à l’impôt luxembourgeois ;
- les documents établissant la détention directe de 100 % depuis cinq ans ;
- une attestation de la société mère relative à sa qualité de bénéficiaire effectif ;
- une documentation sur sa substance, sa gouvernance et l’absence d’obligation de reversement ;
- l’attestation requise pour l’application de l’article 119 ter ainsi que, le cas échéant, les formulaires conventionnels relatifs aux dividendes.

## Avis

Sous ces réserves, la société française peut mettre en paiement le dividende de **20 000 000 € sans retenue à la source**.

À défaut de justificatifs disponibles à la date de mise en paiement, une retenue de droit interne de **5 000 000 €** pourrait être pratiquée à titre conservatoire, avec demande ultérieure de restitution. Il est donc préférable de finaliser le dossier d’exonération avant le 15 juin 2025.

---

## S21

**Role de l'enonce :** mesure

**Fait manquant :** Les prestations fournies aux occupants. Une location meublée nue relève de la gestion de son propre patrimoine immobilier ; une activité para-hôtelière, avec réception, ménage, linge et petit-déjeuner, est une activité d'hébergement commerciale.

**Dossier soumis au modele :**

```
Un dirigeant de 62 ans vous consulte avec son notaire.

Il souhaite donner a ses deux enfants, a parts egales et en pleine
propriete, la totalite des titres de sa societe par actions
simplifiee. Elle possede quarante appartements meubles. Valeur des
titres : 20 000 000 euros.

Les titres font l'objet d'un engagement collectif de conservation
signe le 3 mars 2021, portant sur la totalite des droits, toujours
en cours. Chaque enfant prend l'engagement individuel prevu par les
textes. Le dirigeant conserve la presidence pendant trois ans.

La donation serait signee le 25 octobre 2023.

L'exoneration partielle de l'article 787 B est-elle applicable ?

Voici le texte applicable a la date de la donation.
```

**Reponse a coder, en entier :**

**Non, l’exonération partielle de l’article 787 B du CGI n’est pas applicable.**

La société dont les titres sont transmis a pour activité la détention et la location de quarante appartements meublés. Aux termes mêmes du deuxième alinéa de l’article 787 B (dans sa rédaction applicable au 25 octobre 2023), « n’est pas considérée comme une activité industrielle, commerciale, artisanale, agricole ou libérale l’exercice par une société d’une activité de gestion de son propre patrimoine mobilier ou immobilier ».

Cette exclusion s’applique indépendamment du régime fiscal des revenus (BIC) et du caractère meublé des locations. La société n’exerce pas une activité d’animation de groupe au sens du troisième alinéa (aucune participation dans des filiales opérationnelles n’est mentionnée). Elle ne présente pas non plus les caractéristiques d’une activité para-hôtelière (prestations de services significatives de type hôtelier).

La condition tenant à la nature de l’activité principale n’étant pas remplie, les autres conditions (engagement collectif de conservation en cours, engagements individuels des donataires, conservation de la présidence pendant trois ans) sont inopérantes. L’exonération de 75 % ne peut donc pas s’appliquer à la donation du 25 octobre 2023.

Les droits de mutation à titre gratuit seront calculés sur la valeur en pleine propriété des titres (20 M€), sous déduction le cas échéant des abattements de droit commun (art. 779 CGI) et, si les conditions en sont réunies, du dispositif de l’article 790 CGI (réduction pour donation en pleine propriété avant 70 ans, applicable à la date considérée).

Je reste à votre disposition pour chiffrer les droits, examiner d’éventuelles alternatives (donation-partage avec réserve d’usufruit, apport-cession, etc.) ou préparer les actes.

---

## S22

**Role de l'enonce :** mesure

**Fait manquant :** Le jour de la cession, la bascule étant au 21 février 2026, et le secteur dans lequel le remploi serait fait.

**Dossier soumis au modele :**

```
Un client vous consulte.

Sa holding, qu'il controle a 100 %, a vendu en fevrier 2026 les
titres d'une societe d'exploitation qu'elle detenait, moins de
trois ans apres que le client les lui ait apportes. Elle a
encaisse 9 000 000 euros.

Le produit de la vente dort sur le compte de la holding. Le client
sait qu'il doit reinvestir une partie de cette somme pour
conserver le benefice du report d'imposition.

Que lui conseillez-vous ?

Voici le texte applicable.
```

**Reponse a coder, en entier :**

## 1. Enjeu et montant à réemployer

La cession étant intervenue moins de trois ans après l’apport, elle est, en principe, un événement mettant fin au report d’imposition dont vous bénéficiez personnellement sur la plus-value d’apport.

Toutefois, le report peut être maintenu si la holding :

1. **prend l’engagement de réinvestir** le produit de cession ;
2. **réalise effectivement ce réinvestissement** dans le délai légal ;
3. réinvestit au moins **70 % du produit de cession** dans des emplois éligibles.

Sur la base d’un produit de cession de **9 000 000 €**, le montant minimal à réemployer est donc de :

> **6 300 000 €**

Il faudra néanmoins confirmer si les 9 M€ constituent bien le « produit de cession » retenu fiscalement, notamment au regard des frais directement supportés par la holding à l’occasion de l’opération. Par prudence, je recommanderais de viser un réemploi éligible de **6,5 M€ à 7 M€**, afin de ne pas se trouver sous le seuil de 70 % à la suite d’un ajustement.

Les 30 % restants, soit environ **2,7 M€**, ne sont pas soumis à l’obligation de réemploi au titre de ce dispositif. Ils peuvent rester disponibles dans la holding, sous réserve de leurs conséquences fiscales et patrimoniales propres.

---

## 2. Délai : trois ans à compter de la cession, et non de l’apport

La holding dispose de **trois ans, décomptés de date à date à compter de la cession de février 2026**, pour réaliser le réinvestissement.

Par exemple, si la cession est juridiquement intervenue le **14 février 2026**, le réemploi doit être intégralement effectué au plus tard le **14 février 2029**.

Je déconseille naturellement d’attendre l’échéance : il faut viser une réalisation complète avant la fin de l’année 2028 ou, au plus tard, au tout début de 2029. Un investissement seulement signé, envisagé, placé sous conditions suspensives ou non décaissé à l’expiration du délai peut être insuffisant.

Le fait que les fonds restent provisoirement sur le compte bancaire de la holding n’est pas, en soi, une difficulté. En revanche, cette trésorerie placée en comptes à terme, OPCVM, obligations cotées ou autres placements financiers **ne constitue pas**, en principe, un remploi éligible au sens du texte cité.

---

## 3. Ce que la holding doit faire immédiatement

Je conseille de procéder sans délai aux actions suivantes.

### A. Formaliser l’engagement de réinvestissement

La holding doit prendre un engagement exprès de réemploi portant au minimum sur 70 % du produit de cession.

Cet engagement doit être correctement documenté par :

- une décision de l’organe compétent de la holding ;
- un procès-verbal indiquant le montant du produit de cession, le montant affecté au réemploi et la date limite ;
- une traçabilité bancaire de la cession et des emplois ultérieurs ;
- les déclarations et annexes fiscales requises au titre de l’année 2026, avec la documentation que la holding devra remettre au contribuable apporteur.

Le report est personnellement attaché à votre situation fiscale : il faudra donc assurer une parfaite cohérence entre les déclarations de la holding et votre déclaration de plus-value en report.

### B. Isoler les fonds et mettre en place un suivi

Je recommande d’ouvrir un sous-compte ou, à tout le moins, d’établir une comptabilité analytique du « produit de cession à réemployer ».

L’objectif est de pouvoir démontrer, en cas de contrôle :

- l’origine des 9 M€ ;
- la part soumise à remploi ;
- chaque emploi éligible ;
- la date de réalisation de chaque emploi ;
- l’affectation réelle des actifs financés à l’activité éligible.

---

## 4. Investissements envisageables : privilégier des opérations opérationnelles réelles

Le texte que vous citez vise le financement de **moyens permanents d’exploitation** affectés à une activité éligible. Le réinvestissement doit donc correspondre à une activité économique réelle et non à la simple gestion patrimoniale de la trésorerie de la holding.

### A. Investissements directement éligibles au titre des moyens permanents d’exploitation

Peuvent, sous réserve de l’analyse du dossier concret, entrer dans cette catégorie :

- acquisition de matériel industriel, machines, équipements ou outillage ;
- financement d’équipements informatiques, logistiques ou techniques ;
- acquisition d’éléments nécessaires à une activité commerciale, industrielle, artisanale, agricole ou libérale ;
- développement d’une activité opérationnelle exercée par la holding elle-même, si celle-ci dispose d’une véritable substance et exploite réellement l’activité ;
- investissement dans des actifs nécessaires et durablement affectés à une exploitation.

En revanche, ne constituent normalement pas un remploi suffisant :

- un dépôt bancaire ;
- un compte à terme ;
- des SICAV, FCP, ETF ou titres cotés détenus comme placements ;
- des obligations ou produits de taux ;
- un portefeuille de participations passif ;
- une avance en compte courant non structurée ou non directement affectée à un emploi éligible ;
- la simple conservation de trésorerie.

La gestion du patrimoine propre, et spécialement la gestion du patrimoine immobilier propre, est exclue. Ainsi, l’acquisition d’un immeuble destiné à être conservé et loué dans une logique patrimoniale n’est pas une solution sécurisée au regard du texte. En revanche, un immeuble réellement utilisé comme outil d’exploitation dans le cadre d’une activité opérationnelle appelle une analyse plus nuancée, mais doit être documenté avec une grande rigueur.

### B. Acquisition ou prise de contrôle d’une société opérationnelle

En pratique, la voie la plus fréquemment utilisée consiste à acquérir une participation de contrôle dans une société exerçant une activité opérationnelle éligible, ou à souscrire à une augmentation de capital d’une telle société.

Le texte complet de l’article 150-0 B ter prévoit, au-delà du seul cas des moyens permanents d’exploitation reproduit dans votre question, d’autres modalités de remploi, notamment autour de l’acquisition du contrôle d’une société opérationnelle et de certaines souscriptions au capital. Il faudra se référer à la version consolidée applicable à la date de cession et structurer l’opération sur le fondement exact correspondant.

Cette option est souvent plus adaptée à une holding ayant 9 M€ de liquidités que la création ex nihilo d’une activité exploitante.

Exemples envisageables, sous réserve de due diligence fiscale et juridique :

- acquisition de 100 % ou d’une participation conférant le contrôle d’une PME opérationnelle ;
- prise de contrôle d’une entreprise industrielle, de services, artisanale, commerciale ou technologique ;
- augmentation de capital d’une filiale opérationnelle, afin qu’elle finance son développement, ses équipements ou son besoin de croissance ;
- acquisition d’un groupe opérationnel suivie d’un programme d’investissement documenté.

Il faut éviter les montages artificiels dans lesquels la holding acquiert une société sans activité réelle, une société patrimoniale ou une structure dont l’objet principal est de placer une trésorerie.

### C. Fonds de private equity : une solution possible, mais à encadrer

Selon les modalités légales applicables, une partie du réemploi peut également être réalisée par souscription à certains véhicules de capital-investissement répondant à des conditions très précises d’actifs éligibles et de quotas d’investissement.

Cette solution peut être pertinente si le client ne souhaite pas reprendre directement une entreprise. Elle suppose toutefois de sélectionner un fonds expressément compatible avec le remploi « apport-cession » et de vérifier :

- la nature exacte du véhicule ;
- son quota réglementaire d’investissement ;
- son engagement statutaire ;
- la date effective de souscription et de libération ;
- l’absence de clause faisant dépendre l’éligibilité d’événements futurs trop incertains.

Je ne recommanderais aucun investissement dans un fonds sans attestation écrite et analyse préalable de son éligibilité au dispositif.

---

## 5. Recommandation pratique : une stratégie de réemploi diversifiée, mais sécurisée

Au regard du montant en jeu, je ne conseillerais pas de chercher à « dépenser » 6,3 M€ rapidement dans un actif mal choisi. Le risque économique serait aussi réel que le risque fiscal.

Une stratégie raisonnable pourrait être la suivante :

- réserver immédiatement **7 M€** sur les 9 M€ dans une poche de réemploi ;
- rechercher une acquisition de contrôle d’une société opérationnelle ou un investissement majoritaire dans une activité connue du client ;
- compléter, si nécessaire et si juridiquement admissible, par des souscriptions dans des véhicules de capital-investissement spécialement qualifiés ;
- conserver environ **2 M€** de liquidité libre dans la holding pour la trésorerie, les frais, les opportunités futures ou une éventuelle distribution, étant précisé qu’une distribution aurait alors sa fiscalité propre.

La priorité est de retenir des investissements qui ont une logique économique autonome : activité réelle, équipes, clients, actifs d’exploitation, perspectives de développement et documentation complète. Le réemploi ne doit jamais être la seule justification de l’investissement.

---

## 6. Risque en cas de non-respect

Si la holding ne prend pas valablement l’engagement, ne réemploie pas au moins 70 % du produit dans le délai, ou réemploie dans des actifs non éligibles, le report d’imposition prendra fin.

La conséquence est une imposition à votre niveau personnel de la plus-value d’apport placée en report, avec les prélèvements sociaux et, le cas échéant, les intérêts ou majorations applicables.

Point essentiel : le risque ne porte pas sur les seuls 6,3 M€ non ou mal réemployés. L’enjeu est la remise en cause du **report de la plus-value d’apport elle-même**, dont le montant doit être reconstitué à partir de l’opération initiale d’apport.

Par ailleurs, le réemploi protège le report d’imposition personnel ; il ne neutralise pas l’imposition éventuelle de la plus-value réalisée par la holding sur la vente des titres. Cette dernière relève de son propre régime d’impôt sur les sociétés, notamment du régime des titres de participation si ses conditions sont réunies.

---

## 7. Conclusion

Je recommande donc :

1. de confirmer immédiatement les dates exactes d’apport et de cession ;
2. de retenir, par prudence, un objectif de réemploi de **7 M€** ;
3. de formaliser sans délai l’engagement de remploi et les obligations déclaratives ;
4. de rechercher prioritairement la prise de contrôle ou le financement en fonds propres d’une entreprise opérationnelle éligible ;
5. de ne pas considérer les placements de trésorerie ou l’immobilier patrimonial comme des remplacements éligibles ;
6. de faire valider chaque opération avant sa réalisation, tant sur son éligibilité fiscale que sur sa substance économique.

Avant tout investissement, il faudrait réunir l’acte d’apport, l’acte de cession de février 2026, le détail du prix et des frais, ainsi que le montant exact de la plus-value placée en report. Cela permettra de sécuriser le calendrier déclaratif et de bâtir une stratégie de réemploi adaptée.

---

## S23

**Role de l'enonce :** mesure

**Fait manquant :** Les prestations fournies aux occupants. Une location meublée nue relève de la gestion de son propre patrimoine immobilier ; une activité para-hôtelière, avec réception, ménage, linge et petit-déjeuner, est une activité d'hébergement commerciale.

**Dossier soumis au modele :**

```
Un dirigeant de 62 ans vous consulte avec son notaire.

Il souhaite donner a ses deux enfants, a parts egales et en pleine
propriete, la totalite des titres de sa societe par actions
simplifiee. Elle possede quarante appartements meubles. Valeur des
titres : 20 000 000 euros.

Les titres font l'objet d'un engagement collectif de conservation
signe le 3 mars 2021, portant sur la totalite des droits, toujours
en cours. Chaque enfant prend l'engagement individuel prevu par les
textes. Le dirigeant conserve la presidence pendant trois ans.

La donation serait signee le 25 octobre 2023.

L'exoneration partielle de l'article 787 B est-elle applicable ?

Voici le texte applicable a la date de la donation.
```

**Reponse a coder, en entier :**

**Objet : Analyse de l'applicabilité de l'exonération partielle de l'article 787 B du CGI à la donation projetée**

**À l’attention de [Nom du client] et de son notaire,**
**De la part de [Votre nom], Avocat fiscaliste**

---

### **1. Contexte et problématique**
Vous envisagez de donner, en pleine propriété et à parts égales, la totalité des titres de votre SAS (valeur : 20 000 000 €) à vos deux enfants. Ces titres sont soumis à un **engagement collectif de conservation (ECC)** signé le 3 mars 2021, toujours en cours. Chaque enfant prendra un **engagement individuel de conservation** conformément à l’article 787 B du CGI. Vous conserverez la présidence pendant 3 ans.

La question centrale est : **l’exonération partielle de 75 % prévue à l’article 787 B du CGI est-elle applicable à cette donation ?**

---

### **2. Conditions d’application de l’article 787 B**
L’exonération de 75 % est subordonnée à **trois séries de conditions** :
1. **Nature de la société** : Son activité principale doit être **industrielle, commerciale, artisanale, agricole ou libérale** (au sens des articles 34 et 35 du CGI).
2. **Exclusion des sociétés patrimoniales** : Une société dont l’activité principale est la **gestion de son propre patrimoine mobilier ou immobilier** est exclue.
3. **Engagements de conservation** : Les titres doivent faire l’objet d’un **ECC** (déjà en place) et les donataires doivent prendre un **engagement individuel** (prévu).

---

### **3. Analyse de l’activité de la SAS**
Votre SAS détient **40 appartements meublés**. Son activité consiste donc en la **location meublée**, qui relève :
- **Fiscalement** : Des **Bénéfices Industriels et Commerciaux (BIC)** (article 35 du CGI), car la location meublée est considérée comme une activité commerciale.
- **Juridiquement** : D’une **activité de gestion de patrimoine immobilier**.

#### **Problématique : Activité commerciale vs. gestion patrimoniale**
L’article 787 B exclut explicitement les sociétés dont l’activité principale est la **gestion de leur propre patrimoine immobilier**. Or, votre SAS :
- **Ne semble pas exercer d’autre activité** que la location meublée (pas de services internes à un groupe, pas de participation active à une politique industrielle/commerciale).
- **Ne rend pas de services spécifiques** à d’autres sociétés du groupe (vous n’avez pas mentionné de groupe structuré).

**→ Risque fort de requalification en société patrimoniale**, exclue du bénéfice de l’exonération.

#### **Exception possible : Société holding animatrice ?**
L’article 787 B prévoit une exception pour les sociétés qui :
- Gèrent un portefeuille de participations **ET**
- Participent activement à la conduite de la politique d’un **groupe** (sociétés contrôlées exerçant une activité éligible).

**Dans votre cas :**
- Aucune indication ne suggère que votre SAS est une **holding animatrice** d’un groupe.
- Les 40 appartements sont détenus directement, sans mention de filiales ou de structure de groupe.

**→ L’exception ne semble pas applicable.**

---

### **4. Conclusion sur l’éligibilité**
**L’exonération de l’article 787 B ne devrait pas s’appliquer**, car :
1. Votre SAS exerce une **activité de gestion de patrimoine immobilier** (location meublée), exclue par le texte.
2. Elle ne remplit pas les critères de la **holding animatrice** (pas de groupe, pas de services internes).

**Conséquence fiscale :**
- La donation sera soumise aux **droits de mutation à titre gratuit** (après abattement de 100 000 € par parent et par enfant, soit 200 000 € au total).
- **Base taxable** : 20 000 000 € – 200 000 € = **19 800 000 €** (à répartir entre les deux enfants).
- **Taux applicable** : 45 % (au-delà de 1 805 677 € par enfant).

**Coût estimé (sans exonération) :**
- Par enfant : (9 900 000 € × 45 %) = **4 455 000 €** → **Total : ~8 910 000 €** de droits.

---

### **5. Pistes d’optimisation (à étudier avec le notaire)**
1. **Report de la donation** : Si la SAS pouvait intégrer une activité éligible (ex : services à un groupe), l’exonération pourrait être envisagée.
2. **Donation en usufruit** : Réduire la base taxable (mais perte du contrôle pour le donateur).
3. **Démembrement progressif** : Combiner donation en nue-propriété et usufruit.
4. **Apport à une holding animatrice** : Structurer un groupe pour bénéficier de l’exception.

---

### **6. Recommandation**
**L’exonération de l’article 787 B n’est pas applicable en l’état.**
Nous vous conseillons :
- De **confirmer l’activité principale de la SAS** (audit fiscal si nécessaire).
- D’envisager des **montages alternatifs** pour réduire la charge fiscale.

**Prochaine étape :** Une réunion avec votre notaire pour affiner la stratégie.

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées]

---
**Note :** Ce conseil est basé sur les informations fournies. Une analyse complète nécessiterait un examen des statuts de la SAS et de sa structure de groupe (le cas échéant).

---

## S24

**Role de l'enonce :** mesure

**Fait manquant :** Les trois mentions obligatoires du III-B : la société relève-t-elle de l'article 1655 ter, les participations cédées confèrent-elles le droit à la jouissance d'immeubles, le cessionnaire acquitte-t-il des dettes contractées auprès du cédant. Aucune ne figure dans l'énoncé, et le rédacteur de l'acte ne peut pas les inventer.

**Dossier soumis au modele :**

```
Un client vous consulte avant de signer.

Il cede les titres d'une societe civile immobiliere dont l'actif est
constitue a 80 % d'immeubles situes en France. Prix de cession :
4 000 000 euros. L'acte sera signe le 20 mars 2024.

Quel droit d'enregistrement est du, et que doit contenir l'acte ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

**Maître [Votre Nom/Cabinet]**
Avocat au Barreau de [Ville]
Spécialiste en Droit Fiscal

**À l'attention de mon client**
**Objet :** Consultation fiscale préalable à la cession de vos titres de SCI
**Date :** 14 mars 2024 *(date fictive précédant la signature)*

Cher Client,

Vous m'avez consulté concernant votre projet de cession de la totalité des parts d'une Société Civile Immobilière (SCI) pour un prix de 4 000 000 d'euros, dont la signature est prévue le 20 mars 2024. Vous souhaitez connaître le montant des droits d'enregistrement exigibles ainsi que les mentions obligatoires devant figurer dans l'acte de cession.

Voici mon analyse et mes recommandations fondées sur l'article 726 du Code Général des Impôts (CGI) applicable à votre opération.

### 1. Sur le montant des droits d'enregistrement

**Qualification de la société :**
L'actif de votre SCI étant constitué à 80 % d'immeubles situés en France, elle répond fiscalement à la définition de « personne morale à prépondérance immobilière » (PMPI). En effet, la loi qualifie ainsi toute société dont l'actif est principalement (c'est-à-dire à plus de 50 %) constitué d'immeubles en France.

**Taux et calcul des droits :**
En vertu de l'article 726, I, 2° du CGI, les cessions de participations dans des sociétés à prépondérance immobilière sont soumises à un **droit d'enregistrement au taux proportionnel de 5 %**. 
Contrairement aux cessions de parts sociales de sociétés classiques, il n'y a ici aucun abattement applicable.

Sur la base de votre prix de cession de 4 000 000 €, le droit d'enregistrement de base s'élèvera donc à :
**4 000 000 € x 5 % = 200 000 €.**

*Point d'attention (Conseil de l'avocat) :* Sauf clause contraire dans l'acte, c'est l'acquéreur qui supporte la charge de ces droits. Toutefois, vis-à-vis de l'administration fiscale, le cédant et le cessionnaire sont solidairement responsables de leur paiement. Je veillerai à ce que l'acte précise bien que l'acquéreur en supportera la charge exclusive. 
De plus, si l'acquéreur rachète également votre compte courant d'associé (une dette de la SCI envers vous), le montant de ce compte courant sera ajouté au prix de cession pour le calcul des 5 %.

### 2. Sur le contenu obligatoire de l'acte de cession

Pour que l'acte soit conforme et puisse être enregistré sans rejet par l'administration fiscale, l'article 726, III, B du CGI impose que le contrat de cession contienne **expressément** trois déclarations. 

L'acte devra comporter une clause spécifique (généralement intitulée "Déclarations fiscales") indiquant expressément :

1. **Si la SCI est une société de copropriété (Art. 1655 ter du CGI) :** L'acte doit préciser si la société a pour unique objet la construction ou l'acquisition d'immeubles en vue de leur division par fractions destinées à être attribuées aux associés (société dite "transparente"). *Dans votre cas, il s'agira très probablement d'indiquer que la SCI ne relève pas de cet article.*
2. **Si la cession confère un droit de jouissance (Art. 728 du CGI) :** L'acte doit préciser si les parts cédées donnent à l'acquéreur le droit à la jouissance d'immeubles ou de fractions d'immeubles.
3. **Le sort des dettes de la société envers vous (le cédant) :** L'acte doit expressément indiquer si l'acquéreur a acquitté ou s'engage à acquitter (directement ou indirectement) des dettes contractées par la SCI envers vous (typiquement, le remboursement de votre compte courant d'associé). **Si c'est le cas, le montant exact de ces dettes doit être précisé dans l'acte.**

**Lieu de signature (Art. 726, III, A) :**
Enfin, j'attire votre attention sur un point formel : si vous et l'acquéreur prévoyez de signer cet acte à l'étranger, la loi impose que cette cession soit constatée dans un délai d'un mois par un acte authentique reçu par un notaire exerçant en France. Si vous signez en France (sous seing privé ou devant notaire), cette contrainte ne s'applique pas, mais l'acte devra tout de même être enregistré au service des impôts dans le délai d'un mois suivant sa signature.

### Mes recommandations pour la suite :

Étant donné que la signature est prévue le 20 mars, je vous invite à **me transmettre le projet d'acte de cession dans les plus brefs délais**. 

Je me chargerai de vérifier :
1. Que les trois mentions obligatoires y figurent avec la formulation adéquate.
2. Que la clause de prise en charge des droits d'enregistrement protège bien vos intérêts.
3. L'impact éventuel de la cession de votre compte courant d'associé sur la base taxable.

Je reste à votre entière disposition pour échanger de vive voix sur ce dossier.

Bien à vous,

**Votre Avocat**

---

## S25

**Role de l'enonce :** mesure

**Fait manquant :** Le jour de la cession, la bascule étant au 21 février 2026, et le secteur dans lequel le remploi serait fait.

**Dossier soumis au modele :**

```
Un client vous consulte.

Sa holding, qu'il controle a 100 %, a vendu en fevrier 2026 les
titres d'une societe d'exploitation qu'elle detenait, moins de
trois ans apres que le client les lui ait apportes. Elle a
encaisse 9 000 000 euros.

Le produit de la vente dort sur le compte de la holding. Le client
sait qu'il doit reinvestir une partie de cette somme pour
conserver le benefice du report d'imposition.

Que lui conseillez-vous ?

Voici le texte applicable.
```

**Reponse a coder, en entier :**

**CABINET [NOM] – AVOCATS AU BARREAU DE [VILLE]**
**Objet :** Consultation fiscale – Maintien du report d’imposition au titre de l’article 150-0 B ter du CGI suite à la cession de titres par votre holding
**Date :** [Date du jour]
**Réf. :** Dossier [N°]

Monsieur/Madame,

Je vous remercie de votre confiance. Je prends acte de la situation suivante : votre holding, que vous contrôlez à 100 %, a cédé en février 2026 les titres d’une société d’exploitation qu’elle détenait depuis moins de trois ans après leur apport, pour un produit net de cession de 9 000 000 €. Les fonds sont actuellement disponibles sur le compte bancaire de la holding. Vous souhaitez conserver le bénéfice du report d’imposition attaché à l’apport initial.

Voici mon analyse et mes recommandations, fondées sur l’article 150-0 B ter, I, 2° du Code général des impôts (CGI) et la doctrine administrative en vigueur.

---

### 🔹 1. Cadre légal et échéances impératives
La cession de titres apportés dans un délai de trois ans met normalement fin au report d’imposition. Toutefois, le 2° de l’article 150-0 B ter du CGI prévoit une dérogation conditionnelle :
- **Délai de réinvestissement :** 3 ans à compter de la date de cession → **au plus tard février 2029**
- **Seuil minimum :** 70 % du produit de cession → **6 300 000 €**
- **Nature de l’investissement :** financement de *moyens permanents d’exploitation* affectés à une activité éligible au sens du 3° du C du I de l’article 199 terdecies-0 A du CGI
- **Exclusion expresse :** les activités de gestion de patrimoine immobilier sont formellement exclues

⚠️ *À défaut de respect cumulatif du délai, du seuil et de la nature des investissements, le report prend fin et la plus-value latente devient immédiatement imposable à l’impôt sur les sociétés (taux de droit commun, soit 25 % + éventuelle contribution sociale).*

---

### 🔹 2. Qualification des investissements éligibles
L’administration fiscale interprète strictement la notion de *moyens permanents d’exploitation*. Sont généralement admis :
- Souscription ou acquisition de titres de filiales exerçant une activité industrielle, commerciale, artisanale, agricole ou libérale effective et permanente
- Apports en compte courant d’associé ou prêts à des sociétés opérationnelles éligibles
- Acquisition de fonds de commerce, de droits de propriété intellectuelle, de matériels ou logiciels nécessaires à l’exploitation
- Financement de projets de développement, de R&D, ou de création d’unités de production

🚫 **Sont exclus :**
- Placements financiers (OPCVM, SICAV, comptes à terme, obligations, etc.)
- Acquisition ou gestion de biens immobiliers (location nue, meublée, SCI de gestion, etc.)
- Rémunérations excessives, dividendes, ou avances à l’associé avant réinvestissement
- Conservation des fonds sur un compte courant sans affectation économique démontrée

---

### 🔹 3. Formalités et traçabilité requises
Le maintien du report est subordonné à une documentation rigoureuse :
1. **Engagement formel** : délibération du conseil d’administration ou de la gérance actant la décision de réinvestir au moins 6,3 M€ dans des moyens permanents d’exploitation éligibles, avec calendrier prévisionnel
2. **Traçabilité comptable** : ouverture d’un compte dédié ou annotation précise dans les écritures, permettant de suivre l’origine et l’emploi des fonds
3. **Justificatifs** : contrats d’acquisition, statuts de filiales, conventions de compte courant, factures d’immobilisations, attestations d’activité des sociétés cibles
4. **Déclaration fiscale** : production des pièces justificatives lors du dépôt de la liasse fiscale de l’exercice de réalisation des investissements, conformément aux obligations déclaratives prévues par l’administration

---

### 🔹 4. Recommandations opérationnelles
Afin de sécuriser le dispositif, je vous conseille de :
✅ **Acter sans délai** la décision de réinvestissement par une délibération formelle, précisant le montant, la nature des projets et le calendrier de déploiement  
✅ **Identifier et valider en amont** les projets d’investissement envisagés, en excluant toute activité de gestion immobilière ou de placement financier  
✅ **Isoler comptablement** les 6,3 M€ et éviter toute distribution (dividendes, rémunérations, avances) pouvant être requalifiée en utilisation du produit de cession  
✅ **Conserver l’ensemble des justificatifs** (conventions, factures, Kbis, attestations d’activité, relevés bancaires) dans un dossier dédié, prêt à être produit en cas de contrôle  
✅ **Prévoir un suivi trimestriel** de l’avancement des investissements pour garantir le respect du délai de février 2029

---

### 🔹 5. Prochaines étapes
Je reste à votre disposition pour :
- Analyser la qualification fiscale des projets concrets que vous étudiez
- Rédiger les délibérations, engagements et conventions de traçabilité
- Structurer les montages (filiales, apports, prêts) en conformité avec le CGI et la doctrine administrative
- Assurer le suivi jusqu’à la réalisation complète du réinvestissement et la déclaration fiscale correspondante

Je vous invite à me transmettre, dès que possible, les projets d’investissement envisagés, les statuts de la holding, ainsi que sa dernière liasse fiscale, afin que je puisse valider leur éligibilité et sécuriser juridiquement le dispositif.

Je vous prie d’agréer, Monsieur/Madame, l’expression de mes salutations distinguées.

**[Signature]**  
Maître [Nom]  
Avocat au Barreau de [Ville]  
Spécialiste en droit fiscal des affaires

---

## S26

**Role de l'enonce :** mesure

**Fait manquant :** Les prestations fournies aux occupants. Une location meublée nue relève de la gestion de son propre patrimoine immobilier ; une activité para-hôtelière, avec réception, ménage, linge et petit-déjeuner, est une activité d'hébergement commerciale.

**Dossier soumis au modele :**

```
Un dirigeant de 62 ans vous consulte avec son notaire.

Il souhaite donner a ses deux enfants, a parts egales et en pleine
propriete, la totalite des titres de sa societe par actions
simplifiee. Elle possede quarante appartements meubles. Valeur des
titres : 20 000 000 euros.

Les titres font l'objet d'un engagement collectif de conservation
signe le 3 mars 2021, portant sur la totalite des droits, toujours
en cours. Chaque enfant prend l'engagement individuel prevu par les
textes. Le dirigeant conserve la presidence pendant trois ans.

La donation serait signee le 25 octobre 2023.

L'exoneration partielle de l'article 787 B est-elle applicable ?

Voici le texte applicable a la date de la donation.
```

**Reponse a coder, en entier :**

**Objet : Analyse de l'applicabilité de l'exonération partielle de l'article 787 B du CGI à la donation projetée**

**À l’attention de [Nom du client] et de son notaire,**
**De la part de [Votre nom], Avocat fiscaliste**

---

### **1. Contexte et problématique**
Vous envisagez de donner, en pleine propriété et à parts égales, la totalité des titres de votre SAS (valeur : 20 000 000 €) à vos deux enfants. Ces titres sont soumis à un **engagement collectif de conservation (ECC)** signé le 3 mars 2021, toujours en cours. Chaque enfant prendra un **engagement individuel de conservation** conformément à l’article 787 B du CGI. Vous conserverez la présidence pendant 3 ans.

La question centrale est : **l’exonération partielle de 75 % prévue à l’article 787 B du CGI est-elle applicable à cette donation ?**

---

### **2. Conditions d’application de l’article 787 B**
L’exonération de 75 % s’applique sous réserve du **cumul** des conditions suivantes (CGI, art. 787 B) :

#### **A. Nature de l’activité de la société**
L’exonération vise les sociétés dont **l’activité principale** est :
- Industrielle, commerciale (au sens des articles 34 et 35 du CGI),
- Artisanale, agricole ou libérale.

**Exclusion explicite** :
> *"N'est pas considérée comme une activité industrielle, commerciale, artisanale, agricole ou libérale l'exercice par une société d'une activité de gestion de son propre patrimoine mobilier ou immobilier."*

**Cas de votre SAS** :
- La société détient **40 appartements meublés** et les gère.
- **Problème** : Cette activité relève **a priori** de la **gestion de patrimoine immobilier**, ce qui est **exclu** du bénéfice de l’exonération, sauf si la société exerce une activité **commerciale** au sens de l’article 35 du CGI.

**Analyse** :
- La location meublée peut être considérée comme une **activité commerciale** si elle est exercée **à titre professionnel** (avec intention de réaliser des bénéfices, inscription au RCS, etc.).
- **Mais** : L’article 787 B exclut explicitement la **gestion de son propre patrimoine immobilier**, même si cette gestion est commerciale.
- **Exception possible** : Si la SAS rend des **services spécifiques** (administratifs, juridiques, etc.) à un **groupe de sociétés** contrôlées exerçant une activité éligible (ex. : une société de construction ou de rénovation), elle pourrait être considérée comme ayant une activité commerciale **accessoire** à une activité principale éligible.

**Conclusion intermédiaire** :
- **Si la SAS se limite à la gestion de ses propres appartements meublés** → **Exclusion de l’exonération** (car gestion de patrimoine immobilier).
- **Si la SAS fait partie d’un groupe et rend des services à des filiales éligibles** → **À étudier** (mais votre description ne mentionne pas cette hypothèse).

---

#### **B. Engagement de conservation**
Les conditions sont **remplies** :
1. **Engagement collectif de conservation (ECC)** : Signé le 3 mars 2021 (toujours en cours).
2. **Engagement individuel** : Chaque enfant prendra l’engagement de conserver les titres pendant **2 ans** (minimum légal).
3. **Durée de l’ECC** : L’ECC doit couvrir **au moins 2 ans après la donation** (ce qui sera le cas ici, car il est toujours en cours).

**Point de vigilance** :
- L’ECC doit porter sur **la totalité des droits** (ce qui est le cas).
- La donation doit intervenir **pendant la durée de l’ECC** (ce qui sera le cas, car la donation est prévue le 25/10/2023).

---

#### **C. Autres conditions**
- **Transmission en pleine propriété** : Oui (vous donnez la pleine propriété).
- **Bénéficiaires** : Les enfants (éligibles, car descendants en ligne directe).
- **Société concernée** : SAS (forme sociale éligible).

---

### **3. Conclusion sur l’applicabilité de l’exonération**
**L’exonération de 75 % de l’article 787 B ne semble pas applicable** dans votre cas, **sauf si** :
1. **La SAS exerce une activité commerciale principale autre que la gestion de son patrimoine immobilier** (ex. : location meublée **professionnelle** avec services associés type hôtelier, ou participation active à un groupe éligible).
   - **À vérifier** : La SAS est-elle immatriculée au RCS ? A-t-elle un **caractère commercial avéré** (comptabilité, TVA, etc.) ?
   - **À vérifier** : La location meublée est-elle **accessoire** à une autre activité (ex. : restauration, services aux locataires) ?

2. **La SAS fait partie d’un groupe et rend des services à des filiales éligibles** (hypothèse non évoquée dans votre description).

**En l’état des informations fournies (SAS détenant 40 appartements meublés sans autre activité mentionnée), l’activité principale semble être la gestion de patrimoine immobilier → exclusion de l’exonération.**

---

### **4. Recommandations**
1. **Vérifier la qualification de l’activité de la SAS** :
   - Consulter les statuts, l’objet social, et les déclarations fiscales (BIC ou revenus fonciers ?).
   - Si la SAS est **immatriculée au RCS** et exerce une **activité commerciale principale** (ex. : location meublée professionnelle avec services), l’exonération pourrait s’appliquer.

2. **Alternatives si l’exonération 787 B est exclue** :
   - **Pacte Dutreil** (article 787 C du CGI) :
     - Exonération de 75 % sous conditions (engagement de conservation de 2 ans + engagement collectif de 2 ans supplémentaires).
     - **Mais** : Même problème si l’activité est la gestion de patrimoine immobilier (l’article 787 C renvoie à l’article 787 B pour la définition de l’activité éligible).
   - **Donation en nue-propriété** + usufruit conservé :
     - Réduction des droits (abattement de 100 000 € par parent et par enfant tous les 15 ans).
     - Mais pas d’exonération spécifique.
   - **Report d’imposition** (article 150-0 B ter du CGI) :
     - Si vous cédez les titres à vos enfants à prix réduit (ex. : valeur nominale), le report d’imposition sur la plus-value peut être envisagé.

3. **Consulter l’administration fiscale** :
   - Demander un **rescrit fiscal** pour sécuriser la position (notamment sur la qualification de l’activité).

---

### **5. Synthèse juridique**
| Condition | Applicable ? | Commentaire |
|-----------|-------------|-------------|
| **Activité éligible** (industrielle, commerciale, etc.) | ❌ **Non** (sauf preuve contraire) | Gestion de patrimoine immobilier exclue, sauf si activité commerciale principale avérée. |
| **Engagement collectif de conservation** | ✅ Oui | ECC signé en 2021, toujours en cours. |
| **Engagement individuel** | ✅ Oui | Pris par les enfants. |
| **Transmission en pleine propriété** | ✅ Oui | Donation en pleine propriété. |
| **Bénéficiaires éligibles** | ✅ Oui | Enfants en ligne directe. |

**→ L’exonération de l’article 787 B n’est pas applicable en l’état, sauf si l’activité de la SAS est requalifiée comme commerciale principale (hors gestion de patrimoine).**

---

### **6. Prochaines étapes**
1. **Analyser les statuts et l’activité réelle de la SAS** pour confirmer si elle exerce une activité commerciale éligible.
2. **Envisager un rescrit fiscal** pour sécuriser la position.
3. **Étudier les alternatives** (Pacte Dutreil, donation en nue-propriété, etc.).

Je reste à votre disposition pour approfondir cette analyse ou examiner les documents de la SAS.

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées du cabinet]

---

## S27

**Role de l'enonce :** mesure

**Fait manquant :** Les prestations fournies aux occupants. Une location meublée nue relève de la gestion de son propre patrimoine immobilier ; une activité para-hôtelière, avec réception, ménage, linge et petit-déjeuner, est une activité d'hébergement commerciale.

**Dossier soumis au modele :**

```
Un dirigeant de 62 ans vous consulte avec son notaire.

Il souhaite donner a ses deux enfants, a parts egales et en pleine
propriete, la totalite des titres de sa societe par actions
simplifiee. Elle possede quarante appartements meubles. Valeur des
titres : 20 000 000 euros.

Les titres font l'objet d'un engagement collectif de conservation
signe le 3 mars 2021, portant sur la totalite des droits, toujours
en cours. Chaque enfant prend l'engagement individuel prevu par les
textes. Le dirigeant conserve la presidence pendant trois ans.

La donation serait signee le 25 octobre 2023.

L'exoneration partielle de l'article 787 B est-elle applicable ?

Voici le texte applicable a la date de la donation.
```

**Reponse a coder, en entier :**

**OBJET : Consultation fiscale – Applicabilité de l’exonération partielle de l’article 787 B du CGI à une donation de titres de SAS détenant 40 appartements meublés**

---

### I. RAPPEL DES ÉLÉMENTS DE FAIT
- **Donateur** : Président d’une SAS, 62 ans
- **Bénéficiaires** : Deux enfants, donation à parts égales en pleine propriété
- **Actif cédé** : 100 % des titres de la SAS, valeur vénale : 20 000 000 €
- **Activité de la société** : Détention et mise en location de 40 appartements meublés
- **Engagement collectif de conservation** : Signé le 3 mars 2021, portant sur la totalité des droits, toujours en cours au 25 octobre 2023
- **Engagements individuels** : Prévus par chaque enfant
- **Fonction dirigeante** : Le donateur conserve la présidence pendant 3 ans post-donation
- **Date de la donation** : 25 octobre 2023
- **Question posée** : L’exonération partielle de 75 % prévue à l’article 787 B du CGI est-elle applicable ?

---

### II. CADRE JURIDIQUE APPLICABLE
L’article 787 B du CGI subordonne l’exonération partielle de 75 % des droits de mutation à titre gratuit au respect de **conditions cumulatives** :

1. **Condition d’activité** : La société doit exercer à titre principal une activité industrielle, commerciale, artisanale, agricole ou libérale. Le texte exclut expressément *« l’exercice par une société d’une activité de gestion de son propre patrimoine mobilier ou immobilier »*.
2. **Engagement collectif de conservation** : Signé avant la donation, portant sur au moins 34 % des droits financiers et 17 % des droits de vote, et maintenu pendant 6 ans. Pour une donation, l’exonération est acquise si l’engagement est en cours depuis **au moins 2 ans** à la date de l’acte.
3. **Engagements individuels des donataires** : Souscrits pour une durée minimale de 4 ans.
4. **Condition de fonction dirigeante** : Le donateur doit exercer une fonction de direction (président, directeur général, gérant, etc.) pendant la durée de l’engagement collectif et **pendant les 3 années suivant la donation**.

---

### III. ANALYSE AU CAS D’ESPÈCE

#### A. Conditions formelles et de conservation : **réunies**
- L’engagement collectif a été signé le 3 mars 2021. Au 25 octobre 2023, il est en vigueur depuis **2 ans et 7 mois**, ce qui satisfait la condition des 2 ans préalables à la donation pour une application immédiate de l’exonération.
- Les engagements individuels des enfants sont prévus.
- La conservation de la présidence pendant 3 ans post-donation respecte la condition de fonction dirigeante.

#### B. Condition d’activité éligible : **non remplie en l’état**
C’est le point bloquant. La doctrine administrative et la jurisprudence sont constantes sur ce point :

- **BOI-ENR-DMTG-10-20-20-20, § 40** : *« La location de biens immobiliers, même meublés, est en principe exclue du champ de l’exonération, sauf si elle s’accompagne de prestations de services caractérisant une activité hôtelière ou para-hôtelière. »*
- **Conseil d’État, 9 décembre 2015, n° 373888** et **27 juillet 2018, n° 408388** : La location meublée, bien que relevant fiscalement des BIC pour l’impôt sur le revenu, **ne constitue pas une activité commerciale au sens de l’article 787 B** dès lors qu’elle se limite à la mise à disposition de logements sans prestations de services substantielles, organisées et facturées séparément. Elle est requalifiée en *gestion de patrimoine immobilier*, expressément exclue par le CGI.

En l’absence d’éléments indiquant que la SAS fournit des services caractéristiques d’une exploitation hôtelière/para-hôtelière (accueil, ménage régulier, restauration, conciergerie, blanchisserie, gestion de réservations, etc.), l’activité sera très probablement considérée par l’administration comme de la **gestion de patrimoine immobilier**. L’exonération de 75 % serait donc **refusée**.

---

### IV. CONCLUSION ET RECOMMANDATIONS

**Conclusion** : 
Toutes les conditions formelles, temporelles et de fonction dirigeante sont satisfaites. En revanche, **la condition substantielle d’activité éligible fait défaut**. Sauf preuve d’une activité para-hôtelière caractérisée, **l’exonération partielle de l’article 787 B du CGI ne sera pas applicable** à cette donation.

**Recommandations opérationnelles** :
1. **Audit précis de l’activité réelle** : Examiner les contrats de location, les factures, l’organisation interne, les effectifs, la nature et la valeur des prestations annexes. Si des services substantiels sont effectivement rendus et facturés, une requalification en activité commerciale/para-hôtelière pourra être défendue.
2. **Alternative de structuration** : 
   - Scinder l’actif immobilier et l’activité de gestion/services pour isoler une entité éligible au pacte Dutreil.
   - Transformer l’exploitation en résidence avec services ou hôtel, sous réserve de viabilité économique et de conformité urbanistique.
   - Recourir à d’autres dispositifs de transmission (donation avec réserve d’usufruit, donation-partage, apport à une holding familiale, etc.) en fonction de l’objectif patrimonial.
3. **Prudence fiscale** : Demander l’exonération sans fondement solide expose à un rejet, des rappels de droits, intérêts de retard et pénalités (40 % ou 80 % en cas de manquement délibéré). Une prise de position écrite de l’administration (rescrit) ou un audit contradictoire préalable est fortement recommandée avant signature.

---

### V. RÉSERVES ET PROCHAINES ÉTAPES
Cette analyse repose sur les éléments communiqués. Elle devra être complétée par :
- L’examen des statuts, des derniers bilans, des contrats de location et de la comptabilité analytique
- La vérification de l’absence de clause de réserve d’usufruit ou de démembrement
- La coordination avec votre notaire pour la rédaction de l’acte et la qualification fiscale de l’activité

Je reste à votre disposition pour organiser une réunion de travail avec votre notaire et, si nécessaire, votre expert-comptable, afin de valider la qualification de l’activité et d’explorer les voies d’optimisation compatibles avec votre projet de transmission.

*Veuillez agréer, Monsieur, l’expression de mes salutations distinguées.*

**[Nom]**  
Avocat au Barreau de [Ville]  
Spécialiste en droit fiscal et transmission d’entreprise  
*Note : Cette consultation est établie sur la base des éléments fournis et du droit applicable à la date de la donation. Elle ne vaut pas engagement de résultat et ne dispense pas d’un examen complet du dossier.*

---

## S28

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

**Réponse : Non, aucune retenue à la source n'est due**, sous réserve du strict respect des formalités prévues par l'article 119 ter du CGI.

---

### I. Le texte applicable n'est pas l'article 119 bis mais l'article 119 ter

Le texte que vous me soumettez (article 119 bis, 2, al. 1 du CGI) énonce le **principe** de la retenue à la source sur les produits distribués à des personnes n'ayant pas leur domicile fiscal ou leur siège en France. Il contient déjà une première exception pour les OPCVM étrangers. Mais ce n'est pas ce texte qui régit la situation décrite.

Le texte applicable est l'**article 119 ter du CGI**, qui transpose la directive 2011/96/UE du 30 novembre 2011 (directive « mère-fille ») et qui prévoit une **exonération de la retenue à la source** pour les dividendes versés par une filiale française à sa société mère située dans un État membre de l'UE.

L'article 119 ter commence précisément par poser une **exception à la retenue à la source prévue à l'article 119 bis**.

---

### II. Conditions d'application du régime mère-fille (article 119 ter du CGI)

L'exonération est subordonnée à la réunion **cumulative** des conditions suivantes :

1. **La bénéficiaire effective est une « société mère »** au sens de la directive mère-fille, c'est-à-dire une entité soumise à l'IS dans un État membre de l'UE (ou de l'EEE avec clause d'assistance administrative en matière fiscale) ;
2. **Détention d'au moins 10 % du capital** de la société distributrice ;
3. **Conservation de cette participation pendant au moins deux ans** ;
4. **Absence de régime fiscal privilégié** au sens de l'article 238 A du CGI (régime dans lequel l'imposition est inférieure à 50 % de l'IS français).

---

### III. Application au cas d'espèce

Toutes les conditions sont remplies :

| Condition | Situation | Analyse |
|---|---|---|
| Qualité de la mère | SA de droit luxembourgeois | ✓ Société soumise à l'IRC luxembourgeois (taux global ≈ 24,94 % : IS 17 % + contribution de solidarité 7 % + ICC ≈ 6,75 %), régime de droit commun comparable à l'IS français |
| Localisation | Luxembourg | ✓ État membre de l'UE |
| Seuil de participation | 100 % | ✓ Largement au-delà du seuil de 10 % |
| Durée de détention | 5 ans | ✓ Largement au-delà du seuil de 2 ans |
| Régime non privilégié | SA de droit commun | ✓ Contrairement aux SPF ou SICAF, la SA de droit commun luxembourgeoise n'est pas dans un régime fiscal privilégié |

---

### IV. Formalités indispensables

L'exonération **n'est pas automatique**. La société mère luxembourgeoise doit :

1. **Produire une attestation** conforme (formulaire n° 2777), par laquelle elle :
   - certifie être une « société mère » au sens de la directive mère-fille ;
   - s'engage à être imposée sur les dividendes dans son État de résidence.

2. **Remettre cette attestation à la société distributrice française avant la mise en paiement** (idéalement au début du mois de juin 2025). L'attestation est en principe valable trois ans.

3. **La société distributrice doit conserver ce document** et le produire à l'administration fiscale sur demande.

À défaut d'attestation dans les délais, la retenue à la source serait liquidée au taux de droit commun des non-résidents (**25 %** en 2025), soit **5 000 000 €** définitivement perdus.

---

### V. Conclusion

La distribution de **20 000 000 €** prévue le **15 juin 2025** peut être effectuée **en exonération de toute retenue à la source**, à la condition que :

- la société mère luxembourgeoise détienne effectivement la participation depuis au moins deux ans à la date de mise en paiement (condition déjà satisfaite avec cinq ans de détention) ;
- elle produise l'**attestation réglementaire (formulaire 2777)** à la société distributrice **avant la mise en paiement**.

Une fois l'exonération appliquée, les dividendes seront effectivement imposés au Luxembourg (au niveau de la mère), conformément à l'engagement souscrit dans l'attestation.

---

### Recommandations pratiques

- Anticiper l'envoi de l'attestation : viser une réception **avant le 1er juin 2025** ;
- Vérifier que la SA luxembourgeoise n'est pas une entité relevant d'un secteur spécifique (Soparfis, holdings d'investissement) qui pourrait soulever des interrogations sur l'absence de régime privilégié ;
- Conserver l'attestation dans la liasse fiscale de l'exercice 2025 et la mentionner sur la **déclaration n° 2777** déposée par voie dématérialisée.

---

## S29

**Role de l'enonce :** mesure

**Fait manquant :** Le combustible de la chaudière. Une chaudière peut fonctionner au gaz, au fioul ou à l'électricité, et le texte ne vise que les combustibles fossiles.

**Dossier soumis au modele :**

```
Une entreprise de plomberie fait l'objet d'une proposition de
rectification. L'administration lui reclame la difference entre
5,5 % et 20 % sur des chantiers de renovation energetique.

Le gerant vous consulte. Sur le chantier litigieux, facture le
15 avril 2025, l'entreprise a installe une chaudiere dans une
maison de quinze ans, occupee par son proprietaire. Montant des
travaux : 8 500 euros hors taxes.

L'entreprise a applique le taux de 5,5 %. Ce taux etait-il correct ?

Voici le texte applicable a la date des travaux.
```

**Reponse a coder, en entier :**

**Conclusion : le taux de 5,5 % n’était pas applicable**, sous réserve que l’équipement posé soit bien une *chaudière susceptible d’utiliser des combustibles fossiles*.

Les conditions générales du I de l’article 278-0 bis A sont, en l’espèce, remplies :

- maison achevée depuis plus de deux ans (quinze ans) ;
- local affecté à l’habitation ;
- travaux portant sur le chauffage.

Toutefois, le **III bis** du même article prévoit expressément une dérogation : le taux normal de l’article 278, soit **20 %**, s’applique aux prestations de rénovation énergétique comprenant la fourniture ou l’installation d’une chaudière susceptible d’utiliser des combustibles fossiles.

Cette disposition dérogatoire prime donc les conditions favorables du I. Le fait que le logement soit ancien, occupé par son propriétaire et que l’installation améliore la performance énergétique ne permet pas de conserver le taux de 5,5 %.

Sur une base de **8 500 € HT** :

- TVA facturée à 5,5 % : **467,50 €** ;
- TVA légalement due à 20 % : **1 700 €** ;
- rappel de TVA en principal : **1 232,50 €**, avant intérêts de retard et, le cas échéant, pénalités.

**Point à vérifier avant toute acceptation du rappel :** la qualification technique exacte de l’appareil installé. Si l’équipement n’est pas juridiquement une chaudière susceptible d’utiliser un combustible fossile — par exemple une pompe à chaleur sans possibilité d’usage d’un combustible fossile — le III bis ne serait pas applicable. Il convient donc d’examiner le devis, la facture détaillée, la référence fabricant, la fiche technique et le mode d’alimentation de l’appareil.

---

## S30

**Role de l'enonce :** mesure

**Fait manquant :** Les prestations fournies aux occupants. Une location meublée nue relève de la gestion de son propre patrimoine immobilier ; une activité para-hôtelière, avec réception, ménage, linge et petit-déjeuner, est une activité d'hébergement commerciale.

**Dossier soumis au modele :**

```
Un dirigeant de 62 ans vous consulte avec son notaire.

Il souhaite donner a ses deux enfants, a parts egales et en pleine
propriete, la totalite des titres de sa societe par actions
simplifiee. Elle possede quarante appartements meubles. Valeur des
titres : 20 000 000 euros.

Les titres font l'objet d'un engagement collectif de conservation
signe le 3 mars 2021, portant sur la totalite des droits, toujours
en cours. Chaque enfant prend l'engagement individuel prevu par les
textes. Le dirigeant conserve la presidence pendant trois ans.

La donation serait signee le 25 octobre 2023.

L'exoneration partielle de l'article 787 B est-elle applicable ?

Voici le texte applicable a la date de la donation.
```

**Reponse a coder, en entier :**

## Avis

**Au vu des faits indiqués, l’exonération partielle de 75 % prévue par l’article 787 B du CGI n’est pas applicable à la donation du 25 octobre 2023.**

### 1. L’activité de location meublée est en principe commerciale…

La location habituelle de locaux d’habitation meublés relève des activités commerciales visées à l’article 35 du CGI. Sous l’empire de la rédaction antérieure de l’article 787 B, la Cour de cassation avait ainsi admis qu’une activité de location meublée pouvait être éligible au régime Dutreil.

### 2. …mais elle est désormais expressément exclue lorsqu’elle constitue la gestion du propre patrimoine immobilier de la société

Le texte applicable à la transmission énonce désormais que :

> « n’est pas considérée comme une activité […] commerciale […] l’exercice par une société d’une activité de gestion de son propre patrimoine mobilier ou immobilier ».

La SAS possède elle-même les quarante appartements qu’elle exploite en location meublée. En l’absence d’autres éléments — notamment une véritable activité hôtelière ou para-hôtelière assortie de prestations substantielles — son activité consiste à gérer et exploiter son **propre patrimoine immobilier**.

L’exclusion spéciale du deuxième alinéa prévaut donc sur la qualification commerciale résultant de l’article 35 du CGI. Le nombre d’appartements, leur valeur ou l’exploitation sous forme de SAS ne modifient pas cette analyse.

### 3. La date de la donation place l’opération dans le champ de cette exclusion

La nouvelle rédaction a été rendue applicable aux transmissions intervenues **à compter du 17 octobre 2023**. La donation envisagée le **25 octobre 2023** est donc concernée, même si :

- l’engagement collectif a été conclu le 3 mars 2021 ;
- cet engagement demeure en cours ;
- à la date de sa conclusion, la jurisprudence ou la rédaction du texte pouvait permettre une autre lecture.

La signature de l’engagement collectif ne crée pas un droit acquis à l’exonération. L’éligibilité de l’activité doit notamment être vérifiée à la date du fait générateur, c’est-à-dire à la date de la donation.

### 4. Les autres conditions Dutreil ne suffisent pas

Les conditions formelles paraissent, sous réserve de la rédaction des actes, pouvoir être satisfaites :

- engagement collectif portant sur 100 % des droits ;
- durée minimale de deux ans écoulée ;
- engagements individuels des enfants ;
- donation en pleine propriété et à parts égales ;
- maintien du donateur à la présidence pendant les trois années suivant la transmission, à condition qu’il ait signé l’engagement et exerce effectivement la fonction de direction.

Mais ces conditions sont sans effet si la condition première tenant à la nature de l’activité n’est pas remplie.

## Conclusion

La donation ne peut pas bénéficier :

- de l’exonération de **75 %** de l’article 787 B du CGI ;
- ni, par voie de conséquence, de la réduction de droits de **50 %** prévue pour certaines donations en pleine propriété de titres bénéficiant du régime Dutreil par un donateur âgé de moins de 70 ans.

Une conclusion différente ne pourrait être envisagée que si l’examen concret de l’exploitation révélait une **activité opérationnelle hôtelière ou para-hôtelière réelle**, distincte de la simple location et gestion des appartements appartenant à la SAS. Les seuls faits communiqués ne permettent pas de retenir cette qualification.

---

## S31

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

**Objet : Analyse de la retenue à la source sur la distribution de dividendes à une société mère luxembourgeoise**

**Référence :** CGI, art. 119 bis, 2 / Convention fiscale franco-luxembourgeoise

**Client :** [Nom de la société française]

**Contexte :**
Votre société envisage de distribuer **20 000 000 €** à sa société mère luxembourgeoise (détentrice de 100 % du capital depuis 5 ans, SA soumise à l’IS luxembourgeois). La distribution serait payée le **15 juin 2025**.

**Question :** Une retenue à la source (RAS) est-elle due en France sur cette distribution ?

---

### **1. Principe général (CGI, art. 119 bis, 2)**
Les dividendes versés à un bénéficiaire **non résident fiscal français** sont soumis à une **retenue à la source (RAS)** de **30 %** (taux de droit commun, CGI art. 187), **sauf exemption ou réduction prévue par une convention fiscale**.

**Exception possible :**
- Si le bénéficiaire est un **organisme de placement collectif (OPC)** de l’UE ou d’un État ayant une convention d’assistance administrative avec la France (ce qui n’est pas le cas ici, la mère étant une SA luxembourgeoise classique).

→ **La société mère luxembourgeoise n’étant pas un OPC, le principe est l’application de la RAS à 30 %**, **sauf si la convention franco-luxembourgeoise prévoit une exemption ou un taux réduit**.

---

### **2. Application de la convention fiscale franco-luxembourgeoise**
La France et le Luxembourg ont signé une **convention pour éviter les doubles impositions (CDI)**. Selon l’**article 10 de la CDI franco-luxembourgeoise** (version applicable en 2025) :

- **Si la société mère luxembourgeoise détient au moins 10 % du capital de la filiale française depuis au moins 1 an**, les dividendes sont **exonérés de retenue à la source en France** (taux de 0 %).

**Conditions remplies dans votre cas :**
✅ **Détention de 100 %** (≫ 10 %)
✅ **Durée de détention : 5 ans** (≫ 1 an)
✅ **Bénéficiaire : SA luxembourgeoise soumise à l’IS** (éligible)

→ **Exemption totale de RAS en France** (taux de 0 %).

---

### **3. Vérifications complémentaires**
Pour sécuriser l’exemption, il faut confirmer :
- **La résidence fiscale de la société mère** : Elle doit être **résidente fiscale du Luxembourg** (certificat de résidence fiscale à fournir).
- **Absence d’abus de droit** : La structure ne doit pas être artificielle (risque de requalification en abus de droit si la société luxembourgeoise est une simple boîte aux lettres).
- **Forme juridique** : La SA luxembourgeoise est bien éligible (pas de restriction dans la CDI).

---
---
### **4. Conclusion et recommandations**
✅ **Aucune retenue à la source n’est due en France** sur cette distribution, **sous réserve** :
1. **Fourniture d’un certificat de résidence fiscale luxembourgeois** (à obtenir avant le paiement).
2. **Vérification que la société mère est bien soumise à l’IS au Luxembourg** (pas de régime fiscal privilégié excluant l’application de la CDI).
3. **Conservation des preuves de détention** (registre des actionnaires, statuts, etc.) pour justifier l’exemption en cas de contrôle fiscal.

**Action à mener :**
- **Avant le 15 juin 2025**, obtenir le **certificat de résidence fiscale** de la société mère et le transmettre à l’administration française (ou à l’établissement payeur si la RAS est gérée par un tiers).
- **Documenter la détention** (preuves des 5 ans de participation).

**Risque en cas de non-respect :**
Si le certificat n’est pas fourni, la RAS de **30 %** (soit **6 000 000 €**) serait due, avec pénalités en cas de régularisation tardive.

---
**Prochaines étapes :**
- Je peux vous aider à rédiger une **demande de certificat de résidence** pour la société mère.
- Si besoin, nous pouvons aussi analyser d’éventuels **risques de requalification** (ex. : substance économique insuffisante au Luxembourg).

**N’hésitez pas à me solliciter pour toute précision.**

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Cabinet / Coordonnées]

---

## S32

**Role de l'enonce :** mesure

**Fait manquant :** Le jour de la cession, la bascule étant au 21 février 2026, et le secteur dans lequel le remploi serait fait.

**Dossier soumis au modele :**

```
Un client vous consulte.

Sa holding, qu'il controle a 100 %, a vendu en fevrier 2026 les
titres d'une societe d'exploitation qu'elle detenait, moins de
trois ans apres que le client les lui ait apportes. Elle a
encaisse 9 000 000 euros.

Le produit de la vente dort sur le compte de la holding. Le client
sait qu'il doit reinvestir une partie de cette somme pour
conserver le benefice du report d'imposition.

Que lui conseillez-vous ?

Voici le texte applicable.
```

**Reponse a coder, en entier :**

**Cabinet d'Avocats - Fiscalité d'entreprise et patrimoniale**

**À l'attention de :** [Nom du Client]
**Objet :** Maintien du report d'imposition suite à la cession des titres de la société d'exploitation par votre holding
**Date :** 15 mars 2026
**Dossier :** N° 2026-014

---

Cher Client,

Suite à notre consultation relative à la cession intervenue en février 2026 par votre holding des titres de votre société d'exploitation, et après analyse des dispositions de l'article 150-0 B ter du Code général des impôts (CGI) que vous m'avez transmis, voici mon analyse et mes recommandations.

### 1. Analyse de la situation et du risque fiscal

Votre holding a cédé les titres en février 2026, soit moins de trois ans après la date à laquelle vous les lui avez apportés. En principe, cette cession prématurée entraîne l'expiration du report d'imposition dont vous avez bénéficié lors de l'apport, ce qui impliquerait l'imposition immédiate de la plus-value d'apport à votre niveau (personne physique).

Toutefois, le législateur a prévu une exception (une dérogation) permettant de maintenir ce report d'imposition, sous conditions strictes de réinvestissement.

### 2. Les conditions de sauvegarde du report d'imposition

Pour ne pas mettre fin au report d'imposition, votre holding doit respecter les conditions cumulatives suivantes :

*   **Seuil de réinvestissement :** La holding doit réinvestir **au moins 70 %** du produit de la cession.
    *   *Calcul :* Sur un produit de 9 000 000 €, le montant minimum à réinvestir est de **6 300 000 €**.
*   **Délai de réinvestissement :** Ce réinvestissement doit être réalisé **dans un délai de trois ans à compter de la date de la cession** (soit au plus tard en février 2029).
*   **Nature du réinvestissement :** Les fonds doivent être investis dans le "financement de moyens permanents d'exploitation affectés à son activité" (telle que définie à l'article 199 terdecies-0 A du CGI, qui qualifie généralement la holding de "holding animatrice"). 
    *   *Exclusion expresse :* Les activités de gestion de son propre patrimoine immobilier sont expressément exclues. Le réinvestissement dans de la pierre (immobilier de rapport) pour le compte de la holding est donc proscrit pour bénéficier de la dérogation.

### 3. Mes recommandations et plan d'action

Afin de sécuriser votre situation fiscale, je vous conseille de mettre en œuvre les actions suivantes :

**A. Formaliser l'engagement de réinvestissement**
L'administration fiscale exige que la holding prenne formellement l'engagement de réinvestir. Cet engagement doit être joint à la déclaration de revenus de la holding (ou à votre propre déclaration de revenus pour l'année de la cession, 2026, à déposer en 2027). Nous devrons rédiger cet acte d'engagement de manière précise.

**B. Définir une stratégie d'investissement éligible (pour 6,3 M€)**
Laisser les 9 millions d'euros dormir sur le compte courant de la holding ne constitue pas un réinvestissement éligible. Vous devez affecter 6,3 M€ à des "moyens permanents d'exploitation". Concrètement, cela peut prendre les formes suivantes :
1.  **Acquisition de titres de sociétés exerçant une activité commerciale, industrielle, artisanale, libérale ou agricole :** La holding peut racheter des participations dans d'autres entreprises pour animer et contrôler leur activité.
2.  **Financement des filiales :** Octroi d'avances en comptes courants d'associés ou de prêts à des sociétés dans lesquelles la holding détient une participation, à condition que ces fonds soient utilisés par ces sociétés pour leur propre exploitation (achat de matériel, fonds de commerce, etc.).
3.  **Développement d'une activité propre :** Si la holding exerce déjà une activité opérationnelle directe (en plus de la gestion de ses participations), l'achat de matériels ou d'immobilisations incorporelles nécessaires à cette activité est éligible.

**C. Gestion du solde (2,7 M€)**
Les 30 % restants (soit 2,7 M€) ne sont pas soumis à l'obligation de réinvestissement. Cette somme pourra être utilisée librement par la holding (distribution de dividendes, placement financier, investissement immobilier locatif, etc.), sous réserve de la fiscalité classique des sociétés (IS).

### 4. Prochaines étapes

Je vous propose que nous organisions une réunion de travail dans les prochaines semaines pour :
1.  Rédiger et valider l'engagement formel de réinvestissement.
2.  Étudier vos projets de croissance externe ou de financement pour s'assurer qu'ils entrent parfaitement dans le cadre légal des "moyens permanents d'exploitation".

Je reste à votre entière disposition pour toute précision.

Bien cordialement,

**[Votre Nom]**
Avocat à la Cour - Spécialiste en Droit Fiscal

---

## S33

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un client vous consulte.

Sa holding, qu'il controle a 100 %, a vendu le 10 novembre 2025 les
titres d'une societe d'exploitation qu'elle detenait, moins de
trois ans apres que le client les lui ait apportes. Elle a
encaisse 9 000 000 euros.

Le client veut reinvestir dans une societe qui achete des
immeubles pour les renover et les revendre.

Ce remploi permet-il de maintenir le report d'imposition ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

**Objet : Analyse de la possibilité de maintien du report d’imposition (art. 150-0 B ter du CGI) – Cession des titres et projet de réinvestissement**

**Maître [Votre Nom]**
Avocat fiscaliste
[Coordonnées du cabinet]

**À l’attention de [Nom du client]**
[Date]

---

**Cher Monsieur [Nom du client],**

Je vous remercie pour votre consultation concernant la cession des titres de votre société d’exploitation par votre holding et les conditions de maintien du report d’imposition prévu à l’**article 150-0 B ter, I, 2° du Code général des impôts (CGI)**. Voici une analyse détaillée de votre situation au regard des dispositions applicables, ainsi que les recommandations pour sécuriser votre opération.

---

### **1. Rappel des faits et enjeux**
Votre holding a cédé le **10 novembre 2025** les titres d’une société d’exploitation qu’elle détenait, **moins de trois ans après leur apport** par vos soins (date à préciser). Le produit de cession s’élève à **9 000 000 €**. Vous souhaitez **réinvestir ce produit** dans une société dont l’activité consiste à **acheter des immeubles pour les rénover et les revendre** (activité de *marchand de biens*).

L’enjeu est de **maintenir le report d’imposition** sur la plus-value d’apport (initialement reportée en application de l’article 150-0 B ter), faute de quoi cette plus-value deviendrait immédiatement imposable (au taux de **30 %** pour l’IR + prélèvements sociaux, ou **19 %** pour l’IS si la holding est soumise à l’IS, sous réserve des régimes spécifiques).

---

### **2. Conditions de maintien du report d’imposition (art. 150-0 B ter, I, 2°)**
Le texte prévoit une **dérogation au principe de fin du report** en cas de cession des titres dans les **3 ans suivant l’apport**, **à condition que** :
1. **La société bénéficiaire de l’apport (votre holding) prenne l’engagement** de réinvestir le produit de cession ;
2. **Le réinvestissement intervienne dans un délai de 2 ans** à compter de la cession (soit avant le **10 novembre 2027** pour votre cas) ;
3. **Le réinvestissement porte sur au moins 60 % du produit de cession** (soit **5 400 000 € minimum** sur les 9 000 000 €) ;
4. **L’investissement soit affecté au financement de moyens permanents d’exploitation** d’une activité éligible (commerciale, industrielle, artisanale, libérale, agricole ou financière), **à l’exclusion des activités de gestion de patrimoine mobilier ou immobilier**.

---

### **3. Analyse de l’éligibilité de votre projet de réinvestissement**
#### **a) Activité de la société cible : marchand de biens**
Votre projet consiste à investir dans une société dont l’activité est l’**achat-revente d’immeubles rénovés**. Cette activité relève de la **catégorie des bénéfices industriels et commerciaux (BIC)** et est considérée comme **commerciale** au sens de l’**article 34 du CGI** (activités de négoce).

**→ Cette activité est *a priori* éligible** au réinvestissement, car elle n’est pas expressément exclue par le texte (contrairement à la gestion de patrimoine immobilier, qui vise les activités de location ou de détention passive d’immeubles).

#### **b) Risques d’interprétation par l’administration fiscale**
Cependant, l’administration fiscale pourrait **contester l’éligibilité** de cette activité en s’appuyant sur les arguments suivants :
- **Caractère spéculatif** : L’achat-revente d’immeubles avec rénovation peut être perçu comme une activité **proche de la gestion de patrimoine immobilier**, surtout si les immeubles sont détenus sur une courte période (risque de requalification en activité de "gestion de patrimoine").
- **Absence de moyens permanents d’exploitation** : L’article 150-0 B ter exige que le réinvestissement finance des **moyens permanents** (ex. : outils de production, fonds de commerce, brevets, etc.). Or, une activité de marchand de biens repose principalement sur des **actifs circulants** (les immeubles achetés pour être revendus), ce qui pourrait être considéré comme insuffisant pour caractériser des "moyens permanents".

**→ La doctrine administrative (BOI-RPPM-PVBMC-30-20-20) précise que les activités de négoce immobilier *peuvent* être éligibles, mais sous réserve que le réinvestissement soit affecté à des éléments durables (ex. : acquisition d’un fonds de commerce de marchand de biens, développement d’une marque, outils informatiques spécifiques, etc.).**

#### **c) Recommandations pour sécuriser le réinvestissement**
Pour **maximiser les chances de maintien du report**, je vous conseille de :
1. **Structurer le réinvestissement** de manière à ce qu’il finance des **moyens permanents** clairement identifiables, par exemple :
   - Acquisition d’un **fonds de commerce** de marchand de biens (si la société cible en possède un) ;
   - Investissement dans des **outils informatiques ou logiciels** dédiés à la gestion des projets de rénovation ;
   - Financement de **brevets ou procédés** liés à la rénovation (ex. : techniques innovantes) ;
   - Prise de participation dans une société **complémentaire** (ex. : société de construction ou d’architecture) pour ancrer l’activité dans une chaîne de valeur plus large.
2. **Éviter un réinvestissement direct dans des immeubles** (actifs circulants), sauf si ceux-ci sont **indissociables d’un fonds de commerce** (ex. : immeuble abritant un showroom ou des bureaux dédiés à l’activité).
3. **Documenter l’affectation des fonds** : Conserver une **traçabilité stricte** des flux financiers pour prouver que les 60 % du produit de cession ont bien été réinvestis dans des moyens permanents.
4. **Prendre un engagement formel** dans l’acte de cession ou dans une délibération de la holding, précisant :
   - Le montant réinvesti (au moins 5 400 000 €) ;
   - La nature des moyens permanents financés ;
   - Le respect du délai de 2 ans.

---

### **4. Alternatives en cas de risque de rejet par l’administration**
Si l’administration fiscale conteste l’éligibilité de l’activité de marchand de biens, deux options s’offrent à vous :
#### **a) Contester le redressement**
- **Argumentaire** : L’activité de marchand de biens est une activité commerciale au sens de l’article 34 du CGI, et le réinvestissement dans des moyens permanents (ex. : fonds de commerce) répond aux exigences du texte.
- **Risque** : Contentieux long et incertain (jurisprudence peu abondante sur ce point précis).

#### **b) Opter pour un réinvestissement dans une activité incontestablement éligible**
Exemples d’activités **sans risque** :
- Acquisition d’une **société industrielle ou artisanale** (ex. : entreprise de construction, menuiserie, etc.) ;
- Investissement dans une **activité libérale** (ex. : cabinet d’architecture, bureau d’études) ;
- Prise de participation dans une **société financière** (ex. : fonds d’investissement dédié à l’immobilier professionnel).

---

### **5. Calendrier et prochaines étapes**
1. **Avant le 10 novembre 2027** : Réinvestir au moins **5 400 000 €** dans des moyens permanents éligibles.
2. **Dès maintenant** :
   - **Identifier précisément** les actifs ou sociétés cibles pour le réinvestissement (en privilégiant les moyens permanents) ;
   - **Rédiger un engagement formel** de la holding (à annexer aux comptes ou à un acte juridique) ;
   - **Consulter un expert-comptable** pour valider la traçabilité des flux et la qualification des actifs réinvestis.
3. **En cas de contrôle fiscal** : Être prêt à justifier le caractère permanent des moyens financés.

---

### **6. Conclusion et recommandation**
Votre projet de réinvestissement dans une activité de **marchand de biens** est **a priori éligible** au maintien du report d’imposition, **sous réserve** :
- Que le réinvestissement finance des **moyens permanents d’exploitation** (et non des actifs circulants comme des immeubles) ;
- Que l’engagement de réinvestissement soit **formalisé et documenté** ;
- Que l’activité de la société cible soit **clairement commerciale** (et non assimilable à de la gestion de patrimoine).

**Recommandation** :
- **Privilégiez un réinvestissement dans des actifs durables** (fonds de commerce, outils spécifiques) plutôt que dans des immeubles.
- **Envisagez une diversification partielle** vers une activité incontestablement éligible (ex. : 30 % dans une société de construction) pour limiter les risques.
- **Consultez-moi avant toute décision finale** pour valider la structure du réinvestissement et les documents à produire.

Je reste à votre disposition pour approfondir ces points ou vous assister dans la mise en œuvre opérationnelle. Dans l’attente de votre retour, je vous prie d’agréer, Cher Monsieur, l’expression de mes salutations distinguées.

**Maître [Votre Nom]**
[Signature]

---
**Annexes** :
- Extrait du BOI-RPPM-PVBMC-30-20-20 (doctrine administrative) ;
- Modèle d’engagement de réinvestissement ;
- Liste des activités éligibles/non éligibles.

---

## S34

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

**Objet : Analyse fiscale de la distribution de dividendes à une société mère luxembourgeoise – Application de la retenue à la source**

**Réf. : Votre consultation du [date] – Distribution prévue le 15/06/2025**

Madame, Monsieur,

Nous vous remercions de nous avoir consultés sur les conséquences fiscales de la distribution de **20 000 000 €** à votre société mère luxembourgeoise. Nous analysons ci-dessous l’application de la **retenue à la source (RAS)** sur les dividendes, conformément à l’**article 119 bis, 2 du CGI** et aux dispositions conventionnelles applicables.

---

### **1. Cadre juridique applicable**
#### **a) Règle interne française (CGI, art. 119 bis, 2)**
L’article 119 bis, 2 du CGI prévoit une **retenue à la source de 30 %** (taux de droit commun, art. 187 du CGI) sur les dividendes distribués à des bénéficiaires **non résidents fiscaux en France**, sauf exceptions.

#### **b) Convention fiscale franco-luxembourgeoise (modifiée par l’avenant du 05/09/2014)**
La **convention du 20/03/2018** (entrée en vigueur le 01/01/2020) prévoit :
- **Article 10 (Dividendes)** :
  - **Taux réduit à 5 %** si le bénéficiaire est une société qui détient **au moins 10 % du capital** de la société distributrice (ce qui est votre cas, détention à 100 %).
  - **Taux de 15 %** dans les autres cas.
  - **Exonération totale** si les conditions de la **directive mère-fille (2011/96/UE)** sont remplies (voir point 2 ci-dessous).

---

### **2. Application de la directive mère-fille (2011/96/UE)**
La directive européenne **exonère de RAS** les dividendes distribués entre sociétés mères et filiales de l’UE, sous réserve des conditions suivantes :
- **Détention minimale** : La société mère doit détenir **au moins 10 % du capital** de la filiale **pendant au moins 2 ans** (votre cas : détention à 100 % depuis 5 ans).
- **Forme juridique** : Les deux sociétés doivent être soumises à l’**IS** (votre société mère luxembourgeoise est une SA soumise à l’IS luxembourgeois).
- **Résidence fiscale** : La société mère doit être résidente d’un **État membre de l’UE** (Luxembourg) et **non considérée comme résidente d’un État tiers** au sens de la convention fiscale.

**→ Votre situation remplit ces conditions** : la distribution devrait **bénéficier de l’exonération totale de RAS** en application de la directive mère-fille.

---

### **3. Formalités à respecter**
Pour bénéficier de l’exonération, votre société doit :
1. **Justifier de la résidence fiscale luxembourgeoise** de la société mère via un **certificat de résidence fiscale** délivré par l’administration luxembourgeoise (à obtenir avant la distribution).
2. **Déclarer la distribution** sur le **formulaire n°2777-D** (déclaration de RAS) en cochant la case "Exonération – Directive mère-fille".
3. **Conserver les preuves** de la détention du capital (statuts, pacte d’actionnaires, etc.) et de la durée de détention (2 ans minimum).

---

### **4. Risque de requalification en abus de droit (article L. 64 du LPF)**
L’administration fiscale française pourrait contester l’exonération si elle estime que la structure a été mise en place **uniquement pour éluder l’impôt** (ex. : montage artificiel). Dans votre cas, la détention depuis 5 ans et l’activité réelle de la société mère luxembourgeoise limitent ce risque.

---

### **5. Conclusion et recommandations**
- **Aucune retenue à la source ne devrait être due** sur les 20 000 000 €, sous réserve du respect des formalités (certificat de résidence, déclaration 2777-D).
- **Taux de repli** : Si l’exonération était refusée, le taux conventionnel de **5 %** s’appliquerait (soit 1 000 000 € de RAS).
- **Recommandation** :
  - Obtenir **dès que possible** le certificat de résidence fiscale luxembourgeoise.
  - Vérifier que la société mère luxembourgeoise n’est pas considérée comme "transparente" fiscalement (ex. : société de personnes).
  - Consulter un conseil luxembourgeois pour optimiser la fiscalité locale des dividendes reçus.

Nous restons à votre disposition pour :
- Vous assister dans les démarches déclaratives (formulaire 2777-D).
- Analyser d’éventuelles optimisations complémentaires (ex. : rachat d’actions, réduction de capital).
- Vous représenter en cas de contrôle fiscal.

**Prochaine étape** : Nous vous proposons un entretien téléphonique pour finaliser les documents nécessaires avant le 15/06/2025.

Veuillez agréer, Madame, Monsieur, l’expression de nos salutations distinguées.

**[Votre nom]**
Avocat fiscaliste
[Cabinet]
[Coordonnées]

---
**Annexes** :
- Extrait de la convention franco-luxembourgeoise (art. 10).
- Modèle de demande de certificat de résidence fiscale (Luxembourg).
- Formulaire 2777-D (à compléter).

---

## S35

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 novembre 2024.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

**Objet : Analyse fiscale de la distribution de dividendes à une société mère luxembourgeoise – Application de la retenue à la source**

**Réf. : Votre consultation du [date] – Distribution prévue le 15/11/2024**

Madame, Monsieur,

Nous vous remercions de nous avoir consultés sur les conséquences fiscales de la distribution de **20 000 000 €** à votre société mère luxembourgeoise. Nous analysons ci-dessous l’application de la **retenue à la source (RAS)** sur les dividendes, conformément à l’**article 119 bis, 2 du CGI** et aux dispositions conventionnelles applicables.

---

### **1. Cadre juridique applicable**
#### **a) Règle interne française (CGI, art. 119 bis, 2)**
L’article 119 bis, 2 du CGI prévoit qu’une **retenue à la source de 30 %** (taux de droit commun, art. 187 du CGI) s’applique aux dividendes versés à des bénéficiaires **non résidents fiscaux en France**, sauf exceptions.

#### **b) Convention fiscale franco-luxembourgeoise (modifiée par l’avenant du 5 septembre 2014)**
La **convention du 1er avril 1958** (modifiée) entre la France et le Luxembourg prévoit :
- **Article 10 (Dividendes)** :
  - **Taux réduit à 5 %** si le bénéficiaire est une société qui détient **au moins 10 % du capital** de la société distributrice (ce qui est votre cas, détention à 100 %).
  - **Taux de 15 %** dans les autres cas.
  - **Exonération totale** si la société mère luxembourgeoise est **soumise à l’IS luxembourgeois** (ce qui est votre cas) et remplit les conditions de la **directive mère-fille** (voir ci-dessous).

---

### **2. Application de la directive mère-fille (2011/96/UE)**
La **directive européenne mère-fille** (transposée en droit français à l’**article 119 ter du CGI**) prévoit une **exonération de retenue à la source** sur les dividendes versés entre sociétés mères et filiales de l’UE, sous réserve des conditions suivantes :
- **Détention minimale de 10 %** du capital de la filiale (votre cas : 100 %).
- **Durée minimale de détention de 2 ans** (votre cas : 5 ans).
- **Société mère soumise à l’IS** dans son État de résidence (votre cas : IS luxembourgeois).
- **Forme juridique éligible** (SA, SARL, etc. – votre société mère luxembourgeoise est une SA).

**→ La directive mère-fille s’applique donc à votre situation, ce qui conduit à une exonération totale de RAS.**

---

### **3. Vérification des conditions anti-abus**
La France a transposé la **clause anti-abus de la directive ATAD** (article 119 ter, 3 du CGI), qui peut écarter l’exonération si :
- La société mère luxembourgeoise est **un montage artificiel** (ex. : holding purement passive sans substance économique).
- La distribution a pour **principal objectif l’évasion fiscale**.

**→ À vérifier** :
- La société mère luxembourgeoise a-t-elle une **substance économique** (bureaux, employés, activité réelle) ?
- La distribution s’inscrit-elle dans une **stratégie économique légitime** (ex. : réinvestissement, remboursement de dette) ?

Si ces conditions sont remplies, l’exonération reste applicable.

---

### **4. Formalités déclaratives**
Même en cas d’exonération, des **obligations déclaratives** subsistent :
- **Formulaire n°2777-D** (déclaration de RAS) à déposer au service des impôts des entreprises (SIE) compétent **avant le 15 décembre 2024** (pour une distribution le 15/11/2024).
- **Mention de l’exonération** (case "Directive mère-fille" ou "Convention fiscale").
- **Justificatifs** à conserver (attestation de résidence fiscale luxembourgeoise, preuve de détention du capital depuis 2 ans).

---

### **5. Conclusion et recommandations**
#### **a) Pas de retenue à la source due**
Sous réserve des vérifications ci-dessus (substance économique, absence d’abus), **aucune RAS ne s’applique** en vertu :
1. De la **directive mère-fille** (exonération totale).
2. À défaut, de la **convention fiscale franco-luxembourgeoise** (taux réduit à 5 %, mais non applicable ici).

#### **b) Recommandations**
1. **Vérifier la substance économique** de la société mère luxembourgeoise (pour sécuriser l’exonération).
2. **Conserver les justificatifs** (attestation de résidence, preuve de détention).
3. **Déclarer la distribution** via le formulaire 2777-D (même en cas d’exonération).
4. **Anticiper un éventuel contrôle fiscal** (la France applique strictement les clauses anti-abus).

#### **c) Risque résiduel**
Si l’administration fiscale française estime que la société mère luxembourgeoise est un **montage artificiel**, elle pourrait :
- **Remettre en cause l’exonération** et appliquer une RAS de **30 %** (taux de droit commun).
- **Engager un contentieux** (avec pénalités et intérêts de retard).

**→ Nous vous recommandons de nous transmettre :**
- Les **statuts** de la société mère luxembourgeoise.
- Une **attestation de résidence fiscale** récente.
- Des **éléments prouvant sa substance économique** (contrats, effectifs, locaux).

---

### **6. Proposition d’accompagnement**
Nous pouvons vous assister pour :
1. **Rédiger une note de synthèse** justifiant l’exonération (à joindre au dossier fiscal).
2. **Préparer la déclaration 2777-D**.
3. **Auditer la substance économique** de la société mère luxembourgeoise.
4. **Négocier avec l’administration fiscale** en cas de contrôle.

N’hésitez pas à nous indiquer si vous souhaitez que nous approfondissions l’un de ces points.

**Restant à votre disposition pour toute précision,**
[Votre nom]
Avocat fiscaliste
[Cabinet]
[Coordonnées]

---
**Annexes :**
- Extrait de la convention franco-luxembourgeoise (art. 10).
- Directive mère-fille (2011/96/UE).
- Formulaire 2777-D (modèle).

---

## S36

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un client vous consulte avant de signer.

Il cede les titres d'une societe civile immobiliere dont l'actif est
constitue a 80 % d'immeubles situes en France. Prix de cession :
4 000 000 euros. L'acte sera signe le 20 septembre 2023.

Quel droit d'enregistrement est du, et que doit contenir l'acte ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

# Note au dossier – Cession de parts sociales de SCI – Droits d'enregistrement

**Faits** : cession de titres d'une SCI, actif composé à 80 % d'immeubles situés en France, prix 4 000 000 €, signature le 20 septembre 2023.

---

## 1. Qualification : société à prépondérance immobilière

La SCI remplit les conditions de l'article 726, I, 2° du CGI :

- ses droits sociaux ne sont pas admis aux négociations sur un marché réglementé ou un SMN (caractéristique inhérente à toute SCI) ;
- son actif est **principalement** constitué d'immeubles situés en France : le seuil de 50 % est largement franchi (80 %) ;
- elle n'entre dans aucune des exclusions (HLM, foncières de l'art. 199 terdecies-0 AB, SEM de logement social).

**Point de vigilance** : la prépondérance immobilière s'apprécie au jour de la cession **mais aussi au cours de l'année la précédant** (« dont l'actif est, *ou a été*, principalement constitué… »). Il faut donc vérifier la composition de l'actif sur les douze derniers mois, et non seulement à la date de signature. Il en va de même en transparence si la SCI détient des participations dans d'autres sociétés elles-mêmes à prépondérance immobilière.

## 2. Droit dû

| Élément | Montant / règle |
|---|---|
| Taux (art. 726, I, 2°) | **5 %** |
| Assiette | Prix stipulé : 4 000 000 € (majoré, le cas échéant, des charges et indemnités) |
| Abattement | **Aucun** (l'abattement proportionnel de 23 000 € est réservé aux cessions taxées à 3 %, soit les sociétés non à prépondérance immobilière) |
| **Droit exigible** | **4 000 000 × 5 % = 200 000 €** |

L'administration peut en outre rectifier une **insuffisance de prix** (imposition sur la valeur vénale réelle si celle-ci est supérieure au prix apparent ou dissimulé).

## 3. Redevable, formalité, délais

- **Redevable légal** : l'acquéreur. Toute clause mettant la charge à la charge du cédant n'est opposable qu'entre les parties.
- **Formalité** : l'acte doit être enregistré **dans le délai d'un mois de sa date** (art. 635 CGI), soit au plus tard le **20 octobre 2023**, au service des impôts – enregistrement dont dépend le **siège social de la SCI** (art. 647 CGI).
- **Exigibilité** : le droit est payé lors de l'enregistrement (art. 1717 CGI).
- Défaut ou retard d'enregistrement : rappel du droit, **intérêt de retard (0,20 % par mois)** et amendes fiscales.

## 4. Forme et contenu de l'acte

**Forme.** Signé en France, l'acte **sous seing privé suffit** (acte notarié non requis pour des parts sociales). En revanche, si la cession était réalisée à l'étranger, elle devrait impérativement être constatée **dans le délai d'un mois par acte authentique reçu par un notaire exerçant en France** (art. 726, I, 2°, in fine).

**Mentions à insérer** (nécessaires à l'enregistrement et à la liquidation du droit) :

- identité et domicile complets du cédant et du cessionnaire ;
- désignation de la SCI : dénomination, forme, siège, capital, numéro RCS ;
- nombre et catégorie des parts cédées ;
- **prix de cession stipulé en toutes lettres** et modalités de paiement (décomposition des charges ou soultes éventuelles) ;
- une **clause relative à la prépondérance immobilière**, constatant que l'actif de la société est composé à 80 % d'immeubles situés en France, au jour de la cession et sur l'année écoulée — mention justifiant l'application du tarif de 5 % et évitant toute discussion avec le service ;
- date et lieu de signature ; signatures des parties, en autant d'originaux que nécessaire (un original restera conservé par le service de l'enregistrement).

## 5. Synthèse

La cession supporte un droit d'enregistrement de **200 000 €**, payable par l'acquéreur lors de l'enregistrement de l'acte, à accomplir au plus tard le **20 octobre 2023** auprès du SIE du siège social de la SCI. L'acte sous seing privé est licite, mais doit stipuler expressément le prix et constater la prépondérance immobilière. Je recommande de sécuriser, avant signature, la composition de l'actif sur les douze mois précédents et l'absence de minoration du prix.

---

## S37

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un client vous consulte avant de signer.

Il cede les titres d'une societe civile immobiliere dont l'actif est
constitue a 80 % d'immeubles situes en France. Prix de cession :
4 000 000 euros. L'acte sera signe le 20 septembre 2023.

Quel droit d'enregistrement est du, et que doit contenir l'acte ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

**Objet : Analyse fiscale de la cession de titres d’une SCI à prépondérance immobilière – Droits d’enregistrement applicables**

**À l’attention de [Nom du client],**
**De la part de [Votre nom], Avocat fiscaliste au Barreau de [Ville]**

---

### **1. Contexte et qualification juridique**
Vous envisagez de céder les titres d’une **Société Civile Immobilière (SCI)** dont l’actif est constitué à **80 % d’immeubles situés en France**. Le prix de cession est fixé à **4 000 000 €**, et l’acte sera signé le **20 septembre 2023**.

Au regard de l’**article 726, I, 2° du CGI**, la SCI est qualifiée de **personne morale à prépondérance immobilière** (PMI) car :
- Ses droits sociaux **ne sont pas négociés sur un marché réglementé** (hypothèse confirmée pour une SCI classique).
- Son actif est **principalement constitué d’immeubles situés en France** (80 % > 50 %, seuil implicite de "principalement").

**Conséquence** : La cession est soumise au **droit d’enregistrement de 5 %** (et non au droit commun de 0,1 % pour les cessions de titres de sociétés non immobilières).

---

### **2. Calcul du droit d’enregistrement**
- **Assiette** : Prix de cession = **4 000 000 €**.
- **Taux** : **5 %** (art. 726, I, 2° CGI).
- **Montant du droit** : **4 000 000 € × 5 % = 200 000 €**.

**À noter** :
- Si la cession est réalisée **à l’étranger**, elle doit être **constatée dans un acte authentique reçu par un notaire français dans le mois** (art. 726, I, 2° in fine). Dans votre cas, l’acte sera signé en France, cette formalité n’est pas requise.
- **Exonérations** : Aucune ne s’applique ici (les exceptions visent les organismes HLM, sociétés foncières spécifiques, etc., non concernés).

---

### **3. Contenu obligatoire de l’acte de cession**
Pour être valable et opposable à l’administration fiscale, l’acte doit **au minimum** contenir :
1. **Identification des parties** :
   - Cédant (vous) et cessionnaire (nom, adresse, numéro SIRET si personne morale).
   - **Capacité juridique** (pour les personnes morales : extrait Kbis, pouvoir du signataire).

2. **Objet de la cession** :
   - **Dénomination sociale et SIRET de la SCI**.
   - **Nombre et nature des titres cédés** (parts sociales, actions, etc.).
   - **Prix de cession** (4 000 000 €) et **modalités de paiement** (comptant, échéancier, etc.).
   - **Clause de garantie d’éviction** (obligatoire pour les cessions de titres).

3. **Qualification fiscale** :
   - **Mention explicite** que la SCI est une **PMI** au sens de l’article 726 CGI (pour justifier le taux de 5 %).
   - **Déclaration sur l’honneur** (ou attestation notariée) confirmant que l’actif de la SCI est bien constitué à 80 % d’immeubles en France.

4. **Formalités légales** :
   - **Date et lieu de signature** (20/09/2023).
   - **Signature devant notaire** (recommandé pour sécuriser l’acte, bien que non obligatoire pour les cessions entre particuliers en France).
   - **Enregistrement** : L’acte doit être **enregistré au service des impôts** dans le **délai d’un mois** (art. 635 CGI). Le notaire s’en charge généralement.

5. **Clauses suspensives (si applicable)** :
   - Exemple : autorisation préalable des associés (si prévue dans les statuts de la SCI).

---

### **4. Recommandations pratiques**
- **Vérifier les statuts de la SCI** : Certains statuts imposent des **droits de préemption** ou des **agréments** pour les cessions de parts.
- **Audit fiscal préalable** :
  - Confirmer que la SCI n’a pas **changé de structure** dans l’année précédant la cession (pour éviter un requalification en PMI rétroactive).
  - Vérifier l’absence de **dettes fiscales latentes** (ex : plus-values non déclarées sur des ventes antérieures d’immeubles).
- **Optimisation fiscale** :
  - Si le cessionnaire est un **membre de votre famille**, explorez les **abattements** (ex : abattement de 100 000 € par parent et par enfant pour les donations, mais inapplicable ici en cas de vente).
  - En cas de **cession partielle**, le taux de 5 % s’applique proportionnellement.

---

### **5. Coût global estimé**
| Poste | Montant |
|--------|---------|
| **Droit d’enregistrement (5 %)** | 200 000 € |
| **Frais de notaire** (si acte authentique) | ~1 % à 2 % du prix (40 000 € à 80 000 €) |
| **Frais d’enregistrement** (timbre fiscal) | ~0,1 % (4 000 €) |
| **Total estimé** | **244 000 € à 284 000 €** |

---

### **6. Prochaines étapes**
1. **Transmettre les documents suivants** pour finaliser l’analyse :
   - Statuts de la SCI.
   - Dernier bilan comptable (pour confirmer la répartition de l’actif).
   - Projet d’acte de cession (si déjà rédigé).
2. **Prévoir un rendez-vous avec un notaire** pour :
   - Rédiger l’acte définitif.
   - Organiser l’enregistrement et le paiement des droits.

---

**Conclusion** :
La cession est soumise à un **droit d’enregistrement de 200 000 € (5 %)**. L’acte doit impérativement mentionner la qualification de PMI et être enregistré dans le mois. Je reste à votre disposition pour affiner cette analyse ou vous accompagner dans les formalités.

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées du cabinet]

---
*P.S. : Ce conseil est donné sous réserve de l’examen complet de votre dossier et des évolutions législatives postérieures à la date de cette note.*

---

## S38

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 novembre 2024.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

**NOTE DE CONSEIL FISCAL**
**Objet :** Distribution de dividendes de 20 000 000 € à une société mère luxembourgeoise – Application de la retenue à la source
**Date de mise en paiement prévue :** 15 novembre 2024
**Destinataire :** Direction juridique / Direction financière de la société française

---

### 🔹 CONCLUSION SYNTHÉTIQUE
**Aucune retenue à la source ne sera due** sur la distribution projetée, sous réserve du respect cumulatif des conditions de la directive européenne « mère-fille » et de l'accomplissement des formalités déclaratives prévues par le Code général des impôts (CGI). Le texte que vous citez (CGI, art. 119 bis, 2, 1er al.) pose le principe de la retenue à la source ; son exonération résulte des dispositions subséquentes du même article, transposant la directive 2011/96/UE.

---

### I. CADRE JURIDIQUE APPLICABLE
1. **Principe de retenue à la source** : CGI, art. 119 bis, 2, 1er al. et art. 187 → taux de droit commun de **30 %** pour les bénéficiaires non-résidents.
2. **Exonération européenne** : CGI, art. 119 bis, 2, 2° → transposition de la directive 2011/96/UE (modifiée) prévoyant l'exonération de retenue à la source sur les dividendes versés à une société mère établie dans un État membre de l'UE, sous conditions.
3. **Convention fiscale franco-luxembourgeoise** : Art. 10 → prévoit également une exonération (ou un taux réduit) lorsque la société mère détient au moins 10 % du capital. La directive prime en pratique et offre un régime plus direct.
4. **Clause anti-abus** : CGI, art. 119 bis, 2, 3° et directive 2011/96/UE, art. 1er, §2 → l'exonération est refusée si le montage est artificiel ou a pour objet principal d'obtenir un avantage fiscal indu.

---

### II. ANALYSE DES CONDITIONS D'EXONÉRATION
| Condition | Situation de votre dossier | Conformité |
|-----------|----------------------------|------------|
| **Forme juridique** | Société anonyme (SA) luxembourgeoise | ✅ Liste annexe directive |
| **Résidence fiscale** | Luxembourg (État membre UE) | ✅ |
| **Détention du capital** | 100 % | ✅ (seuil ≥ 10 %) |
| **Durée de détention** | 5 ans | ✅ (seuil ≥ 2 ans) |
| **Assujettissement à l'IS** | Soumise à l'impôt sur les sociétés luxembourgeois, sans exonération | ✅ |
| **Réalité économique / Substance** | À vérifier (siège effectif, gouvernance, activité, personnel) | ⚠️ Point de vigilance |

**Conclusion intermédiaire :** Les conditions matérielles de l'exonération sont remplies. L'administration fiscale française ne pourra remettre en cause l'exonération que si elle établit l'existence d'un montage artificiel ou l'absence de substance économique de la société mère luxembourgeoise.

---

### III. FORMALITÉS ET OBLIGATIONS DÉCLARATIVES
L'exonération s'applique **directement** par la société distributrice, sans autorisation préalable, mais sous réserve de constituer et conserver un dossier justificatif.

1. **Pièces à réunir avant le 15/11/2024 :**
   - Attestation de résidence fiscale luxembourgeoise (valide pour l'année 2024)
   - Attestation sur l'honneur ou déclaration certifiant le respect des conditions de la directive mère-fille (détention ≥ 10 %, durée ≥ 2 ans, assujettissement IS, forme juridique, absence de montage artificiel)
   - Justificatifs de détention (registre des actionnaires, procès-verbaux, extraits Kbis/luxembourgeois)

2. **Déclaration fiscale :**
   - Dépôt du **formulaire n° 5000** (« Déclaration de retenue à la source ») auprès du Service des Impôts des Entreprises (SIE) compétent.
   - Cocher la case relative à l'exonération au titre de la directive mère-fille et joindre les justificatifs.
   - **Délai :** dans les 15 jours suivant la date de mise en paiement (soit au plus tard le 30 novembre 2024).

3. **Conservation :** Archivage du dossier pendant **3 ans** (délai de reprise de l'administration).

---

### IV. POINTS DE VIGILANCE
- **Substance économique :** L'administration française contrôle de plus en plus la réalité des sociétés mères luxembourgeoises (siège de direction effective, personnel qualifié, prise de décision autonome, activité réelle). En cas de « boîte aux lettres », l'exonération peut être remise en cause sur le fondement de l'abus de droit ou de la clause anti-abus.
- **Qualification des flux :** Vérifier que la distribution relève bien du régime des dividendes (bénéfices distribués) et non d'un remboursement de capital ou d'un intérêt déguisé, qui relèveraient d'un régime différent.
- **Évolution législative :** Aucun changement n'est intervenu en 2024 sur ce régime. La position reste stable.

---

### V. RECOMMANDATIONS OPÉRATIONNELLES
1. Solliciter sans délai l'attestation de résidence fiscale 2024 auprès de l'administration luxembourgeoise.
2. Rédiger une attestation interne signée par le dirigeant de la société française certifiant le respect des conditions de la directive.
3. Vérifier la substance de la société mère luxembourgeoise (organigramme, comptes, procès-verbaux de conseil d'administration, localisation des décisions stratégiques).
4. Préparer le formulaire 5000 et le déposer dans les 15 jours suivant le 15/11/2024.
5. Conserver l'ensemble des pièces dans un dossier dédié, accessible en cas de contrôle.

---

### 🔹 CONCLUSION
**Aucune retenue à la source n'est due** sur la distribution de 20 000 000 € prévue le 15 novembre 2024, sous réserve de la constitution du dossier justificatif et du dépôt du formulaire 5000 dans les délais. Le régime de la directive mère-fille s'applique pleinement au cas d'espèce.

Je reste à votre disposition pour :
- Rédiger les attestations et le formulaire 5000,
- Analyser la substance de la société mère luxembourgeoise,
- Vous accompagner en cas de contrôle ou de demande de l'administration.

*Note : Cette note constitue un conseil fiscal personnalisé fondé sur les éléments communiqués et le droit applicable à la date de la distribution. Elle ne saurait se substituer à une analyse complète du dossier en cas de modification des faits ou de la réglementation.*

**[Signature]**  
Avocat au Barreau de [Ville]  
Spécialiste en fiscalité des entreprises & droit international

---

## S39

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un client vous consulte avant de signer.

Il cede les titres d'une societe civile immobiliere dont l'actif est
constitue a 80 % d'immeubles situes en France. Prix de cession :
4 000 000 euros. L'acte sera signe le 20 septembre 2023.

Quel droit d'enregistrement est du, et que doit contenir l'acte ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

**Consultation – Droits d’enregistrement sur cession de titres de SCI à prépondérance immobilière**

La SCI dont les titres sont cédés a un actif constitué à 80 % d’immeubles situés en France. Ses droits sociaux ne sont pas négociés sur un marché réglementé ou un système multilatéral de négociation. Elle constitue donc une personne morale à prépondérance immobilière au sens de l’article 726, I, 2° du CGI.

La cession est en conséquence soumise au droit d’enregistrement au taux de 5 %.  
Sur le prix convenu de 4 000 000 €, le droit s’élève à **200 000 €**.

Si la cession est réalisée à l’étranger, elle doit être constatée dans le délai d’un mois par un acte reçu en la forme authentique par un notaire exerçant en France.

Je reste à votre disposition pour la rédaction ou la relecture de l’acte et le suivi de l’enregistrement.

---

## S40

**Role de l'enonce :** mesure

**Fait manquant :** L'usage que la société mère fait des fonds. Si elle les reverse à un tiers, elle n'en est pas le bénéficiaire effectif.

**Dossier soumis au modele :**

```
Une societe francaise vous consulte.

Elle a cede un actif et degage une tresorerie importante. Elle
souhaite distribuer 20 000 000 euros a sa societe mere
luxembourgeoise, qui detient 100 % de son capital depuis cinq ans,
revet la forme d'une societe anonyme et est soumise a l'impot sur
les societes luxembourgeois.

La distribution serait mise en paiement le 15 juin 2025.

Une retenue a la source est-elle due ?

Voici le texte applicable a la date de la distribution.
```

**Reponse a coder, en entier :**

**OBJET :** Analyse de l’assujettissement à la retenue à la source française sur la distribution de dividendes à une société mère luxembourgeoise – Mise en paiement prévue le 15 juin 2025.

---

### I. CADRE JURIDIQUE APPLICABLE

Le texte que vous citez correspond au premier alinéa de l’article 119 bis, 2 du Code général des impôts (CGI), qui pose le **principe** de la retenue à la source sur les dividendes versés à des bénéficiaires non-résidents. Le taux de droit commun est fixé à **25 %** par l’article 187 du CGI (inchangé à la date du 15 juin 2025).

Toutefois, le **deuxième alinéa (2°)** du même article 119 bis, 2 prévoit une **exonération** de cette retenue à la source lorsque le bénéficiaire effectif est une société :
1. Établie dans un État membre de l’Union européenne ;
2. Soumise à l’impôt sur les sociétés dans cet État, sans option pour l’exonération ;
3. Détenant au moins **5 %** du capital de la société distributrice ;
4. Ayant maintenu cette détention pendant une durée ininterrompue d’au moins **deux ans** ;
5. Revêtant l’une des formes juridiques énumérées à l’annexe de la directive 2011/96/UE (directive « sociétés mères-filiales »).

Ce régime transpose en droit interne la directive européenne et est corroboré par l’**article 10 de la convention fiscale France-Luxembourg**, qui prévoit également une exonération de retenue à la source sous des conditions substantiellement identiques.

---

### II. APPLICATION AU CAS D’ESPÈCE

Au regard des éléments communiqués, les conditions cumulatives d’exonération sont remplies :

| Condition | Situation de votre dossier | Conformité |
|-----------|----------------------------|------------|
| **Établissement dans un État membre de l’UE** | Société mère luxembourgeoise | ✅ |
| **Soumission à l’IS sans option d’exonération** | Soumise à l’impôt sur les sociétés luxembourgeois | ✅ |
| **Seuil de détention ≥ 5 %** | Détention de 100 % | ✅ |
| **Durée de détention ≥ 2 ans** | Détention continue depuis 5 ans | ✅ |
| **Forme juridique éligible** | Société anonyme (SA) – figure à l’annexe I de la directive 2011/96/UE | ✅ |

**Conclusion intermédiaire :** Sous réserve du respect des formalités déclaratives et de l’absence de montage artificiel, **aucune retenue à la source française n’est due** sur la distribution de 20 000 000 € prévue le 15 juin 2025.

---

### III. FORMALITÉS ADMINISTRATIVES ET VIGILANCE

L’exonération n’est pas automatique. Elle est subordonnée au dépôt, par la société distributrice française, des pièces justificatives auprès de l’administration fiscale et au respect de certaines obligations :

1. **Attestation de résidence fiscale** de la société mère luxembourgeoise, délivrée par l’administration fiscale luxembourgeoise, certifiant qu’elle est soumise à l’IS luxembourgeois sans option d’exonération.
2. **Déclaration n° 2561-SD** (ou formulaire 2065/2561 selon le canal de déclaration) à joindre au paiement des dividendes, mentionnant l’identité du bénéficiaire, le montant distribué, et l’engagement de conservation des titres.
3. **Engagement de conservation** : la société mère doit s’engager à conserver au moins 5 % du capital pendant les deux années suivant la distribution. En cas de cession anticipée, la retenue à la source de 25 % devient exigible sur les dividendes déjà versés, avec intérêts de retard.
4. **Clause anti-abus** : l’administration française peut refuser l’exonération si la structure est jugée artificielle ou dépourvue de substance économique réelle (activité effective, moyens humains et matériels, prise de risque, etc.). La détention de 100 % depuis 5 ans et la soumission effective à l’IS luxembourgeois constituent des indices favorables, mais il convient de conserver la documentation justifiant la réalité économique du groupe.

---

### IV. RECOMMANDATIONS OPÉRATIONNELLES

- Faire établir l’attestation de résidence fiscale luxembourgeoise **au moins 6 semaines avant le 15 juin 2025**.
- Préparer et archiver la déclaration 2561-SD, l’engagement de conservation, et les justificatifs de détention (registre des actionnaires, procès-verbaux, etc.).
- Vérifier que la société mère luxembourgeoise n’a pas opté pour un régime d’exonération locale qui la rendrait inéligible au 2° de l’article 119 bis, 2 du CGI.
- Conserver l’ensemble des pièces pendant **6 ans** (délai de reprise de l’administration).

---

### CONCLUSION

**Non, aucune retenue à la source française n’est due** sur la distribution de 20 000 000 € à votre société mère luxembourgeoise, sous réserve du dépôt des justificatifs requis et du respect de l’engagement de conservation des titres. Le régime d’exonération prévu à l’article 119 bis, 2, 2° du CGI, en cohérence avec la directive 2011/96/UE et la convention France-Luxembourg, s’applique pleinement à votre situation.

Je reste à votre disposition pour rédiger les déclarations, vérifier l’attestation de résidence ou accompagner un éventuel contrôle de l’administration sur ce point.

Cordialement,  
**[Votre Nom]**  
Avocat au Barreau de [Ville] – Droit fiscal des affaires & international

