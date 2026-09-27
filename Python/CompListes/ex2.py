# Générer par compréhension de liste : 
# Liste de 100 zéros : 					 
# [1 , 4 , 9 , 16 , etc. , 100] : 				
# ['a1' , 'b1'] à partir de ['a' , 'b'] :			  
# Les 26 lettres majuscules de l’alphabet français :
# La liste des carrés des (entiers pairs <= 100)
# Les cubes des (entiers <= 99 impairs) :
# Les carrés >= 245 des entiers <= 30 : 
# Liste des lettres communes à 'bonjour' et 'jour' : 

l1 = [ x for x in range(100) ]
print(l1)
print()

l2 = [ x**2 for x in range(1, 11) ]
print(l2)
print()

l3 = [ x+str(1) for x in ['a', 'b'] ]
print(l3)
print()

l4 = [ chr(x).upper() for x in range(ord('a'), ord('z') +1) ]
print(l4)
print()

l5 = [ x for x in range(101) if x % 2 == 0 ]
print(l5)
print()

l6 = [ x**3 for x in range(100) if x % 2 != 0 ]
print(l6)
print()

l7 = [ x**2 for x in range(100) if x <= 30 and x**2 >= 245 ]
print(l7)
print()

l8 = [ x for x in 'jour' if x in 'bonjour' ]
print(l8)
print()