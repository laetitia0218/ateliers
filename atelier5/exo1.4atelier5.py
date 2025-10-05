def minimum(L):
    if len(L) == 1:
        return L[0]
    min_du_reste = minimum(L[1:])
    if L[0] < min_du_reste:
        return L[0]
    else:
        return min_du_reste
print(minimum([1,5,3,7,2]))