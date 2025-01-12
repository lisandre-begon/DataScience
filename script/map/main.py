import folium
import pandas as pd
from folium.plugins import HeatMap
from branca.element import Template, MacroElement
import branca.colormap as cm

import immatr_map
import population_map
import routes_map
import borne_map

def is_tuple(obj):
    return isinstance(obj, tuple)

france_bounds = [[41.0, -5.0], [51.5, 9.0]]  # Sud-Ouest et Nord-Est

# Créer une carte centrée sur la France avec des limites
carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
carte.fit_bounds(france_bounds)

res = borne_map.create_layer()
if(is_tuple(res)):
    for el in res:
        el.add_to(carte)
else:
    res.add_to(carte)

res = immatr_map.create_layer()
if(is_tuple(res)):
    for el in res:
        el.add_to(carte)
else:
    res.add_to(carte)

res = population_map.create_layer()
if(is_tuple(res)):
    for el in res:
        el.add_to(carte)
else:
    res.add_to(carte)

res = routes_map.create_layer()
if(is_tuple(res)):
    for el in res:
        el.add_to(carte)
else:
    res.add_to(carte)

folium.LayerControl().add_to(carte)

carte.save("main.html")
print("Carte finale générée : main.html")