# 1_Cadenas

# 1. Escribe un programa que muestre por pantalla 10 palabras
# en inglés junto a su correspondiente traducción al castellano.
# Las palabras deben estar distribuidas en dos columnas y
# alineadas a la izquierda.

cadena_en = "computer, student, cat, pernguin, machine, nature, light, green, book, pyramid"
cadena_es = "ordenador, alumno\\a, gato, pingüino, máquina, naturaleza, luz, verde, libro, pirámide"

x = cadena_en.split(", ")
y = cadena_es.split(", ")

for i in range(0, len(x)):
     print(f"{x[i]:<15} {y[i]:<15}")