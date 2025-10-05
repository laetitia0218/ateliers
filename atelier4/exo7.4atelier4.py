def bubble_sort(lst_to_sort):
    lst = lst_to_sort.copy()
    n = len(lst)
    for i in range(n):              # i = 0, 1, 2, ..., n-1
        for j in range(0, n-1-i):   # parcours jusqu'à l'élément non trié
            if lst[j] > lst[j+1]:
                # échange classique
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst

my_lst_to_sort = [170, 45, 75, 90, 2, 24, 444, 66]

print('liste avant :', my_lst_to_sort)
print('liste apres  :', bubble_sort(my_lst_to_sort))