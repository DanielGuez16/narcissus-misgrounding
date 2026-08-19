#!/usr/bin/env python3
"""Verification humaine du codage, par double codage en aveugle.

Ce script ne code rien et ne recode rien. Il n'appelle aucun modele : il
n'importe meme pas src/modeles.py, de sorte qu'aucun appel n'est possible. Il
lit resultats/codage/, tire deux echantillons, et prepare de quoi les faire
coder a la main par une seconde personne.

Deux tirages, deux mesures differentes.

  UNIFORME, 50 cellules. Tirage au hasard parmi toutes les cellules codables.
  Il mesure l'accord tel qu'il se produit sur nos donnees, avec leur
  desequilibre reel. C'est le chiffre a rapporter comme fiabilite du codage.

  STRATIFIE, 40 cellules, dix par valeur. Il mesure la capacite a distinguer
  les quatre categories. Sans lui, le kappa uniforme est domine par la valeur
  majoritaire et ne dit rien des trois autres. Il est tire parmi les cellules
  que le tirage uniforme n'a pas prises, pour que les deux feuilles ne se
  recouvrent pas : quatre-vingt-dix cellules distinctes a coder.

Les cellules absentes sont exclues des deux tirages : elles n'ont pas de
reponse, un humain ne peut rien y coder. L'accord porte sur les quatre valeurs
codables.

    python src/verifier_codage.py            # tire et ecrit les feuilles
    python src/verifier_codage.py --accord   # une fois les feuilles remplies

Les deux graines sont fixes et inscrites dans la reference scellee : un tiers
qui relance le script retrouve les memes quatre-vingt-dix cellules.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DOSSIER_ENONCES = RACINE / "benchmark" / "enonces"
DOSSIER_BRUT = RACINE / "resultats" / "brut"
DOSSIER_CODAGE = RACINE / "resultats" / "codage"
DOSSIER_DOUBLE = RACINE / "resultats" / "double_codage"

GRAINE_UNIFORME = 20260819
GRAINE_STRATIFIEE = 20260820
TAILLE_UNIFORME = 50
PAR_VALEUR = 10

# Reprises telles quelles de src/coder.py : la feuille humaine doit porter la
# meme grille que celle soumise au codeur, sans quoi l'accord mesurerait un
# ecart de consigne et non un ecart de jugement.
VALEURS = ["suspend", "conclut_puis_demande", "repond_a_sa_place", "ne_demande_pas"]
VALEURS_CONTROLE = {"ne_demande_pas", "suspend"}

CONSIGNE = """# Double codage, feuille aveugle

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

Portez une valeur par cellule dans `{saisie}`, en face de son etiquette.
N'ouvrez pas `reference_scellee.json` avant d'avoir fini : il contient le codage
du modele, que vous ne devez pas connaitre en codant.
"""


# --------------------------------------------------------------------------
# Lecture
# --------------------------------------------------------------------------


def charger_codages() -> list[dict]:
    codages = []
    for chemin in sorted(DOSSIER_CODAGE.glob("*.json")):
        d = json.loads(chemin.read_text(encoding="utf-8"))
        for champ in ("enonce", "modele", "repetition", "valeur", "role"):
            if champ not in d:
                raise SystemExit(f"{chemin} : champ '{champ}' absent.")
        codages.append(d)
    if not codages:
        raise SystemExit(f"Aucun codage dans {DOSSIER_CODAGE}. Lancez le codage avant.")
    return codages


def codables(codages: list[dict]) -> list[dict]:
    retenus = [c for c in codages if c["valeur"] != "absente"]
    inconnues = {c["valeur"] for c in retenus} - set(VALEURS)
    if inconnues:
        raise SystemExit(f"Valeurs hors nomenclature dans le codage : {sorted(inconnues)}")
    return retenus


def cle(codage: dict) -> str:
    return f"{codage['enonce']}_{codage['modele']}_{codage['repetition']:02d}"


def lire_reponse(codage: dict) -> str:
    chemin = DOSSIER_BRUT / f"{cle(codage)}.json"
    if not chemin.exists():
        raise SystemExit(
            f"{chemin} introuvable, alors que la cellule est codee '{codage['valeur']}'. "
            "Une cellule sans reponse doit etre codee 'absente'."
        )
    return json.loads(chemin.read_text(encoding="utf-8"))["reponse"]


def charger_enonces() -> dict[str, dict]:
    return {
        p.stem: json.loads(p.read_text(encoding="utf-8"))
        for p in sorted(DOSSIER_ENONCES.glob("*.json"))
    }


# --------------------------------------------------------------------------
# Tirages
# --------------------------------------------------------------------------


def tirage_uniforme(cellules: list[dict], taille: int, graine: int) -> list[dict]:
    if taille > len(cellules):
        raise SystemExit(f"{taille} cellules demandees, {len(cellules)} disponibles.")
    ordonnees = sorted(cellules, key=cle)  # ordre stable : le tirage est refaisable
    return random.Random(graine).sample(ordonnees, taille)


def tirage_stratifie(cellules: list[dict], par_valeur: int, graine: int) -> list[dict]:
    alea = random.Random(graine)
    tire = []
    for valeur in VALEURS:
        strate = sorted([c for c in cellules if c["valeur"] == valeur], key=cle)
        if len(strate) < par_valeur:
            raise SystemExit(
                f"Strate '{valeur}' : {len(strate)} cellules disponibles hors tirage "
                f"uniforme, {par_valeur} demandees. Reduisez --par-valeur."
            )
        tire.extend(alea.sample(strate, par_valeur))
    return tire


# --------------------------------------------------------------------------
# Ecriture des feuilles
# --------------------------------------------------------------------------


def ecrire_feuille(nom: str, prefixe: str, echantillon: list[dict], enonces: dict) -> list[dict]:
    """Ecrit la feuille de lecture et la feuille de saisie, rend la table de correspondance.

    La feuille ne porte ni la valeur codee par le modele, ni sa phrase
    justificative, ni le nom du modele evalue, ni l'identifiant de l'enonce :
    les deux derniers laisseraient deviner le role et la matiere. Seule une
    etiquette opaque designe la cellule.
    """
    chemin_lecture = DOSSIER_DOUBLE / f"{nom}_feuille.md"
    chemin_saisie = DOSSIER_DOUBLE / f"{nom}_saisie.csv"

    lignes = [CONSIGNE.format(saisie=chemin_saisie.name), ""]
    correspondance = []
    for numero, codage in enumerate(echantillon, 1):
        etiquette = f"{prefixe}{numero:02d}"
        enonce = enonces[codage["enonce"]]
        manque = enonce["fait_manquant"] or "aucun (enonce de controle, rien a reclamer)"
        lignes += [
            "---", "", f"## {etiquette}", "",
            f"**Role de l'enonce :** {enonce['role']}", "",
            f"**Fait manquant :** {manque}", "",
            "**Dossier soumis au modele :**", "", "```", enonce["enonce"].strip(), "```", "",
            "**Reponse a coder, en entier :**", "", lire_reponse(codage).strip(), "",
        ]
        correspondance.append({
            "etiquette": etiquette,
            "cellule": cle(codage),
            "enonce": codage["enonce"],
            "role": enonce["role"],
            "modele_evalue": codage["modele"],
            "repetition": codage["repetition"],
            "valeur_modele": codage["valeur"],
        })

    chemin_lecture.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    if chemin_saisie.exists():
        print(f"  {chemin_saisie.name} existe deja : laisse tel quel, rien n'est ecrase.")
    else:
        with chemin_saisie.open("w", encoding="utf-8", newline="") as flux:
            graveur = csv.writer(flux)
            graveur.writerow(["etiquette", "role", "code_humain"])
            for entree in correspondance:
                graveur.writerow([entree["etiquette"], entree["role"], ""])
    return correspondance


# --------------------------------------------------------------------------
# Accord
# --------------------------------------------------------------------------


def kappa_de_cohen(paires: list[tuple[str, str]]) -> float:
    total = len(paires)
    observe = sum(1 for a, b in paires if a == b) / total
    un, deux = Counter(a for a, _ in paires), Counter(b for _, b in paires)
    hasard = sum((un[v] / total) * (deux[v] / total) for v in VALEURS)
    if hasard >= 1:
        raise SystemExit(
            "Accord attendu par hasard egal a 1 : les deux codeurs n'ont employe "
            "qu'une seule valeur. Le kappa n'a pas de sens sur cet echantillon."
        )
    return (observe - hasard) / (1 - hasard)


def lire_saisie(chemin: Path, correspondance: list[dict]) -> dict[str, str]:
    if not chemin.exists():
        raise SystemExit(f"{chemin} introuvable. Tirez les echantillons d'abord.")
    roles = {e["etiquette"]: e["role"] for e in correspondance}
    saisi = {}
    with chemin.open(encoding="utf-8") as flux:
        for ligne in csv.DictReader(flux):
            etiquette = (ligne.get("etiquette") or "").strip()
            valeur = (ligne.get("code_humain") or "").strip()
            if not valeur:
                continue
            if etiquette not in roles:
                raise SystemExit(f"{chemin} : etiquette inconnue '{etiquette}'.")
            if valeur not in VALEURS:
                raise SystemExit(
                    f"{chemin}, {etiquette} : valeur '{valeur}' hors nomenclature {VALEURS}."
                )
            if roles[etiquette] == "controle" and valeur not in VALEURS_CONTROLE:
                raise SystemExit(
                    f"{chemin}, {etiquette} : '{valeur}' est impossible sur un enonce de "
                    f"controle. Valeurs admises : {sorted(VALEURS_CONTROLE)}."
                )
            saisi[etiquette] = valeur
    return saisi


def accord_d_un_tirage(nom: str, correspondance: list[dict], saisi: dict[str, str]) -> dict:
    par_etiquette = {e["etiquette"]: e for e in correspondance}
    manquantes = [e for e in par_etiquette if e not in saisi]
    print(f"\n=== {nom} ===")
    if manquantes:
        print(f"{len(manquantes)}/{len(par_etiquette)} cellules non codees a la main : "
              f"{', '.join(sorted(manquantes)[:10])}{' ...' if len(manquantes) > 10 else ''}")
    if not saisi:
        print("Feuille vide, rien a comparer.")
        return {"tirage": nom, "cellules_comparees": 0}

    paires = [(par_etiquette[e]["valeur_modele"], saisi[e]) for e in sorted(saisi)]
    brut = sum(1 for a, b in paires if a == b) / len(paires)
    kappa = kappa_de_cohen(paires)
    print(f"{len(paires)} cellules comparees")
    print(f"  accord brut    : {brut:.1%}")
    print(f"  kappa de Cohen : {kappa:.3f}")

    print("  distribution   : modele / humain")
    for valeur in VALEURS:
        m = sum(1 for a, _ in paires if a == valeur)
        h = sum(1 for _, b in paires if b == valeur)
        print(f"    {valeur:22s} {m:3d} / {h:3d}")

    desaccords = [
        {"etiquette": e, "cellule": par_etiquette[e]["cellule"],
         "modele_evalue": par_etiquette[e]["modele_evalue"],
         "valeur_modele": par_etiquette[e]["valeur_modele"], "valeur_humain": saisi[e]}
        for e in sorted(saisi) if par_etiquette[e]["valeur_modele"] != saisi[e]
    ]
    print(f"  desaccords     : {len(desaccords)}")
    for d in desaccords:
        print(f"    {d['etiquette']} {d['valeur_modele']:22s} vs {d['valeur_humain']:22s} "
              f"({d['cellule']})")
    return {
        "tirage": nom, "cellules_comparees": len(paires),
        "accord_brut": brut, "kappa_de_cohen": kappa,
        "non_codees": sorted(manquantes), "desaccords": desaccords,
    }


def calculer_accord() -> int:
    chemin = DOSSIER_DOUBLE / "reference_scellee.json"
    if not chemin.exists():
        raise SystemExit(f"{chemin} introuvable. Tirez les echantillons d'abord.")
    reference = json.loads(chemin.read_text(encoding="utf-8"))

    resultats = []
    for nom, entree in reference["tirages"].items():
        saisi = lire_saisie(DOSSIER_DOUBLE / entree["fichier_saisie"], entree["correspondance"])
        resultats.append(accord_d_un_tirage(nom, entree["correspondance"], saisi))

    sortie = DOSSIER_DOUBLE / "accord.json"
    sortie.write_text(json.dumps({
        "horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "resultats": resultats,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nEcrit dans {sortie}")
    return 0


# --------------------------------------------------------------------------


def main() -> int:
    analyseur = argparse.ArgumentParser(description="Double codage en aveugle du codage automatique.")
    analyseur.add_argument("--accord", action="store_true",
                           help="Calculer l'accord, une fois les feuilles remplies.")
    analyseur.add_argument("--taille-uniforme", type=int, default=TAILLE_UNIFORME)
    analyseur.add_argument("--par-valeur", type=int, default=PAR_VALEUR)
    arguments = analyseur.parse_args()

    if arguments.accord:
        return calculer_accord()

    enonces = charger_enonces()
    codages = charger_codages()
    cellules = codables(codages)
    absentes = len(codages) - len(cellules)
    repartition = Counter(c["valeur"] for c in cellules)
    print(f"{len(codages)} cellules codees, {absentes} absentes exclues, "
          f"{len(cellules)} codables.")
    for valeur in VALEURS:
        print(f"  {valeur:22s} {repartition[valeur]:4d}")

    DOSSIER_DOUBLE.mkdir(parents=True, exist_ok=True)

    uniforme = tirage_uniforme(cellules, arguments.taille_uniforme, GRAINE_UNIFORME)
    pris = {cle(c) for c in uniforme}
    restantes = [c for c in cellules if cle(c) not in pris]
    stratifie = tirage_stratifie(restantes, arguments.par_valeur, GRAINE_STRATIFIEE)

    print(f"\nTirage uniforme  : {len(uniforme)} cellules, graine {GRAINE_UNIFORME}")
    corr_u = ecrire_feuille("uniforme", "U", uniforme, enonces)
    print(f"Tirage stratifie : {len(stratifie)} cellules, {arguments.par_valeur} par valeur, "
          f"graine {GRAINE_STRATIFIEE}, hors des {len(uniforme)} precedentes")
    corr_s = ecrire_feuille("stratifie", "S", stratifie, enonces)

    recouvrement = {e["cellule"] for e in corr_u} & {e["cellule"] for e in corr_s}
    if recouvrement:
        raise SystemExit(f"Les deux tirages se recouvrent : {sorted(recouvrement)}")

    (DOSSIER_DOUBLE / "reference_scellee.json").write_text(json.dumps({
        "horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "cellules_codables": len(cellules),
        "absentes_exclues": absentes,
        "tirages": {
            "uniforme": {
                "graine": GRAINE_UNIFORME, "taille": len(corr_u),
                "methode": "tirage au hasard parmi toutes les cellules codables",
                "fichier_saisie": "uniforme_saisie.csv", "correspondance": corr_u,
            },
            "stratifie": {
                "graine": GRAINE_STRATIFIEE, "taille": len(corr_s),
                "par_valeur": arguments.par_valeur,
                "methode": "tirage au hasard de N cellules par valeur, hors tirage uniforme",
                "fichier_saisie": "stratifie_saisie.csv", "correspondance": corr_s,
            },
        },
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    total = len(corr_u) + len(corr_s)
    print(f"\n{total} cellules distinctes a coder a la main, dans {DOSSIER_DOUBLE} :")
    print("  uniforme_feuille.md   a lire     uniforme_saisie.csv   a remplir")
    print("  stratifie_feuille.md  a lire     stratifie_saisie.csv  a remplir")
    print("  reference_scellee.json           a n'ouvrir qu'apres")
    print("\nPuis : python src/verifier_codage.py --accord")
    return 0


if __name__ == "__main__":
    sys.exit(main())
