import pandas as pd
from script.extract import get_coordinates, get_air_pollution_data

def transform_data():
    df = pd.read_csv('/tmp/geo_temp.csv')  # Lire le fichier temporaire
    df['AQI'] = None
    df['CO'] = None
    df['NO'] = None
    df['NO2'] = None
    df['O3'] = None
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

    df.to_csv('/tmp/geo_transformed_temp.csv', index=False)  # Enregistrer temporairement le fichier transformé
