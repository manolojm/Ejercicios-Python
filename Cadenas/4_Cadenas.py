# 4_Cadenas

# 4. Realizar un programa que dada una cadena de caracteres
# por caracteres, genere otra cadena resultado de invertir
# la primera.

cadena_1 = input("Introduzca una cadena: ")
cadena_2 = ""

for i in range(len(cadena_1), 0, -1):
    cadena_2 += cadena_1[i-1]

# Primera version
print(cadena_2)

# Version simplificada
print(cadena_1[::-1])