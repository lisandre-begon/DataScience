import folium
import pandas as pd
from folium.plugins import HeatMap
from branca.element import Template, MacroElement
import branca.colormap as cm
import random
from folium.plugins import MarkerCluster

def create_layer():
    print("Création de la couche des bornes")
    tabLayer = []

    layer = folium.FeatureGroup(name="bornes")

    data = pd.read_csv("../../data/processed/grouped_borne.csv", sep=",")  # Remplacez par le chemin de votre fichier

    # Créer une carte centrée sur la France

    marker_cluster = MarkerCluster()

    # Ajouter les points au cluster
    for _, row in data.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=row["count"] / 10,
            color="blue",
            fill=True,
            fill_color="blue",
            fill_opacity=0.6,
            tooltip=f'Nombre de bornes: {row["count"]}'
        ).add_to(marker_cluster)

    # Ajouter le cluster à la carte
    marker_cluster.add_to(layer)
    print("Couche des bornes créée")
    return layer

france_bounds = [[41.0, -5.0], [51.5, 9.0]]  # Sud-Ouest et Nord-Est

# Créer une carte centrée sur la France avec des limites
carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
carte.fit_bounds(france_bounds)
create_layer().add_to(carte)

carte.save("carte_bornes.html")
print("Carte générée avec des bornes : carte_bornes.html")