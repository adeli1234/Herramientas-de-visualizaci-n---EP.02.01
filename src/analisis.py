import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/countries.csv")
# print(df.head())

tabla = df.pivot_table(index="Region", values="HDI", aggfunc="mean")
print(tabla)

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="HDI", hue="Region", multiple="stack", palette="Set2")
plt.title("Distribución del Índice de Desarrollo Humano (HDI) por Región")
plt.xlabel("Índice de Desarrollo Humano (HDI)")
plt.ylabel("Cantidad de Países")
plt.savefig("output/hdi_distribution.png")