import pandas as pd

# Chemin vers le fichier CSV
bornes = '../data/processed/grouped_borne.csv'
immatr = '../data/processed/immatr_geo.csv'

# Lecture du fichier CSV avec pandas
df_bornes = pd.read_csv(bornes)
df_immatr = pd.read_csv(immatr)

# Conversion de la colonne 'DATE_ARRETE' en année dans df_immatr
df_immatr['year'] = pd.to_datetime(df_immatr['DATE_ARRETE'], format="%Y-%m-%d", errors='coerce').dt.year
df_immatr = df_immatr[df_immatr['year'] >= 2000]

immatr_years = sorted(df_immatr['year'].unique().astype(int))
print(immatr_years)

# Comptage des immatriculations par année
immatr_tab = []
for y in immatr_years:
    count = df_immatr[df_immatr['year'] <= y].shape[0]
    immatr_tab.append(count)
    print(f"Nombre d'immatriculation en {y} :", count)

# Si df_bornes a une colonne 'DATE_ARRETE', extraire l'année
df_bornes = df_bornes[df_bornes['year'] >= 2000]

bornes_years = sorted(df_bornes['year'].unique().astype(int))
print(bornes_years)

# Comptage des bornes par année
bornes_tab = []
for y in bornes_years:
    count = df_bornes[df_bornes['year'] <= y]['count'].sum()
    bornes_tab.append(count)
    print(f"Nombre de bornes en {y} :", count)






