# Ex2 : Ecrire un programme qui permet de saisir un entier positif composé de 5 chiffres différents, 
# puis de vérifier et d’afficher si cet entier obéit à la règle ou non

n = int(input("Entrez un entier positif composé de 5 chiffres : "))

def verifyNum(n):
    n = str(n)
    lst = []

    if len(n) != 5:
        return "Cet entier ne contient pas 5 chiffres."

    else :
        for e in n:
            if e not in lst:
                lst.append(e)
            else:
                return "Cet entier contient plusieurs fois le même chiffre."
            
        return "Cet entier obéit à la règle."


def verifyNumNoStr(n):
    temp = n
    seen = []
    nb_nb = 0

    while temp > 0:
        nb = temp % 10
        nb_nb += 1

        if nb in seen:
            return False
        else: senn.append(nb)

        temp = temp // 10

    if nb_nb >= 5
        return True
    else:
        return False

    print(lst)
    

##print(verifyNum(n))
print(verifyNumNoStr(n))
