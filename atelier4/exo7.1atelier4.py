import random

#pour verifier si une liste est triee
def est_triee(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Tri stupide
def stupid_sort(lst_to_sort):
    lst = lst_to_sort.copy()  # pour ne pas modifier la liste originale
    while est_triee(lst) == False:
        random.shuffle(lst)  # melanger aleatoirement les elements d'une liste 
    return lst

# Test
liste = [3, 1, 2]
resultat = stupid_sort(liste)
print(resultat)

    