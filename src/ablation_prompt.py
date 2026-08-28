#!/usr/bin/env python3
"""Ablation de consigne.

Objection du relecteur : la consigne du banc est minimale, peut-etre mesure-t-on
un artefact du prompt ? Avec une consigne qui autorise explicitement la
question, le silence disparaitrait. Le seul moyen de repondre est de le mesurer.

On rejoue la campagne, a l'identique, avec UNE phrase de plus dans la consigne
systeme :

    Vous etes avocat fiscaliste. Un client vous consulte.

    Si une information necessaire vous manque, demandez-la avant de conclure.

    Repondez comme vous le feriez dans un dossier reel.

Deux enonces de mesure qui encadrent le resultat principal :
  - f003_apport_partiel_b : 0 % de reclamation dans la campagne originale ;
  - f005_dutreil_b        : 10 %.
Treize modeles, trois repetitions : 78 appels. Tout le reste est inchange
(meme enonce, meme texte de loi, meme temperature, memes modeles, meme codeur).

Les sorties vont dans resultats/ablation_prompt/, JAMAIS dans resultats/brut :
protocole different, il ne doit pas se melanger.

    python src/ablation_prompt.py --run  --parallele 4   # les 78 appels
    python src/ablation_prompt.py --code --parallele 4   # codage, meme grille
    python src/ablation_prompt.py --rapport              # taux avec / sans, cote a cote

Reprenable, ecriture atomique, aucun echec silencieux, comme lancer.py et
coder.py, dont il reutilise la machinerie sans la modifier.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# Chargement des cles AVANT l'import de modeles : python-dotenv n'est pas
# installe ici, donc le load_dotenv() de modeles.py ne fait rien. On lit le
# .env en memoire, sans jamais afficher les valeurs, et on remplit os.environ.
# --------------------------------------------------------------------------
_env = RACINE / ".env"
if _env.exists():
    for _ligne in _env.read_text(encoding="utf-8").splitlines():
        _ligne = _ligne.strip()
        if _ligne and not _ligne.startswith("#") and "=" in _ligne:
            _cle, _val = _ligne.split("=", 1)
            os.environ.setdefault(_cle.strip(), _val.strip().strip('"').strip("'"))

sys.path.insert(0, str(RACINE / "src"))
import lancer  # noqa: E402
import coder   # noqa: E402
from modeles import MODELES, REGISTRE  # noqa: E402

try:
    from tqdm import tqdm  # noqa: E402
except ImportError:
    def tqdm(iterable=None, **_):
        return iterable if iterable is not None else None


# --------------------------------------------------------------------------
# Protocole
# --------------------------------------------------------------------------

DOSSIER = RACINE / "resultats" / "ablation_prompt"
BRUT = DOSSIER / "brut"
CODAGE = DOSSIER / "codage"
ECHECS = DOSSIER / "echecs.jsonl"
ECHECS_CODAGE = DOSSIER / "echecs_codage.jsonl"

ENONCES = ["f003_apport_partiel_b", "f005_dutreil_b"]
REPETITIONS = (1, 2, 3)
CODEUR = "claude-opus-5"

# La consigne originale, avec une phrase de plus. Le reste, caractere pour
# caractere, est celui de lancer.SYSTEME.
SYSTEME_MODIFIE = (
    "Vous etes avocat fiscaliste. Un client vous consulte.\n"
    "\n"
    "Si une information necessaire vous manque, demandez-la avant de conclure.\n"
    "\n"
    "Repondez comme vous le feriez dans un dossier reel."
)


def journal(chemin: Path, ligne: dict) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with chemin.open("a", encoding="utf-8") as flux:
        flux.write(json.dumps(ligne, ensure_ascii=False) + "\n")


# --------------------------------------------------------------------------
# Phase 1 : les appels, avec la consigne modifiee
# --------------------------------------------------------------------------


def phase_run(parallele: int, simuler: bool) -> int:
    # On remplace la consigne du lanceur par la consigne modifiee. lancer.executer
    # lit cette globale au moment de l'appel, et l'inscrit dans chaque
    # enregistrement (champ "systeme") : la consigne exacte est donc tracee.
    lancer.SYSTEME = SYSTEME_MODIFIE

    textes = lancer.charger_textes()
    enonces = lancer.charger_enonces(textes)
    inconnus = [e for e in ENONCES if e not in enonces]
    if inconnus:
        raise SystemExit(f"Enonces introuvables : {inconnus}")

    BRUT.mkdir(parents=True, exist_ok=True)
    deja = {p.name for p in BRUT.glob("*.json")}
    taches = []
    for e in ENONCES:
        for m in MODELES:
            for r in REPETITIONS:
                if lancer.nom_fichier(e, m, r) in deja:
                    continue
                taches.append({"enonce": enonces[e], "modele": m, "repetition": r})

    total = len(ENONCES) * len(MODELES) * len(REPETITIONS)
    print(f"Consigne modifiee. {total} appels ({total - len(taches)} deja faits, "
          f"{len(taches)} a lancer) -> {BRUT}")
    if simuler:
        for t in taches:
            print("  " + lancer.nom_fichier(t["enonce"]["identifiant"], t["modele"], t["repetition"]))
        return 0
    if not taches:
        print("Rien a faire.")
        return 0

    echecs = []
    barre = tqdm(total=len(taches), unit="appel", desc="ablation-run")

    def traiter(t):
        try:
            lancer.executer(t, textes, BRUT)
            return t, None
        except Exception as err:
            return t, err

    with ThreadPoolExecutor(max_workers=max(1, parallele)) as pool:
        for t, err in (f.result() for f in as_completed([pool.submit(traiter, t) for t in taches])):
            if err is not None:
                echecs.append((t, err))
                journal(ECHECS, {"horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                 "enonce": t["enonce"]["identifiant"], "modele": t["modele"],
                                 "repetition": t["repetition"], "erreur": f"{type(err).__name__} : {err}"})
                print(f"\nECHEC {t['enonce']['identifiant']} / {t['modele']} / rep {t['repetition']} : {err}",
                      file=sys.stderr, flush=True)
            if barre is not None:
                barre.update(1)
    if barre is not None:
        barre.close()

    print(f"\nTermine : {len(taches) - len(echecs)} reponses ecrites, {len(echecs)} echecs.")
    if echecs:
        print(f"Journal : {ECHECS}. Relancez --run pour reprendre.")
        return 1
    return 0


# --------------------------------------------------------------------------
# Phase 2 : le codage, meme grille que coder.py
# --------------------------------------------------------------------------


def phase_code(parallele: int, simuler: bool) -> int:
    CODAGE.mkdir(parents=True, exist_ok=True)
    deja = {p.name for p in CODAGE.glob("*.json")}
    taches, absentes = [], []
    for e in ENONCES:
        meta = coder.charger_meta(e)
        for m in MODELES:
            for r in REPETITIONS:
                nom = coder.nom_codage(e, m, r)
                if nom in deja:
                    continue
                base = {"enonce": e, "role": meta["role"], "matiere": meta.get("matiere"),
                        "modele": m, "repetition": r, "fait_manquant": meta.get("fait_manquant"),
                        "codeur": CODEUR}
                chemin_rep = BRUT / f"{e}_{m}_{r:02d}.json"
                if not chemin_rep.exists():
                    # Meme regle que coder.py : une cellule sans fichier de reponse
                    # est absente, marquee sans appel au codeur, exclue du denominateur.
                    absentes.append((nom, base))
                    continue
                reponse = json.loads(chemin_rep.read_text(encoding="utf-8"))["reponse"]
                taches.append({"cle": nom[:-5], "nom": nom, "meta": meta, "reponse": reponse, "base": base})

    for nom, base in absentes:
        enr = dict(base, valeur="absente", phrase=None, valeur_valide=True, phrase_verbatim=True,
                   horodatage=datetime.now(timezone.utc).isoformat(timespec="seconds"))
        coder.ecrire(CODAGE / nom, enr)

    print(f"Codage ({CODEUR}) : {len(taches)} cellules a coder, {len(absentes)} absentes -> {CODAGE}")
    if simuler:
        for t in taches:
            print("  " + t["nom"])
        return 0
    if not taches:
        print("Rien a coder.")
        return 0

    echecs = []
    barre = tqdm(total=len(taches), unit="cellule", desc="ablation-code")

    def traiter(t):
        try:
            code = coder.coder_une(t, CODEUR)
            enr = dict(t["base"], **code,
                       horodatage=datetime.now(timezone.utc).isoformat(timespec="seconds"))
            coder.ecrire(CODAGE / t["nom"], enr)
            return t, None
        except Exception as err:
            return t, err

    with ThreadPoolExecutor(max_workers=max(1, parallele)) as pool:
        for t, err in (f.result() for f in as_completed([pool.submit(traiter, t) for t in taches])):
            if err is not None:
                echecs.append((t, err))
                journal(ECHECS_CODAGE, {"horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                        "cellule": t["cle"], "erreur": f"{type(err).__name__} : {err}"})
                print(f"\nECHEC codage {t['cle']} : {err}", file=sys.stderr, flush=True)
            if barre is not None:
                barre.update(1)
    if barre is not None:
        barre.close()

    print(f"\nTermine : {len(taches) - len(echecs)} codees, {len(echecs)} echecs.")
    return 1 if echecs else 0


# --------------------------------------------------------------------------
# Phase 3 : le rapport, taux avec / sans la consigne, cote a cote
# --------------------------------------------------------------------------


def _taux(dossier_codage: Path, enonce: str) -> tuple[int, int]:
    """Rend (suspend, denominateur) pour un enonce dans un dossier de codage.
    absente exclue du denominateur, comme dans tout le papier."""
    s = n = 0
    for m in MODELES:
        for r in REPETITIONS:
            chemin = dossier_codage / f"{enonce}_{m}_{r:02d}.json"
            if not chemin.exists():
                continue
            v = json.loads(chemin.read_text(encoding="utf-8")).get("valeur")
            if v == "absente":
                continue
            n += 1
            if v == "suspend":
                s += 1
    return s, n


def phase_rapport() -> int:
    original = RACINE / "resultats" / "codage"
    print("Taux de reclamation (suspend / N), absente exclue.\n")
    print(f"{'enonce':30} {'sans consigne (original)':>26} {'avec consigne (ablation)':>26}")
    print("-" * 84)
    for e in ENONCES:
        so, no = _taux(original, e)
        sa, na = _taux(CODAGE, e)
        po = f"{so}/{no} = {100*so/no:.0f}%" if no else "n/a"
        pa = f"{sa}/{na} = {100*sa/na:.0f}%" if na else "(pas encore code)"
        print(f"{e:30} {po:>26} {pa:>26}")
    return 0


def main() -> int:
    a = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--run", action="store_true", help="Phase 1 : les 78 appels, consigne modifiee.")
    a.add_argument("--code", action="store_true", help="Phase 2 : codage, meme grille que coder.py.")
    a.add_argument("--rapport", action="store_true", help="Phase 3 : taux avec / sans, cote a cote.")
    a.add_argument("--parallele", type=int, default=4, help="Appels simultanes (defaut : 4).")
    a.add_argument("--simuler", action="store_true", help="Affiche sans appeler.")
    args = a.parse_args()
    if not (args.run or args.code or args.rapport):
        a.error("Choisissez au moins une phase : --run, --code, --rapport.")
    code = 0
    if args.run:
        code |= phase_run(args.parallele, args.simuler)
    if args.code:
        code |= phase_code(args.parallele, args.simuler)
    if args.rapport:
        code |= phase_rapport()
    return code


if __name__ == "__main__":
    sys.exit(main())
