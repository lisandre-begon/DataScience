import pandas as pd
import streamlit as st

import matplotlib.pyplot as plt

# Charger les données CSV
data = pd.read_csv('../data/processed/pop_prediction.csv')
cities = pd.read_csv('../data/cities.csv')
pop = pd.read_csv('../data/filtered_cities_population.csv')


pouilloux = [46.604876131,4.35310787]
vif = [45.04313947,5.674134613]
lavaldens = [44.99232966,5.903427724]
pontcharra = [45.419806496,6.020923525]

# Afficher les données dans Streamlit
# st.write(data)

# Créer un graphique
fig, ax = plt.subplots()

# Créer un menu déroulant pour sélectionner une ville
ville = st.selectbox(
    'Sélectionnez une ville',
    ('Pouilloux', 'Vif', 'Lavaldens', 'Pontcharra')
)

# Définir les coordonnées en fonction de la ville sélectionnée
if ville == 'Pouilloux':
    lat, lon = pouilloux
elif ville == 'Vif':
    lat, lon = vif
elif ville == 'Pontcharra':
    lat, lon = pontcharra
else:
    lat, lon = lavaldens

filtered_data = data[(data['latitude'] == lat) & (data['longitude'] == lon)]
pop_data = pop[(pop['latitude'] == lat) & (pop['longitude'] == lon)]
print(pop_data)

# Vérifier si des données ont été trouvées
if not filtered_data.empty:
    ax.plot(filtered_data['annee'], filtered_data['prediction_population'])
    ax.scatter(pop_data['annee'], pop_data['valeur_population'], color='red')
else:
    st.write("Aucune donnée trouvée pour les coordonnées spécifiées.")

# Afficher le graphique dans Streamlit
st.pyplot(fig)