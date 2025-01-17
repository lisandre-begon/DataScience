
import streamlit as st
from streamlit_folium import st_folium
import pages.souspages.Immatriculation as Immatriculation  # Correction de l'import
import pages.souspages.Bornes as Bornes
import pages.souspages.FluxRoutiers as FluxRoutiers
import pages.souspages.Population as Population
import pages.souspages.Fusion as Fusion

st.title("Hypothèse 3")

st.write("Carte des bornes / population")

selected_year = st.slider("Sélectionnez l'année :", min_value=2012, max_value=2024, step=1)

with open("../maillage/bornes_population/bornes_population_"+str(selected_year)+".html", "r", encoding="utf-8") as file:
    html_content = file.read()

st.components.v1.html(html_content, height=600)
