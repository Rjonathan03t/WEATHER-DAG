import requests
import csv
import json

def get_air_pollution_data(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    headers = {'User-Agent': 'My Python App'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête : {e}")
        return None

def load_geographic_data(filename):
    geographic_data = {}
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            location = row['Location']
            geographic_data[location] = {
                'altitude': row['Altitude (m)'],
                'proximity': row['Proximity to Industry (km)']
            }
    return geographic_data

def load_demographic_data(filename):
    demographic_data = {}
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            location = row['Location']
            demographic_data[location] = {
                'population': row.get('Population', 'N/A'),
                'density': row.get('Density (people/km²)', 'N/A'),
                'urbanization': row.get('Urbanization (%)', 'N/A'),
                'average_income': row.get('Average Income (USD)', 'N/A'),
                'education_level': row.get("Education Level (%) with Bachelor's or higher", 'N/A')
            }
    return demographic_data

def save_data_to_csv(data, filename):
    if data:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'Location', 'Timestamp', 'AQI', 'CO', 'NO', 'NO2', 'O3', 'SO2', 'PM2.5', 'PM10', 'NH3',
                'Altitude (m)', 'Proximity to Industry (km)', 'Population', 'Density (people/km²)',
                'Urbanization (%)', 'Average Income (USD)', 'Education Level (%)'
            ])
            for entry in data:
                writer.writerow([
                    entry.get('Location', 'N/A'),
                    entry.get('Timestamp', 'N/A'),
                    entry.get('AQI', 'N/A'),
                    entry.get('CO', 'N/A'),
                    entry.get('NO', 'N/A'),
                    entry.get('NO2', 'N/A'),
                    entry.get('O3', 'N/A'),
                    entry.get('SO2', 'N/A'),
                    entry.get('PM2.5', 'N/A'),
                    entry.get('PM10', 'N/A'),
                    entry.get('NH3', 'N/A'),
                    entry.get('Altitude (m)', 'N/A'),
                    entry.get('Proximity to Industry (km)', 'N/A'),
                    entry.get('Population', 'N/A'),
                    entry.get('Density (people/km²)', 'N/A'),
                    entry.get('Urbanization (%)', 'N/A'),
                    entry.get('Average Income (USD)', 'N/A'),
                    entry.get('Education Level (%)', 'N/A')
                ])

def main():
    api_key = '4cbf2ec40fa4073d64fa831d6efcef60'  # Remplacez par votre clé API valide
    geographic_filename = 'Geographic_Data.csv'
    demographic_filename = 'Demographic_Data.csv'
    
    geographic_data = load_geographic_data(geographic_filename)
    demographic_data = load_demographic_data(demographic_filename)
    
    all_data = []
    for location, geo_info in geographic_data.items():
        # Utiliser des coordonnées fictives si pas disponibles
        latitude, longitude = '0', '0'  # Valeurs par défaut si pas de coordonnées réelles
        air_pollution_data = get_air_pollution_data(latitude, longitude, api_key)
        
        if air_pollution_data:
            entry = {
                'Location': location,
                'Timestamp': air_pollution_data['list'][0].get('dt', 'N/A'),
                'AQI': air_pollution_data['list'][0]['main'].get('aqi', 'N/A'),
                'CO': air_pollution_data['list'][0]['components'].get('co', 'N/A'),
                'NO': air_pollution_data['list'][0]['components'].get('no', 'N/A'),
                'NO2': air_pollution_data['list'][0]['components'].get('no2', 'N/A'),
                'O3': air_pollution_data['list'][0]['components'].get('o3', 'N/A'),
                'SO2': air_pollution_data['list'][0]['components'].get('so2', 'N/A'),
                'PM2.5': air_pollution_data['list'][0]['components'].get('pm2_5', 'N/A'),
                'PM10': air_pollution_data['list'][0]['components'].get('pm10', 'N/A'),
                'NH3': air_pollution_data['list'][0]['components'].get('nh3', 'N/A'),
                'Altitude (m)': geo_info['altitude'],
                'Proximity to Industry (km)': geo_info['proximity'],
                'Population': demographic_data.get(location, {}).get('population', 'N/A'),
                'Density (people/km²)': demographic_data.get(location, {}).get('density', 'N/A'),
                'Urbanization (%)': demographic_data.get(location, {}).get('urbanization', 'N/A'),
                'Average Income (USD)': demographic_data.get(location, {}).get('average_income', 'N/A'),
                'Education Level (%)': demographic_data.get(location, {}).get('education_level', 'N/A')
            }
            all_data.append(entry)
    
    save_data_to_csv(all_data, 'air_pollution_data_complete.csv')

if __name__ == "__main__":
    main()
