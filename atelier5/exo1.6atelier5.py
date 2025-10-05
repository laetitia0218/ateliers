def concat_list(LL):
    if len(LL)==0:
        return []
    
    first = LL[0]
    rest = LL[1:]
    
    if type(first) == list:
        return concat_list(first) + concat_list(rest)
    else:
        return [first] + concat_list(rest)
print(concat_list( [[0,1], 2, [3, [4,5]], 6]))