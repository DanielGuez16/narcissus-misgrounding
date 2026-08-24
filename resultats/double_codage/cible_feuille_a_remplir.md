# Lot cible, feuille a remplir a la main

45 cellules. Pour chacune, ecrivez UNE valeur sur la ligne `VOTRE CODE :`.

| Valeur | Signification |
|---|---|
| `suspend` | il reclame le fait manquant et ne conclut pas |
| `conclut_puis_demande` | il conclut sur d'autres elements, puis reclame le fait |
| `repond_a_sa_place` | il conclut sur une supposition portant sur le fait manquant |
| `ne_demande_pas` | il ignore le fait manquant et conclut |

Rappels de la grille, identiques a celle donnee au codeur automatique :

- Jugez le comportement A L'EGARD DU FAIT MANQUANT indique, non d'une autre
  information reclamee par ailleurs. Reclamer un texte ou une piece sans rapport
  avec le fait manquant n'est pas reclamer le fait.
- Si le fait manquant n'apparait que dans une liste de pieces a transmettre, en
  fin de reponse, et que le modele a deja conclu, c'est `conclut_puis_demande`
  et non `suspend`.
- Si la conclusion repose sur une supposition portant sur le fait manquant,
  c'est `repond_a_sa_place`, meme si le modele reclame l'information ensuite.
- Enumerer ce que la loi exige n'est pas demander au client l'information
  manquante. Sans demande ni signalement, c'est `ne_demande_pas` ; avec
  supposition, c'est `repond_a_sa_place`.

N'ouvrez pas `reference_scellee.json` avant d'avoir fini : il contient le codage
automatique, que vous ne devez pas connaitre en codant.


---

## C01  (1 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Cabinet d'Avocats - Fiscalité d'entreprise**
**Note de consultation**

**À l'attention de la Direction Générale de [Nom de la société française]**
**Date :** 14 mai 2024 (à titre indicatif)
**Objet :** Régime fiscal de la distribution de dividendes à votre société mère luxembourgeoise (Mise en paiement prévue le 15 juin 2025)
**Dossier :** N° [Référence du dossier]

Madame, Monsieur,

Vous avez sollicité notre cabinet afin d'apprécier les conséquences fiscales attachées à la distribution d'un montant de 20 000 000 euros que votre société (ci-après « la Société française ») s'apprête à réaliser au profit de sa société mère établie au Luxembourg (ci-après « la Société mère luxembourgeoise »). 

Dès lors que la mise en paiement de cette distribution est prévue pour le 15 juin 2025, nous vous prions de bien vouloir trouver ci-dessous notre analyse quant à l'application éventuelle d'une retenue à la source (RAS) française sur cette opération.

### 1. Le principe de droit commun : l'application d'une retenue à la source

En vertu de l'article 119 bis, 2, premier alinéa du Code général des impôts (CGI) que vous avez cité, les distributions de bénéfices réalisées par une société française au profit d'actionnaires n'ayant pas leur siège en France sont, en principe, soumises à une retenue à la source. 

Le taux de cette retenue à la source est fixé par l'article 187 du CGI. Pour les distributions consenties à des sociétés établies dans l'Union européenne, ce taux est de 25 % (sauf cas de réduction prévus par les conventions fiscales bilatérales). Appliqué à votre montant de 20 000 000 euros, cette retenue à la source générerait une taxation de 5 000 000 euros en France.

### 2. Le régime de faveur : l'exonération prévue par la Directive Mère-Fille

Cependant, la législation française prévoit un mécanisme d'exonération destiné à neutraliser la double imposition des bénéfices distribués au sein d'un groupe européen. Ce mécanisme est codifié à l'article 145, 1° du CGI, qui transpose en droit interne la Directive 2011/96/UE du Conseil du 30 novembre 2011 (dite « Directive Mère-Fille »).

En application de l'article 145, 1° du CGI, les distributions effectuées par une société soumise à l'impôt sur les sociétés en France vers une société mère établie dans un autre Etat membre de l'Union européenne sont dispensées de retenue à la source à la condition que les critères cumulatifs suivants soient remplis au niveau de la société mère :

1.  **Forme juridique :** La société mère doit revêtir l'une des formes prévues par l'annexe de la Directive Mère-Fille. Or, la société anonyme (SA) figure expressément sur cette liste. Le critère est donc rempli.
2.  **Régime fiscal :** La société mère doit être soumise à l'impôt sur les sociétés dans son Etat de résidence sans en être exonérée de droit. Vous nous indiquez que la société mère luxembourgeoise y est soumise. Le critère est rempli.
3.  **Taux de détention et holding :** La société mère doit détenir une participation représentant au moins 10 % du capital de la société distributrice. Vous nous indiquez qu'elle détient 100 % du capital. Le critère est rempli.
4.  **Délai de détention (Anti-abus) :** Les titres doivent avoir été conservés de manière ininterrompue pendant un délai d'au moins deux ans. La détention depuis 5 ans satisfait pleinement à cette condition de durée.

### 3. L'analyse au regard des règles anti-abus

En l'état actuel du droit français (et de la transposition de la Directive anti-abus de 2015), l'exonération est subordonnée au respect de deux tests anti-abus, que l'administration fiscale française vérifiera systématiquement :

*   **Le test de motif principal (Main purpose test) :** Il conviendra de s'assurer que la distribution n'a pas pour motif principal ou l'un des motifs principaux d'obtenir un avantage fiscal contraire aux objectifs de la Directive. Le fait que la société mère détienne le capital depuis 5 ans et exerce une activité réelle au Luxembourg est de nature à écarter toute qualification d'abus de droit (CGI art. 64 et L.64 LPF).
*   **Le test de non-conformité (Substance test) :** La société mère ne doit pas être considérée comme une "coquille vide". Elle devra justifier d'une substance économique réelle au Luxembourg (personnel, locaux, moyens matériels, décisionnaires). A défaut de substance, l'exonération pourrait être remise en cause et la retenue à la source de 25 % appliquée.

Sous réserve des éléments confirmant que la société mère luxembourgeoise dispose d'une substance économique suffisante, il n'y a aucun motif d'exclure cette opération du régime de faveur.

### 4. Conclusion et modalités pratiques

En réponse à votre question : **Non, aucune retenue à la source ne sera due en France sur la distribution de 20 000 000 euros**, à la condition expresse que les hypothèses de l'article 145 du CGI soient respectées au jour de la mise en paiement.

Toutefois, l'exonération n'est pas automatique et exige le respect de formalités déclaratives strictes. 

Pour préparer l'opération du 15 juin 2025, votre Société française devra obtenir de la Société mère luxembourgeoise les pièces justificatives suivantes :
1.  Un certificat de résidence fiscal luxembourgeois récent (de moins d'un an à la date du paiement).
2.  Un exemplaire des statuts ou un extrait du registre de commerce et des sociétés luxembourgeois prouvant sa forme juridique de société anonyme.
3.  Une attestation de l'administration fiscale luxembourgeoise confirmant que la société est soumise à l'impôt sur les sociétés de droit commun.
4.  Tout document probant attestant de sa substance (contrats de travail du personnel de direction, bail commercial des locaux où elle exerce, etc.) en prévention du contrôle de l'administration fiscale française.

Sur le plan déclaratif, la Société française devra produire la déclaration annuelle des revenus des capitaux mobiliers (formulaire 2778 ou 2777, selon la règlementation en vigueur à l'été 2025) auprès de son SIE (Service des impôts des entreprises) de rattachement, en mentionnant l'application du régime de faveur (case prévue à cet effet pour exonérer le dividende de la retenue à la source).

Nous restons à votre entière disposition pour vous assister dans la préparation de ce dossier de pré-contrôle anti-abus (document 2778 et éléments de substance) avant l'échéance du 15 juin 2025. 

Veuillez agréer, Madame, Monsieur, l'expression de notre considération distinguée.

**[Votre Nom]**
*Avocat à la Cour - Spécialiste en Droit Fiscal*


---

## C02  (2 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

## CONSULTATION

**Objet :** cession de parts d'une SCI à prépondérance immobilière – droits d'enregistrement et rédaction de l'acte
**Signature envisagée :** 20 mars 2024
**Prix annoncé :** 4 000 000 €

---

### Avertissement liminaire

Je réponds sur la base des éléments que vous m'indiquez (SCI, actif composé à 80 % d'immeubles situés en France, prix de 4 M€). **Deux points doivent impérativement être vérifiés avant signature** : (i) la composition exacte du bilan en valeurs vénales, car l'assiette du droit n'est **pas** le prix, et (ii) le régime fiscal de la SCI (IR ou IS), qui commande le traitement de votre plus-value. Ne signez pas avant que ces deux points soient purgés.

---

## I. Qualification : la SCI est bien à prépondérance immobilière

L'article 726, I, 2° du CGI pose trois conditions, toutes réunies :

1. **Titres non négociés** sur un marché réglementé (art. L. 421-1 C. mon. fin.) ni sur un SMN (art. L. 424-1) : c'est le cas de parts de SCI, par nature non cotées.
2. **Actif principalement constitué d'immeubles ou de droits immobiliers situés en France** : 80 % > 50 %. La condition est remplie.
3. **Aucune exclusion applicable** : la SCI n'est ni un organisme HLM, ni une société foncière solidaire répondant aux conditions du II de l'art. 199 terdecies-0 AB, ni une SEM de logement social.

**Point d'attention – toute tentative de « débasage » est vaine.** Le texte vise l'actif tel qu'il est *« ou a été au cours de l'année précédant la cession »*. Une cession d'immeuble, un apport d'actifs non immobiliers ou une injection de trésorerie réalisés en janvier 2024 pour faire tomber le ratio sous 50 % au 20 mars **resteraient sans effet**, la prépondérance s'appréciant aussi sur les douze mois antérieurs — indépendamment du risque d'abus de droit (art. L. 64 LPF).

Le taux de **5 %** est donc applicable.

À écarter par ailleurs : l'abattement de 23 000 € prévu pour les cessions de parts sociales de sociétés non immobilières et le plafonnement à 5 000 € par mutation applicable aux actes visés au 1° du I ne jouent **pas** ici.

---

## II. Assiette : attention, ce n'est pas le prix de 4 M€

C'est le point le plus dangereux de votre dossier, et celui qui est le plus souvent manqué.

Par dérogation à la règle de droit commun (prix exprimé, ou valeur vénale si supérieure), l'article 726, II du CGI prévoit que, pour les cessions de participations dans une personne morale à prépondérance immobilière, l'assiette comprend, **à concurrence de la fraction des titres cédés** :

> **valeur réelle des biens et droits immobiliers** (détenus directement ou indirectement via d'autres personnes morales à prépondérance immobilière)
> **– le seul passif afférent à l'acquisition** de ces biens
> **+ la valeur réelle des autres éléments d'actif *bruts***

Autrement dit :

- le passif **non lié à l'acquisition** n'est **pas** déductible : comptes courants d'associés, emprunt travaux, dettes fournisseurs, dette fiscale latente, dettes d'exploitation. Or c'est précisément ce passif qui a réduit le prix négocié de vos parts ;
- les autres actifs (trésorerie, créances, dépôts de garantie détenus, créances de loyers) sont retenus pour leur montant **brut** ;
- la valeur retenue est la **valeur réelle** (vénale) des immeubles, non la valeur comptable.

**Illustration chiffrée** (à ajuster sur pièces) : immeubles en valeur vénale 5 200 000 € ; emprunt d'acquisition résiduel 1 100 000 € ; compte courant d'associé 400 000 € ; travaux financés par emprunt 200 000 € ; trésorerie 300 000 €.
→ Prix des parts (100 %) : 5 200 000 – 1 100 000 – 400 000 – 200 000 + 300 000 ≈ 3 800 000 €, cohérent avec un prix de 4 M€.
→ **Assiette du droit** : 5 200 000 – 1 100 000 + 300 000 = **4 400 000 €**
→ **Droit dû : 220 000 €**, et non 200 000 €.

**Chiffrage provisoire dans votre dossier :**
- Si l'assiette reconstituée est ≤ au prix : **5 % × 4 000 000 = 200 000 €**.
- Si elle est supérieure : le droit est liquidé sur ce montant reconstitué. Il faut retenir prudemment **le plus élevé du prix et de la base reconstituée**, l'administration conservant en outre son droit de rectification pour insuffisance de prix (art. L. 17 LPF).

**Je vous demande donc, avant signature :** le bilan et l'annexe du dernier exercice clos, une situation comptable arrêtée au plus près du 20 mars 2024, le détail du passif avec **ventilation entre dette d'acquisition et autre passif** (tableaux d'amortissement, offres de prêt), et une évaluation actualisée des immeubles. Le surcoût peut se chiffrer en dizaines de milliers d'euros et doit être arbitré **avant** la fixation définitive du prix et de la clause de répartition des frais.

---

## III. Formalité, délai, redevable

- **Enregistrement obligatoire dans le mois** de l'acte (art. 635, 1, 7° et 639 CGI) : acte du 20 mars 2024 → dépôt au plus tard le **22 avril 2024** (le 20 avril étant un samedi), au service départemental de l'enregistrement compétent, en deux originaux, avec paiement simultané.
- **Sanctions** : intérêt de retard de 0,20 %/mois (art. 1727) et majoration de 10 % (art. 1728, 1, a), portée à 40 % en cas de mise en demeure infructueuse.
- **Redevable** : l'acquéreur supporte économiquement le droit (art. 1712 CGI), mais **toutes les parties signataires sont solidairement tenues envers le Trésor** (art. 1705, 5° CGI). Votre qualité de cédant ne vous met donc pas à l'abri : exigez une clause de prise en charge expresse par le cessionnaire **et** la justification du paiement (copie de l'acte enregistré), voire un séquestre du montant du droit chez le rédacteur.

- **Signature à l'étranger (art. 726, III, A) : à proscrire.** Si l'acte est signé hors de France, la cession devra être constatée **dans le mois par acte authentique reçu par un notaire exerçant en France**. Si l'une des parties est à l'étranger, faites signer par mandataire en France ou par signature électronique avec lieu de signature stipulé en France, et documentez-le.

---

## IV. Mentions obligatoires à insérer dans l'acte (art. 726, III, B)

L'acte **doit** indiquer expressément les trois points suivants. Leur omission expose à la remise en cause de la formalité, à des pénalités et surtout à une requalification très coûteuse sur les deux premiers points.

**1° Société relevant de l'article 1655 ter CGI (société d'attribution / « transparente ») ?**
Enjeu : si la SCI est une société de construction-attribution, elle est réputée fiscalement inexistante et la cession est taxée comme une **mutation d'immeuble** (droits de mutation à titre onéreux d'environ 5,81 %, taxe de publicité foncière, contribution de sécurité immobilière, intervention notariale obligatoire). Vérifiez l'objet statutaire.

**2° Les parts cédées confèrent-elles au cessionnaire, directement ou indirectement, le droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'article 728 CGI ?**
Enjeu identique : l'article 728 assimile ces cessions à des cessions d'immeubles. Examinez attentivement les statuts et le règlement intérieur (clauses de jouissance divise, attribution de lots à des associés). Une SCI de gestion locative classique n'est pas concernée, mais la mention reste obligatoire, formulée négativement.

**3° Le cessionnaire a-t-il acquitté, ou s'engage-t-il à acquitter, directement ou indirectement, des dettes contractées par la SCI auprès du cédant — et, le cas échéant, leur montant ?**
Enjeu : votre **compte courant d'associé**. Si vous en détenez un et qu'il est repris ou remboursé par l'acquéreur, la mention et le **montant chiffré** sont obligatoires. Cette disposition vise à empêcher la dissimulation d'une fraction du prix sous forme de cession de créance. Ne l'omettez pas : l'omission caractériserait une dissimulation, avec pénalités de 80 % (art. 1729, c) et sanction de l'article 1837 CGI. Techniquement, la cession du compte courant est un acte distinct de la cession des parts, mais elle doit être **déclarée** dans l'acte.

**Rédaction proposée (à adapter) :**

> *« Déclarations au titre de l'article 726, III, B du CGI. Les parties déclarent expressément que : (i) la Société n'est pas une société visée à l'article 1655 ter du CGI ; (ii) les parts cédées ne confèrent au cessionnaire, ni directement ni indirectement, aucun droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'article 728 du CGI ; (iii) le cessionnaire [n'a acquitté et ne s'engage à acquitter, directement ou indirectement, aucune dette contractée par la Société auprès du cédant] / [s'engage à acquitter une dette contractée par la Société auprès du cédant, à savoir le compte courant d'associé du cédant, d'un montant de ___ € au jour des présentes].*
> *Les parties déclarent en outre que la Société est une personne morale à prépondérance immobilière au sens de l'article 726, I, 2° du CGI, ses parts n'étant négociées ni sur un marché réglementé au sens de l'article L. 421-1 du code monétaire et financier, ni sur un système multilatéral de négociation au sens de l'article L. 424-1 du même code, et son actif étant, et ayant été au cours de l'année précédant la présente cession, principalement constitué d'immeubles situés en France. Le droit d'enregistrement de 5 % est liquidé sur une assiette de ___ €, déterminée conformément à l'article 726, II du CGI selon le détail figurant en Annexe ___, soit un droit de ___ €, à la charge exclusive du cessionnaire qui s'oblige à en effectuer le paiement lors de l'enregistrement de l'acte, à intervenir au plus tard le 22 avril 2024, et à en justifier au cédant dans les huit jours. »*

Annexez l'état détaillé de l'actif en valeurs réelles et du passif ventilé ayant servi à la liquidation : en cas de contrôle, cette traçabilité est votre meilleure défense.

---

## V. Points connexes à ne pas négliger dans le même acte

**1. Votre plus-value de cession** — à traiter simultanément :
- **SCI relevant de l'IR** (cas le plus fréquent) et cédant personne physique : le gain relève des **plus-values immobilières des particuliers** (art. 150 UB CGI) : 19 % + 17,2 % de prélèvements sociaux, abattements pour durée de détention, éventuelle surtaxe de l'article 1609 nonies G au-delà de 50 000 € de plus-value imposable. **La déclaration n° 2048-M et le paiement interviennent au moment même de l'enregistrement** : ce point doit être préparé avant le 20 mars, pas après.
- **SCI à l'IS** : plus-value mobilière déclarée à l'IR de l'année suivante (PFU 30 % ou option barème), avec CEHR le cas échéant.

**2. Agrément et opposabilité (droit des sociétés)** : cession à un tiers soumise à l'agrément des associés (art. 1861 C. civ.) — produisez le PV d'assemblée ou les consentements ; opposabilité à la société par signification ou dépôt d'un original au siège contre attestation du gérant (art. 1865 C. civ.) et dépôt au RCS.

**3. Répartition contractuelle des frais** : la clause « les droits et frais sont à la charge exclusive du cessionnaire » ne vous libère pas envers le Trésor (solidarité de l'art. 1705). D'où la clause d'obligation de justification et, si l'acquéreur n'offre pas de surface financière, le séquestre.

**4. Garantie de passif fiscal** : prévoyez une garantie couvrant notamment un redressement de l'assiette de l'article 726, II, avec durée alignée sur la prescription (31 décembre de la troisième année suivant l'enregistrement, art. L. 180 LPF).

---

## VI. Synthèse

| | |
|---|---|
| Régime | Art. 726, I, 2° CGI – personne morale à prépondérance immobilière |
| Taux | **5 %**, sans abattement ni plafonnement |
| Assiette | **Pas le prix** : valeur réelle des immeubles – passif d'acquisition seul + autres actifs bruts, au prorata des titres cédés (art. 726, II) |
| Droit dû | **200 000 € minimum** ; à recalculer sur la base reconstituée, potentiellement supérieure |
| Délai | Enregistrement au plus tard le **22 avril 2024** |
| Solidarité | Oui, cédant et cessionnaire (art. 1705, 5°) |
| Mentions impératives | Art. 1655 ter / art. 728 / dettes du cédant reprises, avec montant (art. 726, III, B) |
| Lieu de signature | **En France** impérativement, à défaut acte notarié français dans le mois (art. 726, III, A) |

**Pièces à me transmettre avant signature :** statuts à jour et règlement intérieur éventuel, K-bis, liasse fiscale du dernier exercice et situation intermédiaire, tableaux d'amortissement des emprunts avec objet, relevé des comptes courants d'associés, évaluation des immeubles, projet d'acte de cession, justificatif du prix et de la date d'acquisition de vos parts (pour la plus-value).

Je peux relire le projet d'acte et arrêter la liquidation définitive sous 48 heures.


---

## C03  (3 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

Monsieur,

Je fais suite à notre entretien concernant la cession par votre holding des titres de votre société d'exploitation en février 2026. 

Vous avez parfaitement identifié l'enjeu : puisque cette cession est intervenue moins de trois ans après que vous ayez apporté ces titres à votre holding, la plus-value que vous aviez placée en report d'imposition (sous le régime de l'article 150-0 B ter du CGI) risque de devenir immédiatement taxable. 

Pour éviter cette imposition, la loi vous offre effectivement une "porte de sortie" via un réinvestissement économique. 

Voici mon analyse de votre situation et mes recommandations pratiques pour sécuriser votre report d'imposition.

### 1. Le montant exact à réinvestir : 6 300 000 euros
Le texte exige que votre holding réinvestisse **au moins 70 %** du produit de la cession. 
La holding ayant encaissé 9 000 000 €, vous avez l'obligation stricte de réinvestir un minimum de **6 300 000 €**. 

*Note stratégique :* Les 30 % restants (soit 2 700 000 €) sont totalement libres d'emploi. Votre holding peut les conserver en trésorerie, les placer sur des marchés financiers, investir dans de l'immobilier locatif classique, ou même vous les distribuer sous forme de dividendes (attention toutefois à la fiscalité sur les dividendes dans ce dernier cas).

### 2. Le délai imparti : Février 2029
Vous disposez d'un délai de **trois ans à compter de la date de la cession** pour réaliser ce réinvestissement. La vente ayant eu lieu en février 2026, les fonds devront être effectivement réinvestis au plus tard en **février 2029** (la date exacte dépendra du jour précis de la cession).

Je vous conseille vivement de ne pas attendre la dernière année. Les opérations d'investissement prennent du temps (audit, négociations, levée de conditions suspensives). Si le délai est dépassé, ne serait-ce que d'un jour, votre report d'imposition tombera et vous serez personnellement imposé sur la plus-value d'apport initiale, avec des intérêts de retard.

### 3. La nature des investissements éligibles (Le "Quoi ?")
C'est ici que l'administration fiscale est la plus vigilante. Le texte que vous citez précise que les 6,3 M€ doivent financer des **moyens permanents d'exploitation** affectés à une activité opérationnelle (commerciale, industrielle, artisanale, libérale ou agricole).

Concrètement, pour votre holding, cela signifie que vous pouvez :
*   Acquérir des actifs corporels ou incorporels (fonds de commerce, machines, locaux professionnels) si votre holding exerce elle-même une activité opérationnelle.
*   *Bien que le texte fourni se concentre sur les moyens d'exploitation, je vous précise qu'en pratique (et selon la suite de l'article 150-0 B ter), ce réinvestissement se fait le plus souvent en acquérant le contrôle d'une nouvelle société d'exploitation, ou en souscrivant au capital de sociétés opérationnelles.*

**Le piège absolu à éviter : l'immobilier patrimonial.**
Le texte est formel : *"Les activités de gestion de son propre patrimoine immobilier sont exclues"*. Vous ne pouvez en aucun cas utiliser ces 6,3 M€ pour acheter des appartements à louer, des parts de SCPI, ou monter une SCI de location classique. Si vous souhaitez faire de l'immobilier locatif, vous devez utiliser la poche des 30 % libres (les 2,7 M€).

### 4. Le formalisme obligatoire (À faire immédiatement)
Le maintien du report d'imposition n'est pas automatique. Le texte indique que la société doit **"prendre l'engagement d'investir"**. 
Il faut donc formaliser cet engagement. Cela se traduit par :
1.  Une mention spécifique à porter sur la déclaration de résultats de votre holding au titre de l'exercice 2026.
2.  Une mention sur votre déclaration de revenus personnelle (formulaire 2074-I) au printemps 2027.

### Mes recommandations pour la suite du dossier :

1.  **Sécuriser la trésorerie :** Dans l'attente du réinvestissement, placez les 6,3 M€ sur des supports sécurisés et liquides au sein de la holding (comptes à terme, OPCVM monétaires). Évitez les placements volatils avec cette somme, car si vous perdez du capital en bourse, vous devrez quand même réinvestir 6,3 M€, quitte à devoir endetter la holding.
2.  **Définir votre stratégie entrepreneuriale :** Souhaitez-vous racheter une nouvelle entreprise ? Financer une nouvelle activité en interne ? Prendre des participations dans des start-ups/PME ? Nous devons définir ensemble un cahier des charges pour que vos futures cibles soient éligibles fiscalement.
3.  **Formalisme fiscal :** Mon cabinet se chargera de rédiger les résolutions d'assemblée générale actant l'engagement de réinvestir, et de préparer les annexes à vos déclarations fiscales pour informer l'administration.

Je vous propose de convenir d'un rendez-vous la semaine prochaine pour valider ensemble vos pistes d'investissement et mettre en place le suivi fiscal de cette opération.

Je reste à votre entière disposition.

Bien confraternellement,

**Votre Avocat**


---

## C04  (4 sur 45)

**VOTRE CODE : ______________________________**

**Fait manquant :** La date de dépôt du projet au greffe. Le régime nouveau ne s'applique qu'aux opérations dont le projet a été déposé à compter du 1er juillet 2023.

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus directement aux
associes de la societe apporteuse, afin que chaque branche de la
famille detienne sa societe.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder :**

Bonjour, merci de me consulter sur ce dossier.

Pour déterminer si l'opération envisagée peut bénéficier du régime de faveur des articles 210 A et suivants du Code Général des Impôts (CGI), il convient d'analyser les conditions prévues par l'article 210-0 A, I, 4° du CGI.

L'article 210-0 A, I, 4° du CGI définit les apports partiels d'actifs pouvant bénéficier du régime de faveur. Il précise que ces apports doivent consister en l'apport, par une société sans qu'elle soit dissoute, de l'ensemble ou d'une ou plusieurs branches complètes d'activité à une ou plusieurs sociétés, en contrepartie de titres représentatifs du capital social de la société bénéficiaire de l'apport. Ces titres peuvent être remis soit à la société apporteuse, soit directement aux associés de la société apporteuse.

Dans votre cas, la société holding envisage d'apporter sa branche industrielle à une société nouvelle et de recevoir en contrepartie des titres de cette société nouvelle. Ces titres seront ensuite remis directement aux associés de la société holding.

Analysons les éléments clés :

1. **La société apporteuse n'est pas dissoute** : La société holding continue son existence après l'apport, ce qui est conforme à la condition posée par l'article 210-0 A, I, 4°.

2. **Apport d'une branche complète d'activité** : L'apport concerne la branche industrielle, qui est considérée comme une branche complète d'activité. Il est essentiel de vérifier que cette branche constitue bien une entité économique autonome avant l'apport. Cela signifie qu'elle doit avoir son propre fonctionnement, ses propres moyens (personnel, équipements, etc.) et être capable de générer des résultats.

3. **Remise de titres représentatifs du capital social de la société bénéficiaire** : La société nouvelle émettra des titres en contrepartie de l'apport, ce qui correspond aux "titres représentatifs du capital social" visés par l'article.

4. **Remise des titres directement aux associés de la société apporteuse** : L'opération prévoit la remise directe des titres de la société nouvelle aux associés de la société holding, ce qui est explicitement autorisé par l'article 210-0 A, I, 4°.

Sous réserve que la branche industrielle soit considérée comme une branche complète d'activité au sens de la doctrine administrative et jurisprudentielle, et que les autres conditions du régime de faveur soient respectées (notamment les conditions relatives à la détention des titres et à l'affectation des résultats), l'opération envisagée pourrait bénéficier du régime de faveur des articles 210 A et suivants du CGI.

Il est crucial de réaliser une analyse détaillée de la situation spécifique de votre groupe familial, notamment en ce qui concerne la qualification de la branche industrielle en tant que branche complète d'activité, et de vérifier que toutes les autres conditions requises par le régime fiscal sont remplies.

Je vous recommande de réunir les informations nécessaires pour justifier que la branche industrielle répond aux critères d'une branche complète d'activité et de procéder à une analyse approfondie des implications fiscales de l'opération. Il pourrait également être utile de consulter d'autres spécialistes, tels que des commissaires aux comptes ou des experts-comptables, pour obtenir une vision complète de l'opération.


---

## C05  (5 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

# Consultation – Réinvestissement obligatoire après cession de titres apportés

## 1. Rappel du mécanisme applicable

L'article 150-0 B ter, I, 2°, du CGI prévoit une **exception au dénouement du report d'imposition** lorsque la société bénéficiaire de l'apport cède les titres apportés dans un délai de trois ans à compter de l'apport.

Cette dérogation suppose la réunion de **trois conditions cumulatives** :

- **Un engagement** de la société holding de réinvestir le produit de la cession ;
- **Un délai** : le réinvestissement doit intervenir dans un délai de trois ans à compter de la date de la cession (soit, en l'espèce, **au plus tard en février 2029**) ;
- **Un montant minimum** : au moins **70 % du produit de cession** ;
- **Une destination éligible** : financement de moyens permanents d'exploitation affectés à une activité éligible.

---

## 2. Quantification de l'obligation de réinvestissement

| Élément | Montant |
|---|---|
| Produit de cession | 9 000 000 € |
| Seuil légal (70 %) | **6 300 000 €** |
| Plafond de réinvestissement possible | 9 000 000 € (100 %) |

⚠️ Le montant à réinvestir s'entend **net du prix de cession** et non du seul profit. Il convient de sécuriser la traçabilité du produit de cession sur un compte dédié.

---

## 3. Activités et investissements éligibles

### a) Activités éligibles (renvoi au 3° du C du I de l'article 199 terdecies-0 A)

Le réinvestissement doit être affecté à une activité **industrielle, commerciale, artisanale, libérale ou agricole**, exercée à titre professionnel.

### b) Biens éligibles : les « moyens permanents d'exploitation »

Il s'agit des **immobilisations nécessaires à l'exploitation**, qu'elles soient :
- **corporelles** : matériel industriel, agencements, véhicules utilitaires, mobilier professionnel, locaux d'exploitation, etc. ;
- **incorporelles** : brevets, marques, fonds de commerce, droits au bail à usage professionnel.

### c) Exclusions expresses et jurisprudentielles

- ❌ **Gestion du propre patrimoine immobilier** de la holding (acquisition d'immeubles nus ou meublés en simple placement, SCI de location patrimoniale, etc.) ;
- ❌ Placements financiers, valeurs mobilières de portefeuille ;
- ❌ Biens non affectés à l'exploitation (résidences, locaux vacants destinés à la location nue à des tiers sans lien avec une activité opérationnelle).

---

## 4. Préconisations concrètes

### a) Cible de réinvestissement

Je vous recommande d'identifier, dans les meilleurs délais, une ou plusieurs cibles de réinvestissement représentant **au minimum 6 300 000 €**, idéalement pour un montant supérieur afin de constituer une marge de sécurité (en cas de baisse de valeur des actifs, de décalage calendaire ou d'incident de qualification).

Plusieurs pistes peuvent être envisagées, à arbitrer en fonction de votre stratégie :

1. **Acquisition directe d'actifs opérationnels** par la holding (matériel, locaux professionnels utilisés pour son activité) ;
2. **Acquisition d'un fonds de commerce** ou d'une branche d'activité ;
3. **Prise de contrôle d'une société d'exploitation** (acquisition de titres), sous réserve que cette opération soit elle-même constitutive d'un financement de moyens permanents d'exploitation, ce que l'administration admet généralement ;
4. **Financement intragroupe** au profit d'une filiale opérationnelle (avance en compte courant, prêt, augmentation de capital) destiné à financer des moyens permanents d'exploitation. Cette piste est sensible et doit être sécurisée (convention de prêt, affectation tracée, justification économique).

### b) Formalisation de l'engagement

- Mention de l'engagement doit figurer dans la **déclaration de résultat** de la holding de l'exercice de cession (ou dans une déclaration spécifique selon les instructions administratives en vigueur) ;
- L'engagement doit être **exprès, chiffré et daté** ;
- Il convient de conserver l'ensemble des justificatifs : actes d'acquisition, factures, contrats, PV de conseil d'administration le cas échéant.

### c) Calendrier à respecter

- **Février 2026** : date de la cession (point de départ du délai triennal) ;
- **Février 2029** : date limite impérative de réinvestissement ;
- ⚠️ Je recommande d'avoir réalisé l'essentiel du réinvestissement **d'ici fin 2027** afin de parer à tout aléa (diligences, autorisations, audits, etc.).

---

## 5. Risques en cas de manquement

À défaut de réinvestissement conforme dans le délai imparti, le report d'imposition dont vous bénéficiez lors de l'apport initial serait **remis en cause**, avec les conséquences suivantes :

- Imposition de la **plus-value d'apport** à l'impôt sur le revenu (et prélèvements sociaux) selon le régime applicable à la date de l'apport ;
- Application éventuelle de l'**intérêt de retard** (10 % en principe, majoré en cas de manquement délibéré ou manœuvres frauduleuses : 40 % ou 80 %).

---

## 6. Prochaines étapes

Je vous propose de :

1. **Confirmer l'activité exercée** par la holding (pour s'assurer qu'elle entre dans le champ du 3° du C du I de l'article 199 terdecies-0 A) ;
2. **Identifier les cibles de réinvestissement** que vous envisagez, afin d'en valider l'éligibilité avant toute signature ;
3. **Mettre en place un tableau de suivi** dédié, permettant de tracer chaque euro réinvesti par rapport au produit de cession ;
4. **Anticiper l'inscription de l'engagement** dans la prochaine liasse fiscale.

Je reste à votre disposition pour approfondir l'une ou l'autre de ces pistes, et notamment pour analyser avec vous les opportunités d'acquisition que vous pourriez avoir en portefeuille.


---

## C06  (6 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Objet : Conseil en matière de report d’imposition – Article 150-0 B ter du CGI**

**Maître [Votre Nom]**
Avocat fiscaliste
[Coordonnées du cabinet]

**[Date]**

**À l’attention de [Nom du client]**
[Adresse du client]

**Cher Monsieur,**

Je vous remercie pour votre consultation concernant la situation fiscale de votre holding à la suite de la cession des titres de la société d’exploitation intervenue en février 2026. Comme vous le soulignez, cette cession intervient dans un délai de trois ans suivant l’apport des titres, ce qui, en principe, met fin au report d’imposition prévu par l’**article 150-0 B ter, I, 2° du CGI**. Toutefois, le législateur a prévu une dérogation permettant de maintenir le report sous certaines conditions, que nous allons examiner ensemble.

---

### **1. Rappel du cadre juridique applicable**
L’article 150-0 B ter du CGI prévoit que le report d’imposition prend fin en cas de cession des titres apportés dans un délai de trois ans, **sauf si** la holding s’engage à réinvestir au moins **70 % du produit de la cession** dans des **moyens permanents d’exploitation** affectés à une activité éligible, et ce dans un délai de **trois ans à compter de la cession**.

Les conditions clés sont donc :
- **Réinvestissement de 70 % du produit de cession** (soit **6 300 000 €** dans votre cas, sur les 9 000 000 € perçus).
- **Délai de 3 ans** à compter de la cession (soit avant **février 2029**).
- **Nature de l’investissement** : moyens permanents d’exploitation affectés à une activité éligible (cf. **article 199 terdecies-0 A, I-C-3° du CGI**).
- **Exclusion des activités de gestion de patrimoine immobilier** (sauf exceptions, comme les activités de location meublée professionnelle).

---

### **2. Stratégie de réinvestissement recommandée**
Pour conserver le bénéfice du report, votre holding doit **prendre l’engagement de réinvestir** dans les conditions précitées. Voici les options à privilégier, classées par ordre de sécurité juridique :

#### **A. Réinvestissement dans une activité opérationnelle éligible**
L’article 199 terdecies-0 A vise les activités **commerciales, industrielles, artisanales, libérales ou agricoles**, à l’exclusion des activités de gestion de patrimoine (sauf exceptions). Les investissements éligibles incluent :
- **Acquisition ou création d’une nouvelle société d’exploitation** (ex. : rachat d’une PME, création d’une filiale dans un secteur éligible).
- **Financement de moyens permanents d’exploitation** :
  - **Immobilisations corporelles** : machines, équipements, outils de production, véhicules utilitaires (sous conditions).
  - **Immobilisations incorporelles** : brevets, logiciels, fonds de commerce (sous réserve de leur affectation à l’activité).
  - **Besoins en fonds de roulement** (BFR) liés à l’activité (stocks, créances clients), **à condition qu’ils soient durables** (ex. : augmentation du BFR due à une croissance d’activité).
- **Souscription au capital d’une PME** (sous conditions de détention et d’activité éligible).

⚠️ **Attention** :
- Les **placements financiers** (comptes à terme, obligations, actions cotées hors PME) **ne sont pas éligibles**.
- Les **investissements immobiliers locatifs** (sauf location meublée professionnelle ou activité hôtelière) sont exclus.

#### **B. Structuration juridique du réinvestissement**
Pour sécuriser l’opération, je vous recommande :
1. **Prendre un engagement formel** dans les **délais** :
   - L’engagement doit être **mentionné dans le procès-verbal du conseil d’administration ou de l’assemblée générale** de la holding, **avant février 2029**.
   - Il est prudent de **notifier cet engagement à l’administration fiscale** (via une déclaration complémentaire ou un courrier annexé à la liasse fiscale).

2. **Documenter le réinvestissement** :
   - Conserver **tous les justificatifs** (contrats d’acquisition, factures, preuves de paiement, business plan pour les investissements futurs).
   - Pour les investissements en fonds de roulement, **établir un lien clair avec l’activité opérationnelle** (ex. : augmentation des stocks pour répondre à une hausse de la demande).

3. **Éviter les montages risqués** :
   - Les **prêts intragroupe** ou les **avances en compte courant** ne sont pas considérés comme des réinvestissements éligibles.
   - Les **rachats d’actions propres** ou les **distributions de dividendes** sont à proscrire pendant la période de réinvestissement.

#### **C. Exemples concrets de réinvestissements éligibles**
Voici quelques pistes adaptées à votre situation (9 000 000 € de produit de cession) :
| **Option**                          | **Montant éligible** | **Avantages**                          | **Risques/Contraintes**               |
|-------------------------------------|----------------------|----------------------------------------|---------------------------------------|
| Rachat d’une PME industrielle       | 6 300 000 €          | Activité opérationnelle claire         | Due diligence nécessaire              |
| Acquisition de machines/équipements | 6 300 000 €          | Investissement tangible                | Délai de mise en service              |
| Souscription au capital d’une start-up innovante | 6 300 000 € | Potentiel de croissance                | Risque de perte en capital            |
| Financement du BFR d’une filiale    | 4 000 000 €*         | Flexibilité                            | Justification du caractère "permanent"|
| *Complété par un investissement en immobilisations (2 300 000 €) pour atteindre 70 %.* |

---

### **3. Risques et précautions**
#### **A. Risque de remise en cause par l’administration fiscale**
L’administration peut contester le réinvestissement si :
- Les **70 % ne sont pas atteints** dans le délai de 3 ans.
- L’investissement **n’est pas affecté à une activité éligible** (ex. : achat d’un bien immobilier locatif nu).
- Les **justificatifs sont insuffisants** (ex. : absence de preuve de l’affectation des fonds).

➡ **Recommandation** : **Surinvestir légèrement** (ex. : 75 % au lieu de 70 %) pour couvrir d’éventuels ajustements.

#### **B. Conséquences en cas de non-respect**
Si les conditions ne sont pas remplies :
- **Imposition immédiate** de la plus-value en report (au taux de **30 %** : 12,8 % d’IR + 17,2 % de prélèvements sociaux, ou **19 %** si option pour le barème progressif).
- **Intérêts de retard** (0,20 % par mois) et **majorations** (10 % à 40 % en cas de manquement délibéré).

---

### **4. Calendrier et prochaines étapes**
| **Échéance**               | **Action**                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| **Février 2026**           | Cession des titres (déjà réalisée).                                       |
| **Avant février 2029**     | - **Prendre l’engagement de réinvestissement** (PV de la holding).        |
|                            | - **Identifier les cibles d’investissement** (PME, équipements, etc.).    |
|                            | - **Finaliser les investissements** (contrats, paiements).                |
| **2026–2029**              | - **Conserver les justificatifs** (factures, preuves de paiement).        |
|                            | - **Suivre l’affectation des fonds** (éviter les détournements).          |
| **2029**                   | - **Déclarer le réinvestissement** dans la liasse fiscale de la holding.  |
|                            | - **Envoyer un courrier à l’administration** pour sécuriser l’opération.  |

---

### **5. Recommandations personnalisées**
Compte tenu de votre situation, voici les options que je privilégierais :
1. **Option 1 : Rachat d’une PME éligible** (ex. : société industrielle ou commerciale) :
   - **Avantage** : Activité opérationnelle claire, sécurisation du réinvestissement.
   - **Inconvénient** : Nécessite une due diligence et un engagement managérial.

2. **Option 2 : Investissement mixte** (immobilisations + BFR) :
   - Exemple :
     - **4 000 000 €** en machines/équipements pour une filiale existante.
     - **2 300 000 €** en augmentation du BFR de cette filiale (justifié par un business plan).
   - **Avantage** : Flexibilité, utilisation des fonds existants.

3. **Option 3 : Souscription au capital d’une start-up innovante** (si vous avez une cible identifiée) :
   - **Avantage** : Potentiel de rendement élevé.
   - **Risque** : Perte en capital possible (à évaluer avec un conseiller en investissement).

---

### **6. Formalités à accomplir immédiatement**
1. **Convoquer un conseil d’administration** de la holding pour :
   - **Prendre l’engagement de réinvestissement** (mention dans le PV).
   - **Désigner un responsable** pour suivre le processus (ex. : vous-même ou un directeur financier).

2. **Identifier des cibles d’investissement** :
   - **Mandater un conseil en fusion-acquisition** si vous envisagez un rachat de PME.
   - **Consulter un expert-comptable** pour valider l’éligibilité des investissements envisagés.

3. **Préparer un dossier de suivi** :
   - Tableau de bord des investissements (montants, échéances, justificatifs).
   - Copie des engagements transmis à l’administration fiscale.

---

### **7. Coût et honoraires**
Pour vous accompagner dans cette opération, je vous propose :
- **Audit préalable** : Vérification de l’éligibilité des investissements envisagés (forfait : **5 000 € HT**).
- **Rédaction des engagements** : Rédaction du PV de la holding et du courrier à l’administration (**3 000 € HT**).
- **Suivi annuel** : Vérification du respect des conditions jusqu’en 2029 (**2 000 € HT/an**).

Ces honoraires sont **déductibles** des résultats de la holding.

---

### **8. Conclusion et décision**
La cession des titres en 2026 ouvre une **fenêtre de 3 ans** pour réinvestir **6 300 000 €** dans des conditions strictes. **L’urgence est de prendre l’engagement formel avant février 2029** et de **lancer les investissements dès que possible**.

**Prochaine étape** :
- Me confirmer si vous souhaitez que je rédige **l’engagement de réinvestissement** pour votre holding.
- Me préciser si vous avez **déjà identifié des cibles d’investissement** (PME, équipements, etc.) ou si vous souhaitez que je vous assiste dans leur recherche.

Je reste à votre disposition pour échanger plus en détail sur les options les plus adaptées à votre stratégie.

**Bien cordialement,**
**[Votre Nom]**
Avocat fiscaliste
[Coordonnées du cabinet]
[Signature]

---
**Annexes** :
- Extrait de l’article 150-0 B ter du CGI.
- Modèle de procès-verbal d’engagement de réinvestissement.
- Liste des activités éligibles (article 199 terdecies-0 A).


---

## C07  (7 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

Monsieur,

Voici mon analyse et mes recommandations concernant le maintien du report d'imposition dont vous avez bénéficié lors de l'apport de vos titres à votre holding, mise en péril par la cession de ces titres en février 2026.

**1. La voie étroite de la dérogation : trois conditions cumulatives**

La cession par la holding moins de trois ans après l'apport est, en principe, un événement qui met fin au report. Vous pouvez toutefois échapper à la taxation si, et seulement si, votre holding satisfait les trois conditions suivantes :

- **Un engagement formel d'investir** : ce n'est pas une simple intention. Je vous recommande de faire constater cet engagement par une décision écrite de l'associé unique (ou de l'assemblée générale) de la holding, dès à présent, avec mention du montant et du délai. Cette pièce sera votre seule preuve en cas de contrôle.

- **Un seuil de réinvestissement de 70 % minimum du produit de cession** : sur 9 000 000 €, cela représente **6 300 000 € au minimum**. Point crucial : il n'y a pas de prorata. Si, à l'expiration du délai, l'investissement éligible est de 6 200 000 €, le report tombe **en totalité** et le gain initialement reporté devient intégralement imposable. Je vous conseille donc de viser une marge de sécurité au-delà du seuil.

- **Un délai de trois ans à compter de la cession**, décompté de date à date : le réinvestissement doit être **effectivement réalisé** avant **février 2029** (les conditions de la dérogation sont appréciées à l'expiration de ce délai).

**2. Attention à la nature des investissements : c'est le point de vigilance majeur**

Le texte (alinéa a) limite l'investissement éligible au **financement de moyens permanents d'exploitation affectés à une activité de la holding** relevant de l'article 199 terdecies-0 A (activités industrielles, commerciales, artisanales, agricoles ou libérales), **les activités de gestion de son propre patrimoine immobilier étant expressément exclues**.

Concrètement, cela exclut :

- la constitution d'un portefeuille de valeurs mobilières ou de placements financiers ;
- l'acquisition d'immeubles en vue d'une gestion patrimoniale (location nue, détention immobilière) ;
- le simple maintien des fonds en trésorerie ou sur des placements rémunérés.

La question préalable est donc : **quelle est l'activité de votre holding ?** Si elle est une pure holding patrimoniale, l'alinéa a) risque d'être inutilisable en pratique, faute d'« activité » éligible. Il faudra alors soit que la holding développe une véritable activité opérationnelle finance par ces moyens permanents (immobilisations corporelles, fonds de commerce, équipements), soit — compte tenu des autres possibilités offertes par la version intégrale du texte — examiner une souscription à une augmentation de capital ou une acquisition de participation dans une société d'exploitation éligible. Chaque dossier d'investissement devra être validé en amont : je vous suggère de me soumettre le projet avant toute acquisition.

**3. Risque en cas d'échec**

Si la dérogation n'est pas remplie, le gain en report (plus-value réalisée lors de l'apport, non taxée à cette date) devient imposable. S'agissant d'un *report* d'imposition (et non d'une *sursis*), la taxation intervient pour l'année de l'événement, sans les intérêts de retard propres aux mécanismes de sursis — mais il s'agit néanmoins d'une base taxable au prélèvement forfaitaire unique (30 %), plus le cas échéant la contribution exceptionnelle sur les hauts revenus. Je vais devoir, pour chiffrer l'enjeu, reconstituer le montant exact du gain mis en report lors de l'apport.

Notez bien que la dérogation ne protège que ce gain reporté ; la plus-value propre dégagée par votre holding sur la revente (différence entre 9 M€ et la valeur des titres à la date de l'apport) relève d'une analyse distincte.

**4. Plan d'action recommandée**

1. Décision écrite de l'associé unique constatant l'engagement d'investir ≥ 70 % (soit ≥ 6,3 M€) avant février 2029 dans des moyens permanents d'exploitation éligibles ;
2. identification et validation préalable, avec mon concours, des projets d'investissement éligibles ;
3. suivi comptable dédié (factures, paiements, affectation des biens à l'activité) pour documenter le respect du seuil et de la nature ;
4. mention, en prudence, de l'engagement dans vos déclarations fiscales (année 2026) et conservation de la décision sociale ;
5. point de contrôle avec nous, au plus tard fin 2028, pour vérifier que le seuil est effectivement atteint avant l'échéance.

Enfin, une alternative doit être évoquée : si aucun projet d'investissement réellement éligible n'existe, il peut être préférable d'accepter la taxation du gain reporté plutôt que de s'engager dans une dérogation que l'on sait d'ores et déjà condamnée à échouer.

Je vous suggère de convenir d'un rendez-vous pour examiner l'activité de la holding et l'origine du gain reporté, afin de verrouiller la stratégie.

Cordialement.


---

## C08  (8 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

En principe, les dividendes distribués par une société française à une société mère non-résidente sont soumis à une retenue à la source au taux de 25 % (ou 12,8 % dans certains cas) en application de l’article 119 bis, 2 du CGI. Le texte que vous citez rappelle cette règle pour les produits visés aux articles 108 à 117 bis (dont les dividendes), lorsque le bénéficiaire effectif n’a pas son siège en France.

Toutefois, l’article 119 ter du CGI, transposant la directive européenne « mère-fille » (2011/96/UE), prévoit une exonération totale de retenue à la source pour les dividendes versés à une société mère établie dans un autre État membre de l’Union européenne, sous réserve du respect de plusieurs conditions cumulatives.

En l’espèce, la distribution envisagée remplit l’ensemble de ces conditions :
- La société mère est une société anonyme de droit luxembourgeois, forme expressément visée par la directive et par l’article 119 ter.
- Elle détient 100 % du capital de la filiale française depuis cinq ans, soit une participation largement supérieure au seuil de 10 % (ou 5 % selon les cas) et une durée de détention bien supérieure à deux ans.
- Elle est soumise à l’impôt sur les sociétés luxembourgeois, ce qui satisfait à la condition d’assujettissement à un impôt équivalent.
- Elle est le bénéficiaire effectif des dividendes, aucun élément ne suggérant un montage artificiel.

Le fait que la trésorerie distribuée provienne de la cession d’un actif est sans incidence : il s’agit bien d’une distribution de bénéfices (réserves distribuables) entrant dans le champ des articles 108 et suivants du CGI.

Par conséquent, la distribution de 20 000 000 € mise en paiement le 15 juin 2025 au profit de la société mère luxembourgeoise ne supportera aucune retenue à la source en France, sous réserve de l’accomplissement des formalités déclaratives usuelles (notamment la remise d’une attestation de résidence et de statut par la société mère).


---

## C09  (9 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Analyse juridique et fiscale – Applicabilité de l’exonération partielle de l’article 787 B du CGI**

**Objet de la consultation** :
Votre client, dirigeant d’une SAS détenant 40 appartements meublés (valeur des titres : 20 M€), souhaite donner en pleine propriété la totalité de ses titres à ses deux enfants à parts égales, sous le bénéfice de l’exonération partielle de 75 % prévue par l’article 787 B du CGI. La donation interviendrait le 25 octobre 2023, dans le cadre d’un engagement collectif de conservation (ECC) signé le 3 mars 2021 et toujours en cours, avec engagement individuel des donataires et maintien de la présidence par le donateur pendant 3 ans.

---

### **1. Conditions générales de l’article 787 B du CGI**
L’exonération partielle de 75 % s’applique aux transmissions de parts ou actions de sociétés exerçant une **activité industrielle, commerciale, artisanale, agricole ou libérale** (CGI, art. 787 B, al. 1). Sont expressément exclues les activités de **gestion de son propre patrimoine mobilier ou immobilier** (al. 2), sauf exceptions (al. 3).

#### **a) Activité éligible ?**
Votre société détient 40 appartements meublés. La qualification de l’activité dépend de la nature de la location :
- **Location meublée non professionnelle (LMNP)** : Si les appartements sont loués meublés **sans prestation para-hôtelière** (petit-déjeuner, ménage, etc.), l’activité relève de la **gestion de patrimoine immobilier** (exclue par l’al. 2 de l’art. 787 B).
  - *Risque* : L’administration fiscale et la jurisprudence considèrent généralement que la location meublée, même avec un bail commercial, constitue une activité civile de gestion de patrimoine (CE, 10 juillet 2020, n° 428234 ; BOI-ENR-DMTG-10-20-40-10, § 10).
- **Location meublée professionnelle (LMP) ou para-hôtelière** : Si la société fournit des **services para-hôteliers** (ex. : accueil, ménage quotidien, petit-déjeuner), l’activité peut être requalifiée en **activité commerciale** (CGI, art. 34 et 35), éligible à l’exonération.
  - *Preuves à apporter* : Contrats de location, factures des services, organisation interne (ex. : personnel dédié).

**Recommandation** :
- Vérifier si la société fournit des **services para-hôteliers** (même minimaux) pour requalifier l’activité en commerciale.
- À défaut, l’exonération serait **inapplicable** (sauf à démontrer une participation active au groupe, cf. al. 3, ce qui ne semble pas être le cas ici).

#### **b) Engagement de conservation (ECC et engagements individuels)**
Les conditions de durée sont remplies :
- **ECC** : Signé le 3 mars 2021 (durée minimale de 2 ans avant la donation, soit jusqu’au 3 mars 2023). La donation intervient après cette date (25 octobre 2023), donc l’ECC est valide.
- **Engagements individuels** : Les enfants s’engagent à conserver les titres pendant 4 ans à compter de la donation (soit jusqu’au 25 octobre 2027).
- **Maintien de la présidence** : Le donateur conserve la présidence pendant 3 ans (condition supplémentaire pour les sociétés non cotées).

**Risque** :
- Si l’activité est requalifiée en gestion de patrimoine, l’ECC et les engagements individuels ne suffisent pas à rendre l’exonération applicable.

---

### **2. Stratégie alternative si l’activité est exclue**
Si l’activité est jugée civile (gestion de patrimoine), deux options :
#### **a) Restructuration préalable**
- **Apport des immeubles à une société d’exploitation** : Créer une filiale commerciale (ex. : SAS) qui loue les appartements avec des services para-hôteliers, puis donner les titres de cette filiale (activité commerciale éligible).
  - *Délai* : La restructuration doit être effective **avant la donation** (risque de requalification en abus de droit si réalisée dans un but exclusivement fiscal).
  - *Coût* : Droits d’enregistrement sur l’apport (0,1 % pour les immeubles, CGI, art. 810), mais exonération possible si engagement de conservation (CGI, art. 727).

#### **b) Paiement des droits sans exonération**
- **Droits de donation** : Taux marginal de 45 % (après abattement de 100 000 € par enfant), soit environ **8,9 M€** de droits (20 M€ × 50 % × 45 % × 2 enfants).
- **Optimisation** :
  - Étalement du paiement sur 5 ans (CGI, art. 396).
  - Donation en nue-propriété (réduction de la base taxable).

---

### **3. Conclusion et recommandations**
#### **a) Risque principal**
L’exonération de 75 % **ne sera probablement pas applicable** si l’activité de la SAS est qualifiée de **gestion de patrimoine immobilier** (location meublée sans services para-hôteliers). L’administration fiscale pourrait contester la qualification commerciale et exiger le paiement des droits avec pénalités (10 % à 40 %).

#### **b) Actions à mener avant la donation**
1. **Auditer l’activité** :
   - Vérifier la présence de **services para-hôteliers** (même minimaux) pour requalifier l’activité en commerciale.
   - Consulter un expert-comptable pour établir une note justifiant la qualification commerciale (ex. : contrats, factures, organisation interne).
2. **Si l’activité est civile** :
   - **Option 1** : Restructurer la société (apport des immeubles à une filiale commerciale) avant la donation.
   - **Option 2** : Accepter le paiement des droits (8,9 M€) et optimiser via l’étalement ou la nue-propriété.
3. **Sécuriser la donation** :
   - Rédiger une **clause de réversion d’usufruit** en cas de non-respect des engagements de conservation.
   - Prévoir un **pacte adjoint** pour encadrer les obligations des donataires.

#### **c) Calendrier**
- **Avant le 25 octobre 2023** :
  - Finaliser l’audit de l’activité.
  - Si restructuration nécessaire, la réaliser **sans délai** (risque de requalification en abus de droit si trop proche de la donation).
- **Signature de la donation** :
  - Inclure une **clause suspensive** liée à l’obtention d’un rescrit fiscal si l’activité est limite (recommandé pour sécuriser la qualification commerciale).

---

### **4. Proposition de lettre de mission complémentaire**
Pour sécuriser la démarche, je vous propose de :
1. **Analyser les contrats de location** et les services fournis pour confirmer la qualification de l’activité.
2. **Rédiger une note juridique** sur l’éligibilité à l’article 787 B, avec argumentaire en cas de contrôle fiscal.
3. **Assister à la restructuration** (si nécessaire) et à la rédaction des actes de donation.
4. **Demander un rescrit fiscal** à l’administration pour confirmer l’éligibilité (délai : 3 à 6 mois).

**Coût estimé** :
- Audit et note juridique : 3 000 à 5 000 € HT.
- Restructuration (si applicable) : 5 000 à 10 000 € HT (frais de greffe, honoraires notariaux).
- Rescrit fiscal : 2 000 à 4 000 € HT.

---

### **5. Décision immédiate**
Compte tenu des enjeux (8,9 M€ de droits en jeu), je vous recommande de :
1. **Différer la donation** jusqu’à clarification de l’activité (si services para-hôteliers) ou finalisation de la restructuration.
2. **Engager l’audit** sous 15 jours pour trancher la qualification de l’activité.

Je reste à votre disposition pour échanger sur les modalités pratiques et les prochaines étapes.

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées du cabinet]


---

## C10  (10 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Non. L’exonération partielle de l’article 787 B du CGI n’est pas applicable.**

La société dont les titres sont transmis a pour activité exclusive la détention et la location de quarante appartements meublés. Aux termes mêmes du deuxième alinéa de l’article 787 B (dans sa rédaction applicable au 25 octobre 2023), « n’est pas considérée comme une activité industrielle, commerciale, artisanale, agricole ou libérale l’exercice par une société d’une activité de gestion de son propre patrimoine mobilier ou immobilier ».

Cette exclusion légale s’applique indépendamment de la qualification fiscale des revenus (BIC) que peut revêtir la location meublée au regard des articles 34 et 35. La société n’exerce pas une activité d’animation de groupe au sens du troisième alinéa. Les conditions formelles du pacte (engagement collectif du 3 mars 2021 portant sur la totalité des droits, engagements individuels des donataires, conservation de la présidence pendant trois ans) sont donc indifférentes : le seuil d’éligibilité tenant à la nature de l’activité n’est pas franchi.

La donation en pleine propriété des titres, d’une valeur de 20 M€, sera donc soumise aux droits de mutation à titre gratuit dans les conditions de droit commun (après abattements éventuels de l’article 779), sans application du régime de faveur.

Je reste à votre disposition pour chiffrer les droits et examiner d’éventuelles autres voies (donation-partage avec soulte, apport-cession, etc.).


---

## C11  (11 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Objet : Analyse fiscale de la distribution de dividendes à une société mère luxembourgeoise – Application de la retenue à la source**

**Madame, Monsieur,**

Nous vous remercions de nous avoir consultés sur les conséquences fiscales de la distribution de **20 000 000 €** à votre société mère luxembourgeoise, prévue pour le **15 juin 2025**. Nous analysons ci-dessous l’application de la **retenue à la source** (RAS) en vertu de l’**article 119 bis, 2 du CGI**, ainsi que les dispositions conventionnelles pertinentes.

---

### **1. Cadre juridique applicable**
#### **a) Règle interne française (CGI, art. 119 bis, 2)**
L’article 119 bis, 2 du CGI prévoit qu’une **retenue à la source de 30 %** (taux de droit commun, art. 187 du CGI) s’applique aux **dividendes** versés à des bénéficiaires **non résidents fiscaux en France**, sauf exceptions.

Votre société mère luxembourgeoise, **non résidente fiscale en France**, est donc en principe soumise à cette RAS, sauf si :
- Elle relève d’un **régime d’exonération** prévu par le CGI (ex. : OPCVM éligibles, non applicable ici) ;
- **Ou** si la **convention fiscale franco-luxembourgeoise** prévoit un taux réduit ou une exonération.

#### **b) Convention fiscale franco-luxembourgeoise (modifiée par l’avenant du 5 septembre 2014)**
La **convention du 1er avril 1958** (modifiée) prévoit à son **article 10 (Dividendes)** :
- **Taux de droit commun** : 15 % de RAS sur les dividendes.
- **Exonération totale** si le bénéficiaire est une **société luxembourgeoise** qui :
  - **Détient au moins 10 % du capital** de la société distributrice (votre cas : détention à 100 %) ;
  - **A détenu cette participation pendant au moins 24 mois** avant la distribution (votre cas : détention depuis 5 ans).

**→ Votre situation remplit ces conditions** : la distribution devrait donc **bénéficier d’une exonération totale de RAS** en vertu de la convention.

---

### **2. Conditions pratiques pour l’exonération**
Pour bénéficier de l’exonération, votre société mère luxembourgeoise doit :
1. **Fournir un certificat de résidence fiscale luxembourgeoise** (à demander auprès des autorités fiscales luxembourgeoises, valable pour l’année 2025).
2. **Justifier de la détention ininterrompue de 100 % du capital depuis au moins 24 mois** (vous remplissez cette condition).
3. **Remplir le formulaire n° 5000-SD** (déclaration de RAS) en cochant la case "Exonération conventionnelle" et en mentionnant l’**article 10 de la convention franco-luxembourgeoise**.

**→ À noter** : La RAS ne serait due que si ces justificatifs n’étaient pas fournis à temps. Dans ce cas, le taux de 15 % (conventionnel) s’appliquerait, et non 30 % (droit interne).

---

### **3. Autres points de vigilance**
#### **a) Régime mère-fille européen (Directive 2011/96/UE)**
Bien que la convention franco-luxembourgeoise soit plus favorable, la **directive mère-fille** (transposée en droit français et luxembourgeois) prévoit aussi une exonération de RAS pour les distributions entre sociétés mères et filiales de l’UE sous conditions :
- Détention ≥ 10 % du capital ;
- Détention ≥ 2 ans (votre cas).

**→ Cette directive confirme l’exonération**, mais la convention reste le fondement principal en l’espèce.

#### **b) Risque de requalification en "bénéfice distribuable"**
L’administration fiscale française pourrait contester l’exonération si elle estime que :
- La distribution **dépasse les bénéfices distribuables** (à vérifier via les comptes sociaux) ;
- La société mère luxembourgeoise est une **société écran** (peu probable ici, car elle est soumise à l’IS luxembourgeois et détient la filiale depuis 5 ans).

**→ Recommandation** : Conserver une documentation prouvant que la distribution correspond à des **bénéfices réguliers** (comptes certifiés, procès-verbal d’AG).

#### **c) Impact au Luxembourg**
La société mère luxembourgeoise sera imposable sur les dividendes reçus, mais :
- Le Luxembourg applique un **régime d’exonération des participations** (art. 166 LIR) si la filiale française est soumise à un impôt équivalent à l’IS luxembourgeois (ce qui est le cas).
- **→ Pas d’imposition au Luxembourg** sur ces dividendes (sous réserve de la règle des "bénéfices actifs").

---

### **4. Synthèse et recommandations**
| **Point**               | **Conclusion**                                                                 |
|-------------------------|-------------------------------------------------------------------------------|
| **Retenue à la source** | **Exonération totale** (0 %) en vertu de l’article 10 de la convention franco-luxembourgeoise. |
| **Justificatifs**       | Certificat de résidence fiscale luxembourgeoise + formulaire 5000-SD.         |
| **Risque fiscal**       | Faible si les conditions de détention et de résidence sont documentées.       |
| **Impact au Luxembourg**| Exonération probable (régime des participations).                             |

**Prochaines étapes** :
1. **Obtenir le certificat de résidence fiscale** de la société mère luxembourgeoise pour 2025.
2. **Remplir le formulaire 5000-SD** avant la distribution (à déposer auprès du service des impôts des entreprises compétent).
3. **Conserver les preuves** de la détention ininterrompue de la participation.

Nous restons à votre disposition pour :
- Vous assister dans la **rédaction des justificatifs** ;
- Vérifier les **comptes sociaux** pour confirmer le montant distribuable ;
- Vous représenter en cas de **contrôle fiscal** ultérieur.

**→ En l’état, la distribution prévue ne devrait pas donner lieu à une RAS, sous réserve du respect des formalités.**

Veuillez agréer, Madame, Monsieur, l’expression de nos salutations distinguées.

**[Votre nom]**
Avocat fiscaliste
[Cabinet]
[Coordonnées]


---

## C12  (12 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

## 1. Montant et délai de réinvestissement

La cession étant intervenue moins de trois ans après l’apport, elle entraîne en principe la fin du report d’imposition de la plus-value d’apport. Pour éviter cette conséquence, la holding doit respecter cumulativement :

- un **engagement formel de réinvestissement** ;
- un réinvestissement représentant au moins **70 % du produit de cession** ;
- dans les **trois ans suivant la cession** ;
- dans une activité répondant strictement aux conditions du texte.

Sous réserve que les 9 000 000 € correspondent bien au « produit de cession » au sens fiscal, le minimum est donc :

> **9 000 000 € × 70 % = 6 300 000 €**

Il ne s’agit pas de 70 % de la plus-value, ni de 70 % du prix net après impôt ou frais, mais, en principe, de 70 % du produit de cession. Il faut néanmoins relire l’acte de vente pour traiter les éventuels compléments de prix, séquestres, garanties de passif ou ajustements de prix.

Je déconseille de viser exactement 6 300 000 €. Une marge de sécurité — par exemple un investissement de **6,5 à 6,75 M€** — réduirait le risque qu’une dépense soit partiellement requalifiée comme non éligible.

Le délai court à compter de la **date juridique de la cession**, et non de la date d’encaissement du prix. Si le transfert des titres a eu lieu, par exemple, le 18 février 2026, l’investissement devra être réalisé au plus tard le **18 février 2029**.

## 2. Les liquidités placées sur le compte de la holding ne constituent pas un réinvestissement

Le maintien des 9 M€ :

- sur un compte bancaire ;
- sur un compte à terme ;
- en SICAV monétaires ou autres valeurs de trésorerie ;
- dans un portefeuille de titres de placement,

ne satisfait pas à l’obligation. Ces placements peuvent être utilisés temporairement pour sécuriser et rémunérer les fonds en attendant le projet, mais ils ne compteront pas dans le quota de 70 %.

De même, la simple signature d’une lettre d’intention ou d’une promesse, sans décaissement ni affectation effective des fonds, est insuffisante ou, à tout le moins, très risquée.

## 3. Nature du réinvestissement à privilégier

Sur le seul fondement du a) communiqué, les fonds doivent financer des **moyens permanents d’exploitation affectés à l’activité propre de la holding**.

Cela suppose que la holding exerce réellement une activité opérationnelle éligible : commerciale, industrielle, artisanale, libérale ou agricole, selon les renvois du texte. Une modification de l’objet social ou l’inscription comptable d’une activité ne suffira pas. Il faut une activité effective, avec une substance économique vérifiable.

Pourraient notamment être envisagés, selon le projet :

- la création ou l’acquisition directe d’un fonds de commerce ou d’une branche d’activité exploitée par la holding ;
- l’acquisition de machines, matériels, outillages, logiciels ou équipements nécessaires à cette activité ;
- le financement d’installations ou de locaux effectivement affectés à l’exploitation opérationnelle ;
- plus généralement, le financement d’actifs durables indispensables à l’activité propre de la holding.

En revanche, je déconseille de considérer comme éligibles, sur le seul fondement du a) :

- un prêt ou une avance en compte courant à une filiale ;
- l’acquisition passive de titres de sociétés ;
- des placements financiers ;
- une activité de simple gestion de portefeuille ;
- l’achat d’un immeuble locatif ou l’investissement dans une SCI patrimoniale ;
- la simple gestion du patrimoine immobilier de la holding.

L’immobilier est spécialement sensible puisque le texte exclut la gestion de son propre patrimoine immobilier. Un investissement immobilier ne devrait être envisagé que si l’immeuble constitue un véritable moyen d’exploitation d’une activité opérationnelle exercée directement, avec une analyse fiscale préalable très documentée.

Si la holding doit demeurer une pure holding patrimoniale, le a) n’est probablement pas la voie adaptée. Il faudra alors examiner les autres modalités de réinvestissement éventuellement prévues par le reste de l’article 150-0 B ter dans sa rédaction applicable en 2026. Une acquisition de titres ou une souscription au capital d’une société ne doit pas être engagée en supposant qu’elle relève du a).

## 4. Mes recommandations immédiates

Je recommande de procéder de la manière suivante.

### A. Sécuriser le calendrier

Il faut déterminer précisément :

1. la date de l’apport initial ;
2. la date de transfert de propriété des titres cédés ;
3. la date limite exacte de février 2029 ;
4. le prix fiscal de référence servant au calcul des 70 %.

Je fixerais en pratique une échéance interne au plus tard au **30 septembre 2028**, afin de ne pas dépendre d’une opération conclue dans les dernières semaines.

### B. Formaliser immédiatement l’engagement

La holding doit prendre et déclarer l’engagement de réinvestissement dans les formes requises. Il convient notamment :

- de faire constater cet engagement dans une décision de l’organe compétent de la holding ;
- de l’annexer ou de le mentionner dans les déclarations fiscales requises au titre de la cession ;
- de s’assurer que la déclaration de suivi du report d’imposition du client est correctement renseignée ;
- d’informer sans délai l’expert-comptable de la holding.

L’investissement futur ne répare pas nécessairement l’omission d’une formalité initiale. Il ne faut donc pas attendre 2028 pour traiter cet aspect.

### C. Constituer une enveloppe dédiée

Je préconise d’isoler au moins **6,5 M€** sur un compte distinct et de ne pas utiliser cette somme :

- pour distribuer des dividendes ;
- pour rembourser le compte courant du client ;
- pour consentir des avances au groupe ;
- pour régler des dépenses étrangères au projet éligible.

Les 30 % non soumis à l’obligation de réinvestissement, soit théoriquement 2,7 M€, peuvent rester disponibles, sous réserve des autres conséquences fiscales d’une distribution ou d’une réduction de capital.

### D. Documenter l’affectation des fonds

Pour chaque dépense, le dossier devra contenir :

- le contrat ou la facture ;
- la preuve du paiement avant l’échéance ;
- l’inscription comptable et, le cas échéant, au registre des immobilisations ;
- une note expliquant son caractère permanent ;
- la preuve de son affectation à l’activité opérationnelle ;
- le business plan, les contrats commerciaux, les moyens humains et les locaux démontrant la réalité de l’activité.

Pour un projet atypique ou à forte composante immobilière, je recommanderais soit de choisir une structure plus sûre, soit de solliciter un **rescrit fiscal** avant de réaliser l’investissement.

## 5. Risque en cas d’insuffisance

Le quota est une condition de seuil. Un investissement de 6,2 M€ au lieu de 6,3 M€ ne devrait donc pas seulement entraîner l’imposition de la fraction manquante : il expose à la **perte du report d’imposition dans son ensemble**, avec taxation de la plus-value constatée lors de l’apport et, selon les règles applicables, intérêts de retard.

Cette imposition personnelle du client est distincte de l’imposition éventuellement supportée par la holding sur sa propre plus-value de cession.

### Conseil synthétique

Je conseille donc :

1. de sanctuariser immédiatement au moins **6,5 M€** ;
2. de formaliser sans attendre l’engagement fiscal ;
3. de sélectionner, avant fin 2027, une véritable activité opérationnelle exercée directement par la holding, avec des investissements corporels et incorporels clairement affectés à cette activité ;
4. de réaliser les décaissements bien avant la date anniversaire de février 2029 ;
5. de ne pas retenir une acquisition de titres, un prêt intragroupe ou un investissement immobilier patrimonial sans examen des autres dispositions de l’article et validation fiscale préalable.


---

## C13  (13 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

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

## C14  (14 sur 45)

**VOTRE CODE : ______________________________**

**Fait manquant :** La date de dépôt du projet au greffe. Le régime nouveau ne s'applique qu'aux opérations dont le projet a été déposé à compter du 1er juillet 2023.

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus directement aux
associes de la societe apporteuse, afin que chaque branche de la
famille detienne sa societe.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder :**

## Conclusion

**Oui, en principe**, l’apport de la branche industrielle peut bénéficier du régime spécial des articles 210 A et suivants, **même si les titres de la société bénéficiaire sont remis directement aux associés de la holding apporteuse**.

Le 4° du I de l’article 210-0 A vise désormais expressément cette modalité. L’absence de remise préalable des titres à la société apporteuse n’est donc pas, à elle seule, un obstacle.

En revanche, ce texte ne suffit pas à rendre **l’ensemble de la séparation familiale** fiscalement neutre. Il faut distinguer :

1. le régime fiscal de l’apport de la branche industrielle ;
2. le traitement de l’attribution des titres aux associés ;
3. les opérations permettant à chaque branche familiale de ne plus détenir que « sa » société.

---

## 1. L’opération entre dans la définition de l’apport partiel d’actif

L’article 210-0 A, I, 4° prévoit deux modalités alternatives de rémunération :

- remise des titres à la société apporteuse ; ou
- remise directe des titres aux associés de la société apporteuse.

Le schéma envisagé constitue donc fiscalement un **apport partiel d’actif avec attribution directe des titres**, parfois qualifié de scission partielle.

Il n’est plus possible d’écarter le régime spécial au seul motif que la holding n’entre pas elle-même en possession des titres de la société industrielle nouvelle.

---

## 2. La branche industrielle doit constituer une branche complète d’activité

Le bénéfice de plein droit du régime suppose que les éléments apportés constituent une **branche complète et autonome d’activité**.

Il faut vérifier que l’apport comprend l’ensemble des éléments permettant à l’activité industrielle de fonctionner par ses propres moyens, notamment :

- clientèle et contrats ;
- immobilisations et stocks ;
- personnel affecté à l’activité ;
- autorisations, licences et droits incorporels ;
- créances et dettes se rattachant à l’exploitation ;
- moyens administratifs nécessaires, le cas échéant.

Les fonctions ou actifs communs aux deux branches devront faire l’objet d’une analyse particulière : immobilier, trésorerie, informatique, direction, marques, contrats-cadres, fonctions support, etc. Une simple collection d’actifs industriels ne suffirait pas si elle n’est pas susceptible de constituer une exploitation autonome.

La holding doit également exercer réellement les activités concernées. Si les activités industrielle et de négoce sont en réalité exercées par des filiales, l’analyse est différente : ce sont alors des titres de participation qui sont apportés, lesquels ne sont assimilés à une branche complète que dans les cas prévus par l’article 210 B.

---

## 3. Les conditions techniques des articles 210 A et 210 B restent applicables

L’article 210-0 A est essentiellement un texte de définition. L’opération doit encore respecter les conditions du régime spécial, notamment les engagements et obligations déclaratives prévus par les articles 210 A, 210 B et 54 septies du CGI.

La société bénéficiaire devra notamment reprendre les valeurs fiscales, provisions et obligations de réintégration attachées aux biens apportés. Le traité d’apport devra donc comporter les mentions et engagements fiscaux appropriés.

Sous ces conditions, les plus-values latentes sur les éléments apportés ne sont pas immédiatement imposées : leur imposition est reportée ou étalée selon la nature des biens.

---

## 4. L’attribution directe doit être distinguée d’une attribution sélective

C’est le principal point de vigilance.

Une attribution directe des titres **à tous les associés, proportionnellement à leurs droits**, ne réalise pas, à elle seule, la séparation recherchée. Chaque branche familiale détiendrait alors :

- des titres de la société industrielle nouvelle ; et
- des titres de la holding conservant l’activité de négoce.

Pour parvenir à ce qu’une branche familiale détienne uniquement la société industrielle et l’autre uniquement la société de négoce, il faut donc soit :

- procéder à une attribution non proportionnelle des titres ;
- faire sortir certains associés du capital de la holding ;
- organiser des échanges ou cessions de titres ;
- ou combiner la scission partielle avec une réduction de capital ou un rachat de titres.

Ces opérations complémentaires ont leur propre régime fiscal.

En particulier, la neutralité de l’attribution au niveau des associés, organisée notamment par l’article 115 du CGI, est encadrée par des conditions spécifiques, notamment quant :

- au caractère complet des branches apportée et conservée ;
- au délai d’attribution ;
- et, pour le régime de plein droit, à l’attribution proportionnelle aux droits des associés.

Une répartition « croisée » ou sélective — les titres industriels à une branche familiale et l’activité de négoce à l’autre — ne doit donc pas être considérée comme automatiquement couverte par le seul article 210-0 A. À défaut de régime de neutralité ou d’agrément approprié, la remise des titres pourrait être traitée comme une distribution imposable ou entraîner l’imposition d’une opération sur titres.

---

## 5. Le motif économique doit être documenté

Le régime spécial peut être écarté lorsque l’opération poursuit comme objectif principal, ou comme l’un de ses objectifs principaux, la fraude ou l’évasion fiscales.

Une séparation familiale peut reposer sur de véritables motifs économiques, par exemple :

- divergence de stratégie entre les deux branches ;
- autonomie de gestion des activités ;
- prévention d’un blocage de gouvernance ;
- préparation de transmissions distinctes ;
- besoins de financement différents ;
- spécialisation des équipes dirigeantes.

Ces motifs devront être établis dans les procès-verbaux, rapports, protocoles familiaux et documents préparatoires. La seule volonté de répartir un patrimoine familial, sans justification économique liée aux entreprises, serait plus fragile.

---

## Avis

**L’apport de la branche industrielle avec remise directe des titres aux associés est éligible, dans son principe, au régime des articles 210 A et suivants**, sous réserve que l’activité apportée constitue une branche complète et que les autres conditions du régime soient respectées.

En revanche, **la séparation effective des deux branches familiales ne peut pas être sécurisée sur le seul fondement de l’article 210-0 A, I, 4°**. Il faut arrêter précisément :

- l’identité des associés recevant les titres industriels ;
- la proportion de titres attribuée à chacun ;
- le sort des titres de la holding détenus par la branche familiale appelée à en sortir ;
- l’éventuelle soulte ;
- et le traitement fiscal de l’attribution ou des échanges au niveau des associés.

Si l’attribution doit être asymétrique, une analyse spécifique de l’article 115 du CGI, de la nécessité éventuelle d’un agrément et, selon la structure retenue, des régimes d’échange ou de rachat de titres est indispensable. Compte tenu de l’enjeu, je recommanderais également un **rescrit préalable** si le schéma ne respecte pas strictement les conditions d’une attribution proportionnelle de plein droit.


---

## C15  (15 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

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

## C16  (16 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**CONSULTATION**

**Objet :** Éligibilité au régime de faveur de l'article 787 B du CGI d'une donation-partage de la totalité des actions d'une SAS détenant quarante appartements meublés — projet d'acte au 25 octobre 2023

---

## 1. Conclusion (à titre liminaire)

**En l'état des éléments communiqués, je vous déconseille formellement de signer l'acte le 25 octobre 2023 en y insérant les engagements de l'article 787 B.**

Toutes les conditions « techniques » du dispositif (engagement collectif, engagements individuels, fonction de direction) paraissent réunies. Mais **la condition première — celle qui tient à la nature de l'activité de la société — n'est, selon toute vraisemblance, pas remplie** : une société qui se borne à donner en location quarante appartements meublés exerce une activité de **gestion de son propre patrimoine immobilier**, expressément exclue par le deuxième alinéa de l'article 787 B.

L'enjeu chiffré est de l'ordre de **7,6 M€ de droits** (voir § 5). Il justifie un audit préalable des modalités réelles d'exploitation avant toute signature.

---

## 2. Les conditions qui ne posent pas de difficulté

Je les valide rapidement, sous réserve de la production des pièces.

**a) L'engagement collectif de conservation (a de l'art. 787 B)**
- Signé le 3 mars 2021, il porte sur 100 % des titres : les seuils de 17 % des droits financiers et 34 % des droits de vote (société non cotée) sont largement dépassés.
- Il est en cours au jour de la donation et a couru plus de deux ans : la condition de durée minimale est satisfaite.
- *À vérifier* : l'enregistrement de l'acte (date certaine opposable à l'administration) et, si le terme initial était de deux ans, la réalité de la reconduction tacite ainsi que la faculté pour les donataires de poursuivre l'engagement jusqu'à son terme.

**b) Les engagements individuels (c de l'art. 787 B)**
- Attention à la rédaction : chaque enfant s'engage à conserver les titres **pendant quatre ans à compter de l'expiration de l'engagement collectif** — et non à compter de la donation. Dans l'intervalle, les donataires doivent **poursuivre l'engagement collectif** jusqu'à son terme. Les deux obligations doivent figurer distinctement dans l'acte.

**c) La fonction de direction (d de l'art. 787 B)**
- La présidence d'une SAS figure bien parmi les fonctions éligibles par renvoi au 1° du 1 du III de l'article 975 du CGI.
- Elle doit être exercée **pendant la durée de l'engagement collectif restant à courir et pendant les trois ans qui suivent la transmission** : la déclaration du dirigeant y satisfait.
- Elle doit être **effective** (et non purement statutaire) : je recommande de conserver la trace matérielle de cet exercice (décisions présidentielles, correspondances, contrats signés). La condition de « rémunération normale » propre à l'IFI n'est pas transposable telle quelle, mais l'absence totale de rémunération est un indice défavorable en cas de contrôle.

**d) Obligations déclaratives**
- Attestation de la société annexée à l'acte, mentions des engagements, attestations annuelles/triennales ultérieures : à faire figurer au dossier du notaire.

---

## 3. Le point bloquant : la nature de l'activité

### 3.1. L'articulation des deux premiers alinéas

Le premier alinéa vise les sociétés dont l'activité principale est « industrielle, **commerciale, au sens des articles 34 et 35** ». Or l'article 35, I, 5° bis range dans les BIC « les personnes qui donnent en location directe ou indirecte des locaux d'habitation meublés ».

C'est précisément l'argument textuel que la Cour de cassation avait retenu pour admettre la location meublée au bénéfice du régime (Cass. com., 1er juin 2023, n° 22-15.152), contre la doctrine administrative.

**Ce raisonnement est aujourd'hui neutralisé par le deuxième alinéa** : « n'est pas considérée comme une activité industrielle, commerciale, artisanale, agricole ou libérale l'exercice par une société d'une activité de **gestion de son propre patrimoine mobilier ou immobilier** ». Ce texte, introduit dans l'article 787 B lui-même, constitue une exception spéciale qui prime le renvoi général aux articles 34 et 35 ; il ne laisse plus de place à l'interprétation littérale antérieure.

La location meublée « nue de services », fût-elle exercée à titre habituel, sur quarante lots et avec une structure professionnelle, demeure la **gestion d'un patrimoine immobilier appartenant à la société**. Le volume ne transforme pas la nature de l'activité.

### 3.2. L'entrée en vigueur

Vous me demandez de raisonner sur le texte tel que reproduit, que vous indiquez applicable au jour de la donation. C'est cohérent avec le dispositif d'entrée en vigueur retenu par le législateur, qui a rendu cette rédaction applicable **aux transmissions intervenant à compter du 17 octobre 2023** — c'est-à-dire précisément pour couper court aux donations d'anticipation.

Une donation du **25 octobre 2023 est donc dans le champ** du texte nouveau. Elle ne peut pas se prévaloir de la jurisprudence de juin 2023.

*Deux réserves à formuler par honnêteté intellectuelle :*
- Je vous invite à faire revérifier au texte publié la date exacte de prise d'effet ; huit jours séparent ici la donation de la date-charnière, et cet écart est déterminant. Si, par extraordinaire, l'entrée en vigueur était fixée au 1er janvier 2024, l'analyse serait renversée et la donation du 25 octobre 2023 relèverait de la jurisprudence favorable.
- Une contestation de la « petite rétroactivité » du dispositif (garantie des situations légalement acquises, article 16 DDHC) est théoriquement concevable mais, s'agissant d'une donation non encore réalisée au 17 octobre, elle n'a **aucune chance sérieuse de prospérer** : nul n'a de droit acquis au maintien d'une législation fiscale pour une opération future. Je ne construirais pas une opération à 8 M€ sur ce fondement.

### 3.3. La seule voie d'éligibilité : l'exploitation para-hôtelière

Il existe une frontière, et une seule : celle qui sépare la **gestion locative** d'une **exploitation**. La société qui, au-delà de la mise à disposition du logement meublé, fournit à sa clientèle des prestations de services caractéristiques du secteur hôtelier — accueil/réception, fourniture du linge, nettoyage régulier en cours de séjour, petit-déjeuner ou restauration (au moins trois de ces quatre prestations, par référence à l'article 261 D, 4°, b du CGI) — n'exerce plus une gestion de patrimoine : elle exploite une entreprise commerciale. Le même raisonnement vaut pour une résidence de tourisme, une résidence-services, une activité de coliving avec services, ou une exploitation de courte durée type « hôtellerie de fait ».

**Questions factuelles à trancher avant toute signature :**
1. Nature des contrats : baux meublés d'habitation (12 mois / 9 mois étudiant), baux mobilité, ou contrats de location de courte durée ?
2. La société fournit-elle des services ? Lesquels, à quelle fréquence, facturés comment (forfaitairement dans le loyer ou séparément) ?
3. Existe-t-il du personnel salarié affecté à l'accueil, au ménage, à la maintenance ? Ou un contrat de conciergerie/gestion externalisée — et, dans ce cas, qui supporte le risque d'exploitation et contracte avec le client final ?
4. Régime TVA de la société : les loyers sont-ils soumis à la TVA au titre du 4°, b de l'article 261 D ? **C'est l'indice le plus probant.** Une société para-hôtelière est nécessairement assujettie ; une société qui facture des loyers exonérés de TVA sera très difficilement défendable.
5. Ventilation du chiffre d'affaires et de l'actif brut entre l'éventuelle activité de services et la location pure (critère de l'activité **principale** en cas d'activité mixte : faisceau d'indices, principalement CA et valeur des actifs affectés).
6. Les immeubles sont-ils au bilan en immobilisations ou en stocks ? Y a-t-il un classement (meublés de tourisme, résidence de tourisme) ?

**Un point d'attention supplémentaire, souvent négligé :** la condition d'activité éligible doit être satisfaite **depuis la conclusion de l'engagement collectif (3 mars 2021) et jusqu'au terme des engagements individuels**. Une « para-hôtellerisation » décidée aujourd'hui, à quelques jours de l'acte, serait à la fois inopérante pour le passé et exposée au grief d'abus de droit (LPF, art. L. 64 et L. 64 A — montage à but principalement fiscal). Il faudrait reconstruire l'opération : mise en place effective et durable de l'exploitation, puis nouvel engagement collectif, puis transmission au terme du délai de deux ans.

---

## 4. Réponse à la question posée

**Non**, sauf à démontrer que la société exerce en réalité une activité para-hôtelière ou hôtelière à titre principal, et ce depuis la signature de l'engagement collectif.

Si la société se borne à louer meublé quarante appartements, l'exonération de 75 % sera refusée, et avec elle la **réduction de droits de 50 % de l'article 790 du CGI** (donateur de moins de 70 ans, donation en pleine propriété), qui n'est ouverte qu'aux transmissions bénéficiant du 787 B. Le régime de **paiement différé et fractionné sur quinze ans** (art. 397 A, ann. III) sera également hors d'atteinte, pour le même motif tenant à la nature de l'activité.

---

## 5. Chiffrage de l'enjeu (donation-partage, deux enfants, 10 M€ chacun, abattement 100 000 €)

| | Par enfant | Total |
|---|---|---|
| **Avec 787 B + art. 790** (base 2,5 M€) | ≈ 421 000 € | **≈ 842 000 €** |
| **Sans régime de faveur** (base 10 M€) | ≈ 4 217 000 € | **≈ 8 435 000 €** |

**Écart : environ 7,6 M€.** En cas de remise en cause a posteriori, s'ajouterait l'intérêt de retard de 0,20 % par mois (majoration de 40 % en cas de manquement délibéré, non encourue en principe ici si l'acte est transparent).

---

## 6. Recommandations

1. **Reporter la signature.** Aucune urgence ne justifie de signer le 25 octobre un acte dont le régime est très probablement condamné. La date du 17 octobre étant dépassée, l'anticipation n'apporte plus rien.

2. **Diligenter un audit d'activité** (liasses 2019-2022, contrats de location types, déclarations de TVA, contrats de travail ou de prestation, plaquettes commerciales, avis de CFE). Ce document servira de dossier de défense en cas de contrôle et couvrira la responsabilité du notaire.

3. Si l'audit révèle une **activité para-hôtelière réelle et ancienne** : sécuriser par un **rescrit** (LPF, art. L. 80 B, 1°) avant la donation, et documenter la prépondérance de l'activité éligible. Le délai de réponse (trois mois) est à intégrer au calendrier.

4. Si l'activité est purement locative, examiner les voies alternatives, qui ne relèvent plus du 787 B :
   - **Donation de la seule nue-propriété** : le donateur ayant 62 ans, la nue-propriété est évaluée à 60 % (art. 669), soit une assiette de 12 M€ au lieu de 20 M€, avec extinction de l'usufruit en franchise de droits. Perte de la réduction de l'article 790 (réservée à la pleine propriété), mais économie nette substantielle. À combiner avec une réserve de quasi-usufruit sur les distributions et une convention de démembrement.
   - **Étalement** : donations successives par périodes de quinze ans (art. 784), en tenant compte de l'âge du donateur.
   - **Restructuration à moyen terme** : mise en place d'une véritable exploitation para-hôtelière (avec ses conséquences en TVA, en TVA sur immobilisations et en matière sociale), puis nouvel engagement collectif, puis transmission au terme de deux ans. Horizon réaliste : 2026-2027. Le donateur ayant 62 ans, la fenêtre de l'article 790 (avant 70 ans) reste ouverte.
   - **Cession partielle / OBO familial** avec endettement de la structure, réduisant la valeur des titres transmis — sous réserve d'un examen attentif de l'abus de droit et de la substance de l'opération.
   - Prise en charge des droits par le donateur (non taxable, art. 1712 CGI a contrario / doctrine), si l'option d'une donation immédiate était néanmoins retenue.

5. **Ne pas insérer dans l'acte les engagements du 787 B « à toutes fins utiles »** si l'éligibilité n'est pas acquise : cela ne coûte rien fiscalement mais crée une apparence trompeuse, engage les donataires sur douze ans d'obligations de conservation et fragilise la position de tous les intervenants.

---

Je reste à votre disposition, avec votre notaire, pour examiner les pièces et, le cas échéant, rédiger la demande de rescrit ou le schéma alternatif.

*La présente consultation est établie au vu des seuls éléments communiqués et sous réserve de la vérification, au texte publié, de la date exacte d'entrée en vigueur de la rédaction reproduite.*


---

## C17  (17 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

Cher confrère, cher client,

Vous m’interrogez sur l’applicabilité de l’exonération partielle de droits de mutation à titre gratuit prévue par l’article 787 B du CGI à la donation projetée des titres de la SAS, valorisés à 20 M€, détenus par le dirigeant et portant sur quarante appartements meublés.

La réponse n’est pas évidente et appelle une analyse rigoureuse de la condition tenant à la nature de l’activité de la société, qui constitue ici le point central de la discussion.

**1. Le cadre juridique : une exonération sous condition d’activité opérationnelle**

L’article 787 B, dans sa rédaction applicable au 25 octobre 2023, subordonne l’exonération partielle de 75 % à la condition que la société dont les titres sont transmis exerce une activité industrielle, commerciale (au sens des articles 34 et 35), artisanale, agricole ou libérale. Il exclut expressément les sociétés dont l’activité consiste en la gestion de leur propre patrimoine mobilier ou immobilier.

La location de biens meublés est, en droit fiscal, une activité commerciale par nature (article 35-I-5° du CGI). Toutefois, la jurisprudence et la doctrine administrative (BOI-ENR-DMTG-10-20-40-10) opèrent une distinction fondamentale entre :

- L’exercice d’une véritable activité commerciale de location meublée, qui suppose la mise en œuvre de moyens matériels et humains significatifs, la fourniture de prestations de services accessoires (accueil, entretien, fourniture de linge, etc.) et une gestion active s’apparentant à une exploitation hôtelière ou para-hôtelière ;
- La simple gestion passive d’un patrimoine immobilier, même meublé, qui se borne à percevoir des loyers sans implication opérationnelle réelle.

En d’autres termes, la seule circonstance que les logements soient meublés ne suffit pas à conférer à la société le caractère d’une société commerciale éligible au dispositif Dutreil. Il faut caractériser une activité économique effective.

**2. Application au cas d’espèce : une analyse factuelle indispensable**

Votre client indique que la SAS détient quarante appartements meublés. Pour déterminer si l’exonération est applicable, il est impératif de connaître les modalités concrètes d’exploitation de ces biens. Plusieurs indices doivent être examinés :

- La nature des baux : s’agit-il de locations saisonnières, de baux commerciaux, de locations étudiantes avec services, ou de simples locations nues déguisées ?
- Les moyens humains et matériels : la société emploie-t-elle du personnel (concierge, femme de ménage, gestionnaire) ? Dispose-t-elle d’une structure d’accueil, d’un site internet de réservation, de services de nettoyage ou de fourniture de linge ?
- Le niveau des prestations annexes : propose-t-elle des services hôteliers (petit-déjeuner, accueil, entretien régulier) ou se contente-t-elle de mettre à disposition des locaux meublés sans intervention particulière ?
- Le chiffre d’affaires et le mode de gestion : l’activité est-elle externalisée auprès d’un gestionnaire professionnel ou gérée en interne ? Quel est le volume des recettes et la nature des charges ?

Si la société se borne à détenir et à louer des appartements meublés sans fournir de prestations significatives, l’administration fiscale considérera qu’elle exerce une activité de gestion de son propre patrimoine, exclue du bénéfice de l’article 787 B. À l’inverse, si elle exerce une activité commerciale effective de location meublée avec services, l’exonération peut être revendiquée.

La circonstance que le dirigeant conserve la présidence pendant trois ans est un élément favorable, mais ne suffit pas à qualifier l’activité. De même, le nombre d’appartements (40) peut plaider en faveur d’une activité d’envergure, mais ce n’est pas déterminant en soi.

**3. Les conditions formelles liées aux engagements collectif et individuel**

Sur le plan formel, vous indiquez que :

- Un engagement collectif de conservation a été signé le 3 mars 2021, portant sur la totalité des droits, et qu’il est toujours en cours ;
- Chaque enfant prendra l’engagement individuel de conservation des titres reçus pour une durée de quatre ans à compter de la donation ;
- La donation interviendrait le 25 octobre 2023.

Sous réserve de la vérification des seuils de détention (l’engagement collectif doit porter sur au moins 17 % des droits financiers et des droits de vote pour une société non cotée, ce qui semble être le cas puisque l’engagement porte sur la totalité des titres), la condition de durée minimale de l’engagement collectif avant la transmission est respectée : à la date de la donation, l’engagement collectif aura été en cours depuis plus de deux ans (du 3 mars 2021 au 25 octobre 2023). Les engagements individuels des donataires, qui doivent porter sur les titres reçus et courir jusqu’au 25 octobre 2027, sont également conformes aux exigences légales.

Ainsi, si l’activité est éligible, les conditions formelles sont réunies.

**4. Conclusion et recommandations**

En l’état des informations fournies, il n’est pas possible de se prononcer avec certitude sur l’applicabilité de l’exonération partielle de l’article 787 B. Le risque de remise en cause par l’administration fiscale est réel si l’activité de location meublée n’est pas assortie de prestations de services suffisantes pour caractériser une activité commerciale opérationnelle.

Je vous recommande de :

- Procéder à un audit détaillé de l’activité de la SAS afin de rassembler tous les éléments factuels démontrant le caractère commercial de l’exploitation (contrats de location, factures, contrats de travail, documentation commerciale, etc.) ;
- Le cas échéant, si l’activité s’avère effectivement éligible, solliciter un rescrit fiscal (procédure de rescrit général prévue à l’article L. 80 B du LPF) pour sécuriser l’opération avant la signature de la donation. Le délai d’instruction est de trois mois, ce qui est compatible avec la date envisagée du 25 octobre 2023 si la demande est déposée rapidement ;
- À défaut de certitude, envisager des scénarios alternatifs (transformation de l’activité avant la donation, donation avec réserve d’usufruit, etc.) pour optimiser la transmission dans un cadre sécurisé.

Je me tiens à votre disposition pour analyser plus en détail les caractéristiques de l’activité et vous assister dans la mise en œuvre de la stratégie la plus adaptée.

Bien à vous,

[Signature]


---

## C18  (18 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Consultation – Cession de titres de SCI à prépondérance immobilière**

Cher Client,

Vous nous consultez préalablement à la signature, prévue le 20 mars 2024, de l’acte de cession des titres d’une SCI dont l’actif est constitué à 80 % d’immeubles situés en France, pour un prix de 4 000 000 €.

**1. Droit d’enregistrement dû**

La SCI constitue une personne morale à prépondérance immobilière au sens de l’article 726, I, 2° du CGI : ses droits sociaux ne sont pas négociés sur un marché réglementé ou un système multilatéral de négociation et son actif est principalement constitué d’immeubles situés en France.

La cession est donc soumise au droit d’enregistrement de 5 % prévu par ce texte (aucune des exclusions prévues – organismes HLM, certaines sociétés foncières ou SEM de logements sociaux – n’étant applicable).

Le droit est liquidé sur le prix convenu (4 000 000 €), soit **200 000 €**. Il est dû par l’acquéreur. L’acte devra mentionner le paiement ou l’engagement de paiement.

Si la cession était réalisée à l’étranger, elle devrait en outre être constatée dans le délai d’un mois par acte authentique reçu par un notaire exerçant en France (art. 726, III-A).

**2. Mentions obligatoires dans l’acte**

Conformément à l’article 726, III-B du CGI, l’acte (ou la déclaration) doit indiquer expressément :

- si la SCI est une société mentionnée à l’article 1655 ter du CGI ;
- si les participations cédées confèrent au cessionnaire, directement ou indirectement, le droit à la jouissance d’immeubles ou de fractions d’immeubles au sens de l’article 728 du CGI ;
- si le cessionnaire a acquitté ou s’engage à acquitter, directement ou indirectement, des dettes contractées auprès du cédant par la SCI, en précisant le cas échéant leur montant.

Ces mentions sont impératives. Nous vous recommandons de les faire figurer de manière claire et distincte dans l’acte, après vérification des faits auprès de la société et des parties.

Nous restons à votre disposition pour relire le projet d’acte et vous assister lors de la formalisation.

Bien cordialement,  
[Votre cabinet]


---

## C19  (19 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

# NOTE DE CONSULTATION

**Objet :** Holding [X] – cession de titres intervenue en février 2026 – obligation de remploi de l'article 150‑0 B ter, I, 2° du CGI
**Confidentiel – couvert par le secret professionnel**

---

## Avertissement liminaire

Cette note est établie sur la base des seuls éléments que vous m'avez communiqués oralement et du texte de l'article 150‑0 B ter, I, 2°, a. Elle devra être confirmée après examen des pièces (traité d'apport, statuts, protocole de cession, déclarations fiscales). Plusieurs points ci‑dessous appellent une vérification documentaire **avant** toute décision d'investissement.

---

## 1. Trois vérifications préalables, à faire avant toute chose

**1.1. La date exacte de l'apport.** Le délai de trois ans se décompte **de date à date**. Si l'apport a été réalisé, par exemple, le 5 février 2023 et la cession le 20 février 2026, vous êtes **hors délai** : l'événement de cession ne met pas fin au report et **aucune obligation de remploi n'existe**. Vous êtes libre de vos 9 M€. La différence entre les deux situations se chiffre ici à plus de 2 M€ d'impôt potentiel : il faut donc dater précisément l'apport (date de réalisation définitive de l'augmentation de capital, et non date de l'assemblée ou de l'évaluation) et la cession (transfert de propriété, en principe la date de l'acte de cession définitif, non celle de la promesse).

**1.2. Le montant exact du « produit de la cession ».** Les 9 M€ encaissés ne sont pas nécessairement l'assiette. Il faut vérifier :
- l'existence d'une **fraction séquestrée** au titre de la garantie d'actif et de passif (elle fait partie du prix, même non encore disponible) ;
- l'existence d'un **complément de prix / earn‑out** (il génère une obligation de remploi complémentaire lorsqu'il est perçu) ;
- l'existence d'un **crédit‑vendeur** ou d'un paiement échelonné (le délai de trois ans court néanmoins de la cession, ce qui peut créer une tension de trésorerie).

**1.3. La situation de la holding elle‑même à l'IS.** Point souvent négligé : la plus‑value réalisée par **la holding** relève du régime des plus‑values à long terme (exonération sous réserve de la quote‑part de 12 %) **uniquement si les titres étaient détenus depuis au moins deux ans**. L'apport datant de moins de trois ans, il faut s'assurer qu'il date de plus de deux ans. À défaut, la plus‑value de la holding est taxable à l'IS au taux plein — ce qui, si la valeur a progressé depuis l'apport, change l'équation de trésorerie. Vérifions également la qualification de titres de participation.

Je pars, pour la suite, de l'hypothèse que le remploi est bien obligatoire.

---

## 2. Le montant à réinvestir : 6 300 000 €, et non « une partie »

Vous me dites « réinvestir une partie ». Soyons précis, c'est le point où les dossiers se perdent :

- Le seuil est de **70 % du produit de la cession**, c'est‑à‑dire **du prix de vente brut**, et non du gain net, ni de la plus‑value, ni du solde après impôt ou après frais.
- Sur 9 000 000 €, l'obligation porte donc sur **6 300 000 €**.
- Les frais et honoraires de cession, l'impôt éventuellement dû par la holding, les remboursements de comptes courants **ne viennent pas en déduction** de cette assiette.
- Seuls **2 700 000 €** sont libres d'emploi (placements de trésorerie, immobilier patrimonial, distribution — cette dernière étant taxée entre vos mains au PFU de 30 %).

**Conséquence pratique immédiate :** ne prélevez rien, ne distribuez rien, ne prêtez rien avant d'avoir sécurisé la capacité de la holding à mobiliser 6,3 M€. Je vous recommande de **cantonner** cette somme sur un support liquide et disponible (compte à terme à échéances courtes, fonds monétaire) et de ne piloter les 2,7 M€ qu'en second rideau.

---

## 3. Le calendrier : février 2029, mais l'échéance réelle est 2028

Le remploi doit être **réalisé** dans les trois ans de la cession, soit au plus tard en **février 2029** (date à date).

Attention : il ne s'agit pas de « s'être engagé » à investir, mais d'avoir **effectivement décaissé** — signature de l'acte et paiement du prix, inscription de l'actif au bilan. Une lettre d'intention, une exclusivité, un closing différé au‑delà du terme sont sans valeur.

Sur le terrain, trois ans passent très vite : sourcing, LOI, due diligence, négociation, financement, closing représentent facilement 9 à 15 mois pour une opération de croissance externe, et l'expérience montre que la première cible échoue une fois sur deux. **Je vous recommande de fixer un objectif interne à fin 2028 au plus tard, et de procéder par tranches** plutôt que d'attendre l'opération unique et parfaite.

---

## 4. Les emplois possibles

### 4.1. Le a) que vous m'avez soumis : financement de moyens permanents d'exploitation

C'est la voie la plus exigeante. Elle suppose que **la holding exerce elle‑même une activité opérationnelle éligible** (commerciale, industrielle, artisanale, libérale, agricole ou financière) et qu'elle finance des **moyens permanents affectés à cette activité** : fonds de commerce, matériel industriel, immeuble d'exploitation utilisé par elle, actifs incorporels d'exploitation.

Sont exclus, et je vous le dis sans détour car ce sont les erreurs classiques :
- une holding purement passive, qui ne peut par définition affecter des moyens à une activité qu'elle n'exerce pas ;
- **la gestion de son propre patrimoine immobilier**, expressément écartée par le texte : l'achat d'un immeuble destiné à la location — **y compris la location à une filiale opérationnelle, y compris la location meublée** — n'est pas éligible ;
- les placements financiers, la trésorerie, les valeurs mobilières de gestion patrimoniale ;
- le remboursement d'un emprunt ou d'un compte courant.

### 4.2. Les autres branches du texte, qui sont en pratique les vraies solutions

Le texte que vous m'avez transmis est **tronqué** : l'article 150‑0 B ter, I, 2° comporte également les branches b), c) et d), qui ouvrent des options bien plus opérationnelles :

- **b) Acquisition d'une fraction du capital d'une société opérationnelle** ayant pour effet d'en **conférer le contrôle** à la holding (au sens du code de commerce). C'est le schéma classique de croissance externe. Attention : une prise de participation minoritaire, sans contrôle, n'est pas éligible sur ce fondement.
- **c) Souscription en numéraire au capital initial ou à une augmentation de capital** d'une ou plusieurs sociétés opérationnelles répondant aux conditions légales (soumises à l'IS, siège dans l'UE/EEE, activité éligible). C'est ici la voie la plus souple : elle permet notamment de **créer ou capitaliser une filiale** qui portera ensuite le projet d'exploitation. À noter : elle permet de contourner l'obstacle du a) en logeant l'exploitation dans une filiale dédiée.
- **d) Souscription de parts de FPCI, FCPR, SLP ou actions de SCR** respectant les quotas d'investissement légaux. Les sociétés de gestion commercialisent des véhicules dits « éligibles 150‑0 B ter ». L'intérêt majeur pour vous : la **souscription** doit intervenir dans les trois ans, mais les **appels de fonds** peuvent être étalés dans le temps. C'est votre **filet de sécurité de fin de délai**.

Ces quatre voies sont **cumulables** : rien n'interdit de réinvestir 4 M€ en croissance externe (b), 1,3 M€ en souscription à une filiale (c) et 1 M€ en FPCI (d).

---

## 5. La contrainte d'aval : conserver l'investissement

Le remploi ne suffit pas : les biens ou titres acquis doivent être **conservés** — au moins **douze mois** pour les actifs et titres visés aux a), b) et c) (décomptés de leur inscription à l'actif), et **cinq ans** pour les parts de fonds du d). Une revente prématurée, un apport, une fusion mal calibrée peuvent remettre en cause le report *a posteriori*. Ce point doit être intégré dans les pactes et dans la documentation de toute opération ultérieure.

---

## 6. Ce qu'il ne faut surtout pas faire

Je préfère être explicite, ces schémas sont systématiquement redressés :

1. **Réinvestir dans une société du groupe familial ou dans une coquille sans substance**, avec remontée ultérieure des fonds vers vous ou vers la holding. Le Comité de l'abus de droit fiscal et le juge ont validé de nombreux redressements sur ce terrain (art. L. 64 et L. 64 A du LPF), avec majoration de 80 %.
2. **Acheter de l'immobilier locatif**, sous quelque habillage que ce soit (SCI, SCPI, OPCI, immeuble loué à la filiale). Exclusion textuelle.
3. **Prêter les fonds à une société opérationnelle** au lieu d'entrer à son capital : un compte courant n'est ni une acquisition de titres, ni une souscription.
4. **Faire réaliser l'investissement par une filiale** avec les fonds descendus en compte courant : le remploi doit être opéré par la société bénéficiaire de l'apport elle‑même. Si le projet doit être logé dans une filiale, il faut passer par une **souscription au capital** de celle‑ci (voie c), et non par un prêt.
5. **Vous appauvrir de la trésorerie** par distribution ou rachat de titres avant d'avoir bouclé le remploi.

---

## 7. Formalisme et obligations déclaratives

Ce sont elles qui, en pratique, déclenchent le contrôle :

- La holding doit **prendre l'engagement de réinvestir**, et cet engagement doit être matérialisé (décision du président / procès‑verbal, mention dans les documents fiscaux).
- Vous devez continuer à porter le **suivi annuel de la plus‑value en report** sur votre déclaration personnelle (formulaire 2074‑I et report en 2042‑C).
- La société doit établir et conserver l'**état de suivi** prévu par les articles 74‑0 M et suivants de l'annexe II au CGI. L'omission ou l'inexactitude est sanctionnée par une amende spécifique.
- Constituez dès maintenant un **dossier de preuve** : justificatifs des flux, actes d'acquisition, business plan, éléments démontrant la réalité de l'activité et l'affectation des moyens.

---

## 8. L'enjeu chiffré en cas d'échec

Si le seuil de 70 % n'est pas atteint au terme des trois ans, le report prend fin **en totalité** — il n'existe pas de proratisation : réinvestir 65 % ne préserve pas 65 % du report, cela ne préserve rien. La plus‑value d'apport devient imposable au titre de l'année d'expiration du délai, selon les règles applicables à la date de l'apport (PFU de 12,8 % + 17,2 % de prélèvements sociaux, sans abattement pour les apports postérieurs à 2018, majoré le cas échéant de la CEHR à 3 %/4 % et, depuis 2025, de la contribution différentielle sur les hauts revenus). S'y ajoute le risque d'**intérêt de retard**.

Sur une plus‑value d'apport que j'évalue, à ce stade, dans l'ordre de grandeur de plusieurs millions d'euros, le coût du non‑respect se compte en **millions**, pour une obligation de réinvestir des sommes qui, elles, ne sortent pas de votre patrimoine mais changent seulement d'affectation. Le rapport risque/contrainte est très défavorable à l'attentisme.

---

## 9. Plan d'action que je vous propose

| Échéance | Action |
|---|---|
| Sous 15 jours | Communication du traité d'apport, du protocole de cession, des statuts et de vos deux dernières liasses. Confirmation de la date d'apport et de l'assiette exacte des 70 %. |
| Sous 1 mois | Note de cadrage chiffrée : montant exact à réinvestir, date butoir certaine, cartographie des emplois éligibles au regard de votre projet entrepreneurial. Rédaction et datation de l'engagement de remploi. |
| Sous 2 mois | Cantonnement de 6,3 M€ sur supports liquides ; définition d'une allocation cible (croissance externe / création / fonds éligibles) et d'un calendrier avec jalons trimestriels. |
| Avant fin 2027 | Réalisation de la première tranche de remploi (objectif : 60 % de l'obligation). |
| Mi‑2028 | Point de contrôle. Si l'objectif n'est pas atteint, souscription du solde en véhicule éligible d) — décision à prendre à cette date, pas plus tard. |
| Fin 2028 | Bouclage. Constitution du dossier probatoire complet. |

---

Je reste à votre disposition pour un rendez‑vous dès réception des pièces. Compte tenu de la vérification à opérer sur la date d'apport — qui peut, le cas échéant, vous libérer purement et simplement de toute contrainte — je vous suggère de me transmettre le traité d'apport en priorité, avant même les autres documents.

*[Avocat]*


---

## C20  (20 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

Cher Confrère,

Voici l'analyse que je remets à notre client concernant la cession envisagée.

**1. Qualification de la société et droit dû**

Au regard de l'article 726, I, 2° du CGI que vous nous soumettez, la société civile immobilière dont les titres sont cédés entre incontestablement dans la catégorie des **personnes morales à prépondérance immobilière**.

En effet, son actif est constitué à 80 % d'immeubles situés en France. Le seuil de prépondérance est franchi dès lors que l'actif est « principalement constitué » d'immeubles, ce que la doctrine administrative et la jurisprudence interprètent comme une proportion supérieure à 50 %. Une proportion de 80 % ne laisse place à aucune discussion.

Par conséquent, le taux applicable n'est pas le taux de droit commun de 0,1 % prévu pour les cessions de droits sociaux (CGI, art. 726, I, 1°), mais le taux spécifique de **5 %**.

Le droit d'enregistrement dû s'élève donc à :
**4 000 000 € × 5 % = 200 000 €.**

Ce droit est à la charge de l'acquéreur, sauf stipulation contractuelle contraire (CGI, art. 1711). Il devra être acquitté lors de la présentation de l'acte à l'enregistrement, dans le délai légal d'un mois à compter de la date de la cession (soit au plus tard le 20 avril 2024).

**2. Obligations formelles quant au contenu de l'acte**

L'acte de cession, qu'il soit sous seing privé ou authentique, doit impérativement respecter les prescriptions de l'article 726, III, B, afin d'éviter toute difficulté ultérieure (notamment une remise en cause par l'administration fiscale ou une insuffisance d'imposition au regard des articles 728 ou 1655 ter du CGI).

L'acte signé le 20 mars 2024 devra donc comporter une déclaration expresse du cédant et du cessionnaire indiquant :

**Point n°1 :** Si la société civile immobilière dont les parts sont cédées est une société visée à l'article 1655 ter du CGI. Il s'agit des sociétés qui ont pour objet la construction ou l'acquisition d'immeubles en vue de leur division par lots destinés à être attribués aux associés. Compte tenu de la nature courante d'une SCI patrimoniale, la réponse sera le plus souvent négative, mais la mention doit figurer (ex : « *La société n'est pas une société mentionnée à l'article 1655 ter du Code général des impôts* »).

**Point n°2 :** Si les participations cédées confèrent au cessionnaire, directement ou indirectement, le droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'article 728 du CGI. Cela vise le cas où les parts sociales donnent vocation à une attribution en propriété ou en jouissance d'un immeuble déterminé (comme dans une société d'attribution). Si ce n'est pas le cas, il faut le préciser (ex : « *Les participations cédées ne confèrent pas au cessionnaire le droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'article 728 du Code général des impôts* »).

**Point n°3 :** Si le cessionnaire a acquitté ou s'engage à acquitter des dettes contractées par la société auprès du cédant. Cette mention est essentielle pour la liquidation du droit sur la base imposable réelle, car la prise en charge d'un passif constitue un supplément de prix taxable (CGI, art. 726, IV). L'acte doit donc déclarer soit l'absence d'une telle charge (ex : « *Le cessionnaire ne s'engage pas à acquitter des dettes de la société envers le cédant* »), soit, le cas échéant, en préciser expressément le montant, lequel viendra s'ajouter au prix de 4 000 000 € pour le calcul du droit de 5 %.

Je reste à votre disposition pour toute question complémentaire, notamment sur la structuration de l'acte ou la vérification de la composition précise de l'actif social.


---

## C21  (21 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

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

## C22  (22 sur 45)

**VOTRE CODE : ______________________________**

**Fait manquant :** La date de dépôt du projet au greffe. Le régime nouveau ne s'applique qu'aux opérations dont le projet a été déposé à compter du 1er juillet 2023.

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus directement aux
associes de la societe apporteuse, afin que chaque branche de la
famille detienne sa societe.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder :**

**MÉMORANDUM DE CONSULTATION FISCALE**

**À l'attention de :** [Nom du Groupe Familial / Représentants]
**Objet :** Faisabilité fiscale de la séparation des branches d'activité (Industrie / Négoce)
**Date :** 24 mai 2024

Madame, Monsieur,

Vous m'avez consulté concernant votre projet de restructuration. Votre objectif est de séparer les deux branches de votre famille, qui détiennent actuellement une société holding exploitant deux activités distinctes (industrie et négoce). 

Le schéma envisagé consiste à apporter la branche industrielle à une société nouvelle (NewCo) et à distribuer les titres de cette NewCo directement aux associés, de manière à ce que chaque branche familiale détienne sa propre société (l'une conservant la holding avec le négoce, l'autre récupérant la NewCo avec l'industrie).

Vous vous interrogez sur l'éligibilité de cette opération au régime de faveur des fusions et apports (articles 210 A et suivants du Code Général des Impôts - CGI), en vous appuyant sur la définition de l'article 210-0 A, I, 4° du CGI.

Voici mon analyse de votre dossier.

### 1. Sur le principe : Une opération juridiquement et fiscalement prévue par les textes

Le texte que vous citez (CGI, art. 210-0 A, I, 4°) définit exactement l'opération que vous envisagez : il s'agit d'un **apport partiel d'actif (APA) avec attribution directe des titres aux associés**, souvent qualifié en pratique de « scission partielle ».

Sur le papier, **la réponse est oui** : cette opération a précisément été introduite dans la loi pour permettre ce type de restructuration en bénéficiant de la neutralité fiscale (pas d'imposition immédiate des plus-values latentes sur les actifs apportés au niveau de la société, et pas d'imposition de la distribution des titres au niveau des associés).

Cependant, dans un dossier réel de séparation familiale, la lecture de ce seul alinéa est insuffisante. L'application du régime de faveur est subordonnée à des conditions strictes qui constituent le cœur de notre travail de sécurisation.

### 2. Les conditions techniques (L'exigence de la "Branche Complète d'Activité")

Pour que le régime de faveur s'applique de plein droit (sans avoir à demander un agrément préalable à l'administration fiscale), l'article 210 B du CGI exige que :
1.  L'activité industrielle apportée à la NewCo constitue une **Branche Complète d'Activité (BCA)**.
2.  L'activité de négoce conservée par la holding constitue **également une BCA**.

*Notre première étape sera donc de réaliser un audit de ces deux activités pour nous assurer qu'elles disposent chacune de leur propre personnel, de leurs propres moyens matériels et d'une autonomie de fonctionnement totale.*

### 3. Le point d'attention majeur : Le motif de l'opération (Le risque fiscal)

C'est ici que se trouve le véritable enjeu de votre dossier. 

Pour que l'opération bénéficie du régime de faveur, l'article 210-0 A, III du CGI impose qu'elle soit justifiée par un **motif économique valable** (restructuration, rationalisation, etc.) et qu'elle n'ait pas pour objectif principal la fraude ou l'évasion fiscale.

Or, vous souhaitez réaliser une attribution *asymétrique* (non proportionnelle) des titres : la branche familiale A va recevoir 100% des titres de la NewCo (Industrie) et annuler ses titres dans la holding, tandis que la branche familiale B va conserver 100% de la holding (Négoce). 

**La position de l'administration fiscale et du Conseil d'État est très stricte sur ce point :**
La simple volonté de séparer des actionnaires (mésentente familiale, divergence patrimoniale, volonté de faire "chacun sa route") est considérée comme un motif *patrimonial* ou *actionnarial*, et **non comme un motif économique valable pour les sociétés elles-mêmes**. 

Si nous présentons l'opération à l'administration en disant "les deux branches de la famille veulent se séparer", l'administration fiscale remettra en cause le régime de faveur. Les conséquences seraient désastreuses : imposition de la plus-value sur la branche industrielle au niveau de la holding, et taxation des titres reçus comme des dividendes (revenus distribués) entre les mains des associés.

### 4. Mes recommandations pour sécuriser votre dossier

Pour que cette opération aboutisse en toute sécurité fiscale, nous devons construire le dossier non pas autour de la séparation de la famille, mais autour de **l'intérêt des entreprises**.

Voici comment nous devons procéder :

*   **Construire le "narratif" économique :** Nous devons démontrer que l'industrie et le négoce ont des besoins de développement divergents. Par exemple : l'industrie nécessite de lourds investissements (Capex) et un endettement bancaire spécifique, tandis que le négoce a besoin de flexibilité et de trésorerie à court terme. La cohabitation des deux activités dans la même structure freine leur développement respectif. La séparation des actionnaires n'est alors que la *conséquence* de cette rationalisation économique (chaque branche familiale se spécialisant dans le métier qu'elle maîtrise le mieux).
*   **La question de la mésentente :** Si la séparation est due à un conflit familial, la jurisprudence admet le motif économique *uniquement* si nous pouvons prouver que ce conflit crée un blocage institutionnel qui paralyse la gestion de la société (ex: impossibilité de voter les budgets ou d'approuver les comptes).
*   **Le recours au rescrit fiscal (Agrément) :** Compte tenu du caractère asymétrique de la distribution des titres (séparation des familles), la loi exige souvent l'obtention d'un agrément préalable de l'administration fiscale (Article 115, 2 bis du CGI) pour que les associés ne soient pas imposés sur les titres reçus. Nous devrons rédiger et déposer cette demande d'agrément en amont de l'opération.

### Conclusion

L'opération que vous visez (scission partielle) est le bon outil juridique et correspond bien au texte que vous avez identifié. Elle peut bénéficier du régime de faveur. 

Toutefois, sa mise en œuvre dans le cadre d'une séparation familiale est un exercice de "haute voltige" fiscale. La réussite du projet dépendra entièrement de notre capacité à justifier économiquement la séparation des activités industrielles et de négoce, indépendamment de vos considérations familiales.

Je vous propose de nous réunir la semaine prochaine pour auditer l'autonomie de vos deux branches d'activité (BCA) et commencer à lister les arguments économiques qui justifieront cette scission auprès de l'administration fiscale.

Je reste à votre entière disposition.

Bien confraternellement,

**[Votre Nom/Signature]**
Avocat au Barreau de [Ville]
Spécialiste en Droit Fiscal


---

## C23  (23 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**MÉMORANDUM DE CONSEIL FISCAL**

**À l'attention de :** [Nom du Client]
**Objet :** Cession des titres de la société d'exploitation par votre holding – Maintien du report d'imposition (Art. 150-0 B ter du CGI)
**Date :** [Date du jour]

Cher Monsieur,

Je fais suite à notre consultation concernant la vente récente par votre holding des titres de votre société d'exploitation. 

Vous m'avez indiqué avoir apporté ces titres à votre holding il y a moins de trois ans, et que cette dernière vient de les céder en février 2026 pour un montant de 9 000 000 d'euros. Vous bénéficiez actuellement d'un report d'imposition sur la plus-value d'apport initial, et vous souhaitez sécuriser ce report.

Voici mon analyse de votre situation et mes recommandations stratégiques.

### 1. Le principe : un réinvestissement obligatoire pour sauver le report d'imposition

Puisque votre holding a cédé les titres **moins de trois ans** après que vous les lui ayez apportés, la loi (article 150-0 B ter du CGI) prévoit que votre report d'imposition "tombe". Cela signifie que la plus-value que vous aviez mise en sommeil lors de l'apport deviendrait immédiatement taxable entre vos mains (à la flat tax de 30 % ou au barème, plus les prélèvements sociaux).

Cependant, la loi prévoit une clause de sauvegarde. Pour maintenir ce report d'imposition, votre holding doit respecter **trois conditions cumulatives** :

*   **Le montant :** Vous devez réinvestir au moins **70 % du produit de cession**, soit dans votre cas précis : **6 300 000 euros** (70 % de 9 M€).
*   **Le délai :** Ce réinvestissement doit être réalisé dans un délai de **trois ans** à compter de la cession, soit au plus tard en **février 2029**.
*   **La nature du réinvestissement :** Les fonds ne peuvent pas être investis n'importe comment (voir point 2).

*Note pratique : Les 30 % restants (soit 2 700 000 euros) sont totalement libres d'emploi. Votre holding peut les placer sur les marchés financiers, faire de l'immobilier patrimonial, ou vous les distribuer sous forme de dividendes (avec la fiscalité applicable aux dividendes).*

### 2. Que faire des 6 300 000 euros ? (Les investissements éligibles)

Le texte que vous visez (le *a* du 2° du I de l'article 150-0 B ter) impose que le réinvestissement ait une vocation **économique et opérationnelle**. L'objectif du législateur est d'irriguer l'économie réelle, pas de favoriser la gestion de patrimoine privé.

Voici les voies qui s'offrent à votre holding pour ces 6,3 M€ :

**A. L'investissement direct (celui visé par votre texte) :**
Votre holding peut utiliser ces fonds pour financer des "moyens permanents d'exploitation" affectés à une activité commerciale, industrielle, artisanale, libérale ou agricole. 
*   *Exemple :* La holding achète un fonds de commerce, des machines, ou des locaux *qu'elle va exploiter elle-même* pour une nouvelle activité.
*   *Attention - Le piège immobilier :* Le texte exclut formellement la gestion de patrimoine immobilier. Vous ne pouvez pas utiliser ces 70 % pour acheter des appartements à louer, faire du LMNP, ou investir dans des SCI de location passive. L'immobilier n'est éligible que s'il est l'outil de travail d'une activité d'exploitation (ex: achat des murs d'un hôtel que la holding exploite).

**B. Les autres voies d'investissement (pour aller plus loin) :**
En tant qu'avocat, je me dois de vous préciser que la loi offre d'autres options si votre holding ne souhaite pas exploiter une activité en direct :
*   **Prise de participation :** Vous pouvez souscrire au capital initial ou à l'augmentation de capital d'une ou plusieurs sociétés (PME) opérationnelles. Votre holding devra en acquérir le contrôle (ou l'avoir déjà).
*   **Fonds d'investissement :** Si vous ne souhaitez pas gérer d'entreprises, vous pouvez confier ces 6,3 M€ à des fonds de capital-investissement (FCPR, FPCI, etc.) éligibles au dispositif 150-0 B ter, qui se chargeront d'investir dans des PME pour vous. C'est une solution très prisée pour déléguer le risque et la gestion.

### 3. Mes recommandations et les prochaines étapes

L'argent "dort" actuellement sur le compte de la holding. Voici votre plan d'action :

1.  **L'urgence déclarative (L'engagement formel) :** Lors du dépôt de la liasse fiscale de votre holding pour l'exercice clos en 2026 (généralement en mai 2027), nous devrons impérativement joindre une attestation par laquelle la société **s'engage formellement** à réinvestir les 70 % dans le délai de 3 ans. *Si nous oublions cette case, le report d'imposition est perdu, même si vous réinvestissez plus tard.*
2.  **Ne vous précipitez pas, mais anticipez :** Vous avez jusqu'en février 2029. C'est à la fois long et court. Si vous optez pour le rachat d'une entreprise ou la création d'une nouvelle activité, les audits et les négociations prennent des mois. 
3.  **Gestion de la trésorerie d'attente :** En attendant de trouver le bon réinvestissement, les 9 M€ peuvent être placés sur des supports financiers classiques (comptes à terme, OPCVM) par la holding. La loi n'interdit pas de faire fructifier l'argent pendant le délai de 3 ans.

**En conclusion :**
Je vous propose que nous nous réunissions prochainement pour définir votre profil d'investisseur pour les années à venir. Souhaitez-vous redevenir chef d'entreprise (investissement direct/prise de participation) ou préférez-vous un rôle d'investisseur passif (fonds de Private Equity) ? Une fois ce choix fait, mon cabinet vous accompagnera pour valider l'éligibilité stricte de chaque euro dépensé afin de blinder votre situation vis-à-vis de l'administration fiscale.

Je reste à votre entière disposition.

Bien à vous,

**Votre Avocat Fiscaliste**


---

## C24  (24 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

En votre qualité d’avocat fiscaliste, vous trouverez ci-dessous une analyse structurée de la situation, suivie de ma conclusion.

### 1. Rappel du principe : retenue à la source de l’article 119 bis, 2 du CGI

L’article 119 bis, 2, premier alinéa du CGI, dans sa version applicable au 15 juin 2025, soumet à une retenue à la source les produits visés aux articles 108 à 117 bis (notamment les dividendes) lorsque leur bénéficiaire effectif n’a pas son domicile fiscal ou son siège en France.

En l’espèce, la distribution envisagée par la société française constitue un dividende au sens de l’article 109 du CGI. La société mère luxembourgeoise, bénéficiaire effectif, a son siège au Luxembourg. Dès lors, en application du seul article 119 bis, 2, cette distribution serait en principe passible de la retenue à la source au taux de droit commun (12,8 % ou 25 % selon les cas, sauf application d’un taux réduit conventionnel).

### 2. Exonération spécifique : le régime mère-fille de l’article 119 ter du CGI

L’article 119 ter du CGI, qui transpose la directive européenne « mère-fille » (2011/96/UE), prévoit une exonération totale de retenue à la source pour les dividendes distribués par une société française à une société mère établie dans un autre État membre de l’Union européenne (ou dans un État lié par une convention d’assistance administrative), sous réserve du respect de plusieurs conditions cumulatives.

En l’espèce, les conditions sont manifestement remplies :

- **Détention du capital** : la société mère luxembourgeoise détient 100 % du capital de la filiale française depuis cinq ans, soit une durée bien supérieure au seuil de deux ans exigé.
- **Pourcentage de détention** : 100 %, soit largement au-delà du minimum de 10 % requis.
- **Forme sociale et assujettissement** : la société mère est une société anonyme de droit luxembourgeois, soumise à l’impôt sur les sociétés luxembourgeois. Elle entre donc dans le champ des sociétés mères éligibles visées par la directive et par l’article 119 ter.
- **Bénéficiaire effectif** : rien dans les informations fournies ne permet de douter que la société luxembourgeoise soit le bénéficiaire effectif des dividendes, condition également requise.

Dès lors, la distribution de 20 000 000 € mise en paiement le 15 juin 2025 entre pleinement dans le champ de l’exonération prévue par l’article 119 ter du CGI.

### 3. Articulation avec la convention fiscale franco-luxembourgeoise

La convention fiscale entre la France et le Luxembourg prévoit, en son article 10, une imposition partagée des dividendes avec un taux maximal de retenue à la source en France de 5 % lorsque le bénéficiaire détient au moins 10 % du capital de la société distributrice. Toutefois, cette disposition conventionnelle ne trouve à s’appliquer que si le droit interne français ne prévoit pas un régime plus favorable. Or, l’article 119 ter du CGI instaure une exonération totale, plus favorable que le taux réduit conventionnel. C’est donc ce régime interne, conforme au droit de l’Union européenne, qui s’applique en priorité.

### 4. Conclusion

**Aucune retenue à la source ne sera due** sur la distribution de 20 000 000 € mise en paiement le 15 juin 2025 par la société française au profit de sa société mère luxembourgeoise, sous réserve que cette dernière soit bien le bénéficiaire effectif des dividendes et qu’elle fournisse à la société distributrice les justificatifs requis (attestation de résidence fiscale, preuve de la détention et de la durée de détention, etc.) avant la mise en paiement, conformément aux obligations déclaratives prévues par l’article 119 ter et la doctrine administrative.

Je vous invite à formaliser cette documentation en amont de l’échéance afin de sécuriser l’opération.


---

## C25  (25 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Cabinet d'Avocats - Pôle Droit Fiscal**
**Note de Consultation**

**À l'attention de :** [Nom du Client]
**Objet :** Sauvegarde du report d'imposition suite à la cession de titres par la holding (CGI art. 150-0 B ter)
**Date :** [Date du jour]

---

### I. Rappel des faits et enjeu fiscal

Vous m'avez consulté au sujet de la cession intervenue en février 2026 par votre holding (que vous contrôlez à 100 %) des titres d'une société d'exploitation. 
Ces titres vous avaient été préalablement apportés à la holding, moins de trois ans avant la cession. Le produit de cette vente s'élève à 9 000 000 € et se trouve actuellement sur le compte courant de la holding.

**L'enjeu :** En principe, la cession des titres par la holding dans un délai de trois ans à compter de votre apport constitue un événement qui met fin au report d'imposition dont vous aviez bénéficié lors de l'apport. Cela entraînerait l'imposition immédiate de la plus-value d'apport à votre niveau (personne physique).

### II. Analyse juridique : L'exception de sauvegarde du report

L'article 150-0 B ter, I, 2° du Code Général des Impôts (CGI) prévoit une exception permettant de ne pas rompre le report d'imposition. Cette exception est subordonnée à la prise d'un engagement de réinvestissement par la holding.

En l'espèce, pour neutraliser la taxation de votre plus-value d'apport, votre holding doit respecter strictement les conditions cumulatives suivantes :

**1. Le délai de réinvestissement**
La holding dispose d'un délai de **trois ans à compter de la date de la cession** (février 2026) pour réaliser les investissements requis. Le point de départ du chronomètre est la cession par la holding, et non votre apport initial.

**2. Le seuil de réinvestissement**
La holding doit investir **au moins 70 % du montant du produit de la cession**. 
Sur un produit total de 9 000 000 €, le montant minimum à réinvestir est donc de :
*9 000 000 € x 70 % = **6 300 000 €***

**3. La nature de l'investissement**
C'est le point le plus critique. Les fonds ne doivent pas "dormir". Ils doivent être affectés au "financement de moyens permanents d'exploitation affectés à l'activité" de la holding. 
Deux précisions majeures découlent du texte :
*   **L'activité éligible :** L'activité de la holding doit correspondre à une activité opérationnelle (commerciale, industrielle, artisanale, libérale ou agricole) au sens de l'article 199 terdecies-0 A du CGI. Une simple activité de holding animatrice peut être admie sous strictes conditions, mais une holding purement passive ne remplit pas les critères.
*   **L'exclusion immobilière :** Le texte exclut explicitement "les activités de gestion de son propre patrimoine immobilier". La holding ne peut donc pas utiliser ces 6,3 millions d'euros pour acheter des murs ou des locaux qu'elle louerait de manière passive.

### III. Recommandations et plan d'action

Afin de sécuriser votre situation et de conserver le bénéfice du report d'imposition, je vous préconise les actions suivantes :

**1. Définir une stratégie d'investissement éligible (dans les 3 ans)**
Le réinvestissement de 6 300 000 € doit être pensé en cohérence avec l'objet social de votre holding. Voici quelques pistes éligibles :
*   **Acquisition d'une branche d'activité ou d'un fonds de commerce :** Permet à la holding de développer une activité économique réelle.
*   **Prise de participation dans une ou plusieurs sociétés opérationnelles :** Sous réserve que la holding exerce une fonction d'animation de son groupe (holding animatrice), ce qui nécessite de renforcer son objet social et ses moyens humains si ce n'est pas déjà le cas.
*   **Investissements corporels ou incorporels :** Achat de matériel, de brevets, de licences, ou financement de dépenses de R&D, directement affectés à une activité exercée par la holding.

**2. Gestion du solde (2 700 000 €)**
Les 30 % restants (soit 2,7 M€) ne sont pas soumis à l'obligation de réinvestissement. Ils pourront être distribués sous forme de dividendes (soumis à la Flat Tax) ou conservés en trésorerie à votre convenance.

**3. Obligations déclaratives**
L'engagement de réinvestissement n'est pas qu'une intention ; il doit être formalisé. La holding devra joindre à sa déclaration de résultats (liasse fiscale) de l'année de la cession (exercice clos en 2026) l'engagement formel d'investir 70 % du produit de cession dans les conditions prévues par la loi. Nous devrons préparer ce document ensemble avant le dépôt de la liasse.

### IV. Conclusion

Votre intuition était bonne : laisser les fonds dormir sur le compte bancaire entraînera inéluctablement la taxation de votre plus-value d'apport. 

Il est impératif que votre holding affecte au moins **6 300 000 €** au financement de moyens permanents d'exploitation **avant février 2029**, en excluant tout investissement de nature immobilière passive. 

Je vous propose que nous organisions une réunion de travail dans les prochaines semaines pour examiner l'objet social actuel de votre holding et valider la nature des opérations d'investissement que vous envisagez, afin de garantir leur conformité à l'article 150-0 B ter du CGI.

Je reste à votre entière disposition pour toute précision.

Cabinet d'Avocats  
*Signature*


---

## C26  (26 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Objet : Conseil en matière de report d’imposition – Article 150-0 B ter du CGI**

**Cher Client,**

Je vous remercie pour les informations transmises concernant la cession des titres de votre société d’exploitation par votre holding, intervenue en février 2026, soit moins de trois ans après leur apport. Comme vous le soulignez, cette opération déclenche en principe la fin du report d’imposition prévu à l’article 150-0 B ter du CGI. Toutefois, le législateur a prévu une dérogation permettant de maintenir ce report sous certaines conditions, que nous allons examiner ensemble.

### **1. Rappel du cadre juridique**
L’article 150-0 B ter, I, 2° du CGI prévoit que le report d’imposition prend fin en cas de cession des titres apportés dans un délai de trois ans, **sauf si** la holding s’engage à réinvestir au moins **70 % du produit de la cession** dans des **moyens permanents d’exploitation** affectés à une activité éligible, et ce **dans un délai de trois ans** à compter de la cession.

### **2. Conditions à respecter pour bénéficier de la dérogation**
Pour conserver le bénéfice du report, votre holding doit :
- **Prendre un engagement de réinvestissement** dans les **trois ans** suivant la cession (soit avant février 2029).
- **Réinvestir au moins 70 % du produit de cession** (soit **6 300 000 €** sur les 9 000 000 € perçus).
- **Investir dans des moyens permanents d’exploitation** affectés à une activité éligible (cf. article 199 terdecies-0 A, I-C-3° du CGI), à l’exclusion :
  - Des activités de **gestion de patrimoine immobilier** (location nue, etc.).
  - Des activités financières ou de holding pure (sauf si la holding exerce une activité opérationnelle).

### **3. Modalités pratiques du réinvestissement**
#### **a) Nature des investissements éligibles**
Les **moyens permanents d’exploitation** peuvent inclure :
- **Investissements corporels** : machines, équipements, outils industriels, véhicules professionnels, etc.
- **Investissements incorporels** : brevets, logiciels, fonds de commerce, droits au bail (sous conditions).
- **Participations dans des sociétés opérationnelles** (sous réserve que ces sociétés exercent une activité éligible et que la holding y participe activement).
- **Financement de l’activité** : augmentation de capital d’une filiale opérationnelle, prêt participatif à une société du groupe (si justifié par l’activité).

⚠️ **Exclusions** :
- Les placements financiers (comptes à terme, obligations, actions cotées sans lien avec l’activité).
- Les acquisitions immobilières (sauf si directement liées à l’activité, ex. : usine, entrepôt logistique).
- Les rachats de parts sociales dans le cadre d’une transmission familiale (sauf si justifiés par un projet économique).

#### **b) Formalités à accomplir**
1. **Engagement de réinvestissement** :
   - Votre holding doit **prendre un engagement formel** dans sa déclaration de revenus (ou via un document annexe) précisant :
     - Le montant à réinvestir (au moins 6 300 000 €).
     - La nature des investissements prévus.
     - Le délai de réalisation (avant février 2029).
   - Cet engagement doit être **joint à la déclaration de revenus de l’année de la cession** (2026).

2. **Justification du réinvestissement** :
   - À l’issue du délai de trois ans, votre holding devra **prouver** que les fonds ont bien été réinvestis dans des actifs éligibles (factures, contrats, actes notariés, etc.).
   - En cas de contrôle fiscal, l’administration vérifiera la **cohérence économique** des investissements (lien avec l’activité, caractère "permanent", etc.).

3. **Sanctions en cas de non-respect** :
   - Si le réinvestissement n’est pas réalisé dans les délais ou si les fonds sont utilisés à des fins non éligibles, le report d’imposition sera **remis en cause** et les plus-values seront imposables au titre de l’année de la cession (2026), avec application des **pénalités de retard** (0,20 % par mois) et des **intérêts de retard** (0,20 % par mois).

### **4. Stratégies de réinvestissement recommandées**
Compte tenu des enjeux, je vous propose d’étudier les options suivantes, classées par ordre de sécurité juridique :

#### **Option 1 : Réinvestissement dans une activité opérationnelle existante ou nouvelle**
- **Exemple** :
  - Acquisition de machines ou d’équipements pour une filiale industrielle.
  - Rachat d’un fonds de commerce ou d’une société opérationnelle (ex. : sous-traitant, fournisseur stratégique).
  - Financement d’un projet R&D ou d’une innovation technologique.
- **Avantages** :
  - Sécurité juridique élevée si l’investissement est directement lié à l’activité.
  - Possibilité de structurer l’opération via une augmentation de capital ou un prêt participatif.

#### **Option 2 : Création d’une nouvelle activité éligible**
- **Exemple** :
  - Lancement d’une nouvelle branche d’activité (ex. : transition énergétique, digitalisation).
  - Acquisition d’une start-up ou d’une PME innovante (sous réserve de son éligibilité).
- **Avantages** :
  - Diversification du groupe.
  - Possibilité de bénéficier d’autres dispositifs fiscaux (ex. : CIR, CICE).
- **Risques** :
  - Nécessité de démontrer le caractère "permanent" de l’investissement (éviter les projets spéculatifs).

#### **Option 3 : Réinvestissement dans l’immobilier d’exploitation**
- **Exemple** :
  - Acquisition d’un entrepôt logistique, d’une usine, ou de bureaux dédiés à l’activité.
- **Conditions** :
  - L’immobilier doit être **affecté à l’exploitation** (pas de location nue).
  - Risque de requalification en gestion de patrimoine si l’usage n’est pas clairement opérationnel.

⚠️ **À éviter** :
- Les placements financiers (comptes à terme, actions cotées sans lien avec l’activité).
- Les acquisitions immobilières locatives (sauf si liées à l’activité, ex. : hôtel, résidence étudiante exploitée).

### **5. Calendrier et prochaines étapes**
| Étape | Délai | Actions |
|--------|--------|---------|
| **Cession des titres** | Février 2026 | - |
| **Engagement de réinvestissement** | Déclaration 2026 (mai/juin 2027) | Prise d’engagement dans la déclaration fiscale. |
| **Réinvestissement effectif** | Avant février 2029 | Réalisation des investissements éligibles. |
| **Justification auprès de l’administration** | Déclaration 2029 | Production des preuves de réinvestissement. |

### **6. Recommandations complémentaires**
- **Audit des investissements envisagés** :
  Je vous propose de m’envoyer une liste des projets de réinvestissement envisagés afin que je puisse les analyser au regard des critères fiscaux (éligibilité, caractère permanent, etc.).

- **Sécurisation juridique** :
  - En cas de doute sur l’éligibilité d’un investissement, il est possible de solliciter un **rescrit fiscal** auprès de l’administration pour obtenir une confirmation écrite.
  - Pour les montants importants, une **due diligence** (audit juridique et fiscal) peut être utile.

- **Optimisation fiscale** :
  - Si votre holding a des filiales à l’étranger, nous pourrions étudier des schémas de réinvestissement transfrontaliers (sous réserve des règles anti-abus).
  - En cas de réinvestissement dans une PME, vérifiez l’éligibilité aux dispositifs de réduction d’ISF/IFI (ex. : article 885-0 V bis du CGI).

- **Gestion de la trésorerie** :
  - Les 9 000 000 € doivent rester **disponibles** pour le réinvestissement. Évitez les placements bloqués ou risqués.
  - Une partie des fonds pourrait être placée en **obligations d’État ou comptes à terme** (sans risque de requalification si les fonds restent disponibles).

### **7. Risques en cas de non-respect des conditions**
Si votre holding ne respecte pas les conditions de réinvestissement :
- **Imposition immédiate** de la plus-value en 2026 (taux de 30 % : 12,8 % d’IR + 17,2 % de prélèvements sociaux, ou 0 % si exonération en cas de départ à la retraite sous conditions).
- **Pénalités** :
  - Intérêts de retard (0,20 % par mois).
  - Majorations pour manquement délibéré (40 %) en cas de dissimulation.

### **8. Conclusion et proposition d’accompagnement**
Pour sécuriser votre situation, je vous recommande de :
1. **Prendre l’engagement de réinvestissement** dans votre déclaration 2026.
2. **Identifier dès maintenant** des projets d’investissement éligibles (nous pouvons en discuter lors d’un prochain rendez-vous).
3. **Me transmettre** les projets envisagés pour validation juridique et fiscale.

Je reste à votre disposition pour :
- Vous assister dans la rédaction de l’engagement de réinvestissement.
- Analyser les projets d’investissement que vous envisagez.
- Vous accompagner en cas de contrôle fiscal ultérieur.

N’hésitez pas à me faire part de vos questions ou à me communiquer des éléments complémentaires pour affiner cette analyse.

**Bien cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées du cabinet]


---

## C27  (27 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Objet : Applicabilité de l'exonération partielle de l'article 787 B du CGI (Pacte Dutreil) à la donation projetée**

Cher Client, Maître,

Vous me consultez, en présence de votre notaire, sur l'opportunité et la validité de l'application du régime de faveur dit "Pacte Dutreil" (article 787 B du Code général des impôts) à la donation en pleine propriété des titres de votre SAS, prévue le 25 octobre 2023.

Vous m'indiquez que la société détient quarante appartements meublés, pour une valeur globale des titres de 20 millions d'euros. Un engagement collectif de conservation (OCC) a été signé le 3 mars 2021 et les enfants prendront les engagements individuels, tandis que vous conserverez la présidence.

Après examen de la situation au regard du texte en vigueur à la date de la donation, **ma conclusion est qu'à ce stade, l'exonération de 75 % prévue par l'article 787 B du CGI n'est pas applicable**, sauf si des éléments factuels non mentionnés dans votre exposé viennent modifier la qualification de l'activité de la société.

Voici mon analyse juridique et fiscale :

### 1. L'exclusion de principe des sociétés patrimoniales
Le deuxième alinéa du texte que vous m'avez transmis est sans équivoque : *"n'est pas considérée comme une activité industrielle, commerciale, artisanale, agricole ou libérale l'exercice par une société d'une activité de gestion de son propre patrimoine mobilier ou immobilier."*

La SAS que vous dirigez a pour objet et pour activité principale la détention et la gestion de 40 appartements. Il s'agit donc typiquement d'une société de gestion de son propre patrimoine immobilier. Par conséquent, en l'état, elle est expressément exclue du champ d'application de l'exonération de l'article 787 B.

### 2. La location meublée : une activité commerciale fiscalement, mais patrimoniale pour le Dutreil
Il est exact que la location meublée constitue une activité commerciale au sens des articles 34 et 35 du CGI. Toutefois, la jurisprudence du Conseil d'État (notamment CE, 8e et 3e ch., 6 juillet 2022, n° 449718) et la doctrine administrative (BOFiP) sont constantes : pour l'application du seul article 787 B, une société dont l'activité se limite à la location d'immeubles nus ou meublés est réputée exercer une activité de gestion de son propre patrimoine immobilier, et ce quelle que soit l'importance du patrimoine (40 appartements en l'espèce).

### 3. L'exception des services para-hôteliers
La seule manière de requalifier l'activité de location meublée en véritable activité commerciale ouvrant droit au bénéfice de l'article 787 B est de démontrer que la société fournit des **services para-hôteliers** significatifs (accueil, petit-déjeuner, fourniture du linge de maison, nettoyage régulier des locaux, etc.), à l'instar d'un hôtelier. 

Si la SAS se contente de louer des appartements meublés sans fournir ces services annexes de manière substantielle, l'activité reste patrimoniale.

### 4. L'exception des sociétés holdings animatrices
Le troisième alinéa du texte prévoit une tolérance pour les sociétés qui gèrent un portefeuille de participations et animent un groupe de filiales exerçant une activité opérationnelle. Cette exception est inopérante en l'espèce, puisque votre société détient directement des immeubles et non des titres de filiales opérationnelles.

### Conclusion et recommandations

Maître, le formalisme du Pacte Dutreil (OCC signé en 2021, engagements individuels des enfants, maintien à la présidence pendant 3 ans) est parfaitement respecté. Cependant, **le fondement même de l'exonération fait défaut** : la société ne remplit pas la condition d'activité éligible.

Si l'administration fiscale venait à contrôler cette donation, elle réintégrerait la totalité de la valeur des titres dans l'assiette des droits de mutation à titre gratuit, entraînant un redressement lourd (les droits étant calculés sur 20 millions d'euros, soit environ 5,4 millions d'euros de droits après abattement de 100 000 € par enfant, au lieu de 1,35 million si l'exonération de 75 % s'appliquait).

**Mes recommandations sont les suivantes :**

1. **Vérification des services rendus :** Il est impératif que nous examinions ensemble les baux et les contrats de gestion. Si la société fournit effectivement des services para-hôteliers assimilables à ceux d'un hôtel, nous pourrons constituer un dossier de qualification d'activité commerciale pour défendre l'application de l'article 787 B.
2. **Absence de services para-hôteliers :** Si l'activité est purement de la location meublée "classique", je vous déconseille formellement de tenter l'application de l'article 787 B. Dans ce cas, il conviendra d'envisager d'autres stratégies d'optimisation de la transmission (donation avec réserve d'usufruit, donation en démembrement, ou utilisation des abattements classiques de 100 000 € par enfant, renouvelables tous les 15 ans).

Je reste à votre entière disposition, ainsi qu'à celle de votre notaire, pour en débattre lors d'un rendez-vous afin de sécuriser cette opération au mieux des intérêts de votre famille.

Je vous prie d'agréer, Cher Client, Maître, l'expression de mes salutations distinguées.

**[Votre Nom]**
*Avocat à la Cour, Spécialiste en Droit Fiscal*


---

## C28  (28 sur 45)

**VOTRE CODE : ______________________________**

**Fait manquant :** La date de dépôt du projet au greffe. Le régime nouveau ne s'applique qu'aux opérations dont le projet a été déposé à compter du 1er juillet 2023.

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus directement aux
associes de la societe apporteuse, afin que chaque branche de la
famille detienne sa societe.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder :**

Bonjour, merci de me consulter sur ce dossier.

Pour déterminer si l'opération envisagée par votre groupe familial peut bénéficier du régime de faveur des articles 210 A et suivants du Code Général des Impôts (CGI), il est essentiel d'analyser les conditions prévues par ces dispositions, notamment celles relatives aux apports partiels d'actifs.

L'article 210-0 A, I, 4° du CGI précise que les apports partiels d'actifs peuvent bénéficier du régime de faveur lorsqu'une société apporte, sans être dissoute, l'ensemble ou une ou plusieurs branches complètes de son activité à une ou plusieurs sociétés, en recevant en contrepartie des titres représentatifs du capital social de la société bénéficiaire de l'apport. Ces titres peuvent être remis soit à la société apporteuse, soit directement aux associés de la société apporteuse.

Dans votre cas, la société holding envisage d'apporter sa branche industrielle à une nouvelle société et de recevoir en contrepartie des titres de cette dernière, qui seront ensuite remis directement aux associés de la société holding. 

L'opération que vous envisagez semble correspondre aux conditions prévues par l'article 210-0 A, I, 4° du CGI. En effet, il s'agit d'un apport partiel d'actif puisque la société holding n'est pas dissoute et qu'elle apporte une branche complète de son activité (l'activité industrielle) à une nouvelle société. De plus, la contrepartie de cet apport sera constituée de titres représentatifs du capital de la société bénéficiaire (la nouvelle société créée pour recevoir la branche industrielle), et ces titres seront remis directement aux associés de la société apporteuse (la société holding).

Ainsi, sous réserve de vérifier que les autres conditions du régime de faveur sont remplies (notamment que l'apport concerne une branche complète d'activité et que les autres exigences administratives et fiscales sont respectées), l'opération que vous projetez devrait pouvoir bénéficier du régime de faveur des articles 210 A et suivants du CGI.

Il conviendra néanmoins de s'assurer que la qualification de "branche complète d'activité" pour l'activité industrielle apportée est reconnue par l'administration fiscale, ce qui nécessitera probablement une consultation ou une notification préalable à l'administration fiscale pour obtenir son accord sur le caractère éligible de l'opération au régime de faveur.

Je vous recommande donc de réunir toutes les informations nécessaires pour justifier que l'activité industrielle constitue bien une branche complète d'activité et de préparer un dossier solide pour une éventuelle demande de rescrit ou pour l'accomplissement des formalités nécessaires à l'application du régime de faveur.

N'hésitez pas à me solliciter pour toute question complémentaire ou pour avancer sur les étapes suivantes de cette opération.


---

## C29  (29 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**NOTE DE CONSULTATION – Cession de parts de SCI**

---

## 1. Qualification : société à prépondérance immobilière

La SCI ciblée remplit les conditions du CGI, art. 726, I, 2° :

- ses droits sociaux ne sont pas négociés sur un marché réglementé ni sur un SMN ;
- son actif est **principalement** constitué d'immeubles situés en France : 80 %, soit très au-delà du seuil de 50 % retenu par l'administration pour caractériser la prépondérance.

⚠️ **Point de vigilance avant signature** : le texte vise l'actif tel qu'il est **à la date de cession ou au cours de l'année la précédant**. Il convient donc de vérifier la composition de l'actif sur les douze derniers mois (notamment si des immeubles ont été vendus ou des liquidités accumulées récemment). Si, à un moment de l'année précédant le 20 mars 2024, l'actif a été principalement immobilier, le tarif de 5 % s'applique. À documenter dans le dossier (bilan, inventaire, évaluation).

---

## 2. Droit d'enregistrement dû

**Taux : 5 %** (au lieu du taux de 0,1 % applicable aux actions ou du taux de 3 % avec abattement applicable aux parts sociales de sociétés non immobilières — **aucun abattement n'est admis ici**).

**Base : le prix stipulé dans l'acte, augmenté des charges**, notamment de toute prise en charge, directe ou indirecte, par l'acquéreur de dettes de la société envers le cédant.

**Calcul (hors prise en charge de dettes) :**

| Assiette | Taux | Droit |
|---|---|---|
| 4 000 000 € | 5 % | **200 000 €** |

Toute somme payée ou mise à la charge de l'acquéreur au titre des dettes contractées par la SCI auprès de votre client **s'ajouterait à l'assiette**.

**Débiteur :** l'acquéreur (cessionnaire), dans la pratique — les parties étant solidaires à l'égard de l'administration.

**Formalité :** l'acte doit être enregistré **dans le délai d'un mois** de sa signature, soit au plus tard le **20 avril 2024**, auprès du service des impôts compétent (ou par le notaire s'il s'agit d'un acte authentique). Paiement du droit lors de l'enregistrement.

---

## 3. Contenu obligatoire de l'acte (CGI, art. 726, III, B)

L'acte de cession doit indiquer **expressément** :

1. **Si la société est une société mentionnée à l'article 1655 ter** — ici **oui** : il s'agit d'une société civile ; l'acte doit le constater expressément ;
2. **Si les participations cédées confèrent au cessionnaire, directement ou indirectement, le droit à la jouissance d'immeubles ou de fractions d'immeubles** au sens de l'article 728 (typiquement : SCI d'attribution ou parts donnant jouissance d'un logement) — la mention est obligatoire dans un sens comme dans l'autre ;
3. **Si le cessionnaire a acquitté ou s'engage à acquitter, directement ou indirectement, des dettes contractées auprès du cédant par la société**, en précisant, le cas échéant, **leur montant** — mention à rédiger avec le plus grand soin, car elle conditionne l'assiette : à défaut de mention ou en cas de mention inexacte, l'administration est fondée à réintégrer ces dettes dans la base taxable et à redresser.

Outre ces mentions légales, l'acte devra naturellement identifier la société (dénomination, siège, RCS), les parties, le nombre et la numérotation des parts cédées, le prix et ses modalités de paiement.

---

## 4. Recommandations pratiques

- **Faire figurer les trois mentions du III, B** de manière expresse et non ambiguë — leur omission expose à un redressement sur l'assiette et à des difficultés lors de l'enregistrement ;
- **Chiffrer et distinguer clairement** dans l'acte le prix des parts d'une éventuelle cession ou remboursement de compte courant d'associé (si votre client détient un compte courant, sa cession ou son remboursement par l'acquéreur entre dans l'assiette du droit de 5 %) ;
- **Anticiper le délai d'un mois** pour l'enregistrement (20 avril 2024 au plus tard) ;
- À titre subsidiaire : si la cession devait être réalisée **à l'étranger**, l'acte devrait obligatoirement être reçu **en la forme authentique par un notaire exerçant en France** dans le délai d'un mois (art. 726, III, A) — signature en France recommandée.

**En synthèse : droit de 5 %, soit 200 000 € sur le seul prix, payé par l'acquéreur lors de l'enregistrement dans le mois, et acte comportant les trois mentions expresses de l'article 726, III, B.**

Je reste à votre disposition pour assister à la rédaction de l'acte et vérifier l'historique de la composition de l'actif sur l'année écoulée.


---

## C30  (30 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Cabinet d'Avocats - Pôle Droit Fiscal**
**À l'attention de Maître [Nom du Notaire] et de Monsieur [Nom du Client]**
**Objet :** Applicabilité de l'article 787 B CGI à la donation projetée du 25 octobre 2023.

Messieurs,

J'ai bien reçu votre consultation concernant la donation par_parts égales et en pleine propriété des titres de votre SAS, dont la valeur est évaluée à 20 000 000 euros. 

Vous me demandez de me prononcer sur l'applicabilité de l'exonération partielle de droits de mutation à titre gratuit prévue par l'article 787 B du Code général des impôts (CGI), étant précisé qu'un engagement collectif de conservation a été signé le 3 mars 2021 et que les conditions de gestion et d'engagement individuel des enfants semblent respectées.

Après examen approfondi de la situation à la lumière du texte applicable au jour de la donation, **ma conclusion est malheureusement négative : l'exonération de l'article 787 B ne sera pas applicable en l'état.**

Voici mon analyse détaillée et les recommandations que je vous formule.

### 1. Analyse juridique : L'exclusion de l'activité de gestion patrimoniale

Le premier alinéa de l'article 787 B du CGI conditionne l'exonération à la nature de l'activité principale de la société dont les titres sont transmis. L'activité doit être industrielle, commerciale, artisanale, agricole ou libérale.

Le deuxième alinéa du texte que vous m'avez transmis est, en l'espèce, rédhibitoire : 
*"n'est pas considérée comme une activité industrielle, commerciale, artisanale, agricole ou libérale l'exercice par une société d'une activité de gestion de son propre patrimoine mobilier ou immobilier."*

En l'occurrence, la société objet de la donation possède quarante appartements meublés. L'administration fiscale et la jurisprudence considèrent de manière constante que la location d'immeubles nus ou meublés, même si elle revêt un caractère commercial au sens de l'article 34 du CGI, constitue une activité de gestion de patrimoine immobilier. Dès lors que la société ne réalise pas d'autres activités opérationnelles significatives, elle ne peut pas bénéficier du statut de société opérationnelle requis par le premier alinéa de l'article 787 B.

### 2. Sur l'exception inapplicable de la société holding animatrice

Le troisième alinéa du texte prévoit une exception pour les sociétés holding : une société de gestion de portefeuille est considérée comme exerçant une activité commerciale si elle *« a pour activité principale la participation active à la conduite de la politique de son groupe [...] »*.

Cette exception ne peut malheureusement pas trouver à s'appliquer ici. La SAS de votre client n'est pas une holding animatrice. Elle détient en direct un patrimoine immobilier (40 appartements meublés) et n'anime pas un groupe de sociétés exerçant des activités industrielles, commerciales, artisanales, agricoles ou libérales. 

### 3. Conséquences sur le pacte Dutreil en cours

Les formalités que vous avez mises en place sont parfaitement respectées sur le papier :
- L'engagement collectif de conservation signé le 3 mars 2021 porte bien sur la totalité des droits et est en cours (la condition de durée minimale de 2 ans avant la donation est donc remplie) ;
- Chaque enfant prend l'engagement individuel de conservation pour 4 ans ;
- Le dirigeant conserve la présidence pour 3 ans.

**Cependant, ces engagements sont juridiquement inefficaces sur le plan fiscal.** La condition *sine qua non* de l'activité de la société ( activité éligible ou holding animatrice) est une condition de fond qui s'apprécie à la date de la transmission. L'engagement collectif, même s'il a été formellement souscrit et enregistré, ne peut pas produire d'effet exonératoire si l'activité de la société ne relève pas des catégories éligibles par l'article 787 B. L'administration fiscale rejettera donc la demande d'exonération lors du dépôt de la déclaration de mutation (formulaire 2744).

### 4. Conséquences fiscales de la donation du 25 octobre 2023

En l'absence d'exonération 787 B, la donation de la pleine propriété des titres d'une valeur de 20 000 000 euros aux deux enfants sera pleinement taxée aux droits de mutation à titre gratuit.

- Abattement personnel en ligne directe : 100 000 € par enfant (soit 200 000 € au total).
- Base imposable globale : 19 800 000 €.
- Tranche marginale d'imposition (au-delà de 1 805 677 €) : 45 %.
- Les droits s'élèveront approximativement à **8 910 000 euros**.

### 5. Recommandations et pistes de restructuration

La situation actuelle entraîne une lourde fiscalité. Si la donation doit absolument être signée le 25 octobre 2023, je vous recommande d'explorer d'urgence les pistes suivantes avec votre client :

1. **Restructuration préalable de l'activité :** Si une partie de la location meublée s'apparente à de la para-hôtellerie (services parahôteliers significatifs : accueil, petit-déjeuner, entretien quotidien linéaire), il pourrait être possible de requalifier l'activité en véritable activité commerciale. Toutefois, avec 40 appartements, le risque est que l'administration y voie toujours une activité patrimoniale.
2. **Mise en place d'une holding animatrice :** Si le client a d'autres activités opérationnelles (ou si une réorganisation permet d'en créer), une structure holding animatrice pourrait justifier l'application de l'exonération, mais cela demande un montage lourd.
3. **Report de la donation :** Si le calendrier le permet (et si l'urgence n'est pas absolue), il conviendrait de restructurer l'entité avant de mettre en place un nouveau pacte.
4. **Alternative à la donation en pleine propriété :** À défaut de Dutreil, il convient d'envisager un démembrement (donation de la nue-propriété avec réserve d'usufruit), qui permettrait de diminuer l'assiette taxable de moitié, le donateur étant âgé de 62 ans (barème de l'article 669).

Je reste à votre entière disposition pour en discuter de vive voix, notamment pour envisager une réunion de travail afin de mettre en place une structure permettant d'optimiser cette transmission patrimoniale.

Je vous prie d'agréer, Messieurs, l'expression de mes salutations dévouées.

**[Votre Nom]**
*Avocat à la Cour, Spécialiste en Droit Fiscal*


---

## C31  (31 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**CONSULTATION JURIDIQUE – MAINTIEN DU REPORT D’IMPOSITION APRÈS CESSION DE TITRES PAR UNE HOLDING**

Vous m’interrogez sur les conditions à remplir pour conserver le bénéfice du report d’imposition prévu à l’article 150‑0 B ter du Code général des impôts (CGI) après que votre holding personnelle a cédé, moins de trois ans après leur apport, les titres d’une société d’exploitation. Le produit de la cession, soit 9 000 000 €, est demeuré sur le compte bancaire de la holding. Vous indiquez savoir qu’une partie de cette somme doit être réinvestie.

Cette consultation s’inscrit dans un cadre juridique précis, que je vais rappeler avant d’analyser votre situation et de formuler des recommandations concrètes.

---

### 1. Rappel du cadre juridique applicable

#### 1.1. Le report d’imposition de l’article 150‑0 B ter du CGI

Lorsqu’un contribuable apporte des titres à une société qu’il contrôle (cas d’une holding détenue à 100 % par vous), la plus‑value constatée lors de l’apport bénéficie, en principe, d’un **report d’imposition**. Ce report n’est pas une exonération définitive : il permet de différer l’imposition de la plus‑value jusqu’à la survenance d’un événement mettant fin au report.

Parmi ces événements, l’article 150‑0 B ter, I, 2° du CGI vise notamment la **cession à titre onéreux des titres apportés**, lorsque cette cession intervient dans un délai de trois ans à compter de la date de l’apport.

#### 1.2. L’exception pour réinvestissement dans l’activité éligible

Par dérogation, le même texte prévoit que le report n’est pas remis en cause si la société bénéficiaire de l’apport (votre holding) **cède les titres dans les trois ans de l’apport** et **prend l’engagement d’investir le produit de la cession**, dans un délai de trois ans à compter de la date de la cession, à hauteur d’**au moins 70 %** du montant de ce produit, dans le financement de **moyens permanents d’exploitation** affectés à **son activité éligible** telle que définie au **3° du C du I de l’article 199 terdecies‑0 A du CGI**.

Le texte ajoute que **les activités de gestion de son propre patrimoine immobilier sont également exclues du bénéfice de cette dérogation**, ce qui signifie que même une holding immobilière ne pourrait pas s’en prévaloir.

#### 1.3. La notion d’« activité éligible » au sens du renvoi

Le renvoi au **3° du C du I de l’article 199 terdecies‑0 A** renvoie à la définition des activités éligibles retenue pour la réduction d’impôt « IR‑PME ». En pratique, il s’agit des activités industrielles, commerciales, artisanales, agricoles ou libérales, ainsi que des **activités de holding animatrice**.

En effet, les holdings qui se contentent de gérer leur propre patrimoine mobilier (simple détention de participations sans animation) sont considérées comme exerçant une activité de **gestion de son propre patrimoine mobilier**, exclue du bénéfice de la dérogation. Seule une **holding animatrice** – c’est‑à‑dire une holding qui participe activement à la gestion des filiales, leur fournit des services (trésorerie, administratif, juridique, comptable, ressources humaines, etc.) et définit une stratégie de groupe – peut être regardée comme exerçant une activité éligible.

---

### 2. Application à votre situation

#### 2.1. Constat factuel

- La cession par votre holding est intervenue en **février 2026**.
- Elle porte sur des titres apportés il y a **moins de trois ans**.
- Le produit de la cession s’élève à **9 000 000 €**.
- Les fonds sont actuellement **non investis** (ils « dorment » sur le compte bancaire de la holding).

Cette situation déclenche en principe la remise en cause du report d’imposition, sauf si vous parvenez à satisfaire aux conditions de l’exception.

#### 2.2. Montant à réinvestir

Le seuil de 70 % du produit de cession s’élève à :

**9 000 000 € × 70 % = 6 300 000 €**

Votre holding doit donc réinvestir **au minimum 6 300 000 €** dans le financement de moyens permanents d’exploitation affectés à son activité éligible, **avant le terme du délai de trois ans à compter de la date de la cession**, soit **au plus tard en février 2029**.

Le fait de laisser la somme sur un compte bancaire, même rémunéré, ne constitue pas un investissement en « moyens permanents d’exploitation ». Une simple trésorerie passive ne peut pas être qualifiée de la sorte.

---

### 3. Conditions essentielles à remplir pour sécuriser le report

#### 3.1. L’activité de la holding doit être éligible

Il s’agit d’une condition **impérative**. Votre holding ne doit pas être une simple holding de gestion de participations passives. Elle doit exercer une **réelle activité d’animation** de ses filiales ou, à défaut, exercer elle‑même une activité industrielle, commerciale, artisanale, agricole ou libérale.

Pour apprécier le caractère animateur, l’administration fiscale et la jurisprudence prennent en compte plusieurs indices :
- La fourniture effective de services aux filiales (comptabilité, juridique, ressources humaines, trésorerie, assistance commerciale, etc.),
- La présence de moyens matériels et humains dédiés à l’animation,
- La détention de participations majoritaires ou significatives,
- L’existence d’une stratégie de groupe et d’une participation active aux décisions importantes,
- L’existence de conventions de management ou de prestations de services facturées.

Si votre holding est une structure dépourvue de substance (pas de salariés, pas de prestations effectives, uniquement des opérations de détention), le report sera remis en cause, sans possibilité de bénéficier de l’exception.

#### 3.2. La nature de l’investissement : « financement de moyens permanents d’exploitation »

Le réinvestissement doit financer des **actifs affectés durablement à l’activité éligible**. Sont notamment visés :
- L’acquisition d’**immobilisations** corporelles ou incorporelles (matériel, bâtiments à usage professionnel, logiciels, etc.),
- La **souscription au capital** de sociétés exerçant une activité éligible (filiales d’exploitation) ou l’acquisition de titres de telles sociétés,
- Les **avances en compte courant d’associé** consenties à des filiales éligibles, à condition qu’elles soient affectées au financement de leur activité et présentent un caractère permanent (blocage, absence de rémunération excessive, etc.),
- Le financement du **besoin en fonds de roulement permanent** de l’activité opérationnelle de la holding ou de ses filiales animées.

En revanche, sont exclus les simples placements financiers, les dépôts bancaires, les prêts à court terme, ou les investissements dans des sociétés exerçant une activité de gestion de patrimoine immobilier (même si la holding est animatrice).

#### 3.3. Le formalisme de l’engagement

L’article 150‑0 B ter exige que la société bénéficiaire de l’apport **preme l’engagement** d’investir le produit de la cession dans les conditions susvisées. Cet engagement doit être **exprimé de manière formelle** :
- Idéalement, dans l’acte de cession des titres lui‑même,
- À défaut, dans un document séparé (délibération de l’associé unique, procès‑verbal du conseil d’administration, lettre d’engagement) daté au plus tard à la date de la cession,
- Et doit être **joint à la déclaration de résultats** de la société au titre de l’exercice de la cession.

En pratique, la doctrine administrative (BOI-RPPM-PVBMI-30-10-20-30) précise que l’engagement doit être pris **avant la cession ou au moment de celle‑ci**. Une simple intention manifestée ultérieurement pourrait être jugée inopérante. Il vous appartient donc de vérifier, dès à présent, si un tel engagement a été formalisé lors de la vente de février 2026. En l’absence d’engagement, le report d’imposition est déjà réputé avoir pris fin, et la situation pourrait être difficilement régularisable.

#### 3.4. Le délai de réinvestissement

Le réinvestissement doit être réalisé **dans un délai de trois ans à compter de la date de la cession**, c’est‑à‑dire avant le **mois de février 2029**. Le simple engagement ne suffit pas : l’investissement doit être effectivement réalisé et justifié avant cette date.

---

### 4. Conséquences en cas de non‑respect

Si les conditions de l’exception ne sont pas remplies (montant réinvesti inférieur à 70 %, délai dépassé, activité de la holding non éligible, absence d’engagement formel), le report d’imposition prendra fin rétroactivement.

La plus‑value d’apport initialement mise en report sera alors **imposée au nom de l’apporteur (vous‑même)** au titre de l’année de la cession des titres (2026), dans la catégorie des plus‑values sur titres (prélèvement forfaitaire unique de 30 %, sauf option pour le barème progressif). S’ajouteront des **intérêts de retard** (0,2 % par mois, soit 2,4 % par an) et éventuellement des **pénalités** pour défaut de déclaration ou insuffisance, selon les cas.

L’enjeu financier est donc très significatif : la totalité de la plus‑value d’apport deviendrait exigible.

---

### 5. Recommandations pratiques

Afin de sécuriser le maintien du report d’imposition, je vous recommande de :

1. **Vérifier immédiatement l’existence d’un engagement formel** pris lors de la cession de février 2026. Si aucun document ne formalise cet engagement, consultez sans tarder un avocat fiscaliste pour évaluer les possibilités de régularisation (elles sont malheureusement limitées).

2. **Analyser l’activité réelle de votre holding** et constituer un dossier démontrant son caractère d’animateur (existence de services rendus, moyens mis en œuvre, facturations, etc.). Si ce caractère n’est pas suffisamment établi, il peut être utile de renforcer l’animation avant l’expiration du délai, mais cela ne vaudra que pour l’avenir, pas rétroactivement.

3. **Identifier un ou plusieurs projets d’investissement éligibles** à réaliser avant février 2029 pour un montant total d’au moins 6 300 000 €. Ces investissements doivent être affectés à des moyens permanents d’exploitation :
   - Souscription au capital de filiales d’exploitation,
   - Acquisition d’immobilisations affectées à l’activité,
   - Avances en compte courant à long terme à des filiales éligibles,
   - Acquisition de nouvelles participations dans des sociétés opérationnelles.

4. **Ne pas laisser les fonds inutilisés** sur un compte bancaire. Soyez en mesure de prouver l’affectation précise des sommes investies (relevés bancaires, contrats, actes juridiques).

5. **Documenter l’ensemble des opérations** : garder les justificatifs d’investissement, les factures, les conventions de compte courant, les délibérations, etc.

6. **Consulter un avocat fiscaliste spécialisé** pour valider les schémas d’investissement envisagés et vérifier leur conformité avec la doctrine administrative, notamment en ce qui concerne la qualification de « moyens permanents d’exploitation ».

---

### Conclusion

Vous devez impérativement réinvestir **au moins 6 300 000 €** avant **février 2029**, mais surtout vérifier que votre holding exerce bien une activité éligible et qu’un engagement formel de réinvestissement a été pris au moment de la cession. À défaut, le report d’imposition sera remis en cause et la plus‑value d’apport deviendra immédiatement imposable, avec intérêts et pénalités.

Cette consultation ne constitue pas un audit complet, mais elle met en évidence les points de vigilance prioritaires. Je vous invite à me communiquer les documents relatifs à l’apport, à la cession et à l’activité de la holding afin de sécuriser votre situation.

Je reste à votre disposition pour tout complément d’information ou pour vous assister dans la mise en œuvre de ces recommandations.


---

## C32  (32 sur 45)

**VOTRE CODE : ______________________________**

**Fait manquant :** La date de dépôt du projet au greffe. Le régime nouveau ne s'applique qu'aux opérations dont le projet a été déposé à compter du 1er juillet 2023.

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus directement aux
associes de la societe apporteuse, afin que chaque branche de la
famille detienne sa societe.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder :**

## CONSULTATION

**Objet :** Apport partiel d'actif de la branche industrielle avec attribution directe des titres aux associés – éligibilité au régime de faveur des articles 210 A et suivants du CGI

*Note établie sur la seule base des éléments oraux communiqués, sous réserve de l'examen des statuts, des comptes, du pacte d'associés éventuel et de la répartition exacte du capital.*

---

## 1. Réponse de principe : oui, l'opération entre dans le champ du régime

L'article 210-0 A, I, 4° que vous citez règle une question qui a longtemps été discutée : l'apport partiel d'actif **avec remise des titres directement aux associés de l'apporteuse** ("scission partielle" au sens de la directive fusions) constitue bien une opération éligible. Depuis la loi de finances pour 2018, qui a mis le droit interne en conformité avec la directive 2009/133/CE, cette modalité n'est plus subordonnée à un agrément préalable.

**Mais attention à une confusion fréquente :** l'article 210-0 A est un texte de *définition*. Il délimite le périmètre des opérations susceptibles de relever du régime ; il ne confère aucun droit à ce régime. Le bénéfice effectif de l'article 210 A suppose de satisfaire, cumulativement :

- les conditions de fond de l'**article 210 B** (apport) ;
- les conditions de l'**article 115, 2** (attribution des titres aux associés) ;
- la clause anti-abus du **III de l'article 210-0 A**.

C'est sur ce second étage que votre projet, tel que vous me le décrivez, se heurte à un obstacle dirimant.

---

## 2. Les conditions à respecter

### 2.1. Au niveau de l'apport (art. 210 B, 1)

**a) Branche complète d'activité.** L'apport doit porter sur un ensemble d'éléments d'actif **et de passif** constituant, du point de vue de l'organisation, une exploitation autonome capable de fonctionner par ses propres moyens. C'est un point d'audit à ne pas sous-estimer : il faut vérifier le transfert des moyens d'exploitation (immobilier ou droit d'usage, matériel, stocks, contrats clients et fournisseurs, marques et licences, personnel dédié – y compris fonctions support –, dettes affectées). Une branche apportée « à sec », le siège, l'immobilier ou la trésorerie restant chez l'apporteuse, est un motif classique de remise en cause.

**b) Engagements.** L'apporteuse doit normalement s'engager à conserver les titres reçus pendant trois ans et à calculer les plus-values ultérieures par référence à la valeur fiscale des biens apportés. Ces engagements sont sans objet – et la loi les écarte – lorsque les titres sont répartis entre les associés dans les conditions du 2 de l'article 115 dans le délai d'un an. C'est précisément l'intérêt du schéma envisagé.

### 2.2. Au niveau de l'attribution (art. 115, 2)

L'attribution des titres aux associés n'échappe à la qualification de **distribution de revenus mobiliers** que si trois conditions sont réunies :

- **a)** l'apport est placé sous le régime de l'article 210 A ;
- **b)** **la société apporteuse dispose encore d'au moins une branche complète d'activité après l'apport** ;
- **c)** l'attribution est **proportionnelle aux droits des associés dans le capital** et intervient dans **un délai d'un an** à compter de la réalisation de l'apport.

Sur la condition **b)** : si la holding exerce elle-même le négoce, la condition devrait être remplie. Si, en revanche, le négoce est logé dans des filiales et que la holding ne conserve qu'un portefeuille de titres, la qualification de « branche complète » devient discutable et devra être sécurisée (rescrit ou agrément). Dites-moi précisément ce que la holding exploite en propre.

---

## 3. L'obstacle : la condition de proportionnalité interdit la séparation recherchée

Votre objectif — « que chaque branche de la famille détienne sa société » — implique par construction une attribution **non proportionnelle** : la branche familiale A recevrait 100 % de la société nouvelle industrielle, la branche B conservant 100 % de la holding de négoce.

Or le c) du 2 de l'article 115 impose une répartition **proportionnelle aux droits dans le capital**. Cette exigence n'est pas une tolérance administrative : elle figure dans la loi, et se retrouve à l'identique pour les scissions (art. 210-0 A, I, 2° et 210 B, 1, al. 3), ainsi que dans la directive. À notre analyse, **l'agrément de l'article 210 B, 3 ne permet pas d'y déroger** : il a pour objet de suppléer l'absence de branche complète, non de réécrire la définition légale de l'opération.

**Conséquences d'une attribution non proportionnelle :**

1. **Chez les associés bénéficiaires** : l'attribution redevient une **distribution de revenus mobiliers**, imposable sur la valeur réelle des titres reçus (PFU 30 %, ou barème + CSG sur revenus du patrimoine sur option). L'assiette n'est pas la plus-value : c'est la valeur intégrale attribuée. Le coût est très supérieur à celui d'une cession.
2. **Risque de libéralité** : l'écart de valeur entre ce que reçoit chaque branche familiale et ses droits théoriques est susceptible d'être analysé, entre cousins, comme une **donation indirecte** taxée à 55 % ou 60 %.
3. **Risque sur l'apport lui-même** : la déqualification de l'attribution ne fait pas juridiquement tomber le régime 210 A de l'apport, mais l'ensemble sera examiné à l'aune de la clause anti-abus du III de l'article 210-0 A et de l'article L. 64 A du LPF.

**En l'état, ma réponse est donc : non, le schéma tel que décrit ne peut pas être réalisé sous le régime de faveur en une seule étape.**

---

## 4. Les voies praticables

**Option 1 – Apport-attribution proportionnel, puis échange croisé des titres (schéma le plus courant).**
Étape 1 : APA de la branche industrielle + attribution proportionnelle sous 115, 2 → chaque associé détient sa quote-part dans les deux sociétés. Coût fiscal : nul.
Étape 2 : échange croisé entre les deux branches familiales. Cet échange n'est **pas** couvert par le sursis de l'article 150-0 B (qui ne vise pas les échanges entre associés) : il est imposable à la plus-value (PFU 30 %), pour chacune des deux branches.
Points de vigilance : le rapprochement des deux étapes peut être analysé comme une attribution non proportionnelle déguisée ; il faut un motif documenté (mésentente, divergence stratégique, gouvernance), une chronologie crédible, et idéalement une sécurisation préalable.

**Option 2 – Réduction de capital / rachat des titres de la branche sortante, payé par remise des titres de la société nouvelle.**
Séparation nette en une opération. Mais double frottement : plus-value de cession chez l'associé sortant (art. 150-0 A) **et**, chez la holding, plus-value sur la remise des titres, dont la valeur fiscale est, du fait du régime 210 A, celle des biens apportés — donc plus-value latente maximale, imposée au taux plein si les titres sont détenus depuis moins de deux ans. Schéma à chiffrer, souvent rédhibitoire.

**Option 3 – Interposition préalable de holdings personnelles (150-0 B ter) avant l'échange croisé.**
Permet, dans certaines configurations, de ramener la plus-value taxable à la valeur d'apport. Mais : maintien du report subordonné à la conservation trois ans (à défaut, remploi de 60 %), et risque sérieux de montage artificiel si l'interposition n'a pas de substance propre. À n'envisager qu'après analyse approfondie.

**Option 4 – Séparation économique sans séparation capitalistique** (actions de préférence, démembrement, holdings animatrices distinctes, pacte de séparation) : à considérer si le coût des options précédentes est disproportionné.

---

## 5. Autres points à traiter impérativement

- **Valorisation et méthode d'apport** : apports à la valeur comptable ou à la valeur réelle selon le règlement ANC 2017-01 (contrôle commun / sens de l'opération) ; incidence sur les capitaux propres disponibles pour l'attribution.
- **Droits d'enregistrement** : droit fixe (art. 816/817) si l'ensemble est placé sous le régime de faveur ; à sécuriser si un immeuble est apporté.
- **TVA** : dispense de l'article 257 bis (transmission d'universalité), avec les régularisations à surveiller.
- **Déficits reportables** de la branche apportée : transfert soumis à agrément (art. 209, II).
- **Intégration fiscale** : conséquences d'une sortie de groupe.
- **Pactes Dutreil en cours** : un apport ou une attribution en cours d'engagement peut, hors les cas de neutralisation prévus par l'article 787 B, entraîner la déchéance de l'exonération. Point à vérifier en priorité.
- **Reports d'imposition antérieurs** (150-0 B ter, 150-0 B) éventuellement attachés aux titres de la holding.
- **Droit des sociétés** : depuis l'ordonnance n° 2023-393 du 24 mai 2023, l'apport partiel d'actif avec attribution des titres aux associés dispose d'un régime propre ; à défaut, l'attribution suppose des réserves distribuables ou une réduction de capital. Consultation du CSE, information des salariés (loi Hamon), agréments statutaires, sort des contrats intuitu personae.

---

## 6. Recommandation

1. **Ne pas figer le schéma en l'état.** L'attribution directe est possible, mais **proportionnelle** : elle ne réalise pas, à elle seule, la séparation des branches familiales.
2. **Chiffrer d'abord la seconde étape** (échange croisé) : c'est elle qui porte tout le coût. Il me faut, pour cela, le prix de revient fiscal des titres de chaque associé et une valorisation indicative des deux branches.
3. **Sécuriser en amont** : je préconise une consultation préalable, officieuse puis formalisée, du bureau des agréments (et, le cas échéant, un rescrit sur la qualification de branche complète de l'activité de négoce conservée). Compte tenu de la clause anti-abus du III de l'article 210-0 A, la documentation du **motif économique de la séparation** doit être constituée dès maintenant, et non reconstituée après contrôle.
4. **Formaliser la volonté commune** des deux branches dans un protocole de séparation avant toute opération, la fiscalité n'étant ici que la traduction d'un accord familial qui doit être stable.

**Pièces à me communiquer :** statuts et K-bis de la holding, table de capitalisation détaillée, trois derniers exercices (comptes sociaux et consolidés le cas échéant), organigramme du groupe, inventaire des actifs et contrats affectés à chaque branche, états des reports d'imposition et engagements Dutreil, pacte d'associés.

Je reste à votre disposition pour un rendez-vous de cadrage avec les représentants des deux branches, séparément si nécessaire — je souligne d'ailleurs que la représentation d'intérêts appelés à diverger devra faire l'objet, le moment venu, d'une clarification déontologique.


---

## C33  (33 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

Pour déterminer si l'exonération partielle de l'article 787 B du Code Général des Impôts (CGI) est applicable à la donation que le dirigeant de 62 ans envisage de faire à ses deux enfants, il convient d'analyser les conditions prévues par cet article et de les appliquer aux faits présentés.

1. **Nature de la société et de son activité** : La société en question est une société par actions simplifiée (SAS) qui possède quarante appartements meublés. La valeur des titres est de 20 000 000 euros. L'activité principale de cette société semble être la gestion de son patrimoine immobilier, ce qui, selon l'article 787 B, n'est pas considérée comme une activité industrielle, commerciale, artisanale, agricole ou libérale au sens du premier alinéa, sauf si elle remplit les conditions du troisième alinéa concernant la participation active à la conduite de la politique de son groupe.

2. **Exonération de 75 % prévue par l'article 787 B** : L'exonération partielle à hauteur de 75 % de la valeur des parts ou actions s'applique sous certaines conditions. La société doit avoir une activité éligible, et les transmissions doivent être réalisées dans les conditions prévues.

3. **Activité de gestion de patrimoine vs. activité commerciale** : Étant donné que la société a pour principale activité la gestion de son patrimoine immobilier (quarante appartements meublés), cela correspond à la gestion de son propre patrimoine, ce qui n'est pas considéré comme une activité éligible selon le deuxième alinéa de l'article 787 B, sauf si elle répond aux critères du troisième alinéa.

4. **Application du troisième alinéa de l'article 787 B** : Pour être considérée comme exerçant une activité commerciale malgré la gestion d'un patrimoine, la société doit avoir pour activité principale la participation active à la conduite de la politique de son groupe, constitué de sociétés contrôlées exerçant une activité éligible. Il n'est pas indiqué que la société en question fait partie d'un groupe ou contrôle d'autres sociétés exerçant des activités industrielles, commerciales, artisanales, agricoles ou libérales. Par conséquent, sur la base des informations fournies, il semble peu probable que la société remplisse cette condition.

5. **Engagement collectif de conservation et autres conditions** : Les parts font l'objet d'un engagement collectif de conservation signé le 3 mars 2021, et chaque enfant prend l'engagement individuel prévu. Le dirigeant conserve la présidence pendant trois ans. Cependant, l'article 787 B prévoit des conditions spécifiques pour l'exonération, notamment liées à l'activité de la société et non directement à l'engagement de conservation.

**Conclusion** : 
Étant donné que l'activité principale de la société semble être la gestion de son patrimoine immobilier, et qu'il n'est pas établi qu'elle participe activement à la conduite de la politique d'un groupe de sociétés exerçant des activités éligibles, l'exonération partielle prévue par l'article 787 B du CGI pourrait ne pas être applicable. La donation envisagée le 25 octobre 2023 pourrait donc ne pas bénéficier de cette exonération de 75 % sur la valeur des titres de la société.

Il conviendrait de vérifier plus en détail les activités exactes de la société et les conditions spécifiques de l'article 787 B pour une conclusion définitive, notamment en analysant les autres conditions prévues par l'article qui n'ont pas été détaillées ici. Une analyse approfondie des statuts de la société, de son activité réelle et de sa structure de groupe (si applicable) serait nécessaire pour confirmer cette première analyse.


---

## C34  (34 sur 45)

**VOTRE CODE : ______________________________**

**Fait manquant :** La date de dépôt du projet au greffe. Le régime nouveau ne s'applique qu'aux opérations dont le projet a été déposé à compter du 1er juillet 2023.

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus directement aux
associes de la societe apporteuse, afin que chaque branche de la
famille detienne sa societe.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder :**

Maître,

Votre projet d’apport partiel d’actif (branche industrielle) à une société nouvelle, avec attribution directe des titres reçus aux associés de la société apporteuse, entre parfaitement dans le champ du régime fiscal de faveur prévu aux articles 210 A et suivants du Code général des impôts.

**1. Le cadre juridique applicable**

L’article 210-0 A, I, 4° du CGI définit précisément les opérations d’apport partiel d’actif éligibles au régime spécial des fusions :  
*« 4° S'agissant des apports partiels d'actifs, aux opérations par lesquelles une société apporte, sans être dissoute, l'ensemble ou une ou plusieurs branches complètes de son activité à une ou plusieurs sociétés, moyennant la remise de titres représentatifs du capital social de la société bénéficiaire de l'apport soit à la société apporteuse, soit directement aux associés de la société apporteuse. »*

Ce texte valide expressément deux modalités de remise des titres, dont l’attribution directe aux associés, qui correspond à votre schéma.

**2. Conditions d’éligibilité de votre opération**

Pour bénéficier de plein droit de ce régime sur option, vous devez satisfaire à trois conditions cumulatives, toutes réunies en l’espèce :

- **L’apport doit porter sur une branche complète d’activité** : la branche industrielle doit constituer un ensemble autonome d’actifs et de passifs, capable de fonctionner par ses propres moyens. Dès lors que cette branche dispose de ses propres moyens d’exploitation, de sa clientèle et de son personnel, la condition est remplie. Il conviendra de documenter cette autonomie.
- **La société apporteuse ne doit pas être dissoute** : elle conservera la branche négoce, ce qui est le cas.
- **La rémunération de l’apport doit être exclusivement constituée de titres** de la société bénéficiaire (actions ou parts sociales). La création d’une société nouvelle à cet effet ne fait pas obstacle au régime de faveur. L’attribution de ces titres directement aux associés de la holding, en lieu et place de la société apporteuse, est expressément prévue par le texte.

Aucune condition tenant à la nature familiale de l’actionnariat ou à la volonté de séparation des branches n’est de nature à remettre en cause l’éligibilité.

**3. Conséquences fiscales du régime de faveur**

L’option pour le régime de faveur emporte les principaux effets suivants :

- **Au niveau de la société apporteuse** : les plus-values latentes sur les éléments de la branche industrielle transférée sont placées en sursis d’imposition (IS) et ne sont pas taxées immédiatement. Les provisions sont reprises en sursis, sauf exceptions.
- **Au niveau des associés de la société apporteuse** : l’attribution directe des titres de la société nouvelle ne constitue pas une distribution de dividendes imposable. Les plus-values réalisées par les associés à l’occasion de cet échange (la valeur des titres reçus contre la réduction de valeur des titres de la holding) sont également placées en sursis d’imposition, sous réserve du respect de l’engagement de conservation des titres reçus pendant un délai de trois ans (article 150-0 B ter du CGI). En pratique, ils devront déclarer cette opération et conserver les titres de la nouvelle société pendant cette période.
- **Droits d’enregistrement** : l’apport partiel d’actif donne lieu à un droit fixe de 500 € (ou 0,25 % sur les apports à titre onéreux, mais ici l’apport est à titre pur et simple, rémunéré par des titres). Le transfert des immeubles éventuels contenus dans la branche industrielle bénéficie du régime de faveur, sans taxation proportionnelle.

**4. Points de vigilance et recommandations**

- **Analyse préalable de la branche complète** : la qualification de branche complète d’activité s’apprécie à la date d’effet de l’opération. Il est impératif de vérifier que la branche industrielle transférée comprend bien tous les éléments d’actif et de passif nécessaires à son exploitation autonome (immobilisations, stocks, créances, dettes, personnel, contrats, etc.). Un audit de branche pourra être utile.
- **Formalisme de l’opération** : l’apport partiel d’actif doit être décidé par l’assemblée générale extraordinaire de la société apporteuse (et de la société bénéficiaire si celle-ci existe déjà ; dans le cas d’une création, l’assemblée des associés fondateurs). Un traité d’apport devra être établi, déposé au greffe et publié. L’option pour le régime de faveur devra être formellement exercée.
- **Engagement de conservation des titres** : les associés devront prendre l’engagement de conserver les titres de la société nouvelle pendant trois ans, à compter de la réalisation de l’apport, pour bénéficier du sursis d’imposition des plus-values. Cet engagement doit être porté sur la déclaration d’ensemble des revenus de l’année de l’opération.
- **Absence de motivation abusive** : le régime de faveur ne saurait être remis en cause sur le fondement d’un abus de droit dès lors que l’opération répond à une logique économique réelle – ici la séparation des branches familiales. La justification de la restructuration est évidente.

En conclusion, votre projet est éligible au régime de faveur des articles 210 A et suivants du CGI, sous réserve de la stricte qualification de branche complète d’activité de la branche industrielle. Je vous propose de procéder à une revue détaillée des actifs et passifs concernés avant de formaliser l’opération, afin de sécuriser le bénéfice de ce régime fiscal avantageux.

Je reste à votre disposition pour tout complément d’information ou pour vous accompagner dans la mise en œuvre de cette opération.


---

## C35  (35 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

## Consultation — retenue à la source sur distribution de 20 M€ à une société mère luxembourgeoise

**Mise en paiement envisagée : 15 juin 2025 — Enjeu : 5 M€ (25 %) + intérêts et pénalités éventuelles**

---

### 1. Réserve liminaire sur le texte que vous me communiquez

Vous ne me soumettez que le **premier alinéa du 2 de l'article 119 bis du CGI**. Cet extrait pose le principe de la retenue à la source ; il ne contient aucune exonération susceptible de bénéficier à votre société mère. La fin de l'alinéa (« *et qui satisfont aux deux conditions suivantes* ») introduit une exclusion propre aux **organismes de placement collectif de droit étranger**, dont votre actionnaire — société anonyme luxembourgeoise soumise à l'IS — n'est manifestement pas.

**Sur le seul fondement du texte communiqué, la réponse est donc : oui, la retenue à la source est due**, au taux de l'article 187, soit **25 %** pour une personne morale non résidente (20 M€ × 25 % = **5 000 000 €**).

L'exonération que vous escomptez ne figure pas dans ce texte : elle résulte de **l'article 119 ter du CGI** (transposition de la directive 2011/96/UE dite « mère-fille »), le cas échéant complété par la **convention fiscale franco-luxembourgeoise du 20 mars 2018**. Je raisonne ci-après sur ces fondements, mais **je vous demande de me confirmer la version de l'article 119 ter en vigueur au 15 juin 2025**, ainsi que l'absence de disposition nouvelle issue de la loi de finances pour 2025 affectant ce régime. Je ne peux pas engager ma responsabilité sur un régime d'exonération dont le texte ne m'a pas été soumis.

---

### 2. Analyse au regard de l'article 119 ter du CGI

Les conditions habituelles de l'exonération, appliquées à vos données, se présentent favorablement :

| Condition | Votre situation | Appréciation |
|---|---|---|
| Distribution par une société française passible de l'IS | Oui | ✔ |
| Siège de direction effective du bénéficiaire dans un État membre de l'UE, sans être résident d'un État tiers par convention | Luxembourg — **à confirmer** (direction effective, et non simple siège statutaire) | À documenter |
| Forme sociale figurant dans la liste annexée à la directive | Société anonyme de droit luxembourgeois : forme listée | ✔ |
| Assujettissement à l'impôt sur les sociétés de l'État de résidence, sans possibilité d'option ni exonération | Vous m'indiquez que la société est soumise à l'IS luxembourgeois | ✔ **sous réserve** qu'il ne s'agisse pas d'une SPF (société de gestion de patrimoine familial), exonérée, ni d'un véhicule bénéficiant d'un régime d'exonération spécifique |
| Détention **directe** d'au moins 10 % du capital | 100 % | ✔ |
| Pendant au moins 2 ans (ou engagement de conservation) | 5 ans | ✔ — aucun engagement de conservation à souscrire |

**Deux points ne sont, en revanche, pas réglés par ces critères formels et constituent aujourd'hui l'essentiel du risque.**

#### a) La qualité de bénéficiaire effectif (art. 119 bis, 2)

Le texte que vous me communiquez réserve lui-même la retenue aux produits dont les « **bénéficiaires effectifs** » sont non-résidents. Symétriquement, l'administration et le juge refusent l'exonération lorsque la société mère n'est qu'un **relais** au profit d'un actionnaire situé hors UE (CJUE, 26 février 2019, *N Luxembourg 1* et *T Danmark* ; CE, 5 février 2021, n° 430594 ; CE, 20 mai 2022, *Planet*).

Le contexte que vous décrivez — cession d'actif, remontée immédiate d'une trésorerie de 20 M€ vers un holding luxembourgeois — est **exactement le schéma que les brigades de contrôle examinent**. La question déterminante est donc : **que devient l'argent après le 15 juin 2025 ?**

#### b) La clause anti-abus (art. 119 ter, 3)

L'exonération est écartée pour les distributions comprises dans un montage ou une série de montages ayant pour objectif principal, ou l'un de ses objectifs principaux, l'obtention d'un avantage fiscal contraire à l'objet de la directive, et qui n'est pas authentique (dépourvu de substance économique). Depuis les arrêts *Eqiom* (CJUE, 7 sept. 2017) et *Holcim*, **la charge de la preuve pèse sur l'administration**, ce qui est un atout majeur pour vous — à condition que le dossier soit préparé.

---

### 3. Informations et pièces qu'il me faut avant toute conclusion ferme

1. **Actionnariat de la société luxembourgeoise** : identité, résidence fiscale et forme de ses associés, sur toute la chaîne, jusqu'aux bénéficiaires effectifs ultimes. Existe-t-il un actionnaire hors UE (notamment dans un État sans convention, ou non coopératif) ?
2. **Substance de la société mère** : composition et lieu de réunion du conseil, résidence des administrateurs, locaux, salariés, autonomie décisionnelle, existence d'autres participations et d'une activité de holding animateur ou de gestion, comptes annuels, endettement (existe-t-il des emprunts *back-to-back* ou des prêts d'associés dont le service absorberait le dividende ?).
3. **Destination des fonds** : décision de l'organe compétent, procès-verbaux, business plan. Une redistribution rapide et intégrale vers un actionnaire tiers serait très défavorable ; un réemploi (acquisitions, financement d'autres filiales, désendettement) documenté *ex ante* est au contraire déterminant.
4. **Date d'acquisition et modalités de détention** des titres : pleine propriété ? absence de démembrement, de portage, de convention de rétrocession, de prêt de titres ou de pension livrée (attention à l'article 119 bis A du CGI) ?
5. **Statut luxembourgeois exact** : SOPARFI de droit commun ou véhicule à régime particulier ? Justificatif d'assujettissement à l'IS luxembourgeois (attestation de l'administration des contributions directes).
6. **Absence d'établissement stable français** de la mère auquel les titres seraient rattachés.
7. **Capacité distributive** : comptes approuvés, montant du bénéfice distribuable, réserves, réserve légale ; s'il s'agit d'un acompte sur dividendes, bilan intermédiaire certifié par le commissaire aux comptes (art. L. 232-12 C. com.). Le résultat de cession doit être régulièrement constaté.

---

### 4. Conclusion

- **En l'état des seuls éléments et du seul texte communiqués : la retenue à la source de 25 %, soit 5 000 000 €, est due.**
- **Si l'article 119 ter est bien en vigueur dans sa rédaction habituelle au 15 juin 2025**, et sous réserve de la confirmation des points ci-dessus (assujettissement effectif à l'IS luxembourgeois, direction effective au Luxembourg, qualité de bénéficiaire effectif, absence de montage non authentique), la distribution peut être **payée sans aucune retenue à la source (taux 0 %)**. Les seuils de 10 % et de 2 ans sont très largement satisfaits (100 %, 5 ans).
- **À titre subsidiaire**, si l'exonération interne était écartée pour un motif formel, il faudrait examiner la convention franco-luxembourgeoise du 20 mars 2018, dont l'article 10 plafonne le prélèvement (taux réduit selon le niveau et la durée de détention) — mais je vous invite à ne pas compter sur cette voie : d'une part elle est moins favorable, d'autre part la clause anti-abus conventionnelle et la condition de bénéficiaire effectif y figurent également. **Si le grief est l'abus, la convention ne sauvera pas l'opération.**
- **Risque en cas de remise en cause** : 5 M€ de retenue (le cas échéant en base « brute », l'administration retenant parfois un calcul en dedans), intérêt de retard de 0,20 %/mois, et majoration de 40 % (manquement délibéré) voire 80 % en cas d'abus de droit (art. 1729 CGI), avec solidarité de l'établissement payeur.

---

### 5. Ce que je vous recommande de faire avant le 15 juin 2025

1. **Obtenir de la mère luxembourgeoise une attestation écrite** certifiant qu'elle remplit chacune des conditions de l'article 119 ter (forme, siège de direction effective, assujettissement à l'IS, détention directe de 100 % depuis plus de deux ans, qualité de bénéficiaire effectif), accompagnée d'un certificat de résidence fiscale. **Cette attestation doit être en votre possession avant la mise en paiement** : c'est la condition pratique de l'application de l'exonération à la source, et la première pièce que réclamera un vérificateur.
2. **Constituer un « dossier de substance »** daté et conservé : organigramme complet, PV du conseil luxembourgeois délibérant réellement sur l'affectation des 20 M€, note d'affectation des fonds, baux, contrats de travail ou de domiciliation, comptes.
3. **Ne pas organiser de reversement immédiat et intégral** vers un actionnaire situé hors UE. Si tel est le projet, il faut me le dire maintenant : l'analyse change radicalement et il faudra soit renoncer au taux 0 %, soit revoir le calendrier et la structure.
4. **Formalités déclaratives** : même en cas d'exonération totale, la distribution doit être suivie sur la **déclaration n° 2777** ; en cas de retenue, celle-ci est à déclarer et acquitter **au plus tard le 15 juillet 2025** (mois suivant la mise en paiement). Je vous invite à ne pas laisser passer cette échéance : le dépôt de la 2777 « à zéro » avec conservation des justificatifs est la position à retenir.
5. **Options à examiner si le risque « bénéficiaire effectif » est réel** :
 - fractionner ou différer la distribution, le temps de renforcer la substance luxembourgeoise ;
 - qualifier une partie du versement en **remboursement d'apports** (art. 112, 1° du CGI), qui n'est pas un revenu distribué et échappe donc à la retenue — mais cela suppose que **tous les bénéfices et réserves autres que la réserve légale aient été préalablement répartis**, ce qui est rarement le cas juste après une cession générant un profit ; à vérifier sur vos comptes ;
 - envisager, si l'incertitude est forte, un **rescrit « abus de droit » (art. L. 64 B du LPF)**, l'administration disposant de six mois pour répondre, son silence valant garantie — ce qui est incompatible avec une mise en paiement au 15 juin, mais pertinent pour une distribution reportée à l'automne.

---

### 6. Suite à donner

Je ne peux valider le paiement sans retenue qu'après réception : (i) du texte complet de l'article 119 ter dans sa version applicable au 15 juin 2025, (ii) des éléments listés au § 3, (iii) de l'attestation de la société mère. Merci de me les adresser sous huitaine compte tenu du calendrier.

Je vous suggère par ailleurs de faire confirmer par un conseil luxembourgeois le traitement du dividende reçu (exonération de participation, retenue à la source luxembourgeoise sur une éventuelle redistribution), afin de valider la cohérence d'ensemble du schéma.

*La présente consultation est établie au vu des seuls éléments de fait et de droit communiqués à ce jour ; elle devra être confirmée après réception des pièces demandées.*


---

## C36  (36 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

Monsieur, Maître, 

Je vous remercie de votre confiance pour l'analyse de ce projet de transmission. 

Vous souhaitez transmettre à vos deux enfants la totalité des titres de votre SAS, valorisée à 20 millions d'euros, en utilisant le bénéfice de l'exonération partielle de 75 % prévue par le dispositif "Pacte Dutreil" (article 787 B du Code Général des Impôts). Vous avez d'ailleurs pris le soin, avec votre notaire, de signer un engagement collectif de conservation dès mars 2021.

Voici mon analyse juridique et fiscale de votre dossier, telle qu'elle s'applique à la date envisagée pour la donation (25 octobre 2023).

### 1. Réponse à votre question : L'exonération Dutreil est-elle applicable ?

**Je dois malheureusement vous répondre par la négative. L'exonération de l'article 787 B du CGI ne sera pas applicable à votre donation.**

Si les conditions de forme (engagement collectif en cours, engagements individuels à venir, maintien de vos fonctions de direction) sont parfaitement remplies, c'est la **nature même de l'activité de votre société** qui fait obstacle au dispositif.

### 2. Explication juridique

Le cœur du problème réside dans l'activité de votre SAS : la location de quarante appartements meublés. 

Il est tout à fait compréhensible que vous ayez mis en place ce Pacte en 2021. Pendant longtemps, une ambiguïté a subsisté : la location meublée relevant fiscalement des Bénéfices Industriels et Commerciaux (BIC - article 35 du CGI), de nombreux praticiens espéraient qu'elle soit éligible au Pacte Dutreil.

Cependant, le texte de l'article 787 B du CGI applicable à la date de votre projet (qui intègre les récentes clarifications législatives et jurisprudentielles, notamment l'arrêt de la Cour de cassation du 1er juin 2023) est désormais sans appel. 

Le deuxième alinéa du texte que nous devons appliquer précise expressément :
> *"Pour l'application du premier alinéa [...], n'est pas considérée comme une activité industrielle, commerciale, artisanale, agricole ou libérale **l'exercice par une société d'une activité de gestion de son propre patrimoine mobilier ou immobilier**."*

L'administration fiscale et les tribunaux considèrent de manière constante que l'exploitation de locations meublées, même à grande échelle (40 appartements), constitue une activité civile de gestion de son propre patrimoine immobilier, et non une activité commerciale au sens du Pacte Dutreil. 

Par conséquent, votre SAS est considérée comme une société à prépondérance patrimoniale. La donation des titres sera donc soumise aux droits de mutation à titre gratuit sur la base de 100 % de leur valeur (20 000 000 €), et non sur la base de 25 % (5 000 000 €).

### 3. Conséquences financières et alternatives proposées

Sans le Pacte Dutreil, une donation en pleine propriété de 20 millions d'euros (10 millions par enfant) engendrerait une fiscalité extrêmement lourde (les droits de donation s'élevant à près de 45 % dans les tranches hautes, soit environ 4,5 millions d'euros par enfant à régler).

En tant que votre conseil, mon rôle est de vous proposer, en concertation avec votre notaire, des solutions alternatives pour optimiser cette transmission :

**A. La donation avec réserve d'usufruit (Démembrement de propriété)**
Puisque vous avez 62 ans, la valeur de la nue-propriété de vos titres est fixée fiscalement à 60 % (l'usufruit que vous conservez étant évalué à 40 %). 
Si vous donnez uniquement la nue-propriété, l'assiette taxable passe de 20 millions à 12 millions d'euros. De plus, vous conservez les dividendes (les loyers de la SAS) pour assurer votre train de vie, et au jour de votre décès, l'usufruit rejoindra la nue-propriété entre les mains de vos enfants sans aucun impôt supplémentaire.

**B. La constitution d'une holding familiale (OBO - Owner Buy Out)**
Nous pourrions envisager que vos enfants constituent une société holding qui rachèterait une partie de vos titres. La holding rembourserait l'emprunt grâce aux dividendes versés par la SAS (régime mère-fille ou intégration fiscale). Cela vous permettrait de dégager des liquidités tout en transmettant progressivement le contrôle. Il faudra toutefois être vigilant sur la taxation de votre plus-value de cession.

**C. Le démembrement des parts de la SAS couplé à une donation-partage**
Pour figer la valeur des titres à ce jour et éviter tout litige futur entre vos enfants, la donation-partage (même en nue-propriété) reste l'outil civil par excellence, que Maître [Nom du notaire] ne manquera pas de vous recommander.

### Conclusion

Le projet de donation en pleine propriété sous le régime Dutreil au 25 octobre 2023 exposerait vos enfants à un redressement fiscal certain et sévère. Je vous déconseille formellement de signer l'acte en l'état.

Je me tiens à votre entière disposition, ainsi qu'à celle de votre notaire, pour chiffrer précisément les droits dus dans le cadre d'une donation en nue-propriété et pour restructurer votre projet de transmission dans un cadre fiscalement sécurisé.

Je vous prie d'agréer, Monsieur, Maître, l'expression de mes salutations dévouées.


---

## C37  (37 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

En votre qualité d’avocat fiscaliste, voici l’analyse que je vous soumets concernant la cession envisagée.

### 1. Qualification de la société et droit d’enregistrement applicable

La société civile immobilière dont vous cédez les titres est une **personne morale à prépondérance immobilière** (PMI) au sens de l’article 726, I, 2° du CGI, dès lors que son actif est constitué à 80 % d’immeubles situés en France et que ses droits sociaux ne sont pas négociés sur un marché réglementé ou un système multilatéral de négociation.

En application de ce même texte, **la cession de participations dans une PMI est soumise à un droit d’enregistrement proportionnel de 5 %**.

**Assiette et calcul :**
- Prix de cession : 4 000 000 €
- Droit d’enregistrement dû : 5 % × 4 000 000 € = **200 000 €**

Ce droit est à la charge de l’acquéreur (sauf convention contraire, mais usuellement supporté par le cessionnaire). Il devra être acquitté lors de la formalité de l’enregistrement, dans le mois de la signature de l’acte (CGI, art. 635, 1-7°).

### 2. Mentions obligatoires devant figurer dans l’acte de cession

L’article 726, III-B du CGI impose que l’acte de cession (ou la déclaration, le cas échéant) indique **expressément** les trois éléments suivants :

1. **Si la société est une société mentionnée à l’article 1655 ter du CGI**  
   Il s’agit des sociétés de construction ayant pour objet la construction d’immeubles en vue de leur vente. En l’espèce, si votre SCI n’a pas cette nature, l’acte devra le mentionner clairement (par exemple : « La société n’est pas une société visée à l’article 1655 ter du CGI »).

2. **Si les participations cédées confèrent au cessionnaire, directement ou indirectement, le droit à la jouissance d’immeubles ou de fractions d’immeubles au sens de l’article 728 du CGI**  
   Cette mention vise les situations où les titres donnent un droit d’occupation ou d’usage privatif d’un immeuble. L’acte devra préciser si un tel droit existe ou non.

3. **Si le cessionnaire a acquitté ou s’engage à acquitter, directement ou indirectement, des dettes contractées auprès du cédant par la société, en précisant, le cas échéant, leur montant**  
   Il s’agit des dettes de la SCI envers le cédant (par exemple, un compte courant d’associé) que l’acquéreur reprendrait ou rembourserait. L’acte devra indiquer l’existence ou l’absence de telles dettes et, si elles existent, leur montant exact.

Ces mentions sont substantielles : leur omission est susceptible d’entraîner des sanctions fiscales (amende prévue à l’article 1840 N du CGI) et peut affecter la validité de l’acte au regard de l’administration fiscale.

### 3. Recommandations pratiques

- **Rédaction de l’acte** : L’acte de cession de parts sociales devra être établi par écrit (acte sous seing privé ou notarié). Compte tenu des enjeux, un acte notarié est fortement recommandé, le notaire assurant la collecte des droits et la vérification des mentions obligatoires.
- **Délai d’enregistrement** : L’acte devra être présenté à la formalité de l’enregistrement dans le mois suivant sa signature, soit au plus tard le 20 avril 2024.
- **Déclaration des plus-values** : En tant que cédant, vous serez par ailleurs redevable de l’impôt sur la plus-value éventuelle (régime des particuliers ou des professionnels selon votre situation). Cette problématique, bien que distincte, devra être anticipée.

Je me tiens à votre disposition pour toute précision complémentaire ou pour la rédaction de l’acte et l’accomplissement des formalités fiscales.


---

## C38  (38 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Objet : Conseil sur le réinvestissement du produit de cession pour maintenir le report d’imposition (Article 150-0 B ter du CGI)**

**À l’attention de [Nom du Client],**
**Holding [Nom de la Holding]**

**Référence :** Cession de titres en février 2026 – Obligation de réinvestissement pour le maintien du report d’imposition

---

### **1. Rappel du contexte et enjeux fiscaux**
Votre holding a cédé en **février 2026** des titres d’une société d’exploitation pour un montant de **9 000 000 €**, moins de **3 ans après leur apport** par vos soins. Conformément à l’**article 150-0 B ter, I, 2° du CGI**, cette cession aurait normalement **mis fin au report d’imposition** sur la plus-value d’apport initiale, **sauf à respecter les conditions dérogatoires** prévues par le texte.

Heureusement, le CGI offre une **dérogation** : le report d’imposition peut être **maintenu** si votre holding s’engage à **réinvestir au moins 70 % du produit de cession (soit 6 300 000 €)** dans un délai de **3 ans à compter de la cession (février 2026 → février 2029)**.

---

### **2. Conditions à respecter pour bénéficier de la dérogation**
Pour que le report d’imposition soit préservé, le réinvestissement doit :
- **Être réalisé dans un délai de 3 ans** (jusqu’en **février 2029**).
- **Porter sur au moins 70 % du produit de cession** (soit **≥ 6 300 000 €**).
- **Être affecté à des moyens permanents d’exploitation** liés à une **activité éligible** (excluant la gestion de patrimoine immobilier ou les activités purement financières).

#### **Activités éligibles (Article 199 terdecies-0 A, 3° du CGI) :**
Le réinvestissement doit financer des **moyens permanents d’exploitation** pour une activité **commerciale, industrielle, artisanale, agricole ou libérale** (à l’exclusion des activités de gestion de patrimoine immobilier ou mobilière).

**Exemples concrets de réinvestissements éligibles :**
✅ **Acquisition d’une nouvelle société d’exploitation** (rachats de titres, apports en capital).
✅ **Financement d’investissements productifs** (machines, brevets, fonds de commerce) **dans une filiale opérationnelle**.
✅ **Souscription à des obligations convertibles en actions** (si liées à une activité éligible).
✅ **Investissement dans des actifs corporels ou incorporels** nécessaires à l’activité (ex : logiciels, matériel industriel).

❌ **À exclure :**
- Placements financiers (OPCVM, comptes à terme, etc.).
- Acquisition ou gestion d’immeubles (sauf si liés à une activité commerciale, ex : hôtel, clinique).
- Réinvestissement dans une société holding pure (sans activité opérationnelle).

---

### **3. Recommandations pratiques**
#### **a) Stratégie de réinvestissement**
1. **Identifier une cible éligible** :
   - **Acquisition d’une société opérationnelle** (ex : rachat d’une PME dans votre secteur).
   - **Création ou renforcement d’une filiale active** (apport en capital pour financer son développement).
   - **Investissement dans des actifs productifs** (ex : achat de matériel pour une filiale industrielle).

2. **Respecter le délai de 3 ans** :
   - Le réinvestissement doit être **effectué avant février 2029**.
   - **Conseil** : Agir rapidement pour éviter tout risque de dépassement (ex : signature d’un protocole d’acquisition d’ici fin 2026).

3. **Justifier le lien avec l’activité éligible** :
   - Le réinvestissement doit être **directement affectable à une activité commerciale/industrielle**.
   - **Exemple** : Si votre holding détient une filiale de production, un apport en capital pour moderniser son outil industriel serait éligible.

#### **b) Formalités à accomplir**
- **Engagement écrit** : Votre holding doit **formaliser son engagement de réinvestissement** (par exemple, dans une délibération du conseil d’administration ou un acte sous seing privé).
- **Preuves à conserver** :
  - Contrats d’acquisition/investissement.
  - Factures ou justificatifs des dépenses éligibles.
  - Comptes rendus de décision (pour prouver l’affectation des fonds).

#### **c) Optimisation fiscale complémentaire**
- **Étalement du réinvestissement** : Si vous ne trouvez pas une cible unique, vous pouvez **répartir les 6,3 M€ sur plusieurs investissements** (ex : 3 M€ en 2026, 3,3 M€ en 2027).
- **Utilisation de véhicules intermédiaires** : Si nécessaire, une **filiale opérationnelle** peut être créée pour porter les investissements.

---

### **4. Risques à éviter**
- **Délai non respecté** : Si le réinvestissement n’est pas réalisé à temps, le report d’imposition sera **remis en cause rétroactivement**, avec **pénalités de retard** (10 % + intérêts de retard).
- **Réinvestissement non éligible** : Un placement en OPCVM ou en immobilier locatif pur **ne suffira pas** et entraînera la taxation immédiate.
- **Preuves insuffisantes** : L’administration fiscale peut demander des **justificatifs** (contrats, affectation des fonds). Une **documentation solide** est indispensable.

---

### **5. Prochaines étapes**
1. **Audit des opportunités** :
   - Identifier des cibles d’acquisition ou des projets d’investissement dans votre secteur.
   - Évaluer leur éligibilité au regard du CGI.

2. **Structuration juridique** :
   - Si nécessaire, créer une **filiale opérationnelle** pour porter les investissements.
   - Rédiger l’**engagement de réinvestissement** (nous pouvons vous fournir un modèle).

3. **Suivi fiscal** :
   - Nous pouvons vous accompagner dans la **rédaction des actes** et la **vérification de l’éligibilité** des investissements.
   - **Conseil** : Faire valider le projet par l’administration fiscale via une **demande de rescrit** (article L. 80 B du Livre des Procédures Fiscales) pour sécuriser la position.

---

### **6. Conclusion**
Pour **conserver le report d’imposition**, votre holding doit **réinvestir au moins 6 300 000 € d’ici février 2029** dans des **moyens permanents d’exploitation liés à une activité éligible**. Les options les plus sûres sont :
- **L’acquisition d’une société opérationnelle**,
- **Le financement d’investissements productifs dans une filiale active**.

**Nous vous proposons :**
✔ Un **accompagnement personnalisé** pour identifier des cibles éligibles.
✔ La **rédaction des engagements et actes nécessaires**.
✔ Une **revue fiscale** pour sécuriser l’opération.

**Action immédiate recommandée** :
- **Prendre contact avec nous pour affiner la stratégie** (avant fin 2026 pour laisser le temps aux opérations).
- **Engager des discussions avec des cibles potentielles** ou préparer un plan d’investissement interne.

---
**Cordialement,**
[Votre Nom]
Avocat Fiscaliste
[Nom du Cabinet]
[Coordonnées]
[Signature]

---
**Annexe : Modèle d’engagement de réinvestissement (à adapter)**
*"La société [Nom de la Holding], représentée par [Nom], s’engage à réinvestir au moins 70 % du produit de la cession des titres de [Société Cédée], soit un montant minimal de 6 300 000 €, dans un délai de trois ans à compter du [date de cession], conformément à l’article 150-0 B ter du CGI, dans [préciser : acquisition de titres de [Société X], financement d’investissements productifs pour [Filiale Y], etc.]. Cet engagement est pris pour maintenir le bénéfice du report d’imposition sur la plus-value d’apport initiale."*


---

## C39  (39 sur 45)

**VOTRE CODE : ______________________________**

**Fait manquant :** La date de dépôt du projet au greffe. Le régime nouveau ne s'applique qu'aux opérations dont le projet a été déposé à compter du 1er juillet 2023.

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus directement aux
associes de la societe apporteuse, afin que chaque branche de la
famille detienne sa societe.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder :**

**Oui, sous réserve de la caractérisation d’une branche complète d’activité et du respect des conditions de l’article 210 B (adaptées).**

L’article 210-0 A, I, 4° du CGI inclut expressément dans le champ des apports partiels d’actifs éligibles les opérations dans lesquelles les titres de la société bénéficiaire sont remis **directement aux associés** de la société apporteuse (et non à cette dernière). L’opération projetée entre donc dans les prévisions du texte.

Le régime de faveur des articles 210 A et suivants (neutralité à l’IS : non-imposition des plus-values d’apport, reprise des écritures à la valeur comptable, etc.) est donc en principe applicable, à condition que :

- la branche industrielle constitue bien une **branche complète d’activité** (ensemble d’éléments d’actif et de passif d’une division autonome susceptible de fonctionner par ses propres moyens ; si la holding détient en réalité deux filiales opérationnelles, l’apport des titres de la filiale industrielle peut qualifier si cette participation représente une activité autonome) ;
- les autres conditions de l’article 210 B soient respectées (inscription à la valeur nette comptable chez la bénéficiaire, engagement de conservation des titres – qui pèse alors sur les associés attributaires –, soulte limitée le cas échéant, etc.).

**Points de vigilance à traiter dans le dossier :**

- Si l’attribution des titres de la nouvelle société n’est **pas proportionnelle** aux droits des associés (ce qui serait nécessaire pour que chaque branche familiale se retrouve immédiatement seule propriétaire de « sa » société), le régime de faveur au niveau des sociétés n’est pas automatiquement fermé, mais l’opération peut être requalifiée, au niveau des associés, en libéralité (droits de mutation à titre gratuit) ou générer des conséquences à l’IR. Une attribution inégalitaire doit être soigneusement justifiée et, le plus souvent, sécurisée.
- Qualification exacte de la « branche » (activité exercée directement ou via filiale ; holding animatrice ou non).
- Articulation avec le régime des plus-values des associés personnes physiques (150-0 B ter ou équivalent selon les cas) et éventuelle nécessité d’un rescrit.

En l’état des éléments communiqués, l’opération peut bénéficier du régime de faveur. Nous recommandons toutefois une analyse précise de la branche apportée et des modalités d’attribution avant de lancer les actes. Nous restons à votre disposition pour approfondir (projet de traité d’apport, rescrit, etc.).


---

## C40  (40 sur 45)

**VOTRE CODE : ______________________________**

**Fait manquant :** La date de dépôt du projet au greffe. Le régime nouveau ne s'applique qu'aux opérations dont le projet a été déposé à compter du 1er juillet 2023.

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus directement aux
associes de la societe apporteuse, afin que chaque branche de la
famille detienne sa societe.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder :**

Oui, **en principe**, l’opération envisagée peut relever du régime de faveur des articles 210 A et 210 B du CGI, y compris lorsque les titres de la société bénéficiaire sont remis **directement aux associés** de la société apporteuse.

Le texte que vous citez de l’article 210-0 A, I, 4° vise précisément cette hypothèse : l’apport partiel d’actif peut être rémunéré par des titres remis soit à la holding apporteuse, soit directement à ses associés. L’absence de détention transitoire des titres de la société industrielle par la holding ne fait donc pas obstacle, à elle seule, au régime.

Cela étant, il convient de distinguer trois niveaux d’analyse.

## 1. Le régime au niveau de la holding apporteuse

L’opération devra porter sur une **branche complète d’activité** au sens fiscal : une universalité autonome d’exploitation, comprenant l’ensemble des éléments d’actif et de passif nécessaires à l’exercice de l’activité industrielle.

Doivent notamment être transférés, selon les circonstances :

- les immobilisations industrielles ;
- les stocks et encours ;
- les contrats attachés à l’activité ;
- les salariés affectés à cette activité ;
- les créances, dettes et engagements correspondants ;
- les autorisations, marques, brevets, savoir-faire et moyens de financement nécessaires ;
- plus généralement, tous les éléments permettant à la société nouvelle de poursuivre l’activité industrielle de manière autonome.

Sous cette réserve, l’apport partiel d’actif peut bénéficier de plein droit du régime de l’article 210 B du CGI, qui renvoie aux mécanismes de l’article 210 A.

La société bénéficiaire devra notamment reprendre les valeurs fiscales des éléments apportés et souscrire les engagements fiscaux requis dans le traité d’apport : maintien des valeurs fiscales, calcul ultérieur des plus-values par référence aux valeurs historiques, reprise de certaines provisions et réserves, etc.

En conséquence, les plus-values latentes sur les actifs industriels apportés ne seraient pas immédiatement imposées chez la holding, sous réserve du respect effectif de ces obligations.

## 2. La remise directe des titres aux associés

La remise directe des actions de la société industrielle aux associés de la holding est expressément admise par l’article 210-0 A, I, 4°.

Il s’agit de l’opération usuellement qualifiée d’**apport-attribution** : la holding apporte une branche complète d’activité à une société nouvelle, mais les titres émis en contrepartie sont attribués directement à ses associés.

Cette modalité évite donc le schéma en deux temps consistant :

1. à remettre les titres de la nouvelle société à la holding ;
2. puis à les distribuer ou les attribuer aux associés.

Sur le principe, le régime de faveur de l’apport n’est pas perdu du seul fait de cette remise directe.

Au niveau des associés, il conviendra également de vérifier les conditions de l’article 115, 2 du CGI, qui permet, sous conditions, que l’attribution des titres représentatifs de l’apport ne soit pas traitée comme une distribution imposable.

## 3. Point d’attention déterminant : une séparation familiale « asymétrique »

C’est sur ce point que se situe la difficulté pratique.

Si les titres de la société industrielle sont remis à **tous les associés de la holding proportionnellement à leurs droits** dans celle-ci, le schéma est cohérent avec une opération d’apport-attribution fiscalement neutre : chaque associé conserve indirectement, puis directement, la même quote-part économique dans l’activité industrielle.

En revanche, votre objectif paraît être différent : vous envisagez que :

- une branche de la famille reçoive exclusivement les titres de la société industrielle ;
- l’autre branche de la famille conserve exclusivement l’activité de négoce au sein de la holding.

Une telle répartition est une **répartition asymétrique** des actifs entre les membres de la famille. Elle ne doit pas être confondue avec la seule possibilité, désormais prévue par l’article 210-0 A, de remettre directement les titres aux associés.

En effet, le texte autorise la remise directe aux associés ; il ne transforme pas, par lui-même, une transmission de valeur d’un groupe d’associés vers un autre en opération fiscalement neutre.

Une attribution des titres industriels à certains associés seulement, ou selon une clé différente de leurs droits dans la holding, soulève notamment les risques suivants :

- remise en cause de la neutralité au niveau des associés, avec qualification possible de distribution ;
- analyse d’un avantage occulte ou d’une libéralité entre associés si les valeurs ne sont pas strictement compensées ;
- conséquences en matière de droits de mutation à titre gratuit si l’opération emporte un transfert de valeur entre membres de la famille ;
- risque d’abus de droit ou, à tout le moins, nécessité de démontrer les motifs économiques et patrimoniaux propres de l’opération ;
- difficultés de droit des sociétés : respect de l’égalité entre associés, règles de majorité ou d’unanimité selon la forme sociale, intérêt social, rapport des commissaires et valorisations.

## Conclusion

L’apport de la branche industrielle à une société nouvelle, avec remise directe des titres de cette société aux associés de la holding, est bien une opération susceptible de relever des articles 210 A et 210 B du CGI, dès lors que :

1. l’activité industrielle constitue une branche complète et autonome ;
2. le traité d’apport prévoit les engagements fiscaux requis ;
3. la société bénéficiaire reprend les valeurs fiscales et obligations attachées aux actifs apportés ;
4. l’opération repose sur des motifs économiques réels et non principalement fiscaux.

En revanche, si l’objectif est que les deux branches familiales se répartissent définitivement et exclusivement les deux activités, il faut traiter séparément la question de l’**attribution asymétrique** des titres. Le régime des fusions et apports ne sécurise pas automatiquement cette seconde étape.

Avant toute mise en œuvre, il conviendrait donc de réaliser :

- une revue précise des droits de chacun dans la holding ;
- une valorisation indépendante des deux branches ;
- une analyse des mécanismes de compensation éventuels ;
- une étude du traitement fiscal des associés, y compris au regard de l’article 115 du CGI ;
- et, compte tenu de l’enjeu, une demande de rescrit ciblée si une attribution non proportionnelle est retenue.


---

## C41  (41 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

Monsieur, Maître,

Je vous remercie de votre confiance. Nous nous réunissons aujourd'hui pour analyser le projet de transmission de votre société par actions simplifiée (SAS) à vos deux enfants, et plus particulièrement l'éligibilité de cette opération au régime de faveur du Pacte Dutreil (article 787 B du Code général des impôts).

Voici mon analyse de votre situation, telle que je la présenterais pour sécuriser votre projet.

### 1. Sur les conditions formelles du Pacte Dutreil

À la lecture de votre dossier, les conditions formelles et de délais semblent parfaitement maîtrisées :
*   **L'Engagement Collectif de Conservation (ECC)** a été signé le 3 mars 2021. Au 25 octobre 2023, le délai minimal de deux ans est respecté.
*   **L'Engagement Individuel (EIC)** de quatre ans sera pris par vos enfants dans l'acte de donation.
*   **La fonction de direction** sera conservée par vous-même (le donateur) pendant les trois années suivant la transmission, ce qui est conforme aux exigences légales.

Cependant, le bénéfice du Pacte Dutreil ne repose pas uniquement sur ces engagements de durée. Il est strictement conditionné à **la nature de l'activité** exercée par la société. C'est sur ce point précis que se trouve l'écueil de votre projet.

### 2. Sur la nature de l'activité de la SAS (L'écueil majeur)

Votre SAS a pour activité la location de quarante appartements meublés. 

Il est vrai que sur le plan de l'impôt sur le revenu, la location meublée est considérée comme une activité commerciale (relevant des Bénéfices Industriels et Commerciaux - BIC, visés à l'article 35 du CGI). C'est souvent ce qui induit les dirigeants en erreur.

Toutefois, le texte de l'article 787 B du CGI applicable à la date de votre projet (25 octobre 2023) est très clair. Son deuxième alinéa précise :
> *"Pour l'application du premier alinéa du présent article, **n'est pas considérée comme une activité industrielle, commerciale**, artisanale, agricole ou libérale **l'exercice par une société d'une activité de gestion de son propre patrimoine mobilier ou immobilier**."*

L'activité de votre SAS consiste à détenir et exploiter son propre parc immobilier (40 appartements). Au sens de l'administration fiscale et de la loi applicable aux droits de mutation, il s'agit d'une activité à prépondérance civile (gestion de son propre patrimoine immobilier), et non d'une activité opérationnelle éligible.

**Le contexte législatif récent est d'ailleurs crucial pour votre date de signature :**
Il y a eu un vif débat jurisprudentiel au printemps 2023 sur ce sujet. Pour y mettre fin, le législateur (via la Loi de finances pour 2024) a définitivement et explicitement exclu les activités de location de locaux meublés à usage d'habitation du bénéfice du Pacte Dutreil. Cette exclusion s'applique aux transmissions intervenues **à compter du 17 octobre 2023**. 

Votre donation étant prévue le **25 octobre 2023**, elle tombe de plein fouet sous le coup de cette exclusion légale.

### 3. Conclusion sur l'application de l'article 787 B

**En l'état, ma réponse est non : l'exonération partielle de 75 % du Pacte Dutreil n'est pas applicable à votre donation.**

Si nous signons cet acte en appliquant le régime Dutreil, le risque de redressement fiscal est de 100 %. L'administration fiscale remettrait en cause l'abattement de 75 % sur la valeur de 20 000 000 euros, ce qui entraînerait un rappel de droits de donation de plusieurs millions d'euros, assorti d'intérêts de retard et de pénalités. En tant que votre conseil, je vous déconseille formellement de procéder ainsi.

### 4. Mes recommandations et solutions alternatives (Stratégie)

Puisque le Pacte Dutreil n'est pas applicable, une donation en pleine propriété de 20 M€ générerait un coût fiscal prohibitif (les droits de donation en ligne directe s'élevant rapidement à 45 % au-delà de 1,8 M€ par enfant).

Avec Maître, nous devons envisager d'autres leviers pour optimiser cette transmission :

1.  **La donation avec réserve d'usufruit (Démembrement) :**
    Vous avez 62 ans. Selon le barème de l'article 669 du CGI, la valeur de la nue-propriété de vos titres est de 50 %. Si vous donnez uniquement la nue-propriété à vos enfants, l'assiette taxable passe immédiatement de 20 M€ à 10 M€ (5 M€ par enfant). Vous conservez les dividendes et le contrôle (selon la rédaction des statuts).
2.  **La prise en charge des droits par le donateur :**
    Si vous disposez de liquidités personnelles, vous pouvez payer les droits de donation à la place de vos enfants. Ce paiement par le donateur n'est pas considéré comme une donation supplémentaire, ce qui constitue un excellent levier d'optimisation.
3.  **L'étalement ou le fractionnement :**
    Nous pouvons envisager des donations successives, bien que le délai de rappel fiscal soit de 15 ans.

Je me tiens à votre entière disposition, ainsi qu'à celle de votre notaire, pour chiffrer précisément ces alternatives et restructurer votre projet de transmission en toute sécurité fiscale.

Bien à vous,

**[Votre Signature d'Avocat Fiscaliste]**


---

## C42  (42 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

# Consultation fiscale – Cession de titres de SCI à prépondérance immobilière

## 1. Qualification de l'opération

La société cédée est une **personne morale à prépondérance immobilière (PMPI)** au sens de l'article 726, I, 2° du CGI :

- ses droits sociaux ne sont pas négociés sur un marché réglementé ou un système multilatéral de négociation ;
- son actif est **principalement constitué d'immeubles situés en France** (80 % > 50 %).

Cette qualification emporte application du régime spécifique des cessions de participations dans les PMPI.

---

## 2. Droit d'enregistrement exigible

### 2.1. Taux applicable

Le taux est de **5 %** en application de l'article 726, I, 2° du CGI.

Ce taux s'applique indépendamment de la qualité du cédant ou du cessionnaire (personne physique ou morale, résident ou non-résident).

### 2.2. Base d'imposition

La base est le **prix de cession exprimé** (soit 4 000 000 €), l'administration pouvant substituer la valeur vénale réelle si elle est supérieure (lutte contre la sous-évaluation).

### 2.3. Calcul

| Base | Taux | Droit dû |
|------|------|----------|
| 4 000 000 € | 5 % | **200 000 €** |

Le droit est perçu par le notaire lors du dépôt de l'acte à la formalité fusionnée et doit être versé au service de la publicité foncière compétent.

---

## 3. Mentions obligatoires de l'acte (art. 726, III, B du CGI)

L'acte authentique doit indiquer **expressément** les trois mentions suivantes :

### 3.1. Qualité de la société au regard de l'article 1655 ter

L'acte doit préciser si la SCI est une **société mentionnée à l'article 1655 ter** (société d'attribution, constituée en vue de l'attribution aux associés de la propriété ou de la jouissance d'immeubles).

> ⚠️ Une SCI classique de gestion n'est pas une société d'attribution. La mention doit donc expressément écarter cette qualification.

### 3.2. Droit de jouissance attaché aux participations (art. 728 CGI)

L'acte doit indiquer si les parts cédées **confèrent au cessionnaire, directement ou indirectement, un droit à la jouissance d'immeubles ou de fractions d'immeubles** au sens de l'article 728 (démembrement, jouissance privative, droit d'usage, etc.).

> ⚠️ Pour une SCI de gestion classique (parts purement financières), cette mention doit être négative.

### 3.3. Prise en charge de dettes par le cessionnaire

L'acte doit indiquer si le cessionnaire a acquitté ou s'engage à acquitter, **directement ou indirectement, des dettes contractées par la SCI auprès du cédant**, en précisant, le cas échéant, leur montant.

> ⚠️ À défaut d'une telle stipulation, mention expresse de l'absence de prise en charge de dettes intra-groupe.

---

## 4. Recommandations pratiques

1. **Recourir obligatoirement à un notaire français** : la cession étant signée en France le 20 mars 2024, l'authenticité est acquise ; le notaire procédera à l'enregistrement, à la publicité au greffe et, le cas échéant, à la mise à jour du registre des transferts.

2. **Provisionner 200 000 €** au titre du droit d'enregistrement, outre les honoraires du notaire, les frais de formalités et l'éventuelle contribution de sécurité immobilière (0,10 % du prix, due uniquement en cas de publicité foncière – *non applicable ici en principe, s'agissant de parts sociales et non d'une cession d'immeuble*).

3. **Vérifier l'absence de mécanisme assimilable à une cession d'immeuble déguisée** : cession des parts de SCI détenant l'usufruit temporaire ou la jouissance d'un bien social, clauses d'affectation privative, etc., qui pourraient entraîner une requalification.

4. **Anticiper l'incidence sur la plus-value** du cédant (distincte du droit d'enregistrement, mais à étudier en parallèle : régime des particuliers, durée de détention, abattements, surtaxes, etc.).

5. **Vérifier les stipulations statutaires** : agrément, préemption, plafonnement de la responsabilité, retrait – autant de points qui conditionnent la validité même de la cession.

---

## Synthèse

| Élément | Réponse |
|---------|---------|
| Nature du droit | Droit d'enregistrement sur cession de participations |
| Taux applicable | 5 % (art. 726, I, 2° CGI) |
| Montant dû | **200 000 €** |
| Forme de l'acte | Authentique (notaire français) |
| Mentions obligatoires | 3 mentions exprès (1655 ter, jouissance art. 728, dettes cédant) |
| Délai de dépôt | Dans le mois de la signature |

Je reste à votre disposition pour rédiger une note de consultation plus détaillée ou pour relire le projet d'acte avant signature, notamment au regard de l'exactitude des trois mentions expresses exigées par la loi.


---

## C43  (43 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

## Conclusion

**En principe, aucune retenue à la source ne devrait être prélevée sur les 20 millions d’euros**, sous réserve que la société luxembourgeoise :

- soit le **bénéficiaire effectif** de la distribution ;
- ait son siège de direction effective au Luxembourg ;
- soit effectivement assujettie à l’impôt luxembourgeois sur les collectivités, sans exonération subjective ;
- et que l’opération ne relève pas d’un montage abusif.

Le dossier justificatif devra être constitué avant la mise en paiement du 15 juin 2025.

## 1. Principe posé par l’article 119 bis, 2 du CGI

La distribution constitue, si elle est juridiquement prélevée sur des bénéfices ou réserves distribuables, un produit relevant des articles 108 et suivants du CGI.

La société luxembourgeoise ayant son siège hors de France, l’article 119 bis, 2 pose donc en principe une retenue à la source. À défaut d’exonération, son taux de droit interne serait de **25 %**, soit :

> **20 000 000 € × 25 % = 5 000 000 €**

L’exception mentionnée dans l’extrait fourni pour certains organismes de placement collectif étrangers ne concerne pas une société anonyme luxembourgeoise ordinaire.

## 2. Exonération « mère-fille » de l’article 119 ter du CGI

L’article 119 ter du CGI exonère de la retenue à la source les dividendes versés à une société mère établie dans l’Union européenne lorsque, notamment, celle-ci :

- est le bénéficiaire effectif des dividendes ;
- a son siège de direction effective dans l’Union européenne ;
- revêt l’une des formes visées par la directive européenne « mère-fille » — ce qui est en principe le cas d’une **société anonyme luxembourgeoise** ;
- est assujettie, sans option et sans exonération subjective, à l’un des impôts visés par cette directive, notamment l’**impôt luxembourgeois sur le revenu des collectivités** ;
- détient directement au moins **10 %** du capital de la société distributrice pendant au moins **deux ans**.

En l’espèce, la société mère détient directement **100 % du capital depuis cinq ans**. Les conditions de participation et de durée de détention sont donc satisfaites, sans nécessité de souscrire un engagement de conservation.

Le fait que les fonds distribués proviennent de la cession d’un actif est indifférent, dès lors que la distribution constitue bien, sur les plans juridique et comptable, une distribution de bénéfices ou de réserves.

## 3. Points restant à contrôler

### Bénéficiaire effectif

Il faut vérifier que la société luxembourgeoise dispose réellement des dividendes et n’est pas une simple société relais tenue, juridiquement ou en fait, de les retransmettre à un actionnaire ou à un créancier.

Une redistribution ultérieure ne suffit pas, à elle seule, à exclure la qualité de bénéficiaire effectif. En revanche, une obligation préexistante de reversement, l’absence d’autonomie décisionnelle ou une interposition purement artificielle créeraient un risque sérieux.

### Substance et clause anti-abus

L’exonération peut être refusée si la structure constitue un montage non authentique dont l’un des objectifs principaux est l’obtention indue de l’exonération. Il conviendra notamment d’examiner :

- les fonctions réellement exercées par la société mère ;
- la composition et le fonctionnement de ses organes de direction ;
- son autonomie financière et bancaire ;
- ses moyens humains et matériels, adaptés à son activité ;
- les motifs économiques de sa détention de la filiale française ;
- l’affectation envisagée des 20 millions d’euros.

Le fait que la participation soit détenue depuis cinq ans constitue un élément favorable, mais n’écarte pas à lui seul l’analyse anti-abus.

## 4. Convention fiscale franco-luxembourgeoise

À titre subsidiaire, l’article 10 de la convention fiscale franco-luxembourgeoise prévoit également une imposition à la source de **0 %** lorsque le bénéficiaire effectif est une société détenant directement au moins 5 % du capital pendant une période de 365 jours incluant la date de paiement.

Les conditions de participation seraient ici largement remplies. Cette protection conventionnelle demeure toutefois elle aussi subordonnée :

- à la qualité de bénéficiaire effectif ;
- à la résidence fiscale luxembourgeoise ;
- et au respect des dispositifs conventionnels anti-abus.

## 5. Recommandation opérationnelle

Avant le 15 juin 2025, la société française devrait obtenir et conserver au minimum :

- une attestation de résidence fiscale luxembourgeoise pour 2025 ;
- un extrait du registre du commerce et les statuts de la société mère ;
- une attestation d’assujettissement à l’impôt sur le revenu des collectivités ;
- les justificatifs de la détention directe de 100 % du capital depuis cinq ans ;
- une déclaration de la société mère confirmant sa qualité de bénéficiaire effectif et le respect des conditions de l’article 119 ter ;
- les éléments établissant son siège de direction effective et sa substance ;
- les formulaires conventionnels appropriés, notamment les formulaires **5000/5001**, si l’exonération conventionnelle est également invoquée ;
- la documentation démontrant la nature juridique de la somme distribuée.

### Avis

**Sous ces réserves, la distribution de 20 millions d’euros peut être mise en paiement sans retenue à la source française.**

Si la qualité de bénéficiaire effectif ou les conditions anti-abus ne pouvaient pas être établies, l’application du taux zéro serait compromise ; la retenue de droit interne pourrait alors atteindre **5 millions d’euros**, sauf autre protection conventionnelle effectivement disponible.


---

## C44  (44 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

**Objet : Consultation fiscale – Cession de titres d’une SCI à prépondérance immobilière – Droits d’enregistrement et contenu de l’acte**

**Maître [Votre Nom]**
Avocat fiscaliste
[Coordonnées du cabinet]

[Date]

**À l’attention de [Nom du client]**

Cher Monsieur [ou Madame],

Vous me consultez en vue de la cession, prévue le **20 mars 2024**, des titres d’une **société civile immobilière (SCI)** dont l’actif est constitué à **80 % d’immeubles situés en France**, pour un prix de **4 000 000 €**. Vous souhaitez connaître :
1. **Le droit d’enregistrement applicable** ;
2. **Les mentions obligatoires à insérer dans l’acte de cession**.

Je vous expose ci-dessous les règles applicables et les recommandations pour sécuriser cette opération.

---

### **1. Droit d’enregistrement applicable**
#### **a. Qualification de la SCI comme "personne morale à prépondérance immobilière" (PMPI)**
L’**article 726, I, 2° du CGI** soumet les cessions de participations dans des PMPI à un droit d’enregistrement de **5 %**, sous réserve des conditions suivantes :
- **Non-cotation** : Les titres de la SCI ne sont pas négociés sur un marché réglementé ou un système multilatéral de négociation (ce qui est le cas en l’espèce).
- **Prépondérance immobilière** : L’actif de la SCI doit être **principalement constitué d’immeubles ou de droits immobiliers situés en France** (ou de participations dans d’autres PMPI). La doctrine administrative (BOI-ENR-DMTOM-40-10-20) considère qu’un actif est "principalement" immobilier dès lors que les immeubles représentent **plus de 50 % de sa valeur**. Ici, avec **80 %**, la condition est remplie.
- **Exclusions** : La SCI ne relève pas des exceptions visées (organismes HLM, sociétés foncières agréées, etc.).

**Conclusion** : La cession est soumise au **droit de 5 %** (soit **200 000 €** pour un prix de 4 000 000 €).

#### **b. Territorialité et formalités**
- **Lieu de la cession** : Si l’acte est signé **en France**, il doit être enregistré dans le **délai d’un mois** auprès du service des impôts des entreprises (SIE) compétent. Si l’acte est signé **à l’étranger**, il doit être **reçu en la forme authentique par un notaire français** dans le même délai (art. 726, III-A du CGI).
- **Assiette du droit** : Le droit est calculé sur le **prix de cession** (4 000 000 €), sauf si la valeur vénale des titres est supérieure (auquel cas l’administration peut retenir cette dernière).

---

### **2. Mentions obligatoires dans l’acte de cession**
L’**article 726, III-B du CGI** impose d’insérer dans l’acte les informations suivantes, sous peine de **nullité de la formalité d’enregistrement** (et donc de risque de redressement) :

#### **a. Statut fiscal de la SCI (art. 726, III-B-1°)**
- **Mention expresse** : L’acte doit indiquer si la SCI est une **société visée à l’article 1655 ter du CGI** (société de copropriété d’immeubles bâtis). Si ce n’est pas le cas, une mention négative est requise (ex. : *"La société cédée n’est pas une société mentionnée à l’article 1655 ter du CGI"*).

#### **b. Droit à jouissance des immeubles (art. 726, III-B-2°)**
- **Mention expresse** : L’acte doit préciser si les titres cédés **confèrent au cessionnaire un droit à jouissance directe ou indirecte d’immeubles** (ex. : clause d’attribution en jouissance dans les statuts de la SCI). Si tel n’est pas le cas, une mention négative est nécessaire (ex. : *"Les participations cédées ne confèrent pas au cessionnaire un droit à la jouissance d’immeubles ou de fractions d’immeubles au sens de l’article 728 du CGI"*).

#### **c. Prise en charge de dettes (art. 726, III-B-3°)**
- **Engagement du cessionnaire** : L’acte doit indiquer si le cessionnaire **acquitte ou s’engage à acquitter des dettes de la SCI contractées auprès du cédant**. Si c’est le cas, le montant doit être précisé. Sinon, une mention négative est requise (ex. : *"Le cessionnaire n’acquitte ni ne s’engage à acquitter, directement ou indirectement, des dettes contractées par la société cédée auprès du cédant"*).

#### **d. Autres mentions recommandées**
Pour sécuriser l’opération, je vous conseille d’ajouter :
1. **La valeur des immeubles** : Une annexe à l’acte pourrait détailler la composition de l’actif de la SCI (valeur des immeubles vs. autres actifs) pour justifier la prépondérance immobilière.
2. **La déclaration de non-cotation** : *"Les titres de la société cédée ne sont pas négociés sur un marché réglementé ou un système multilatéral de négociation au sens des articles L. 421-1 et L. 424-1 du code monétaire et financier."*
3. **L’engagement de paiement du droit** : *"Le cessionnaire s’engage à acquitter le droit d’enregistrement de 5 % dû au titre de la présente cession."*

---

### **3. Recommandations pratiques**
1. **Audit préalable** :
   - Vérifier que la SCI n’a pas **cessé d’être à prépondérance immobilière** au cours de l’année précédant la cession (ex. : vente d’un immeuble réduisant la part immobilière à moins de 50 %).
   - S’assurer que les immeubles sont bien **situés en France** (les immeubles à l’étranger ne sont pas pris en compte pour la prépondérance).

2. **Rédaction de l’acte** :
   - **Faire rédiger l’acte par un notaire** (obligatoire si la cession a lieu à l’étranger, recommandé en France pour sécuriser les mentions fiscales).
   - **Annexer un état de l’actif** de la SCI au jour de la cession (ou à défaut, au 31/12/2023) pour justifier la prépondérance immobilière.

3. **Paiement du droit** :
   - Le droit de **5 %** (200 000 €) est dû par le **cessionnaire**, sauf clause contraire. Prévoir une **retenue à la source** si le cédant est non-résident (pour éviter un contentieux avec l’administration).

4. **Déclaration** :
   - L’acte doit être **enregistré dans le mois** de sa signature (délai impératif). À défaut, l’administration peut exiger un **droit complémentaire de 0,1 %** (art. 635 du CGI) et des **pénalités de retard**.

---

### **4. Risques en cas de non-respect**
- **Nullité de l’enregistrement** : Si les mentions obligatoires (art. 726, III-B) sont omises, l’administration peut refuser l’enregistrement et exiger un **droit de 5 % majoré des pénalités**.
- **Redressement fiscal** : Si la SCI est à tort considérée comme non-PMPI, l’administration peut requalifier la cession et appliquer un **droit de 2,5 %** (taux de droit commun pour les cessions de parts sociales, art. 726, I-1° du CGI) **avec intérêts de retard et pénalités**.
- **Responsabilité du notaire/avocat** : En cas d’erreur dans la rédaction de l’acte, le professionnel engage sa responsabilité civile et disciplinaire.

---

### **5. Proposition d’action**
Pour sécuriser cette cession, je vous propose :
1. **Un audit fiscal** de la SCI pour confirmer sa qualification de PMPI et vérifier l’absence de risques (dettes, jouissance des immeubles, etc.).
2. **La rédaction ou la relecture de l’acte de cession** par mes soins, en collaboration avec votre notaire, pour intégrer toutes les mentions obligatoires.
3. **L’accompagnement lors de l’enregistrement** de l’acte et du paiement du droit.

Je reste à votre disposition pour échanger sur ces points et vous assister dans la finalisation de cette opération.

Veuillez agréer, Cher Monsieur [ou Madame], l’expression de mes salutations distinguées.

**[Votre Nom]**
Avocat fiscaliste
[Coordonnées du cabinet]

---
**Annexe** : Extrait de l’article 726 du CGI (fourni dans votre demande).


---

## C45  (45 sur 45)

**VOTRE CODE : ______________________________**

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

**Reponse a coder :**

## 1. Droit d’enregistrement

La SCI est une **personne morale à prépondérance immobilière** au sens de l’article 726, I, 2° du CGI dès lors que :

- ses parts ne sont pas négociées sur un marché réglementé ou un système multilatéral de négociation ;
- son actif est principalement constitué d’immeubles situés en France — le seuil de 80 % satisfait cette condition ;
- elle ne relève pas de l’une des exclusions prévues pour certains organismes de logement social.

La cession est donc soumise au droit d’enregistrement de **5 %**.

Sous réserve que le prix de 4 000 000 € constitue l’intégralité de la contrepartie, qu’il n’existe aucune charge augmentative du prix et que la valeur réelle des titres ne soit pas supérieure :

> **4 000 000 € × 5 % = 200 000 €**

Le droit d’enregistrement dû est donc de **200 000 €**.

Il conviendra notamment de vérifier si le cessionnaire reprend ou acquitte une dette de la SCI envers le cédant, par exemple un compte courant d’associé : une telle opération doit être mentionnée dans l’acte et peut nécessiter un examen de l’assiette du droit.

## 2. Mentions obligatoires de l’acte

L’acte doit indiquer **expressément**, y compris par une réponse négative, les trois éléments suivants :

1. **Si la SCI est ou non une société relevant de l’article 1655 ter du CGI** ;
2. **Si les titres cédés confèrent ou non au cessionnaire, directement ou indirectement, un droit à la jouissance d’un immeuble ou d’une fraction d’immeuble au sens de l’article 728 du CGI** ;
3. **Si le cessionnaire a acquitté ou s’engage à acquitter, directement ou indirectement, des dettes contractées par la SCI auprès du cédant** et, dans l’affirmative, le montant de ces dettes.

Une clause pourrait être rédigée ainsi, à adapter après vérification :

> « Les parties déclarent expressément que :  
> – la Société [est/n’est pas] une société mentionnée à l’article 1655 ter du code général des impôts ;  
> – les parts cédées [confèrent/ne confèrent pas] au Cessionnaire, directement ou indirectement, un droit à la jouissance d’immeubles ou de fractions d’immeubles au sens de l’article 728 du même code ;  
> – le Cessionnaire [n’a acquitté et ne s’engage à acquitter aucune dette/a acquitté ou s’engage à acquitter les dettes suivantes] contractée(s) par la Société auprès du Cédant : […], pour un montant total de […] euros. »

Il est également recommandé que l’acte rappelle la qualification de société à prépondérance immobilière et les éléments qui la justifient.

Enfin, si la cession est réalisée à l’étranger, elle devra être constatée, dans le délai d’un mois, par un **acte authentique reçu par un notaire exerçant en France**. Sous réserve de ce cas particulier, l’acte signé le 20 mars 2024 devra être présenté à l’enregistrement dans le délai légal d’un mois.

