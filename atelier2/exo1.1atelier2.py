def exo_liste(ma_list:list)-> float:
    if len(ma_list)==0:
        return 0
    else:
        return sum(ma_list) / len(ma_list)
    
print(exo_liste([1,2,3,5,9]))