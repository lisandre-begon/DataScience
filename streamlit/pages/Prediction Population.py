import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from scipy.optimize import curve_fit

# Load data
df_pop = pd.read_csv("../data/cities_population.csv", low_memory=False)
df_pop = df_pop.loc[df_pop.groupby(['longitude', 'latitude', 'annee'])['valeur_population'].idxmax()]

# Filter for France (Latitude and Longitude constraints)
df_pop = df_pop[(df_pop['latitude'] >= 41.0) & (df_pop['latitude'] <= 51.5) & 
                (df_pop['longitude'] >= -5.0) & (df_pop['longitude'] <= 9.5)]

df_pop.to_csv("../data/filtered_cities_population.csv", index=False)

# Streamlit setup for displaying results
st.title("Estimation de la Population de 2011 à 2025")
st.write("Voici une estimation de la population de la France métropolitaine pour les années à venir en utilisant différents modèles.")

# Function to compute total population per year
def somme_population_pour_annee(annee):
    res = df_pop[df_pop['annee'] == annee]['valeur_population'].sum()
    return res

# Get unique years and calculate population for each year
annees = df_pop['annee'].unique()
population = [somme_population_pour_annee(a) for a in annees]

populations = np.array(population)  
annees_future = np.arange(2011, 2025).reshape(-1, 1)
annees = annees.reshape(-1, 1)

# Linear Regression Model
modele_lineaire = LinearRegression()
modele_lineaire.fit(annees, populations)
predictions_lineaire = modele_lineaire.predict(annees_future)

# Polynomial Regression Model (Degree 2)
poly_features = PolynomialFeatures(degree=2)
annees_poly = poly_features.fit_transform(annees)
modele_poly2 = LinearRegression()
modele_poly2.fit(annees_poly, populations)
annees_future_poly = poly_features.transform(annees_future)
predictions_poly2 = modele_poly2.predict(annees_future_poly)

# Exponential Growth Model
def modele_exponentiel(t, P0, r):
    return P0 * np.exp(r * (t - 2011))

params, _ = curve_fit(modele_exponentiel, annees.flatten(), populations, p0=(50000, 0.01))
predictions_exp = modele_exponentiel(annees_future.flatten(), *params)

# Real data for comparison
populations_reelles = [65350000, 65660000, 66000000, 66310000, 66550000, 66720000, 66920000, 67160000, 67390000, 67570000, 67760000, 67970000, 68170000]
annees_reelles = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

# Display plot using Streamlit
st.subheader("Visualisation des résultats")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(annees, populations, color='black', label='Données du csv')
ax.scatter(annees_reelles, populations_reelles, color='green', label='Données réelles')
ax.plot(annees_future, predictions_lineaire, label='Régression Linéaire', linestyle='--')
ax.plot(annees_future, predictions_poly2, label='Régression Polynomiale (degré 2)', linestyle='-.')
ax.plot(annees_future, predictions_exp, label='Croissance Exponentielle', linestyle=':')
ax.set_xlabel('Année')
ax.set_ylabel('Population')
ax.set_title('Estimation de la population de 2011 à 2025')
ax.legend()
ax.grid(True)

# Streamlit display the plot
st.pyplot(fig)

# Display the results in a table using Streamlit
st.subheader("Tableau des résultats")
resultats = pd.DataFrame({
    'Année': annees_future.flatten(),
    'Régression Linéaire': predictions_lineaire,
    'Régression Polynomiale (degré 2)': predictions_poly2,
    'Croissance Exponentielle': predictions_exp
})

st.write(resultats)

# Save model predictions (you can choose to display or not)
def save_modele(modele):
    prediction = np.round(modele.predict(annees_future)).astype(int)
    df_predictions = pd.DataFrame({
        'Année': annees_future.flatten(),
        'Prédiction': prediction
    })
    df_predictions.to_csv(f"pop_prediction/{modele.__class__.__name__}.csv", index=False)

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
bordeaux = [44.857621613,-0.5733793060000001]

# Afficher les données dans Streamlit
# st.write(data)

# Créer un graphique
fig, ax = plt.subplots()

# Créer un menu déroulant pour sélectionner une ville
ville = st.selectbox(
    'Sélectionnez une ville',
    ('Bordeaux','Pouilloux', 'Vif', 'Lavaldens', 'Pontcharra')
)

# Définir les coordonnées en fonction de la ville sélectionnée
if ville == 'Pouilloux':
    lat, lon = pouilloux
elif ville == 'Vif':
    lat, lon = vif
elif ville == 'Pontcharra':
    lat, lon = pontcharra
elif ville == 'Bordeaux':
    lat, lon = bordeaux
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

save_modele(modele_lineaire)
