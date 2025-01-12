import folium
import pandas as pd
from folium.plugins import HeatMap
from branca.element import Template, MacroElement
import branca.colormap as cm
import random

def create_layer():
    print("Début création layer flux routiers")
    layer = folium.FeatureGroup(name="flux routiers")

    data = pd.read_csv("../../data/processed/TMJA2019_geo.csv", sep=";")  # Remplacez par le chemin de votre fichier

    data = data.dropna(subset=["latitudeD", "longitudeD", "latitudeF", "longitudeF", "TMJA"])

    for _, row in data.iterrows():
        folium.PolyLine(
            locations=[  # Liste des coordonnées : départ -> arrivée
                [row["latitudeD"], row["longitudeD"]],
                [row["latitudeF"], row["longitudeF"]]
            ],
            color="blue",  # Couleur de la ligne
            weight=row["TMJA"] / 7500,  # Ajuster l'épaisseur selon le trafic
            opacity=0.8,  # Opacité de la ligne
            tooltip=f'Trafic: {row["TMJA"]}'
        ).add_to(layer)

    print("Layer flux routiers crée")

    return layer

france_bounds = [[41.0, -5.0], [51.5, 9.0]]

carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
carte.fit_bounds(france_bounds)

create_layer().add_to(carte)

carte.save("carte_lignes_trafic.html")
print("Carte générée avec des lignes de trafic : carte_lignes_trafic.html")