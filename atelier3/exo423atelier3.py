#question2
def presente(lettre, mot):
    for i in range(len(mot)):
        if mot[i] == lettre:
            return i
    return -1
print(presente('e','eau'))
print(presente('e','bon'))

#question3

def mot_possible(mot, lettres):
    #transformer les lettres en liste
    list_lettres = list(lettres)

    for lettre in mot:
        pos = presente(lettre, list_lettres)#si la lettre se trouve dans le mot alors on retourne sa position sinon -1
        if pos == -1:      # lettre absente
            return False
        else:
            list_lettres.pop(pos) # on retire la lettre avec l'aquelle on viens de verifier 
    return True
print(mot_possible ("oiseaux", "isoezacvux"))
print(mot_possible ("tortue", "iszacvx"))
