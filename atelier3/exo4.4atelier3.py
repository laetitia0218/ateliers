#trouver les mots les plus long  qu'on peux ecrire avec les lettres dispo 
from exo2atelier3 import mots_Nlettres
from exo423atelier3 import mot_possible
def mot_optimaux(dico, lettres):
    max_len = len(lettres)  # longueur max possible d'un mot
    while max_len > 0:
        # On récupère tous les mots de longueur max_len
        mots_longueur = mots_Nlettres(dico, max_len)
        mots_possibles = []

        # On teste chaque mot si on peut le faire avec les lettres
        for mot in mots_longueur:
            if mot_possible(mot, lettres):
                mots_possibles.append(mot)

        if mots_possibles:  # si on a trouvé au moins un mot
            return mots_possibles

        max_len -= 1  # sinon on teste des mots plus courts

    return []  # aucun mot possible
# Exemple simple de dictionnaire
dico = ["chat", "chien", "lapin", "papa", "chapeau", "velo", "chaton"]

# Lettres disponibles
lettres = "aaplnchtiueo"

# Appel de la fonction
mots_max = mot_optimaux(dico, lettres)

print("Mots les plus longs possibles :", mots_max)



