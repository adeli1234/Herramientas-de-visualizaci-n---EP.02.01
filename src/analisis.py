import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/countries.csv")
# print(df.head())

tabla = df.pivot_table(index="Region", values="HDI", aggfunc="mean")
print(tabla)

plt.figure(figsize=(10, 6))
sns.histplot(
    data=df,
    x="HDI",
    kde=True,
    color="#1C4C9A",
    bins=15
    )
plt.title("La mayoría de los países se concentran en niveles de desarrollo alto y medio-alto")
plt.xlabel("Índice de Desarrollo Humano (HDI)")
plt.ylabel("Cantidad de Países")
plt.savefig("output/hdi_distribution.png")

