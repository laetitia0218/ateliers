def listPairs(L):
    if len(L) == 0:
        return
    if L[0] % 2 == 0:
        print(L[0])
    listPairs(L[1:])

# Tests
listPairs([1,2,3,4,5,6])
listPairs([1,3,5])
