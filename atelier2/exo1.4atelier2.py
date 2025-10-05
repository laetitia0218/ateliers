def val_max( ma_list: int) -> int:
    max = ma_list[0]
    for i in range(len(ma_list)):
        if ma_list[i]>max:
            max=ma_list[i]
    return max
print(val_max([1,5,6,8,9,3]))        