def checkPalindrome( string ):
    if len(string) == 0:
        return True
    else:
        if string[0] == string[-1]:
            return True == checkPalindrome( string[1:-1] )

print( checkPalindrome( 'tesset' ) )
