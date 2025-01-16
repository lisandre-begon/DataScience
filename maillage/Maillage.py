import random
import geopandas as gpd
from shapely.geometry import Polygon
from typing import List
import folium
from folium.plugins import HeatMap
import Cell
import pandas as pd

max_data = 0
min_data = 10

def generate_france_grid(fonction, cell_size: float) -> List[Cell.Cell]:
    global max_data
    global min_data
    """
    Génère un maillage de la France avec des cellules de taille spécifiée et des taux aléatoires.
    
    :param cell_size: Taille des cellules (en degrés)
    :return: Liste des cellules couvrant la France
    """
    # Limites géographiques de la France métropolitaine
    min_lat, max_lat = 41.0, 51.5   # Latitude
    min_lon, max_lon = -5.0, 9.5    # Longitude

    grid_cells = []

    total = 0

    lat = min_lat
    while lat < max_lat:
        lon = min_lon
        while lon < max_lon:
            random_data = fonction(lat, lon, cell_size)
            if(random_data[0] != 0):
                cell = Cell.Cell(latitude=lat + cell_size / 2,
                            longitude=lon + cell_size / 2,
                            size=cell_size,
                            data=random_data[0],
                            data_size=random_data[1])
                total += random_data[1]
                if(random_data[0] > max_data):
                    max_data = random_data[0]
                if(random_data[0] < min_data):
                    min_data = random_data[0]
                #print("Total data_size : "+str(total))

                grid_cells.append(cell)
            lon += cell_size
        lat += cell_size
        taux = 1 - (max_lat - lat)/(max_lat - min_lat)
        print(taux* 100, "%")
    

    return grid_cells

def maillage_bornes(lat: float, lon: float, cell_size : float) -> float:
    df = pd.read_csv("../data/processed/grouped_borne.csv", low_memory=False)
    df2 = pd.read_csv("../data/cities_population.csv", low_memory=False)
    
    lat_min, lat_max = lat, lat + cell_size # Plage de latitude
    lon_min, lon_max = lon, lon + cell_size    # Plage de longitude

    """
    Fonction de génération de données pour les bornes de recharge.
    
    :param lat: Latitude de la cellule
    :param lon: Longitude de la cellule
    :return: Nombre de bornes de recharge
    """
    filtre = (df['latitude'].between(lat_min, lat_max)) & (df['longitude'].between(lon_min, lon_max))
    filtre2 = (df2['latitude'].between(lat_min, lat_max)) & (df2['longitude'].between(lon_min, lon_max))

    numerateur = df.loc[filtre, 'count'].sum()
    denominateur = df2.loc[filtre2, 'valeur_population'].sum()

    # Vérifier que le dénominateur est valide (ni zéro, ni NaN, ni infini)
    if pd.notna(denominateur) and denominateur != 0 and not denominateur == float('inf'):
        resultat = float(numerateur / denominateur) * 100000
        #print(f"Division valide : numerateur = {numerateur}, denominateur = {denominateur}, resultat = {resultat}")
    else:
        resultat = 0  
        #print(f"⚠️ Division invalide : denominateur = {denominateur}")

    return (resultat, denominateur)

def maillage_VE(lat: float, lon: float, cell_size : float) -> float:




    df = pd.read_csv("../data/processed/grouped_borne.csv", low_memory=False)
    df2 = pd.read_csv("../data/processed/immatr_geo.csv", low_memory=False)
    
    lat_min, lat_max = lat, lat + cell_size # Plage de latitude
    lon_min, lon_max = lon, lon + cell_size    # Plage de longitude

    """
    Fonction de génération de données pour les bornes de recharge.
    
    :param lat: Latitude de la cellule
    :param lon: Longitude de la cellule
    :return: Nombre de bornes de recharge
    """
    filtre = (df['latitude'].between(lat_min, lat_max)) & (df['longitude'].between(lon_min, lon_max))
    filtre2 = (df2['latitude'].between(lat_min, lat_max)) & (df2['longitude'].between(lon_min, lon_max))

    numerateur = df.loc[filtre, 'count'].sum()
    denominateur = df2.loc[filtre2, 'NB_VP_RECHARGEABLES_EL'].sum()

    # Vérifier que le dénominateur est valide (ni zéro, ni NaN, ni infini)
    if pd.notna(denominateur) and denominateur != 0 and not denominateur == float('inf'):
        resultat = float(numerateur / denominateur) * 100000
        #print(f"Division valide : numerateur = {numerateur}, denominateur = {denominateur}, resultat = {resultat}")
    else:
        resultat = 0  
        #print(f"⚠️ Division invalide : denominateur = {denominateur}")

    return (resultat, denominateur)

total_borne = 0

def maillage_bornes_habitants(lat: float, lon: float, cell_size : float) -> float:
    global total_borne
    df_borne = pd.read_csv("../data/processed/grouped_borne.csv", low_memory=False)
    df_pop = pd.read_csv("../data/processed/pop_prediction.csv", low_memory=False)


    df_pop['year'] = df_pop['annee']
    bornes_years = df_borne['year'].unique()
    bornes_years = [int(year) for year in bornes_years if 2012 <= int(year) <= 2024]
    bornes_years.sort()
    pop_years = df_pop['year'].unique().tolist()
    pop_years = [int(years) for years in pop_years if 2012 <= int(years) <= 2024]

    # print("bornes_years : "+str(bornes_years))
    # print("population_years : "+str(pop_years))

    lat_min, lat_max = lat, lat + cell_size # Plage de latitude
    lon_min, lon_max = lon, lon + cell_size    # Plage de longitude
    year = 2024

    filtre_borne = (df_borne['latitude'].between(lat_min, lat_max)) & (df_borne['longitude'].between(lon_min, lon_max)) & (df_borne['year'] <= year)
    filtre_pop = (df_pop['latitude'].between(lat_min, lat_max)) & (df_pop['longitude'].between(lon_min, lon_max)) & (df_pop['year'] == year)

    numerateur = df_borne.loc[filtre_borne, 'count'].sum()
    denominateur = df_pop.loc[filtre_pop, 'prediction_population'].sum()
    total_borne += numerateur
    #print("Total bornes : "+str(total_borne))

    if pd.notna(denominateur) and denominateur != 0 and not denominateur == float('inf'):
        resultat = float(numerateur / denominateur) 
        #print(f"Division valide : numerateur = {numerateur}, denominateur = {denominateur}, resultat = {resultat}")
    else:
        resultat = 0  
        #print(f"⚠️ Division invalide : denominateur = {denominateur}")

    return (resultat, denominateur)



def cells_to_geodataframe(cells: List[Cell.Cell]) -> gpd.GeoDataFrame:
    """
    Convertit une liste de cellules en GeoDataFrame pour visualisation.
    
    :param cells: Liste de cellules
    :return: GeoDataFrame avec géométrie des cellules et leurs données
    """
    polygons = [cell.to_polygon() for cell in cells]
    data = [cell.data for cell in cells]

    # Convertir les données en GeoDataFrame
    gdf = gpd.GeoDataFrame({'geometry': polygons, 'data': data})

    # Sauvegarder le GeoDataFrame dans un fichier shapefile
    gdf.to_file("france_grid.shp")

    # Sauvegarder le GeoDataFrame dans un fichier GeoJSON
    gdf.to_file("france_grid.geojson", driver='GeoJSON')
    return gpd.GeoDataFrame({'geometry': polygons, 'data': data})

def plot_heatmap(dossier, cells: List[Cell.Cell]):
    """
    Affiche une heatmap sur Folium avec les cellules et leurs données.
    
    :param cells: Liste des cellules
    """
    # Créer la carte centrée sur la France
    m = folium.Map(location=[46.5, 2.5], zoom_start=6)

    # Préparer les données pour la heatmap (latitude, longitude, poids)
    data_max = max(cell.data for cell in cells)

    heat_data = [(cell.latitude, cell.longitude, cell.data/data_max) for cell in cells]

    # Ajouter la heatmap à la carte
    HeatMap(heat_data, radius=33, blur=30, max_zoom=10).add_to(m)

    # Ajouter une légende à la carte
    folium.LayerControl().add_to(m)
    # Ajouter une légende des couleurs à la carte
    colormap = folium.LinearColormap(
        colors=['blue', 'green', 'yellow', 'orange', 'red'],
        vmin=min_data,
        vmax=max_data,
        caption='Intensity of Data'
    )
    colormap.add_to(m)

    if(min_data != 0):
        colormap = folium.LinearColormap(
        colors=['red', 'orange', 'yellow', 'green', 'blue'],
        vmin=1/max_data,
        vmax=1/min_data,
        caption='Intensity of Data'
    )

    colormap.add_to(m)
    # Sauvegarder la carte
    if dossier != "" :
        dossier = dossier + "/"

    m.save(dossier+"france_heatmap.html")
    print("Heatmap générée et sauvegardée sous france_heatmap.html.")

def csv_to_cells(csv_path: str, size: float) -> List[Cell.Cell]:
    """
    Lit un CSV et crée une liste de Cell avec les colonnes latitude, longitude, data et data_size.
    
    :param csv_path: Chemin vers le fichier CSV
    :param size: Taille des cellules
    :return: Liste de cellules
    """
    df = pd.read_csv(csv_path)

    cells = []
    for _, row in df.iterrows():
        cell = Cell.Cell(
            latitude=row['latitude'],
            longitude=row['longitude'],
            size=size,
            data=row['data'],
            data_size=row['data_size']
        )
        cells.append(cell)
    return cells

# Exemple d'utilisation
if __name__ == "__main__":
    cell_size = 0.25  # Taille de la cellule en degrés (~50 km)
    france_grid = generate_france_grid(maillage_bornes_habitants, cell_size)
    france_gdf = cells_to_geodataframe(france_grid)

    # france_grid = csv_to_cells("bornes_immatr.csv", cell_size)

    df = pd.DataFrame([cell.to_dict() for cell in france_grid])
    df.to_csv("bornes_population/bornes_population.csv", index=False)
    print("Grille de France sauvegardée sous france_grid.csv.")
    
    # Générer et afficher la heatmap
    plot_heatmap("bornes_population",france_grid)

