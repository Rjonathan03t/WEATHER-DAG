import pandas as pd

def load_data():
    df = pd.read_csv('/home/nathan/airflow/weather/dags/data/raw/pollution.csv')
    df.to_csv('/home/nathan/airflow/weather/dags/data/raw/pollution.csv', index=False)
