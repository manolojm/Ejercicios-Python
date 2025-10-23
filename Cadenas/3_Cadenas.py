# 3_Cadenas

# 3. Realizar un programa que comprueba si una cadena
# leída por teclado comienza por una subcadena introducida
# por teclado.

cadena_1 = input("Introduzca una cadena: ")
cadena_2 = input("Introduzca una subcadena: ")

# Devuelve la posicion de la primera ocurrencia o -1 si no coinciden
resultado = cadena_1.find(cadena_2)

# Cualquier resultado distinto a 0 no nos va a interesar
if resultado == 0:
    print("La cadena empieza por la subcadena")
else:
    print("La cadena NO empieza por la subcadena")
    
# Metodo alternativo
resultado_2 = cadena_1.startswith(cadena_2)

if resultado_2 == True:
    print("La cadena empieza por la subcadena")
else:
    print("La cadena NO empieza por la subcadena")