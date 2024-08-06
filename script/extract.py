import pandas as pd
import requests

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

def extract_data(file_path):
    df = pd.read_csv(file_path)
    df.to_csv('/tmp/geo_temp.csv', index=False)
