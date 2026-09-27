##Ecrire une fonction surfcarre qui calcule la surface
##d’un carré de côté « a » fourni en argument
##
##Ecrire une fonction surfcube qui calcule la surface
##d’un cube de côté « a » fourni en argument et qui utilise
##la fonction surfCarre
##
##Ecrire un programme qui calcule le volume d’un cube
##de côté « a » fourni en argument et qui utilise la fonction surfCube
##
##Ecrire une fonction surfVolCube qui renvoie la surface et
##le volume d’un cube. Utiliser cette fonction pour afficher
##la surface et le volume du cube (la surface du cube est : ….. ,
##son volume est …..

def surfCarre(a):
    surf = a**2
    return surf

def surfCube(a):
    surf = a**2 *6
    
    return surf

def surfVolume(a):
    surf = surfCube(a)
    vol = a**3

    return surf, vol

print( surfVolume(2) )
