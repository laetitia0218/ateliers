import random

def choose_element_list(list_in_which_to_choose):
    # choisir un index au hasard et retourner l'élément correspondant
    element= random.randrange(len(list_in_which_to_choose))
    return list_in_which_to_choose[element]

# Liste triée de départ
liste_depart= [0, 'e', 2, 3, 4, 5, 'z', 7, 8, 9]
print('Liste triée de départ:', liste_depart)

# Choix aléatoire d'éléments
e1 = choose_element_list(liste_depart)
print('À la première exécution,', e1, 'a été sélectionné')

e2 = choose_element_list(liste_depart)
print('À la deuxième exécution,', e2, 'a été sélectionné')

# Vérification 
if e1 != e2:
    print("Les deux éléments sélectionnés sont différents")
else:
    print("Les deux éléments sélectionnés sont identiques")
