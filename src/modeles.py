"""Couche d'acces aux modeles de langue.

Point d'entree unique :

    interroger(modele, systeme, message) -> texte

`modele` est une cle courte du registre ci-dessous (par exemple "claude-opus-5"
ou "gpt-5.6-sol"), pas un identifiant fournisseur. Le registre fait la
traduction, ce qui permet de changer d'identifiant ou de fournisseur sans
toucher au reste du code.

Deux dorsales seulement, pour eviter treize integrations :
  - "anthropic"   : API directe Anthropic ;
  - "openrouter"  : tout le reste.

REGLE ABSOLUE : aucun echec silencieux. Toute anomalie (cle absente, erreur
HTTP, reponse vide, reponse tronquee, temperature refusee) leve une
ErreurModele portant le nom du modele, l'enonce concerne quand il est connu,
et le message d'origine. Il n'y a nulle part de `except: pass`, ni de valeur
de repli qui masquerait un probleme.
"""

from __future__ import annotations

import json
import os
import random
import sys
import time
from dataclasses import dataclass, field

import requests

try:  # chargement facultatif du fichier .env
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # python-dotenv non installe : les variables doivent venir de l'environnement
    pass


# --------------------------------------------------------------------------
# Reglages generaux
# --------------------------------------------------------------------------

URL_OPENROUTER = "https://openrouter.ai/api/v1/chat/completions"

# 600 s : une consultation complete demande plusieurs minutes de generation.
# Mesure du 18 aout 2026 : jusqu'a 6 min sur claude-opus-5.
DELAI_SECONDES = int(os.environ.get("NARCISSUS_DELAI", "600"))
# 16 000 et non 4 000 : les modeles a raisonnement depensent une part du budget
# en reflexion avant d'ecrire. Mesure du 18 aout 2026 sur claude-opus-5 et
# l'enonce f001_chaudiere_a : 3 719 jetons de reflexion et 5 800 de reponse
# visible, soit 7 526 au total. A 4 000, la reponse revenait tronquee, ou vide
# quand la reflexion avait tout consomme. 16 000 ne suffisait toujours pas a
# f003_apport_partiel_b. C'est un plafond, non une cible : un modele qui repond
# court ne coute pas plus cher parce qu'il est haut.
JETONS_MAX = int(os.environ.get("NARCISSUS_JETONS_MAX", "32000"))
TENTATIVES_MAX = int(os.environ.get("NARCISSUS_TENTATIVES", "6"))
# Plafond de l'attente entre deux reprises quand le fournisseur n'impose pas de
# Retry-After (backoff exponentiel : 2, 4, 8, 16, 32... borne a ce plafond).
PLAFOND_ATTENTE = int(os.environ.get("NARCISSUS_PLAFOND_ATTENTE", "60"))

# OpenRouter peut router une requete vers plusieurs fournisseurs pour un meme
# modele. `require_parameters` restreint le routage aux fournisseurs qui
# honorent tous les parametres envoyes, dont la temperature. Indispensable
# pour que "temperature 0" veuille dire quelque chose.
EXIGER_PARAMETRES = os.environ.get("NARCISSUS_EXIGER_PARAMETRES", "1") == "1"


class ErreurModele(RuntimeError):
    """Echec d'un appel a un modele. Jamais rattrapee silencieusement."""

    def __init__(self, modele: str, message: str, enonce: str | None = None):
        self.modele = modele
        self.enonce = enonce
        self.message = message
        situation = f"modele={modele}"
        if enonce:
            situation += f" enonce={enonce}"
        super().__init__(f"[{situation}] {message}")


# --------------------------------------------------------------------------
# Registre des treize modeles
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Modele:
    cle: str
    famille: str          # "ferme" ou "ouvert"
    dorsale: str          # "anthropic" ou "openrouter"
    identifiant: str      # identifiant chez le fournisseur
    temperature_zero: bool = True   # False = le modele refuse de fixer la temperature
    note: str = ""
    entetes: dict = field(default_factory=dict)

    def identifiant_effectif(self) -> str:
        """Identifiant fournisseur, surchargeable par variable d'environnement.

        NARCISSUS_ID_<CLE>, tirets et points remplaces par des soulignes.
        Exemple : NARCISSUS_ID_GPT_5_6_SOL=openai/gpt-5.6-sol
        """
        variable = "NARCISSUS_ID_" + self.cle.upper().replace("-", "_").replace(".", "_")
        return os.environ.get(variable, self.identifiant)


# Identifiants verifies un a un contre le catalogue OpenRouter le 18 aout 2026,
# ainsi que le champ supported_parameters qui declare si la temperature est
# reglable. Le registre est la reference : NARCISSUS_ID_<CLE> ne sert qu'a
# surcharger ponctuellement, jamais a reparer une entree fausse. Un identifiant
# qui cesse d'exister se traduit par une erreur HTTP 404 explicite, jamais par
# un silence.
REGISTRE: dict[str, Modele] = {
    # ---------------------------- modeles fermes ---------------------------
    "claude-opus-5": Modele(
        cle="claude-opus-5",
        famille="ferme",
        dorsale="anthropic",
        identifiant="claude-opus-5",
        temperature_zero=False,
        note="L'API repond \"`temperature` is deprecated for this model\" (constate le "
             "18 aout 2026). Appel sans parametre de temperature.",
    ),
    "gpt-5.6-sol": Modele(
        cle="gpt-5.6-sol",
        famille="ferme",
        dorsale="openrouter",
        identifiant="openai/gpt-5.6-sol",
        temperature_zero=False,
        note="Le catalogue ne liste pas temperature parmi les parametres acceptes. "
             "Appel sans parametre de temperature.",
    ),
    "gpt-5.6-terra": Modele(
        cle="gpt-5.6-terra",
        famille="ferme",
        dorsale="openrouter",
        identifiant="openai/gpt-5.6-terra",
        temperature_zero=False,
        note="Idem gpt-5.6-sol : temperature non reglable, d'apres le catalogue.",
    ),
    "gemini-3.1-pro": Modele(
        cle="gemini-3.1-pro",
        famille="ferme",
        dorsale="openrouter",
        identifiant="google/gemini-3.1-pro-preview",
        note="Le catalogue ne connait Gemini 3.1 Pro que par son canal preview.",
    ),
    "grok-4.6": Modele(
        cle="grok-4.6",
        famille="ferme",
        dorsale="openrouter",
        identifiant="x-ai/grok-4.6",
    ),
    # ---------------------------- modeles ouverts --------------------------
    "mistral-large-3": Modele(
        cle="mistral-large-3",
        famille="ouvert",
        dorsale="openrouter",
        identifiant="mistralai/mistral-large-2512",
        note="Mistral Large 3 porte l'instantane 2512 au catalogue.",
    ),
    "mistral-medium-3.5": Modele(
        cle="mistral-medium-3.5",
        famille="ouvert",
        dorsale="openrouter",
        identifiant="mistralai/mistral-medium-3-5",
        note="Le catalogue ecrit la version avec un tiret, non un point.",
    ),
    "kimi-k3": Modele(
        cle="kimi-k3",
        famille="ouvert",
        dorsale="openrouter",
        identifiant="moonshotai/kimi-k3",
    ),
    "glm-5.2": Modele(
        cle="glm-5.2",
        famille="ouvert",
        dorsale="openrouter",
        identifiant="z-ai/glm-5.2",
        note="GLM-5.3 n'existe pas : le catalogue s'arrete a GLM 5.2, deja retenue "
             "dans le premier papier.",
    ),
    "deepseek-v4-pro": Modele(
        cle="deepseek-v4-pro",
        famille="ouvert",
        dorsale="openrouter",
        identifiant="deepseek/deepseek-v4-pro",
        note="DeepSeek V4 n'existe pas sous ce seul nom : Pro et Flash sont deux "
             "modeles distincts. Pro est le seul comparable au reste du panel. "
             "L'alias pointait sur l'instantane 0423 le 18 aout 2026.",
    ),
    "qwen-3.6-plus": Modele(
        cle="qwen-3.6-plus",
        famille="ouvert",
        dorsale="openrouter",
        identifiant="qwen/qwen3.6-plus",
        note="Grand modele stable de la generation 3.6. Max Preview a ete ecarte : "
             "pas de canal preview sur une campagne de 507 appels.",
    ),
    "minimax-m3": Modele(
        cle="minimax-m3",
        famille="ouvert",
        dorsale="openrouter",
        identifiant="minimax/minimax-m3",
    ),
    "llama-4-maverick": Modele(
        cle="llama-4-maverick",
        famille="ouvert",
        dorsale="openrouter",
        identifiant="meta-llama/llama-4-maverick",
    ),
}

MODELES = list(REGISTRE)


def fiche_modele(cle: str, contexte: str | None = None) -> Modele:
    """Fiche du registre pour une cle, ou ErreurModele si la cle est inconnue."""
    if cle not in REGISTRE:
        connus = ", ".join(MODELES)
        raise ErreurModele(cle, f"modele inconnu. Modeles du registre : {connus}", contexte)
    return REGISTRE[cle]


def cle_api(variable: str, nom_modele: str, contexte: str | None = None) -> str:
    valeur = os.environ.get(variable, "").strip()
    if not valeur:
        raise ErreurModele(
            nom_modele,
            f"variable d'environnement {variable} absente ou vide. "
            "Renseignez-la dans .env (voir .env.exemple). Aucune cle n'est ecrite dans le code.",
            contexte,
        )
    return valeur


# --------------------------------------------------------------------------
# Point d'entree
# --------------------------------------------------------------------------


def interroger(modele: str, systeme: str, message: str, contexte: str | None = None) -> str:
    """Envoie une consigne systeme et un message a un modele, rend le texte.

    `contexte` est l'identifiant de l'enonce en cours. Il n'influe pas sur
    l'appel : il sert uniquement a ce que l'exception dise de quel enonce il
    s'agit.
    """
    return interroger_detail(modele, systeme, message, contexte)["texte"]


def interroger_detail(
    modele: str, systeme: str, message: str, contexte: str | None = None
) -> dict:
    """Comme interroger, mais rend aussi la latence et les compteurs de jetons."""
    fiche = fiche_modele(modele, contexte)
    depart = time.monotonic()
    if fiche.dorsale == "anthropic":
        brut = _appel_anthropic(fiche, systeme, message, contexte)
    elif fiche.dorsale == "openrouter":
        brut = _appel_openrouter(fiche, systeme, message, contexte)
    else:
        raise ErreurModele(modele, f"dorsale inconnue : {fiche.dorsale}", contexte)
    latence = round(time.monotonic() - depart, 3)

    texte = brut["texte"]
    if not texte or not texte.strip():
        raise ErreurModele(
            modele,
            f"reponse vide (motif d'arret : {brut.get('motif_arret')}). "
            "Reponse non exploitable, l'appel est considere en echec.",
            contexte,
        )
    if brut.get("motif_arret") in {"length", "max_tokens"}:
        raise ErreurModele(
            modele,
            f"reponse tronquee a {JETONS_MAX} jetons (motif d'arret : {brut['motif_arret']}). "
            "Relancez avec NARCISSUS_JETONS_MAX plus eleve ; une reponse coupee "
            "fausserait le codage.",
            contexte,
        )

    brut["texte"] = texte
    brut["latence"] = latence
    brut["modele"] = fiche.cle
    brut["identifiant_fournisseur"] = fiche.identifiant_effectif()
    brut["temperature_zero"] = fiche.temperature_zero
    return brut


# --------------------------------------------------------------------------
# Dorsales
# --------------------------------------------------------------------------


def _appel_anthropic(fiche: Modele, systeme: str, message: str, contexte: str | None) -> dict:
    try:
        import anthropic
    except ImportError as erreur:
        raise ErreurModele(fiche.cle, f"paquet anthropic absent : {erreur}", contexte) from erreur

    client = anthropic.Anthropic(api_key=cle_api("ANTHROPIC_API_KEY", fiche.cle, contexte))
    conseil_temperature = (
        "\n  -> Ce modele refuse le parametre temperature. Passez temperature_zero=False "
        f"sur '{fiche.cle}' dans REGISTRE, et signalez-le dans le papier : la temperature "
        "n'est pas reglable pour ce modele."
    )
    parametres = {
        "model": fiche.identifiant_effectif(),
        "max_tokens": JETONS_MAX,
        "system": systeme,
        "messages": [{"role": "user", "content": message}],
    }
    if fiche.temperature_zero:
        parametres["temperature"] = 0

    def tenter():
        # Flux continu, non par gout du direct : au-dela d'un certain budget de
        # jetons, le SDK refuse l'appel classique, une generation pouvant
        # depasser dix minutes. Le message final est identique.
        try:
            with client.messages.stream(**parametres) as flux:
                return flux.get_final_message()
        except anthropic.BadRequestError as erreur:
            message = f"{type(erreur).__name__} : {erreur}"
            if "temperature" in message.lower():
                raise ErreurModele(fiche.cle, message + conseil_temperature, contexte) from erreur
            raise

    reponse = _avec_reprises(tenter, fiche, contexte)

    texte = "".join(bloc.text for bloc in reponse.content if getattr(bloc, "type", "") == "text")
    return {
        "texte": texte,
        "motif_arret": reponse.stop_reason,
        "jetons_entree": reponse.usage.input_tokens,
        "jetons_sortie": reponse.usage.output_tokens,
    }


def _appel_openrouter(fiche: Modele, systeme: str, message: str, contexte: str | None) -> dict:
    entetes = {
        "Authorization": f"Bearer {cle_api('OPENROUTER_API_KEY', fiche.cle, contexte)}",
        "Content-Type": "application/json",
    }
    entetes.update(fiche.entetes)

    corps = {
        "model": fiche.identifiant_effectif(),
        "max_tokens": JETONS_MAX,
        "messages": [
            {"role": "system", "content": systeme},
            {"role": "user", "content": message},
        ],
    }
    if fiche.temperature_zero:
        corps["temperature"] = 0
        if EXIGER_PARAMETRES:
            corps["provider"] = {"require_parameters": True}

    def tenter():
        reponse = requests.post(
            URL_OPENROUTER, headers=entetes, json=corps, timeout=DELAI_SECONDES
        )
        if reponse.status_code != 200:
            _lever_http(fiche, reponse, contexte)
        return reponse.json()

    charge = _avec_reprises(tenter, fiche, contexte)

    # OpenRouter peut rendre un 200 portant une erreur dans le corps.
    if "error" in charge and charge.get("error"):
        raise ErreurModele(fiche.cle, f"erreur OpenRouter dans le corps : {charge['error']}", contexte)
    choix = charge.get("choices")
    if not choix:
        raise ErreurModele(
            fiche.cle, f"reponse sans champ choices : {json.dumps(charge)[:800]}", contexte
        )

    premier = choix[0]
    contenu = premier.get("message", {}).get("content") or ""
    if isinstance(contenu, list):  # certains fournisseurs rendent une liste de blocs
        contenu = "".join(
            bloc.get("text", "") for bloc in contenu if isinstance(bloc, dict)
        )
    usage = charge.get("usage") or {}
    return {
        "texte": contenu,
        "motif_arret": premier.get("finish_reason") or premier.get("native_finish_reason"),
        "jetons_entree": usage.get("prompt_tokens"),
        "jetons_sortie": usage.get("completion_tokens"),
        "fournisseur_effectif": charge.get("provider"),
    }


# --------------------------------------------------------------------------
# Erreurs et reprises
# --------------------------------------------------------------------------

CODES_TRANSITOIRES = {408, 409, 429, 500, 502, 503, 504, 520, 522, 524}


class _ErreurTransitoire(Exception):
    """Erreur passagere : on reessaie. Si les reprises s'epuisent, elle devient ErreurModele."""

    def __init__(self, message: str, retry_after: float | None = None):
        super().__init__(message)
        # Secondes demandees par le fournisseur via l'en-tete Retry-After, si present.
        self.retry_after = retry_after


def _lever_http(fiche: Modele, reponse, contexte: str | None) -> None:
    detail = reponse.text[:1000]
    message = f"HTTP {reponse.status_code} sur {fiche.identifiant_effectif()} : {detail}"

    if reponse.status_code == 400 and "temperature" in detail.lower():
        raise ErreurModele(
            fiche.cle,
            message
            + "\n  -> Ce modele refuse le parametre temperature. Passez "
              f"temperature_zero=False sur '{fiche.cle}' dans REGISTRE, et signalez-le "
              "dans le papier : la temperature n'est pas reglable pour ce modele.",
            contexte,
        )
    if reponse.status_code in CODES_TRANSITOIRES:
        # Depassement de debit (429) ou indisponibilite (503) : respecter le
        # Retry-After renvoye par le fournisseur quand il est chiffre en secondes.
        brut = reponse.headers.get("Retry-After") or reponse.headers.get("retry-after")
        retry_after = None
        if brut:
            try:
                retry_after = float(brut)
            except ValueError:
                retry_after = None  # forme date-HTTP : on retombe sur le backoff
        raise _ErreurTransitoire(message, retry_after=retry_after)
    raise ErreurModele(fiche.cle, message, contexte)


def _avec_reprises(action, fiche: Modele, contexte: str | None):
    derniere = ""
    for tentative in range(1, TENTATIVES_MAX + 1):
        retry_after = None
        try:
            return action()
        except _ErreurTransitoire as erreur:
            derniere = str(erreur)
            retry_after = erreur.retry_after
        except requests.exceptions.RequestException as erreur:
            derniere = f"reseau : {type(erreur).__name__} : {erreur}"
        except ErreurModele:
            raise  # deja explicite, inutile de reessayer
        except Exception as erreur:  # SDK Anthropic et imprevus : on qualifie puis on decide
            texte = f"{type(erreur).__name__} : {erreur}"
            transitoire = any(
                marque in texte.lower()
                for marque in ("rate limit", "overloaded", "timeout", "connection", "529", "503")
            )
            if not transitoire:
                raise ErreurModele(fiche.cle, texte, contexte) from erreur
            derniere = texte

        if tentative < TENTATIVES_MAX:
            # Retry-After s'il est connu, sinon backoff exponentiel plafonne. Le
            # jitter empeche N appels simultanes de repartir tous en meme temps
            # (effet de troupeau qui reprovoquerait aussitot le depassement).
            if retry_after is not None:
                attente = retry_after + random.uniform(0, 1)
            else:
                attente = min(2 ** tentative, PLAFOND_ATTENTE) + random.uniform(0, tentative)
            print(
                f"  reprise {tentative}/{TENTATIVES_MAX - 1} pour {fiche.cle} "
                f"dans {attente:.1f}s ({derniere[:200]})",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(attente)

    raise ErreurModele(
        fiche.cle,
        f"echec apres {TENTATIVES_MAX} tentatives. Derniere erreur : {derniere}",
        contexte,
    )
