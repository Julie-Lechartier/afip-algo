from functions import *

# Nom de fichier à charger
fileName = "FIFA_World_cup/FIFA-2022.txt";

# Charge les données à partir d'un fichier
data = Charger_donner(fileName);
print(data)

#suppression de l'en-tête
supprimer_entete(fileName)

#nouveau fichier copié
fichier2 = "text.txt"
enregistrer_fichier(data, fichier2)





#transformation des lignes en colonnes
transformation_colonne(data, fichier2)





#affichage de trois lettres
affichier_nom_trois_lettres(data, fichier2)


#melanger les lignes
print(melanger_lignes(fichier2))

#calculer les point 
calculer_points(fichier2)