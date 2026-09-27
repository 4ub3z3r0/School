# fonction puissance (recu)

def puissanceRec( x, n ):
    print("Called")
    if n == 0:
        return 1
    elif n < 0:
        return x / puissanceRec( x, -(n-1) )
    else:
        if n%2 == 0:
            return (x**x) * puissanceRec( x, n-2 )
        else:
            return x* puissanceRec( x, n-1 )

    
    

print( puissanceRec( 2, 5 ) )
