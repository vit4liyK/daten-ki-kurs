# Aufgabe 1 - Funktion
def beschreibe_person(name, alter, beruf):
    return f"Hi, ich bin {name}, ich bin {alter} Jahre alt und arbeite als {beruf}."

# Aufgabe 2 - Liste
aktivitaeten = ["Gewichtheben", "Gaming", "Musik"]

# Aufgabe 3 - Schleife
for aktivitaet in aktivitaeten:
    print(f"Ich mag: {aktivitaet}")

# Aufgabe 4 - Bedingung
alter = 29
if alter >= 18:
    print("Erwachsen")
else:
    print("Minderjährig")

# Aufgabe 5 - Funktion aufrufen
print(beschreibe_person("Vitaliy", 29, "Erzieher"))