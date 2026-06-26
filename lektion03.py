import numpy as np

kinder_gewichte = np.array([22, 30, 15, 18, 10])

print(np.sum(kinder_gewichte)) # Summer aller Gewichte
print(np.mean(kinder_gewichte)) # Durchschnitt aller Gewichte
print(np.max(kinder_gewichte)) # Höchstes Gewicht
print(np.min(kinder_gewichte)) # Kleinstes Gewicht

print(kinder_gewichte * 2) # jeden Wert verdoppeln


matrix = np.array([
    [1, 2, 3, 6],
    [4, 5, 6, 7],
    [7, 8, 9, 8]
])

print(matrix.shape)