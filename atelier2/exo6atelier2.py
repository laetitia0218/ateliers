def agencement(nbEmplacements: int, lObjets: list[int]) -> tuple[list[int], list[int]]:  
    vitrine1 = []
    vitrine2 = []
    
    for obj in lObjets:
        print(f"Placer {obj} | vitrine1={vitrine1}, vitrine2={vitrine2}")  # DEBUG
        
        if obj in vitrine1 and obj in vitrine2:
            print("⚠️ déjà dans les deux -> None")
            return None
        
        # Si déjà dans vitrine1 -> essaye vitrine2
        if obj in vitrine1:
            if obj not in vitrine2 and len(vitrine2) < nbEmplacements:
                vitrine2.append(obj)
            else:
                return None
        
        # Sinon on essaye vitrine1 d'abord
        elif obj not in vitrine1 and len(vitrine1) < nbEmplacements:
            vitrine1.append(obj)
        
        # Sinon vitrine2
        elif obj not in vitrine2 and len(vitrine2) < nbEmplacements:
            vitrine2.append(obj)
        
        else:
            return None  
    
    return vitrine1, vitrine2


# Test
nbEmplacements = 4   
lObjets = [1, 2, 2, 3, 4, 5, 5]
print("Résultat :", agencement(nbEmplacements, lObjets))
