import random as rd
import time as t

# 23 eleves dans une classe, on prend leur jour de naissance et on regarde si il y a un double

num_lst = [ rd.randint(1,365) for i in range( 23 ) ]
print( num_lst )
print()

def searchDoubles( lst ):
    temp = 2**366

    for e in lst:
        print( temp ** (0.5 * (366 - e)) )

        

searchDoubles( num_lst )
