import os

fileName = "FIFA_World_cup/FIFA-2022.txt";

#1. Fonction `charger_donnees(fichier: str) -> list`
def Charger_donner (data):
    data = open(fileName, "r+")
   

#2. Fonction `supprimer_entete(fichier: str) -> list`
def supprimer_entete(data):
    lignes = data.readlines()
    data.seek(0);
    data.truncate();
    data.writelines(lignes[1:]);
#comment afficher le résultat ?


#3. Fonction `afficher_nom_trois_lettres(str) -> str`
def affichier_nom_trois_lettres(data):
    lignecol = data.readlines();
    for ligne in lignecol:
        sep = ","
        acc = 0
        sequence = ''#message erreur no values
        if ligne == sep:
            acc = acc + 1
        if acc > 0 and acc <= 1 and ligne != sep :
            sequence += ligne;
    team = sequence[0]+sequence[1]+sequence[2]
    print(team)


#    print(ligne)     
#file.close()
    
#char name[50]:
#    name[0] = "F" création d'un index
#fonction char[50] on déclare le nombre de place à réserver
#[:2].upper() placement et masjucule
# couper = slice(3)
#split
#with open ("FIFA_World_cup/FIFA-2022.txt", "r+") as fichier:
#    print(fichier.split(','))

#fichier = pd.read_csv("FIFA_World_cup/FIFA-2022.txt", sep=" ", header=None)
#print(fichier)




# 4. Fonction `enregistrer_fichier("donnees, fichier.ext") -> fichier.ext`
def enregistrer_fichier(data):
    with open(fileName, "r+") as fichier_source:
        donnee = fichier_source.read()
    fichier_source.close
    text = open("text.txt", 'a')
    with open(text, 'w') as fichier_secondaire:
        fichier_secondaire.write(donnee)
    fichier_secondaire.close
    print("Texte FIFA mis a jour.")