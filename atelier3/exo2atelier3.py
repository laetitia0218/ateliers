# -----------------------------
# EXERCICE 2 - MOTS CROISÉS
# -----------------------------

# 1. Mots avec exactement n lettres
def mots_Nlettres(lst_mot, n):
    return [mot for mot in lst_mot if len(mot) == n]

# 2. Vérifier si un mot commence par un préfixe
def commence_par(mot, prefixe):
    return mot.startswith(prefixe)

# 3. Vérifier si un mot finit par un suffixe
def finit_par(mot, suffixe):
    return mot.endswith(suffixe)

# 4. Liste des mots qui finissent par un suffixe
def finissent_par(lst_mot, suffixe):
    return [mot for mot in lst_mot if mot.endswith(suffixe)]

# 5. Liste des mots qui commencent par un préfixe
def commencent_par(lst_mot, prefixe):
    return [mot for mot in lst_mot if mot.startswith(prefixe)]

# 6. Liste des mots selon préfixe, suffixe et longueur (sans for ni if explicite)
def liste_mots(lst_mot, prefixe, suffixe, n):
    return list(filter(lambda mot: mot.startswith(prefixe) and mot.endswith(suffixe) and len(mot) == n, lst_mot))

# 7. Lire un fichier pour créer la liste de mots
def dictionnaire(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        return [ligne.strip() for ligne in f.readlines()]

# -----------------------------
# Programme de test
# -----------------------------
def test_exercice2():
    lst_mot = ["jouer","bonjour","punir","jour","aurevoir","revoir","pouvoir","cour","abajour","finir","aimer"]

    # Test mots_Nlettres
    if mots_Nlettres(lst_mot, 5) != ["jouer","punir","finir","aimer"]:
        return "Erreur mots_Nlettres"

    # Test commence_par
    if not commence_par("bonjour", "bon"):
        return "Erreur commence_par"

    # Test finit_par
    if not finit_par("bonjour", "jour"):
        return "Erreur finit_par"

    # Test finissent_par
    if finissent_par(lst_mot, "our") != ["jour","cour"]:
        return "Erreur finissent_par"

    # Test commencent_par
    if commencent_par(lst_mot, "re") != ["revoir"]:
        return "Erreur commencent_par"

    # Test liste_mots
    if liste_mots(lst_mot, "a", "r", 5) != ["aimer"]:
        return "Erreur liste_mots"

    # Test dictionnaire (décommente si fichier littre.txt disponible)
    # try:
    #     mots = dictionnaire("littre.txt")
    #     if not mots:
    #         return "Erreur dictionnaire - fichier vide"
    # except:
    #     return "Erreur dictionnaire - fichier introuvable"

    return "Tous les tests passent"

# -----------------------------
# Exécution du test
# -----------------------------
print(test_exercice2())
