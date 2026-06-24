# 1) Dictionary erstellen und alle Keys ausgeben mit einer Schleife
kita_kind = {
    "name": "Rene",
    "alter": 4,
    "lieblingsfarbe": "blau"
}

kita_kind["lieblingstier"] = "Bär"

for key in kita_kind:
    print(f"Key: {key}")

# 2) Liste mit Zahlen und Duplikaten konvertieren
zahlen = [1, 2, 2, 3, 3]
print(zahlen)
zahlen.append(4)
zahlen.append(5)
zahlen.remove(2)
zahlen.remove(3)

zahlen_set = set(zahlen)
print(zahlen_set)

#3 Tuple mit Geburtsdatum
geburts_datum = (1,1,1901)
print(geburts_datum)