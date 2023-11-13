# Projet d'Extraction et Traitement des Emplois du Temps

## Description du Projet

Ce projet Python a pour objectif d'extraire et de traiter les données des fichiers d'emploi du temps au format .ics, spécifiquement pour les formations universitaires (BUT1, BUT2, BUT3). L'objectif principal est de générer une page HTML organisant les informations des séances d'enseignement. Les données extraites incluent la date, l'heure de début, la durée, le type de séance, la salle, le groupe d'étudiants, et l'enseignant associé.

## Structure du Projet

L'arborescence du projet est organisée comme suit :

## Comment Exécuter le Programme

Le programme principal est `sequence_enseignement.py`, qui prend en argument les noms des fichiers .ics, le code du module, et le répertoire de sortie pour la page HTML. Voici un exemple d'utilisation :

$ ./sequence_enseignement.py --input-file ADECal_BUT1.ics ADECal_BUT2.ics ADECal_BUT3.ics --module R107 --output-dir ./../html/

## Documentation

La documentation complète du projet est disponible dans le dossier docs. Vous pouvez générer la documentation en utilisant les outils appropriés.

## Tests Unitaires

Les tests unitaires pour chaque fonction développée se trouvent dans le dossier tests. Vous pouvez les exécuter pour vérifier le bon fonctionnement du code.

## Auteur

Nohan VIOT
Léo MERLET
Rokia SISSAKO
