import sys
import os

import pandas as pd
import pendulum

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extract import get_coordinates, get_air_pollution_data


def merge_pollution_to_demographic():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../data/raw/Demographic_Data.csv')
    df = pd.read_csv(file_path)
    Geographic_With_Pollution = pd.read_csv(file_path) 
    Geographic_With_Pollution['Date'] = None 
    Geographic_With_Pollution['AQI'] = None
    Geographic_With_Pollution['CO'] = None
    Geographic_With_Pollution['NO'] = None
    Geographic_With_Pollution['NO2'] = None
    Geographic_With_Pollution['O3'] = None
    Geographic_With_Pollution['SO2'] = None
    Geographic_With_Pollution['PM2_5'] = None
    Geographic_With_Pollution['PM10'] = None
    Geographic_With_Pollution['NH3'] = None
    for index, row in df.iterrows():
        city = row['Location']
        if pd.notna(city):
            lat, lon = get_coordinates(city)
            if lat and lon:
                pollution_data = get_air_pollution_data(lat, lon)
                if pollution_data and 'list' in pollution_data:
                    components = pollution_data['list'][0]['components']
                    Geographic_With_Pollution.at[index, 'Date'] = pendulum.now().to_datetime_string()
                    Geographic_With_Pollution.at[index, 'AQI'] = pollution_data['list'][0]['main']['aqi']
                    Geographic_With_Pollution.at[index, 'CO'] = components['co']
                    Geographic_With_Pollution.at[index, 'NO'] = components['no']
                    Geographic_With_Pollution.at[index, 'NO2'] = components['no2']
                    Geographic_With_Pollution.at[index, 'O3'] = components['o3']
                    Geographic_With_Pollution.at[index, 'SO2'] = components['so2']
                    Geographic_With_Pollution.at[index, 'PM2_5'] = components['pm2_5']
                    Geographic_With_Pollution.at[index, 'PM10'] = components['pm10']
                    Geographic_With_Pollution.at[index, 'NH3'] = components['nh3']
    output_path = os.path.join(base_dir, '../data/raw/Pollution_With_Demographic.csv')
    Geographic_With_Pollution.to_csv(output_path, index=False)

def merge_pollution_to_geographic():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../data/raw/Geographic_Data.csv')
    df = pd.read_csv(file_path)
    Geographic_With_Pollution = pd.read_csv(file_path) 
    Geographic_With_Pollution['Date'] = None 
    Geographic_With_Pollution['AQI'] = None
    Geographic_With_Pollution['CO'] = None
    Geographic_With_Pollution['NO'] = None
    Geographic_With_Pollution['NO2'] = None
    Geographic_With_Pollution['O3'] = None
    Geographic_With_Pollution['SO2'] = None
    Geographic_With_Pollution['PM2_5'] = None
    Geographic_With_Pollution['PM10'] = None
    Geographic_With_Pollution['NH3'] = None
    for index, row in df.iterrows():
        city = row['Location']
        if pd.notna(city):
            lat, lon = get_coordinates(city)
            if lat and lon:
                pollution_data = get_air_pollution_data(lat, lon)
                if pollution_data and 'list' in pollution_data:
                    components = pollution_data['list'][0]['components']
                    Geographic_With_Pollution.at[index, 'Date'] = pendulum.now().to_datetime_string()
                    Geographic_With_Pollution.at[index, 'AQI'] = pollution_data['list'][0]['main']['aqi']
                    Geographic_With_Pollution.at[index, 'CO'] = components['co']
                    Geographic_With_Pollution.at[index, 'NO'] = components['no']
                    Geographic_With_Pollution.at[index, 'NO2'] = components['no2']
                    Geographic_With_Pollution.at[index, 'O3'] = components['o3']
                    Geographic_With_Pollution.at[index, 'SO2'] = components['so2']
                    Geographic_With_Pollution.at[index, 'PM2_5'] = components['pm2_5']
                    Geographic_With_Pollution.at[index, 'PM10'] = components['pm10']
                    Geographic_With_Pollution.at[index, 'NH3'] = components['nh3']
    output_path = os.path.join(base_dir, '../data/raw/Pollution_With_Geographic.csv')
    Geographic_With_Pollution.to_csv(output_path, index=False)