def incluse(l1, l2):
    if len(l1)==0:#Si la première liste l1 est vide : tous ses éléments ont été trouvés dans l2
        return True
    if len(l2)==0:#Si l2 est vide mais que l1 n’est pas vide, alors il reste des éléments à trouver
        return False
    if l1[0] == l2[0]:
        return incluse(l1[1:], l2[1:])#on compare le reste des elements
    else:
        return incluse(l1, l2[1:])#Si l1[0] != l2[0], on ignore le premier élément de l2 et on continue
    
l1 = [1, 3]
l2 = [1, 2, 3, 4]

print(incluse(l1, l2))

