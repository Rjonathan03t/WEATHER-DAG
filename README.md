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
