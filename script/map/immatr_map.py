import folium
import pandas as pd
from folium.plugins import HeatMap
from branca.element import Template, MacroElement
import branca.colormap as cm
import random

def rescale(value, min_val, max_val, nmin, nmax):
    if min_val == max_val:
        raise ValueError("min_val et max_val ne doivent pas être identiques (division par zéro).")

    # Rééchelonnement
    scaled_value = nmin + ((value - min_val) / (max_val - min_val)) * (nmax - nmin)
    return scaled_value

import math

def rescale_exp(value, min_val, max_val, nmin, nmax):
    if min_val == max_val:
        raise ValueError("min_val et max_val ne doivent pas être identiques (division par zéro).")

    # Calcul de la moyenne
    mid_val = (min_val + max_val) / 2

    # Normalisation de la valeur entre 0 et 1
    if value <= mid_val:
        # En dessous de la moyenne : croissance lente (logarithmique ou aplatie)
        normalized = (value - min_val) / (mid_val - min_val)
        scaled = nmin + normalized * (nmax - nmin) * 0.3  # 0.3 pour rendre la croissance faible
    else:
        # Au-dessus de la moyenne : croissance exponentielle
        normalized = (value - mid_val) / (max_val - mid_val)
        scaled = nmin + 0.3 * (nmax - nmin) + (1 - math.exp(-3 * normalized)) * (nmax - nmin) * 0.7

    return scaled

def create_layer():
    print("Début création layer immatriculation")

    layer1 = folium.FeatureGroup(name="immatriculation VE")
    layer2 = folium.FeatureGroup(name="immatriculation % VE")

    data = pd.read_csv("../../data/processed/immatr_geo.csv", sep=",")  # Remplacez par le chemin de votre fichier

    min_val = data["NB_VP_RECHARGEABLES_EL"].min()
    max_val = data["NB_VP_RECHARGEABLES_EL"].max()

    max_moy = (data["NB_VP_RECHARGEABLES_EL"] / data["NB_VP"]).max()
    min_moy = (data["NB_VP_RECHARGEABLES_EL"] / data["NB_VP"]).min()

    heat_data = [
        [
            row["latitude"],
            row["longitude"],
            rescale(row["NB_VP_RECHARGEABLES_EL"], min_val, max_val, 1, 20)
        ]
        for _, row in data.iterrows()
    ]
    HeatMap(heat_data, radius=15, max_zoom=13).add_to(layer1)

    heat_data_pop = [
        [
            row["latitude"],
            row["longitude"],
            rescale_exp(row["NB_VP_RECHARGEABLES_EL"] / row["NB_VP"], 0, max_moy, 0, 1)
        ]
        for _, row in data.iterrows()
    ]
    HeatMap(heat_data_pop, radius=15, max_zoom=13, name="% voiture éléctrique").add_to(layer2)

    # Ajouter une échelle des couleurs
    colormap1 = cm.LinearColormap(colors=['blue', 'green', 'yellow', 'orange', 'red'], vmin=min_val, vmax=max_val)
    colormap1.caption = 'Nombre de véhicules rechargeables électriques'

    colormap2 = cm.LinearColormap(colors=['blue', 'green', 'yellow', 'orange', 'red'], vmin=min_moy, vmax=max_moy)
    colormap2.caption = '% de véhicules rechargeables électriques'
    print("Layer immatriculation crée")

    return (layer1,layer2, colormap1, colormap2)

france_bounds = [[41.0, -5.0], [51.5, 9.0]]  # Sud-Ouest et Nord-Est

# Créer une carte centrée sur la France avec des limites
carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
carte.fit_bounds(france_bounds)

for el in create_layer():
    el.add_to(carte)

folium.LayerControl().add_to(carte)

carte.save("immatr_map.html")
print("Carte générée avec des bornes : immatr_map.html")