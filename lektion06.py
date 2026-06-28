import pandas as pd
import matplotlib.pyplot as plt

# Simulierte Daten - Bearbeitungszeiten in Minuten
prozess_daten = {
    "schritt": ["Antrag", "Prüfung", "Genehmigung", "Versand"],
    "dauer_minuten": [5, 45, 120, 10],
    "fehlerrate": [0.02, 0.15, 0.05, 0.01]
}

df = pd.DataFrame(prozess_daten)

# KPI 1 - Gesamtdauer
gesamtdauer = df["dauer_minuten"].sum()
print(f"Gesamtdauer des Prozesses: {gesamtdauer} Minuten")

# KPI 2 - Eingpass finden (längster Schritt)
engpass = df.loc[df["dauer_minuten"].idxmax(), "schritt"]
print(f"Engpass: {engpass}")

# KPI 3 - Durchschnittliche Fehlerrate
avg_fehler = df["fehlerrate"].mean()
print(f"Durchschnittliche Fehlerrate: {avg_fehler:.2%}")

# Visualisierung
plt.bar(df["schritt"], df["dauer_minuten"], color="steelblue")
plt.title("Prozessschritte und Dauer")
plt.xlabel("Schritt")
plt.ylabel("Dauer (Minuten)")
plt.show()