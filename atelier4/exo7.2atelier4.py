def insertion_sort(list_to_sort):
    lst = list_to_sort.copy()   # copier pour ne pas modifier la liste originale
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]   # décalage
            j -= 1
        lst[j] = x
    return lst
my_lst_to_sort = [170, 45, 75, 90, 2, 24, 802, 66]
print("liste avant :", my_lst_to_sort)
print("liste apres :", insertion_sort(my_lst_to_sort))
