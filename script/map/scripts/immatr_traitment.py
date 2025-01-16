import pandas as pd

# Charger les deux fichiers CSV
csv1 = pd.read_csv("../../../data/cities.csv", sep=",")
csv2 = pd.read_csv("../../../data/raw/voitures-par-commune-par-energie (1).csv", sep=";")

# Définir la colonne commune pour la jointure
colonne_commune = "code_geo"

# Faire la jointure (par défaut, une jointure interne)
nouveau_csv = pd.merge(csv1, csv2, on=colonne_commune, how="inner")

# Choisir les colonnes à inclure dans le nouveau CSV
colonnes_a_conserver = ["code_geo", "city_code","zip_code","latitude","longitude","DATE_ARRETE","NB_VP_RECHARGEABLES_EL","NB_VP_RECHARGEABLES_GAZ","NB_VP"]
nouveau_csv = nouveau_csv[colonnes_a_conserver]

# Sauvegarder le nouveau CSV
nouveau_csv.to_csv("../../../data/processed/immatr_geo.csv", index=False)

print("Le nouveau fichier CSV a été créé : immatr_geo.csv")
