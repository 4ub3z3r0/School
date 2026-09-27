# Ex3 : Ecrire un programme permettant de lire un nombre entier n 
# puis calcule son factoriel en utilisant une boucle while

n = int(input("Entrez un entier n : "))
facto = 1

for i in range(1, n+1):
    facto *= i

print(facto)