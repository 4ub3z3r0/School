n = 4
matrice = [ [1 if i==j else 0 for j in range(n)] for i in range(n) ]
# ou
matrice = [ [int(j==i) for j in range(n)] for i in range(n) ]
# int( i==j ) converti True en 1 et False en 0

print( matrice )
