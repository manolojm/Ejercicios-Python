# 11_Listas
import random

def mostrar_vectores():
    print("\n- - - - - - - - - -")
    print("Índice: ")
    
    for i in range(10):
        print(f"{str(i) + ' |':>6}", end='')
    print("\nValor: ")
    
    for i in range(10):
        print(f"{str(vector_numeros[i]) + ' |':>6}", end='')
    print("\n- - - - - - - - - -")

vector_numeros = []
vector_mayores = []
vector_menores = []

for i in range(10):
    nuevo_numero = (random.randint(0, 200))
    vector_numeros.append(nuevo_numero)
    if nuevo_numero > 100:
        vector_mayores.append(nuevo_numero)
    else:
        vector_menores.append(nuevo_numero)

print("Array original:")
mostrar_vectores()

vector_numeros.clear()

for i in range(10):
    if len(vector_menores) > 0:
        nuevo_numero = vector_menores.pop(0)
        vector_numeros.append(nuevo_numero)
    if len(vector_mayores) > 0:    
        nuevo_numero = vector_mayores.pop(0)
        vector_numeros.append(nuevo_numero)

print("Array resultado:")
mostrar_vectores()