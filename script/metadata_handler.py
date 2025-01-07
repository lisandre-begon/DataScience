#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
metadata_handler.py
-------------------
Fonctions pour mapper ou interpréter les métadonnées 
(ex.: traduire codes en libellés).
"""

import pandas as pd

def map_population_codes(df_population, df_metadata):
    """
    Par exemple, remplacer 'PTOT' par 'Population Totale', etc.
    """
    if df_metadata is None or df_metadata.empty:
        print("[AVERTISSEMENT] Aucune métadonnée fournie.")
        return df_population

    # Construire un dictionnaire de mapping pour POPREF_MEASURE
    measure_mapping = (
        df_metadata[df_metadata["COD_VAR"] == "POPREF_MEASURE"]
        .set_index("COD_MOD")["LIB_MOD"]
        .to_dict()
    )
    
    # Appliquer ce mapping
    df_population["type_population"] = df_population["type_population"].map(measure_mapping)
    
    return df_population
