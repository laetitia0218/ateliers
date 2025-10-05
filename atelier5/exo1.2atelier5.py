def  factorielle_recursive(n:int)->int:
    if n==0:
        return 1
    else:
        return n*factorielle_recursive(n-1)
    
print(factorielle_recursive(5))
