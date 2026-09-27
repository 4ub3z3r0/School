# Trouver le max d'une liste avec son index
# Trouver le n ième max d'une liste avec son index

import random

n = int(input("Insérez n (correspondant au n ième maximum) : "))
lst = list()


def genLst(n):
    lst = []

    for i in range(n):
        lst.append((random.randint(0, 100), i))
    return lst


def findMax(lst):
    maxi = 0
    
    for e in lst:
        if e > maxi:
            maxi = e

    return maxi

def n_maxi(lst, n):
    maxi = findMax(lst)
    nieme = 0
    ind = 0

    for i in range(len(lst)):
        if lst[i] == maxi and nieme != n:
            nieme += 1
            ind = i

    if nieme < n:
        return None

    return ind



lst = genLst(8)
lst = [ 0, 12, 20, 6, 20, 1, 20 ]
print()
print(lst)
print(n_maxi(lst, n))
