import pandas as pd
import os

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../data/raw/pollution.csv')
    df = pd.read_csv(file_path)
    df.to_csv(file_path, index=False)
