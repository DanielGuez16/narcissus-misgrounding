#!/usr/bin/env python3
"""Test de disponibilite des treize modeles.

Premier script a lancer. Envoie une question triviale a chaque modele et
affiche : le modele, la reponse, la latence, le statut. Si un modele ne
repond pas, on le sait avant d'engager la campagne.

    python src/tester_modeles.py
    python src/tester_modeles.py --modeles claude-opus-5 grok-4.6

Code de sortie 0 si les treize repondent, 1 sinon. Les echecs sont affiches
en entier, avec le message d'erreur du fournisseur : rien n'est avale.
"""

from __future__ import annotations

import argparse
import sys
import time

from modeles import MODELES, REGISTRE, ErreurModele, interroger_detail

SYSTEME = "Vous repondez de facon breve."
QUESTION = "En un seul mot : quelle est la capitale de la France ?"


def main() -> int:
    analyseur = argparse.ArgumentParser(description="Test des modeles du registre.")
    analyseur.add_argument(
        "--modeles",
        nargs="+",
        default=MODELES,
        metavar="CLE",
        help="Modeles a tester (par defaut : les treize du registre).",
    )
    arguments = analyseur.parse_args()

    inconnus = [cle for cle in arguments.modeles if cle not in REGISTRE]
    if inconnus:
        print(f"Modeles inconnus : {', '.join(inconnus)}", file=sys.stderr)
        print(f"Registre : {', '.join(MODELES)}", file=sys.stderr)
        return 1

    print(f"Test de {len(arguments.modeles)} modeles.")
    print(f"Question : {QUESTION}\n")

    reussites, echecs = [], []
    for cle in arguments.modeles:
        fiche = REGISTRE[cle]
        etiquette = f"{cle} ({fiche.famille}, {fiche.dorsale}, {fiche.identifiant_effectif()})"
        print(f"--- {etiquette}")
        depart = time.monotonic()
        try:
            detail = interroger_detail(cle, SYSTEME, QUESTION, contexte="test_disponibilite")
        except ErreurModele as erreur:
            latence = time.monotonic() - depart
            print(f"    statut   : ECHEC apres {latence:.2f}s")
            print(f"    erreur   : {erreur}\n")
            echecs.append((cle, str(erreur)))
            continue

        reponse = " ".join(detail["texte"].split())
        if len(reponse) > 200:
            reponse = reponse[:200] + " [...]"
        print(f"    reponse  : {reponse}")
        print(f"    latence  : {detail['latence']:.2f}s")
        temperature = "0" if detail["temperature_zero"] else "non reglable"
        print(f"    jetons   : {detail.get('jetons_entree')} entree / "
              f"{detail.get('jetons_sortie')} sortie | temperature : {temperature}")
        if detail.get("fournisseur_effectif"):
            print(f"    routage  : {detail['fournisseur_effectif']}")
        print("    statut   : OK\n")
        reussites.append(cle)

    print("=" * 70)
    print(f"OK    : {len(reussites)}/{len(arguments.modeles)}  {', '.join(reussites) or '-'}")
    print(f"ECHEC : {len(echecs)}/{len(arguments.modeles)}  "
          f"{', '.join(cle for cle, _ in echecs) or '-'}")
    if echecs:
        print("\nDetail des echecs :")
        for cle, message in echecs:
            print(f"  - {cle} : {message}")
        print(
            "\nUn identifiant fournisseur errone (HTTP 404) se corrige sans toucher au "
            "code, par NARCISSUS_ID_<CLE> dans .env. Voir le README."
        )
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
