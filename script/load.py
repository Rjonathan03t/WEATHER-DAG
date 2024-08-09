import pandas as pd
import os

def load_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pollutiong_file_path = os.path.join(base_dir, '../data/raw/Pollution_With_Geographic.csv')
    pollutiong = pd.read_csv(pollutiong_file_path)
    pollutiong.to_csv(pollutiong_file_path, index=False)
    pollutiond_file_path = os.path.join(base_dir, '../data/raw/Pollution_With_Demographic.csv')
    pollutiond = pd.read_csv(pollutiond_file_path)
    pollutiond.to_csv(pollutiond_file_path, index=False)
