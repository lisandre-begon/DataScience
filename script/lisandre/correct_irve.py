import pandas as pd

# 1) Load your CSV
df_irve = pd.read_csv("../data/processed/IRVE_clean.csv", sep=",", encoding="utf-8")

# 2) Extract any 5-digit sequence from 'adresse_station' using a regex
df_irve["extracted_insee"] = (
    df_irve["adresse_station"]
    .str.extract(r"(\b\d{5}\b)", expand=False)
    .astype("string")  # Ensures we keep leading zeros if found
)

# 3) Make sure 'code_insee_commune' is also string
df_irve["code_insee_commune"] = df_irve["code_insee_commune"].astype("string")

# 4) Fill missing 'code_insee_commune' with 'extracted_insee'
df_irve["code_insee_commune"] = df_irve["code_insee_commune"].fillna(df_irve["extracted_insee"])

# 5) Some rows might have 4-digit codes (like "6000" instead of "06000").
#    Use .str.zfill(5) to ensure they are exactly 5 digits long, adding leading zeros if needed.
df_irve["code_insee_commune"] = df_irve["code_insee_commune"].fillna("")
df_irve["code_insee_commune"] = df_irve["code_insee_commune"].str.zfill(5)

# 6) Drop the helper column if no longer needed
df_irve.drop(columns=["extracted_insee"], inplace=True)

# 7) Save your cleaned version
df_irve.to_csv("IRVE_clean_improved.csv", index=False)

print("[INFO] Done extracting/filling code_insee_commune with leading zeros!")
