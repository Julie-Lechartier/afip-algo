from functions import *

# Nom de fichier à charger
fileName = "FIFA_World_cup/FIFA-2022.txt";

# Charge les données à partir d'un fichier
data = Charger_donner(fileName);
print(data)

#suppression de l'en-tête
print(supprimer_entete(fileName))

#nouveau fichier copié
fichier2 = "text.txt"
enregistrer_fichier(data, "text.txt")

#affichage de trois lettres
affichier_nom_trois_lettres(data, fichier2)


#melanger les lignes
print(melanger_lignes(fichier2))