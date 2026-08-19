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

Portez une valeur par cellule dans `stratifie2_saisie.csv`, en face de son etiquette.
N'ouvrez pas `reference_scellee.json` avant d'avoir fini : il contient le codage
du modele, que vous ne devez pas connaitre en codant.


---

## T01

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

**Sous réserve des vérifications précisées ci-dessous, aucune retenue à la source française ne devrait être due** sur la distribution de 20 000 000 € mise en paiement le 15 juin 2025.

L’article 119 bis, 2 du CGI pose certes le principe d’une retenue à la source sur les distributions versées à un bénéficiaire établi hors de France. Toutefois, la distribution devrait bénéficier de l’**exonération “mère-fille” prévue par l’article 119 ter du CGI**, qui transpose la directive 2011/96/UE.

## Conditions de l’exonération

Les conditions paraissent remplies au vu des informations communiquées :

- la société mère est une **société anonyme luxembourgeoise**, forme éligible ;
- elle est établie dans un État membre de l’Union européenne ;
- elle est soumise à l’impôt luxembourgeois sur les sociétés, en principe sans option et sans exonération ;
- elle détient directement **100 %** du capital de la société française, soit davantage que le seuil légal de 10 % ;
- cette participation est détenue depuis **cinq ans**, soit au-delà de la durée minimale de deux ans.

Il conviendra également de confirmer que :

1. la société française distributrice est passible de l’impôt sur les sociétés au taux normal ;
2. la distribution n’est pas fiscalement déductible du résultat de la société française ;
3. la société luxembourgeoise a son siège de direction effective dans l’Union européenne et n’est pas considérée, en vertu d’une convention fiscale, comme résidente d’un État tiers ;
4. elle est le **bénéficiaire effectif** des sommes, c’est-à-dire qu’elle n’agit pas comme simple mandataire, fiduciaire ou société relais tenue de reverser les fonds à un tiers ;
5. la structuration ne constitue pas un montage non authentique ayant pour objectif principal, ou parmi ses objectifs principaux, l’obtention indue de l’exonération.

La seule qualité d’actionnaire à 100 % ne suffit pas, à elle seule, à établir la qualité de bénéficiaire effectif. Il faut notamment examiner l’existence d’engagements de reversement, le financement du groupe, les flux concomitants et la substance fonctionnelle de la société luxembourgeoise.

## Conséquences chiffrées

Si l’ensemble de ces conditions est satisfait :

- distribution brute : **20 000 000 €** ;
- retenue à la source française : **0 €** ;
- montant versé à la société luxembourgeoise : **20 000 000 €**.

À défaut d’exonération, le taux interne applicable à une personne morale serait en principe de **25 %**, soit une retenue de **5 000 000 €**. La convention fiscale franco-luxembourgeoise pourrait alors, sous réserve notamment de la qualité de bénéficiaire effectif et des formalités requises, limiter cette retenue à **5 %**, soit **1 000 000 €**, compte tenu de la participation détenue depuis plus de 365 jours.

## Formalités et pièces à réunir avant le 15 juin 2025

Afin d’appliquer l’exonération dès la mise en paiement, nous recommandons d’obtenir avant cette date :

- un certificat de résidence fiscale luxembourgeois valable pour 2025 ;
- une attestation de soumission à l’impôt luxembourgeois sur les sociétés sans exonération ;
- un extrait du registre de commerce luxembourgeois et les statuts ;
- les justificatifs de la détention de 100 % depuis cinq ans ;
- une attestation de bénéficiaire effectif ;
- une attestation relative au respect des conditions de l’article 119 ter ;
- une note documentant la substance de la société mère et l’absence d’obligation juridique ou économique de reverser la distribution.

**Avis :** sur les faits indiqués, l’exonération de retenue à la source est applicable en principe. Elle ne devra toutefois être mise en œuvre qu’après validation de la qualité de bénéficiaire effectif de la société luxembourgeoise et accomplissement des formalités justificatives avant le paiement.

---

## T02

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

**Objet : Analyse du report d’imposition dans le cadre de la cession de titres par votre holding – Application de l’article 150-0 B ter du CGI**

**À l’attention de [Nom du client],**
**De la part de [Votre nom], Avocat fiscaliste**

---

### **1. Contexte et problématique**
Votre holding (détentrice à 100 % des titres) a cédé le **10 novembre 2025** des titres d’une société d’exploitation pour un montant de **9 000 000 €**, moins de **3 ans** après leur apport par vos soins. Vous envisagez de **réinvestir** ce produit dans une société dédiée à l’achat, la rénovation et la revente d’immeubles (activité de *marchand de biens*).

La question centrale est de savoir si ce **réinvestissement** permet de **maintenir le report d’imposition** initialement obtenu lors de l’apport des titres à la holding, conformément à l’**article 150-0 B ter, I, 2° du CGI**.

---

### **2. Rappel du régime de report d’imposition (article 150-0 B ter)**
L’apport de titres à une holding peut bénéficier d’un **report d’imposition** de la plus-value réalisée à l’occasion de l’apport (sous conditions, notamment de détention minimale des titres apportés).
Ce report est **remis en cause** si :
- La holding cède les titres **dans un délai de 3 ans** à compter de l’apport (sauf exceptions).

**Exception prévue à l’article 150-0 B ter, I, 2° :**
Le report est **maintenu** si la holding :
1. **Cède les titres dans les 3 ans** de l’apport (ce qui est votre cas),
2. **S’engage à réinvestir au moins 60 % du produit de cession** (soit **5 400 000 €** dans votre cas),
3. **Dans un délai de 2 ans** à compter de la cession (soit avant le **10 novembre 2027**),
4. **Dans des actifs éligibles**, à savoir :
   > *"le financement de moyens permanents d’exploitation affectés à son activité commerciale, industrielle, artisanale, libérale, agricole ou financière"* (CGI, art. 150-0 B ter, I, 2° a).

**Exclusion expresse** :
Les *"activités de gestion de son propre patrimoine mobilier ou immobilier"* sont **exclues** du bénéfice de cette dérogation.

---

### **3. Analyse de votre projet de réinvestissement**
Votre projet consiste à investir dans une société dont l’activité est :
- **L’achat d’immeubles**,
- **Leur rénovation**,
- **Leur revente** (activité de *marchand de biens*).

#### **Qualification juridique de l’activité**
- **Activité commerciale** : La jurisprudence et la doctrine fiscale considèrent que l’activité de **marchand de biens** (achat pour revendre après transformation) relève bien du **secteur commercial** (au sens des **articles 34 et 35 du CGI**).
  - Exemple : CE, 19 juillet 1985, n° 44.844 (activité de lotisseur-marchand de biens = commerciale).
  - L’administration fiscale admet généralement cette qualification (BOI-BIC-PVMV-30-20-10, § 10).

- **Exclusion de la "gestion de patrimoine"** :
  L’activité de **marchand de biens** ne se limite pas à la **simple gestion de patrimoine immobilier** (qui serait exclue). Elle implique une **transformation active** (rénovation) et une **revente dans un but lucratif**, ce qui la distingue de la gestion passive.

#### **Éligibilité du réinvestissement**
Pour que le réinvestissement soit valable :
1. **Forme du réinvestissement** :
   - Le produit de cession (9 M€) doit financer des **"moyens permanents d’exploitation"** de la société cible.
   - Cela peut inclure :
     - **Apport en capital** à la société de marchand de biens (si les fonds sont affectés à son exploitation),
     - **Prêt participatif** ou **compte courant d’associé** (si les fonds sont utilisés pour l’activité commerciale).
   - **À exclure** : Un simple placement financier ou l’achat d’immeubles en direct par la holding (ce serait de la gestion de patrimoine).

2. **Preuve de l’affectation** :
   - Il faudra **documenter** que les fonds réinvestis servent bien à financer l’activité commerciale (ex : achat de stocks, travaux de rénovation, frais de structure de la société de marchand de biens).
   - Un **engagement écrit** de la holding (délibération du conseil d’administration ou de l’associé unique) sera nécessaire pour formaliser l’affectation.

3. **Délai** :
   - Le réinvestissement doit intervenir **avant le 10 novembre 2027** (2 ans après la cession).

---

### **4. Risque fiscal et recommandations**
#### **Risque principal : Requalification en "gestion de patrimoine"**
- Si l’administration fiscale estime que la société cible se livre en réalité à de la **simple gestion immobilière** (sans activité commerciale caractérisée), le report d’imposition pourrait être **remis en cause**.
- **Exemple de risque** :
  - Si la société achète des immeubles, les rénove **superficiellement**, et les revend après plusieurs années sans réelle plus-value liée à une activité industrielle ou commerciale, l’administration pourrait contester la qualification.

#### **Recommandations pour sécuriser le dispositif**
1. **Structurer la société cible comme un vrai marchand de biens** :
   - **Objet social clair** : Mention explicite de l’achat, rénovation et revente d’immeubles.
   - **Activité effective** :
     - Réalisations de travaux **substantiels** (et non cosmétiques),
     - Rotation rapide des biens (éviter une détention longue),
     - Comptabilité distincte (suivi des coûts de rénovation, marge commerciale).
   - **Immatriculation** au **registre du commerce et des sociétés (RCS)** en tant que marchand de biens.

2. **Preuves du réinvestissement** :
   - **Délibération de la holding** :
     - Décision formelle de réinvestir **au moins 60 % du produit** (5,4 M€) dans la société cible,
     - Précision que les fonds serviront à financer son activité commerciale.
   - **Convention de compte courant ou prêt** :
     - Si le réinvestissement passe par un prêt, prévoir des **clauses d’affectation** aux besoins d’exploitation.
   - **Suivi comptable** :
     - Tenir une **traçabilité** des fonds réinvestis (ex : virement dédié, utilisation fléchée).

3. **Respect du délai de 2 ans** :
   - Le réinvestissement doit être **effectif** avant le 10/11/2027.
   - **Attention** : Un simple engagement ne suffit pas ; il faut que les fonds soient **déjà investis** (ex : apport en capital réalisé, prêt accordé).

4. **Consultation préalable de l’administration (optionnel mais recommandé)** :
   - Une **demande de rescrit** (article L. 80 B du Livre des Procédures Fiscales) peut être déposée pour sécuriser la position de l’administration sur :
     - La qualification de l’activité de la société cible,
     - L’éligibilité du réinvestissement au sens de l’article 150-0 B ter.

---

### **5. Conclusion et synthèse**
| **Critère**               | **Votre situation**                          | **Conformité** |
|---------------------------|---------------------------------------------|----------------|
| Cession dans les 3 ans    | Oui (10/11/2025)                            | ✅             |
| Réinvestissement ≥ 60 %   | 5,4 M€ sur 9 M€ (soit 60 %)                  | ✅             |
| Délai de 2 ans            | Avant le 10/11/2027                         | ✅ (à respecter) |
| Activité éligible         | Marchand de biens (commerciale)             | ✅ **Sous réserve** |
| Exclusion gestion patrimoine | Activité active (rénovation + revente)    | ✅ **Si bien documenté** |

**→ Le réinvestissement dans une société de marchand de biens **peut** permettre de maintenir le report d’imposition, **à condition que** :**
1. L’activité de la société cible soit **clairement commerciale** (et non de la gestion de patrimoine),
2. Les fonds soient **effectivement affectés** à son exploitation,
3. Les **preuves** (délibérations, comptabilité, objet social) soient **solides**.

**→ Risque résiduel** : Si l’administration conteste la qualification commerciale, le report pourrait être remis en cause. Une **sécurisation préalable** (rescrit) est donc conseillée.

---
### **6. Prochaines étapes proposées**
1. **Finaliser la structure de la société cible** (objet social, immatriculation RCS).
2. **Préparer les documents de réinvestissement** (délibération, convention de prêt/apport).
3. **Engager le réinvestissement avant le 10/11/2027** (idéalement dès que possible).
4. **Envisager un rescrit** pour sécuriser la position fiscale (délai de réponse : ~6 mois).

**Je reste à votre disposition pour :**
- Rédiger les actes nécessaires (délibération, convention),
- Vous accompagner dans une demande de rescrit,
- Analyser plus en détail la structure de la société cible.

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées du cabinet]

---

## T03

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

Bonjour Monsieur, cher Confrère (Maître),

Je vous remercie de votre consultation. J'ai pris attentivement connaissance des éléments de votre dossier concernant le projet de transmission de votre SAS à vos deux enfants.

Je vais être direct : en l'état actuel de la situation et de la nature de votre société, l'exonération partielle de 75 % du Pacte Dutreil (article 787 B du CGI) **n'est malheureusement pas applicable**. 

Si nous signons cet acte en appliquant le régime Dutreil, le risque de redressement fiscal est, selon moi, certain.

Voici l'analyse juridique qui motive ma position, ainsi que les pistes que nous pouvons explorer avec votre notaire pour optimiser cette transmission.

### 1. L'analyse juridique : le piège de la location meublée

Sur le plan formel, vous avez fait un excellent travail d'anticipation. L'engagement collectif signé en 2021 est valide, les enfants sont prêts à signer leur engagement individuel, et vous conservez la présidence. Les conditions "mécaniques" du Pacte Dutreil sont remplies.

Cependant, le blocage se situe sur la **condition de fond : la nature de l'activité de la société.**

Votre SAS détient et exploite quarante appartements meublés. Il est vrai que sur le plan de l'impôt sur le revenu, la location meublée est une activité commerciale relevant de l'article 35 du CGI (Bénéfices Industriels et Commerciaux). C'est souvent ce qui induit les dirigeants en erreur.

Mais pour l'application des droits de mutation (le Pacte Dutreil), le texte de l'article 787 B que vous visez est très clair dans son deuxième alinéa : 
> *"n'est pas considérée comme une activité industrielle, commerciale [...] l'exercice par une société d'une activité de gestion de son propre patrimoine mobilier ou immobilier."*

L'administration fiscale, confortée par la jurisprudence récente de la Cour de cassation et du Conseil d'État, considère de manière constante que **la location meublée à usage d'habitation constitue la gestion par la société de son propre patrimoine immobilier**. Elle revêt donc un caractère civil pour l'application de l'impôt sur le patrimoine, et ce, même si elle est fiscalisée dans la catégorie des BIC.

Par conséquent, votre SAS ne remplit pas la condition d'activité exigée par l'article 787 B du CGI.

### 2. Les conséquences financières

Si vous donnez la pleine propriété des titres (20 000 000 €) à vos deux enfants (10 000 000 € chacun) sans le bénéfice du Pacte Dutreil, la taxation se fera au barème progressif des droits de donation en ligne directe (qui monte jusqu'à 45 %). 

Après l'abattement de 100 000 € par enfant, le coût fiscal de l'opération s'élèverait à environ **4,4 millions d'euros par enfant**, soit près de 8,8 millions d'euros au total.

### 3. Mes recommandations et stratégies alternatives

Puisque la voie du Pacte Dutreil est fermée pour cette société, nous devons, avec votre notaire, envisager d'autres leviers d'optimisation fiscale :

**A. La donation avec réserve d'usufruit (Démembrement)**
Vous avez 62 ans. Selon le barème fiscal (article 669 du CGI), la valeur de la nue-propriété de vos titres est de 50 % de leur valeur en pleine propriété. 
Si vous donnez uniquement la nue-propriété à vos enfants et conservez l'usufruit (les dividendes/loyers), l'assiette taxable passe de 20 M€ à 10 M€. Les droits de donation seraient divisés par deux (environ 2,1 M€ par enfant). Au moment de votre décès, l'usufruit s'éteindra et vos enfants deviendront pleins propriétaires sans aucun droit supplémentaire à payer.

**B. La prise en charge des droits par le donateur**
Si vous disposez de liquidités personnelles, vous pouvez payer vous-même les droits de donation à la place de vos enfants. L'administration fiscale ne considère pas ce paiement comme une donation supplémentaire. C'est un excellent moyen de réduire votre patrimoine taxable futur tout en soulageant vos enfants.

**C. La donation de titres avec soulte ou étalement**
Si les enfants doivent payer les droits, nous pouvons envisager des mécanismes de distribution de réserves de la SAS (si elle en a) pour les aider à financer la fiscalité, bien que cela génère une imposition (flat tax) qu'il faudra modéliser.

### Conclusion

Je vous déconseille formellement de procéder à cette donation sous le régime de l'article 787 B du CGI le 25 octobre prochain. Le risque de requalification avec pénalités est trop élevé.

Je me tiens à votre entière disposition, ainsi qu'à celle de Maître, pour modéliser financièrement la piste de la donation en démembrement de propriété, qui me semble être la solution la plus protectrice et la plus efficace dans votre situation actuelle.

Bien à vous,

**[Votre Signature d'Avocat Fiscaliste]**

---

## T04

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

**Note d'analyse – Pacte Dutreil (CGI, art. 787 B) – Projet de donation du 5 octobre 2023**

---

## I. Réponse en bref

Sur le papier, le montage est bien construit : engagement collectif en cours depuis plus de deux ans, engagements individuels pris par chaque donataire, maintien d'une fonction de direction éligible pendant trois ans. **Ces conditions paraissent satisfaites, sous réserves de vérification.**

Mais l'exonération se heurte à un obstacle potentiellement rédhibitoire, qui se situe en amont : **la condition d'activité opérationnelle de la société**. Une SAS qui « possède quarante appartements meublés » exerce vraisemblablement une activité de location meublée. Or, sauf exploitation para-hôtelière caractérisée, la location meublée **n'est pas une activité commerciale au sens de l'article 787 B**. Si tel est le cas, l'exonération est exclue, quand bien même toutes les autres conditions seraient réunies.

C'est ce point qu'il faut trancher **avant** toute signature.

---

## II. Le point déterminant : la nature de l'activité

- L'article 787 B exige une société ayant une activité **industrielle, commerciale, artisanale, agricole ou libérale**. La forme commerciale de la SAS ne suffit pas : c'est la nature réelle de l'activité qui commande. Une société commerciale par la forme peut exercer une activité civile de gestion patrimoniale.
- Certes, la location meublée relève des BIC au plan fiscal. Mais pour le pacte Dutreil, le juge et l'administration exigent une **exploitation commerciale effective** : la location meublée simple, même exercée à titre professionnel (LMP), est assimilée à la gestion d'un patrimoine privé et ne qualifie pas (**CE, 9 juillet 2021, n° 447299** ; BOI-ENR-DMTG-10-20-20-20).
- N'est éligible que l'exploitation s'apparentant à de la **para-hôtellerie**, c'est-à-dire la fourniture, en sus de l'hébergement, de services du type : accueil de la clientèle, fourniture du petit-déjeuner, fourniture du linge de maison, nettoyage régulier des locaux (en pratique, au moins trois de ces prestations, rendus avec des moyens propres).

**Questions à trancher immédiatement :** quelle est la nature des conventions d'occupation (baux meublés classiques ? baux mobilité ? location saisonnière ?) ; quelles prestations sont réellement fournies ; la société emploie-t-elle du personnel ; les recettes sont-elles soumises à TVA (indice fort de para-hôtellerie, la location meublée nue de services en étant exonérée) ; y a-t-il un classement « meublé de tourisme » ou une exploitation type résidence de tourisme ?

Si l'exploitation se limite à encaisser des loyers meublés, la condition d'activité **n'est pas remplie** : l'exonération est vouée à l'échec, avec un risque de reprise massive en cas de contrôle.

---

## III. Les autres conditions : a priori satisfaites, sous réserves

**1. Engagement collectif (art. 787 B, 1° et 885 I bis).** Seuils pour société non cotée : 17 % des droits financiers et 34 % des droits de vote – la totalité des droits les dépasse. Durée minimale de deux ans et engagement en cours au jour de la transmission : signé le 3 mars 2021, il court depuis 2 ans et 7 mois. **Points à vérifier** : l'engagement « collectif » suppose **au moins deux signataires** ; si votre client détient seul 100 % des titres, il ne peut pas exister – il faut identifier les cosignataires. Vérifier aussi la date certaine et la portée à la connaissance de la société.

**2. Engagements individuels de conservation (art. 787 B, 2°).** Pris par chaque enfant dans l'acte : conforme. Durée de **quatre ans à compter du terme de l'engagement collectif** (ou de la donation si celui-ci est déjà échu – vérifier la durée contractuelle de l'engagement du 3 mars 2021). Toute cession par un enfant avant le terme remet en cause l'exonération sur les titres cédés, sauf exceptions limitées (cession à un co-donataire reprenant l'engagement, licenciement, invalidité, décès).

**3. Fonction de direction (art. 787 B, 3°).** La condition peut être remplie alternativement par un donataire **ou par un associé signataire de l'engagement collectif** : le donateur, signataire, qui conserve la présidence, peut donc la satisfaire – c'est d'ailleurs le schéma classique admis par l'administration. La présidence de SAS est une fonction éligible. Deux vigilances : (i) la fonction doit être maintenue **jusqu'au 5 octobre 2026** et votre client doit y exercer son **activité principale** (rémunération de la société > 50 % de ses revenus professionnels) ; (ii) à 62 ans, un départ à la retraite avant le terme ferait sauter l'exonération – il est prudent d'anticiper la relève par l'un des enfants.

**4. Divers.** Siège social dans l'UE/EEE : à confirmer. SAS : société par actions éligible. L'acte authentique devra mentionner expressément les engagements et être enregistré dans le mois. Aucune condition d'âge du donateur n'existe dans le 787 B (ne pas confondre avec l'ancien article 790, abrogé en 2019). La donation des titres n'interrompt pas l'engagement collectif dès lors que les donataires prennent l'engagement individuel.

---

## IV. Enjeu financier (ordres de grandeur, abattements de 100 000 € supposés disponibles)

| | Avec exonération 75 % | Sans exonération |
|---|---|---|
| Assiette taxable par enfant | 2 400 000 € | 9 900 000 € |
| DMTG par enfant | ≈ 842 000 € | ≈ 4 217 000 € |
| **Total (deux enfants)** | **≈ 1 685 000 €** | **≈ 8 435 000 €** |

L'enjeu de l'exonération avoisine **6,75 M€** : il justifie à lui seul de ne rien précipiter.

---

## V. Recommandations

1. **Caractériser l'activité avant tout acte** : production des baux, factures, descriptif des prestations, masse salariale, régime de TVA.
2. **Si l'exploitation est réellement para-hôtelière** : constituer le dossier de preuve et solliciter un **rescrit préalable** (LPF, art. L. 80 B, 6°) – fortement recommandé vu l'enjeu ; l'administration répond en principe sous trois mois.
3. **Si l'exploitation est une location meublée simple** : l'exonération n'est pas acquise. Deux voies : conversion réelle de l'exploitation en activité para-hôtelière (exercée effectivement, avec moyens, avant la donation – toute conversion de complaisance serait contestée), puis acte ; ou stratégie alternative sans 787 B (donation-partage, démembrement).
4. **Sécuriser la direction** : vérifier la rémunération du client et sa prépondérance ; prévoir la désignation d'un enfant en relais avant octobre 2026.
5. **Vérifier les antérieurs** : donations de moins de 15 ans (abattements), origine des titres (apports en report d'imposition le cas échéant).
6. Recommander une **donation-partage** pour figer la valeur entre les deux enfants.

Je me tiens à votre disposition pour examiner les baux et conventions d'exploitation dès réception.

---

## T05

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

**Objet : Analyse de la légalité de l’application du taux réduit de TVA (5,5 %) sur le chantier du 15 avril 2025 – Réponse à la proposition de rectification**

**Maître [Votre Nom]**
Avocat fiscaliste
[Coordonnées du cabinet]

À l’attention de [Nom du gérant],
[Nom de l’entreprise de plomberie]
[Adresse]

**[Date]**

**Réf. : Dossier [numéro de dossier] – Réponse à la proposition de rectification (TVA à 5,5 % vs 20 %)**

Cher Monsieur [Nom du gérant],

Je vous remercie de m’avoir consulté sur la proposition de rectification notifiée par l’administration fiscale concernant l’application du taux réduit de TVA (5,5 %) sur le chantier de rénovation énergétique réalisé le **15 avril 2025** (installation d’une chaudière pour un montant de **8 500 € HT**). Je vous expose ci-dessous une analyse détaillée de la situation, ainsi que les arguments juridiques à opposer à l’administration pour contester la rectification.

---

### **1. Rappel des faits et du litige**
Votre entreprise a facturé l’installation d’une chaudière dans une maison de **15 ans**, occupée par son propriétaire, en appliquant le **taux réduit de 5,5 %** (au lieu de 20 %). L’administration fiscale conteste ce taux et exige le paiement de la différence (soit **14,5 % de 8 500 € = 1 232,50 €**), au motif que les conditions du **CGI, art. 278-0 bis A** ne seraient pas remplies.

---

### **2. Analyse juridique : le taux de 5,5 % était-il applicable ?**
L’article **278-0 bis A du CGI** (dans sa version en vigueur au 15 avril 2025) prévoit un taux réduit de 5,5 % pour les **prestations de rénovation énergétique**, sous réserve de trois conditions cumulatives (I) et d’une exclusion spécifique (III bis) :

#### **A. Conditions cumulatives du I (taux à 5,5 %)**
1. **Locaux achevés depuis au moins 2 ans** :
   - La maison avait **15 ans** à la date des travaux → **Condition remplie**.
2. **Usage d’habitation à l’issue des travaux** :
   - Le logement était occupé par son propriétaire → **Condition remplie**.
3. **Prestations portant sur des équipements éligibles** :
   - L’installation d’une chaudière peut relever du **3° du I** (chauffage et ventilation), **sous réserve qu’elle contribue à économiser l’énergie ou à recourir à des énergies renouvelables**.
   - **Problème** : Le texte ne précise pas si *toutes* les chaudières sont éligibles, ou seulement celles répondant à des critères techniques (ex. : rendement, type de combustible).

#### **B. Exclusion du III bis (taux à 20 %)**
Le **III bis** introduit une **dérogation** au taux réduit pour :
> *« les prestations de rénovation énergétique comprenant la fourniture ou l’installation d’une chaudière susceptible d’utiliser des combustibles fossiles. »*

**Interprétation stricte de l’exclusion** :
- Le texte vise **uniquement les chaudières "susceptibles d’utiliser des combustibles fossiles"**, c’est-à-dire celles **conçues pour fonctionner avec du fioul, du gaz naturel, ou du charbon**.
- **Si la chaudière installée était** :
  - **Une chaudière à condensation gaz** (même si elle utilise un combustible fossile) → **Exclue du taux réduit** (taux à 20 %).
  - **Une chaudière biomasse (bois, granulés)** ou **une pompe à chaleur** → **Éligible au taux réduit** (5,5 %), car elle ne relève pas de l’exclusion du III bis.

**Problème** : Votre facture ne précise pas le **type de chaudière** installée. Or, c’est un élément **déterminant** pour l’application du taux réduit.

---

### **3. Arguments à opposer à l’administration**
#### **A. Charge de la preuve**
- En matière de TVA, **c’est à l’administration de prouver que les conditions du taux réduit ne sont pas remplies** (CE, 10 juillet 2020, n° 426159).
- **Vous devez fournir** :
  - La **facture détaillée** (mentionnant le type de chaudière installée).
  - Une **attestation du fabricant** ou une **fiche technique** prouvant que la chaudière n’est **pas "susceptible d’utiliser des combustibles fossiles"** (ex. : chaudière biomasse, pompe à chaleur).
  - Si la chaudière est éligible à des **aides de l’État** (MaPrimeRénov’, CEE), cela peut constituer un **indice favorable** (mais pas une preuve absolue).

#### **B. Interprétation restrictive du III bis**
- Le **III bis** est une **dérogation** au principe du taux réduit. Il doit donc être interprété **strictement**.
- **Seules les chaudières conçues pour fonctionner avec des combustibles fossiles** sont exclues. Si la chaudière installée était **hybride** (ex. : pompe à chaleur + appoint gaz) ou **100 % renouvelable**, le taux réduit s’applique.
- **Jurisprudence** : Le Conseil d’État a rappelé que les exclusions au taux réduit doivent être **claires et non équivoques** (CE, 13 mars 2019, n° 410650).

#### **C. Erreur de l’administration**
- Si l’administration se base uniquement sur le fait que la prestation concerne une chaudière **sans vérifier son type**, sa position est **fragile**.
- Vous pouvez **contester la rectification** en demandant à l’administration de **préciser les éléments sur lesquels elle fonde son rejet** (type de chaudière, combustible utilisé).

#### **D. Tolérance administrative (si applicable)**
- Dans certains cas, l’administration admet le taux réduit pour des chaudières à **haut rendement** (ex. : chaudières à condensation gaz **très performantes**), même si elles utilisent des combustibles fossiles.
- **À vérifier** : Si votre chaudière répondait aux **critères techniques des aides de l’ANAH ou de l’ADEME**, cela pourrait appuyer votre position.

---

### **4. Stratégie de défense**
#### **Étape 1 : Réponse à la proposition de rectification**
- **Délai** : Vous avez **30 jours** à compter de la réception de la proposition pour répondre (prolongation possible sur demande).
- **Contenu de la réponse** :
  1. **Contestation du bien-fondé** de la rectification au motif que :
     - L’administration n’a pas prouvé que la chaudière était **susceptible d’utiliser des combustibles fossiles**.
     - Les conditions du **I de l’article 278-0 bis A** sont remplies (local de +2 ans, usage d’habitation).
  2. **Demande de précisions** : Exiger de l’administration qu’elle indique **le type exact de chaudière** qu’elle considère comme exclu du taux réduit.
  3. **Production de preuves** :
     - Facture détaillée.
     - Fiche technique de la chaudière.
     - Attestation du fabricant (si disponible).
     - Preuves d’éligibilité à des aides (MaPrimeRénov’, CEE).

#### **Étape 2 : Recours hiérarchique (si rejet)**
- Si l’administration maintient sa position, vous pouvez :
  1. **Saisir le supérieur hiérarchique** du vérificateur (lettre recommandée avec AR).
  2. **Engager un recours contentieux** devant le **tribunal administratif** (dans un délai de 2 mois à compter de la décision de rejet).

#### **Étape 3 : Régularisation (si nécessaire)**
- Si la chaudière était bien **exclue du taux réduit** (ex. : chaudière gaz classique), vous devrez **régulariser la TVA** (20 %) et payer les **intérêts de retard** (0,2 % par mois).
- **Négociation possible** : L’administration peut accepter un **étalement du paiement** ou une **réduction des pénalités** en cas de bonne foi.

---

### **5. Recommandations**
1. **Vérifiez immédiatement** :
   - Le **type de chaudière** installée (marque, modèle, combustible utilisé).
   - La **fiche technique** du fabricant (pour prouver qu’elle n’est pas "susceptible d’utiliser des combustibles fossiles").
2. **Conservez tous les documents** :
   - Devis, facture, bon de commande, attestation du fabricant, preuves d’éligibilité aux aides.
3. **Ne payez pas immédiatement** :
   - Attendez la réponse de l’administration à votre contestation.
4. **Préparez un argumentaire technique** :
   - Si la chaudière est éligible, insistez sur le fait que le **III bis ne s’applique pas**.
   - Si elle ne l’est pas, négociez les pénalités.

---

### **6. Conclusion**
À ce stade, **l’application du taux réduit de 5,5 % n’est pas automatiquement exclue**, mais elle dépend **du type de chaudière installée**. Si celle-ci n’est **pas conçue pour fonctionner avec des combustibles fossiles**, vous avez de **solides arguments** pour contester la rectification.

**Prochaines étapes** :
- Me transmettre **tous les documents relatifs à la chaudière** (facture, fiche technique, etc.).
- Je rédigerai une **réponse formelle à l’administration** dans les meilleurs délais.

Je reste à votre disposition pour échanger sur ce dossier et affiner la stratégie en fonction des éléments que vous me fournirez.

Veuillez agréer, Cher Monsieur, l’expression de mes salutations distinguées.

**[Votre Nom]**
Avocat fiscaliste
[Coordonnées du cabinet]

---
**Annexes** :
- Copie de la proposition de rectification.
- Extrait de l’article 278-0 bis A du CGI (version 2025).
- Modèle de réponse à l’administration (à adapter).

---

## T06

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

L’activité de la SAS consiste dans la détention et la location de quarante appartements meublés, soit une activité de gestion de son propre patrimoine immobilier. Le deuxième alinéa de l’article 787 B (dans sa rédaction applicable au 25 octobre 2023) exclut expressément une telle activité du champ des activités industrielles, commerciales, artisanales, agricoles ou libérales ouvrant droit au régime. Cette exclusion s’applique indépendamment de la qualification commerciale (BIC) que peut revêtir la location meublée au regard de l’impôt sur le revenu ou de l’impôt sur les sociétés.

Les autres conditions formelles du dispositif (engagement collectif de conservation en cours depuis plus de deux ans, engagements individuels des donataires, conservation de la présidence pendant trois ans) sont en l’état réunies, mais elles sont inopérantes dès lors que la condition tenant à la nature de l’activité n’est pas satisfaite. La société n’entre pas davantage dans l’exception prévue pour les holdings animatrices, qui suppose un groupe de sociétés opérationnelles contrôlées.

La donation en pleine propriété des titres, d’une valeur de 20 M€, sera donc soumise aux droits de mutation à titre gratuit dans les conditions de droit commun (après abattements éventuels), sans application de l’exonération de 75 %.

Je reste à votre disposition pour examiner d’éventuelles mesures alternatives (donation-partage avec réserve d’usufruit, pacte Dutreil sur une autre structure, etc.) ou pour affiner l’analyse si des éléments complémentaires sur l’activité réelle (prestations para-hôtelières caractérisées, mixité d’activités, etc.) devaient modifier cette appréciation.

---

## T07

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

**Objet : Analyse de la légalité de l’application du taux réduit de TVA (5,5 %) sur le chantier du 15 avril 2025 – Réponse à la proposition de rectification**

**Maître [Votre Nom]**
Avocat fiscaliste
[Vos coordonnées]
[Date]

**À l’attention de [Nom du gérant]**
[Nom de l’entreprise]
[Adresse de l’entreprise]

---

**Cher Monsieur [Nom du gérant],**

Je vous remercie de m’avoir consulté sur la proposition de rectification notifiée par l’administration fiscale concernant l’application du taux de TVA sur le chantier de rénovation énergétique réalisé le **15 avril 2025** (installation d’une chaudière dans une maison de 15 ans, facturée **8 500 € HT**). L’administration conteste l’application du taux réduit de **5,5 %** et exige le paiement de la différence avec le taux normal (**20 %**), soit **1 232,50 €** (8 500 € × 14,5 %).

Je vous propose ci-dessous une analyse juridique détaillée de la situation, ainsi que les arguments à opposer à l’administration pour contester cette rectification.

---

### **1. Rappel des conditions légales pour bénéficier du taux réduit de 5,5 % (CGI, art. 278-0 bis A)**
Pour que les travaux de rénovation énergétique bénéficient du taux réduit de **5,5 %**, trois conditions cumulatives doivent être remplies (I de l’article 278-0 bis A du CGI) :

1. **Ancienneté du local** : Les travaux doivent être effectués dans des locaux **achevés depuis au moins deux ans**.
   → **Vérification** : La maison a 15 ans (condition remplie).

2. **Usage d’habitation** : Les locaux doivent être **affectés à un usage d’habitation** à l’issue des travaux.
   → **Vérification** : La maison est occupée par son propriétaire (condition remplie).

3. **Nature des travaux** : Les prestations doivent porter sur la **pose, l’installation ou l’entretien** de matériaux/équipements visant à :
   - **Améliorer l’isolation thermique** ;
   - **Optimiser le chauffage ou la ventilation** ;
   - **Produire de l’eau chaude sanitaire** ;
   **avec un objectif d’économie d’énergie ou de recours aux énergies renouvelables**.

   → **Vérification** : L’installation d’une chaudière peut relever de cette catégorie **si elle répond à ces critères** (ex. : chaudière à condensation, à granulés, etc.).

**Exception (III bis)** : Le taux réduit **ne s’applique pas** si les travaux comprennent la fourniture ou l’installation d’une **chaudière susceptible d’utiliser des combustibles fossiles** (ex. : chaudière au fioul ou au gaz naturel non performante).

---

### **2. Analyse du litige : la chaudière installée est-elle éligible au taux réduit ?**
L’administration considère probablement que la chaudière installée est **susceptible d’utiliser des combustibles fossiles**, ce qui exclurait le taux réduit (III bis). Pour contester cette position, il convient de vérifier :

#### **a) Type de chaudière installée**
- **Si la chaudière est une chaudière à condensation au gaz naturel ou au fioul** :
  - Ces chaudières **utilisent des combustibles fossiles** et sont donc **exclues du taux réduit** (III bis).
  - **Conséquence** : Le taux de **20 %** s’applique, et la rectification est justifiée.

- **Si la chaudière est une chaudière à granulés (bois), à bûches, ou une pompe à chaleur** :
  - Ces équipements **ne relèvent pas de l’exception du III bis** (ils utilisent des énergies renouvelables ou non fossiles).
  - **Conséquence** : Le taux réduit de **5,5 %** s’applique, et la rectification est infondée.

#### **b) Preuves à fournir**
Pour justifier l’application du taux réduit, vous devez **prouver que la chaudière installée n’est pas susceptible d’utiliser des combustibles fossiles**. Les éléments suivants peuvent être utiles :
- **Facture du fournisseur** : Mention du type de chaudière (ex. : "chaudière à granulés", "pompe à chaleur air-eau").
- **Notice technique du fabricant** : Spécifications indiquant le type de combustible utilisé.
- **Attestation du fabricant ou de l’installateur** : Certifiant que la chaudière ne fonctionne pas avec des combustibles fossiles.
- **Label ou certification** : Ex. : "Flamme Verte" pour les chaudières à bois, "NF PAC" pour les pompes à chaleur.

**→ Si ces preuves démontrent que la chaudière n’utilise pas de combustibles fossiles, le taux réduit de 5,5 % est applicable.**

---

### **3. Stratégie de défense face à l’administration**
#### **a) Réponse à la proposition de rectification**
Dans un premier temps, je vous propose d’adresser à l’administration une **réponse motivée** contestant la rectification, en joignant les preuves suivantes :
1. **Copie de la facture du fournisseur** (mentionnant le type de chaudière).
2. **Notice technique ou fiche produit** de la chaudière.
3. **Attestation de l’installateur** confirmant que la chaudière n’utilise pas de combustibles fossiles.
4. **Extrait du devis ou bon de commande** précisant la nature des travaux.

**Argumentaire** :
- Les travaux remplissent les conditions du **I de l’article 278-0 bis A** (local de plus de 2 ans, usage d’habitation, amélioration énergétique).
- La chaudière installée **n’est pas susceptible d’utiliser des combustibles fossiles** (preuve à l’appui), donc l’**exception du III bis ne s’applique pas**.
- Le taux réduit de **5,5 %** est donc légalement applicable.

#### **b) Recours en cas de rejet**
Si l’administration maintient sa position, deux options s’offrent à vous :
1. **Réclamation contentieuse** devant le service des impôts (dans un délai de **2 mois** à compter de la réponse de l’administration).
2. **Saisine du tribunal administratif** en cas de rejet de la réclamation.

---

### **4. Recommandations complémentaires**
- **Vérifiez systématiquement le type de chaudière** avant d’appliquer le taux réduit sur vos futurs chantiers. Les chaudières au gaz ou au fioul (même performantes) sont exclues du taux réduit.
- **Conservez tous les justificatifs** (factures, notices, attestations) pour chaque chantier de rénovation énergétique.
- **En cas de doute sur un équipement**, consultez la **liste des matériels éligibles** publiée par l’ADEME ou demandez une **attestation du fabricant**.

---

### **5. Conclusion et prochaines étapes**
À ce stade, **tout dépend du type de chaudière installée** :
- **Si la chaudière n’utilise pas de combustibles fossiles** : Le taux réduit de **5,5 %** est applicable, et la rectification doit être contestée.
- **Si la chaudière utilise des combustibles fossiles** : Le taux de **20 %** s’applique, et il est préférable de régulariser la situation pour éviter des pénalités.

**Prochaine étape** :
Je vous propose de me transmettre **la facture du fournisseur et la notice technique de la chaudière** afin que je puisse :
1. Vérifier son éligibilité au taux réduit.
2. Rédiger une réponse argumentée à l’administration si la chaudière est éligible.

Dans l’attente de ces éléments, je reste à votre disposition pour toute précision.

Veuillez agréer, Cher Monsieur, l’expression de mes salutations distinguées.

**[Votre Nom]**
Avocat fiscaliste
[Votre cabinet]
[Coordonnées]

---
**Annexes** :
- Extrait de l’article 278-0 bis A du CGI.
- Modèle de réponse à la proposition de rectification (sur demande).

---

## T08

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

Notre étude,
[Date du jour]

**Objet : Proposition de rectification – Remise en cause du taux de TVA (5,5 % / 20 %) sur chantier de rénovation énergétique**
**Réf. :** [Référence du dossier]

**À l'attention de [Monsieur le Gérant / Nom de l'entreprise],**

Suite à votre consultation relative à la proposition de rectification notifiée par l'administration fiscale concernant la facturation du chantier du 15 avril 2025 pour un montant de 8 500 € HT, je vous prie de bien vouloir trouver ci-après mon analyse.

### 1. Analyse juridique de la situation

La question posée est de savoir si l'application du taux réduit de TVA à 5,5 % sur l'installation d'une chaudière dans une maison d'habitation achevée depuis plus de deux ans était conforme à la législation en vigueur à la date des travaux.

En vertu des dispositions de l'article 278-0 bis A du Code Général des Impôts (CGI) que vous avez transmis, l'application du taux réduit de 5,5 % est conditionnée par la réunion de plusieurs critères énumérés au paragraphe I :
1. Les locaux doivent être achevés depuis au moins deux ans (condition remplie en l'espèce, la maison ayant 15 ans).
2. Les locaux doivent être affectés à un usage d'habitation (condition remplie en l'espèce).
3. Les prestations doivent porter sur la pose, l'installation... de systèmes ayant pour objet d'économiser l'énergie... par l'amélioration du chauffage (condition *en apparence* remplie).

**Toutefois, l'analyse ne doit pas s'arrêter au paragraphe I.**

Le paragraphe III bis du même article prévoit une **exception majeure** à ces conditions :
*"Par dérogation au I du présent article, le taux prévu à l'article 278 [soit le taux normal de 20 %] s'applique aux prestations de rénovation énergétique comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles."*

### 2. Application au cas d'espèce

L'opération que vous avez facturée le 15 avril 2025 concerne exclusivement l'installation d'une chaudière. La qualification juridique de l'opération dépend donc d'un facteur technique essentiel : **le type de chaudière installée**.

*   **Cas n°1 : La chaudière est susceptible d'utiliser des combustibles fossiles (gaz, fioul, charbon...).**
    Dans ce cas de figure, l'exception prévue au III bis de l'article 278-0 bis A s'applique. Le taux normal de 20 % est obligatoire. L'administration fiscale est donc fondée à vous réclamer la différence de TVA.
    Pour information, le surcoût de TVA pour votre client aurait été de : 8 500 € x 14,5 % = 1 232,50 €.

*   **Cas n°2 : La chaudière n'est pas susceptible d'utiliser des combustibles fossiles (ex. chaudière à biomasse/boisson, pompe à chaleur PAC qui n'est pas une chaudière, etc.).**
    Dans ce cas de figure, l'exception III bis ne s'applique pas. Les conditions du paragraphe I étant par ailleurs remplies, le taux de 5,5 % que vous avez appliqué est strictement conforme à la loi. L'administration fiscale a donc commis une erreur d'appréciation.

### 3. Conclusions et recommandations

Le taux de 5,5 % que vous avez appliqué n'était correct **que si** la chaudière installée est un modèle fonctionnant exclusivement avec des énergies renouvelables (et non avec des énergies fossiles).

**Démarche à suivre :**

1.  **Si vous avez installé une chaudière "fossile" (gaz, fioul, hybride...) :**
    L'administration a raison. Je vous recommande d'accepter la proposition de rectification pour éviter la majoration de 40 % pour manquement délibéré. Il faudra régulariser la TVA (1 232,50 €) et, le cas échéant, refacturer cette différence au client final si vos conditions générales de vente le prévoient.

2.  **Si vous avez installé une chaudière "non fossile" (ex. chaudière à granulés de bois) :**
    L'administration a tort. Il conviendra de lui adresser une réponse argumentée dans le délai légal (généralement 30 jours) en lui indiquant que les travaux entrent strictement dans le champ du I de l'article 278-0 bis A du CGI et qu'ils échappent à l'exception du III bis, la chaudière installée n'étant pas susceptible d'utiliser des combustibles fossiles. Nous joindrons à notre courrier la fiche technique de l'équipement posé en preuve.

Je vous invite à me transmettre en retour la nature exacte de la chaudière installée (et idéalement sa référence technique) afin que je puisse finaliser la réponse à l'administration fiscale dans les délais impartis.

Je reste à votre entière disposition pour toute précision utile.

Bien cordialement,

**[Votre Prénom Nom]**
*Avocat fiscaliste au Barreau de [Ville]*

---

## T09

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

**Non, aucune retenue à la source n’est due** (sous réserve du respect des conditions de l’article 119 ter du CGI et de l’absence de montage artificiel).

L’article 119 bis, 2 du CGI que vous citez instaure bien le principe d’une retenue à la source sur les dividendes versés à des bénéficiaires non résidents (autres que certains OPC étrangers remplissant des conditions spécifiques). Ce texte ne constitue toutefois pas le régime applicable en l’espèce.

L’exonération de retenue à la source prévue à l’article 119 ter du CGI (transposition de la directive « mères-filiales ») s’applique. Les conditions sont réunies :

- société distributrice française soumise à l’IS ;
- bénéficiaire effectif : société de capitaux de forme éligible (SA luxembourgeoise) établie dans un État membre de l’UE, soumise à l’impôt sur les sociétés luxembourgeois de droit commun sans option ni exonération ;
- détention de 100 % du capital depuis cinq ans (seuil de 10 % et durée minimale de deux ans largement dépassés) ;
- mise en paiement le 15 juin 2025.

La clause anti-abus de l’article 119 ter, 3 du CGI n’apparaît pas caractérisée au vu des éléments communiqués (détention historique de 100 %, société opérationnelle luxembourgeoise soumise à l’IS).

La convention fiscale franco-luxembourgeoise n’a pas à être mobilisée (le taux conventionnel serait de 5 % en cas de participation qualifiée, mais la directive prime et aboutit à 0 %).

**Recommandations pratiques**  
Conserver au dossier : attestation de résidence fiscale de la mère, justificatifs de détention continue, et le cas échéant une attestation sur l’honneur relative à la qualité de bénéficiaire effectif et à l’absence d’arrangement artificiel. Aucune formalité déclarative particulière n’est requise auprès du Trésor pour bénéficier de l’exonération, mais la société distributrice doit être en mesure de justifier du régime appliqué en cas de contrôle.

Je reste à votre disposition pour formaliser l’attestation ou examiner tout élément complémentaire (notamment si la mère luxembourgeoise bénéficie d’un régime particulier).

---

## T10

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

## Avis

Les éléments communiqués ne permettent pas, à eux seuls, de confirmer le taux de 5,5 %. Il faut impérativement connaître le type de chaudière installé.

Les deux premières conditions de l’article 278-0 bis A sont remplies :

- la maison était achevée depuis quinze ans, donc depuis plus de deux ans ;
- elle était affectée à l’habitation, peu important qu’elle soit occupée par son propriétaire.

En revanche, le III bis exclut expressément du taux de 5,5 % toute prestation comprenant la fourniture ou l’installation d’une chaudière **susceptible d’utiliser des combustibles fossiles**.

Par conséquent :

- **si la chaudière fonctionne au gaz, au fioul ou peut utiliser un autre combustible fossile**, le taux applicable était obligatoirement de **20 %**. Le taux de 5,5 % était alors erroné ;
- **si elle fonctionne exclusivement avec une énergie non fossile** — par exemple une chaudière biomasse — le III bis ne s’applique pas. Le taux de 5,5 % peut alors être admis, sous réserve que l’équipement réponde bien aux conditions techniques de la rénovation énergétique ;
- la seule désignation « chaudière » sur la facture ne suffit donc pas à justifier automatiquement le rappel au taux de 20 %.

Si la chaudière était à combustible fossile, la TVA omise sur 8 500 € HT s’élève à :

- TVA facturée à 5,5 % : **467,50 €** ;
- TVA due à 20 % : **1 700 €** ;
- différence : **1 232,50 €**, hors intérêts de retard et éventuelles majorations.

Il convient de vérifier immédiatement le devis, la facture détaillée, la référence fabricant, la fiche technique et la source d’énergie de l’appareil. **Si la chaudière est au gaz ou au fioul, la rectification est fondée sur le principe. Si elle est exclusivement non fossile, elle doit être contestée, sous réserve du respect des autres critères techniques ouvrant droit au taux de 5,5 %.**

---

## T11

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

**CONSULTATION**

**Objet :** éligibilité au régime de faveur de l'article 787 B du CGI d'une donation‑partage en pleine propriété de la totalité des actions d'une SAS détenant 40 appartements meublés — Donation projetée le 25 octobre 2023 — Valeur 20 000 000 €.

---

## 1. Conclusion (à lire en premier)

**En l'état des éléments communiqués, l'exonération de 75 % n'est pas applicable.** La SAS exerce, sauf démonstration contraire à établir, une activité de **gestion de son propre patrimoine immobilier**, expressément exclue par le deuxième alinéa de l'article 787 B — texte qui, contrairement à ce que l'on pourrait croire, **s'applique bien à une donation du 25 octobre 2023**.

Toutes les autres conditions (engagement collectif, engagements individuels, direction) sont en revanche satisfaites ou aisément sécurisables : elles sont sans effet, la condition d'activité étant une condition première et autonome.

**Je vous déconseille formellement de passer l'acte le 25 octobre 2023 en revendiquant le 787 B.** Enjeu du redressement : environ **7,6 M€ de droits**, outre intérêts de retard et majoration de 40 % en cas de manquement délibéré.

---

## 2. Le point bloquant : la nature de l'activité

### 2.1. Le texte applicable et sa date d'entrée en vigueur

Le texte que vous me soumettez — et notamment son deuxième alinéa excluant « *l'exercice par une société d'une activité de gestion de son propre patrimoine mobilier ou immobilier* » — est celui issu de **l'article 23 de la loi de finances pour 2024 (loi n° 2023‑1322 du 29 décembre 2023)**.

Le législateur a assorti cette disposition d'une **entrée en vigueur anticipée : elle s'applique aux transmissions intervenant à compter du 17 octobre 2023** (date de dépôt de l'amendement), précisément pour couper court aux donations « d'aubaine » consécutives à la jurisprudence de la Cour de cassation de juin 2023.

**Votre donation, signée le 25 octobre 2023, est postérieure de huit jours à cette date de bascule.** Le fait générateur des droits de mutation étant la date de l'acte (art. 750 ter et 784 CGI), c'est le texte nouveau qui gouverne l'opération.

> *Point de vigilance* : je vérifierai avant signature la rédaction exacte du II de l'article 23 de la LF 2024. Si une contestation devait être engagée, l'argument de la « petite rétroactivité » (atteinte aux situations légalement acquises / à l'espérance légitime née de la jurisprudence) est très fragile : le Conseil constitutionnel admet de longue date les mesures anti‑optimisation rétroagissant à la date d'annonce publique. Ce n'est pas une base sur laquelle je construirais un dossier de 7,6 M€.

### 2.2. Pourquoi la location meublée est désormais exclue

Jusqu'au 16 octobre 2023, votre dossier était **plaidable** : l'article 787 B renvoyant aux articles 34 et 35 du CGI, et la location meublée relevant de plein droit des BIC (art. 35, I, 5° bis), la Cour de cassation avait jugé (Cass. com., 1er juin 2023, n° 22‑15.152) qu'une société de location meublée exerçait une activité commerciale au sens du 787 B, en désavouant la doctrine administrative contraire.

C'est **exactement cette jurisprudence** que l'article 23 de la LF 2024 a entendu neutraliser. La location de 40 appartements meublés, dès lors qu'elle se limite à la mise à disposition de locaux garnis de meubles moyennant loyer, constitue le prototype même de la « gestion de son propre patrimoine immobilier » désormais exclue. La qualification BIC en matière d'impôt sur le revenu est indifférente : le deuxième alinéa institue une **règle spéciale propre aux droits de mutation à titre gratuit**, qui déroge au renvoi aux articles 34 et 35.

La doctrine administrative (BOI‑ENR‑DMTG‑10‑20‑40‑10) a été mise à jour en ce sens et cite expressément la location meublée parmi les activités civiles exclues.

### 2.3. La seule porte de sortie : l'exploitation para‑hôtelière ou hôtelière véritable

L'exclusion vise la **gestion** patrimoniale, non l'**exploitation** commerciale. Une société qui exploite une véritable activité hôtelière ou para‑hôtelière — c'est‑à‑dire qui fournit, dans des conditions similaires à celles de l'hôtellerie, au moins trois des quatre services de référence (petit‑déjeuner, nettoyage régulier des locaux, fourniture de linge de maison, réception même non personnalisée de la clientèle), avec les moyens humains et matériels correspondants — n'est pas dans la gestion de son propre patrimoine : elle exploite un fonds.

**J'ai donc besoin, avant toute chose, des éléments suivants :**

1. Décomposition du chiffre d'affaires des trois derniers exercices : loyers nus / loyers meublés « longue durée » / prestations de services ;
2. Contrats types signés avec les occupants (baux d'habitation meublée ? contrats de séjour ? durée moyenne d'occupation ?) ;
3. Effectif salarié de la société, fiches de poste, masse salariale ;
4. Situation TVA : les recettes sont‑elles soumises à la TVA au titre du b du 4° de l'article 261 D du CGI ? (indice déterminant, quoique non décisif à lui seul) ;
5. Existe‑t‑il un mandat de gestion / une conciergerie externalisée, un classement « meublé de tourisme », une exploitation de type résidence services ?
6. Bilan : les biens sont‑ils inscrits en immobilisations, existe‑t‑il un fonds de commerce, une clientèle propre ?

Si la société exploite en réalité une résidence de tourisme ou une activité para‑hôtelière étoffée, le dossier redevient défendable. Si elle se borne à encaisser 40 loyers meublés au mois ou à l'année, il ne l'est pas — et aucune habileté rédactionnelle n'y changera rien.

Deux avertissements complémentaires :

- **La condition d'activité doit être satisfaite en continu**, depuis la conclusion de l'engagement collectif (3 mars 2021) et jusqu'au terme de l'engagement individuel (soit ici jusqu'en 2028 environ). Une « commercialisation » de l'activité opérée dans les semaines précédant la donation serait à la fois insuffisante rétroactivement et exposée à l'abus de droit (art. L. 64 et L. 64 A du LPF, montage à but principalement fiscal).
- Le caractère **principal** de l'activité s'apprécie au moyen d'un faisceau d'indices (part du CA, part de l'actif brut immobilisé affecté). Une société mixte doit être prépondérante côté opérationnel.

---

## 3. Les autres conditions : audit rapide

Je les examine pour mémoire, et parce qu'elles serviront si le dossier est restructuré.

**a) Engagement collectif (a du 787 B) — satisfaite.**
Signé le 3 mars 2021, portant sur 100 % des droits financiers et de vote (seuils requis pour une société non cotée : 17 % / 34 %), en cours depuis plus de deux ans au jour de la donation. La donation peut donc intervenir pendant la phase collective. Vérifier néanmoins : date certaine de l'acte (enregistrement ou acte authentique), et que l'engagement a bien été souscrit « pour lui et ses ayants cause à titre gratuit ».

**b) Engagements individuels (c du 787 B) — satisfaite.**
Chaque enfant s'engage à conserver ses titres 4 ans à compter de l'expiration de l'engagement collectif. À faire figurer dans le corps de l'acte, avec rappel exprès de l'engagement collectif annexé et attestation de la société.

**c) Fonction de direction (d du 787 B) — POINT DE VIGILANCE RÉEL.**
La fonction doit être exercée, pendant l'engagement collectif puis pendant **trois ans à compter de la transmission**, par **un associé signataire de l'engagement collectif** ou par **l'un des donataires**.

Or votre client, s'il donne la **totalité** de ses titres, cesse d'être associé au jour de la donation. L'administration considère que la personne exerçant la direction doit conserver la qualité d'associé partie à l'engagement ; la sécurité du montage est donc discutable en l'état.

**Deux correctifs simples, à retenir dans tous les cas :**
- soit le donateur conserve une fraction de titres (ne serait‑ce qu'un bloc symbolique) jusqu'au terme des trois ans ;
- soit — solution que je privilégie — **l'un des deux enfants est nommé président ou directeur général** de la SAS concomitamment à la donation, la présidence de SAS et la direction générale étant admises comme fonctions éligibles pour les sociétés soumises à l'IS.

Rappel : la fonction doit être **effectivement exercée** et donner lieu à une **rémunération normale** (procès‑verbaux, délégations, preuve de l'activité réelle à conserver).

---

## 4. L'enjeu chiffré

| | Avec 787 B (si applicable) | Sans 787 B |
|---|---|---|
| Assiette par enfant | 10 M€ – 75 % = 2 500 000 € | 10 000 000 € |
| Abattement (art. 779, I) | – 100 000 € | – 100 000 € |
| Droits bruts par enfant | ≈ 842 400 € | ≈ 4 217 400 € |
| Réduction de 50 % (art. 790 : donateur < 70 ans, pleine propriété) | – 421 200 € | néant |
| **Droits par enfant** | **≈ 421 200 €** | **≈ 4 217 400 €** |
| **Droits totaux** | **≈ 842 400 €** | **≈ 8 434 800 €** |

Écart : **≈ 7,6 M€**. J'attire l'attention sur le fait que la réduction de 50 % de l'article 790, dont votre client remplit la condition d'âge, est **réservée aux transmissions bénéficiant du 787 B** : elle tombe avec l'exonération.

Autre conséquence collatérale : le **paiement différé‑fractionné** sur 15 ans (art. 1717 CGI et 397 A de l'annexe III) est lui aussi subordonné à l'exercice par la société d'une activité industrielle, commerciale, artisanale, agricole ou libérale. Il risque d'être refusé pour le même motif. Le financement des droits doit donc être anticipé.

---

## 5. Recommandations

1. **Ne pas signer le 25 octobre 2023** en l'état. Reporter l'acte, l'échéance étant sans urgence fiscale : le texte nouveau est pérenne, il n'y a plus de « fenêtre » à saisir.

2. **Audit d'activité** sur la base des pièces listées au § 2.3. Si une exploitation para‑hôtelière réelle existe déjà et est documentée depuis mars 2021, le dossier peut être repris ; j'établirai alors une note de position à conserver au dossier (et, le cas échéant, un **rescrit** sur le fondement de l'article L. 80 B, 1° du LPF — je recommande vivement cette sécurisation préalable, compte tenu du montant).

3. **Si l'activité est purement locative**, deux voies :
 - **Voie longue** : transformer réellement l'activité (structuration para‑hôtelière : personnel, services, contrats, TVA), puis **souscrire un nouvel engagement collectif** une fois la mutation opérationnelle effective et documentée, et différer la donation. Le donateur ayant 62 ans, le calendrier est compatible avec le maintien du bénéfice de l'article 790 (moins de 70 ans). Cette voie ne doit pas être artificielle : elle suppose une transformation économique authentique.
 - **Voie alternative, sans 787 B** : optimiser autrement — **donation avec réserve d'usufruit** (à 62 ans, usufruit valorisé 40 %, assiette ramenée à 12 M€, soit une économie d'environ 3,6 M€ de droits, avec extinction en franchise au décès), éventuellement combinée à un **démembrement croisé / donation‑partage échelonnée** sur plusieurs périodes de 15 ans, à une **prise en charge des droits par le donateur** (non taxable comme libéralité supplémentaire), voire à un **OBO** permettant de dégager la liquidité nécessaire. Ces schémas ne procurent pas l'effet du 787 B mais sont robustes.

4. Dans tous les cas, **nommer un enfant dirigeant** pour purger la difficulté du d) du 787 B.

Je reste à votre disposition, ainsi que celle de Maître ..., pour une réunion de travail dès réception des pièces. Je souligne que la présente analyse est fondée sur les seuls éléments décrits (40 appartements meublés, sans autre précision) : la conclusion serait susceptible d'évoluer si la réalité de l'exploitation s'avérait différente.

---

## T12

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

**Cabinet d'Avocats - Fiscalité et Droit des Affaires**
**Note de Synthèse à l'attention de Maître [Nom du Notaire] et de Monsieur [Nom du Client]**

**Objet : Applicabilité de l'exonération des droits de mutation à titre gratuit (Article 787 B du CGI) dans le cadre de la donation projetée d'une SAS patrimoniale.**
**Date : 18 octobre 2023**

Messieurs,

Vous m'avez consulté afin de vérifier l'applicabilité du régime de faveur prévu par l'article 787 B du CGI (pacte "Dutreil") à l'occasion de la donation par notre client, âgé de 62 ans, de la totalité des titres de sa SAS à ses deux enfants, en pleine propriété et à parts égales. 

La donation est projetée pour le 25 octobre 2023. La société détient un patrimoine de quarante appartements meublés, pour une valeur des titres s'élevant à 20 000 000 d'euros.

Après analyse de la situation à l'aune du texte de l'article 787 B du CGI applicable à la date de la donation, **ma réponse est positive, sous réserve du respect d'une condition de fond qui devra être rigoureusement documentée : la preuve de l'activité commerciale de la société.**

Voici mon analyse détaillée et mes recommandations pour sécuriser l'opération.

### 1. L'épineuse question de l'activité de la société (Condition de fond)

Le premier alinéa de l'article 787 B exige que la société ait une "activité principale industrielle, commerciale, artisanale, agricole ou libérale". 

Le deuxième alinéa exclut expressément du bénéfice de l'exonération "l'exercice par une société d'une activité de gestion de son propre patrimoine mobilier ou immobilier". 

**En l'espèce, la société possède quarante appartements meublés.** 
La location meublée constitue, par principe, une activité commerciale au sens des articles 34 et 35 du CGI. Toutefois, l'Administration fiscale (BOI-ENR-CTL-10-20) et la jurisprudence sont extrêmement vigilantes : si la société se contente d'une gestion passive de son patrimoine (encaissement des loyers, paiement des charges), l'activité sera requalifiée en "gestion de patrimoine" et l'exonération sera refusée, avec des conséquences fiscales désastreuses (perte de l'abattement de 75%, soit un surcoût de droits d'environ 4,5 millions d'euros).

Pour que l'exonération s'applique, il est impératif de démontrer que la société exerce une activité commerciale *active*. La jurisprudence (notamment *CE, 8e-3e sect., 26 mars 2014, n° 357938, Société civile de Montesquieu*) considère qu'il y a activité commerciale lorsque la société assure la gestion de ses immeubles de manière active, ce qui implique des actes matériels et juridiques allant au-delà de la simple perception des revenus (commercialité accrue par des prestations de services type accueil, entretien, blanchisserie, restauration, ou gestion intensive impliquant un personnel dédié).

**Recommandation :** Il est indispensable que nous constituions, dès à présent, un dossier de preuve de l'activité commerciale de la SAS (statuts précisant l'objet, contrats de location meublée prévoyant des prestations de services annexes, factures de prestataires, contrats de travail du personnel d'exploitation et d'entretien, déclarations fiscales BIC/IS). Ce dossier devra être annexé à l'acte de donation ou conservé aux archives de la société pour répondre à toute demande de l'Administration dans le cadre d'une procédure de rescrit ou d'un contrôle.

### 2. L'analyse des conditions formelles et temporelles du Pacte "Dutreil"

Sous réserve que la condition d'activité soit remplie, les autres conditions de l'article 787 B semblent parfaitement respectées en l'état du dossier que vous m'avez transmis :

**A. L'engagement collectif de conservation (ECC)**
*   **Date de conclusion :** L'ECC a été signé le 3 mars 2021. La donation du 25 octobre 2023 intervient plus de deux ans après la signature de cet engagement. La condition de l'antériorité minimale de deux ans est donc remplie.
*   **Objet :** L'engagement porte sur la totalité des droits de la société. 
*   **Durée :** L'ECC doit être en cours à la date de la donation, ce qui est le cas.

**B. L'engagement individuel de conservation**
*   Les deux enfants donataires prendront, lors de la donation du 25 octobre 2023, l'engagement individuel de conservation prévu par les textes. 
*   Cet engagement portera sur les titres reçus (la moitié du capital chacun) et sera d'une durée de 4 ans, courant à compter de la date de l'acte de donation.

**C. La condition de direction**
*   L'article 787 B exige que l'un des associés liés par l'engagement (le donateur ou l'un des donataires) exerce de manière effective, pendant les 5 années suivant la transmission, l'une des fonctions de direction énumérées par le texte.
*   En l'espèce, le dirigeant (donateur) conserve la présidence de la SAS pendant trois ans. 
*   *Point de vigilence :* Le texte exige une durée de direction de 5 ans. Puisque le donateur ne reste que 3 ans, il faudra impérativement qu'à l'issue de ce mandat, l'un des deux enfants (donataires) prenne le relais à la présidence ou dans une autre fonction de direction éligible (Directeur Général, membre du directoire, etc.) pour les 2 années restantes. Je vous invite à formaliser cet engagement de succession à la direction dans les actes ou par tout moyen démontrant la continuité de la direction.

### 3. Conséquences fiscales chiffrées

Si l'ensemble de ces conditions est respecté et documenté, l'exonération de 75 % s'appliquera sur la valeur des titres.

*   **Valeur totale des titres :** 20 000 000 €
*   **Valeur exonérée (75 %) :** 15 000 000 €
*   **Base imposable (25 %) :** 5 000 000 €

Cette base imposable sera ensuite divisée entre les deux enfants (soit 2 500 000 € chacun), avant application des abattements en ligne directe (100 000 €, renouvelable tous les 15 ans, sous réserve qu'il n'ait pas été utilisé depuis 2008) et du barème des droits de mutation à titre gratuit.

### Conclusion

L'opération projetée est éligible au régime de faveur de l'article 787 B du CGI. Le montage que vous avez préparé avec Maître [Nom du Notaire] est structurellement conforme aux exigences temporelles et formelles du texte.

**Le seul point de risque résiduel réside dans la nature de l'activité de la SAS.** La détention de 40 appartements meublés attire systématiquement l'attention de l'Administration fiscale sur la qualification de "gestion passive de patrimoine". 

Je vous propose, Maître, d'annexer à l'acte de donation du 25 octobre un mémorandum détaillé démontrant l'intensité commerciale de l'activité de la SAS. Alternativement, ou de manière complémentaire, nous pourrions solliciter un rescrit fiscal de l'Administration sur la qualification de l'activité de la société avant la signature de l'acte, bien que le délai de réponse (généralement 3 à 6 mois) ne permette probablement pas de l'obtenir avant le 25 octobre. 

Je me tiens à votre entière disposition pour rédiger ce mémorandum d'activité ou pour affiner les actes de donation en vue de l'échéance du 25 octobre.

Veuillez agréer, Messieurs, l'expression de mes salutations distinguées.

**[Signature]**
**Avocat à la Cour**

---

## T13

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

**Objet : Consultation fiscale – Maintien du report d'imposition suite à la cession de titres par votre holding**

Cher Client,

Suite à notre rendez-vous concernant la cession intervenue en février 2026 des titres de votre société d'exploitation par votre holding, je vous prie de bien vouloir trouver ci-dessous mon analyse et mes recommandations relatives au maintien du report d'imposition prévu à l'article 150-0 B ter du Code Général des Impôts (CGI).

### 1. Rappel de la situation et du risque fiscal
En vertu de l'article 150-0 B ter I 2° du CGI, la cession par votre holding des titres que vous lui avez apportés intervient moins de trois ans après votre apport. En principe, cet événement déclenche l'imposition immédiate de la plus-value d'apport que vous aviez reportée.
Toutefois, la loi prévoit une exception permettant de ne pas mettre fin au report d'imposition, sous des conditions strictes de réinvestissement du produit de la cession.

### 2. Le seuil de réinvestissement
Pour conserver le bénéfice du report d'imposition, votre holding doit réinvestir au moins 70 % du produit de la cession.
Le produit de la vente s'élevant à 9 000 000 €, le montant minimum à réinvestir est donc de :
**9 000 000 € x 70 % = 6 300 000 €.**

### 3. Le délai de réinvestissement
Ce réinvestissement doit être réalisé dans un délai de trois ans à compter de la date de la cession de février 2026. Vous disposez donc, de date à date, **jusqu'en février 2029** pour effectuer cet investissement.

### 4. La nature du réinvestissement et l'activité de la holding
C'est le point le plus critique de votre dossier. Le texte exige que le réinvestissement porte sur le "financement de moyens permanents d'exploitation affectés à son activité", l'activité de la holding devant être éligible au sens de l'article 199 terdecies-0 A du CGI (activité commerciale, industrielle, artisanale, agricole ou libérale).

*   **La nature de l'activité de la holding :** Si votre holding est une "holding passive" (dont l'objet exclusif est la gestion de son propre patrimoine mobilier), elle ne remplit pas cette condition et le réinvestissement sera impossible. Il est impératif que votre holding soit une **"holding animatrice"**, c'est-à-dire qu'elle participe activement à la direction et à la coordination de ses filiales, ou qu'elle exerce une activité opérationnelle directe.
*   **L'exclusion immobilière :** La loi exclut expressément les activités de gestion de son propre patrimoine immobilier. L'achat d'un immeuble (même de bureaux) pour les besoins de la holding ou de ses filiales doit être analysé avec une extrême prudence, l'administration fiscale étant très stricte sur ce point.
*   **Les moyens permanents d'exploitation :** Le réinvestissement peut consister en l'acquisition de titres de nouvelles sociétés d'exploitation, d'un fonds de commerce, de matériel, ou de tout élément corporel ou incorporel nécessaire à l'exercice de l'activité éligible de la holding.

### 5. Les obligations déclaratives
La holding doit formellement prendre l'engagement de réinvestir. Cet engagement doit être joint à la déclaration de revenus de l'année de cession (déclaration 2074 ou formulaire spécifique). Il est crucial de formaliser cet engagement dès la déclaration de l'année 2026 pour ne pas perdre le bénéfice du dispositif.

### 6. Mes recommandations et plan d'action
1.  **Audit de l'activité de la holding :** Je vous conseille de vérifier immédiatement l'objet social de votre holding dans ses statuts et son activité réelle. Si elle est passive, il faudra envisager une modification de l'objet social et une animation effective des filiales pour la qualifier de "holding animatrice".
2.  **Stratégie de réinvestissement :** Nous devrons définir ensemble un plan d'investissement de 6,3 M€ d'ici 2029. L'acquisition de nouvelles filiales actives ou le financement de leur développement sont des pistes privilégiées.
3.  **Formalisation :** Je me chargerai de rédiger et d'annexer l'engagement de réinvestissement à votre prochaine déclaration fiscale.

Je reste à votre entière disposition pour en discuter plus en détail et mettre en place la stratégie la plus adaptée à vos objectifs.

Cordialement,

**Votre Avocat Fiscaliste**

---

## T14

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

**NOTE DE CONSULTATION — TVA : taux applicable à la pose d'une chaudière (art. 278-0 bis A CGI)**

---

**1. Faits et enjeu financier**

- Chantier facturé le 15 avril 2025 : pose d'une chaudière dans une maison achevée depuis 15 ans, occupée par son propriétaire.
- Montant : 8 500 € HT. TVA facturée à 5,5 %, soit **467,50 €**.
- L'administration soutient le taux normal : 8 500 € × 20 % = 1 700 €, soit un **rappel de 1 232,50 €**, auxquels s'ajouteront les intérêts de retard (0,20 % par mois) et d'éventuelles pénalités.

---

**2. Analyse juridique**

*a) Les conditions du I de l'article 278-0 bis A sont réunies*

- Local achevé depuis plus de deux ans : oui (15 ans) — condition du 1° ;
- Usage d'habitation à l'issue des travaux : oui (résidence du propriétaire) — 2° ;
- Prestation portant sur l'amélioration du chauffage — 3°, b.

Sur le seul examen du I, le taux de 5,5 % serait donc rempli. **Mais l'analyse ne s'arrête pas là.**

**2. Le point décisif : le III bis de l'article 278-0 bis A**

Le III bis (introduit par la loi de finances pour 2022, applicable depuis le 1er janvier 2022) écarte le taux réduit pour les prestations **« comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles »**, auxquelles s'applique le taux de l'article 278, soit **20 %**.

Trois précisions importantes sur ce dispositif (cf. également BOI-TVA-LIQ-30-20-90) :

- Le critère est **large** : sont visés le gaz naturel, le fioul, le GPL, le charbon. Il suffit que la chaudière soit *susceptible* de fonctionner, même partiellement, avec de tels combustibles — peu importe sa performance énergétique (les chaudières gaz à condensation, autrefois à 5,5 %, sont désormais exclues) ou l'intention d'usage du client.
- Le taux normal s'applique alors à **l'ensemble de la prestation** comprenant la fourniture ou l'installation de la chaudière — et non au taux intermédiaire de 10 %, le III bis renvoyant expressément à l'article 278. La position de l'administration est cohérente avec ce texte.
- Ne sont **pas** visées les chaudières fonctionnant exclusivement aux énergies renouvelables (bois, granulés, biomasse), qui demeurent au 5,5 % dès lors que les conditions du I sont remplies — ce qui est le cas ici (local achevé depuis plus de deux ans, usage d'habitation, amélioration du chauffage au sens du b du 3°).

**3. Conclusion**

La réponse dépend d'un fait que je dois vérifier avec vous : **la nature de la chaudière installée**.

- **Chaudière gaz, fioul, GPL, ou mixte capable de brûler un combustible fossile** → le taux de 5,5 % était **erroné**. Le III bis renvoie expressément à l'article 278 : le taux correct est **20 %** (et non 10 %). La rectification serait fondée en droit.
- **Chaudière bois/biomasse ne pouvant utiliser aucun combustible fossile** → le taux de 5,5 % était **correct** et la rectification doit être contestée.

Le fait que l'administration réclame le 20 % — et non le 10 % — indique qu'elle se fonde précisément sur le III bis et qu'elle considère la chaudière comme fossile.

**4. Pièces à me transmettre sans délai**

- Facture et devis détaillés du chantier ;
- Fiche technique fabricant de la chaudière (marque, modèle, énergie utilisée) ;
- Le cas échéant, attestation ou documentation démontrant l'impossibilité d'un fonctionnement aux combustibles fossiles.

**5. Stratégie procédurale**

- **Délai** : réponse à la proposition de rectification dans les **30 jours** (prorogeable sur demande motivée, art. L. 57 LPF). Ne laissez pas courir ce délai.
- **Si chaudière renouvelable** : réponse motivée, fiche technique à l'appui. L'administration, qui porte la charge de la preuve du bien-fondé du rappel, devra démontrer que l'appareil est « susceptible d'utiliser des combustibles fossiles ».
- **Si chaudière fossile** : intérêt à régulariser rapidement pour stopper les intérêts de retard, et à vérifier l'absence de pénalités pour mauvaise foi (40 %), difficilement soutenables si l'erreur est de bonne foi ; une demande de remise gracieuse des pénalités (art. L. 247 LPF) peut être envisagée, le principal restant dû.

**6. Points de vigilance**

- La proposition vise-t-elle **d'autres chantiers** ? La même analyse doit être conduite chantier par chantier.
- Le III bis est en vigueur depuis le **1er janvier 2022**. Si l'entreprise a continué à facturer des chaudières fossiles à 5,5 % en 2022-2024, il existe un risque de rappels sur ces exercices (reprise possible jusqu'au 31 décembre de la troisième année suivante, art. L. 169 LPF). Il faut sécuriser dès maintenant la politique de facturation : **20 % pour toute chaudière fossile, 5,5 % réservé aux équipements éligibles** (pompes à chaleur, chaudières biomasse, isolation, etc.).

---

Merci de me faire parvenir la fiche technique de la chaudière : c'est la pièce qui décidera de l'issue du contrôle sur ce point.

---

## T15

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

Bonjour, je vous remercie de me consulter sur cette affaire. Analysons ensemble la situation pour déterminer si l'application du taux de 5,5 % par votre entreprise pour les travaux de rénovation énergétique effectués sur le chantier litigieux était correcte.

Tout d'abord, il est essentiel de comprendre les conditions énoncées par l'article 278-0 bis A du Code Général des Impôts (CGI) pour bénéficier du taux réduit de TVA à 5,5 % pour les prestations de rénovation énergétique.

1. **Les travaux ont été effectués dans des locaux achevés depuis au moins deux ans** : La maison en question a quinze ans, ce qui satisfait largement à cette condition.

2. **Les locaux sont affectés ou destinés à être affectés à un usage d'habitation** : La maison est occupée par son propriétaire, ce qui remplit cette condition.

3. **Les prestations portent sur la pose, l'installation, l'adaptation ou l'entretien de matériaux, d'équipements, d'appareils ou de systèmes ayant pour objet d'économiser l'énergie ou de recourir à de l'énergie produite à partir de sources renouvelables** : L'installation d'une chaudière peut potentiellement entrer dans cette catégorie si elle répond aux critères d'économie d'énergie ou d'utilisation d'énergies renouvelables.

Cependant, il est crucial de considérer le III bis de l'article 278-0 bis A, qui stipule une dérogation importante : **"Par dérogation au I du présent article, le taux prévu à l'article 278 s'applique aux prestations de rénovation énergétique comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles."**

Dans votre cas, l'entreprise a installé une chaudière. La question clé est de savoir si cette chaudière est "susceptible d'utiliser des combustibles fossiles". Si c'est le cas, selon le III bis, le taux réduit de 5,5 % ne s'applique pas, et le taux normal (actuellement 20 %) doit être appliqué.

Pour déterminer la correctitude de l'application du taux de 5,5 %, il nous faut connaître le type de chaudière installée. Si la chaudière est susceptible d'utiliser des combustibles fossiles (comme le gaz, le fioul, etc.), alors l'entreprise aurait dû appliquer le taux de TVA de 20 %. Si, en revanche, la chaudière utilise exclusivement des sources d'énergie renouvelables (comme une chaudière à bois avec un certain niveau de performance, ou une chaudière fonctionnant à l'électricité avec un rendement élevé, encore que cela soit moins commun pour les chaudières), il pourrait être argumenté que le taux réduit est applicable.

Je recommande de vérifier les spécifications techniques de la chaudière installée pour déterminer si elle utilise ou est susceptible d'utiliser des combustibles fossiles. Si tel est le cas, l'administration fiscale a raison de réclamer la différence de TVA. Dans le cas contraire, il faudrait préparer un argumentaire solide pour justifier l'application du taux réduit, en s'appuyant sur les caractéristiques de la chaudière et les dispositions de l'article 278-0 bis A du CGI.

Il est également important de considérer les preuves et la documentation que votre entreprise peut fournir pour étayer sa position, y compris les factures, les spécifications de la chaudière, et toute autre documentation pertinente.

Je vous conseille de rassembler toutes les informations nécessaires concernant la chaudière installée et de me les communiquer pour que nous puissions évaluer ensemble la situation et déterminer la marche à suivre.

---

## T16

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

Bonjour, je vous remercie de me consulter sur cette affaire. Pour déterminer si le remploi envisagé par votre holding permet de maintenir le report d'imposition après la cession des titres de la société d'exploitation, il convient d'analyser ensemble les conditions prévues par l'article 150-0 B ter, I, 2° du Code Général des Impôts (CGI).

Vous avez indiqué que la holding a vendu les titres de la société d'exploitation le 10 novembre 2025, moins de trois ans après que vous les lui ayez apportés, et a ainsi encaissé 9 000 000 euros. L'article 150-0 B ter, I, 2° du CGI prévoit que le report d'imposition est maintenu malgré la cession des titres dans un délai de trois ans à compter de l'apport, si la société bénéficiaire de l'apport (votre holding) prend l'engagement d'investir le produit de la cession dans un délai de deux ans à compter de la date de la cession et à hauteur d'au moins 60 % du montant de ce produit.

Le montant minimum à réinvestir serait donc de 60 % de 9 000 000 euros, soit 5 400 000 euros, dans les deux ans suivant la cession, c'est-à-dire avant le 10 novembre 2027.

L'article précise que le réinvestissement doit être fait dans le financement de moyens permanents d'exploitation affectés à certaines activités spécifiques, notamment commerciale, industrielle, artisanale, libérale, agricole ou financière. Il est explicitement exclu de bénéficier de cette dérogation pour les activités de gestion de son propre patrimoine mobilier ou immobilier.

Vous envisagez de réinvestir dans une société qui achète des immeubles pour les rénover et les revendre. Cette activité peut être considérée comme une activité commerciale au sens de l'article 34 du CGI, dans la mesure où elle implique l'acquisition de biens destinés à être revendus après rénovation, ce qui constitue une opération commerciale.

Cependant, il est crucial de vérifier que la société dans laquelle vous envisagez d'investir remplit les conditions pour être considérée comme exerçant une activité éligible au sens de l'article 150-0 B ter, I, 2°. Il faudra notamment s'assurer que l'activité de rénovation et de revente d'immeubles est bien qualifiable d'activité commerciale et non de gestion de patrimoine immobilier.

Pour maintenir le report d'imposition, votre holding devra prendre l'engagement de réinvestir au moins 5 400 000 euros dans les deux ans suivant la cession, dans une activité éligible. Il est donc essentiel de structurer soigneusement ce réinvestissement et de documenter les démarches entreprises pour satisfaire aux exigences de l'article 150-0 B ter, I, 2° du CGI.

Je vous recommande de préparer un dossier solide qui démontre la nature commerciale de l'activité de la société cible et qui détaille le plan de réinvestissement. Cela vous permettra de justifier auprès de l'administration fiscale que les conditions pour maintenir le report d'imposition sont remplies.

Il serait également prudent de consulter l'administration fiscale par voie de rescrit pour obtenir une confirmation préalable sur la qualification de l'activité de la société cible et sur le respect des conditions de réinvestissement, afin de sécuriser votre position.

Je reste à votre disposition pour discuter plus en détail des étapes à suivre et pour vous aider à préparer les éléments nécessaires à la justification de votre réinvestissement.

---

## T17

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

## CONSULTATION

**Objet :** cession de parts d'une SCI à prépondérance immobilière – droits d'enregistrement, base taxable, mentions obligatoires de l'acte
**Date de l'acte projeté :** 20 mars 2024
**Prix annoncé :** 4 000 000 €

---

### Avertissement liminaire

Le texte que vous me communiquez ne reprend que le I, 2° et le III de l'article 726 du CGI. **Le II de l'article 726 est ici déterminant** : c'est lui qui fixe l'assiette du droit pour les personnes morales à prépondérance immobilière, et il déroge à la règle du prix. Ma réponse en tient compte. Je réserve par ailleurs mon analyse définitive à la lecture des statuts, du dernier bilan et de l'état de l'actif immobilier de la SCI.

---

## 1. Qualification : société à prépondérance immobilière

Trois conditions du I, 2° :

- **Titres non négociés** sur un marché réglementé ou un SMN : acquis pour une SCI (parts sociales non négociables).
- **Actif principalement immobilier en France** : « principalement » = plus de 50 %. Avec 80 % d'immeubles situés en France, le seuil est franchi. Attention : le texte vise l'actif **à la date de la cession *ou* à un moment quelconque de l'année précédant la cession** — une « décharge » de l'immobilier réalisée dans les douze mois précédant le 20 mars 2024 serait sans effet. Nous devrons documenter la composition de l'actif au 20 mars 2024 **et** depuis le 20 mars 2023.
- **Aucune exclusion applicable** (organisme HLM, société foncière au sens du 1 du II de l'article 199 terdecies‑0 AB, SEM de logement social).

Deux précisions utiles :
- le ratio s'apprécie en **valeur réelle** (et non en valeur comptable) ;
- contrairement aux articles 150 UB ou 244 bis A, **il n'y a pas d'exclusion des immeubles affectés à l'exploitation** pour l'application de l'article 726. Le débat est ici sans objet (SCI), mais je le signale pour les filiales éventuelles.

**Conclusion : taux de 5 %** (droit budgétaire d'État, sans taxe additionnelle départementale ou communale).

---

## 2. La question centrale : l'assiette, qui n'est pas nécessairement le prix

C'est le point sur lequel je vous alerte **avant signature**.

Pour les cessions de participations dans une personne morale à prépondérance immobilière, l'assiette n'est pas le prix stipulé mais, à concurrence de la fraction des titres cédés :

> **la valeur réelle des biens et droits immobiliers** détenus directement ou indirectement (via d'autres personnes morales à prépondérance immobilière), **sous déduction du seul passif afférent à l'acquisition de ces biens**,
> **+ la valeur réelle des autres éléments d'actif bruts**.

Autrement dit : les dettes **autres** que celles contractées pour l'acquisition des immeubles (compte courant d'associé de financement de travaux, dette d'exploitation, dividende à distribuer, emprunt de refinancement, dette fiscale latente…) **ne sont pas déductibles**. Le mécanisme est un dispositif anti‑« gonflement du passif ».

**Conséquence pratique :** un prix de 4 000 000 € correspondant à un immeuble de 10 000 000 € financé par un emprunt d'acquisition de 4 000 000 € et un compte courant de 2 000 000 € donne une assiette de **6 000 000 €**, soit **300 000 € de droits** et non 200 000 €.

**Il me faut donc, avant chiffrage définitif :**
1. la valeur vénale des immeubles (expertise ou évaluation retenue par les parties) ;
2. le détail du passif avec, pour chaque ligne, **la justification de son affectation à l'acquisition** de l'immeuble (acte de prêt, tableau d'amortissement, affectation hypothécaire) ;
3. l'inventaire des autres actifs **bruts** (trésorerie, créances, dépôts de garantie…) en valeur réelle ;
4. le pourcentage exact de parts cédées.

À défaut de justificatifs sur l'affectation du passif, l'administration réintègre la dette dans l'assiette. **Je recommande de constituer un dossier probatoire annexé à l'acte.**

À titre indicatif seulement, **si** l'assiette légale coïncidait avec le prix : 4 000 000 × 5 % = **200 000 €**.

---

## 3. Redevable, forme et délai

- **Redevable légal** : l'acquéreur (art. 1712 CGI, sauf stipulation contraire). Les parties signataires d'un acte sous seing privé sont tenues solidairement du dépôt et du paiement. **Prévoyez une clause expresse** de prise en charge, avec provision séquestrée le jour de la signature.
- **Formalité** : enregistrement de l'acte auprès du service départemental de l'enregistrement compétent (art. 635, 2, 7° CGI ; à défaut d'acte, déclaration n° 2759‑SD).
- **Délai : un mois à compter du 20 mars 2024**, soit le 20 avril 2024 — jour qui tombe un **samedi**, la formalité peut donc être accomplie jusqu'au **lundi 22 avril 2024** inclus.
- **Retard** : intérêt de retard de 0,20 % par mois (art. 1727) + majoration de 10 % (art. 1728).
- **Cession réalisée à l'étranger** (III, A) : obligation de faire constater la cession, **dans le mois**, par acte authentique reçu par un notaire exerçant en France. Si la signature doit intervenir hors de France (signature électronique à distance, closing à l'étranger), organisez cette réitération notariée dès à présent — c'est une source classique de contentieux.

---

## 4. Mentions obligatoires à insérer dans l'acte (art. 726, III, B)

L'acte **doit** indiquer expressément les trois points suivants. Je vous propose la rédaction ci‑dessous, à adapter après vérification des statuts :

> **« Déclarations au titre de l'article 726, III, B du code général des impôts**
>
> Les parties déclarent expressément, pour les besoins de l'enregistrement :
>
> **1°** que la Société **n'est pas** [*/ est*] une société visée à l'article 1655 ter du code général des impôts ;
>
> **2°** que les parts sociales cédées **ne confèrent pas** [*/ confèrent*] au Cessionnaire, directement ou indirectement, le droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'article 728 du même code ;
>
> **3°** que le Cessionnaire **n'a acquitté et ne s'engage à acquitter**, directement ou indirectement, aucune dette contractée auprès du Cédant par la Société [*/ que le Cessionnaire s'engage à acquitter, directement ou indirectement, les dettes contractées auprès du Cédant par la Société, d'un montant de … euros*].
>
> Les parties déclarent en outre, pour l'application du II de l'article 726 du code général des impôts, que la valeur réelle des biens et droits immobiliers détenus directement et indirectement par la Société s'élève à … euros, que le passif afférent à leur acquisition s'élève à … euros, et que la valeur réelle des autres éléments d'actif bruts s'élève à … euros, l'assiette du droit ressortant, à concurrence de la fraction des titres cédés (… %), à … euros. Un état détaillé figure en Annexe … . »

**Pourquoi ces mentions ne sont pas de pure forme :**

- **1° (art. 1655 ter)** : si la SCI est une société **d'attribution transparente**, la cession est fiscalement traitée comme une cession de l'immeuble lui‑même. On sort du 5 % pour tomber dans les **droits de mutation à titre onéreux d'immeubles** (≈ 5,80 % à 5,81 % selon le département, hors contribution de sécurité immobilière), avec acte notarié et publicité foncière obligatoires. Vérification impérative des statuts.
- **2° (art. 728)** : même conséquence lorsque les parts confèrent la jouissance d'immeubles. À vérifier au regard des clauses statutaires d'attribution en jouissance et des éventuelles conventions annexes.
- **3°** : la reprise de compte courant du cédant par le cessionnaire est un **complément de prix** ; l'administration la réintègre dans l'assiette. Si un compte courant du cédant existe (fréquent en SCI), il faut clarifier son sort **maintenant** : cession du compte courant en sus du prix des parts (le prix de cession du compte courant n'est pas soumis au droit de 5 %, mais l'existence de la dette a une incidence sur l'assiette au titre du II), remboursement préalable, ou abandon.

L'omission de ces mentions, ou une déclaration inexacte, expose à rectification, aux intérêts de retard et, en cas de dissimulation, aux majorations de l'article 1729 ainsi qu'aux sanctions de la dissimulation de prix (art. 1837), les parties étant solidairement tenues.

---

## 5. Points de vigilance à traiter avant la signature du 20 mars

1. **Plus‑value du cédant.** Si vous êtes une personne physique et que la SCI relève de l'IR, la cession relève du régime des plus‑values immobilières (art. 150 UB) : 19 % + 17,2 % de prélèvements sociaux, abattements pour durée de détention (exonération d'IR à 22 ans, de PS à 30 ans), et surtaxe de l'article 1609 nonies G à examiner. Si vous êtes non‑résident : prélèvement de l'article 244 bis A et, le cas échéant, représentant fiscal accrédité. **Ce chiffrage doit être fait avant de figer le prix.**
2. **Droit de préemption urbain.** Attention à l'article L. 213‑1 du code de l'urbanisme : la cession de la majorité des parts d'une SCI dont le patrimoine est constitué d'une unité foncière dont la cession serait soumise au DPU est elle‑même soumise à préemption. Si tel est le cas, une **DIA doit être purgée avant signature** — c'est une cause de nullité, indépendante de la fiscalité.
3. **Agrément et formalités sociales** : agrément des associés, notification à la société, dépôt des statuts modifiés au greffe / RBE.
4. **Clause fiscale de l'acte** : prise en charge des droits par le cessionnaire, provision au closing, obligation de dépôt à la charge d'une partie identifiée, garantie de passif fiscal (IFI, taxe de 3 % des articles 990 D et suivants si la chaîne de détention comporte des entités étrangères, TVA sur travaux, taxe sur les bureaux le cas échéant).
5. **Cohérence prix / valeur vénale** : une assiette légale nettement supérieure au prix attire l'attention sur l'insuffisance de prix (art. L. 17 LPF). Il faut pouvoir justifier l'écart par le passif non déductible, et non par une sous‑évaluation.

---

## 6. Pièces à me transmettre sans délai

Statuts à jour ; procès‑verbaux d'assemblée ; derniers bilans et balance détaillée ; actes de prêt et tableaux d'amortissement ; état des comptes courants d'associés ; titres de propriété et évaluation des immeubles ; baux en cours ; le cas échéant, extrait de la matrice cadastrale et renseignements d'urbanisme.

---

### Synthèse

| Question | Réponse |
|---|---|
| Régime | Cession de participations dans une personne morale à prépondérance immobilière (CGI, art. 726, I, 2°) |
| Taux | **5 %** |
| Assiette | **Non le prix** : valeur réelle des immeubles − passif d'acquisition seul + autres actifs bruts, au prorata des titres cédés (art. 726, II) — chiffrage à finaliser |
| Ordre de grandeur | **200 000 €** si l'assiette est égale au prix ; davantage en présence d'un passif non affecté à l'acquisition |
| Redevable | L'acquéreur (art. 1712), parties solidaires |
| Délai | Enregistrement au plus tard le **lundi 22 avril 2024** |
| Acte | Doit comporter les **trois déclarations du III, B** de l'article 726, et j'y ajoute l'état détaillé de l'assiette |
| Alerte | Vérifier art. 1655 ter / art. 728 : le cas échéant, DMTO immobiliers (~5,81 %) et acte notarié |

Je vous propose de me communiquer le projet d'acte pour insertion des clauses fiscales et validation du chiffrage définitif avant le 20 mars.

---

## T18

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
**Objet :** Distribution de dividendes à une société mère luxembourgeoise – Application de la retenue à la source
**Date :** 15 novembre 2024
**Destinataire :** Direction financière / Juridique de la société française
**Référence :** CGI art. 119 bis 2 ; Directive 2011/96/UE ; Convention fiscale franco-luxembourgeoise

---

### 🔹 CONCLUSION SYNTHÉTIQUE
**Aucune retenue à la source ne sera due** sur la distribution de 20 000 000 € prévue le 15 novembre 2024, sous réserve du respect des conditions de la directive « mère-fille » et de la constitution d’un dossier documentaire conforme. La société française pourra appliquer l’exonération de droit, sans demande préalable d’agrément, mais devra respecter des obligations déclaratives et de conservation de pièces.

---

### I. CADRE JURIDIQUE APPLICABLE

1. **Principe de droit interne** (CGI, art. 119 bis, 2, 1er alinéa) : les dividendes versés à des non-résidents sont soumis à une retenue à la source au taux de droit commun de **30 %** (CGI, art. 187, 1).
2. **Exception communautaire** (CGI, art. 119 bis, 2, 2°) : transposition de la directive 2011/96/UE (directive « mère-fille »). Les dividendes versés à une société mère établie dans un État membre de l’UE sont **exonérés de retenue à la source** lorsque les conditions cumulatives suivantes sont remplies.
3. **Convention fiscale franco-luxembourgeoise** (art. 10) : prévoit également une exonération (ou un taux de 0 %) lorsque la mère détient au moins 10 % du capital. La directive prime en pratique et offre un régime plus direct.

---

### II. ANALYSE DES CONDITIONS D’EXONÉRATION

| Condition | Situation client | Conformité |
|-----------|------------------|------------|
| **Forme juridique** de la mère | Société anonyme (SA) luxembourgeoise | ✅ Liste annexée à la directive |
| **Résidence fiscale** | Luxembourg (État membre UE) | ✅ |
| **Détention du capital** | 100 % depuis 5 ans | ✅ (seuil ≥ 10 %, durée ≥ 2 ans) |
| **Assujettissement à l’IS** | Soumise à l’impôt sur les sociétés luxembourgeois, sans exonération | ✅ |
| **Réalité économique / Substance** | À vérifier (siège effectif, gouvernance, activité, personnel) | ⚠️ Point de vigilance |

👉 **Conclusion d’analyse** : Les conditions légales et communautaires sont remplies. L’exonération de retenue à la source est applicable.

---

### III. FORMALITÉS ET OBLIGATIONS DÉCLARATIVES

L’exonération est **d’application directe** depuis la réforme de 2019. Aucun agrément préalable n’est requis, mais la société française doit :

1. **Constituer un dossier documentaire** (à conserver 3 ans) :
   - Attestation de résidence fiscale luxembourgeoise (valide pour l’année 2024)
   - Déclaration sur l’honneur de la société mère attestant du respect des conditions de la directive 2011/96/UE
   - Justificatif de détention (extrait du registre des actionnaires, procès-verbal d’assemblée)
   - Attestation d’assujettissement à l’IS luxembourgeois (ou mention dans les comptes/statuts)

2. **Déposer la déclaration de retenue à la source** (formulaire CERFA n° 5000) :
   - Délai : **avant le 15 décembre 2024** (15 du mois suivant le paiement)
   - Mentionner explicitement l’exonération au titre du CGI art. 119 bis, 2, 2°
   - Joindre ou conserver les pièces justificatives en cas de contrôle

3. **Paiement** : Aucun versement au Trésor public n’est attendu. En cas d’erreur ou de contrôle, l’administration pourra exiger le paiement de la retenue + intérêts de retard.

---

### IV. POINTS DE VIGILANCE

| Risque | Recommandation |
|--------|----------------|
| **Clause anti-abus** (directive art. 1(2) + CGI art. 205 A) | Vérifier que la société mère luxembourgeoise dispose d’une substance réelle (siège de direction effective, personnel qualifié, activité de holding active, comptes audités). Une structure « écran » ou purement fiscale pourrait entraîner une requalification. |
| **Principal Purpose Test (PPT)** | S’assurer que la distribution ne s’inscrit pas dans un montage dont l’un des objectifs principaux est d’obtenir un avantage fiscal indu. |
| **Délai de conservation** | Conserver l’ensemble des pièces justificatives jusqu’au **15 novembre 2027** (délai de reprise de droit commun). |
| **Autres produits** | Si la distribution inclut des intérêts, redevances ou plus-values, le régime de retenue à la source diffère. Cette note ne couvre que les dividendes. |

---

### V. RECOMMANDATIONS OPÉRATIONNELLES

1. **Dès maintenant** : Solliciter l’attestation de résidence fiscale 2024 auprès de l’administration luxembourgeoise et faire signer la déclaration sur l’honneur par la société mère.
2. **Avant le 15/11/2024** : Valider le bordereau de virement, mentionner « Dividendes – Exonération CGI 119 bis 2, 2° » et archiver le dossier.
3. **Avant le 15/12/2024** : Déposer le formulaire 5000 via le portail impots.gouv.fr, en cochant la case d’exonération et en indiquant le motif légal.
4. **En cas de doute sur la substance** : Envisager une demande d’attestation de non-retenue à la source auprès du Service des Impôts des Entreprises (SIE) compétent, ou solliciter un rescrit écrit.

---

### VI. CONCLUSION

La distribution de 20 000 000 € à la société mère luxembourgeoise **ne donne pas lieu à retenue à la source**, sous réserve du respect des conditions de la directive mère-fille et de la constitution d’un dossier documentaire probant. La société française peut procéder au virement net de toute retenue, à condition de déposer le formulaire 5000 dans les délais et de conserver les justificatifs.

Je reste à votre disposition pour :
- Rédiger les modèles de déclaration sur l’honneur et de bordereau de distribution
- Vérifier la conformité du dossier documentaire avant paiement
- Accompagner le dépôt du formulaire 5000 ou, si nécessaire, la demande de rescrit

*Note : Cette analyse s’appuie sur la législation et la jurisprudence en vigueur à la date de la distribution (15 novembre 2024). Elle ne préjuge pas d’une éventuelle évolution législative ou d’une position particulière de l’administration dans le cadre d’un contrôle.*

**[Signature]**  
Avocat au Barreau de Paris  
Spécialiste en fiscalité des entreprises et droit international

---

## T19

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

**CABINET [NOM]**
Avocats au Barreau de [Ville]
Droit fiscal – Droit des sociétés
[Coordonnées]

**OBJET :** Consultation fiscale – Maintien du report d’imposition au titre de l’article 150-0 B ter du CGI suite à la cession de titres par votre holding
**DATE :** [Date du jour]
**DESTINATAIRE :** [Nom du client]

---

Monsieur/Madame,

Je vous remercie de votre confiance et prends acte des éléments que vous m’avez communiqués. Votre holding, que vous contrôlez à 100 %, a cédé en février 2026 les titres d’une société d’exploitation qu’elle détenait depuis moins de trois ans après leur apport, pour un produit net de cession de 9 000 000 €. Les fonds sont actuellement disponibles sur le compte de la holding et vous souhaitez conserver le bénéfice du report d’imposition attaché à l’apport initial.

Je vous prie de trouver ci-dessous mon analyse juridique et mes recommandations opérationnelles.

### 1. Cadre légal et échéances
Conformément à l’article 150-0 B ter, I, 2° du CGI, la cession des titres apportés dans un délai de trois ans met normalement fin au report d’imposition et rend la plus-value latente immédiatement imposable. Toutefois, une dérogation expresse permet de maintenir le report sous condition d’un réinvestissement :
- **Montant minimum :** 70 % du produit de cession, soit **6 300 000 €**
- **Délai de réalisation :** dans les **trois ans à compter de la date de cession**, soit au plus tard **février 2029**
- **Nature des investissements :** financement de « moyens permanents d’exploitation » affectés à une activité éligible au sens du 3° du C du I de l’article 199 terdecies-0 A du CGI
- **Exclusion expresse :** les activités de gestion de patrimoine immobilier sont formellement exclues du bénéfice de cette dérogation.

### 2. Qualification des investissements éligibles
La notion de « moyens permanents d’exploitation » est interprétée strictement par l’administration fiscale (BOI-RPPM-PVBMI-30-30-20). À titre indicatif, sont généralement considérés comme éligibles :
- Apports en capital ou souscription à l’augmentation de capital de sociétés exerçant une activité industrielle, commerciale, artisanale, agricole ou libérale à titre principal
- Acquisition de fonds de commerce, de matériel, d’outillages, de logiciels métier, de brevets ou de marques directement affectés à l’exploitation
- Prêts ou avances en compte courant à des sociétés opérationnelles, sous réserve que les fonds soient effectivement utilisés pour acquérir ou financer des actifs d’exploitation durables
- Souscription à certains véhicules d’investissement agréés (FCPI, FIP, fonds de développement économique) sous conditions strictes de qualification

⚠️ **Sont exclus :** les placements financiers classiques (comptes à terme, OPCVM, assurance-vie, SCPI, SCI de gestion ou de location, holdings purement patrimoniales, prêts à des entités à activité immobilière ou financière).

### 3. Formalités et traçabilité exigées
Pour que la dérogation soit opposable à l’administration, votre holding doit :
1. **Prendre un engagement formel de réinvestissement**, mentionné dans la déclaration de résultats (liasse fiscale) ou formalisé par acte séparé daté et signé
2. **Réaliser effectivement les décaissements éligibles** avant février 2029
3. **Conserver l’ensemble des justificatifs** : contrats, factures, procès-verbaux d’assemblées, attestations bancaires, tableaux de suivi des flux, preuves d’affectation à l’exploitation
4. **Déclarer le maintien du report** dans les déclarations fiscales annuelles et joindre l’engagement ainsi que l’état d’avancement des réinvestissements

En cas de non-respect du seuil de 70 %, du délai ou de la nature des actifs, le report sera remis en cause. La plus-value deviendra immédiatement imposable au barème progressif ou au PFU, avec application d’intérêts de retard et, potentiellement, de pénalités pour manquement délibéré.

### 4. Recommandations opérationnelles
Compte tenu de la situation actuelle (fonds dormants), je vous conseille de :
- **Identifier sans délai** un ou plusieurs projets d’investissement éligibles (création/reprise de société opérationnelle, acquisition d’actifs d’exploitation, financement de développement commercial/industriel, etc.)
- **Éviter tout placement financier ou immobilier** qui ne répondrait pas aux critères légaux
- **Structurer les opérations en amont** pour garantir la qualification fiscale et la traçabilité des flux
- **Formaliser l’engagement de réinvestissement** dans les meilleurs délais, avant la prochaine échéance déclarative
- **Mettre en place un tableau de suivi** des décaissements, avec dates, montants, bénéficiaires et nature des actifs financés

### 5. Prochaines étapes
Je me tiens à votre disposition pour :
- Rédiger l’engagement de réinvestissement conforme aux exigences administratives
- Valider la qualification fiscale des opérations que vous envisagez
- Assurer le suivi déclaratif et la constitution du dossier probant
- Anticiper les questions susceptibles d’être soulevées en cas de contrôle fiscal

Je vous invite à me transmettre, dans les meilleurs délais, les documents relatifs à l’apport initial, à la cession de février 2026, ainsi que les projets d’investissement envisagés, afin que je puisse vous remettre une note de validation fiscale détaillée.

Je reste à votre entière disposition pour en discuter lors d’un prochain rendez-vous.

Veuillez agréer, Monsieur/Madame, l’expression de mes salutations distinguées.

**[Signature]**  
Avocat fiscaliste  
Cabinet [Nom]

---

## T20

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

## 1. Droit d’enregistrement applicable

La SCI est une personne morale dont les parts ne sont pas négociées sur un marché réglementé. Son actif étant constitué à **80 % d’immeubles situés en France**, elle est, à la date de la cession, une **personne morale à prépondérance immobilière** au sens de l’article 726, I, 2° du CGI.

La cession de ses parts est donc soumise au droit d’enregistrement proportionnel de :

\[
4\,000\,000 \times 5\% = 200\,000\ \text{euros}
\]

Le droit dû est donc, sous réserve que le prix corresponde au moins à la valeur vénale des titres et qu’il n’existe pas de charges augmentant le prix taxable, de **200 000 €**.

Il n’y a pas lieu d’appliquer l’abattement de 23 000 € applicable, dans certaines hypothèses, aux cessions ordinaires de droits sociaux : cet abattement ne concerne pas les cessions de participations dans des personnes morales à prépondérance immobilière taxées à 5 %.

L’assiette doit, en pratique, être le **prix stipulé augmenté des charges imposées à l’acquéreur** ; l’administration peut retenir la valeur vénale si elle excède le prix déclaré.

## 2. Délai et formalité

La cession de parts sociales doit être soumise à la formalité de l’enregistrement dans le délai d’un mois de sa date.

Pour un acte signé le **20 septembre 2023**, la formalité devait donc être accomplie, en principe, au plus tard le **20 octobre 2023**.

Le droit est normalement acquitté lors de cette formalité. L’acquéreur supporte usuellement économiquement le droit, mais la répartition contractuelle entre les parties ne limite pas les droits de l’administration à réclamer le paiement aux personnes légalement tenues.

## 3. Contenu de l’acte

L’article 726 ne prévoit pas, en lui-même, une liste autonome de mentions obligatoires spécifique aux cessions de participations immobilières. Néanmoins, afin de sécuriser la liquidation du droit de 5 % et de documenter le dossier, l’acte devrait notamment comporter :

- l’identification complète du cédant et du cessionnaire ;
- l’identification de la SCI : dénomination, siège, numéro SIREN, capital social, répartition du capital avant cession ;
- le nombre, la numérotation ou l’identification des parts cédées, leur valeur nominale et les droits qui y sont attachés ;
- l’origine de propriété des parts par le cédant ;
- le prix de cession, les modalités de paiement, ainsi que toute charge ou tout complément de prix éventuel ;
- la date de transfert de propriété et de jouissance ;
- les déclarations nécessaires sur l’absence ou l’existence d’un agrément requis au titre des statuts de la SCI et, le cas échéant, la justification de cet agrément ;
- une déclaration relative au régime fiscal applicable, indiquant que la SCI est à prépondérance immobilière au sens de l’article 726, I, 2° du CGI ;
- les éléments justifiant cette qualification : notamment la composition de l’actif, la valeur des immeubles français et, si nécessaire, le calcul faisant apparaître la proportion de 80 % ;
- une clause précisant la liquidation des droits d’enregistrement au taux de 5 %, soit 200 000 € sur la base retenue de 4 000 000 €, et désignant la partie qui en supportera la charge économique ;
- les pouvoirs donnés au rédacteur ou au mandataire pour accomplir l’enregistrement.

Il est également prudent d’annexer ou de conserver au dossier une situation patrimoniale et une valorisation de la SCI à la date de la cession, permettant de justifier tant la prépondérance immobilière que l’assiette déclarée.

## 4. Cas particulier : cession réalisée à l’étranger

La dernière phrase de l’article 726, I, 2° est impérative :

> lorsque la cession est réalisée à l’étranger, elle doit être constatée dans le délai d’un mois par un acte authentique reçu par un notaire exerçant en France.

Ainsi :

- **si l’acte est conclu en France**, l’article 726 n’impose pas, pour ce seul motif, un acte notarié ; un acte sous seing privé peut être envisagé, sous réserve des exigences civiles et statutaires de la SCI ;
- **si la cession est réalisée à l’étranger**, elle doit impérativement être constatée, dans le mois, par un **acte authentique reçu par un notaire français**. Un simple acte sous seing privé étranger ne satisfait pas à cette exigence particulière.

En synthèse : **droit de 5 %, soit 200 000 €**, à acquitter lors de l’enregistrement dans le mois ; et, si l’opération est réalisée à l’étranger, nécessité supplémentaire d’un **acte authentique français dans ce même délai**.

---

## T21

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

**NOTE DE CONSULTATION**

**Objet :** Donation de la totalité des titres de la SAS (parc de 40 appartements meublés — valeur 20 M€) au profit des deux enfants, à parts égales et en pleine propriété — Applicabilité de l'exonération partielle de droits (CGI, art. 787 B).

---

### Conclusion synthétique

**Oui, l'exonération à 75 % est applicable.** Le seul point de discussion — la nature de l'activité de la société — se résout favorablement : l'exploitation de 40 appartements en location meublée constitue une activité *commerciale* au sens des articles 34 et 35 du CGI, et non une « gestion de son propre patrimoine immobilier » exclue par le deuxième alinéa. Les trois conditions du dispositif sont par ailleurs réunies. Quelques vérifications de forme et points de vigilance figurent au § 6.

---

### 1. La condition d'activité — point névralgique du dossier

Je pars du postulat — à confirmer — que la SAS donne ces appartements en **location meublée à titre habituel**.

- La location meublée est une **activité commerciale par nature** : les produits relèvent des BIC (art. 34 CGI ; BOI-BIC-CHAMP-10-10-20-20). Le fait que la SAS soit à l'IS est sans incidence : l'appréciation porte sur la *nature* de l'activité au regard des articles 34 et 35.
- L'exclusion du deuxième alinéa vise les activités patrimoniales — location d'immeubles **nus**, gestion d'un portefeuille de valeurs mobilières (BOI-ENR-DMTG-10-20-20-20, § 80 et s.). L'administration admet expressément que la **location d'immeubles meublés est une activité commerciale éligible**. C'est la nature de l'exploitation qui importe, non la propriété des immeubles par la société.
- L'importance du parc (40 lots) démontre une exploitation habituelle et organisée, qui écarte toute qualification de simple gestion patrimoniale.
- L'activité doit être « principale » : elle est ici a priori exclusive. À vérifier : absence de location nue significative ou de placements de trésorerie prépondérants.

→ **Condition remplie.**

### 2. L'engagement collectif de conservation (1°)

- Seuils applicables aux engagements conclus depuis le 1er janvier 2019 (art. 31, loi n° 2018-1317 du 28 déc. 2018) : 10 % des droits financiers et 20 % des droits de vote (société non cotée). L'engagement porte sur **100 % des droits** → seuils très largement dépassés.
- Le donateur détenant seul la totalité des titres, l'engagement est **« réputé collectif »** (seuil atteint par le donateur et ses ayants cause) : il pouvait valablement être signé par lui seul.
- Durée minimale de deux ans : conclu le 3 mars 2021, il a couru plus de deux ans et est **en cours** à la date de la transmission (25 octobre 2023) → condition remplie.
- La transmission elle-même ne rompt pas l'engagement : les donataires le poursuivent jusqu'à son terme, leurs engagements individuels prenant le relais.

### 3. Les engagements individuels de conservation (2°)

- Chaque enfant doit s'engager à conserver les titres pendant **4 ans à compter de l'expiration de l'engagement collectif** (durée issue de la réforme de 2019). Il est indiqué que chacun prend « l'engagement individuel prévu par les textes » → condition remplie.
- Ces engagements devront figurer dans l'acte de donation.

### 4. La fonction de direction (3°)

- Depuis la réforme de 2019, la fonction peut être exercée par **le donateur lui-même** (« l'un des héritiers, donataires ou légataires *ou le donateur* »), pendant la durée de l'engagement collectif **et** pendant les trois ans suivant la transmission.
- La **présidence** d'une SAS figure parmi les fonctions visées par l'article 975, III, 1°, auquel renvoie le texte.
- Le maintien de la présidence pendant trois ans satisfait donc la condition, sous trois réserves :
  - **exercice effectif** de la fonction (pouvoirs réels, implication effective ; une rémunération, même modeste, est un indice utile) ;
  - exercice **pendant l'engagement collectif** : vérifier qu'il était président depuis mars 2021 et qu'il le demeurera jusqu'au terme de l'engagement si celui-ci court au-delà du 25 octobre 2026 ;
  - **compatibilité statutaire** : vérifier que les statuts n'exigent pas que le président soit associé (il ne détiendra plus aucun titre).

### 5. Conséquences chiffrées (indicatif)

- Assiette exonérée : 15 M€ ; assiette taxable : 5 M€, soit 2,5 M€ par enfant.
- Après abattement de 100 000 € par enfant (art. 779, sous réserve de l'absence de donation antérieure depuis 15 ans) : 2,4 M€ taxables par enfant.
- Droits (barème 2023) : **≈ 842 000 € par enfant, soit ≈ 1,68 M€ au total** — au lieu d'environ 8,4 M€ sans le régime. Paiement fractionné ou différé possible (art. 404 A).

### 6. Points de vigilance et recommandations

- **Sanction** : rupture d'un engagement (cession avant terme) ou cessation de la présidence avant l'échéance → rappel de l'exonération majoré d'intérêts de retard, sauf exceptions légales (décès, licenciement, invalidité, restructurations, reprise des engagements lors d'une transmission ultérieure). Les enfants doivent en être parfaitement informés.
- **Vérifications formelles** : date certaine de l'acte du 3 mars 2021 (enregistrement) et durée stipulée — l'engagement doit impérativement être en cours le jour de la donation ; le proroger avant signature si nécessaire.
- **Forme** : privilégier la **donation-partage** (art. 1075 et s. C. civ.), qui fige la valeur des titres et sécurise l'égalité entre les enfants.
- L'**âge du donateur** (62 ans) est sans incidence : la réduction de droits pour donation avant 70 ans (ancien art. 790 A) est supprimée depuis le 1er janvier 2019.
- Piste écartée mais à porter à sa connaissance : une **réserve d'usufruit** réduirait encore l'assiette (usufruit de 40 % entre 61 et 70 ans, art. 669) ; le client ayant opté pour la pleine propriété, nous n'en faisons pas le fondement de la structuration.

---

**Conclusion :** L'exonération partielle de l'article 787 B est applicable à hauteur de 75 % de la valeur des titres, soit 15 M€. Sous réserve des vérifications indiquées, la donation peut être signée le 25 octobre 2023.

---

## T22

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

## Conclusion

**Non.** Sur les faits décrits, la donation du 25 octobre 2023 ne peut pas bénéficier de l’exonération de 75 % prévue à l’article 787 B du CGI, même si les conditions de conservation et de direction sont par ailleurs satisfaites.

## Motif : l’activité de la SAS est exclue

La location habituelle de logements meublés constitue certes une activité commerciale au sens fiscal de l’article 35 du CGI.

Toutefois, le deuxième alinéa du texte applicable prévoit expressément que :

> « n’est pas considérée comme une activité […] commerciale […] l’exercice par une société d’une activité de gestion de son propre patrimoine […] immobilier ».

Or la SAS :

- possède elle-même les quarante appartements ;
- les donne en location meublée ;
- et, d’après les éléments communiqués, n’exerce aucune autre activité opérationnelle principale.

Son activité doit donc être regardée comme la **gestion de son propre patrimoine immobilier**. L’exclusion spéciale du deuxième alinéa prévaut sur la qualification fiscale de la location meublée au regard de l’article 35.

La solution pourrait être différente pour une véritable activité hôtelière ou para-hôtelière, caractérisée par des prestations de services substantielles et une exploitation commerciale dépassant la simple mise à disposition de logements meublés. De tels éléments ne figurent cependant pas dans les faits exposés.

## Incidence de la date du 25 octobre 2023

La date est déterminante. La nouvelle définition légale de l’activité éligible, issue de la loi de finances pour 2024, a été rendue applicable aux transmissions intervenues **à compter du 17 octobre 2023**.

La donation signée le **25 octobre 2023** entre donc dans son champ, bien que l’engagement collectif ait été conclu le 3 mars 2021. La signature antérieure de cet engagement ne cristallise pas le régime fiscal applicable : l’éligibilité doit notamment être appréciée au jour de la transmission.

## Les autres conditions ne permettent pas de corriger cette difficulté

Les éléments suivants paraissent conformes au dispositif :

- engagement collectif portant sur 100 % des droits ;
- durée minimale de deux ans acquise ;
- engagements individuels des deux enfants ;
- transmission en pleine propriété ;
- conservation de la présidence par le donateur pendant trois ans après la donation, sous réserve qu’il ait bien exercé cette fonction dans les conditions requises pendant l’engagement collectif.

Mais ces conditions ne suffisent pas : **l’exercice d’une activité éligible est une condition préalable et autonome**.

## Conséquences pratiques

La donation serait donc soumise aux droits de donation sur la valeur intégrale des titres, soit **10 millions d’euros par enfant**, sous déduction notamment de l’abattement en ligne directe disponible.

La réduction de droits de 50 % prévue pour certaines donations d’entreprises en pleine propriété par un donateur âgé de moins de 70 ans ne serait pas davantage applicable, puisqu’elle suppose que les titres bénéficient de l’exonération de l’article 787 B.

En conséquence, je déconseillerais de déposer l’acte en revendiquant le régime Dutreil sans pouvoir démontrer que la SAS exerce en réalité une véritable activité hôtelière ou para-hôtelière principale, distincte de la simple gestion locative de ses propres appartements.

---

## T23

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

**Objet : Conseil sur le réinvestissement du produit de cession pour maintenir le report d’imposition (Article 150-0 B ter du CGI)**

**À l’attention de [Nom du Client],**
**Holding [Nom de la Holding]**

**Référence :** Cession de titres en février 2026 – Obligation de réinvestissement pour préserver le report d’imposition

---

### **1. Rappel du contexte et enjeux fiscaux**
Votre holding a cédé en **février 2026** des titres d’une société d’exploitation pour un montant de **9 000 000 €**, moins de **3 ans après leur apport** par vos soins. Conformément à l’**article 150-0 B ter, I, 2° du CGI**, cette cession aurait normalement **mis fin au report d’imposition** sur la plus-value latente au moment de l’apport.

Cependant, le texte prévoit une **dérogation** : le report d’imposition peut être **maintenu** si la holding s’engage à **réinvestir au moins 70 % du produit de cession (soit 6 300 000 €)** dans un délai de **3 ans à compter de la date de cession (février 2026 → février 2029)**.

---

### **2. Conditions strictes du réinvestissement (Art. 150-0 B ter, I, 2° a)**
Le réinvestissement doit être affecté :
- **Exclusivement au financement de moyens permanents d’exploitation** liés à une **activité éligible** (au sens du **3° du C du I de l’article 199 terdecies-0 A du CGI**).
  - **Activités éligibles** : Activités industrielles, commerciales, artisanales, agricoles, ou libérales (sous conditions).
  - **Activités exclues** :
    - **Gestion de patrimoine immobilier** (même si la holding détient des immeubles, leur gestion pure est exclue).
    - Activités financières ou de simple détention de participations (sauf si la holding exerce une activité opérationnelle éligible).

**→ Votre holding doit donc justifier d’une activité opérationnelle éligible** (ex. : animation du groupe, prestations de services facturées aux filiales, etc.). Si elle est une **holding pure (détention de participations sans activité opérationnelle)**, le réinvestissement ne sera **pas éligible** à la dérogation.

---

### **3. Solutions concrètes pour votre holding**
#### **Option 1 : Réinvestir dans des moyens permanents d’exploitation éligibles**
Si votre holding exerce une **activité éligible** (ex. : services aux filiales, conseil, R&D), vous pouvez :
- **Acquérir des immobilisations corporelles ou incorporelles** (matériel, brevets, logiciels) **affectées à cette activité**.
- **Financer des dépenses de développement** (recrutement, marketing, etc.) **liées à l’activité opérationnelle**.
- **Investir dans une nouvelle filiale opérationnelle** (création ou acquisition d’une société exerce une activité éligible).

**Exemple :**
- Achat d’un **bâtiment industriel** loué à une filiale (si la holding a une activité de **location meublée** ou **prestation de services**).
- Acquisition d’un **fonds de commerce** ou d’une **licence** pour une activité commerciale.

**⚠️ Attention :**
- Les investissements doivent être **directement liés à l’activité éligible** (pas de placement financier ou immobilier passif).
- **Preuves à conserver** : Factures, contrats, justificatifs d’affectation à l’activité.

---

#### **Option 2 : Réinvestir via une filiale opérationnelle**
Si votre holding **n’a pas d’activité éligible**, vous pouvez :
1. **Créer une filiale opérationnelle** (ex. : SASU) exercant une activité éligible (ex. : conseil, production, etc.).
2. **Injecter les 6 300 000 €** dans cette filiale sous forme :
   - **D’apport en capital** (augmentation de capital).
   - **De compte courant d’associé** (si remboursable à plus de 5 ans = moyen permanent).
3. **La filiale utilise les fonds** pour financer son activité (achat de matériel, stocks, etc.).

**Avantage :**
- La holding **respecte l’obligation de réinvestissement** via une structure éligible.
- **Risque** : L’administration fiscale pourrait contester si la filiale est considérée comme une **coquille vide** (il faut une **réelle activité économique**).

---

#### **Option 3 : Réinvestir dans des titres de sociétés opérationnelles (sous conditions)**
Si votre holding **détient déjà des filiales opérationnelles**, vous pouvez :
- **Augmenter leur capital** (pour financer leur développement).
- **Leur accorder des prêts participatifs** (si remboursables à long terme = moyen permanent).

**Condition :**
- Les filiales doivent exercer une **activité éligible** (pas de holding pure).

---

### **4. Pièges à éviter**
❌ **Placements financiers** (OPCVM, comptes à terme, etc.) → **Non éligibles**.
❌ **Achat d’immeubles en direct** (sauf si la holding a une activité de **location meublée professionnelle** ou **hôtelière**).
❌ **Réinvestissement dans une autre holding** (sauf si cette dernière a une activité éligible).
❌ **Dépassement du délai de 3 ans** (février 2026 → février 2029) → **Perte du report d’imposition**.

---

### **5. Recommandations pratiques**
1. **Vérifier l’éligibilité de l’activité de la holding** :
   - Si elle est **purement financière**, **créer une filiale opérationnelle** pour y injecter les fonds.
   - Si elle a une **activité mixte**, **isoler les dépenses éligibles**.

2. **Documenter le réinvestissement** :
   - **Engagement écrit** (délibération du conseil d’administration ou de l’associé unique) précisant :
     - Le montant réinvesti (≥ 70 % = 6 300 000 €).
     - La nature des investissements (immobilisations, financements de filiales, etc.).
     - Leur affectation à une **activité éligible**.
   - **Preuves comptables** (factures, contrats, relevés bancaires).

3. **Respecter le délai de 3 ans** :
   - **Échéance : février 2029** (date à date à partir de la cession).
   - **Conseil** : Réinvestir **dès que possible** pour éviter tout risque de retard.

4. **Anticiper un éventuel contrôle fiscal** :
   - L’administration peut demander la **justification de l’activité éligible** et du **lien entre l’investissement et cette activité**.

---

### **6. Conséquences en cas de non-respect**
Si le réinvestissement n’est **pas réalisé à 70 % dans les 3 ans** :
- **Imposition immédiate** de la plus-value latente au moment de l’apport (avec pénalités de retard si applicable).
- **Majoration de 10 %** (en cas de manquement à l’engagement de réinvestissement).

---

### **7. Prochaines étapes**
1. **Analyser l’activité actuelle de la holding** :
   - Est-elle éligible ? Si non, **créer une structure opérationnelle**.
2. **Identifier les investissements possibles** :
   - Immobilisations, financements de filiales, etc.
3. **Rédiger l’engagement de réinvestissement** (à conserver en cas de contrôle).
4. **Suivre le calendrier** :
   - **Février 2029** = date limite pour le réinvestissement.

---
**Conclusion :**
Pour **conserver le report d’imposition**, votre holding doit **réinvestir 6 300 000 € d’ici février 2029** dans des **moyens permanents liés à une activité éligible**. Si la holding n’a pas d’activité opérationnelle, la solution la plus sûre est de **créer une filiale éligible** et d’y injecter les fonds.

**Je reste à votre disposition pour :**
- Vous aider à **structurer le réinvestissement** (choix des actifs, montage juridique).
- **Rédiger l’engagement de réinvestissement** (document opposable à l’administration).
- **Vérifier l’éligibilité de l’activité** de la holding ou de ses filiales.

**Cordialement,**
[Votre Nom]
Avocat Fiscaliste
[Cabinet d’avocats]
[Coordonnées]

---

## T24

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un client vous consulte.

Sa holding, qu'il controle a 100 %, a vendu le 10 mars 2026 les
titres d'une societe d'exploitation qu'elle detenait, moins de
trois ans apres que le client les lui ait apportes. Elle a
encaisse 9 000 000 euros.

Le client veut reinvestir dans une societe qui achete des
immeubles pour les renover et les revendre.

Ce remploi permet-il de maintenir le report d'imposition ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

**CONSULTATION**

**Objet :** Éligibilité d'un remploi dans une activité d'achat-rénovation-revente d'immeubles au regard de l'article 150-0 B ter, I, 2° du CGI

**Réf. :** Cession du 10 mars 2026 – produit de 9 000 000 €

---

## 1. Rappel des faits tels que vous me les avez exposés

- Vous avez apporté à une holding que vous contrôlez à 100 % les titres d'une société d'exploitation ; la plus-value d'apport a été placée en report d'imposition de plein droit (art. 150-0 B ter CGI).
- La holding a cédé ces titres le 10 mars 2026, soit **moins de trois ans** après l'apport, pour un produit de 9 000 000 €.
- Vous envisagez de réinvestir dans une société dont l'objet est l'acquisition d'immeubles en vue de leur rénovation et de leur revente.

Ces éléments devront être confirmés par les pièces (acte d'apport et sa date exacte, acte de cession, détail du prix et de ses éventuels compléments).

---

## 2. Le cadre : l'obligation de remploi

La cession intervenant dans le délai de trois ans de l'apport, le report d'imposition **prend fin de plein droit**, sauf si la holding :

1. **prend l'engagement** de réinvestir,
2. **au moins 70 % du produit de cession**, soit ici **6 300 000 €** (le seuil se calcule sur le prix de cession, et non sur la plus-value ni sur le net d'impôt),
3. **dans un délai de trois ans** à compter de la cession, soit **au plus tard le 10 mars 2029**,
4. **dans un investissement d'une nature limitativement énumérée** par le texte.

C'est ce quatrième point qui est décisif dans votre dossier.

---

## 3. Analyse : le remploi envisagé n'est pas éligible

### 3.1. Le renvoi opéré par le texte applicable

Le a) du 2° subordonne l'éligibilité au fait que les moyens financés soient affectés à une activité **« définie au 3° du C du I de l'article 199 terdecies-0 A »**.

Ce point est capital. La rédaction usuelle du dispositif de remploi vise l'activité « commerciale au sens des articles 34 ou 35 » du CGI. L'article 35 range expressément parmi les activités commerciales celle des **marchands de biens** (achat d'immeubles en vue de la revente), de sorte que, sous cette rédaction, un remploi dans une activité d'achat-revente d'immeubles peut être admis, la seule exclusion étant la gestion par la société de son *propre* patrimoine immobilier.

**Tel n'est pas le texte qui vous est applicable.** Le renvoi au 3° du C du I de l'article 199 terdecies-0 A (dispositif « IR-PME ») emporte un périmètre sensiblement plus étroit : cette disposition, si elle vise bien les activités commerciales, industrielles, artisanales, libérales et agricoles, en **exclut expressément** les activités financières, les **activités de construction d'immeubles en vue de leur vente ou de leur location** et, plus largement, les **activités immobilières**.

L'emploi de l'adverbe *« également »* dans la seconde phrase du a) confirme cette lecture : l'exclusion de la gestion du propre patrimoine immobilier **s'ajoute** aux exclusions résultant du renvoi ; elle ne s'y substitue pas.

### 3.2. Application à votre projet

Une société qui acquiert des immeubles pour les rénover et les revendre relève :

- soit de l'**activité immobilière / de marchand de biens**, expressément exclue ;
- soit, si les travaux sont suffisamment lourds pour caractériser une construction ou une reconstruction, de l'**activité de construction d'immeubles en vue de leur vente**, tout aussi expressément exclue.

Dans les deux hypothèses, **l'activité est hors du champ du remploi éligible**.

### 3.3. Deux obstacles complémentaires

- **Nature de l'emploi.** Le a) exige le financement de « **moyens permanents d'exploitation** ». Les immeubles acquis pour être revendus constituent des **stocks**, non des immobilisations affectées durablement à l'exploitation. Même à supposer l'activité éligible, un financement de stock immobilier ne satisferait pas cette condition.
- **Les autres branches du remploi.** Le souscription ou l'acquisition de titres d'une société tierce (branches b et c du 2°, non reproduites dans l'extrait que vous me communiquez) suppose que la **société cible exerce une activité mentionnée au a)**. La condition d'activité étant appréciée par renvoi, l'exclusion se propage : investir *dans* une société de marchand de biens n'est pas davantage éligible qu'exercer soi-même cette activité. Seule la souscription de parts de fonds éligibles (FCPR, FPCI, SLP, SCR) échappe partiellement à cette logique, mais les quotas d'investissement de ces fonds sont eux-mêmes construits sur la même définition d'activité.

### 3.4. Conclusion

**Non : le remploi envisagé ne permet pas de maintenir le report d'imposition.** Un engagement de réinvestissement souscrit sur ce fondement serait remis en cause à l'occasion d'un contrôle.

*Réserve d'usage :* le raisonnement repose sur la version du 3° du C du I de l'article 199 terdecies-0 A en vigueur à la date de la cession ; je vous propose d'en faire annexer le texte exact à la note définitive, la portée de l'exclusion des « activités immobilières » étant le pivot de l'analyse.

---

## 4. Conséquences d'un remploi non conforme

Si l'engagement est pris puis non tenu (ou tenu par un investissement non éligible), la plus-value en report devient imposable **au titre de l'année d'expiration du délai de trois ans**, soit 2029, sans que l'attente ait procuré autre chose qu'un différé précaire — outre le risque de pénalités et d'intérêt de retard.

Deux points pratiques trop souvent négligés :

- L'impôt est dû par **vous, personne physique**, alors que la trésorerie est **dans la holding**. Il faudra donc appréhender les fonds (dividende ou réduction de capital), ce qui déclenche une **seconde couche d'imposition**. Le coût global doit être chiffré avant toute décision.
- La liquidation s'effectue selon le régime applicable à la date de l'apport (taux, abattements le cas échéant), majorée des prélèvements sociaux, de la CEHR et, potentiellement, de la contribution différentielle sur les hauts revenus.

---

## 5. Options envisageables

**Option 1 – Le « panachage » (recommandée si le projet immobilier vous tient à cœur).**
Seuls 70 % du produit doivent être réinvestis de manière éligible. **2 700 000 € demeurent libres d'emploi** et peuvent parfaitement être investis dans la société de marchand de biens, sans incidence sur le report. Reste à identifier un remploi éligible à hauteur de 6 300 000 € avant le 10 mars 2029.

**Option 2 – Requalifier économiquement le projet immobilier.**
Certaines activités à support immobilier ne sont pas des « activités immobilières » au sens des textes dès lors qu'elles constituent une véritable exploitation avec prestations de services (hôtellerie, para-hôtellerie, résidences services, exploitation de sites). Le curseur est délicat et l'analyse devra être menée activité par activité, sur la base d'un business plan. Ce n'est en tout état de cause **pas** le cas d'une opération d'achat-rénovation-revente.

**Option 3 – Le remploi via fonds.**
Souscription de parts de FPCI/FCPR/SLP éligibles. Attention : délais de libération des souscriptions et **obligation de conservation de cinq ans**, qui immobilise durablement les fonds.

**Option 4 – Renoncer au report et purger l'impôt.**
Solution parfois rationnelle : elle libère 100 % de la trésorerie de toute contrainte et supprime le risque de contrôle sur le remploi. Elle suppose un chiffrage précis (montant de la plus-value en report, régime applicable, coût de la remontée des fonds). Si vous retenez cette voie, la plus-value doit être déclarée au titre des revenus 2026, en 2027.

---

## 6. Points de vigilance

- **Assiette des 70 %** : le produit de cession s'entend du prix stipulé, y compris les sommes séquestrées ; les compléments de prix éventuels suivent leur propre régime de remploi.
- **Formalisme** : l'engagement de réinvestissement doit être matérialisé et l'état de suivi du report annexé à vos déclarations annuelles. Un défaut purement déclaratif est sanctionné.
- **Conservation** : les biens ou titres acquis en remploi doivent être conservés (douze mois au minimum pour les titres, cinq ans pour les fonds). Un débouclage anticipé fait tomber le report rétroactivement.
- **Abus de droit** : toute construction visant à faire passer pour opérationnelle une activité en réalité immobilière (interposition d'une société opérationnelle de façade, contrat de prestations artificiel) exposerait à l'article L. 64 ou L. 64 A du LPF, avec majoration de 80 %. Je vous le déconseille formellement.
- **Calendrier** : trois ans passent vite pour déployer 6,3 M€ sur des cibles éligibles. Le sourcing doit commencer immédiatement.

---

## 7. Diligences que je vous propose

1. Communication de l'acte d'apport, de l'acte de cession et des déclarations 2074-I déjà déposées.
2. Chiffrage comparatif à 24/48 mois des options 1 et 4 (coût fiscal global, trésorerie disponible).
3. Note de sécurisation sur le ou les remplois éligibles finalement retenus, avant tout engagement contractuel.
4. Le cas échéant, examen de l'opportunité d'un rescrit sur la nature de l'activité de la cible envisagée.

Je reste à votre disposition pour en discuter. Tant qu'une cible éligible n'est pas identifiée, je vous invite à **ne prendre aucun engagement d'investissement** sur le projet de marchand de biens au-delà de l'enveloppe libre de 2,7 M€.

---

## T25

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

**MÉMORANDUM FISCAL**

**À l'attention de la Direction Financière / Direction Fiscale**
**Date :** 24 mai 2024 *(Date de la consultation)*
**Objet :** Retenue à la source sur distribution de dividendes à votre société mère luxembourgeoise (Mise en paiement prévue le 15 juin 2025).

Madame, Monsieur,

Vous m'avez consulté concernant le traitement fiscal d'une distribution de dividendes d'un montant de 20 000 000 d'euros que votre société (résidente fiscale française) envisage de verser le 15 juin 2025 à sa société mère, résidente fiscale au Luxembourg. 

Voici mon analyse de la situation au regard de la législation fiscale applicable.

### 1. Conclusion exécutive

**Sous réserve de la confirmation de la substance économique de votre société mère (clause anti-abus), aucune retenue à la source ne sera due en France sur cette distribution.** 

Bien que l'article que vous citez pose le principe d'une imposition, votre situation permet de bénéficier d'une exonération totale en vertu du régime européen "Mère-Fille" transposé en droit interne français.

### 2. Analyse détaillée

**A. Le principe : l'application d'une retenue à la source**
Vous avez très justement identifié l'article 119 bis, 2 du Code Général des Impôts (CGI). Ce texte pose le principe selon lequel les revenus distribués par une société française à un bénéficiaire dont le siège est hors de France sont soumis à une retenue à la source (dont le taux de droit commun pour les personnes morales est aujourd'hui aligné sur le taux de l'IS, soit 25 %).

**B. L'exception applicable à votre situation : l'exonération (Article 119 ter du CGI)**
En tant qu'avocat, mon rôle est d'articuler ce principe avec les régimes d'exonération existants. La France a transposé la Directive européenne "Mère-Fille" à l'article 119 ter du CGI. Cet article prévoit une **exonération totale** de retenue à la source si plusieurs conditions cumulatives sont remplies. 

Au regard des éléments que vous m'avez communiqués, nous validons l'ensemble de ces critères objectifs :
1. **Localisation :** La société mère a son siège de direction effective dans un État membre de l'UE (Luxembourg).
2. **Forme juridique :** Elle revêt la forme d'une Société Anonyme (SA), forme expressément visée par l'annexe de la directive européenne.
3. **Assujettissement à l'impôt :** Elle est soumise à l'impôt sur les sociétés luxembourgeois, sans possibilité d'option et sans en être exonérée.
4. **Seuil de participation :** Elle détient 100 % de votre capital (le minimum légal requis est de 5 % ou 10 % selon les cas).
5. **Durée de détention :** Elle détient ces titres depuis 5 ans (le minimum légal requis est de 2 ans).

**C. Les points de vigilance (Clause anti-abus et Bénéficiaire effectif)**
Pour que cette exonération s'applique de plein droit, je dois attirer votre attention sur deux conditions subjectives fondamentales que l'administration fiscale française vérifie systématiquement lors de distributions de montants importants (20 M€) :

*   **Le bénéficiaire effectif :** La société luxembourgeoise doit avoir la libre disposition de ces 20 millions d'euros. Elle ne doit pas agir comme un simple agent ou relais obligé de reverser immédiatement ce dividende à une autre entité (par exemple, hors de l'UE).
*   **La clause anti-abus (Art. 119 ter, 3 du CGI) :** Le montage ne doit pas être artificiel et mis en place dans le but principal d'éluder l'impôt. Concrètement, cela signifie que votre société mère luxembourgeoise doit avoir une **substance économique réelle** : des locaux, des dirigeants qui prennent des décisions au Luxembourg, éventuellement des salariés, et une véritable activité de holding (gestion de participations). Si la société luxembourgeoise est une simple "boîte aux lettres", l'administration fiscale française pourrait refuser l'exonération.

### 3. Recommandations pratiques et formalités

Pour appliquer cette exonération à la source le 15 juin 2025, vous devrez :
1. **Obtenir une attestation** de votre société mère luxembourgeoise certifiant qu'elle remplit bien les conditions de l'article 119 ter du CGI (notamment son assujettissement à l'IS luxembourgeois et sa qualité de bénéficiaire effectif).
2. **Déclarer cette distribution** sur le formulaire n°2777 (Déclaration des revenus de capitaux mobiliers) le mois suivant la mise en paiement (soit avant le 15 juillet 2025), en indiquant le montant distribué dans la case prévue pour les distributions exonérées (régime mère-fille européen).

Je me tiens à votre entière disposition pour auditer la "substance" de votre société mère luxembourgeoise afin de sécuriser définitivement cette opération, ou pour vous assister dans la rédaction de l'attestation fiscale requise.

Restant à votre disposition, je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

**[Votre Signature]**
Avocat au Barreau
Département Droit Fiscal

---

## T26

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

**Réponse :**

Monsieur,

Vous envisagez de céder les titres d’une société civile immobilière (SCI) dont l’actif est composé à 80 % d’immeubles situés en France, pour un prix de 4 000 000 €. L’acte de cession sera signé le 20 mars 2024. Vous m’interrogez sur le droit d’enregistrement applicable et sur le contenu obligatoire de l’acte.

### 1. Qualification et droit d’enregistrement

La SCI dont vous cédez les parts est une personne morale à prépondérance immobilière au sens de l’article 726, I, 2° du CGI, dès lors que son actif est principalement constitué d’immeubles ou de droits immobiliers situés en France (80 % > 50 %).

La cession de participations dans une telle société est soumise au droit d’enregistrement au taux fixe de **5 %**, en application de ce même texte.

**Assiette du droit :** le prix de cession stipulé dans l’acte, augmenté, le cas échéant, des charges ou indemnités prévues au profit du cédant, ainsi que des dettes prises en charge par le cessionnaire (si celui-ci s’engage à les acquitter).

**Calcul :**
- Prix de cession : 4 000 000 €
- Droit d’enregistrement dû : 4 000 000 € × 5 % = **200 000 €**

Ce droit est en principe à la charge de l’acquéreur, sauf convention contraire entre les parties. Il doit être payé lors de l’enregistrement de l’acte, dans le délai d’un mois à compter de sa date (article 635, 2° quinquies du CGI pour les cessions de participations dans des sociétés à prépondérance immobilière).

### 2. Mentions obligatoires dans l’acte

Conformément à l’article 726, III-B du CGI, l’acte de cession doit indiquer **expressément** les trois informations suivantes :

1. **Si la société est une société mentionnée à l’article 1655 ter du CGI** (société immobilière de jouissance ou de construction-attribution).  
   → En pratique, il s’agit de sociétés qui attribuent aux associés un droit de jouissance sur un immeuble ou une fraction d’immeuble. Si ce n’est pas le cas, la mention « non » doit être portée.

2. **Si les participations cédées confèrent au cessionnaire, directement ou indirectement, le droit à la jouissance d’immeubles ou de fractions d’immeubles au sens de l’article 728 du CGI.**  
   → Cette mention est essentielle car, si un tel droit de jouissance existe, la cession pourrait être soumise non pas au droit de 5 % mais au régime fiscal des mutations d’immeubles (taux plus élevé, actuellement 5,80665 %). Une réponse négative doit être clairement indiquée si la SCI ne relève pas de ce régime.

3. **Si le cessionnaire a acquitté ou s’engage à acquitter, directement ou indirectement, des dettes contractées auprès du cédant par la personne morale (par exemple, un compte courant d’associé) et, le cas échéant, le montant de ces dettes.**  
   → Cette précision permet à l’administration de s’assurer que la prise en charge de telles dettes est bien incluse dans l’assiette du droit d’enregistrement, comme un supplément de prix.

L’omission de l’une de ces mentions rend l’acte incomplet et expose les parties à des sanctions fiscales (amende prévue à l’article 1768 du CGI, par exemple). Il est donc impératif de les faire figurer dans l’acte, même par une simple déclaration négative.

### 3. Conséquences pratiques

- **Enregistrement** : l’acte de cession devra être présenté à la formalité de l’enregistrement dans le mois suivant sa signature (au plus tard le 20 avril 2024) auprès du service des impôts des entreprises (SIE) compétent.
- **Paiement du droit** : le droit de 200 000 € sera acquitté lors de cette formalité.
- **Recommandation** : il est conseillé de faire établir l’acte par un notaire ou, à tout le moins, de le faire enregistrer afin de lui donner date certaine et d’assurer sa pleine opposabilité aux tiers (notamment à l’égard de la société dont les parts sont cédées).

Je reste à votre disposition pour toute précision ou pour la rédaction de l’acte.

Bien à vous,

[Votre nom]  
Avocat fiscaliste

---

## T27

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

Bonjour, je vous remercie de me consulter sur cette affaire. Pour déterminer si le taux de 5,5 % était applicable aux travaux réalisés par votre entreprise, il convient d'analyser les conditions prévues par l'article 278-0 bis A, I du Code Général des Impôts (CGI) en vigueur à la date des travaux, soit le 20 janvier 2025.

Selon les informations que vous m'avez fournies, les travaux consistaient en l'installation d'une chaudière dans une maison âgée de quinze ans, occupée par son propriétaire, pour un montant de 8 500 euros hors taxes. Votre entreprise a facturé ces travaux au taux réduit de 5,5 %.

Pour bénéficier du taux réduit de TVA, les prestations doivent remplir trois conditions cumulatives prévues par l'article 278-0 bis A, I du CGI :

1. **Être effectuées dans des locaux achevés depuis au moins deux ans** : La maison où les travaux ont été réalisés a quinze ans, ce qui satisfait largement à cette condition.

2. **Être destinées à des locaux affectés ou destinés à être affectés à un usage d'habitation** : La maison est occupée par son propriétaire, ce qui signifie qu'elle est affectée à un usage d'habitation. Cette condition est donc remplie.

3. **Porter sur la pose, l'installation, l'adaptation ou l'entretien de matériaux, d'équipements, d'appareils ou de systèmes ayant pour objet d'économiser l'énergie ou de recourir à de l'énergie produite à partir de sources renouvelables** : L'installation d'une chaudière peut potentiellement relever de cette catégorie si elle contribue à économiser l'énergie ou à utiliser des sources d'énergie renouvelables.

Cependant, pour confirmer que le taux réduit est applicable, il faudrait vérifier si la chaudière installée répond aux critères spécifiques d'amélioration de l'isolation thermique, du chauffage et de la ventilation, ou de la production d'eau chaude sanitaire, et si elle est considérée comme un équipement permettant d'économiser l'énergie ou de recourir à de l'énergie produite à partir de sources renouvelables.

Il est crucial d'examiner les caractéristiques techniques de la chaudière installée. S'il s'agit d'une chaudière à haute performance énergétique ou utilisant des sources d'énergie renouvelables (comme une chaudière à biomasse, par exemple), il est probable que les travaux remplissent les conditions pour bénéficier du taux réduit de TVA.

En revanche, si la chaudière est une chaudière standard sans caractéristiques particulières en matière d'économie d'énergie ou d'utilisation d'énergies renouvelables, le taux réduit pourrait ne pas être justifié.

Je recommande de rassembler les documents techniques relatifs à la chaudière installée, tels que les spécifications du fabricant, les notices d'installation, et tout autre document pouvant attester de ses caractéristiques énergétiques. Ces éléments seront essentiels pour justifier l'application du taux réduit de 5,5 % et pour défendre votre position face à la proposition de rectification de l'administration fiscale.

Il conviendra ensuite de préparer une réponse détaillée à l'administration fiscale, en argumentant sur la base des textes applicables et des éléments de fait relatifs aux travaux réalisés. Si nécessaire, nous pourrons également envisager de solliciter un entretien avec les services fiscaux pour discuter des éléments techniques et juridiques qui soutiennent votre position.

Je reste à votre disposition pour discuter plus en détail de cette affaire et pour vous accompagner dans vos échanges avec l'administration fiscale.

---

## T28

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

## T29

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

**Analyse juridique et fiscale – Applicabilité de l’exonération partielle de l’article 787 B du CGI**

**Objet de la consultation** :
Votre client, dirigeant d’une SAS détenant 40 appartements meublés (valeur des titres : 20 M€), souhaite donner en pleine propriété la totalité de ses titres à ses deux enfants à parts égales, sous engagement collectif de conservation (Dutreil) en cours depuis le 3 mars 2021. La donation serait signée le 25 octobre 2023, avec maintien de la présidence du donateur pendant 3 ans.

**Question** : L’exonération partielle de 75 % prévue par l’article 787 B du CGI est-elle applicable ?

---

### **I. Conditions générales de l’article 787 B du CGI**
L’exonération partielle de 75 % s’applique aux transmissions de parts ou actions de sociétés exerçant une **activité industrielle, commerciale, artisanale, agricole ou libérale** (CGI, art. 787 B, al. 1). Sont expressément exclues les activités de **gestion de son propre patrimoine mobilier ou immobilier** (al. 2).

#### **1. Activité éligible ?**
Votre société détient 40 appartements meublés. La qualification de l’activité est cruciale :
- **Gestion de patrimoine immobilier** : Par principe, la location meublée est une activité civile (CGI, art. 35, I-5°), sauf si elle relève d’une **activité commerciale** au sens de l’article 34 du CGI (ex. : location meublée avec prestations para-hôtelières).
- **Jurisprudence et doctrine** :
  - La location meublée **sans prestations** est considérée comme une gestion de patrimoine (exclue de l’exonération).
  - La location meublée **avec prestations** (petit-déjeuner, ménage, réception) peut être qualifiée d’activité commerciale (éligible).
  - **Critère** : La société doit fournir des **prestations significatives** (ex. : services hôteliers) pour être considérée comme commerciale (CE, 24 juin 2020, n° 428506 ; BOI-ENR-DMTG-10-20-40-10, § 100).

**Recommandation** :
- **Vérifier les prestations** : Si la société fournit des services (ménage, petit-déjeuner, réception), l’activité peut être commerciale.
- **Preuves** : Contrats de location, factures, descriptif des services, comptabilité (compte 706 "Prestations de services").
- **Risque** : À défaut, l’administration fiscale pourrait requalifier l’activité en gestion de patrimoine (exclusion de l’exonération).

#### **2. Engagement Dutreil (CGI, art. 787 B, al. 4 et suivants)**
Les conditions sont a priori remplies :
- **Engagement collectif** : Signé le 3 mars 2021 (en cours à la date de la donation).
- **Engagement individuel** : Pris par chaque enfant.
- **Conservation des titres** : Les enfants devront conserver les titres pendant 4 ans à compter de la donation (soit jusqu’au 25 octobre 2027).
- **Fonction de direction** : Le donateur conserve la présidence pendant 3 ans (condition remplie).

**Attention** :
- L’engagement collectif doit porter sur **au moins 34 % des droits** (si la société n’est pas cotée). Ici, il porte sur la totalité des titres (condition remplie).
- La société doit conserver son activité éligible pendant toute la durée des engagements.

---

### **II. Points de vigilance et risques**
#### **1. Activité réelle de la société**
- **Contrôle de l’administration** : L’administration fiscale peut contester la qualification commerciale de l’activité si les prestations sont insuffisantes.
- **Solution** : Documenter les prestations (ex. : contrats, factures, témoignages) pour prouver le caractère commercial.

#### **2. Durée des engagements**
- **Engagement collectif** : Doit être en cours à la date de la donation (ici, signé en 2021, donc valide).
- **Engagement individuel** : Les enfants doivent conserver les titres pendant 4 ans (jusqu’en 2027).
- **Fonction de direction** : Le donateur doit exercer une fonction de direction pendant 3 ans (jusqu’en 2026).

#### **3. Valeur des titres**
- L’exonération s’applique sur **75 % de la valeur des titres** (soit 15 M€ exonérés, 5 M€ taxables).
- **Droits de donation** : Calculés sur 5 M€ (après abattement de 100 000 € par enfant, soit 200 000 € au total).
  - Barème progressif (2023) : Taux marginal de 45 % pour la tranche > 1,805 M€.
  - **Montant estimé** : Environ 2,1 M€ de droits (à affiner selon la situation familiale).

---

### **III. Recommandations**
1. **Qualification de l’activité** :
   - Vérifier que la location meublée s’accompagne de **prestations significatives** (ex. : services hôteliers).
   - Conserver les preuves (contrats, factures, comptabilité).

2. **Engagements Dutreil** :
   - Respecter la durée de conservation des titres (4 ans pour les enfants, 3 ans pour la direction).
   - Ne pas céder les titres avant l’échéance.

3. **Optimisation fiscale** :
   - Si l’activité est requalifiée en gestion de patrimoine, l’exonération ne s’appliquera pas. Envisager :
     - Une **transformation de l’activité** (ex. : création d’une filiale hôtelière).
     - Une **donation en nue-propriété** (pour réduire la base taxable).

4. **Démarches** :
   - Déclarer la donation sur le formulaire **2735** (avec mention de l’engagement Dutreil).
   - Joindre les preuves de l’activité commerciale.

---

### **IV. Conclusion**
**L’exonération partielle de 75 % est applicable sous réserve** :
✅ Que l’activité de location meublée soit **qualifiée de commerciale** (prestations significatives).
✅ Que les engagements Dutreil soient respectés (conservation des titres, fonction de direction).

**Risque** : Si l’activité est requalifiée en gestion de patrimoine, l’exonération sera refusée (droits de donation sur 20 M€).

**Prochaines étapes** :
1. Auditer les prestations de la société pour confirmer le caractère commercial.
2. Préparer les preuves (contrats, comptabilité).
3. Signer la donation avant le 25 octobre 2023 en respectant les engagements.

Je reste à votre disposition pour approfondir l’analyse ou assister à la rédaction des actes.

**Me [Votre Nom]**
Avocat fiscaliste
[Coordonnées]

---

## T30

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

**NOTE DE CONSULTATION FISCALITÉ PATRIMONIALE**
**Objet :** Applicabilité de l’exonération partielle de l’article 787 B du CGI à une donation de titres de SAS détenant 40 appartements meublés
**Date de la consultation :** [Date du jour]
**Destinataires :** Monsieur [Nom], Président de la SAS [Nom] ; Maître [Nom], Notaire

---

### I. RAPPEL DES FAITS ET QUESTION POSÉE

Vous envisagez de consentir, le 25 octobre 2023, une donation entre vifs à vos deux enfants, à parts égales et en pleine propriété, de la totalité des titres de votre SAS, d’une valeur de 20 000 000 €. La société détient un patrimoine immobilier composé de 40 appartements meublés.

Un engagement collectif de conservation a été souscrit le 3 mars 2021, portant sur 100 % des droits sociaux, et est toujours en cours. Vos enfants s’engageront individuellement à conserver les titres. Vous conservez la présidence de la SAS pendant trois ans suivant la donation.

**Question :** L’exonération partielle de droits de mutation à titre gratuit prévue à l’article 787 B du CGI est-elle applicable à cette opération ?

---

### II. CADRE JURIDIQUE ET CONDITIONS D’APPLICATION DE L’ARTICLE 787 B DU CGI

L’article 787 B du CGI prévoit une exonération de 75 % de la valeur des parts ou actions transmises à titre gratuit, sous réserve du respect cumulatif des conditions suivantes :

1. **Condition d’activité éligible** : L’activité principale de la société doit être industrielle, commerciale, artisanale, agricole ou libérale. Le texte exclut expressément *« l’exercice par une société d’une activité de gestion de son propre patrimoine mobilier ou immobilier »*.
2. **Engagement collectif de conservation** : Souscrit avant la transmission, portant sur au moins 34 % des droits financiers et 20 % des droits de vote, et maintenu pendant 6 ans. Pour une donation, l’engagement doit être en cours depuis **au moins 2 ans** à la date de l’acte.
3. **Engagement individuel des donataires** : Souscrit par chaque bénéficiaire pour une durée minimale de 4 ans.
4. **Fonction dirigeante du donateur** : Le transmetteur doit avoir exercé une fonction de direction (président, directeur général, gérant, etc.) pendant la durée de l’engagement collectif et la conserver pendant **3 ans** suivant la transmission.

---

### III. ANALYSE APPLIQUÉE AU CAS D’ESPÈCE

#### A. Condition d’activité éligible : point bloquant
La société détient 40 appartements meublés. Sauf éléments contraires non communiqués, cette activité relève de la **location meublée** (régime des BIC pour l’impôt sur le revenu). 

Or, la doctrine administrative (BOI-ENR-DMTG-10-20-20-20, § 40) et la jurisprudence constante du Conseil d’État (CE 9 déc. 2015, n° 373888 ; CE 27 juill. 2018, n° 408388) précisent que :
- La simple mise à disposition de logements meublés, même soumise au régime des BIC, est qualifiée de **gestion de patrimoine immobilier** et **n’ouvre pas droit** à l’exonération de l’article 787 B.
- Seule une activité à caractère **hôtelier ou para-hôtelier**, impliquant la fourniture de prestations de services substantielles, organisées et commercialisées (accueil, nettoyage régulier, conciergerie, restauration, gestion centralisée des réservations, etc.), peut être requalifiée en activité commerciale éligible.

En l’état des éléments fournis, l’activité de la SAS ne remplit pas la condition d’activité éligible. **L’exonération de 75 % est donc inapplicable.**

#### B. Conditions formelles et de conservation
- **Engagement collectif** : Signé le 3 mars 2021. Au 25 octobre 2023, il est en cours depuis 2 ans et 7 mois → condition des 2 ans préalables à la donation **remplie**.
- **Engagement individuel** : Prévu par les enfants → condition **remplie** sous réserve de rédaction conforme.
- **Fonction dirigeante** : Conservation de la présidence pendant 3 ans post-donation → condition **remplie**.

Ces conditions sont satisfaites, mais elles ne peuvent suppléer l’absence d’activité éligible.

---

### IV. CONSÉQUENCES FISCALES ET RECOMMANDATIONS

#### 1. En l’état
La donation sera soumise aux droits de mutation à titre gratuit sur la valeur intégrale des titres (20 000 000 €), après application de l’abattement de 100 000 € par enfant. Le barème progressif s’appliquera sur la base taxable, générant un coût fiscal significatif.

#### 2. Vérifications préalables indispensables
Avant de signer l’acte, il convient de documenter précisément la nature de l’activité :
- Contrats de location (baux meublés, réservations, plateformes)
- Prestations effectivement fournies aux occupants
- Organisation commerciale, moyens humains et logistiques dédiés
- Qualification comptable et fiscale (BIC industriel/commercial vs gestion de patrimoine)

Si l’activité présente un caractère para-hôtelier avéré, une **requalification** pourrait être défendue, mais elle reste soumise à l’appréciation de l’administration et à un risque contentieux.

#### 3. Sécurisation possible
- **Rescrit fiscal** (BOI-RES-GEN-000010) : Demande à l’administration de se prononcer sur l’éligibilité de l’activité au regard de l’article 787 B. Délai de réponse : 3 mois. Silence = accord tacite.
- **Restructuration préalable** : Si l’activité le permet, transformation en résidence de services ou création d’une holding animatrice avec filiales opérationnelles (sous réserve de substance économique et de délais de conservation).
- **Alternatives patrimoniales** : Donation avec démembrement, donation-partage avec soulte, utilisation de l’assurance-vie (limitée pour les titres sociaux), ou report de la transmission dans le cadre d’une cession à titre onéreux avec pacte Dutreil (article 787 B bis) si un repreneur externe est identifié.

---

### V. CONCLUSION

**L’exonération partielle de l’article 787 B du CGI n’est pas applicable en l’état**, la détention et la location de 40 appartements meublés étant qualifiées de gestion de patrimoine immobilier, expressément exclue du champ de l’exonération. Les autres conditions (engagements, fonction dirigeante, délai de 2 ans) sont remplies, mais ne peuvent pallier l’absence d’activité éligible.

Je vous recommande de :
1. Faire auditer la réalité de l’activité (prestations, organisation, qualification comptable) ;
2. Solliciter un rescrit fiscal si des éléments permettent de défendre un caractère commercial substantiel ;
3. Évaluer avec votre notaire et votre conseil fiscal les alternatives de transmission les plus adaptées à votre situation patrimoniale et familiale.

Je reste à votre disposition pour examiner les documents de la société, rédiger la demande de rescrit ou étudier les scénarios alternatifs.

*Note : Cette analyse est fondée sur les éléments communiqués et sur la législation applicable à la date de la donation envisagée. Elle ne préjuge pas de la position de l’administration fiscale, qui conserve son pouvoir d’appréciation et de contrôle. Une étude complète des statuts, bilans, contrats et organisation de la société est nécessaire avant toute signature.*

**[Signature]**  
Avocat au Barreau de [Ville]  
Spécialiste en droit fiscal et patrimoine

---

## T31

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

**NOTE DE CONSULTATION**

**Objet : Distribution de 20 000 000 € à la société mère luxembourgeoise — mise en paiement le 15 juin 2025 — existence d'une retenue à la source**

---

**En synthèse**

Non, aucune retenue à la source ne devrait être due. Le principe de droit interne (retenue de 25 %) est neutralisé par l'exonération « mère-fille » de l'article 119 ter du CGI, dont les conditions paraissent remplies au vu des faits communiqués. Cette exonération reste subordonnée à la qualité de bénéficiaire effectif de la société mère, à l'absence de montage non authentique, et à l'accomplissement de formalités préalables au paiement.

---

**I. Le principe : une retenue à la source de 25 %**

Les dividendes versés à un bénéficiaire effectif n'ayant pas son siège en France supportent en principe la retenue de l'article 119 bis, 2 du CGI, au taux prévu par l'article 187, 2, aligné sur le taux normal de l'IS, soit **25 %** en 2025 pour une personne morale.

La société distributrice française est le redevable légal : si une retenue était due, elle devrait être versée au Trésor au plus tard le 15 du mois suivant la mise en paiement (relevé n° 2777-SD), soit ici le 15 juillet 2025. Le taux majoré de 75 % (États ou territoires non coopératifs) n'est pas en cause : le Luxembourg n'est pas un ETNC.

**II. L'exonération du régime mère-fille (CGI, art. 119 ter ; directive 2011/96/UE)**

| Condition | Faits | Remplie |
|---|---|---|
| Filiale passible de l'IS dans les conditions de droit commun, siège en France | Société française | ✓ |
| Siège de direction effective de la mère dans l'UE | Luxembourg | ✓ |
| Forme visée à l'annexe I de la directive | SA luxembourgeoise | ✓ |
| Soumission à l'impôt sur les sociétés local (IRC) sans option ni exonération | Soumise à l'IS luxembourgeois | ✓ |
| Détention directe ≥ 10 % conservée ≥ 2 ans | 100 % depuis 5 ans | ✓ |
| Qualité de bénéficiaire effectif | À documenter | À vérifier |

Deux précisions utiles :
- le fait que les dividendes soient **exonérés au Luxembourg** au titre de son propre régime mère-fille est sans incidence : la condition porte sur la soumission de la société à l'IRC, non sur l'imposition effective des produits ;
- la détention de 5 ans dispense de souscrire un engagement de conservation de deux ans.

**III. Points de vigilance**

1. **Clause anti-abus** (art. 119 ter, dernier alinéa, issu de la LF pour 2019) : l'exonération est écartée pour les montages non authentiques mis en place pour obtenir, à titre principal ou comme l'un des objectifs principaux, l'avantage fiscal (voir aussi CJUE, 26 fév. 2019, « affaires danoises », C-116/16 et C-117/16 ; C-6/16, *Eqiom*). Il convient de documenter la **substance** de la société mère (locaux, salariés, organes de direction effectifs, pouvoir d'utilisation des dividendes) et l'absence d'obligation de rétrocession vers un État tiers. La charge de la preuve de l'abus pèse sur l'administration, mais le dossier doit être constitué par précaution.
2. **Qualification de la distribution** : l'exonération vise les distributions de bénéfices. Le produit de cession de l'actif constituant un bénéfice distribuable, la distribution décidée par l'assemblée générale entre dans le champ. Un remboursement d'apports ou de primes relèverait d'un régime distinct.
3. La contribution additionnelle de 3 % sur les distributions est abrogée depuis 2017 : sans objet.

**IV. Formalités impératives avant le 15 juin 2025**

- Recueillir auprès de la société mère, **avant la mise en paiement**, une attestation certifiant qu'elle remplit les conditions de l'article 119 ter (contenu précisé au BOI-RPPM-RCM-30-30-20-40 : identité, forme, siège de direction effective, numéro fiscal, taux et durée de détention, soumission à l'IRC, qualité de bénéficiaire effectif). La distributrice la conserve pour la produire à toute demande de l'administration.
- Souscrire l'imprimé fiscal unique (IFU n° 2561) mentionnant la distribution et son bénéficiaire.
- À défaut d'attestation au jour du paiement : retenue de 25 % à verser, puis demande de remboursement par la société mère, au plus tard le 31 décembre de la deuxième année suivant celle du paiement.

**V. Solution de repli conventionnelle**

Si l'exonération de droit interne venait à être contestée, la convention franco-luxembourgeoise du 20 mars 2018 (en vigueur depuis le 1er janvier 2020) plafonne l'impôt à la source à **5 %** lorsque le bénéficiaire effectif est une société détenant directement au moins 10 % du capital (art. 10), sous réserve de la clause de finalité principale issue de l'instrument multilatéral. L'exonération interne, plus favorable, s'applique en priorité.

---

**Recommandations**

1. Confirmer le statut fiscal luxembourgeois de la mère (avis d'imposition à l'IRC, extrait RCSL, statuts — écarter tout statut exonéré type SPF ou organisme de placement) ;
2. Documenter la substance et la qualité de bénéficiaire effectif ;
3. Faire signer l'attestation 119 ter avant le 15 juin 2025 ;
4. Faire approuver régulièrement la distribution par l'assemblée générale ;
5. Souscrire l'IFU.

Je me tiens à votre disposition pour préparer l'attestation et sécuriser le dossier en prévision d'un éventuel contrôle.

---

## T32

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un client vous consulte.

Sa holding, qu'il controle a 100 %, a vendu le 10 mars 2026 les
titres d'une societe d'exploitation qu'elle detenait, moins de
trois ans apres que le client les lui ait apportes. Elle a
encaisse 9 000 000 euros.

Le client veut reinvestir dans une societe qui achete des
immeubles pour les renover et les revendre.

Ce remploi permet-il de maintenir le report d'imposition ?

Voici le texte applicable a la date de la cession.
```

**Reponse a coder, en entier :**

**CONSULTATION**

**Objet :** Cession par une société holding de titres apportés depuis moins de trois ans – conditions du remploi de l'article 150-0 B ter, I, 2° du CGI – éligibilité d'un réinvestissement dans une activité d'achat-rénovation-revente d'immeubles

---

## 1. Rappel des données

- Votre holding, que vous contrôlez à 100 %, a reçu par apport les titres d'une société d'exploitation. La plus-value d'apport est placée en **report d'imposition** de plein droit (art. 150-0 B ter) **à votre nom personnel**.
- Elle a cédé ces titres le **10 mars 2026**, soit **moins de trois ans après l'apport**.
- Prix encaissé : **9 000 000 €**.
- Projet de remploi : prise de participation / souscription dans une société qui **achète des immeubles, les rénove et les revend** (activité de marchand de biens au sens de l'article 35, I, 1° du CGI).

**Précision liminaire :** votre question porte sur le seul a) du 2° du I, qui est le texte que vous m'avez communiqué. La réponse suppose toutefois d'examiner l'ensemble des voies de remploi (a, b, c et d), dont les conditions d'activité ne sont **pas identiques**. Je raisonne ci-après sur l'article dans sa rédaction applicable à la cession ; la rédaction exacte en vigueur au 10 mars 2026 devra être vérifiée avant toute décision, l'article ayant été modifié à plusieurs reprises.

---

## 2. Le cadre du remploi : les paramètres à respecter

Puisque la cession intervient dans les trois ans de l'apport, le report ne survit **que** si la holding :

| Paramètre | Valeur dans votre dossier |
|---|---|
| Engagement de réinvestir | à prendre par la société cédante, formalisé et repris dans les obligations déclaratives (état de suivi annexé à votre 2042 / 2074-I) |
| Quotum | **70 % du produit de cession**, soit **6 300 000 €** — le produit s'entend du **prix brut encaissé**, et non du prix net d'impôt ou de la plus-value dégagée par la holding |
| Délai | **3 ans de date à date**, soit au plus tard le **10 mars 2029** |
| Nature du remploi | limitativement énumérée aux a) à d) du 2° |
| Conservation | 12 mois pour les biens ou titres acquis/souscrits (a, b, c) ; 5 ans pour les parts de fonds (d) |
| Fraction libre | **2 700 000 €** (30 %), affectables sans contrainte |

**Sanction du non-respect :** expiration du report et imposition, **à votre niveau personnel**, de la plus-value d'apport (PFU 12,8 % + 17,2 % de prélèvements sociaux, soit 30 %, majoré de la CEHR à 3 ou 4 %), avec application de l'intérêt de retard de l'article 1727 décompté depuis l'apport. Compte tenu du montant en jeu, l'enjeu se chiffre vraisemblablement en millions d'euros : le sujet ne souffre aucune approximation.

---

## 3. L'activité d'achat-rénovation-revente est-elle éligible au titre du a) ?

**Ma réponse est négative, et le risque est élevé.**

Le a) comporte **deux filtres cumulatifs**, et c'est le premier qui est décisif :

**a) Premier filtre — le renvoi au 3° du C du I de l'article 199 terdecies-0 A.** Depuis la modification opérée par la loi de finances pour 2019, le a) ne se réfère plus à une définition autonome de l'activité éligible (« activité commerciale, industrielle, artisanale, libérale, agricole ou financière »), mais **importe la liste d'exclusions du dispositif IR-PME**. Or ce texte, s'il vise bien l'activité commerciale au sens des articles 34 **et 35** du CGI, en **exclut expressément les activités immobilières** (construction d'immeubles en vue de leur vente ou de leur location, promotion et location immobilières). L'administration, dans sa doctrine relative à l'IR-PME comme au remploi de l'article 150-0 B ter, retient une lecture large de cette exclusion et y range **l'activité de marchand de biens**, de lotisseur et de promoteur.

C'est précisément le piège de ce dossier : sous l'empire de la rédaction antérieure à 2019, un remploi dans une société de marchand de biens était **éligible**, l'exclusion ne visant que la gestion par la holding de *son propre* patrimoine. De nombreux schémas ont été validés sur cette base et la littérature en circulation est encore largement obsolète. Le renvoi au 199 terdecies-0 A a fermé cette porte.

**b) Second filtre — l'exclusion de la gestion du propre patrimoine immobilier.** Sur ce terrain seul, votre projet serait défendable : des immeubles acquis en vue de la revente constituent un **stock**, non un patrimoine géré, et la jurisprudence distingue traditionnellement le marchand de biens du gestionnaire de patrimoine. Mais cet argument est inopérant, car le premier filtre suffit à écarter l'opération.

**c) Aggravation possible.** Si les « rénovations » envisagées sont lourdes au point de s'analyser en une reconstruction, l'opération relève de la **promotion immobilière**, exclusion la plus explicite du texte. Le contenu technique des travaux projetés doit être documenté.

**Conclusion sur le a) :** le financement, par la holding elle-même, de moyens d'exploitation affectés à une activité d'achat-rénovation-revente d'immeubles **ne permet pas** de maintenir le report.

---

## 4. Les autres voies de remploi

**Voie b) — acquisition du contrôle d'une société existante.** Le b) exige que la société acquise exerce « une activité mentionnée au a », « sous la même exception ». **Même exclusion, même conclusion : non éligible.** Racheter une société de marchand de biens déjà constituée est donc à proscrire.

**Voie c) — souscription en numéraire au capital initial ou à une augmentation de capital.** C'est ici que subsiste une **ouverture, réelle mais fragile**. Le c) ne renvoie pas au a) : il renvoie aux conditions du b du 3° du II de l'article 150-0 D ter, lesquelles retiennent une définition **sensiblement plus large** de l'activité éligible — activité commerciale, industrielle, artisanale, libérale, agricole ou financière, à la seule exception de la **gestion de son propre patrimoine mobilier ou immobilier**. Le marchand de biens, dont les immeubles sont des stocks, n'entre pas dans cette exclusion.

Il existe donc un **argument textuel sérieux** pour soutenir qu'une **souscription en numéraire** au capital d'une société de marchand de biens est éligible, alors que l'acquisition de ses titres sur le marché secondaire ne l'est pas. Cette asymétrie, régulièrement relevée par la doctrine des auteurs, ne résulte pas nécessairement d'une volonté délibérée du législateur, et je ne peux pas vous garantir que l'administration s'y tiendra en cas de contrôle : le raisonnement par cohérence d'ensemble du dispositif (dont l'objet est le financement de l'économie productive, à l'exclusion de l'immobilier) pourrait lui être opposé. **Je ne recommande pas de bâtir un remploi de 6,3 M€ sur ce fondement sans sécurisation préalable.**

**Voie d) — souscription de parts de FPCI, FCPR, SLP ou SCR éligibles.** Le quota d'investissement de ces fonds doit être respecté en sociétés exerçant une activité relevant du a) ; les fonds à sous-jacent immobilier sont donc écartés. Voie inutilisable pour votre projet, mais très utile comme **solution de repli** (cf. § 5).

---

## 5. Mes recommandations

**1. Ne pas engager les 70 % dans l'opération immobilière en l'état.** Le risque de déchéance du report est trop élevé au regard de l'enjeu.

**2. Utiliser la poche libre de 30 %.** Rien ne vous interdit d'affecter **2 700 000 €** à l'opération d'achat-rénovation-revente, sous quelque forme que ce soit (souscription, acquisition, compte courant, co-investissement). C'est la solution la plus simple si le projet immobilier peut être calibré à cette hauteur.

**3. Si vous souhaitez y affecter davantage : déposer une demande de rescrit** (LPF, art. L. 80 B, 1°) décrivant précisément l'activité de la société cible (achat-revente sans construction, nature et ampleur des travaux, absence de détention locative durable) et sollicitant confirmation de l'éligibilité d'une **souscription en numéraire** au titre du c). Le délai de réponse de trois mois est compatible avec votre échéance du 10 mars 2029, à condition d'engager la démarche rapidement. En l'absence de réponse favorable, vous conserverez le temps de réorienter le remploi.

**4. Explorer une requalification opérationnelle du projet.** Une société d'**entreprise générale de rénovation** intervenant comme prestataire pour le compte de tiers (activité industrielle et commerciale de travaux, sans détention des immeubles) est, elle, incontestablement éligible. Si votre logique économique est le savoir-faire de rénovation plutôt que la spéculation immobilière, une architecture séparant la structure de travaux (financée par le remploi) et la structure de portage immobilier (financée par la poche de 30 % et par la dette) mérite d'être étudiée. Attention toutefois : un tel montage ne doit pas être artificiel, sauf à s'exposer à l'abus de droit (LPF, art. L. 64 et L. 64 A).

**5. Prévoir une solution de repli calendaire.** Le remploi n'a pas à être unique : vous pouvez panacher (souscription au capital d'une PME opérationnelle, FPCI éligible 150-0 B ter, acquisition majoritaire d'une cible industrielle ou de services). Je recommande de **verrouiller au moins 6 300 000 € d'investissements incontestablement éligibles au plus tard fin 2028**, quitte à recourir à un FPCI éligible comme variable d'ajustement, plutôt que de se retrouver contraint en février 2029.

**6. Points de vigilance complémentaires :**
- **Assiette du quotum** : 70 % de 9 000 000 €, sans déduction de l'IS acquitté par la holding sur sa propre plus-value de cession ni des frais. Vérifier la trésorerie disponible et l'existence éventuelle d'un complément de prix (earn-out), qui viendrait augmenter l'assiette et rouvrir un délai.
- **Conservation** : 12 mois d'inscription à l'actif ; un aller-retour rapide sur les titres souscrits ferait tomber le report.
- **Formalisme** : engagement de réinvestissement de la société cédante, et surtout **maintien rigoureux de vos états de suivi annuels** — leur défaut est en pratique le premier motif de remise en cause.
- **Financement bancaire** : le remploi doit être réalisé en fonds propres pour la souscription ; l'effet de levier bancaire au niveau de la cible n'est pas pénalisant, mais il ne doit pas servir à « gonfler » artificiellement le montant investi.

---

## 6. Réponse synthétique à votre question

**Non.** Un réinvestissement dans une société d'achat-rénovation-revente d'immeubles ne permet pas, au titre du a) du 2° du I de l'article 150-0 B ter, de maintenir le report d'imposition : le renvoi au 3° du C du I de l'article 199 terdecies-0 A exclut les activités immobilières, et cette exclusion est plus large que la seule « gestion de son propre patrimoine immobilier » que le texte mentionne par ailleurs. Le même obstacle vaut pour une acquisition de contrôle au titre du b).

Une **souscription en numéraire** au capital d'une telle société pourrait, au titre du c), échapper à cette exclusion en raison d'un renvoi textuel différent, mais cette lecture n'est pas sécurisée et ne doit être mise en œuvre qu'après **rescrit**.

À défaut, l'opération immobilière ne peut être financée que **dans la limite de la fraction libre de 30 %, soit 2 700 000 €**, les 6 300 000 € restants devant être orientés vers un remploi éligible avant le **10 mars 2029**.

Je reste à votre disposition pour rédiger la demande de rescrit et pour arrêter, avec votre conseil en investissement, le plan de remploi et son calendrier. Merci de me transmettre l'acte d'apport, l'acte de cession, vos états de suivi du report et la documentation de présentation de la société cible.

---

## T33

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

Madame, Monsieur,

Je vous remercie de votre consultation. Vous m'avez interrogé sur le traitement fiscal, et plus particulièrement sur l'exigibilité d'une retenue à la source en France, d'une distribution de dividendes d'un montant de 20 000 000 euros que votre société (française) envisage de verser le 15 juin 2025 à sa société mère résidente au Luxembourg.

Voici mon analyse de votre situation.

### 1. Le principe : l'application d'une retenue à la source

Comme vous l'avez justement relevé en citant l'article 119 bis, 2 du Code Général des Impôts (CGI), le droit interne français pose le principe selon lequel les revenus distribués par une société française à un actionnaire dont le siège est situé hors de France sont soumis à une retenue à la source. 

Le taux de droit commun de cette retenue à la source pour une personne morale est aligné sur le taux normal de l'impôt sur les sociétés (soit 25 %).

Toutefois, ce principe est assorti d'exemptions prévues par le droit européen et les conventions fiscales bilatérales.

### 2. L'exonération au titre du régime "Mère-Fille" européen (Art. 119 ter du CGI)

La directive européenne "Mère-Fille", transposée en droit français à **l'article 119 ter du CGI**, permet d'exonérer totalement de retenue à la source les dividendes distribués par une filiale française à sa société mère européenne, sous réserve que plusieurs conditions cumulatives soient remplies. 

Au regard des éléments que vous m'avez communiqués, nous pouvons valider ces conditions :

*   **Forme sociale :** La société mère doit revêtir l'une des formes énumérées par la directive. La forme de Société Anonyme (SA) luxembourgeoise est expressément visée. *(Condition remplie)*
*   **Assujettissement à l'impôt :** La société mère doit être passible de l'impôt sur les sociétés de son État de résidence, sans possibilité d'option et sans en être exonérée. Vous m'indiquez qu'elle est soumise à l'IS luxembourgeois. *(Condition remplie)*
*   **Seuil de participation :** La société mère doit détenir au moins 10 % (voire 5 % sous certaines conditions) du capital de la société distributrice. Elle détient ici 100 %. *(Condition remplie)*
*   **Durée de détention :** Les titres doivent être conservés pendant au moins deux ans. La société mère détient les titres depuis cinq ans. *(Condition remplie)*

**Conclusion intermédiaire :** Sur la base de ces éléments objectifs, la distribution de 20 M€ prévue le 15 juin 2025 **bénéficie d'une exonération totale (0 %) de retenue à la source en France** en vertu de l'article 119 ter du CGI.

*Note subsidiaire : Même si le droit interne ne s'appliquait pas, la Convention fiscale franco-luxembourgeoise du 20 mars 2018 (article 10) prévoit également une retenue à la source de 0 % pour les participations supérieures à 5 % détenues depuis au moins 365 jours.*

### 3. Points d'attention et réserves d'usage (Clause anti-abus)

En tant que votre conseil, il est de mon devoir d'attirer votre attention sur la **clause anti-abus générale** prévue à l'article 119 ter, 3 du CGI. 

L'exonération de retenue à la source ne s'applique pas si la distribution s'inscrit dans un "montage ou une série de montages qui, ayant été mis en place pour obtenir, à titre d'objectif principal ou au titre d'un des objectifs principaux, un avantage fiscal allant à l'encontre de l'objet ou du but [de l'exonération], n'est pas authentique compte tenu de l'ensemble des faits et circonstances pertinents".

De plus, l'article 119 bis, 2 du CGI que vous citez mentionne la notion de **"bénéficiaire effectif"**. 

L'administration fiscale française est particulièrement vigilante sur les distributions importantes (comme c'est le cas ici avec 20 M€ issus d'une cession d'actif) vers le Luxembourg. Pour sécuriser cette exonération, nous devrons nous assurer que :
1.  La société mère luxembourgeoise est bien le *bénéficiaire effectif* de ce dividende (elle ne doit pas avoir l'obligation juridique ou de fait de reverser ce dividende à une autre entité située dans un pays tiers).
2.  La société mère luxembourgeoise dispose d'une **substance économique réelle** au Luxembourg (locaux, dirigeants qualifiés prenant les décisions, comptes bancaires, etc.) et n'est pas une simple "société boîte aux lettres".

### 4. Formalités déclaratives

Pour bénéficier de cette exonération lors de la mise en paiement le 15 juin 2025, votre société française devra :
*   Obtenir en amont une attestation de la société mère luxembourgeoise certifiant qu'elle remplit les conditions de l'article 119 ter du CGI.
*   Déclarer cette distribution sur la déclaration n° 2777 (à déposer et payer le cas échéant le 15 du mois suivant la mise en paiement, soit le 15 juillet 2025), en indiquant le montant distribué et l'application de l'exonération.

### Conclusion

**Aucune retenue à la source ne sera due** sur cette distribution de 20 000 000 euros, sous réserve que la société mère luxembourgeoise dispose d'une substance économique adéquate et soit le bénéficiaire effectif des fonds.

Je me tiens à votre entière disposition pour vous assister dans la rédaction de la documentation juridique de distribution, la revue de la substance de votre société mère, et l'accomplissement des formalités déclaratives (formulaire 2777).

Restant à votre écoute,

Bien à vous,

**[Votre Signature]**
Avocat au Barreau

---

## T34

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

La SCI est, au vu des éléments fournis, une **personne morale à prépondérance immobilière** au sens de l’article 726, I, 2° du CGI :

- ses titres ne sont, par nature, pas négociés sur un marché réglementé ou un système multilatéral de négociation ;
- son actif est constitué à 80 % d’immeubles situés en France, soit « principalement » d’immeubles français.

## 1. Droit d’enregistrement dû

La cession est soumise au droit d’enregistrement au taux de **5 %**.

Sous réserve que le prix de 4 000 000 € représente bien la totalité de la contrepartie taxable et qu’aucune valeur réelle supérieure ne doive être retenue :

\[
4\,000\,000 \times 5\% = 200\,000\ €.
\]

Le droit d’enregistrement s’élève donc à **200 000 €**.

### Point d’attention sur l’assiette

L’assiette n’est pas nécessairement limitée au seul prix affiché dans l’acte. Elle comprend, en principe, le prix stipulé augmenté des charges éventuellement mises à la charge du cessionnaire ; si la valeur réelle des titres est supérieure, cette valeur peut être retenue.

Une vigilance particulière est requise si :

- le cessionnaire reprend une dette due par la SCI au cédant, notamment un compte courant d’associé ;
- le prix est réduit ou compensé par la reprise d’engagements ;
- une partie de la contrepartie est différée, conditionnelle ou indirecte.

Ces éléments peuvent avoir une incidence tant sur l’assiette que sur les mentions obligatoires de l’acte.

## 2. Mentions obligatoires dans l’acte

L’acte de cession — ou la déclaration servant à la formalité — doit indiquer **expressément**, y compris par une réponse négative, les trois points prévus à l’article 726, III-B du CGI.

### a) Situation de la SCI au regard de l’article 1655 ter du CGI

L’acte doit préciser si la SCI est ou non une société mentionnée à l’article 1655 ter du CGI.

Cette qualification vise notamment certaines sociétés civiles ayant pour objet la construction ou l’acquisition d’immeubles en vue de leur division par fractions destinées à être attribuées aux associés. Il convient donc de vérifier les statuts, l’objet social et le fonctionnement effectif de la SCI avant de cocher cette mention.

**Formulation-type :**  
> « La Société [n’est pas / est] une société mentionnée à l’article 1655 ter du code général des impôts. »

### b) Droit de jouissance d’immeubles conféré au cessionnaire

L’acte doit préciser si les titres cédés confèrent au cessionnaire, directement ou indirectement, un droit à la jouissance d’un immeuble ou d’une fraction d’immeuble au sens de l’article 728 du CGI.

Cette mention est particulièrement importante lorsque les parts sont assorties d’une jouissance privative d’un lot, d’un appartement, d’un local ou d’une fraction d’immeuble.

**Formulation-type :**  
> « Les participations cédées [ne confèrent pas / confèrent] au cessionnaire, directement ou indirectement, un droit à la jouissance d’un immeuble ou d’une fraction d’immeuble au sens de l’article 728 du code général des impôts. »

En cas de réponse positive, il est recommandé d’identifier précisément l’immeuble ou la fraction d’immeuble concerné(e) et le fondement statutaire ou conventionnel de ce droit.

### c) Reprise ou paiement de dettes de la SCI envers le cédant

L’acte doit indiquer si le cessionnaire a acquitté, ou s’engage à acquitter, directement ou indirectement, des dettes contractées par la SCI auprès du cédant. Lorsqu’il existe une telle dette, son **montant** doit être précisé.

Cette situation vise typiquement le remboursement, par la SCI ou économiquement par le cessionnaire, d’un compte courant d’associé détenu par le cédant.

**Formulation-type en l’absence de dette :**  
> « Le cessionnaire n’a pas acquitté et ne s’engage pas à acquitter, directement ou indirectement, de dettes contractées par la Société auprès du cédant. »

**En présence d’un compte courant ou d’une dette envers le cédant :**  
> « Le cessionnaire [a acquitté / s’engage à acquitter], directement ou indirectement, une dette de la Société envers le cédant, correspondant à [nature de la dette], pour un montant de [●] euros. »

## 3. Hypothèse d’une signature à l’étranger

Si la cession est réalisée à l’étranger, elle devra, en application de l’article 726, III-A du CGI, être **constatée dans le mois** par un acte authentique reçu par un **notaire exerçant en France**.

Si l’acte est signé en France, cette exigence particulière ne s’applique pas ; la cession devra néanmoins faire l’objet de la formalité d’enregistrement dans le délai applicable.

## Conclusion pratique

Pour une signature le 20 mars 2024, il convient donc de prévoir dans l’acte :

1. un droit d’enregistrement de **200 000 €**, sous réserve de confirmation de l’assiette complète ;  
2. la qualification de la SCI comme personne morale à prépondérance immobilière ;  
3. les déclarations expresses requises sur :
   - l’article 1655 ter du CGI ;
   - l’existence ou non d’un droit de jouissance immobilier attaché aux titres ;
   - l’existence ou non de dettes de la SCI envers le cédant reprises ou acquittées par le cessionnaire, avec leur montant le cas échéant.

Avant signature, il faut surtout auditer le **compte courant d’associé du cédant**, les conventions de remboursement ou de garantie, ainsi que les droits de jouissance attachés aux parts : ce sont les points susceptibles de modifier l’assiette ou de rendre les déclarations de l’acte inexactes.

---

## T35

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

Bonjour, je vous remercie de me consulter avant de signer l'acte de cession des titres de la société civile immobilière.

Après analyse de la situation, il apparaît que la société civile immobilière dont vous cédez les titres est une personne morale à prépondérance immobilière au sens de l'article 726, I, 2° du Code Général des Impôts (CGI). En effet, son actif est constitué à 80 % d'immeubles situés en France, ce qui répond à la condition de prépondérance immobilière.

Par conséquent, la cession de ces titres est soumise au droit d'enregistrement prévu par l'article 726, I, 2° du CGI, qui est de 5 % du prix de cession.

Le prix de cession étant de 4 000 000 euros, le droit d'enregistrement dû sera de 200 000 euros (4 000 000 x 5 %).

En outre, l'article 726, III, B du CGI prévoit que l'acte de cession doit contenir certaines mentions expresses. Ainsi, l'acte doit indiquer :

1. si la société civile immobilière est une société mentionnée à l'article 1655 ter du CGI (société dont les titres ne sont pas négociés sur un marché réglementé) ;
2. si les participations cédées confèrent au cessionnaire, direct ou indirect, le droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'article 728 du CGI ;
3. si le cessionnaire a acquitté ou s'engage à acquitter, directement ou indirectement, des dettes contractées auprès du cédant par la société civile immobilière, en précisant, le cas échéant, leur montant.

Il est important de vérifier ces éléments et de les mentionner expressément dans l'acte de cession pour satisfaire aux exigences fiscales.

Enfin, je vous rappelle que l'acte de cession sera signé le 20 mars 2024. Il est donc important de s'assurer que les formalités nécessaires sont accomplies dans les délais impartis.

Je vous recommande de faire appel à un notaire exerçant en France pour recevoir l'acte en la forme authentique, comme cela est requis pour les cessions de participations dans des personnes morales à prépondérance immobilière.

Je reste à votre disposition pour tout complément d'information ou pour discuter des implications fiscales de cette opération.

---

## T36

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

En votre qualité de dirigeant souhaitant transmettre à vos deux enfants, en pleine propriété et à parts égales, la totalité des titres de votre société par actions simplifiée (SAS) pour une valeur de 20 000 000 euros, vous m’interrogez sur l’applicabilité de l’exonération partielle de 75 % prévue à l’article 787 B du Code général des impôts (CGI), dans sa version en vigueur au 5 octobre 2023.

Je reprends ci-après les conditions posées par ce texte, avant d’examiner leur mise en œuvre dans votre situation.

---

### 1. Rappel du dispositif de l’article 787 B du CGI

L’article 787 B, premier alinéa, exonère de droits de mutation à titre gratuit, à concurrence de 75 % de leur valeur, les parts ou actions d’une société ayant une activité industrielle, commerciale, artisanale, agricole ou libérale, transmises en pleine propriété, sous réserve du respect des conditions suivantes :

- un **engagement collectif de conservation** des titres, signé par le défunt ou le donateur et d’autres associés, portant sur un pourcentage minimal de droits, et ayant été conclu depuis au moins deux ans avant la transmission ;
- un **engagement individuel** de conservation des titres reçus, pris par chaque donataire dans l’acte de donation, pour une durée de quatre ans à compter de la transmission ;
- le maintien, pendant toute la durée de l’engagement collectif et les trois années suivant la transmission, de l’exercice d’une **fonction de direction** au sein de la société par l’un des signataires de l’engagement collectif ou par l’un des donataires.

---

### 2. Analyse des conditions formelles et de durée

#### 2.1. Engagement collectif de conservation
Un engagement collectif a été signé le 3 mars 2021, portant sur la totalité des droits de la SAS, et est toujours en cours. La donation serait consentie le 5 octobre 2023, soit plus de deux ans après la signature de l’engagement.  
La condition de durée minimale de deux ans avant la transmission est donc **satisfaite**.

#### 2.2. Engagement individuel des donataires
Les deux enfants, donataires, prendront chacun dans l’acte de donation l’engagement de conserver les titres reçus pendant quatre ans.  
Cette condition est **remplie**.

#### 2.3. Fonction de direction
Vous-même, donateur et signataire de l’engagement collectif, conserverez la présidence de la SAS pendant trois ans à compter de la donation. La fonction de président d’une SAS est une fonction de direction éligible au sens de l’article 787 B (CGI, ann. II, art. 294 ter).  
Cette condition est également **satisfaite**.

---

### 3. Le point crucial : l’activité de la société

L’article 787 B exige que la société dont les titres sont transmis exerce une activité **industrielle, commerciale, artisanale, agricole ou libérale**. La nature de l’activité s’apprécie au regard de l’activité réelle et effective de la société.

#### 3.1. La location meublée : une activité commerciale par nature, mais sous conditions
La location de biens meublés est, en principe, une activité commerciale par nature (article 34 du CGI). Toutefois, la jurisprudence et la doctrine administrative excluent du bénéfice du « pacte Dutreil » les activités de simple gestion passive d’un patrimoine immobilier.

Ainsi, une société dont l’activité se borne à la location de logements meublés sans prestations de services significatives, sans moyens matériels et humains dédiés, est réputée exercer une activité **civile de gestion de patrimoine**, non éligible à l’exonération partielle (BOI-ENR-DMTG-20-30-20-10, § 150 et suiv. ; CE, 8 février 2019, n° 407641, Sté A. ; CE, 19 juin 2020, n° 428834, Sté B.).

À l’inverse, la location meublée peut être qualifiée d’activité commerciale opérationnelle lorsqu’elle s’accompagne de prestations de services para-hôtelières (entretien, fourniture de linge, nettoyage régulier, accueil des locataires, etc.) ou lorsqu’elle nécessite la mise en œuvre de moyens matériels et humains importants, conférant à la société un caractère actif.

#### 3.2. Application à votre situation
Votre SAS détient **quarante appartements meublés**. Vous indiquez en conserver la présidence pendant trois ans, ce qui suggère une implication personnelle dans la gestion.  
Cependant, les éléments que vous m’avez communiqués ne permettent pas de caractériser avec certitude la nature de l’activité :

- S’agit-il de locations saisonnières de type meublé de tourisme, avec des services réguliers (ménage, linge, accueil) ?
- Ou de locations nues longue durée, même si les logements sont meublés, sans prestations particulières ?
- La société emploie-t-elle du personnel dédié ? Dispose-t-elle d’une structure d’exploitation (site internet, service de réservation, etc.) ?

En l’absence de ces précisions, **le risque de requalification en activité de gestion passive de patrimoine immobilier est réel**. L’administration fiscale pourrait refuser le bénéfice de l’exonération partielle, considérant que la société n’exerce pas une activité commerciale éligible.

---

### 4. Conclusion et recommandations

Sous réserve de la qualification effective de l’activité de la SAS comme une activité commerciale opérationnelle (et non une simple gestion passive), les conditions de l’exonération partielle de 75 % prévue à l’article 787 B du CGI sont réunies pour la donation projetée du 5 octobre 2023.

Je vous recommande de procéder sans délai à une **analyse approfondie de l’activité réelle** de la société, en examinant notamment :
- la nature des locations (courte durée, services proposés),
- les moyens matériels et humains affectés à l’exploitation,
- la comptabilisation des recettes (BIC ou revenus fonciers).

Afin de sécuriser l’opération, il est possible de solliciter un **rescrit fiscal** auprès de l’administration (article L. 80 B du LPF) pour obtenir une prise de position formelle sur l’éligibilité de l’activité. Cette démarche est vivement conseillée compte tenu de l’enjeu patrimonial (20 M€).

Je me tiens à votre disposition pour vous assister dans cette analyse et pour la rédaction de l’acte de donation en y intégrant l’ensemble des engagements requis.

Votre conseil fiscal

---

## T37

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

Cher Client, Cher Confrère,

La question est de savoir si la donation projetée peut bénéficier de l'exonération partielle de 75 % prévue à l’article 787 B du Code général des impôts (CGI), soit une exonération d’assiette de 15 000 000 euros.

**La réponse est négative.** L’exonération n’est pas applicable en l’espèce. La société, bien qu’exploitée sous forme de SAS, exerce une activité de location de locaux meublés à usage d’habitation. Cette activité est de nature civile au sens du droit fiscal, et non commerciale, ce qui exclut le bénéfice du dispositif.

---

### I. Analyse détaillée des conditions de l’article 787 B du CGI

L’article 787 B subordonne l’exonération à plusieurs conditions cumulatives. Votre projet remplit la plupart d’entre elles, mais achoppe sur une condition fondamentale tenant à la nature de l’activité sociale.

#### A. Les conditions remplies dans votre projet

Je relève que votre schéma satisfait aux exigences suivantes :

1.  **Nature de la transmission** : Donation en pleine propriété de parts sociales.
2.  **Engagement collectif de conservation** : Un engagement collectif a été signé le 3 mars 2021, portant sur la totalité des titres, pour une durée minimale de deux ans. Il est toujours en cours au jour de la donation projetée (le 5 octobre 2023), soit plus de deux ans après sa signature.
3.  **Engagement individuel** : Chaque enfant donataire prendra, dans l’acte de donation, l’engagement individuel de conserver les titres reçus pendant quatre ans.
4.  **Poursuite de l’activité et direction** : L’un des signataires de l’engagement collectif (le donateur lui-même) conservera la présidence de la société pendant les trois années suivant la transmission, conformément au 4° de l’article 787 B.

#### B. La condition dirimante : l’activité de la société

Le point bloquant est la condition posée par le premier alinéa de l’article 787 B : la société doit exercer une activité « **industrielle, commerciale, artisanale, agricole ou libérale** ».

Votre société, une SAS, donne en location **quarante appartements meublés**. Cette activité est, en droit fiscal, une activité de **location de locaux meublés à usage d’habitation**.

La jurisprudence constante et la doctrine administrative (BOI-ENR-DMTG-10-20-40-10, § 220 et suivants) analysent cette activité comme suit :

-   La location de locaux nus est une activité civile, sauf rares exceptions.
-   **La location de locaux meublés à usage d’habitation est également une activité civile**, bien que l’article 35 du CGI la qualifie fiscalement de bénéfices industriels et commerciaux (BIC) pour le seul calcul de l’impôt sur le revenu du bailleur.

Cette qualification en BIC est une fiction fiscale propre à la détermination de la catégorie de revenus imposable. **Elle ne confère pas pour autant un caractère commercial à l’activité de la société** pour l’application des droits de mutation à titre gratuit.

Le Conseil d’État a eu l’occasion de le confirmer nettement. Dans un arrêt de principe (CE, 21 octobre 2011, n° 328787, *M. et Mme Marion*), la Haute Juridiction a jugé que l’activité de location d’un immeuble à usage commercial, fiscalement qualifiée de BIC, restait une activité civile pour l’application de l’exonération des biens professionnels (ancien article 885 R du CGI, logique reprise pour l’article 787 B). La doctrine administrative transpose cette analyse à l’activité de location meublée à usage d’habitation.

Ainsi, la location meublée, même à titre habituel et avec un nombre important de lots (quarante appartements), demeure une activité **civile** au sens de l’article 787 B du CGI. Elle ne figure pas dans la liste des activités éligibles (industrielle, commerciale, etc.).

---

### II. Confirmation par la doctrine fiscale

Le BOFiP (BOI-ENR-DMTG-10-20-40-10) est explicite au § 225 :

> « *Ne sont pas considérées comme des activités commerciales au sens de l’article 787 B du CGI les activités de location de locaux meublés à usage d’habitation, quand bien même elles seraient exercées à titre habituel et revêtiraient un caractère spéculatif. Ces activités sont de nature civile.* »

Il n’existe pas, à ma connaissance, de tolérance ou de mesure transitoire permettant d’assimiler ces activités à une activité commerciale pour le bénéfice du « pacte Dutreil ».

---

### III. Conclusion et préconisations

En l’état actuel de la législation et de son interprétation, la donation des titres de la SAS, dont l’actif est composé de quarante appartements donnés en location meublée, **ne peut pas bénéficier de l’exonération partielle de 75 % de l’article 787 B du CGI**.

La seule qualification de l’activité sociale suffit à exclure le dispositif, quand bien même toutes les autres conditions formelles seraient scrupuleusement respectées.

**Voie alternative possible à explorer :**

Si l’objectif prioritaire est l’optimisation fiscale de la transmission, il faudrait envisager une restructuration en amont pour rendre la société éligible. Cela pourrait passer par :

1.  Une modification substantielle de l’activité opérationnelle de la société, en y adjoignant une réelle activité commerciale prépondérante (par exemple, des prestations de services para-hôtelières significatives, similaires à celles retenues pour la qualification de « résidence de tourisme » ou d’« établissement commercial »). Cette voie est complexe et doit être soigneusement évaluée, car la jurisprudence administrative (CAA Paris, 7 janvier 2020, n° 18PA02129) exige que les services fournis dépassent la simple gestion locative normale pour requalifier l’activité en activité commerciale.
2.  Une option pour l’impôt sur les sociétés de la SAS, si ce n’est pas déjà le cas. Cette option, bien que fiscalement avantageuse par ailleurs, est sans incidence sur la nature civile ou commerciale de l’activité de location meublée pour l’application de l’article 787 B.

Sans une telle transformation, la donation reste imposable aux droits de mutation à titre gratuit selon le tarif progressif en ligne directe, après application d’un abattement de 100 000 euros par parent et par enfant. L’impact financier sera considérable.

Je me tiens à votre disposition pour expertiser avec vous et votre notaire les pistes de restructuration envisageables afin de sécuriser l’application du régime de faveur dans un délai compatible avec vos objectifs.

Je vous prie d'agréer, Cher Client, Cher Confrère, l'expression de mes salutations distinguées.

[Signature de l'avocat fiscaliste]

---

## T38

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

# CONSULTATION

**Objet :** obligation de remploi de l'article 150-0 B ter, I, 2° du CGI – cession de février 2026 pour 9 000 000 €

---

## Avertissement liminaire

L'extrait que vous me communiquez ne reproduit que le **a)** du 2° du I de l'article 150-0 B ter. Le texte comporte également des **b), c) et d)**, qui ouvrent trois autres catégories de remploi, en pratique bien plus utilisables qu'un pur financement de moyens d'exploitation par une holding. Mon avis ci-dessous raisonne sur l'article complet.

Par ailleurs, je réserve l'incidence éventuelle des dispositions de la loi de finances pour 2026 sur les taux d'imposition de la plus-value en report (PFU, CEHR, contribution différentielle).

---

## 1. Trois vérifications avant tout conseil

Je ne peux pas vous conseiller utilement sans les éléments suivants, et je vous les demande par priorité.

**1.1. La date exacte de l'apport.** Le délai de trois ans se décompte **de date à date**. Si l'apport est antérieur au jour de la cession de février 2026 diminué de trois ans — même de vingt-quatre heures — **il n'y a aucune obligation de remploi** et le report est maintenu sans contrainte. Vous me dites « moins de trois ans » ; c'est précisément le genre de qualification qu'il faut vérifier sur l'acte, et non sur le souvenir. Je veux le traité d'apport, le PV d'AGE et le rapport du commissaire aux apports.

**1.2. La structure du prix.** L'assiette des 70 % est le **produit de la cession**, c'est-à-dire le **prix brut**, sans déduction de l'IS, des frais d'intermédiation ni des sommes séquestrées au titre de la garantie de passif. Je dois donc savoir :
- si les 9 M€ sont intégralement encaissés ou si une fraction est sous séquestre / à terme (crédit-vendeur) ;
- s'il existe une clause d'*earn-out*. Le complément de prix perçu ultérieurement supporte sa **propre obligation de remploi de 70 %, dans un délai de deux ans à compter de sa perception** — piège classique, souvent découvert trop tard.

**1.3. Le montant de la plus-value en report et son coût de sortie.** C'est la donnée qui commande l'arbitrage. Si la plus-value en report est de 8 M€, la déchéance coûte de l'ordre de 2,7 à 3 M€ (PFU 30 % + CEHR, sous réserve des règles applicables et d'éventuels abattements pour apports anciens) : le remploi s'impose. Si elle est de 400 000 €, il n'est pas certain qu'il soit rationnel de s'imposer trois ans de contrainte et une immobilisation de 6,3 M€ pour économiser 130 000 €. **Nous devons chiffrer avant de décider.** Je souhaite l'état de suivi (2074-I) et la déclaration de l'année de l'apport.

*Point connexe :* vérifiez le régime IS de la cession au niveau de la holding. Si elle détenait les titres depuis **plus de deux ans**, le régime des titres de participation s'applique (imposition de la seule quote-part de frais et charges de 12 %, soit ~3 % de coût effectif). En deçà de deux ans, la plus-value est taxée à 25 % en totalité, ce qui peut créer une tension de trésorerie puisque les 70 % se calculent, eux, sur le prix **brut**. Dans un schéma d'apport-cession classique, la plus-value de la holding est cependant faible (prix de cession ≈ valeur d'apport).

---

## 2. Le périmètre de l'obligation, si elle est confirmée

| Paramètre | Valeur |
|---|---|
| Assiette | 9 000 000 € (prix brut) |
| Quotité à remployer | **70 % = 6 300 000 €** |
| Fraction libre d'emploi | 2 700 000 € |
| Échéance | **février 2029**, date à date à compter de la cession |
| Engagement | pris par la **holding**, formalisé, et suivi déclaratif annuel |

Deux points que je souligne parce qu'ils sont mal compris :

- **Le seuil est couperet.** Un remploi de 65 % n'emporte pas un maintien partiel du report : il emporte la **déchéance totale**. On vise donc en pratique 75 %, pas 70 %.
- **C'est la holding cédante qui doit réinvestir**, et non une filiale, une société sœur ou vous-même. Un apport en compte courant, un prêt intra-groupe ou un placement financier ne sont pas des remplois.

---

## 3. Les quatre voies de remploi et leurs pièges

**a) Financement de moyens permanents d'exploitation** affectés à l'activité opérationnelle **de la holding elle-même**. Ce n'est utilisable que si votre holding exerce une véritable activité opérationnelle propre (ou une animation effective). Pour une holding qui n'a jamais eu que des titres à son actif, cette voie est en pratique fermée. L'immobilier de rapport, la location meublée et les activités de gestion de patrimoine sont exclus.

**b) Acquisition d'une fraction du capital d'une société opérationnelle avec prise de contrôle.** La voie la plus solide sur le plan économique. Le contrôle s'apprécie au sens du 2° du III de l'article L. 233-3 du code de commerce (majorité des droits de vote, contrôle de fait, contrôle conjoint par accord). Attention : il faut **acquérir** le contrôle ; renforcer une participation dans une société que vous contrôlez déjà n'est pas éligible par cette voie. L'acquisition d'une holding animatrice est admise, mais l'animation doit être **effective et documentée dès l'acquisition** — c'est un terrain de contentieux.

**c) Souscription en numéraire au capital** (initial ou augmentation) d'une société opérationnelle soumise à l'IS. Pas de condition de contrôle. Utilisable y compris dans une société que vous contrôlez déjà, sous réserve d'un besoin de financement réel — un aller-retour de trésorerie serait requalifié.

**d) Souscription de parts de FCPR, FPCI, SLP ou de titres de SCR.** C'est la soupape. La souscription doit intervenir dans les trois ans ; les versements peuvent être étalés sur **cinq ans** à compter de la souscription ; le véhicule doit respecter un quota d'investissement de **75 %** en sociétés opérationnelles, et les parts doivent être **conservées cinq ans**. Le marché propose de nombreux fonds explicitement « éligibles 150-0 B ter ». Deux réserves : (i) vous portez le risque du respect du quota par le fonds — exigez une clause contractuelle et une attestation annuelle du dépositaire ; (ii) cette voie **allonge à dix ans** (au lieu de cinq) la durée de conservation exigée du donataire en cas de donation ultérieure des titres de la holding.

**Obligation de conservation :** 12 mois pour les biens et titres acquis au titre des a), b) et c), décomptés de leur inscription à l'actif ; 5 ans pour les parts de fonds du d).

**Emplois non éligibles** (liste des erreurs que je vois le plus souvent) : SCPI, OPCI, immobilier locatif nu ou meublé, contrat de capitalisation, compte à terme, portefeuille titres, compte courant d'associé, rachat de vos propres titres, acquisition minoritaire hors souscription.

---

## 4. Ce que je vous conseille

**4.1. Cloisonner immédiatement la trésorerie.** Ouvrez un compte dédié pour 6 300 000 € (je recommande de sanctuariser 6,8 M€). Le solde de 2,7 M€ est libre : il peut être placé sans contrainte dans la holding (contrat de capitalisation, immobilier, private equity non labellisé). Rappelez-vous que sa sortie vers votre patrimoine personnel reste un dividende imposable.

**4.2. Ne pas confondre trois ans et « j'ai le temps ».** Ce qui compte est le **décaissement effectif**, pas la signature d'une LOI. Un build-up prend douze à dix-huit mois entre l'identification de la cible et le closing, et une opération peut échouer à trois mois de la signature. Je fixe donc l'échéance interne à **septembre 2028**, six mois avant le terme légal.

**4.3. Séquencer.** Je vous propose l'architecture suivante :
- **Phase 1 (2026) :** définition de la thèse d'investissement opérationnelle et mandat de recherche de cible. Objectif : 3,5 à 4,5 M€ par la voie b).
- **Phase 2 (2026-2027) :** souscription de 2 à 2,5 M€ dans deux ou trois FPCI éligibles, sur des millésimes différents. Cette poche est votre filet de sécurité : elle est certaine dans son principe et étale les appels de fonds. Elle doit être souscrite **tôt**, pas en 2028 en catastrophe.
- **Phase 3 (2027-2028) :** ajustement par souscriptions au capital (voie c) pour atteindre les 75 %.

**4.4. Sécuriser la preuve.** Constituez dès maintenant un dossier de remploi : engagement formalisé par décision du président, mention dans la liasse, état de suivi annuel, attestations des sociétés cibles sur leur activité, attestations des fonds sur le quota de 75 %, et pour toute holding animatrice une convention d'animation exécutée avec preuves matérielles. En cas de contrôle, la charge probatoire de l'éligibilité vous incombe.

**4.5. Ne prenez aucune décision de distribution** avant d'avoir bouclé le remploi.

---

## 5. Points d'attention connexes

- **Transmission.** La donation des titres de la holding purge définitivement le report si le donataire les conserve **cinq ans** (**dix ans** si la holding a remployé via des fonds du d). Si une transmission familiale est envisagée, cela conditionne l'arbitrage entre b)/c) et d). À intégrer dès maintenant dans le schéma.
- **Décès.** Le décès de l'apporteur éteint définitivement le report. Cela peut modifier l'analyse coût/contrainte selon votre âge et votre état de santé.
- **Départ à l'étranger.** Tout projet d'expatriation doit être examiné avant, et non après.
- **Abus de droit.** Le dispositif est un régime légal : le recourir n'est pas abusif en soi. En revanche, un remploi de façade (coquille sans substance, société prétendument opérationnelle mais patrimoniale, circularité des flux) est régulièrement remis en cause. Chaque remploi doit avoir une **substance économique démontrable**.

---

## 6. Prochaine étape

Merci de me transmettre sous huitaine : le traité d'apport et le PV d'AGE, le protocole de cession et l'acte réitératif, le relevé de compte attestant l'encaissement, la déclaration de revenus de l'année de l'apport et l'état de suivi 2074-I, ainsi que les comptes de la holding.

Je vous adresserai alors une note chiffrée arrêtant (i) la date butoir exacte, (ii) l'assiette définitive des 70 % en intégrant séquestre et compléments de prix, (iii) le coût comparé du remploi et de la déchéance, et (iv) un projet d'engagement de remploi et de calendrier d'exécution.

---

## T39

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

**Objet : Conseil sur le réinvestissement du produit de cession pour maintenir le report d’imposition (Article 150-0 B ter du CGI)**

**À l’attention de [Nom du Client],**
**Holding [Nom de la Holding]**

**Référence :** Cession de titres en février 2026 – Obligation de réinvestissement pour préserver le report d’imposition

---

### **1. Rappel du contexte et enjeux fiscaux**
Votre holding a cédé en **février 2026** des titres d’une société d’exploitation pour un montant de **9 000 000 €**, moins de **3 ans après leur apport** par vos soins. Conformément à l’**article 150-0 B ter, I, 2° du CGI**, cette cession aurait normalement **mis fin au report d’imposition** sur la plus-value latente au moment de l’apport.

Cependant, le texte prévoit une **dérogation** : le report d’imposition peut être **maintenu** si votre holding s’engage à **réinvestir au moins 70 % du produit de cession (soit 6 300 000 €)** dans un délai de **3 ans à compter de la date de cession (février 2026 → février 2029)**.

---

### **2. Conditions strictes du réinvestissement (Art. 150-0 B ter, I, 2° a)**
Le réinvestissement doit être affecté :
- **Exclusivement au financement de moyens permanents d’exploitation** liés à une **activité éligible** (au sens du **3° du C du I de l’article 199 terdecies-0 A du CGI**).
  - **Activités éligibles** : Activités industrielles, commerciales, artisanales, agricoles ou libérales (sous conditions).
  - **Activités exclues** :
    - **Gestion de patrimoine immobilier** (même pour votre propre compte).
    - Activités financières ou de simple détention de participations (sauf exceptions précises).

**→ Votre holding doit donc investir dans une activité opérationnelle concrète**, et non dans des placements financiers ou immobiliers passifs.

---

### **3. Stratégies de réinvestissement recommandées**
Pour respecter les critères légaux, voici des pistes **sécurisées fiscalement** :

#### **A. Réinvestissement dans une activité opérationnelle**
- **Acquisition d’une nouvelle société d’exploitation** (via achat de titres ou apport en capital) :
  - La holding pourrait **racheter une société active** (ex : entreprise industrielle, commerciale) et **financer son développement** (machines, stocks, R&D).
  - **Attention** : La société cible doit exercer une **activité éligible** (pas de holding pure ou de gestion immobilière).

- **Création d’une filiale opérationnelle** :
  - La holding pourrait **créer une nouvelle société** (ex : start-up, activité de production) et y injecter les fonds sous forme de **capital ou comptes courants d’associés** (si affectés à des moyens permanents).

#### **B. Financement de moyens permanents existants**
Si votre holding a déjà une **activité éligible** (ex : une filiale active), elle peut :
- **Augmenter le capital** de cette filiale pour financer des investissements productifs (usines, brevets, etc.).
- **Accorder des prêts participatifs** ou **comptes courants bloqués** à la filiale, **à condition que les fonds soient affectés à des moyens permanents** (ex : achat de matériel, fonds de roulement durable).

#### **C. Investissements directs dans des actifs éligibles**
- **Achat de matériel industriel** (si la holding exerce elle-même une activité éligible, ce qui est rare pour une holding classique).
- **Financement de R&D** via une filiale dédiée.

---

### **4. Pièges à éviter**
- **Réinvestissement dans l’immobilier** :
  - Même si la holding achète un bien immobilier **pour son activité propre** (ex : locaux pour une filiale), cela pourrait être **requalifié en gestion de patrimoine** (exclu du dispositif).
  - **Solution alternative** : Si l’immobilier est indispensable (ex : usine), structurez l’investissement via une **filiale opérationnelle** (ex : SCI à l’IR avec activité de location meublée éligible).

- **Placements financiers** :
  - Les investissements en **actions, obligations, ou fonds** (même en private equity) **ne sont pas éligibles**, car ils relèvent de la gestion de patrimoine.

- **Délai de 3 ans** :
  - Le réinvestissement doit être **effectué avant février 2029**. Un engagement écrit (ex : pacte d’associés, délibération) est **fortement recommandé** pour prouver la volonté de réinvestir à l’administration fiscale.

---

### **5. Formalités à respecter**
1. **Engagement écrit** :
   - Rédiger un **document formel** (délibération du conseil d’administration ou de l’associé unique) **avant février 2029**, précisant :
     - Le montant à réinvestir (**≥ 6 300 000 €**).
     - La nature de l’investissement (ex : "achat de 100 % de la société X, active dans la fabrication de...").
     - Le calendrier prévisionnel.

2. **Preuves du réinvestissement** :
   - Conserver tous les **justificatifs** (contrats d’acquisition, factures, statuts de la filiale, etc.) pour prouver que les fonds ont bien été affectés à une **activité éligible**.

3. **Déclaration fiscale** :
   - Dans la **liasse fiscale de la holding**, mentionner le réinvestissement dans les **cases prévues** (ex : formulaire 2050 pour les plus-values).

---

### **6. Recommandation finale**
**Priorité absolue** : **Réinvestir 6 300 000 € minimum d’ici février 2029 dans une activité opérationnelle éligible**, via :
✅ **L’acquisition d’une société active** (secteur industriel, commercial, etc.).
✅ **Le financement d’une filiale existante ou nouvelle** (capital, prêts participatifs) pour des moyens permanents.

**À éviter** :
❌ L’immobilier pur (sauf via une filiale avec activité éligible).
❌ Les placements financiers (actions, fonds).
❌ Tout réinvestissement après février 2029.

---
**Prochaines étapes proposées** :
1. **Audit des activités éligibles** dans votre groupe pour identifier des cibles de réinvestissement.
2. **Structuration juridique** (ex : création d’une filiale, montage d’une acquisition).
3. **Rédaction de l’engagement de réinvestissement** (à valider avec votre expert-comptable).

**Je reste à votre disposition pour affiner cette stratégie en fonction de votre situation précise.**

**Cordialement,**
[Votre Nom]
Avocat Fiscaliste
[Cabinet X]
[Coordonnées]

---

## T40

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

**Objet : Analyse de l’application du taux réduit de TVA (5,5 %) sur un chantier de rénovation énergétique – Réponse à la proposition de rectification**

**À l’attention de [Nom du gérant]**
**De la part de [Votre nom], Avocat fiscaliste**

---

### **1. Contexte et problème posé**
Votre entreprise a facturé, le **15 avril 2025**, l’installation d’une chaudière dans une maison de **15 ans** (donc achevée depuis plus de 2 ans) occupée par son propriétaire, pour un montant de **8 500 € HT**. Vous avez appliqué le **taux réduit de 5,5 %** au titre des prestations de rénovation énergétique (CGI, art. 278-0 bis A).
L’administration fiscale conteste ce taux et réclame la différence entre **5,5 % et 20 %**, soit **14,5 %** de majoration (soit **1 232,50 €** de TVA supplémentaire).

**Question : Le taux de 5,5 % était-il légalement applicable ?**

---

### **2. Analyse juridique**
#### **A. Conditions générales du taux réduit (CGI, art. 278-0 bis A, I)**
Pour bénéficier du taux réduit de **5,5 %**, les prestations doivent remplir **cumulativement** les conditions suivantes :
1. **Locaux achevés depuis plus de 2 ans** → **Condition remplie** (maison de 15 ans).
2. **Affectation à l’habitation** → **Condition remplie** (logement occupé par son propriétaire).
3. **Prestations éligibles** : pose/installation d’équipements visant à économiser l’énergie ou utiliser des énergies renouvelables, notamment :
   - **Amélioration du chauffage** (point c) du I) → **Condition potentiellement remplie** (installation d’une chaudière).

**→ À ce stade, le taux réduit semble applicable.**

#### **B. Exception spécifique aux chaudières (CGI, art. 278-0 bis A, III bis)**
**Texte clé** :
> *"Par dérogation au I du présent article, le taux prévu à l'article 278 s'applique aux prestations de rénovation énergétique comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles."*

- **Interprétation** :
  - Le **taux normal de 20 %** (art. 278 du CGI) s’applique **obligatoirement** si la chaudière installée est **susceptible de fonctionner avec des combustibles fossiles** (gaz, fioul, etc.), **même si elle est également compatible avec des énergies renouvelables** (ex. : chaudière hybride).
  - **Little green lie** : L’administration fiscale considère que toute chaudière **non 100 % renouvelable** (ex. : chaudière à granulés avec appoint gaz) tombe sous cette exception.

- **Conséquence** :
  Si la chaudière installée **peut utiliser du gaz, du fioul ou tout autre combustible fossile**, le taux réduit de **5,5 % est exclu**, et le taux normal de **20 %** s’applique.

#### **C. Application à votre cas**
- **Type de chaudière installée** :
  - **Si la chaudière est 100 % renouvelable** (ex. : chaudière à granulés de bois **exclusivement**, pompe à chaleur) → **5,5 % applicable**.
  - **Si la chaudière est mixte ou fossile** (ex. : chaudière gaz à condensation, même haute performance) → **20 % applicable** (III bis).

**Problème** : Vous n’avez pas précisé le type de chaudière. **C’est le point déterminant.**

---
---

### **3. Solutions et recommandations**
#### **A. Vérification immédiate**
1. **Consulter la facture et le devis** :
   - Quel est le **modèle exact de la chaudière** ?
   - Est-elle **100 % renouvelable** (ex. : label "100 % biomasse") ou **compatible avec des combustibles fossiles** ?

2. **Preuves à rassembler** :
   - Fiche technique du fabricant (mentionnant les combustibles compatibles).
   - Attestation du fournisseur confirmant l’absence de compatibilité avec les énergies fossiles.

#### **B. Stratégie de défense**
- **Si la chaudière est 100 % renouvelable** :
  - **Contester la rectification** en fournissant les preuves techniques.
  - Argument : Le **III bis** ne s’applique pas, car la chaudière n’est **pas susceptible** d’utiliser des fossiles.

- **Si la chaudière est mixte/fossile** :
  - **Reconnaître l’erreur** et négocier un étalement du paiement (l’administration peut accepter un plan de règlement).
  - **Vérifier si d’autres travaux** (isolation, etc.) sur le même chantier pourraient bénéficier du taux réduit (pour limiter la régularisation).

#### **C. Prévention pour l’avenir**
- **Systématiquement vérifier** le type de chaudière avant d’appliquer le taux réduit.
- **Exiger une attestation du client** confirmant que l’équipement est 100 % renouvelable (si applicable).
- **Former vos équipes** sur les exceptions du **III bis** (piège fréquent en rénovation énergétique).

---
---

### **4. Conclusion**
| **Type de chaudière**       | **Taux applicable** | **Action recommandée**                          |
|-----------------------------|---------------------|-----------------------------------------------|
| 100 % renouvelable          | 5,5 %               | Contester la rectification avec preuves.      |
| Mixte ou fossile            | 20 %                | Accepter la régularisation (1 232,50 €).      |

**→ Sans information sur le type de chaudière, il est impossible de trancher.**
**Urgence** : Identifiez le modèle exact et consultez sa fiche technique.

---
**Prochaines étapes** :
1. Me transmettre **le modèle de la chaudière** pour analyse précise.
2. Si nécessaire, je peux rédiger un **recours gracieux** ou une **réponse détaillée à l’administration**.

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées]

---
**PS** : Si la chaudière est fossile, la régularisation est inévitable, mais nous pouvons vérifier si d’autres postes de la facture (main-d’œuvre liée à l’isolation, etc.) pourraient rester à 5,5 %.

