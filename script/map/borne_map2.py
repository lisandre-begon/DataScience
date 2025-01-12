import folium
import pandas as pd
from folium.plugins import HeatMap
from branca.element import Template, MacroElement
import branca.colormap as cm
import random
from folium.plugins import MarkerCluster
import json
from folium.plugins import TimestampedGeoJson
from folium import GeoJson
from shapely.geometry import Point
from sklearn.cluster import DBSCAN
import geopandas as gpd
import json

def create_layer():
    print("Création de la couche des bornes")

    data = pd.read_csv("../../data/processed/grouped_borne.csv", sep=",")  # Remplacez par le chemin de votre fichier

    features = []

    for _, row in data.iterrows():
        if pd.notna(row['latitude']) and pd.notna(row['longitude']) and pd.notna(row['year']):
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [row['longitude'], row['latitude']]
                },
                "properties": {
                    "time": f"{int(row['year'])}-01-01T00:00:00Z",  # L'year de mise en service
                    "popup": f"Année: {row['year']}<br>Nombre de bornes: {row['count']}"
                }
            }
            features.append(feature)
        else:
            print(f"Ligne ignorée: Latitude ou Longitude ou Year manquant - {row}")

    # Créer un objet GeoJSON
    if features:
        geojson_data = {
            "type": "FeatureCollection",
            "features": features
        }

        with open("bornes.geojson", "w") as f:
            json.dump(geojson_data, f)
        print("GeoJSON créé avec succès.")
    else:
        print("Aucune donnée valide pour créer un GeoJSON.")

    layer = TimestampedGeoJson(
        geojson_data,
        period='PT1H',  # Période de l'animation, ici une heure par an
        duration='1s',  # Durée de chaque étape dans l'animation
        auto_play=True,
        loop=True,
        max_speed=1
    )

    for feature in geojson_data['features']:
        if 'geometry' not in feature or 'coordinates' not in feature['geometry']:
            print("Attention, géométrie manquante ou invalide pour cette feature :", feature)

    with open("bornes.geojson", "w") as f:
        json.dump(geojson_data, f)
        
    print("Couche des bornes créée")
    return layer

france_bounds = [[41.0, -5.0], [51.5, 9.0]]  # Sud-Ouest et Nord-Est

# Créer une carte centrée sur la France avec des limites
carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
carte.fit_bounds(france_bounds)
GeoJson(create_layer(), name='GeoJSON').add_to(carte)

carte.save("carte_bornes.html")
print("Carte générée avec des bornes : carte_bornes.html")