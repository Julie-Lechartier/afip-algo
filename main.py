from functions import *

# Nom de fichier à charger
fileName = "FIFA_World_cup/FIFA-2022.txt";

# Charge un fichier en lecture
data = open(fileName, "r+")

# Charge les données à partir d'un fichier
print(Charger_donner(data))


#suppression de l'en-tête
print(supprimer_entete(data))


#affichage de trois lettres
print(affichier_nom_trois_lettres(supprimer_entete))