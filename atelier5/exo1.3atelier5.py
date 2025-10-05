def longueur(L):
    if len(L)==0:#test d'arret
        return 0
    return 1 + longueur(L[1:])


print(longueur([1,2,3,4]))  
print(longueur([]))          
