

def rendre_monnaie(somme: int, valeurs: list[int], disponible: list[int]) -> list[int]:
    resultat = []  # ici on va stocker combien on rend pour chaque valeur

    for i in range(len(valeurs)):
         max_possible = somme // valeurs[i]   # combien on pourrait utiliser
         utilise = min(max_possible, disponible[i])  # mais pas plus que ce qu’on a
         resultat.append(utilise)  # on ajoute ce qu’on a utilisé
         somme -= utilise * valeurs[i]  # on enlève de la somme

    if somme == 0:
        return resultat
    else:
        return None
    
valeurs = [50, 20, 10, 5, 2, 1]
disponible = [2, 2, 3, 5, 10, 20]

print(rendre_monnaie(50, valeurs, disponible))
