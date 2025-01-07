#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
load_data.py
------------
Fonctions de chargement des fichiers CSV en DataFrames pandas.
"""

import pandas as pd
import os

def load_csv(file_path, sep=",", encoding="utf-8"):
    """
    Charge un fichier CSV dans un DataFrame pandas, gère l'absence du fichier.
    """
    if not os.path.exists(file_path):
        print(f"[ERREUR] Fichier introuvable : {file_path}")
        return pd.DataFrame()
    df = pd.read_csv(file_path, sep=sep, encoding=encoding)
    print(f"[INFO] Chargé : {file_path} | {df.shape[0]} lignes, {df.shape[1]} colonnes")
    return df

def load_population_data(data_file, metadata_file=None):
    """
    Charge les données et métadonnées de population.
    """
    population_df = load_csv(data_file, sep=";", encoding="utf-8")
    
    if metadata_file is not None:
        metadata_df = load_csv(metadata_file, sep=";", encoding="utf-8")
        return population_df, metadata_df
    else:
        return population_df, None

def load_tmja_data(file_path):
    """
    Charge le fichier TMJA (Trafic).
    """
    tmja_df = load_csv(file_path, sep=";", encoding="utf-8")
    return tmja_df

def load_irve_data(file_path):
    """
    Charge le fichier IRVE (infrastructures de recharge).
    """
    irve_df = load_csv(file_path, sep=",", encoding="utf-8")
    return irve_df
