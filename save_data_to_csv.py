import csv

def save_data_to_csv(data, filename):
    if data and 'list' in data:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow([
                'Timestamp', 'AQI', 'CO', 'NO', 'NO2', 'O3', 'SO2', 'PM2.5', 'PM10', 'NH3'
            ])
            
            for item in data['list']:
                writer.writerow([
                    item['dt'],
                    item['main']['aqi'],
                    item['components'].get('co', 'N/A'),
                    item['components'].get('no', 'N/A'),
                    item['components'].get('no2', 'N/A'),
                    item['components'].get('o3', 'N/A'),
                    item['components'].get('so2', 'N/A'),
                    item['components'].get('pm2_5', 'N/A'),
                    item['components'].get('pm10', 'N/A'),
                    item['components'].get('nh3', 'N/A')
                ])
