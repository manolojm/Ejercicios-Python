# 6_Cadenas

cadena1 = input("Introduzca una cadena: ")
cadena2 = ""

for i in range(len(cadena1), 0, -1):
    cadena2 += cadena1[i-1]
    
print(cadena2)