import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../../../data/processed/immatr_geo.csv', sep=",")
min_val = data["NB_VP_RECHARGEABLES_EL"].min()
max_val = data["NB_VP_RECHARGEABLES_EL"].max()
n = 100
step = int(max_val / n)
print(step)

print(min_val), print(max_val)

df = pd.DataFrame(columns=['VT','VE', 'RAPPORT', 'CITY_CODE'])
for index, row in data.iterrows():
    vt = row['NB_VP']
    ve = row['NB_VP_RECHARGEABLES_EL']
    city_code = row['city_code']
    rapport = row['NB_VP_RECHARGEABLES_EL'] / row['NB_VP'] if row['NB_VP'] != 0 else 0
    df.loc[len(df)] = [vt, ve, rapport, city_code]

plt.figure(figsize=(10, 6))
plt.scatter(df['VT'], df['RAPPORT'], alpha=0.5)
plt.title('Relation between VT and RAPPORT')
plt.xlabel('VT')
plt.ylabel('RAPPORT')
plt.grid(True)
plt.savefig('plot.png')
plt.close()

df.to_csv('test.csv', index=False)
