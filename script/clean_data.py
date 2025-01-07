#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
clean_data.py
-------------
Fonctions responsables du nettoyage et de la normalisation des DataFrames.
"""

import pandas as pd
import numpy as np

def clean_population_data(df_population):
    """
    Nettoie et normalise le DataFrame population.
    Exemple : Gérer valeurs manquantes, renommer colonnes, etc.
    """
    # Exemples de nettoyage (à adapter selon vos besoins réels)
    df_population.dropna(subset=["OBS_VALUE"], inplace=True)
    
    # Renommer quelques colonnes pour plus de clarté
    df_population.rename(columns={
        "GEO": "code_geo",
        "POPREF_MEASURE": "type_population",
        "TIME_PERIOD": "annee",
        "OBS_VALUE": "valeur_population"
    }, inplace=True)
    
    # Autres opérations de nettoyage...
    
    return df_population

def clean_tmja_data(df_tmja):
    """
    Nettoie et normalise le DataFrame TMJA.
    """
    # Exemples
    df_tmja.dropna(subset=["TMJA"], inplace=True)
    df_tmja.rename(columns={
        "TMJA": "trafic_moyen_journalier",
        "xD": "x_debut",
        "yD": "y_debut"
    }, inplace=True)
    
    # Conversion d'un champ en numérique
    df_tmja["trafic_moyen_journalier"] = pd.to_numeric(df_tmja["trafic_moyen_journalier"], errors="coerce")
    
    # Autres opérations...
    
    return df_tmja

def clean_irve_data(df_irve):
    """
    Nettoie et normalise le DataFrame IRVE.
    """
    # Suppression des lignes vides
    df_irve.dropna(subset=["nom_enseigne", "consolidated_longitude", "consolidated_latitude"], inplace=True)
    
    # Renommer pour plus de cohérence
    df_irve.rename(columns={
        "consolidated_longitude": "longitude",
        "consolidated_latitude": "latitude",
        "puissance_nominale": "puissance"
    }, inplace=True)
    
    # Exemple de conversion en float
    df_irve["longitude"] = pd.to_numeric(df_irve["longitude"], errors="coerce")
    df_irve["latitude"] = pd.to_numeric(df_irve["latitude"], errors="coerce")
    
    return df_irve
