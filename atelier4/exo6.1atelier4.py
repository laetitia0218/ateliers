def sort_list(lst):
#copie de la liste
    copie = list(lst)

    # Tri 
    for i in range(len(copie)):
        min_index = i
        for j in range(i+1, len(copie)):
            if copie[j] < copie[min_index]:
                min_index = j

        temp = copie[i]                 
        copie[i] = copie[min_index]    
        copie[min_index] = temp         

    return copie
print(sort_list([0,6,7,1,3]))