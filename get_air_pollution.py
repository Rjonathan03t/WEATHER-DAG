import requests
import json

def get_air_pollution_data(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    headers = {'User-Agent': 'My Python App'}  # Ajoutez un User-Agent

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for error HTTP status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
        return None

def print_data(data):
    if data:
        print(json.dumps(data, indent=4))

# Exemple pour Paris
latitude = 48.8566  
longitude = 2.3522  


api_key = '4cbf2ec40fa4073d64fa831d6efcef60'

data = get_air_pollution_data(latitude, longitude, api_key)
print_data(data)
