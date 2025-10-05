def position(ma_list:int, elt:int)->int:
    for i in range(len(ma_list)):
        if ma_list[i]==elt:
            return i
        else:
            return -1
        

print(position([1,2,4,9,5,6,7],4))

### avec une boucle while

def position(ma_list:int, elt:int)->int:
    i=0
    while i < len(ma_list):
         if ma_list[i]==elt:
            return i
         i+=1

    
    return -1
print(position([1, 2, 4, 9, 5,8, 6, 7], 8))