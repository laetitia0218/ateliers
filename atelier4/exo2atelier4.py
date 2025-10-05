import random

def mix_list(list_to_mix):
    copie = list(list_to_mix)  # copie pour ne pas modifier l'original
    melange = []
    while copie:
        element= random.randrange(len(copie))  # choisir un element au hasard
        melange.append(copie[element])  # ajouter l'élément à la nouvelle liste melange
        copie.pop(element)  # retirer l'élément de la copie pour eviter de le reprendre 
    return melange

# liste depart
liste_depart = [0, 'e', 2, 3, 4, 'bon', 6, 7, 8, 9]
print('la liste de depart est:', liste_depart)

# liste melangé
liste_sortie = mix_list(liste_depart)
print('la liste melangé est:', liste_sortie)
