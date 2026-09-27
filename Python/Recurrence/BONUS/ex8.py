# Exercice 8 : La courbe de Koch est une figure qui s’obtient de manière récursive.
# Le cas de base (ordre zéro de la récurrence) est un segment de longueur L (fig.1)
#
# Le cas récursif d’ordre s’obtient en divisant ce segment en 3 morceaux de même
# longueur L/3, puis en dessinant un triangle équilatéral dont la base est le morceau
# du milieu, e, prenant soin de ne pas dessiner cette base. (fig.2). On forme une sorte
# de chapeau.
#
# On réitère ce processus à l’ordre (n-1) pour chaque segment de ce chapeau.

import turtle as t


def koch( L, n ):
    l = L/3

    if n == 0:
        return t.forward( l )

    else:   
        koch( L, n-1 )
        t.left( 60 )
        koch( L, n-1 )
        t.right( 120 )
        koch( L, n-1 )
        t.left( 60 )
        koch( L, n-1 )


koch( 30, 3)
