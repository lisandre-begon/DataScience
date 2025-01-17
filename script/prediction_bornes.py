import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Ouvre le CSV avec pandas
df = pd.read_csv('../data/processed/grouped_borne.csv')

# Récupère les années uniques du CSV et les met en int
years = df['year'].unique().astype(int)

# Supprime les années qui ne sont pas entre 2012 et 2024
years = [year for year in years if 2012 <= year <= 2024]
years.sort()
print("Années utilisées :", years)

# Tableau des résultats des bornes
bornes = [df[df['year'] <= y]['count'].sum() for y in years]
for y, total in zip(years, bornes):
    print(f"Nombre de bornes en {y} :", total)

# Conversion en tableaux NumPy et reshaping
years = np.array(years).reshape(-1, 1)  # Matrice 2D pour scikit-learn
bornes = np.array(bornes).reshape(-1, 1)  # Matrice 2D pour scikit-learn

# Créer une régression linéaire
model = LinearRegression()
model.fit(years, bornes)

# Affiche les coefficients de la régression
print("Coefficient de la régression (pente) :", model.coef_[0][0])
print("Ordonnée à l'origine :", model.intercept_[0])

annees_futures = np.arange(2012, 2031).reshape(-1, 1)

# Prédictions pour les années futures avec la régression linéaire
predictions = model.predict(annees_futures)

# Régressions polynomiales pour plusieurs degrés
degrees = [2, 3, 4]
poly_predictions = {}

for degree in degrees:
    poly = PolynomialFeatures(degree=degree)
    years_poly = poly.fit_transform(years)
    poly_model = LinearRegression()
    poly_model.fit(years_poly, bornes)

    # Prédictions pour les années futures
    annees_futures_poly = poly.transform(annees_futures)
    poly_predictions[degree] = poly_model.predict(annees_futures_poly)

    # Affiche les coefficients pour chaque degré
    # print(f"Degré {degree} - Coefficients :", poly_model.coef_)
    # print(f"Degré {degree} - Ordonnée à l'origine :", poly_model.intercept_)

# Visualisation des résultats
plt.figure(figsize=(10, 6))

# Données réelles
plt.scatter(years, bornes, color='blue', label='Données réelles')

# Régression linéaire
plt.plot(annees_futures, predictions, color='red', label='Régression linéaire')

# Régressions polynomiales
colors = ['green', 'orange', 'purple', 'cyan']
for i, degree in enumerate(degrees):
    plt.plot(annees_futures, poly_predictions[degree], color=colors[i],
             label=f'Régression polynomiale (degré {degree})')

            # Calcul et affichage des statistiques de réussite pour chaque courbe

# Statistiques pour la régression linéaire
mse_linear = mean_squared_error(bornes, model.predict(years))
r2_linear = r2_score(bornes, model.predict(years))
print(f"Régression linéaire - MSE: {mse_linear:.2f}, R2: {r2_linear:.2f}")

# Statistiques pour les régressions polynomiales
for degree in degrees:
    poly = PolynomialFeatures(degree=degree)
    years_poly = poly.fit_transform(years)
    poly_model = LinearRegression()
    poly_model.fit(years_poly, bornes)
    
    mse_poly = mean_squared_error(bornes, poly_model.predict(years_poly))
    r2_poly = r2_score(bornes, poly_model.predict(years_poly))
    print(f"Régression polynomiale (degré {degree}) - MSE: {mse_poly:.2f}, R2: {r2_poly:.2f}")

# Ajout des labels et du titre
plt.xlabel('Année')
plt.ylabel('Nombre de bornes')
plt.title('Régression du nombre de bornes par année')
plt.legend()

# Affichage du plot
plt.show()
