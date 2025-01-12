import folium
import pandas as pd
from folium.plugins import HeatMap

def create_layer():
    print("Création de la couche Heatmap des bornes")

    # Charger les données
    data = pd.read_csv("../../data/processed/grouped_borne.csv", sep=",")  # Remplacez par le chemin de votre fichier

    # Récupération des années uniques
    years = data['year'].unique()
    print("Années disponibles dans les données:", years)

    layer_tab = []

    # Création d'une HeatMap par année
    for y in years:
        heat_data = []
        max_count = data['count'].max()

        # Récupérer les coordonnées pondérées par le nombre de bornes
        for _, row in data[data['year'] < y].iterrows():
            heat_data.append([
                row["latitude"],
                row["longitude"],
                row["count"]/max_count  # Poids basé sur le nombre de bornes
            ])

        # Création de la couche HeatMap
        heat_layer = folium.FeatureGroup(name=f"Heatmap {y}", show=False)
        HeatMap(heat_data, radius=15, blur=15, max_zoom=10, min_opacity=0.4).add_to(heat_layer)
        layer_tab.append(heat_layer)

    print("Couche Heatmap créée")
    return layer_tab

# Définir les limites de la France
france_bounds = [[41.0, -5.0], [51.5, 9.0]]

# Créer la carte centrée sur la France
carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
carte.fit_bounds(france_bounds)

# Ajouter la couche Heatmap
res = create_layer()
if isinstance(res, list):
    for el in res:
        el.add_to(carte)
else:
    res.add_to(carte)

# Ajouter le contrôle des couches
folium.LayerControl().add_to(carte)

# Sauvegarder la carte
carte.save("carte_bornes_heatmap.html")
print("Carte Heatmap générée : carte_bornes_heatmap.html")
