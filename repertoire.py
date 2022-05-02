
# Mini projet débutant.
import json
print('#'*50)
print("\n Répertoir trop puissant |\n version réalisée par Red Richards, \n alias \
 Mr Fantastique à l'occasion de son apparition dans Docteur Strange 2\n")
print('#'*50)

def ajouter_nom():
    nom  = input("Nom : ")
    numero = input(f"Numéro de {nom}")


def afficher_repertoir():
    pass

def detruire_urgence():
    pass

def rechercher_nom():
    pass

#######################
#       Menu          #
#######################
choix = None
while choix != 0:
    print(" \nVeuillez choisir une option\n")
    print(" 1 - Ajouter un nom")
    print(" 2 - Consulter le répertoire")
    print(" 0 - Pour quitter")
    choix = input("-->")
    if choix in [0, 1, 2]:
        print(f"Votre choix est le {choix}")
        if choix == 1:
            print("Vous débutez la procédure d'ajout d'un nouveau nom")
            ajouter_nom()
    else:
        print("Choix invalide, veuillez recommencer")