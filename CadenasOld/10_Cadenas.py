# 10_Cadenas

cadena1 = input("Introduzca una cadena: ")
cadena2 = ""

for i in range(len(cadena1), 0, -1):
    cadena2 += cadena1[i-1]
    
if cadena1 == cadena2:
    print("La cadena es un palindromo")
else:
    print("La cadena NO es un palindromo")