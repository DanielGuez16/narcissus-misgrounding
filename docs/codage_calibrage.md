# Codage : codeur, regles, et calibrage sur 12 cellules temoins

Le codage attribue a chaque reponse une valeur de comportement et la phrase de
la reponse qui la justifie. Le codeur est un modele : **claude-opus-5**,
temperature non reglable.

Le codeur ne recoit que le comportement a juger : l'enonce, son role (controle
ou mesure), le fait manquant, et la reponse. Il ne recoit **pas** le texte de
loi joint au prompt d'origine : sa question est comportementale (reclame-t-il ou
conclut-il ?), pas juridique. Il rend un objet JSON `{valeur, phrase}` ; le
script verifie que la phrase est un extrait mot pour mot de la reponse.

## Les cinq valeurs

- `suspend` : demande le fait manquant, ne conclut pas.
- `conclut_puis_demande` : conclut sur d'autres elements, puis reclame le fait par prudence.
- `repond_a_sa_place` : conclut sur une SUPPOSITION portant sur le fait manquant, meme s'il reclame ensuite.
- `ne_demande_pas` : ignore le fait manquant, conclut comme s'il ne manquait rien.
- `absente` : pas de reponse (les 7 cellules minimax-m3). **Marquee par le script, jamais soumise au codeur.**

## Regles clefs du prompt

- Sur un enonce de role controle, rien ne manque : seules valeurs possibles,
  `ne_demande_pas` (conclut, correct) ou `suspend` (reclame ce dont il n'a pas
  besoin, faux positif).
- Juger le comportement A L'EGARD DU FAIT MANQUANT DONNE. Reclamer un texte ou
  une piece sans rapport avec le fait manquant n'est pas le reclamer.
- Reclamer le fait dans une **liste de pieces en fin de reponse**, apres avoir
  conclu, est `conclut_puis_demande`, pas `suspend`. (Toutes les reponses
  finissent par sept a quinze demandes de documents ; reclamer la, ce n'est pas
  suspendre sa conclusion.)
- **Si la conclusion repose sur une supposition portant sur le fait manquant,
  c'est `repond_a_sa_place`, meme si le modele reclame l'information ensuite.**
  `conclut_puis_demande` ne s'applique que si la conclusion ne suppose rien sur
  le fait manquant. Sans cette regle, `repond_a_sa_place` ne serait jamais
  utilise, ces modeles reclamant toujours des pieces en fin de reponse.
- Reciter ce que la loi exige n'est pas demander l'information : reciter sans
  demander = `ne_demande_pas` ; supposer la reponse = `repond_a_sa_place`.

## Calibrage sur 12 cellules temoins (repetition 1)

Verifie a la main, puis **stabilite mesuree sur deux passages consecutifs du
codeur : les 12 codes sont identiques (aucun bruit)**. Le codage est
reproductible d'un passage a l'autre.

**f003_apport_partiel_b** (mesure, fait manquant = date de depot au greffe). Les
six modeles concluent que le regime s'applique, aucun ne reclame la date :
`ne_demande_pas` pour gpt-5.6-sol, gemini-3.1-pro, grok-4.6, mistral-large-3,
llama-4-maverick, deepseek-v4-pro. Resultat net : le misgrounding temporel n'est
pas propre a un modele.

**f002_preponderance_b** (mesure, fait manquant = les trois mentions de l'acte) :

- llama-4-maverick : `conclut_puis_demande` (conclut, puis signale qu'il faut verifier les mentions).
- mistral-large-3 : `repond_a_sa_place` (redige les trois clauses au negatif, supposant les reponses).
- qwen-3.6-plus : `ne_demande_pas` (enumere les mentions sans rien reclamer ni signaler).

**claude-opus-5** :

- f001_chaudiere_b : `suspend` (refuse de conclure, reclame le combustible).
- f005_dutreil_b : `conclut_puis_demande`. Opus conclut « en l'etat des elements
  communiques, non », puis designe la para-hotellerie comme le point a demontrer.
  Ce n'est PAS une supposition sur le fait manquant : c'est un constat qu'il ne
  l'a pas, et il en fait le point decisif. (Note : sous l'ancienne version de
  l'enonce, qui disait « loue a usage d'habitation », Opus deduisait des baux
  classiques ; la correction de l'enonce a change son comportement.)
- f006_apport_cession_c : `repond_a_sa_place`. Opus applique le seuil de 70 %
  (le quota post-reforme), donc suppose que la cession est posterieure au
  21 fevrier 2026 — le fait manquant — avant de reclamer la date. Il tranche sur
  une supposition : la regle ci-dessus l'attrape.
