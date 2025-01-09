import pandas as pd
from pyproj import Transformer

# Charger les données
csv1 = pd.read_csv("../../data/raw/TMJA2019.csv", sep=";")
# Ajouter des colonnes pour les coordonnées géographiques
csv1["latitudeD"] = None
csv1["longitudeD"] = None
csv1["latitudeF"] = None
csv1["longitudeF"] = None

# Créer un transformateur Lambert 93 -> WGS 84
transformer = Transformer.from_crs("EPSG:2154", "EPSG:4326")

# print(type(csv1["xD"][0]))
# print(float(csv1["xD"][0].replace(",", ".")))
for el in range(len(csv1["xD"])):
    x = float(csv1["xD"][el].replace(",", "."))
    y = float(csv1["yD"][el].replace(",", "."))
    # csv1["xD"][el], csv1["yD"][el] = transformer.transform(x, y)
    lat, lon = transformer.transform(x, y)
    print(lat,  " --- : --- ", lon)
    csv1["latitudeD"][el] = lat
    csv1["longitudeD"][el] = lon

# Supprimer les colonnes xD et yD
csv1 = csv1.drop(columns=["xD", "yD"])

for el in range(len(csv1["xF"])):
    x = float(csv1["xF"][el].replace(",", "."))
    y = float(csv1["yF"][el].replace(",", "."))
    lat, lon = transformer.transform(x, y)
    print(lat,  " --- : --- ", lon)
    csv1["latitudeF"][el] = lat
    csv1["longitudeF"][el] = lon

# Supprimer les colonnes xD et yD
csv1 = csv1.drop(columns=["xF", "yF"])

# Enregistrer les données avec les nouvelles colonnes dans un nouveau fichier CSV
csv1.to_csv("../../data/processed/TMJA2019_geo.csv", sep=";", index=False)

print("done")
