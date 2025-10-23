# 6_Listas

vector_numeros = []
#vector_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Introducimos los 15 numeros por teclado
print("Introduzca 15 numeros: ")
for i in range(15):
    nuevo_numero = int(input(str(i+1) + "/15 -> "))
    vector_numeros.append(nuevo_numero)

# Sacamos el ultimo valor y lo metemos en la primera posicion
ultimo_numero = vector_numeros.pop()
vector_numeros.insert(0, ultimo_numero)

#Vector desplazado
print(f"\n{vector_numeros}")