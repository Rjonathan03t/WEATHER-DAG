import sys
import os

import pandas as pd

# Ajouter le répertoire de script au chemin
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extract import get_coordinates, get_air_pollution_data


def transform_data():
   
    # Définir le chemin relatif basé sur le répertoire du script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../data/raw/Geographic_Data.csv')
    df = pd.read_csv(file_path)
    df['AQI'] = None
    df['CO'] = None
    df['NO'] = None
    df['SO2'] = None
    df['PM2_5'] = None
    df['PM10'] = None
    df['NH3'] = None
    for index, row in df.iterrows():
        city = row['Location']
        if pd.notna(city):
            lat, lon = get_coordinates(city)
            if lat and lon:
                pollution_data = get_air_pollution_data(lat, lon)
                if pollution_data and 'list' in pollution_data:
                    components = pollution_data['list'][0]['components']
                    df.at[index, 'AQI'] = pollution_data['list'][0]['main']['aqi']
                    df.at[index, 'CO'] = components['co']
                    df.at[index, 'NO'] = components['no']
                    df.at[index, 'NO2'] = components['no2']
                    df.at[index, 'O3'] = components['o3']
                    df.at[index, 'SO2'] = components['so2']
                    df.at[index, 'PM2_5'] = components['pm2_5']
                    df.at[index, 'PM10'] = components['pm10']
                    df.at[index, 'NH3'] = components['nh3']  
    output_path = os.path.join(base_dir, '../data/raw/pollution.csv')
    df.to_csv(output_path, index=False)