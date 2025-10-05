### une version avec une boucle for basée sur les indices (for i in range(.....))

def nb_sup(ma_list: list, e: int) -> int:
    cpt = 0
    for i in range(len(ma_list)):
        if ma_list[i] > e:
            cpt = cpt + 1
    if cpt==0:
            print("aucun nombre de la list est superieur a: ", e)  
    return cpt
        

print(nb_sup([1, 2, 6, 8, 7, 4, 9], 10))


### une version avec une boucle for basée sur les éléments (for e in liste)

def nb_sup(ma_list: list, e: int) -> int:
    cpt = 0
    
    for valeur in ma_list:
        if valeur> e:
            cpt = cpt + 1
    if cpt==0: 
             print("aucun nombre de la list est superieur a: ", e)  
    return cpt 
print(nb_sup([1, 2, 6, 8, 7, 4, 9], 15))      
print(nb_sup([1, 2, 6, 8, 7, 4, 9], 2)) 

### Une version avec une boucle while

def nb_sup(ma_list: list, e: int) -> int:
    cpt = 0
    i = 0
    while i < len(ma_list):
        if ma_list[i] > e:
            cpt += 1
        i += 1   # toujours incrémenter i, peu importe le cas
    if cpt == 0:   # à vérifier après la boucle
        print("Aucun nombre de la liste n'est supérieur à:", e)
    return cpt

print(nb_sup([1, 2, 6, 8, 7, 4, 9], 6))  # Résultat attendu: 2
           
