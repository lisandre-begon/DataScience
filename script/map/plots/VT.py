import pandas as pd
import plotly.express as px

# Charger les données depuis un fichier CSV
# Remplacez 'data.csv' par le chemin de votre fichier
df = pd.read_csv('test.csv')

# Créer un graphique interactif (exemple : ligne ou scatter)
# fig = px.line(df, x='VT', y='RAPPORT', title='Rapport VE/V par nombre de V')  # Modifiez les colonnes
# ou pour un scatter :
fig = px.scatter(df, x='VT', y='RAPPORT', title='Exemple de graphique interactif', hover_data=['CITY_CODE'])

# Afficher le graphique dans le navigateur
fig.write_html("dynamic_plot.html")
