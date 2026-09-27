import random as rd
import time as t

# 23 eleves dans une classe, on prend leur jour de naissance et on regarde si il y a un double

num_lst = [ rd.randint(1,365) for i in range( 23 ) ]

def searchDoubles( lst ):
    temp = [ False for i in range(1,366) ]

    for e in lst:
        if temp[e] == False:
            temp[e] = True
        else:
            return True, e
    return False
        

print( searchDoubles( num_lst ) )
