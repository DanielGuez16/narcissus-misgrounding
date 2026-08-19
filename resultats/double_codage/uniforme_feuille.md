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

Portez une valeur par cellule dans `uniforme_saisie.csv`, en face de son etiquette.
N'ouvrez pas `reference_scellee.json` avant d'avoir fini : il contient le codage
du modele, que vous ne devez pas connaitre en codant.


---

## U01

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

**Non, aucune retenue à la source n’est due.**

Les dividendes versés par une société française à des non-résidents relèvent en principe de l’article 119 bis, 2 du CGI et sont soumis à retenue à la source au taux de l’article 187. L’exception prévue par le texte que vous citez (OPC étrangers remplissant certaines conditions) ne s’applique pas ici.

Cette imposition de principe est toutefois écartée par l’article 119 ter du CGI, qui transpose la directive « mères-filiales ». Les conditions sont réunies :

- la bénéficiaire a son siège dans un État membre de l’Union européenne (Luxembourg) ;
- elle revêt une forme éligible (société anonyme) et est soumise à l’impôt sur les sociétés luxembourgeois sans option ni exonération ;
- elle détient 100 % du capital de la société distributrice depuis cinq ans (seuil de 10 % et durée minimale de deux ans largement dépassés) ;
- elle est l’ayant droit effectif des dividendes.

La clause anti-abus de l’article 119 ter, 3 n’apparaît pas caractérisée au vu des éléments communiqués (détention historique, forme sociétaire classique, assujettissement réel à l’IS luxembourgeois).

La convention franco-luxembourgeoise n’a pas à être mobilisée : l’exonération interne est plus favorable.

La société distributrice peut donc procéder au paiement le 15 novembre 2024 sans retenue à la source. Elle conservera les justificatifs (statuts, attestation de résidence et d’assujettissement à l’IS, historique de détention) pour le cas d’un contrôle. Si un établissement payeur intervient, il conviendra de lui transmettre ces éléments afin qu’il n’applique pas la retenue.

Je reste à votre disposition pour formaliser l’attestation ou examiner tout élément complémentaire (substance de la société luxembourgeoise, éventuelle chaîne de détention, etc.).

---

## U02

**Role de l'enonce :** mesure

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

**Reponse a coder, en entier :**

**Analyse juridique et fiscale de l’opération projetée au regard du régime de faveur des articles 210 A et suivants du CGI**

**Objet de la consultation**
Votre groupe familial souhaite séparer ses deux branches d’activité (industrielle et négoce) en apportant la branche industrielle à une société nouvelle, avec remise directe des titres reçus en contrepartie aux associés de la holding apporteuse. Vous sollicitez notre avis sur l’éligibilité de cette opération au régime de faveur des **apports partiels d’actifs (APA)** prévu par les **articles 210 A et suivants du CGI**, notamment au regard des conditions posées par l’**article 210-0 A, I, 4°**.

---

### **1. Rappel des conditions du régime de faveur (article 210 A CGI)**
Pour bénéficier du régime de faveur (report d’imposition des plus-values d’apport), l’opération doit remplir les conditions cumulatives suivantes :
- **Apport d’une branche complète d’activité** (BCA) ou d’un ensemble d’éléments assimilés (art. 210 A, I).
- **Remise de titres représentatifs du capital de la société bénéficiaire** :
  - Soit **à la société apporteuse** (qui les conserve ou les distribue ultérieurement),
  - Soit **directement aux associés de la société apporteuse** (comme dans votre projet).
- **Engagement de conservation des titres reçus** (art. 210 B) et autres obligations déclaratives.

---

### **2. Analyse de votre projet au regard des conditions légales**
#### **a) Apport d’une branche complète d’activité (BCA)**
- **Définition d’une BCA** (art. 210 A, I) :
  Une BCA s’entend d’un **ensemble d’actifs et de passifs** constituant une **unité économique autonome**, capable de fonctionner par ses propres moyens. Elle doit inclure tous les éléments nécessaires à son exploitation (clients, contrats, personnel, immobilisations, etc.).
  - **Vérification à effectuer** :
    - La branche industrielle doit être **autonome** (comptablement et juridiquement) au sein de la holding.
    - Elle doit disposer de ses propres moyens humains, matériels et financiers pour fonctionner indépendamment.
    - **Risque** : Si la branche industrielle partage des ressources (ex : services administratifs, contrats transverses) avec la branche négoce, l’administration fiscale pourrait contester le caractère de BCA.
    - **Recommandation** :
      - **Isoler comptablement** la branche industrielle (comptes séparés, contrats spécifiques).
      - **Documenter** l’autonomie de la branche (organigramme, contrats, effectifs dédiés).

#### **b) Remise directe des titres aux associés de la holding**
- **Condition remplie** :
  L’**article 210-0 A, I, 4°** prévoit expressément que les titres peuvent être remis **directement aux associés** de la société apporteuse (et non à la société elle-même). Votre projet est donc **conforme à la lettre du texte**.
  - **Précision** :
    Cette modalité est souvent utilisée pour **simplifier la séparation des branches** (éviter une distribution ultérieure des titres par la holding).

#### **c) Autres conditions à respecter**
- **Engagement de conservation des titres** (art. 210 B) :
  Les associés recevant les titres de la nouvelle société devront s’engager à les conserver **pendant 3 ans** (sous peine de remise en cause du report d’imposition).
  - **Recommandation** :
    Prévoir une **clause d’engagement de conservation** dans l’acte d’apport et informer les associés de cette obligation.

- **Obligations déclaratives** :
  - **Déclaration spéciale** (formulaire n°2080) à joindre à la déclaration de revenus de la holding.
  - **Mention dans l’acte d’apport** du bénéfice du régime de faveur.

---

### **3. Risques et points de vigilance**
#### **a) Risque de requalification en distribution déguisée**
- L’administration fiscale pourrait contester l’opération si elle estime que la **remise directe des titres aux associés** constitue une **distribution déguisée** de dividendes (soumise à imposition immédiate).
  - **Argumentaire pour sécuriser l’opération** :
    - L’apport est **réalisé à la valeur réelle** (et non à une valeur minorée).
    - La holding **ne conserve aucun actif** lié à la branche industrielle (éviter tout "démembrement" de la BCA).
    - Les associés **ne reçoivent pas un avantage anormal** (la valeur des titres reçus correspond à la valeur de la BCA apportée).

#### **b) Risque de perte du régime de faveur en cas de non-respect des conditions**
- Si l’administration démontre que :
  - La branche industrielle **n’est pas une BCA** (manque d’autonomie),
  - Les titres **ne sont pas conservés 3 ans**,
  - L’apport **masque une distribution**,
  → **Remise en cause du report d’imposition** (imposition immédiate des plus-values latentes).

---

### **4. Recommandations pratiques**
#### **a) Structuration de l’opération**
1. **Évaluation préalable** :
   - Faire réaliser une **évaluation indépendante** de la branche industrielle (par un expert-comptable ou un commissaire aux apports) pour justifier la valeur d’apport.
2. **Acte d’apport** :
   - Rédiger un **projet d’apport** détaillant :
     - La description de la BCA (actifs/passifs transférés),
     - La valeur d’apport et la méthode d’évaluation,
     - L’engagement de conservation des titres (3 ans),
     - La mention expresse du **bénéfice du régime de faveur (art. 210 A CGI)**.
3. **Formalités** :
   - **Dépôt du projet d’apport** au greffe du tribunal de commerce (pour les sociétés par actions).
   - **Publication d’un avis** dans un journal d’annonces légales.
   - **Déclaration fiscale** (formulaire n°2080) dans les délais.

#### **b) Alternatives en cas de risque sur la BCA**
Si l’autonomie de la branche industrielle est contestable, deux options :
1. **Apport à une société existante** (plutôt qu’à une nouvelle société) pour renforcer l’autonomie de la BCA.
2. **Scission partielle** (art. 210-0 A, I, 3° CGI) :
   - La holding est **dissoute** et ses actifs sont répartis entre deux sociétés nouvelles (une pour chaque branche).
   - **Avantage** : La scission est plus difficilement contestable qu’un APA.
   - **Inconvénient** : Plus complexe (liquidation de la holding, formalités accrues).

---

### **5. Conclusion et avis**
**Votre projet est éligible au régime de faveur des articles 210 A et suivants du CGI sous réserve :**
✅ **Que la branche industrielle constitue une BCA** (autonome et complète).
✅ **Que les titres soient remis directement aux associés** (conformément à l’art. 210-0 A, I, 4°).
✅ **Que les associés s’engagent à conserver les titres 3 ans**.
✅ **Que l’apport soit réalisé à la valeur réelle** (sans avantage anormal pour les associés).

**Recommandation finale** :
- **Faire auditer la branche industrielle** par un expert-comptable pour confirmer son autonomie.
- **Rédiger un acte d’apport détaillé** avec mention expresse du régime de faveur.
- **Anticiper les obligations déclaratives** (formulaire n°2080, engagement de conservation).

**En cas de doute sur l’autonomie de la BCA**, une **scission partielle** pourrait être une alternative plus sécurisée.

---
**Prochaines étapes proposées** :
1. **Audit de la branche industrielle** (1 à 2 semaines).
2. **Rédaction du projet d’apport** (avec notre assistance).
3. **Dépôt des formalités** (greffe, publication, déclaration fiscale).

Nous restons à votre disposition pour approfondir tout point spécifique ou vous accompagner dans la mise en œuvre.

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées du cabinet]

---

## U03

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

En tant qu'avocat fiscaliste, je vais analyser cette situation de manière structurée pour déterminer si la distribution envisagée est soumise à une retenue à la source.

## 1. Qualification juridique de la distribution

La distribution de 20 000 000 euros par une société française à sa société mère luxembourgeoise constitue un dividende au sens de l'article 109 du CGI. Nous sommes donc bien dans le champ des "produits visés aux articles 108 à 117 bis" mentionné par l'article 119 bis, 2.

## 2. Champ d'application territorial de la retenue à la source

L'article 119 bis, 2, premier alinéa soumet à retenue à la source les distributions dont les bénéficiaires effectifs n'ont pas leur siège en France. La société mère étant une société anonyme luxembourgeoise ayant son siège au Luxembourg, elle entre a priori dans le champ de cette retenue.

## 3. Examen de l'exception prévue pour les organismes de placement collectif (OPC)

L'article mentionne une exception pour "les organismes de placement collectif constitués sur le fondement d'un droit étranger" situés dans un État membre de l'UE et remplissant certaines conditions.

Votre cliente est une société anonyme luxembourgeoise détenant 100 % du capital de la filiale française depuis cinq ans. **Il ne s'agit pas d'un OPC étranger** mais d'une société commerciale classique. Par conséquent, cette exception ne s'applique pas.

## 4. Application du régime mère-fille prévu par la directive européenne

Bien que non visé par l'extrait que vous m'avez communiqué, il est indispensable d'examiner l'application de l'article 119 ter du CGI, qui transpose la directive "mère-fille" (directive 2011/96/UE) :

**Conditions requises par l'article 119 ter :**
- La société mère doit détenir au moins 5 % du capital de la filiale (ou une participation d'au moins 2,5 M€ selon l'option) : **condition remplie** (détention à 100 %)
- La détention doit être continue depuis au moins 2 ans à la date de mise en paiement : **condition remplie** (détention depuis 5 ans)
- La société mère doit être soumise à l'impôt sur les sociétés dans un État membre de l'UE : **condition remplie** (société luxembourgeoise soumise à l'IS luxembourgeois)
- La société mère doit revêtir l'une des formes énumérées à l'annexe de la directive (dont la société anonyme fait partie) : **condition remplie**

## 5. Conclusion

**Aucune retenue à la source ne devrait être due en application de l'article 119 ter du CGI.**

Je tiens cependant à souligner trois points de vigilance :

1. **La société mère doit être le "bénéficiaire effectif"** des dividendes au sens de l'article 119 ter. Si elle agissait comme une entité relais pour le compte de tiers situés hors UE, le régime de faveur pourrait être remis en cause (arrêt de la CJUE, affaires "Danish cases").

2. **La preuve de la détention continue** depuis deux ans doit pouvoir être rapportée (extrait K-bis, statuts, registre des mouvements de titres).

3. **Une déclaration de la société mère** attestant qu'elle remplit les conditions de l'article 119 ter devra être fournie à l'administration fiscale française, selon les modalités prévues par la doctrine administrative (BOI-RPPM-RCM-30-30-20-10).

En l'état des informations fournies et sous réserve de la vérification de ces points, la distribution de 20 000 000 euros le 15 juin 2025 pourra être effectuée sans retenue à la source.

---

## U04

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

**Avis – maintien du report d’imposition de l’apport-cession**

La cession par la holding, en février 2026, des titres apportés moins de trois ans auparavant constitue, en principe, un événement mettant fin au report d’imposition dont vous bénéficiez personnellement au titre de l’apport.

Le report peut toutefois être maintenu si la holding respecte le mécanisme de réinvestissement prévu par l’article 150-0 B ter, I, 2° du CGI.

## 1. Montant minimal à réinvestir

Le produit de cession encaissé s’élève à :

- **9 000 000 €**

La holding doit en réinvestir au moins **70 %**, soit :

- **6 300 000 € minimum**

Les **2 700 000 € restants** ne sont pas soumis à l’obligation de réinvestissement au titre du texte cité. Ils peuvent donc, en principe, demeurer disponibles dans la holding, sous réserve des autres conséquences fiscales et juridiques d’une éventuelle distribution ou utilisation.

Par prudence, le calcul doit être réalisé sur le **produit brut de cession** retenu juridiquement, et non sur la somme restant après frais, remboursement d’une dette, séquestre, complément de prix éventuel ou autres prélèvements. Il conviendra de relire l’acte de cession afin de déterminer exactement l’assiette du seuil de 70 %.

## 2. Délai

Le réinvestissement doit intervenir dans les **trois ans de la cession**, décomptés de date à date.

Si la cession a eu lieu, par exemple, le **15 février 2026**, le montant minimal de 6 300 000 € devra avoir été effectivement investi au plus tard le **15 février 2029**.

Il ne faut toutefois pas attendre l’échéance : le texte impose à la holding de **prendre l’engagement de réinvestir**. Cet engagement doit être formalisé et les obligations déclaratives propres à l’apport-cession doivent être respectées.

Je recommande donc une mise en œuvre immédiate, même si les acquisitions ou investissements sont échelonnés.

## 3. Nature des réinvestissements : attention aux actifs éligibles

Sur le fondement du seul a) du texte qui vous est communiqué, le réinvestissement doit financer des **moyens permanents d’exploitation** affectés à une activité opérationnelle éligible : activité commerciale, industrielle, artisanale, agricole ou libérale, à l’exclusion notamment de la gestion de son propre patrimoine immobilier.

Concrètement, peuvent notamment relever de cette logique, sous réserve de leur affectation réelle à une activité éligible :

- matériels industriels et équipements de production ;
- véhicules, outils, machines, installations techniques ;
- logiciels, matériels informatiques, équipements professionnels ;
- droits incorporels nécessaires à l’exploitation ;
- agencements et équipements durables ;
- actifs nécessaires au lancement ou au développement d’une activité opérationnelle réellement exercée par la holding ou par une structure entrant dans le cadre légal applicable.

En revanche, ne doivent pas être présentés comme un réinvestissement éligible au titre de cette seule disposition :

- le maintien des fonds sur des comptes bancaires, comptes à terme ou placements de trésorerie ;
- l’achat de titres cotés ou d’OPCVM à titre de placement ;
- l’acquisition d’un portefeuille financier passif ;
- la constitution d’une trésorerie sans emploi opérationnel ;
- l’acquisition ou la détention d’immeubles dans une logique de gestion patrimoniale ou locative propre.

L’immobilier appelle une vigilance particulière : un immeuble utilisé de façon effective pour les besoins d’une activité opérationnelle peut soulever une analyse différente d’un immeuble détenu pour être loué ou valorisé patrimonialement. Il faudra donc examiner le projet précis, sa substance économique et l’activité réellement exercée.

## 4. Recommandation pratique

Je conseille de procéder en quatre temps.

### A. Sécuriser immédiatement l’engagement

Faire adopter par l’organe compétent de la holding une décision formalisée :

- rappelant la cession intervenue en février 2026 ;
- constatant le produit de 9 000 000 € ;
- prenant l’engagement de réinvestir au moins 6 300 000 € ;
- fixant l’échéance exacte du délai de trois ans ;
- identifiant les catégories de projets opérationnels envisagés ;
- interdisant toute utilisation des sommes susceptible de compromettre la capacité de réinvestissement.

Il est préférable d’isoler comptablement et, si possible, bancairment, les sommes destinées au réinvestissement.

### B. Construire un calendrier de réinvestissement

Il convient d’établir un plan d’investissement réaliste, avec un objectif de réalisation sensiblement antérieur à février 2029.

Par exemple :

- 2026 : sélection des projets et premières acquisitions ;
- 2027-2028 : réalisation de l’essentiel des investissements ;
- avant l’échéance de février 2029 : vérification que le seuil de 6 300 000 € est atteint sur des dépenses éligibles et effectivement réalisées.

Le simple fait d’avoir signé une lettre d’intention, engagé des discussions ou prévu un investissement ne suffit pas nécessairement : il faut pouvoir démontrer la réalisation effective de l’investissement dans le délai.

### C. Ne pas confondre investissement opérationnel et placement patrimonial

La holding ne doit pas se contenter de placer les 6,3 M€ en attente sur des supports financiers ou immobiliers passifs. Cela ne répondrait pas, en lui-même, à l’exigence de financement de moyens permanents d’exploitation prévue par le texte cité.

Si le projet consiste en la reprise d’une autre société, une souscription au capital d’une société opérationnelle ou l’investissement par l’intermédiaire d’un véhicule, il faudra examiner les autres modalités éventuellement prévues par l’article 150-0 B ter dans sa version complète. Ces opérations ne doivent pas être mises en œuvre sur la seule base du a) reproduit dans votre question.

### D. Organiser la preuve

Pour chaque investissement, il faudra conserver :

- les décisions sociales ;
- les contrats, factures et actes d’acquisition ;
- les preuves de paiement ;
- les justificatifs de l’affectation à l’activité opérationnelle ;
- les documents démontrant la nature de l’activité exercée ;
- les déclarations fiscales relatives au report et à la cession.

En cas de contrôle, l’administration examinera non seulement les montants, mais aussi la réalité économique et l’affectation opérationnelle des actifs financés.

## 5. Risque en cas de non-respect

Si la holding ne prend pas l’engagement requis, n’investit pas au moins 6 300 000 € dans le délai, ou réalise des investissements ne répondant pas aux conditions légales, le report d’imposition peut prendre fin.

La plus-value d’apport initialement placée en report deviendrait alors imposable entre vos mains, indépendamment de la fiscalité éventuellement due par la holding sur sa propre cession des titres.

Il y a donc bien deux sujets fiscaux distincts :

1. la fiscalité de la holding sur la vente des titres apportés ;
2. votre report personnel d’imposition sur la plus-value d’apport, dont le maintien dépend du réinvestissement.

## Conclusion

La recommandation immédiate est la suivante :

- **formaliser sans délai l’engagement de réinvestir** ;
- réserver au minimum **6 300 000 €** ;
- les affecter, avant l’expiration du délai de trois ans courant à compter de février 2026, à des **moyens permanents d’exploitation liés à une activité opérationnelle éligible** ;
- éviter tout placement financier ou immobilier patrimonial présenté artificiellement comme un réinvestissement ;
- valider, avant signature, l’éligibilité fiscale de chaque opération envisagée.

Avant toute décision d’investissement, il conviendra de reprendre la date exacte de l’apport, la date exacte de la cession, l’acte de cession et l’ensemble de l’article 150-0 B ter applicable à l’opération, afin de sécuriser les modalités de réinvestissement adaptées au projet retenu.

---

## U05

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

Maître, Cher Client,

Je vous remercie de me consulter sur ce dossier de transmission à titre gratuit. La question que vous posez est centrale et nécessite une analyse rigoureuse de la nature de l'activité de votre société par actions simplifiée (SAS) au regard des conditions d'éligibilité du dispositif dit "Dutreil" (article 787 B du CGI).

Voici mon analyse quant à l'application de l'exonération partielle de 75 % pour la donation envisagée le 5 octobre 2023.

### 1. Sur le respect des conditions formelles et temporelles du dispositif

S'agissant des conditions liées à l'engagement de conservation et à la direction, les éléments que vous m'avez fournis remplissent les critères exigés par les textes :

*   **L'engagement collectif de conservation (ECC) :** Il a été signé le 3 mars 2021 et porte sur la totalité des titres. La donation intervenant le 5 octobre 2023, la condition de conservation d'au moins deux ans avant la transmission est respectée.
*   **L'engagement individuel de conservation :** La prise d'engagement par les deux enfants, pour une durée de 4 ans à compter de la donation, est conforme aux exigences de l'article 787 B.
*   **La fonction de direction :** Le fait que le dirigeant (donateur) conserve la présidence de la SAS pendant trois ans à compter de la donation satisfait à la condition d'exercice effectif d'une fonction de direction.

Sur le plan purement procédural, le montage est donc parfaitement validé.

### 2. Sur la condition substantielle : l'éligibilité de l'activité (Le point de blocage)

L'article 787 B du CGI exige que la société ait une "activité industrielle, commerciale, artisanale, agricole ou libérale". 

Bien que la location meublée soit fiscalement assimilée à une activité commerciale (BIC) en droit fiscal général, l'administration fiscale a une interprétation très stricte de cette condition pour l'application du pacte Dutreil. 

Selon la doctrine administrative (BOI-ENR-PT-30-20-10), l'activité de location meublée ne peut être regardée comme une activité éligible que si elle revêt un véritable **caractère commercial**. L'administration exclut de ce dispositif les activités qui relèvent de la simple gestion d'un patrimoine privé.

Pour que la location de vos 40 appartements meublés soit éligible, il faudrait démontrer que la SAS fournit, en plus de la mise à disposition du logement, des prestations para-hôtelières significatives (comparable à un service hôtelier). Sont notamment exigées au moins trois des quatre prestations suivantes :
*   Le petit-déjeuner ;
*   Le nettoyage régulier des locaux ;
*   La fourniture du linge de maison ;
*   La réception de la clientèle avec un service de conciergerie ou de gardiennage.

Si la SAS se contente de louer des appartements meublés avec une gestion locative classique (encaissement des loyers, entretien courant, éventuellement via un simple mandataire immobilier), l'administration fiscale requalifiera cette activité en "gestion de patrimoine privé". 

### Conclusion et préconisations

À la lecture des éléments actuels, **l'exonération partielle de 75 % de l'article 787 B du CGI n'est malheureusement pas applicable**, sauf à démontrer que la SAS exerce une activité de location meublée avec des services para-hôtelières substantiels, ce qui semble peu probable au vu de la simple détention de 40 appartements meublés.

En l'absence d'éligibilité au régime Dutreil, la donation de la pleine propriété des titres d'une valeur de 20 000 000 euros sera soumise aux droits de mutation à titre gratuit dans les conditions de droit commun (après abattement de 100 000 € par enfant), soit une fiscalité très lourde (taux marginaux de 35 % puis 45 %).

**Je vous recommande donc les actions suivantes avant la signature du 5 octobre 2023 :**

1.  **Audit de l'activité :** Nous devons vérifier précisément les contrats de location et les prestations offertes par la SAS pour confirmer ou non l'absence de caractère para-hôtelier.
2.  **Réflexion sur la structuration :** Si l'activité n'est pas éligible, il convient d'étudier des alternatives pour optimiser la transmission (donation en nue-propriété avec réserve d'usufruit pour réduire l'assiette, apport des titres à une holding si une activité commerciale éligible peut être greffée, etc.), bien que cela nécessite de repousser l'acte du 5 octobre.

Je reste à votre entière disposition, Maître, pour en débattre et ajuster notre stratégie en fonction du degré de service offert par la SAS à ses locataires.

Bien cordialement,

**[Votre Nom]**
*Avocat fiscaliste*

---

## U06

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

**OBJET : Consultation fiscale – Application du taux de TVA à 5,5 % sur installation de chaudière (facture du 15/04/2025)**

Monsieur le Gérant,

Je vous remercie de m’avoir soumis ce dossier. Vous trouverez ci-dessous mon analyse juridique, les conséquences fiscales et la stratégie à adopter face à la proposition de rectification.

---

### 🔍 1. Analyse juridique des conditions d’application du taux réduit

L’article 278-0 bis A du CGI pose, en son I, trois conditions cumulatives pour bénéficier du taux réduit de 5,5 % sur les prestations de rénovation énergétique :
1. **Local achevé depuis au moins 2 ans** → ✅ Votre chantier porte sur une maison de 15 ans.
2. **Usage d’habitation** → ✅ Le local est occupé par son propriétaire.
3. **Travaux portant sur l’amélioration du chauffage** → ✅ L’installation d’une chaudière entre dans le champ du 3° b).

**En apparence, le taux de 5,5 % semble donc justifié.**

Cependant, le **III bis** du même article prévoit une **dérogation expresse** :
> *« Par dérogation au I du présent article, le taux prévu à l'article 278 s'applique aux prestations de rénovation énergétique comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles. »*

L’article 278 CGI fixe le **taux normal de TVA à 20 %**. Cette disposition a pour effet de **priver du taux réduit toute installation de chaudière fonctionnant (ou pouvant fonctionner) avec un combustible fossile** (gaz naturel, fioul, charbon, GPL, etc.), y compris les chaudières à condensation gaz.

---

### ⚖️ 2. Le critère décisif : la nature exacte de la chaudière installée

La réponse à votre question dépend exclusivement de la **technologie et du combustible** de l’équipement facturé :

| Type de chaudière | Taux applicable | Fondement |
|-------------------|----------------|-----------|
| Gaz, fioul, charbon, GPL (y compris condensation) | **20 %** | Art. 278-0 bis A, III bis CGI |
| Pompe à chaleur (air/eau, sol/eau, géothermie) | **5,5 %** | III bis inapplicable (pas de combustible fossile) |
| Biomasse (bois, granulés) / Solaire thermique / Hybride éligible | **5,5 %** | III bis inapplicable |

👉 **Si la chaudière est à combustible fossile**, l’administration est **fondée** à réclamer le rappel au taux de 20 %.  
👉 **Si la chaudière est éligible** (PAC, biomasse, solaire, etc.), votre application du taux de 5,5 % est **correcte** et la rectification doit être contestée.

---

### 📉 3. Conséquences financières (si le taux de 20 % s’applique)

- **Rappel de TVA** : `(20 % – 5,5 %) × 8 500 € HT = 1 232,50 €`
- **Intérêts de retard** : calculés au taux légal en vigueur à la date d’exigibilité (0,20 %/mois en 2025)
- **Pénalités** : 40 % en cas de manquement délibéré ou 80 % en cas de manœuvres frauduleuses. En l’absence de ces éléments, la pénalité de 10 % pour erreur de bonne foi peut s’appliquer, sous réserve de régularisation.

---

### 🛡️ 4. Stratégie et recommandations procédurales

1. **Vérifiez immédiatement la fiche technique et la facture fournisseur** de la chaudière. Identifiez le combustible principal et la référence exacte.
2. **Répondez à la proposition de rectification dans le délai de 30 jours** (art. L. 57 du LPF). Le silence vaut acceptation.
3. **Deux scénarios** :
   - ✅ **Si chaudière éligible** : Joignez à votre réponse la fiche technique, l’attestation RGE, la facture d’achat, et citez le III bis *a contrario*. Demandez l’annulation de la rectification.
   - ⚠️ **Si chaudière à combustible fossile** : 
     - Régularisez spontanément le rappel de TVA.
     - Sollicitez une **remise gracieuse des pénalités** (art. L. 247 du LPF) en invoquant la bonne foi, la complexité du dispositif, l’absence de précédent contentieux et la correction spontanée.
     - Vérifiez si une **attestation de taux réduit** (Cerfa n°12810) avait été correctement renseignée et conservée. Son absence ou son inexactitude aggrave le risque de pénalités.

4. **Documentation à conserver** : devis, facture, attestation du client, fiche technique, preuve de l’ancienneté du logement, justificatif RGE, échange avec le fournisseur.

---

### 📝 Conclusion

Le taux de 5,5 % n’était **correct que si la chaudière installée n’est pas susceptible d’utiliser un combustible fossile**. Dans le cas contraire, le III bis de l’article 278-0 bis A CGI impose le taux de 20 %, et l’administration est fondée.

Je vous invite à me transmettre **dès que possible** la référence exacte de la chaudière, sa fiche technique et la copie de l’attestation de taux réduit. Sur cette base, je rédigerai la réponse à l’administration, soit pour contester la rectification, soit pour négocier la régularisation et la remise des pénalités.

Je reste à votre disposition pour un échange téléphonique ou un rendez-vous en cabinet afin de finaliser la stratégie de réponse.

Veuillez agréer, Monsieur le Gérant, l’expression de mes salutations distinguées.

**[Votre Nom]**  
Avocat au Barreau de [Ville]  
Spécialiste en droit fiscal des entreprises

---

## U07

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus a la societe
apporteuse.

Le projet d'apport a ete depose au greffe du tribunal de commerce
le 10 novembre 2022.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder, en entier :**

**MÉMORANDUM FISCAL**

**À l'attention de :** [Nom du Groupe Familial / Représentants]
**Objet :** Éligibilité de votre projet de restructuration au régime de faveur des fusions (Art. 210 A et suivants du CGI) et réalisation de vos objectifs de séparation.

Madame, Monsieur,

Vous m'avez consulté concernant le projet de restructuration de votre groupe familial. 

Il ressort de votre exposé que votre société holding, qui détient actuellement deux branches d'activité (industrielle et négoce), a déposé un projet d'apport au greffe le 10 novembre 2022. Ce projet prévoit l'apport de la branche industrielle à une société nouvelle, moyennant la remise des titres de cette dernière **à la société apporteuse** (la holding). Votre objectif final est de permettre aux deux branches de la famille de se séparer.

Vous vous interrogez sur l'éligibilité de cette opération au régime de faveur prévu par les articles 210 A et suivants du Code Général des Impôts (CGI).

Voici mon analyse de votre dossier.

### 1. Sur l'éligibilité de l'opération au régime de faveur (Art. 210 A et s. du CGI)

À la lecture stricte du projet que vous avez déposé et du texte applicable (CGI, art. 210-0 A, I, 4°), l'opération que vous décrivez est juridiquement qualifiée d'**apport partiel d'actif (APA)**. 

En effet, la holding apporte une partie de son activité à une autre société et reçoit en échange les titres de la société bénéficiaire.

**La réponse à votre question est OUI** : cette opération peut bénéficier du régime de faveur (qui permet une neutralité fiscale, c'est-à-dire l'absence d'imposition immédiate des plus-values latentes sur les actifs apportés), **sous réserve de respecter deux conditions cumulatives majeures** :

1.  **La condition tenant à l'objet de l'apport (La Branche Complète d'Activité - BCA) :** 
    Pour que le régime de faveur s'applique de plein droit (sans avoir à demander un agrément préalable à l'Administration fiscale), la branche industrielle apportée doit constituer une "branche complète d'activité". Sur le plan fiscal, cela signifie qu'elle doit constituer un ensemble capable de fonctionner par ses propres moyens (personnel, matériel, clientèle, etc.).
2.  **La condition tenant à l'engagement de conservation (Art. 210 B du CGI) :**
    La société apporteuse (votre holding) devra prendre l'engagement, dans l'acte d'apport, de conserver les titres de la société nouvelle reçus en échange pendant au moins **trois ans**.

### 2. Point d'alerte majeur : L'inadéquation de ce schéma avec votre objectif de séparation

En tant que votre conseil, il est de mon devoir d'attirer votre attention sur un point fondamental : **l'opération telle qu'elle est rédigée dans le projet déposé le 10 novembre 2022 ne permet pas, à elle seule, de séparer les deux branches de la famille.**

En effet, si la holding reçoit et conserve les titres de la société nouvelle (comme l'exige le schéma classique de l'APA), les deux branches de la famille resteront associées au sein de la holding. La holding détiendra simplement la branche négoce en direct, et la branche industrielle via sa nouvelle filiale. La famille ne sera donc pas séparée.

### 3. La solution recommandée : L'Apport-Attribution (ou Scission)

Pour atteindre votre objectif de séparation familiale tout en maintenant la neutralité fiscale, l'apport partiel d'actif doit être suivi (ou accompagné) d'une seconde étape : **l'attribution des titres reçus aux associés**. 

Concrètement, la holding doit distribuer les titres de la société nouvelle à la branche de la famille qui souhaite reprendre l'activité industrielle, en échange de l'annulation de leurs titres dans la holding (réduction de capital). 

Cette opération globale (souvent appelée "apport-attribution" ou "scission partielle") bénéficie également d'un cadre fiscal très favorable, mais les conditions sont plus strictes :
*   **Neutralité pour les associés (Art. 115-2 du CGI) :** Pour que la distribution des titres ne soit pas lourdement taxée comme un dividende entre les mains des membres de la famille, il faut impérativement que la branche apportée (l'industrie) **ET** la branche conservée par la holding (le négoce) constituent toutes deux des Branches Complètes d'Activité (BCA).
*   **Levée de l'obligation de conservation :** Si cette attribution est réalisée proportionnellement ou dans le cadre d'une séparation justifiée, la holding est dispensée de son obligation de conserver les titres pendant 3 ans. En revanche, ce sont les associés (les membres de la famille) qui devront s'engager à conserver les titres reçus pendant 3 ans.

### Conclusion et prochaines étapes

Votre projet d'apport déposé le 10 novembre 2022 est une excellente première étape et **est parfaitement éligible au régime de faveur des articles 210 A et suivants du CGI**, à condition que l'activité industrielle soit autonome (BCA).

Cependant, pour finaliser la séparation de la famille sans déclencher un frottement fiscal prohibitif, nous devons nous assurer que :
1.  Le traité d'apport contient bien les mentions fiscales obligatoires (engagements de l'article 210 B).
2.  L'activité de négoce qui restera dans la holding est également une BCA autonome.
3.  Les assemblées générales extraordinaires (AGE) qui vont approuver cet apport prévoient également la réduction de capital et l'attribution des titres aux membres de la famille concernés, sous le bénéfice de l'article 115-2 du CGI.

Je me tiens à votre entière disposition pour revoir le projet de traité d'apport déposé au greffe et préparer avec vous les résolutions d'assemblée générale nécessaires à la réussite de votre séparation.

Bien à vous,

**Votre Avocat Fiscaliste**

---

## U08

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

**OBJET :** Consultation fiscale – Applicabilité de l’exonération partielle de l’article 787 B du CGI à une donation de titres de SAS détenant un parc de locations meublées.

**DESTINATAIRES :** Monsieur le Dirigeant, Maître le Notaire

---

### 1. RÉPONSE DIRECTE
En l’état des éléments communiqués, **l’exonération partielle de 75 % prévue à l’article 787 B du CGI est en principe applicable**, sous réserve de la vérification formelle de deux conditions cumulatives non explicitement confirmées dans votre exposé : 
- la durée d’exercice d’une fonction de direction par le donateur **avant** la donation (minimum 2 ans) ;
- la qualification commerciale effective et prépondérante de l’activité de la SAS.

Si ces deux points sont établis, la donation du 5 octobre 2023 bénéficiera de l’exonération sur 75 % de la valeur des titres, soit 15 000 000 € sur 20 000 000 €.

---

### 2. ANALYSE DES CONDITIONS DE L’ARTICLE 787 B DU CGI

L’exonération partielle est subordonnée au respect cumulatif des conditions suivantes :

#### a) Activité éligible
La société doit exercer une activité **industrielle, commerciale, artisanale, agricole ou libérale**. 
- La location meublée est fiscalement qualifiée d’activité commerciale (BIC), qu’elle relève du régime LMP ou LMNP. 
- **Point de vigilance :** L’administration fiscale peut contester l’éligibilité si l’activité est jugée purement patrimoniale ou si la location meublée n’est pas l’activité prépondérante de la SAS (seuil de 50 % du chiffre d’affaires ou de la valeur des actifs). Il conviendra de vérifier l’objet social, les liasses fiscales récentes et l’absence d’actifs ou de revenus étrangers à cette activité.

#### b) Engagement collectif de conservation
- **Durée minimale :** 2 ans. Signé le 3 mars 2021, il est en cours au 5 octobre 2023 (2 ans et 7 mois). ✅ Condition remplie.
- **Portée :** Doit couvrir au moins 34 % des droits financiers et de vote (17 % si société cotée). Votre engagement porte sur 100 %. ✅ Condition remplie.
- **Formalités :** L’engagement doit avoir été enregistré et conservé. Il doit être joint à la déclaration de donation.

#### c) Engagement individuel des donataires
- Chaque enfant doit souscrire un engagement de conservation des titres reçus pour **6 ans à compter de la donation**. 
- Cet engagement doit être **expressément stipulé dans l’acte de donation** et produit à l’administration. ✅ Condition remplie sous réserve de rédaction conforme.

#### d) Condition de direction ou d’emploi
L’article 787 B, 2° du CGI exige que :
1. Le donateur (ou l’un des co-signataires de l’engagement collectif) ait exercé une **fonction de direction** dans la société pendant **au moins 2 ans avant la transmission** ;
2. Il **continue d’exercer** une fonction de direction ou soit salarié de la société pendant **au moins 3 ans après la transmission**.

- Vous conservez la présidence pendant 3 ans post-donation. ✅ Condition post-transfert remplie.
- ⚠️ **Condition pré-transfert à vérifier :** Vous devez justifier d’une fonction de direction effective (président, directeur général, gérant, etc.) exercée sans interruption pendant les 24 mois précédant le 5 octobre 2023. Cette condition est substantielle ; son non-respect entraîne la perte de l’exonération.

#### e) Autres exigences formelles
- La donation doit être enregistrée dans les délais légaux.
- Les engagements (collectif et individuels) doivent être annexés à la déclaration n°2735.
- Toute cession, donation ou transmission anticipée des titres avant l’expiration des engagements entraîne un rappel des droits exonérés, majorés des intérêts de retard.

---

### 3. POINTS DE VIGILANCE ET RECOMMANDATIONS OPÉRATIONNELLES

| Point | Risque | Recommandation |
|-------|--------|----------------|
| **Qualification de l’activité** | Requalification en gestion de patrimoine civil | Joindre à la déclaration les 3 derniers bilans, l’objet social, et une attestation du commissaire aux comptes ou de l’expert-comptable confirmant le caractère commercial prépondérant. |
| **Fonction de direction préexistante** | Perte totale de l’exonération si < 2 ans avant le 5/10/2023 | Vérifier les PV d’assemblées, statuts, et justificatifs de rémunération/dirigeant depuis au moins octobre 2021. |
| **Rédaction de l’acte** | Nullité ou inefficacité fiscale des engagements | Insérer des clauses expresses reprenant les termes légaux des engagements collectif et individuels, avec mention des durées et des sanctions en cas de manquement. |
| **Conservation des titres** | Rappel fiscal en cas de cession anticipée | Prévoir un pacte d’actionnaires ou des clauses statutaires limitant la cessibilité pendant 6 ans, et informer les enfants des obligations de conservation. |

---

### 4. CONCLUSION

Sous réserve de la confirmation écrite que vous avez exercé une fonction de direction dans la SAS pendant au moins deux ans avant le 5 octobre 2023, et que l’activité de location meublée constitue bien l’activité commerciale prépondérante de la société, **l’exonération partielle de 75 % de l’article 787 B du CGI est applicable**.

La base taxable aux droits de mutation à titre gratuit sera donc de **5 000 000 €**, à répartir entre les deux enfants (2 500 000 € chacun), après application des abattements directs ligne (100 000 € par enfant) et du barème progressif.

Je reste à votre disposition, ainsi qu’à celle de Maître le Notaire, pour :
- rédiger ou valider les clauses fiscales de l’acte de donation ;
- préparer le dossier de déclaration n°2735 et les engagements annexes ;
- accompagner les formalités de conservation et le suivi post-donation.

Veuillez agréer, Monsieur, Maître, l’expression de mes salutations distinguées.

**[Votre Nom]**  
Avocat au Barreau de [Ville]  
Spécialiste en droit fiscal et patrimonial  
[Coordonnées]

---

## U09

**Role de l'enonce :** mesure

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

**Reponse a coder, en entier :**

## Conclusion

**Oui, en principe.** L’opération envisagée relève de la catégorie des **apports partiels d’actif avec attribution directe des titres aux associés de la société apporteuse** (« apport-attribution »), expressément visée par l’article 210-0 A, I, 4° du CGI.

Le fait que les titres de la société nouvelle ne soient pas remis à la holding apporteuse, mais directement à ses associés, **ne fait donc pas obstacle**, par lui-même, au bénéfice du régime spécial des fusions prévu aux articles 210 A et 210 B du CGI.

Cette conclusion est toutefois subordonnée au respect des conditions de fond, de forme et de substance économique du régime.

---

## 1. L’opération entre bien dans le champ d’un apport partiel d’actif éligible

L’article 210-0 A, I, 4° vise explicitement les apports partiels d’actif par lesquels une société apporte, sans dissolution :

- une ou plusieurs **branches complètes d’activité** ;
- à une ou plusieurs sociétés bénéficiaires ;
- en contrepartie de titres de la société bénéficiaire ;
- remis soit à la société apporteuse, **soit directement aux associés de cette dernière**.

Le schéma décrit correspond donc, en principe, au texte :

1. la holding conserve son existence et l’activité de négoce ;
2. elle apporte l’activité industrielle à une société nouvelle ;
3. les titres de la société nouvelle sont attribués directement aux associés de la holding.

Il ne s’agit pas nécessairement d’une scission complète : la holding conserve une activité autonome, celle de négoce. C’est précisément l’hypothèse d’un apport partiel d’actif.

---

## 2. Condition essentielle : l’activité industrielle doit constituer une branche complète d’activité

Le régime de l’article 210 B suppose que l’apport porte sur une **branche complète d’activité**.

Cela signifie que l’ensemble apporté doit constituer une exploitation autonome, susceptible de fonctionner par ses propres moyens chez la société bénéficiaire immédiatement après l’apport.

Devraient donc notamment être transférés à la société nouvelle, selon le cas :

- les immobilisations industrielles ;
- les stocks afférents ;
- les contrats clients et fournisseurs ;
- les contrats de travail des salariés affectés à l’activité ;
- les autorisations administratives, licences et assurances transférables ;
- les créances et dettes propres à la branche ;
- les moyens de financement nécessaires à l’exploitation ;
- les éléments incorporels : marque, savoir-faire, fichiers clients, logiciels, etc.

Une simple mise à disposition de certains actifs, ou le transfert isolé de titres, d’immeubles ou de matériels, ne suffirait pas si la société nouvelle ne pouvait pas exercer de manière autonome l’activité industrielle.

Une revue préalable des actifs, passifs, contrats et fonctions affectés à chacune des activités est donc indispensable.

---

## 3. Application des articles 210 A et 210 B

Sous réserve que la société bénéficiaire soit soumise à l’IS ou à un impôt équivalent et que les autres conditions soient satisfaites, l’apport d’une branche complète d’activité peut être placé, sur option, sous le régime de l’article 210 B du CGI, lequel renvoie au régime de faveur de l’article 210 A.

Les conséquences principales sont les suivantes.

### Pour la société apporteuse

Les plus-values latentes afférentes aux actifs apportés ne sont, en principe, pas immédiatement imposées.

La neutralité est toutefois conditionnée au respect du régime et aux engagements pris par la société bénéficiaire.

### Pour la société bénéficiaire

La société nouvelle devra notamment reprendre les éléments apportés selon les valeurs fiscales appropriées et respecter les engagements prévus par l’article 210 A, notamment en matière :

- de reprise des provisions ;
- de réintégration des plus-values afférentes à certains biens amortissables ;
- de calcul ultérieur des plus-values à partir des valeurs fiscales historiques lorsque cela est requis.

### Pour les associés

L’attribution directe des titres de la société bénéficiaire aux associés de l’apporteuse n’est pas, en elle-même, assimilée à une distribution taxable lorsque l’apport est régulièrement placé sous le régime de l’article 210 B.

C’est l’objet de l’article 115, 2 du CGI, qui neutralise, sous conditions, l’attribution aux associés des titres représentatifs de l’apport partiel d’actif.

La fiscalité propre des associés devra néanmoins être vérifiée selon leur statut :

- personnes physiques résidentes ;
- sociétés soumises à l’IS ;
- associés non-résidents ;
- éventuels démembrements de propriété ;
- pactes Dutreil, engagements de conservation ou autres régimes particuliers.

---

## 4. Point de vigilance majeur : l’attribution des titres entre les deux branches familiales

Le texte autorise la remise directe des titres « aux associés de la société apporteuse ». Il permet donc l’apport-attribution.

Toutefois, le projet familial doit être précisé.

### Hypothèse 1 : attribution proportionnelle à tous les associés

Si chaque associé de la holding reçoit des titres de la société industrielle nouvelle proportionnellement à sa participation actuelle dans la holding, l’opération est la plus classique.

Mais, dans cette hypothèse, chaque membre de la famille détiendra encore, indirectement ou directement :

- une participation dans l’activité de négoce via la holding ;
- une participation dans l’activité industrielle via la société nouvelle.

Elle ne réalise donc pas, à elle seule, une séparation capitalistique entre les deux branches familiales.

### Hypothèse 2 : attribution de la société industrielle à une seule branche familiale

Si l’objectif est que :

- la branche familiale A détienne exclusivement la société industrielle ;
- la branche familiale B conserve exclusivement la holding et l’activité de négoce,

l’opération devient plus sensible.

Il convient alors d’organiser juridiquement et fiscalement l’attribution différenciée des titres : réduction de capital, annulation ou échange de titres de la holding, éventuelles soultes, réorganisation préalable de l’actionnariat, etc.

Le texte de l’article 210-0 A ne pose pas, à lui seul, une règle expresse de répartition proportionnelle. Néanmoins, une attribution non proportionnelle ou réservée à certains associés appelle une analyse renforcée :

- respect de l’égalité entre associés et du droit des sociétés ;
- détermination de la contrepartie économique pour les associés ne recevant pas les titres de la société industrielle ;
- absence de libéralité ou d’avantage occulte ;
- traitement fiscal des éventuelles annulations, rachats, échanges ou soultes ;
- risque de remise en cause de la neutralité si l’opération est, en réalité, analysée comme une distribution, un rachat de titres ou une cession déguisée.

En pratique, pour une séparation asymétrique entre deux groupes familiaux, il est fréquent de devoir combiner l’apport-attribution avec une opération sur le capital ou une réorganisation des titres. Cette seconde étape doit être étudiée séparément : elle ne bénéficie pas automatiquement du régime de l’article 210 B du seul fait que l’apport y est éligible.

---

## 5. Substance économique et clause anti-abus

Le régime spécial peut être écarté lorsque l’opération a comme objectif principal, ou l’un de ses objectifs principaux, la fraude ou l’évasion fiscales et n’est pas justifiée par des motifs économiques valables.

En l’espèce, la volonté de séparer deux activités distinctes et deux branches familiales constitue, en principe, un **motif économique et patrimonial sérieux**, à condition qu’il soit réel et documenté :

- divergences de stratégie industrielle et commerciale ;
- autonomie des équipes dirigeantes ;
- besoins de financement distincts ;
- prévention des conflits de gouvernance ;
- clarification de la transmission familiale ;
- séparation des risques économiques.

Il conviendra de faire figurer ces motifs dans la documentation sociale, le traité d’apport, les rapports des organes de direction et, le cas échéant, le protocole familial.

---

## 6. Formalités à prévoir

Le bénéfice du régime exige notamment :

- un traité d’apport précisément rédigé ;
- l’identification exhaustive de la branche complète apportée ;
- les décisions sociales nécessaires ;
- l’intervention éventuelle d’un commissaire aux apports ;
- l’exercice de l’option pour le régime de l’article 210 B ;
- le respect des engagements de la société bénéficiaire ;
- les déclarations fiscales spécifiques, notamment celles prévues à l’article 54 septies du CGI ;
- une documentation de la justification économique de l’opération.

---

## Avis

L’apport de l’activité industrielle à une société nouvelle, avec remise directe des titres de cette société aux associés de la holding, **peut relever du régime de faveur des articles 210 A et 210 B du CGI**.

L’article 210-0 A, I, 4° a précisément prévu cette modalité d’attribution directe.

La sécurité du schéma dépendra principalement :

1. de la qualification effective de l’activité industrielle comme branche complète et autonome ;
2. du respect des obligations du régime de l’article 210 B ;
3. de la manière dont seront répartis les titres de la société industrielle entre les deux branches familiales ;
4. de l’absence de soulte excessive ou de transfert de valeur non justifié ;
5. de la documentation des motifs économiques de la séparation.

Si l’objectif est une attribution asymétrique — une branche familiale recevant l’activité industrielle et l’autre conservant l’activité de négoce —, une étude spécifique de la mécanique capitalistique complémentaire est indispensable. Au regard de l’enjeu, un rescrit fiscal peut être opportun avant la réalisation de l’opération.

---

## U10

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

**Non. Ce remploi n’est pas éligible et ne permet pas de maintenir le report d’imposition.**

Le report prévu à l’article 150-0 B ter du CGI prend fin en cas de cession des titres apportés dans les trois ans de l’apport, sauf si la holding cédante (société bénéficiaire de l’apport) prend l’engagement de remployer, dans les deux ans de la cession et à hauteur d’au moins 60 % du produit (soit ici au moins 5 400 000 €), ce produit dans le financement de moyens permanents d’exploitation affectés à **son** activité commerciale (au sens des articles 34 ou 35), industrielle, artisanale, libérale, agricole ou financière. Les activités de gestion de son propre patrimoine mobilier ou immobilier sont expressément exclues.

L’investissement envisagé (prise de participation ou apport dans une société dont l’objet est l’achat, la rénovation et la revente d’immeubles) ne satisfait pas ces conditions, pour deux raisons cumulatives :

- Il s’agit d’une prise de participation, c’est-à-dire d’un emploi dans le patrimoine mobilier de la holding. Cette activité est exclue par le texte même.
- Les fonds ne financent pas des moyens permanents d’exploitation de la holding elle-même. Ils financent l’activité (et le stock) d’une autre personne morale. Même si la cible exerce une activité commerciale de marchand de biens (article 35 du CGI), cela reste l’activité de la cible, non celle de la holding.

À titre surabondant, même si la holding exerçait elle-même l’activité d’achat-rénovation-revente, les immeubles acquis en vue de la revente constitueraient des stocks (actifs circulants) et non des moyens permanents d’exploitation (immobilisations affectées de façon durable à l’activité). Le texte exige précisément des moyens permanents.

En l’absence de remploi éligible dans le délai de deux ans, le report d’imposition prendra fin. La plus-value en report deviendra imposable au titre de l’année de la cession des titres (2025), selon les règles de droit commun applicables à cette date, avec les majorations et intérêts de retard éventuels en cas de défaut de déclaration.

Je vous invite à me communiquer les éléments complémentaires (date exacte de l’apport, montant de la plus-value en report, statuts et activité réelle actuelle de la holding, projet précis de la société cible et modalités d’investissement envisagées) afin d’examiner s’il existe une autre voie de remploi conforme ou des mesures d’accompagnement possibles. Dans l’attente, aucun engagement de remploi ne doit être pris sur cette opération.

---

## U11

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

**Sous réserve que l’activité de la SAS consiste seulement à donner en location les quarante appartements meublés, l’exonération partielle de l’article 787 B du CGI n’est pas applicable à la donation du 25 octobre 2023.**

### 1. L’activité de location meublée est expressément exclue lorsqu’elle relève de la gestion du patrimoine immobilier propre

Certes, la location habituelle de locaux d’habitation meublés présente un caractère commercial au sens des articles 34 et 35 du CGI.

Toutefois, le deuxième alinéa de l’article 787 B constitue une exclusion spéciale :

> « n’est pas considérée comme une activité […] commerciale […] l’exercice par une société d’une activité de gestion de son propre patrimoine mobilier ou immobilier ».

Une société qui détient ses propres appartements et les donne simplement en location meublée exerce, pour l’application du régime Dutreil, une **activité de gestion de son propre patrimoine immobilier**. Peu importent à cet égard :

- le nombre d’appartements ;
- l’exercice de l’activité au moyen d’une SAS ;
- l’assujettissement de la société à l’impôt sur les sociétés ;
- la qualification fiscale de bénéfices industriels et commerciaux au regard des articles 34 et 35.

L’exception concernant les **holdings animatrices** est sans incidence ici : la société décrite détient directement les immeubles et non un portefeuille de participations dans des filiales opérationnelles.

### 2. La date du 25 octobre 2023 place la donation dans le champ de cette exclusion

La règle précitée s’applique aux transmissions intervenues à compter du **17 octobre 2023**. Une donation signée le **25 octobre 2023** est donc concernée, même si l’engagement collectif a été conclu antérieurement, le 3 mars 2021.

La date de conclusion du pacte ne cristallise pas l’éligibilité de l’activité au regard de la loi applicable à la donation.

### 3. Les autres conditions annoncées ne permettent pas de remédier à cette difficulté

Sur les éléments fournis, les conditions formelles paraissent par ailleurs organisées :

- engagement collectif portant sur la totalité des droits et d’une durée supérieure à deux ans ;
- engagements individuels pris par les deux enfants ;
- donation en pleine propriété et à parts égales ;
- maintien du donateur comme président pendant trois ans, sous réserve que la fonction soit effectivement exercée et que les autres exigences du pacte soient respectées.

Mais ces conditions de conservation et de direction ne suffisent pas : **l’exercice d’une activité éligible constitue une condition autonome et préalable**. L’activité patrimoniale de location meublée fait donc obstacle au bénéfice du régime.

### 4. Réserve en cas d’activité hôtelière ou para-hôtelière véritable

La conclusion serait susceptible d’être différente si la société ne se limitait pas à louer des appartements meublés, mais exploitait réellement une activité hôtelière ou para-hôtelière comportant des prestations substantielles : accueil organisé, nettoyage régulier pendant le séjour, fourniture et renouvellement du linge, petits-déjeuners, personnel dédié, services aux occupants, etc.

Il faudrait alors établir que l’activité principale est une **activité opérationnelle de prestations de services**, et non la simple valorisation locative des immeubles détenus. Cette qualification dépend des conditions concrètes d’exploitation, et non des seuls statuts ou de la dénomination de l’activité.

## Conclusion

Dans l’hypothèse d’une **location meublée ordinaire**, je déconseille de placer la donation du 25 octobre 2023 sous le régime de l’article 787 B :

- l’exonération de 75 %, soit **15 millions d’euros** sur une valeur totale de 20 millions d’euros, ne serait pas acquise ;
- corrélativement, la réduction de 50 % des droits prévue pour certaines donations en pleine propriété avant 70 ans ne pourrait pas être revendiquée sur ce fondement.

Avant la signature, il conviendrait néanmoins d’auditer les baux, les prestations effectivement fournies, les moyens humains, la facturation et le traitement TVA afin de vérifier si l’exploitation peut être qualifiée d’hôtelière ou de para-hôtelière. À défaut, la donation doit être chiffrée sans régime Dutreil.

---

## U12

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

**Cabinet d'Avocats**
**Objet :** Consultation fiscale préalable à la cession de titres d'une SCI
**Dossier :** Cession de parts de SCI à prépondérance immobilière
**Date :** 18 septembre 2023

Cher Client,

Vous m'avez consulté en vue de la cession des titres de votre Société Civile Immobilière (SCI), dont l'actif est constitué à 80 % d'immeubles situés en France, pour un prix de 4 000 000 euros, avec une signature prévue le 20 septembre 2023. 

Après examen des éléments factuels et du texte législatif en vigueur à la date de l'opération (article 726, I, 2° du Code Général des Impôts), voici mon analyse quant au droit d'enregistrement applicable et aux mentions obligatoires devant figurer dans l'acte de cession.

### 1. Sur la qualification de la SCI et le droit d'enregistrement dû

Aux termes de l'article 726, I, 2° du CGI, les cessions de participations dans des personnes morales à prépondérance immobilière sont soumises à un droit d'enregistrement de 5 %.

La définition d'une personne morale à prépondérance immobilière repose sur deux critères cumulatifs :
1. Les droits sociaux ne sont pas négociés sur un marché réglementé ou un système multilatéral de négociation. S'agissant d'une SCI, ses parts ne sont pas cotées, ce critère est donc rempli.
2. L'actif de la société est principalement constitué d'immeubles ou de droits immobiliers situés en France. La notion de "principalement" s'entend d'une proportion supérieure à 50 % de l'actif brut ou net. En l'espèce, l'actif de votre SCI est constitué à 80 % d'immeubles situés en France. 

Votre SCI remplit donc les conditions pour être qualifiée de personne morale à prépondérance immobilière.

**Calcul du droit d'enregistrement :**
Le droit de 5 % s'applique sur le prix de cession, soit :
* 4 000 000 € x 5 % = **200 000 euros**.

Ce droit devra être acquitté lors de l'enregistrement de l'acte de cession par le service de la publicité foncière (via le notaire ou le pôle de gestion comptable, selon le lieu de dépôt).

### 2. Sur le contenu de l'acte de cession

Pour que l'opération soit valablement enregistrée au taux de 5 % et pour se prémunir contre tout redressement fiscal de l'administration (qui pourrait contester la qualification de prépondérance immobilière), l'acte de cession devra impérativement contenir un certain nombre de mentions et de déclarations.

**A. Les mentions justifiant la prépondérance immobilière**
L'acte devra comporter une déclaration détaillée de la composition de l'actif de la SCI, à la date de la cession et au cours de l'année précédant celle-ci. Il faudra y faire apparaître distinctement :
* La valeur des immeubles et droits immobiliers situés en France (les 80 %) ;
* La valeur des autres éléments d'actif (liquidités, meubles, etc.) ;
* La valeur totale de l'actif, afin que le rapport soit manifestement supérieur à 50 %.
* Une déclaration expresse confirmant que les titres de la SCI ne sont pas admis aux négociations sur un marché réglementé ou un système multilatéral de négociation.

**B. L'hypothèse d'une cession à l'étranger**
Le texte de l'article 726 prévoit une formalité spécifique si la cession est réalisée à l'étranger. Si l'acte du 20 septembre 2023 devait être signé hors de France, la loi impose qu'il soit constaté dans le délai d'un mois par un acte reçu en la forme authentique par un notaire exerçant en France. 
Si la signature a lieu en France, cette formalité ne s'applique pas, mais l'acte devra tout de même être enregistré dans les conditions de droit commun (généralement dans le mois de la signature).

### 3. Recommandations avant signature

Avant de signer l'acte le 20 septembre 2023, je vous recommande de :
1. Vérifier avec le notaire rédacteur que le projet d'acte contient bien les clauses de déclaration d'actif mentionnées ci-dessus.
2. Vous assurer que les 80 % d'actif immobilier sont calculés sur une base cohérente (valeur vénale ou valeur comptable, l'administration acceptant généralement la valeur vénale) et que ce ratio n'a pas fluctué sous le seuil de 50 % au cours de l'année écoulée.
3. Prévoir le règlement du droit de 200 000 euros par les soins du notaire lors de la formalité d'enregistrement (sauf convention contraire entre vous et l'acquéreur, le droit étant légalement à la charge du vendeur, mais en pratique souvent négocié).

Je me tiens à votre entière disposition pour examiner le projet d'acte avant sa signature, afin de sécuriser juridiquement et fiscalement cette opération.

Bien cordialement,

**[Votre Nom]**
*Avocat à la Cour, Spécialiste en Droit Fiscal*

---

## U13

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus a la societe
apporteuse.

Le projet d'apport a ete depose au greffe du tribunal de commerce
le 10 novembre 2022.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder, en entier :**

**NOTE DE CONSEIL FISCAL**
**Objet :** Éligibilité au régime de faveur des apports partiels d'actifs (articles 210 A et suivants du CGI)
**Date :** [Date du jour]
**Destinataire :** Groupe familial / Direction juridique et fiscale

---

### I. RAPPEL DU CADRE JURIDIQUE

Le régime de faveur des apports partiels d'actifs (APA), prévu aux articles 210 A et suivants du Code général des impôts (CGI), permet de réaliser en franchise d'impôt sur les sociétés et de droits de mutation la transmission d'une branche complète d'activité, sous réserve du respect de conditions cumulatives :

1. **Objet de l'opération** : apport, sans dissolution de la société apporteuse, d'une ou plusieurs branches complètes d'activité à une société bénéficiaire ;
2. **Contrepartie** : remise exclusive de titres représentatifs du capital de la société bénéficiaire ;
3. **Autonomie de la branche** : la branche apportée doit constituer un ensemble autonome, capable de fonctionner par ses propres moyens (actifs, passifs, contrats, personnel, clientèle) ;
4. **Agrément préalable** : demande d'agrément adressée à l'administration fiscale **avant la réalisation de l'opération** et, en principe, **au moins six mois avant la date prévue** ;
5. **Absence de motif principal d'évasion fiscale** : l'opération ne doit pas avoir pour but principal ou pour l'un de ses buts principaux la fraude ou l'évasion fiscale.

Le régime est conditionné à l'obtention d'un agrément exprès de l'administration fiscale (BOI-IS-CHG-10-20-10, § 100 et s.).

---

### II. ANALYSE DE VOTRE OPÉRATION AU REGARD DES CONDITIONS SUBSTANTIELLES

Sur le plan structurel, votre projet remplit les critères de fond :
- La holding apporte une branche industrielle à une société nouvelle sans être dissoute ;
- La contrepartie consiste en la remise de titres de la nouvelle société à la holding apporteuse ;
- Sous réserve de vérifier que la branche industrielle constitue bien un ensemble autonome (ce qui suppose un inventaire précis des actifs, passifs, contrats, salariés et éléments incorporels affectés), la condition de "branche complète d'activité" semble remplie.

**Le point de vigilance majeur ne réside donc pas dans la nature de l'opération, mais dans son calendrier et le respect de la procédure d'agrément.**

---

### III. LE POINT CRITIQUE : LE DÉPÔT AU GREFFE DU 10 NOVEMBRE 2022

La doctrine administrative et la jurisprudence sont constantes sur un point : **l'agrément doit être obtenu avant tout acte matérialisant ou engageant irrémédiablement l'opération**.

Or, le dépôt du projet d'apport au greffe du tribunal de commerce est considéré par l'administration comme un acte préparatoire engageant la société et rendant l'opération irréversible (BOI-IS-CHG-10-20-10, § 120 ; CE, 9 mars 2018, n° 405.652). En conséquence :

- Si la demande d'agrément a été **déposée auprès de la Direction des Grandes Entreprises ou de la Direction des Résidents Étrangers et des Services Généraux avant le 10 novembre 2022**, le régime de faveur reste en principe applicable, sous réserve de l'obtention de l'agrément et du respect des autres conditions.
- Si la demande d'agrément a été **formalisée après le 10 novembre 2022**, ou si aucune demande n'a été adressée, **le régime de faveur est très probablement inapplicable**. L'administration considère que l'opération est déjà "engagée" et que la condition de l'agrément préalable n'est plus remplie.

Dans cette hypothèse, l'apport serait soumis au régime de droit commun :
- Imposition immédiate des plus-values latentes sur les actifs apportés ;
- Application des droits de mutation à titre onéreux (sauf exonération spécifique) ;
- Perte du report d'imposition jusqu'à la cession des titres reçus.

---

### IV. RECOMMANDATIONS PRATIQUES

1. **Vérifier la date exacte de dépôt de la demande d'agrément** : Consulter le récépissé de dépôt ou l'accusé de réception de l'administration. Si le dépôt est antérieur au 10/11/2022, le régime reste défendable.
2. **Qualifier juridiquement le dépôt du 10/11/2022** : S'il s'agissait d'un simple "projet informatif" non signé, non publié et sans engagement ferme, une argumentation pourrait être tentée pour soutenir que l'opération n'était pas encore "réalisée". Cette voie reste toutefois aléatoire et soumise à l'appréciation stricte du service vérificateur.
3. **Si l'agrément n'a pas été demandé à temps** :
   - Évaluer l'impact fiscal en régime de droit commun (plus-values, droits de mutation, TVA) ;
   - Examiner la possibilité de restructurer l'opération (ex. : apport en nature différé, scission, ou création d'une holding intermédiaire) si le calendrier le permet encore ;
   - Solliciter un rescrit fiscal pour sécuriser le traitement, en exposant précisément les faits et le calendrier.
4. **Préparer le dossier de justification de l'autonomie de la branche** : Inventaire détaillé, contrats transférés, affectation du personnel, plan de financement, et preuve de l'absence de motif d'évasion fiscale.

---

### V. RÉSERVES D'USAGE

Cette analyse est établie sur la base des éléments communiqués et du droit fiscal en vigueur à la date de la présente note. Elle ne préjuge pas de la position de l'administration fiscale, qui demeure souveraine dans l'octroi de l'agrément et dans l'interprétation des conditions de forme. Une étude complète des actes, du calendrier exact des démarches et de la situation comptable et fiscale de la holding est indispensable avant toute prise de décision définitive.

Je reste à votre disposition pour examiner les pièces justificatives, vérifier le statut de la demande d'agrément et, le cas échéant, préparer une réponse argumentée à l'administration ou une alternative structurale.

**[Signature]**  
Avocat au Barreau de [Ville]  
Spécialiste en droit fiscal des entreprises et restructurations

---

## U14

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

**NOTE DE CONSULTATION**

**Objet :** Proposition de rectification TVA – chantier facturé le 15 avril 2025 – installation d'une chaudière – taux applicable

---

## 1. Réponse en l'état : le dossier n'est pas en état d'être tranché

Je ne peux pas vous dire, sur les seuls éléments que vous me communiquez, si le taux de 5,5 % était correct. Il manque **deux informations déterminantes**, et ce sont précisément celles sur lesquelles se jouera le litige :

1. **La nature de la chaudière installée** (marque, modèle, combustible) ;
2. **La date d'achèvement des travaux**, ainsi que la date d'acceptation du devis et de l'éventuel acompte — la date de facturation (15 avril 2025) n'étant pas, en matière de prestations de services, la date qui commande le taux.

Merci de me transmettre les pièces listées au § 6 avant l'expiration du délai de réponse.

---

## 2. Les conditions du I de l'article 278-0 bis A sont, elles, satisfaites

Sur les trois conditions cumulatives du I, aucune ne pose difficulté au cas d'espèce :

- **1° Locaux achevés depuis au moins deux ans** : maison de quinze ans → condition remplie (à documenter par l'attestation du client, cf. § 6) ;
- **2° Affectation à l'habitation** : maison occupée par son propriétaire → condition remplie ;
- **3° Prestation portant sur l'installation d'un équipement d'amélioration du chauffage** : l'installation d'une chaudière relève bien du b) du 3°.

**Autrement dit, si l'administration entend rehausser, ce n'est pas sur le I — c'est nécessairement sur le III bis.** Vérifiez que la proposition de rectification est bien motivée sur ce fondement : une proposition qui se bornerait à viser « l'article 278-0 bis A » sans identifier le texte d'exclusion appliqué serait insuffisamment motivée au regard de l'article L. 57 du LPF, ce qui constitue un moyen de procédure à ne pas négliger.

---

## 3. Le point de blocage : le III bis

Le III bis écarte le taux réduit et impose le taux normal aux prestations « **comprenant la fourniture ou l'installation d'une chaudière susceptible d'utiliser des combustibles fossiles** ».

Trois observations sur la portée de ce texte :

**a) Le critère est technique, non factuel.** Le texte ne vise pas la chaudière qui *utilise* des combustibles fossiles, mais celle qui est *susceptible* d'en utiliser. Il suffit donc que l'appareil soit techniquement conçu pour fonctionner au gaz naturel, au propane, au fioul ou au charbon. Conséquences pratiques :

| Équipement installé | Taux |
|---|---|
| Chaudière gaz (y compris à condensation, THPE) | **20 %** |
| Chaudière fioul | **20 %** |
| Chaudière hybride (PAC + appoint gaz) | **20 %** |
| Chaudière polycombustible (bois/fioul) | **20 %** |
| Chaudière biomasse (bûches, granulés) exclusivement | **5,5 %** |
| Chaudière électrique | **5,5 %** (sous réserve, cf. infra) |

L'argument selon lequel la chaudière serait alimentée en biométhane ou en biopropane est, à mon sens, **voué à l'échec** : l'appareil reste techniquement susceptible de fonctionner au gaz naturel.

**b) L'exclusion contamine toute la prestation.** Le texte vise la prestation « comprenant » la fourniture ou l'installation. Si la chaudière est fossile, ce n'est pas seulement l'appareil mais l'ensemble de l'opération de rénovation énergétique facturée qui bascule au taux normal. Il est également indifférent que le matériel ait été acheté par le client : la seule *installation* suffit à déclencher l'exclusion.

**c) Réserve sur la chaudière électrique.** Si l'appareil est une chaudière électrique, le III bis ne s'applique pas, mais il faudra vérifier au BOFiP si l'administration subordonne le bénéfice du 3° du I à des caractéristiques techniques minimales fixées par arrêté. Je fais ce point avant de vous répondre définitivement.

---

## 4. La question de la date : c'est votre meilleure ligne de défense potentielle

Le III bis est issu de la loi de finances pour 2025. Deux mécanismes doivent être vérifiés, et ils peuvent à eux seuls neutraliser le redressement :

**a) Le fait générateur.** Pour une prestation de services, le fait générateur est l'**achèvement de la prestation** (art. 269, 1-a du CGI), et c'est la date du fait générateur qui détermine le taux applicable. **La facture du 15 avril 2025 n'est qu'un document.** Si le chantier a été achevé avant l'entrée en vigueur du III bis, le taux de 5,5 % demeure applicable quand bien même la facture serait postérieure. Il faut donc documenter précisément la date d'achèvement (PV de réception, dernier bon d'intervention, dernier bon de livraison, fiche de pose, mise en service).

**b) Le dispositif transitoire.** Ce type de mesure s'accompagne classiquement d'une clause de sauvegarde maintenant le taux réduit pour les opérations ayant fait l'objet d'un **devis accepté et d'un acompte encaissé** avant la date d'effet. Je vérifie le texte exact de l'article de la loi de finances et la doctrine BOFiP publiée — vous ne m'avez transmis que l'article codifié, qui ne comporte pas les dispositions d'entrée en vigueur. **Si vous disposez d'un devis signé et d'un acompte encaissé en début d'année, ce point devient central.**

C'est très fréquemment sur ce terrain que ces rectifications tombent : l'administration raisonne sur la date de facture, alors que le droit raisonne sur le fait générateur et sur les mesures transitoires.

---

## 5. Si le taux de 5,5 % est écarté : contester le *quantum*, pas seulement le principe

L'administration vous réclame la différence **entre 5,5 % et 20 %**, soit 14,5 % × 8 500 € = **1 232,50 €** de droits.

Deux angles de contestation subsidiaires :

**a) Le taux intermédiaire de 10 %.** Les travaux d'amélioration et d'entretien portant sur des locaux d'habitation achevés depuis plus de deux ans relèvent en principe du taux de 10 % (art. 279-0 bis du CGI). La question est donc de savoir si la loi de finances pour 2025 a également exclu les chaudières fossiles du champ de l'article 279-0 bis, ou si elle s'est bornée à modifier l'article 278-0 bis A. **Si seule la première disposition a été modifiée, le rappel doit être limité à la différence entre 5,5 % et 10 %**, soit 382,50 €, et non 1 232,50 €. Je vérifie ce point en priorité : c'est un moyen à fort rendement. (Je vous signale toutefois que la formulation même de la proposition de rectification laisse penser que l'administration considère les deux taux réduits comme exclus, ce qui correspond à l'objectif de transposition de la directive (UE) 2022/542.)

**b) L'assiette.** Vérifiez la rédaction du devis. Si le prix a été convenu **toutes taxes comprises**, la TVA doit être calculée « en dedans » sur les 8 967,50 € encaissés, et non « en dehors » sur 8 500 € HT. L'écart n'est pas négligeable et l'administration commet régulièrement cette erreur.

**c) Les pénalités.** Si l'administration a appliqué la majoration de 40 % pour manquement délibéré, elle est très contestable : le III bis est un texte **nouveau**, d'application immédiate, dans un secteur où les professionnels appliquaient le 5,5 % depuis des années aux chaudières à condensation. La charge de la preuve de l'intention délibérée pèse sur l'administration (art. L. 195 A du LPF) et elle ne peut se déduire de la seule erreur de taux. À défaut, seuls les intérêts de retard (0,20 %/mois) sont dus.

**d) La répercussion sur le client final.** Si le rappel est confirmé, vous pouvez émettre une facture rectificative au maître d'ouvrage. Vérifiez toutefois les stipulations du devis : si le prix était ferme et TTC, la récupération auprès du particulier sera juridiquement délicate, et le coût restera à votre charge. C'est un élément à intégrer dans l'arbitrage entre contestation et transaction.

---

## 6. Pièces à me transmettre sans délai

1. La proposition de rectification **complète** (avec l'avis de réception) et le tampon de réception ;
2. Le devis, avec date de signature du client ;
3. Le justificatif de l'acompte éventuel (relevé bancaire, date d'encaissement) ;
4. La **fiche technique du matériel** installé (marque, modèle, combustible) et la facture du fournisseur ;
5. Tout élément établissant la **date d'achèvement** des travaux ;
6. L'**attestation du client** (formulaire 1300-SD ou 1301-SD) certifiant l'ancienneté et l'affectation du local ;
7. La facture émise le 15 avril 2025 ;
8. Le détail des autres chantiers visés par le contrôle (la rectification porte apparemment sur plusieurs chantiers : l'analyse ci-dessus devra être conduite **chantier par chantier**, car la réponse peut différer selon la nature de chaque appareil et la chronologie).

---

## 7. Urgence procédurale

Vous disposez de **trente jours** à compter de la réception de la proposition de rectification pour présenter vos observations, **prorogeables de trente jours sur simple demande écrite** formulée dans le délai initial (art. L. 57 du LPF). Si le délai initial est déjà entamé, **je dépose dès aujourd'hui la demande de prorogation** : elle est de droit et ne coûte rien.

En cas de désaccord persistant, la voie de la commission des impôts directs et des taxes sur le chiffre d'affaires reste ouverte, puis la réclamation contentieuse.

---

## Synthèse

- Les conditions du I de l'article 278-0 bis A sont remplies : le débat porte exclusivement sur le III bis.
- **Chaudière gaz ou fioul + travaux achevés après l'entrée en vigueur du texte, sans devis/acompte antérieurs → le 5,5 % était erroné.**
- **Chaudière biomasse ou électrique, ou travaux achevés avant l'entrée en vigueur, ou devis accepté et acompte encaissé avant la date d'effet → le 5,5 % était fondé et le redressement doit être abandonné.**
- Dans tous les cas, la question de savoir si le rappel doit être arrêté à 10 % plutôt qu'à 20 % mérite d'être soulevée, de même que la décharge des pénalités.

Je reste à votre disposition pour un point téléphonique dès réception des pièces.

---

## U15

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

## Avis

Au vu des seuls éléments communiqués, l’application du taux de **5,5 % est défendable, mais elle n’est pas automatiquement acquise du seul fait qu’il s’agit de l’installation d’une chaudière**.

Les trois conditions de l’article 278-0 bis A, I du CGI sont cumulatives.

### 1. Ancienneté du logement

La maison est achevée depuis quinze ans.

La condition tenant à des locaux achevés depuis au moins deux ans est donc remplie.

### 2. Affectation à l’habitation

La maison est occupée par son propriétaire. Elle est donc affectée à l’usage d’habitation.

Cette seconde condition est également remplie. Le statut de propriétaire occupant est sans incidence défavorable.

### 3. Nature de la prestation

La prestation consiste en la pose d’une chaudière, donc d’un équipement intervenant dans le **chauffage**.

Toutefois, le texte exige plus précisément que l’équipement ait pour objet :

- d’économiser l’énergie ; ou
- de recourir à une énergie produite à partir de sources renouvelables,

par l’amélioration notamment du chauffage.

Il faut donc pouvoir établir que la chaudière installée répond effectivement à cette finalité de rénovation énergétique. La seule désignation « chaudière » sur la facture ne suffit pas nécessairement : une chaudière standard, sans élément établissant un gain énergétique ou le recours à une énergie renouvelable, peut être regardée comme un simple équipement de chauffage et non comme un équipement de rénovation énergétique au sens du 5,5 %.

## Conclusion pratique

### Le taux de 5,5 % était correct si :

L’entreprise peut justifier que la chaudière posée était un équipement améliorant l’efficacité énergétique du chauffage ou utilisant une énergie renouvelable. Il convient notamment de réunir :

- le devis accepté ;
- la facture détaillée ;
- la référence exacte, la marque et le modèle de la chaudière ;
- la fiche technique et les caractéristiques de rendement ou de performance ;
- le cas échéant, les documents montrant le remplacement d’un équipement ancien et énergivore ;
- tout document commercial ou technique faisant apparaître l’économie d’énergie attendue.

Dans cette hypothèse, les trois conditions légales sont réunies et la proposition de rectification doit être contestée sur le fond.

### Le taux de 5,5 % est fragile si :

La chaudière est une chaudière conventionnelle et que le dossier ne permet pas de démontrer sa vocation à économiser l’énergie ou à utiliser une source renouvelable.

Dans ce cas, l’administration peut écarter le taux de 5,5 %. Mais elle ne peut pas, pour autant, réclamer mécaniquement l’application du taux normal de **20 %**.

## Point essentiel : le taux subsidiaire de 10 %

Même si le bénéfice du taux de 5,5 % devait être refusé, le chantier porte, a priori, sur des travaux d’amélioration dans une habitation achevée depuis plus de deux ans. Il convient donc d’examiner l’application subsidiaire du taux réduit de **10 %**, applicable aux travaux d’amélioration, de transformation, d’aménagement et d’entretien des logements de plus de deux ans.

Le montant de 8 500 € HT ne permet pas, à lui seul, de conclure à l’application de 20 %. Il faut vérifier notamment :

- la nature précise de la chaudière ;
- si les travaux s’inscrivent dans une rénovation globale susceptible d’être assimilée à une production d’immeuble neuf ;
- si l’équipement est exclu du taux de 10 % par un texte particulier ;
- les conditions de facturation et les justificatifs détenus par l’entreprise.

Sur les faits exposés, une rectification de **5,5 % à 20 %** paraît donc, au minimum, contestable si l’administration n’explique pas pourquoi le taux de 10 % serait lui-même exclu.

## Position à soutenir dans la réponse à la proposition de rectification

Je conseillerais de répondre sur deux niveaux :

1. **À titre principal**, maintien du taux de 5,5 %, sous réserve de produire les éléments techniques établissant que la chaudière améliore l’efficacité énergétique du chauffage ou recourt à une énergie renouvelable.

2. **À titre subsidiaire**, si le vérificateur refusait le 5,5 %, demande d’application du taux de 10 % applicable aux travaux d’amélioration d’un logement de plus de deux ans, sauf démonstration par l’administration d’une exclusion précise.

En conséquence, avant toute réponse définitive, il faut obtenir la référence exacte de la chaudière et les pièces techniques correspondantes. C’est cet élément qui déterminera la solidité de la défense au taux de 5,5 %.

---

## U16

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

Monsieur,

Vous m’interrogez sur les conséquences de la cession, en février 2026, par votre holding des titres d’une société d’exploitation que vous lui aviez apportés moins de trois ans auparavant, et sur les conditions à respecter pour conserver le report d’imposition dont vous bénéficiez personnellement en application de l’article 150-0 B ter du CGI.

Je vous précise ci-après l’analyse de la situation et les recommandations qui en découlent.

## 1. Rappel du régime applicable

L’apport de titres à une société contrôlée par l’apporteur bénéficie, sous conditions, d’un report d’imposition de la plus-value constatée au jour de l’apport. Ce report est prévu par l’article 150-0 B ter du CGI.

Ce report prend normalement fin, notamment, en cas de cession des titres apportés par la société bénéficiaire de l’apport dans un délai de trois ans à compter de la date de l’apport (article 150-0 B ter, I, 2° du CGI).

Toutefois, le même texte prévoit une exception : le report n’est pas remis en cause si la société bénéficiaire de l’apport (votre holding) cède les titres dans ce délai de trois ans et prend l’engagement d’investir le produit de la cession, dans un délai de trois ans à compter de la date de la cession, à hauteur d’au moins 70 % de ce produit, dans le financement de moyens permanents d’exploitation affectés à son activité éligible, telle que définie au 3° du C du I de l’article 199 terdecies-0 A du CGI.

En l’espèce, la cession par la holding est intervenue moins de trois ans après votre apport. Le report d’imposition dont vous bénéficiez est donc susceptible d’être remis en cause, sauf si votre holding satisfait aux conditions de l’exception précitée.

## 2. Conditions à respecter pour conserver le report

### a. Prise d’engagement formel

Votre holding doit prendre l’engagement d’investir au moins 70 % du produit de la cession, soit un minimum de **6 300 000 euros** (9 000 000 € × 70 %), dans un délai de trois ans à compter de la date de la cession, c’est-à-dire **avant la fin du mois de février 2029**.

Cet engagement doit être formalisé. En pratique, il est pris dans la déclaration de résultats de l’exercice au cours duquel la cession est intervenue (exercice clos en 2026, déposé en 2027). Il est vivement recommandé de joindre un courrier explicite mentionnant cet engagement et de le conserver soigneusement, car l’administration fiscale peut en demander la justification.

### b. Nature du réinvestissement

Le produit de la cession doit être investi dans des **moyens permanents d’exploitation affectés à l’activité de la holding**. Cela exclut les simples placements financiers, les comptes courants d’associés ou la trésorerie dormante.

L’activité de la holding doit être éligible au sens du 3° du C du I de l’article 199 terdecies-0 A. Sont notamment exclues :
- les activités de gestion de patrimoine mobilier ou immobilier ;
- les activités de holding « passive », c’est-à-dire une simple détention de titres sans animation effective du groupe.

En revanche, une **holding animatrice** peut être considérée comme exerçant une activité éligible, à condition qu’elle participe activement à la conduite de la politique de son groupe et au contrôle de ses filiales, et qu’elle rende, le cas échéant, des services internes à ces sociétés.

Ainsi, le réinvestissement peut notamment prendre la forme :
- d’acquisitions d’immobilisations corporelles ou incorporelles directement affectées à l’activité opérationnelle de la holding ;
- de souscriptions au capital ou d’acquisitions de titres de sociétés d’exploitation, **si et seulement si** la holding est qualifiée de holding animatrice (et non passive), et que ces titres constituent des moyens permanents d’exploitation de son activité d’animation.

Il est impératif que la holding justifie de la réalité de son rôle d’animatrice (participation aux décisions stratégiques, contrôle de gestion, services rendus, etc.). À défaut, le réinvestissement dans des titres de filiales ne serait pas éligible et le report serait remis en cause.

### c. Suivi des investissements

La holding devra être en mesure de démontrer, année par année, que les investissements réalisés respectent l’engagement pris. Des obligations déclaratives spécifiques existent (état de suivi des plus-values en report d’imposition, formulaire n° 2074-I ou équivalent). Il conviendra de les respecter scrupuleusement.

## 3. Conséquences en cas de non-respect des conditions

Si l’engagement n’est pas pris, si le montant de 6 300 000 € n’est pas investi dans les délais, ou si les investissements ne sont pas éligibles, le report d’imposition prendra fin rétroactivement à la date de l’apport initial.

Vous serez alors personnellement imposé sur la plus-value d’apport initialement placée en report, au titre de l’année de l’apport, avec application de l’impôt sur le revenu (et des prélèvements sociaux) selon le barème en vigueur à cette date, majoré des intérêts de retard. Aucune pénalité spécifique n’est en principe encourue, mais le coût financier peut être significatif.

## 4. Recommandations pratiques

Je vous invite à mettre en œuvre sans délai les actions suivantes :

1. **Formaliser l’engagement de réinvestissement** dans les déclarations de la holding dès que possible, et au plus tard lors du dépôt de la liasse fiscale de l’exercice 2026.
2. **Déterminer précisément la nature de l’activité de votre holding** (opérationnelle ou animatrice) et réunir les éléments probants démontrant cette qualification (procès-verbaux de décisions, contrats de prestations de services, organigramme, etc.).
3. **Identifier des investissements éligibles** représentant au moins 6 300 000 € et les réaliser dans le délai de trois ans. Il est conseillé de privilégier des actifs clairement affectés à l’activité de la holding et d’éviter tout investissement passif.
4. **Conserver une documentation exhaustive** sur les investissements réalisés (factures, actes d’acquisition, preuves d’affectation à l’activité, etc.) et respecter les obligations déclaratives annuelles.
5. **Anticiper la date limite de février 2029** : le délai de trois ans est décompté de date à date. Tout retard entraînerait la déchéance du report.

Je vous invite à me communiquer des précisions sur l’activité actuelle de votre holding et sur les investissements envisagés afin de valider leur éligibilité au regard de la doctrine administrative et de la jurisprudence.

Je reste à votre disposition pour tout complément d’information ou pour vous accompagner dans la mise en œuvre de ces démarches.

Bien à vous,

**[Votre nom]**  
Avocat fiscaliste

---

## U17

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

**Note à l’attention du gérant**

**Objet :** Proposition de rectification – TVA sur travaux de rénovation énergétique (facture du 15 avril 2025 – 8 500 € HT)

Vous m’interrogez sur le bien-fondé du taux de 5,5 % appliqué à l’installation d’une chaudière dans une maison achevée depuis quinze ans et occupée par son propriétaire.

**Analyse**

Les conditions du I de l’article 278-0 bis A du CGI sont, en l’espèce, réunies :
- locaux achevés depuis plus de deux ans ;
- affectation à l’habitation ;
- prestation portant sur l’installation d’un équipement de chauffage.

Toutefois, le III bis du même article déroge expressément à ce régime. Il soumet au taux normal de l’article 278 (20 %) les prestations de rénovation énergétique qui comprennent la fourniture ou l’installation d’une chaudière susceptible d’utiliser des combustibles fossiles.

Sauf à démontrer que l’appareil installé n’est pas susceptible d’utiliser de tels combustibles (ce que les éléments actuellement communiqués ne permettent pas d’établir), le taux réduit de 5,5 % n’était pas applicable. Le taux de 20 % s’imposait.

**Conséquences**

La proposition de rectification apparaît fondée sur ce point. Le complément de TVA (et les intérêts de retard) est donc dû, sous réserve d’un éventuel examen des autres chefs de redressement ou d’une discussion sur la qualification exacte de l’appareil.

Je reste à votre disposition pour examiner le dossier de l’administration, préparer les observations et, le cas échéant, rechercher si l’appareil installé échappe réellement à la dérogation du III bis.

Bien cordialement.

---

## U18

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

Pour déterminer si l'exonération partielle de l'article 787 B du Code Général des Impôts (CGI) est applicable à la donation que le dirigeant de 62 ans envisage de faire à ses deux enfants, il convient d'analyser les conditions prévues par cet article et de les confronter aux faits de l'espèce.

1. **Nature de la société et de son activité** : La société en question est une société par actions simplifiée (SAS) qui possède quarante appartements meublés. La valeur des titres est de 20 000 000 euros. L'activité principale de cette société semble être la gestion de son patrimoine immobilier, ce qui, selon l'article 787 B, n'est pas considérée comme une activité industrielle, commerciale, artisanale, agricole ou libérale au sens des premiers alinéas.

2. **Exclusion de l'exonération pour gestion de patrimoine** : L'article 787 B exclut explicitement l'exonération pour les sociétés dont l'activité principale est la gestion de leur propre patrimoine mobilier ou immobilier. Étant donné que la société en question possède quarante appartements meublés, il est probable que son activité principale soit considérée comme relevant de la gestion de son propre patrimoine immobilier.

3. **Exception pour participation active à la conduite de la politique d'un groupe** : L'article prévoit une exception à l'exclusion mentionnée ci-dessus pour les sociétés qui ont pour activité principale la participation active à la conduite de la politique de leur groupe, constitué de sociétés exerçant une activité éligible. Cependant, les faits ne mentionnent pas que la société fasse partie d'un groupe ou qu'elle ait une activité de participation active dans un tel groupe. Par conséquent, cette exception ne semble pas applicable.

4. **Engagement collectif de conservation et autres conditions** : Les titres font l'objet d'un engagement collectif de conservation signé le 3 mars 2021, et chaque enfant prend l'engagement individuel prévu. Le dirigeant conserve la présidence pendant trois ans. Cependant, l'exonération prévue par l'article 787 B est conditionnée par des critères liés à l'activité de la société et non directement aux engagements de conservation ou à la gouvernance post-donation.

**Conclusion** : Étant donné que l'activité principale de la société semble être la gestion de son patrimoine immobilier, il est probable que l'exonération partielle prévue par l'article 787 B du CGI ne soit pas applicable à la donation envisagée. La société ne paraît pas remplir les conditions requises pour bénéficier de cette exonération, notamment parce que son activité principale est la gestion de son propre patrimoine immobilier, ce qui est explicitement exclu par le texte. Il conviendrait de vérifier si d'autres exonérations ou dispositifs fiscaux pourraient être applicables à cette situation.

---

## U19

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

**Note de consultation — Maintien du report d'imposition (CGI, art. 150-0 B ter, I, 2°)**

**I. Faits et mécanisme**

Vous avez apporté à votre holding (détenue à 100 %) les titres de votre société d'exploitation ; la plus-value d'apport a été placée en report d'imposition. La cession de ces titres par la holding le 10 novembre 2025, moins de trois ans après l'apport, constitue en principe un événement mettant fin au report. La dérogation est toutefois ouverte si la holding réinvestit le produit de la cession dans les conditions de l'alinéa a.

**II. Conditions de la dérogation (cumulatives)**

1. Cession par la société bénéficiaire de l'apport dans les trois ans de l'apport — condition remplie ;
2. **Engagement de la holding** d'investir le produit de cession — la doctrine exige qu'il soit pris au moment de la cession, dans l'acte ou dans un document séparé établi à cette occasion (BOI-RPPM-PVBMI-20-10-20-40). Point à vérifier d'urgence, la cession étant déjà intervenue ;
3. Réinvestissement dans un délai de deux ans, soit **au plus tard le 10 novembre 2027** ;
4. À hauteur d'au moins 60 % du produit de cession, soit **≥ 5 400 000 €**. Le seuil s'apprécie globalement : en dessous, le report tombe en totalité, sans prorata ;
5. Financement de **moyens permanents d'exploitation** affectés à une activité éligible de la holding, la gestion de son propre patrimoine mobilier ou immobilier étant expressement exclue.

**III. Analyse du projet**

*1. La forme du réinvestissement.* Les « moyens permanents d'exploitation » s'entendent des éléments de l'actif immobilisé (incorporels, corporels, financiers), à l'exclusion des éléments circulants. Il en résulte que :

- l'acquisition directe d'immeubles destinés à être revendus ne fonctionnerait pas : pour un marchand de biens, ces immeubles sont des **stocks**, non des moyens permanents ;
- en revanche, la souscription ou l'acquisition de **titres de la société cible** peut constituer une immobilisation financière éligible, à condition que les titres soient inscrits à l'actif immobilisé et détenus durablement (titres de participation), et non de simples titres de placement.

*2. L'activité de la holding — le point décisif.* Le réinvestissement doit être affecté à l'activité propre de la holding, laquelle doit être commerciale (art. 34-35), industrielle, artisanale, libérale, agricole ou financière :

- si votre holding est une **holding patrimoniale passive** (détention de participations, perception de dividendes et de produits de cession), la prise de participation dans la société de rénovation-revente relèvera de la gestion de son propre patrimoine mobilier : la dérogation sera écartée et le report prendra fin ;
- si elle est une **holding animatrice** — participation active à la politique du groupe, prestations effectivement rendues et facturées aux filiales, moyens réels — son activité est financière et commerciale, et les titres des filiales constituent des moyens permanents d'exploitation : la dérogation est ouverte.

*3. L'activité de la cible.* L'achat d'immeubles en vue de leur revente, même après rénovation, est une activité commerciale par nature (marchand de biens), et non une gestion de patrimoine immobilier. Cette circonstance est favorable mais secondaire : le texte juge l'activité de la **holding**, non celle de la filiale. Une participation minoritaire et passive resterait de la gestion de patrimoine mobilier, quelle que soit l'activité de la cible.

**IV. Conclusion**

Le remploi envisagé **peut** maintenir le report, mais pas automatiquement. Il le maintiendra si, et seulement si : (i) l'engagement de réinvestir a été valablement pris ; (ii) la holding réinvestit elle-même au moins 5,4 M€ avant le 10 novembre 2027 ; (iii) sous forme de titres de participation détenus durablement ; et (iv) la holding exerce une activité réelle d'animation. **Si la holding demeure une simple holding patrimoniale, la réponse est négative** : le report prend fin et la plus-value d'apport devient imposable (en pratique au PFU de 30 %, sauf option pour le barème).

**V. Recommandations**

1. Vérifier immédiatement l'acte du 10 novembre 2025 : l'engagement y figure-t-il ? À défaut, le maintien du report est fragile et il faudra construire l'argumentaire.
2. Le réinvestissement doit être opéré **par la holding, avec des fonds restés dans la holding** : aucune distribution, aucun rachat de vos titres, aucune avance en compte courant.
3. Si la holding est aujourd'hui passive, la doter d'une animation **réelle** avant le réinvestissement : conventions d'animation et de prestations, facturation, moyens humains et matériels, participation effective aux décisions. Une transformation de pure forme serait vulnérable à la procédure d'abus de droit.
4. Prendre le contrôle (ou une influence notable) de la cible et animer effectivement sa politique ; veiller à ce qu'elle se consacre à l'achat-revente et évite la détention locative, qui brouillerait l'analyse.
5. Comptabiliser les titres en immobilisations financières, documenter l'opération (PV, business plan, conventions, factures) et conserver la participation durablement.
6. Compte tenu de l'enjeu — rappel de l'impôt différé, assorti d'intérêts de retard, si les conditions ne sont pas remplies au 10 novembre 2027 — envisager une prise de position formelle de l'administration (LPF, art. L. 80 B) avant le réinvestissement.

---

## U20

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

En tant qu’avocat fiscaliste, voici mon analyse pour la cession que vous projetez.

**1. Droit d’enregistrement dû**

La société civile immobilière (SCI) dont l’actif est constitué à 80 % d’immeubles situés en France est une **personne morale à prépondérance immobilière** (PMPI) au sens de l’article 726, I, 2° du CGI, en vigueur au 20 septembre 2023. En effet, son actif est principalement composé d’immeubles français.

La cession de titres d’une PMPI est soumise à un **droit d’enregistrement au taux de 5 %**, prévu par ce même article. La base taxable est le prix de cession, soit **4 000 000 euros**.

Le montant dû s’élève donc à :  
**4 000 000 € × 5 % = 200 000 euros**.

Il n’existe pas, dans ce cadre, d’abattement ou d’exonération applicable aux cessions de parts de SCI à prépondérance immobilière par des personnes physiques (sauf cas particuliers comme les organismes HLM ou les sociétés foncières sous conditions, ce qui n’est pas votre situation).

Ce droit est exigible lors de l’enregistrement de l’acte, dans le mois suivant la signature, sous peine de pénalités de retard et d’intérêts.

**2. Contenu de l’acte de cession**

L’acte constatant la cession de parts de SCI, qu’il soit sous seing privé ou notarié, doit être signé le 20 septembre 2023 et contenir les mentions obligatoires permettant son enregistrement et la perception du droit proportionnel. Il doit notamment préciser :

- **L’identité des parties** : noms, prénoms, dates et lieux de naissance, adresses, régimes matrimoniaux pour les cédants et cessionnaires.
- **La description précise des parts cédées** : nombre, nature (pleine propriété, nue-propriété ou usufruit), identification de la SCI (dénomination, forme, capital, siège social, numéro RCS).
- **Le prix de cession** : ventilé, le cas échéant, entre valeur des parts et prise en charge de dettes, avec les modalités de paiement.
- **La date de cession** (20 septembre 2023) et la date d’entrée en jouissance.
- **Une déclaration de la société** selon laquelle elle est à prépondérance immobilière au sens de l’article 726, I, 2° du CGI, attestant que son actif est ou a été, au cours de l’année précédant la cession, principalement constitué d’immeubles situés en France. Cette déclaration est essentielle pour justifier le taux de 5 % et peut être établie par le gérant de la SCI.
- **La mention du droit d’enregistrement applicable** et l’engagement de l’acquéreur (ou, selon la convention, du vendeur) de s’acquitter des droits.
- **La signature des parties** (ou de leurs mandataires).

Si la cession était réalisée à l’étranger, l’article 726, I, 2° in fine imposerait qu’elle soit constatée dans le délai d’un mois par un acte authentique reçu par un notaire exerçant en France. En l’espèce, la cession ayant lieu en France, un acte sous seing privé est suffisant.

**Recommandation pratique** :  
- Faites établir l’acte par un notaire ou un avocat spécialisé pour sécuriser la déclaration de prépondérance immobilière et le calcul des droits.  
- Prévoyez le paiement de 200 000 euros lors de l’enregistrement, à effectuer au service de la publicité foncière ou au service des impôts des entreprises (SIE) dans le mois suivant la signature.  
- Conservez tous les justificatifs de la valorisation de l’actif immobilier pour répondre à d’éventuelles demandes de l’administration fiscale.

Je reste à votre disposition pour tout complément ou pour la rédaction de l’acte.

---

## U21

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

**Objet : Consultation fiscale relative à la distribution de dividendes à une société mère luxembourgeoise – Appréciation de la retenue à la source**

Madame, Monsieur,

Vous me consultez au sujet de la distribution d'un montant de 20 000 000 euros que votre société française (ci-après la « Société Distributrice ») envisage de mettre en paiement au profit de sa société mère luxembourgeoise (ci-après la « Société Mère ») le 15 juin 2025.

Vous me demandez de déterminer si cette opération donnera lieu à l'application d'une retenue à la source en France.

Après examen des éléments factuels que vous m'avez communiqués et des textes applicables, voici mon analyse.

### 1. Le principe de la retenue à la source

Le texte que vous citez, l'article 119 bis, 2, premier alinéa du Code général des impôts (CGI), édicte le principe général selon lequel les distributions de bénéfices (dividendes) effectuées par des sociétés françaises au profit de bénéficiaires effectifs n'ayant pas leur siège en France sont soumises à une retenue à la source. 

Le taux normal de cette retenue à la source, prévu à l'article 187 du CGI, est de 25 %. En l'absence d'exonération ou de réduction, la distribution de 20 000 000 euros entraînerait donc une retenue à la source de 5 000 000 euros.

### 2. L'exonération prévue par le droit interne (transposition de la Directive Mère-Fille)

Toutefois, la suite du texte de l'article 119 bis, 2 du CGI (au paragraphe *b*) prévoit une exonération totale de cette retenue à la source pour les distributions effectuées au profit de sociétés mères établies dans un autre État membre de l'Union européenne, sous réserve du respect de conditions strictes.

Pour bénéficier de cette exonération, les conditions suivantes doivent être cumulativement remplies :
1.  **La forme de la société mère :** La Société Mère doit revêtir l'une des formes prévues par la Directive Mère-Fille. En l'espèce, la Société Mère est une société anonyme (SA), ce qui correspond à l'une des formes éligibles.
2.  **L'assujettissement à l'impôt sur les sociétés :** La Société Mère doit être soumise à l'impôt sur les sociétés au Luxembourg, sans pouvoir bénéficier d'une option pour ce régime. Vous m'indiquez qu'elle y est effectivement soumise.
3.  **Le seuil de détention :** La Société Mère doit détenir directement une participation représentant au moins 5 % du capital de la Société Distributrice. En l'espèce, la détention est de 100 %.
4.  **La durée de détention :** La participation doit être détenue de manière continue depuis au moins deux ans. Vous m'indiquez que la Société Mère détient le capital depuis cinq ans, ce qui satisfait largement cette condition.
5.  **Le bénéficiaire effectif :** La Société Mère doit être le bénéficiaire effectif des sommes distribuées, ce qui est le cas ici puisqu'elle en est la propriétaire directe à 100 %.

L'ensemble de ces conditions étant remplies, la distribution entre dans le champ d'application de l'exonération prévue par le droit interne français.

### 3. La convention fiscale franco-luxembourgeoise

Par ailleurs, la convention fiscale signée entre la France et le Luxembourg prévoit, à son article 5, que les dividendes payés par une société française à une société luxembourgeoise peuvent être imposés en France. Toutefois, l'imposition est limitée à 15 %, voire à 0 % si le bénéficiaire effectif détient directement au moins 10 % du capital de la société distributrice. 

La combinaison de l'exonération de droit interne (Directive Mère-Fille) et de la convention fiscale permet de ramener le taux de la retenue à la source à **0 %**.

### 4. Les obligations formales à respecter impérativement

L'exonération n'est pas automatique. Elle est subordonnée au respect d'obligations déclaratives strictes *antérieures* à la mise en paiement des sommes.

Pour que la Société Distributrice puisse appliquer le taux de 0 % lors du paiement du 15 juin 2025, elle devra impérativement être en possession, **avant cette date**, d'un formulaire 5000 (Cerfa n° 12816*09) dûment complété et signé par la Société Mère, accompagné du formulaire 5001 (annexe au formulaire 5000). 

Ce formulaire 5000 doit être certifié par l'administration fiscale luxembourgeoise, qui attestera que la Société Mère est résidente fiscale au Luxembourg et soumise à l'impôt sur les sociétés sans option. 

À défaut d'être en possession de ce document complet et valide à la date du 15 juin 2025, la Société Distributrice sera dans l'obligation d'appliquer la retenue à la source au taux de 25 % (soit 5 000 000 euros) sur les 20 millions d'euros versés. La Société Mère pourrait ensuite demander le remboursement de cette retenue à la source auprès de l'administration fiscale française, mais cette procédure est longue (plusieurs mois) et nécessite des démarches complexes.

### Conclusion

Sous réserve de l'obtention et de la vérification du formulaire 5000 certifié par l'administration luxembourgeoise avant le 15 juin 2025, **aucune retenue à la source ne sera due en France** sur la distribution de 20 000 000 euros à votre société mère luxembourgeoise.

Je vous recommande d'engager dès à présent les démarches auprès de votre société mère pour qu'elle sollicite la délivrance de ce formulaire 5000 auprès des autorités fiscales luxembourgeoises, afin de respecter le délai imparti avant la mise en paiement prévue.

Je reste à votre entière disposition pour vous assister dans la rédaction des actes de distribution et la vérification des formulaires.

Bien cordialement,

**[Votre Nom]**  
Avocat au Barreau de [Ville]  
Spécialiste en Droit Fiscal

---

## U22

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

**OBJET : Consultation préalable à la cession de parts de SCI – Droit d’enregistrement et mentions obligatoires**
**DATE DE LA CESSION :** 20 mars 2024
**PRIX DE CESSION :** 4 000 000 €

Maître,

Je vous prie de trouver ci-après mon analyse fiscale et mes recommandations rédactionnelles, établies sur la base des éléments communiqués et du texte du CGI que vous avez joint.

---

### I. DROIT D’ENREGISTREMENT DÛ

**1. Qualification de la cession**
La société cédée est une société civile immobilière dont l’actif est constitué à 80 % d’immeubles situés en France. Ce ratio excède largement le seuil de prépondérance immobilière (actif « principalement constitué » d’immeubles ou de droits immobiliers situés en France). La société entre donc dans la catégorie des **personnes morales à prépondérance immobilière (PMPI)** au sens de l’article 726, I, 2° du CGI.

**2. Taux et assiette**
Conformément à l’article 726, I, 2° du CGI, les cessions de participations dans une PMPI sont soumises à un droit d’enregistrement forfaitaire de **5 %**.

**3. Calcul**
- Prix de cession : 4 000 000 €
- Droit d’enregistrement dû : 4 000 000 € × 5 % = **200 000 €**

Ce droit est dû par le cessionnaire, mais les parties peuvent conventionnellement en prévoir le partage ou la prise en charge par le cédant. Il est exigible au moment du dépôt de l’acte à la recette des impôts.

---

### II. MENTIONS OBLIGATOIRES DANS L’ACTE

L’article 726, III, B du CGI impose que l’acte (ou la déclaration de cession) **indique expressément** les trois points suivants. Leur omission ou leur imprécision expose à des rehaussements, pénalités ou difficultés de traitement par le service des impôts.

1. **Qualification au titre de l’article 1655 ter du CGI**  
   L’acte doit préciser si la société cédée est une société mentionnée à l’article 1655 ter (sociétés transparentes fiscalement : SCI, SNC, etc., non soumises à l’IS). Si la SCI a opté pour l’IS ou y est soumise de droit, cette mention doit être explicitement négative.

2. **Droit à la jouissance d’immeubles (article 728 du CGI)**  
   L’acte doit indiquer si les parts cédées confèrent au cessionnaire (directement ou indirectement) un droit à la jouissance d’immeubles ou de fractions d’immeubles au sens de l’article 728 (ex. attribution en nature, bail, usufruit, droit d’usage). Si tel n’est pas le cas, la mention doit être formulée de manière négative et non équivoque.

3. **Prise en charge de dettes du cédant**  
   L’acte doit préciser si le cessionnaire a acquitté ou s’engage à acquitter, directement ou indirectement, des dettes contractées auprès du cédant par la société cédée. Si c’est le cas, **le montant exact de ces dettes doit être indiqué**. À défaut, mentionner expressément l’absence de telles dettes.

📌 *Recommandation rédactionnelle* : Ces trois mentions doivent figurer dans un paragraphe dédié, intitulé « Mentions fiscales obligatoires (article 726, III, B du CGI) », et être rédigées de manière affirmative ou négative mais explicite. Une formulation du type « les parties déclarent ne pas être en mesure de préciser… » est insuffisante et risquée.

---

### III. FORMALITÉS COMPLÉMENTAIRES

- **Délai de formalisation** : L’acte doit être enregistré dans le mois de sa signature (règle de droit commun des cessions de parts sociales). Le droit de 200 000 € sera acquitté à cette occasion.
- **Signature à l’étranger** : Si l’acte est signé hors de France, l’article 726, III, A impose qu’il soit **constaté dans un délai d’un mois par un acte authentique reçu par un notaire exerçant en France**. Si la signature a lieu en France, un acte sous seing privé suffit, sous réserve de son enregistrement.
- **Justificatifs à joindre** : Il est prudent de conserver et de pouvoir produire, en cas de contrôle, un état de l’actif net comptable ou fiscal de la SCI à la date de cession (ou au cours de l’année précédente) attestant du seuil de 80 %.

---

### IV. RECOMMANDATIONS PRATIQUES

1. **Vérification du seuil de prépondérance** : Confirmez par un état d’actif actualisé que la proportion d’immeubles français reste ≥ 50 % à la date de signature (ou au cours des 12 mois précédents). Une requalification en cession de droits sociaux classique (taux de 3 % ou exonération) n’est pas possible ici, mais une erreur de qualification pourrait entraîner un rappel de droits.
2. **Rédaction des mentions** : Intégrez les trois mentions obligatoires telles que détaillées ci-dessus. Je reste à votre disposition pour vous transmettre une clause type conforme.
3. **Budget et trésorerie** : Anticipez le paiement des 200 000 € de droits d’enregistrement, ainsi que les éventuels frais de notaire (si acte authentique ou signature à l’étranger) et les honoraires de formalisation.
4. **Coordination avec le notaire** : Si un notaire intervient, lui transmettre dès maintenant le projet d’acte et les éléments d’actif de la SCI afin qu’il puisse vérifier la conformité des mentions et procéder à l’enregistrement dans les délais.

Je reste à votre entière disposition pour relire le projet d’acte avant signature, vérifier la cohérence des mentions fiscales, ou vous assister lors du dépôt à la recette des impôts.

Veuillez agréer, Maître, l’expression de mes salutations distinguées.

**[Votre Nom]**  
Avocat au Barreau de [Ville]  
Spécialiste en droit fiscal et patrimoine

---

## U23

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

Bonjour, je vous remercie de me consulter avant de signer l'acte de cession des titres de votre société civile immobilière.

Après avoir examiné les informations que vous m'avez fournies, je constate que l'actif de la société est constitué à 80 % d'immeubles situés en France. Selon l'article 726, I, 2° du Code Général des Impôts (CGI), la cession de participations dans une personne morale à prépondérance immobilière est soumise à un droit d'enregistrement de 5 %.

La société civile immobilière dont vous cédez les titres remplit les conditions pour être considérée comme une personne morale à prépondérance immobilière, car son actif est principalement constitué d'immeubles situés en France et ses droits sociaux ne sont pas négociés sur un marché réglementé.

Par conséquent, le droit d'enregistrement applicable à la cession de ces titres est de 5 % du prix de cession, soit 200 000 euros (4 000 000 x 5 %).

En outre, l'article 726, III, B du CGI exige que l'acte de cession contienne certaines mentions expresses. L'acte doit indiquer :

1. si la société est une société mentionnée à l'article 1655 ter du CGI (société dont les titres sont soumis à certaines obligations déclaratives) ;
2. si les participations cédées confèrent au cessionnaire le droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'article 728 du CGI ;
3. si le cessionnaire a acquitté ou s'engage à acquitter, directement ou indirectement, des dettes contractées auprès du cédant par la société, en précisant, le cas échéant, leur montant.

Il est essentiel de vérifier ces éléments et de les mentionner explicitement dans l'acte pour satisfaire aux exigences fiscales.

Enfin, puisque l'acte sera signé le 20 mars 2024, il n'y a pas de problème de délai particulier à considérer puisque la cession n'est pas réalisée à l'étranger. Cependant, il est toujours prudent de s'assurer que toutes les formalités sont accomplies dans les délais impartis par la loi.

Je vous recommande de faire vérifier ces informations et de les inclure dans l'acte de cession pour éviter tout problème avec l'administration fiscale. Il serait également sage de consulter un notaire pour la rédaction de l'acte, car il est qualifié pour s'assurer que toutes les exigences légales et fiscales sont respectées.

---

## U24

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

La cession intervenue le 10 mars 2026, moins de trois ans après l’apport, met en principe fin au report d’imposition de la plus-value d’apport du client. Le report ne peut être conservé que si la holding respecte strictement la condition de remploi prévue par l’article 150-0 B ter.

## 1. Montant et délai du remploi

La holding doit :

- prendre l’engagement de remploi ;
- réinvestir au moins **70 % du produit de cession**, soit **6 300 000 €** sur les 9 000 000 € encaissés ;
- dans les **trois ans de la cession**, soit au plus tard le **10 mars 2029** (appréciation de date à date).

Le remploi doit être réalisé **par la holding bénéficiaire de l’apport**, et non personnellement par le client.

## 2. L’activité d’achat, rénovation et revente d’immeubles

Une activité consistant à acheter des immeubles, les rénover puis les revendre relève, en principe, d’une activité de **marchand de biens** ou de **promotion immobilière**. C’est une activité commerciale ; elle ne se confond donc pas, par nature, avec la simple « gestion de son propre patrimoine immobilier », expressément exclue par le texte.

Il ne faut toutefois pas s’arrêter à cette qualification générale.

### Le point bloquant : la nature du remploi

Le a) du 2° du I de l’article 150-0 B ter exige le financement de **moyens permanents d’exploitation** affectés à une activité éligible.

Or, pour une société qui achète des immeubles afin de les rénover et de les revendre :

- les immeubles destinés à la revente constituent normalement des **stocks** ;
- les travaux de rénovation engagés sur ces immeubles concourent également à la constitution ou à la valorisation de ce stock ;
- ces dépenses ne correspondent donc pas, en principe, à des **moyens permanents d’exploitation**.

En conséquence, un apport de fonds à une société de marchand de biens destiné à financer l’acquisition des immeubles à revendre, les travaux et le cycle d’exploitation immobilier **ne permet pas, sur le seul fondement du a), de satisfaire à l’obligation de remploi**.

Autrement dit : l’activité de marchand de biens n’est pas automatiquement exclue parce qu’elle est immobilière, mais le financement de son stock immobilier n’est pas, lui, un financement de moyens permanents d’exploitation.

## 3. Cas dans lesquels un remploi pourrait néanmoins être admis

Le financement pourrait être retenu, à hauteur des seules dépenses correspondantes, s’il est réellement affecté à des immobilisations durables utilisées par l’entreprise dans son activité, par exemple :

- bureaux ou locaux utilisés durablement par la société pour ses besoins propres, et non destinés à la revente ;
- matériels, équipements, véhicules, outils, logiciels, systèmes techniques ;
- actifs incorporels ou autres immobilisations nécessaires à l’exploitation.

Cela ne permettrait généralement pas d’absorber un remploi de 6,3 M€ dans une activité dont l’essentiel des besoins porte sur l’acquisition et la rénovation d’immeubles destinés à être revendus.

À l’inverse, si la société acquérait des immeubles pour les conserver et les louer, elle se heurterait alors directement à l’exclusion visant la gestion de son propre patrimoine immobilier.

## 4. Attention à une autre voie de remploi

Le texte complet de l’article 150-0 B ter prévoit également, sous certaines conditions, des modalités de réinvestissement distinctes, notamment l’acquisition d’une participation conférant le contrôle d’une société opérationnelle éligible. Cette voie doit être distinguée du financement de moyens permanents prévu au a).

Ainsi, si la holding acquiert le contrôle d’une société exerçant effectivement une activité de marchand de biens, l’analyse peut différer selon la modalité exacte de l’opération : souscription au capital, acquisition de titres existants, prise de contrôle, emploi effectif des fonds, etc. Il faudrait alors vérifier les conditions propres à cette autre branche du dispositif, qui ne se réduit pas à la question des immobilisations permanentes.

## Conclusion

**Non, en l’état, le projet de financer une société qui achète, rénove et revend des immeubles ne sécurise pas le maintien du report sur le fondement du a) cité.** Les immeubles et travaux destinés à la revente sont normalement des stocks, et non des moyens permanents d’exploitation.

Le report ne pourrait être préservé que si :

1. au moins **6,3 M€** sont remployés avant le **10 mars 2029** ;
2. le remploi est effectué par la holding ;
3. l’investissement relève d’une modalité légalement admise ;
4. et, s’il est invoqué le a), les fonds financent réellement des immobilisations permanentes affectées à une activité éligible, non le stock immobilier ou les travaux de revente.

Avant tout engagement, il conviendrait donc de structurer précisément l’investissement envisagé — souscription, acquisition de contrôle, emploi des fonds par la cible, calendrier et documentation de l’engagement de remploi — afin d’éviter la remise en cause du report sur l’intégralité de la plus-value d’apport.

---

## U25

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

**Objet : Analyse de la possibilité de maintien du report d’imposition (article 150-0 B ter du CGI) – Cession des titres et projet de réinvestissement**

**Maître [Votre Nom]**
Avocat fiscaliste
[Coordonnées du cabinet]

**À l’attention de [Nom du client]**
[Date]

---

**Cher Monsieur [Nom du client],**

Je vous remercie pour votre consultation concernant la cession des titres de votre société d’exploitation par votre holding, intervenue le **10 novembre 2025**, et les conditions de maintien du **report d’imposition** prévu à l’**article 150-0 B ter, I, 2° du CGI**. Voici une analyse détaillée de votre situation au regard des dispositions fiscales applicables, ainsi que des recommandations pour sécuriser votre projet de réinvestissement.

---

### **1. Rappel des faits et du cadre juridique**
Votre holding a cédé les titres d’une société d’exploitation qu’elle détenait, **moins de trois ans après leur apport** par vos soins (opération initialement éligible au report d’imposition de l’article 150-0 B ter). Le produit de cession s’élève à **9 000 000 €**.

Vous envisagez de **réinvestir ce produit** dans une société dont l’activité consiste à **acheter des immeubles pour les rénover et les revendre** (activité de **marchand de biens** ou **promoteur immobilier**). L’enjeu est de déterminer si ce réinvestissement permet de **maintenir le report d’imposition**, conformément à l’article 150-0 B ter, I, 2° a) du CGI.

---

### **2. Conditions de maintien du report d’imposition**
Pour bénéficier du maintien du report, **trois conditions cumulatives** doivent être remplies (article 150-0 B ter, I, 2° a)) :

#### **a) Délai de réinvestissement**
- La holding doit **s’engager à investir le produit de cession** dans un délai de **2 ans à compter de la date de cession** (soit avant le **10 novembre 2027**).
- **60 % minimum du produit de cession** doit être réinvesti (soit **5 400 000 €** sur les 9 000 000 €).

#### **b) Nature de l’investissement**
Le réinvestissement doit concerner :
- Le **financement de moyens permanents d’exploitation** affectés à une **activité commerciale, industrielle, artisanale, libérale, agricole ou financière** (articles 34 ou 35 du CGI).
- **Exclusion expresse** : Les activités de **gestion du propre patrimoine mobilier ou immobilier** de la holding ne sont pas éligibles.

#### **c) Activité éligible**
L’activité de la société cible doit être **commerciale au sens de l’article 34 ou 35 du CGI**. Les activités immobilières peuvent être éligibles **sous conditions** :
- **Marchand de biens** (achat-revente d’immeubles) : **Oui**, car considérée comme une activité commerciale (article 35, I-1° du CGI).
- **Promotion immobilière** (construction pour revente) : **Oui**, également commerciale.
- **Location meublée** ou **gestion de patrimoine immobilier** : **Non**, car exclues par le texte.

**Votre projet** (achat-rénovation-revente d’immeubles) **semble donc éligible**, car il relève de l’activité de **marchand de biens**, considérée comme commerciale.

---

### **3. Points de vigilance et risques**
#### **a) Preuve de l’affectation des fonds**
- Le réinvestissement doit être **directement lié à l’activité commerciale** de la société cible (ex. : acquisition d’immeubles à rénover, financement de travaux, etc.).
- **Risque** : Si les fonds sont utilisés pour des actifs non directement liés à l’activité (ex. : trésorerie passive, acquisition d’un siège social non exploité), l’administration pourrait contester le maintien du report.

#### **b) Caractère "permanent" des moyens d’exploitation**
- Les actifs financés doivent être **affectés durablement** à l’activité (ex. : immeubles destinés à la revente, stocks de matériaux, etc.).
- **Exemple de non-éligibilité** : Un immeuble acquis pour être loué (même temporairement) avant revente pourrait être requalifié en gestion de patrimoine.

#### **c) Formalisme**
- La holding doit **prendre un engagement de réinvestissement** dans l’acte de cession ou dans une déclaration annexe (à joindre à la déclaration de revenus n° 2074).
- **Recommandation** : Conserver une **traçabilité comptable** des fonds réinvestis (ex. : comptes dédiés, justificatifs d’affectation).

#### **d) Contrôle fiscal**
- L’administration peut vérifier **a posteriori** (dans un délai de 3 ans) que les conditions sont remplies.
- **Sanction** : En cas de non-respect, le report est remis en cause avec **imposition immédiate** de la plus-value (taux de 30 % en 2025, soit **2 700 000 €** d’impôt + prélèvements sociaux).

---

### **4. Recommandations pratiques**
#### **a) Structuration du réinvestissement**
1. **Choisir une société cible** dont l’activité est **exclusivement commerciale** (marchand de biens ou promoteur).
   - Vérifier ses statuts et son objet social (mention explicite de l’achat-revente d’immeubles).
2. **Flécher les fonds** vers des actifs éligibles :
   - Acquisition d’immeubles à rénover/revendre.
   - Financement de travaux ou de stocks (matériaux, etc.).
3. **Éviter les actifs non éligibles** :
   - Immeubles de rapport (location).
   - Placements financiers ou trésorerie non affectée.

#### **b) Formalisation de l’engagement**
- **Rédiger un engagement écrit** (à annexer à la déclaration fiscale) précisant :
  - Le montant réinvesti (au moins 60 % du produit de cession).
  - La nature des actifs financés (ex. : "acquisition d’un immeuble situé [adresse] destiné à la revente après rénovation").
  - Le délai de réinvestissement (avant le 10/11/2027).

#### **c) Suivi comptable et fiscal**
- **Tenir une comptabilité distincte** pour les fonds réinvestis.
- **Conserver tous les justificatifs** (actes d’acquisition, factures de travaux, etc.) pendant 3 ans après la déclaration.

#### **d) Alternative : Réinvestissement dans une activité non immobilière**
Si le risque de requalification vous semble trop élevé, vous pourriez envisager un réinvestissement dans une **activité commerciale non immobilière** (ex. : acquisition d’une PME industrielle, financement d’une start-up, etc.), ce qui éliminerait tout débat sur l’éligibilité.

---

### **5. Conclusion et prochaines étapes**
Votre projet de réinvestissement dans une activité de **marchand de biens** **peut permettre de maintenir le report d’imposition**, sous réserve :
1. Du **respect du délai de 2 ans** (avant le 10/11/2027).
2. De l’**affectation des fonds à des actifs éligibles** (immeubles à rénover/revendre, travaux, etc.).
3. De la **formalisation d’un engagement clair** et de la **traçabilité des fonds**.

**Prochaines étapes proposées** :
- **Audit de la société cible** : Vérifier son objet social et son activité réelle.
- **Rédaction de l’engagement de réinvestissement** : À joindre à votre déclaration fiscale 2025.
- **Accompagnement comptable** : Mise en place d’une comptabilité dédiée aux fonds réinvestis.

Je reste à votre disposition pour approfondir ces points ou vous assister dans la mise en œuvre de cette stratégie. N’hésitez pas à me solliciter pour un rendez-vous afin d’affiner les modalités pratiques.

**Veuillez agréer, Cher Monsieur [Nom du client], l’expression de mes salutations distinguées.**

**[Votre Nom]**
Avocat fiscaliste
[Coordonnées du cabinet]

---
**Annexes** :
- Extrait de l’article 150-0 B ter du CGI.
- Modèle d’engagement de réinvestissement (sur demande).

---

## U26

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

**Note de consultation**

Monsieur le Gérant,

Vous m’interrogez, à la suite de la proposition de rectification reçue, sur le bien-fondé du taux de 5,5 % que vous avez appliqué sur la facture du 20 janvier 2025 (installation d’une chaudière, 8 500 € HT) dans une maison achevée depuis quinze ans et occupée par son propriétaire.

**1. Conditions posées par l’article 278-0 bis A, I du CGI (texte que vous m’avez communiqué)**

Trois conditions cumulatives doivent être réunies :

- locaux achevés depuis au moins deux ans : la maison a quinze ans, la condition est remplie (il faudra toutefois être en mesure de le justifier : acte de propriété, taxe foncière, permis de construire, etc.) ;
- locaux affectés ou destinés à être affectés à un usage d’habitation à l’issue des travaux : occupation par le propriétaire, condition remplie ;
- prestation portant sur la pose/installation d’équipements ayant pour objet d’économiser l’énergie par l’amélioration du chauffage : l’installation d’une chaudière entre dans le champ du b) du 3°.

Sur le seul fondement du texte que vous m’avez transmis, le taux de 5,5 % paraît donc applicable.

**2. Points de vigilance (qui expliquent probablement le redressement à 20 %)**

Le I de l’article 278-0 bis A n’est pas autosuffisant. Les équipements doivent en outre respecter des caractéristiques et performances minimales fixées par arrêté. Toutes les chaudières n’y figurent pas (seules certaines chaudières à très haute performance énergétique, selon le combustible et le rendement, sont éligibles au 5,5 %). Une chaudière « standard » relève du taux intermédiaire de 10 % (art. 279-0 bis), pas du 20 %.

Par ailleurs, l’application du taux réduit (5,5 % ou 10 %) est subordonnée à la détention, avant facturation, de l’attestation simplifiée (ou normale) établie par le client. En l’absence d’attestation régulière, l’administration est fondée à revendiquer le taux normal de 20 % à votre encontre.

**3. Conséquence pratique**

- Si la chaudière répond aux critères techniques de l’arrêté et si vous détenez l’attestation : le 5,5 % est correct. Il convient de contester intégralement le rappel.
- Si la chaudière n’est pas éligible au 5,5 % mais que les autres conditions des travaux dans un logement de plus de deux ans sont réunies et que l’attestation a été recueillie : le taux applicable est 10 %. Le rappel ne peut porter que sur la différence 5,5 / 10 %, pas sur la différence 5,5 / 20 %.
- En l’absence d’attestation : le 20 % est plus difficile à écarter, même si l’on peut tenter de démontrer la réalité des conditions de fond.

**Suite à donner**

Adressez-moi dès que possible :
- la proposition de rectification complète,
- la facture et le devis,
- l’attestation client (si elle existe),
- la marque, le modèle et la fiche technique de la chaudière,
- tout élément sur l’ancienneté et l’affectation du logement.

Je pourrai alors rédiger les observations dans le délai de 30 jours et, le cas échéant, limiter très sensiblement le rappel (voire l’anéantir).

Je reste à votre disposition.

Bien cordialement,

---

## U27

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

**Objet : Consultation fiscale – Application du taux réduit de TVA (5,5 %) sur travaux de rénovation énergétique**

Cher client,

Suite à votre consultation concernant la proposition de rectification notifiée par l'administration fiscale à votre entreprise de plomberie, j'ai examiné les éléments du dossier à l'aune du texte légal que vous m'avez transmis (CGI, art. 278-0 bis A, I).

À la lecture de ces éléments, **je vous confirme que l'application du taux réduit de TVA à 5,5 % sur ce chantier était parfaitement correcte.** 

L'administration fiscale se trompe et sa proposition de rectification doit être contestée. Voici l'analyse juridique qui fonde notre position :

**1. Sur l'ancienneté du local (Condition 1°)**
Le texte exige que les prestations soient effectuées dans des locaux achevés depuis au moins deux ans. En l'espèce, la maison dans laquelle vous avez intervenu est âgée de quinze ans. Cette condition est donc largement remplie.

**2. Sur l'affectation du local (Condition 2°)**
Le texte exige que les locaux soient affectés ou destinés à l'habitation. Vous m'indiquez que la maison est occupée par son propriétaire. Il s'agit donc indéniablement d'un local à usage d'habitation. Cette condition est satisfaite.

**3. Sur la nature des travaux (Condition 3°)**
Le texte subordonne le taux réduit aux prestations portant sur la pose, l'installation ou l'adaptation d'équipements ayant pour objet d'économiser l'énergie ou de recourir à des énergies renouvelables, notamment par l'amélioration du chauffage (b) et de la production d'eau chaude sanitaire (c). 
En l'espèce, vous avez procédé à l'installation d'une chaudière. Cet équipement relève directement de l'amélioration du système de chauffage et/ou de la production d'eau chaude sanitaire du logement. La nature des travaux réalisés entre donc strictement dans le champ d'application du taux réduit.

**Conclusions et recommandations :**

L'ensemble des conditions cumulatives prévues par l'article 278-0 bis A du CGI étant réuni, la facturation de ces travaux au taux de 5,5 % pour un montant de 8 500 euros HT est régulière. Le redressement visant à réclamer la différence avec le taux normal de 20 % est infondé.

**Mesures à prendre :**
1. **Ne pas accepter le redressement :** Il est impératif de ne pas acquitter la somme réclamée et de ne pas signer l'accord tacite proposé par l'administration.
2. **Respecter le délai de réponse :** Vous disposez d'un délai de 30 jours (généralement) à compter de la réception de la proposition de rectification pour formuler vos observations. 
3. **Constitution du dossier de preuve :** Je vous invite à me transmettre dès que possible les documents suivants afin que je puisse rédiger votre réponse à l'administration :
   * La copie de la proposition de rectification reçue.
   * La facture du 20 janvier 2025.
   * Une attestation sur l'honneur du propriétaire de la maison (ou tout document cadastral/acte de propriété) justifiant que la construction date de plus de 15 ans et qu'il s'agit de son habitation.
   * La documentation technique de la chaudière installée (prouvant qu'elle relève du chauffage/production d'eau chaude).

Dès réception de ces pièces, je me chargerai de rédiger les observations contradictoires à adresser à l'inspecteur des finances publiques afin de faire valoir vos droits et d'obtenir la décharge totale de ce redressement.

Je reste à votre entière disposition pour toute précision.

Bien cordialement,

**[Votre Nom]**  
*Avocat à la Cour*  
*Spécialiste en droit fiscal*

---

## U28

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
#### **2.1. Principe général : RAS sur les revenus de capitaux mobiliers (RCM)**
L’**article 119 bis, 2 du CGI** prévoit qu’une **retenue à la source (RAS) est due** sur les produits visés aux articles 108 à 117 bis (dont les dividendes) **lorsque le bénéficiaire effectif est une personne n’ayant pas son domicile fiscal ou son siège en France**, sauf exceptions.

Le taux de la RAS est fixé par l’**article 187 du CGI** (généralement **30 %** pour les dividendes, sous réserve de conventions fiscales).

#### **2.2. Exceptions à la RAS**
L’article 119 bis, 2 du CGI exclut la RAS pour certains bénéficiaires, notamment :
- Les **organismes de placement collectif (OPC)** situés dans un État membre de l’UE ou un État ayant conclu une convention d’assistance administrative avec la France (ce qui n’est pas le cas ici, la Mère étant une SA luxembourgeoise classique).
- **Les sociétés mères au sens de la directive mère-fille (2011/96/UE)** : Cette directive, transposée en droit français par l’**article 119 ter du CGI**, **exonère de RAS les dividendes distribués à une société mère résidente dans l’UE**, sous conditions.

---

### **3. Application à votre situation**
#### **3.1. La Mère est-elle éligible à l’exonération de la directive mère-fille ?**
Pour bénéficier de l’exonération de RAS, **trois conditions cumulatives** doivent être remplies (art. 119 ter du CGI) :
1. **La Mère doit être une "société mère"** :
   - Elle détient **au moins 10 % du capital** de la Filiale (ici, 100 %, donc condition remplie).
   - **Durée minimale de détention** : La participation doit être détenue **depuis au moins 2 ans** (ici, 5 ans, donc condition remplie).

2. **La Mère doit être soumise à l’impôt sur les sociétés dans un État membre de l’UE** :
   - Le Luxembourg est un État membre de l’UE.
   - La Mère est une SA soumise à l’**impôt sur les sociétés luxembourgeois (ISOC)**, donc condition remplie.

3. **La Mère doit être considérée comme le "bénéficiaire effectif"** des dividendes :
   - Aucune indication ne suggère une interposition abusive (ex. : société écran). Sous réserve de confirmation, cette condition semble remplie.

**→ Conclusion partielle** : La Mère remplit **a priori** les conditions de l’article 119 ter du CGI, ce qui **exonère la distribution de RAS française**.

#### **3.2. Vérification des autres exceptions**
- **Convention fiscale franco-luxembourgeoise** :
  La convention du **1er avril 2020** (entrée en vigueur en 2022) prévoit à son **article 10 (Dividendes)** :
  - Une **RAS maximale de 5 %** si le bénéficiaire effectif est une société détenant **au moins 10 % du capital** (ici, 100 %).
  - **0 % de RAS** si la société mère détient **au moins 95 % du capital** (ce qui est votre cas).

  **→ La convention est plus favorable que la directive mère-fille** (qui exonère déjà la RAS), mais confirme l’absence de RAS dans votre situation.

- **Régime des sociétés mères et filiales (art. 145 du CGI)** :
  Ce régime concerne l’**exonération d’IS** pour la Filiale sur les dividendes reçus, et non la RAS. Irrelevant ici.

---

### **4. Conclusion et recommandations**
#### **4.1. Pas de retenue à la source applicable**
Au regard :
1. De la **directive mère-fille (art. 119 ter CGI)** → **Exonération de RAS**.
2. De la **convention franco-luxembourgeoise (art. 10)** → **Taux de 0 %** (détention > 95 %).

**→ Aucune retenue à la source française n’est due** sur la distribution de 20 000 000 € à la Mère luxembourgeoise.

#### **4.2. Formalités à respecter**
- **Justificatifs à fournir** :
  - **Attestation de résidence fiscale** de la Mère (delivrée par l’administration luxembourgeoise) prouvant qu’elle est soumise à l’ISOC au Luxembourg.
  - **Preuve de la détention de 100 % du capital depuis 5 ans** (registre des actionnaires, statuts, etc.).
  - **Déclaration sur l’honneur** confirmant que la Mère est le bénéficiaire effectif (pas de structure interposée).

- **Déclaration fiscale** :
  - La Filiale doit **mentionner la distribution dans sa déclaration de résultats (liasse fiscale)** et cocher la case correspondant à l’exonération (case 8UU ou équivalente, selon le formulaire en vigueur en 2025).

#### **4.3. Points de vigilance**
- **Bénéficiaire effectif** : Si la Mère est une simple holding passive sans substance économique, l’administration française pourrait contester son statut de bénéficiaire effectif (risque de **requalification en abus de droit**).
- **Évolution législative** : Vérifier que les textes (CGI, convention) n’ont pas été modifiés avant juin 2025.

---

### **5. Synthèse**
| Critère | Analyse | Résultat |
|---------|---------|----------|
| **Bénéficiaire non résident** | Mère luxembourgeoise | RAS applicable en principe (art. 119 bis, 2 CGI) |
| **Exception directive mère-fille** | Détention > 10 % depuis > 2 ans + ISOC UE | **Exonération de RAS** (art. 119 ter CGI) |
| **Convention franco-luxembourgeoise** | Détention > 95 % | **Taux de 0 %** (art. 10) |
| **Conclusion** | **Aucune RAS n’est due** | **Distribution exonérée** |

---
**Recommandation finale** :
La distribution peut être effectuée **sans retenue à la source française**, sous réserve de :
1. Conserver les justificatifs de détention et de résidence fiscale.
2. Déclarer correctement l’opération dans la liasse fiscale 2025.
3. S’assurer que la Mère est bien le bénéficiaire effectif (pas de montage abusif).

**Prochaines étapes** :
- Nous pouvons rédiger une **note de synthèse** pour votre service comptable.
- Si nécessaire, solliciter un **rescrit fiscal** pour sécuriser la position (bien que le cas semble clair).

N’hésitez pas à me solliciter pour toute précision complémentaire.

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Cabinet X]

---

## U29

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

**Note de consultation — report d’imposition (CGI, art. 150-0 B ter)**

La cession intervenue en février 2026, moins de trois ans après l’apport, met fin au report d’imposition **sauf** si la holding prend l’engagement de réinvestir, dans les trois ans de la cession (soit jusqu’en février 2029) et à hauteur d’**au moins 70 %** du produit (soit **6 300 000 €**), dans le financement de moyens permanents d’exploitation affectés à **son** activité éligible.

L’activité doit correspondre à celle visée au 3° du C du I de l’article 199 terdecies-0 A (commerciale, industrielle, artisanale, libérale ou agricole, dans les conditions de ce texte). Sont expressément exclues les activités de gestion de son propre patrimoine immobilier. Un simple placement de trésorerie, l’acquisition d’immeubles de rapport ou le maintien d’une activité purement patrimoniale/holding ne suffit pas.

**Conséquences pratiques immédiates**
- La holding doit formaliser l’engagement (déclaration de l’année de cession et suivi ultérieur). À défaut, ou si le réinvestissement n’est pas réalisé dans les conditions et délais, le report tombe : la plus-value d’apport redevient imposable entre vos mains (avec les conséquences en droits et, le cas échéant, intérêts de retard).
- Les 30 % restants (2 700 000 €) peuvent être utilisés plus librement (distribution, autre emploi). Une distribution générera toutefois une imposition à l’IR/PS entre vos mains.
- Les « moyens permanents d’exploitation » s’entendent principalement d’immobilisations affectées durablement à l’activité opérationnelle de la holding elle-même (fonds, matériel, locaux d’exploitation, etc.). L’acquisition de titres d’une autre société n’entre pas dans le a) du texte que vous m’avez soumis.

**Recommandations**
1. Qualifiez dès maintenant l’activité que la holding exercera effectivement (création, acquisition d’un fonds, développement d’une activité opérationnelle). Sans activité éligible propre, le réinvestissement au titre du a) est inopérant.
2. Identifiez et documentez les investissements éligibles avant toute immobilisation des fonds. Conservez la traçabilité du produit de cession.
3. Ne procédez à aucune distribution ou emploi non conforme des 70 % avant validation de l’éligibilité.
4. Anticipez le suivi déclaratif et la justification à l’administration (engagement, réalisation, affectation, conservation).

Je vous propose un rendez-vous rapide pour examiner les projets d’investissement envisagés, vérifier leur éligibilité au regard du texte et de la doctrine, et préparer l’engagement ainsi que le calendrier. Transmettez-moi les éléments de la cession (acte, valorisation, déclaration d’apport initiale) et tout projet déjà identifié.

Restant à votre disposition.

---

## U30

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

**Note de consultation – Cession de parts de SCI – Droits d'enregistrement**

---

## 1. Qualification : société à prépondérance immobilière

La SCI remplit les deux conditions cumulatives de l'article 726, I, 2° du CGI :

- **Titres non admis aux négociations** sur un marché réglementé ou un système multilatéral de négociation : c'est le cas de toute SCI classique ;
- **Actif principalement constitué d'immeubles situés en France** : avec 80 % de l'actif en immeubles français, le seuil de prépondérance (> 50 %) est largement franchi.

**Point de vigilance avant signature** : le texte vise l'actif tel qu'il « est, **ou a été au cours de l'année précédant la cession** ». Il faut donc vérifier la composition de l'actif non seulement au 20 septembre 2023, mais aussi sur les douze mois précédents. Si la société a, par exemple, cédé un immeuble il y a huit mois et détient temporairement la liquidité du prix, la prépondérance immobilière peut être caractérisée sur cette période même si elle ne l'est plus au jour de la cession. Je recommande de faire figurer un état de l'actif en annexe de l'acte.

La société n'entre dans aucune des exclusions (HLM, société foncière, SEM de logement social).

## 2. Droit d'enregistrement dû

**Taux : 5 %** (art. 726, I, 2° CGI).

**Assiette : le prix de cession en totalité, sans aucun abattement.** C'est un point essentiel : l'abattement de 23 000 € ne s'applique qu'aux cessions de parts sociales taxées à 3 % (1° du même article). Il est **exclu** pour les participations dans des personnes morales à prépondérance immobilière. L'assiette est le prix stipulé ou, si elle est supérieure, la valeur vénale réelle des titres au jour de la cession.

**Calcul :**

| Élément | Montant |
|---|---|
| Prix de cession | 4 000 000 € |
| Taux | 5 % |
| **Droit d'enregistrement** | **200 000 €** |

**Redevable** : l'acquéreur, sauf clause contraire de prise en charge par le cédant (à trancher dans la négociation — cela a une incidence économique et parfois fiscale sur la plus-value).

## 3. Formalités

- **Enregistrement dans le délai d'un mois** de la date de l'acte (art. 635 CGI), soit au plus tard le **20 octobre 2023**, auprès du service des impôts des entreprises compétent. Paiement du droit lors de l'enregistrement.
- **Hypothèse particulière** : si la cession était réalisée **à l'étranger**, le texte impose qu'elle soit constatée **dans le délai d'un mois par un acte authentique reçu par un notaire exerçant en France**. Si la signature a lieu en France, cette formalité ne s'applique pas, mais il faut le vérifier si l'une des parties envisage de signer hors de France.

## 4. Contenu de l'acte

L'acte (sous seing privé suffisant si signé en France, l'authenticité n'étant requise que pour les cessions réalisées à l'étranger) doit comporter :

1. **Date et lieu** de signature ;
2. **Identité et domicile complets des parties** (cédant et acquéreur) ;
3. **Identification de la société** : dénomination, forme, siège social, numéro RCS ;
4. **Désignation précise des titres cédés** : nombre de parts, numérotation le cas échéant, quote-part du capital ;
5. **Prix de cession** (4 000 000 €) et modalités de paiement ;
6. **Origine de propriété du cédant** (titre d'acquisition des parts) ;
7. **Mention expresse de la qualification de personne morale à prépondérance immobilière**, avec un état de la composition de l'actif (idéalement annexé) justifiant l'application du taux de 5 % — cela sécurise l'enregistrement et prévient toute discussion ultérieure avec le service ;
8. **Stipulation de la charge des droits** (acquéreur, sauf convention contraire) ;
9. Le cas échéant, les clauses usuelles : garantie d'actif et de passif, répartition du résultat de l'exercice en cours, prise d'effet et transfert de jouissance.

## 5. Recommandations

- Faire établir un **état certifié de l'actif** à la date de cession et sur l'année écoulée (bilan ou attestation de l'expert-comptable) ;
- Vérifier la **valeur vénale** des titres : si le prix de 4 M€ est manifestement inférieur à la valeur réelle (actif net réévalué des immeubles), l'administration pourrait rehausser l'assiette ;
- Anticiper le financement des 200 000 € de droits par l'acquéreur dès la signature ;
- Rappel : la plus-value du cédant relève d'un régime distinct (impôt sur le revenu ou IS selon sa qualité) — à traiter séparément si vous le souhaitez.

Je reste à votre disposition pour revoir le projet d'acte avant signature.

---

## U31

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

**Objet : Analyse du report d’imposition dans le cadre de la cession de titres par votre holding – Application de l’article 150-0 B ter du CGI**

**À l’attention de [Nom du Client],**
**De la part de [Votre Nom], Avocat Fiscaliste**

---

### **1. Contexte et problématique**
Votre holding (détentrice à 100 % des titres) a cédé le **10 mars 2026** des titres d’une société d’exploitation pour un montant de **9 000 000 €**, moins de **3 ans** après leur apport par vos soins. Vous envisagez de **réinvestir** ce produit dans une société dédiée à l’**achat, rénovation et revente d’immeubles**, et souhaitez savoir si ce remploi permet de **maintenir le report d’imposition** prévu à l’article **150-0 B ter, I, 2° du CGI**.

---

### **2. Rappel du régime de report d’imposition (apport de titres)**
L’**apport de titres** à une holding peut bénéficier d’un **report d’imposition** de la plus-value réalisée (art. 150-0 B ter du CGI), sous réserve que :
- La holding **contrôle** la société dont les titres sont apportés (ce qui est votre cas, à 100 %).
- Les titres sont **conservés** par la holding pendant **au moins 3 ans** à compter de l’apport.

**Exception** : Si la holding cède les titres **dans les 3 ans**, le report est **remis en cause**… **sauf** si elle prend l’engagement de **réinvestir** le produit de cession selon les conditions de l’**article 150-0 B ter, I, 2°, alinéa 2**.

---

### **3. Conditions du remploi dérogatoire (art. 150-0 B ter, I, 2°)**
Pour éviter la **remise en cause du report**, la holding doit :
1. **Céder les titres dans les 3 ans** de l’apport (votre cas : cession le 10/03/2026, soit < 3 ans après l’apport).
2. **Prendre l’engagement** de réinvestir **au moins 70 % du produit de cession** (soit **6 300 000 €** minimum sur 9 000 000 €).
3. **Réinvestir dans un délai de 3 ans** à compter de la cession (soit avant le **10 mars 2029**).
4. **Affecter les fonds** à :
   - **Le financement de moyens permanents d’exploitation** liés à une **activité éligible** (art. 199 terdecies-0 A, 3° du C du I).
   - **Exclusion expresse** : Les **activités de gestion de patrimoine immobilier** (location, etc.) **ne sont pas éligibles**.

---

### **4. Analyse de votre projet de réinvestissement**
Votre projet consiste à investir dans une société qui :
- **Achte des immeubles**,
- **Les rénove**,
- **Les revend**.

#### **→ Qualification de l’activité**
- **Activité de marchand de biens** (achat-revente) :
  - **Non éligible** au report, car considérée comme une **activité de gestion de patrimoine immobilier** (même si elle inclut de la rénovation).
  - **Référence** : L’article **150-0 B ter, I, 2°, a)** exclut explicitement *"les activités de gestion de son propre patrimoine immobilier"*.
  - **Jurisprudence et doctrine** : L’administration fiscale (BOI-RPPM-PVBMC-20-20-30-10, § 120) et la jurisprudence (CE, 8 juillet 2020, n° 435215) considèrent que l’**achat-revente d’immeubles** (même avec travaux) relève de la **gestion de patrimoine**, sauf si l’activité est **industrielle ou commerciale à part entière** (ex. : promotion immobilière avec construction neuve).

- **Activité de rénovation** :
  - Si la société se limite à **rénover pour revendre**, sans transformation profonde (ex. : changement de destination), elle reste dans le champ de la **gestion de patrimoine**.
  - Pour être éligible, il faudrait une **activité industrielle ou commerciale distincte** (ex. : division en lots, construction neuve, etc.), ce qui ne semble pas être votre cas.

#### **→ Conclusion sur l’éligibilité**
Votre projet **ne semble pas éligible** au report d’imposition, car :
❌ L’**achat-revente d’immeubles** (même avec rénovation) est **exclu** par l’article 150-0 B ter.
❌ La **gestion de patrimoine immobilier** est **expressément visée** par l’exclusion.

---

### **5. Solutions alternatives pour maintenir le report**
Si vous souhaitez **conserver le report**, voici des pistes **éligibles** :

#### **A. Réinvestir dans une activité éligible (art. 199 terdecies-0 A, 3° du C du I)**
Exemples d’activités **non exclues** :
- **Activité industrielle, commerciale ou artisanale** (ex. : usine, commerce, service).
- **Activité agricole** (sous conditions).
- **Activité de location meublée** (si **non considérée comme gestion de patrimoine** – à analyser au cas par cas).

#### **B. Structurer différemment le réinvestissement**
- **Créer une société opérationnelle** (ex. : société de production, de services) et y injecter les fonds.
- **Éviter toute activité liée à l’immobilier** (sauf si **promotion immobilière avec construction neuve**, sous réserve de qualification).

#### **C. Reporter la cession au-delà de 3 ans**
- Si possible, **attendre mars 2027** (3 ans après l’apport) pour céder les titres **sans condition de remploi**.

---

### **6. Conséquences fiscales en cas de réinvestissement non éligible**
Si vous réinvestissez dans l’**achat-revente d’immeubles** :
- **Le report d’imposition est remis en cause** :
  - La **plus-value latente** sur l’apport initial devient **imposable immédiatement** (au taux de **30 %** PFU ou barème progressif + 17,2 % PS).
  - **Pénalités** possibles en cas de **manquement à l’engagement de remploi** (majoration de 10 % ou 40 % en cas de mauvaise foi).

---

### **7. Recommandations**
1. **Vérifier la qualification exacte de l’activité** :
   - Si la société de réinvestissement a une **activité mixte** (ex. : rénovation lourde + transformation en logements sociaux), une analyse fine est nécessaire.
   - **Consulter l’administration** (rescrit fiscal) pour sécuriser le montage.

2. **Envisager un réinvestissement dans une activité éligible** :
   - Exemple : **Société de production, de services, ou de commerce** (hors immobilier).

3. **Documenter l’engagement de remploi** :
   - Si vous optez pour une activité éligible, **rédaction d’un engagement écrit** (à joindre à la déclaration fiscale).

4. **Anticiper les délais** :
   - Le réinvestissement doit être **effectué avant le 10 mars 2029**.

---

### **8. Prochaines étapes**
Pour affiner l’analyse, je vous propose :
✅ **Un examen des statuts et de l’activité exacte** de la société de réinvestissement.
✅ **Une simulation fiscale** pour évaluer l’impact en cas de remise en cause du report.
✅ **Une demande de rescrit** à la DGFiP pour sécuriser le montage.

**Je reste à votre disposition pour en discuter plus en détail et vous accompagner dans la structuration optimale.**

**Cordialement,**
**[Votre Nom]**
Avocat Fiscaliste
[Coordonnées du cabinet]

---
**Annexe : Extrait de l’article 150-0 B ter du CGI (version applicable en 2026)**
> *"2° De la cession à titre onéreux, du rachat, du remboursement ou de l'annulation des titres apportés, si cet événement intervient dans un délai, décompté de date à date, de trois ans à compter de l'apport des titres. Toutefois, il n'est pas mis fin au report d'imposition lorsque la société bénéficiaire de l'apport cède les titres dans un délai de trois ans à compter de la date de l'apport et prend l'engagement d'investir le produit de leur cession, dans un délai de trois ans à compter de la date de la cession et à hauteur d'au moins 70 % du montant de ce produit :
> a) Dans le financement de moyens permanents d'exploitation affectés à son activité définie au 3° du C du I de l'article 199 terdecies-0 A. Les activités de gestion de son propre patrimoine immobilier sont également exclues du bénéfice de cette dérogation ;"*

---

## U32

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

# NOTE AU DOSSIER — Retenue à la source sur distribution de dividendes

**Faits** : Distribution de 20 000 000 € par une société française à sa société mère luxembourgeoise (SA, détention de 100 % depuis 5 ans, soumise à l'IRC) — mise en paiement le 15 juin 2025.

**En résumé** : En principe, la retenue à la source de droit commun (25 %) s'applique. **En l'espèce, aucune retenue n'est due**, la distribution remplissant *a priori* toutes les conditions de l'exonération du régime mère-fille prévue à l'article 119 ter du CGI. Cette exonération doit toutefois être **sécurisée et documentée**, le risque fiscal pesant sur la société distributrice française.

---

## I. Le principe : une retenue à la source de 25 %

Les dividendes (produits visés aux articles 108 à 117 bis CGI) mis en paiement au profit d'un bénéficiaire effectif n'ayant pas son siège en France donnent lieu à la retenue à la source de l'article 119 bis, 2, dont le taux est fixé par l'article 187, 2 : **25 %** (taux aligné sur le taux normal de l'IS).

- **Fait générateur / exigibilité** : la mise en paiement, soit le 15 juin 2025.
- **Enjeu théorique** : 20 M€ × 25 % = **5 000 000 €**.
- **Redevable** : la société française distributrice, qui devrait reverser la retenue dans les quinze premiers jours du mois suivant la mise en paiement (soit avant le 15 juillet 2025) auprès du service des impôts des non-résidents.

## II. L'exonération du régime mère-fille (art. 119 ter CGI)

L'article 119 ter, transposant la directive 2011/96/UE, dispense de toute retenue les dividendes distribués à une société mère établie dans l'UE. Vérification des conditions au cas d'espèce :

| Condition | Analyse |
|---|---|
| Siège de direction effective dans un État membre de l'UE | ✔ Luxembourg (à confirmer : direction effective réellement au Luxembourg, sans déport du siège effectif hors UE par une convention) |
| Forme sociale visée par l'annexe de la directive | ✔ Société anonyme |
| Assujettissement à l'IS local, sans possibilité d'option ni exonération | ✔ Soumission à l'IRC — **à vérifier** : ne pas être un véhicule exonéré (SPF, SICAR, OPC…) ; le fait que les dividendes soient exonérés au Luxembourg est sans incidence, l'exigence portant sur l'assujettissement de la personne morale |
| Participation ≥ 10 % du capital de la distributrice | ✔ 100 % |
| Détention ≥ 2 ans (ou engagement de conservation) | ✔ 5 ans |
| Qualité de bénéficiaire effectif des dividendes | ✔ *A priori* — voir points de vigilance infra |
| Absence de montage relevant de la procédure d'abus de droit (L. 64 A LPF) | À documenter — voir infra |

Toutes les conditions étant remplies à la date de mise en paiement, **la retenue à la source ne s'applique pas**.

## III. Sécurisation de l'opération (à mettre en œuvre avant le 15 juin 2025)

L'exonération s'applique sans autorisation préalable, mais la société française, en tant que redevable potentiel, doit être en mesure de **justifier des conditions** en cas de contrôle :

1. **Recueillir une attestation** de la société mère (selon la doctrine administrative, BOI-RPPM-RCM-30-30-20-40) certifiant : siège de direction effective au Luxembourg, forme SA, assujettissement à l'IRC sans option ni exonération, détention de 100 % depuis plus de deux ans, qualité de bénéficiaire effectif, absence de montage abusif.
2. **Conserver les pièces justificatives** : extrait RCS luxembourgeois, statuts, attestation de résidence fiscale, derniers comptes approuvés.
3. **Formalité déclarative** : la distribution devra être reportée sur l'**IFU (imprimé n° 2561)**, à déposer au plus tard le 15 mars 2026, même en l'absence de retenue.
4. **Aucun reversement** (pas de relevé 2777-SD) n'est à effectuer si l'exonération s'applique.

## IV. Points de vigilance

- **Qualité de bénéficiaire effectif / substance** : la jurisprudence de la CJUE (affaires danoises, 26 février 2019) et la clause anti-abus interne exposent l'opération à une remise en cause si la société mère était une simple société « conduite » (notamment si elle est elle-même détenue par un groupe hors UE et redistribue quasi intégralement le produit sans substance économique). Il convient de documenter sa substance (gouvernance, moyens, finalité économique). Rien dans les faits rapportés ne suggère une telle configuration, mais ce point doit être **confirmé avant la mise en paiement**.
- **Sanctions en cas de requalification** : la retenue (5 M€) serait recouvrée contre la société française, assortie de l'intérêt de retard et, le cas échéant, des pénalités de 40 % voire 80 % propres à la procédure d'abus de droit.
- **Aspect extra-fiscal** : vérifier l'existence de sommes distribuables (droit des sociétés) au regard des capitaux propres après cession de l'actif.

## V. Filet de sécurité subsidiaire

Si, par hypothèse, l'exonération de l'article 119 ter devait être écartée, la **convention franco-luxembourgeoise du 20 mars 2018** (applicable depuis le 1er janvier 2020) prévoit également l'**exonération totale** des dividendes dont le bénéficiaire effectif est une société détenant directement au moins 5 % du capital pendant une période de 365 jours incluant le jour du paiement — conditions ici remplies (sous réserve de la clause anti-abus PPT). À défaut, le taux conventionnel serait de 15 %.

---

## Conclusion

**Aucune retenue à la source n'est due** sur la distribution de 20 000 000 € mise en paiement le 15 juin 2025, dès lors que les conditions de l'article 119 ter CGI sont satisfaites — ce qui apparaît être le cas. Je recommande toutefois, avant le 15 juin 2025 : (i) la confirmation écrite de l'assujettissement effectif de la société mère à l'IRC et de sa qualité de bénéficiaire effectif, (ii) la collecte de l'attestation et des justificatifs, (iii) la déclaration de la distribution sur l'IFU. Souhaitez-vous que nous préparions le modèle d'attestation et revérifiions la structure de détention en amont au Luxembourg ?

---

## U33

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

Bonjour, je vous remercie de me consulter avant de signer l'acte de cession des titres de votre société civile immobilière.

Après analyse de la situation, il apparaît que la société dont vous cédez les titres est une personne morale à prépondérance immobilière au sens de l'article 726, I, 2° du Code Général des Impôts (CGI), puisque son actif est constitué à 80 % d'immeubles situés en France et que ses droits sociaux ne sont pas négociés sur un marché réglementé.

Par conséquent, la cession de ces titres est soumise au droit d'enregistrement prévu par l'article 726, I, 2° du CGI, soit un taux de 5 %.

Le montant du droit d'enregistrement dû sera donc de 5 % de 4 000 000 euros, soit 200 000 euros.

En outre, l'article 726, III, B du CGI prévoit que l'acte de cession doit contenir certaines mentions expresses, à savoir :

1. si la personne morale est une société mentionnée à l'article 1655 ter du CGI (société dont les titres ne sont pas négociés sur un marché réglementé) ;
2. si les participations cédées confèrent au cessionnaire, direct ou indirect, le droit à la jouissance d'immeubles ou de fractions d'immeubles au sens de l'article 728 du CGI ;
3. si le cessionnaire a acquitté ou s'engage à acquitter, directement ou indirectement, des dettes contractées auprès du cédant par cette personne morale, en précisant, le cas échéant, leur montant.

Il est donc essentiel que l'acte de cession que vous allez signer le 20 mars 2024 contienne ces mentions expresses.

Je vous recommande de vérifier avec le notaire qui recevra l'acte que ces mentions seront bien incluses dans l'acte, et de vous assurer que le droit d'enregistrement sera acquitté conformément aux dispositions de l'article 726 du CGI.

N'hésitez pas à me poser d'autres questions si vous avez besoin de précisions supplémentaires.

---

## U34

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

**Objet : Consultation fiscale – Application du taux de TVA à 5,5 % sur travaux de rénovation énergétique (facture du 20/01/2025)**

Monsieur le Gérant,

Je vous remercie de m’avoir soumis la proposition de rectification notifiée à votre entreprise. Après analyse des éléments factuels et du cadre légal applicable à la date des travaux, je vous livre ci-dessous mon appréciation juridique et les suites à privilégier.

### 🔍 1. Analyse au regard de l’article 278-0 bis A du CGI
Le taux réduit de 5,5 % s’applique aux prestations de rénovation énergétique remplissant **cumulativement** les trois conditions énoncées par le texte que vous m’avez communiqué. Sur la base des informations fournies :

| Condition | Vérification | Conclusion |
|-----------|--------------|------------|
| 1° Local achevé depuis ≥ 2 ans | Maison de 15 ans | ✅ Remplie |
| 2° Usage d’habitation | Occupée par son propriétaire | ✅ Remplie |
| 3° Amélioration du chauffage/ventilation/ECS | Installation d’une chaudière | ✅ Remplie en principe |

**En première analyse, l’application du taux de 5,5 % apparaît donc justifiée.**

### ⚠️ 2. Pourquoi l’administration conteste-t-elle ce taux ?
En pratique, les requalifications au taux normal de 20 % sur ce type de dossier reposent rarement sur les conditions de base, mais sur des **exigences substantielles ou formelles non satisfaites** :

1. **Nature et performance de l’équipement** : Le taux de 5,5 % est réservé aux matériels contribuant *effectivement* à des économies d’énergie. L’administration exige généralement une chaudière à condensation, une pompe à chaleur, un système biomasse ou tout équipement répondant aux critères de performance énergétique en vigueur. Un remplacement par un modèle standard non performant peut justifier le taux de 20 %.
2. **Attestation du client** : L’application du taux réduit est subordonnée à la détention, avant facturation, de l’attestation de simplification (Cerfa n° 12816*04) signée par le maître d’ouvrage, confirmant l’ancienneté du local, sa destination d’habitation et le caractère des travaux. Son absence ou son irrégularité entraîne systématiquement la requalification.
3. **Mentions obligatoires sur la facture** : La facture doit explicitement mentionner le taux de 5,5 %, la référence à l’article 278-0 bis A du CGI, et détailler la nature des travaux (pose/adaptation d’un équipement d’amélioration du chauffage).
4. **Qualification « remplacement à l’identique »** : Si la chaudière installée présente les mêmes caractéristiques énergétiques que l’ancienne, l’administration peut considérer qu’il n’y a pas d’« amélioration » au sens du 3° b), et appliquer le taux de 20 %.

### 📂 3. Documents à me transmettre sans délai
Afin de préparer une réponse argumentée à la proposition de rectification (délai de réponse : 30 jours à compter de la notification), je vous prie de me faire parvenir :
- La facture du 20/01/2025 (version définitive)
- Le devis signé et le bon de commande
- La fiche technique / certificat de performance de la chaudière installée
- L’attestation de simplification signée par le client
- Toute preuve de l’état antérieur (photos, rapport de diagnostic, ancien équipement)
- Le courrier de proposition de rectification et ses annexes

### 🛡️ 4. Stratégie recommandée
- **Si le dossier est complet et conforme** : Nous répondrons à l’administration en contestant le bien-fondé du rappel, en joignant les pièces justificatives et en rappelant la doctrine administrative (BOI-TVA-LIQ-30-20-10) qui valide le taux de 5,5 % dès lors que les conditions sont remplies et documentées.
- **Si une irrégularité est constatée** (attestation manquante, chaudière non performante, mentions insuffisantes) : Nous étudierons la possibilité d’une régularisation spontanée, assortie d’une demande de remise gracieuse des pénalités et, le cas échéant, d’un échéancier de paiement.
- **Dans tous les cas** : Je veillerai à préserver vos droits de défense, à respecter les délais légaux et à éviter toute aggravation de la situation (majorations, intérêts de retard).

Je reste à votre disposition pour examiner le dossier complet et rédiger la réponse à l’administration dans les meilleurs délais. Vous pouvez me transmettre les pièces par voie sécurisée ou les déposer à mon cabinet.

Je vous prie d’agréer, Monsieur le Gérant, l’expression de ma considération distinguée.

**[Votre Nom]**  
Avocat au Barreau de [Ville]  
Spécialiste en droit fiscal des entreprises  
[Coordonnées]

---

## U35

**Role de l'enonce :** mesure

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

**Reponse a coder, en entier :**

**NOTE DE CONSULTATION — Apport partiel d'actif avec remise directe des titres aux associés**

---

### Réponse de principe

**Oui.** L'opération envisagée peut bénéficier du régime spécial des fusions (CGI, art. 210 A et s.), en application expresse de l'article 210-0 A, I, 4° que vous citez.

Cette possibilité — apport partiel d'actif « sans dissolution » avec remise des titres **directement aux associés** de la société apporteuse — a été introduite par l'article 11 de la loi de finances rectificative pour 2017, applicable aux opérations réalisées depuis le 1er janvier 2018. Elle transpose dans notre droit la notion de « scission partielle » de la directive 2009/133/CE (art. 2, b), consacrée par la jurisprudence CJUE, *Foggia*, C-375/98). Avant 2018, la remise directe aux associés n'était admise que pour les scissions ; le texte permet désormais de réaliser fiscalement une « scission sans dissolution », ce qui correspond exactement à votre projet.

Le régime n'est toutefois pas automatique : il suppose une **option expresse** (depuis 2018, le régime spécial est devenu optionnel) et le respect de conditions strictes.

---

### I. Conditions à réunir

1. **Branche complète et autonome.** L'activité industrielle apportée doit constituer un ensemble d'éléments d'actif **et de passif** capable de fonctionner par ses propres moyens (installations, matériel, stocks, contrats, clientèle et, en pratique, personnel affecté). Point critique : si l'activité industrielle est en réalité logée dans une **filiale**, l'apport des titres de cette filiale ne vaut pas apport de branche complète et le régime est exclu. Il faut donc vérifier que la holding exploite directement les deux activités.

2. **Conservation par la holding d'au moins une branche complète.** La branche négoce demeurant dans la holding, la condition est satisfaite. Corollaire : on ne pourrait pas apporter simultanément les deux branches à deux sociétés sans dissoudre la holding — l'opération s'analyserait alors en scission, laquelle exige la dissolution (BOI-IS-FUS-10-20).

3. **Qualité des sociétés.** Apporteuse et bénéficiaire soumises à l'IS (France ou UE). La société nouvelle convient ; aucune condition de détention préalable n'est exigée.

4. **Rémunération en titres** de la société bénéficiaire (soulte éventuelle ≤ 10 % de la valeur nominale des titres).

5. **Engagements de la société bénéficiaire** (art. 210 A, I) : reprise des éléments à leur valeur fiscale, calcul des amortissements et des plus-values ultérieures sur la base fiscale, reprise des provisions. Le non-respect entraîne la réintégration des plus-values en sursis.

6. **Engagement de conservation des titres pendant trois ans.** Lorsque les titres sont remis directement aux associés, cet engagement est souscrit **par les associés bénéficiaires de la remise** (adaptation prévue par la doctrine). Sanction : réintégration des plus-values par la société bénéficiaire, au prorata des titres cédés.

7. **Logique économique.** La séparation des deux branches familiales et la clarification des pérismètres constituent un motif de gestion valable, qu'il conviendra de documenter (risque d'abus de droit si l'opération était principalement fiscale).

---

### II. Conséquences du régime

- **Holding (apporteuse)** : neutralisation des plus-values sur les éléments apportés (fonds, matériels, immeubles éventuels) ; transfert des provisions sans reprise ; **continuité de l'exercice** (pas de clôture, contrairement à une scission). Les déficits afférents à la branche apportée peuvent être transférés à la société nouvelle **sur agrément** (art. 210 A, I-6°) ; les autres demeurent à la holding.
- **Société nouvelle (bénéficiaire)** : inscription comptable aux valeurs réelles mais continuité fiscale ; obligations déclaratives (relevé des plus-values en sursis annexé à la liasse) ; possibilité d'effet rétroactif (art. 210 A, III).
- **Associés** : la remise directe est **assimilée à une scission**. Pour les personnes physiques : pas de revenu distribué imposable ; sursis d'imposition de l'échange (art. 150-0 B) ; répartition du prix d'acquisition de leurs titres de la holding entre titres conservés et titres reçus, au prorata des valeurs vénale, avec conservation de l'antériorité. Contribution de 3 % sur les distributions : exonérée (art. 235 ter ZCA, II).
- **Taxes annexes** : transfert d'une universalité hors champ de TVA (art. 257 bis) ; apports purs et simples enregistrés au droit fixe ; en présence d'immeubles, exonération possible des droits de mutation (art. 816) sous conditions.

---

### III. Structuration au regard de l'objectif familial

Point d'attention essentiel : une remise des titres de la société nouvelle à **tous** les associés, au prorata de leurs droits, laisserait chaque branche familiale détentrice des deux sociétés — l'objectif ne serait pas atteint.

Le régime fiscal n'exige aucune proportionnalité. La structuration appropriée consiste donc en :

- l'apport de la branche industrielle à la société nouvelle, les titres étant remis **à la seule branche familiale 1** ;
- corrélativement, une **réduction du capital de la holding** éteignant les titres de cette branche, qui sort ainsi du capital (mécanique d'échange assimilée à une scission déséquilibrée, sous sursis).

Au plan du droit des sociétés, l'apport partiel devra être soumis au régime juridique des scissions (C. com., art. L. 236-16 et L. 236-22), l'attribution dérogatoire à la proportionnalité requérant l'**unanimité** des associés (art. L. 236-15) — réalisable dans un groupe familial.

Alternative : la scission complète (dissolution de la holding, deux sociétés bénéficiaires) ouvre le même régime fiscal mais entraîne dissolution et clôture d'exercice. L'apport partiel avec remise directe est l'outil le plus souple.

---

### IV. Points de vigilance

- **Qualification de la branche** : audit préalable (effectifs, contrats, passif afférent transféré) ;
- **Mode de détention de l'industrie** : si elle est en filiale, restructuration préalable nécessaire (fusion/TUP), avec prudence au regard de l'abus de droit ;
- **Valorisations aux valeurs réelles**, commissaire aux apports/commissaire à la scission ;
- **Agrément** si transfert de déficits souhaité ;
- **Verrou de trois ans** sur les titres de la société nouvelle pour la branche familiale 1 (les opérations intercalaires en sursis ne rompent pas l'engagement, BOI-IS-FUS-20-20) ;
- Formalisation de l'**option** et des engagements dans le traité d'apport, date d'effet, calendrier des assemblées et dépôt au greffe.

---

Souhaitez-vous que nous validions d'abord la qualification de branche complète au vu de l'organigramme et des balances des deux activités ? C'est le point de passage déterminant avant de structurer le traité d'apport.

---

## U36

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

**NOTE D’ANALYSE FISCALE**
**Objet :** Régime de la retenue à la source sur la distribution de dividendes à la société mère luxembourgeoise
**Date de la distribution prévue :** 15 novembre 2024
**Montant :** 20 000 000 €
**Rédigé par :** [Votre Nom], Avocat au Barreau, Spécialiste en droit fiscal

---

### 🔹 SYNTHÈSE
En l’état des éléments communiqués, **aucune retenue à la source ne devrait être due** sur la distribution du 15 novembre 2024, sous réserve :
1. du respect des conditions de fond prévues par la directive mère-fille et la convention franco-luxembourgeoise ;
2. de la production des justificatifs administratifs dans les délais ;
3. de l’absence de montage artificiel ou de défaut de substance de la société mère luxembourgeoise.

---

### 🔹 ANALYSE JURIDIQUE

#### 1. Principe de droit interne : la retenue à la source
L’article 119 bis, 2, premier alinéa du CGI soumet à retenue à la source les dividendes versés à des personnes n’ayant pas leur siège ou domicile fiscal en France. Le taux de droit commun est fixé à **12,8 %** par l’article 187 du CGI.

Ce principe est toutefois tempéré par :
- le droit de l’Union européenne (directive 2011/96/UE dite « mère-fille ») ;
- la convention fiscale franco-luxembourgeoise du 1er avril 1958 modifiée.

#### 2. Application de la directive mère-fille (transposée à l’art. 119 bis, 2, 2° CGI)
L’exonération de retenue à la source est acquise lorsque les conditions cumulatives suivantes sont remplies :
| Condition | Situation du dossier |
|-----------|----------------------|
| Formes juridiques éligibles (Annexe I de la directive) | SA française et SA luxembourgeoise ✅ |
| Détention d’au moins 10 % du capital | 100 % ✅ |
| Durée de détention ininterrompue d’au moins 2 ans | 5 ans ✅ |
| Assujettissement effectif à l’impôt sur les sociétés sans exonération | Confirmé pour la mère luxembourgeoise ✅ |
| Résidence dans un État membre de l’UE | France et Luxembourg ✅ |

👉 **Conclusion :** La distribution entre dans le champ de l’exonération prévue par l’article 119 bis, 2, 2° du CGI.

#### 3. Convention fiscale franco-luxembourgeoise
L’article 10 de la convention prévoit une retenue à la source à **0 %** lorsque la société bénéficiaire détient directement au moins 10 % du capital de la société distributrice. Ce fondement conventionnel vient en complément de la directive et confirme l’absence de prélèvement.

#### 4. Vigilance : clause anti-abus et exigence de substance
Le bénéfice de l’exonération est subordonné au respect des clauses anti-abus :
- **Directive mère-fille (art. 1er, §2)** et **CGI (art. 119 bis, 2, 3°)** : refus du régime si le montage a pour objet principal ou l’un des objets principaux d’obtenir un avantage fiscal.
- **Jurisprudence CJUE (Eqiom, C-6/16 ; Deister, C-116/16 & C-117/16)** : l’administration peut écarter l’exonération en cas de montage artificiel, de société « boîte aux lettres » ou d’absence de réalité économique.

📌 **Recommandation :** Vérifier que la société mère luxembourgeoise dispose d’une substance réelle (siège effectif, personnel qualifié, processus décisionnel autonome, comptabilité régulière, assujettissement effectif à l’IS luxembourgeois, absence de dépendance excessive envers des tiers).

---

### 🔹 OBLIGATIONS DÉCLARATIVES ET FORMALITÉS

Pour bénéficier de l’exonération, la société française doit impérativement :
1. **Obtenir une attestation de résidence fiscale** de la société mère luxembourgeoise (modèle OCDE ou formulaire 5000), délivrée par l’administration fiscale luxembourgeoise, certifiant son assujettissement à l’IS.
2. **Déposer la déclaration n° 2777** (ou 2777-SD) auprès du Service des Impôts des Entreprises (SIE) compétent, **au plus tard le jour du paiement** (15/11/2024). En pratique, il est fortement conseillé de la transmettre 10 à 15 jours avant.
3. **Joindre à la déclaration** :
   - L’attestation de résidence fiscale ;
   - Un engagement écrit de conservation des titres pendant 2 ans (déjà satisfait) ;
   - Tout justificatif de substance si le SIE le demande.
4. **Conserver l’ensemble du dossier** pendant 6 ans (délai de reprise de l’administration).

⚠️ **Risque procédural :** En l’absence de déclaration 2777 ou de justificatifs complets au jour du paiement, l’administration appliquera automatiquement la retenue à 12,8 %. La restitution est possible mais longue (procédure de réclamation contentieuse, délai moyen 12 à 18 mois).

---

### 🔹 RECOMMANDATIONS OPÉRATIONNELLES

1. **Dès maintenant :** Solliciter l’attestation de résidence fiscale luxembourgeoise (délai administratif : 2 à 4 semaines).
2. **Avant le 1er novembre 2024 :** Constituer un dossier de substance (PV d’assemblée, organigramme, contrats de services, preuves de direction effective, extrait Kbis luxembourgeois, avis d’imposition IS).
3. **Avant le 10 novembre 2024 :** Préparer et transmettre la déclaration 2777 au SIE compétent, avec accusé de réception.
4. **Dans la convention de distribution :** Insérer une clause de garantie prévoyant la prise en charge par la mère luxembourgeoise de toute retenue à la source qui serait indûment appliquée par l’administration française.
5. **En cas de contrôle :** Être en mesure de démontrer la réalité économique du groupe et l’absence de montage à finalité exclusivement fiscale.

---

### 🔹 CONCLUSION
Sous réserve de la production des justificatifs dans les délais et de l’absence de montage artificiel, **la distribution de 20 000 000 € au 15 novembre 2024 peut être effectuée sans retenue à la source**. Le régime applicable repose sur la directive mère-fille et la convention franco-luxembourgeoise, toutes deux prévoyant une exonération totale.

Je reste à votre disposition pour :
- Rédiger et déposer la déclaration 2777 ;
- Vérifier la conformité du dossier de substance ;
- Assister la société en cas de demande de justificatifs ou de contrôle du SIE.

Veuillez agréer, Madame, Monsieur, l’expression de mes salutations distinguées.

**[Votre Nom]**  
Avocat au Barreau de Paris  
Spécialiste en droit fiscal des entreprises  
📧 [email] | 📞 [téléphone]  

*Note : Cette analyse est établie sur la base des éléments communiqués et du droit applicable à la date de la distribution. Elle ne vaut pas garantie absolue contre un contrôle de l’administration fiscale, dont l’appréciation reste souveraine.*

---

## U37

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus a la societe
apporteuse.

Le projet d'apport a ete depose au greffe du tribunal de commerce
le 10 novembre 2022.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder, en entier :**

**En l’état des faits décrits, l’apport partiel d’actif peut relever du régime spécial des articles 210 A et suivants du CGI**, sous réserve que l’activité industrielle constitue bien une **branche complète d’activité**.

### 1. Qualification de l’opération

L’opération envisagée présente les caractéristiques d’un apport partiel d’actif :

- la holding apporte, sans dissolution, son activité industrielle à une société nouvelle ;
- elle conserve son activité de négoce ;
- la société bénéficiaire rémunère l’apport par l’émission de ses propres titres ;
- ces titres sont remis à la holding apporteuse.

Cette dernière condition est importante : au regard du texte applicable au projet déposé le **10 novembre 2022**, les titres de la société bénéficiaire devaient être remis **à la société apporteuse**. Elle est donc satisfaite dans votre schéma.

L’article 210-0 A, I, 4° définit ainsi l’opération éligible ; l’article 210 B, I du CGI rend ensuite le régime de l’article 210 A applicable de plein droit aux apports partiels d’actif portant sur une ou plusieurs branches complètes d’activité.

### 2. Condition essentielle : l’existence d’une branche complète d’activité

L’activité industrielle doit former un ensemble autonome susceptible de fonctionner par ses propres moyens après l’apport. En pratique, devront être transférés à la société nouvelle, notamment :

- les immobilisations, stocks et autres actifs affectés à l’activité industrielle ;
- les dettes et provisions qui s’y rattachent ;
- les contrats, autorisations, marques ou droits nécessaires à l’exploitation ;
- les salariés affectés à l’activité, avec transfert des contrats de travail conformément à l’article L. 1224-1 du Code du travail ;
- plus largement, les moyens humains, matériels et financiers permettant la poursuite autonome de l’activité.

Le seul fait de qualifier comptablement une activité de « branche industrielle » ne suffit pas. Il faudra documenter son autonomie effective, en particulier si certaines fonctions support, financements, actifs immobiliers, marques ou contrats sont actuellement mutualisés avec l’activité de négoce.

### 3. Conséquences fiscales

Si ces conditions sont réunies, le régime de faveur s’applique de plein droit :

- absence d’imposition immédiate, chez la holding apporteuse, des plus-values afférentes aux éléments apportés ;
- reprise par la société bénéficiaire des valeurs fiscales des actifs apportés ;
- imposition ultérieure des plus-values lors de la cession des actifs par la société bénéficiaire, selon les règles de droit commun ;
- maintien, sous conditions, des provisions et engagements fiscaux transférés.

Le traité d’apport devra naturellement comporter les engagements et mentions requis par l’article 210 A du CGI, notamment la reprise des valeurs fiscales et les modalités de suivi des éléments apportés.

### 4. Point de vigilance : cette opération ne sépare pas, à elle seule, les deux branches familiales

L’apport tel que décrit laisse la holding propriétaire :

- de l’activité de négoce, directement ;
- des titres de la société nouvelle exerçant l’activité industrielle.

Il réalise donc une **séparation juridique des activités**, mais pas nécessairement une séparation capitalistique entre les deux branches de la famille.

Si l’objectif réel est que les titres de la société industrielle nouvelle soient attribués directement à certains associés familiaux, il s’agirait d’un schéma d’**apport-attribution** ou de **scission partielle**. Or, au 10 novembre 2022, le texte alors applicable exigeait la remise des titres à la société apporteuse, et non à ses associés.

L’extension ultérieure du régime aux opérations dans lesquelles les titres sont remis aux associés de l’apporteuse — sous réserve d’une attribution proportionnelle à leurs droits — ne pouvait pas bénéficier à un projet de traité déposé au greffe avant son entrée en vigueur. La date du dépôt du **10 novembre 2022** est donc déterminante sur ce point.

### Conclusion

- **Oui**, l’apport de la branche industrielle à une société nouvelle peut bénéficier du régime des articles 210 A et 210 B du CGI, si cette activité constitue effectivement une branche complète d’activité et que les titres de la société nouvelle sont attribués à la holding apporteuse.
- **Non**, ce dépôt du 10 novembre 2022 ne permet pas, dans le cadre de ce régime, une attribution directe des titres de la société nouvelle aux membres de l’une ou l’autre branche familiale. Une telle séparation capitalistique supposerait une opération complémentaire, à analyser distinctement au regard de ses conséquences fiscales.

---

## U38

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

En tant qu’avocat fiscaliste, voici l’analyse que je porterais à votre dossier.

---

**1. Le cadre juridique applicable**

L’article 278-0 bis A, I du CGI, dans sa rédaction issue de la loi de finances pour 2024 et applicable aux travaux facturés le 20 janvier 2025, soumet au taux réduit de TVA de 5,5 % les **prestations de rénovation énergétique** répondant cumulativement aux trois conditions suivantes :

- être réalisées dans des **locaux achevés depuis au moins deux ans** ;
- porter sur des **locaux affectés ou destinés à être affectés à un usage d’habitation** à l’issue des travaux ;
- consister en la **pose, l’installation, l’adaptation ou l’entretien de matériaux, d’équipements, d’appareils ou de systèmes ayant pour objet d’économiser l’énergie ou de recourir à des énergies renouvelables**, par l’amélioration de l’isolation thermique, du chauffage/ventilation ou de la production d’eau chaude sanitaire.

Le taux normal de TVA est de 20 % (article 278 du CGI). L’enjeu du litige est donc de savoir si l’installation de la chaudière litigieuse relève bien de ce taux réduit.

---

**2. Application au cas d’espèce**

**a) Conditions relatives au local**

- **Locaux achevés depuis au moins deux ans** : la maison a quinze ans. La condition est remplie.
- **Affectation à usage d’habitation** : la maison est occupée par son propriétaire. La condition est remplie.

**b) Condition relative à la nature des travaux**

C’est ici que se situe le point de friction. Le texte exige que la prestation porte sur un équipement **ayant pour objet d’économiser l’énergie ou de recourir à des énergies renouvelables**, en améliorant le chauffage.

L’installation d’une chaudière peut, en principe, répondre à cette définition, **à condition qu’il s’agisse d’un équipement éligible**. En effet, ni le texte légal ni la doctrine administrative ne considèrent que *toute* chaudière, quelle que soit sa technologie, a pour objet d’économiser l’énergie.

Ainsi, pour les travaux de chauffage, sont notamment réputés éligibles au taux réduit de 5,5 % (BOFiP, TVA-LIQ-30-20-10) :
- les **chaudières à condensation** (gaz ou fioul) ;
- les **chaudières à micro-cogénération gaz** ;
- les **pompes à chaleur** (air/eau, eau/eau, géothermiques) ;
- les **chaudières biomasse** (bois, granulés) ;
- les **systèmes solaires thermiques** pour le chauffage ou l’eau chaude sanitaire ;
- certains équipements de régulation/programmation performants.

En revanche, une **chaudière standard à basse température**, une chaudière classique au gaz ou au fioul, même neuve, **n’est pas considérée comme ayant pour objet d’économiser l’énergie** au sens de l’article 278-0 bis A. Elle relève alors du taux normal de 20 %.

Or, dans le cas présent, vous m’indiquez uniquement que l’entreprise a installé « une chaudière », sans précision sur sa nature technique (condensation, biomasse, PAC, etc.). C’est précisément sur ce point que l’administration fonde probablement sa rectification.

---

**3. Conséquences pratiques**

**a) Vérification de la nature de la chaudière**

Avant toute contestation, il est impératif de déterminer précisément le type de chaudière installée. Les éléments suivants doivent être réunis :
- le devis et la facture détaillée ;
- la référence exacte du matériel ;
- la documentation technique du fabricant (étiquette énergie, fiche produit) ;
- tout justificatif attestant qu’il s’agit d’un équipement éligible (par exemple, certificat « CE » ou mention « chaudière à condensation »).

**b) Si la chaudière est effectivement éligible**

Si la chaudière installée est, par exemple, une chaudière à condensation, le taux de 5,5 % appliqué par l’entreprise était correct. Il conviendra alors de **contester la proposition de rectification** en apportant la preuve de l’éligibilité du matériel, en s’appuyant sur le texte légal et la doctrine administrative.

**c) Si la chaudière n’est pas éligible**

Si la chaudière est un modèle standard (non condensation, non biomasse, non PAC), l’administration est fondée à réclamer le complément de TVA (différence entre 20 % et 5,5 %). Dans ce cas, je vous recommande d’accepter la rectification pour ce chantier, mais de vérifier si d’autres chantiers de l’entreprise sont concernés par le même problème, afin d’anticiper d’éventuels redressements complémentaires.

**d) Régularisation et prévention**

Si le taux réduit a été appliqué à tort, l’entreprise devra émettre une **facture rectificative** mentionnant le taux de 20 % et reverser la TVA complémentaire. Il est conseillé de mettre en place un contrôle interne pour s’assurer, avant chaque facturation, que les équipements installés répondent aux critères ouvrant droit au taux réduit.

---

**4. Conclusion**

Le taux de 5,5 % n’est correct **que si la chaudière installée fait partie des équipements listés comme économes en énergie ou utilisant des énergies renouvelables**. En l’état des informations fournies, il est impossible de se prononcer définitivement.

**Ma recommandation** : avant de répondre à la proposition de rectification, il faut identifier précisément le modèle de chaudière installé. S’il s’agit d’un équipement éligible, nous préparerons une contestation solide. Dans le cas contraire, mieux vaut régulariser rapidement pour limiter les pénalités et éviter un contentieux inutile.

Je me tiens à votre disposition pour examiner les pièces techniques et vous assister dans la réponse à l’administration.

---

## U39

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

**Note de consultation — Proposition de rectification TVA — Chantier du 15 avril 2025**

**I. Rappel des faits et de la question posée**

Votre société a facturé le 15 avril 2025 la pose d'une chaudière dans une maison achevée depuis quinze ans, occupée par son propriétaire, pour un prix de 8 500 € HT, au taux de 5,5 %. L'administration réclame l'écart entre le taux appliqué (5,5 %) et le taux normal (20 %), soit théoriquement un rappel de 1 232,50 €. La question est de savoir si cette rectification est fondée sur le texte applicable (CGI, art. 278-0 bis A).

**II. Analyse juridique**

*1. Les conditions du taux de 5,5 % sont, en principe, réunies (I)*

Le I du texte soumet le passage au taux réduit de 5,5 % à trois conditions cumulatives :

- **Local achevé depuis au moins deux ans** : la maison a quinze ans. La condition est satisfaite, et de loin.
- **Local affecté à un usage d'habitation** : la maison est occupée par son propriétaire. Le texte n'exige pas qu'il s'agisse de la résidence principale ; une résidence secondaire suffirait. La condition est donc remplie.
- **Prestation portant sur l'amélioration du chauffage en vue d'économies d'énergie** (3°, b) : la pose d'une chaudière relève en principe de cette rubrique.

À première vue, l'opération semblait donc bien éligible au 5,5 %.

*2. Mais l'exception du III bis vise précisément les chaudières*

C'est ici que se situe la difficulté. Le III bis, issu de l'article 32 de la loi de finances pour 2024 (loi n° 2023-1322 du 29 décembre 2023), applicable aux opérations dont la TVA est devenue exigible à compter du 1er mars 2024, dispose que **le taux de 20 % s'applique aux prestations comprenant la fourniture ou l'installation d'une chaudière *susceptible d'utiliser des combustibles fossiles***.

Trois observations décisives :

- **Le critère retenu est extrêmement large.** Le texte ne vise pas les chaudières *fonctionnant* aux combustibles fossiles, mais celles qui sont *susceptibles d'y recourir*. Une chaudière mixte (gaz + bois, gaz + biogaz) ou adaptable au fioul tombe dans l'exclusion, même si le combustible effectivement utilisé est renouvelable.
- Sont en pratique visées les chaudières au **gaz naturel, propane/butane, fioul ou charbon**. Seules demeurent au 5,5 % les chaudières fonctionnant **exclusivement** à des combustibles renouvelables (biomasse, granulés de bois, biogaz pur), ainsi que les équipements qui ne sont pas des chaudières (pompes à chaleur, par exemple). C'est la position dégagée par la doctrine administrative (BOI-TVA-LIQ-30-20-90).
- **Portée de l'exclusion** : le III bis vise la « prestation **comprenant** » la fourniture ou l'installation. La fourniture et la pose constituent une opération unique (livraison d'ouvrage) ; il n'est donc pas possible de dissocier la chaudière proprement dite de la main-d'œuvre pour réserver le 5,5 % à l'une des composantes. C'est l'intégralité de la prestation facturée qui bascule à 20 %.

*3. Pas de repli sur le taux de 10 %*

Le III bis désigne expressément « le taux prévu à l'article 278 », c'est-à-dire le taux normal de 20 %. La voie d'un éventuel repli sur le taux intermédiaire de 10 % (CGI, art. 279-0 bis) est fermée : la loi a entendu taxer ces chaudières au taux normal, symbole de la sortie du droit fiscal favorable aux énergies fossiles.

*4. Entrée en vigueur*

Aucune difficulté de temporalité : la facture est du 15 avril 2025, plus d'un an après l'entrée en vigueur du dispositif (1er mars 2024). La règle transitoire liée à la date d'exigibilité est ici sans portée, sauf — à vérifier — l'hypothèse peu probable d'acomptes encaissés avant le 1er mars 2024.

**III. Réponse : tout dépend du combustible de la chaudière**

Je ne peux trancher définitivement sans une information que le dossier ne me donne pas encore : la nature exacte de la chaudière installée. Deux scénarios :

- **Si la chaudière fonctionne au gaz, au fioul, au charbon, ou est susceptible d'utiliser ces combustibles (y compris mixte)** : le taux de 5,5 % appliqué était **incorrect**. La rectification est sur ce point fondée en droit. L'ancienne doctrine, qui admettait encore les chaudières gaz ou fioul « très haute performance énergétique » au taux réduit, a cessé de s'appliquer depuis le 1er mars 2024 : beaucoup d'entreprises du secteur ont été surprises par ce basculement, mais le texte est clair.
- **S'il s'agit d'une chaudière biomasse (granulés, bois) ou biogaz exclusivement** : le III bis ne s'applique pas et le 5,5 % était **correct**. Il faudra alors répondre à la proposition de rectification en demandant son abandon pur et simple, en produisant la documentation technique du fabricant attestant du combustible exclusif.

À noter également : si la facture de 8 500 € comprend d'autres éléments que la chaudière (régulation, émetteurs), l'administration les suivra vraisemblablement au 20 % en tant qu'équipements associés à l'appareil exclu.

**IV. Conséquences chiffrées (si le redressement est maintenu)**

- Rappel de TVA : 8 500 € × 14,5 points = **1 232,50 €** ;
- **Intérêts de retard** : 0,20 % par mois (2,4 % l'an) depuis l'exigibilité ; ils sont une créance insusceptible de remise ;
- **Pénalités** : sauf mauvaise foi dont la preuve incombe à l'administration, le redressement de taux ne s'accompagne en principe pas d'amende (la taxe additionnelle de 5 % ou les majorations de 40 %/80 % supposent des manœuvres ou un dépôt tardif).

Enfin, soyez lucide sur la répercussion : le client final étant un particulier et le prix ayant vraisemblablement été convenu TTC, la société aura, en pratique, beaucoup de mal à récupérer le complément de TVA auprès de lui. Le rappel pèsera donc sur l'entreprise.

**V. Suites à donner et recommandations**

1. **Me faire parvenir de toute urgence** la facture, le devis et la désignation technique exacte de la chaudière (marque, modèle, combustible) — c'est la clé du dossier.
2. **Respecter le délai de réponse de 30 jours** ouvert par la proposition de rectification (CGI, LPF, art. L. 57 ; prorogeable de 30 jours supplémentaires sur demande motivée). Une absence de réponse rendrait le redressement définitif.
3. **Si chaudière fossile** : les chances de succès au fond sont très faibles ; je recommande alors de payer rapidement pour stopper les intérêts de retard, tout en sollicitant par écrit une remise gracieuse au titre de la bonne foi (LPF, art. L. 247), en plaidant le caractère récent du dispositif et un usage professionnel ancré sur l'ancienne doctrine.
4. **Si chaudière exclusivement renouvelable** : réponse écrite circonstanciée avec pièces, demande d'abandon, puis, en cas de maintien, réclamation contentieuse et saisine du tribunal administratif.
5. **Pour l'avenir** : mettre en place une vérification systématique du combustible avant facturation ; en cas d'hésitation sur un appareil hybride, sécuriser la position par un rescrit (LPF, art. L. 80 B).

Je reste à votre disposition pour préparer la réponse dès que j'aurai la documentation technique de la chaudière.

---

## U40

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

# Consultation fiscale – Report d'imposition – Article 150-0 B ter, I, 2° du CGI

## I. Rappel des faits

- Cession le **10 novembre 2025** par la holding des titres d'une société d'exploitation ;
- Délai depuis l'apport : **inférieur à trois ans** ;
- Produit de cession : **9 000 000 €** ;
- Projet de remploi : souscription au capital / financement d'une société ayant pour activité **l'achat d'immeubles en vue de les rénover et de les revendre** (activité de marchand de biens).

## II. Cadre juridique

En application de l'article 150-0 B ter, I, 1° du CGI, la cession des titres apportés dans le délai de trois ans met normalement fin au report d'imposition dont bénéficiait le client.

Toutefois, le **2° du I** prévoit une exception : le report est maintenu si la société bénéficiaire de l'apport (la holding) prend l'engagement de réinvestir **au moins 60 % du produit de cession**, dans un **délai de deux ans** à compter de la cession, dans :

> « a) Le financement de **moyens permanents d'exploitation** affectés à son activité commerciale au sens des articles 34 ou 35, industrielle, artisanale, libérale, agricole ou financière. Les activités de **gestion de son propre patrimoine mobilier ou immobilier** sont exclues du bénéfice de cette dérogation ».

Deux conditions cumulatives doivent donc être remplies :
1. Réinvestir dans des **moyens permanents d'exploitation** ;
2. Affectés à une activité **commerciale (art. 34 ou 35), industrielle, artisanale, libérale, agricole ou financière** — à l'exclusion de la gestion patrimoniale.

## III. Analyse

### A. Sur la nature de l'activité de la société cible – qualification

L'activité d'**achat, rénovation et revente d'immeubles** constitue une activité de **marchand de biens**. Cette activité est expressément visée par l'article 35, I-2° du CGI, qui range dans la catégorie des bénéfices industriels et commerciaux les profits réalisés par les personnes qui se livrent à des opérations de caractère commercial portant sur des immeubles.

À ce titre, la société cible exerce une **activité commerciale au sens de l'article 35 du CGI**, et non une activité de gestion de patrimoine immobilier.

➡ **La société cible n'entre pas dans le champ de l'exclusion** prévue par l'article 150-0 B ter, I, 2°, a) (« gestion de son propre patrimoine mobilier ou immobilier »). La jurisprudence et la doctrine administrative considèrent en effet que le marchand de biens, qui accomplit des actes de commerce sur des immeubles, se distingue du détenteur patrimonial qui se contente de percevoir des loyers ou de valoriser son capital.

### B. Sur la nature des biens financés – problème central

C'est ici que la difficulté se concentre. Le texte exige que le remploi porte sur des **« moyens permanents d'exploitation »**.

Cette notion renvoie aux éléments de l'**actif immobilisé** de l'entreprise, utilisés de manière **durable** dans le cadre de l'exploitation (terrains et constructions affectés à l'exploitation, matériel, outillage, brevets, etc.). Elle s'oppose aux éléments de l'**actif circulant** — et notamment aux **stocks de marchandises**.

Or, dans une activité de marchand de biens :
- Les immeubles acquis en vue de la revente constituent des **stocks** au sens comptable et fiscal (compte 31 du plan comptable général) ;
- Ils ne sont pas des immobilisations : leur durée de détention est par nature temporaire ;
- Ils ne sont pas « affectés » durablement à l'exploitation au sens d'un outil industriel ou commercial.

Le BOI-RFMT-PV-30-30-30 (§ 150 et suivants) précise d'ailleurs que les biens doivent être inscrits à l'actif immobilisé et utilisés durablement par la société.

➡ **Le financement d'immeubles destinés à la revente ne constitue pas, en principe, le financement de « moyens permanents d'exploitation » au sens de l'article 150-0 B ter, I, 2°, a).**

## IV. Conclusion

**Le remploi envisagé ne permet pas, selon moi, de maintenir le report d'imposition**, et ce pour deux raisons cumulatives :

1. **L'activité de la société cible n'est pas en elle-même exclue** : en qualité d'activité commerciale au sens de l'article 35 du CGI, elle aurait pu théoriquement entrer dans le champ de la dérogation ;

2. **Mais les immeubles acquis pour être rénovés et revendus ne sont pas des moyens permanents d'exploitation** : ils relèvent des stocks et non de l'actif immobilisé, condition expresse posée par le texte.

## V. Recommandations

Pour préserver le report d'imposition, le client pourrait envisager des opérations de remploi alternatives, sous réserve de faisabilité économique :

- **Financement de moyens permanents d'exploitation** d'une société cible exerçant une activité éligible (commerciale, industrielle, artisanale, etc.) : acquisition de locaux d'exploitation, de matériel, prise de participation au capital ;
- **Acquisition directe par la holding d'immobilisations d'exploitation** (par exemple, locaux affectés à sa propre activité) ;
- À défaut, le report prendra fin et la plus-value d'apport deviendra imposable dans les conditions de droit commun.

Compte tenu des enjeux (plus-value d'apport potentiellement très substantielle), je recommande de formaliser l'engagement de remploi dans les délais prescrits et de sécuriser juridiquement le projet **avant tout investissement**. Une consultation complémentaire avec un avis écrit de l'administration (rescrit fiscal – article L. 80 B du LPF) pourrait être envisagée si le client souhaite lever toute incertitude.

---

*Note : Cette analyse est fondée sur le texte applicable à la date de la cession. Elle devra être confirmée par l'examen de la doctrine administrative (BOI-RFMT-PV-30-30-30) et par une note détaillée sur les conditions précises du remploi projeté.*

---

## U41

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

## 1. Situation et enjeu

La cession intervenue en février 2026, moins de trois ans après l’apport des titres à votre holding contrôlée, constitue en principe un événement mettant fin au report d’imposition de la plus-value d’apport.

Le report peut toutefois être maintenu si la holding :

- prend formellement l’engagement de réinvestir ;
- réinvestit, dans les trois ans de la cession, au moins **70 % du produit de cession** ;
- dans des investissements répondant strictement aux conditions du texte.

Sur la base d’un produit de cession de **9 000 000 €**, le montant minimal à réinvestir est donc de :

> **9 000 000 € × 70 % = 6 300 000 €**

Sous réserve de vérifier si les 9 M€ correspondent bien au « produit de cession » retenu fiscalement (notamment s’il existe des frais directement liés à la vente, un séquestre, un complément de prix, etc.).

Le délai expire, de date à date, en **février 2029**. Si la cession est par exemple intervenue le 18 février 2026, le réinvestissement devra être effectivement réalisé au plus tard le 18 février 2029. En pratique, je recommande de viser une réalisation plusieurs mois avant l’échéance.

L’absence de réinvestissement conforme à hauteur de 6,3 M€ entraînerait la fin du report sur la totalité de la plus-value d’apport en report — et non sur la seule quote-part non réinvestie.

---

## 2. Ce que la holding peut faire, et ce qu’elle ne doit pas faire

### A. Le placement temporaire de la trésorerie est possible, mais ne vaut pas réinvestissement

Le fait que les 9 M€ restent temporairement sur le compte bancaire de la holding ne remet pas, à lui seul, le report en cause : le texte vous laisse trois ans pour effectuer le réinvestissement.

En revanche, les placements de trésorerie — comptes à terme, SICAV monétaires, obligations, comptes-titres, fonds diversifiés, private equity non éligible, etc. — ne constituent pas, par eux-mêmes, un réinvestissement éligible au sens du a) cité.

Ils peuvent être utilisés dans l’attente d’une opération, mais la holding doit conserver la liquidité nécessaire pour financer l’investissement qualifiant avant février 2029.

### B. Au regard du seul a) communiqué : financer de vrais moyens permanents d’exploitation

Le a) vise le financement de moyens permanents d’exploitation affectés à une activité opérationnelle éligible : activité commerciale, industrielle, artisanale, libérale ou agricole, à l’exclusion de la gestion de son propre patrimoine immobilier.

Concrètement, le réinvestissement peut notamment prendre la forme, sous réserve de l’analyse précise du projet, de :

- l’acquisition d’un fonds de commerce ou d’une branche complète d’activité ;
- l’acquisition d’équipements, machines, installations techniques ou matériels nécessaires à une activité exploitée ;
- l’acquisition de droits ou actifs incorporels nécessaires à une exploitation : logiciels, brevets, licences, clientèle, etc. ;
- le financement d’une activité nouvelle réellement exercée par la holding elle-même, si elle devient une société opérationnelle ;
- plus largement, d’investissements immobilisés et effectivement affectés à une activité économique éligible.

À l’inverse, ne doivent pas être présentés comme des moyens permanents d’exploitation :

- l’acquisition d’un immeuble conservé dans une logique patrimoniale ou locative ;
- les placements financiers ;
- le remboursement d’une dette sans lien direct avec l’acquisition ou le financement de moyens permanents d’exploitation ;
- les avances ou prêts à des sociétés sans emploi démontrable dans des actifs d’exploitation éligibles ;
- une opération immobilière de gestion de patrimoine.

### C. Attention particulière si le projet consiste à investir dans une autre société

Si l’objectif est d’acquérir une participation dans une société opérationnelle, de créer une filiale ou de souscrire à son augmentation de capital, il faut examiner les autres modalités de réinvestissement prévues par l’article 150-0 B ter dans sa rédaction complète.

Le seul a) reproduit dans votre question ne doit pas être interprété extensivement : une simple prise de participation ou souscription au capital d’une société opérationnelle n’est pas automatiquement assimilable au financement, par la holding, de ses propres moyens permanents d’exploitation.

Ce type d’opération peut être admissible sous les autres branches du dispositif, sous conditions propres : nature de l’activité de la cible, niveau de contrôle, modalités de souscription ou d’acquisition, absence de gestion patrimoniale, durée de conservation, etc. Il faudra donc structurer l’opération avant sa signature, et non après.

---

## 3. Recommandation pratique : organiser immédiatement un programme de réinvestissement

Je recommande les mesures suivantes.

### 1. Formaliser sans délai l’engagement de réinvestissement

La holding doit prendre une décision formelle constatant :

- la cession des titres en février 2026 ;
- le produit net retenu pour le calcul ;
- l’engagement de réinvestir au moins **6,3 M€** ;
- le délai maximal applicable, soit février 2029 ;
- les catégories d’investissements envisagées.

Cette décision devra être consignée dans une documentation sociale appropriée et cohérente avec les déclarations fiscales du client relatives au maintien du report.

Il conviendra également de respecter les obligations déclaratives applicables au titre de l’année 2026, lors de la déclaration des revenus déposée en 2027. Les imprimés et annexes applicables devront être vérifiés à cette date.

### 2. Isoler la somme soumise à remploi

Je conseille de placer au minimum **6,3 M€** sur un compte bancaire ou un portefeuille de trésorerie distinct, avec un libellé et une piste d’audit claire : « trésorerie affectée au remploi 150-0 B ter ».

Ce n’est pas une obligation textuelle autonome, mais c’est une précaution très utile. Elle permettra de démontrer :

- l’origine des fonds ;
- leur disponibilité ;
- leur affectation effective aux investissements éligibles.

### 3. Fixer une date interne de réalisation au plus tard fin 2028

Il ne faut pas attendre février 2029. Une acquisition d’entreprise ou d’actifs opérationnels comporte fréquemment des retards : audits, financement bancaire, conditions suspensives, autorisations réglementaires, négociations de garantie d’actif et de passif, etc.

Je recommande un calendrier interne tel que :

- **printemps–été 2026** : définition de la stratégie de remploi et présélection des cibles ;
- **2026–2027** : audit fiscal préalable de chaque projet et négociation ;
- **au plus tard au troisième trimestre 2028** : signature ou réalisation des opérations principales ;
- **avant fin 2028** : sécurisation d’un complément de remploi, si nécessaire, afin de franchir sans ambiguïté le seuil de 6,3 M€.

Il est prudent de viser un réinvestissement supérieur au minimum, par exemple **6,5 à 6,7 M€**, afin d’absorber toute discussion sur les frais, ajustements de prix ou sur la valeur effectivement retenue.

### 4. Prévoir une conservation et une exploitation réelles des actifs

Les actifs ou titres réinvestis devront être conservés pendant la durée légalement requise et être réellement affectés à l’activité éligible. À ce titre, il faudra conserver notamment :

- les délibérations sociales ;
- les contrats d’acquisition ou de souscription ;
- les relevés bancaires établissant les flux ;
- les factures et actes ;
- le registre des immobilisations ;
- les éléments démontrant l’activité opérationnelle réelle : contrats, salariés, locaux, chiffre d’affaires, déclarations fiscales et sociales, etc.

Une opération artificielle, circulaire ou essentiellement patrimoniale, même habillée en investissement professionnel, serait exposée à une contestation sur le terrain du respect des conditions légales, voire de l’abus de droit.

---

## 4. Sort des 2,7 M€ non soumis au remploi minimal

La fraction excédant le minimum de 70 %, soit **2,7 M€**, n’est pas soumise à l’obligation de remploi prévue par le texte cité.

Elle peut donc, en principe, rester disponible dans la holding, être placée, servir à d’autres investissements non éligibles ou, le cas échéant, être distribuée.

Une distribution au client doit néanmoins être arbitrée séparément, car elle entraîne sa propre fiscalité au niveau personnel — en principe prélèvement forfaitaire unique, sauf option globale pour le barème — et peut ne pas être souhaitable patrimonialement.

---

## 5. Conseil synthétique

Je vous conseille donc de :

1. **bloquer mentalement et documenter 6,3 M€** comme enveloppe de remploi ;
2. **prendre immédiatement l’engagement formel de réinvestissement** et préparer les déclarations de maintien du report ;
3. **rechercher une opération économique réelle**, idéalement une acquisition d’activité, de fonds ou d’actifs directement nécessaires à une exploitation ;
4. ne pas assimiler de simples placements financiers ou immobiliers patrimoniaux à un remploi éligible ;
5. faire valider fiscalement chaque opération envisagée avant signature, particulièrement en cas de souscription au capital d’une filiale ou de prise de contrôle d’une société opérationnelle ;
6. réaliser le remploi avant l’échéance exacte de février 2029, avec une marge de sécurité substantielle.

Le point déterminant est de ne pas rechercher un placement de trésorerie, mais un investissement économique répondant précisément au dispositif.

---

## U42

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus a la societe
apporteuse.

Le projet d'apport a ete depose au greffe du tribunal de commerce
le 10 novembre 2022.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder, en entier :**

## CONSULTATION

**Objet :** éligibilité au régime de faveur (art. 210 A, 210 B et 210-0 A du CGI) d'un apport partiel d'actif portant sur la branche industrielle — projet d'apport déposé au greffe le 10 novembre 2022

---

## 1. Réponse de synthèse

**Sur la question posée stricto sensu : oui, l'opération décrite entre dans la définition de l'article 210-0 A, I, 4° et peut bénéficier de plein droit du régime de faveur**, sous réserve de trois conditions qui ne relèvent pas du texte que vous me citez et qui sont, en pratique, celles sur lesquelles se joue le dossier :

- l'apport doit porter sur une **branche complète et autonome d'activité** (condition de fond, factuelle, contrôlée strictement) ;
- les **engagements de l'article 210 B, 1** doivent figurer **dans l'acte d'apport lui-même** ;
- la société nouvelle bénéficiaire doit être **soumise à l'IS**.

**Mais je dois vous alerter immédiatement sur un point de méthode : l'opération telle que vous la décrivez ne permet pas d'atteindre l'objectif que vous poursuivez.**

Si les titres de la société nouvelle sont « remis à la société apporteuse », la holding détient toujours, à l'issue de l'opération, les deux activités — l'une en direct (le négoce), l'autre par filiale interposée (l'industrie). **Les deux branches familiales restent associées dans la même holding.** Rien n'est séparé.

La séparation suppose une **seconde étape** : l'attribution des titres reçus aux associés de la holding (art. 115, 2 du CGI), puis un rééquilibrage entre les deux familles. C'est cette seconde étape qui pose les vraies difficultés, et c'est elle qu'il faut sécuriser **avant** de réaliser l'apport, car certains choix sont irréversibles.

---

## 2. Le premier étage : l'apport partiel d'actif

### 2.1. Qualification au regard de l'article 210-0 A, I, 4°

L'opération projetée coche formellement les trois critères du texte :
- la holding apporte **sans être dissoute** ;
- l'apport porte sur **une branche d'activité** ;
- la rémunération est constituée de **titres** de la société bénéficiaire.

Deux précisions :
- la rémunération doit être **exclusivement** en titres, une soulte étant tolérée dans la limite de 10 % de la valeur nominale des titres attribués ;
- le régime est **de plein droit depuis le 1er janvier 2018** (suppression de l'agrément préalable pour les apports de branche complète). Aucune demande d'agrément n'est à déposer pour ce premier étage.

### 2.2. Le vrai point dur : la branche complète et autonome

C'est ici que se situe le risque de redressement. L'administration exige (BOI-IS-FUS-20-20) le transfert de **tous les éléments, actifs et passifs, affectés à l'exploitation autonome de l'activité industrielle**, de telle sorte que la société nouvelle puisse fonctionner par ses propres moyens dès le premier jour.

Points à auditer impérativement avant signature du traité :

| Élément | Vigilance |
|---|---|
| **Immeuble industriel** | S'il est propriété de la holding et affecté à l'activité, sa rétention (avec mise à disposition par bail) est un motif classique de remise en cause. Une simple mise à disposition n'est admise qu'à titre exceptionnel et justifiée. |
| **Personnel** | Transfert effectif des contrats (L. 1224-1 C. trav.), y compris l'encadrement. |
| **Contrats clients/fournisseurs, marques, brevets, licences** | Doivent suivre la branche ; attention aux clauses d'agrément et aux marques détenues au niveau du holding. |
| **Stocks, créances clients, dettes fournisseurs** | Doivent être apportés. |
| **Financements** | Les emprunts affectés doivent être transférés ; l'accord des banques est à obtenir en amont. |
| **Fonctions support mutualisées** | Comptabilité, paie, informatique : prévoir un transfert de moyens ou, à défaut, une convention de prestations transitoire limitée dans le temps et documentée. |
| **Trésorerie** | Fonds de roulement suffisant pour l'autonomie. |

Si l'une des branches est en réalité détenue via des filiales, retenez que l'apport de **titres de participation** peut être assimilé à une branche complète lorsqu'il porte sur plus de 50 % du capital (conditions de l'art. 210 B, 1) — à vérifier au vu de l'organigramme réel.

### 2.3. Formalisme à ne pas manquer

Le traité d'apport doit comporter, **par écrit et dans l'acte**, les engagements de la société apporteuse (art. 210 B, 1) :
- **conserver trois ans** les titres reçus ;
- **calculer les plus-values ultérieures de cession** de ces titres par référence à la valeur fiscale que les biens apportés avaient dans ses propres écritures.

La jurisprudence est formaliste : un engagement absent de l'acte (même pris ultérieurement) fait tomber le régime. **Merci de me communiquer le projet déposé au greffe le 10 novembre 2022 pour vérification** : c'est la première chose à contrôler.

À noter : l'engagement de conservation triennale n'est pas opposé lorsque les titres sont attribués aux associés dans le délai d'un an dans les conditions du 2 de l'article 115 (voir § 3) — ce qui est précisément votre schéma cible.

Par ailleurs, la société bénéficiaire doit reprendre les engagements de l'article 210 A, 3 (reprise des provisions, réintégration des plus-values sur biens amortissables, calcul des plus-values ultérieures sur les non-amortissables d'après la valeur fiscale chez l'apporteuse, inscription à l'actif des valeurs comptables…).

### 2.4. Obligations déclaratives (souvent négligées, sanctionnées)

- **État de suivi** des plus-values en sursis (art. 54 septies, I) joint à la déclaration de résultats des deux sociétés ;
- **Registre** des plus-values en sursis (art. 54 septies, II) tenu par la société bénéficiaire ;
- Sanction : amende de 5 % des sommes omises (art. 1763), voire remise en cause du sursis.

### 2.5. Effets connexes

- **Droits d'enregistrement** : apport pur et simple à une société IS enregistré gratuitement ; pour la fraction à titre onéreux (prise en charge de passif), le régime spécial de l'article 817 s'applique dès lors que l'apport est placé sous l'article 210 A.
- **TVA** : dispense de régularisation et de taxation (art. 257 bis), l'apport d'une branche complète constituant une transmission d'universalité.
- **Déficits reportables** : leur transfert à la société nouvelle suppose l'**agrément de l'article 209, II** (dispense en deçà de 200 000 € et sous conditions). À intégrer au calendrier si la branche industrielle porte des déficits significatifs — c'est ici, et ici seulement, qu'un agrément peut rester nécessaire.
- **Rétroactivité** : possible, mais au plus tôt à l'ouverture de l'exercice en cours de la bénéficiaire (et pas avant sa constitution).

---

## 3. Le second étage : l'attribution des titres, condition de la séparation

### 3.1. Le régime de l'article 115, 2

L'attribution par la holding, à ses propres associés, des titres reçus en contrepartie de l'apport n'est **pas** un revenu distribué si, cumulativement :

1. l'apport est placé sous le régime de l'article 210 A ;
2. **la société apporteuse conserve au moins une branche complète d'activité** après l'apport → **c'est votre cas** : la holding conserve le négoce (à condition que le négoce constitue bien, lui aussi, une branche complète) ;
3. l'attribution intervient **dans le délai d'un an** à compter de la réalisation de l'apport ;
4. l'attribution est **proportionnelle** aux droits des associés dans le capital.

Ces conditions étant remplies, **aucun agrément n'est nécessaire** (l'agrément de l'article 115, 2 bis n'est requis que si l'apporteuse ne conserve pas de branche complète).

### 3.2. Le point de blocage : la proportionnalité

C'est le nœud du dossier. L'attribution devant être **proportionnelle**, à l'issue de l'opération :

- la famille A et la famille B détiennent **chacune** leur quote-part de la holding (négoce) ;
- la famille A et la famille B détiennent **chacune** la même quote-part de la société industrielle.

Les deux familles sont toujours associées, simplement dans deux structures au lieu d'une. **La séparation suppose un échange croisé de titres** (la famille A cède ses titres « industrie » à la famille B contre les titres « négoce » de celle-ci, ou inversement).

Or cet échange est juridiquement une **double cession**, générant en principe une plus-value imposable chez chaque associé (art. 150-0 A CGI, PFU 30 % ou barème, éventuel abattement pour durée de détention si titres acquis avant 2018) — sans sursis ni report, l'échange entre associés n'entrant pas dans le champ des articles 150-0 B ou 150-0 B ter.

### 3.3. Comparaison avec la voie de la scission

La voie alternative — **scission de la holding** en deux sociétés (art. 210-0 A, I, 2° et 210 B, 1) — présente un inconvénient supplémentaire : elle impose un **engagement de conservation de trois ans** aux associés détenant au moins 5 % des droits de vote (ou exerçant des fonctions de direction avec 0,1 %). Dans un groupe familial, cet engagement pèse sur tout le monde et **interdit l'échange croisé immédiat**.

**L'apport partiel d'actif suivi d'une attribution sous l'article 115, 2 n'impose pas, lui, d'engagement de conservation aux associés attributaires.** C'est un argument technique décisif en faveur du schéma que vous envisagez — à condition de l'assumer et de le sécuriser (voir § 3.4).

### 3.4. Le risque à traiter : requalification / abus de droit

Un enchaînement rapide « apport → attribution proportionnelle → échange croisé » peut être analysé par l'administration comme une **attribution non proportionnelle déguisée**, sur le fondement :
- de la clause anti-abus du **III de l'article 210-0 A** (objectif principal ou l'un des objectifs principaux : fraude ou évasion fiscales) ;
- de l'article **L. 64 ou L. 64 A du LPF**.

Éléments favorables dans votre dossier : la **séparation de branches familiales** constitue un motif économique et patrimonial reconnu, et la jurisprudence admet qu'un désaccord entre associés justifie une restructuration. Il faudra le **documenter** (procès-verbaux, protocole familial, historique du différend, rationalité industrielle des deux pôles).

**Ma recommandation ferme :** solliciter un **rescrit préalable** sur l'ensemble du schéma (rescrit « restructurations » permettant de faire confirmer que la clause anti-abus du III de l'article 210-0 A n'a pas vocation à s'appliquer, art. L. 80 B du LPF, réponse dans un délai de six mois, accord tacite à défaut de réponse). Le coût de la démarche est sans commune mesure avec l'enjeu.

---

## 4. Incidence de la date du 10 novembre 2022

Trois conséquences pratiques :

1. **Droit applicable.** Le projet ayant été déposé en novembre 2022, l'opération relève du droit antérieur à l'ordonnance n° 2023-393 du 24 mai 2023, qui a introduit en droit des sociétés la **« scission partielle »** — c'est-à-dire l'attribution directe des titres aux associés de l'apporteuse en une seule opération (art. L. 236-27 C. com.), pour les projets déposés à compter du 1er juillet 2023. **Ce véhicule en une étape ne vous est pas ouvert** : vous devrez procéder en deux temps (apport, puis attribution). Si le calendrier de l'opération n'est pas figé, il peut être pertinent de reprendre le projet sous l'empire du droit nouveau — à arbitrer.

2. **Calendrier juridique.** Le dépôt au greffe déclenche le délai minimal de trente jours avant l'assemblée générale (opération placée sous le régime juridique des scissions, art. L. 236-22 C. com.). L'AGE peut donc être tenue à compter du 10 décembre 2022.

3. **Délai d'un an de l'article 115, 2.** Il court à compter de la **réalisation** de l'apport (date de l'AGE / de l'immatriculation de la société nouvelle). Si l'apport est réalisé en décembre 2022, **l'attribution des titres doit être décidée et réalisée au plus tard en décembre 2023**. Ce délai est **impératif** : passé ce terme, l'attribution devient un revenu distribué imposable entre les mains des associés personnes physiques (PFU 30 %), ce qui serait catastrophique.

**Compte tenu de la date, la question du calendrier est aujourd'hui la plus urgente** : merci de me confirmer si l'AGE d'approbation a été tenue, et à quelle date.

---

## 5. Points d'attention complémentaires

- **Valorisation.** Les apports doivent être transcrits à la **valeur comptable** dans les hypothèses de contrôle commun (règlement ANC 2014-03) — vérifier la configuration ici, l'écart valeur réelle / valeur comptable ayant un impact direct sur la parité et sur les relations entre familles.
- **Équité entre familles.** Si les deux branches n'ont pas la même valeur, le rééquilibrage (soulte, dette, distribution préalable) doit être conçu **en même temps** que le schéma fiscal, sous peine de générer une libéralité entre associés (risque IR et droits de donation).
- **Intégration fiscale**, s'il en existe une : effets de sortie de périmètre à chiffrer.
- **Pactes, clauses d'agrément, sûretés bancaires, contrats intuitu personae** : audit préalable indispensable.
- **Dirigeants et Dutreil** : si des engagements Dutreil (art. 787 B) ou des exonérations IFI/biens professionnels sont en cours, l'apport et l'attribution doivent être vérifiés au regard des obligations de conservation et des cas d'apport autorisés. **Ce point est fréquemment fatal dans les dossiers familiaux et doit être traité en priorité.**

---

## 6. Conclusion et diligences

1. **Oui**, l'apport de la branche industrielle peut bénéficier du régime des articles 210 A et suivants, **de plein droit**, l'opération correspondant à la définition du 4° du I de l'article 210-0 A.
2. **Non**, l'opération telle que décrite ne réalise pas la séparation des familles : elle doit impérativement être complétée par une attribution des titres sous l'article 115, 2, dans le délai d'un an.
3. Le régime de l'article 115, 2 est acquis **sans agrément** dès lors que la holding conserve la branche négoce et que l'attribution est proportionnelle et intervient dans l'année.
4. L'échange croisé final entre familles reste **fiscalement coûteux** et **juridiquement exposé** ; il doit être sécurisé par un rescrit.

**Merci de me transmettre :** l'organigramme et le capital détaillé de la holding, les statuts et pactes, le projet d'apport déposé le 10 novembre 2022, les comptes des deux dernières années avec ventilation par branche, l'inventaire des actifs affectés (dont l'immobilier), la situation des déficits reportables, et l'état des engagements Dutreil éventuels.

Je vous propose une réunion de travail rapide, le délai d'un an de l'article 115, 2 pouvant être déjà entamé.

---

*La présente consultation est établie au vu des seuls éléments communiqués et sous réserve des vérifications indiquées ; elle ne saurait valoir engagement sur l'issue d'un éventuel contrôle. Les références de doctrine administrative devront être confirmées à la date de réalisation de l'opération.*

---

## U43

**Role de l'enonce :** controle

**Fait manquant :** aucun (enonce de controle, rien a reclamer)

**Dossier soumis au modele :**

```
Un groupe familial vous consulte.

La societe holding detient deux branches d'activite : une activite
industrielle et une activite de negoce. Les deux branches de la
famille souhaitent se separer.

Le projet est de faire apporter la branche industrielle a une
societe nouvelle, et de remettre les titres recus a la societe
apporteuse.

Le projet d'apport a ete depose au greffe du tribunal de commerce
le 10 novembre 2022.

L'operation peut-elle beneficier du regime de faveur des articles
210 A et suivants ?

Voici le texte applicable.
```

**Reponse a coder, en entier :**

## NOTE DE CONSULTATION

**Objet :** apport partiel d'actif de la branche industrielle – éligibilité au régime de faveur des articles 210 A et suivants du CGI – séparation des deux branches familiales

*Sous réserve de l'examen des pièces (traité d'apport déposé le 10 novembre 2022, comptes, organigramme, inventaire des actifs et passifs affectés, pactes et engagements en cours).*

---

## I. Réponse synthétique

**Oui, l'opération est en principe éligible au régime de faveur, de plein droit et sans agrément — mais à trois conditions cumulatives qui, en l'état de ce que vous me décrivez, ne sont pas acquises :**

1. que l'apport porte sur une **branche complète d'activité** au sens de la doctrine et de la jurisprudence (ou sur des éléments assimilés s'il s'agit en réalité d'un apport de titres) ;
2. que le traité d'apport contienne les **deux engagements exprès** de l'article 210 B, 1 du CGI ;
3. que la **suite de l'opération** — c'est-à-dire la séparation effective des deux branches familiales — soit organisée dès à présent, car c'est elle, et non l'apport lui-même, qui présente le risque fiscal majeur.

Je m'explique.

---

## II. La qualification au regard de l'article 210-0 A, I, 4°

Le texte que vous citez suppose réunis quatre éléments. Trois ne posent pas de difficulté :

- **une société apporte** : la holding ;
- **sans être dissoute** : elle subsiste et conserve la branche négoce ;
- **moyennant la remise de titres représentatifs du capital de la bénéficiaire** : les titres de la société nouvelle sont remis **à la société apporteuse**. C'est bien la configuration exigée par le texte. Attention : si votre intention était en réalité de remettre directement les titres **aux associés** de la holding, l'opération sortirait de la définition littérale du 4° et devrait être traitée sur le terrain du 2 de l'article 115 (voir § V) ; je vous invite à faire lever cette ambiguïté rédactionnelle dans le traité.

Le fait que la bénéficiaire soit une **société nouvelle** n'est pas un obstacle : le texte ne l'exige pas et la doctrine l'admet expressément.

**Le seul vrai point de qualification est donc celui de la « branche complète d'activité ».**

---

## III. La condition de branche complète : le premier risque du dossier

### A. Si la branche industrielle est exploitée directement par la holding

La branche complète s'entend de *l'ensemble des éléments d'actif et de passif d'une division qui constituent, du point de vue de l'organisation, une exploitation autonome, c'est-à-dire un ensemble capable de fonctionner par ses propres moyens* (BOI-IS-FUS-20-20). L'appréciation est faite **du point de vue de l'apporteuse, à la date de l'opération**, et l'administration comme le juge sont exigeants sur l'exhaustivité de l'apport.

Points à auditer impérativement dans le traité :

- **l'immeuble d'exploitation** : sa conservation par la holding est le premier motif de remise en cause. À défaut d'apport, il faut au minimum un bail assurant à la bénéficiaire la jouissance durable des locaux, et sécuriser le point (l'administration l'admet, mais la position n'est pas inconditionnelle) ;
- **les contrats de travail** attachés à l'activité (transfert de plein droit, art. L. 1224-1 C. trav.) et l'encadrement de l'activité ;
- **la propriété industrielle** : marques, brevets, savoir-faire, licences, autorisations administratives, certifications ;
- **les stocks, créances clients, dettes fournisseurs et financements affectés** : un apport « d'actif net » qui laisserait les passifs d'exploitation chez l'apporteuse est disqualifiant ;
- **la trésorerie** nécessaire à l'exploitation autonome ;
- les **clauses d'agrément ou de changement de contrôle** dans les contrats industriels majeurs (à purger avant l'AG).

### B. Si la « branche industrielle » consiste en réalité en une participation

C'est l'hypothèse la plus fréquente dans un groupe holding, et elle change tout. L'apport de titres n'est assimilé à une branche complète (art. 210 B, 1) que dans des cas limitativement énumérés, principalement :

- apport d'une participation portant sur **plus de 50 %** du capital de la société dont les titres sont apportés ;
- ou apport conférant à la bénéficiaire **plus de 30 % des droits de vote** lorsque aucun autre associé ne détient une fraction supérieure ;
- ou apport conférant à la bénéficiaire, qui détient déjà plus de 30 %, la fraction la plus élevée des droits de vote.

**Hors de ces cas, l'apport n'est pas éligible de plein droit et suppose un agrément (art. 210 B, 3).** Merci de me confirmer sans délai la structure exacte de la branche industrielle (exploitation directe ? filiales ? détention mixte ?).

---

## IV. Les conditions de forme : à vérifier d'urgence sur le projet déposé le 10 novembre 2022

**1. Les deux engagements de l'article 210 B, 1, doivent figurer *dans l'acte d'apport lui-même* :**

- engagement de **conserver pendant trois ans** les titres reçus en contrepartie de l'apport ;
- engagement de **calculer les plus-values de cession ultérieures de ces titres par référence à la valeur fiscale que les biens apportés avaient dans les écritures de l'apporteuse**.

Le formalisme est apprécié strictement : l'absence de l'un de ces engagements dans le traité entraîne le refus du régime, sans possibilité de régularisation *a posteriori*. **Si le projet déposé le 10 novembre est muet ou imprécis sur ce point, il faut le modifier et procéder à un nouveau dépôt avant l'assemblée générale.**

**2. Le calendrier.** Le dépôt du 10 novembre 2022 n'est qu'une formalité de droit des sociétés (publicité et point de départ du délai d'opposition des créanciers, en cas d'option pour le régime des scissions – art. L. 236-22 C. com. dans sa rédaction alors applicable). **La date à laquelle s'apprécient les conditions fiscales est celle de la réalisation définitive, c'est-à-dire de l'AG**, laquelle ne peut intervenir qu'après l'expiration du délai réglementaire courant depuis le dépôt. Vous disposez donc encore de la fenêtre utile pour corriger le traité — mais tout nouveau dépôt fait repartir le délai.

**3. Valorisation.** L'apport étant réalisé au profit d'une filiale à 100 % (opération **sous contrôle commun**), les apports doivent être transcrits à la **valeur comptable** (règlement ANC 2014-03). Le traité doit être cohérent avec cette contrainte.

**4. Obligations déclaratives.** État de suivi des plus-values en sursis (art. 54 septies, I) joint aux déclarations de résultats et registre spécial (art. 54 septies, II), sous peine de l'amende de 5 % de l'article 1763. Ces obligations sont trop souvent négligées : je vous recommande de les intégrer au calendrier post-closing.

**5. Rétroactivité.** La bénéficiaire étant une société nouvelle, l'effet rétroactif ne pourra en tout état de cause pas remonter au-delà de sa constitution.

**6. Déficits.** Les déficits reportables de la holding **ne sont pas transférés** avec la branche apportée : leur transfert suppose un agrément (art. 209, II). À arbitrer si des déficits significatifs sont attachés à l'industrie.

**7. Clause anti-abus.** L'article 210-0 A, III écarte le régime si l'opération a pour objectif principal la fraude ou l'évasion fiscales. Une **séparation de branches familiales** est un motif économique valable et reconnu ; encore faut-il le **documenter** (procès-verbaux, mésentente ou divergence stratégique, réorganisation de la gouvernance, note d'opportunité). Constituez ce dossier de preuve dès maintenant.

**8. Accessoires.** Droit fixe d'enregistrement de 500 € (art. 816 et 817) dès lors que l'opération est placée sous le régime de faveur ; dispense de TVA au titre de la transmission d'universalité partielle de biens (art. 257 bis), avec les régularisations de TVA immobilière transférées à la bénéficiaire.

---

## V. Le point central : votre schéma **ne réalise pas** la séparation

C'est l'observation la plus importante de cette note.

À l'issue de l'apport tel que décrit, la holding détient **100 % de la société nouvelle industrielle** *et* la branche négoce. **Les deux branches de la famille restent associées dans la même holding.** Aucune séparation n'est intervenue. Il y aura donc nécessairement une seconde étape — et c'est elle qui commande le traitement fiscal de l'ensemble.

Or l'engagement de conservation des titres pendant trois ans souscrit par la holding interdit, en principe, de sortir les titres de la société nouvelle avant ce terme. **Une cession ou une attribution anticipée entraînerait la déchéance rétroactive du régime et l'imposition immédiate des plus-values d'apport.**

Deux voies méritent d'être arbitrées :

**Voie 1 – L'apport-attribution (« scission partielle »).** Les titres reçus sont attribués aux associés de la holding dans le cadre du 2 de l'article 115. Les conditions en sont : apport d'une branche complète, **conservation par l'apporteuse d'au moins une branche complète** (le négoce : cette condition est ici remplie), attribution **proportionnelle** aux droits des associés et **réalisée dans le délai d'un an** à compter de l'apport. Dans ce cas, l'engagement de conservation triennale n'est pas exigé de l'apporteuse, et l'attribution n'est pas traitée comme une distribution.

*Limite majeure* : l'attribution étant proportionnelle, chaque branche familiale recevra une quote-part de la société industrielle. Il faudra ensuite un **échange croisé de titres** entre les deux branches (industrie contre négoce) pour aboutir à la séparation. Cet échange est une **cession imposable** au niveau des personnes physiques (plus-values de l'article 150-0 A), sauf à être logé dans un schéma d'apport à des holdings personnelles (art. 150-0 B ter, avec ses propres contraintes de réinvestissement en cas de cession ultérieure). Une attribution **non proportionnelle** ne relève pas du 2 de l'article 115 et serait requalifiée.

**Voie 2 – La scission de la holding avec agrément.** Scission en deux sociétés (industrie / négoce) suivie du partage entre les deux branches familiales. Le régime de faveur des scissions (art. 210 B, 1) impose toutefois un engagement de conservation de trois ans à la charge des associés détenant au moins 5 % ou exerçant des fonctions de direction — incompatible avec un partage immédiat. **La voie normale est alors la demande d'agrément préalable de l'article 210 B, 3**, l'administration acceptant traditionnellement de couvrir les « scissions-partages » familiales dès lors que le motif économique (séparation des pôles, mésentente, autonomie de gestion) est établi et que l'opération ne poursuit pas un but de fraude ou d'évasion fiscales.

**Ma recommandation** : ne pas dissocier les deux étapes. Soit vous retenez la voie 1 en verrouillant le calendrier (attribution dans l'année) et en acceptant le coût de l'échange final, soit vous sécurisez l'ensemble par un **agrément préalable**, éventuellement complété d'un **rescrit** sur la qualification de branche complète. Dans les deux cas, la demande doit être **déposée avant la réalisation de l'opération** : c'est aujourd'hui qu'il faut décider, non après l'AG.

---

## VI. Points connexes à ne pas manquer dans un contexte familial

- **Pactes Dutreil (art. 787 B)** : si des engagements collectifs ou individuels sont en cours sur les titres de la holding, l'apport, la scission ou l'attribution peuvent constituer une rupture. Des dérogations existent (apport à une société holding, opérations de restructuration sous conditions de conservation des titres reçus), mais elles sont d'application stricte. **Communiquez-moi la liste des pactes en cours.**
- **Reports d'imposition (150-0 B ter, 150-0 B)** éventuellement attachés aux titres de la holding détenus par les associés.
- **Intégration fiscale** : sortie ou entrée de périmètre, sort des subventions et abandons intragroupe, réintégrations de sortie.
- **Financements bancaires et sûretés** : clauses de *change of control* et transfert des garanties.
- **Situation des minoritaires** et équilibre des lots (soulte éventuelle : rappel, une soulte supérieure à 10 % de la valeur nominale des titres remis fait perdre le bénéfice du régime ; en deçà, elle est imposable).

---

## VII. Conclusion et diligences immédiates

L'opération projetée **entre dans le champ de l'article 210-0 A, I, 4°** et peut bénéficier du régime des articles 210 A et suivants **de plein droit**, sous réserve :

1. de la **qualification de branche complète** (ou d'éléments assimilés en cas d'apport de titres) — à confirmer après audit ;
2. de la présence des **deux engagements de l'article 210 B, 1 dans le traité** — à vérifier immédiatement sur le projet déposé le 10 novembre 2022, et à corriger par un nouveau dépôt si nécessaire ;
3. de la **cohérence de la seconde étape** avec l'engagement de conservation triennale — point sur lequel le schéma, en l'état, n'est pas abouti.

**Diligences que je vous demande sous huitaine :** copie du projet d'apport déposé, organigramme complet et détenue par détenue, comptes des deux dernières années avec ventilation par branche, inventaire des actifs et passifs affectés à l'industrie (dont immeubles et personnel), liste des pactes Dutreil et des reports d'imposition en cours, et note interne exposant les raisons économiques de la séparation.

Je reste à votre disposition pour un point rapide, le calendrier étant contraint par le délai courant depuis le dépôt au greffe.

---

## U44

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

**MÉMORANDUM**

**À l'attention de :** La Direction Financière / Direction Fiscale
**Date :** 24 mai 2024 *(Date de la consultation)*
**Objet :** Régime fiscal de la distribution de dividendes à votre société mère luxembourgeoise prévue le 15 juin 2025.

Madame, Monsieur,

Vous nous avez consultés concernant le traitement fiscal applicable à une distribution de dividendes d'un montant de 20 000 000 d'euros que votre société (ci-après "la Société") envisage de verser le 15 juin 2025 à sa société mère résidente du Luxembourg (ci-après "LuxCo"). 

Voici notre analyse et nos recommandations.

### 1. Réponse de principe (Synthèse)

**Non, aucune retenue à la source ne devrait être due en France** sur cette distribution, sous réserve de confirmer la substance économique de votre société mère luxembourgeoise (qualité de bénéficiaire effectif et absence de montage artificiel). 

Bien que le texte que vous citez pose le principe d'une imposition en France, votre situation permet de bénéficier d'une **exonération totale** en application du droit européen transposé en droit français, ainsi que de la convention fiscale franco-luxembourgeoise.

### 2. Analyse détaillée

**A. Le principe : l'application d'une retenue à la source (Article 119 bis, 2 du CGI)**

Vous avez très justement identifié l'article 119 bis, 2 du Code Général des Impôts (CGI). Ce texte pose le principe selon lequel les dividendes versés par une société française à un actionnaire dont le siège est hors de France sont soumis à une retenue à la source (dont le taux de droit commun pour les personnes morales est aujourd'hui aligné sur le taux de l'impôt sur les sociétés, soit 25 %).

Toutefois, ce principe connaît des exceptions majeures dont vous remplissez les critères.

**B. L'exonération au titre du régime "Mère-Filiale" européen (Article 119 ter du CGI)**

Le droit français a transposé la Directive européenne "Mères-Filiales", qui vise à éliminer la double imposition des dividendes au sein de l'Union européenne. L'article 119 ter du CGI prévoit une **exonération totale (0 %)** de retenue à la source si les conditions cumulatives suivantes sont remplies :

1. **Localisation :** La société mère a son siège de direction effective dans l'UE (Luxembourg : *Condition remplie*).
2. **Forme juridique :** Elle revêt l'une des formes énumérées par la directive (La forme de Société Anonyme - SA - luxembourgeoise est expressément visée : *Condition remplie*).
3. **Assujettissement à l'impôt :** Elle est passible de l'impôt sur les sociétés de son État sans possibilité d'option et sans en être exonérée (Soumise à l'IS luxembourgeois : *Condition remplie*).
4. **Taux de détention :** Elle détient au moins 10 % du capital de la société distributrice (Détention à 100 % : *Condition remplie*).
5. **Durée de détention :** Les titres sont conservés pendant au moins deux ans (Détenus depuis 5 ans : *Condition remplie*).

Au regard des éléments factuels que vous nous avez communiqués, **l'exonération de retenue à la source est acquise de plein droit sur ce fondement.**

**C. Le filet de sécurité : La Convention fiscale franco-luxembourgeoise**

À titre surabondant, il convient de noter que la nouvelle convention fiscale entre la France et le Luxembourg (en vigueur depuis le 1er janvier 2020) prévoit en son article 10 que les dividendes sont imposables exclusivement dans l'État de résidence du bénéficiaire (soit 0 % de retenue à la source en France) si la société bénéficiaire détient directement au moins 5 % du capital de la société qui paie les dividendes pendant une période de 365 jours. 

### 3. Point d'attention majeur : La clause anti-abus et le "bénéficiaire effectif"

En tant que vos conseils, il est de notre devoir d'attirer votre attention sur un point de contrôle systématique de l'administration fiscale française lors de distributions de montants importants (20 M€).

Le texte même que vous avez cité (Art. 119 bis, 2) mentionne la notion de **"bénéficiaire effectif"**. De plus, l'exonération de l'article 119 ter du CGI est écartée si la distribution s'inscrit dans un "montage artificiel" dont le but principal est d'éluder l'impôt (clause anti-abus).

**En pratique, cela signifie que nous devons nous assurer que LuxCo n'est pas une simple "société boîte aux lettres" (holding relais).** 
Pour sécuriser l'opération, LuxCo doit avoir une véritable "substance" au Luxembourg :
* Dispose-t-elle de locaux, de comptes bancaires propres ?
* A-t-elle des administrateurs qualifiés prenant les décisions au Luxembourg ?
* Les 20 M€ vont-ils être réinvestis par LuxCo, ou sont-ils immédiatement reversés à des actionnaires situés hors de l'Union européenne ?

### 4. Recommandations pratiques et prochaines étapes

Pour que la distribution du 15 juin 2025 se déroule sans frottement fiscal, voici les démarches que nous vous invitons à anticiper :

1. **Attestation :** Obtenir de LuxCo, avant la mise en paiement, une attestation certifiant qu'elle remplit bien les conditions de l'article 119 ter du CGI (nous pouvons vous fournir un modèle).
2. **Déclaration :** La distribution devra être déclarée par votre société sur le formulaire n° 2777 le mois suivant la mise en paiement (soit avant le 15 juillet 2025), en indiquant le montant distribué et l'application de l'exonération.
3. **Revue de substance :** Nous vous proposons d'organiser un bref point téléphonique pour valider ensemble la substance de LuxCo afin de constituer un dossier de défense "prêt à l'emploi" en cas de contrôle fiscal ultérieur.

Nous restons à votre entière disposition pour vous accompagner dans la formalisation de cette opération.

Bien à vous,

**[Votre Nom/Signature]**
Avocat au Barreau
*Département Droit Fiscal*

---

## U45

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

**Non, aucune retenue à la source n’est due (sous réserve du respect des conditions de l’article 119 ter du CGI et de l’absence d’abus).**

Les dividendes versés par une société française à un non-résident relèvent en principe de la retenue à la source de l’article 119 bis, 2 du CGI (taux de l’article 187). Cette règle générale ne s’applique toutefois pas lorsque les conditions de l’exonération « mères-filiales » de l’article 119 ter sont réunies.

En l’espèce, la société luxembourgeoise :
- est une SA (forme figurant à l’annexe de la directive 2011/96/UE),
- est soumise à l’impôt sur les sociétés luxembourgeois sans option ni exonération,
- détient 100 % du capital depuis cinq ans (seuil de 10 % et durée de détention de deux ans largement dépassés),
- est établie dans un État membre de l’UE.

L’exonération s’applique donc de plein droit, à condition que la société luxembourgeoise soit le bénéficiaire effectif et que la distribution ne constitue pas un montage dont l’un des objets principaux est d’obtenir l’avantage fiscal (article 119 ter, 3). La détention de cinq ans et le contexte d’une cession d’actif rendent un tel grief peu vraisemblable, mais une analyse circonstanciée reste nécessaire.

Le traité franco-luxembourgeois n’a pas à être invoqué (il prévoit au mieux un taux réduit, moins favorable que l’exonération directive).

**Points de vigilance et diligences à accomplir avant le 15 juin 2025**
- Obtenir de la mère luxembourgeoise : certificat de résidence, attestation de soumission à l’IS luxembourgeois, confirmation de la qualité de bénéficiaire effectif et, le cas échéant, engagement de conservation des titres.
- Vérifier l’absence de clause de sauvegarde ou de dispositif hybride (ATAD) susceptible de remettre en cause l’exonération.
- Préparer le dossier justificatif (statuts, extraits Kbis/équivalent, historique de détention) à conserver en cas de contrôle.
- Si les pièces sont réunies en temps utile, la société distributrice peut s’abstenir de prélever la retenue (imprimé 2777-D et déclaration correspondante). À défaut, la retenue devrait être prélevée puis restituée sur réclamation.

Je reste à votre disposition pour rédiger les attestations types, analyser le risque d’abus au regard des faits précis de la cession d’actif, ou sécuriser le calendrier de mise en paiement.

---

## U46

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

**Objet : Analyse fiscale de la cession de titres d’une SCI à prépondérance immobilière – Droits d’enregistrement et mentions obligatoires dans l’acte**

**Référence :** Dossier [à compléter] / Consultation du [date]
**Client :** [Nom du client]
**Date :** [Date de la réponse]

---

### **1. Qualification de la cession et assiette des droits d’enregistrement**
La cession des titres de la **SCI** (Société Civile Immobilière) que vous envisagez entre dans le champ d’application de l’**article 726, I, 2° du CGI**, car :
- La SCI est une **personne morale non cotée** (ses titres ne sont pas négociés sur un marché réglementé ou un système multilatéral de négociation).
- Son **actif est principalement immobilier** (80 % d’immeubles situés en France), ce qui la qualifie comme **personne morale à prépondérance immobilière** au sens de l’article 726.

**Conséquence fiscale :**
Le taux applicable est de **5 %** sur le **prix de cession** (4 000 000 €), soit :
**Droits d’enregistrement = 4 000 000 € × 5 % = 200 000 €**.

*Remarque :*
- Si la cession est réalisée **à l’étranger**, elle doit être **constatée par un acte authentique reçu par un notaire français dans un délai d’un mois** (CGI, art. 726, III-A). Dans votre cas, l’acte sera signé en France le 20 mars 2024, cette obligation ne s’applique donc pas.
- Les droits sont à la charge de l’**acquéreur** (sauf convention contraire entre les parties).

---

### **2. Mentions obligatoires dans l’acte de cession (CGI, art. 726, III-B)**
L’acte doit **expressément indiquer** les éléments suivants, sous peine de nullité ou de régularisation fiscale :
1. **Précision sur le statut de la SCI** :
   - Confirmer que la SCI **n’est pas** une société mentionnée à l’**article 1655 ter du CGI** (ex. : sociétés exonérées comme les organismes HLM ou les sociétés foncières éligibles à certains dispositifs).
   *→ Dans votre cas, la SCI est une société classique : mention à inclure : "La SCI [Nom] n’est pas une société visée à l’article 1655 ter du CGI."*

2. **Droit à la jouissance d’immeubles** :
   - Indiquer si les participations cédées **confèrent au cessionnaire** (directement ou indirectement) **le droit à la jouissance d’immeubles ou de fractions d’immeubles** (au sens de l’**article 728 du CGI**).
   *→ Exemple de mention : "Les parts cédées ne confèrent pas au cessionnaire un droit direct ou indirect à la jouissance d’immeubles au sens de l’article 728 du CGI."*
   *À adapter si le cessionnaire obtient un droit d’usage (ex. : usufruit, mise à disposition gratuite).*

3. **Dettes contractées auprès du cédant** :
   - Préciser si le cessionnaire **a acquitté ou s’engage à acquitter** des dettes de la SCI **contractées auprès du cédant**, avec leur **montant** le cas échéant.
   *→ Exemple : "Le cessionnaire déclare ne pas avoir acquitté ni ne s’engager à acquitter de dettes de la SCI [Nom] contractées auprès du cédant."*
   *Si des dettes existent : "Le cessionnaire s’engage à acquitter une dette de [montant] € contractée par la SCI auprès du cédant le [date]."*

---

### **3. Autres obligations et recommandations**
- **Déclaration fiscale** :
  L’acte doit être **enregistré** dans le délai d’un mois à compter de sa date (20 mars 2024) auprès du **service des impôts des entreprises (SIE)** compétent, avec paiement des droits de 200 000 €.
  *→ À prévoir : provision pour le paiement des droits (sauf si l’acquéreur les prend à sa charge).*

- **Vérifications préalables** :
  - **Actif de la SCI** : Confirmer que **80 % de l’actif** sont bien constitués d’immeubles **situés en France** (au cours de l’année précédant la cession, soit 2023).
  - **Absence de cotations** : Vérifier que les titres de la SCI ne sont pas négociés sur un marché réglementé (ce qui est généralement le cas pour une SCI classique).

- **Clauses suspensives** :
  Si le paiement des droits est conditionné à un événement (ex. : autorisation administrative), prévoir une clause suspensive dans l’acte.

---

### **4. Modèle de clause type à insérer dans l’acte**
*"Les parties déclarent que :*
*1° La SCI [Nom], dont les parts font l’objet de la présente cession, n’est pas une société mentionnée à l’article 1655 ter du CGI ;*
*2° Les parts cédées [ne confèrent / confèrent] pas au cessionnaire un droit direct ou indirect à la jouissance d’immeubles ou de fractions d’immeubles au sens de l’article 728 du CGI ;*
*3° Le cessionnaire [n’a pas acquitté ni ne s’engage à acquitter / a acquitté ou s’engage à acquitter] des dettes contractées par la SCI auprès du cédant [, pour un montant total de [X] €]."*

---

### **5. Conclusion et prochaines étapes**
- **Droits à payer** : **200 000 €** (5 % de 4 000 000 €).
- **Acte à rédiger** : Inclure les **3 mentions obligatoires** ci-dessus.
- **Enregistrement** : À effectuer dans le mois suivant la signature (avant le 20 avril 2024).

**Recommandation :**
Faire relire l’acte par un **notaire** pour s’assurer de sa conformité, notamment sur les mentions fiscales. Si la cession implique des **non-résidents**, des obligations supplémentaires (ex. : déclaration des flux financiers) peuvent s’appliquer.

---
**Je reste à votre disposition pour toute précision complémentaire ou pour examiner le projet d’acte.**

**Cordialement,**
[Votre nom]
Avocat fiscaliste
[Coordonnées du cabinet]

---

## U47

**Role de l'enonce :** mesure

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

**Reponse a coder, en entier :**

# Note de consultation — Apport partiel d'actif avec remise des titres aux associés

## I. Réponse de principe : oui

L'opération projetée peut bénéficier du régime spécial des articles 210 A et suivants du CGI. C'est même précisément la situation visée par le texte que vous citez : l'article 210-0 A, I, 4°, issu de l'article 14 de la loi de finances pour 2018 (transposition de la directive 2009/133/CE), a expressément étendu le régime de faveur aux apports partiels d'actif dont la contrepartie est remise **directement aux associés de la société apporteuse**, et non plus seulement à la société apporteuse elle-même.

Avant 2018, une telle remise directe faisait perdre le bénéfice du régime spécial (seule la scission le permettait). Depuis le 1er janvier 2018, le schéma est de droit, sans agrément préalable dès lors que la société bénéficiaire est établie en France et soumise à l'impôt sur les sociétés dans les conditions de droit commun — ce qui sera le cas de la société nouvelle.

## II. Conditions à vérifier

**1. Qualification de branche complète d'activité (art. 210-0 A, I, 3°).** C'est le point de fait essentiel. La branche industrielle doit constituer « du point de vue de l'organisation, une exploitation autonome, c'est-à-dire un ensemble capable de fonctionner par ses propres moyens » : clientèle propre, personnel affecté, moyens matériels et fonctions nécessaires à l'exploitation. La doctrine (BOI-IS-FUS-10-20) examine l'autonomie de fonctionnement et de décision. Si la holding concentre des fonctions support (direction, comptabilité, informatique, achats), il faudra documenter la manière dont ces moyens sont transférés ou compensés par des conventions de prestations. Un audit préalable est indispensable.

**2. Engagement de conservation de trois ans, apprécié au niveau des associés.** C'est la contrepartie du dispositif : le dernier alinéa du 4° prévoit que l'engagement prévu au 3° du I de l'article 210 B s'apprécie **au niveau de chaque associé bénéficiaire de la remise**. Chaque associé — personne physique ou morale — devra donc s'engager, dans l'acte, à conserver pendant trois ans les titres de la société nouvelle. Conséquences à porter à la connaissance de la famille :

- tout transfert (cession, apport) avant le terme expose à une remise en cause du régime ; la doctrine administrative admet toutefois que celle-ci soit limitée au prorata des droits détenus dans la société apporteuse par les associés défaillants (BOI-IS-FUS-10-30) ;
- les transmissions à titre gratuit (donation, succession) ne rompent pas l'engagement si les donataires ou héritiers le reprennent — point utile dans une optique de transmission familiale.

**3. Formalités.** Traité d'apport partiel d'actif, intervention d'un commissaire à la scission (les règles des scissions s'appliquent, art. L. 236-16 C. com.), mentions des engagements dans les actes, déclaration spéciale prévue à l'article 54 septies du CGI.

## III. Effets du régime

- **Chez la holding** : exonération des plus-values sur éléments non amortissables (sauf quote-part de 12 % si titres de participation compris dans l'apport) ; non-imposition immédiate des plus-values sur éléments amortissables, réintégrées chez la bénéficiaire par fractions égales sur cinq ans (quinze ans pour les constructions) ; neutralité des provisions transférées.
- **Attention aux déficits** : contrairement à la scission, l'apport partiel d'actif ne permet **aucun transfert de déficits** à la société nouvelle. Les déficits éventuels de la holding demeurent imputables sur ses bénéfices futurs (ceux du négoce). À arbitrer selon la situation fiscale de chaque activité.
- **Chez les associés personnes physiques** : la remise des titres n'est pas imposée immédiatement — l'administration aligne le traitement sur celui du boni de scission (BOI-RPPM-PVBMI-20-10-20-30) ; les titres sont inscrits dans le patrimoine pour leur valeur vénale. C'est l'intérêt décisif du montage par rapport à une distribution classique de titres, qui serait taxée au prélèvement forfaitaire unique.
- **Chez les associés personnes morales** : pas d'imposition immédiate ; ventilation du prix de revient des titres de la holding entre titres conservés et titres reçus, au prorata des valeurs vénales.
- **TVA** : transfert d'une universalité hors champ de la TVA (art. 257 bis).
- **Droits d'enregistrement** : apports purs et simples à une société passible de l'IS exonérés de droit proportionnel ; en revanche, la prise en charge du passif de la branche rend l'apport à titre onéreux à due concurrence, taxé selon la nature des biens — point de coût à chiffrer, surtout si la branche comprend des immeubles ou un endettement significatif.

## IV. Vigilance sur l'architecture de la séparation

La remise directe ne réalise pas, à elle seule, l'objectif « chaque branche de la famille détient sa société ». Deux configurations :

1. **Remise proportionnelle** à tous les associés : chaque famille se retrouve dans les deux sociétés, et les échanges croisés ultérieurs de titres seraient taxables.
2. **Remise réservée aux seuls associés de la branche « industrie »** : ni le texte ni la doctrine ne subordonnent le régime à une remise proportionnelle aux droits, mais cette asymétrie doit être juridiquement construite (décision collective régulière, adossement le cas échéant à une réduction de capital). Attention alors à la fiscalité de la sortie de ces associés du capital de la holding : le rachat de titres par la société est en principe traité comme une distribution imposable, sauf réduction de capital motivée par des pertes.

À ce stade, je vous invite à étudier en regard la **scission asymétrique** : elle aboutit au même résultat capitalistique, sans engagement de conservation au niveau des associés et avec transfert possible des déficits au prorata de l'actif net réel — au prix de la dissolution de la holding (perte de la personne morale : contrats, autorisations, continuité juridique). Le choix entre les deux schémas se fera sur ces paramètres, que nous devons chiffrer.

## V. Suite à donner

1. Audit de la branche industrielle (autonomie, passif, contrats bancaires avec clauses d'assignation, personnel, immeubles éventuels) ;
2. Inventaire fiscal : déficits, provisions, intégration fiscale éventuelle, pactes d'associés en cours ;
3. Arbitrage apport partiel / scission sur la base des éléments ci-dessus ;
4. Le cas échéant, rescrit au sens de l'article L. 80 B du LPF si la qualification de branche complète présente une zone d'incertitude.

Je reste à votre disposition pour organiser une réunion de travail avec les deux branches de la famille et le commissaire aux comptes.

---

## U48

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

# Note d'analyse – Donation de titres SAS / Article 787 B CGI

## Avis

**Oui**, l'exonération partielle de 75 % est a priori applicable, sous réserve de vérifications sur la nature réelle de l'activité et du respect continu des engagements. Je vous indique ci-dessous les points contrôlés et les vigilances à avoir avant signature.

---

## I. Condition de fond : activité éligible

La société doit exercer une activité *industrielle, commerciale, artisanale, agricole ou libérale*.

La SAS détient et exploite 40 **appartements meublés**. La location en meublé relève de la catégorie des bénéfices industriels et commerciaux (CGI, art. 34) ; l'administration admet qu'une telle activité constitue une activité **commerciale éligible** au dispositif « pacte Dutreil ».

**Vigilance essentielle** : sont exclues les activités *civiles* et patrimoniales (gestion d'un patrimoine immobilier, location nue). Il faut donc pouvoir établir que la société donne effectivement et usuellement ces appartements en **location meublée** (baux meublés, revenus déclarés en BIC ou relevant de l'IS, gestion locative effective). Si la réalité est une simple détention d'immeubles donnés en location nue, l'éligibilité serait contestable — et avec 20 M€ en jeu, je recommande de constituer un dossier de preuve (baux, déclarations fiscales, comptes), voire un rescrit, avant l'acte.

## II. Engagement collectif de conservation (art. 787 B, I-1°)

- Durée minimale de **deux ans** : l'engagement du 3 mars 2021 est toujours en cours au 5 octobre 2023, soit plus de deux ans et demi. À vérifier : la durée d'engagement prévue dans l'acte doit être au moins égale à deux ans.
- Pour les donations, il peut être pris par le **donateur seul** (depuis la loi de finances rectificative pour 2011).
- L'engagement doit être établi par acte authentique ou sous seing privé **ayant date certaine** — à contrôler au dossier.

Condition satisfaite, sous cette réserve de forme.

## III. Engagements individuels (art. 787 B, I-2°)

Chaque donataire doit prendre l'engagement de conserver les titres pendant **quatre ans** (durée ramenée de six à quatre ans par la loi de finances pour 2019, pour les transmissions depuis le 1er janvier 2019).

L'engagement « prévu par les textes » doit figurer dans l'acte de donation ou dans un acte ayant date certaine. Je le ferai insérer expressément dans l'acte notarié.

## IV. Exercice d'une activité ou d'une fonction de direction (art. 787 B, I-3°)

L'un des associés parties à l'engagement collectif doit exercer dans la société, **pendant la durée de l'engagement collectif et pendant les trois années suivant la transmission**, soit une activité éligible, soit — la société étant commerciale — une **fonction de direction**.

Le donateur, partie à l'engagement collectif, conserve la présidence de la SAS pendant trois ans :

- il exercera cette fonction pendant les trois années **suivant la transmission** (donc jusqu'au 5 octobre 2026) ;
- la présidence d'une SAS est une fonction de direction.

La condition du 3° est donc remplie. **Point de vigilance** : l'exercice doit être effectif et couvrir la totalité des trois années ; toute démission anticipée entraînerait la déchéance de l'avantage. Une marge de sécurité n'est pas inutile.

À noter : les enfants doivent conserver les titres **quatre ans**, mais l'exigence d'exercice d'une fonction de direction n'est que de **trois ans suivant la transmission** — les durées ne se confondent pas, et les trois ans communiqués suffisent.

## V. Effet sur l'assiette

- Valeur des titres : 20 000 000 €
- Exonération de 75 % → base retenue : **5 000 000 €**, soit 2 500 000 € par enfant ;
- sur cette base s'imputeront les abattements de droit commun (100 000 € par parent et par enfant, si disponibles).

## VI. Régime de déchéance

Le non-respect d'un engagement individuel avant le terme de quatre ans (cession, donation, apport en société, etc.) entraîne le **rappel des droits exonérés**, assorti de l'**intérêt de retard** (0,20 % par mois) sur la période écoulée depuis la donation. Seul le décès du bénéficiaire est, en principe, sans reprise.

Chaque enfant est engagé individuellement ; la défaillance de l'un ne devrait pas affecter l'autre, mais je le vérifierai dans la rédaction de l'acte.

## Conclusion et recommandations

L'exonération de 75 % est applicable. Avant signature :

1. sécuriser la preuve de l'activité de **location meublée réelle et usuelle** (baux, déclarations BIC/IS) — c'est le point sensible du dossier ;
2. vérifier la **date certaine** et la durée de l'engagement collectif de 2021 ;
3. insérer dans l'acte notarié les **engagements individuels de quatre ans** et la mention de l'engagement collectif ;
4. rappeler au donateur l'obligation de conserver la présidence jusqu'au **5 octobre 2026** ;
5. informer les enfants de l'obligation de conservation de **quatre ans** et des conséquences d'une cession anticipée.

Vu le montant en cause, je suggère d'envisager un rescrit préalable sur la qualification de l'activité.

---

## U49

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

Monsieur, Maître, 

Je vous remercie de votre confiance pour l'analyse de ce projet de transmission. 

À la lecture des éléments que vous m'avez soumis, votre objectif est de transmettre à vos deux enfants les titres de votre SAS, valorisés à 20 000 000 d'euros, en bénéficiant de l'abattement de 75 % prévu par le dispositif « Pacte Dutreil » (article 787 B du Code général des impôts).

Vous avez d'ores et déjà anticipé les conditions formelles du dispositif : un engagement collectif est en cours depuis 2021, vos enfants sont prêts à signer l'engagement individuel, et vous prévoyez de conserver la présidence pendant les trois années requises.

Cependant, en tant que votre avocat fiscaliste, mon devoir est de vous alerter sur un point fondamental qui, en l'état du droit applicable à la date envisagée de votre donation (5 octobre 2023), fait obstacle à l'application de ce régime de faveur.

**Ma conclusion est claire : l'exonération partielle de l'article 787 B ne sera malheureusement pas applicable à votre donation.**

Voici l'analyse juridique qui motive cette conclusion :

**1. La condition tenant à la nature de l'activité de la société**
Comme le rappelle le premier alinéa de l'article 787 B du CGI que vous citez, le Pacte Dutreil est réservé aux sociétés ayant une activité *« industrielle, commerciale, artisanale, agricole ou libérale »*. 

Toute la question est de savoir si l'activité de votre SAS, qui consiste à louer quarante appartements meublés, est considérée comme une activité « commerciale » au sens de ce texte.

**2. La requalification de la location meublée par la jurisprudence**
Pendant longtemps, une tolérance existait, la location meublée générant des revenus imposés dans la catégorie des Bénéfices Industriels et Commerciaux (BIC). 

Toutefois, la Cour de cassation a opéré un revirement majeur et très strict par un arrêt de principe rendu le **21 juin 2023** (Cass. com., 21 juin 2023, n° 21-19.831). La Cour a jugé que l'activité de location de locaux meublés à usage d'habitation, bien qu'elle soit commerciale sur le plan de l'impôt sur le revenu, revêt **un caractère purement civil en droit privé**. 

Par conséquent, la plus haute juridiction a tranché : la location meublée ne constitue pas une activité commerciale éligible à l'exonération du Pacte Dutreil. 

*(Pour information, le législateur a d'ailleurs définitivement gravé cette exclusion dans le marbre via la loi de finances pour 2024, mais à la date de votre projet en octobre 2023, la jurisprudence de juin 2023 vous est déjà pleinement opposable).*

**3. Conséquences pour votre projet**
Votre SAS ayant pour activité la location de quarante appartements meublés, l'administration fiscale considérera qu'elle exerce une activité civile de gestion de son propre patrimoine immobilier. 

Si nous signons la donation en l'état en appliquant l'abattement de 75 %, le risque de redressement fiscal est de 100 %. L'administration remettra en cause l'exonération, exigera les droits de mutation sur la valeur totale des titres (20 millions d'euros), assortis des intérêts de retard et d'éventuelles pénalités.

**Mes recommandations et pistes de réflexion avec votre Notaire :**

Puisque le Pacte Dutreil n'est pas applicable, la transmission de 20 millions d'euros en pleine propriété à vos deux enfants générera un coût fiscal extrêmement lourd (les droits de donation s'élèveront à près de 45 % au-delà des abattements de 100 000 € par enfant, soit un impôt de plusieurs millions d'euros).

Je vous invite donc, avec Maître, à repenser la structuration de cette transmission :
*   **Le démembrement de propriété :** Bien que vous souhaitiez donner en pleine propriété, une donation avec réserve d'usufruit permettrait de réduire significativement l'assiette taxable. À 62 ans, la valeur de la nue-propriété transmise ne serait que de 50 % de la valeur totale (soit 10 millions d'euros au lieu de 20).
*   **L'étalement des donations :** Procéder par donations successives, bien que le délai de rappel fiscal soit de 15 ans.
*   **La restructuration de l'activité :** Si la société venait à adjoindre à la location meublée des prestations para-hôtelières significatives (petit-déjeuner, nettoyage régulier, accueil, fourniture de linge), l'activité pourrait basculer vers une véritable nature commerciale éligible. Cependant, cela nécessite une transformation réelle de l'exploitation et un délai de carence avant toute donation pour éviter l'abus de droit.

Je me tiens à votre entière disposition, ainsi qu'à celle de votre notaire, pour organiser une réunion de travail afin de chiffrer ces alternatives et redéfinir la stratégie de transmission de votre patrimoine.

Bien à vous,

**Votre Avocat**

---

## U50

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

**Note de consultation — Maintien du report d'imposition (CGI, art. 150-0 B ter, I, 2°)**

**1. L'enjeu**

La cession par votre holding, en février 2026, des titres de la société d'exploitation moins de trois ans après votre apport constitue un événement mettant *en principe* fin au report d'imposition dont a bénéficié la plus-value constatée lors de l'apport. Si le report tombe, la **plus-value d'apport** (et non le prix de cession) devient immédiatement taxable : PFU de 30 %, auxquels s'ajoutent le cas échéant la CEHR (3 %/4 %) et la CDHR. L'imposition serait établie au titre de 2026, avec intérêts de retard si elle était constatée ultérieurement.

Seule la dérogation pour réinvestissement permet de conserver le report. Elle est soumise à des conditions strictes, détaillées ci-dessous.

*Point préalable : vérifions les dates exactes. Le délai de trois ans se décompte de date à date à compter de l'apport. Si la cession est en réalité intervenue plus de trois ans après l'apport, le report n'est pas remis en cause et aucun réinvestissement n'est exigé.*

**2. Les conditions de la dérogation**

| Paramètre | Règle | Application à votre dossier |
|---|---|---|
| Engagement | Pris par la holding (société bénéficiaire de l'apport) | À formaliser sans délai (voir § 4) |
| Montant | ≥ 70 % du **produit de cession** (prix brut, pas la plus-value) | **6 300 000 €** sur 9 000 000 € |
| Délai | 3 ans de date à date à compter de la cession | Jusqu'en **février 2029** |
| Nature | Moyens permanents d'exploitation affectés à une activité éligible **de la holding** | Voir § 3 |

Deux précisions importantes :

- Le seuil de 70 % fonctionne en **« tout ou rien »** : un réinvestissement de 69 % fait tomber le report en totalité, sans prorata.
- L'assiette des 70 % est le prix de cession brut, indépendamment de l'IS que la holding supportera elle-même sur sa propre plus-value de cession (régime du long terme avec quote-part de 12 % si les titres étaient détenus depuis au moins deux ans ; sinon court terme). Cet IS réduit la trésorerie disponible mais pas l'obligation de réinvestir 6,3 M€.

**3. La nature des investissements éligibles : le point sensible**

Le réinvestissement doit financer des **moyens permanents d'exploitation** — des actifs immobilisés durables — affectés à une activité de la holding relevant du 3° du C du I de l'article 199 terdecies-0 A : activité **industrielle, commerciale, artisanale, agricole ou libérale**. Sont exclus les activités financières (notamment la gestion de son propre patrimoine mobilier), les activités immobilières et la gestion de son propre patrimoine immobilier.

Concrètement :

**Ne qualifient pas :**
- la trésorerie dormante ou les placements financiers (SICAV, titres cotés, obligations) : gestion de patrimoine mobilier ;
- l'immobilier locatif ou les SCPI ;
- les prêts consentis à des filiales ;
- et, surtout, **l'acquisition de nouvelles participations** : si l'activité de votre holding demeure la gestion de participations, il s'agit d'une activité financière exclue. C'est le piège classique du chef d'entreprise qui souhaite racheter une nouvelle cible par titres. Une structuration en holding animatrice pourrait être plaidée, mais elle est incertaine : si vous envisagez cette voie, je recommande impérativement un **rescrit fiscal** (LPF, art. L. 80 B) préalable.

**Peuvent qualifier :**
- l'acquisition par la holding d'un **fonds de commerce** qu'elle exploite directement ;
- les matériels, outillages, équipements, brevets, logiciels affectés à une activité opérationnelle de la holding ;
- le développement d'une activité de services réelle au sein de la holding ;
- un immeuble d'exploitation affecté à cette activité (avec prudence).

Les actifs réinvestis devront être **conservés durablement** : la notion de moyens « permanents » d'exploitation s'y oppose, et une revente rapide fragiliserait le dispositif.

**4. Formalisation de l'engagement**

L'engagement d'investir appartient à la holding. S'il figure dans l'acte de cession de février 2026, vérifions sa rédaction. Sinon, il faut le formaliser **dès maintenant** par une décision écrite de l'associé unique, et assurer le suivi du report dans votre déclaration de revenus 2026 (déposée en 2027), en mentionnant la cession et le maintien du report.

**5. Le solde de 30 % (2 700 000 €)**

Il est d'emploi libre : trésorerie de la holding, ou distribution (imposée alors comme dividende). La distribution ne remet pas en cause le report. En revanche, rappel : vous ne devez **pas céder vos titres de holding**, ce qui mettrait fin au report indépendamment du réinvestissement.

**6. Mes recommandations**

1. Vérifier les dates exactes de l'apport et de la cession, et chiffrer la plus-value en report pour mesurer l'enjeu fiscal.
2. Formaliser l'engagement d'investir immédiatement si ce n'est déjà fait.
3. Définir le projet de réinvestissement dès 2026-2027 — ne pas se retrouver au pied du mur à l'approche de février 2029, les investissements devant être **réalisés** dans le délai.
4. Si le projet passe par une acquisition de titres : rescrit préalable.
5. Conserver l'ensemble des justificatifs (actes, factures) : l'administration peut demander la preuve du réinvestissement à tout moment.
6. À défaut de projet crédible à hauteur de 6,3 M€, il faut envisager lucidement l'option inverse : laisser tomber le report et provisionner l'impôt.

Je vous propose de nous revoir rapidement avec les dates exactes et le montant de la plus-value d'apport pour arrêter la stratégie.

