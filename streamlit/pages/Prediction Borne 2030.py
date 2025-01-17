import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Configure Streamlit
st.set_page_config(page_title="Régression du nombre de bornes", layout="wide")

# Titre de la page
st.title("Analyse et Régression du Nombre de Bornes par Année")

st.write("Objectif pour 2030 : 400 000 bornes en france")

file_path = "../data/processed/grouped_borne.csv"

if file_path:
    # Lecture du CSV
    df = pd.read_csv(file_path)

    # Récupère les années uniques et filtre
    years = df['year'].unique().astype(int)
    years = [year for year in years if 2012 <= year <= 2024]
    years.sort()

    # Calcul du nombre de bornes pour chaque année
    bornes = [df[df['year'] <= y]['count'].sum() for y in years]
    
    # Affichage des données calculées
    st.write("**Données par année :**")
    st.table(pd.DataFrame({"Année": years, "Nombre de bornes": bornes}))

    # Conversion en tableaux NumPy
    years = np.array(years).reshape(-1, 1)
    bornes = np.array(bornes).reshape(-1, 1)

    # Régression linéaire
    model = LinearRegression()
    model.fit(years, bornes)
    annees_futures = np.arange(2012, 2031).reshape(-1, 1)
    predictions = model.predict(annees_futures)

    # Régressions polynomiales
    degrees = [2, 3, 4]
    poly_predictions = {}
    for degree in degrees:
        poly = PolynomialFeatures(degree=degree)
        years_poly = poly.fit_transform(years)
        poly_model = LinearRegression()
        poly_model.fit(years_poly, bornes)
        annees_futures_poly = poly.transform(annees_futures)
        poly_predictions[degree] = poly_model.predict(annees_futures_poly)

    # Graphiques
    st.write("**Graphique des Régressions :**")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(years, bornes, color='blue', label='Données réelles')
    ax.plot(annees_futures, predictions, color='red', label='Régression linéaire')

    colors = ['green', 'orange', 'purple']
    for i, degree in enumerate(degrees):
        ax.plot(annees_futures, poly_predictions[degree], color=colors[i],
                label=f'Régression polynomiale (degré {degree})')

    ax.set_xlabel('Année')
    ax.set_ylabel('Nombre de bornes')
    ax.set_title('Régression du nombre de bornes par année')
    ax.legend()
    st.pyplot(fig)

    # Statistiques des régressions
    st.write("**Statistiques des Régressions :**")
    mse_linear = mean_squared_error(bornes, model.predict(years))
    r2_linear = r2_score(bornes, model.predict(years))
    st.write(f"**Régression linéaire :** MSE = {mse_linear:.2f}, R2 = {r2_linear:.2f}")

    st.write("\n\n")
    # Prédictions pour 2029 et 2030
    st.write("**Prédictions pour 2029 et 2030 :**")
    pred_2029 = model.predict(np.array([[2029]]))[0][0]
    pred_2030 = model.predict(np.array([[2030]]))[0][0]
    st.write(f"Régression linéaire : 2029 = {pred_2029:.0f}, 2030 = {pred_2030:.0f}")

    # Prédictions pour 2029 et 2030 pour les régressions polynomiales
    pred_2029_2030_poly = []
    for degree in degrees:
        poly = PolynomialFeatures(degree=degree)
        poly_model = LinearRegression()
        poly_model.fit(poly.fit_transform(years), bornes)
        pred_2029_poly = poly_model.predict(poly.transform(np.array([[2029]])))[0][0]
        pred_2030_poly = poly_model.predict(poly.transform(np.array([[2030]])))[0][0]
        pred_2029_2030_poly.append([degree, pred_2029_poly, pred_2030_poly])

    st.write("**Prédictions pour 2029 et 2030 (Régressions polynomiales) :**")
    st.table(pd.DataFrame(pred_2029_2030_poly, columns=["Degré", "2029", "2030"]))

    # Statistiques des régressions polynomiales
    stats_poly = []
    for degree in degrees:
        poly = PolynomialFeatures(degree=degree)
        years_poly = poly.fit_transform(years)
        poly_model = LinearRegression()
        poly_model.fit(years_poly, bornes)
        mse_poly = mean_squared_error(bornes, poly_model.predict(years_poly))
        r2_poly = r2_score(bornes, poly_model.predict(years_poly))
        stats_poly.append([degree, mse_poly, r2_poly])

    st.write("**Statistiques des Régressions Polynomiales :**")
    st.table(pd.DataFrame(stats_poly, columns=["Degré", "MSE", "R2"]))

else:
    st.warning("Veuillez charger un fichier CSV contenant les données à analyser.")
