import pandas as pd

# DataFrame aus einem Dictionary erstellen
daten = {
    "name": ["Anna", "Ben", "Clara", "David"],
    "alter": [4, 5, 3, 6],
    "gewicht": [18, 22, 15, 24]
}

df = pd.DataFrame(daten)
print(df)

## Filtern
# Nur Kinder die älter als 4 sind
aeltere = df[df["alter"] > 4]
print(aeltere)

# Nur eine Spalte anzeigen
print(df["name"])

# Bestimmte Zeile anzeigen (Index 0 = Anna)
print(df.iloc[0])


## Basis Statistik
print(df["gewicht"].mean()) # Durchschnitt
print(df["gewicht"].max())  # Maximum
print(df["alter"].min())    # Minimum
print(df.describe())        # Alles auf einmal!

## Neue Spalte hinzufügen
df["groesse"] = [105, 112, 98, 118]
print(df)


# CSV laden
df_csv = pd.read_csv("kinder.csv")
print(df_csv)