# Ex 5 : Ecrire un programme qui permet d’afficher les N premiers termes de la suite de Fibonacci. 
# Le nombre N est fourni par l’utilisateur.
# La suite de Fibonacci est une suite d'entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent. 
# Elle commence par les termes 0 et 1 si on part de l'indice 0, ou par 1 et 1 si on part de l'indice 1.
# Fn est donc définie par F0 = 0, F1 = 1 et Fn = Fn-1 + Fn-2

n = int(input("Combien de termes voulez vous connaître ? "))
lst = [0, 1, 2]

if n <= 3:
    print(lst[:n])
else:
    for i in range(2, n-1):
        lst.append(lst[i]+lst[i-1])
    print(lst)
