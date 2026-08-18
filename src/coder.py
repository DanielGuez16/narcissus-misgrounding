#!/usr/bin/env python3
"""Codage des reponses. NON ECRIT A CE STADE, VOLONTAIREMENT.

Le script de codage sera ecrit apres la lecture manuelle des reponses de
calibrage, quand les categories seront arretees sur pieces plutot que
devinees a l'avance. Ce fichier tient la place et documente l'intention ;
il ne fait rien et le dit franchement plutot que de rendre un resultat faux.

Entree prevue  : resultats/brut/*.json
Sortie prevue  : resultats/codage/
"""

import sys


def main() -> int:
    print(
        "Le script de codage n'est pas encore ecrit.\n"
        "Etapes prealables :\n"
        "  1. python src/lancer.py --calibrage --modeles <cle>\n"
        "  2. lecture manuelle des treize reponses dans resultats/brut/\n"
        "  3. arret des categories de codage sur ces reponses\n"
        "  4. ecriture de ce script\n",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
