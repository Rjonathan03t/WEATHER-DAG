import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

pollution_file_path = '/home/artiana/airflow/WEATHER-DAG/data/raw/pollution.csv'
demographic_file_path = '/home/artiana/airflow/WEATHER-DAG/data/raw/Demographic_Data.csv'

# Charger les données depuis les fichiers CSV
df_pollution = pd.read_csv(pollution_file_path)
df_demographic = pd.read_csv(demographic_file_path)

# Fusionner les données de pollution avec les données démographiques sur la colonne 'Location'
df = pd.merge(df_pollution, df_demographic, on='Location')

# 1. Analyse des Corrélations
def analyze_correlations(df):
    # Sélectionner uniquement les colonnes numériques
    numeric_df = df.select_dtypes(include=['number'])
    
    # Calculer les corrélations
    correlations = numeric_df.corr()
    

    print("Corrélations entre les niveaux de pollution et les facteurs démographiques et géographiques:")
    print(correlations)
    
    # Créer une heatmap des corrélations
    plt.figure(figsize=(14, 10))
    sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Corrélations entre les niveaux de pollution et les facteurs démographiques et géographiques')
    plt.show()



if __name__ == "__main__":
    analyze_correlations(df)
 
