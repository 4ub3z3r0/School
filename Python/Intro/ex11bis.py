##Ex 11:
##
##Mots à trou
##    • Un mot est ici une chaine de caractères composée uniquement de
##    lettres de l'alphabet.
##    • Un mot à trous comporte également zéro, une ou plusieurs fois
##    le caractère ".".
##    On dira que mot_complet correspond à mot_a_trous, si on peut
##    remplacer chaque "." de mot_a_trous par une lettre de façon à
##    obtenir mot_complet.
##    • "INFO.MA.IQUE" est un mot à trous,
##    • "INFORMATIQUE" est un mot qui lui correspond,
##    • "AUTOMATIQUE" est un mot qui ne lui correspond pas.
##Objectif
##Écrire une fonction telle que correspond(mot_complet, mot_a_trous) 
##renvoie un booléen qui détermine si « mot_complet correspond à 
##mot_a_trous »

def testString( word, gap_word ):
    for i in range(len(word)):
        if word[i] != gap_word[i] and gap_word[i] != ':':
            return False
