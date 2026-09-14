from random import randint
from os import remove, path

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
                    resetStatistiques()
                case 2:
                    valeurOk = True
                case _:
                    raise ValueError()
        except ValueError:
            print("Erreur : choix invalide")

def jouer():
    printRappels()

    codeSecret = genererCodeSecret()

    nbTentatives = 0
    codeTrouve = False

    while nbTentatives < NB_MAX_TENTATIVES and not(codeTrouve):
        stringInput = f"Essai n°{nbTentatives + 1} : "
        tentative = list(input(stringInput))
        isTentativeValide = validerTentative(tentative)
        if not(isTentativeValide):
            print("Erreur : format incorrect")
        else:
            nbTentatives += 1
            nbCorrects = getNbCorrects(tentative, codeSecret)
            print(f"Correct : {nbCorrects}")
            if nbCorrects == LONGUEUR_CODE:
                codeTrouve = True

    score = NB_MAX_TENTATIVES - nbTentatives
    sauvegarderScore(score)
    print(f"Score : {score}")
    
    menu(False)

def printRappels():
    print("Rappel des couleurs disponibles : ")
    stringCouleurs = ""
    for couleur in COULEURS:
        stringCouleurs += couleur + " "
    print(stringCouleurs)
    print(f"Longueur du code secret : {LONGUEUR_CODE}")
    print(f"Nombre maximum de tentatives : {NB_MAX_TENTATIVES}")
    stringFormat = ""
    for i in range(LONGUEUR_CODE):
        stringFormat += COULEURS[i % len(COULEURS)]
    print(f"Veuillez entrer vos essais au format « {stringFormat} »")

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

def getNbCorrects(tentative, codeSecret):
    nbCorrects = 0
    for i in range(len(codeSecret)):
        if tentative[i] == codeSecret[i]:
            nbCorrects += 1
    return nbCorrects

def sauvegarderScore(score):
    nbParties = 0
    scoreTotal = 0
    if path.isfile(".save"):
        with open(".save") as f:
            save = f.read()
            nbParties = int(save.split("\n")[0])
            scoreTotal = int(save.split("\n")[1])
    nbParties += 1
    scoreTotal += score
    with open(".save", "w") as f:
        f.write(f"{nbParties}\n{scoreTotal}")

def resetStatistiques():
    if path.isfile(".save"):
        remove(".save")
    menu(True)

menu(True)