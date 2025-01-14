#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py
-------
Point d'entrée principal pour orchestrer le pipeline :
1) Chargement des données
2) Nettoyage et normalisation
3) Application des métadonnées (optionnel)
4) Sauvegarde dans le dossier 'processed'
"""

import os
import pandas as pd

from load_data import (
    load_population_data,
    load_tmja_data,
    load_irve_data
)
from clean_data import (
    clean_population_data,
    clean_tmja_data,
    clean_irve_data
)
from metadata_handler import (
    map_population_codes
)

# Définir les chemins vers les dossiers
DATA_RAW_DIR = os.path.join("..", "data", "raw")
DATA_PROCESSED_DIR = os.path.join("..", "data", "processed")

def main():
    # --- 1) CHARGEMENT ---
    population_data_file = os.path.join(DATA_RAW_DIR, "population_data.csv")
    population_metadata_file = os.path.join(DATA_RAW_DIR, "population_metadata.csv")
    tmja_file = os.path.join(DATA_RAW_DIR, "TMJA2019.csv")
    irve_file = os.path.join(DATA_RAW_DIR, "IRVE.csv")
    
    # Charger les données
    df_population, df_population_meta = load_population_data(population_data_file, population_metadata_file)
    df_tmja = load_tmja_data(tmja_file)
    df_irve = load_irve_data(irve_file)
    
    # --- 2) NETTOYAGE ---
    df_population_clean = clean_population_data(df_population)
    df_tmja_clean = clean_tmja_data(df_tmja)
    df_irve_clean = clean_irve_data(df_irve)
    
    # --- 3) UTILISATION DES MÉTADONNÉES (optionnel) ---
    df_population_clean = map_population_codes(df_population_clean, df_population_meta)
    
    # --- 4) SAUVEGARDE ---
    if not os.path.exists(DATA_PROCESSED_DIR):
        os.makedirs(DATA_PROCESSED_DIR, exist_ok=True)
    
    df_population_clean.to_csv(os.path.join(DATA_PROCESSED_DIR, "population_data_clean.csv"), index=False)
    df_tmja_clean.to_csv(os.path.join(DATA_PROCESSED_DIR, "TMJA2019_clean.csv"), index=False)
    df_irve_clean.to_csv(os.path.join(DATA_PROCESSED_DIR, "IRVE_clean.csv"), index=False)
    
    print("\n[INFO] Toutes les données ont été nettoyées et sauvegardées dans 'data/processed'.")

if __name__ == "__main__":
    main()
