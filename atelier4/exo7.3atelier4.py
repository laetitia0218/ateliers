def selection_sort(lst_to_sort):
    lst = lst_to_sort.copy() 
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j # mettre à jour la position du min
        if min_index != i:#le min n'est pas a la position i alors on echange 
           
           temp = lst[i]              
           lst[i] = lst[min_index]    
           lst[min_index] = temp      

    return lst


my_lst_to_sort = [170, 45, 75, 90, 2, 24, 406, 66]
print("liste avant  :", my_lst_to_sort)
print("liste apres :", selection_sort(my_lst_to_sort))
