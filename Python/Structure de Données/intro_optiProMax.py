import random as rd
import time as t

num_lst = [ rd.randint(1,365) for i in range( 23 ) ]
print( num_lst )
print()

def searchDoubles( lst ):
    S = 2**366

    for e in lst:
        if S&(1<<e) == 0 :
            S = S|(1<<e)
        else:
            print(e)
        

searchDoubles( num_lst )
