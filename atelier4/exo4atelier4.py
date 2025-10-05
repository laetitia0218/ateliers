import random

def extract_elements_list(list_in_which_to_choose, int_nbr_of_element_to_extract):
    copie = list(list_in_which_to_choose)  # copie pour ne pas modifier la liste originale
    extrait = []
    
    for i in range(int_nbr_of_element_to_extract):
        element = random.randrange(len(copie))  # choisir un element au hasard
        extrait.append(copie[element])      # ajouter l'élément et le retirer de la copie
        copie.pop(element)#on supprime l'element de copie 
    return extrait

# Test
liste_depart= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('la liste de depart est :', liste_depart)

liste_sortie = extract_elements_list(liste_depart, 5)
print('la sous liste de sortie est :', liste_sortie)

