import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df_pop = pd.read_csv("../data/cities_population.csv", low_memory=False)
df_pop = df_pop.loc[df_pop.groupby(['longitude', 'latitude', 'annee'])['valeur_population'].idxmax()]
# Filtrer les entrées pour ne garder que celles en France métropolitaine (y compris la Corse)
# Les coordonnées géographiques de la France métropolitaine sont approximativement :
# Latitude: 41.0 à 51.0
# Longitude: -5.0 à 10.0

df_pop = df_pop[(df_pop['latitude'] >= 41.0) & (df_pop['latitude'] <= 51.5) &
                (df_pop['longitude'] >= -5.0) & (df_pop['longitude'] <= 9.5)]

df_pop.to_csv("../data/filtered_cities_population.csv", index=False)

def somme_population_pour_annee(annee):
    res = df_pop[df_pop['annee'] == annee]['valeur_population'].sum()
    print("Pour "+str(annee)+" on a "+str(res))
    return res

# Exemple de données : Années et populations
annees = df_pop['annee'].unique()
print(annees)

population = []
for a in annees:
    population.append(somme_population_pour_annee(a))
print(population)

populations = np.array(population)  # Exemple de population
annees_future = np.arange(2011, 2025).reshape(-1, 1)
annees = annees.reshape(-1, 1)

# Exemple d'utilisation
annee_donnee = 2020

# 1. Modèle de Régression Linéaire
modele_lineaire = LinearRegression()
modele_lineaire.fit(annees, populations)
predictions_lineaire = modele_lineaire.predict(annees_future)

def save_modele(modele):
    prediction = np.round(modele.predict(annees_future)).astype(int)
    df_predictions = pd.DataFrame({
        'Année': annees_future.flatten(),
        'Prédiction': prediction
    })
    df_predictions.to_csv(f"pop_prediction/{modele.__class__.__name__}.csv", index=False)

# 2. Modèle de Régression Polynomiale (degré 2)
poly_features = PolynomialFeatures(degree=2)
annees_poly = poly_features.fit_transform(annees)
modele_poly2 = LinearRegression()
modele_poly2.fit(annees_poly, populations)
annees_future_poly = poly_features.transform(annees_future)
predictions_poly2 = modele_poly2.predict(annees_future_poly)

# 3. Modèle de Croissance Exponentielle
def modele_exponentiel(t, P0, r):
    return P0 * np.exp(r * (t - 2011))

# Estimation des paramètres P0 et r
from scipy.optimize import curve_fit
params, _ = curve_fit(modele_exponentiel, annees.flatten(), populations, p0=(50000, 0.01))
predictions_exp = modele_exponentiel(annees_future.flatten(), *params)

populations_reelles = [65350000, 65660000, 66000000, 66310000, 66550000, 66720000, 66920000, 67160000, 67390000, 67570000, 67760000, 67970000, 68170000]
annees_reelles = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

# Visualisation des résultats
plt.figure(figsize=(10, 6))
plt.scatter(annees, populations, color='black', label='Données du csv')
plt.scatter(annees_reelles, populations_reelles, color='green', label='Données réelles')
plt.plot(annees_future, predictions_lineaire, label='Régression Linéaire', linestyle='--')
plt.plot(annees_future, predictions_poly2, label='Régression Polynomiale (degré 2)', linestyle='-.')
plt.plot(annees_future, predictions_exp, label='Croissance Exponentielle', linestyle=':')
plt.xlabel('Année')
plt.ylabel('Population')
plt.title('Estimation de la population de 2011 à 2025')
plt.legend()
plt.grid(True)
plt.show()

# Résultats sous forme de tableau
resultats = pd.DataFrame({
    'Année': annees_future.flatten(),
    'Régression Linéaire': predictions_lineaire,
    'Régression Polynomiale (degré 2)': predictions_poly2,
    'Croissance Exponentielle': predictions_exp
})

print(resultats)

save_modele(modele_lineaire)

# import ace_tools as tools
# tools.display_dataframe_to_user(name="Estimation de la Population", dataframe=resultats)
