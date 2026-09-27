# Exercice 13 : Élocution 

# Chez le dentiste, la bouche grande ouverte, lorsqu'on essaie 
# de parler, il ne reste que les voyelles. Même les ponctuations 
# sont supprimées. Vous devez écrire une fonction dentiste qui 
# prend une chaine de caractères texte et qui renvoie une autre 
# chaine ne contenant que les voyelles de texte, placées dans 
# l'ordre.

# On ne considèrera que des textes écrits en minuscules, 
# sans accents.

vowels = [ 'a', 'e', 'i', 'o', 'u', 'y' ]


string = 'helloworld'

def sort( string ):
    new_string = ''
    for e in string:

        if e in vowels:
            new_string += e

    return new_string

print( sort(string) )
