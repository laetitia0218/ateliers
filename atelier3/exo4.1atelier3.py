def mot_correspond(mot, motif):
    if len(mot) != len(motif):
        return False

    for i in range(len(mot)):
        if motif[i] != "." and mot[i] != motif[i]:
            return False

    return True
print(mot_correspond('pain','p.in'))
print(mot_correspond('eau','peau'))
print(mot_correspond('..','..'))