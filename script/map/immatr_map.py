import folium
import pandas as pd
from folium.plugins import HeatMap
import branca.colormap as cm
import os
import math

def rescale(value, min_val, max_val, nmin, nmax):
    if min_val == max_val:
        return nmin
    return nmin + ((value - min_val) / (max_val - min_val)) * (nmax - nmin)

def rescale_exp(value, min_val, max_val, nmin, nmax):
    if min_val == max_val:
        return nmin
    mid_val = (min_val + max_val) / 2
    if value <= mid_val:
        normalized = (value - min_val) / (mid_val - min_val)
        scaled = nmin + normalized * (nmax - nmin) * 0.3
    else:
        normalized = (value - mid_val) / (max_val - mid_val)
        scaled = nmin + 0.3 * (nmax - nmin) + (1 - math.exp(-3 * normalized)) * (nmax - nmin) * 0.7
    return scaled

def create_layer(data, year):
    print(f"Création des couches pour l'année {year}")

    # Filtrer les données pour l'année sélectionnée
    data_year = data[data['year'] <= year]

    layer1 = folium.FeatureGroup(name=f"Immatriculation VE {year}")
    layer2 = folium.FeatureGroup(name=f"% Immatriculation VE {year}")

    min_val = data_year["NB_VP_RECHARGEABLES_EL"].min()
    max_val = data_year["NB_VP_RECHARGEABLES_EL"].max()

    max_moy = (data_year["NB_VP_RECHARGEABLES_EL"] / data_year["NB_VP"]).max()
    min_moy = (data_year["NB_VP_RECHARGEABLES_EL"] / data_year["NB_VP"]).min()

    # Heatmap brute
    heat_data = [
        [row["latitude"], row["longitude"], rescale(row["NB_VP_RECHARGEABLES_EL"], min_val, max_val, 1, 20)]
        for _, row in data_year.iterrows()
    ]
    HeatMap(heat_data, radius=15, max_zoom=13, show=False).add_to(layer1)

    # Heatmap proportionnelle
    heat_data_pop = [
        [row["latitude"], row["longitude"], rescale_exp(row["NB_VP_RECHARGEABLES_EL"] / row["NB_VP"], 0, max_moy, 0, 1)]
        for _, row in data_year.iterrows()
    ]
    HeatMap(heat_data_pop, radius=15, max_zoom=13).add_to(layer2)

    # Échelles de couleur
    colormap1 = cm.LinearColormap(colors=['blue', 'green', 'yellow', 'orange', 'red'], vmin=min_val, vmax=max_val)
    colormap1.caption = f'Nombre de véhicules rechargeables électriques ({year})'

    colormap2 = cm.LinearColormap(colors=['blue', 'green', 'yellow', 'orange', 'red'], vmin=min_moy, vmax=max_moy)
    colormap2.caption = f'% de véhicules rechargeables électriques ({year})'

    return layer1, layer2, colormap1, colormap2

def generate_maps():
    # Charger les données
    data = pd.read_csv("../../data/processed/immatr_geo.csv", sep=",")

    # Créer un dossier de sortie
    output_dir = "immatr"
    os.makedirs(output_dir, exist_ok=True)

    # Obtenir les années uniques
    years = sorted(data['year'].unique())

    france_bounds = [[41.0, -5.0], [51.5, 9.0]]

    for year in years:
        # Créer la carte pour chaque année
        carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
        carte.fit_bounds(france_bounds)

        # Ajouter les couches de l'année
        for layer in create_layer(data, year):
            layer.add_to(carte)

        folium.LayerControl().add_to(carte)

        # Sauvegarder la carte dans un fichier HTML par année
        file_path = os.path.join(output_dir, f"immatr_map_{year}.html")
        carte.save(file_path)
        print(f"Carte sauvegardée : {file_path}")

from datetime import datetime

def get():
    # Charger les données
    data = pd.read_csv("../../data/processed/immatr_geo.csv", sep=",")
    print("coucou")

    # Obtenir les années uniques

    data['year'] = pd.to_datetime(data['DATE_ARRETE'], format="%Y-%m-%d", errors='coerce').dt.year
    
    years = sorted(data['year'].dropna().unique())

    france_bounds = [[41.0, -5.0], [51.5, 9.0]]
    res = []

    for year in years:

        # Ajouter les couches de l'année
        for layer in create_layer(data, year):
            res.append(layer)

    return res


# # Lancer la génération
# generate_maps()
