from random import randint

COULEURS = ["R", "V", "B", "J", "M", "N"]
LONGUEUR_CODE = 4
NB_MAX_TENTATIVES = 12

def menu(premierLancement):
    print("----------------------------------------")
    print("|              Mastermind              |")
    print("----------------------------------------")
    if premierLancement:
        print("| 0 - Jouer                            |")
    else:
        print("| 0 - Rejouer                          |")
    print ("| 1 - Remettre à zéro les statistiques |")
    print ("| 2 - Quitter                          |")
    print("----------------------------------------")
    valeurOk = False
    while not(valeurOk):
        try:
            choixUtilisateur = int(input(""))
            match (choixUtilisateur):
                case 0:
                    valeurOk = True
                    jouer()
                case 1:
                    valeurOk = True
                case 2:
                    valeurOk = True
                case _:
                    raise ValueError()
        except ValueError:
            print("Erreur : choix invalide")

def jouer():
    print("Rappel des couleurs disponibles : ")
    stringCouleurs = ""
    for couleur in COULEURS:
        stringCouleurs += couleur + " "
    print(stringCouleurs)

    codeSecret = genererCodeSecret()

def genererCodeSecret():
    codeSecret = []
    for i in range(LONGUEUR_CODE):
        indexCouleur = randint(0, len(COULEURS) - 1)
        couleur = COULEURS[indexCouleur]
        codeSecret.append(couleur)
    return codeSecret

menu(True)