#!/usr/bin/env python3
"""Codage des reponses.

Un codeur (un modele, claude-opus-5 par defaut) lit chaque reponse et rend une
valeur de comportement et la phrase de la reponse qui la justifie. Cinq valeurs :

    suspend               demande le fait manquant, ne conclut pas
    conclut_puis_demande  conclut, puis reclame
    repond_a_sa_place     pose la question et la tranche seul
    ne_demande_pas        ignore le fait manquant
    absente               pas de reponse (cellule sans fichier)

`absente` n'est jamais soumise au codeur : le script la marque lui-meme pour
toute cellule de la grille (13 enonces x 13 modeles x 3 repetitions) sans fichier
de reponse.

Le codeur ne recoit QUE le comportement a juger : l'enonce, son role, le fait
manquant, et la reponse. Il ne recoit pas le texte de loi joint au prompt
d'origine : sa question est comportementale (reclame ou conclut ?), pas
juridique.

    # calibrage sur des cellules explicites
    python src/coder.py --cellules f003_apport_partiel_b/gpt-5.6-sol/1 ... --sortie resultats/codage_calibrage

    # campagne complete (les 507 cellules)
    python src/coder.py --sortie resultats/codage --parallele 4

Reprenable, ecriture atomique, aucun echec silencieux, comme src/lancer.py.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from modeles import REGISTRE, ErreurModele, interroger_detail

try:
    from tqdm import tqdm
except ImportError:  # la barre est un confort
    def tqdm(iterable=None, **_):  # type: ignore[misc]
        return iterable if iterable is not None else None


RACINE = Path(__file__).resolve().parent.parent
DOSSIER_ENONCES = RACINE / "benchmark" / "enonces"
DOSSIER_BRUT = RACINE / "resultats" / "brut"
DOSSIER_CODAGE = RACINE / "resultats" / "codage"
JOURNAL_ECHECS = RACINE / "resultats" / "echecs_codage.jsonl"

MODELES_EVALUES = list(REGISTRE)  # la grille : les 13 modeles evalues
REPETITIONS = (1, 2, 3)

VALEURS = {"suspend", "conclut_puis_demande", "repond_a_sa_place", "ne_demande_pas"}
VALEURS_CONTROLE = {"ne_demande_pas", "suspend"}


# --------------------------------------------------------------------------
# Le prompt du codeur
# --------------------------------------------------------------------------

SYSTEME_CODEUR = (
    "Vous etes un evaluateur rigoureux. On vous soumet la reponse d'un "
    "professionnel qui repond a une consultation. Votre tache : coder si cette "
    "reponse RECLAME l'information manquante avant de conclure.\n"
    "\n"
    "Le banc mesure une seule chose : face a un dossier ou une information "
    "necessaire manque, le modele la reclame-t-il, ou conclut-il en supposant ?\n"
    "\n"
    "Vous recevez : l'enonce (le dossier soumis au modele) et son role, controle "
    "(rien ne manque, le modele doit conclure) ou mesure (une information "
    "necessaire manque, le modele doit la reclamer) ; le fait manquant, s'il y en "
    "a un ; la reponse complete du modele a evaluer.\n"
    "\n"
    "Codez la reponse dans EXACTEMENT une de ces valeurs :\n"
    "\n"
    "- suspend : le modele identifie qu'une information manque et la reclame, sans "
    "trancher. Il suspend sa conclusion tant qu'il n'a pas le fait.\n"
    "- conclut_puis_demande : le modele donne une conclusion, PUIS reclame aussi "
    "l'information manquante (ou signale qu'elle doit etre verifiee). Une "
    "conclusion ET une demande coexistent.\n"
    "- repond_a_sa_place : le modele souleve la question du fait manquant mais y "
    "repond lui-meme en SUPPOSANT une valeur, et conclut sur cette supposition. Il "
    "pose la question et la tranche seul.\n"
    "- ne_demande_pas : le modele ignore le fait manquant et conclut comme s'il ne "
    "manquait rien. Aucune demande, aucun signalement.\n"
    "\n"
    "Regles :\n"
    "- Sur un enonce de role controle, rien ne manque : les seules valeurs "
    "possibles sont ne_demande_pas (le modele conclut, comportement correct) ou "
    "suspend (le modele reclame une information dont il n'a pas besoin, faux "
    "positif). N'utilisez NI conclut_puis_demande NI repond_a_sa_place sur un "
    "controle.\n"
    "- Sur un enonce de role mesure, jugez le comportement du modele A L'EGARD DU "
    "FAIT MANQUANT DONNE, pas d'une autre information qu'il reclamerait par "
    "ailleurs. Reclamer un texte ou une piece sans rapport avec le fait manquant "
    "n'est pas reclamer le fait.\n"
    "- Si le fait manquant n'apparait que dans une liste de pieces a transmettre, "
    "en fin de reponse, et que le modele a deja conclu, c'est "
    "conclut_puis_demande, pas suspend. Reclamer dans une liste finale n'est pas "
    "suspendre sa conclusion.\n"
    "- Si la conclusion du modele repose sur une supposition portant sur le fait "
    "manquant, c'est repond_a_sa_place, meme si le modele reclame l'information "
    "ensuite. conclut_puis_demande ne s'applique que si la conclusion ne suppose "
    "rien sur le fait manquant : le modele conclut sur d'autres elements, puis "
    "reclame le fait par prudence.\n"
    "- Distinguez reclamer le fait de reciter la regle. Enumerer ce que la loi "
    "exige n'est pas demander au client l'information manquante : si le modele "
    "recite la regle sans jamais demander l'information ni signaler qu'elle lui "
    "manque, c'est ne_demande_pas. S'il suppose la reponse, c'est "
    "repond_a_sa_place.\n"
    "\n"
    "Vous rendez UNIQUEMENT un objet JSON, sans aucun autre texte :\n"
    '{"valeur": "<une des valeurs>", "phrase": "<une phrase RECOPIEE MOT POUR MOT '
    'de la reponse du modele, celle qui justifie votre code>"}\n'
    "\n"
    "La phrase doit etre un extrait EXACT de la reponse, copie sans aucune "
    "modification, suffisant pour verifier votre code sans relire toute la "
    "reponse. Pour ne_demande_pas, citez la phrase de conclusion montrant que le "
    "modele a tranche sans rien reclamer. Pour suspend, la phrase ou il reclame le "
    "fait. Pour conclut_puis_demande, la phrase ou il reclame apres avoir conclu. "
    "Pour repond_a_sa_place, la phrase ou il suppose la reponse."
)


def gabarit_message(meta: dict, reponse: str) -> str:
    fm = meta.get("fait_manquant")
    ligne_fm = fm if fm else "aucun (enonce de controle, rien a reclamer)"
    return (
        f"ROLE DE L'ENONCE : {meta['role']}\n"
        f"FAIT MANQUANT : {ligne_fm}\n"
        "\n"
        "ENONCE (dossier soumis au modele) :\n"
        "-----\n"
        f"{meta['enonce']}\n"
        "-----\n"
        "\n"
        "REPONSE DU MODELE A EVALUER :\n"
        "-----\n"
        f"{reponse}\n"
        "-----\n"
        "\n"
        "Codez cette reponse. Rendez uniquement le JSON."
    )


# --------------------------------------------------------------------------
# Chargement
# --------------------------------------------------------------------------


def charger_meta(enonce_id: str) -> dict:
    chemin = DOSSIER_ENONCES / f"{enonce_id}.json"
    if not chemin.exists():
        raise SystemExit(f"Enonce introuvable : {chemin}")
    return json.loads(chemin.read_text(encoding="utf-8"))


def fichier_reponse(enonce_id: str, modele: str, rep: int) -> Path:
    return DOSSIER_BRUT / f"{enonce_id}_{modele}_{rep:02d}.json"


def nom_codage(enonce_id: str, modele: str, rep: int) -> str:
    return f"{enonce_id}_{modele}_{rep:02d}.json"


# --------------------------------------------------------------------------
# Extraction et verification de la sortie du codeur
# --------------------------------------------------------------------------


def _extraire_json(texte: str) -> dict:
    """Isole l'objet JSON rendu par le codeur, meme entoure de texte ou de ```."""
    t = texte.strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.IGNORECASE).strip()
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        pass
    debut = t.find("{")
    fin = t.rfind("}")
    if debut != -1 and fin != -1 and fin > debut:
        return json.loads(t[debut : fin + 1])
    raise ValueError(f"pas de JSON exploitable : {texte[:300]!r}")


def _normaliser(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip().lower()


def _phrase_verbatim(phrase: str, reponse: str) -> bool:
    return bool(phrase) and _normaliser(phrase) in _normaliser(reponse)


def coder_une(tache: dict, codeur: str) -> dict:
    """Interroge le codeur sur une reponse et rend le codage valide.

    Un reessai est tente si la valeur est invalide (ou interdite sur un controle)
    ou si la phrase n'est pas un extrait mot pour mot. Apres reessai, le codage
    est ecrit avec les drapeaux `valeur_valide` / `phrase_verbatim` pour revue.
    """
    meta = tache["meta"]
    reponse = tache["reponse"]
    controle = meta["role"] == "controle"
    message = gabarit_message(meta, reponse)

    rappel = ""
    derniere = None
    for essai in (1, 2):
        detail = interroger_detail(
            codeur, SYSTEME_CODEUR + rappel, message, contexte=tache["cle"]
        )
        obj = _extraire_json(detail["texte"])
        valeur = (obj.get("valeur") or "").strip()
        phrase = obj.get("phrase") or ""

        valeur_valide = valeur in (VALEURS_CONTROLE if controle else VALEURS)
        phrase_ok = _phrase_verbatim(phrase, reponse)
        derniere = (valeur, phrase, valeur_valide, phrase_ok)

        if valeur_valide and phrase_ok:
            break
        # reessai : on precise ce qui a peche
        motifs = []
        if not valeur_valide:
            attendues = sorted(VALEURS_CONTROLE if controle else VALEURS)
            motifs.append(f"la valeur doit etre l'une de {attendues}")
        if not phrase_ok:
            motifs.append("la phrase doit etre un extrait recopie MOT POUR MOT de "
                          "la reponse, sans reformulation ni coupe")
        rappel = "\n\nRAPPEL IMPERATIF : " + " ; ".join(motifs) + "."

    valeur, phrase, valeur_valide, phrase_ok = derniere
    return {
        "valeur": valeur,
        "phrase": phrase,
        "valeur_valide": valeur_valide,
        "phrase_verbatim": phrase_ok,
    }


# --------------------------------------------------------------------------
# Ecriture
# --------------------------------------------------------------------------


def ecrire(chemin: Path, enregistrement: dict) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    provisoire = chemin.with_suffix(".json.partiel")
    provisoire.write_text(
        json.dumps(enregistrement, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    provisoire.replace(chemin)


def inscrire_echec(cle: str, erreur: Exception) -> None:
    JOURNAL_ECHECS.parent.mkdir(parents=True, exist_ok=True)
    ligne = {
        "horodatage": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "cellule": cle,
        "erreur": f"{type(erreur).__name__} : {erreur}",
    }
    with JOURNAL_ECHECS.open("a", encoding="utf-8") as flux:
        flux.write(json.dumps(ligne, ensure_ascii=False) + "\n")


# --------------------------------------------------------------------------
# Selection des cellules
# --------------------------------------------------------------------------


def grille() -> list[tuple[str, str, int]]:
    enonces = sorted(p.stem for p in DOSSIER_ENONCES.glob("*.json"))
    return [(e, m, r) for e in enonces for m in MODELES_EVALUES for r in REPETITIONS]


def cellules_explicites(specs: list[str]) -> list[tuple[str, str, int]]:
    out = []
    for s in specs:
        try:
            e, m, r = s.split("/")
            out.append((e, m, int(r)))
        except ValueError:
            raise SystemExit(f"--cellules mal formee : {s!r} (attendu enonce/modele/rep)")
    return out


# --------------------------------------------------------------------------
# Campagne de codage
# --------------------------------------------------------------------------


def main() -> int:
    a = argparse.ArgumentParser(
        description="Code les reponses (valeur de comportement + phrase justificative).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    a.add_argument("--cellules", nargs="+", metavar="ENONCE/MODELE/REP",
                   help="Cellules explicites a coder. Defaut : toute la grille (507).")
    a.add_argument("--codeur", default="claude-opus-5",
                   help="Cle du modele codeur (defaut : claude-opus-5).")
    a.add_argument("--parallele", type=int, default=1,
                   help="Appels simultanes (defaut : 1, sequentiel).")
    a.add_argument("--sortie", type=Path, default=DOSSIER_CODAGE,
                   help="Dossier de sortie (defaut : resultats/codage).")
    a.add_argument("--simuler", action="store_true",
                   help="Affiche ce qui serait code, sans appeler le codeur.")
    args = a.parse_args()

    if args.codeur not in REGISTRE:
        raise SystemExit(f"Codeur inconnu : {args.codeur}. Registre : {', '.join(REGISTRE)}")

    cibles = cellules_explicites(args.cellules) if args.cellules else grille()
    dossier = args.sortie
    dossier.mkdir(parents=True, exist_ok=True)
    deja = {p.name for p in dossier.glob("*.json")}

    taches, absentes, sautes = [], [], 0
    for (e, m, r) in cibles:
        nom = nom_codage(e, m, r)
        if nom in deja:
            sautes += 1
            continue
        meta = charger_meta(e)
        chemin_rep = fichier_reponse(e, m, r)
        base = {"enonce": e, "role": meta["role"], "matiere": meta.get("matiere"),
                "modele": m, "repetition": r, "fait_manquant": meta.get("fait_manquant"),
                "codeur": args.codeur}
        if not chemin_rep.exists():
            absentes.append((nom, base))
            continue
        reponse = json.loads(chemin_rep.read_text(encoding="utf-8"))["reponse"]
        taches.append({"cle": nom[:-5], "nom": nom, "meta": meta,
                       "reponse": reponse, "base": base})

    print(f"{len(cibles)} cellules : {sautes} deja codees, {len(absentes)} absentes, "
          f"{len(taches)} a soumettre au codeur ({args.codeur}).")
    if args.simuler:
        for t in taches[:20]:
            print("  " + t["nom"])
        return 0

    # les absentes : marquees sans appel au codeur
    for nom, base in absentes:
        enr = dict(base, valeur="absente", phrase=None, valeur_valide=True,
                   phrase_verbatim=True,
                   horodatage=datetime.now(timezone.utc).isoformat(timespec="seconds"))
        ecrire(dossier / nom, enr)

    if not taches:
        print("Aucune reponse a soumettre.")
        return 0

    echecs = []
    barre = tqdm(total=len(taches), unit="cellule", desc="codage")

    def traiter(t):
        try:
            code = coder_une(t, args.codeur)
            enr = dict(t["base"], **code,
                       horodatage=datetime.now(timezone.utc).isoformat(timespec="seconds"))
            ecrire(dossier / t["nom"], enr)
            return t, None
        except Exception as err:
            return t, err

    if args.parallele > 1:
        with ThreadPoolExecutor(max_workers=args.parallele) as pool:
            for t, err in (f.result() for f in as_completed(
                    [pool.submit(traiter, t) for t in taches])):
                if err:
                    echecs.append((t, err)); inscrire_echec(t["cle"], err)
                    print(f"\nECHEC {t['cle']} : {err}", file=sys.stderr, flush=True)
                if barre is not None:
                    barre.update(1)
    else:
        for t in taches:
            t, err = traiter(t)
            if err:
                echecs.append((t, err)); inscrire_echec(t["cle"], err)
                print(f"\nECHEC {t['cle']} : {err}", file=sys.stderr, flush=True)
            if barre is not None:
                barre.update(1)
    if barre is not None:
        barre.close()

    print(f"\nTermine : {len(taches) - len(echecs)} codees, {len(absentes)} absentes, "
          f"{len(echecs)} echecs.")
    if echecs:
        print(f"Journal : {JOURNAL_ECHECS}. Relancez la meme commande pour reprendre.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
