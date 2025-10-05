def somme_recursive(liste):
    if len(liste)==0: #test d'arret
        return 0
    return liste[0] + somme_recursive(liste[1:])


liste1 = [1, 2, 3, 4, 5]

print(somme_recursive(liste1))

liste2 = []

print(somme_recursive(liste2))
