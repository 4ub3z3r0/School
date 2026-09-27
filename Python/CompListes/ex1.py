##Soient 2 listes nb = [65, 66], ltr = ["A", "D"]
##Evaluer directement les listes suivantes :
##[ 1 for k in range(4) ]
## --> [ 1, 1, 1, 1]

##[ 0 for k in range (2) ]
## --> [ 0, 0 ]

##[ triple(p) for p in [4 , -1 , 0 ] ]
## --> [ 12, -3, 0 ]

##[ 2*m + 1 for m in range (4) ]
## --> [ 1, 3, 5, 7 ]

##[ h.upper( ) for h in ['n','s','i'] ]
## --> [ 'N', 'S', 'I' ]

##[ ord(z) for z in ['a','b','c'] ]
## --> [ 97, 98, 99 ]

##['mot' + str(k) for k in range(1)]
## --> [ 'mot0' ]


lst = [ 'mot' + str(k) for k in range(1) ]

print(lst)
