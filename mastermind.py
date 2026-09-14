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
                case 1:
                    valeurOk = True
                case 2:
                    valeurOk = True
                case _:
                    raise ValueError()
        except ValueError:
            print("Erreur : choix invalide")

menu(True)