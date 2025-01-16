
import streamlit as st

def app():
    st.write("Carte des immatriculations")
    
    with open("../script/map/cartes/heatmap_population.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    st.components.v1.html(html_content, height=600)