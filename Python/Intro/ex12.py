# Exercice 12 : Occurrences d'un caractère dans un mot
# 
# Écrire une fonction compte_occurrences qui prend en paramètres 
# cible, un caractère (une chaine de caractères de longueur 1), 
# et mot, une chaine de caractères, et qui renvoie le nombre 
# d'occurrences de cible dans mot ; c'est-à-dire le nombre de fois 
# où cible apparait dans mot.
# 
# On n'utilisera pas la méthode count.

string = input( 'Enter a word : ' )
letter = input( 'Enter any letter present in the word : ' )

def countOccurrences( target, word ):
    count = 0
    target = target.lower()
    word = word.lower()
    
    for e in word:
        if target == e:
            count += 1

    return count


print( countOccurrences( letter, string ) )
