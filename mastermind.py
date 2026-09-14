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

    nbTentatives = 0
    codeTrouve = False

    while nbTentatives < NB_MAX_TENTATIVES and not(codeTrouve):
        stringInput = f"Essai n°{nbTentatives + 1}"
        tentative = list(input(""))
        isTentativeValide = validerTentative(tentative)
        if not(isTentativeValide):
            print("Erreur : format incorrect")

def genererCodeSecret():
    codeSecret = []
    for i in range(LONGUEUR_CODE):
        indexCouleur = randint(0, len(COULEURS) - 1)
        couleur = COULEURS[indexCouleur]
        codeSecret.append(couleur)
    return codeSecret

def validerTentative(tentative):
    isTentativeValide = True
    if len(tentative) != LONGUEUR_CODE:
        isTentativeValide = False
    else:
        for lettre in tentative:
            if lettre not in COULEURS:
                isTentativeValide = False
    return isTentativeValide

menu(True)