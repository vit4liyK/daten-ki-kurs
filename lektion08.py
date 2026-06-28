import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Daten
noten =[55, 60, 72, 78, 85, 88, 91, 94]

# 1. Grundlegende Statistik
print(f"Mittelwert:      {np.mean(noten):.1f}")
print(f"Median:      {np.median(noten):.1f}")
print(f"Standardabweichung:      {np.std(noten):.1f}")
print(f"Varianz:      {np.var(noten):.1f}")
print(f"25% Perzentil:      {np.percentile(noten, 25):.1f}")
print(f"75% Perzentil:      {np.percentile(noten, 75):.1f}")

# 2. Ausreißer Effekt zeigen
noten_mit_ausreisser = noten + [5]
print(f"\nMittelwert mit Ausreißer: {np.mean(noten_mit_ausreisser):.1f}")
print(f"Median mit Ausreißer: {np.median(noten_mit_ausreisser):.1f}")

# 3. Visualisierung - Histogramm
plt.hist(noten, bins=5, color="steelblue", edgecolor="black")
plt.axvline(np.mean(noten), color="red", label="Mittelwert")
plt.axvline(np.median(noten), color="green", label="Median")
plt.title("Notenverteilung")
plt.xlabel("Note")
plt.ylabel("Anzahl")
plt.legend()
plt.show()

