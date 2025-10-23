# 8_Listas
import random
vector_numeros = []
vector_pares = []
vector_impares = []

for i in range(20):
    nuevo_numero = (random.randint(0, 100))
    vector_numeros.append(nuevo_numero)
    if nuevo_numero % 2 == 0:
        vector_pares.append(nuevo_numero)
    else:
        vector_impares.append(nuevo_numero)
    
print("El vector de número ha salido: ")
print(vector_numeros)

vector_numeros.clear()
vector_numeros += vector_pares
vector_numeros += vector_impares

print("\nEl vector de número ahora es: ")
print(vector_numeros)