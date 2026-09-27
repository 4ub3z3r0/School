# recherche dichotomique recursive

lst_of_nums = [ 1, 5, 7, 50, 100, 110, 115, 200 ]
target = 5

def search( lst, n ):
    if len(lst) == 1:
        return lst[0] == n
    
    mid = ( lst[ (len(lst)//2) ], (len(lst)//2) ) # mid( mid, index )
    
    if mid[0] == n:
        return True
    else:
        if n > mid[0]:
            return search( lst[ mid[1] :], n )
        else:
            return search( lst[:mid[1]], n )


print( search( lst_of_nums, target ) )
