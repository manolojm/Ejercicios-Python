# 19_Cadenas

# 19. Realiza un programa que pinte un triángulo relleno
# tal como se muestra en los ejemplos. El usuario debe
# introducir la altura de la figura.

n = int(input("Introduzca la altura del triangulo: "))
print()

cadena = "*"
numero_asteriscos = n

for i in range(0, n):
    print(f'{cadena * numero_asteriscos:<50}')
    numero_asteriscos -= 1