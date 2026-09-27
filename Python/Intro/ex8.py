# Ex 8 : Ecrire une fonction supprimeDoublon(liste) qui supprime 
# les doublons d"une liste saisie par l"utilisateur 
# ex : [‘a","b","a","c","d","c","e"] 
# renvoie : [‘a","b","c","d","e"]

lst = [1, 2, 3, 4, 5, 5, 6, 5, 7]

def delDoubles(lst):
    
    for e in lst:
        if e in lst[lst.index(e)+1:]:# on enlève e si il y a e après
            lst.remove(e)
    
##    return lst

##print( delDoubles(lst) )

print(lst)
delDoubles(lst)
print(lst)
