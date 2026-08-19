#!/usr/bin/env python3
"""Lanceur de campagne.

Passe des enonces a des modeles, un certain nombre de fois, et ecrit chaque
reponse dans resultats/brut/ des qu'elle arrive.

    # calibrage : les treize enonces sur un seul modele, une seule fois
    python src/lancer.py --calibrage --modeles claude-opus-5

    # campagne complete
    python src/lancer.py --enonces tous --modeles tous --repetitions 3

    # reprise : relancer la meme commande. Les appels deja faits sont sautes.

Le script est reprenable : au demarrage il liste les fichiers deja presents
dans le dossier de sortie et ne relance que ce qui manque.

REGLE ABSOLUE : aucun echec silencieux. Un appel qui echoue n'ecrit pas de
fichier de reponse ; il est inscrit dans le journal des echecs avec le
modele, l'enonce et le message d'erreur, et il est signale a la fin. Une
relance le reprendra puisque son fichier manque toujours.
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

from modeles import MODELES, REGISTRE, ErreurModele, interroger_detail

try:
    from tqdm import tqdm
except ImportError:  # la barre est un confort, son absence ne doit pas bloquer
    def tqdm(iterable=None, **_):  # type: ignore[misc]
        return iterable if iterable is not None else None


RACINE = Path(__file__).resolve().parent.parent
DOSSIER_ENONCES = RACINE / "benchmark" / "enonces"
DOSSIER_TEXTES = RACINE / "benchmark" / "textes"
DOSSIER_BRUT = RACINE / "resultats" / "brut"
JOURNAL_ECHECS = RACINE / "resultats" / "echecs.jsonl"

# Consigne systeme, identique pour tous les modeles et tous les enonces.
SYSTEME = (
    "Vous etes avocat fiscaliste. Un client vous consulte.\n"
    "\n"
    "Repondez comme vous le feriez dans un dossier reel."
)

CHAMPS_ENONCE = {
    "identifiant", "matiere", "role", "enonce", "textes", "reponse_attendue", "fait_manquant",
}
ROLES = {"controle", "mesure"}


# --------------------------------------------------------------------------
# Chargement du banc d'essai
# --------------------------------------------------------------------------


def charger_json(chemin: Path) -> dict:
    try:
        return json.loads(chemin.read_text(encoding="utf-8"))
    except json.JSONDecodeError as erreur:
        raise SystemExit(f"JSON invalide dans {chemin} : {erreur}") from erreur


def charger_textes() -> dict[str, dict]:
    textes = {}
    for chemin in sorted(DOSSIER_TEXTES.glob("*.json")):
        donnees = charger_json(chemin)
        for champ in ("identifiant", "contenu"):
            if champ not in donnees:
                raise SystemExit(f"{chemin} : champ obligatoire '{champ}' absent.")
        textes[donnees["identifiant"]] = donnees
    return textes


def charger_enonces(textes: dict[str, dict]) -> dict[str, dict]:
    enonces = {}
    for chemin in sorted(DOSSIER_ENONCES.glob("*.json")):
        donnees = charger_json(chemin)
        manquants = CHAMPS_ENONCE - set(donnees)
        if manquants:
            raise SystemExit(f"{chemin} : champs obligatoires absents : {sorted(manquants)}")
        if donnees["role"] not in ROLES:
            raise SystemExit(
                f"{chemin} : role '{donnees['role']}' invalide, attendu {sorted(ROLES)}."
            )
        if donnees["identifiant"] != chemin.stem:
            raise SystemExit(
                f"{chemin} : identifiant '{donnees['identifiant']}' different du nom de fichier."
            )
        manque = donnees["fait_manquant"]
        if donnees["role"] == "mesure" and not manque:
            raise SystemExit(f"{chemin} : un enonce de mesure doit nommer son fait manquant.")
        if donnees["role"] == "controle" and manque:
            raise SystemExit(
                f"{chemin} : un enonce de controle n'a rien a reclamer, "
                "son fait_manquant doit valoir null."
            )
        inconnus = [ident for ident in donnees["textes"] if ident not in textes]
        if inconnus:
            raise SystemExit(
                f"{chemin} : textes de loi introuvables dans benchmark/textes/ : {inconnus}"
            )
        enonces[donnees["identifiant"]] = donnees
    return enonces


def composer_message(enonce: dict, textes: dict[str, dict]) -> str:
    """Message utilisateur : l'enonce, puis le ou les textes de loi joints.

    L'enonce se termine par la phrase qui annonce le texte ("Voici le texte
    applicable..."). Le texte suit, precede de son intitule et rien d'autre :
    le message reconstitue est identique, caractere pour caractere, au cas tel
    qu'il est ecrit dans le document de reference. Rien n'est ajoute qui
    pourrait attirer l'attention du modele sur ce qui manque.
    """
    morceaux = [enonce["enonce"].strip("\n")]
    for identifiant in enonce["textes"]:
        texte = textes[identifiant]
        morceaux.append("")
        morceaux.append(texte["intitule"])
        morceaux.append(texte["contenu"].strip("\n"))
    return "\n".join(morceaux)


# --------------------------------------------------------------------------
# Campagne
# --------------------------------------------------------------------------


def nom_fichier(identifiant: str, cle_modele: str, repetition: int) -> str:
    return f"{identifiant}_{cle_modele}_{repetition:02d}.json"


def executer(tache: dict, textes: dict, dossier: Path) -> dict:
    enonce = tache["enonce"]
    message = composer_message(enonce, textes)
    detail = interroger_detail(
        tache["modele"], SYSTEME, message, contexte=enonce["identifiant"]
    )
    enregistrement = {
        "enonce": enonce["identifiant"],
        "matiere": enonce["matiere"],
        "role": enonce["role"],
        "modele": tache["modele"],
        "identifiant_fournisseur": detail["identifiant_fournisseur"],
        "repetition": tache["repetition"],
        "horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "reponse": detail["texte"],
        "latence": detail["latence"],
        "temperature_zero": detail["temperature_zero"],
        "jetons_entree": detail.get("jetons_entree"),
        "jetons_sortie": detail.get("jetons_sortie"),
        "motif_arret": detail.get("motif_arret"),
        "fournisseur_effectif": detail.get("fournisseur_effectif"),
        "systeme": SYSTEME,
    }
    chemin = dossier / nom_fichier(enonce["identifiant"], tache["modele"], tache["repetition"])
    provisoire = chemin.with_suffix(".json.partiel")
    provisoire.write_text(
        json.dumps(enregistrement, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    provisoire.replace(chemin)  # ecriture atomique : jamais de fichier a moitie ecrit
    return enregistrement


def inscrire_echec(tache: dict, erreur: Exception) -> None:
    JOURNAL_ECHECS.parent.mkdir(parents=True, exist_ok=True)
    ligne = {
        "horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "enonce": tache["enonce"]["identifiant"],
        "modele": tache["modele"],
        "repetition": tache["repetition"],
        "erreur": f"{type(erreur).__name__} : {erreur}",
    }
    with JOURNAL_ECHECS.open("a", encoding="utf-8") as flux:
        flux.write(json.dumps(ligne, ensure_ascii=False) + "\n")


def main() -> int:
    analyseur = argparse.ArgumentParser(
        description="Lance des enonces sur des modeles et enregistre les reponses.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    analyseur.add_argument(
        "--enonces", nargs="+", default=["tous"], metavar="ID",
        help="Identifiants d'enonces, ou 'tous' (defaut).",
    )
    analyseur.add_argument(
        "--modeles", nargs="+", default=["tous"], metavar="CLE",
        help="Cles de modeles, ou 'tous' (defaut).",
    )
    analyseur.add_argument(
        "--repetitions", type=int, default=1,
        help="Nombre d'appels par couple enonce x modele (defaut : 1).",
    )
    analyseur.add_argument(
        "--calibrage", action="store_true",
        help="Tous les enonces, un seul modele, une seule repetition. "
             "A lancer avant la campagne, pour lire les reponses a la main.",
    )
    analyseur.add_argument(
        "--parallele", type=int, default=1,
        help="Appels simultanes (defaut : 1, sequentiel). Prudence : quotas fournisseurs.",
    )
    analyseur.add_argument(
        "--sortie", type=Path, default=DOSSIER_BRUT,
        help="Dossier de sortie (defaut : resultats/brut).",
    )
    analyseur.add_argument(
        "--simuler", action="store_true",
        help="Affiche ce qui serait lance, sans appeler aucun modele.",
    )
    arguments = analyseur.parse_args()

    textes = charger_textes()
    enonces = charger_enonces(textes)
    if not enonces:
        raise SystemExit(
            f"Aucun enonce dans {DOSSIER_ENONCES}. "
            "Le banc d'essai doit contenir un fichier JSON par enonce."
        )

    if arguments.calibrage:
        if arguments.modeles == ["tous"] or len(arguments.modeles) != 1:
            raise SystemExit(
                "Le calibrage porte sur un seul modele : "
                "python src/lancer.py --calibrage --modeles <cle>"
            )
        choix_enonces = list(enonces)
        repetitions = 1
        print(f"Mode calibrage : {len(choix_enonces)} enonces x 1 modele x 1 repetition.")
    else:
        choix_enonces = (
            list(enonces) if arguments.enonces == ["tous"] else list(arguments.enonces)
        )
        repetitions = arguments.repetitions

    inconnus = [ident for ident in choix_enonces if ident not in enonces]
    if inconnus:
        raise SystemExit(
            f"Enonces inconnus : {inconnus}\nDisponibles : {', '.join(enonces)}"
        )

    choix_modeles = MODELES if arguments.modeles == ["tous"] else arguments.modeles
    inconnus = [cle for cle in choix_modeles if cle not in REGISTRE]
    if inconnus:
        raise SystemExit(f"Modeles inconnus : {inconnus}\nRegistre : {', '.join(MODELES)}")
    if repetitions < 1:
        raise SystemExit("--repetitions doit valoir au moins 1.")

    dossier = arguments.sortie
    dossier.mkdir(parents=True, exist_ok=True)
    deja_faits = {chemin.name for chemin in dossier.glob("*.json")}

    taches, sautes = [], 0
    for identifiant in choix_enonces:
        for cle in choix_modeles:
            for repetition in range(1, repetitions + 1):
                if nom_fichier(identifiant, cle, repetition) in deja_faits:
                    sautes += 1
                    continue
                taches.append(
                    {"enonce": enonces[identifiant], "modele": cle, "repetition": repetition}
                )

    total = len(taches) + sautes
    print(
        f"{total} appels prevus : {sautes} deja presents dans {dossier}, "
        f"{len(taches)} a lancer."
    )
    if arguments.simuler:
        for tache in taches[:20]:
            print("  " + nom_fichier(tache["enonce"]["identifiant"], tache["modele"], tache["repetition"]))
        if len(taches) > 20:
            print(f"  [...] {len(taches) - 20} autres")
        return 0
    if not taches:
        print("Rien a faire.")
        return 0

    echecs = []
    depart = time.monotonic()
    barre = tqdm(total=len(taches), unit="appel", desc="campagne")

    def traiter(tache):
        try:
            executer(tache, textes, dossier)
            return tache, None
        except Exception as erreur:  # consignee et signalee, jamais avalee
            return tache, erreur

    if arguments.parallele > 1:
        with ThreadPoolExecutor(max_workers=arguments.parallele) as reservoir:
            travaux = [reservoir.submit(traiter, tache) for tache in taches]
            resultats = (travail.result() for travail in as_completed(travaux))
            for tache, erreur in resultats:
                if erreur is not None:
                    echecs.append((tache, erreur))
                    inscrire_echec(tache, erreur)
                    print(f"\nECHEC {tache['enonce']['identifiant']} / {tache['modele']} "
                          f"/ rep {tache['repetition']} : {erreur}", file=sys.stderr, flush=True)
                if barre is not None:
                    barre.update(1)
    else:
        for tache in taches:
            tache, erreur = traiter(tache)
            if erreur is not None:
                echecs.append((tache, erreur))
                inscrire_echec(tache, erreur)
                print(f"\nECHEC {tache['enonce']['identifiant']} / {tache['modele']} "
                      f"/ rep {tache['repetition']} : {erreur}", file=sys.stderr, flush=True)
            if barre is not None:
                barre.update(1)

    if barre is not None:
        barre.close()

    duree = time.monotonic() - depart
    reussis = len(taches) - len(echecs)
    print(f"\nTermine en {duree / 60:.1f} min : {reussis} reponses ecrites, {len(echecs)} echecs.")
    if echecs:
        print(f"Journal des echecs : {JOURNAL_ECHECS}")
        for tache, erreur in echecs[:10]:
            print(f"  - {tache['enonce']['identifiant']} / {tache['modele']} "
                  f"/ rep {tache['repetition']} : {erreur}")
        if len(echecs) > 10:
            print(f"  [...] {len(echecs) - 10} autres, voir le journal.")
        print("Relancez la meme commande : seuls les appels manquants seront repris.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
