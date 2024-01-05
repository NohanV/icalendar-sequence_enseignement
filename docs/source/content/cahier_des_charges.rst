=============================================
I-calendar : service enseignant
=============================================

-------------------------
Cadre et objectif général
-------------------------

Le projet a pour objectif d'extraire les **données des fichiers des emplois du temps** des 3 formations du département : BUT1, DUT2, LPARM que vous aurez préalablement extraits du logiciel ADE de l'ent de l'Université afin de déterminer le service d'enseignement d'un enseignant.

Les étapes principales du projet consistent à :

* lire et extraire les données pertinentes des fichiers ``.ics`` ;

* les traiter afin de pouvoir produire pour un enseignant donné :
      * pour chaque module enseigné les données suivantes :
	 * Nom du module
	 * Nombre d'heures de cours (hC)
	 * Nombre d'heures de TD (hTD)
	 * Nombre d'heures de TP (hTP)
	 * Nombre d'heures de contôle de TP (hcTP)
	 * Nombre d'heures de contrôle de cours  (hcC)
	 * Nombre d'heures de présence (hP)
	 * Nombre d'heures équivalent TD (hETD) : hETD = 1.5*hC + hTD + hTP + hcTP
      * le sous-total de ces heures pour chaque formation
      * le total de ces heures pour toutes les formations

* de construire une page html/css sur laquelle seront présentées les données extraites et calculées sous la forme d'un tableau de la forme suivante :

 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
 |Formation  |Code du module    | Nom du module                    | H cours| H TD| H TP| H ctrl cours| H ctrl TP| H présence |H ETD  |
 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
 |BUT1       | R-107            | Fondamentaux de la programmation |  5.0   | 12.0| 21.0| 1.5         | 3.0      |  53.0      | 55.5  |
 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
 |           | SAE-15           | Traiter des données              |  1.0   |  6.0| 18.0| 0.0         | 6.0      |  31.0      | 31.5  |
 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
 |Total BUT1 |                  |                                  |  6.0   | 18.0| 39.0| 1.5         | 9.0      |  84.0      | 87.0  |
 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
 |DUT2       | OST01            | TNS                              |  3.0   |  6.0| 15.0| 1.5         | 3.0      |  27.5      | 28.5  |
 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
 |Total DUT2 |                  |                                  |  3.0   |  6.0| 15.0| 1.5         | 3.0      |  27.5      | 28.5  |
 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
 |LP ARM     | M34              | Administration système           |  0.0   |  2.0| 18.0| 0.0         | 0.0      |  20.0      | 21.0  |
 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
 |Total LPARM|                  |                                  |  0.0   |  2.0| 18.0| 0.0         | 0.0      |  20.0      | 21.0  |
 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
 |Total      |                  |                                  |  9.0   | 26.0| 72.0| 3.0         | 12.0     | 131.5      | 136.5 |
 +-----------+------------------+----------------------------------+--------+-----+-----+-------------+----------+------------+-------+
  
Le projet doit :

* utiliser l'outil de gestion de version Git et un IDE de développement Python ;

* être structuré suivant l'arborescence indiquée ci-après

* pouvoir s'exécuter sur le système Linux des salle de TP lors de la démonstration finale ;

* être documenté :
        * description du projet au format restructuredText,
	* commentaires pertinents dans le code (si utile à la compréhension),
	* commentaires des fonctions développées


* comporter un répertoire de test où toutes les fonctions Python développées auront un code test unitaire

--------------------------------------------
Environnement de développement et dépôt GIT
--------------------------------------------

Le projet est rattaché à un dépôt GIT que vous aurez créé sur GitHub et à la livraison de vos codes informatiques. Le versionnement étant tracé et daté, il servira de **preuves** pour le travail.

-----------------------------------
Langages de scripting/programmation
-----------------------------------

Le projet doit utiliser :

* le langage de programmation **Python** (version > 3.7) pour les **codes sources** gérant la lecture, l'analyse, le traitement des données et la publication de leur analyse. 

* et/ou le langage de script **bash** pour les scripts permettant l'automatisation de certains traitements et de la publication des résultats  (vu en **R108-Base des systèmes d'exploitation**)



----------------------
Arborescence du projet
----------------------


Votre projet doit :

* être exécuté par le biais d'un script ``programme_projet.py``. Ce script reprendra la structure classique des programmes vue en **R107-Fondamentaux de la programmation** et décrite dans le formulaire Python. Il prendra d'éventuels paramètres en arguments spécifiés ci-après. 

* respecter l'arborescence suivante (``PROJETGitHUB`` désigne le répertoire auquel est rattaché votre projet et constitue la base du dépôt local Git) :

   .. code-block:: bash

      PROJETGitHUB
      ├── .git/
      ├── data/
      │   └── ...
      ├── docs/
      │     ├── build/
      │     │    └── html/
      │     └── source/ 
      │    	 ├── index.rst 
      │    	 ├── conf.py 
      │    	 ├── content/ 
      │    	 ├── _static/ 
      │          └── _templates/    
      ├── html/
      │   └── ...
      ├── __init__.py
      ├── nomprojet/
      │    └── nomprojet.py
      ├── tests/
      │   ├── __init__.py
      │   └── test_programme_projet.py  
      ├── .gitignore
      ├── AUTHORS
      │ 
      └── requirements.txt


      
   * ``.git`` le répertoire dédié à Git.
  
   * ``data`` le répertoire dédié à stocker différents fichiers de données récupérées et générées pour les besoin du projet.

   * ``docs`` le répertoire dédié à stocker la documentation du projet au format retructuredText (répertoire généré automatiquement par sphinx-build).

   * ``html`` répertoire contenant le site web statique de présentation des résultats

   * ``__init__.py`` fichier indiquant la version du projet :
	.. code-block:: python
			
		__version__ = '0.1.0'

   * ``nomprojet`` le répertoire dédié aux fichiers source Python développés lors du projet

   * ``tests`` le répertoire dédié aux tests unitaires des fonctions développées dans le projet

   * ``tests/__init__.py`` fichier vide

   * ``.gitignore`` le fichier permettant de configurer Git pour ne pas envoyer sur le dépôt distant les fichiers temporaires 

   * ``AUTHORS`` le fichier indiquant le nom des auteurs et de leurs coordonnées 
          
   * ``requirements.txt`` fichier texte décrivant la version de Python  utilisée et les dépendances du programme python (modules et version des modules Python)
   

.. warning::

   * Les fichiers : ``.gitignore`` commence avec un point.

.. note:: Vous pouvez :

   * ajouter au besoin autant de modules que nécessaires, pour structurer votre code, en les stockant à la racine du répertoire ``nomprojet``.


---------------------------------------------
Paramètres en argument du programme principal
---------------------------------------------
Votre programme devra prendre en argument les noms des 3 fichiers i-calendar des formations BUT1, DUT2 et LP ARM que vous aurez au préalable extraits de l'emploi du temps ainsi que le nom de l'enseignant et le répertoire dans lequel sera générée la page web :

 .. code-block:: bash
		 
	$ ./programme_projet.py --input-file ADECal_BUT1.ics ADECal_DUT2.ics ADECal_LPARM.ics --name nom_enseignant --output-dir ./../html/

--------------------------------------------
Documentation
--------------------------------------------  
* La documentation générale du projet devra être écrite au format restructuredText. Vous pourrez pour cela vous appuyer sur le logiciel `Sphinx <https://www.sphinx-doc.org/en/master/tutorial/getting-started.html>`_ ;

* Il conviendra d'ajouter des commentaires *doctrings* en début de fonction afin de :
     * préciser ce que fait la fonction,
     * d'indiquer son auteur, ses dates de création et de dernière modification,
     * décrire ses paramètres et le cas échéant leurs types,
     * décrire les bornes d'utilisation de paramètres pour un bon fonctionnement de la fonction et exceptions qui sont suceptibles d'être levées,
     * ce qu'elle retourne
     * donner un exemple d'utilisation

--------------------
Tests unitaires
--------------------

En vous inspirant du TP sur les fonctions, vous devrez écrire un code de test de chaque fonction développée dans le projet.
Celui-ci sera placé dans un programme Python du répertoire ``tests``.




