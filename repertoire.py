
# Mini projet débutant.
import json
print('#'*50)
print("\n Mon super agenda \n")
print('#'*50)

def ajouter_nom(data):
    nom = input("Nom : ")
    numero = input(f"Numéro de {nom} :")
    data[nom] = numero
    with open('data.json', 'w') as fp:
        json.dump(data, fp)

def afficher_repertoir():
    pass

def detruire_urgence():
    pass

def rechercher_nom():
    pass

with open('data.json', 'r') as fp:
    data = json.load(fp)
choix = None
print(data)
#######################
#       Menu          #
#######################


while choix != 0:
    print(" \nVeuillez choisir une option\n")
    print(" 1 - Ajouter un nom")
    print(" 2 - Consulter le répertoire")
    print(" 0 - Pour quitter")
    choix = int(input("-->"))
    if choix in [0, 1, 2]:
        print(f"Votre choix est le {choix}")
        if choix == 1:
            print("Vous débutez la procédure d'ajout d'un nouveau nom")
            ajouter_nom(data)
    else:
        print("Choix invalide, veuillez recommencer")