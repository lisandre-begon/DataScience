import streamlit as st

st.title("Infrastructures de recharge en France : état et perspectives")

# CSS pour justifier le texte
st.markdown(
    """
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="justified-text">
    Bienvenue sur notre projet de Data Science en groupe de 4, consacré aux infrastructures de recharge en France. 
    Nous sommes ravis de vous présenter notre analyse approfondie sur l'état actuel et les perspectives futures des infrastructures de recharge pour véhicules électriques en France.

    ### Contexte
    En France, le secteur des transports est le principal contributeur aux émissions de CO₂, représentant 38 % des émissions totales. Face à cette situation préoccupante, le gouvernement s’engage dans une transition écologique en promouvant activement la mobilité électrique. Cette démarche vise à réduire l’impact environnemental des déplacements et à répondre aux enjeux climatiques urgents.

    Les efforts pour encourager l’adoption de véhicules électriques portent déjà leurs fruits, comme en témoigne la forte augmentation des immatriculations, notamment une croissance spectaculaire du nombre de ventes de +128 % en 2020 et de 60% en 2021*. Cependant, cette adoption massive s’accompagne de défis majeurs, notamment le développement des infrastructures de recharge publique. Ces infrastructures doivent non seulement suivre le rythme de cette croissance, mais aussi répondre aux besoins diversifiés des usagers.

    ### Objectifs du Projet
    L’un des enjeux centraux est de garantir un équilibre entre le nombre de bornes de recharge disponibles et le parc croissant de véhicules électriques. Par ailleurs, il est essentiel d’assurer une répartition homogène des infrastructures sur tout le territoire pour éviter les disparités régionales et permettre à tous les usagers d’accéder facilement aux bornes, quelles que soient leur localisation ou leurs habitudes de déplacement.

    ### Notre Équipe
    Nous sommes un groupe de quatre étudiants de Polytech Montpellier spécialisés en Informatique et Gestion. Notre équipe est composée de :
    - BEGON Lisandre
    - DRUCKE Alois
    - FRIESS Mathis
    - GIVRE Zolan

    ### Méthodologie
    Pour répondre à ces questions cruciales, nous nous appuyons sur une analyse approfondie des données disponibles sur l'INSEE et data.gouv. Nous utilisons des techniques de Data Science pour explorer, visualiser et modéliser les données afin de fournir des insights pertinents et des recommandations pour le développement futur des infrastructures de recharge.

    Nous espérons que vous trouverez notre projet informatif et inspirant. N'hésitez pas à explorer les différentes sections pour en savoir plus sur notre travail et nos conclusions.
    </div>
    """,
    unsafe_allow_html=True
)