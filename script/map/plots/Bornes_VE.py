import pandas as pd
import plotly.express as px

# Charger les données depuis un fichier CSV
# Remplacez 'data.csv' par le chemin de votre fichier
df = pd.read_csv("../data/processed/grouped_borne.csv", low_memory=False)
df2 = pd.read_csv("../../data/processed/immatr_geo.csv", low_memory=False)


df['data'] = df['data'] / 1000000
print(df['data_size'].sum())

# Créer un graphique interactif (exemple : ligne ou scatter)
# fig = px.line(df, x='VT', y='RAPPORT', title='Rapport VE/V par nombre de V')  # Modifiez les colonnes
# ou pour un scatter :
fig = px.scatter(df, x='data', y='data_size', title='Bornes / VE')

# Afficher le graphique dans le navigateur
fig.write_html("bornes_ve.html")
