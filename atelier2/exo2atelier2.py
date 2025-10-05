def val_maxW(ma_list:list)->int:
    nb_max=ma_list[0]
    i=0
    while i<len(ma_list):
          if ma_list[i]>nb_max:
            nb_max=ma_list[i]
          i=i+1
    return nb_max
print(val_maxW([1,8007,2,6,100]))