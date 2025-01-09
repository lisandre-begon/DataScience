import folium
import pandas as pd
from folium.plugins import HeatMap
from branca.element import Template, MacroElement
import branca.colormap as cm

def create_layer():
    print("Début création layer immatriculation")

    layer = folium.FeatureGroup(name="population")

    # Charger les données
    data = pd.read_csv("../../data/cities_population.csv")  # Remplacez par le chemin de votre fichier

    data = data.dropna(subset=["latitude", "longitude", "valeur_population"])

    max_population = data['valeur_population'].max()

    heat_data = [[row['latitude'], row['longitude'], row['valeur_population'] / max_population] for index, row in data.iterrows()]

    # Ajouter la Heatmap à la carte
    HeatMap(heat_data, radius=16, blur=15, max_zoom=1).add_to(layer)

    colormap = cm.LinearColormap(colors=['blue', 'green', 'yellow', 'red'],
                                vmin=data['valeur_population'].min(),
                                vmax=data['valeur_population'].max(),
                                caption='Échelle de population')

    print("Layer population crée")
    
    return (layer,colormap)




france_bounds = [[41.0, -5.0], [51.5, 9.0]]  # Sud-Ouest et Nord-Est

# Créer une carte centrée sur la France avec des limites
carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
carte.fit_bounds(france_bounds)

for el in create_layer():
    el.add_to(carte)

carte.save("heatmap_population.html")

print("La carte interactive a été générée")
