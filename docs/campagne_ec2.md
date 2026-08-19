# Faire tourner la campagne sur une instance EC2

Procedure pas a pas pour lancer les 507 appels (13 enonces x 13 modeles x 3
repetitions) sur une instance EC2, sans laisser tourner sa propre machine.
Ecrite pour un acces **SSM** (ssm-user avec sudo), sans SSH ni cle privee.

Le depot est **prive** : le clone demande un jeton. Les resultats sont
volumineux au sens du versionnement (ignores par `.gitignore`) mais legers en
octets (~507 fichiers JSON, quelques Mo) : on les recupere par une branche git
dediee, ce qui evite S3 et scp.

---

## Prerequis

```bash
python3 --version                 # 3.10 ou plus
sudo dnf install -y git tmux      # Amazon Linux ; sur Ubuntu : sudo apt-get install -y git tmux
```

## 1. Deposer le depot (prive -> jeton)

Cree sur GitHub un **fine-grained PAT** limite a ce depot, permission
**Contents: Read and write** (le "write" sert a repousser les resultats en fin
de course).

```bash
git clone https://github.com/DanielGuez16/narcissus-misgrounding.git
# a l'invite : Username = DanielGuez16 ; Password = colle le PAT
cd narcissus-misgrounding
```

Le clone part de zero : `resultats/brut/` est vide (ignore par git), donc les
507 appels tourneront tous.

## 2. Deposer les cles sans les versionner

```bash
cp .env.exemple .env
nano .env      # renseigne ANTHROPIC_API_KEY et OPENROUTER_API_KEY, puis Ctrl-O, Ctrl-X
```

`.env` est deja dans `.gitignore` : il ne sera jamais commite. `modeles.py` le
charge automatiquement (python-dotenv). Ne mets jamais le PAT ni les cles dans
un fichier suivi ; si tu as colle le PAT dans l'URL du remote, remets l'URL
propre apres :

```bash
git remote set-url origin https://github.com/DanielGuez16/narcissus-misgrounding.git
```

## 3. Environnement et dependances

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Verifier les 13 modeles avant d'engager la campagne

```bash
python src/tester_modeles.py
```

Code de sortie 0 si les treize repondent. Un identifiant fournisseur faux se
manifeste par un 404 explicite ; corrige-le via `NARCISSUS_ID_<CLE>` dans
`.env`, sans toucher au code.

## 5. Lancer en arriere-plan et se deconnecter (tmux)

`tmux` survit a la fermeture de la session SSM (son serveur est un demon).

```bash
tmux new -s campagne
# --- dans la fenetre tmux ---
source .venv/bin/activate
python src/lancer.py --enonces tous --modeles tous --repetitions 3 --parallele 6 \
    2>&1 | tee campagne.log
# detacher sans arreter : Ctrl-b puis d
```

Tu peux alors fermer la session SSM : la campagne continue. `--parallele 6` est
prudent (les taches consecutives visent des modeles differents, donc des
fournisseurs differents, ce qui etale la charge). Monte a 10 si tout passe ;
evite 20 (plusieurs modeles partagent un meme fournisseur).

## 6. Suivre l'avancement a distance

Reconnecte-toi en SSM, puis :

```bash
cd narcissus-misgrounding
ls resultats/brut/*.json | wc -l               # progression vers 507
wc -l resultats/echecs.jsonl 2>/dev/null       # echecs eventuels
tmux attach -t campagne                         # revoir la barre en direct (Ctrl-b d pour re-detacher)
tail -f campagne.log
```

## 7. Si l'instance s'arrete ou redemarre pendant la campagne

**La reprise est concue pour ca, et elle est verifiee.** Au demarrage, le
lanceur liste les fichiers deja presents dans le dossier de sortie et ne
relance **que ce qui manque**. Chaque reponse est ecrite de facon atomique
(`.json.partiel` puis `replace`) : un appel coupe en plein vol ne laisse jamais
de fichier a moitie ecrit, et sera simplement refait.

Apres un redemarrage, il suffit de relancer **la meme commande** :

```bash
source .venv/bin/activate
python src/lancer.py --enonces tous --modeles tous --repetitions 3 --parallele 6 \
    2>&1 | tee -a campagne.log
```

Le lanceur affiche alors, par exemple, `507 appels prevus : 431 deja presents,
76 a lancer.` et ne refait que les 76.

> **Test verifie (19 aout 2026).** llama-4-maverick, 13 enonces en sequentiel.
> Processus tue par `kill -9` a **3/13** (equivalent d'un arret machine) :
> aucun residu `.partiel`. Relance de la meme commande -> en-tete
> `13 appels prevus : 3 deja presents dans resultats/test_reprise, 10 a lancer`,
> resultat final **13/13, 0 echec**. Seuls les 10 manquants ont ete refaits.

**Echecs vs interruptions.** Un appel qui echoue (reseau, debit) n'ecrit pas de
fichier : il est journalise dans `resultats/echecs.jsonl` et repris a la
relance, puisque son fichier manque toujours. En cas de depassement de debit
(HTTP 429), chaque appel est deja reessaye sur place avec attente croissante
(Retry-After du fournisseur s'il est fourni, sinon backoff exponentiel plafonne
avec jitter) avant d'etre eventuellement journalise.

**Une reserve, propre a Opus 5.** Les reponses les plus longues (jusqu'a 32 000
jetons) peuvent depasser 10 minutes et echouer avec un message du SDK Anthropic
« Streaming is required for operations that may take longer than 10 minutes ».
Cet echec est **deterministe** : la reprise seule ne le guerira pas. Si l'un des
couples Opus 5 x enonce long (typiquement `f003_apport_partiel_b`) reste en
echec apres relance, il faut activer le streaming cote Anthropic ou plafonner
les jetons pour ce cas ; ce n'est pas gere automatiquement a ce jour.

## 8. Recuperer les resultats a la fin

Les resultats sont ignores par git mais legers en octets : on les repousse sur
une **branche dediee** (methode compatible SSM, sans SSH).

```bash
git checkout -b resultats-run1
git add -f resultats/brut resultats/echecs.jsonl
git commit -m "Resultats campagne run1 (507 appels, 3 reps)"
git push origin resultats-run1
```

Puis, sur ta machine :

```bash
git fetch origin && git checkout resultats-run1
```

Variantes si tu preferes : `tar czf resultats.tgz resultats/brut && aws s3 cp
resultats.tgz s3://<ton-bucket>/` (si le role de l'instance autorise S3), ou
`scp` si un acces SSH est disponible.

## Garde-fous

- **Budget.** Recharge OpenRouter a ~50 EUR (25 EUR est trop juste) ; prevois
  ~10 EUR cote Anthropic pour Opus 5, qui passe par l'API directe et non par
  OpenRouter.
- **Debit.** Si un modele renvoie des 429 en boucle, baisse `--parallele` ; le
  backoff + Retry-After absorbe le reste et rien n'est perdu (reprise par simple
  relance de la meme commande).
- **Fraicheur du clone.** Lance la campagne sur un clone frais (dossier
  `resultats/brut/` vide), pour ne pas confondre une reprise avec un melange de
  resultats d'un run anterieur.
