from typing import Tuple
def is_mail(str_arg: str) ->Tuple[int, int]:
    # Vérification 1 : présence de @
    if "@" not in str_arg:
        return (0, 2)
    
    # Séparation corps / domaine
    try:
        corps, domaine = str_arg.split("@")
    except ValueError:  # si plusieurs @
        return (0, 2)
    
    # Vérification  2 : corps
    if (not corps or corps[0] == "." or corps[-1] == "." or ".." in corps):
        return (0, 1)
    for c in corps:
        if not (c.isalnum() or c in "-_."):
            return (0, 1)
    
    # Vérification 3 : domaine
    if "." not in domaine:
        return (0, 4)
    if (not domaine or domaine[0] == "." or domaine[-1] == "." or ".." in domaine):
        return (0, 3)
    for c in domaine:
        if not (c.isalnum() or c == "-." or c in "-."):
            return (0, 3)
    
    # Tout est bon
    return (1, 0)

print(is_mail("laeti18@univ-corse.fr"))
print(is_mail("laeti18.univ-corse.fr"))