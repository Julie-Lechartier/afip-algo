import os



FifaText = "FIFA_World_cup/FIFA-2022.txt";
file = open(FifaText, "r+");

#1. Fonction `charger_donnees(fichier: str) -> list`
print(file.read());
file.close()

#2. Fonction `supprimer_entete(fichier: str) -> list`

with open(FifaText, "r+") as supp:
    lignes = supp.readlines();
    supp.seek(0);
    supp.truncate();
    supp.writelines(lignes[1:]);
    supp.close()
#comment afficher le résultat ?


#3. Fonction `afficher_nom_trois_lettres(str) -> str`
with open(FifaText, "r+") as file:
    lignecol = file.readlines();
    colonnes = [lignecol.strip().split(",") for ligne in lignecol];
    for ligne in colonnes:
        print('\t'.join(ligne))
file.close()

#[:2].upper() placement et masjucule
# couper = slice(3)
#split
#with open ("FIFA_World_cup/FIFA-2022.txt", "r+") as fichier:
#    print(fichier.split(','))

#fichier = pd.read_csv("FIFA_World_cup/FIFA-2022.txt", sep=" ", header=None)
#print(fichier)