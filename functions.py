import os
import random

fileName = "FIFA_World_cup/FIFA-2022.txt";

#1. Fonction `charger_donnees(fichier: str) -> list`
def Charger_donner (fileName):
    with open(fileName, "r+") as file:
        return file.readlines()
   

#2. Fonction `enregistrer_fichier("donnees, fichier.ext") -> fichier.ext`
def enregistrer_fichier(data, fichier2):
    with open(fichier2, 'w') as fichier_secondaire:
        fichier_secondaire.writelines(data)
    print("Texte FIFA mis a jour.")
    


#3. Fonction `supprimer_entete(fichier: str) -> list`
def supprimer_entete(data, fichier2):
    with open(fichier2, 'r+') as donne:
        lignes = donne.readlines()
        donne.seek(0);
        donne.truncate();
        donne.writelines(lignes[1:]);
        
#3. fonction transformer le fichier2 sous forme de colonne
def transformation_colonne(data, fichier2):
    with open(fichier2, 'w') as file:
        for line in data:
            colonnes = line.strip().split(',')
            file.write(','.join(colonnes) + '\n')   

#4. Fonction `afficher_nom_trois_lettres(str) -> str`
def affichier_nom_trois_lettres(data, fichier2):
    with open(fichier2, 'w') as resultat:
        for ligne in data:
            colonnes =ligne.strip().split(',')
            if len(colonnes) >=2:
                colonnes[1] = colonnes[1][:3]
                resultat.write(','.join(colonnes) + '\n')
            else:
                print("Impossible de faire le changement")
   

#6. mélanger les lignes d'un fichier
def melanger_lignes(fichier2):
    with open(fichier2, 'r') as file:
        lines = file.readlines()
        random.shuffle(lines)
    with open(fichier2, 'w') as file:
        file.writelines(lines)



