
import streamlit as st

def app():
    st.write("Double cartes")
    
    # Slider pour sélectionner l'année
    selected_year = st.slider("Sélectionnez l'année :", min_value=2020, max_value=2024, step=1)

    # Génération dynamique du chemin de la carte HTML
    file_path2 = f"../script/map/cartes_immatr/immatr_map_{selected_year}.html"
    col1, col2 = st.columns(2)

    try:
        with col1:
            menu = st.selectbox(
                "Choisissez la carte 1 :",
                ["Immatriculation", "Bornes", "Flux routiers", "Population"]
            )

            if(menu == "Immatriculation") :
                file_path2 = f"../script/map/cartes_immatr/immatr_map_{selected_year}.html"
                st.subheader("Carte des Immatriculations")
            elif(menu == "Bornes") :
                file_path2 = f"../script/map/cartes_bornes/carte_{selected_year}.0.html"
                st.subheader("Carte des Bornes")
            elif(menu == "Flux routiers") :
                file_path2 = f"../script/map/carte_lignes_trafic.html"
                st.subheader("Carte du trafic")
            else :
                file_path2 = f"../script/map/cartes/heatmap_population.html"
                st.subheader("Carte de la population")
            

            # Chargement de la première carte
            with open(file_path2, 'r', encoding='utf-8') as f:
                html_content1 = f.read()

            st.components.v1.html(html_content1, height=400, scrolling=True)
        
        with col2:
            menu2 = st.selectbox(
                "Choisissez la carte 2 :",
                ["Immatriculation", "Bornes", "Flux routiers", "Population"]
            )

            if(menu2 == "Immatriculation") :
                file_path2 = f"../script/map/cartes_immatr/immatr_map_{selected_year}.html"
                st.subheader("Carte des Immatriculations")
            elif(menu2 == "Bornes") :
                file_path2 = f"../script/map/cartes_bornes/carte_{selected_year}.0.html"
                st.subheader("Carte des Bornes")
            elif(menu2 == "Flux routiers") :
                file_path2 = f"../script/map/carte_lignes_trafic.html"
                st.subheader("Carte du trafic")
            else :
                file_path2 = f"../script/map/cartes/heatmap_population.html"
                st.subheader("Carte de la population")

            # Chargement de la première carte
            with open(file_path2, 'r', encoding='utf-8') as f:
                html_content1 = f.read()

            st.components.v1.html(html_content1, height=400, scrolling=True)

    except FileNotFoundError:
        st.error(f"Le fichier pour l'année {selected_year} n'a pas été trouvé.")
