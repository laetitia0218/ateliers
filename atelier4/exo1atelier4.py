import random 
def gen_list_random_int(int_nbr=10, int_binf=0, int_bsup=10):
    lst= []
    for i in range(int_nbr):
        lst.append (random.randrange(int_binf,int_bsup))
    return lst
    
print(gen_list_random_int(5,2,9))
print(gen_list_random_int())
