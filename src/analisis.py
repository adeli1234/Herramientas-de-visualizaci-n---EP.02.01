import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/countries.csv")
# print(df.head())

tabla = df.pivot_table(index="categoria", values="valor", aggfunc="mean")
print(tabla)