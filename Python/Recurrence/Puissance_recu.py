# fonction puissance (recu)

def puissanceRec( x, n ):
    if n == 0:
        return 1
    elif n > 0:
        return x * puissanceRec( x, n-1 )
    else:
        return x / puissanceRec( x, -(n-1) )
    

print( puissanceRec( 2, -4 ) )
