def moy_sup(ma_liste: list, e: int) -> float:
    somme = 0
    cpt = 0
    for valeur in ma_liste:
        if valeur> e:
            somme += valeur
            cpt += 1
    if cpt == 0:
        return 0.0
    return somme / cpt

print(moy_sup([1, 2, 6, 8, 7, 4, 9], 5))  



