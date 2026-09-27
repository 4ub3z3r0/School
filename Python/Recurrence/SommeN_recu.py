# somme des n (recursif)

##def S( n ):
##    
##    if n < 1:
##        assert n >= 0, 'n must be > 0'
##        return 0
##    else:
##        return n + S( n-1 )

def S_rec( n ):
    
    if n == 0:
        return 0
    else:
        return n + S( n-1 )

def S( n ):
    assert n >= 0, 'n must be > 0'
    return S_rec( n )

print( S(50) )
print( S(-50) )
