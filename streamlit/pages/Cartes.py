import streamlit as st
from streamlit_folium import st_folium
import pages.souspages.Immatriculation as Immatriculation  # Correction de l'import
import pages.souspages.Bornes as Bornes
import pages.souspages.FluxRoutiers as FluxRoutiers
import pages.souspages.Population as Population
import pages.souspages.Fusion as Fusion

st.title("Cartes")

# Menu de sélection
menu = st.selectbox(
    "Choisissez la carte :",
    ["Immatriculation", "Bornes", "Flux routiers", "Population", "Fusion"]
)

# Affichage en fonction du choix
if menu == "Immatriculation":
    Immatriculation.app()  # Appelle la fonction app() d'Immatriculation
elif(menu == "Bornes"):
    Bornes.app()  # Appelle la fonction app() de Bornes
elif(menu == "Flux routiers"):
    FluxRoutiers.app()
elif(menu == "Population"):
    Population.app()
elif(menu == "Fusion"):
    Fusion.app()
else:
    st.write("Erreur de choix")
