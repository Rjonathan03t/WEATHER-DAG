Projet d'Analyse de la Pollution de l'Air

Introduction

Ce projet analyse les niveaux de pollution de l'air en utilisant des données récupérées via l'API OpenWeatherMap. Les données sont combinées avec des informations démographiques et géographiques pour produire des visualisations interactives avec Looker Studio.

Prérequis:

Assurez-vous d'avoir Python installé sur votre machine. Vous aurez également besoin des bibliothèques suivantes :

    psycopg2-binary
    pyarrow
    seaborn
    pandas
    matplotlib

Installation

#cloner le repository

    git clone https://github.com/Rjonathan03t/WEATHER-DAG.git

#Créer un Environnement Virtuel

    python -m venv venv
    source venv/bin/activate

Installer les Dépendances

Créez un fichier requirements.txt avec le contenu suivant :

    psycopg2-binary
    pyarrow
    seaborn
    pandas
    matplotlib

Installez les dépendances avec :

    pip install -r requirements.txt

#Lancer le Programme

Exécuter le Script de Collecte
Le script récupère les données de pollution et les stocke en fichiers CSV locaux.

    python extract.py

#Configurer et Lancer Apache Airflow

Initialiser la Base de Données Airflow
bash

    airflow db init

Démarrer le Scheduler et le Web Server Airflow:

    airflow scheduler
    airflow webserver

Ou tapez juste:

    airflow standalone

#Planifier les Tâches avec Airflow

Accédez à l'interface web d'Airflow  à l'adresse:

     http://localhost:8080
et déclenchez les DAGs appropriés.


###Documentation

Pour des détails supplémentaires sur le développement et l'utilisation du projet, consultez la documentation fournie dans le repository

    [https://github.com/Rjonathan03t/WEATHER-DAG/blob/main/AIR%20POLLUTION.pdf].

Veuillez consulter le lien suivant pour voir le tableau de bord:

    https://lookerstudio.google.com/u/1/reporting/3d76ec8b-618a-4fd4-bc56-c2b07a60f3ff/page/p_wcad8vpzjd/edit

###Contributeurs

    Jonathan - STD 22105
    Toky - STD 22106
    Rojo Tiana - STD 22107

    
