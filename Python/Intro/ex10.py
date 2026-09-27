##Ex10 :
##    
##    • Soient les listes suivantes :
##t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##t2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
##      "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
##Écrire un petit programme qui crée une nouvelle liste t3. Celle-ci
##devra contenir tous les éléments des deux listes en les alternant,
##de telle manière que chaque nom de mois soit suivi du nombre de jours
##correspondant : ["Janvier",31,"Février",28,"Mars",31, etc...].
##
##    • Écrire un programme qui affiche « proprement » tous les éléments
##    d"une liste. Si on l"appliquait par exemple à la liste t2 de
##    l"exercice ci-dessus, on devrait obtenir :
##      Janvier Février Mars Avril Mai Juin Juillet Août Septembre Octobre
##      Novembre Décembre
##
##    • Écrire un programme qui recherche le plus grand élément présent
##    dans une liste donnée. Par exemple, si on l"appliquait à la liste
##    [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher la phrase :
##      le plus grand élément de cette liste a la valeur 75.
##
##    • Écrire un programme qui analyse un par un tous les éléments
##    d"une liste de nombres (par exemple celle de l"exercice précédent)
##    pour générer deux nouvelles listes. L"une contiendra seulement les
##    nombres pairs de la liste initiale, et l"autre les nombres impairs.
##    Par exemple, si la liste initiale est celle de l"exercice précédent,
##    le programme devra construire une liste pairs qui contiendra
##    [32, 12, 8, 2], et une liste impairs qui contiendra [5, 3, 75, 15].
##  Astuce : pensez à utiliser l"opérateur modulo (%) déjà cité précédemment.
##
##    • Écrire un programme qui analyse un par un tous les éléments d"une
##    liste de mots (par exemple : ["Jean", "Maximilien", "Brigitte", "Sonia",
##    "Jean-Pierre", "Sandra"] ) pour générer deux nouvelles listes.
##    L"une contiendra les mots comportant moins de 6 caractères,
##    l"autre les mots comportant 6 caractères ou davantage.


t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
      "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

t3 = [( x, y )for x in t2 for y in t1]

lst_num = [32, 5, 12, 8, 3, 75, 2, 15]

def proper_list(lst):
    string = ""
    for e in lst:
        string += e
        string += " "

    return string


def find_max(lst):
    maxi = 0

    for e in lst:
        if e > maxi:
            maxi = e

    return maxi


def parity(lst):
    even = []
    odd = []
    
    for e in lst:
        if e % 2 == 0:
            even.append(e)

        else:
            odd.append(e)

    return even, odd


def words_under_six(lst):
    less = []
    more = []
    
    for e in lst:
        if len(e) < 6:
            less.append(e)

        else:
            more.append(e)

    return less, more

print(t3)

print()

print( proper_list(t2) )

print()

print( find_max(lst_num) )

print()

print( parity(lst_num) )

print()

print( words_under_six(t2) )
