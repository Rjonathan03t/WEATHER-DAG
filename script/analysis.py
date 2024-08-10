import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
pollution_file_path = os.path.join(base_dir, '../data/raw/Pollution_With_Demographic.csv')
demographic_file_path = os.path.join(base_dir, '../data/raw/Pollution_With_Geographic.csv')

df_pollution = pd.read_csv(pollution_file_path)
df_demographic = pd.read_csv(demographic_file_path)

# Fusionner les données de pollution avec les données démographiques sur la colonne 'Location'
df = pd.merge(df_pollution, df_demographic, on='Location')

def analyze_correlations(df):
    numeric_df = df.select_dtypes(include=['number'])
    
    correlations = numeric_df.corr()

    print("Corrélations entre les niveaux de pollution et les facteurs démographiques et géographiques:")
    print(correlations)

    plt.figure(figsize=(14, 10))
    sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Corrélations entre les niveaux de pollution et les facteurs démographiques et géographiques')
    plt.show()

def plot_aqi_vs_altitude(df):
    aqi_col = 'AQI_x'  # ou 'AQI_y', selon ce qui est affiché dans df.columns
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Altitude (m)', y=aqi_col)
    plt.title('Tendance du AQI en fonction de l\'altitude')
    plt.xlabel('Altitude (m)')
    plt.ylabel(aqi_col)
    plt.show()

def plot_aqi_vs_proximity(df):
    aqi_col = 'AQI_x'  # ou 'AQI_y', selon ce qui est affiché dans df.columns
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Proximity to Industry (km)', y=aqi_col)
    plt.title('Tendance du AQI en fonction de la proximité des industries')
    plt.xlabel('Proximité aux industries (km)')
    plt.ylabel(aqi_col)
    plt.show()

def plot_aqi_vs_density(df):
    aqi_col = 'AQI_x'  # ou 'AQI_y', selon ce qui est affiché dans df.columns
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Density (people/km²)', y=aqi_col)
    plt.title('Tendance du AQI en fonction de la densité de population')
    plt.xlabel('Densité (personnes/km²)')
    plt.ylabel(aqi_col)
    plt.show()

def plot_aqi_vs_income(df):
    aqi_col = 'AQI_x'  # ou 'AQI_y', selon ce qui est affiché dans df.columns
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Average Income (USD)', y=aqi_col)
    plt.title('Tendance du AQI en fonction du revenu moyen')
    plt.xlabel('Revenu moyen (USD)')
    plt.ylabel(aqi_col)
    plt.show()

if __name__ == "__main__":
    analyze_correlations(df)
    plot_aqi_vs_altitude(df)
    plot_aqi_vs_proximity(df)
    plot_aqi_vs_density(df)
    plot_aqi_vs_income(df)
