import pandas as pd
from datetime import datetime
# from pyproj import Transformer
# import ast

data = pd.read_csv("../../../data/processed/IRVE_geo.csv", sep=",")

data['year'] = pd.to_datetime(data['date_mise_en_service'], format='%Y-%m-%d', errors='coerce').dt.year.astype(int, errors='ignore')

grouped = data.groupby(['latitude', 'longitude', 'year']).size().reset_index(name='count')

num_elements = len(grouped)
print(f"Number of elements in the CSV file: {num_elements}")

initial_count = len(grouped)
grouped = grouped.dropna(subset=['year'])
final_count = len(grouped)
print(f"Number of rows removed: {initial_count - final_count}")

grouped.to_csv("../../../data/processed/grouped_borne.csv", index=False)

