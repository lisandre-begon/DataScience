import pandas as pd
from datetime import datetime
# from pyproj import Transformer
# import ast

data = pd.read_csv("../../../data/processed/IRVE_geo.csv", sep=",")

grouped = data.groupby(['latitude', 'longitude']).size().reset_index(name='count')

print(data['date_mise_en_service'])

#pour tout les elements de la colonne date_mise_en_service
years = []
for i in range(len(data['date_mise_en_service'])):
    if(str(data['date_mise_en_service'][i]) != "nan"):
        date_object = datetime.strptime(str(data['date_mise_en_service'][i]), "%Y-%m-%d")
        year = date_object.year
        if year not in years:
            years.append(year)
print("years :")
print(years)
        
print("Nouveau fichier CSV généré : output.csv")

