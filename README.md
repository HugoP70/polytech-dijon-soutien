# polytech-dijon-soutien

## Présentation

Ce projet est un mastermind en ligne de commande.

Il a été réalisé dans le cadre du module de soutien informatique de la troisième année du diplôme d'Ingénieur Informatique et Réseaux option Cybersécurité au sein de l'école Polytech.

## Démarrage

### Windows

```
python3 -m venv .venv
.venv\Scripts\activate
python3 mastermind.py
```

### Linux

```
python3 -m venv .venv
source .venv/bin/activate
python3 mastermind.py
```

## Paramétrage

Il est possible de changer les couleurs, leur nombre, la longueur du code secret, le nombre maximum de tentatives et le chemin du fichier de sauvegarde au début du fichier `mastermind.py` : 

```
COULEURS = ["R", "V", "B", "J", "M", "N"]
LONGUEUR_CODE = 4
NB_MAX_TENTATIVES = 12
PATH_SAUVEGARDE = ".save"
```
