# 2_Cadenas

cadena1 = input("Introduzca una cadena: ")
cadena2 = input("Introduzca una subcadena: ")

# Devuelve la posicion de la primera ocurrencia o -1 si no coinciden
resultado = cadena1.find(cadena2)

# Cualquier resultado distinto a 0 no nos va a interesar
if resultado == 0:
    print("La cadena empieza por la subcadena")
else:
    print("La cadena NO empieza por la subcadena")