# 9_Cadenas

cadena1 = input("Introduzca una cadena: ")
cadena2 = input("Introduzca una subcadena: ")

# Devuelve la posicion de la primera ocurrencia o -1 si no coinciden
resultado = cadena1.find(cadena2)

# Cualquier resultado distinto a -1 significa que coinciden
if resultado != -1:
    print("La cadena contiene la subcadena")
else:
    print("La cadena NO contiene la subcadena")