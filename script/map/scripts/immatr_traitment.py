import pandas as pd

# Charger les deux fichiers CSV
csv1 = pd.read_csv("../../../data/cities.csv", sep=",")
csv2 = pd.read_csv("../../../data/raw/voitures_commune.csv", sep=";")

# Définir la colonne commune pour la jointure
colonne_commune = "code_geo"

# Faire la jointure (par défaut, une jointure interne)
nouveau_csv = pd.merge(csv1, csv2, on=colonne_commune, how="inner")

# Choisir les colonnes à inclure dans le nouveau CSV
colonnes_a_conserver = ["code_geo", "city_code","zip_code","latitude","longitude","NB_VP_RECHARGEABLES_EL","NB_VP_RECHARGEABLES_GAZ","NB_VP"]
nouveau_csv = nouveau_csv[colonnes_a_conserver]

# Regrouper les entrées par 'code_geo', 'latitude' et 'longitude' et additionner les colonnes 'NB_VP_RECHARGEABLES_EL', 'NB_VP_RECHARGEABLES_GAZ' et 'NB_VP'
nouveau_csv = nouveau_csv.groupby(['code_geo', 'latitude', 'longitude'], as_index=False).agg({
    'city_code': 'first',
    'zip_code': 'first',
    'NB_VP_RECHARGEABLES_EL': 'sum',
    'NB_VP_RECHARGEABLES_GAZ': 'sum',
    'NB_VP': 'sum'
})

# Sauvegarder le nouveau CSV
nouveau_csv.to_csv("../../../data/processed/immatr_geo.csv", index=False)

print("Le nouveau fichier CSV a été créé : cities_population.csv")
