# 16_Cadenas

# 16. Escribe un programa que lea un número n e imprima
# una pirámide de números con n filas como en la siguiente
# figura:

n = int(input("Introduzca la altura del triangulo: "))
print("")
cadena = ""

for i in range(1, n+1):
    for j in range(1, i+1):
        cadena += str(j)
    print(f"{cadena[:-1] + cadena[::-1]:^30}")
    cadena = ""
    