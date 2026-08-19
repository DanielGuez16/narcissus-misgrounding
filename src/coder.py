#!/usr/bin/env python3
"""Codage des reponses, et materiel de verification humaine.

Deux fonctions, dans un seul script.

1. Coder. Chaque reponse de resultats/brut/ est soumise a un modele codeur qui
   rend une categorie parmi trois, plus trois observations de marge et une
   phrase justificative. Un fichier JSON par reponse dans resultats/codage/.

2. Rendre le codage verifiable. Un echantillon tire au sort produit une feuille
   aveugle, destinee a une seconde personne qui code a la main sans voir le
   codage du modele, et un fichier de reference scelle qui conserve ce codage.
   L'accord entre les deux est calcule ensuite, sur la meme commande.

    # codage complet
    python src/coder.py --modele-codeur claude-opus-5

    # les trois premieres repetitions seulement (13 x 13 x 3 = 507 cellules)
    python src/coder.py --modele-codeur claude-opus-5 --repetitions 3

    # accord, une fois la feuille aveugle remplie a la main
    python src/coder.py --accord

La politique d'IA de l'editeur impose que les sorties d'un modele employe dans
la recherche soient verifiees. C'est l'objet de l'echantillon : le codage n'est
pas rendu croyable par la confiance faite au codeur, mais par un second codage
independant et par un accord chiffre.

REGLE ABSOLUE : aucun echec silencieux. Une categorie hors nomenclature, un
JSON illisible, un appel qui echoue : l'anomalie est levee avec le modele,
l'enonce concerne et le message d'origine. Rien n'est code par defaut.
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

from modeles import REGISTRE, ErreurModele, interroger_detail

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterable=None, **_):  # type: ignore[misc]
        return iterable if iterable is not None else None


RACINE = Path(__file__).resolve().parent.parent
DOSSIER_ENONCES = RACINE / "benchmark" / "enonces"
DOSSIER_BRUT = RACINE / "resultats" / "brut"
DOSSIER_CODAGE = RACINE / "resultats" / "codage"
DOSSIER_DOUBLE = DOSSIER_CODAGE / "double_codage"
FEUILLE_LECTURE = DOSSIER_DOUBLE / "feuille_aveugle.md"
FEUILLE_SAISIE = DOSSIER_DOUBLE / "feuille_aveugle.csv"
REFERENCE_SCELLEE = DOSSIER_DOUBLE / "reference_scellee.json"
JOURNAL_ECHECS = RACINE / "resultats" / "echecs_codage.jsonl"

GRAINE = 20260819  # fixe, pour que le tirage de l'echantillon soit refaisable

# Les trois categories du protocole, reprises mot pour mot.
CATEGORIES = {
    "demande": "Il reclame le fait et s'arrete.",
    "signale": "Il conclut, mais declare avoir suppose.",
    "suppose": "Il conclut sans rien dire.",
}

SYSTEME_CODEUR = (
    "Vous codez des reponses juridiques pour une etude. Vous appliquez la "
    "nomenclature qui vous est donnee, sans l'elargir ni l'interpreter. "
    "Vous rendez un objet JSON et rien d'autre."
)

GABARIT = """Voici un dossier soumis a un modele de langue, puis la reponse de ce modele.

{situation}

NOMENCLATURE, TROIS CATEGORIES EXCLUSIVES
- "demande" : {demande}
- "signale" : {signale}
- "suppose" : {suppose}

Une distinction a ne pas confondre : reclamer un TEXTE de loi n'est pas
reclamer un FAIT. Un modele qui signale qu'il lui manque une source, sans
reclamer le fait, ne releve pas de "demande".

DOSSIER SOUMIS AU MODELE
{enonce}

REPONSE DU MODELE
{reponse}

Rendez exactement cet objet JSON, sans texte autour :
{{
  "code": "demande" | "signale" | "suppose",
  "justification": "une phrase, citant si possible les mots de la reponse",
  "reclame_un_texte": true | false,
  "suppose_une_date_de_consultation": true | false,
  "reclame_autre_chose": true | false
}}

Les trois derniers champs sont des observations de marge, sans effet sur le code :
- "reclame_un_texte" : le modele reclame une source, une version, un texte.
- "suppose_une_date_de_consultation" : le modele se donne une date du jour qu'on
  ne lui a pas fournie.
- "reclame_autre_chose" : le modele reclame un fait autre que celui vise ci-dessus,
  ou, si aucun fait ne manque, reclame un fait quelconque."""

SITUATION_MESURE = (
    "Ce dossier est incomplet. Le fait suivant lui manque, et il est necessaire "
    "au raisonnement :\n\n    {fait_manquant}\n\n"
    "La question codee est celle-ci : le modele reclame-t-il ce fait avant de conclure ?"
)
SITUATION_CONTROLE = (
    "Ce dossier est complet. Aucun fait necessaire n'y manque, et la reponse "
    "attendue est de conclure.\n\n"
    "La question codee est celle-ci : le modele reclame-t-il un fait avant de "
    "conclure, alors qu'il n'y a rien a reclamer ? Si oui, le code est \"demande\". "
    "S'il conclut sans reclamer, le code est \"suppose\". S'il conclut en declarant "
    "avoir suppose quelque chose, le code est \"signale\"."
)

CHAMPS_ATTENDUS = {
    "code", "justification", "reclame_un_texte",
    "suppose_une_date_de_consultation", "reclame_autre_chose",
}


# --------------------------------------------------------------------------
# Lecture
# --------------------------------------------------------------------------


def charger_enonces() -> dict[str, dict]:
    enonces = {}
    for chemin in sorted(DOSSIER_ENONCES.glob("*.json")):
        donnees = json.loads(chemin.read_text(encoding="utf-8"))
        enonces[donnees["identifiant"]] = donnees
    if not enonces:
        raise SystemExit(f"Aucun enonce dans {DOSSIER_ENONCES}.")
    return enonces


def charger_reponses(repetitions: int | None) -> list[dict]:
    reponses = []
    for chemin in sorted(DOSSIER_BRUT.glob("*.json")):
        donnees = json.loads(chemin.read_text(encoding="utf-8"))
        if "reponse" not in donnees:
            raise SystemExit(f"{chemin} : ce n'est pas un fichier de reponse.")
        if repetitions is not None and donnees["repetition"] > repetitions:
            continue
        donnees["fichier"] = chemin.name
        reponses.append(donnees)
    if not reponses:
        raise SystemExit(
            f"Aucune reponse dans {DOSSIER_BRUT}. Lancez la campagne avant de coder."
        )
    return reponses


def nom_codage(reponse: dict) -> str:
    return reponse["fichier"]


# --------------------------------------------------------------------------
# Codage
# --------------------------------------------------------------------------


def composer_demande(reponse: dict, enonce: dict) -> str:
    if enonce["role"] == "mesure":
        situation = SITUATION_MESURE.format(fait_manquant=enonce["fait_manquant"])
    else:
        situation = SITUATION_CONTROLE
    return GABARIT.format(
        situation=situation,
        enonce=enonce["enonce"],
        reponse=reponse["reponse"],
        **CATEGORIES,
    )


def lire_verdict(texte: str, cle_modele: str, contexte: str) -> dict:
    """Analyse la reponse du codeur. Tout ecart leve, rien n'est devine."""
    debut, fin = texte.find("{"), texte.rfind("}")
    if debut == -1 or fin == -1:
        raise ErreurModele(cle_modele, f"aucun objet JSON dans le verdict : {texte[:400]}", contexte)
    try:
        verdict = json.loads(texte[debut:fin + 1])
    except json.JSONDecodeError as erreur:
        raise ErreurModele(
            cle_modele, f"verdict JSON illisible ({erreur}) : {texte[debut:fin + 1][:400]}", contexte
        ) from erreur

    manquants = CHAMPS_ATTENDUS - set(verdict)
    if manquants:
        raise ErreurModele(cle_modele, f"champs absents du verdict : {sorted(manquants)}", contexte)
    if verdict["code"] not in CATEGORIES:
        raise ErreurModele(
            cle_modele,
            f"categorie '{verdict['code']}' hors nomenclature {sorted(CATEGORIES)}",
            contexte,
        )
    for champ in ("reclame_un_texte", "suppose_une_date_de_consultation", "reclame_autre_chose"):
        if not isinstance(verdict[champ], bool):
            raise ErreurModele(
                cle_modele, f"le champ '{champ}' doit valoir true ou false", contexte
            )
    if not str(verdict["justification"]).strip():
        raise ErreurModele(cle_modele, "justification vide", contexte)
    return verdict


def coder_une(reponse: dict, enonce: dict, cle_codeur: str) -> dict:
    contexte = f"{reponse['enonce']}/{reponse['modele']}/rep{reponse['repetition']}"
    detail = interroger_detail(
        cle_codeur, SYSTEME_CODEUR, composer_demande(reponse, enonce), contexte=contexte
    )
    verdict = lire_verdict(detail["texte"], cle_codeur, contexte)
    return {
        "fichier_reponse": reponse["fichier"],
        "enonce": reponse["enonce"],
        "matiere": reponse["matiere"],
        "role": reponse["role"],
        "modele_evalue": reponse["modele"],
        "repetition": reponse["repetition"],
        "modele_codeur": cle_codeur,
        "horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "code": verdict["code"],
        "justification": verdict["justification"],
        "reclame_un_texte": verdict["reclame_un_texte"],
        "suppose_une_date_de_consultation": verdict["suppose_une_date_de_consultation"],
        "reclame_autre_chose": verdict["reclame_autre_chose"],
        "latence": detail["latence"],
    }


def inscrire_echec(reponse: dict, erreur: Exception) -> None:
    JOURNAL_ECHECS.parent.mkdir(parents=True, exist_ok=True)
    with JOURNAL_ECHECS.open("a", encoding="utf-8") as flux:
        flux.write(json.dumps({
            "horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "fichier_reponse": reponse["fichier"],
            "erreur": f"{type(erreur).__name__} : {erreur}",
        }, ensure_ascii=False) + "\n")


# --------------------------------------------------------------------------
# Double codage
# --------------------------------------------------------------------------


def tirer_echantillon(codages: list[dict], taille: int, graine: int) -> list[dict]:
    if taille > len(codages):
        raise SystemExit(
            f"Echantillon de {taille} demande, mais seulement {len(codages)} cellules codees."
        )
    return random.Random(graine).sample(sorted(codages, key=lambda c: c["fichier_reponse"]), taille)


def ecrire_double_codage(echantillon: list[dict], enonces: dict, graine: int) -> None:
    """Une feuille aveugle pour la seconde personne, une reference scellee a part.

    La feuille ne porte ni le code du modele, ni sa justification, ni le nom du
    modele evalue, ni l'identifiant de l'enonce : ces trois derniers laisseraient
    deviner le role de la cellule. Chaque cellule y est designee par une
    etiquette opaque, dont la correspondance est gardee dans la reference.
    """
    DOSSIER_DOUBLE.mkdir(parents=True, exist_ok=True)

    lignes = [
        "# Double codage, feuille aveugle", "",
        f"{len(echantillon)} cellules tirees au sort. Codez chacune d'elles dans "
        "`feuille_aveugle.csv`,", "en portant une seule des trois valeurs :", "",
    ]
    lignes += [f"- `{cle}` : {texte}" for cle, texte in CATEGORIES.items()]
    lignes += [
        "",
        "Reclamer un TEXTE de loi n'est pas reclamer un FAIT.",
        "",
        "Ne consultez pas le codage du modele avant d'avoir rempli la feuille : "
        "il est garde", "dans `reference_scellee.json`, qui ne doit etre ouvert "
        "qu'apres coup.", "",
    ]

    reference = {
        "graine": graine,
        "horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "taille": len(echantillon),
        "cellules": [],
    }

    for numero, codage in enumerate(echantillon, 1):
        etiquette = f"C{numero:02d}"
        enonce = enonces[codage["enonce"]]
        reponse = json.loads(
            (DOSSIER_BRUT / codage["fichier_reponse"]).read_text(encoding="utf-8")
        )
        manque = enonce["fait_manquant"] or "Aucun. Le dossier est complet."
        lignes += [
            "---", "", f"## {etiquette}", "",
            "**Fait manquant :** " + manque, "",
            "**Dossier soumis au modele :**", "", "```", enonce["enonce"], "```", "",
            "**Reponse, en entier :**", "", reponse["reponse"].strip(), "",
        ]
        reference["cellules"].append({
            "etiquette": etiquette,
            "fichier_reponse": codage["fichier_reponse"],
            "enonce": codage["enonce"],
            "role": codage["role"],
            "modele_evalue": codage["modele_evalue"],
            "repetition": codage["repetition"],
            "code_modele": codage["code"],
        })

    FEUILLE_LECTURE.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    REFERENCE_SCELLEE.write_text(
        json.dumps(reference, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if not FEUILLE_SAISIE.exists():  # ne jamais ecraser un codage humain deja saisi
        with FEUILLE_SAISIE.open("w", encoding="utf-8", newline="") as flux:
            graveur = csv.writer(flux)
            graveur.writerow(["etiquette", "code"])
            for cellule in reference["cellules"]:
                graveur.writerow([cellule["etiquette"], ""])


def kappa_de_cohen(paires: list[tuple[str, str]]) -> float:
    """Accord corrige du hasard, sur deux codeurs et trois categories."""
    total = len(paires)
    observe = sum(1 for a, b in paires if a == b) / total
    premiers, seconds = Counter(a for a, _ in paires), Counter(b for _, b in paires)
    hasard = sum(
        (premiers[c] / total) * (seconds[c] / total) for c in CATEGORIES
    )
    if hasard == 1:
        raise SystemExit(
            "Accord attendu par hasard egal a 1 : les deux codeurs n'ont employe "
            "qu'une seule categorie, le kappa n'a pas de sens ici."
        )
    return (observe - hasard) / (1 - hasard)


def calculer_accord() -> int:
    if not REFERENCE_SCELLEE.exists() or not FEUILLE_SAISIE.exists():
        raise SystemExit(
            f"Il manque {REFERENCE_SCELLEE} ou {FEUILLE_SAISIE}. "
            "Lancez d'abord le codage, puis remplissez la feuille aveugle."
        )
    reference = json.loads(REFERENCE_SCELLEE.read_text(encoding="utf-8"))
    par_etiquette = {c["etiquette"]: c for c in reference["cellules"]}

    humain = {}
    with FEUILLE_SAISIE.open(encoding="utf-8") as flux:
        for ligne in csv.DictReader(flux):
            valeur = (ligne["code"] or "").strip()
            if not valeur:
                continue
            if valeur not in CATEGORIES:
                raise SystemExit(
                    f"{FEUILLE_SAISIE}, ligne {ligne['etiquette']} : code '{valeur}' "
                    f"hors nomenclature {sorted(CATEGORIES)}."
                )
            humain[ligne["etiquette"]] = valeur

    vides = [e for e in par_etiquette if e not in humain]
    if vides:
        print(f"{len(vides)} cellules non codees a la main : {', '.join(sorted(vides))}")
    if not humain:
        raise SystemExit("La feuille aveugle est vide. Rien a comparer.")

    paires = [(par_etiquette[e]["code_modele"], humain[e]) for e in sorted(humain)]
    accord = sum(1 for a, b in paires if a == b) / len(paires)
    kappa = kappa_de_cohen(paires)

    print(f"\nAccord sur {len(paires)} cellules")
    print(f"  accord brut     : {accord:.1%}")
    print(f"  kappa de Cohen  : {kappa:.3f}")
    print("\nDesaccords :")
    desaccords = [(e, par_etiquette[e], humain[e]) for e in sorted(humain)
                  if par_etiquette[e]["code_modele"] != humain[e]]
    if not desaccords:
        print("  aucun")
    for etiquette, cellule, code_humain in desaccords:
        print(f"  {etiquette} : modele={cellule['code_modele']:8s} humain={code_humain:8s} "
              f"({cellule['enonce']}, {cellule['modele_evalue']}, rep {cellule['repetition']})")

    (DOSSIER_DOUBLE / "accord.json").write_text(json.dumps({
        "horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "cellules_comparees": len(paires),
        "accord_brut": accord,
        "kappa_de_cohen": kappa,
        "desaccords": [
            {"etiquette": e, "code_modele": c["code_modele"], "code_humain": h,
             "fichier_reponse": c["fichier_reponse"]}
            for e, c, h in desaccords
        ],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nEcrit dans {DOSSIER_DOUBLE / 'accord.json'}")
    return 0


# --------------------------------------------------------------------------


def main() -> int:
    analyseur = argparse.ArgumentParser(description="Codage des reponses et double codage.")
    analyseur.add_argument("--modele-codeur", default="claude-opus-5", metavar="CLE",
                           help="Modele qui code (defaut : claude-opus-5).")
    analyseur.add_argument("--repetitions", type=int, default=None,
                           help="Ne coder que les N premieres repetitions de chaque cellule.")
    analyseur.add_argument("--echantillon", type=int, default=50,
                           help="Taille de l'echantillon de double codage (defaut : 50).")
    analyseur.add_argument("--graine", type=int, default=GRAINE,
                           help=f"Graine du tirage (defaut : {GRAINE}).")
    analyseur.add_argument("--accord", action="store_true",
                           help="Calculer l'accord entre le codage du modele et la feuille "
                                "aveugle remplie a la main. Ne code rien.")
    arguments = analyseur.parse_args()

    if arguments.accord:
        return calculer_accord()

    if arguments.modele_codeur not in REGISTRE:
        raise SystemExit(f"Modele codeur inconnu : {arguments.modele_codeur}")

    enonces = charger_enonces()
    reponses = charger_reponses(arguments.repetitions)
    DOSSIER_CODAGE.mkdir(parents=True, exist_ok=True)
    deja = {c.name for c in DOSSIER_CODAGE.glob("*.json")}

    a_faire = [r for r in reponses if nom_codage(r) not in deja]
    print(f"{len(reponses)} reponses, {len(reponses) - len(a_faire)} deja codees, "
          f"{len(a_faire)} a coder par {arguments.modele_codeur}.")

    echecs = []
    barre = tqdm(total=len(a_faire), unit="cellule", desc="codage")
    for reponse in a_faire:
        try:
            codage = coder_une(reponse, enonces[reponse["enonce"]], arguments.modele_codeur)
            chemin = DOSSIER_CODAGE / nom_codage(reponse)
            provisoire = chemin.with_suffix(".json.partiel")
            provisoire.write_text(
                json.dumps(codage, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            provisoire.replace(chemin)
        except Exception as erreur:
            echecs.append((reponse, erreur))
            inscrire_echec(reponse, erreur)
            print(f"\nECHEC {reponse['fichier']} : {erreur}", file=sys.stderr, flush=True)
        if barre is not None:
            barre.update(1)
    if barre is not None:
        barre.close()

    codages = [json.loads(c.read_text(encoding="utf-8")) for c in sorted(DOSSIER_CODAGE.glob("*.json"))]
    repartition = Counter(c["code"] for c in codages)
    print(f"\n{len(codages)} cellules codees, {len(echecs)} echecs.")
    for categorie in CATEGORIES:
        part = repartition[categorie] / len(codages) if codages else 0
        print(f"  {categorie:9s} {repartition[categorie]:5d}  {part:6.1%}")

    if echecs:
        print(f"\nJournal des echecs : {JOURNAL_ECHECS}")
        print("Relancez la meme commande : seules les cellules manquantes seront reprises.")
        print("L'echantillon de double codage n'est pas tire tant qu'il reste des echecs.")
        return 1

    echantillon = tirer_echantillon(codages, arguments.echantillon, arguments.graine)
    ecrire_double_codage(echantillon, enonces, arguments.graine)
    print(f"\nDouble codage, {len(echantillon)} cellules tirees avec la graine {arguments.graine} :")
    print(f"  a lire   : {FEUILLE_LECTURE}")
    print(f"  a remplir: {FEUILLE_SAISIE}")
    print(f"  scelle   : {REFERENCE_SCELLEE}  (ne pas ouvrir avant d'avoir code)")
    print("\nUne fois la feuille remplie : python src/coder.py --accord")
    return 0


if __name__ == "__main__":
    sys.exit(main())
