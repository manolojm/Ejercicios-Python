# 10_Listas
import random
import Min_max

vector_numeros = []

for i in range(10):
    nuevo_numero = (random.randint(0, 100))
    vector_numeros.append(nuevo_numero)
    
print(vector_numeros)
    
while True:
    numero = Min_max.leer_numero_entero(mensaje="Introduzca un número entero: ")
    if numero in vector_numeros:
        print("\nHemos encontrado su número.")
        break
    else:
        print("\nIntroduzca otro número: ")
        
lugar = vector_numeros.index(numero)
vector_numeros.remove(numero)
vector_numeros.insert(0, numero)
print(f"\n{vector_numeros}")
    
    
