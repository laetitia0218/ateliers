import random

# -------------------------
# Fonction pour trouver les positions d'une lettre dans un mot
# -------------------------
def places_lettre(ch: str, mot: str) -> list:
    positions = []
    for i in range(len(mot)):
        if ch == mot[i]:
            positions.append(i)
    return positions

# -------------------------
# Fonction pour afficher le mot avec lettres trouvées et tirets
# -------------------------
def outputStr(mot: str, lpos: list) -> str:
    resultat = []
    for i in range(len(mot)):
        if i in lpos:
            resultat.append(mot[i])
        else:
            resultat.append('_')
    return ' '.join(resultat)

# -------------------------
# Dessin du pendu
# -------------------------
pendu = [
    "|---] ",
    "| O ",
    "| T ",
    "|/ \\ ",
    "|______"
]

# -------------------------
# Lecture de la liste de capitales depuis le fichier
# -------------------------
def build_list(fileName: str) -> list:
    file = open(fileName, "r")
    content = file.readlines()
    file.close()

    mots = []
    for ligne in content:
        ligne = ligne.strip()
        parties = ligne.split("\t")
        if len(parties) > 0:
            capitale = parties[1].lower()
            mots.append(capitale)
    return mots

# -------------------------
# Construire un dictionnaire : clé = taille du mot, valeur = liste de mots
# -------------------------
def build_dict(lst: list) -> dict:
    d = {}
    for mot in lst:
        taille = len(mot)
        if taille not in d:
            d[taille] = []
        d[taille].append(mot)
    return d

# -------------------------
# Sélection d'un mot aléatoire selon la taille
# -------------------------
def select_word(sorted_words: dict, mot_len: int) -> str:
    mots = sorted_words[mot_len]
    element = random.randrange(len(mots))
    return mots[element]

# -------------------------
# Choix du mot selon le niveau de difficulté
# -------------------------
def choose_level(dico: dict) -> str:
    print("Vous allez choisir le niveau de difficulté du mot.")
    niveau = input("Choisissez un niveau (easy / normal / hard) : ").lower()
    if niveau == "easy":
        tailles = [i for i in dico.keys() if i < 7]
    elif niveau == "normal":
        tailles = [i for i in dico.keys() if 6 < i < 9]
    elif niveau == "hard":
        tailles = [i for i in dico.keys() if i > 8]
    else:
        print("Niveau inconnu, niveau 'easy' sélectionné par défaut.")
        tailles = [i for i in dico.keys() if i < 7]

    mot_len = random.choice(tailles)
    return select_word(dico, mot_len)

# -------------------------
# Programme principal
# -------------------------
def runGame():
    lst = build_list(r"C:\Users\laeti\Documents\atelier3\capitales.txt")
    dico = build_dict(lst)

    print("\nBienvenue au jeu du Pendu")
    mot = choose_level(dico)

    lettres_trouvees = []
    erreurs = 0

    print("Mot à deviner :", outputStr(mot, lettres_trouvees))

    while erreurs < 5 and len(lettres_trouvees) != len(mot):
        lettre = input("Proposez une lettre : ").lower()

        if len(lettre) != 1:
            print("Entrez une seule lettre !")
            continue

        pos = places_lettre(lettre, mot)

        if pos != []:  # lettre trouvée
            print("Bravo ! La lettre", lettre, "est dans le mot.")
            for p in pos:
                if p not in lettres_trouvees:
                    lettres_trouvees.append(p)
        else:  # lettre absente
            erreurs += 1
            print("Mauvaise lettre !")
            print(pendu[erreurs-1])

        print(outputStr(mot, lettres_trouvees))
        print("Erreurs :", erreurs, "/ 5\n")

    # Fin du jeu
    if len(lettres_trouvees) == len(mot):
        print("Félicitations ! Vous avez trouvé le mot :", mot)
    else:
        print("Vous avez perdu ! Le mot était :", mot)

# Lancer le jeu
runGame()
