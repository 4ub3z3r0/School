lst = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -10 ]

def Somme( lst ):
    if len( lst ) == 1:
        return lst[0]
    else:
        if lst[-1] >= 0:
            return lst[-1] + Somme( lst[:-1] )
        else:
            return Somme( lst[:-1] )

print( Somme( lst ) )
