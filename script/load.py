import pandas as pd

def load_data():
    df = pd.read_csv('/tmp/geo_transformed_temp.csv')
    df.to_csv('/tmp/geographie_pollution.csv', index=False)
