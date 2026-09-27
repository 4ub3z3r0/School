def nbChiffres( n ):
    if n <= 0:
        return 0
    else:
        return 1 + nbChiffres( n//10 )

print( nbChiffres( 34126 ) )
