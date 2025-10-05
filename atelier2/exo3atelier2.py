def separer(lst:list,lsep:list)->list:
    negative=[]
    positive=[]
    null=[]


    for i in range(len(lst)):
        if lst[i]==0:
            null.append(lst[i])
        elif lst[i]<0:
            negative.append(lst[i])

        else:
            positive.append(lst[i])
    lsep= negative + null + positive
    return lsep


lst=[-1,0,0,6,5,-4,-7,9,3,0,0]
print(separer(lst,[]))

    