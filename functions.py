import os

#1. Fonction `charger_donnees(fichier: str) -> list`
fichier = open("FIFA_World_cup/FIFA-2022.txt", "r")
print(fichier.read())
fichier.close()

#2. Fonction `supprimer_entete(fichier: str) -> list`
with open ("FIFA_World_cup/FIFA-2022.txt", "r+") as fichier:
    ligne1 = fichier.readlines()
    fichier.seek(0)
    fichier.truncate()
    fichier.writelines(ligne1[1:])
fichier.close()

#3. Fonction `afficher_nom_trois_lettres(str) -> str`
#[:2].upper() placement et masjucule
# couper = slice(3)
#split
with open ("FIFA_World_cup/FIFA-2022.txt", "r+") as fichier:
    print(fichier.split(','))