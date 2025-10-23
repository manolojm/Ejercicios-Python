# 1_Listas
import random

vector_numeros = []

for i in range(10):
    nuevo_numero = (random.randint(1, 10))
    vector_numeros.append(nuevo_numero)
#print(vector_numeros)

for index, i in enumerate(vector_numeros):
    print(f"Posición {str(index) + ':':<3} - número: {i:<3} - cuadrado: {i**2:<3} - cubo: {i**3:<3}")