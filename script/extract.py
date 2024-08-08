import pandas as pd
import requests
import os

api_key = "4cbf2ec40fa4073d64fa831d6efcef60"

def get_coordinates(city):
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(geocode_url)
    data = response.json()
    if data:
        return data[0]['lat'], data[0]['lon']
    else:
        return None, None

def get_air_pollution_data(lat, lon):
    pollution_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(pollution_url)
    return response.json()

def extract_data():
    # Définir le chemin relatif basé sur le répertoire du script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../data/raw/Geographic_Data.csv')
    return pd.read_csv(file_path)
