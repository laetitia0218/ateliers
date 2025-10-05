#Le tri fusion divise récursivement la liste en deux moitiés jusqu’à ce que chaque sous liste ait 0 ou 1 élément, puis fusionne ces souslistes triées pour obtenir la liste finale triée.
def fusion(A, B):
    result = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    # ajouter les éléments restants
    result.extend(A[i:])
    result.extend(B[j:])
    return result

def fusion_sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort.copy()  # liste déjà triée, on renvoie une copie
    mid = len(list_to_sort) // 2
    partie_1= fusion_sort(list_to_sort[:mid])
    partie_2 = fusion_sort(list_to_sort[mid:])
    return fusion(partie_1, partie_2)

my_lst_to_sort = [170, 45, 75, 90, 2, 24, 802, 66]

print('liste avant :', my_lst_to_sort)
print('liste apres :', fusion_sort(my_lst_to_sort))

