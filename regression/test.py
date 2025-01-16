import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = 'pop_prediction/pop_prediction.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
import matplotlib.pyplot as plt

# Calculer la somme des prédictions par année
sum_predictions_per_year = df.groupby('annee')['prediction_population'].sum()

# Afficher les sommes dans la console
for i in range(2011, 2025):
    sum_prediction_population = sum_predictions_per_year.get(i, 0)  # 0 si l'année n'est pas présente
    print(f"Sum of prediction_population for the year {i}: {sum_prediction_population}")

populations_reelles = [65350000, 65660000, 66000000, 66310000, 66550000, 66720000, 66920000, 67160000, 67390000, 67570000, 67760000, 67970000, 68170000]
annees_reelles = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

# Tracer la somme totale des prédictions de population par année
plt.figure(figsize=(10, 6))
plt.plot(sum_predictions_per_year.index, sum_predictions_per_year.values, marker='o', linestyle='-', color='b')
plt.title('Total Population Predictions Over the Years')
plt.scatter(annees_reelles, populations_reelles, color='green', label='Données réelles')
plt.xlabel('Year')
plt.ylabel('Total Predicted Population')
plt.grid(True)
plt.xticks(range(2011, 2025))  # Assure que toutes les années sont sur l'axe X
plt.tight_layout()
plt.show()
