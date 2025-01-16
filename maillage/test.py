import pandas as pd

# Remplacez 'france_grid.csv' par le chemin de votre fichier CSV
df = pd.read_csv('france_grid.csv')

# Affichez la valeur maximale de la colonne 'data'
print(f"Max value: {df['data'].max()} at latitude: {df.loc[df['data'].idxmax(), 'latitude']} and longitude: {df.loc[df['data'].idxmax(), 'longitude']}")