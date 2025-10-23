# 2_Listas

vector_cadenas = []

for i in range(5):
    nueva_cadena = input("Introduzca nueva cadenas: ")
    vector_cadenas.append(nueva_cadena)

vector_2 = vector_cadenas.copy()
vector_2.reverse()

print(vector_2)