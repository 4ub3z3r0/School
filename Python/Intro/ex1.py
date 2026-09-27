# Ex1 :
# Générer une liste de n entiers éléatoires (entre 0 et 100)
# Ecrire un programme qui calcule la somme des n premiers termes de cette liste

import random as rd

lst = []
n = int(input("Entrez le nombre d'entiers souhaités : "))
add = 0

for i in range(n):
    lst.append(rd.randint(0, 100))
    add += lst[-1]

print(lst)
print(add)