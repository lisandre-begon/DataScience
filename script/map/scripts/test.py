import pandas as pd

# 📂 Charger le fichier CSV
df = pd.read_csv('../../../data/processed/immatr_geo.csv', sep=",")

print(df['DATE_ARRETE'])

# 🕒 Conversion de la colonne 'DATE_ARRETE' en datetime
df['DATE_ARRETE'] = pd.to_datetime(df['DATE_ARRETE'], errors='coerce')

# 📊 Filtrer pour obtenir la date la plus récente par CODGEO
latest_dates = df[df['DATE_ARRETE'] == df.groupby('CODGEO')['DATE_ARRETE'].transform('max')]

# print(latest_dates)


# ➕ Calculer la somme des 'NB_VP' pour les CODGEO avec la date la plus récente
somme_nb_vp = latest_dates.groupby('CODGEO')['NB_VP_RECHARGEABLES_EL'].sum()

# 🖨️ Afficher les résultats
print(somme_nb_vp)
