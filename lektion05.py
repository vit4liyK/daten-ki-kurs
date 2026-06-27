import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Daten
daten = {
    "name": ["Anna", "Ben", "Clara", "David"],
    "alter": [4, 5, 3, 6],
    "gewicht": [18, 22, 15, 24]
}

df = pd.DataFrame(daten)

# Balkendiagramm
plt.bar(df["name"], df["gewicht"])
plt.title("Gewicht der Kinder")
plt.xlabel("Name")
plt.ylabel("Gewicht (kg)")
plt.show()

# Liniendiagramm
plt.plot(df["name"], df["gewicht"], marker="o")
plt.title("Gewicht der Kinder")
plt.xlabel("Name")
plt.ylabel("Gewicht (kg)")
plt.show()

# Seaborn - schöneres Balkendiagramm
sns.barplot(data=df, x="name", y="gewicht")
plt.title("Gewicht der Kinder (Seaborn)")
plt.show()

# Seaborn Heatmap - zeigt Korrelationen zwischen Spalten
sns.heatmap(df[["alter", "gewicht"]].corr(), annot=True, cmap="coolwarm")
plt.title("Korrelationen zwischen Alter und Gewicht")
plt.show()