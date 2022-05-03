
# Mini projet débutant.
import json
print('#'*50)
print("\n Mon super repertoire \n")
print('#'*50)

def ajouter_nom(data: dict) -> None:
    """
        Procédure permettant d'ajouter un nom au dictionnaire data et
        de l'enregistrer au format Json
        :param data: dic
        :return: None
    """
    nom = input("Nom : ")
    numero = input(f"Numéro de {nom} :")
    data[nom] = numero
    with open('data.json', 'w') as fp:
        json.dump(data, fp)

def afficher_repertoire(data):
    i = 1
    for nom, numero in data.items():
        print(f"{i}.\t {nom}  {numero}")

def detruire_urgence():
    pass

def rechercher_nom(nom: str) -> str:
    """
        Fonction qui vérifie si un membre est dans le repertoire
        retourne son numéro s'il s'y trouve, None sinon
    :param nom: str
    :return: bool
    """
    return data.get(nom, None)

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
    if choix in [0, 1, 2, 3]:
        print(f"Votre choix est le {choix}")
        if choix == 1:
            print("Vous débutez la procédure d'ajout d'un nouveau nom")
            ajouter_nom(data)
        elif choix == 2:
            afficher_repertoire(data)
        elif choix == 3:
            num = rechercher_nom(input("entrez le nom dont vous voulez le numéro"))
            if num:
                print(f"Le numéro de est {num}")
            else:
                print(f"Le numéro n'est pas présent dans notre repertoire ")
    else:
        print("Choix invalide, veuillez recommencer")