import folium
import pandas as pd
from folium.plugins import HeatMap
import os

import routes_map

def create_and_save_heatmaps():
    print("Création des Heatmaps par année...")

    # Charger les données
    data = pd.read_csv("../../data/processed/grouped_borne.csv", sep=",")  # Remplacez par le chemin correct

    # Créer un dossier pour stocker les cartes
    output_dir = "cartes_bornes_habitants"
    os.makedirs(output_dir, exist_ok=True)

    # Récupération des années uniques
    years = sorted(data['year'].unique())
    print("Années disponibles :", years)

    # Définir les limites de la France
    france_bounds = [[41.0, -5.0], [51.5, 9.0]]

    # Création et sauvegarde de la Heatmap pour chaque année
    for year in years:
        print(f"Création de la Heatmap pour l'année {year}...")

        # Préparation des données de la Heatmap
        heat_data = []
        max_count = data['count'].max()

        for _, row in data[data['year'] <= year].iterrows():
            heat_data.extend([
                [row["latitude"], row["longitude"]] for _ in range(int(row["count"]))]
            )

        # Créer la carte
        carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
        carte.fit_bounds(france_bounds)

        # Ajouter la Heatmap
        HeatMap(heat_data, radius=15, blur=15, max_zoom=10, min_opacity=0.4).add_to(carte)

        # Sauvegarder la carte pour l'année en cours
        file_path = os.path.join(output_dir, f"carte_{year}.html")
        carte.save(file_path)
        print(f"Carte sauvegardée : {file_path}")

    print("Toutes les cartes Heatmap ont été générées et sauvegardées.")

def get():
    res = []
    print("Création des Heatmaps par année...")

    # Charger les données
    data = pd.read_csv("../../data/processed/grouped_borne.csv", sep=",")  # Remplacez par le chemin correct

    # Créer un dossier pour stocker les cartes
    output_dir = "bornes"
    os.makedirs(output_dir, exist_ok=True)

    # Récupération des années uniques
    years = sorted(data['year'].unique())
    print("Années disponibles :", years)

    # Définir les limites de la France
    france_bounds = [[41.0, -5.0], [51.5, 9.0]]

    # Création et sauvegarde de la Heatmap pour chaque année
    for year in years:
        print(f"Création de la Heatmap pour l'année {year}...")

        # Préparation des données de la Heatmap
        heat_data = []
        max_count = data['count'].max()

        for _, row in data[data['year'] <= year].iterrows():
            heat_data.extend([
                [row["latitude"], row["longitude"]] for _ in range(int(row["count"]))]
            )

        carte = folium.FeatureGroup(name=f"Heatmap {year}")


        # Ajouter la Heatmap
        HeatMap(heat_data, radius=15, blur=15, max_zoom=10, min_opacity=0.4).add_to(carte)
        res.append(carte)
    return res
        
# Exécuter la fonction
# create_and_save_heatmaps()
