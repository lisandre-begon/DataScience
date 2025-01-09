import pandas as pd
from pyproj import Transformer
import ast


# Charger les données
csv1 = pd.read_csv("../../../data/raw/IRVE.csv", sep=",")
# Ajouter des colonnes pour les coordonnées géographiques
csv1["latitude"] = None
csv1["longitude"] = None

transformer = Transformer.from_crs("EPSG:2154", "EPSG:4326")

for i in range(len(csv1["coordonneesXY"])):
    el = csv1["coordonneesXY"][i]
    el = ast.literal_eval(el)
    lat = el[1]
    lon = el[0]

    csv1["latitude"][i] = lat
    csv1["longitude"][i] = lon

# Supprimer les colonnes xD et yD
csv1 = csv1.drop(columns=["coordonneesXY"])

# Enregistrer les données avec les nouvelles colonnes dans un nouveau fichier CSV
csv1.to_csv("../../../data/processed/IRVE_geo.csv", sep=",", index=False)

print("done")
