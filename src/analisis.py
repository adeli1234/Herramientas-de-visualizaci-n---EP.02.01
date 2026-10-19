import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/countries.csv")
# print(df.head())

tabla = df.pivot_table(index="Region", values="HDI", aggfunc="mean")
print(tabla)

# Gráfica 1
# Pregunta: ¿Cómo se distribuye el desarrollo humano en el mundo?

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

# Gráfica 2
# Pregunta: ¿Qué reguiones registran los promedios de desarrollo más altos?
colores = ["#1C4C9A" if hdi > 0.8 else "#B9C3D1" for hdi in tabla["HDI"]]

plt.figure(figsize=(10, 6))
sns.barplot(
    data=tabla,
    x="HDI",
    y="Region",
    palette=colores
)
plt.title("Promedios de Desarrollo por Región")
plt.xlabel("Índice de Desarrollo Humano (HDI)")
plt.ylabel("Región")
plt.savefig("output/hdi_por_region.png")

# Gráfica 3
# Pregunta: ¿Existe relacion entre el PIB per cápita y la huella ecológica?
if df['GDP per Capita'].dtype == object:
    df['GDP_clean'] = df['GDP per Capita'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
else:
    df['GDP_clean'] = df['GDP per Capita']

plt.figure(figsize=(10, 5))
paleta_multi = ["#1C4C9A", "#B9C3D1", "#E69F00", "#56B4E9", "#009E73", "#0072B2", "#D55E00"]

sns.scatterplot(
    data=df,
    x="GDP_clean",
    y="Total Ecological Footprint",
    hue="Region",
    palette=paleta_multi,
    alpha=0.85
)
plt.xscale('log')
plt.title("Un mayor ingreso per cápita se asocia exponencialmente con una mayor huella ecológica", fontsize=11, fontweight='bold')
plt.xlabel("PIB per Cápita (USD, escala logarítmica)")
plt.ylabel("Huella Ecológica Total (ha/cápita)")
plt.savefig("gdp_vs_huella_relacion.png")