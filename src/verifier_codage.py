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
GRAINE_MELANGE = 20260821
GRAINE_CIBLE = 20260822
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
    """Tire N cellules par valeur, PUIS melange l'ordre de presentation.

    Le melange n'est pas cosmetique. Sans lui, les strates se suivent en blocs
    de N reponses de meme valeur, et la feuille cesse d'etre aveugle : un
    codeur qui lit dix reponses semblables d'affilee en deduit la structure du
    tirage et code la onzieme en connaissant sa categorie. Le premier tirage
    stratifie, ecrit avant ce correctif, presentait ce defaut.
    """
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
    random.Random(GRAINE_MELANGE).shuffle(tire)
    return tire


def tirage_cible(cellules: list[dict], enonces_vises: list[str], negatifs: int,
                 graine: int, deja: set[str]) -> tuple[list[dict], dict]:
    """Toutes les cellules positives de certains enonces, plus des negatifs tires.

    Les tirages uniforme et stratifie ne contiennent aucun positif issu de ces
    enonces : le kappa qu'ils donnent ne mesure donc pas la fiabilite du chiffre
    que le papier avance. Ce lot y remedie en prenant les positifs un par un,
    puisqu'ils sont trop rares pour qu'un tirage au hasard en attrape.

    Les positifs sont pris tous, meme deja vus : il n'y en a pas d'autres. Les
    negatifs, eux, sont tires hors de tout ce qui a deja ete soumis a un codeur.
    """
    vises = [c for c in cellules if c["enonce"] in enonces_vises]
    positifs = [c for c in vises if c["valeur"] == "suspend"]
    negatifs_dispo = sorted(
        [c for c in vises if c["valeur"] != "suspend" and cle(c) not in deja], key=cle
    )
    if len(negatifs_dispo) < negatifs:
        raise SystemExit(
            f"{negatifs} negatifs demandes, {len(negatifs_dispo)} disponibles hors "
            "cellules deja soumises a un codeur."
        )
    alea = random.Random(graine)
    echantillon = sorted(positifs, key=cle) + alea.sample(negatifs_dispo, negatifs)

    # Melange, sous contrainte : deux positifs ne doivent pas se suivre, sans quoi
    # le codeur voit une serie et en deduit ce qu'on lui cache.
    for essai in range(1, 1001):
        alea.shuffle(echantillon)
        rangs = [i for i, c in enumerate(echantillon) if c["valeur"] == "suspend"]
        if all(b - a > 1 for a, b in zip(rangs, rangs[1:])):
            break
    else:
        raise SystemExit("Aucun melange trouve ou les positifs ne se suivent pas.")

    detail = {
        "positifs": len(positifs), "negatifs": negatifs,
        "enonces_vises": enonces_vises, "melanges_essayes": essai,
        "positifs_deja_soumis": sorted(cle(c) for c in positifs if cle(c) in deja),
    }
    return echantillon, detail


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
# Saisie interactive
# --------------------------------------------------------------------------

TRAIT = "\u2500"

DEFINITIONS = {
    "suspend": "il reclame le fait manquant et ne conclut pas",
    "conclut_puis_demande": "il conclut sur d'autres elements, puis reclame le fait",
    "repond_a_sa_place": "il conclut sur une supposition portant sur le fait manquant",
    "ne_demande_pas": "il ignore le fait manquant et conclut",
}


def _largeur() -> int:
    import shutil
    return min(shutil.get_terminal_size((100, 40)).columns, 100)


def _effacer() -> None:
    print("\033[2J\033[H", end="")


def afficher_cellule(rang: int, total: int, entree: dict, enonce: dict, reponse: str) -> list[str]:
    """Affiche une cellule et rend la liste des valeurs proposees, dans l'ordre montre.

    Ne montrent jamais : le nom du modele evalue, l'identifiant de l'enonce, la
    valeur codee par le modele, sa phrase justificative.
    """
    largeur = _largeur()
    _effacer()
    print(TRAIT * largeur)
    print(f"  {rang} sur {total}")
    print(TRAIT * largeur)
    manque = enonce["fait_manquant"] or "aucun (enonce de controle, rien a reclamer)"
    print("\nFAIT MANQUANT\n")
    print("  " + manque)
    print("\n" + TRAIT * largeur)
    print("DOSSIER SOUMIS AU MODELE")
    print(TRAIT * largeur + "\n")
    print(enonce["enonce"].strip())
    print("\n" + TRAIT * largeur)
    print("REPONSE DU MODELE")
    print(TRAIT * largeur + "\n")
    print(reponse.strip())
    print("\n" + TRAIT * largeur)

    proposees = [v for v in VALEURS if enonce["role"] != "controle" or v in VALEURS_CONTROLE]
    for numero, valeur in enumerate(proposees, 1):
        print(f"  {numero}  {valeur:22s} {DEFINITIONS[valeur]}")
    print(f"\n  r  revoir cette reponse        q  quitter et reprendre plus tard")
    print(TRAIT * largeur)
    return proposees


def enregistrer(chemin: Path, correspondance: list[dict], saisi: dict[str, str]) -> None:
    provisoire = chemin.with_suffix(".csv.partiel")
    with provisoire.open("w", encoding="utf-8", newline="") as flux:
        graveur = csv.writer(flux)
        graveur.writerow(["etiquette", "role", "code_humain"])
        for entree in correspondance:
            graveur.writerow([entree["etiquette"], entree["role"],
                              saisi.get(entree["etiquette"], "")])
    provisoire.replace(chemin)


def saisir(nom: str) -> int:
    """Codage a la main, une cellule a la fois, reprenable."""
    reference = charger_reference()
    if not reference or nom not in reference["tirages"]:
        raise SystemExit(f"Tirage '{nom}' introuvable dans la reference scellee.")
    entree = reference["tirages"][nom]
    correspondance = entree["correspondance"]
    chemin_saisie = DOSSIER_DOUBLE / entree["fichier_saisie"]
    enonces = charger_enonces()

    saisi = {}
    if chemin_saisie.exists():
        with chemin_saisie.open(encoding="utf-8") as flux:
            for ligne in csv.DictReader(flux):
                valeur = (ligne.get("code_humain") or "").strip()
                if valeur:
                    saisi[ligne["etiquette"]] = valeur

    total = len(correspondance)
    restantes = [(i, c) for i, c in enumerate(correspondance, 1)
                 if c["etiquette"] not in saisi]
    if not restantes:
        print(f"Les {total} cellules de '{nom}' sont deja codees.")
        print(f"Accord : python src/verifier_codage.py --accord --tirage {nom}")
        return 0
    if len(saisi):
        print(f"{len(saisi)} cellules deja codees, reprise a la {restantes[0][0]}e.")

    for rang, cellule in restantes:
        enonce = enonces[cellule["enonce"]]
        reponse = json.loads(
            (DOSSIER_BRUT / f"{cellule['cellule']}.json").read_text(encoding="utf-8")
        )["reponse"]
        proposees = afficher_cellule(rang, total, cellule, enonce, reponse)
        while True:
            try:
                touche = input("  Votre code : ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print(f"\n\nArret. {len(saisi)}/{total} codees.")
                print(f"Reprendre : python src/verifier_codage.py --saisir {nom}")
                return 0
            if touche == "q":
                print(f"\nArret. {len(saisi)}/{total} codees.")
                print(f"Reprendre : python src/verifier_codage.py --saisir {nom}")
                return 0
            if touche == "r":
                proposees = afficher_cellule(rang, total, cellule, enonce, reponse)
                continue
            if touche.isdigit() and 1 <= int(touche) <= len(proposees):
                saisi[cellule["etiquette"]] = proposees[int(touche) - 1]
                enregistrer(chemin_saisie, correspondance, saisi)
                break
            print(f"  Tapez un chiffre de 1 a {len(proposees)}, ou r, ou q.")

    print(f"\nLes {total} cellules sont codees.")
    print(f"Accord : python src/verifier_codage.py --accord --tirage {nom}")
    return 0


# --------------------------------------------------------------------------
# Accord
# --------------------------------------------------------------------------


class KappaDegenere(Exception):
    """Un codeur n'a employe qu'une seule valeur : le kappa ne mesure plus rien.

    Quand un codeur code tout a l'identique, l'accord attendu par hasard egale
    l'accord observe, et le kappa vaut zero par construction, quel que soit le
    contenu. Le nombre existe, il ne veut rien dire. Le rendre serait pire que
    ne rien rendre : il a l'apparence d'un resultat.
    """


def kappa_de_cohen(paires: list[tuple[str, str]]) -> float:
    total = len(paires)
    observe = sum(1 for a, b in paires if a == b) / total
    un, deux = Counter(a for a, _ in paires), Counter(b for _, b in paires)
    for nom, compte in (("le codage automatique", un), ("le codage a la main", deux)):
        if len(compte) == 1 and total > 1:
            raise KappaDegenere(
                f"{nom} n'emploie qu'une seule valeur, '{next(iter(compte))}', sur les "
                f"{total} cellules. Le kappa vaudrait zero par construction et ne "
                "mesurerait rien."
            )
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
    print(f"{len(paires)} cellules comparees")
    print(f"  accord brut    : {brut:.1%}")
    try:
        kappa = kappa_de_cohen(paires)
        print(f"  kappa de Cohen : {kappa:.3f}")
    except KappaDegenere as anomalie:
        kappa = None
        print(f"  kappa de Cohen : NON CALCULE")
        print(f"    {anomalie}")
        print("    Un codage constant n'est pas un codage. Verifiez la feuille de saisie "
              "avant\n    d'en tirer quoi que ce soit.")

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
    resultat = {
        "tirage": nom, "cellules_comparees": len(paires),
        "accord_brut": brut, "kappa_de_cohen": kappa,
        "non_codees": sorted(manquantes), "desaccords": desaccords,
    }
    if kappa is None:
        resultat["kappa_non_calcule"] = (
            "un codeur n'emploie qu'une seule valeur : kappa degenere, non rapportable"
        )
    return resultat


def calculer_accord(tirage: str = "tous") -> int:
    chemin = DOSSIER_DOUBLE / "reference_scellee.json"
    if not chemin.exists():
        raise SystemExit(f"{chemin} introuvable. Tirez les echantillons d'abord.")
    reference = json.loads(chemin.read_text(encoding="utf-8"))

    resultats = []
    for nom, entree in reference["tirages"].items():
        if tirage != "tous" and nom != tirage:
            print(f"\n=== {nom} : hors du calcul demande (--tirage {tirage}) ===")
            continue
        if entree.get("statut") == "ecarte" and tirage == "tous":
            print(f"\n=== {nom} : ecarte, non calcule ===")
            print(f"    motif : {entree.get('motif')}")
            print(f"    pour le calculer malgre tout : --tirage {nom}")
            continue
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


def saisie_remplie(chemin: Path) -> bool:
    if not chemin.exists():
        return False
    with chemin.open(encoding="utf-8") as flux:
        return any((l.get("code_humain") or "").strip() for l in csv.DictReader(flux))


def verifier_correspondance_stable(nom: str, nouvelle: list[dict]) -> None:
    """Interdit de remapper des etiquettes sous une feuille deja codee.

    La reference porte la correspondance etiquette -> cellule. Si le tirage
    change apres qu'une feuille a ete remplie, les valeurs saisies designeraient
    d'autres cellules sans que rien ne le signale.
    """
    chemin = DOSSIER_DOUBLE / "reference_scellee.json"
    if not chemin.exists():
        return
    ancienne = json.loads(chemin.read_text(encoding="utf-8"))["tirages"].get(nom)
    if not ancienne:
        return
    if not saisie_remplie(DOSSIER_DOUBLE / ancienne["fichier_saisie"]):
        return
    avant = [(e["etiquette"], e["cellule"]) for e in ancienne["correspondance"]]
    apres = [(e["etiquette"], e["cellule"]) for e in nouvelle]
    if avant != apres:
        raise SystemExit(
            f"Le tirage '{nom}' a change, alors que {ancienne['fichier_saisie']} contient "
            "deja un codage a la main. Reecrire la reference ferait pointer les etiquettes "
            "saisies vers d'autres cellules, sans que rien ne le signale.\n"
            f"Deplacez {DOSSIER_DOUBLE} ailleurs si vous voulez refaire ce tirage, "
            "ou gardez la reference actuelle."
        )


def charger_reference() -> dict | None:
    chemin = DOSSIER_DOUBLE / "reference_scellee.json"
    return json.loads(chemin.read_text(encoding="utf-8")) if chemin.exists() else None


def ecrire_reference(reference: dict) -> None:
    reference["horodatage"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (DOSSIER_DOUBLE / "reference_scellee.json").write_text(
        json.dumps(reference, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def cellules_deja_tirees(reference: dict | None) -> set[str]:
    if not reference:
        return set()
    return {
        e["cellule"]
        for tirage in reference["tirages"].values()
        for e in tirage["correspondance"]
    }


def ajouter_tirage(reference: dict, nom: str, prefixe: str, par_valeur: int,
                   cellules: list[dict], enonces: dict) -> None:
    """Ajoute un tirage stratifie neuf, hors de tout ce qui a deja ete tire.

    Un tirage deja ecrit n'est jamais recalcule : la feuille qu'une personne a
    lue et le codage qu'elle a rendu ne doivent pas pouvoir bouger sous eux.
    Un nouveau tirage s'ajoute a cote, sur des cellules encore jamais vues.
    """
    if nom in reference["tirages"]:
        raise SystemExit(f"Le tirage '{nom}' existe deja dans la reference.")
    deja = cellules_deja_tirees(reference)
    disponibles = [c for c in cellules if cle(c) not in deja]
    print(f"{len(deja)} cellules deja tirees, {len(disponibles)} encore jamais vues.")
    for valeur in VALEURS:
        n = sum(1 for c in disponibles if c["valeur"] == valeur)
        print(f"  {valeur:22s} {n:4d} disponibles")

    echantillon = tirage_stratifie(disponibles, par_valeur, GRAINE_STRATIFIEE)
    correspondance = ecrire_feuille(nom, prefixe, echantillon, enonces)
    croise = {e["cellule"] for e in correspondance} & deja
    if croise:
        raise SystemExit(f"Le nouveau tirage reprend des cellules deja vues : {sorted(croise)}")
    reference["tirages"][nom] = {
        "graine": GRAINE_STRATIFIEE, "graine_melange": GRAINE_MELANGE,
        "taille": len(correspondance), "par_valeur": par_valeur,
        "methode": "tirage au hasard de N cellules par valeur, hors de tout tirage "
                   "anterieur, puis melange de l'ordre de presentation",
        "fichier_saisie": f"{nom}_saisie.csv", "correspondance": correspondance,
    }


def main() -> int:
    analyseur = argparse.ArgumentParser(description="Double codage en aveugle du codage automatique.")
    analyseur.add_argument("--accord", action="store_true",
                           help="Calculer l'accord, une fois les feuilles remplies.")
    analyseur.add_argument("--tirage", default="tous",
                           help="Restreindre le calcul d'accord a un tirage (defaut : tous).")
    analyseur.add_argument("--nouveau-tirage", metavar="NOM",
                           help="Ajouter un tirage stratifie neuf, sur des cellules jamais "
                                "tirees, melange. N'en recalcule aucun autre.")
    analyseur.add_argument("--prefixe", default="T",
                           help="Prefixe des etiquettes du nouveau tirage (defaut : T).")
    analyseur.add_argument("--tirage-cible", metavar="NOM",
                           help="Ajouter un lot ciblant les cellules positives d'enonces "
                                "donnes, plus des negatifs tires sur les memes enonces.")
    analyseur.add_argument("--enonces", nargs="+", metavar="ID",
                           help="Enonces vises par --tirage-cible.")
    analyseur.add_argument("--negatifs", type=int, default=40,
                           help="Nombre de negatifs du lot cible (defaut : 40).")
    analyseur.add_argument("--saisir", metavar="NOM",
                           help="Coder un lot a la main, une cellule a la fois, au clavier.")
    analyseur.add_argument("--ecarter", metavar="NOM",
                           help="Marquer un tirage comme ecarte, avec --motif.")
    analyseur.add_argument("--motif", default="", help="Motif de la mise a l'ecart.")
    analyseur.add_argument("--taille-uniforme", type=int, default=TAILLE_UNIFORME)
    analyseur.add_argument("--par-valeur", type=int, default=PAR_VALEUR)
    arguments = analyseur.parse_args()

    if arguments.accord:
        return calculer_accord(arguments.tirage)

    enonces = charger_enonces()
    codages = charger_codages()
    cellules = codables(codages)
    reference = charger_reference()

    if arguments.ecarter:
        if not reference or arguments.ecarter not in reference["tirages"]:
            raise SystemExit(f"Tirage '{arguments.ecarter}' introuvable dans la reference.")
        if not arguments.motif:
            raise SystemExit("--ecarter demande --motif : un tirage ecarte sans raison ecrite "
                             "est un chiffre perdu sans trace.")
        reference["tirages"][arguments.ecarter]["statut"] = "ecarte"
        reference["tirages"][arguments.ecarter]["motif"] = arguments.motif
        ecrire_reference(reference)
        print(f"Tirage '{arguments.ecarter}' marque ecarte : {arguments.motif}")
        return 0

    if arguments.saisir:
        return saisir(arguments.saisir)

    if arguments.tirage_cible:
        if reference is None:
            raise SystemExit("Aucune reference : tirez d'abord les echantillons initiaux.")
        if arguments.tirage_cible in reference["tirages"]:
            raise SystemExit(f"Le tirage '{arguments.tirage_cible}' existe deja.")
        if not arguments.enonces:
            raise SystemExit("--tirage-cible demande --enonces.")
        inconnus = [e for e in arguments.enonces if e not in enonces]
        if inconnus:
            raise SystemExit(f"Enonces inconnus : {inconnus}")
        DOSSIER_DOUBLE.mkdir(parents=True, exist_ok=True)
        deja = cellules_deja_tirees(reference)
        echantillon, detail = tirage_cible(cellules, arguments.enonces,
                                           arguments.negatifs, GRAINE_CIBLE, deja)
        correspondance = ecrire_feuille(arguments.tirage_cible, "C", echantillon, enonces)
        reference["tirages"][arguments.tirage_cible] = {
            "graine": GRAINE_CIBLE, "taille": len(correspondance),
            "methode": "toutes les cellules positives des enonces vises, plus des negatifs "
                       "tires au hasard sur ces memes enonces hors cellules deja soumises "
                       "a un codeur, puis melange sous contrainte de non-adjacence des positifs",
            "fichier_saisie": f"{arguments.tirage_cible}_saisie.csv",
            "correspondance": correspondance, **detail,
        }
        ecrire_reference(reference)
        print(f"\nTirage '{arguments.tirage_cible}' : {len(correspondance)} cellules "
              f"({detail['positifs']} positifs, {detail['negatifs']} negatifs), "
              f"graine {GRAINE_CIBLE}, melange trouve au {detail['melanges_essayes']}e essai")
        if detail["positifs_deja_soumis"]:
            print("  positifs deja vus par un codeur (lot ecarte) : "
                  + ", ".join(detail["positifs_deja_soumis"]))
        print(f"  a coder : python src/verifier_codage.py --saisir {arguments.tirage_cible}")
        return 0

    if arguments.nouveau_tirage:
        if reference is None:
            raise SystemExit("Aucune reference : tirez d'abord les echantillons initiaux.")
        DOSSIER_DOUBLE.mkdir(parents=True, exist_ok=True)
        ajouter_tirage(reference, arguments.nouveau_tirage, arguments.prefixe,
                       arguments.par_valeur, cellules, enonces)
        ecrire_reference(reference)
        entree = reference["tirages"][arguments.nouveau_tirage]
        print(f"\nTirage '{arguments.nouveau_tirage}' : {entree['taille']} cellules neuves, "
              f"graine {GRAINE_STRATIFIEE}, melange {GRAINE_MELANGE}")
        print(f"  a lire    : {DOSSIER_DOUBLE / (arguments.nouveau_tirage + '_feuille.md')}")
        print(f"  a remplir : {DOSSIER_DOUBLE / entree['fichier_saisie']}")
        return 0

    if reference is not None:
        print("Une reference existe deja. Les tirages ecrits ne sont pas recalcules.")
        for nom, entree in reference["tirages"].items():
            statut = entree.get("statut", "actif")
            print(f"  {nom:12s} {entree['taille']:3d} cellules  {statut}"
                  + (f" ({entree['motif']})" if entree.get("motif") else ""))
        print("\nPour ajouter un tirage : --nouveau-tirage NOM")
        return 0
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
    corr_u = [{"etiquette": f"U{i:02d}", "cellule": cle(c)} for i, c in enumerate(uniforme, 1)]
    verifier_correspondance_stable("uniforme", corr_u)
    corr_u = ecrire_feuille("uniforme", "U", uniforme, enonces)
    print(f"Tirage stratifie : {len(stratifie)} cellules, {arguments.par_valeur} par valeur, "
          f"graine {GRAINE_STRATIFIEE}, melange avec la graine {GRAINE_MELANGE}, "
          f"hors des {len(uniforme)} precedentes")
    corr_s = [{"etiquette": f"S{i:02d}", "cellule": cle(c)} for i, c in enumerate(stratifie, 1)]
    verifier_correspondance_stable("stratifie", corr_s)
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
