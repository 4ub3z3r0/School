def Boucle( i, k ):
    if i <= k:
        print( i )
        return Boucle( i+1, k )
    else:
        return k

Boucle( 0, 3 )n 
