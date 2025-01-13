
import streamlit as st

def app():
    st.write("Carte des immatriculations")

     # Slider pour sélectionner l'année
    selected_year = st.slider("Sélectionnez l'année :", min_value=2020, max_value=2024, step=1)

    # Génération dynamique du chemin de la carte HTML
    file_path = f"../script/map/immatr/immatr_map_{selected_year}.html"

    # Chargement de la carte HTML sélectionnée
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Affichage de la carte dans Streamlit
        st.components.v1.html(html_content, height=600, scrolling=True)

    except FileNotFoundError:
        st.error(f"Le fichier pour l'année {selected_year} n'a pas été trouvé.")
