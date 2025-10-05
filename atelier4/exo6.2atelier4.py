import random
import time
import matplotlib.pyplot as plt # type: ignore

# ----- Ta fonction de tri -----
def sort_list(lst):
    copie = list(lst)
    for i in range(len(copie)):
        min_index = i
        for j in range(i+1, len(copie)):
            if copie[j] < copie[min_index]:
                min_index = j
        temp = copie[i]
        copie[i] = copie[min_index]
        copie[min_index] = temp
    return copie

# ----- Comparaison -----
sizes = [10, 50, 100, 300,600]  # différentes tailles de listes
times_my = []       # temps pour ta fonction
times_builtin = []  # temps pour sorted

for i in sizes:
    # créer une liste aléatoire
    lst = [random.randint(0, 1000) for _ in range(i)]

    # mesurer temps pour sort_list
    start = time.perf_counter()
    sort_list(lst)
    end = time.perf_counter()
    times_my.append(end - start)

    # mesurer temps pour sorted
    start = time.perf_counter()
    sorted(lst)
    end = time.perf_counter()
    times_builtin.append(end - start)
print("Taille", i, ": sort_list =", times_my[-1], "secondes , sorted =", times_builtin[-1], "secondes")


# ----- Affichage graphique -----
plt.plot(sizes, times_my, marker="o", label="sort_list ")
plt.plot(sizes, times_builtin, marker="x", label="sorted")
plt.xlabel("Taille de la liste")
plt.ylabel("Temps (s)")
plt.title("Comparaison ")
plt.legend()
plt.show()
