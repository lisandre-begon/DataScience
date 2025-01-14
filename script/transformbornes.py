import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, LineString

# Load IRVE data
irve = pd.read_csv("../data/processed/IRVE_geo.csv")
gdf_irve = gpd.GeoDataFrame(
    irve, 
    geometry=gpd.points_from_xy(irve['longitude'], irve['latitude']), 
    crs="EPSG:4326"
)

# Load TMJA data
tmja = pd.read_csv("../data/processed/TMJA2019_geo.csv")
tmja['geometry'] = tmja.apply(
    lambda row: LineString([(row['longitudeD'], row['latitudeD']), (row['longitudeF'], row['latitudeF'])]), 
    axis=1
)
gdf_tmja = gpd.GeoDataFrame(tmja, geometry='geometry', crs="EPSG:4326")
