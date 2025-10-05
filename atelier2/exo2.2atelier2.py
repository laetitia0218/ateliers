def nb_occurrences(ma_list:int, e:int)->int:
    nb=0
    for i in range(len(ma_list)):
        if ma_list[i]==e :
            nb+=1
    return nb 
print(nb_occurrences([1,2,5,8,6,9,4,5,5],5))