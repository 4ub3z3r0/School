def nbBits( n ):
    if n <= 1:
        return 1
    else:
        if n%2 == 0:
            return 0 + nbBits( n//2 )
        else:
            return 1 + nbBits( n//2 )
        
print( nbBits( 250 ) )
