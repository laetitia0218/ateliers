import random
import time
import matplotlib.pyplot as plt # type: ignore

# ---- Tes fonctions ----
def mix_list(list_to_mix):
    copie = list(list_to_mix)  
    melange = []
    while copie:
        element = random.randrange(len(copie))
        melange.append(copie[element])
        copie.pop(element)
    return melange

def extract_elements_list(list_in_which_to_choose, int_nbr_of_element_to_extract):
    copie = list(list_in_which_to_choose)
    extrait = []
    for i in range(int_nbr_of_element_to_extract):
        element = random.randrange(len(copie))
        extrait.append(copie[element])
        copie.pop(element)
    return extrait

# ---- Fonction de comparaison ----
def perf_mix(func1, func2, sizes, nb_exec):
    times_func1 = []
    times_func2 = []
    
    for n in sizes:
        lst = list(range(n))  # une liste de taille n
        
        # temps moyen func1
        total1 = 0
        for _ in range(nb_exec):
            start = time.perf_counter()
            func1(lst[:])
            end = time.perf_counter()
            total1 += end - start
        times_func1.append(total1 / nb_exec)

        # temps moyen func2
        total2 = 0
        for _ in range(nb_exec):
            start = time.perf_counter()
            func2(lst[:])
            end = time.perf_counter()
            total2 += end - start
        times_func2.append(total2 / nb_exec)
    
    return times_func1, times_func2

# Comparaison extract_elements_list vs sample
sizes = [10, 100, 1000, 5000]
times_my, times_builtin = perf_mix(
    lambda lst: extract_elements_list(lst, 5),   # ta fonction
    lambda lst: random.sample(lst, 5),          # fonction Python
    sizes, 10
)

print("Résultats extract_elements_list :", times_my)
print("Résultats sample :", times_builtin)

plt.plot(sizes, times_my, "o-", label="extract_elements_list ")
plt.plot(sizes, times_builtin, "x-", label="sample")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps moyen (s)")
plt.title("Comparaison extract_elements_list et sample")
plt.legend()
plt.show()

