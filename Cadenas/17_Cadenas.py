# 17_Cadenas

# 17. Realiza un programa que pinte la letra U por pantalla
# hecha con asteriscos. El programa pedirá la altura. Fíjate
# que el programa inserta un espacio y pinta dos asteriscos
# menos en la base para simular la curvatura de las esquinas
# inferiores.

n = int(input("Introduzca la altura de la u: "))
print("")

cadena = "*"
cadena_cierre = (("* ") * (n-2))

for i in range(0, n):
    if i == n-1:
        print(f'{cadena_cierre:^50}')
    else:
        print(f'{cadena + " " + "  " * (n-1) + cadena:^50}')