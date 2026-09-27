def Somme( n ):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n**2 + Somme( n-1 )

print( Somme( 3 ) )
