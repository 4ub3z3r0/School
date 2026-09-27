# Ex 4 : On dispose d’une feuille de papier d’épaisseur e (ex 0,1 mm)
# Combien de fois doit-on la plier au minimum pour que l’épaisseur dépasse une hauteur de 400 m
# Ecrire un programme pour résoudre ce probème

e = float(input("Insérez l'épaisseur de la feuille (en mm) : "))
folds = 0

while e <= 400000:
    folds += 1
    e += e

print(folds)