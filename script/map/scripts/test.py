import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('../../../data/processed/immatr_geo.csv', sep=",")

# Calculer le rapport NB_VP_RECHARGEABLE / NB_VP
df['RAPPORT'] = df['NB_VP_RECHARGEABLES_EL'] / df['NB_VP']

# Trier le DataFrame par le rapport en ordre décroissant et sélectionner les 10 premières lignes
top_10_villes = df.nlargest(10, 'RAPPORT')

# Afficher les noms des 10 villes avec le rapport le plus haut
print("Les 10 villes avec le rapport NB_VP_RECHARGEABLE / NB_VP le plus haut sont:")
print(top_10_villes[['city_code', 'RAPPORT']])