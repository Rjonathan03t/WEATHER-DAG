import pandas as pd

 #chacun change le path localement
basePath = '/home/nathan/airflow/weather/dags/data/raw/'

def load_data():
    df = pd.read_csv(f'{basePath}pollution.csv')
    df.to_csv(f'{basePath}pollution.csv', index=False)
