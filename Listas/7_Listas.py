# 7_Listas
import random
vector_numeros = []

for i in range(100):
    nuevo_numero = (random.randint(0, 20))
    vector_numeros.append(nuevo_numero)
    
print("El vector de número ha salido: ")
print(vector_numeros)


numero_1 = int(input("\nIntroduzca un primer valor: "))
numero_2 = int(input("Introduzca un segundo valor: "))

num_ocurrencias = vector_numeros.count(numero_1)
for i in range(num_ocurrencias):
    lugar = vector_numeros.index(numero_1)
    vector_numeros.remove(numero_1)
    vector_numeros.insert(lugar, str(numero_2))
    
print("\nEl vector de número es ahora: ")
print(vector_numeros)