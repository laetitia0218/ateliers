# Fonction pour construire la liste des mots à partir d'un fichier
def build_list(fileName: str) -> list:
    # ouvrir le fichier en lecture
    file = open(fileName, "r")
    content = file.readlines()  # lire toutes les lignes
    file.close()

    mots = []  # liste qui contiendra les capitales

    # parcourir chaque ligne
    for ligne in content:
        ligne = ligne.strip()           # enlever les espaces ou retours à la ligne
        parties = ligne.split("\t")    # séparer par tabulation
        if len(parties) > 0:
            capitale = parties[1].lower()  # prendre la première partie et mettre en minuscules
            mots.append(capitale)          # ajouter à la liste

    return mots
liste_mots = build_list("capitales.txt")
print(liste_mots)

 
