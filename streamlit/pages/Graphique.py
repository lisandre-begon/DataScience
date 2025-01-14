import streamlit as st
import dask.dataframe as dd
import plotly.express as px

st.title("Évolution des infrastructures de recharge et des immatriculations de véhicules électriques")

@st.cache_data
def load_data_bornes():
    data = dd.read_csv('/Users/zolan/Library/Mobile Documents/com~apple~CloudDocs/Semestre 7/Projet Data Science/DataScience/data/processed/grouped_borne.csv')
    return data.compute()

data_bornes = load_data_bornes()
data_agg_bornes = data_bornes.groupby('year')['count'].sum().reset_index()

fig_bornes = px.line(
    data_agg_bornes, 
    x='year', 
    y='count', 
    title="Évolution du nombre de bornes de recharge dans le temps"
)
fig_bornes.update_layout(
    xaxis_title="Année", 
    yaxis_title="Nombre de bornes de recharge", 
    xaxis=dict(tickmode='linear', tick0=2012, dtick=1, range=[2012, 2024]),
    yaxis=dict(showgrid=True, gridcolor='rgba(255, 255, 255, 0.3)'),
    hovermode="x unified"  # Affiche la valeur pour chaque point au passage du curseur
)
st.plotly_chart(fig_bornes)

@st.cache_data
def load_data_immatriculations():
    data = dd.read_csv(
        '/Users/zolan/Library/Mobile Documents/com~apple~CloudDocs/Semestre 7/Projet Data Science/DataScience/data/processed/immatr_geo.csv',
        dtype={'code_geo': str},
        usecols=['year', 'NB_VP_RECHARGEABLES_EL']
    )
    data = data.sample(frac=0.1)
    return data.compute()

data_immatriculations = load_data_immatriculations()
data_agg_immatriculations = data_immatriculations.groupby('year')['NB_VP_RECHARGEABLES_EL'].sum().reset_index()

fig_immatriculations = px.line(
    data_agg_immatriculations, 
    x='year', 
    y='NB_VP_RECHARGEABLES_EL', 
    title="Évolution des immatriculations de véhicules électriques dans le temps"
)
fig_immatriculations.update_layout(
    xaxis_title="Année", 
    yaxis_title="Nombre de véhicules électriques immatriculés", 
    xaxis=dict(tickmode='linear', tick0=2020, dtick=1, range=[2020, 2024]),
    yaxis=dict(showgrid=True, gridcolor='rgba(255, 255, 255, 0.3)'),
    hovermode="x unified"  # Affiche la valeur pour chaque point au passage du curseur
)
st.plotly_chart(fig_immatriculations)