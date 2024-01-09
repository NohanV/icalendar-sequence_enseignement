# Projet d'Extraction et Traitement des Emplois du Temps

## Description du Projet

Ce projet Python a pour objectif d'extraire et de traiter les données des fichiers d'emploi du temps au format .ics, spécifiquement pour les formations universitaires (BUT1, BUT2, BUT3). L'objectif principal est de générer une page HTML organisant les informations des séances d'enseignement. Les données extraites incluent la date, l'heure de début, la durée, le type de séance, la salle, le groupe d'étudiants, et l'enseignant associé.


## Comment Exécuter le Programme
Avant toute chose afin d'installer les dépendances, il est nécessaire de créer un environnement virtuel. La méthode pour cela est :
```
git clone git@github.com:NohanV/icalendar-sequence_enseignement.git
python3 -m venv .venv
source .venv/bin/activate
cd icalendar-sequence_enseignement/
python3 -m pip install -r requirements.txt
```
Le programme principal est `sequence_enseignement.py`, qui prend en argument les noms des fichiers .ics (contenu dans la dossier data), le code du module, et le répertoire de sortie pour la page HTML. Voici un exemple d'utilisation :
```
$ python3 icalendar_se/sequence_enseignement.py --input-file data/ADECal_BUT1.ics data/ADECal_BUT2.ics data/ADECal_BUT3.ics --module "R103" --output-dir html/
```
## Documentation

La documentation complète du projet est disponible dans le dossier docs.

## Tests Unitaires

Les tests unitaires pour chaque fonction développée se trouvent dans le dossier tests. Vous pouvez les exécuter pour vérifier le bon fonctionnement du code.

## Auteur

Nohan VIOT
Léo MERLET
Rokia SISSAKO
