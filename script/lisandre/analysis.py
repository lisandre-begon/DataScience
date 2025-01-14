import pandas as pd
import folium

# Load the IRVE data
irve_data_path = "../data/processed/IRVE_clean.csv"
df_irve = pd.read_csv(irve_data_path, low_memory=False)

# Fix coordonneesXY formatting issues
df_irve['coordonneesXY'] = df_irve['coordonneesXY'].str.replace(r'[ ;]', ',', regex=True)

# Split coordonneesXY into longitude and latitude
df_irve[['longitude', 'latitude']] = df_irve['coordonneesXY'].str.split(',', expand=True)

# Convert to numeric
df_irve['longitude'] = pd.to_numeric(df_irve['longitude'], errors='coerce')
df_irve['latitude'] = pd.to_numeric(df_irve['latitude'], errors='coerce')

# Filter out invalid rows
df_irve_clean = df_irve.dropna(subset=['latitude', 'longitude'])

# Save invalid rows for inspection
df_invalid = df_irve[df_irve_clean.index.difference(df_irve.index)]
df_invalid.to_csv("invalid_coordinates.csv", index=False)
print(f"Saved rows with invalid coordinates to 'invalid_coordinates.csv'.")

# Ensure there are valid rows
if df_irve_clean.empty:
    print("No valid coordinates found. Please check 'invalid_coordinates.csv' for details.")
else:
    # Compute map center
    map_center = [df_irve_clean['latitude'].mean(), df_irve_clean['longitude'].mean()]

    # Initialize the Folium map
    irve_map = folium.Map(location=map_center, zoom_start=6)

    # Add points to the map
    for _, row in df_irve_clean.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Borne at ({row['latitude']}, {row['longitude']})"
        ).add_to(irve_map)

    # Save the map
    irve_map.save("irve_map_coordonneesXY.html")
    print("Map saved as 'irve_map_coordonneesXY.html'. Open this file in a browser to view the map.")
