# 5_Listas
import random

matriz = []
vector_tmp = []
suma_filas = []
suma_columnas = []

# Llenamos a 0 el vector suma_filas
for i in range(5):
    suma_filas.append(0)

# Llenamos a 0 el vector suma_columnas
for i in range(5):
    suma_columnas.append(0)

# Llenamos con enteros la matriz
for i in range(5):
    for j in range(5):
        nuevo_numero = (random.randint(1, 9))
        vector_tmp.append(nuevo_numero)
        suma_filas[i] += nuevo_numero
        suma_columnas[j] += nuevo_numero
        
    vector_copia = vector_tmp.copy()
    matriz.append(vector_copia)
    vector_tmp.clear()

# Ver por pantalla los resultados
print("- - - Matriz original - - -")
print("")
for i in range(5):
    print(f"{matriz[i]}")
    
# Suma de cada fila    
print("\nLa suma de cada fila es: ")
for i in range(5):
    print(f"Fila {i}: {suma_filas[i]:<6}", end="")
print("")

# Suma de cada columna
print("\nLa suma de cada columna es: ")
for i in range(5):
    print(f"Colm. {i}: {suma_columnas[i]:<5}", end="")
print("")