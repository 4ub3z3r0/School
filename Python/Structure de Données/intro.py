import random as rd
import time as t

num_lst = [ rd.randint(0, 100) for i in range( 10000 ) ]


def searchDoubles( lst ):
    temp = []
    for e in lst:
        if e in temp:
            return True
        temp.append( e )


print( searchDoubles( num_lst ) )
