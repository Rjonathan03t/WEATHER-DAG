import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv('air_pollution_data_complete.csv')

# Afficher les premières lignes
print(df.head())

# Statistiques descriptives
print(df.describe())

# Visualisation des tendances
plt.figure(figsize=(10, 6))
plt.plot(df['Location'], df['AQI'], marker='o')
plt.title('AQI par Localisation')
plt.xlabel('Location')
plt.ylabel('AQI')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
