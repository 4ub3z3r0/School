# Exercice 14 : Tester si deux listes contiennent des 
# valeurs différentes : 
#
# Un laboratoire reçoit des résultats depuis deux sources 
# différentes. Les résultats sont deux tableaux d'entiers 
# source_1 et source_2 de même longueur.
#
# Quand deux résultats concordent, on considère qu'il n'y 
# aura pas à refaire l'expérience, on le codera par False, 
# mais si les résultats sont différents, on considère qu'il 
# faudra refaire cette expérience, on le codera par True.
#
# Écrire une fonction telle que differences(source_1, source_2) 
# renvoie un tableau de la longueur commune à source_1 et source_2 
# rempli de booléens.

lst_1 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

lst_2 = [ 0, 0, 2, 2, 4, 4, 6, 6, 8, 8 ]

def Test( source, source_2 ):
    result = []
    
    for i in range(len( source )):

        if source[i] == source_2[i]:
            result.append(False)

        else:
            result.append(True)

    return result
