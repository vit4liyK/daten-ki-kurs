import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Daten laden
df = pd.read_csv("schueler.csv")
print("=== Datensatz ===")
print(df)
()

# 2. Überblick
print("=== Überblick ===")
print(df.describe())
print()

# 3. KPIs berechnen
print("=== KPIs ===")
print(f"Durchschnitt Mathe: {df['mathe'].mean():.1f}")
print(f"Durchschnitt Deutsch: {df['deutsch'].mean():.1f}")
print(f"Durchschnitt Sport: {df['sport'].mean():.1f}")
print(f"Beste Anwesenheit: {df.loc[df['anwesenheit'].idxmax(), 'name']}")
print(f"Schlechteste Mathe Note: {df.loc[df['mathe'].idxmin(), 'name']}")
print()

# 4. Filtern - Schüler mit Mathe unter 70
print("=== Schüler mit Mathe unter 70 ===")
schwache_mathe = df[df["mathe"] < 70]
print(schwache_mathe[["name", "mathe"]])
print()

# 5. Visualisierung 1 - Noten Vergleich als Balkendiagram
df.plot(x="name", y=["mathe", "deutsch", "sport"], kind="bar", figsize=(10, 6))
plt.title("Noten Vergleich pro Schüler")
plt.xlabel("Schüler")
plt.ylabel("Note")
plt.legend()
plt.tight_layout()
plt.show()

# 6. Visualisierung 2 - Korrelation Heatmap
sns.heatmap(df[["mathe", "deutsch", "sport", "anwesenheit"]].corr(),
        annot=True, cmap="coolwarm")
plt.title("Korrelation zwischen Fächern")
plt.show()

# 7. Visualisierung 3 - Anwesenheit vs Mathe Note
plt.scatter(df["anwesenheit"], df["mathe"])
for i, name in enumerate(df["name"]):
    plt.annotate(name, (df["anwesenheit"][i], df["mathe"][i]))
plt.title("Anwesenheit vs Mathe Note")
plt.xlabel("Anwesenheit (%)")
plt.ylabel("Mathe Note")
plt.show() 

