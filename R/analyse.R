# Chargement des librairies nécessaires
library(tidyverse)
library(sf)  # Pour manipuler les données géospatiales

# Importation des fichiers CSV
irve <- read.csv("~/Library/Mobile Documents/com~apple~CloudDocs/Semestre 7/Projet Data Science/DataScience/data/processed/grouped_borne.csv")
population <- read.csv("~/Library/Mobile Documents/com~apple~CloudDocs/Semestre 7/Projet Data Science/DataScience/data/cities_population.csv")
tmja <- read.csv("~/Library/Mobile Documents/com~apple~CloudDocs/Semestre 7/Projet Data Science/DataScience/data/processed/TMJA2019_geo.csv")
immatriculation <- read.csv("~/Library/Mobile Documents/com~apple~CloudDocs/Semestre 7/Projet Data Science/DataScience/data/processed/immatr_geo.csv")

head(irve)
head(population)
head(tmja)
head(immatriculation)
